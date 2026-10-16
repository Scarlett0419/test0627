# 02 — YouTube: the "build the demo first" / spec-website cold-call method

Research date: 2026-10-15. Scope: YouTube creators teaching "build a sample site for a business before contacting it, then use it as the hook" (mainly cold calls; some DMs, Facebook posts and WhatsApp), plus written scripts by the same creators.

**How things were verified**
- Every YouTube video was checked through the YouTube oEmbed endpoint and/or the watch page (`ytInitialData`: title, channel, date, views, description, chapters).
- Transcripts are YouTube auto-captions pulled as VTT and converted to text. The auto-captions contain small transcription errors (for example "Reloom" for Relume, "Indie" for Indianapolis). Lines in quotation marks below are copied from those captions. Lines marked *(paraphrase)* come from chapters, descriptions or a third-party summary (videohighlight.com) and are not verbatim.
- Some transcripts could not be retrieved because YouTube returned HTTP 429 or a bot check; those sources are marked "metadata only". Reddit could not be reached from this environment (blocked to both the fetcher and the search tool), so no Reddit threads are included. View counts were captured on 2026-10-15.

---

## 1. Verified sources

| # | Creator / channel | Title | URL | Date | Views | What I could read | Demo-first? |
|---|---|---|---|---|---|---|---|
| 1 | Pavlo | Watch me book 3-5 meetings a day (web design cold calling) | https://www.youtube.com/watch?v=kmp4iFCf8Jo | 2024-02-16 | 352K | Full transcript + description | Yes. "Already built", shown only on Zoom |
| 2 | Pavlo | How i book 3-5 meetings a day (selling websites cold calling) | https://www.youtube.com/watch?v=0ezv6zRdM7c | 2026-01-21 | 42K | Full transcript + chapters | Yes ("talking website"), shown only on Zoom |
| 3 | Pavlo | Sell AI Websites To Local Businesses (Copy Me) | https://www.youtube.com/watch?v=WWCzZ56VAT4 | 2025-01-04 | 303K | Chapters + third-party summary (no transcript) | Partly: builds after a reply, free homepage |
| 4 | Spencer Reist | How to Book 3+ Meetings a Day Web Design Cold Calling (Proven Script) | https://www.youtube.com/watch?v=-POaWp9_UaM | 2024-10 | 85K | Full transcript | Yes, booked as a video call |
| 5 | Abou Toure | How To Book 3+ Web Design Meetings Per Day [Live Cold Calling] | https://www.youtube.com/watch?v=VXOSVmvwV0c | 2025-06-30 | 105K | Full transcript | Yes, shown only on screen-share |
| 6 | Abou Toure | How To Get Web Design Clients With Cold Calling (Proven Script) | https://www.youtube.com/watch?v=alvCIWw-KCM | date not captured (429) | n/a | Full transcript | Yes: Relume mockup, but "reach out first, then make the wireframe" |
| 7 | Abou Toure | Sell AI Websites To Local Businesses In 2026 (Full Course) | https://www.youtube.com/watch?v=H4dNdlzVGnw | 2025-05-09 | 285K | Chapters + third-party summary | Yes (mockups via Relume; IG DMs + calls) |
| 8 | Kai Stone | How i book 3-5 meetings a day Cold Calling ($319,000/month web design agency - full script) | https://www.youtube.com/watch?v=tU52nLIUz8Y | 2026-02-23 | 312K | Full transcript + **linked Google Doc script** (read in full) | Yes: a GoHighLevel template swapped per lead |
| 9 | Sean Cahill | the best Cold Call you've ever seen (selling $1000+ AI websites like candy) | https://www.youtube.com/watch?v=NBUdUZKN7Ts | 2026-05-04 | 31K | Full transcript + chapters | Claims "already built" but builds it **after** the call |
| 10 | Sean Cahill | Watch Me Sell $750 Websites LIVE (Unfiltered Cold Calls) | https://www.youtube.com/watch?v=Hf8urpy3GCU | date not captured | n/a | Full transcript | Same; says on camera the sites are "not yet created" |
| 11 | Goutham Scales | From Cold Call to Client in 10min (Web Design) | https://www.youtube.com/watch?v=M2YdKnjrC1M | 2026-04-13 | 2.8K | Full transcript | Claims "rebuilt", admits "which I was [lying]" |
| 12 | GHL Wizard | Watch Me Book 5–7 Meetings a Day (AI Demo Cold Calling) | https://www.youtube.com/watch?v=rMiN2321J6s | 2026-03-22 | 5K | Full transcript + chapters | Yes. Texts the demo **during** the call |
| 13 | Highlevel Haris | How Many Ai Websites Can I Sell in 100 Cold Calls? (HOLY) | https://www.youtube.com/watch?v=DQJGqH6uogk | date not captured | n/a | Full transcript | Claims "built", explicitly builds only after interest (UK) |
| 14 | JustLikeDrew | Live cold calling for web design (uncut) | https://www.youtube.com/watch?v=Qae8DdnFlaM | date not captured | n/a | Full transcript | Yes. **Sends the preview first**, skips Zoom |
| 15 | Max Ross | I Cold Called 25 Local Businesses (web design cold calling) | https://www.youtube.com/watch?v=Iex1weHMhE4 | 2024-08-12 | 31K | Full transcript | Builds **with permission** ("no strings attached") (UK) |
| 16 | Samuel Darby | How I book 3-5 meetings a day (web design cold calling) | https://www.youtube.com/watch?v=jtzYca5x0RY | 2024-06-27 | n/a | Full transcript | Offers a "free design" (Figma) shown on a video call (UK) |
| 17 | Cameron Jeanes | I Started Getting Web Design Clients When I Did This.. (best cold outreach strategy) | https://www.youtube.com/watch?v=coq11ZnucH4 | 2024-10-20 | 59K | **Metadata only** (chapters: "Providing value first", "The new outreach script", "The free mockup process", "Closing the deal") | Yes, per chapters |
| 18 | Adam Erhart | I Give Local Businesses a Free Website. Then They Pay Me $297/Mo | https://www.youtube.com/watch?v=EJ8sQIBEwRk | 2026-09-11 | 111K | **Metadata only** (chapters incl. "The Exact Facebook Post…", "The Exact Delivery Message That Sets Up the Sale", "The Cold Message That Turns Outreach Into a 'Gift'", "3 Mistakes That Can Kill This Strategy") | Yes: free site, then $297/mo |
| 19 | Payton Clark Smith | Cold Calling To Sell Websites Live | https://www.youtube.com/watch?v=u7JBvYR2UKI | 2026-04-22 | n/a | Full transcript (short) | No: "your site looks broken/hacked" angle (cited in the Avoid list only) |
| 20 | Efeturi | LIVE: 19-year-old's first time cold calling (selling AI websites) | https://www.youtube.com/watch?v=Mya5hu8YLNo | 2026-05-26 | 755 | Full transcript | Offers to build free "to get testimonials" (UK) |
| W1 | Kai Stone (written) | "FULL COLD CALL SCRIPT" Google Doc linked from #8 | https://docs.google.com/document/d/1b47QX3gtSYZxHDXTwAHHtx3HSpOPDtcBz9O9R9eNykk/edit | n/a | n/a | Full text | Written version of #8 |
| W2 | SiteSeeker (vendor blog, not a YouTuber) | Cold Call Script for Web Design: Word for Word, With Objections | https://siteseeker.ai/blog/cold-call-script-web-design | updated 2026-09-27 | n/a | Page read via fetch | Preview-first, texted during the call |

