#!/usr/bin/env node
/**
 * Bulk-send "image + prompt" pairs to the chatgpt.com web app, opening a
 * brand-new chat for every pair, using your own logged-in browser session
 * (no OpenAI API key). Run login.js once first to create that session.
 *
 * Read scripts/chatgpt_web/README.md before running this at any volume:
 * driving the consumer web UI like a bot is against OpenAI's Terms of
 * Service and can get an account flagged/limited. This script exists
 * because you decided that trade-off is acceptable for your own account;
 * it deliberately paces requests and runs a visible (non-headless) browser
 * to look as close to normal manual use as possible, but that is a
 * mitigation, not a guarantee.
 *
 * Usage:
 *   node send_batch.js --input-dir ../../images --output-dir ../../outputs \
 *     --prompt "Turn this into a watercolor painting"
 *
 *   node send_batch.js --input-dir ../../images --output-dir ../../outputs \
 *     --prompts-csv ../prompts.example.csv
 *
 * Prompt resolution per image (same convention as bulk_generate.py):
 *   1) --prompts-csv row matching the filename
 *   2) sidecar text file next to the image (cat.png -> cat.txt)
 *   3) --prompt fallback
 * An image with none of those is skipped.
 */
const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");
const { parseArgs } = require("./lib/args");

const SUPPORTED_EXTS = new Set([".png", ".webp", ".jpg", ".jpeg"]);

const SELECTORS = {
  composer: ["#prompt-textarea"],
  sendButton: ['button[data-testid="send-button"]', 'button[aria-label="Send prompt"]'],
  stopButton: ['button[data-testid="stop-button"]', 'button[aria-label="Stop generating"]'],
  attachButton: [
    'button[data-testid="composer-plus-btn"]',
    'button[aria-label="Attach files"]',
    'button[aria-label="Add photos and files"]',
  ],
  uploadMenuItem: [
    'div[role="menuitem"]:has-text("Upload from computer")',
    'div[role="menuitem"]:has-text("Add photos & files")',
    'div[role="menuitem"]:has-text("Upload a file")',
  ],
  assistantMessage: ['div[data-message-author-role="assistant"]'],
  newChatLink: ['a[href="/"]', 'button:has-text("New chat")', 'a:has-text("New chat")'],
};

function log(...a) {
  console.log(new Date().toISOString().slice(11, 19), ...a);
}

async function firstVisible(page, selectors) {
  for (const sel of selectors) {
    const loc = page.locator(sel);
    const n = await loc.count();
    for (let i = 0; i < n; i++) {
      const el = loc.nth(i);
      if (await el.isVisible().catch(() => false)) return el;
    }
  }
  return null;
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

function randomDelayMs(minSec, maxSec) {
  return (minSec + Math.random() * (maxSec - minSec)) * 1000;
}

/** Minimal parser for the "filename,prompt" CSV used by bulk_generate.py (quoted 2nd column ok). */
function loadPromptMap(csvPath) {
  const map = {};
  if (!csvPath) return map;
  const text = fs.readFileSync(csvPath, "utf8");
  for (const rawLine of text.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line) continue;
    const m = line.match(/^([^,]+),\s*"?(.*?)"?$/);
    if (!m) continue;
    const [, filename, prompt] = m;
    if (filename.toLowerCase() === "filename") continue;
    map[filename.trim()] = prompt.trim();
  }
  return map;
}

function resolvePrompt(imagePath, defaultPrompt, promptMap) {
  const base = path.basename(imagePath);
  if (promptMap[base]) return promptMap[base];
  const sidecar = imagePath.replace(/\.[^.]+$/, ".txt");
  if (fs.existsSync(sidecar)) {
    const text = fs.readFileSync(sidecar, "utf8").trim();
    if (text) return text;
  }
  return defaultPrompt || null;
}

async function startNewChat(page) {
  await page.goto("https://chatgpt.com/", { waitUntil: "domcontentloaded" });
  // If already on a fresh composer this is a no-op; if a "New chat" control
  // exists (sidebar), clicking it guarantees we're not continuing a thread.
  const newChat = await firstVisible(page, SELECTORS.newChatLink);
  if (newChat) await newChat.click().catch(() => {});
  const composer = await waitForOne(page, SELECTORS.composer, 30000);
  if (!composer) throw new Error("Composer not found — are you logged in? Run login.js first.");
}

