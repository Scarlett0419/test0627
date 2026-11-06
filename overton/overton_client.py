"""Minimal, rate-limited client for the Overton API (https://app.overton.io/swagger.php).

Documented behaviour this client relies on:
  * Base URL https://app.overton.io/, every call needs `api_key` and `format=json`.
  * Endpoints: documents.php (policy docs), people.php (people mentioned in policy),
    articles.php (scholarly articles cited in policy), generate_id_set.php (POST, DOI sets).
  * Responses have `query` (total_results, pages, current_page, next_page_url), `facets`, `results`.
  * Paginate with `page=N`; no `next_page_url` means the last page.
  * At most ~1 request/second. Over-limit calls return HTTP 429 with empty results,
    and repeated abuse can get the key blocked, so we throttle and back off.

Filter parameters beyond `query`, `plain_dois_cited`, `sort` and `page` are not
publicly documented. Copy them from the app's Export -> "Generate API call" URL
and pass them through `**params`.

Keep the API key server-side (env var OVERTON_API_KEY). Never ship it in the dashboard.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Callable, Iterator

BASE_URL = "https://app.overton.io/"

Transport = Callable[[str, str, bytes | None, dict], tuple[int, bytes]]


def _urllib_transport(method: str, url: str, body: bytes | None, headers: dict) -> tuple[int, bytes]:
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


class OvertonError(RuntimeError):
    pass


class OvertonClient:
    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str = BASE_URL,
        min_interval: float = 1.1,
        max_retries: int = 5,
        transport: Transport | None = None,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self.api_key = api_key or os.environ.get("OVERTON_API_KEY")
        if not self.api_key:
            raise OvertonError("No API key. Set OVERTON_API_KEY or pass api_key=...")
        self.base_url = base_url.rstrip("/") + "/"
        self.min_interval = min_interval
        self.max_retries = max_retries
        self._transport = transport or _urllib_transport
        self._sleep = sleep
        self._last_call = 0.0

    # ------------------------------------------------------------------ core
    def _throttle(self) -> None:
        wait = self.min_interval - (time.monotonic() - self._last_call)
        if wait > 0:
            self._sleep(wait)
        self._last_call = time.monotonic()

    def _request(self, method: str, endpoint: str, params: dict, form: dict | None = None) -> dict:
        params = {k: v for k, v in params.items() if v is not None}
        params.update(format="json", api_key=self.api_key)
        url = self.base_url + endpoint + "?" + urllib.parse.urlencode(params, doseq=True)
        body = urllib.parse.urlencode(form).encode() if form is not None else None
        headers = {"Accept": "application/json", "User-Agent": "sf-overton-dashboard/0.1"}
        if body is not None:
            headers["Content-Type"] = "application/x-www-form-urlencoded"

        for attempt in range(self.max_retries + 1):
            self._throttle()
            status, raw = self._transport(method, url, body, headers)
            if status == 429 or status >= 500:
                if attempt == self.max_retries:
                    break
                self._sleep(min(60, 2 ** (attempt + 1)))
                continue
            if status >= 400:
                raise OvertonError(f"HTTP {status} from {endpoint}: {raw[:300]!r}")
            try:
                data = json.loads(raw or b"{}")
            except json.JSONDecodeError as e:
                raise OvertonError(f"Non-JSON response from {endpoint}: {raw[:300]!r}") from e
            if isinstance(data, dict) and data.get("error"):
                raise OvertonError(f"Overton error from {endpoint}: {data['error']}")
            return data
        raise OvertonError(f"Gave up on {endpoint} after {self.max_retries} retries (HTTP {status})")

    def get(self, endpoint: str, **params: Any) -> dict:
        return self._request("GET", endpoint, params)

    def paginate(self, endpoint: str, *, max_pages: int | None = None, **params: Any) -> Iterator[dict]:
        """Yield every result across pages. Stops when next_page_url is absent or pages are exhausted."""
        page = int(params.pop("page", 1))
        fetched = 0
        while True:
            data = self.get(endpoint, page=page, **params)
            results = data.get("results") or []
            yield from results
            fetched += 1
            q = data.get("query") or {}
            total_pages = q.get("pages")
            if not results:
                return
            if total_pages is not None:
                if page >= int(total_pages):
                    return
            elif not q.get("next_page_url"):
                return
            if max_pages is not None and fetched >= max_pages:
                return
            page += 1

    # ------------------------------------------------------------- endpoints
    def search_documents(self, query: str | None = None, **params: Any) -> dict:
        """One page of policy documents. `query` is full-text (use quotes for phrases)."""
        return self.get("documents.php", query=query, **params)

    def iter_documents(self, query: str | None = None, *, max_pages: int | None = None, **params: Any) -> Iterator[dict]:
        return self.paginate("documents.php", query=query, max_pages=max_pages, **params)

    def documents_citing(self, doi_or_set: str, *, max_pages: int | None = None, **params: Any) -> Iterator[dict]:
        """Policy documents citing a DOI, or a set id from generate_id_set()."""
        return self.paginate("documents.php", plain_dois_cited=doi_or_set, max_pages=max_pages, **params)

    def search_people(self, query: str, **params: Any) -> dict:
        """People mentioned in policy (people.php). Parameters undocumented; pass extras via **params."""
        return self.get("people.php", query=query, **params)

    def search_articles(self, query: str | None = None, **params: Any) -> dict:
        """Scholarly articles cited in policy (articles.php)."""
        return self.get("articles.php", query=query, **params)

    def generate_id_set(self, identifiers: list[str]) -> str:
        """POST a list of DOIs (or ISBNs/ORCIDs/PMIDs) and get a reusable set id like 'set:1:abc...'."""
        data = self._request("POST", "generate_id_set.php", {}, form={"dois": "\n".join(identifiers)})
        set_id = data.get("set") or data.get("set_id")
        if not set_id:
            raise OvertonError(f"generate_id_set returned no set id: {data}")
        return set_id


def name_query(variants: list[str]) -> str:
    """Build an OR'd exact-phrase query from name spellings, e.g. Böhm / Boehm / Bohm."""
    return " OR ".join(f'"{v}"' for v in variants)
