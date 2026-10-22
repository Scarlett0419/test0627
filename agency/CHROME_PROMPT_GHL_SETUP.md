# Claude in Chrome prompt — finish the GHL setup

Paste everything inside the box below into **Claude in Chrome** while you're logged into GoHighLevel in that browser, inside the **vanguard Structures** sub-account. It builds the 4 workflows and the contract template, and stops for you at the Stripe login. Check its work before publishing anything that sends messages.

````text
You're helping me finish setting up my GoHighLevel sub-account "vanguard Structures" (Vanguard Studios, a web studio selling websites to US local businesses). Work in my current GoHighLevel tab. Ask me before anything that sends a real message to a real contact, and stop and hand over to me whenever a login, payment or permission screen appears.

TASK 1 — Connect Stripe
Go to Payments → Integrations → Stripe → Connect. When the Stripe login appears, STOP and tell me to log in. After I've finished, confirm the integration shows as connected. Products already exist: The Foundation ($997 one-time), The Full Presence ($1,497 one-time) and Care Plan ($197/month). Check they're there under Payments → Products and that each shows its price.

TASK 2 — Build these 4 workflows exactly as specified, then Save. Publish workflows 1, 3 and 4. Leave workflow 2 (Reminders) as a draft and tell me so I can check its wait steps. If a menu label differs from the spec, use the nearest equivalent and tell me what you chose. Use the merge-field picker for every {{...}} field so the names match. For Slack, if there's no native Slack action, add an Internal Notification email to me instead and tell me.

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


TASK 3 — Contract template
Go to Payments → Documents & Contracts → Templates → + New → Blank. Name it "Website Build Agreement". Add a Text block containing the agreement below. Re-insert {{contact.company_name}}, {{contact.first_name}}, {{contact.last_name}} and {{contact.email}} using the merge-field picker. Replace the package table in section 1.1 with a Products/Price block offering The Foundation and The Full Presence (choose one per client) and Care Plan as optional. Turn on payment collection on signing if the option exists. Add Signature and Date fields for the client (recipient) and for me (sender). Leave anything in [square brackets] as it is; I'll fill those in. Save as a template, don't send it to anyone.

### WEBSITE BUILD AGREEMENT

This agreement is between **[Your legal name / company name], trading as Vanguard Studios**, [registered address] ("**Vanguard**", "we"), and **{{contact.company_name}}**, represented by **{{contact.first_name}} {{contact.last_name}}**, {{contact.email}} ("**Client**", "you").

It starts on the date the Client signs (the "**Start Date**").

---

#### 1. What we're building

1.1 **Package.** You are buying the package selected below:

| Package | Includes | Price (one-time, USD) |
|---|---|---|
| ☐ **The Foundation** | A custom website of up to **5 pages** | **$997** |
| ☐ **The Full Presence** | A custom website of up to **8 pages**, plus online booking or inquiry integration, gallery and testimonials section | **$1,497** |

1.2 **Every package includes:**
- custom design, built mobile-first, with a clear call-to-action on every page;
- website copy written by Vanguard from your onboarding form and one 30-minute kick-off call;
- a niche site blueprint (recommended pages, structure and calls-to-action) before design starts;
- a mobile photo guide and curated stock images where you don't have photos;
- local SEO foundation: page titles, meta descriptions, heading structure, and a Google Business Profile optimization checklist;
- **two rounds of revisions** (section 4);
- the "Love It or We Fix It" design reset (section 5.2);
- a 30-minute handoff session showing you how to make basic updates;
- 30 days of defect fixes after launch (section 8).

1.3 **Not included** (available as a separate quote): logo or brand design; professional photography or video; e-commerce or online payments beyond a booking/inquiry tool; more pages than your package allows; blog content; paid advertising; ongoing SEO or rankings work; third-party costs (section 6.3); content translation; and changes requested after launch (covered by the Care Plan or quoted separately).

---

#### 2. Price and payment

2.1 The package price is due **in full, up front, when you sign** this agreement. Work starts once payment has cleared.

2.2 Prices are in US dollars. You're responsible for any bank, currency-conversion or card fees on your side.

2.3 If you have a question about a charge, contact us first at [support email]. We'll answer within 2 business days. Filing a card dispute or chargeback without contacting us first is a breach of this agreement.

---

#### 3. Timeline and the 14-Day Launch Guarantee

3.1 **Onboarding.** After payment you'll get a short onboarding form. When it's submitted, we book a 30-minute **kick-off call**. The kick-off call date is **Day 0**.

3.2 **Build schedule** (calendar days from Day 0): design direction preview by Day 3; revision round 1 by Day 8; revision round 2 by Day 11; launch by **Day 14**. We confirm the exact dates by email after the kick-off call.

3.3 **Your review windows.** You have **2 business days** to reply to each review (1 business day for revision round 2). Please send feedback in one consolidated message from one named approver.

3.4 **14-Day Launch Guarantee.** If your site is not live within 14 days of the kick-off call, and you have met the review windows and provided the items you agreed to, **your first month of the Care Plan is free**. If you don't take the Care Plan, you can instead use that month as a $197 credit toward extra work within 6 months. This is the only remedy for a late launch.