Context: the US is the main market for most of these creators. Sources 13, 15 and 16 are UK calls, and Pavlo calls US numbers from abroad using local numbers bought in GoHighLevel. Most creators earn affiliate commission on GoHighLevel, which is worth remembering when weighing their claims.

---

## 2. Per-source notes

### 1. Pavlo: "Watch me book 3-5 meetings a day" (kmp4iFCf8Jo)
- **Structure:** confirm the business → "are you open?" pattern interrupt plus "didn't see a website" → "I built you a beautiful website… if you like it you can keep it" → "is that something you would even want to look at?" → refuse to send it and book a Zoom → (sometimes) a quick price comparison → lock a time.
- **Opener (verbatim):** "okay cool yeah I just I wasn't sure if uh you guys were open it it said closed for some reason I I didn't see a website or anything you guys are still like open and and doing service calls right"
- **Demo framing (verbatim):** "I actually built you guys a a beautiful website if if I do say so myself uh if you like it you can you can keep it is that something you would you would even want to look at"
- **When asked "you already have it built?" (verbatim):** "yes sir I have the homepage built uh I didn't build out the rest of the site I believe in giving value first so I could show you the homepage and then if you like it we could we could maybe um you know work together"
- **"Send it to me" (verbatim):** "well it's not live like it's not on it's not online um it's I have it here on my computer so if you want I could just share my screen and show you on Zoom"
- **Price (verbatim, to a price shopper):** "ours is 150 and it's it's done in a day"
- **Booking (verbatim):** "it'd be better if we just book it in and we could jump on Zoom and I'll just show you cuz it's not live obviously"
- **Claimed result:** four meetings booked "in a few hours" in this video. He says he never leaves voicemails because an automation follows up by text and voicemail.
- **Flags:** He uses "it said closed for some reason" on almost every call. Nothing on screen shows the listings were actually marked closed, so it reads as a scripted pretext. He also sends automatic SMS to anyone who doesn't pick up (TCPA consent risk; see the Avoid list).

