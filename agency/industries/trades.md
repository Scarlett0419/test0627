# Industry Playbook — Trades
**Covers:** roofing, fencing, painting, plumbing, HVAC, concrete, landscaping, handyman, general contractors
**Use with:** SETTER_SCRIPT.md, CLOSER_SCRIPT.md, DEMO_PLAYBOOK.md, OFFER.md
> No market statistics here on purpose. Anything numeric you say on a call must come from the prospect or a source you checked.

---

## 1. How They Get Customers Today
- **Referrals / word of mouth** — past customers, neighbors who saw the crew working, GCs subbing work out.
- **Lead marketplaces** — Angi, HomeAdvisor, Thumbtack, Nextdoor. They pay for leads that are often shared with competitors.
- **Google Business Profile** — the "website" for many; calls come straight off the map listing.
- **Facebook** — local groups, a business page with job photos.
- **Physical signage** — truck wraps, yard signs, door hangers.

**Why no website:** busy with jobs, "never needed one," burned by a cheap builder, think a site is for bigger companies, or believe GBP/Facebook is enough.

**Decision-maker:** the owner (often also the lead tech). Spouse/office manager often answers the phone and handles books — treat them as a gatekeeper *and* an influencer.

**When reachable:** early morning before crews roll out, lunch, and early evening after the job site. Mid-morning/afternoon they're on a roof or under a sink — keep it short or book a callback. Always stay within 8am–9pm *their* time (SETTER_SCRIPT compliance).

---

## 2. What the Website Must Do
| Must-have | Why |
|---|---|
| **"Get a Free Quote" form** (name, phone, address/ZIP, job type, photo upload optional) | Captures leads while the owner is on a job |
| **Click-to-call** sticky on mobile; "24/7 Emergency" for plumbing/HVAC only if they actually offer it | Emergency buyers call, they don't browse |
| **Project gallery / before-after** | The work sells itself; homeowners want proof |
| **Service area** (list of towns or map) | Qualifies leads, helps local search |
| **License / insurance / bonded badges** | Only display what the owner confirms and you can verify (e.g., state license lookup). Never assert a license is required or held without checking |
| **Reviews** pulled/quoted from Google (with permission) | Trust |
| **Financing mention** | Only if the owner already offers financing through a provider |
| **Services pages** per trade line (e.g., repair vs. replacement) | Local SEO + clarity |

**Tier fit:**
- **Foundation** — handymen, solo painters, small fence/landscape crews.
- **Full Presence** — roofers, HVAC, plumbing, GCs, multi-service or multi-crew outfits (gallery + service-area pages + quote flow).

---

## 3. Owner Language & Pains
They say: "jobs," "bids," "estimates," "tire-kickers," "I'm booked out," "the phone rings off the hook in spring," "Angi leads are junk," "I'm on a roof all day."

Pains: paying for shared leads; missing calls while working; competing on price; bids that ghost; slow seasons; looking small next to competitors with trucks and sites.

### SPIN Questions (closer)
1. **S:** "Where did your last five jobs come from — referral, Angi/Thumbtack, Google, or a sign?"
2. **P:** "When you're on a job and the phone rings, what happens to that call?"
3. **P:** "How do you feel about the leads from Angi/HomeAdvisor — how many turn into jobs, and how many other contractors got the same lead?"
4. **I:** "If someone gets referred to you, Googles your name, and finds only a map pin — while the other guy has a site full of finished jobs — who do you think they call first?"
5. **I:** "What does a missed after-hours call cost you — what's your average job worth?" (Let *them* give the number.)
6. **I:** "When winter/slow season hits, what fills the calendar?"
7. **N:** "If homeowners could see your past work and send you photos of their job before you drive out, how much time would that save on estimates?"
8. **N:** "If even one or two of the jobs you're paying lead fees for came in directly instead, what would that be worth over a year?"

---

## 4. Objections
**"I've got more work than I can handle."**
> "Love that. A site isn't just more calls — it's *better* calls. Service area and a quote form filter out the jobs you don't want, and you can raise prices when people see your work first. And it keeps the phone ringing in the slow months."

**"Word of mouth is enough."**
> "Word of mouth is your best source — so what happens after the referral? Most people look you up before calling. The site's job is to close the referral your customer already gave you."