3.5 **Pauses.** The timeline (and the guarantee date) moves later, day for day, whenever something we're waiting on from you is late: a review reply, content or photos you agreed to send, access to your domain or Google Business Profile, or approver availability. We'll tell you in writing on the first late day, with the new launch date.

3.6 **Going quiet.** If we don't hear from you for **10 business days** while waiting on you, the project goes on hold. If we don't hear from you for **30 days** after that, we'll launch the site based on the latest approved version (or deliver the files if launch needs your access), and the project counts as complete.

---

#### 4. Revisions

4.1 Two revision rounds are included. A round is one consolidated set of changes to the site as it stands (wording, images, layout tweaks, colors, sections within your page count).

4.2 New pages, new features or a change of scope after kick-off are outside the package. We'll quote them before doing any work.

---

#### 5. Approvals and the "Love It or We Fix It" policy

5.1 You approve the site for launch in writing (email is fine). Launch counts as approval if you've been sent the final version and haven't raised changes within your review window.

5.2 **Love It or We Fix It.** If, at the first design preview (Day 3), you feel the look and feel has **missed the mark entirely**, tell us in writing within that review window. We will build a new visual direction (new layout, type and color approach, not just tweaks) within 3 business days, at no extra cost. This is available once per project and replaces normal revision notes for that preview.

---

#### 6. What you provide

6.1 You'll provide accurate business information (services, prices, hours, service area, licenses), plus any logo, photos and testimonials you want used, through the onboarding form or kick-off call.

6.2 **Access.** Where we need access to your domain, hosting or Google Business Profile, you'll **invite us as a user or manager**. We will never ask for your passwords, and you should never send them to us.

6.3 **Third-party costs** are yours and paid directly to the provider in your name, including your domain name (about $10–$20/year) and any paid booking, email or software tools you choose. If you take the Care Plan, standard hosting is included (section 9).

6.4 You confirm you have the right to use everything you send us (photos, logos, text, reviews), and that the business information you give us is accurate. You're responsible for claims about your business, licenses and prices shown on the site.

---

#### 7. Ownership

7.1 Once the package price is paid in full, **you own the website's design, copy and content created for you**, and the domain is registered in your name.

7.2 We keep ownership of our own pre-existing tools, code libraries, templates and know-how, and give you a permanent, free license to use them as part of your website.

7.3 Stock images, fonts, plugins and platforms are used under their own licenses.

7.4 We may show your website in our portfolio and on social media. Email us if you'd rather we didn't, and we'll stop.

---

#### 8. After launch

8.1 For **30 days after launch**, we fix any defects (something that doesn't work as built) free of charge.

8.2 After that, changes are covered by the Care Plan or quoted separately.

---

#### 9. Care Plan (optional)

9.1 ☐ **Client adds the Care Plan: $197/month**, billed monthly from the launch date. Includes hosting management, security updates and backups, up to 1 hour of content updates per month (unused time doesn't roll over), and 48-hour response on business days.

9.2 Month-to-month. Cancel any time with notice before your next billing date; there's no lock-in and no refund for a partial month.

9.3 If you cancel, we'll hand over or move the site to hosting in your name within 14 days, or give you a full export, so you're never stuck.

---

#### 10. Cancellation and refunds

10.1 **Before the kick-off call:** you can cancel for a **full refund**.

10.2 **After the kick-off call and before the Day 3 design preview:** you can cancel for a **50% refund**.

10.3 **After the design preview has been delivered:** the package price is **non-refundable**. Section 5.2 is there to make sure you're happy with the direction.

10.4 We may end this agreement if you materially breach it and don't fix the breach within 10 business days of written notice. If we end the agreement for a reason that isn't your fault, we'll refund the unused part of the package price.

---

#### 11. What we don't promise

We build a professional website designed to earn trust and turn visitors into inquiries. **We don't guarantee search rankings, a number of leads or customers, or revenue**, because those depend on things outside our control (your market, reviews, competitors, search engines).

---

#### 12. Liability

12.1 Our total liability under this agreement is limited to the amount you paid us under it.

12.2 Neither of us is liable for indirect losses, such as lost profits, lost business or lost data, except where the law doesn't allow this to be limited.

12.3 Nothing here limits liability for fraud or anything else that can't be limited by law.

---

#### 13. General

13.1 **Independent businesses.** We're independent of each other; neither of us can bind the other.

13.2 **Confidentiality.** We each keep the other's non-public business information confidential.

13.3 **Notices** go by email to the addresses on this agreement.

13.4 **Entire agreement.** This is the whole agreement and replaces anything said before. Changes must be in writing and agreed by both of us (email is fine).

13.5 **Governing law.** This agreement is governed by the laws of **[England and Wales]**, and the courts of **[England and Wales]** have jurisdiction. *(Confirm with your lawyer; some US clients will ask for their own state's law.)*

13.6 **Electronic signatures** are valid and binding.

---

**Signed for Vanguard Studios:** ______________________ Name: [Your name] Date: ________

**Signed for {{contact.company_name}}:** ______________________ Name: {{contact.first_name}} {{contact.last_name}} Date: ________

---


WHEN DONE: give me a short checklist of what you completed, what you skipped or changed, and anything I need to finish by hand.
````
