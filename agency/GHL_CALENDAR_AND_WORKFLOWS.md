# GHL — Calendar Meeting Link + the 4 Workflows

Click-by-click for the two jobs the API can't do. About 30 minutes in total. Menu names can shift slightly between GHL updates; if a label differs, look for the nearest match.

---

## Part 1 — Meeting link on "Vanguard Consultation" (5–10 min)

### A. Connect Google (gives Google Meet links) or Zoom
- **Google Meet:** Settings → **Calendars** → **Connections** tab → **Add new** → Google → sign in with the Google account you take calls on → allow access.
- **Zoom (instead):** Settings → **Integrations** → **Zoom** → Connect → sign in.

### B. Block your personal time
Still in Settings → Calendars → Connections: set your Google/Outlook calendar as a **conflict calendar** ("Check for conflicts"), so anything already in your diary can't be booked over.

### C. Put the link on the calendar
1. **Calendars** (left menu) → **Calendar Settings** → find **Vanguard Consultation** → **⋮ → Edit**.
2. **Meeting details / Location** → choose **Google Meet** (or **Zoom**). A unique link is created for every booking.
3. Check the times while you're there: Mon–Fri 14:00–21:00 UK, 30-min slots, 15-min buffer. Change if you want.
4. **Notifications** tab: turn **off** GHL's default confirmation/reminder emails and texts for this calendar. The workflows below send them instead, so the owner doesn't get two of everything.
5. **Save.** Copy the calendar's **booking link** (Share / Permanent link). This is the link setters use, instead of Calendly.

**Test:** book yourself a slot from the link with a test email. You should get a Meet/Zoom link in the invite.

---

## Part 2 — The 4 workflows (20–25 min)

All in **Automation → Workflows → + Create Workflow → Start from scratch**. Name each one, build it, then click **Publish** (top right) and **Save**. Unpublished workflows don't run.

Merge fields used below: `{{contact.first_name}}`, `{{contact.company_name}}`, `{{contact.demo_link}}` (our custom field), `{{appointment.only_start_date}}`, `{{appointment.only_start_time}}`, `{{appointment.timezone}}`, `{{appointment.meeting_location}}`, `{{appointment.reschedule_link}}`. Use the **{ }** picker in each message box to insert them so the exact names match your account.

### Workflow 1 — "Booked: confirm + alert"

**Trigger:** *Customer Booked Appointment* → filter **Calendar is Vanguard Consultation**.

**Actions, in order:**
1. **Create/Update Opportunity** → Pipeline **Vanguard Sales** → Stage **Meeting Booked** → Status **Open** (tick "allow backward stage movement" off).
2. **Send Email** to the contact:
   - **Subject:** `Confirmed: your website walkthrough with Vanguard`
   - **Body:**
     > Hi {{contact.first_name}},
     >
     > You're booked in for {{appointment.only_start_date}} at {{appointment.only_start_time}} ({{appointment.timezone}}).
     >
     > Here's the demo we built for {{contact.company_name}} so you can take a look first: {{contact.demo_link}}
     >
     > Join here at the time: {{appointment.meeting_location}}
     > Need a different time? {{appointment.reschedule_link}}
     >
     > Talk soon,
     > [Your name], Vanguard
     > [business address]
3. **If/Else** → condition **Contact Tags includes `sms-consent`**
   - **Yes branch → Send SMS:** `Hi {{contact.first_name}}, it's [Your name] from Vanguard. You're booked for {{appointment.only_start_date}} at {{appointment.only_start_time}} to go through the site we built for {{contact.company_name}}. Reply STOP to opt out.`
   - **No branch:** nothing.
4. **Slack** (Integrations action → Slack → Send message to channel `#bookings`): `New booking: {{contact.company_name}} ({{contact.first_name}}) on {{appointment.only_start_date}} {{appointment.only_start_time}} {{appointment.timezone}}. Setter: please add the hand-off note in this thread.`
   *No Slack action in your account?* Use **Webhook** → POST to your Slack incoming-webhook URL with body `{"text":"New booking: {{contact.company_name}} on {{appointment.only_start_date}} {{appointment.only_start_time}}"}`. Keep the webhook URL private.