### 2. Pavlo: "How i book 3-5 meetings a day (selling websites cold calling)" (0ezv6zRdM7c)
- Same skeleton, with a "talking website" (AI chat/booking) as the demo. **Verbatim:** "I actually built you guys a talking website. It's basically ready to book appointments and I could take a lot of these calls, too. Is that is I mean is that something you would even want to see?"
- **Pushback, then re-ask (verbatim):** "I gotcha. I mean, like I said, it's already done. I mean, do you want to just see it?"
- **"Send it" (verbatim):** "it is like on my computer, though. So like obviously I'm not I can't launch a website for you. So really the best way to do it is if if I just showed you on Zoom"
- **Booking tactic:** proposes "Friday at like 3:00 pm", then says "Let's just schedule something and then if we have to reschedule it, I'll call you the same day."
- The description lists the objections he handles: "I'm winding down", "we already have a website", "send me a sample", "I'm driving", "I'm moving locations" *(from the description)*.
- **Flag:** He again uses "closed when I tried to look you up" as an opener, and again relies on automatic SMS and voicemail follow-up.

### 3. Pavlo: "Sell AI Websites To Local Businesses (Copy Me)" (WWCzZ56VAT4)
- No transcript, so everything here is *(paraphrase)* from videohighlight's summary and the chapters. He advises waiting for a reply before building, and opening by offering to fix issues on the current site rather than pitching a new one. He shows the owner a draft homepage filled with sample content and their reviews, and prices a "copy-paste" site at about $150/mo hosting with a free homepage, or $1,000–$6,000 upfront for a full build.
- This is useful as a contrast: the same creator builds on reply for some channels and claims "already built" on calls.

### 4. Spencer Reist: "How to Book 3+ Meetings a Day…" (-POaWp9_UaM)
- **Principles (verbatim):** "one I never I never pitch the gatekeeper two sound like a real person not a robot and three these guys are busy so typically I'll just jump straight into the offer"
- **Opener (verbatim):** "hey Victor this is Spencer um so the reason I'm calling I'm actually checking out your [business] here right now and I noticed you have some great reviews but didn't have a website so believe it or not I actually went ahead and built you a brand new beautiful website to help you get more jobs on Google and I was wondering if you had like 10 to 15 minutes tomorrow to jump on a quick video call to check it out"
- **Shorter variant (verbatim):** "I noticed you didn't have a website so I actually built you uh a brand new beautiful one I was wondering if you'd be open to jumping on like a quick 10minute video call tonight or tomorrow to check it out"
- **After the yes:** light discovery ("are most of your jobs right now just coming from word of mouth… I'm assuming you're able to take on more jobs though right"), then gets the email for the invite and adds "do you get text at this number… I'll remind you over text as well". He asks before texting.
- **Honesty moment (verbatim, when asked how fast he can get them to page one):** "I don't want to make any false promises because to be honest a lot of it will come down to getting reviews… I don't want to say like artificial ones because because Google cracks down on those"
- **One miss:** a prospect said "if you send it to my husband's email he can [look] at it". He took the email and the meeting didn't happen, which supports showing the demo on a call rather than sending it cold.

### 5. Abou Toure: "How To Book 3+ Web Design Meetings Per Day [Live Cold Calling]" (VXOSVmvwV0c)
- **Opener (verbatim):** "Hey, I'm located in South Calgary. I just found you guys on Google. Fantastic reviews, by the way. And I noticed you didn't have a website, so I just went ahead and built you one from scratch if you just have five 10 minutes to see it."
- **"Not interested" (verbatim):** "I totally hear you. And most my clients say the exact same thing before they actually see the website… Like I said, it's already built. If you have 5 10 minutes, even right now, I'll just share my screen, show it to you."
- **Framing (verbatim):** "Already fully built. I'll just show it to you. If you like it, we can publish it. If you don't, I'll go kick rocks."
- **"Can you send me the link?" (verbatim):** "Ah, I really wish I could do that, but it's actually like hosted on my laptop since it's not published yet. Um, so the only way we'll be able to do that is like I just share my screen and show it to you."
- **"What's the cost?" (beginner Johnny, verbatim):** "it really does depend on the page, but… that's the thing we're going to be also talking about as soon as you see the website. 200 to 5,000"
- **Show-up lock (verbatim):** "Just just a heads up. I've spent quite a bit of time working on this website, so I just want to confirm that you're sure you can make it at noon so we don't waste each other's time"
- **Flags:** In #6 he says the Relume mockup takes "30 seconds" to "5 minutes", so "spent quite a bit of time" overstates the effort. He also built the mockup in Relume, which gives a shareable link, so "hosted on my laptop" is a convenient excuse rather than the real reason he won't send it.

