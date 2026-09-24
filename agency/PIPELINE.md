# Vanguard Sales Pipeline

**Agency:** Vanguard — Premium Website Design for Local & Service Businesses
**Model:** Setter cold outreach → Owner closes and delivers
**Niches:** Faith organizations, Beauty/Wellness, Fitness, Construction/Trades

---

## Pipeline Stages

### Stage 1: Cold Lead
**Definition:** Contact identified, not yet reached.
**Owner:** Setter
**Actions:**
- Pull business from target niche list (Google Maps, Instagram, Facebook, referrals)
- Qualify: Does the business have a weak/outdated/no website?
- Find decision-maker name and contact info (phone preferred, then DM/email)
- Scrub phone against the National DNC Registry + internal do-not-call list; log scrub date
- Log in CRM with all available fields
- Screenshot their current website (or note no site)

**Exit Criteria:** Lead qualified and DNC-clean → moves to Demo Built

---

### Stage 2: Demo Built
**Definition:** A personalized demo site exists at a live link **before the first dial** — the setter's hook is "we already built it," so it has to be true.
**Owner:** Setter (collects info) → Owner or demo builder (builds + spot-checks)
**Actions:**
- Setter submits: business name, niche, services, city, phone, current site URL, and any verified facts (Google rating, years in business)
- Build with `scripts/generate_demo.py` (pass verified facts only via `--highlights`) — or, for high-value leads, a custom build using the `frontend-design` + `vertical-site-conventions` skills
- Deploy to a shareable link (`netlify-deploy` skill; see DEMO_PLAYBOOK.md)
- Owner spot-checks the first demos each week: nothing invented, no scraped logos/photos
- Paste demo link into CRM

**Exit Criteria:** Demo link live and logged → lead enters the dial queue

---

