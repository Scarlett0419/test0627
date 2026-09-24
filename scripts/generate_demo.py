#!/usr/bin/env python3
"""
Vanguard Demo Site Generator
Generates a personalized demo HTML page for prospects before a sales call.

Usage:
    python generate_demo.py --business_name "Glow Beauty Studio" \
        --industry beauty \
        --tagline "Where beauty meets confidence" \
        --phone "(555) 123-4567" \
        --location "Austin, TX" \
        --services "Facials,Lash Extensions,Brow Tinting,Chemical Peels" \
        --booking_url "https://calendly.com/vanguard-agency" \
        --highlights "4.9★:Google rating,12:Years in Austin"

    --highlights is optional and must only contain facts verified from the
    prospect's own Google profile, site, or socials. Omit it and the trust bar
    is left out entirely.

    Or with JSON input:
    python generate_demo.py --json '{"business_name": "Iron Core Gym", ...}'
"""

import argparse
import json
import re
import sys
from html import escape
from pathlib import Path


# ─── Industry presets ────────────────────────────────────────────────────────

INDUSTRY_PRESETS = {
    "beauty": {
        "hero_adjectives": ["radiant", "flawless", "luminous"],
        "hero_verb": "Feel",
        "default_tagline": "Beauty that moves you.",
        "cta_text": "Book Your Session",
        "accent": "#c2885a",
        "bg_light": "#faf8f5",
        "icon_set": ["✦", "◆", "●"],
        "service_intro": "Treatments crafted for you",
    },
    "fitness": {
        "hero_adjectives": ["stronger", "faster", "unstoppable"],
        "hero_verb": "Get",
        "default_tagline": "Train harder. Live better.",
        "cta_text": "Start Training",
        "accent": "#d97706",
        "bg_light": "#fafaf8",
        "icon_set": ["▲", "◆", "●"],
        "service_intro": "Programs built to push limits",
    },
    "faith": {
        "hero_adjectives": ["community", "purpose", "hope"],
        "hero_verb": "Find",
        "default_tagline": "A place to belong.",
        "cta_text": "Join Us This Sunday",
        "accent": "#7c6d5a",
        "bg_light": "#faf9f7",
        "icon_set": ["✦", "◆", "○"],
        "service_intro": "Ministries & programs",
    },
    "construction": {
        "hero_adjectives": ["built right", "built to last", "built for you"],
        "hero_verb": "Get It",
        "default_tagline": "Quality you can stand on.",
        "cta_text": "Get a Free Quote",
        "accent": "#b45309",
        "bg_light": "#fafaf8",
        "icon_set": ["▲", "■", "◆"],
        "service_intro": "What we build",
    },
    "other": {
        "hero_adjectives": ["exceptional", "trusted", "results-driven"],
        "hero_verb": "Experience",
        "default_tagline": "Excellence delivered.",
        "cta_text": "Get in Touch",
        "accent": "#d97706",
        "bg_light": "#fafaf8",
        "icon_set": ["✦", "◆", "●"],
        "service_intro": "Our services",
    },
}


# ─── HTML generation ─────────────────────────────────────────────────────────

def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def render_services(services: list[str], accent: str, icon_set: list[str]) -> str:
    cards = []
    for i, svc in enumerate(services):
        icon = icon_set[i % len(icon_set)]
        card = f"""
        <div class="service-card">
          <span class="service-icon" style="color:{accent}">{icon}</span>
          <h3>{svc.strip()}</h3>
        </div>"""
        cards.append(card)
    return "\n".join(cards)


def render_trust_bar(highlights: list[tuple[str, str]]) -> str:
    if not highlights:
        return ""
    items = "\n".join(
        f"""        <div class="trust-item">
          <span class="trust-num">{num}</span>
          <span class="trust-label">{label}</span>
        </div>"""
        for num, label in highlights
    )
    return f"""<div class="trust-bar">
    <div class="container">
      <div class="trust-inner">
{items}
      </div>
    </div>
  </div>"""


def parse_highlights(raw) -> list[tuple[str, str]]:
    if not raw:
        return []
    entries = raw if isinstance(raw, list) else str(raw).split(",")
    pairs = []
    for entry in entries:
        num, sep, label = str(entry).partition(":")
        if sep and num.strip() and label.strip():
            pairs.append((num.strip(), label.strip()))
    return pairs


