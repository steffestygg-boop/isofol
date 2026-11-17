"""Regression tests for sourced, time-stamped share prices and dashboard cards."""
import datetime as dt
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from update_stock_quote import validate_chart, SYMBOL

class StockQuoteTests(unittest.TestCase):
    def test_valid_source_quote(self):
        now = int(dt.datetime.now(dt.timezone.utc).timestamp())
        payload = {"chart":{"result":[{"meta":{
            "symbol":SYMBOL,"currency":"SEK",
            "regularMarketPrice":0.2268,"regularMarketTime":now
        }}]}}
        q=validate_chart(payload)
        self.assertEqual(q["symbol"],SYMBOL)
        self.assertEqual(q["currency"],"SEK")
        self.assertEqual(q["price"],0.2268)
        self.assertIn("quote_time",q)

    def test_wrong_symbol_or_currency_rejected(self):
        now = int(dt.datetime.now(dt.timezone.utc).timestamp())
        for k,v in (("currency","USD"),("symbol","SYNACT.ST"),("regularMarketPrice",-1),("regularMarketPrice",0)):
            with self.subTest(key=k):
                meta={"symbol":SYMBOL,"currency":"SEK",
                      "regularMarketPrice":1.0,"regularMarketTime":now}
                meta[k]=v
                with self.assertRaises(ValueError):
                    validate_chart({"chart":{"result":[{"meta":meta}]}})

    def test_outdated_and_future_quote_rejected(self):
        now = int(dt.datetime.now(dt.timezone.utc).timestamp())
        for when in (now-11*86400,now+3600):
            with self.assertRaises(ValueError):
                validate_chart({"chart":{"result":[{"meta":{
                    "symbol":SYMBOL,"currency":"SEK",
                    "regularMarketPrice":1.0,"regularMarketTime":when
                }}]}})

    def test_initial_close_is_source_dated_not_invented_intra_day(self):
        q=json.loads((ROOT/"data"/"stock_quote.json").read_text(encoding="utf-8"))
        self.assertEqual(q["symbol"],SYMBOL)
        self.assertEqual(q["currency"],"SEK")
        self.assertGreater(q["price"],0)
        self.assertTrue(q["quote_time"])
        self.assertIn("source_url",q)

    def test_dashboard_shares_quote_and_source_timestamp(self):
        h=(ROOT/"index.html").read_text(encoding="utf-8")
        for marker in (
            'id="shared-stock-price"',
            'id="shared-stock-quote-status"',
            "fetch('./data/stock_quote.json",
            'setInterval(refresh,120000)',
            "q.symbol!==expectedSymbol",
            "q.currency!=='SEK'"
        ):
            self.assertIn(marker,h)
        self.assertNotIn("embed-widget-single-quote.js",h)

if __name__ == "__main__":
    unittest.main()
