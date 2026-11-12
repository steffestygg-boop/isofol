"""Fetch the most recently reported ISOFOL.ST share price for the static dashboard.

Yahoo Finance provides delayed, best-effort market data. The timestamp is the
market's quote timestamp, not the moment this job happened to execute.
Never overwrite a verified quote with an error page or malformed data.
"""
import datetime as dt
import json
import pathlib
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "price.json"
SYMBOL = "ISOFOL.ST"
URLS = [
    f"https://query2.finance.yahoo.com/v8/finance/chart/{SYMBOL}?range=5d&interval=5m",
    f"https://query1.finance.yahoo.com/v8/finance/chart/{SYMBOL}?range=5d&interval=5m",
]


def get_quote():
    errors = []
    for url in URLS:
        try:
            request = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/123 Safari/537.36",
                "Accept": "application/json",
            })
            with urllib.request.urlopen(request, timeout=18) as response:
                data = json.load(response)
            result = data["chart"]["result"][0]
            meta = result["meta"]
            if meta.get("currency") != "SEK":
                raise ValueError("Unexpected trading currency")
            price = float(meta["regularMarketPrice"])
            market_time = int(meta["regularMarketTime"])
            if not 0 < price < 1000:
                raise ValueError("Price out of reasonable range")
            quote_time = dt.datetime.fromtimestamp(market_time, tz=dt.timezone.utc)
            now = dt.datetime.now(dt.timezone.utc)
            if quote_time > now + dt.timedelta(minutes=10) or now - quote_time > dt.timedelta(days=7):
                raise ValueError("Quote date is out of range")
            previous = meta.get("previousClose") or meta.get("chartPreviousClose")
            previous = float(previous) if previous is not None else None
            if previous is not None and not 0 < previous < 1000:
                previous = None
            return {
                "symbol": SYMBOL,
                "price": price,
                "currency": "SEK",
                "as_of": quote_time.isoformat(timespec="seconds").replace("+00:00", "Z"),
                "previous_close": previous,
                "source": "Yahoo Finance (fördröjd)",
                "source_url": "https://finance.yahoo.com/quote/ISOFOL.ST/",
            }
        except (ValueError, KeyError, IndexError, TypeError, OSError, urllib.error.URLError) as exc:
            errors.append(f"{url.split('/')[2]}: {type(exc).__name__}: {exc}")
    raise RuntimeError("Could not retrieve valid quote; retaining previous data. " + " / ".join(errors))


if __name__ == "__main__":
    quote = get_quote()
    if OUT.exists():
        try:
            previous = json.loads(OUT.read_text(encoding="utf-8"))
            if previous.get("as_of") and previous["as_of"] > quote["as_of"]:
                raise RuntimeError("Refusing to replace a newer cached quote with older market data")
        except json.JSONDecodeError:
            pass
    content = json.dumps(quote, ensure_ascii=False, indent=2) + "\n"
    OUT.write_text(content, encoding="utf-8")
    print(f"ISOFOL.ST: {quote['price']} SEK, as of {quote['as_of']}")
