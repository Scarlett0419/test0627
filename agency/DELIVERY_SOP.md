# Vanguard: Client Delivery SOP
**The 21-Day Authority Website System, from payment to launch and beyond**

Picks up where `PIPELINE.md` Stage 7 (Closed Won) ends. Offer terms come from `OFFER.md`. Notifications are in `GHL_DISCORD_WORKFLOWS.md`.

**Roles:** **Owner** = Vanguard (one person: sales, build, support). **Client** = the business owner, or the one approver they name.

**Rules that apply everywhere:**
- Never ask for, accept or store passwords. Access is shared through manager/delegate invites only. If a client sends a password anyway, don't use it. Ask them to change it, then send the invite steps.
- One named approver per client. Feedback from anyone else gets sent through that person.
- Every date, approval and change request goes in writing (email in GHL). A call doesn't count until the recap email is sent.
- Log every client-caused pause in GHL (a contact note tagged `clock-paused`) on the day it happens.

> **Open item for the owner** (settle before first use):
> - Guarantee wording in the contract must match Section 4, especially "feedback on schedule = 2 business days".

---

## 0. Delivery at a glance

| Step | Trigger | Owner | Done when |
|---|---|---|---|
| 1. Payment → automations | Stripe/GHL payment received | Automated + Owner | Welcome email and onboarding form sent, `#wins` posted, project card created |
| 2. Onboarding form | Welcome email | Client | Form submitted, assets uploaded, GBP manager invite sent |
| 3. Kick-off call (Day 0) | Form submitted | Owner + Client | Call held, timeline dates confirmed by email. **The 21-day clock starts.** |
| 4. Build (Days 1–21) | Kick-off | Owner | Site live on the client domain |
| 5. Launch + handoff | QA passed | Owner | Launch checklist complete, handoff session held |
| 6. Care Plan offer | Handoff session | Owner | Client said yes (billing set up) or no (logged) |
| 7. Post-launch asks | Launch + 7 days | Owner | Review requested, referral asked, testimonial captured or declined |

---

## 1. Payment received → automated steps

Payment is 100% upfront at signing. **No work and no kick-off booking until payment clears.**

| # | What happens | Who/what | Done when |
|---|---|---|---|
| 1 | Payment clears in GHL/Stripe | Client pays | Payment shows in GHL |
| 2 | Opportunity moves to **Closed Won** | GHL (auto or Owner) | Stage = Closed Won |
| 3 | `#wins` posts twice: 4a "Closed Won" and 4b "Payment received" | GHL → Discord | Both posts visible. If not, see the test plan in `GHL_DISCORD_WORKFLOWS.md` §8 |
| 4 | **Welcome email** with onboarding form link (Template A) | GHL workflow "Client Onboarding" | Email delivered (check GHL email log) |
| 5 | Tags `client-active` and `package-foundation` or `package-full-presence`; custom field `onboarding_sent_date` | GHL workflow | Fields populated |
| 6 | 48h wait → if form not submitted, chase-up (see 2.3) | GHL workflow | Branch configured |
| 7 | Owner creates a project folder and a delivery card (client, package, pages, price paid, setter) | Owner, within 1 business day | Folder and card exist |
| 8 | When the form is submitted: `#pipeline-alerts` 5c post, then the Owner books kick-off | GHL → Discord → Owner | Kick-off on calendar within 3 business days of submission |

**Client responsibility:** complete the form (about 20–30 min, estimate) and book kick-off.

---

## 2. Onboarding form (GHL form "Client Onboarding")

### 2.1 Question list

