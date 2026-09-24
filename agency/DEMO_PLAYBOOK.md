# Vanguard Demo Playbook
## How to Use the Prospect Demo in the Sales Process

---

## 1. When to Build the Demo

**Build the demo BEFORE the first cold call — not after.**

The demo is a pattern interrupt. It replaces "we build great websites" with "we already built yours." That sentence only lands if the page exists before the setter picks up the phone. Building it after contact is made loses the surprise entirely.

**The exact timing:**
- Setter researches the prospect (5–10 min)
- Setter generates the demo using `generate_demo.py`
- Setter uploads and gets the live URL (see Section 4)
- Setter dials — demo URL ready to send mid-call (by text only if they say yes to a text, otherwise email)
- If the prospect doesn't pick up: send the URL in the voicemail follow-up **email** (no cold texts — see SETTER_SCRIPT.md)

Do not build demos in bulk and blast them. Build one targeted demo per qualified prospect. If the prospect doesn't meet your ICP (wrong industry, too small, already has a good site), skip the demo and dial with a standard pitch.

---

## 2. What to Research Before Building

You need five things. All five are findable in under 10 minutes using only public sources.

### Business Name
Obvious — but confirm the exact trading name from their Google Business Profile (GBP), not a directory listing that may be outdated.

### Industry
Pick from: `beauty`, `fitness`, `faith`, `construction`, or `other`. Match to the closest preset so the tone and design language fit.

### Tagline
Check in order:
1. Their existing website hero section
2. Their GBP description
3. Their Instagram/Facebook bio
4. Their Yelp listing intro

If none exists, leave `--tagline` blank — the industry preset fills in a strong default.

### Phone Number
Pull from GBP. That's the number the setter will call — it belongs in the footer.

### Services
Check:
1. Their website's services or menu page
2. Their GBP "Services" tab (many local businesses fill this in)
3. Their Instagram highlights (beauty/fitness businesses often list services there)
4. Yelp or StyleSeat listings for beauty; Mindbody for fitness

Aim for 4–8 services. Fewer than 4 looks thin; more than 8 makes the grid messy.

### Location / City
City + state is enough. Pull from GBP.

### Booking URL
Default is the Vanguard Calendly link (`--booking_url`). This is intentional — the CTA books a call with Vanguard, not with the prospect's business. That's the conversion event.

---

## 3. How to Host the Demo

Choose one method. All three work.

### Option A: Netlify Drop (Recommended — free, instant, professional URL)
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag and drop the `.html` file
3. Netlify gives you a URL like `random-name-123456.netlify.app`
4. Optional: rename it via the Netlify dashboard to something like `glow-beauty-demo.netlify.app`
5. Share that URL on the call

Pros: instant, no account needed for a drop, HTTPS by default, loads fast.
Cons: the random URL is ugly unless you rename it (free account rename is available).

### Option B: GitHub Pages (Best for teams managing multiple demos)
1. Create a GitHub repo called `vanguard-demos` (private)
2. Enable GitHub Pages on the `main` branch from `/docs` folder
3. Save each demo as `docs/{slug}_demo.html`
4. URL: `https://yourorg.github.io/vanguard-demos/{slug}_demo.html`

Pros: version controlled, team access, professional subdomain.
Cons: slight setup overhead.

### Option C: Email the File Directly
For prospects who are already warm (responded to an outreach) or small operations where a link feels too slick:
1. Attach the `.html` file to an email
2. Subject: `We built a demo site for [Business Name]`
3. Body: keep it to 2 sentences (see Section 5)

Pros: zero hosting needed.
Cons: some email clients block `.html` attachments; the prospect must download and open it.

---

## 4. How the Setter References It on the Cold Call

The demo is a hook, not a presentation. The setter's job is to get curiosity, not to explain the whole website.

**Script framework:**

> "Hey [Name], this is [Setter] from Vanguard — quick question for you. We came across [Business Name] online and noticed your current site and we actually put together a quick demo of what a new version could look like for you. I wanted to see if [Owner Name] had 30 seconds to take a look at it."

