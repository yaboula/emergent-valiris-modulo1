from pathlib import Path
import re

root = Path(r'D:\the next level\valiris-restaurants')
paths = [
    'docs/design/m1-extended-journeys.md',
    'docs/design/m1-connected-journey.md',
    'docs/adr/0010-diner-account-and-display-recovery.md',
    'docs/adr/README.md', 'docs/README.md',
    'docs/product/m1-design-briefs.md',
    'docs/product/m0-journeys-and-criteria.md',
    'docs/project/roadmap.md', 'docs/project/m0-closeout.md',
]

def anchors(doc):
    result = []
    for h in re.findall(r'^#{1,6} (.+)$', doc, re.M):
        result.append(re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-'))
    return result

checked_links = 0
for name in paths:
    path = root / name
    doc = path.read_text(encoding='utf-8')
    assert doc.count('```') % 2 == 0, name
    own_anchors = anchors(doc)
    assert len(set(own_anchors)) == len(own_anchors), ('duplicate headings', name)
    for link in re.findall(r'\]\(([^)]+)\)', doc):
        if link.startswith(('https://', 'http://', 'mailto:')):
            continue
        target_name, _, fragment = link.partition('#')
        target = path.parent / target_name if target_name else path
        assert target.exists(), (name, link)
        if fragment:
            assert target.is_file(), (name, link)
            assert fragment in anchors(target.read_text(encoding='utf-8')), (name, link)
        checked_links += 1

extended = (root / paths[0]).read_text(encoding='utf-8')
state_ids = re.findall(r'^### (J\d{2}-[POAC]\d{2}):', extended, re.M)
assert len(set(state_ids)) == len(state_ids), 'duplicate state ID'
assert set(re.findall(r'J\d{2}-[POAC]\d{2}', extended)) <= set(state_ids), 'undefined state ID'
criteria = re.findall(r'^\| (J\d{2}\.\d) \|', extended, re.M)
source = (root / 'docs/product/m0-journeys-and-criteria.md').read_text(encoding='utf-8')
expected = re.findall(r'^- \*\*(J1[0-5]\.\d):', source, re.M)
assert len(expected) == 20
assert sorted(criteria) == sorted(expected), (criteria, expected)
for prefix, count in [('E', 18), ('W', 7)]:
    case_ids = re.findall(r'^\| (' + prefix + r'\d{2}) ', extended, re.M)
    assert case_ids == [f'{prefix}{i:02}' for i in range(1, count + 1)], case_ids
if '## 11. Fresh J10' in extended:
    findings = re.findall(r'^\| (XF\d{2}) ', extended, re.M)
    cases = re.findall(r'^\| (Q\d{2}) ', extended, re.M)
    assert findings == [f'XF{i:02}' for i in range(1, 13)], findings
    assert cases == [f'Q{i:02}' for i in range(1, 21)], cases
    reviewed_criteria = re.findall(r'^\| Q\d{2} \| (J1[0-5]\.\d)', extended, re.M)
    assert sorted(reviewed_criteria) == sorted(expected), reviewed_criteria
    assert not re.search(r'(?<![\w-])(?:A0[1-9]|C0[1-6])\b', extended), 'ambiguous extended account/connection ID'
    print('PASS: 12 unique correction findings and 20 fresh counterexamples; each source criterion rechecked once; account/connection destinations fully qualified.')
for card in re.split(r'^### J\d{2}-[POAC]\d{2}:', extended, flags=re.M)[1:]:
    assert '**Actor /' in card and re.search(r'composition', card, re.I), card[:100]
    assert re.search(r'actions', card, re.I), card[:100]
print(f'PASS: {len(state_ids)} unique defined states; all 20 source criteria exactly once; 18 author cases; 7 walkthroughs; {checked_links} local/internal links across 9 documents; balanced fences and unique headings.')
