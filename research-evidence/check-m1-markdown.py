from pathlib import Path
from collections import Counter
import re

root = Path(r'D:\the next level\valiris-restaurants')
path = root / 'docs/design/m1-connected-journey.md'
doc = path.read_text(encoding='utf-8')
anchors = set()
for heading in re.findall(r'^#{1,6} (.+)$', doc, re.M):
    slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
    anchors.add(slug)
internal = re.findall(r'\]\(#([^)]+)\)', doc)
assert set(internal) <= anchors, sorted(set(internal) - anchors)
local = [x for x in re.findall(r'\]\(([^)]+)\)', doc) if not x.startswith(('http', '#'))]
assert all((path.parent / x.split('#', 1)[0]).exists() for x in local)
coverage = doc.split('## 7.', 1)[1].split('## 8.', 1)[0]
expanded = []
for row in coverage.splitlines():
    if not row.startswith('| B'):
        continue
    field = row.split('|')[1]
    def expand(match):
        left, start, right, end = match.groups()
        assert left == right
        expanded.extend(f'{left}.{i:02}' for i in range(int(start), int(end)+1))
        return ''
    remaining = re.sub(r'(B\d)\.(\d{2})\u2013(B\d)\.(\d{2})', expand, field)
    expanded.extend(re.findall(r'B\d\.\d{2}', remaining))
matrix = (root / 'docs/product/m0-capability-matrix.md').read_text(encoding='utf-8')
expected = set(re.findall(r'B\d\.\d{2}', matrix))
assert len(expected) == 72
assert set(expanded) == expected
assert all(n == 1 for n in Counter(expanded).values())
assert doc.count('```') % 2 == 0
assert len(re.findall(r'^\| T\d\b', doc, re.M)) == 8
for item in ['C1', 'C2', 'C3', 'X01', 'X02', 'X03', 'X04', 'L10a', 'D11']:
    assert item in doc
assert 'Recommend **Figma Design**' not in doc
if '## 11. C1-C3 author review' in doc:
    findings = re.findall(r'^\| (F\d{2}) ', doc, re.M)
    cases = re.findall(r'^\| (V\d{2}) ', doc, re.M)
    assert findings == [f'F{i:02}' for i in range(1, 15)], findings
    assert cases == [f'V{i:02}' for i in range(1, 17)], cases
    print('PASS: 14 unique correction findings and 16 unique documentary counterexamples.')
print(f'PASS: {len(local)} local links; {len(internal)} document action links; 72 capabilities once each; 8 review tasks; storyboard/recovery markers and fences.')
