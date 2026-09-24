#!/usr/bin/env python3
"""GHL -> Discord relay (fallback for accounts without the Custom Webhook action).

GHL's standard "Webhook" workflow action POSTs GHL's own JSON payload, which
Discord rejects. Point that action at this relay instead; the relay rebuilds
the message as a Discord embed (properly JSON-encoded, so quotes/newlines in
merge fields can't break it) and forwards it to the right channel webhook.

Standard library only (Python 3.9+). No secrets live in this file.

Environment variables
  RELAY_TOKEN                     required; shared secret GHL sends as ?token=...
  DISCORD_WEBHOOK_BOOKED_CALLS    Discord webhook URL for #booked-calls
  DISCORD_WEBHOOK_NO_SHOWS        ... #no-shows
  DISCORD_WEBHOOK_DEMO_REQUESTS   ... #demo-requests
  DISCORD_WEBHOOK_WINS            ... #wins
  DISCORD_WEBHOOK_PIPELINE_ALERTS ... #pipeline-alerts
  PORT                            optional, default 8080

GHL setup (standard Webhook action)
  URL:  https://<your-relay-host>/<channel>?token=<RELAY_TOKEN>
        <channel> is one of: booked-calls, no-shows, demo-requests, wins, pipeline-alerts
  Custom Data (key/value pairs, shown as embed fields in this order):
        title  -> embed title, e.g. "New call booked"   (optional)
        color  -> decimal colour, e.g. 3447003           (optional)
        any other key -> a field, e.g. Setter = {{contact.setter_assigned}}

Run locally:  RELAY_TOKEN=... DISCORD_WEBHOOK_WINS=... python3 relay.py
"""

import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

CHANNELS = {
    # path: (env var, default title, default colour)
    "booked-calls": ("DISCORD_WEBHOOK_BOOKED_CALLS", "New call booked", 3447003),
    "no-shows": ("DISCORD_WEBHOOK_NO_SHOWS", "No-show / cancellation - rebook within 2h", 15158332),
    "demo-requests": ("DISCORD_WEBHOOK_DEMO_REQUESTS", "Demo build requested", 10181046),
    "wins": ("DISCORD_WEBHOOK_WINS", "Closed Won", 3066993),
    "pipeline-alerts": ("DISCORD_WEBHOOK_PIPELINE_ALERTS", "Pipeline update", 15844367),
}

# Discord embed limits (developer docs, Embed Limits).
MAX_TITLE, MAX_NAME, MAX_VALUE, MAX_FIELDS, MAX_TOTAL = 256, 256, 1024, 25, 6000
# Fallback fields read from GHL's standard payload when no Custom Data was sent.
FALLBACK_KEYS = [("Business", "company_name"), ("Contact", "full_name"), ("Phone", "phone"), ("Email", "email")]


def _clip(text, limit):
    text = str(text).strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


def build_message(channel, payload):
    """Turn a GHL webhook payload into a Discord execute-webhook body."""
    _, default_title, default_color = CHANNELS[channel]
    custom = payload.get("customData") or payload.get("custom_data") or {}
    if not isinstance(custom, dict):
        custom = {}

    title = _clip(custom.get("title") or default_title, MAX_TITLE)
    try:
        color = int(custom.get("color", default_color))
    except (TypeError, ValueError):
        color = default_color

    pairs = [(k, v) for k, v in custom.items() if k not in ("title", "color")]
    if not pairs:
        pairs = [(label, payload.get(key)) for label, key in FALLBACK_KEYS]

    fields, used = [], len(title)
    for name, value in pairs:
        if value in (None, "") or len(fields) >= MAX_FIELDS:
            continue
        name, value = _clip(name, MAX_NAME), _clip(value, MAX_VALUE)
        if used + len(name) + len(value) > MAX_TOTAL:
            break
        used += len(name) + len(value)
        fields.append({"name": name, "value": value, "inline": len(value) <= 40})

    return {
        "embeds": [{"title": title, "color": color, "fields": fields}],
        "allowed_mentions": {"parse": []},  # never ping @everyone/@here/users/roles
    }


def post_to_discord(url, body):
    data = json.dumps(body).encode("utf-8")
    for attempt in range(2):
        req = urllib.request.Request(url, data=data, method="POST",
                                     headers={"Content-Type": "application/json",
                                              "User-Agent": "ghl-discord-relay/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                return resp.status
        except urllib.error.HTTPError as err:
            if err.code == 429 and attempt == 0:  # rate limited: wait once, retry
                try:
                    wait = float(json.loads(err.read() or b"{}").get("retry_after", 1))
                except ValueError:
                    wait = 1.0
                time.sleep(min(wait, 5))
                continue
            return err.code
        except urllib.error.URLError:
            return 502
    return 429


class Handler(BaseHTTPRequestHandler):
    def _reply(self, code, msg):
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(msg.encode())

    def do_POST(self):
        parsed = urlparse(self.path)
        channel = parsed.path.strip("/")
        token = (parse_qs(parsed.query).get("token") or [""])[0] or self.headers.get("X-Relay-Token", "")
        expected = os.environ.get("RELAY_TOKEN", "")
        if not expected or not hmac.compare_digest(token, expected):
            return self._reply(401, "unauthorized")
        if channel not in CHANNELS:
            return self._reply(404, "unknown channel")
        url = os.environ.get(CHANNELS[channel][0])
        if not url:
            return self._reply(500, "webhook URL not configured")
        try:
            length = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(min(length, 1_000_000)) or b"{}")
        except (ValueError, json.JSONDecodeError):
            return self._reply(400, "invalid JSON")
        if not isinstance(payload, dict):
            return self._reply(400, "expected a JSON object")
        status = post_to_discord(url, build_message(channel, payload))
        self._reply(200 if status in (200, 204) else 502, f"discord status {status}")

    def log_message(self, fmt, *args):  # log path without the ?token= query string
        sys.stderr.write("%s %s\n" % (self.command, urlparse(self.path).path))


if __name__ == "__main__":
    if not os.environ.get("RELAY_TOKEN"):
        sys.exit("RELAY_TOKEN is not set")
    port = int(os.environ.get("PORT", "8080"))
    print(f"ghl-discord-relay listening on :{port}")
    ThreadingHTTPServer(("", port), Handler).serve_forever()
