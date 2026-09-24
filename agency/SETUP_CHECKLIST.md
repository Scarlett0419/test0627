# Vanguard — Sales Pipeline Setup Checklist

Everything needed to take the pipeline in `PIPELINE.md`, `OFFER.md`, `SETTER_SCRIPT.md`, and `DEMO_PLAYBOOK.md` from docs to a live, running operation. Check items off as they're completed.

---

## Phase 0 — Legal & Admin

- [ ] Form an LLC — liability shield before any contracts are signed or payments collected
- [ ] Open a business bank account — keep client payments separate from personal funds
- [ ] Lawyer review of the client contract (proposal/scope/payment terms in `OFFER.md`) before it's used live
- [ ] Lawyer review of calling/texting practices — B2B calls are partly exempt from the federal DNC rules, but small-business owners' cell phones blur that line, and state rules vary; get this signed off before setters start dialing at volume

## Phase 1 — GHL Core Setup

- [x] GHL account (already have)
- [ ] Build pipeline with stages from `PIPELINE.md`: Cold Lead → Demo Built → Contacted → Meeting Booked → On Call → Proposal Sent → Closed Won / Closed Lost
- [ ] Create custom fields (full list in `PIPELINE.md` CRM Field List): demo link, DNC scrub date, internal DNC flag, SMS consent (Y/N + date/time + how given), setter assigned, website quality rating, niche
- [ ] Set up GHL booking calendar to replace Calendly — done when the setter's booking link in `SETTER_SCRIPT.md` points to GHL and confirmation emails/texts fire automatically
- [ ] Set up dialer for setters — confirm call recording is only enabled in one-party-consent states; disable recording (or get explicit consent) in all-party-consent states
- [ ] Build reminder workflows: 24-hour, 1-hour, and no-show follow-up (matches cadence in `PIPELINE.md` Stage 4 and Post-No-Show rules)
- [ ] Build proposal/contract templates in GHL Documents & Contracts with e-signature — done when a template can be sent and signed end-to-end (see `OFFER.md` pricing/terms)
- [ ] Connect Stripe — configure full up-front payment at signing, plus a monthly Care Plan subscription started at launch
- [ ] Build client onboarding form (kick-off questionnaire per `PIPELINE.md` Stage 7: brand assets, domain access, copy)
- [ ] Configure DND settings for internal do-not-call — anyone who says "don't call me" gets flagged same day (per `SETTER_SCRIPT.md` Setter Rule 8)

## Phase 2 — Phone / SMS / Email Deliverability

- [ ] Register A2P 10DLC brand + campaign — required before any SMS goes out from GHL; do this before setters start texting
- [ ] Register CNAM for caller ID reputation — done when outbound calls show the business name instead of a raw number
- [ ] Provision local (not toll-free) numbers per market to reduce "Spam Likely" flags
- [ ] Subscribe to the National Do Not Call Registry (telemarketing.donotcall.gov) — or confirm the dialer/list service already scrubs against it
- [ ] Stand up the internal do-not-call list in GHL (separate from the national registry) — every opt-out request gets logged here immediately
- [ ] Register a separate cold-email domain (not the main agency domain) — protects primary domain reputation
- [ ] Set up SPF, DKIM, and DMARC on the cold-email domain
- [ ] Run a 2–3 week email warm-up before sending cold volume — done when warm-up sequence completes with no spam-folder placement
- [ ] Add a physical business address to all outbound email templates (legal requirement, also referenced in `SETTER_SCRIPT.md` email templates)

## Phase 3 — Demo Pipeline

- [ ] Create free Netlify account for demo hosting
- [ ] Set up a subdomain (e.g. `demo.youragency.com`) pointed at Netlify — done when a test demo resolves on that subdomain instead of a random `.netlify.app` URL
- [ ] Install Python 3 on the machine(s) that will run `scripts/generate_demo.py`
- [ ] Confirm `generate_demo.py` runs end-to-end and produces a live link (see `DEMO_PLAYBOOK.md` Sections 1–3)
- [ ] Set up Claude Code access for custom/high-value demo builds (per `PIPELINE.md` Stage 2 — uses `frontend-design` + `vertical-site-conventions` skills)
- [ ] Decide + document lead-source method: Google Maps manual research by niche + city, or a purchased list — avoid any scraping tool that violates Google's Terms of Service
- [ ] Set up Zoom or Google Meet for the owner's screen-share consultation calls
- [ ] Decide the platform client sites will be built/hosted on (GHL Sites, WordPress, Webflow, or custom) — this decision is required before the Care Plan can be sold, since hosting/updates depend on it
- [ ] Choose a domain registrar for client domain purchases/transfers

## Phase 4 — Team & Discord

- [x] Discord server exists (already have)
- [ ] Create channels: `#demo-requests`, `#booked-calls`, `#no-shows`, `#wins`, `#pipeline-alerts`, `#call-reviews`, `#scripts-and-docs`, `#leaderboard`
- [ ] Finalize setter pay plan (see `SETTER_PAY_PLAN.md`)
- [ ] Have setters sign a contractor agreement covering pay terms and a compliance clause (DNC/TCPA adherence) — coordinate with the Phase 0 lawyer review
- [ ] Run Discord onboarding for new setters (see `DISCORD_ONBOARDING.md`)
- [ ] Build GHL → Discord webhooks so pipeline events post automatically (see `GHL_DISCORD_WORKFLOWS.md`) — done when a new demo, booking, no-show, and closed-won each post to the right channel

## Phase 5 — Go-Live Test

- [ ] Book a test appointment end to end through the real booking flow
- [ ] Confirm the 24-hour and 1-hour reminders actually fire
- [ ] Confirm Discord notifications post to the correct channels for a test booking and a test close
- [ ] Send a test contract through GHL Documents & Contracts and confirm it can be e-signed
- [ ] Run a test $1 Stripe charge and confirm it processes and refunds cleanly

## Phase 6 — Delivery Readiness

- [ ] Agency website: embed the GHL calendar as a "Book a Call" CTA
- [ ] Agency website: add a portfolio section with real client work
- [ ] Agency website: confirm address/contact info is displayed (matches the physical-address requirement in Phase 2)
- [x] Agency website exists (already have)
- [ ] Confirm the Closed Won → onboarding flow works end to end: onboarding form sends automatically, brand assets/domain access/copy get collected, and the project handoff to delivery is clear (per `PIPELINE.md` Stage 7)
