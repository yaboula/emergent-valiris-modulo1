from pathlib import Path
from collections import Counter
import hashlib, json, re, subprocess

root = Path(r'D:\the next level\valiris-restaurants')
out = Path(__file__).parent
commit = '2eb8e86831c4c00315078b5442e20fc5273150c9'
paths = [
    'docs/design/m1-content-preparation.md',
    'docs/adr/0011-shared-menu-content-and-contextual-maintenance.md',
    'docs/product/m0-journeys-and-criteria.md',
    'docs/design/m1-connected-journey.md',
    'docs/design/m1-extended-journeys.md',
    'docs/product/m0-capability-matrix.md',
    'docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md',
]

def frozen(path, rev=commit):
    return subprocess.check_output(['git', 'show', f'{rev}:{path}'], cwd=root)

def anchors(text):
    return [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
            for h in re.findall(r'^#{1,6} (.+)$', text, re.M)]

source_hashes = {}
for index, path in enumerate(paths):
    raw = frozen(path)
    assert raw.replace(b'\r\n', b'\n') == (root / path).read_bytes().replace(b'\r\n', b'\n'), ('checkout content differs', path)
    source_hashes[path] = hashlib.sha256(raw).hexdigest()
    if index < 3:
        (out / (Path(path).stem + '.snapshot.md')).write_bytes(raw)

cp = frozen(paths[0]).decode('utf-8')
adr = frozen(paths[1]).decode('utf-8')
links = 0
for path, text in [(paths[0], cp), (paths[1], adr)]:
    hs = anchors(text)
    assert len(hs) == len(set(hs)), ('duplicate heading', path)
    assert text.count('```') % 2 == 0
    assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)', text, re.M)
    width = None
    for line in text.splitlines():
        if line.startswith('|'):
            current = len(line.split('|'))
            assert width is None or width == current, ('table', path, line)
            width = current
        else:
            width = None
    for link in re.findall(r'\]\(([^)]+)\)', text):
        if link.startswith(('https://', 'http://', 'mailto:')):
            continue
        dest, _, frag = link.partition('#')
        target = (root / path).parent / dest if dest else root / path
        assert target.exists(), (path, link)
        if frag:
            assert frag in anchors(target.read_text(encoding='utf-8')), (path, link)
        links += 1

cards = lambda text: dict(re.findall(r'^### (CP-[IRAGSMBX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)', text, re.M | re.S))
states = cards(cp)
assert len(states) == 27
assert len(re.findall(r'^### CP-[IRAGSMBX]\d{2}:', cp, re.M)) == 27
assert set(re.findall(r'CP-[IRAGSMBX]\d{2}', cp)) <= set(states)
for key, card in states.items():
    for field in ['**Actor / objective / entry / version:', '**Composition / copy:', '**Actions / effect:', '**Errors / recovery / check:']:
        assert field in card, (key, field)
expected = [f'J3.{i}' for i in range(1, 7)] + ['J4.1', 'J4.4', 'J5.2', 'J5.4', 'J6.1', 'J6.2', 'J6.3', 'J7.3']
actual = re.findall(r'^\| (J[3-7]\.\d) \|', cp, re.M)
assert actual == expected
criteria = frozen(paths[2]).decode('utf-8')
assert set(expected) <= set(re.findall(r'^- \*\*(J\d+\.\d):', criteria, re.M))
caps = re.findall(r'^\| (B[45]\.\d{2}) \|', cp, re.M)
assert caps == [f'B4.{i:02}' for i in range(1, 12)] + [f'B5.{i:02}' for i in range(2, 10)]
for tag, count in [('PC', 24), ('PW', 5), ('DS', 4)]:
    assert re.findall(r'^\| (' + tag + r'\d{2}) ', cp, re.M) == [f'{tag}{i:02}' for i in range(1, count + 1)]
assert states == cards(frozen(paths[0], 'c4f219c').decode('utf-8'))
for path in [paths[5], paths[6], 'docs/adr/0008-first-launch-capability-commitment.md', 'docs/adr/0009-studio-design-and-registered-diner-personalisation.md']:
    assert frozen(path) == frozen(path, 'c4f219c'), ('protected source changed', path)
matrix = frozen(paths[5]).decode('utf-8')
assert len(re.findall(r'^\| B\d\.\d{2} /', matrix, re.M)) == 72
scope = Counter(re.search(r'\| (Included|Configurable|Connection-dependent) \|', row).group(1)
                for row in matrix.splitlines() if re.match(r'^\| B\d\.\d{2} /', row))
assert scope == {'Included': 36, 'Configurable': 30, 'Connection-dependent': 6}
assert not subprocess.check_output(['git', 'status', '--porcelain'], cwd=root).strip()
subprocess.run(['git', 'diff', '--check', 'c4f219c', commit], cwd=root, check=True)
result = {'date': '2026-10-02', 'baseline': commit, 'source_sha256': source_hashes,
          'checkout_matches_git_after_line_ending_normalization': True,
          'local_link_occurrences_cp_and_adr': links, 'states': 27, 'criterion_mappings': actual,
          'affected_capability_rows': caps, 'pc': 24, 'walkthroughs': 5, 'ds': 4,
          'cp_state_bodies_unchanged_from_c4f219c': True,
          'matrix_parents': 72, 'scope_counts': dict(scope), 'protected_sources_unchanged': True,
          'repo_clean': True, 'whitespace_check': True,
          'scope': 'Document integrity. Manual independent G4 and G1 reasoning recorded separately; no software, UX or capability completion.'}
(out / 'document-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}, ensure_ascii=False, indent=2))
