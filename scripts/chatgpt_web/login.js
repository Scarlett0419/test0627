#!/usr/bin/env node
/**
 * One-time (or occasional) interactive login step.
 *
 * Opens a real, visible Chromium window pointed at chatgpt.com using a
 * persistent profile directory. Log in by hand (including any 2FA/captcha),
 * then come back to this terminal and press Enter. The session (cookies,
 * local storage) is saved to disk under --profile-dir and reused by
 * send_batch.js so you don't have to log in every run.
 *
 * Usage:
 *   node login.js [--profile-dir ./chatgpt-profile]
 */
const { chromium } = require("playwright");
const readline = require("readline");
const path = require("path");
const { parseArgs } = require("./lib/args");

async function main() {
  const args = parseArgs(process.argv.slice(2), {
    "profile-dir": "./chatgpt-profile",
  });
  const profileDir = path.resolve(args["profile-dir"]);

  console.log(`Using profile dir: ${profileDir}`);
  const context = await chromium.launchPersistentContext(profileDir, {
    headless: false,
    viewport: { width: 1280, height: 900 },
  });

  const page = context.pages()[0] || (await context.newPage());
  await page.goto("https://chatgpt.com/", { waitUntil: "domcontentloaded" });

  console.log("\nLog in to ChatGPT in the opened browser window.");
  console.log("Once you can see the chat composer (i.e. you're fully logged in),");
  await new Promise((resolve) => {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    rl.question("press Enter here to save the session and exit... ", () => {
      rl.close();
      resolve();
    });
  });

  await context.close();
  console.log(`Session saved to ${profileDir}. You can now run send_batch.js.`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
