"""Fetch public Google News RSS headlines about Isofol; do not infer clinical milestones."""
import datetime as dt
import email.utils
import html
import re
import ipaddress
import socket
import json
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
QUERY = '("Isofol Medical" OR "arfolitixorin") when:90d'
URL = 'https://news.google.com/rss/search?' + urllib.parse.urlencode({'q': QUERY, 'hl': 'sv', 'gl': 'SE', 'ceid': 'SE:sv'})
req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0 (compatible; IsofolTracker/1.0)'})
with urllib.request.urlopen(req, timeout=25) as response:
    content = response.read()
root = ET.fromstring(content)

def article_summary(news_url):
    """Retrieve a short, source-based excerpt, never an invented summary."""
    try:
        from bs4 import BeautifulSoup
        from googlenewsdecoder import gnewsdecoder
        decoded = gnewsdecoder(news_url, interval=0)
        article_url = decoded.get('decoded_url') if isinstance(decoded, dict) else None
        if not article_url:
            return '', news_url
        parsed = urllib.parse.urlparse(article_url)
        if parsed.scheme != 'https' or not parsed.hostname:
            return '', news_url
        # Do not fetch local or private network destinations.
        addresses = socket.getaddrinfo(parsed.hostname, 443, type=socket.SOCK_STREAM)
        if not addresses or any(not ipaddress.ip_address(a[4][0]).is_global for a in addresses):
            return '', news_url
        request = urllib.request.Request(article_url, headers={'User-Agent': 'Mozilla/5.0 (compatible; IsofolTracker/1.0)'})
        with urllib.request.urlopen(request, timeout=9) as response:
            if response.url != article_url or 'text/html' not in response.headers.get('Content-Type', ''):
                return '', news_url
            page = response.read(450_000).decode('utf-8', errors='replace')
        soup = BeautifulSoup(page, 'html.parser')
        for selector in ['meta[property="og:description"]', 'meta[name="description"]', 'meta[name="twitter:description"]']:
            tag = soup.select_one(selector)
            description = ' '.join((tag.get('content', '') if tag else '').split())
            if len(description) >= 90 and 'cookie' not in description.lower() and 'javascript' not in description.lower():
                return description[:650], article_url
        article = soup.select_one('article') or soup.select_one('main')
        if article:
            paragraphs = [' '.join(p.get_text(' ', strip=True).split()) for p in article.select('p')]
            paragraphs = [p for p in paragraphs if len(p) >= 80]
            if paragraphs:
                return ' '.join(paragraphs[:2])[:650], article_url
        return '', article_url
    except Exception as exc:
        print('Article summary unavailable:', type(exc).__name__)
        return '', news_url

items = []
seen = set()
for item in root.findall('./channel/item'):
    title = (item.findtext('title') or '').strip()
    link = (item.findtext('link') or '').strip()
    published = (item.findtext('pubDate') or '').strip()
    source = (item.findtext('source') or '').strip()
    if not title or not link or link in seen or 'isofol' not in title.casefold():
        continue
    seen.add(link)
    try:
        date = email.utils.parsedate_to_datetime(published).astimezone(dt.timezone.utc).date().isoformat()
    except Exception:
        date = ''
    items.append({'title': title, 'url': link, 'date': date, 'source': source})
items.sort(key=lambda item: item['date'], reverse=True)
items = items[:16]
for item in items:
    summary, original_url = article_summary(item['url'])
    item['summary'] = summary
    item['summary_source'] = 'publisher' if summary else 'unavailable'
    if original_url != item['url']:
        item['url'] = original_url
if not items:
    raise RuntimeError('No RSS items returned; retaining prior data instead of publishing an empty list')
output = {'updated_at': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'), 'feed': 'Google News RSS – search results, not independently verified', 'items': items}
(ROOT / 'data' / 'news.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Saved', len(items), 'headlines')