def generate_html(
    business_name: str,
    industry: str,
    tagline: str,
    phone: str,
    location: str,
    services: list[str],
    booking_url: str,
    highlights: list[tuple[str, str]] | None = None,
) -> str:
    business_name = escape(business_name)
    tagline = escape(tagline)
    phone = escape(phone)
    location = escape(location)
    services = [escape(s) for s in services]
    booking_url = escape(booking_url)
    trust_bar = render_trust_bar([(escape(n), escape(l)) for n, l in highlights or []])

    preset = INDUSTRY_PRESETS.get(industry, INDUSTRY_PRESETS["other"])
    accent = preset["accent"]
    bg = preset["bg_light"]
    tagline = tagline or preset["default_tagline"]
    cta = preset["cta_text"]
    service_intro = preset["service_intro"]
    hero_word = preset["hero_adjectives"][0]
    service_cards = render_services(services, accent, preset["icon_set"])

    # Derive a short location label
    city = location.split(",")[0].strip() if location else ""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{business_name}</title>
  <style>
    /* ── Reset & tokens ── */
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    :root {{
      --bg:        {bg};
      --ink:       #0a0a0a;
      --ink-muted: #5a5a58;
      --accent:    {accent};
      --accent-dk: #92400e;
      --white:     #ffffff;
      --radius:    6px;
      --fs-xs:     0.75rem;
      --fs-sm:     0.875rem;
      --fs-base:   1rem;
      --fs-lg:     1.25rem;
      --fs-xl:     1.5rem;
      --fs-2xl:    2rem;
      --fs-3xl:    2.75rem;
      --fs-4xl:    3.75rem;
      --font:      -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    }}

    html {{ scroll-behavior: smooth; }}

    body {{
      font-family: var(--font);
      background: var(--bg);
      color: var(--ink);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}

    /* ── Utilities ── */
    .container {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 0 24px;
    }}

    /* ── Nav ── */
    nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--bg);
      border-bottom: 1px solid rgba(0,0,0,0.07);
      padding: 18px 0;
    }}

    .nav-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .nav-brand {{
      font-size: var(--fs-lg);
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--ink);
      text-decoration: none;
    }}

    .nav-brand span {{
      color: var(--accent);
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 32px;
      list-style: none;
    }}

    .nav-links a {{
      font-size: var(--fs-sm);
      font-weight: 500;
      color: var(--ink-muted);
      text-decoration: none;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{ color: var(--ink); }}

    .btn {{
      display: inline-block;
      padding: 11px 26px;
      border-radius: var(--radius);
      font-size: var(--fs-sm);
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
      cursor: pointer;
      border: none;
    }}

    .btn-primary {{
      background: var(--accent);
      color: var(--white);
    }}

    .btn-primary:hover {{
      background: var(--accent-dk);
      transform: translateY(-1px);
      box-shadow: 0 4px 16px rgba(0,0,0,0.18);
    }}

    .btn-outline {{
      background: transparent;
      color: var(--ink);
      border: 1.5px solid var(--ink);
    }}

    .btn-outline:hover {{
      background: var(--ink);
      color: var(--white);
    }}

    /* ── Hero ── */
    .hero {{
      padding: 100px 0 80px;
      position: relative;
      overflow: hidden;
    }}

    .hero::before {{
      content: '';
      position: absolute;
      top: -120px;
      right: -160px;
      width: 560px;
      height: 560px;
      border-radius: 50%;
      background: radial-gradient(circle, {accent}18 0%, transparent 70%);
      pointer-events: none;
    }}

    .hero-eyebrow {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: var(--fs-xs);
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 24px;
    }}

    .hero-eyebrow::before {{
      content: '';
      display: block;
      width: 24px;
      height: 2px;
      background: var(--accent);
    }}

    .hero h1 {{
      font-size: clamp(var(--fs-3xl), 5.5vw, var(--fs-4xl));
      font-weight: 800;
      line-height: 1.1;
      letter-spacing: -0.03em;
      max-width: 700px;
      margin-bottom: 24px;
    }}

    .hero h1 em {{
      font-style: normal;
      color: var(--accent);
    }}

    .hero-sub {{
      font-size: var(--fs-lg);
      color: var(--ink-muted);
      max-width: 520px;
      margin-bottom: 40px;
      line-height: 1.65;
    }}

    .hero-actions {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 16px;
    }}

    .hero-meta {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: var(--fs-sm);
      color: var(--ink-muted);
    }}

    .hero-meta::before {{
      content: '📍';
      font-size: 0.9em;
    }}

    /* ── Trust bar ── */
    .trust-bar {{
      border-top: 1px solid rgba(0,0,0,0.07);
      border-bottom: 1px solid rgba(0,0,0,0.07);
      padding: 28px 0;
      margin-bottom: 80px;
    }}

    .trust-inner {{
      display: flex;
      flex-wrap: wrap;
      gap: 40px;
      align-items: center;
      justify-content: center;
    }}

    .trust-item {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
    }}

    .trust-num {{
      font-size: var(--fs-2xl);
      font-weight: 800;
      color: var(--ink);
      letter-spacing: -0.03em;
    }}

    .trust-label {{
      font-size: var(--fs-xs);
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--ink-muted);
    }}

    /* ── Services ── */
    .section {{
      padding: 80px 0;
    }}

    .section-header {{
      margin-bottom: 56px;
    }}

    .section-kicker {{
      display: inline-block;
      font-size: var(--fs-xs);
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 12px;
    }}

    .section-header h2 {{
      font-size: clamp(var(--fs-2xl), 3.5vw, var(--fs-3xl));
      font-weight: 800;
      letter-spacing: -0.025em;
      line-height: 1.15;
    }}

    .section-header p {{
      margin-top: 16px;
      font-size: var(--fs-lg);
      color: var(--ink-muted);
      max-width: 520px;
    }}

    .services-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 2px;
      background: rgba(0,0,0,0.07);
      border: 1px solid rgba(0,0,0,0.07);
      border-radius: calc(var(--radius) + 2px);
      overflow: hidden;
    }}

    .service-card {{
      background: var(--bg);
      padding: 36px 28px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      transition: background 0.18s;
    }}

    .service-card:hover {{ background: var(--white); }}

    .service-icon {{
      font-size: 1.1rem;
      line-height: 1;
    }}

    .service-card h3 {{
      font-size: var(--fs-base);
      font-weight: 700;
      letter-spacing: -0.01em;
    }}

    /* ── CTA band ── */
    .cta-band {{
      background: var(--ink);
      color: var(--white);
      padding: 80px 0;
    }}

    .cta-band-inner {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 32px;
    }}

    .cta-band h2 {{
      font-size: clamp(var(--fs-xl), 3vw, var(--fs-3xl));
      font-weight: 800;
      letter-spacing: -0.025em;
      line-height: 1.15;
      max-width: 520px;
    }}

    .cta-band h2 em {{
      font-style: normal;
      color: var(--accent);
    }}

    .cta-band .btn-primary {{
      flex-shrink: 0;
      padding: 16px 36px;
      font-size: var(--fs-base);
    }}

    /* ── Contact strip ── */
    .contact-strip {{
      padding: 64px 0;
      border-bottom: 1px solid rgba(0,0,0,0.07);
    }}

    .contact-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 32px;
    }}

    .contact-item h4 {{
      font-size: var(--fs-xs);
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 8px;
    }}

    .contact-item p {{
      font-size: var(--fs-base);
      font-weight: 600;
      color: var(--ink);
    }}

    /* ── Footer ── */
    footer {{
      padding: 28px 0;
    }}

    .footer-inner {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}

    .footer-copy {{
      font-size: var(--fs-xs);
      color: var(--ink-muted);
    }}

    .watermark {{
      font-size: var(--fs-xs);
      font-weight: 600;
      color: var(--ink-muted);
      letter-spacing: 0.04em;
    }}

    .watermark a {{
      color: var(--accent);
      text-decoration: none;
    }}

    .watermark a:hover {{ text-decoration: underline; }}

    /* ── Demo ribbon ── */
    .demo-ribbon {{
      background: var(--accent);
      color: var(--white);
      text-align: center;
      font-size: var(--fs-xs);
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 10px;
    }}

    /* ── Responsive ── */
    @media (max-width: 640px) {{
      .nav-links {{ display: none; }}
      .hero {{ padding: 60px 0 48px; }}
      .trust-inner {{ gap: 24px; }}
      .cta-band-inner {{ flex-direction: column; align-items: flex-start; }}
    }}
  </style>
