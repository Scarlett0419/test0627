# GoHighLevel Build Log

Built via the GHL API on 21 Oct 2026 in sub-account **vanguard Structures** (location `VtQXuTK0aam1kdjpvzQ7`, time zone Europe/London). No tokens are stored in this repo.

## Done through the API

**Pipeline:** `Vanguard Sales` (id `Z9L2zyo1BqB264gX2iKa`)
Cold Lead → Demo Built → Contacted → Meeting Booked → On Call → Proposal Sent → Closed Won → Closed Lost.
The empty default "Marketing Pipeline" was deleted.

**Calendar:** `Vanguard Consultation` (id `UhYVsNtzcGJSkMQDWUaG`, slug `vanguard-consultation`)
30-minute slots, 15-minute buffer, Mon–Fri 14:00–21:00 UK time (09:00–16:00 US Eastern in summer time), up to 8 a day, bookable 2 hours to 14 days ahead, auto-confirm, reschedule and cancel allowed.

**Contact custom fields (21):** Demo Link · Demo Built · DNC Scrub Date · Internal Do Not Call · SMS Consent · SMS Consent Date Time · SMS Consent Method · Niche · City Market · Website Quality · Business Size · Lead Source · Setter Assigned · Follow Up Attempt Number · Last Contact Date · Next Follow Up Date · Intent Score 1 to 10 · Main Objection · Demo Link Sent Before Call · Setter Call Notes · Closer Call Notes

**Opportunity custom fields (7):** Package · Care Plan · Payment Collected Amount · Payment Collected Date · Refunded Amount · Refunded Date · Commission Rate. (Lost Reason uses GHL's built-in field.)

**Tags (19):** needs-dnc-scrub · dnc-scrubbed · do-not-contact · sms-consent · demo-built · demo-link-sent · no-show · care-plan · beauty-wellness · fitness · trades · auto · pet-local-services · src-cold-call · src-linkedin · src-facebook · src-email · src-reddit · src-referral

**Sample data:** the 4 "(Example)" deals were deleted. The 5 "(example)" contacts still show in the account and need deleting by hand (Contacts → select all 5 → Delete).

## Still to do in the GHL app (the API can't, or shouldn't)

1. **Calendar meeting location:** Settings → Calendars → Vanguard Consultation → Meeting location → Zoom or Google Meet. Connect your Google/Outlook calendar under Calendars → Connections so personal events block slots.
2. **Choose one booking tool:** the GHL calendar triggers workflows natively; Calendly needs an extra integration. Recommended: use the GHL calendar link for setters.
3. **Workflows** (Automation → Workflows → Create new):
   - *Booked:* trigger Customer Booked Appointment (Vanguard Consultation) → Create/Update Opportunity (Vanguard Sales → Meeting Booked) → Send confirmation email with demo link → notify Slack.
   - *Reminders:* trigger Customer Booked Appointment → Wait until 24h before → email → If/Else tag `sms-consent` → SMS → Wait until 2h before → email (+ SMS if consent).
   - *No-show:* trigger Appointment Status = No show → add tag `no-show` → task for the setter "call within 15 minutes" → notify Slack.
   - *Opt-out:* trigger Contact Tag Added `do-not-contact` → set DND on all channels.
4. **Setter logins:** Settings → My Staff → Add employee → role User; allow Contacts, Opportunities and Conversations (assigned data only), Calendars; turn off Settings, Payments, Marketing and exports.
5. **Phone numbers + A2P/calling registration**, then **Stripe** under Payments → Integrations.
6. **Leads:** after the DNC scrub, Claude imports the scrubbed lists with niche, city and source tags.