5. **Internal Notification** → Email → to you: same text as the Slack message.

### Workflow 2 — "Reminders"

**Trigger:** *Customer Booked Appointment* → filter **Calendar is Vanguard Consultation**.

**Actions:**
1. **Wait** → *Event/Appointment time* → **24 hours before**.
2. **Send Email** — Subject `Tomorrow: your Vanguard website walkthrough` — Body:
   > Hi {{contact.first_name}}, quick reminder that we're going through the site for {{contact.company_name}} tomorrow at {{appointment.only_start_time}} ({{appointment.timezone}}). Link: {{appointment.meeting_location}}. If the time no longer works: {{appointment.reschedule_link}}
3. **If/Else** → tag `sms-consent` → Yes: **Send SMS** `Reminder: your Vanguard walkthrough is tomorrow at {{appointment.only_start_time}}. Need to move it? {{appointment.reschedule_link}} Reply STOP to opt out.`
4. **Wait** → *Event/Appointment time* → **2 hours before**.
5. **Send Email** — Subject `Starting in 2 hours` — Body: `Hi {{contact.first_name}}, see you at {{appointment.only_start_time}}. Join here: {{appointment.meeting_location}}`
6. **If/Else** → tag `sms-consent` → Yes: **Send SMS** `See you at {{appointment.only_start_time}}: {{appointment.meeting_location}} Reply STOP to opt out.`

**Settings tab:** turn on **"Allow re-entry"** (so rebooked contacts get reminders again) and set the workflow to **stop when the appointment is cancelled** if your version offers it; otherwise add a *Goal* "Appointment status is Cancelled".

### Workflow 3 — "No-show"

You (the closer) mark a no-show by opening the appointment and setting **Status → No show**.

**Trigger:** *Appointment Status* → filter **Calendar is Vanguard Consultation** and **Status is No show**.

**Actions:**
1. **Add Contact Tag** → `no-show`.
2. **Add Task** → Title `Call within 15 min: no-show rebook` → Assign to **the contact's assigned user** (the setter) → Due in **15 minutes**.
3. **Slack / Webhook** → `No-show: {{contact.company_name}}. Setter, call now and offer two new slots.`
4. **Wait** 10 minutes → **Send Email** — Subject `Sorry we missed you` — Body:
   > Hi {{contact.first_name}}, looks like something came up, no problem at all. Grab a new time that suits you here: [booking link]. The demo for {{contact.company_name}} is still here: {{contact.demo_link}}
5. **If/Else** tag `sms-consent` → Yes: **Send SMS** `Hi {{contact.first_name}}, sorry we missed you today. Want to pick a new time? [booking link] Reply STOP to opt out.`

### Workflow 4 — "Opt-out"

**Trigger:** *Contact Tag Added* → tag **`do-not-contact`**.

**Actions:**
1. **Enable DND** (Update contact → DND) → **All channels** on.
2. **Remove from All Workflows** (or *Remove from workflow* → choose Workflows 1–3).
3. **Update Opportunity** → Pipeline Vanguard Sales → Status **Lost** → Lost reason **Not interested**.
4. **Internal Notification** → `Added to do-not-contact: {{contact.company_name}} {{contact.phone}}`.

Setters add the `do-not-contact` tag the same day anyone says "don't call me". GHL also sets DND automatically when someone replies STOP to a text.

---

## Test before go-live (5 min)

1. Create a test contact with your own email (and your phone, plus the `sms-consent` tag, only if A2P is approved).
2. Book it from the calendar link 3+ hours ahead → check: confirmation email, Slack/internal alert, opportunity moved to **Meeting Booked**.
3. Open the appointment → set **No show** → check the tag, task and email.
4. Add the `do-not-contact` tag → check DND is on and the opportunity is Lost.
5. Delete the test contact.