### 6. Abou Toure: "How To Get Web Design Clients With Cold Calling (Proven Script)" (alvCIWw-KCM)
- **Thesis (verbatim):** "You want to show you don't want to tell. So, what we're going to do is we're going to build a quick website mockup. It's only going to take 30 seconds and then we're going to reach out to the client and tell them that we already built them a website."
- **Why it works, in his words (verbatim):** "it demonstrates value immediately. So, you're leading with free work instead of leading with promises like, oh, I'll build you a free website, but that doesn't really mean much" … "it's going to make them curious because they want to see what you already created".
- **Script (verbatim):** "Hey, I just found you guys on Google. Phenomenal reviews by the way, and I noticed you didn't have a website. I just built you a completely new website from scratch. Do you maybe have 10, five minutes later in the day for me to show it to you? If you like it, fantastic. I'll go ahead and publish it for you. If not, no worries. I just want to show it to you."
- **Anti-pattern he names (verbatim):** the generic "I specialize in building custom professional websites… I actually have 25% discount on all my packages right now" opener "only works with desperate people".
- **Key admission (verbatim):** "by the way, you're going to reach out to the prospect first and then you're going to make the wireframe just in case they don't answer." In other words, he says "already built" before anything has been built.
- **Claimed:** "maybe… seven times more positive response rate" and "one out of three people who actually hop on sales call with you are actually going to end up buying". He also suggests outsourcing the build on Fiverr for "50 bucks" and charging about $500. His full objection doc is gated behind an Instagram DM.

### 7. Abou Toure: "Sell AI Websites To Local Businesses In 2026 (Full Course)" (H4dNdlzVGnw)
- *(Paraphrase, videohighlight summary)* He uses two channels, cold calls and Instagram DMs. For DMs: like three posts, follow, then send a friendly first message **"posing as a potential client"**, and prefer voice notes over text. He shares Relume concept links so the client can pick a version. Claimed: a $1,500 client signed via an IG DM.
- **Flag:** Opening a DM as a fake customer is deceptive. This comes from a third-party summary and is not verified against the transcript.

### 8. Kai Stone: "$319,000/month web design agency - full script" (tU52nLIUz8Y) + Google Doc (W1)
- **How the demo is made (verbatim):** "inside Go High Level… I would literally just come here and type plumber… I would just change out their business name, uh their phone number… and I would change out their location, and I would literally leave everything else pretty much the exact same… the product is already done for you"
- **Opener, live call (verbatim):** "my friend Julie Becker actually uh my mom's friend kind of gave me your number. She said you guys do like really good work, but you guys don't have like a website or anything like that. Is that Is that true?"
- **Demo framing (verbatim):** "I basically kind of graduated college and I'm starting like a web design agency. Uh actually, pretty much built you a whole website for free if you want to check it out." … "the website build is free. We'd probably just charge you uh anywhere from 97 to 200 bucks a month for hosting"
- **Written script (Doc, verbatim):** "Right now I'm doing (insert your service) for super cheap with the hopes I might be able to get a testimonial from you… do you mind if I build something out for you to take a look at?" The pricing answer in the Doc: "So I cover the cost of the monthly hosting and the domain name, right now I'm just charging between $97-$497 depending on how crazy you wanna get with it. If you have like 10 minutes today or tomorrow I could walk you through some of the work I've done and kinda just give you a little free audit of your business."
- **Booking (Doc, verbatim):** "Sweet! Even better than a call back let me just schedule into my calendar… Don't give them too many options… say 'How's "x time" today, I also have "x time open tomorrow", what works better for you?'" He follows with a commitment check: "besides the off chance there's a zombie apocalypse at 'x appointment time' would there be any reason you wouldn't show up?" Then he gives a reason to attend: "at the very least you can learn a little bit about your business from an advertising perspective + see what some of your competitors are doing".
- **Link timing:** On the call he asks for an email to "send you the link" or offers to text the Zoom join link, and offers to pull photos from the Google profile so the owner gets "a better idea of what it uh what it might look like". The demo itself is shown on Zoom. **Verbatim:** "The only thing you are trying to do with that cold call is to get them on the Zoom appointment… That's where you can send them a little bit of a video beforehand".
- **Claimed:** $319K MRR (he shows Stripe on screen), 3–5 meetings a day from 6–8 hours of dialing, and most closes come after 5–11 follow-ups. The Doc's setter KPIs are about 150 calls a day, 1–2 booked a day, and 3–5 of 5–10 weekly bookings showing up.
- **Flags:** The "Julie Becker" referral is invented. He admits it on camera (verbatim): "using that Julie Becker is a pattern interrupt… You can argue if it's ethical or not". His suggested alternative also misleads: "go look at their reviews on Google and just say, 'Hey, this person sent me your number'". The "web design student / part of like a school thing" persona is presented as a pretext. Free build plus hosting framing is fine only if true.

