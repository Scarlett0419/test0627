---
name: agency-pipeline
description: Runs Vanguard's website-agency sales pipeline end to end — prospecting local businesses with weak or missing websites, building a personalised demo site before the setter dials, setter cold-call scripts, booking, the owner's consultation/close, proposals, contracts and client onboarding. Use when working on any stage of that pipeline, e.g. "build a demo for this lead", "prep me for my call with X", "write the proposal for X", "review this week's pipeline", "coach this setter call", "onboard the new client".
---

# Vanguard Agency Pipeline

Setters cold call local businesses whose website is weak or missing, open with "we noticed your site and already built you a demo version", and book a 15–30 min call. The owner closes and delivers. The source-of-truth docs live in `agency/`; this skill routes each stage to the right doc and downloaded skill.

## Stage → docs → skills

| Stage | Read first | Use these skills |
|---|---|---|
| 1. Find & qualify leads | `agency/PIPELINE.md` Stage 1 | `prospecting` (local-business branch scores website status) |
| 2. Build the demo (before dialing) | `agency/DEMO_PLAYBOOK.md` | `scripts/generate_demo.py` for volume; `frontend-design` + `vertical-site-conventions` for high-value leads; `cro` to list the current site's gaps as call talking points; `netlify-deploy` to host; `webapp-testing` for before/after screenshots |
| 3. Setter outreach | `agency/SETTER_SCRIPT.md` | `sales-enablement` (talk tracks), `cold-email` (follow-ups), `sms` (texting rules) |
| 4. Meeting booked → show up | `agency/PIPELINE.md` Stage 4 | `meeting-conversion` (reminders, no-show recovery) |
| 5. Consultation & close | `agency/CLOSER_SCRIPT.md`, `agency/OFFER.md` | built-in `spin-selling`, `storybrand`; `hormozi-sales`, `negotiation`, `sandler` |
| 6. Proposal & contract | `agency/OFFER.md` §4–5 | `client-proposal-generator`, `contract-and-proposal-writer` |
| 7. Onboard & deliver | `agency/PIPELINE.md` Stage 7 | `onboarding-checklist`, `frontend-design` |
| Weekly review | `agency/PIPELINE.md` metrics | `pipeline-reviewer` (on a CRM CSV export); `next-step-commitment` to grade call transcripts |
| Offer changes | `agency/OFFER.md` | built-in `100m-offers`, `money-models`; `offers` |

## Non-negotiables

- **Never invent facts** — not about the prospect (ratings, years, client counts on a demo) and not about Vanguard (testimonials, results). Demo stats go in only via `--highlights` from verified sources. Unknowns stay `[TBD]`.
- **The demo must exist before the dial.** The hook is "we already built it".
- **No unsolicited texts.** Text only people who said yes to texts on a call; log consent in the CRM. Everyone else gets email/DM. DNC-scrub every number before it enters the dial queue. Recommend legal review before scaling calling/texting.
- **Honest urgency only.** No fabricated scarcity or pretext closes (skip the "ID close" in `hormozi-sales`).
- Offer prices come from `agency/OFFER.md`; don't quote numbers that aren't there.

## Third-party skills

Everything except this skill was downloaded from GitHub and vetted; see `.claude/skills/SOURCES.md` for repos, commits and licenses. Some examples in them are SaaS- or enterprise-flavoured — adapt to local-business deal sizes ($1.8K–$2.8K projects).