If they ask what it is:
> "It's a live webpage — want me to text you the link right now while we're talking? It's just a free mockup, takes 10 seconds to open."

If they say they're busy / not interested:
> "Totally get it. It's already built, so it'd be a shame for it to go to waste — can I email or text you the link so you can look whenever?"

*(Only send it if they say yes, by the channel they chose. Log SMS consent in the CRM.)*

**Key rules for setters:**
- Never say "we'd like to build you a website" — say "we already built you a demo"
- With their OK, send the URL during the call, not after — keeps them on the line
- The goal of the call is to book the consultation, not to pitch the demo
- Do not spend more than 60 seconds describing the demo on the cold call

**Follow-up text format** (only after they said yes to a text):
> "Hey [Name] — [Setter] from Vanguard. Here's that demo site we built for [Business Name]: [URL]. Completely free, no strings. Happy to walk you through it on a quick call this week. Reply STOP to opt out."

---

## 5. How the Owner / Closer Uses It on the Consultation Call

By the time the prospect is on a consultation call, they've seen the demo. Use it as a reference point, not a surprise.

**Opening:**
> "You had a chance to look at the demo page we sent over — what was your first impression?"

Let them react. Do not jump in to sell.

**If they liked it:**
> "Good — that's actually built from a pretty simple set of inputs. What we'd do for your real site is take that same foundation and add [their specific need — booking integration, photo gallery, SEO, etc.]. Here's what that looks like in practice..."

**If they had notes or wanted changes:**
> "Perfect — that's exactly the kind of feedback we'd work through together. The demo is intentionally a starting point. Your actual site would reflect your brand, your photos, your exact services. Let me show you what we've done for similar businesses..."

**Key closer rules:**
- Pull up the demo on screen share at the start of the call — it's a shared anchor
- Use the demo to validate their taste, not to defend the design
- Always move from the demo to a real project within the first 5 minutes
- Do not let the consultation become a design critique session — redirect to outcomes

---

## 6. What NOT to Put in the Demo

### Do not use their real logo
You don't have permission. Using a business's logo without consent — even on a private demo — opens IP liability. The script intentionally uses text-only branding. If they want to see it with their logo, that's a step that happens after they engage.

### Do not make up testimonials or reviews
The demo has no stats bar unless you pass verified facts with `--highlights` (e.g. `"4.8★:Google rating,22:Years in Austin"` copied from their Google profile). Never guess numbers — a prospect who sees "500+ clients" on their own demo when they've served 80 knows instantly it's fake. Never add "Jane D. — 5 stars" style quotes.

### Do not use real client photos from their existing site
Pulling images from their current site for the demo is a copyright issue. The demo uses no images — clean type-and-grid layout only. If they want a photo-forward version, that's the proposal stage.

### Do not promise a specific design
The demo is a directional preview, not a mockup of their final site. Make that clear on the call. Say "this is a starting point" — never "this is what you'll get."

### Do not put competitor pricing in the demo
Do not add language like "websites like yours cost $X elsewhere." Keep the demo purely about the prospect, not about competitive framing.

### Do not use the prospect's real booking/checkout links
The CTA should always point to a Vanguard booking URL (Calendly or equivalent). Do not link to their existing booking system — that defeats the purpose of the demo.

### Do not send the demo to a gatekeeper
The demo is for the decision-maker (owner, founder, operator). If you only have a front desk contact, ask for the owner before sending. A gatekeeper who "passes it along" breaks the chain of context.

---

## 7. Quick Reference

| Step | Action | Time |
|------|--------|------|
| Research prospect | GBP, website, Instagram | 5–10 min |
| Generate demo | `python3 scripts/generate_demo.py --business_name ...` | 1 min |
| Host demo | Netlify Drop | 2 min |
| Setter dials | Reference demo on call, send URL mid-call (with OK) | Live |
| Follow-up | Email URL + 2-sentence message (text only with consent) | 1 min |
| Consultation | Open demo on screen share, redirect to project | 5 min |

---

*Vanguard — Internal Use Only*
