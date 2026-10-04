from pathlib import Path
from collections import Counter
import re
import subprocess

root = Path(r'D:\the next level\valiris-restaurants')
paths = [
    'docs/design/m1-content-preparation.md',
    'docs/design/m1-connected-journey.md',
    'docs/design/m1-extended-journeys.md',
    'docs/adr/0011-shared-menu-content-and-contextual-maintenance.md',
    'docs/adr/0010-diner-account-and-display-recovery.md',
    'docs/adr/README.md', 'docs/README.md',
    'docs/product/m1-design-briefs.md',
    'docs/product/m0-journeys-and-criteria.md',
    'docs/project/roadmap.md', 'docs/project/m0-closeout.md',
    'CHANGELOG.md',
]

def anchors(doc):
    return [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
            for h in re.findall(r'^#{1,6} (.+)$', doc, re.M)]

links = 0
for name in paths:
    path = root / name
    doc = path.read_text(encoding='utf-8')
    assert doc.count('```') % 2 == 0, ('fences', name)
    headings = anchors(doc)
    assert len(headings) == len(set(headings)), ('headings', name)
    assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)', doc, re.M), name
    table_width = None
    for line in doc.splitlines():
        if line.startswith('|'):
            # All table cells here use no escaped pipes.
            width = len(line.split('|'))
            if table_width is None:
                table_width = width
            assert width == table_width, ('table', name, line)
        else:
            table_width = None
    for link in re.findall(r'\]\(([^)]+)\)', doc):
        if link.startswith(('http://', 'https://', 'mailto:')):
            continue
        target_name, _, fragment = link.partition('#')
        target = path.parent / target_name if target_name else path
        assert target.exists(), (name, link)
        if fragment:
            assert fragment in anchors(target.read_text(encoding='utf-8')), (name, link)
        links += 1

doc = (root / paths[0]).read_text(encoding='utf-8')
ids = re.findall(r'^### (CP-[IRAGSMBX]\d{2}):', doc, re.M)
assert len(ids) == len(set(ids)) == 27, ids
assert set(re.findall(r'CP-[IRAGSMBX]\d{2}', doc)) <= set(ids), 'undefined CP state'
cards = re.findall(r'^### (CP-[IRAGSMBX]\d{2}):[^\n]+\n(.*?)(?=^### |^## |\Z)', doc, re.M | re.S)
assert len(cards) == 27
for state, content in cards:
    for label in ['**Actor / objective / entry / version:', '**Composition / copy:',
                  '**Actions / effect:', '**Errors / recovery / check:']:
        assert label in content, (state, label)
    assert re.search(r'→|\]\(', content), ('destination', state)

expected = [f'J3.{i}' for i in range(1, 7)] + ['J4.1', 'J4.4', 'J5.2', 'J5.4', 'J6.1', 'J6.2', 'J6.3', 'J7.3']
criteria = re.findall(r'^\| (J[3-7]\.\d) \|', doc, re.M)
assert criteria == expected, criteria
source = (root / 'docs/product/m0-journeys-and-criteria.md').read_text(encoding='utf-8')
assert set(expected) <= set(re.findall(r'^- \*\*(J\d+\.\d):', source, re.M))
capabilities = re.findall(r'^\| (B[45]\.\d{2}) \|', doc, re.M)
expected_caps = [f'B4.{i:02}' for i in range(1, 12)] + [f'B5.{i:02}' for i in range(2, 10)]
assert capabilities == expected_caps, capabilities
for prefix, count in [('PC', 24), ('PW', 5), ('PF', 3)]:
    found = re.findall(r'^\| (' + prefix + r'\d{2}) ', doc, re.M)
    assert found == [f'{prefix}{i:02}' for i in range(1, count + 1)], found

assert re.findall(r'^\| (DS\d{2}) ', doc, re.M) == [f'DS{i:02}' for i in range(1, 5)]
baseline = '60d76ad'
def original(name):
    return subprocess.check_output(['git', 'show', f'{baseline}:{name}'], cwd=root).decode('utf-8')
for name, prefix in [('docs/design/m1-connected-journey.md', 'V'),
                     ('docs/design/m1-extended-journeys.md', 'Q')]:
    current = (root / name).read_text(encoding='utf-8')
    old_rows = re.findall(r'^\| ' + prefix + r'\d{2} .*$', original(name), re.M)
    new_rows = re.findall(r'^\| ' + prefix + r'\d{2} .*$', current, re.M)
    assert old_rows == new_rows, ('changed prior cases', name)
    assert len(old_rows) == (16 if prefix == 'V' else 20)

prior_source = original('docs/product/m0-journeys-and-criteria.md')
criterion_rows = lambda s: re.findall(r'^- \*\*J\d+\.\d:.*$', s, re.M)
assert criterion_rows(source) == criterion_rows(prior_source), 'changed source criteria'
for name in ['docs/product/m0-capability-matrix.md',
             'docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md',
             'docs/adr/0008-first-launch-capability-commitment.md',
             'docs/adr/0009-studio-design-and-registered-diner-personalisation.md']:
    assert (root / name).read_text(encoding='utf-8') == original(name), ('changed accepted/source document', name)

coverage = (root / 'docs/design/m1-connected-journey.md').read_text(encoding='utf-8').split('## 7.', 1)[1].split('## 8.', 1)[0]
expanded = []
for row in coverage.splitlines():
    if not row.startswith('| B'):
        continue
    field = row.split('|')[1]
    def expand(m):
        left, start, right, end = m.groups()
        assert left == right
        expanded.extend(f'{left}.{i:02}' for i in range(int(start), int(end)+1))
        return ''
    remaining = re.sub(r'(B\d)\.(\d{2})–(B\d)\.(\d{2})', expand, field)
    expanded.extend(re.findall(r'B\d\.\d{2}', remaining))
matrix = (root / 'docs/product/m0-capability-matrix.md').read_text(encoding='utf-8')
assert len(expanded) == len(set(expanded)) == 72
assert set(expanded) == set(re.findall(r'B\d\.\d{2}', matrix))
assert 'Separate S1:' in coverage and 'Separate S2:' in coverage
print(f'PASS: 27 unique defined cards with all required fields; 14 unchanged-source criterion mappings; 19 capability rows; 24 contrasts/5 walkthroughs/3 corrections; {links} local/internal links across 12 documents; tables/headings/fences valid.')
print('PASS: all 16 V and 20 Q rows preserved; source criteria/matrix/functional definition/accepted ADRs unchanged; 72 parent IDs exactly once and separate S1/S2 preserved. Documentary integrity only, no software/real interaction or independent validation.')
