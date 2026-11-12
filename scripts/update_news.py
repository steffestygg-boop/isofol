"""Fetch public Google News RSS headlines about Isofol; do not infer clinical milestones."""
import datetime as dt
import email.utils
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
if not items:
    raise RuntimeError('No RSS items returned; retaining prior data instead of publishing an empty list')
output = {'updated_at': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'), 'feed': 'Google News RSS – search results, not independently verified', 'items': items}
(ROOT / 'data' / 'news.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Saved', len(items), 'headlines')