### Stage 3: Contacted
**Definition:** Outreach has been attempted (call, voicemail, email, DM).
**Owner:** Setter
**Actions:**
- Log every touchpoint with timestamp
- If no answer: voicemail on attempt 1, email with demo link same day (text only if they've previously said yes to texts)
- Follow-up cadence runs (see Follow-Up Rules below)
- If connected but not booked: handle objections, re-attempt booking; offer to send the demo link either way

**Exit Criteria:** Meeting booked, OR lead marked Cold/Not Interested after full cadence

---

### Stage 4: Meeting Booked
**Definition:** Prospect has confirmed a call on the calendar.
**Owner:** Setter (books) → Owner (prepares)
**Actions:**
- Setter sends calendar link (Calendly or similar)
- Confirmation sent immediately after booking (text if they said yes to texts, otherwise email)
- 24-hour reminder sent by setter (same channel rule; see `meeting-conversion` skill for show-rate tactics)
- 1-hour reminder sent by setter
- Owner receives lead brief: business name, niche, current site issues, setter notes
- Owner reviews demo site before call

**Exit Criteria:** Call happens (moves to On Call) or no-show (setter follows up within 2 hours to rebook)

---

### Stage 5: On Call
**Definition:** Owner is on consultation call with prospect.
**Owner:** Owner (closes)
**Actions:**
- Owner runs SPIN discovery (see CLOSER_SCRIPT.md)
- Owner walks through demo
- Owner presents offer and price
- Owner handles objections
- Owner attempts close on the call

**Exit Criteria:** Verbal yes (moves to Proposal Sent or Closed Won), or follow-up needed (moves to Proposal Sent)

---

### Stage 6: Proposal Sent
**Definition:** Owner has sent formal proposal or follow-up after the call.
**Owner:** Owner
**Actions:**
- Proposal includes scope, price, timeline, payment terms
- Sent within 24 hours of call
- Owner follows up by phone 48 hours after sending if no response
- Second follow-up at 5 days if still no response
- Third follow-up at 10 days — after this, lead is marked Closed Lost unless they re-engage

**Exit Criteria:** Prospect signs/pays (Closed Won) or goes dark for 10+ days (Closed Lost)

---

### Stage 7: Closed Won
**Definition:** Client has signed the agreement and paid the project fee in full.
**Owner:** Owner
**Actions:**
- Send onboarding form / kick-off questionnaire
- Collect brand assets, domain access, copy
- Project moves to delivery
- Request testimonial/review at project completion
- Ask for referrals at go-live

---

### Stage 8: Closed Lost
**Definition:** Prospect declined, went dark, or is not a fit.
**Owner:** Setter (re-nurture) / Owner (high-value follow-up)
**Actions:**
- Log reason for loss
- Tag for re-nurture in 60–90 days if reason was timing
- Remove if not a fit (wrong niche, no budget, no interest)

---

## Key Metrics to Track

| Metric | Target | Who Tracks |
|--------|--------|------------|
| Dials per setter per day | 50–80 | Setter |
| Connections (live answers) per day | 10–20 | Setter |
| Meetings booked per day | 2–4 | Setter |
| Show rate (booked vs. showed) | 70%+ | Owner |
| Demo-to-meeting conversion | 40%+ | Setter |
| Close rate (calls to Closed Won) | 30–50% | Owner |
| Avg deal size | Track per niche | Owner |
| Time from booked to call | < 5 days | Setter |
| Re-book rate (no-shows recovered) | 50%+ | Setter |

**Weekly review:** Every Monday — setter reviews dial volume and booking rate; owner reviews show rate and close rate.

---

## CRM Field List

Capture the following for every lead:

**Contact Info**
- Business name
- Owner/decision-maker first name
- Phone number (mobile preferred)
- DNC scrubbed? (date) · Internal do-not-call flag
- SMS consent (Y/N + date/time + how given — verbal on call, form, etc.)
- Email address
- Instagram / Facebook handle
- Website URL (or "none")

**Qualification**
- Niche (faith / beauty-wellness / fitness / construction-trades / other)
- City / market
- Website quality rating: None / Terrible / Outdated / Decent / Good
- Estimated business size (solo / small team / established)
- Lead source (cold call / DM / referral / inbound)

**Pipeline Tracking**
- Current stage
- Date entered current stage
- Last contact date
- Next follow-up date
- Follow-up attempt # (1–5+)
- Setter assigned
- Demo built? (Y/N + link)
- Meeting date/time (if booked)
- Outcome (Closed Won / Closed Lost + reason)
- Deal value

**Notes**
- Setter call notes (objections raised, vibe, what resonated)
- Owner call notes (discovery answers, key pain points, what closed or killed the deal)

---

## Follow-Up Cadence Rules

### Setter Follow-Up (Cold Lead → Meeting Booked)

| Attempt | Timing | Method |
|---------|--------|--------|
| 1 | Day 1 | Cold call — if no answer, leave voicemail |
| 2 | Day 1 (same day as VM) | Email with demo link, referencing voicemail |
| 3 | Day 3 | Call again — if no answer, drop DM |
| 4 | Day 5 | Call + email with demo hook |
| 5 | Day 8 | Final call + "closing the loop" email |

After 5 attempts with no response: mark Contacted/Cold, tag for re-nurture in 60 days.

**Demo hook rule:** The demo is already built (Stage 2), so lead with it on attempt 1 — every voicemail and email mentions it.

**Texting rule:** no texts to anyone who hasn't said yes to texts. Templates and reasons in SETTER_SCRIPT.md.

### Post-No-Show Follow-Up (Setter)
- 2 hours after missed call: text to rebook if they gave SMS consent at booking, otherwise email
- Same day: phone call attempt
- 24 hours later: final rebook attempt
- If no response after 3 rebook attempts: mark Contacted, restart cadence

### Owner Follow-Up (Proposal Sent)
- Day 1 post-call: send proposal
- Day 3: follow-up call ("Just checking you got the proposal — any questions?")
- Day 7: follow-up email, or text if they gave consent (create urgency around start date availability — only if it's true)
- Day 12: final follow-up — "I want to make sure I'm not holding a spot if you've decided to go another direction"
- Day 12+: mark Closed Lost, setter re-nurtures in 60 days

---

## Notes on Niche Prioritization

- **Faith orgs:** Long decision cycles, but high loyalty and referral potential. Social proof: Christ United.
- **Beauty/Wellness:** Fast decisions, visual-driven — demo impact is highest here. Social proof: Elixa Beauty.
- **Fitness:** Competitive, but owners respond to lead generation angle. Social proof: MagniFit.
- **Construction/Trades:** High deal sizes, skeptical buyers — credibility and professionalism are the key levers. Social proof: Vanguard Structures.