**A. Business details**
1. Legal business name / name as it should appear on the site
2. Primary contact name, mobile, email
3. **Approver:** the one person who approves design and copy (name, email, phone)
4. Business address. Also: do customers come to you, do you go to them, or both? (Service-area businesses can hide the address.)
5. Main phone number for the site (click-to-call). Is it text-enabled? (Y/N)
6. Business email for form notifications
7. Year founded, licenses/insurance/certifications to display (e.g. licensed & insured, license #)
8. In 2–3 sentences: what makes you different from competitors?

**B. Services and prices**
9. List every service (name, 1-line description)
10. Prices or "starting at" prices for each. Or check: "Don't show prices" / "Quote only"
11. Top 3 services you want more of (these get priority placement)
12. Anything you do NOT want to be called for

**C. Service area and hours**
13. Cities / neighborhoods / ZIPs you serve (list the main towns to target)
14. Travel radius or limits
15. Business hours by day, plus emergency/after-hours availability (towing, plumbing, roofing)
16. Holiday or seasonal hours

**D. Brand and assets** (file upload fields)
17. Logo upload (vector or PNG preferred). Check "I don't have a logo" if not.
18. Photos: work, team, shop/storefront, before/after (upload). Check "I need stock / photo guide" if not.
19. Brand colors (hex codes if known, or "match my logo", or "no preference")
20. Fonts or style words (e.g. "bold", "clean", "luxury", "friendly")
21. **2–3 websites you like** (any industry) and what you like about each
22. 1–2 competitor sites, and what you want to do better

**E. Domain and access (no passwords, ever)**
23. Do you own a domain? (Y/N). If yes, the domain name
24. Domain registrar (GoDaddy, Namecheap, Squarespace/Google Domains, Wix, other, don't know)
25. Who controls the registrar account? (you / old web person / don't know)
26. Current website URL, if any, and do you have access to it?
27. **Google Business Profile:** add our email as a **Manager** (step-by-step link included). Checkbox: "I've sent the manager invite" / "I don't have a GBP" / "I need help"
28. Booking tool in use (Square, Vagaro, Booksy, Mindbody, Calendly, Jobber, Housecall Pro, none)
29. Social profile links

> Form help text, shown at the top of section E: *"We will never ask for your passwords. We'll send simple steps to add us as a user or manager, and you stay the owner of everything."*

**F. Reviews and proof**
30. Google review link (or "don't know". The Owner can pull it from GBP)
31. Other review pages (Yelp, Facebook, Angi, Nextdoor)
32. 2–5 real customer testimonials you have permission to use (quote + first name/initial)
33. Can we feature your Google reviews on the site? (Y/N)

**G. Logistics**
34. Best times for the kick-off call (or embedded GHL calendar)
35. Any hard deadline (event, season, grand opening)?
36. Anything else we should know?

### 2.2 Done when
- All required fields are complete, and logo/photos are uploaded or "need help" is checked
- Approver is named
- GBP manager invite was received (or "no GBP" noted)
- Registrar is known (DNS access is sorted at launch via a delegate invite or a screen-share)

### 2.3 Chase-up if not submitted
| When | Channel | Message |
|---|---|---|
| +48h | SMS + email (GHL auto) | "Hi {{first_name}}, quick nudge: your onboarding form is the only thing between us and your kick-off. Takes about 20 min: {{link}}" |
| +96h | Owner calls personally | Offer to fill it out together on the phone (15 min) |
| +7 days | Email | Friendly note: the project is on hold until the form comes in, and the 21-day clock hasn't started yet |
| Weekly after | Email | Light touch, and log it in GHL |

The clock doesn't start until kick-off, so a slow form costs the client time, not Vanguard's guarantee.

---

## 3. Kick-off call (30 min, Zoom/phone, recorded with permission)

**This call starts the 21-day clock. Day 0 = kick-off date.**

**Prep (Owner, 15 min before):** read the form answers, look at their current site/GBP/competitors, and draft a sitemap and the 21-day dates.

| Min | Agenda |
|---|---|
| 0–3 | Welcome. Explain how the project works: Owner builds everything personally, one approver, email for approvals |
| 3–10 | Business deep-dive: ideal customer, top 3 services, what makes you different, why customers pick you, common questions/objections |
| 10–15 | Walk through the proposed sitemap (Foundation 5 pages / Full Presence 7–8 + booking, gallery, testimonials). Confirm pages |
| 15–19 | Design direction: review their 2–3 sites they like. Pick 3 style words. Confirm colors/logo. Photo plan (theirs, stock, or photo guide) |
| 19–23 | Tech: domain/registrar, GBP invite status, booking tool, where form leads should go |
| 23–28 | **Timeline:** read out the milestone dates (Section 4), plus the feedback rule: "You get 2 business days to respond to each review. If a reply is late, the launch date moves by the same number of days." |
| 28–30 | Next steps: Owner sends the kick-off confirmation email today. Client replies "Confirmed" |

**Done when:** call held, missing items listed, **Template B sent the same day** with all dates, and the client replied "Confirmed" (if they haven't replied by the next day, nudge them. Work starts either way).

---

## 4. The 21-day build timeline

Calendar days from kick-off (Day 0). Client review windows are **2 business days** (the "N" in the contract; the Owner may change it, but keep it consistent everywhere). Dates are written into the Template B email.

| Day | Milestone | Owner does | Client does | Done when |
|---|---|---|---|---|
| 0 | Kick-off | Call + confirmation email | Attends, confirms dates | Template B sent |
| 1–3 | **Sitemap + copy draft** | Writes all copy (per `vertical-site-conventions` for the niche), final sitemap | Sends any missing assets | Copy doc and sitemap shared |
| 4 | **Design direction** | Homepage design preview (desktop + mobile), built on the frontend-design approach | Reviews copy + design direction (2 business days) | Client replied: approve / changes / "missed the mark" (triggers Section 6) |
| 5–10 | **Build** | Builds all pages, forms, booking, GBP link, SEO basics on a staging URL (Netlify preview) | Nothing needed | All pages on staging |
| 11 | **Revision round 1 sent** | Sends staging link + feedback instructions (Template C) | Consolidated feedback in **one** email (2 business days) | Feedback received |
| 12–14 | R1 changes | Applies changes | — | Changes done |
| 15 | **Revision round 2 sent** | Sends updated staging (Template C) | Final feedback (2 business days) | Feedback received |
| 16–17 | R2 changes + **pre-launch QA** | Applies changes, runs the Section 5 checklist | Sends written launch approval | "Approved to launch" received |
| 18 | **Launch** | DNS, go-live, Section 7 checklist | Available for DNS help if needed | Site live on the domain, SSL on |
| 19–21 | **Buffer** | Absorbs slippage and handles the handoff session | Attends handoff | Handoff held |

**Buffer:** the plan targets launch on Day 18, which leaves 3 days of Owner-side buffer inside the guarantee. Don't spend the buffer on scope creep.

### How client delays pause the clock
- The clock pauses when a client deliverable is late: a review reply past its 2-business-day window, missing assets they committed to, a GBP/DNS action we're waiting on, or an unavailable approver.
- **Pause length = business days late.** The launch date and the guarantee date both move by the same amount.
- **Communicating it:** on the first late day, send Template D (delay notice) with the new launch date. Log it in GHL tagged `clock-paused` with the day count. Nothing is paused unless it's in writing.
- Owner-side delays (illness, overbooking) do **not** pause the clock. If the Owner misses the adjusted date, the **first Care Plan month is free**. Honor it without argument and tell the client before they have to ask.
- If a client goes silent for 10+ business days (estimate threshold), move the project to "On hold". Resuming gets a new launch date confirmed in writing.

---

## 5. Build standards checklist (the pre-launch QA gate)

Tick all of these before asking for launch approval.

**Mobile and speed**
- [ ] Designed mobile-first. Checked at about 375px, tablet and desktop, with no horizontal scroll
- [ ] PageSpeed Insights (mobile) run, and the score recorded in the project file. Fix large images and render-blocking assets. Aim for green; record the actual score and don't claim a number the test didn't show
- [ ] Images compressed/WebP, lazy-loaded below the fold

**Conversion**
- [ ] Click-to-call (`tel:`) button in the header and sticky on mobile
- [ ] Booking link/embed (Full Presence, or where the client has a booking tool) or a quote/contact form on every key page
- [ ] Contact form **tested end to end**: submission reaches the client's email (and GHL if connected), with a confirmation message shown
- [ ] Google Business Profile link / "Leave us a review" link / map embed
- [ ] Clear primary CTA above the fold on every page

**Local SEO basics**
- [ ] Unique title tag and meta description on every page (service + city)
- [ ] One H1 per page, logical H2/H3 structure
- [ ] **NAP** (name, address, phone) identical on the site, GBP and the footer
- [ ] `LocalBusiness` (or a more specific subtype, e.g. `HairSalon`, `Plumber`, `AutoRepair`) JSON-LD schema with NAP, hours, geo and URL. Validated in Google's Rich Results Test
- [ ] Service area pages/section name the real towns served
- [ ] XML sitemap + robots.txt. Submitted in Search Console (if the client grants access)

**Accessibility basics**
- [ ] Alt text on meaningful images
- [ ] Color contrast passes WCAG AA for body text and buttons
- [ ] Form fields have labels, keyboard navigation works, focus is visible
- [ ] Tap targets are big enough on mobile

**Tech and legal**
- [ ] Analytics installed (GA4 or the agreed tool), with a form-submit or call-click event if possible
- [ ] SSL active, and http→https and www/non-www redirects in place
- [ ] Favicon, social share image (OG tags)
- [ ] Privacy policy page (and terms if they collect data/bookings), linked in the footer. Use a template generator; this isn't legal advice
- [ ] Copyright year, business name correct, no lorem ipsum, no placeholder links
- [ ] Spell-check done. Prices/hours match what the client approved

**Done when:** every box is ticked and results are saved in the project file.

---

## 6. "Love It or We Fix It" process

**What triggers it:** at the **Day 4 design direction preview** (the first design preview), the client says the look and feel **missed the mark entirely**. This is different from normal revision notes like "change the blue", "move this section" or "different photo". Those go into R1/R2.

**Process**
1. Client says so in writing within the Day 4 review window.
2. Owner holds a 15-min call. Collect 2–3 new reference sites and new style words. Figure out what felt wrong.
3. Owner builds a **new visual direction** (a new layout, type and color approach, not tweaks) within 3 business days.
4. The client reviews it in the normal 2-business-day window. From here the normal R1/R2 process applies.

**Limits**
- **One reset per project.** It covers visual direction only, not scope, page count, copy strategy or features.
- It must be invoked at the first design preview, not after build or revisions.
- There's no charge, and the investment doesn't change. Launch moves by the days the reset takes; state the new date in writing. The 21-Day guarantee date moves too, because this is a client-requested redo. Say so kindly and clearly in the call and the email.
- If the second direction is also rejected, the Owner steps in personally (a call) to find a path. More resets are at the Owner's discretion. There are no refunds under this policy unless the contract says otherwise.

---

## 7. Launch checklist and handoff

### 7.1 Launch checklist (Day 18)
- [ ] Written launch approval from the approver
- [ ] **Backup** of the final build (git tag/commit + zip in the project folder). For the old site, save a copy/screenshot of any pages being replaced
- [ ] Production deploy (Netlify: `netlify deploy --prod`, or push to the production branch). See the `netlify-deploy` skill
- [ ] **DNS:** client adds Vanguard as a delegate/user at the registrar, **or** a 15-min screen-share where the client clicks. Set records (A/ALIAS/CNAME per host). Note the old records first so they can be rolled back
- [ ] SSL certificate issued. https works on the apex and www
- [ ] **Redirects:** map old site URLs to new pages (301s) so old links and Google results don't 404
- [ ] Every form re-tested on the **live** domain. Click-to-call tested from a phone
- [ ] Speed test re-run on the live URL, and the result recorded
- [ ] Analytics receiving live hits
- [ ] GBP website field updated to the new URL (via manager access)
- [ ] Search Console: property verified, sitemap submitted (if access granted)
- [ ] 24h later: DNS propagated, forms still arriving, no errors
- [ ] Send the launch email (Template E). Post in `#wins` "Site live: {{business}}" (manual)

**Done when:** all boxes are ticked and the site has been live and error-free for 24h.

### 7.2 Handoff session (30 min, within the Day 19–21 buffer)
| Min | Agenda |
|---|---|
| 0–5 | Walk through the live site on their phone |
| 5–15 | How to do basic updates (or how to request them), where form leads land, how to check the review link |
| 15–20 | Ownership: they own the domain, GBP and content. List of what's where (no passwords in the doc) |
| 20–27 | **Care Plan conversation** (Section 8) |
| 27–30 | Review + referral ask (Section 9), plus next steps |

**Done when:** session held, and a recap email sent with the "what's where" summary.

---

## 8. Care Plan conversion

### What's included monthly ($150–$250/mo, month-to-month, starts at launch)
- Hosting management
- Security updates and monitoring
- Regular backups
- Up to **1 hour** of content updates/month (swap photos, update hours/prices, add a service). Unused time doesn't roll over
- Priority response: 48-hour turnaround on requests
- Not included: new pages, redesigns, new features. Those are quoted (Section 10)

### Script (handoff session, about 5 minutes)
> "So the site's live and it's yours. Quick question: when your hours change, or you add a service, or you want to swap in new photos, who's going to handle that?"
>
> *(Let them answer. Usually "I don't know" or "I'd call you.")*
>
> "That's what most owners say. So we have the Care Plan. It's [$X] a month and it covers hosting, security, backups, and up to an hour of updates every month. You text or email me, and it's done within 48 hours. No contract, cancel any month. It's basically so you never have to think about the website again."
>
> "Want me to set that up starting today?"
>
> - **Yes:** "Great. I'll send the billing link now." (GHL recurring invoice. Tag `care-plan`.)
> - **"Let me think":** "Totally fine. I'll send a one-page summary. Any time in the next 30 days the setup is the same." (Follow up in 7 days.)
> - **No:** "No problem. If anything comes up, updates are available at [hourly/flat rate TBD by owner]." Log the reason.

If the 21-Day guarantee was missed, the first month is free. Say that up front: "Your first month is on us, as promised."

**Done when:** yes (billing active) or no (reason logged in GHL).

---

## 9. Post-launch: reviews, referrals, testimonials

| When | Action | Owner | Done when |
|---|---|---|---|
| Handoff session | Verbal referral ask: "Who else do you know who runs a business and is embarrassed by their website?" Get names or a warm intro | Owner | Asked, and names logged in GHL as referral leads |
| Launch + 7 days | Send the Google review request (Template F) with Vanguard's **own** GBP review link | Owner / GHL | Sent. Chase once at +5 days |
| Launch + 30–60 days | Testimonial / case-study check-in: "Has the site changed anything? New calls, bookings, fewer tire-kickers?" | Owner | Answer captured |

**Rules for testimonials and case studies**
- **Real results only.** Use the client's own words and numbers they can back up (calls, form fills, bookings from analytics/GHL). Never round up, estimate or invent.
- **Get written permission** (email is fine) before publishing their name, logo, screenshots or quotes. Store the permission email in GHL.
- Before/after screenshots are fine with permission. Don't imply outcomes the site didn't produce.
- No incentive in exchange for reviews (against Google's policy).

---

## 10. Scope control

**In scope:** the package bought (Foundation: 5 pages; Full Presence: 7–8 pages + booking integration, gallery, testimonials section), copy, design, SEO foundation, 2 revision rounds, one Love It or We Fix It reset, launch and handoff.

**Out of scope (quote separately):**
- Extra pages beyond the package: **[$TBD by owner] per page**
- E-commerce / online store, payments, memberships, customer logins
- Custom booking systems (we embed/link their existing tool)
- Logo design / full branding
- Professional photography or videography
- Ongoing SEO campaigns, ads, blog content, social media
- Copy in more than one language
- Migrating large volumes of old content (e.g. blog archives)
- Revision rounds beyond 2 (outside Care Plan): **[$TBD by owner]**
- Email hosting setup, and fixing registrar/GBP ownership disputes

**Change request process**
1. The client asks for something new. Owner replies: "Great idea. That's outside the current package. Here's the quote and how it affects the timeline."
2. A written quote with price and days added. The client approves and pays before work starts.
3. Added work either goes **after launch** (default, which protects the 21-day date) or extends the launch date by agreement in writing.
4. Log it in GHL. Small items (under 15 min, Owner's discretion) can be done free, once, and should be named as a courtesy.

---

## 11. Capacity (estimates, to be validated)

These are **estimates**, not measured data. Replace them with your real numbers after 5–10 builds (see "TBD: average turnaround" in `OFFER.md`).

- Estimated Owner build time per site: roughly 25–40 hours (Foundation) to 35–55 hours (Full Presence), plus calls and admin. **Estimate.**
- With sales calls also on the Owner's calendar, a realistic load is about **3–4 active builds at once, staggered** so kick-offs are about 5–7 days apart and launch weeks don't overlap. **Estimate.**
- Never start more than **2 kick-offs in the same week** (estimate), because design-direction days and launch days pile up.
- Care Plan clients take time too (up to 1 hr/client/month). Count them against capacity as they grow.

**When at capacity**
1. Keep accepting payments only if you can give a kick-off date **within 10 business days** (estimate threshold). Otherwise…
2. **Waitlist:** offer the next open kick-off date in writing before they pay. The 21-day clock starts at kick-off, so the guarantee is safe.
3. **Tell the setters** in Discord (`#scripts-and-docs` or a pinned post in `#wins`): "Next kick-off slot: [date]." Setters say "Our next build slot opens [date]." Don't invent scarcity; only say it when it's true.
4. Review capacity every Monday: active builds, their day numbers, the next open slot.

---

## 12. Client email templates

Merge fields use GHL syntax. Replace [brackets] before sending.

### A. Welcome (auto, on payment)
**Subject:** Welcome to Vanguard. Your site starts here

Hi {{contact.first_name}},

Thank you! Your payment is in and your 21-Day Authority Website is officially underway.

**Step 1 (about 20–30 min):** fill out your onboarding form: [form link]
Upload your logo and photos, tell us about your services, and add us as a manager on your Google Business Profile (steps are in the form). **We'll never ask for your passwords.**

**Step 2:** book your 30-min kick-off call: [calendar link]. Your 21-day timeline starts on that call.

Questions? Just reply here.

[Owner name], Vanguard

### B. Kick-off confirmation (same day as kick-off)
**Subject:** Your launch timeline: {{contact.company_name}}

Hi {{contact.first_name}},

Great call today. Here's what we agreed:

**Pages:** [list]
**Approver:** [name]
**Still needed from you:** [items + due date]

**Your timeline**
- Copy + design direction to review: [Day 4 date]
- Revision round 1: [Day 11 date]
- Revision round 2: [Day 15 date]
- Launch: [Day 18 date] (guarantee date: [Day 21 date])

Each review has a **2-business-day** reply window. If a reply comes in late, the launch and guarantee dates move by the same number of days. I'll always confirm any change by email.

Please reply **"Confirmed"** so we're locked in.

[Owner name]

### C. Revision request
**Subject:** Round [1/2] ready for your review: reply by [date]

Hi {{contact.first_name}},

Your site is ready to review: [staging link]

Please look at it on your **phone and computer**, then send **one email** with all your changes by **[date, 2 business days]**. Helpful format:
- Page, then section, then what to change

This is round [1 of 2]. [If round 2: "After this round we move to final checks and launch."]

[Owner name]

### D. Delay notice
**Subject:** Quick update on your launch date

Hi {{contact.first_name}},

We're still waiting on [feedback on round 1 / photos / the GBP invite / DNS step], which was due [date]. To keep things fair, your timeline pauses while we wait. Your launch date is now **[new date]**, and your guarantee date moves to **[new date]**.

As soon as I have [item], I'll pick right back up. Just reply here or call me at [phone] if I can make it easier.

[Owner name]

*(Owner-side delay version: "That's on me, not you. Your new date is [date]. [If past guarantee date:] As promised, your first month of the Care Plan is free.")*

### E. Launch
**Subject:** You're live! {{contact.company_name}} is online

Hi {{contact.first_name}},

Your new site is live: [URL]

Try it: tap the call button, send yourself a test through the form, and share the link with your team.

Next up is our 30-min handoff session on **[date/time]**. I'll show you how everything works and where your leads show up.

Congratulations. It's a great-looking site.

[Owner name]

### F. Review request (launch + 7 days)
**Subject:** Quick favor?

Hi {{contact.first_name}},

It's been a week since launch. I hope the new site is already making you proud to share it.

If you were happy with how the project went, would you leave a quick Google review? It helps a small shop like mine a lot: [Vanguard Google review link]

And if anything isn't right, reply here first and I'll fix it.

Thank you!
[Owner name]
