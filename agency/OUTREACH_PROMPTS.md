# Vanguard — Outreach Automation Prompts

The daily jobs behind `Vanguard-Outreach-System.xlsx` (tab: Automations). Claude finds, reads, sorts and drafts; you approve and send. Nothing is sent, posted or connected on LinkedIn, Facebook or Reddit without you.

| ID | Job | When | Where it runs |
|---|---|---|---|
| A1 | Reddit leads digest (F5Bot → Outlook) | Daily, 7:45am | Claude Code scheduled task (cloud) with the Outlook (Mailbox) connector |
| A2 | LinkedIn inbox triage | Daily, 8:15am and 4:30pm | Claude in Chrome on your computer (logged into LinkedIn) |
| A3 | LinkedIn prospect finder | Weekdays, 9:15am | Claude in Chrome on your computer |
| A4 | Facebook groups & Messenger sweep | Daily, 10:00am | Claude in Chrome on your computer (logged into Facebook) |
| A5 | Cold email replies sweep | Daily, 8:30am and 4:30pm | Claude in Chrome on your computer (GoHighLevel Conversations, or your cold-email tool's unified inbox) |
| A6 | Weekly review | Fridays, 4:00pm | Any Claude chat — attach this workbook |

Replace anything in [brackets] before you schedule a prompt.

## A1 — Reddit leads digest (F5Bot → Outlook)

**When:** Daily, 7:45am  
**Where:** Claude Code scheduled task (cloud) with the Outlook (Mailbox) connector  
**Status:** Ready to schedule — needs your time zone

```text
You are my lead scout for Vanguard, a web studio that builds websites for US local businesses (about $2,000 one-time, live within 14 days of kick-off, free demo first).

1. Using the Outlook (Mailbox) connector, make ONE search_emails call: from "f5bot", since yesterday's date, limit 25. The mailbox is on a free plan of 5 calls per day, so use at most 3 more calls in total (read_email only when a preview has no post link). Never send, move or delete email.
2. From the alerts, collect every Reddit post or comment URL.
3. For each URL, fetch the post (try the URL with ".json" on the end, or old.reddit.com). Skip anything older than 72 hours, locked, or already answered by a hired designer.
4. Score each one 1–5 for buying intent: 5 = a business owner asking to hire someone to build a website now; 3 = asking for recommendations or prices; 1 = a developer, student, job seeker or general discussion.
5. For every post scoring 3+, draft a reply that leads with 2–3 genuinely useful tips for their situation, then one line: "If you want it done for you, I run a small web studio (Vanguard) and can mock up a free demo so you can judge it first." Check the subreddit's rules in the sidebar: if self-promotion is banned, draft a tips-only reply and say so.
6. Output a digest table, best first: score, subreddit, post title, link, age, what they need (one line), drafted reply. End with: "Post replies yourself after checking each thread."
Do not post anything to Reddit.
```

## A2 — LinkedIn inbox triage

**When:** Daily, 8:15am and 4:30pm  
**Where:** Claude in Chrome on your computer (logged into LinkedIn)  
**Status:** Paste into Claude in Chrome and set to repeat daily

```text
Open https://www.linkedin.com/messaging/ in a new tab. I run Vanguard, a web studio that builds websites for US local businesses (about $2,000 one-time, live within 14 days of kick-off, free demo first).

1. Open every conversation that is unread, or where the other person wrote last in the past 7 days.
2. For each one, classify the reply:
Reply types (pick one per conversation):
Interested · Price question · Send info · Wants demo · Not now · Has a website · Referral · Partner · Not interested · Opt-out · Auto-reply · Wrong person · Booked · Who are you
3. Draft my reply using the matching template from the Reply Playbook below, personalised with one detail from their message or profile. Keep it under 80 words, warm, no hard sell. If they want a demo, ask for their business name and any Google/Facebook/Instagram page.
4. Also check My Network → Invitations (list them, do not accept or decline) and Notifications for comments on my posts that need an answer.
5. Output a table: name, company, reply type, their last message (one line), my drafted reply, next stage, follow-up date.

Reply Playbook:
- Price question → "Fair question. It depends on what you need, but most of our builds land around $2,000, one-time, and the demo is free. Want me to put one together so you can see what you'd get?"
- Send info → share two portfolio links and offer a free demo for their business.
- Wants demo → ask for business name + any page; promise the demo within 48 hours, then book a 15-min walkthrough: [Calendly link].
- Not now → ask when to check back; set the follow-up date.
- Has a website → offer a free 3-point review, no pressure.
- Referral → thank them and ask for an intro.
- Not interested / Opt-out → one polite line, then mark Do-Not-Contact.

Rules: never send, post, comment, connect, accept or decline anything without my approval in this chat. Never invent facts about a prospect or about Vanguard. Prices: only the ballpark "most of our builds land around $2,000, one-time; the demo is free". Anyone who says stop / not interested / remove me goes on the Do-Not-Contact list and gets no further outreach.
```

## A3 — LinkedIn prospect finder

**When:** Weekdays, 9:15am  
**Where:** Claude in Chrome on your computer  
**Status:** Paste into Claude in Chrome and set to repeat on weekdays

```text
Find today's LinkedIn prospects for Vanguard (websites for US local businesses). Do not send any connection requests or messages.

Part A — buying signals (do first):
Search LinkedIn posts from the past 24 hours (Posts filter, sort by latest) for each of: "need a website", "looking for a web designer", "recommend a web designer", "website for my business", "anyone know a web developer". List posts by business owners or people asking on behalf of one. For each: author, link, what they need, and a drafted comment (helpful, mentions I can mock up a free demo) plus a drafted DM.

Part B — owners and referral partners (up to 15 people in total):
Search People with: titles Owner / Founder / Co-owner; company size 1–10; locations from my target list [CITIES]; industries: personal care, wellness and fitness, construction, automotive, restaurants, retail, pet services. Also find up to 5 referral partners in the same cities: bookkeepers, accountants, business coaches, photographers, print/sign shops, marketing freelancers who don't build websites.
Skip anyone I'm already connected with or have a pending invite to.
For each person: name, title, business, city, profile link, whether their business has a website (check the company page or a quick Google search), and one personalised first message to send after they accept (under 60 words, mentions one real detail, offers a free demo for owners or a referral swap for partners).

Output: two tables (A and B), ready for me to action. Rules: never send, post, comment, connect, accept or decline anything without my approval in this chat. Never invent facts about a prospect or about Vanguard. Prices: only the ballpark "most of our builds land around $2,000, one-time; the demo is free". Anyone who says stop / not interested / remove me goes on the Do-Not-Contact list and gets no further outreach.
```

## A4 — Facebook groups & Messenger sweep

**When:** Daily, 10:00am  
**Where:** Claude in Chrome on your computer (logged into Facebook)  
**Status:** Paste into Claude in Chrome and set to repeat daily

```text
Do my Facebook sweep for Vanguard (websites for US local businesses, about $2,000 one-time, free demo first). Do not post, comment, react, add friends or message anyone.

1. Messenger: open https://www.facebook.com/messages/ including Message Requests. For each unread thread or one where they wrote last, classify the reply:
Reply types (pick one per conversation):
Interested · Price question · Send info · Wants demo · Not now · Has a website · Referral · Partner · Not interested · Opt-out · Auto-reply · Wrong person · Booked · Who are you
and draft my response (under 80 words, uses the Reply Playbook in my spreadsheet: ballpark price only, offer the free demo, book with [Calendly link]).
2. Groups: open each group in my list [GROUP LINKS]. In each, search for posts from the last 48 hours containing: website, web designer, web developer, recommend, anyone know, need a site. Read the group rules once and note whether service offers are allowed.
3. For each post where someone needs a website or asks for a recommendation: group, author, link, what they need, a drafted public comment (helpful, says who I am, offers a free demo) and a drafted follow-up DM. Only draft a DM where they asked publicly or invited DMs.
4. List up to 10 other posts by local business owners where a genuinely helpful comment would fit (questions about getting more customers, Google reviews, booking, marketing), with a drafted comment that gives value and does not pitch.

Output three tables: Messenger replies, Website requests, Value comments. Rules: never send, post, comment, connect, accept or decline anything without my approval in this chat. Never invent facts about a prospect or about Vanguard. Prices: only the ballpark "most of our builds land around $2,000, one-time; the demo is free". Anyone who says stop / not interested / remove me goes on the Do-Not-Contact list and gets no further outreach.
```

## A5 — Cold email replies sweep

**When:** Daily, 8:30am and 4:30pm  
**Where:** Claude in Chrome on your computer (GoHighLevel Conversations, or your cold-email tool's unified inbox)  
**Status:** Paste into Claude in Chrome once your sending tool is live

```text
Open my cold-email inbox ([GHL Conversations URL or cold-email tool unibox URL]) in a new tab. Look at every reply received since the last sweep.

1. Classify each reply:
Reply types (pick one per conversation):
Interested · Price question · Send info · Wants demo · Not now · Has a website · Referral · Partner · Not interested · Opt-out · Auto-reply · Wrong person · Booked · Who are you
2. Draft my reply for each (under 80 words) using the Reply Playbook: ballpark price only, demo link + Calendly link for interested replies, polite one-liner for no.
3. Opt-outs ("stop", "remove me", "unsubscribe", angry replies): do not draft a reply; list them so I can add them to the suppression list today.
4. Auto-replies: note the return date as the next follow-up date.
5. Output a table: sender, business, reply type, one-line summary, drafted reply, next stage, follow-up date. Also report today's numbers if the tool shows them: sent, opens if tracked, replies, bounces.
Rules: never send, post, comment, connect, accept or decline anything without my approval in this chat. Never invent facts about a prospect or about Vanguard. Prices: only the ballpark "most of our builds land around $2,000, one-time; the demo is free". Anyone who says stop / not interested / remove me goes on the Do-Not-Contact list and gets no further outreach.
```

## A6 — Weekly review

**When:** Fridays, 4:00pm  
**Where:** Any Claude chat — attach this workbook  
**Status:** Run manually each Friday

```text
Attached is my Vanguard outreach workbook. Review this week:
1. From 'Daily Log', total each activity for this week and compare with 'Daily KPIs' targets. Which channels and days fell short?
2. From 'Lead Tracker', count leads by stage and by channel, list every OVERDUE follow-up, and list conversations that went quiet for 5+ days.
3. Compare actual conversion rates (conversations per touch, calls per conversation) with the planning assumptions in 'Funnel Math'. Say which assumptions to change and to what.
4. Give me the 3 changes for next week that would most likely add booked calls, ranked, and anything I should stop doing.
Keep it under 300 words plus the tables.
```