</head>
<body>

  <!-- Demo notice ribbon -->
  <div class="demo-ribbon">
    ✦ This is a complimentary demo site built for {business_name} by Vanguard ✦
  </div>

  <!-- Nav -->
  <nav>
    <div class="container">
      <div class="nav-inner">
        <a href="#" class="nav-brand">
          {business_name.split()[0]}<span>{"." if len(business_name.split()) == 1 else " " + " ".join(business_name.split()[1:])}</span>
        </a>
        <ul class="nav-links">
          <li><a href="#services">Services</a></li>
          <li><a href="#contact">Contact</a></li>
          <li><a href="{booking_url}" class="btn btn-primary">{cta}</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Hero -->
  <section class="hero">
    <div class="container">
      <div class="hero-eyebrow">{city or location}</div>
      <h1>
        {preset["hero_verb"]} <em>{hero_word}</em><br />results — every time.
      </h1>
      <p class="hero-sub">
        {tagline}
      </p>
      <div class="hero-actions">
        <a href="{booking_url}" class="btn btn-primary">{cta} &rarr;</a>
        <a href="#services" class="btn btn-outline">See our services</a>
      </div>
      {f'<p class="hero-meta" style="margin-top:24px">{location}</p>' if location else ""}
    </div>
  </section>

  <!-- Trust bar -->
  {trust_bar}

  <!-- Services -->
  <section class="section" id="services">
    <div class="container">
      <div class="section-header">
        <span class="section-kicker">{service_intro}</span>
        <h2>Everything you need,<br />in one place.</h2>
        <p>We specialize in delivering results that speak for themselves — for every client, every time.</p>
      </div>
      <div class="services-grid">
        {service_cards}
      </div>
    </div>
  </section>

  <!-- CTA band -->
  <section class="cta-band">
    <div class="container">
      <div class="cta-band-inner">
        <h2>Ready to take the<br /><em>next step?</em></h2>
        <a href="{booking_url}" class="btn btn-primary">{cta} &rarr;</a>
      </div>
    </div>
  </section>

  <!-- Contact -->
  <section class="contact-strip" id="contact">
    <div class="container">
      <div class="contact-grid">
        {f'<div class="contact-item"><h4>Call Us</h4><p>{phone}</p></div>' if phone else ""}
        {f'<div class="contact-item"><h4>Location</h4><p>{location}</p></div>' if location else ""}
        <div class="contact-item">
          <h4>Book Online</h4>
          <p><a href="{booking_url}" style="color:var(--accent);text-decoration:none">{cta} &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-inner">
        <span class="footer-copy">&copy; {business_name}. All rights reserved.</span>
        <span class="watermark">
          Demo by Vanguard
        </span>
      </div>
    </div>
  </footer>

