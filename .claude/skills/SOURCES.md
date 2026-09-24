## Demo-website building skills (added 2026-09-24)

| Skill | Repo | Commit SHA | License | Why it helps demo building |
|---|---|---|---|---|
| frontend-design | https://github.com/anthropics/skills (skills/frontend-design) | 34040c9c568585f6929bedeaad110ad08f079624 | Apache-2.0 | Plan-then-build design process that avoids templated "AI look"; gives each prospect a distinct palette, type and hero. |
| vertical-site-conventions | https://github.com/rampstackco/claude-skills (skills/vertical-site-conventions) | 3d4510a94a76ead80122c691b5c480f92f3fbe40 | MIT | Per-vertical composition checklists (salons/gyms/barbers, restaurants, nonprofits/churches) so demos read as the prospect's industry, with honest demo-only booking. |
| webapp-testing | https://github.com/anthropics/skills (skills/webapp-testing) | 34040c9c568585f6929bedeaad110ad08f079624 | Apache-2.0 | Playwright patterns and a local-server helper for before/after screenshots of the prospect's current site and the demo. |
| netlify-deploy | https://github.com/netlify/context-and-tools (skills/netlify-deploy) | 0830047fec55c33ea3f360b528c2039b9d96d97f | MIT | Official Netlify CLI deploy guide (draft or prod, `--allow-anonymous` temp sites) to get a shareable demo link fast. |
| cro | https://github.com/coreyhaines31/marketingskills (skills/cro) | 5b2c0007766c6a1cf1d53fd8fc73e979e0821022 | MIT | Structured conversion audit of the prospect's current site (value prop, CTAs, trust, friction) that gives setters talking points. |

LICENSE files: the anthropics skills ship LICENSE.txt. For the three MIT skills, the repo-root LICENSE was copied into each folder as LICENSE. Nothing else in the skill folders was changed.

## Offer, sales and agency-operations skills (added 2026-09-24)

| Skill | Repo | Commit SHA | License | Why it helps the agency |
|---|---|---|---|---|
| offers | https://github.com/coreyhaines31/marketingskills (skills/offers) | 5b2c0007766c6a1cf1d53fd8fc73e979e0821022 | MIT | Offer construction with service/agency-retainer formats (paid-pilot guarantees, capacity scarcity, productized naming) and anti-hype guardrails; complements 100m-offers. |
| prospecting | https://github.com/coreyhaines31/marketingskills (skills/prospecting) | 5b2c0007766c6a1cf1d53fd8fc73e979e0821022 | MIT | Local-SMB branch scores businesses by website status (none / social-only / weak / has site), giving setters a qualified call list, with compliance guardrails against scraping. |
| hormozi-sales | https://github.com/andrescala/alex-hormozi-gtm-skills (Skills/hormozi-sales) | d8519910f8ce3a26f301cf9cfeebede900167510 | MIT | Closer playbook for the setter-to-closer model: CLOSER call structure, objection scripts (price, spouse/partner, "think about it"), show-rate reminders and funnel KPIs. |
| client-proposal-generator | https://github.com/OneWave-AI/claude-skills (client-proposal-generator) | f317e08649a6584ed4cd0b1ae353f123f4daf791 | MIT | Turns a discovery call into a 3-tier proposal (exec summary, scope, timeline, pricing, terms) and refuses to make up case studies. Its pricing benchmarks are consulting-scale, so swap in the agency's own prices. |
| onboarding-checklist | https://github.com/OneWave-AI/claude-skills (onboarding-checklist) | f317e08649a6584ed4cd0b1ae353f123f4daf791 | MIT | Agency-mode client onboarding plan (asset collection, approval gates, revision limits, launch) plus 5 client email templates. |
| contract-and-proposal-writer | https://github.com/alirezarezvani/claude-skills (business-growth/skills/contract-and-proposal-writer) | 19392f7a08264ed00486a251f5b2098321771f94 | MIT | Web-dev fixed-price contract and monthly retainer templates (milestone payments, IP on full payment, change orders, termination). A starting point, not legal advice. |

LICENSE: each folder has a copy of its repo-root MIT LICENSE. Nothing else in the skill folders was changed. Note: prospecting's "Tool Integrations" table links to ../../tools/ files in the source repo, which were not copied, so those links do not resolve.

## Outbound sales, appointment-setting and pipeline skills (added 2026-09-24)

| Skill | Repo | Commit SHA | License | Why it's useful |
|---|---|---|---|---|
| sales-enablement | https://github.com/coreyhaines31/marketingskills (skills/sales-enablement) | 5b2c0007766c6a1cf1d53fd8fc73e979e0821022 | MIT | Builds setter talk tracks, objection docs (objection, why they say it, response, proof, follow-up question), demo-walkthrough scripts and a sales playbook. |
| cold-email | https://github.com/coreyhaines31/marketingskills (skills/cold-email) | 5b2c0007766c6a1cf1d53fd8fc73e979e0821022 | MIT | Short peer-voice outreach and 3-5 touch follow-up sequences with a different angle each time and a breakup email that is honoured. Bans fake "Re:" subject lines. |
| sms | https://github.com/coreyhaines31/marketingskills (skills/sms) | 5b2c0007766c6a1cf1d53fd8fc73e979e0821022 | MIT | Mainly here for its TCPA / A2P 10DLC / quiet-hours / STOP-HELP compliance reference before setters text prospects. The sequence templates are written for e-commerce. |
| meeting-conversion | https://github.com/louisblythe/Sales-Skills (skills/meeting-conversion) | e0f13a6eb41be22fa1f8493b148077cdd6c6654a | MIT (README statement only; repo has no LICENSE file, see LICENSE-NOTE.txt) | Show-rate playbook for booked appointments: confirmation within 5 minutes, day-before and day-of reminders, pre-meeting check-in, and no-show recovery. |
| next-step-commitment | https://github.com/zime-ai/zime-gtm-skills (skills/next-step-commitment) | 4f134175badd08302f070c77449822c48403eeb1 | MIT | Checks a call transcript's ending: did the setter lock in a specific action, a date, and something the prospect also committed to? Gives one rewrite. Runs locally. |
| sandler | https://github.com/zime-ai/zime-gtm-skills (skills/sandler) | 4f134175badd08302f070c77449822c48403eeb1 | MIT | Coaches the closer by scoring a call transcript on the Sandler steps (up-front contract, pain, budget, decision, fulfilment) with a quote for every finding. It flags pitching before pain and closes that were assumed rather than agreed. |
| negotiation | https://github.com/wondelai/skills (negotiation) | c172996495bed0fcd26896a9416b2093fd7073f0 | MIT | Chris Voss techniques for the close: labelling, calibrated "how/what" questions, accusation audit, "that's right", and handling "that's not fair". |
| pipeline-reviewer | https://github.com/quotakit/salesops-skills (skills/pipeline-reviewer) | b88a629fcfcafd0a1d348b9f70eb9de6a1fea19c | MIT | Weekly review of a CRM export using a bundled local pandas script (no network access): flags stale, slipped and aging deals, shows totals per rep, and gives a fix/kill list. |

LICENSE: the repo-root MIT LICENSE was copied into each folder as LICENSE, except meeting-conversion (see note above). Nothing else in the skill folders was changed. prospecting (listed above) was already installed and was not duplicated. The coreyhaines31 skills link to ../../tools/ files that were not copied, so those links do not resolve.
