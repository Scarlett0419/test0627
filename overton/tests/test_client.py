import json
import sys
import unittest
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from classify import to_mention  # noqa: E402
from overton_client import OvertonClient, OvertonError, name_query  # noqa: E402


class FakeTransport:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def __call__(self, method, url, body, headers):
        self.calls.append((method, url, body))
        status, payload = self.responses.pop(0)
        return status, json.dumps(payload).encode()


def page(n, pages, ids, nxt=True):
    return {"query": {"current_page": n, "pages": pages, "next_page_url": "x" if nxt else None},
            "results": [{"policy_document_id": i} for i in ids]}


def client(responses):
    t = FakeTransport(responses)
    return OvertonClient("KEY", transport=t, sleep=lambda s: None), t


class ClientTests(unittest.TestCase):
    def test_adds_key_and_format(self):
        c, t = client([(200, page(1, 1, [1], nxt=False))])
        c.search_documents('"Steffen Böhm"')
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(t.calls[0][1]).query)
        self.assertEqual(qs["api_key"], ["KEY"])
        self.assertEqual(qs["format"], ["json"])
        self.assertEqual(qs["query"], ['"Steffen Böhm"'])

    def test_paginates_until_last_page(self):
        c, t = client([(200, page(1, 3, [1, 2])), (200, page(2, 3, [3])), (200, page(3, 3, [4], nxt=False))])
        ids = [r["policy_document_id"] for r in c.iter_documents("x")]
        self.assertEqual(ids, [1, 2, 3, 4])
        self.assertEqual(len(t.calls), 3)

    def test_max_pages(self):
        c, t = client([(200, page(1, 9, [1])), (200, page(2, 9, [2]))])
        self.assertEqual(len(list(c.iter_documents("x", max_pages=2))), 2)

    def test_retries_on_429(self):
        c, t = client([(429, {}), (200, page(1, 1, [1], nxt=False))])
        self.assertEqual(len(c.search_documents("x")["results"]), 1)
        self.assertEqual(len(t.calls), 2)

    def test_raises_on_api_error(self):
        c, _ = client([(200, {"error": "bad key"})])
        with self.assertRaises(OvertonError):
            c.search_documents("x")

    def test_generate_id_set_accepts_either_key(self):
        c, t = client([(200, {"set": "set:1:abc"}), (200, {"set_id": "set:1:def"})])
        self.assertEqual(c.generate_id_set(["10.1/a", "10.1/b"]), "set:1:abc")
        self.assertEqual(c.generate_id_set(["10.1/c"]), "set:1:def")
        self.assertEqual(t.calls[0][0], "POST")
        self.assertIn(b"10.1%2Fa%0A10.1%2Fb", t.calls[0][2])

    def test_name_query(self):
        self.assertEqual(name_query(["Steffen Böhm", "Steffen Boehm"]), '"Steffen Böhm" OR "Steffen Boehm"')


class ClassifyTests(unittest.TestCase):
    def test_to_mention(self):
        doc = {"policy_document_id": "p1", "title": "Circular food waste strategy", "published_on": "2024-05-01T00:00",
               "source": {"title": "Defra", "country": "UK", "type": "government"}}
        m = to_mention(doc, "s1", "cited")
        self.assertEqual(m["country"], "United Kingdom")
        self.assertEqual(m["region"], "Europe")
        self.assertEqual(m["source_type"], "Government")
        self.assertEqual(m["published_on"], "2024-05-01")
        self.assertIn("Circular Economy", m["topics"])
        self.assertIn("Food & Agriculture", m["topics"])


if __name__ == "__main__":
    unittest.main()
