# 05 — Objections & Gatekeepers (YouTube + Instagram slice)

Scope: objections specific to selling websites to US local businesses (salons, barbers, gyms, trades, auto, pet, restaurants) with no/weak website, plus honest gatekeeper handling. Offer context: Vanguard setter books a 15–30 min demo/fit call with the owner-closer; demo site already built; ~$2,000 one-time, upfront, live within 14 days of kick-off.

## How this was researched (read first)

- **YouTube metadata** (title, channel) was verified for every video via the oEmbed endpoint. Upload dates and descriptions came from the rendered watch page through a reader proxy, or from yt-dlp `info.json`.
- **Transcripts** are YouTube auto-captions. A parallel research task had already saved them in this session's scratchpad (`scratchpad/demo-first-yt/txt/`). Direct caption download from this sandbox was bot-blocked, so videos marked "no transcript" below are cited only by title, chapters and description, and their handlers are labelled **paraphrase/chapter-level**.
- **Quoting rules.** Quotes are copied from those caption files. Auto-captions have small errors such as missing punctuation and misheard words, and I left them uncorrected. "//" marks a change of speaker.
- **Instagram did not work.** Profiles returned a login wall or "Please wait a few minutes" (rate limit), and search engines don't index reel captions. Only one Instagram fact was verified: @abouxtoure's profile page metadata ("140K Followers, 745 Following, 16 Posts"). Several of these creators point to Instagram from their YouTube descriptions (Abou Toure, Pavlo @pavels_life, Danyyil Giba @danyyilgiba, Jeremy Miner @jeremyleeminer). **No Instagram reel captions are quoted here.**
- One public Google Doc was read in full: Kai Stone's "full cold call script", linked from his video description.

---

## 1. Verified sources