### 9–10. Sean Cahill (NBUdUZKN7Ts, Hf8urpy3GCU, also o2QjKG5aKhs)
- **Opener (verbatim, NBU):** "My name is um Shawn Cahill. I am a local website designer in the area, and just to keep it super quick with you. I don't want to waste your time or nothing. I I basically saw here on Google that you do not have a website. Is Is that correct?" Then: "So, I actually went ahead and built you guys a website. I use very very new and improved AI software…"
- **Price (verbatim):** "So the website would be around $750… that's a one-time fee but then we also offer services to manage the websites from a month-to-month basis which would essentially be around $100 to $200". He states the price directly when asked, and it is the one example in this set of an upfront price on the setter call.
- **Ownership question:** "I own the website after you create it, correct?" Answer: "Yeah it's your website."
- **Booking (verbatim):** "we'll do like a Google Meet or Zoom… I'll be able to share my screen with you and take you through the entire thing". This was in reply to the owner asking "do you want to… send it to me".
- **Flags:** The Hf8 intro says (verbatim) "we are going to be cold calling local businesses pitching them on websites that we have not yet created", yet on the calls he says "I actually built you guys a website". In NBU he says it took "nearly half a day's of work" and builds it on camera after the call. In Hf8 he claims "a few friends… they get their nails done at your shop" and "I've built websites for numerous business around you", neither of which can be checked.

### 11. Goutham Scales: "From Cold Call to Client in 10min" (M2YdKnjrC1M)
- **Opener (verbatim):** "can you give me like 20 seconds to let me know why I gave you a call?" … "I don't have anything to sell, but I've actually rebuilt your entire website totally for free. If you had like 5 minutes, I can show you the website. If you like it, you can keep it."
- **"Why free?" (verbatim):** "I'm just getting into the business and I'm trying to get some testimonials". He also offers to connect the domain so they "can have it for free". The owner then pushed on what was improved.
- **Admission (verbatim):** "No, I don't really build a website before the call. I just do that because I wanted to increase my booking rate and my show up rate… he thought I was lying, which I was". The owner booked a meeting 20 minutes out to test him.
- **Flags:** He invents an "already built" claim and opens with "I don't have anything to sell" while selling.

### 12. GHL Wizard: "AI Demo Cold Calling" (rMiN2321J6s)
- **Opener (verbatim):** "Hey, are you guys open right now? I'm looking online and it says you guys are closed." He only later says why he's calling.
- **Framing (verbatim):** "the reason I'm calling is because I basically built this AI agent… I'm not trying to sell you anything on this call… I'm just trying to give you a demo you can test."
- **Sends the demo during the call, with permission (verbatim):** "all I need… is either an email or a number that I can send this exact demo through". Owner: "this number works fine. We can take texts." Then: "go in, ask as if you're a customer… try to break it". He calls back after the owner opens it and offers a free setup ("I normally charge around $500 setup fee").
- His demo is a "self-selling" page with an embedded AI agent ("Maria") that pitches the owner.
- **Flags:** He opens as a would-be customer and says he's "not trying to sell you anything", though the call is a sales call.

### 13. Highlevel Haris: "100 Cold Calls" (DQJGqH6uogk), UK
- **Script (verbatim):** "Hey, how you doing?" [pause] … "I live locally in [location]… would it be cool for me to pop down after hours to show you guys in person what I built for you?" → "So I spent the last few days building this new smart website system for you, hooked up with some pretty cool tech because we're both local. Would you be against me coming down and showing you everything I built?"
- He explains why each part works: being local builds trust, the pauses mimic a real conversation, "spent the last few days" triggers reciprocity, and "would you be against" is hard to say yes to. He offers an in-person demo or WhatsApp.
- **Admission (verbatim):** "you cold call these guys without building anything… I'm going to cold call and say I built XY Z F, but I haven't built anything. If they actually show interest, then I'll build it."
- **Flag:** "Spent the last few days" and "built" are both fabricated by his own account.