async function waitForOne(page, selectors, timeoutMs) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    const el = await firstVisible(page, selectors);
    if (el) return el;
    await sleep(300);
  }
  return null;
}

async function attachImage(page, imagePath) {
  // Many chat UIs keep a hidden <input type="file"> in the DOM at all times;
  // try that first since it skips the OS file-picker entirely.
  let input = page.locator('input[type="file"]').first();
  if ((await input.count()) > 0) {
    await input.setInputFiles(imagePath);
    return;
  }

  const attachBtn = await firstVisible(page, SELECTORS.attachButton);
  if (!attachBtn) {
    throw new Error(
      "Could not find the attach/plus button in the composer. ChatGPT's UI " +
        "may have changed — see README.md 'If selectors break'."
    );
  }
  await attachBtn.click();

  const menuItem = await firstVisible(page, SELECTORS.uploadMenuItem);
  if (menuItem) await menuItem.click();

  input = page.locator('input[type="file"]').first();
  const deadline = Date.now() + 5000;
  while ((await input.count()) === 0 && Date.now() < deadline) {
    await sleep(200);
    input = page.locator('input[type="file"]').first();
  }
  if ((await input.count()) === 0) {
    throw new Error(
      "No file input appeared after opening the attach menu. ChatGPT's UI " +
        "may have changed — see README.md 'If selectors break'."
    );
  }
  await input.setInputFiles(imagePath);
}

async function sendPrompt(page, text) {
  const composer = await waitForOne(page, SELECTORS.composer, 15000);
  if (!composer) throw new Error("Composer textarea not found before sending.");
  await composer.click();
  // Give the UI a beat to finish registering the attached image thumbnail.
  await sleep(1000);
  await composer.fill(""); // just in case
  await page.keyboard.type(text, { delay: 15 });

  const sendBtn = await firstVisible(page, SELECTORS.sendButton);
  if (sendBtn) {
    await sendBtn.click();
  } else {
    await page.keyboard.press("Enter");
  }
}

async function waitForResponseComplete(page, timeoutMs) {
  // The stop-generating button shows up while a reply streams in, then goes
  // away when it's done. Its brief appearance is normal; its absence the
  // whole time usually means the message hasn't started sending yet.
  await waitForOne(page, SELECTORS.stopButton, 8000).catch(() => null);
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    const stopBtn = await firstVisible(page, SELECTORS.stopButton);
    if (!stopBtn) return true;
    await sleep(500);
  }
  return false; // timed out still generating
}

async function extractLastAssistantTurn(page) {
  const turns = page.locator(SELECTORS.assistantMessage[0]);
  const count = await turns.count();
  if (count === 0) return { text: "", imageUrls: [] };
  const last = turns.nth(count - 1);
  const text = await last.innerText().catch(() => "");
  const imgs = last.locator("img");
  const imgCount = await imgs.count();
  const imageUrls = [];
  for (let i = 0; i < imgCount; i++) {
    const img = imgs.nth(i);
    const srcset = await img.getAttribute("srcset").catch(() => null);
    const src = await img.getAttribute("src").catch(() => null);
    let url = src;
    if (srcset) {
      const candidates = srcset.split(",").map((s) => s.trim().split(" ")[0]);
      if (candidates.length) url = candidates[candidates.length - 1];
    }
    if (url && !url.startsWith("data:")) imageUrls.push(url);
  }
  return { text, imageUrls };
}

async function downloadImage(context, url, destPath) {
  const resp = await context.request.get(url);
  if (!resp.ok()) throw new Error(`Download failed (${resp.status()}) for ${url}`);
  fs.writeFileSync(destPath, await resp.body());
}

