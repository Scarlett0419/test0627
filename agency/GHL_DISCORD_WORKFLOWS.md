# GHL → Discord Notification Workflows

**Purpose:** post pipeline events from GoHighLevel (GHL) into the team's Discord channels automatically, so nobody has to watch the CRM.
**Owner:** Agency owner (builds and maintains). **Setup time:** about 2 hours including tests.
**Related:** `PIPELINE.md` (stages and CRM fields), `SETTER_PAY_PLAN.md` (custom field names), `SETUP_CHECKLIST.md` Phase 4, `DISCORD_ONBOARDING.md` (channel guide).

---

## 1. At a glance

| # | Discord channel | GHL workflow name | Trigger | Embed colour |
|---|---|---|---|---|
| 1 | `#booked-calls` | `DISCORD 1 · Booked call` | Appointment Status = Booked/Confirmed (consultation calendar) | Blue `3447003` (#3498DB) |
| 2a | `#no-shows` | `DISCORD 2a · No-show` | Appointment Status = No-show | Red `15158332` (#E74C3C) |
| 2b | `#no-shows` | `DISCORD 2b · Cancelled` | Appointment Status = Cancelled | Orange `15105570` (#E67E22) |
| 3 | `#demo-requests` | `DISCORD 3 · Demo request` | Form Submitted = "Demo Build Request" | Purple `10181046` (#9B59B6) |
| 4a | `#wins` | `DISCORD 4a · Closed Won` | Pipeline Stage Changed → Closed Won | Green `3066993` (#2ECC71) |
| 4b | `#wins` | `DISCORD 4b · Payment received` | Payment Received | Green `3066993` (#2ECC71) |
| 5a | `#pipeline-alerts` | `DISCORD 5a · Proposal sent` | Pipeline Stage Changed → Proposal Sent | Yellow `15844367` (#F1C40F) |
| 5b | `#pipeline-alerts` | `DISCORD 5b · Contract signed` | Documents & Contracts, status Completed | Teal `1752220` (#1ABC9C) |
| 5c | `#pipeline-alerts` | `DISCORD 5c · Onboarding form in` | Form Submitted = "Client Onboarding" | Grey `9807270` (#95A5A6) |

That makes 9 small workflows for 5 channels. Each workflow does one job, which makes them easier to test and debug than one large branching workflow. Each has exactly **one action**: a **Custom Webhook** that POSTs a Discord embed.

---

## 2. What was verified and what wasn't

Research date: 2026-09-24. The official pages were found through web search. Direct page fetches from help.gohighlevel.com and discord.com were **blocked in the research environment**, so the facts below come from search-engine excerpts of those official pages, not from reading each page in full. Before relying on a detail marked Unverified, check it in your own GHL account.

| Claim | Status | Source |
|---|---|---|
| **Custom Webhook** is a separate workflow action from the standard **Webhook** action. It lets you set the method (GET/POST/PUT/DELETE), headers, query params, auth, Content-Type and a **raw body** with merge fields (tag icon → dynamic value picker) | **Verified** | [Workflow Action – Custom Webhook](https://help.gohighlevel.com/support/solutions/articles/155000003305-workflow-action-custom-webhook), [Custom Webhook LC Premium guide](https://help.gohighlevel.com/support/solutions/articles/48001238167-guide-to-custom-webhook-workflow-action) |
| The standard **Webhook (Outbound)** action sends GHL's own payload (contact fields plus trigger-context objects). You cannot set the body, so Discord would reject it | **Verified** (payload shape). The claim that Discord rejects it is inferred: Discord requires `content`/`embeds`, and GHL's payload has neither | [Workflow Action – Webhook (Outbound)](https://help.gohighlevel.com/support/solutions/articles/155000003299-workflow-action-webhook-outbound-) |
| Custom Webhook is a **Premium action**: 100 free lifetime executions per sub-account once Premium Features are enabled in Agency settings, then **$0.01 per execution**, or a Workflows Pro plan (Starter $10/mo, Growth $25/mo, Scale $50/mo, agency-level, each with its own bundle and overage rate) | **Verified** from HighLevel pages. Prices can change, so check your agency billing page | [Enable & rebill Premium Features](https://help.gohighlevel.com/support/solutions/articles/155000005678-how-to-enable-and-rebill-premium-features-for-workflows), [Workflows Pro plan tiers](https://help.gohighlevel.com/support/solutions/articles/155000003971-workflows-pro-plan-new-pricing-tiers), [Changelog: premium categories](https://ideas.gohighlevel.com/changelog/new-workflow-pricing-categories-premium-features-ai-models) |
| The standard Webhook action is **not** premium or billed | **Unverified**. No page we saw lists it as premium |  |
| Trigger names **Appointment Status** (filters: status Booked/Confirmed/Showed/No-show/Cancelled/Invalid, In Calendar, In Calendar Group, tags, Modified By) and **Customer Booked Appointment** (fires only when the *customer* books through a booking link; no recurring appointments) | **Verified** | [Appointment Status](https://help.gohighlevel.com/support/solutions/articles/155000002619-workflow-trigger-appointment-status), [Customer Booked Appointment](https://help.gohighlevel.com/support/solutions/articles/155000002675-workflow-trigger-customer-booked-appointment) |
| **Form Submitted** trigger with a "Form is" filter | **Verified** | [Form Submitted](https://help.gohighlevel.com/support/solutions/articles/155000002550-workflow-trigger-form-submitted) |
| **Pipeline Stage Changed** (filters: pipeline, stage, assigned user, lead value) and **Opportunity Status Changed** (Moved From/To Status, In Pipeline, Pipeline Stage, Assigned To, Tag, Lead Value) | **Verified** | [Pipeline Stage Changed](https://help.gohighlevel.com/support/solutions/articles/155000002493-workflow-trigger-pipeline-stage-changed), [Opportunity Status Changed](https://help.gohighlevel.com/support/solutions/articles/155000003252-workflow-trigger-opportunity-status-changed) |
| **Payment Received** trigger covers funnels, invoices, calendars, memberships, forms **and manual entries**. A separate **Invoice** trigger has a Paid status | **Verified** | [Payment Received](https://help.gohighlevel.com/support/solutions/articles/155000003534-workflow-trigger-payment-received), [Invoice](https://help.gohighlevel.com/support/solutions/articles/155000002835-workflow-trigger-invoice) |
| **Documents & Contracts** trigger with Status filter (Sent, Viewed, Signed/Accepted, Completed), Template Name and Recipient Type | **Verified** | [Documents & Contracts trigger](https://help.gohighlevel.com/support/solutions/articles/155000001491-workflow-trigger-documents-contracts) |
| Merge-field syntax is `{{object.field}}`, and custom fields are `{{contact.<unique_key>}}` (key shown in Settings → Custom Fields) | **Verified** | [Overview of merge fields](https://help.gohighlevel.com/support/solutions/articles/155000004390-overview-of-merge-fields-custom-variables), [Custom fields](https://help.gohighlevel.com/support/solutions/articles/48001161579-how-to-use-custom-fields) |
| Specific keys: `{{contact.first_name}}`, `{{contact.company_name}}`, `{{contact.phone}}`, `{{opportunity.lead_value}}` | **Likely.** `lead_value` appears on HighLevel's own ideas board. The others are standard contact fields | [ideas board: opportunity.lead_value](https://ideas.gohighlevel.com/opportunities/p/merge-field-opportunitylead-value-should-output-as-a-currency-field-not-plain-te) |
| `{{appointment.start_time}}`, `{{user.name}}`, `{{opportunity.name}}`, `{{custom_values.<key>}}` and any payment-amount or document-name field | **Unverified.** Third-party sources contradict each other (one lists `appointment.start_time`, another says `appointment.start_date_time`). **Insert these with the picker** (tag icon in the Custom Webhook body) and replace the placeholders in this doc with whatever the picker inserts |  |
| Whether GHL **JSON-escapes** merge values inside a Custom Webhook raw body | **Unverified.** No documentation found. **Assume it doesn't** (see §5) |  |
| Discord: `content` ≤ 2000 chars. Embed title ≤ 256, description ≤ 4096, ≤ 25 fields, field name ≤ 256 / value ≤ 1024, all embeds ≤ 6000 chars total, up to 10 embeds per message. `color` is an **integer** (decimal, not `"#hex"`) | **Verified.** The 10-embed and 6000 figures come from Discord's docs and are widely confirmed | [Discord Webhook resource](https://discord.com/developers/docs/resources/webhook), [Discord Embed limits (community)](https://support.discord.com/hc/en-us/community/posts/4411276183959-Embed-limits), [Webhooks guide: color](https://birdie0.github.io/discord-webhooks-guide/structure/embed/color.html) |
| `"allowed_mentions": {"parse": []}` disables @everyone, @here, user and role pings unless you whitelist specific IDs | **Verified** | [Discord Webhook resource](https://discord.com/developers/docs/resources/webhook), [allowed_mentions guide](https://birdie0.github.io/discord-webhooks-guide/structure/allowed_mentions.html) |
| Rate limits: a 429 response carries `retry_after` | **Verified** | [Discord Rate Limits](https://discord.com/developers/docs/topics/rate-limits) |
| Creating a webhook: Server Settings (or Edit Channel) → Integrations → Webhooks → New Webhook → Copy Webhook URL. Requires *Manage Webhooks* permission | **Verified** | [Discord: Intro to Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) |

**Cost estimate:** 9 workflows × roughly 2–4 bookings per setter per day, plus the other events, comes to a few hundred executions a month. After the 100 free executions, that's about **$3–$8/month** at $0.01 each. Only buy a Workflows Pro tier if other premium actions push volume up.

---

## 3. One-time prerequisites in GHL

1. **Enable Premium Features** (agency view): follow "How to enable and rebill Premium Features for Workflows" (link in §2). Without this step, Custom Webhook either won't appear or won't run. If you can't enable it, use the relay in §9.
2. **Pipeline stages** match `PIPELINE.md` exactly: Cold Lead, Demo Built, Contacted, Meeting Booked, On Call, Proposal Sent, Closed Won, Closed Lost.
3. **Custom fields**: use the names from `SETTER_PAY_PLAN.md` §6. Open Settings → Custom Fields and copy each field's **unique key**. This doc assumes these keys:

   | Field | Assumed key | Type | Note |
   |---|---|---|---|
   | Niche | `contact.niche` | Dropdown | faith / beauty-wellness / fitness / construction-trades / other |
   | Demo Link | `contact.demo_link` | URL / single line | |
   | Setter Assigned | `contact.setter_assigned` | User (per pay plan) | **Check in testing.** If a User-type field posts an ID instead of a name, switch to `{{user.name}}` (the contact's assigned user) or make it a Dropdown of setter names |
   | City | `contact.city` | standard field | |
   | Website | `contact.website` | standard field | current site URL, or "none" |

   If your keys differ, find-and-replace them in the bodies below.
4. **Forms**: create **"Demo Build Request"** (setter-facing) and **"Client Onboarding"** (client-facing, per `PIPELINE.md` Stage 7).
   - **Important for the demo form:** GHL forms create or update the contact that matches the email/phone typed in. Setters must enter the **business's** phone/email, never their own, or the setter's own contact record gets overwritten. Add a hidden or required "Setter" field mapped to Setter Assigned.
5. **Calendar**: one consultation calendar for the owner, for example "Vanguard Consultation". Open its settings and note whether new bookings land as **Confirmed** (auto-confirm on) or **Booked**. Workflow 1 filters on that status.
6. **Workflow settings for every workflow below**: turn **Allow re-entry ON**, because the same contact can book, no-show and rebook. Leave the workflow in **Draft** until its test passes, then **Publish**.

---

## 4. Create the Discord webhooks (one per channel)

Do this five times, once each for `#booked-calls`, `#no-shows`, `#demo-requests`, `#wins` and `#pipeline-alerts`.

1. In Discord (desktop or web; creating webhooks on mobile is limited), hover the channel → **gear icon (Edit Channel)** → **Integrations** → **Webhooks** → **New Webhook**. The same list is also at Server Settings → Integrations → Webhooks. You need the *Manage Webhooks* permission.
2. Name it after its source, e.g. `GHL · booked-calls`. Optionally upload the Vanguard logo as the avatar. Confirm the **Channel** dropdown shows the right channel.
3. Click **Copy Webhook URL**, then **Save Changes**.
4. Paste the URL **straight into GHL** and nowhere else:
   - **Recommended:** Settings → Custom Values → create `Discord · booked-calls` (etc.) and paste the URL as its value. In each Custom Webhook, insert that custom value into the URL field with the tag icon. When you rotate a URL later, you change it in one place.
   - Or paste it directly into the Custom Webhook's URL field.

**Treat each webhook URL as a password.** Anyone who has it can post into the channel as your bot.
- Never commit it to this repo or any file, never paste it in Discord, Slack, email or AI chats, and never put it in a screenshot.
- Only the owner (and any GHL admin with Settings access) should be able to see it.
- **If one leaks:** delete that webhook in Discord (Edit Channel → Integrations → Webhooks → Delete Webhook), which kills the old URL immediately. Create a new one and update the GHL custom value, then re-run that channel's test from §8.

---

## 5. Common Custom Webhook configuration

For every workflow, add the action **Custom Webhook** and set:

| Setting | Value |
|---|---|
| Mode | **CUSTOM**, for full control of method, content type and raw body |
| Method | **POST** |
| URL | the channel's Discord webhook URL, or the custom value that holds it |
| Authorization | None |
| Headers | `Content-Type: application/json` |
| Content-Type | `application/json` |
| Body (raw) | the JSON in the matching section below |

Optional: add `?wait=true` to the end of the URL. Discord then returns the created message (HTTP 200) instead of an empty 204, which makes GHL's execution log easier to read.

### JSON safety: merge fields can break the body

GHL pastes merge-field values into the body as raw text. We found no documentation saying it escapes them for JSON, so assume it doesn't. A value that contains any of the following turns the body into invalid JSON, and Discord answers **400** with no post:
- a **double quote** `"`, e.g. a business name typed as `The "Best" Gym`
- a **backslash** `\`
- a **line break**, e.g. from a multi-line "services" or notes box

Apostrophes (`Joe's Gym`) are safe. Mitigations, in order:
1. **Only put merge fields inside JSON string values.** Never use them as keys, and never unquoted (not even numbers).
2. **Never merge free-text or multi-line fields**, such as setter notes, services or call notes. The bodies below only use short single-line fields. Put a "see GHL" pointer in Discord instead.
3. **Keep data clean at entry.** Tell setters not to type `"` or `\` in business names. Use single-line inputs, dropdowns and URL fields on the forms.
4. **Never put a possibly-empty merge field in a spot Discord requires.** An empty embed field value, or an empty `url`, is rejected by Discord. So the bodies below build the embed **description** from static labels plus merge fields (`**Demo:** {{contact.demo_link}}`), which is never empty. They don't use `fields[]` or `url` with merge values.
5. **Watch the workflow's execution history.** A failed Custom Webhook step shows the error there. §8 includes a deliberate "quote in the name" test so you know how your account behaves.
6. If quotes keep breaking posts, move that workflow to the relay in §9. It builds the JSON with a real encoder, so any value is safe.

`\n` inside the body templates below is a JSON newline escape that Discord renders as a line break. It is part of the template, not a merge value, so it is safe.

---

## 6. The workflows

Paste-ready bodies follow. Replace the `{{...}}` placeholders with the picker's exact version if yours differ (§2). Every body sets `"allowed_mentions": {"parse": []}`, so a business called "@everyone Plumbing" can never ping the server.

### Workflow 1: `#booked-calls` (new appointment booked)

**Trigger:** **Appointment Status**
- Filter *Appointment status* is **Confirmed** if the calendar auto-confirms, otherwise **Booked** (see §3.5). Pick one status only. Selecting both double-posts when a Booked appointment is later confirmed.
- Filter *In Calendar* is **Vanguard Consultation**.

**Why not "Customer Booked Appointment"?** According to HighLevel, that trigger only fires when the *customer* books through the booking link without your team's involvement. Setters often book the owner's calendar themselves during the call, and that booking wouldn't fire it. Appointment Status catches both. Note that a **reschedule** may fire again, so the title says "booked / rescheduled".

**Action:** Custom Webhook (§5), URL = `#booked-calls` webhook.

```json
{
  "username": "Vanguard CRM",
  "allowed_mentions": { "parse": [] },
  "embeds": [
    {
      "title": "Call booked / rescheduled: {{contact.company_name}}",
      "color": 3447003,
      "description": "**Setter:** {{contact.setter_assigned}}\n**Business:** {{contact.company_name}}\n**Owner/contact:** {{contact.first_name}} {{contact.last_name}}\n**Niche:** {{contact.niche}}\n**City:** {{contact.city}}\n**When:** {{appointment.start_time}}\n**Demo:** {{contact.demo_link}}",
      "footer": { "text": "Owner: review the demo + setter notes in GHL before the call" }
    }
  ]
}
```

Add a second action if you like: **Update Opportunity → stage Meeting Booked**. That keeps the pipeline in sync with the calendar. It doesn't post to Discord.

### Workflow 2a: `#no-shows` (no-show)

**Trigger:** **Appointment Status**, filter *Appointment status* is **No-show**, *In Calendar* is **Vanguard Consultation**.
The owner (or whoever runs the call) marks the appointment **No-show** in the calendar as soon as it's clear the prospect isn't coming. That click starts the setter's 2-hour rebook clock.

```json
{
  "username": "Vanguard CRM",
  "allowed_mentions": { "parse": [] },
  "embeds": [
    {
      "title": "NO-SHOW: {{contact.company_name}}. Rebook within 2 hours",
      "color": 15158332,
      "description": "**Setter:** {{contact.setter_assigned}}\n**Business:** {{contact.company_name}}\n**Contact:** {{contact.first_name}} {{contact.last_name}}\n**Phone:** {{contact.phone}}\n**Missed slot:** {{appointment.start_time}}\n**Demo:** {{contact.demo_link}}\n\nRebook text only if SMS consent = Yes, otherwise email. Then call same day (PIPELINE.md, Post-No-Show).",
      "footer": { "text": "React with a check mark when rebooked" }
    }
  ]
}
```

### Workflow 2b: `#no-shows` (cancelled)

**Trigger:** **Appointment Status**, filter *Appointment status* is **Cancelled**, *In Calendar* is **Vanguard Consultation**. You can also set *Modified By* = Customer if internal cancellations (such as the owner moving a slot) shouldn't alert setters.

```json
{
  "username": "Vanguard CRM",
  "allowed_mentions": { "parse": [] },
  "embeds": [
    {
      "title": "CANCELLED: {{contact.company_name}}. Rebook within 2 hours",
      "color": 15105570,
      "description": "**Setter:** {{contact.setter_assigned}}\n**Business:** {{contact.company_name}}\n**Contact:** {{contact.first_name}} {{contact.last_name}}\n**Phone:** {{contact.phone}}\n**Cancelled slot:** {{appointment.start_time}}\n**Demo:** {{contact.demo_link}}\n\nRebook text only if SMS consent = Yes, otherwise email.",
      "footer": { "text": "React with a check mark when rebooked" }
    }
  ]
}
```

**Optional setter ping.** To ping a role such as `@Setters` in `#no-shows`, add `"content": "<@&ROLE_ID>"` and change mentions to `"allowed_mentions": { "parse": [], "roles": ["ROLE_ID"] }`. With `parse` still empty, only that one role can be pinged. Get ROLE_ID from Discord with Developer Mode on → right-click role → Copy Role ID.

### Workflow 3: `#demo-requests` (setter requests a demo build)

**Trigger:** **Form Submitted**, filter *Form is* **Demo Build Request**.
**Form fields**, mapped to contact fields: Business name → Company Name, Owner first name, Business phone, Business email (optional), Niche, City, Current website, Setter. For verified facts (Google rating, years in business), use a single-line field and keep them out of the Discord body. The builder reads them in GHL.

```json
{
  "username": "Vanguard CRM",
  "allowed_mentions": { "parse": [] },
  "embeds": [
    {
      "title": "Demo requested: {{contact.company_name}}",
      "color": 10181046,
      "description": "**Requested by:** {{contact.setter_assigned}}\n**Business:** {{contact.company_name}}\n**Niche:** {{contact.niche}}\n**City:** {{contact.city}}\n**Current site:** {{contact.website}}\n**Phone:** {{contact.phone}}\n\nBuild with scripts/generate_demo.py (verified facts only), deploy, paste the link into Demo Link, then move the opportunity to Demo Built.",
      "footer": { "text": "Builder: react with a check mark when the demo is live" }
    }
  ]
}
```

### Workflow 4a: `#wins` (opportunity moved to Closed Won)

**Trigger:** **Pipeline Stage Changed**, *In Pipeline* = Vanguard Sales, *Pipeline Stage* = **Closed Won**.
Alternative: **Opportunity Status Changed** with *Moved To Status* = Won. Use **one or the other**, not both, or every win posts twice. The stage trigger is recommended because the team works by stage.

```json
{
  "username": "Vanguard CRM",
  "allowed_mentions": { "parse": [] },
  "embeds": [
    {
      "title": "CLOSED WON: {{contact.company_name}}",
      "color": 3066993,
      "description": "**Business:** {{contact.company_name}}\n**Niche:** {{contact.niche}}\n**Set by:** {{contact.setter_assigned}}\n**Deal value:** ${{opportunity.lead_value}}\n\nNext: onboarding form goes out today (PIPELINE.md Stage 7).",
      "footer": { "text": "Vanguard · Closed Won" }
    }
  ]
}
```

### Workflow 4b: `#wins` (payment received)

**Trigger:** **Payment Received**. Optionally filter to your project products (not the Care Plan) if those filters appear on your plan; we couldn't verify the filter list. Payment Received also covers manually recorded payments. If you bill only through GHL invoices, you can use the **Invoice** trigger with status **Paid** instead.

The payment-amount merge field name is **unverified**. Open the picker inside this Custom Webhook while it sits under the Payment Received trigger, insert the amount field, and swap it for `{{PAYMENT_AMOUNT_FROM_PICKER}}` below. Until you do, the literal placeholder text will show in Discord, which is harmless but ugly.

```json
{
  "username": "Vanguard CRM",
  "allowed_mentions": { "parse": [] },
  "embeds": [
    {
      "title": "Payment received: {{contact.company_name}}",
      "color": 3066993,
      "description": "**Business:** {{contact.company_name}}\n**Amount:** {{PAYMENT_AMOUNT_FROM_PICKER}}\n**Set by:** {{contact.setter_assigned}}\n\nIf this is a project payment, move the opportunity to Closed Won (if it isn't already) and log Payment Collected.",
      "footer": { "text": "Vanguard · Payments" }
    }
  ]
}
```

A deal usually triggers both 4a and 4b, so `#wins` gets two posts: "Closed Won" and "Payment received". That's intended, since one is the verbal or signed win and the other is the cash.

### Workflow 5a: `#pipeline-alerts` (moved to Proposal Sent)

**Trigger:** **Pipeline Stage Changed**, *In Pipeline* = Vanguard Sales, *Pipeline Stage* = **Proposal Sent**.

```json
{
  "username": "Vanguard CRM",
  "allowed_mentions": { "parse": [] },
  "embeds": [
    {
      "title": "Proposal sent: {{contact.company_name}}",
      "color": 15844367,
      "description": "**Business:** {{contact.company_name}}\n**Niche:** {{contact.niche}}\n**Set by:** {{contact.setter_assigned}}\n**Value:** ${{opportunity.lead_value}}\n\nFollow-up clock: call Day 3, email/text Day 7, final Day 12 (PIPELINE.md, Owner Follow-Up).",
      "footer": { "text": "Vanguard · Proposal Sent" }
    }
  ]
}
```

### Workflow 5b: `#pipeline-alerts` (proposal/contract signed)

**Trigger:** **Documents & Contracts**, *Status* = **Completed** (every signer done). Set *Template Name* = your proposal/contract template.
Use Completed rather than Signed/Accepted so that documents with several signers (you plus the client) post once, not once per signature. Test this: if your template has only the client as signer, Signed/Accepted and Completed may both fire.

The document-name merge field is unverified, so the template name goes in as static text.

```json
{
  "username": "Vanguard CRM",
  "allowed_mentions": { "parse": [] },
  "embeds": [
    {
      "title": "Contract signed: {{contact.company_name}}",
      "color": 1752220,
      "description": "**Business:** {{contact.company_name}}\n**Signed by:** {{contact.first_name}} {{contact.last_name}}\n**Document:** Vanguard Website Agreement\n\nCheck the payment went through. If paid, move to Closed Won.",
      "footer": { "text": "Vanguard · Documents & Contracts" }
    }
  ]
}
```

### Workflow 5c: `#pipeline-alerts` (onboarding form submitted)

**Trigger:** **Form Submitted**, *Form is* **Client Onboarding**.
Onboarding answers (brand notes, logins) are long and sensitive. **Don't** merge them into Discord. The post only says the form arrived.

```json
{
  "username": "Vanguard CRM",
  "allowed_mentions": { "parse": [] },
  "embeds": [
    {
      "title": "Onboarding form received: {{contact.company_name}}",
      "color": 9807270,
      "description": "**Client:** {{contact.company_name}}\n**Submitted by:** {{contact.first_name}} {{contact.last_name}}\n\nAnswers are in GHL (contact record → Form submissions). Kick off delivery.",
      "footer": { "text": "Vanguard · Onboarding" }
    }
  ]
}
```

---

## 7. What each post looks like

Example for Workflow 1 with a test contact:

> **Vanguard CRM** · BOT
> ▌ **Call booked / rescheduled: ZZ Test Bakery** (blue bar)
> ▌ **Setter:** Maya R.
> ▌ **Business:** ZZ Test Bakery
> ▌ **Owner/contact:** Test Owner
> ▌ **Niche:** beauty-wellness
> ▌ **City:** Austin
> ▌ **When:** Thu, Sep 24, 2026 3:30 PM
> ▌ **Demo:** https://zz-test-bakery.netlify.app
> ▌ *Owner: review the demo + setter notes in GHL before the call*

The other posts follow the same pattern with their own colour bar. A line with an empty value (e.g. `**Demo:**` with nothing after it) means that field is blank in GHL. Fix the data, not the workflow.

---

## 8. Test plan

Run this before publishing each workflow. Use one test contact and delete its test data afterwards.

**Test channel:** create a webhook on `#bot-test` (see DISCORD_ONBOARDING.md) and point each workflow's Custom Webhook URL at it while testing. Once the message looks right, swap in the real channel's webhook URL and publish.

**Setup:** create contact **"ZZ Test Owner"**, company **"ZZ Test Bakery"**, with your own phone/email, niche beauty-wellness, city Austin, demo link = any live demo, and Setter Assigned = you. Create an opportunity for it in Vanguard Sales at stage Contacted with value 2300.

| # | How to fire it | Expected in Discord | Pass if |
|---|---|---|---|
| 1 | Book ZZ Test on the **Vanguard Consultation** calendar for tomorrow, first from the GHL calendar (as a setter would), then again through the public booking link | Blue post in `#booked-calls` with every line filled, including the time and a clickable demo link | Both bookings post once each, the time is in the right timezone, and there's no ping |
| 2a | Open that appointment → status **No-show** | Red "NO-SHOW" post in `#no-shows` | Posts within about a minute |
| 2b | Book again → **Cancel** it | Orange "CANCELLED" post in `#no-shows` | Posts once |
| 3 | Open the **Demo Build Request** form's preview link and submit it for "ZZ Test Bakery" | Purple post in `#demo-requests` | Setter name shows as a **name**, not an ID (see §3.3) |
| 4a | Drag the test opportunity to **Closed Won** | Green "CLOSED WON" post with `$2300` | Posts once. If you also built the Opportunity Status trigger, delete one of them |
| 4b | On ZZ Test, create a $1 invoice → **Record payment** manually (or pay with a Stripe test card), then void/refund it | Green "Payment received" post with the amount | The amount shows real numbers, not `{{...}}` |
| 5a | Drag the opportunity to **Proposal Sent** | Yellow post in `#pipeline-alerts` | Posts once |
| 5b | Send the proposal template to your own email and sign it | Teal "Contract signed" post | Exactly **one** post per document |
| 5c | Submit the **Client Onboarding** form preview as ZZ Test | Grey "Onboarding form received" post | No answers are leaked into Discord |
| Safety | Rename the company to `ZZ "Quote" Bakery` and repeat test 5a | Either a normal post, meaning GHL escapes quotes, or **no post** and a 400 error in the workflow's execution history, meaning it doesn't | Write down which. If no post, enforce the §5 data rule or move to the relay |
| Mentions | Rename the company to `@everyone Test` and repeat 5a | The text shows literally | **Nobody gets a notification** |

If a post doesn't appear, open the workflow → **Execution Logs / Enhanced History** → the Custom Webhook step:
- **400**: invalid JSON (see §5) or an empty required field.
- **401/404**: the webhook was deleted or the URL is wrong.
- **429**: rate limited. This is rare at this volume; the step can be retried.
- For deep debugging, point the URL temporarily at a webhook.site address to see exactly what GHL sends. HighLevel documents this approach in [How to use webhook.site to troubleshoot](https://help.gohighlevel.com/support/solutions/articles/48001212085-how-to-use-webhook-site-to-troubleshoot-your-api-requests). Switch it back afterwards; don't leave contact data on third-party sites.

GHL may also offer a "test workflow" option in the builder. Trigger-specific values (appointment, opportunity, payment) can come through blank in that mode, so the real-event tests above are the ones that count.

When all tests pass, delete the ZZ Test contact, opportunity, invoice and appointments, and tick the Phase 4 items in `SETUP_CHECKLIST.md`.

---

## 9. Fallback: no Custom Webhook on your plan

If Premium Features can't be enabled, use GHL's **standard Webhook** action (not premium, as far as we could find) and send it through a small relay. The relay reshapes GHL's payload into a Discord embed. It also solves the quote-escaping problem, because the relay builds the JSON itself.

### Option A: tiny relay (written, in this repo)

`scripts/ghl_discord_relay/relay.py` uses only the Python standard library and has no dependencies. It was tested locally against a mock Discord endpoint.
- **Secrets come only from environment variables:** `RELAY_TOKEN`, plus `DISCORD_WEBHOOK_BOOKED_CALLS`, `DISCORD_WEBHOOK_NO_SHOWS`, `DISCORD_WEBHOOK_DEMO_REQUESTS`, `DISCORD_WEBHOOK_WINS` and `DISCORD_WEBHOOK_PIPELINE_ALERTS`. Set them in your host's secret settings, never in a committed file.
- **Endpoints:** `POST /<channel>?token=<RELAY_TOKEN>`, where `<channel>` is `booked-calls`, `no-shows`, `demo-requests`, `wins` or `pipeline-alerts`. A wrong token returns 401. The token is never logged.
- **Building the post:** in the GHL standard Webhook action, add **Custom Data** key/value pairs:
  - `title` becomes the embed title, e.g. `Call booked: {{contact.company_name}}`.
  - `color` is optional, e.g. `3447003`. Each channel has a default colour.
  - Every other key becomes an embed field, in order, e.g. `Setter` = `{{contact.setter_assigned}}`, `Demo` = `{{contact.demo_link}}`.
  - Empty values are skipped, text is clipped to Discord's limits, `allowed_mentions` is always `{"parse": []}`, and a 429 is retried once.
  - If no Custom Data arrives, the relay falls back to the business name, contact name, phone and email from GHL's standard payload.
- **Unverified:** we assume GHL nests Custom Data under a `customData` key in the payload. The relay also accepts `custom_data`. Check once with webhook.site. If the key differs, change the lookup at the top of `build_message()`.
- **Hosting:** any small always-on host that runs Python 3.9+ and gives you HTTPS, such as a Render/Railway/Fly.io web service, Google Cloud Run, or a $5 VPS behind Caddy. Run `python3 relay.py`; it listens on `$PORT`, default 8080. Put the relay URL, including `?token=`, only in GHL, and treat it as a secret like the Discord URLs.

### Option B: n8n (if you already run it)

1. **Webhook** node (POST) at path `ghl/:channel`, with Header Auth credential `X-Relay-Token`. GHL's standard Webhook action may not support custom headers, so a `token` query parameter checked in an IF node is fine too.
2. **Switch** on `{{$json.params.channel}}`, one output per Discord channel.
3. **HTTP Request** node per output: POST, *Send Body* = JSON, *Specify Body* = Using JSON with an expression that builds the object from `$json.body.customData`. The fields and `allowed_mentions` work the same as in the relay above. Let n8n serialise the object; don't hand-build JSON strings with quotes.
4. Store the Discord URLs as n8n credentials or environment variables, never as plain text in the node, so exported workflow JSON doesn't leak them.

---

## 10. Maintenance

- **Monthly:** glance at each workflow's execution history for failed steps, and check premium execution spend in agency billing.
- **When a field key changes** (e.g. you rename Demo Link), update every body that uses it. Search this doc for the old key.
- **New setter:** nothing to change. Posts use the contact's Setter Assigned value.
- **Setter leaves:** they lose Discord access. The webhooks don't need to be rotated unless they had GHL Settings access or copied a URL.
- **Leaked URL:** delete the webhook in Discord, create a new one, update the GHL custom value, then re-run that channel's test (§4).