### 14. JustLikeDrew: "Live cold calling for web design (uncut)" (Qae8DdnFlaM)
- **Preview-first, no Zoom (verbatim):** "I saw you guys on Facebook. I noticed you didn't have a website, so I actually made you one. I just want to know if I could send you that preview."
- **Reasoning, quoting ChatGPT on camera (verbatim):** "contractors hate Zoom calls. They're on job sites… [a] preview makes it real immediately. Zoom feels like a sales call, time commitment… It's slower."
- **Outcome:** Several flat "no"s in this uncut video. He says he gave up too quickly: "I should have objection handled him better." He mentions three follow-ups booked earlier, but the evidence is thin.

### 15. Max Ross: "I Cold Called 25 Local Businesses" (Iex1weHMhE4), UK, calling for a friend's agency
- **Permission-based framing (verbatim):** "I'm a business owner like yourself and at the moment we're actually creating free website designs for local businesses in [area] with no strings attached… I was curious if you'd be opposed if we built yourself a website a template for your business completely free of charge over the next few days and then what we can do is we can present it to you over a really quick call once we've built it out just to see what you think does that sound good"
- **Reassurance (verbatim):** "if you think it looks good great… if not then yeah you just you can just tell us it looks terrible… we'll go our separate ways"
- This is the honest version of the method: nothing is claimed as built until it is. Owners were polite ("that's very kind of you"), but bookings were low in the clip. He keeps the booking link open while dialing.

### 16. Samuel Darby: "How I book 3-5 meetings a day" (jtzYca5x0RY), UK
- **Opener (verbatim):** "you guys are still operating right… the reason I'm calling is we just completed a um website for company down your road called luxury law[ns] um and I wondered if you guys would be interested in a completely free design that we can send to you guys you guys can have a look if you like it you can keep it um and if not no harm done"
- **Delivery:** The design lives in Figma and is shown "on a video call for like 5 10 minutes". When asked to WhatsApp it, he offers to send the *finished nearby site* instead and keeps the new design for the call.
- His real local proof ("down your road") is the strongest honest credibility line in the set, provided it's true.

### 17. Cameron Jeanes (coq11ZnucH4): metadata only
- The chapters show a value-first outreach script, a "free mockup process" and "closing the deal". The transcript was blocked (429), so his wording and channel are unverified. Re-pull it before relying on this source.

### 18. Adam Erhart (EJ8sQIBEwRk): metadata only
- The chapters describe a **Facebook-post** route ("The Exact Facebook Post That Gets Business Owners to Raise Their Hand"), a build after the owner responds, a "Delivery Message That Sets Up the Sale", a cold message framed as a "gift", then a $297/mo upsell, plus "3 Mistakes That Can Kill This Strategy". The transcript was blocked. It is worth a re-pull because it is the clearest "free site → monthly plan" teaching from a large channel (111K views in about a month).

### W2. SiteSeeker blog (vendor; written)
- **Preview opener (quoted by fetch tool):** "I actually put together a quick preview of what a site for you could look like." … "Do you have thirty seconds?" Mid-call: "Can I text you a link to a preview?"
- It calls a live link texted during the call "the strongest thing you can offer". On compliance (quoted): "Only text after the owner says yes, and send it yourself from your own phone, one message at a time." On price: "If an owner asks 'how much?' and you hesitate, you lose credibility."

---

## 3. Script patterns for our offer (Vanguard: demo already built, $2,000 one-time, live in 14 days, optional $197/mo)

Our demo genuinely exists before the dial, so we can use the strongest lines in this set honestly. Each line below was adapted from the source cited after it.