async function main() {
  const args = parseArgs(process.argv.slice(2), {
    "input-dir": "../../images",
    "output-dir": "../../outputs",
    "profile-dir": "./chatgpt-profile",
    "min-delay": "8",
    "max-delay": "20",
    timeout: "240000",
  });

  const inputDir = path.resolve(args["input-dir"]);
  const outputDir = path.resolve(args["output-dir"]);
  const profileDir = path.resolve(args["profile-dir"]);
  const dryRun = !!args["dry-run"];
  const overwrite = !!args["overwrite"];
  const headless = args["headless"] === "true" || args["headless"] === true;
  const minDelay = parseFloat(args["min-delay"]);
  const maxDelay = parseFloat(args["max-delay"]);
  const timeoutMs = parseInt(args["timeout"], 10);

  if (!fs.existsSync(inputDir)) {
    console.error(`--input-dir ${inputDir} does not exist`);
    process.exit(1);
  }
  fs.mkdirSync(outputDir, { recursive: true });

  const promptMap = loadPromptMap(args["prompts-csv"] ? path.resolve(args["prompts-csv"]) : null);

  const images = fs
    .readdirSync(inputDir)
    .filter((f) => SUPPORTED_EXTS.has(path.extname(f).toLowerCase()))
    .sort()
    .map((f) => path.join(inputDir, f));

  if (images.length === 0) {
    console.error(`No supported images (${[...SUPPORTED_EXTS].join(", ")}) found in ${inputDir}`);
    process.exit(1);
  }

  const jobs = [];
  for (const imagePath of images) {
    const stem = path.parse(imagePath).name;
    const prompt = resolvePrompt(imagePath, args["prompt"], promptMap);
    const responsePath = path.join(outputDir, `${stem}_response.txt`);
    if (!prompt) {
      log(`Skipping ${path.basename(imagePath)}: no prompt (no --prompt, no sidecar .txt, no CSV row)`);
      continue;
    }
    if (fs.existsSync(responsePath) && !overwrite) {
      log(`Skipping ${path.basename(imagePath)}: already processed (${path.basename(responsePath)} exists)`);
      continue;
    }
    jobs.push({ imagePath, stem, prompt, responsePath });
  }

  if (dryRun) {
    for (const j of jobs) log(`[dry-run] ${path.basename(j.imagePath)} | prompt: ${j.prompt}`);
    log(`Done (dry-run). ${jobs.length} job(s) would run.`);
    return;
  }

  if (jobs.length === 0) {
    log("Nothing to do.");
    return;
  }

  if (!fs.existsSync(profileDir)) {
    console.error(
      `Profile dir ${profileDir} doesn't exist yet. Run "node login.js --profile-dir ${args["profile-dir"]}" first.`
    );
    process.exit(1);
  }

  const context = await chromium.launchPersistentContext(profileDir, {
    headless,
    viewport: { width: 1280, height: 900 },
  });
  const page = context.pages()[0] || (await context.newPage());

  let ok = 0,
    failed = 0;

  for (const job of jobs) {
    log(`--- ${path.basename(job.imagePath)} ---`);
    try {
      await startNewChat(page);
      await attachImage(page, job.imagePath);
      await sendPrompt(page, job.prompt);
      const finished = await waitForResponseComplete(page, timeoutMs);
      if (!finished) log("Warning: timed out waiting for the reply to finish; grabbing whatever is there.");

      const { text, imageUrls } = await extractLastAssistantTurn(page);
      fs.writeFileSync(job.responsePath, text || "(no text captured)");

      if (imageUrls.length === 0) {
        log("No image found in the reply (refusal, text-only answer, or selector mismatch) — see the saved response text.");
      }
      for (let i = 0; i < imageUrls.length; i++) {
        const ext = ".png";
        const suffix = imageUrls.length > 1 ? `_${i + 1}` : "";
        const dest = path.join(outputDir, `${job.stem}_chatgpt${suffix}${ext}`);
        await downloadImage(context, imageUrls[i], dest);
        log(`Saved ${path.basename(dest)}`);
      }
      ok++;
    } catch (err) {
      log(`FAILED on ${path.basename(job.imagePath)}: ${err.message}`);
      failed++;
    }

    if (job !== jobs[jobs.length - 1]) {
      const delay = randomDelayMs(minDelay, maxDelay);
      log(`Waiting ${(delay / 1000).toFixed(1)}s before the next one...`);
      await sleep(delay);
    }
  }

  await context.close();
  log(`Done. ${ok} succeeded, ${failed} failed.`);
  process.exit(failed && !ok ? 1 : 0);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