| # | Title | Creator (channel) | Date | URL | What I could read |
|---|---|---|---|---|---|
| 1 | How To Book 3+ Web Design Meetings Per Day [Live Cold Calling] | Abou Toure | 2025-06-30 | https://www.youtube.com/watch?v=VXOSVmvwV0c | Full auto-transcript (live calls: not interested, send link, price, busy) |
| 2 | How To Get Web Design Clients With Cold Calling (Proven Script) | Abou Toure | (date not captured) | https://www.youtube.com/watch?v=alvCIWw-KCM | Full auto-transcript (script + "show don't tell" rationale) |
| 3 | How To Respond To The 6 Most Common Web Design Objections | Abou Toure | 2025-09-11 | https://www.youtube.com/watch?v=FJvxl_TlchI | **No transcript.** Chapters only: "Cold call: not interested", "Cold call: existing website", "Cold call: asking for price", "Sales call: cheaper options / need to think / too busy" |
| 4 | How i book 3-5 meetings a day Cold Calling ($319,000/month web design agency - full script) | Kai Stone | 2026-02-23 | https://www.youtube.com/watch?v=tU52nLIUz8Y | Full auto-transcript, linked Google Doc script, and comments (several comments call out the lying) |
| 5 | How to Book 3+ Meetings a Day Web Design Cold Calling (Proven Script) | Spencer Reist | 2024-10-03 | https://www.youtube.com/watch?v=-POaWp9_UaM | Full auto-transcript (word of mouth, "never pitch the gatekeeper", honest SEO promise) |
| 6 | How i book 3-5 meetings a day (selling websites cold calling) | Pavlo | 2026-01-21 | https://www.youtube.com/watch?v=0ezv6zRdM7c | Full auto-transcript (word of mouth, already have site, send it, busy) |
| 7 | Watch Me Cold Call LIVE & Get Rejected 😂 1 meeting booked :( | Pavlo | 2026-01-14 | https://www.youtube.com/watch?v=6Neolinn5JY | Full auto-transcript (includes a **lie to a gatekeeper**; see Avoid list) |
| 8 | Watch me book 3-5 meetings a day (web design cold calling) | Pavlo | 2024-02-16 | https://www.youtube.com/watch?v=kmp4iFCf8Jo | Full auto-transcript (already has someone building, price ask, business partner) |
| 9 | How I book 3-5 meetings a day (web design cold calling) | Samuel Darby | 2024-06-27 | https://www.youtube.com/watch?v=jtzYca5x0RY | Full auto-transcript (no-obligation framing, "send it to your own guy", busy) |
| 10 | I Cold Called 25 Local Businesses (web design cold calling) | Max Ross | 2024-08-12 | https://www.youtube.com/watch?v=Iex1weHMhE4 | Full auto-transcript (owner check, "not the one", "tried a website before", busy) |
| 11 | watch me earn $1,000+ in 5 minutes selling websites… (Live Cold Call) | Sean Cahill | 2026-07-20 | https://www.youtube.com/watch?v=o2QjKG5aKhs | Full auto-transcript ("what makes you think I need a website?", busy after a 12-hour day) |
| 12 | Watch Me Sell $750 Websites LIVE (Unfiltered Cold Calls) | Sean Cahill | 2026-05-01 | https://www.youtube.com/watch?v=Hf8urpy3GCU | Full auto-transcript ("someone's working on it", price, "what company are you with?") |
| 13 | Watch Me FAIL Cold Calls Live (Selling Websites + AI Receptionist) | Danyyil Giba | 2026-05-27 | https://www.youtube.com/watch?v=lTchl4s_oNE | Full auto-transcript (honest "this is a sales call" opener, word of mouth, front desk) |
| 14 | Live cold calling for web design (uncut) | JustLikeDrew | 2025-12-12 | https://www.youtube.com/watch?v=Qae8DdnFlaM | Full auto-transcript (honest answer to a gatekeeper's "who/what company") |
| 15 | How i book 3-5 meetings a day (cold calling SMMA) | Thomas Gonnet | 2022-09-24 | https://www.youtube.com/watch?v=PzUQLSyVOQU | Full auto-transcript (honest "this is a cold call" opener and honest gatekeeper ask). Local-marketing agency, not web design |
| 16 | Cold Call Masterclass: The Perfect Script (With LIVE Calls to Prove It) | 30 Minutes to President's Club (Armand Farrokh & Nick Cegelski) | 2026-01-20 | https://www.youtube.com/watch?v=2vivv2HeiBU | Full auto-transcript ("not interested" handler, permission opener) |
| 17 | How to Cold Call Busy People and Actually Get the Meeting \| Ask Jeb Blount | Sales Gravy (Jeb Blount) | 2026-04-29 | https://www.youtube.com/watch?v=9UmgG25bmDI | Full auto-transcript (home-services owners: "busy", "how much", "is this advertising?") |
| 18 | How to Get Past The Gatekeeper (Cold Calling) | 30 Minutes to President's Club | 2024-08-30 | https://www.youtube.com/watch?v=ThE3yXiNX4o | **No transcript.** Description/chapters: "The Job of a Gatekeeper", "Mistakes Salespeople Make with Gatekeepers", "The Triple Bypass Technique" |
| 19 | Wondering what to say on a cold call for a website design client? Here's the goal! | Build That Agency (Adam McLaughlin) | 2023-12-26 (premiered) | https://www.youtube.com/watch?v=hAAxvZCX0lI | Full auto-transcript (lead with a free evaluation; borrow credibility honestly) |
| 20 | Sales objection: "Where did you get my number?" | Cognism (Morgan J Ingram & David Bentham) | 2023-04-05 | https://www.youtube.com/watch?v=OIBmAYsuy44 | **No transcript.** Description only |
| 21 | Josh Braun's Exact Cold Calling Script (+ 7 objection responses) | Chris Bussing | 2026-05-06 | https://www.youtube.com/watch?v=fwyxBrj4m-8 | **No transcript.** Chapters incl. "How to respond to 'How did you get my number?'", "Objection response: 'I'm too busy'", "'Call me later this week'" |
| 22 | We Already Have A Company for that Objection | Jeremy Miner | (date not captured) | https://www.youtube.com/watch?v=p1WAMpdX23w | **No transcript.** Description + chapters ("Neutral questioning techniques", "The two-truths question") |

Supporting document: Kai Stone's script (Google Doc linked from #4): https://docs.google.com/document/d/1b47QX3gtSYZxHDXTwAHHtx3HSpOPDtcBz9O9R9eNykk. It was read in full and contains both handlers and deceptive tactics.

Also verified, but no wording extracted: Sell Better "10 Most Common Cold Call Objections" (2024-12-13, https://www.youtube.com/watch?v=-m_pMr52b6M), 30MPC "The 5 Data-Backed Cold Call Scripts…" (2026-03-24, https://www.youtube.com/watch?v=TJdNyztb2gU), Self-Made Web Designer "Sales Objections Every Web Designer Will Hear" (2025-05-27, https://www.youtube.com/watch?v=uKJ696doJO4), Trent Dressel "3 ways to overcome 'I'm not interested…'" (2023-09-14, https://www.youtube.com/watch?v=VH1DBC6n42Q).

---

## 2. Objection handlers

Format for each objection: the best handlers found, with the source number from the table, and then a **proposed Vanguard handler**. Every proposed handler stays honest, follows the setter price policy, and goes back to booking the demo/fit call with the owner.

Pattern across the web-design creators: they don't argue on the cold call. They acknowledge, give one reason, re-offer a **no-obligation look at something already built**, and book a short screen-share. Kai Stone (#4) says it outright: "the entire point of that cold call is not to try to sell them the website… All you're trying to do is sell the Zoom call."

### 2.1 "I don't need a website — I get all my business from word of mouth / Facebook / Instagram / my Google listing"

Handlers found:
- **Spencer Reist (#5).** He asks about capacity and builds on the reviews the owner already has: "are most of your jobs right now just coming from word of mouth or… // yeah pretty much… // …and I'm assuming you're able to take on more jobs though right // yeah that's my my plan… so this yeah the website we can definitely help you get get some more jobs on Google and you have a great Foundation because you have seven five star reviews".
- **Max Ross (#10).** Referrals look you up before they call: "if you are growing off referrals quite a lot I mean the first thing they will check out is that website and that obviously like some of them for sure they'll just get your number but I mean it does help".
- **Sean Cahill (#11)**, answering "what makes you think that I need a website?" He first checks capacity ("could you use the additional customers?"), then: "it makes you appear not only like more legitimate… builds immediate trust with with photos and honestly can even justify higher pricing… It would also allow customers that do not want to pick up the phone… to book a quote with you via your website."
- **Kai Stone's doc (#4)**, on "we already have enough business": "the reason (your service) still works is because it allows you to charge more for the same service you're already doing… If you're already turning away business you can now quote the overflow you get at a higher price". On the live call, when an owner asks who looks online for a plumber, he answers with a search scenario: "the first thing you're going to do is go on Google and type in like air condition repair near me… If you don't pop up, then you don't get the business".
- **Abou Toure (#2)** gives the framing rather than a rebuttal: "business owners don't need a website. What they need is more money, more clients, better leads… So you have to be the one to demonstrate that to them… You want to show you don't want to tell."
- When it works and when it doesn't. In Pavlo (#6) the owner answers "Like most of our clients… do word of mouth" with "No, I'm okay" and still books after a no-cost "just see it" re-offer. In Max Ross (#10) and Danyyil Giba (#13), owners who were truly booked out ("I've got work… until next March"; "I've been around for 17 years. I don't advertise… It's word of mouth.") were let go politely, and both creators say pushing a genuinely full business is wasted time.

**Proposed Vanguard handler:**
> "That makes total sense. Word of mouth is the best kind of customer, and honestly most of the owners we talk to say the same thing. Can I ask, if someone gets your name from a friend, what do they find when they look you up? Right now it's your [Google listing / Facebook page]. All we did was build the next step: a simple site with your photos, services and hours, and a button to [book / call / request a quote], so those referrals land somewhere that looks as good as your work. It's already built, and seeing it costs nothing. [Owner name] can walk you through it in 15 minutes. Would early tomorrow or after you close be better?"
>
> If they say they're fully booked: "Love that. Then this might be more about charging what you're worth than getting more volume. Want to take a look anyway, no pressure? If not, no problem at all." (One soft re-offer, then let them go.)

Don't claim "you're losing $X a month". See the Avoid list.

### 2.2 "We already have a website" / "my nephew (son, buddy) does it" / "someone's working on it"

Handlers found:
- **Samuel Darby (#9)**, to an owner whose guy is already on it: "it's completely free… you could always take some of those ideas and send it to your own guy if you wanted to… if you got somebody already it's absolutely fine".
- **Pavlo (#8).** The owner says his site is being made. Pavlo asks to show his anyway ("do you even want to look at what I built for you… I just have to show you on Zoom") and books it. Then he asks out of curiosity what the current company charges. He tells viewers this is "probably not the best lead… since he is a Price Shopper and he already has someone building a website".
- **Sean Cahill (#12)**, to "we have somebody currently working on it": he says he already built one and "I would love to have the opportunity to at least show it to you. If you don't like it, no problem at all." He also claims "I probably could offer you a much better price… the website is probably even better than whoever you have working on it". That is a comparison he can't back up, and Vanguard shouldn't copy it.
- **Abou Toure (#3)** has a chapter called "Cold call: existing website". No transcript was available, so its wording isn't known.
- **Jeremy Miner (#22)**, "We Already Have A Company for that": the chapters mention neutral questioning and "The two-truths question". No transcript, so no wording.
- No video transcript in this set had a specific "my nephew built it" handler. The general rule from these videos applies: respect the current person, and offer a side-by-side look with no obligation.

**Proposed Vanguard handler:**
> "Oh nice, then you're ahead of most shops I call. Out of curiosity, is it live, and is it getting you calls or bookings? … Totally fair. Your nephew obviously knows your business, so no knock on him at all. We'd already built a version for you before I called, so there's nothing to lose by seeing it side by side. If his is better, great, keep it. If you see something you like, you can even pass the ideas along to him. It's a 15-minute look with [owner name]. Is [day] morning or afternoon better?"
>
> If the site is new and actively being built, and they clearly aren't open to it: "Got it. I'll leave you alone then. Mind if we check back in a few months?" Log it and move on.

### 2.3 "How much?" (apply the setter price policy exactly)

Handlers found:
- **Jeb Blount (#17).** He advises against leading with the bare word "depends" ("it feels like you're arguing with them") and suggests: "That's a very good question and it's one that I… expected you to ask. And that's exactly why I want to get together with you in an appointment… so that I can learn a little bit more about your business, understand your goals, and then I can tailor a package… How about we get together on Thursday?"
- **Abou Toure's beginner, Johnny (#1).** On the first ask he answers with a broad, honest range and then books: "it really does depend on the page, but… that's the thing we're going to be also talking about as soon as you see the website. 200 to 5,000".
- **Samuel Darby (#9)** gives a plain ballpark with the payment terms: "they start from like £399… for like a simple five-page site… half up front half at the end". He also confirms "if I don't like it I ain't going to buy it // no of course you don't have to pay".
- **Kai Stone's doc (#4)** uses "5th grade math", comparing the price with the value of one job. That's useful for the closer, not the setter. His "if I can't get you at least one job a year… I'd probably just go play in traffic" is a joke that works like a guarantee. Avoid it.

**Proposed Vanguard handler (follows the policy):**
> First ask: "Fair question. It depends on what you'd actually want on the site. Quick one so I don't guess: would you want people to be able to book or request a quote online, or mostly just find your info and call?" → Then go back to booking: "That's exactly what [owner name] will tailor on the call."
>
> Second ask: "Totally fair. Most of our builds land around two thousand, one-time, and the demo itself is free. [Owner name] will show you exactly what's included for yours. Does [day/time] work?"
>
> Never: exact quotes, discounts, "special price", payment plans, or "I can get you a deal". If they push a third time: "Honestly, that's the most accurate number I can give without guessing. The 15 minutes with [owner name] is where you get a real number."

### 2.4 "What's the catch?" / "Is this a scam?"

Handlers found:
- **Kai Stone (#4)** names the catch outright. The owner says "Free ain't nothing free in this world", and Kai answers: "I get it. So, I will I will say there's a catch. So, if if I show it to you and you do like it… the whole website build is free, but we obviously would still have to charge you like hosting and stuff." (Disclosing the catch is the good part. The "web design student / school thing" cover story around it is not; see Avoid.)
- **Kai Stone (#4)**, on scam fear: "a lot of these guys are just some nerd in their mom's basement who like are trying to scam you. I get it." Then he offers a short no-obligation look ("you don't have to like buy it or anything").
- **JustLikeDrew (#14)** answers with verifiable identity: "Me and my brother, we make websites for contractors who don't have one… It's called Winston Web Works. You can search it up."
- **Sean Cahill (#12)**, to "what company are you with?": "I actually run my own business here in Tampa… I'm a private website designer. My name is Sean Cahill. You can look me up".
- **JustLikeDrew (#14)**, in commentary: prospects often won't click a Loom link "because they think you're like a scammer… people don't really trust links". That's one reason to show the demo live on the call rather than text a cold link.
- **Jeb Blount (#17)** on "is this advertising?": "you would say, yes, it is. But it's a little bit different than what you have typically experienced". Own the sales call. (The "juicy stat" he then makes up on the spot in the roleplay is not something to copy; see Avoid.)

**Proposed Vanguard handler:**
> "Good question, and I'd ask the same thing. Here's the honest version: the demo is free, and you're under zero obligation. We build it first because it's easier to show you than to describe it. If you like it and want it live, that's a paid build, usually around two thousand one-time, and [owner name] goes through all of that on the call. If you don't like it, you just say no. I'm [first name] with Vanguard, a small web design shop. You can look us up at [domain]. Want to see it [day] at [time]?"

(This combines Kai Stone's "there's a catch" transparency, Sean Cahill and JustLikeDrew's verifiable identity, and the price policy. Mentioning the price here is allowed because it answers "what's the catch" truthfully.)

### 2.5 "Just send it to me" / "Text me the link" / "Email me"

Handlers found:
- **Abou Toure (#1)**: "Ah, I really wish I could do that, but it's actually like hosted on my laptop since it's not published yet… so the only way we'll be able to do that is like I just share my screen". **Pavlo (#6)** uses the same move ("it is like on my computer… I can't launch a website for you"). Both work on the call, but if a shareable preview exists, the line is false. See the Avoid list.
- **Samuel Darby (#9)** offers a lighter version: "I can send you a WhatsApp with the website that we did… you don't need to do anything". To someone who's busy, he follows the message with a short video call: "it takes 5 minutes on a video call to show you the design".
- **Spencer Reist (#5)**: when an owner's spouse said "send it to my husband's email", he simply took the email. Low pressure, but no meeting was booked.
- **Build That Agency (#19)** turns the email into the follow-up: "what's the best email address for me to send your free evaluation… that obviously allows you to follow up with them later".
- **Sell Better (gaCfPXsHAU4)** has a 2024 short on "send me an email": "three things you can do". Verified title, no transcript.

**Proposed Vanguard handler (honest version of the screen-share push):**
> "Happy to. I'll text you a screenshot right now so you know it's real. The reason we do a quick screen-share instead of just a link is that [owner name] walks you through it and changes things live, like your photos and which services go first. A link on its own doesn't show you much. It's 15 minutes. Want me to text you the screenshot and lock in [day] at [time] at the same time?"
>
> If they insist on a link only: send what Vanguard's policy allows, and still propose a time ("I'll put a tentative 15 minutes on [day] in the text. Just reply 'no' if it doesn't work.").

Decision for the team: is the live demo URL shared before the call, yes or no? Setters must not claim it "can't be sent" if it can.

### 2.6 "I'm busy" / "Call me later"

Handlers found:
- **Jeb Blount (#17)**, coaching a rep who calls home-services owners: "I figured you'd be busy. I mean, in your business, why wouldn't you be? That's why I called. I want to find another time that's more convenient for you." His diagnosis: "when someone says I'm busy, they're overwhelmed right now… They're not thinking about next Thursday." He also recommends calling trades early (start "around 7:00"), because owners on a roof default to "How much does it cost?" to get you off the phone.
- **Pavlo (#6)** books a tentative slot and confirms on the day: "I'll just book you in for Friday, and then on Friday, I'll call you and see if that time is still good. If not, we can then reschedule".
- **Abou Toure (#1)** offers two days, then does a commitment check: "Tuesday or Wednesday?… Does it work before 12 or after 12?" and "I've spent quite a bit of time working on this website, so I just want to confirm that you're sure you can make it at noon so we don't waste each other's time".
- **Max Ross (#10)** on not pushing: "when they genuinely have something coming on pushing is the worst thing to do".
- **Chris Bussing**: short "I'm Busy! I'm Running To A Meeting!" (https://www.youtube.com/watch?v=IIR3ja131BQ, 2023-09-13). Verified title, no transcript.

**Proposed Vanguard handler:**
> "Totally get it, I figured you'd be slammed, that's on me. I won't keep you. It's a 15-minute look at the site we built you, with [owner name]. Is early better, like 7:30 before you open, or after close around 6? … Great, I'll text you a confirmation now. Anything that would stop you making [time]?"

(Two time options, a text confirmation, and a gentle commitment check. Use Abou's "I've spent time on this" line only because it's true: Vanguard does build the demo before dialing.)

### 2.7 "Not interested"

Handlers found:
- **Abou Toure (#1)**: "I totally hear you. And most my clients say the exact same thing before they actually see the website… Like I said, it's already built. If you have 5 10 minutes… I'll just share my screen… If you like it, we can publish it. If you don't, I'll go kick rocks."
- **30MPC, Armand Farrokh (#16)**: "Shoot. This one's totally on me… I guess you probably would have reached out to me if you had been interested. just so nobody from my team bugs you again. Is it… that you already have [X]? Or is it that [the problem] isn't happening… or is it that you you just hate getting cold calls and it's it's okay if that's the case?"
- **Max Ross (#10)**, in commentary: "he can say he's not interested but he had no idea what I was going to say… it's just about how you frame the tonality so you don't sound… like you're trying to sell something".
- **Danyyil Giba (#13)**: after a no, he takes one "last thing" shot at curiosity, then accepts the no gracefully.

**Proposed Vanguard handler:**
> "Fair enough, and I appreciate you being straight with me. Can I ask, so I don't waste your time again: is it that you're happy with how customers find you now, that you've got someone on the website side already, or that you just hate these calls? (Totally fine if it's that.)" → If there's an opening: "Makes sense. It's already built, so it's a no-pressure 15 minutes. If it's not for you, I'll leave you alone." → If it's a firm no: "Got it. I'll make sure we don't call again. Have a good one." (Then actually mark them do-not-call.)

### 2.8 "How did you get my number?"

Handlers found:
- No transcript in this set had a clean handler. **Cognism (#20)** and **Chris Bussing's Josh Braun breakdown (#21)** each have a dedicated segment, but no transcript was available, so their wording isn't quoted.
- The honest answer in our case is factual. Every creator above sources leads from public listings: Google Maps / Google Business Profile (Abou Toure #2, Max Ross #10, Samuel Darby #9) or Facebook (JustLikeDrew #14: "I saw you guys on Facebook. I noticed you didn't have a website").
- The **negative example** is Kai Stone's invented referral ("my mom's friend Julie Becker referred me"). Its point is to dodge this exact question. See Avoid.

**Proposed Vanguard handler:**
> "It's the number on your [Google listing / Facebook page]. That's actually how we found you: great reviews, but no website showing up. That's why we built the demo. If you'd rather I not call this number, just say so and I'll take it off our list."

Compliance note (my addition, not from the sources): dial manually, honor do-not-call requests right away, and keep an internal DNC list. Many small-business numbers are owners' cell phones, so have counsel confirm TCPA and state rules before using any autodialer or texting.

### 2.9 "I tried a website before and it didn't bring anything"

Handlers found:
- **Max Ross (#10)**. The owner said "I used to have the website I never got any more custom from that website", and Max answered with the referral-validation point: "if you are growing off referrals quite a lot… the first thing they will check out is that website… it does help". He also suggested the old site may not have been set up well ("that might be just because it wasn't [ranking] very well" is partly garbled in the captions).
- **Payton Clark Smith ("Cold Calling To Sell Websites Live", https://www.youtube.com/watch?v=u7JBvYR2UKI, 2026-04-22)** asks a diagnostic question about the old site: "Before this got hacked, was your website working pretty well for you?"
- **Build That Agency (#19)** suggests reviewing what's actually working: "worst case scenario I waste a little bit of time but you find out that everything's working well for you best case scenario… we see some opportunities for improvement".

**Proposed Vanguard handler:**
> "That's really common, and fair. A lot of sites just sit there. Can I ask what it was missing? Was it showing up on Google, could people book or call from it, was it kept up to date? … That's exactly what [owner name] looks at. The demo we built is set up around [your Google reviews / a book-or-call button]. If it doesn't look better than what you had, you've lost 15 minutes. Does [day/time] work?"

Never promise rankings or lead volumes. Spencer Reist (#5) models the honest version: "I don't want to make any false promises because to be honest a lot of it will come down to getting reviews".

### 2.10 "I need to talk to my partner / wife / husband"

Handlers found:
- **Pavlo (#8)**: the owner said "let me get my business partner… talk to him and then we'll meet", and Pavlo simply booked the time so the partner could join.
- **Spencer Reist (#5)**: a spouse answered and asked him to "send it to my husband's email". He took the email.
- **Sean Cahill (NBUdUZKN7Ts, 2026-05-04)**: the owner was in the car with his wife and asked for a call tomorrow; Sean booked "tomorrow… around 6:00 p.m." on the spot.

**Proposed Vanguard handler:**
> "Of course. It's their business too. Easiest thing is to have them on the call so nobody has to repeat it. When are you both usually free, early morning or evening? … Perfect. I'll text you both the link. What's their first name so [owner name] can greet them?"

---

## 3. Gatekeepers at small businesses (front desk, stylist answering the shop phone, spouse, office manager, answering service or AI)

What the sources show:
- **Don't pitch the gatekeeper.** Spencer Reist (#5): "I never I never pitch the gatekeeper". In practice he asks for the owner by first name, which he pulls from Google reviews or the listing, as Kai Stone's doc (#4) also suggests: "you can usually find their name in their google reviews". Danyyil Giba (#13) also says "normally I wouldn't really pitch the… front desk part".
- **Be honest about why you're calling.** Thomas Gonnet (#15), when the person who answered wasn't the owner: "this is… kind of a pitch for the owner um so maybe could I call later or do you have a maybe a phone number um I could call". The front desk then offered to pass along his name and number, and he gave a one-line reason.
- **Answer identity questions plainly.** JustLikeDrew (#14), asked "Let's start with your name and where you're calling from… What company?": "my name is Andrew… Me and my brother, we make websites for contractors who don't have one… It's called Winston Web Works. You can search it up."
- **Use a "this is a sales call" permission opener** once you reach someone who might be the owner. Thomas Gonnet (#15): "I'm gonna be honest with you this is a cold call so I do have something to pitch your business would you like to hang up now or give me 30 seconds". Danyyil Giba (#13): "This is actually a sales call. Do you want to hang up or give me 30 seconds?" Pavlo (#7): "I said this is a cold call. Do you want to give me 20 seconds to see what I have built?" 30MPC (#16) notes that this static opener is "getting more and more popular" and recommends leading with context first. For Vanguard the context is true: "I saw you on Google/Facebook and built you a site".
- **When it's not the decision-maker, don't pitch. Get the best time and move on.** Max Ross (#10): "I'm not going to waste my time speak to someone who's not going to be able to make a decision". Ask when the owner is reachable. In the Pavlo (#7) call, the receptionist offered "after lunch".
- **Timing for trades.** Jeb Blount (#17) recommends calling home services early, "around 7:00". Several creators note that small-business numbers are usually the owner's mobile: Max Ross (#10): "when the business is small enough… they're almost always mobes".
- **AI receptionists or answering services** are showing up more often (Danyyil Giba #13 reached two "office AI assistant" lines). Leave a short, honest message with your name, company and callback number; don't try to trick the bot.
- **30MPC gatekeeper video (#18)**: chapters only ("The Job of a Gatekeeper", "Mistakes Salespeople Make with Gatekeepers", "The Triple Bypass Technique"). The technique itself was not readable, so it isn't described here.

**Proposed Vanguard front-desk script (honest):**
> Gatekeeper: "Thanks for calling [Salon], this is Jess."
> Setter: "Hi Jess, this is [first name] with Vanguard. Is [owner first name] around?"
> Gatekeeper: "What's this regarding?"
> Setter: "Totally fair. I'm a web designer. We noticed [Salon] doesn't have a website, just the Google listing, so we built a free demo version for [owner]. It's a quick sales call, so no need to interrupt them. When's the best time to catch them, before you open or after close?"
> If they offer a message: "That'd be great. It's [name], Vanguard, [number]. The short version is we built [Salon] a free demo website and I'd love 15 minutes to show it to them. Could I also get the best time to call back? … Thanks, Jess, you're a lifesaver."
> Log the gatekeeper's name and the suggested time, and call back at that time. Greet the gatekeeper by name next time.

---

## 4. Avoid list (deceptive or non-compliant tactics seen in these sources)

| Tactic | Where seen | Why to avoid |
|---|---|---|
| **Invented referral**: "my mom's friend Julie Becker referred me… she said you did super high quality work" | Kai Stone, Google Doc script and live calls (#4). He admits: "You can argue if it's ethical or not" | It's a lie, and owners check. Top comments on the video: "If he's showing you he's willing to lie to a prospect, he's willing to lie to you"; "You don't need to deceive people to sell your services." One commenter suggests the honest version: "Just be straight up and tell them you're looking through businesses without a site" |
| **Fake reviewer referral**: "go look at their reviews on Google and just say, 'Hey, this person sent me your number'" | Kai Stone (#4), suggested as the alternative | Same problem: it attributes a referral to a real customer who never gave one |
| **False persona / cover story**: "I just graduated college… web design student… part of like a school thing" while running a claimed $319K/mo agency | Kai Stone (#4) | Misrepresents who's calling and why it's free |
| **Lying to a gatekeeper**: asked "what is this in reference to?", answered "I'm filing a complaint." | Pavlo, live call (#7) | Outright deception of staff. It damages trust with the owner and can create complaints |
| **Pretext about the listing**: "you guys are still open, right? It said closed for some reason" / "I checked last night it said closed", repeated across several businesses | Pavlo (#6, #7) | Says only if actually true for that listing. A scripted false claim is deceptive |
| **"It's only on my laptop, I can't send a link"** when a preview could be shared | Abou Toure (#1), Pavlo (#6) | Fine only if literally true. Otherwise give the real reason (a walkthrough is better) and offer a screenshot |
| **Saying "I already built it" before building it**: "you're going to reach out to the prospect first and then you're going to make the wireframe just in case they don't answer" | Abou Toure (#2) | Vanguard builds the demo before dialing. Keep it that way so the hook is always true |
| **Implied familiarity or claims you can't back up**: "Have you heard my name tossed around?"; trainers note "It does not matter if they've heard your name"; "we just completed a website for a company down your road" said to every lead; "I've built websites for numerous business around you"; "my girlfriends… get their nails done at your shop" | 30MPC (#16); Samuel Darby (#9); Sean Cahill (#12) | Use social proof only when it's real and specific to Vanguard (a real client in that niche or area). Never use made-up local proof or invented personal connections |
| **Invented stats**: "Give me a juicy stat… 25% higher profit jobs" made up in a roleplay | Jeb Blount roleplay (#17) | No made-up lift, revenue or "you're losing $X" claims. Use only verified Vanguard client results |
| **Implied guarantees / overpromising**: "If I can't get you at least one job a year… I'd probably just go play in traffic"; "guarantee at least 15 prepaid… appointments… or your money back" | Kai Stone doc (#4); Thomas Gonnet (#15) | Setters must not promise results, rankings or refunds. Model it on Spencer Reist: "I don't want to make any false promises" |
| **Price games**: "I probably could offer you a much better price… better than whoever you have"; "Normally… 300 bucks a month… I'll give it to you for 197"; leading with "25% discount" | Sean Cahill (#12); GHL Wizard (rMiN2321J6s); Abou Toure warns against discounts (#2) | Against the setter policy: no discounts, no exact quotes, no "special pricing" |
| **Fake urgency or guilt**: "I already canceled my date with my girlfriend… You're more important to me" | Pavlo (#6), joking | Even as a joke it's manufactured pressure. Avoid |
| **Pretext notification**: "We get notified anytime like a site gets broken or hacked… that's why I reached out" | Payton Clark Smith (u7JBvYR2UKI) | Use only if Vanguard actually has such monitoring. Otherwise say "I came across your site and it looks like it's down" |
| **Ignoring a clear no / no DNC**: "you keep calling until they tell you they're not interested or tell you to go play in traffic" (5–11 callbacks) | Kai Stone doc (#4) | Follow-up is fine; after an explicit "don't call", stop and log DNC |

---

### Gaps / caveats
- Instagram content could not be read (login wall and rate limit). No reel wording is included.
- Several of the best-titled trainer videos had no transcript (30MPC gatekeeper, Cognism "where did you get my number", Josh Braun breakdown, Jeremy Miner, Abou Toure's "6 objections"). They are cited only at the chapter level. If someone can open them in a browser, the "existing website", "how did you get my number" and gatekeeper segments are worth transcribing.
- All quotes come from auto-captions and may contain transcription errors.
