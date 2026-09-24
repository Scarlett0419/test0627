# Vanguard — Discord Server Setup & Setter Onboarding

How the Vanguard Discord is laid out, who can do what in it, and how a new setter goes from day 1 to certified.

**How this fits with the other docs:**

| Doc | What it's for |
|---|---|
| `PIPELINE.md` | Stages, CRM fields, follow-up cadence, targets |
| `SETTER_SCRIPT.md` | Openers, objection handlers, voicemail, email/text/DM templates, setter rules |
| `DEMO_PLAYBOOK.md` | When and how demos get built, hosted, and used on calls. Includes what never goes in a demo |
| `CLOSER_SCRIPT.md` | What the owner does on the booked call (setters read it so they know what they're booking into) |
| `OFFER.md` | What we sell. Setters never quote price |
| `SETTER_PAY_PLAN.md` | Setter pay, commissions, and how certification affects pay. **Not repeated here** |
| `GHL_DISCORD_WORKFLOWS.md` | The GoHighLevel → Discord automations that feed the bot channels. **Not repeated here** |
| `SETUP_CHECKLIST.md` | The full go-live checklist. This doc covers Phase 4, "Run Discord onboarding" |

**Stack:** GoHighLevel (GHL) is the CRM, dialer, and calendar. Discord is where the team talks and where GHL events show up. **GHL is the source of truth.** If something is in Discord but not in GHL, it didn't happen.

---

## 1. Server Structure

The server already exists. Set it up with the categories below. Set permissions **on the category** and keep each channel synced to its category unless a channel's row says otherwise.

**Legend:** O = Owner · SC = Setter (certified) · ST = Setter (trainee) · DB = Demo Builder · "threads" = can reply only in threads on existing posts

### WELCOME

| Channel | Purpose | Who can post | Who can see |
|---|---|---|---|
| `#start-here` | Rules, first steps, and where everything lives (pinned template in §6) | O | Everyone, including members with no role yet |
| `#announcements` | Process changes, doc updates, schedule changes, certifications | O | All roles |
| `#scripts-and-docs` | Pinned index of the current docs and links (pinned template in §6). Questions about the docs go in `#questions` | O | All roles |

### SALES FLOOR

| Channel | Purpose | Who can post | Who can see |
|---|---|---|---|
| `#general` | Team chat that isn't about a specific lead | All roles | All roles |
| `#daily-checkins` | Start-of-day and end-of-day posts (templates in §4) | O, SC, ST | O, SC, ST |
| `#hot-leads` | A lead that needs the owner's eyes today (template in §7) | O, SC, ST | O, SC, ST |
| `#questions` | Questions about scripts, GHL, or process. Search before you ask | All roles | All roles |
| `#call-reviews` | One post per call: a GHL recording link plus what you want feedback on. Feedback goes in the post's thread | O, SC, ST | O, SC, ST |
| `#leaderboard` | Weekly rankings, taken from GHL | O (reactions only for everyone else) | O, SC, ST |

### PIPELINE FEED (bot-fed, read-only for humans)

GHL webhooks post into these channels. **Humans do not post top-level messages here.** To say something about a bot post, open a thread on that post. The wiring for each channel is in `GHL_DISCORD_WORKFLOWS.md`.

| Channel | Fed by | What humans do here | Who can see |
|---|---|---|---|
| `#booked-calls` | New appointment booked | The booking setter confirms in the thread that the lead brief is complete in GHL | O, SC, ST |
| `#no-shows` | Appointment no-show or cancelled | The booking setter replies in the thread with the rebook plan, then the outcome (the rebook starts within 2 hours, per `PIPELINE.md`) | O, SC, ST |
| `#demo-requests` | Setter requests a demo build for a lead (see §5) | The builder claims the request and posts the demo link in the thread. The setter confirms they tested it | O, SC, ST, DB |
| `#wins` | Deal closed / deposit paid | Congratulations go in the thread | All roles |
| `#pipeline-alerts` | Proposal signed or viewed, onboarding form submitted, other stage changes | The owner acts. Setters can read along | O, SC |

### TRAINING

| Channel | Purpose | Who can post | Who can see |
|---|---|---|---|
| `#training` | Week-1 tasks, checklist progress, roleplay scheduling, quiz answers | O, SC, ST | O, SC, ST |

### DEMO BUILD

| Channel | Purpose | Who can post | Who can see |
|---|---|---|---|
| `#demo-builds` | Builder work notes, spot-check requests, and demo QA fixes. Nothing that belongs to a specific request (that goes in its `#demo-requests` thread) | O, DB | O, DB |

### VOICE

| Channel | Purpose | Who can join |
|---|---|---|
| `Power Hour` | Dialing together. Stay muted unless you're talking to the room. The owner drops in to listen | O, SC, ST |
| `Roleplay Room` | Script roleplays and weekly call review | O, SC, ST |
| `Owner Office` | 1:1s. Locked; the owner moves people in | O (others by invite/move) |

### OWNER ONLY

| Channel | Purpose | Who can post / see |
|---|---|---|
| `#owner-log` | Owner notes, AutoMod flags, compliance incidents, certification sign-offs | O |
| `#bot-test` | Test posts while building or changing GHL workflows. If `GHL_DISCORD_WORKFLOWS.md` names a different test channel, use that one | O |
| `#1on1-<setter-name>` | One private channel per setter, visible only to the owner and that setter. Used for pay questions (see `SETTER_PAY_PLAN.md`), coaching notes, and certification feedback | O + that setter |

---

## 2. Roles & Permissions

### Roles (top to bottom in Server Settings → Roles)

| Role | Who | Can see | Can post |
|---|---|---|---|
| **Owner** | You | Everything | Everything. **The only role with** Administrator, Manage Server, Manage Roles, Manage Channels, **Manage Webhooks**, and Create Invite |
| **Demo Builder** (optional) | Whoever builds demos, if that isn't the owner | WELCOME, `#general`, `#questions`, `#demo-requests`, `#wins`, `#demo-builds` | `#general`, `#questions`, `#demo-builds`; threads in `#demo-requests` and `#wins` |
| **Setter (certified)** | Setters who passed the §3 checklist | Everything except DEMO BUILD and OWNER ONLY (plus their own `#1on1-` channel) | Human channels in SALES FLOOR and TRAINING; threads in the feed channels |
| **Setter (trainee)** | New setters, week 1 until certified | Same as certified, **minus `#pipeline-alerts`** | Same as certified. Trainees dial only in supervised blocks (§3) |
| `@everyone` (no role) | Anyone who just joined | `#start-here` only | Nothing |

### Permission setup, step by step

1. **`@everyone` at server level:** turn off View Channels. Then allow View Channels on `#start-here` only. Anyone the owner hasn't given a role sees one channel.
2. **Each category:** allow View Channels (and Send Messages where the §1 tables say so) for the roles listed. Sync the channels to their category.
3. **PIPELINE FEED category**, for Setter (certified), Setter (trainee), and Demo Builder:
   - **Deny:** Send Messages, Create Private Threads, Mention @everyone/@here/All Roles, Attach Files
   - **Allow:** View Channels, Read Message History, Add Reactions, Create Public Threads, Send Messages in Threads
   - Webhooks still post even with Send Messages denied. That's intended.
4. **`#announcements`, `#scripts-and-docs`, `#leaderboard`, `#start-here`:** deny Send Messages to everyone except the Owner. Allow Add Reactions.
5. **Server-wide for non-owner roles:** deny Mention @everyone/@here/All Roles, Manage Webhooks, Manage Messages, and Create Invite. On the **Owner** role, turn on "Allow anyone to @mention this role" so that `@Owner` works for escalations (§7).
6. **Security settings:**
   - Server Settings → Safety Setup: verification level **Medium or higher**, and **require 2FA** for moderator actions
   - Default notifications: **Only @mentions**
   - Invites: only the owner creates them, **single-use, expiring in 24 hours**
   - Optional: an AutoMod regex rule on `#general`, `#questions`, and `#hot-leads` that flags phone-number and email patterns into `#owner-log` (see §7 on personal data)

### Webhook URLs are secrets

- A Discord webhook URL lets **anyone who has it** post into that channel as the bot. Treat it like a password.
- **Only the Owner creates webhooks** (Channel → Edit → Integrations → Webhooks). Name them clearly, e.g. `GHL – Booked Calls`.
- Copy the URL **straight into the GHL workflow** and keep a copy only in the owner's password manager. The GHL side is in `GHL_DISCORD_WORKFLOWS.md`.
- **Never** paste a webhook URL into any Discord channel (including owner-only ones), a DM, an email, a screenshot, a doc, or a git commit. The repo's docs refer to webhooks **by channel name only**.
- **If a URL leaks** (someone sees it, it gets committed, or strange posts appear): delete that webhook in Integrations right away, create a new one, update the GHL workflow, and note the incident in `#owner-log` **without** the URL.

### Offboarding a setter (same day they leave)

Remove their roles and kick them from the server. Deactivate their GHL user. Archive their `#1on1-` channel. Reassign their open leads and booked calls in GHL. Any final pay goes through `SETTER_PAY_PLAN.md`.

---

## 3. Setter Onboarding — Week 1

**Before Day 1 (owner):**
- [ ] Contractor agreement signed, including the DNC/TCPA compliance clause (`SETUP_CHECKLIST.md` Phase 4)
- [ ] Pay plan walked through and acknowledged (`SETTER_PAY_PLAN.md`)
- [ ] GHL user created with setter permissions, a dialer number assigned, and their GHL booking link working
- [ ] Discord invite sent (single-use); the **Setter (trainee)** role and a `#1on1-<name>` channel ready
- [ ] Calling/texting sign-off from the lawyer and A2P 10DLC registration done (`SETUP_CHECKLIST.md` Phases 0 and 2). **Texting stays off until A2P is approved**, even with consent

### Day 1 — Setup + read the docs

| Task | Done when |
|---|---|
| Join Discord, turn on 2FA, set your nickname to `First L. — Setter` | The owner assigns the trainee role |
| Read `#start-here` and the `#scripts-and-docs` pin | You react with a check mark on both pins |
| Read `PIPELINE.md` in full (stages, CRM fields, follow-up cadence, targets) | — |
| Read `SETTER_SCRIPT.md` in full. Say every line out loud twice | — |
| Read `DEMO_PLAYBOOK.md` §1, §2, §4, §6 | — |
| Skim `CLOSER_SCRIPT.md` and `OFFER.md`, so you know what happens after you book. **You never quote price** | — |
| Log into GHL: find the pipeline, a contact record, the calendar, the dialer, and the DND (do-not-call) setting | You show the owner each one on a screen share |
| Post in `#training`: "3 things I'm clear on, 3 things I'm not" | The owner answers in a thread |

### Day 2 — Compliance training (nothing else happens until this is passed)

The owner runs this live in `Roleplay Room` (about 45 min), then gives a written quiz in `#1on1-<name>`. **The pass mark is 100%.** Retakes are allowed.

| Rule | What it means in practice |
|---|---|
| **No texts without verbal consent** | Only text someone who said yes to a text on a live call. Log it in GHL: "SMS consent: yes, [date/time], verbal". No yes means email. Every text identifies Vanguard and includes "Reply STOP to opt out". A STOP is honored immediately. (`SETTER_SCRIPT.md`, Follow-Up Templates) |
| **DNC scrub before the dial** | Every number is scrubbed against the National Do Not Call Registry, with the scrub date logged in GHL, before it enters the dial queue. No scrub date means no dial. |
| **Internal do-not-call list** | Anyone who says "don't call me" / "take me off your list" gets the GHL DND flag **that day**, before your next dial. No exceptions (Setter Rule 8). Tell the owner in your `#1on1-` channel if they were upset or mentioned legal action. |
| **Calling hours: 8am–9pm in the prospect's time zone** | Check the prospect's time zone, not yours. If a state rule on the owner's list is stricter, the stricter rule wins. |
| **The hook must be true** | Only say "we already built you a demo" if the demo link is live and you tested it on your phone. No demo means you don't dial that lead with the demo hook. |
| **Nothing invented** | No made-up reviews, stats, client counts, urgency, or scarcity. Facts on demos are verified and sourced (§5). |
| **Call recording** | Recording is only on where it's legal (one-party-consent states; `SETUP_CHECKLIST.md` Phase 1). Never record outside GHL. Never download or share recording files; share the GHL link. |
| **Personal data** | Rules in §7. Short version: post the GHL link, not the person's details. |

### Day 3 — Roleplay + shadowing

- **Roleplay with the owner (60 min, `Roleplay Room`):**
  - Both openers (has a site / no site)
  - All six objection handlers
  - The booking close, including the "Is this a cell I can text?" consent question
  - The voicemail (under 25 seconds)
  - The owner plays rude, busy, curious, and gatekeeper prospects
  - Repeat until each piece is smooth
- **Shadow recorded calls:** listen to at least 5 calls the owner picks from `#call-reviews` (good ones and bad ones). For each, reply in its thread with: what the gap callout was, when the demo hook landed, which objection came up and how it was handled, and whether the booking close asked for text consent.
- **First demo requests:** research and submit **3 real demo requests** (§5 template) for DNC-clean, qualified leads. The owner reviews the facts and sources in the thread. These leads become your Day 4 dial list, since you can't dial a lead until its demo is live.

### Day 4 — First supervised dials

- **The block:** 60–90 min in `Power Hour`, with the owner present (listening in through GHL if the dialer supports it, otherwise reviewing the recordings the same day)
- **Who you can dial:** only leads with a live, tested demo and a logged DNC scrub date, and only within calling hours
- **Target:** 20–30 dials. The goal is **clean** calls: a correct compliance check before every dial and every touchpoint logged in GHL the same day
- **After the block:** a 15-min debrief in `Roleplay Room`, then your first EOD post (§4)
- **Stopping rule:** the owner stops the session immediately for any compliance miss. You fix it, roleplay it, then resume

### Day 5 — Second supervised block + first call review

- **Two supervised blocks:** 40–60 dials total
- **Call reviews:** post 2 calls to `#call-reviews` (§4 format): your best one and your roughest one
- **Follow-ups:** send the voicemail follow-up emails for every no-answer from Days 4–5, per the `PIPELINE.md` cadence
- **Checklist review:** go through the certification checklist below with the owner in `Owner Office`. Most setters finish it in week 2. That's normal.

### Certification checklist (Trainee → Certified)

The owner signs off each item in `#1on1-<name>`. When all are checked, the owner switches the role, posts in `#announcements`, and logs the sign-off in `#owner-log`. For what changes in pay, see `SETTER_PAY_PLAN.md`.

- [ ] Compliance quiz passed at 100%
- [ ] Roleplay passed on the owner's scorecard:
  - opener under 30 seconds, with a specific gap callout
  - demo framed as already built
  - handles at least 4 of the 6 objections without reading
  - booking close asks for text consent
  - no pricing talk
  - voicemail under 25 seconds
- [ ] 5+ shadowed calls broken down in `#call-reviews`
- [ ] 3+ demo requests approved on the first pass (all facts sourced, nothing guessed)
- [ ] 100+ supervised dials with **zero** compliance misses (hours, DNC, texting, internal DNC flags)
- [ ] Every touchpoint logged in GHL the same day, for 3 days in a row (the owner spot-checks)
- [ ] Start-of-day and EOD posts made for 3+ days in a row
- [ ] At least 1 meeting booked, with the lead brief complete in GHL and the confirmation sent through the correct channel (text only with consent)
- [ ] Handled at least 1 no-show or callback correctly (thread reply in `#no-shows`, rebook attempt logged)

**Losing certification:** a serious compliance miss (texting without consent, dialing a DNC or internal-DNC number, calling outside hours, lying about a demo) moves a certified setter back to trainee until they re-pass the quiz and a supervised block.

---

## 4. Daily & Weekly Rhythm

Targets come from `PIPELINE.md`: **50–80 dials, 10–20 connects, 2–4 booked per day.** Trainees aren't held to them in week 1.

### Start of day (in `#daily-checkins`, before your first dial)

```
SOD — [Name] — [Date]
Dial block(s): [e.g. 9:30–11:30, 1:00–3:00 — in MY time zone]
Markets calling today: [cities / time zones]
Demo-ready leads in queue: [#]  (live demo + DNC scrub date logged)
Callbacks / rebooks due today: [#]
Today's goal: [dials] dials / [booked] booked
Working on: [one skill, e.g. "shorter opener" or "busy objection"]
```

### End of day (in `#daily-checkins`, same day, from your GHL numbers)

```
EOD — [Name] — [Date]
Dials: [#]
Connects (live decision-maker conversations): [#]
Booked: [#]
Demos requested: [#]
No-shows rebooked: [#] of [#]
Added to internal DNC: [#]
Callbacks set for tomorrow: [#]
All touchpoints logged in GHL: yes / no (if no, why and when)
Win: [one line]
Stuck on: [one line, or "nothing"]
```

The owner replies in a thread when something needs attention. Don't post raw dial logs or contact lists.

### Weekly

| When | What | Where |
|---|---|---|
| **Monday** | Weekly review, per `PIPELINE.md`. Setters review their dial volume and booking rate; the owner reviews show rate and close rate. The owner posts the leaderboard | `#leaderboard`, `Roleplay Room` |
| **By Wednesday EOD** | Each setter posts 2 calls to `#call-reviews` (their best one and their roughest one) | `#call-reviews` |
| **Thursday** | Weekly call review (45 min). Play 2–3 calls, the room gives feedback, one roleplay per setter on the weak spot | `Roleplay Room` |
| **Friday** | The owner posts any script or doc changes for next week | `#announcements` |

**`#call-reviews` post format** (the recording stays in GHL; post the link only):

```
CALL REVIEW — [Setter] — [Date]
GHL call link: [link]
Business / niche / city: [Business Name] / [niche] / [city]
Outcome: booked / not booked / callback / DNC request
Why I'm posting it: [best call / roughest call / weird objection]
Feedback I want: [e.g. "how to handle 'we already have a guy'"]
Timestamp to jump to: [mm:ss]
```

**`#leaderboard`** (the owner posts it every Monday, from GHL reports, not from what people self-report):

```
LEADERBOARD — Week of [date]
Ranked by meetings that SHOWED (booked meetings that were no-shows don't count)
1. [Name] — Showed [#] | Booked [#] | Connect→Book [%] | Dials [#]
2. ...
Team: Show rate [%] | Rebook rate [%] | Demo→meeting [%]
Shout-out: [specific call or habit worth copying]
```

We rank by meetings that showed, not by dials, so there's no reason to game volume. Any compliance miss that week removes the setter from the board. For bonuses or pay tied to these numbers, see `SETTER_PAY_PLAN.md`.

---

## 5. Requesting a Demo (`#demo-requests`)

A demo has to exist **before the first dial** (`PIPELINE.md` Stage 2, `DEMO_PLAYBOOK.md` §1). Only request one for a lead that is **qualified** (weak, outdated, or no site; right niche) and **DNC-clean**.

**How it gets there:** you submit the request from the lead's record in GHL, and the automation posts it to `#demo-requests`. The trigger and field mapping are in `GHL_DISCORD_WORKFLOWS.md`. Anything that didn't fit, like extra source links, goes in a thread on the bot's post. **If the automation is down,** post the same template in `#questions` starting with `[DEMO REQUEST — BOT DOWN]` and @Owner once.

### Demo request template (every field required unless marked optional)

```
DEMO REQUEST
Setter: [Name]
GHL contact: [link]
Business name: [exact trading name, as on their Google Business Profile]
Niche: faith / beauty-wellness / fitness / construction-trades / other: [___]
Services (4–8): [service 1], [service 2], [service 3], [service 4], ...
  Source: [URL of their services page / GBP Services tab / IG highlights / Yelp / Mindbody]
City, State: [city, ST]
Business phone (public, from GBP): [number]
Current site URL: [URL]  — or "none" (only on: GBP / Facebook / IG — link it)
Gap I'll call out on the dial: [one line, e.g. "no online booking", "broken on mobile", "no site"]
Tagline (optional): "[exact text]"  Source: [URL]  — leave blank if none found
Verified facts (only what you can link to; leave blank rather than guess):
  - [fact, e.g. "4.8 stars, 212 Google reviews"] | Source: [URL] | Checked: [date]
  - [fact, e.g. "Serving Austin since 2004"] | Source: [URL] | Checked: [date]
DNC-clean: yes — scrubbed [date], not on internal DNC
Custom build? (optional): no / yes — why this lead is high-value: [one line]
```

**Rules**
- **Facts need a source link, or they stay out.** No guessed numbers, no invented reviews or quotes. Verified facts become the demo's `--highlights` (`DEMO_PLAYBOOK.md` §6).
- **Don't ask for their logo or photos.** Demos use text-only branding and no scraped images.
- **Don't include the owner's personal info.** The decision-maker's name, personal cell, and email stay in GHL. The public business phone is the only number in the request.
- **One request per lead.** Don't bulk-request.

**What happens next**
1. The builder (the owner or the Demo Builder) claims it by opening a thread and saying "on it". Target turnaround: the next business day.
2. The builder posts the live demo link in the thread and adds it to the GHL contact. The owner spot-checks the first demos each week.
3. **You open the link on your phone before dialing** and reply "tested" in the thread. If anything is wrong (a wrong fact, a typo, a broken layout), say so in the thread and don't dial until it's fixed.

---

## 6. Pinned Message Templates

### Pin for `#start-here`

```
WELCOME TO VANGUARD

What we do: we build premium websites for local service businesses (faith orgs,
beauty/wellness, fitness, construction/trades). Setters cold call businesses with
weak or missing websites. Before we dial, we've already built them a demo. The
setter books a 15–30 min call with the owner, and the owner closes and delivers.

Your job as a setter: book qualified calls that actually show up. Honestly and legally.

THE NON-NEGOTIABLES
1. GHL is the source of truth. Log every touchpoint the same day.
2. No texts unless the prospect said yes to a text on the call (logged in GHL).
3. Every number gets a DNC scrub before the dial. "Don't call me" = internal DNC flag the same day.
4. Call only 8am–9pm in the PROSPECT's time zone.
5. Only say "we already built you a demo" if it's live and you've tested it.
6. Never invent facts, reviews, numbers, or urgency.
7. Never paste prospect personal data in Discord. Post the GHL link.
8. Never quote price. "Great question for the call."

FIRST STEPS
1. Turn on Discord 2FA. Set your nickname to "First L. — Setter".
2. Read the pin in #scripts-and-docs and every doc it lists.
3. Say hi in #general. Post your Day 1 "3 clear / 3 unclear" in #training.
4. Questions go in #questions. Urgent things: @Owner (rules for when are in #scripts-and-docs → DISCORD_ONBOARDING §7).

WHERE THINGS LIVE
#daily-checkins: start-of-day and end-of-day posts
#hot-leads: leads that need the owner today
#call-reviews: recordings for feedback (GHL links only)
#booked-calls #no-shows #demo-requests #wins #pipeline-alerts: bot feeds. Reply in threads only.
#1on1-<you>: private with the owner (pay, coaching, certification)

React with a check mark once you've read this.
```

### Pin for `#scripts-and-docs`

```
SCRIPTS & DOCS — current versions (updated [date])

When a doc changes, the owner posts what changed in #announcements and updates this pin.
Only use the linked copies below. Don't use old downloads or screenshots.

READ FIRST (setters)
- SETTER_SCRIPT.md: openers, objections, voicemail, email/text/DM templates, setter rules → [link]
- PIPELINE.md: stages, CRM fields, follow-up cadence, daily targets → [link]
- DEMO_PLAYBOOK.md: read §1, §2, §4, §6 (how demos work and what never goes in one) → [link]
- DISCORD_ONBOARDING.md: this server, week-1 training, templates, escalation → [link]

KNOW WHAT YOU'RE BOOKING INTO
- CLOSER_SCRIPT.md: what the owner does on the call → [link]
- OFFER.md: what we sell (setters never quote price) → [link]

YOUR PAY
- SETTER_PAY_PLAN.md → [link]  (questions go in your #1on1 channel, not here)

HOW THE BOT CHANNELS WORK
- GHL_DISCORD_WORKFLOWS.md → [link]

QUICK TEMPLATES (full versions in DISCORD_ONBOARDING.md)
- Demo request → §5
- SOD / EOD posts → §4
- Call review post → §4
- Hot lead post → §7

GHL LINKS
- Pipeline → [link]   - My calendar / booking link → [link]   - Dialer → [link]
```

---

## 7. Etiquette & Escalation

### When to @Owner

**@Owner right away (during working hours) for:**
- **A hot lead that needs the owner today:** they want to talk now, want a same-day slot, or are ready to buy. Post it in `#hot-leads` (template below) and @Owner in that post.
- **A compliance problem:** a prospect says they're on the DNC list, threatens legal action, asks you to delete their data, or you realize you texted or dialed someone you shouldn't have. Post it in your `#1on1-` channel, not in public channels.
- **A booked call is at risk:** the demo link is broken or has a wrong fact, and the call is within 24 hours.
- **The bot is wrong:** a booking didn't post, something posted to the wrong channel, or a bot post shows personal data it shouldn't.
- **A security issue:** a suspicious invite, a strange bot post, or a possible webhook or GHL login leak.

**Don't @Owner for:** script or process questions (use `#questions`), EOD numbers, or a normal demo request. Those get answered in the normal flow.

**After hours:** only ping for a meeting booked within the next 12 hours that's at risk, or for a compliance or security issue. Everything else waits for the next morning.

### Posting a hot lead (`#hot-leads`)

```
HOT LEAD — [Business Name] ([niche], [city])
GHL contact: [link]
Status: booked for [day, time, THEIR time zone] / wants callback today at [time] / wants owner now
Why hot: [one line, in their words if possible]
Demo: [link] — they've seen it: yes / no
Objections raised: [short list or "none"]
Text consent: yes / no (as logged in GHL)
Need from owner: [the specific ask] by [time]  @Owner
```

The owner replies in the thread. The setter updates the thread with the outcome.

### Personal data: what never goes in Discord

- **OK to post:** business name, niche, city, public business phone and website (demo requests only), the GHL contact link, first name when it's needed for context
- **Never post:**
  - personal cell numbers or personal emails (anything that isn't the listed business phone)
  - home addresses
  - screenshots of GHL contact records
  - call recording files
  - payment details
  - anything personal the prospect shared (health, money trouble, family)
  - lists or exports of leads
- **Posted something by mistake?** Delete it, then tell the owner in your `#1on1-` channel so they can check whether it was copied anywhere.
- Don't share Discord content outside the server, and don't screenshot it for anyone outside the team.

### General etiquette

- **Threads, not top-level replies.** Replies to any post go in its thread, and the bot feeds are threads-only.
- **Keep it professional.** No mocking prospects, even ones who were rude. Assume anything you write could be read back to them.
- **Search before you ask** in `#questions`. If your question is new, the answer may end up in a doc.
- **Celebrate in the `#wins` thread.** A win belongs to the whole team: setter, builder, and owner.
- **Notifications:** keep `#no-shows` and `#hot-leads` on All Messages. Set the other feed channels to @mentions only.
- **Disagree in your `#1on1-` channel, not in public.** Suggest script ideas in `#questions`. The owner decides what changes and announces it.