### A. Openers (confirm → observation → built-it claim → small ask)
1. **Spencer-style, direct (#4):** "Hey, is this [Owner]? This is [Name] with Vanguard. I'm looking at [Business] on Google right now. Great reviews, but I noticed you don't have a website, so believe it or not we actually went ahead and built you one. Do you have 10 minutes tomorrow for a quick video call so I can show it to you?"
2. **Abou-style, with "go kick rocks" release (#5/#6):** "…I noticed you didn't have a website, so we built you one from scratch. If you like it, great, we'll talk about putting it live. If not, no worries, I'll go kick rocks." Keep the release line, which lowers pressure.
3. **Pavlo-style permission question (#1):** "…we actually built you a site, and honestly I think it looks great. Is that something you'd even want to look at?" "Do you even want to look?" invites a yes/no and is easy to say yes to.
4. **Honest "local proof" variant (#16):** "We just finished a site for [real nearby client], and I put one together for you too. Would you want to see it?" Use this only with a real, referenceable client.
5. **Reviews/GBP hook for no-site businesses (#4, #6, #9):** "I found you on Google Maps. [4.8 stars / 60 reviews] is great, but when someone taps your listing there's no website to land on." This is a factual observation. Pavlo's "it said closed" is not, unless the listing really says so.

### B. Demo-framing lines
- "Already fully built. I'll just show it to you." (#5)
- "I believe in giving value first, so I built the homepage. If you like it we could work together." (#1). Be precise about what's built (homepage vs full site).
- "If you like it, you can keep it." (#1, #11, #16) **Do not use as-is for Vanguard.** Our build is $2,000 paid upfront, so "keep it" would be misleading. Safer: "If you like it, we can talk about getting it live for you. If not, no hard feelings."
- "No strings attached… if you think it looks terrible, just tell us and we'll go our separate ways." (#15) This fits our offer honestly.
- Reason it exists (honest version): "We build a sample for local businesses we'd like to work with. It's faster to show you than to describe it." This replaces the testimonial / "student" pretexts in #8 and #11.

### C. "What's the catch / how much?"
- The sources split. **Deflect to the call:** Abou (#5): "that's the thing we're going to be also talking about as soon as you see the website" (then gave "200 to 5,000"). Kai Stone's Doc gives a **range plus a reason to meet**: "$97–$497… If you have like 10 minutes today or tomorrow I could walk you through…". **State it straight:** Sean Cahill (#9) gave "$750 one-time" plus $100–$200/mo, and the owner still booked. SiteSeeker (W2): hesitating "lose[s] credibility".
- **Recommendation for our setters:** answer plainly, then return to the booking. "No catch. The sample's free to look at. If you want it live, builds are typically around $2,000 one-time and go live within two weeks; [Owner/closer] walks you through exactly what's included on the call. Does tomorrow at 4 or Thursday at 10 work better?" Never say "free website" unqualified (see Avoid list).

### D. Booking asks
- Two-option close (Kai Stone Doc): "How's [time] today, or I also have [time] tomorrow. What works better?"
- Short and specific (#4/#5): "10-minute video call tonight or tomorrow?"
- Commitment check (Kai Stone Doc, #5): "Besides a zombie apocalypse, any reason you couldn't make [time]?" Abou's "I've spent quite a bit of time on this" works only if it's true.
- Logistics (#4): get the email for the invite, then **ask** "Do you get texts at this number? I'll send a reminder", and wait for the yes.
- Give a reason to show up (Kai Stone Doc): "At the very least you'll see what your competitors are doing online."
- "Send it to me" handling. Honest version for us: "Happy to send a link after we talk. It makes more sense with 10 minutes of context, and it's [Owner] who built it, so he can tweak things live. Can we lock in 10 minutes?" Don't claim it's "only on my laptop" if it's a hosted preview (see section 4).

---

## 4. Debate: send the demo link before or during the call, or show it only on the call?

| Position | Who | Argument / evidence |
|---|---|---|
| **Show only on a booked call (do not send)** | Pavlo (#1, #2), Abou Toure (#5), Spencer Reist (#4), Sean Cahill (#9/#10), Samuel Darby (#16), Goutham (#11), Kai Stone (#8) | The demo is the reason to book. Sending it removes the reason for the meeting. Every live "send it to me" request in Pavlo and Abou was turned into a Zoom booking with "it's not live / on my laptop". Spencer's one email-only lead ("send it to my husband's email") went nowhere in the clip. Kai Stone: "The only thing you are trying to do with that cold call is to get them on the Zoom appointment". This is the majority position by a wide margin, and the creators with the biggest audiences hold it. |
| **Send during the call, after a verbal yes, then call back** | GHL Wizard (#12), SiteSeeker (W2) | The demo "does the hard selling". The owner tests it live and the setter follows up while interest is hot. GHL Wizard got a callback where the owner said "it seems pretty cool". SiteSeeker calls a texted live link "the strongest thing you can offer" and requires the yes first. |
| **Send the preview instead of a meeting** | JustLikeDrew (#14) | Contractors are on job sites and "hate Zoom". A preview "makes it real immediately", while Zoom "feels like a sales call". The uncut video shows mostly refusals, so the evidence is weak. |
| **Send something adjacent, keep the demo for the call** | Samuel Darby (#16), Kai Stone Doc (W1) | Darby WhatsApps a *finished nearby site* as proof and keeps the new design for the call. Kai Stone sends a case study or selfie video right after booking as a "hook" and to cut no-shows. |

**Evidence quality:** Nobody gives controlled numbers. All of it is anecdotal, live-call footage or claims. The "show on call" camp has more on-camera bookings, but those are edited highlight reels except #5 and #14 (uncut). Some of the "it's on my laptop" excuses are false (Relume and GoHighLevel previews are shareable links), so part of this camp's success relies on a white lie.

**Suggested synthesis for Vanguard:**
1. **Default: show it on the booked call.** Our setter's job is the booking, and the closer is the builder, so the reveal should be his.
2. When an owner insists on seeing it now and won't book, **text a view-only link with permission, then lock the callback time on the same call.** Use a "what you'll see" message rather than a cold link. Don't invent a reason it can't be sent.
3. After booking, send a short confirmation (with consent): calendar invite, one screenshot or the business name in the hero image as a teaser, and the closer's name. Kai Stone and the no-show literature both say a pre-call touch lifts show rates.
4. Track it as a test: book rate and show rate for "show on call" vs. "send during call" by niche. Trades may lean toward sending (JustLikeDrew's argument). Salons and gyms may book more readily.

---

## 5. Avoid list (seen in these sources; do not copy)

1. **Saying "already built" when it isn't.** Abou Toure (#6: "reach out… first and then… make the wireframe"), Highlevel Haris (#13: "say I built XYZ but I haven't built anything"), Goutham (#11: "which I was [lying]") and Sean Cahill (#10: "websites that we have not yet created") all do this. Vanguard really does build first, so keep it that way: no demo, no "built" claim. Don't overstate the effort ("spent the last few days", "half a day") either.
2. **Fake referrals or fake relationships.** Kai Stone's "my mom's friend Julie Becker referred me" (he concedes "You can argue if it's ethical or not") and his alternative of naming a Google reviewer as the referrer. Sean Cahill's unverified "my friends get their nails done at your shop".
3. **Pretending to be a customer or inventing a problem.** GHL Wizard opens "are you guys open right now? I'm looking online and it says you guys are closed". Pavlo opens "it said closed for some reason" on nearly every call. Abou's DM method has you "pos[e] as a potential client" (per summary). Only say a listing shows "closed", "broken" or "hacked" if you actually saw it. Payton Clark Smith's "It looks like uh maybe it's disconnected or got hacked or something" (#19) happened to be true (the owner confirmed it), and his follow-on "we get notified anytime like a site gets broken or hacked" is an unverifiable claim. Never script it.
4. **"I'm not selling anything" / "I don't have anything to sell".** GHL Wizard and Goutham say this on what are sales calls.
5. **False personas.** "I just graduated college", "part of like a school thing", "trying to get testimonials" (Kai Stone, Goutham, Efeturi #20: "I'm just starting out. I'm trying to get some testimonials"). Our setters represent an agency, so say so.
6. **"Free website" / "if you like it you can keep it"** when the real price is $2,000 upfront. This misleads on price. Say "free to look at" instead.
7. **Unconsented automated texts and voicemails.** Pavlo's GoHighLevel workflow auto-texts and auto-voicemails everyone who doesn't answer. Under the US TCPA and state mini-TCPAs (e.g., Florida, Oklahoma), automated or marketing texts to mobile numbers need prior consent, and ringless or prerecorded voicemail is risky. Text only after a verbal yes on the call, sent manually (SiteSeeker W2 agrees). Scrub against the National DNC list and state lists. Many sole-trader business lines are personal cell phones.
8. **Caller ID games.** Pavlo buys local-area-code numbers to call the US from abroad. Local presence is legal if the caller ID is accurate and can be called back. Never spoof another business's number.
9. **Results promises.** Spencer Reist's own line is the model: "I don't want to make any false promises". Don't promise rankings, page-one placement or "more customers". Never suggest fake or "artificial" reviews.
10. **Fake scarcity.** Seen as discount-led openers ("25% discount on all my packages right now", which Abou calls weak) and pressure lines. Don't invent deadlines or "only 2 spots" claims.
11. **Over-promising "keep it" or domain hand-over** before terms exist. Settle ownership terms explicitly. The prospect in #9 asked "I own the website after you create it?", so the closer needs a clear answer.

---

### Gaps / follow-ups
- Transcripts for Cameron Jeanes (coq11ZnucH4), Adam Erhart (EJ8sQIBEwRk), Pavlo WWCzZ56VAT4/hA91LtOslDs and Abou H4dNdlzVGnw were blocked by YouTube rate limits. Re-pulling them would add the DM, Facebook and email versions of the method.
- Reddit (r/webdev, r/freelance, r/agency) could not be accessed from this environment.
- Upload dates were not captured for #6, #10, #13 and #14 (titles and channels are verified via oEmbed).