</body>
</html>"""
    return html


# ─── CLI ─────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Vanguard Demo Site Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--json", metavar="JSON", help="All inputs as a JSON string")
    p.add_argument("--business_name", help="Business name")
    p.add_argument(
        "--industry",
        choices=list(INDUSTRY_PRESETS.keys()),
        default="other",
        help="Industry preset",
    )
    p.add_argument("--tagline", default="", help="Short tagline (optional)")
    p.add_argument("--phone", default="", help="Phone number")
    p.add_argument("--location", default="", help="City, State")
    p.add_argument(
        "--services",
        default="",
        help="Comma-separated list of services",
    )
    p.add_argument(
        "--booking_url",
        default="https://calendly.com/vanguard-agency",
        help="CTA booking/contact URL",
    )
    p.add_argument(
        "--highlights",
        default="",
        help='Verified facts only, "value:label" comma-separated, e.g. "4.9★:Google rating,12:Years in Austin"',
    )
    p.add_argument(
        "--output_dir",
        default=".",
        help="Directory to save the output HTML file (default: current dir)",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()

    # Load from JSON if provided
    if args.json:
        try:
            data = json.loads(args.json)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        data = {
            "business_name": args.business_name,
            "industry": args.industry,
            "tagline": args.tagline,
            "phone": args.phone,
            "location": args.location,
            "services": args.services,
            "booking_url": args.booking_url,
            "highlights": args.highlights,
        }

    # Validate required fields
    if not data.get("business_name"):
        print("ERROR: --business_name is required (or 'business_name' in JSON)", file=sys.stderr)
        sys.exit(1)

    # Parse services
    services_raw = data.get("services", "")
    if isinstance(services_raw, list):
        services = [s.strip() for s in services_raw if s.strip()]
    else:
        services = [s.strip() for s in str(services_raw).split(",") if s.strip()]

    if not services:
        services = ["Our Services"]

    industry = data.get("industry", "other")
    if industry not in INDUSTRY_PRESETS:
        industry = "other"

    html = generate_html(
        business_name=data["business_name"],
        industry=industry,
        tagline=data.get("tagline", ""),
        phone=data.get("phone", ""),
        location=data.get("location", ""),
        services=services,
        booking_url=data.get("booking_url", "https://calendly.com/vanguard-agency"),
        highlights=parse_highlights(data.get("highlights")),
    )

    output_dir = Path(args.output_dir if not args.json else data.get("output_dir", "."))
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = slugify(data["business_name"]) + "_demo.html"
    output_path = output_dir / filename

    output_path.write_text(html, encoding="utf-8")
    print(f"✓  Demo generated: {output_path.resolve()}")


if __name__ == "__main__":
    main()