**"I pay Angi/HomeAdvisor."**
> "Keep it if it's working. The difference: those leads get shared and you pay per lead, forever. Your own site is a one-time build and the leads are only yours. Most owners use it to lean on the paid stuff less over time."

**"I'm not a computer guy."**
> "You don't have to be. We write it, build it, launch it. Your whole job is one call and sending us some job photos off your phone. The Care Plan handles changes — you just text us."

**"Too expensive."**
> "What's one average job worth to you? If the site brings in one job you wouldn't have gotten, it's paid for. The Foundation tier is there if we need to start leaner."

**"I'll get my nephew to do it / Wix."**
> Use OFFER.md #7 — quote-flow, service-area pages and local SEO setup are what separates a brochure from a lead machine.

---

## 5. Setter Openers & Talking Points
**Variant A — reviews angle (only if you saw them):**
> "Hey [Name], [Setter] with Vanguard. I found [Business] on Google — solid reviews for [trade] in [city] — but no website, just the map listing. We went ahead and built you a demo with your services on it. Got 15 minutes this week so the owner can walk you through it?"

**Variant B — job-site timing:**
> "I know you're probably heading to a job, so I'll be quick — we built a free demo website for [Business]. Can I grab 15 minutes with you early morning or after you're off site?"

**Variant C — truck/sign angle:**
> "You've clearly got a presence around [city] — people see your trucks. When they Google you, there's nowhere to send them. We built that page already."

Talking points: "free quote form works while you're on the roof," "show your finished jobs," "leads that are only yours," social proof: *Vanguard Structures* (construction).
Don't: promise rankings, quote lead-cost numbers you haven't verified, or call them "unlicensed."

---

## 6. Demo Guidance
```
python scripts/generate_demo.py --industry construction \
  --business_name "..." --phone "..." --location "City, ST" \
  --services "Roof Replacement,Roof Repair,Storm Damage,Gutters,Inspections" \
  --highlights "value:label,..."    # verified only
```
- **Preset:** `construction` for all trades (default CTA "Get a Free Quote"). Landscaping/handyman also fine on `construction`.
- **Sections to emphasise on the call:** hero + quote CTA, services grid, trust bar, contact/footer phone. Talk through gallery and service-area as what the full build adds.
- **CTA wording ideas:** "Get a Free Quote," "Request an Estimate," "Call Now — Emergency Service" (only if they do emergencies), "Schedule an Inspection."
- **Services:** 4–8 from GBP services tab/Facebook. Use their words.
- **--highlights (verified only):** years in business (from BBB/state records/their own listing), Google rating + review count as currently shown, license # only if found on the state lookup, "Family-owned" only if they say so. When sources conflict (common in directories), leave it out.

---

## 7. Seasonality, Payment, Red Flags
| Trade | Busy | Best time to sell |
|---|---|---|
| Roofing | After storms / hail and wind events; warm months | Just before season or in slow lulls; post-storm they're too busy to talk |
| Landscaping | Spring–fall | Late winter ("get ready for spring") |
| HVAC | Peak heat and cold | Shoulder seasons (spring/fall) |
| Painting/concrete/fencing | Dry, warm months | Winter planning period |
| Plumbing/handyman/GC | Fairly year-round | Anytime; avoid early morning emergencies |

(Seasonality is general and regional — ask "when's your slow season?")

**Ability to pay upfront:** usually fine — owners are used to deposits and job-sized invoices. Frame the price against one job. If cash is tight in the off-season, offer Foundation, don't discount.

**Red flags:** can't confirm any license/insurance they claim; wants the site to list services they don't do; "I'll pay after it brings jobs"; no phone answered ever (lead will die on the site too); asks us to copy a competitor's photos.

---

## 8. Upsell / Care Plan Angles
- **Care Plan:** "Text us new job photos, we post them" — keeps the gallery fresh monthly.
- Seasonal banner swaps (storm response, spring clean-up, furnace tune-ups).
- Additional service-area / city pages (scope extra).
- Review request link and GBP updates.
- Financing page once they sign up with a provider.
- Later: Spanish-language page if their customer base needs it.
