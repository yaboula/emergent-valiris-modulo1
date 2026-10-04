from pathlib import Path
from collections import Counter
import hashlib, json, re, subprocess

root = Path(r'D:\the next level\valiris-restaurants')
out = Path(__file__).parent
commit = '9cfe77ba652d8b22b412f69a93d24987a9201098'
paths = [
    'docs/design/m1-service-and-maintenance.md',
    'docs/adr/0012-confirm-delegated-updates-per-assignment.md',
    'docs/product/m0-journeys-and-criteria.md',
    'docs/design/m1-connected-journey.md',
    'docs/design/m1-content-preparation.md',
    'docs/design/m1-extended-journeys.md',
    'docs/product/m0-capability-matrix.md',
]

def frozen(path, rev=commit):
    return subprocess.check_output(['git', 'show', f'{rev}:{path}'], cwd=root)

def anchors(text):
    return [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
            for h in re.findall(r'^#{1,6} (.+)$', text, re.M)]

hashes, checkout_hashes = {}, {}
for i, path in enumerate(paths):
    raw = frozen(path)
    local = (root / path).read_bytes()
    assert raw.replace(b'\r\n', b'\n') == local.replace(b'\r\n', b'\n'), ('checkout content differs', path)
    hashes[path] = hashlib.sha256(raw).hexdigest()
    checkout_hashes[path] = hashlib.sha256(local).hexdigest()
    if i < 3:
        (out / (Path(path).stem + '.snapshot.md')).write_bytes(raw)

text = frozen(paths[0]).decode('utf-8')
adr = frozen(paths[1]).decode('utf-8')
links = 0
for path, s in [(paths[0], text), (paths[1], adr)]:
    hs = anchors(s)
    assert len(hs) == len(set(hs))
    assert s.count('```') % 2 == 0
    assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)', s, re.M)
    width = None
    for line in s.splitlines():
        if line.startswith('|'):
            current = len(line.split('|'))
            assert width is None or width == current, ('table', path, line)
            width = current
        else:
            width = None
    for link in re.findall(r'\]\(([^)]+)\)', s):
        if link.startswith(('http://', 'https://', 'mailto:')):
            continue
        dest, _, frag = link.partition('#')
        target = (root / path).parent / dest if dest else root / path
        assert target.exists(), (path, link)
        if frag:
            assert frag in anchors(target.read_text(encoding='utf-8')), (path, link)
        links += 1

cards = lambda s: dict(re.findall(r'^### (J[89]-[SMUX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)', s, re.M | re.S))
states = cards(text)
assert len(states) == len(re.findall(r'^### J[89]-[SMUX]\d{2}:', text, re.M)) == 22
assert set(re.findall(r'J[89]-[SMUX]\d{2}', text)) <= set(states)
for name, card in states.items():
    for field in ['**Actor / objective / entry / version:', '**Composition / copy:', '**Actions / effect:', '**Errors / recovery / check:']:
        assert field in card, (name, field)
expected = [f'J8.{i}' for i in range(1, 5)] + [f'J9.{i}' for i in range(1, 4)]
criteria = re.findall(r'^\| (J[89]\.\d) \|', text, re.M)
assert criteria == expected
source = frozen(paths[2]).decode('utf-8')
source_rows = lambda s: re.findall(r'^- \*\*J\d+\.\d:.*$', s, re.M)
assert set(expected) <= set(re.findall(r'^- \*\*(J\d+\.\d):', source, re.M))
assert source_rows(source) == source_rows(frozen(paths[2], '2eb8e86').decode('utf-8'))
caps = re.findall(r'^\| (B\d\.\d{2}) \|', text, re.M)
assert caps == ['B1.06', 'B1.07', 'B1.08', 'B6.11'] + [f'B7.{i:02}' for i in range(1, 11)]
for tag, count in [('SC', 26), ('SW', 5)]:
    assert re.findall(r'^\| (' + tag + r'\d{2}) ', text, re.M) == [f'{tag}{i:02}' for i in range(1, count + 1)]
old = frozen(paths[0], '2eb8e86').decode('utf-8')
assert states == cards(old)
assert re.findall(r'^\| SC\d{2} .*$', text, re.M) == re.findall(r'^\| SC\d{2} .*$', old, re.M)
for path in [paths[1], paths[6], 'docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md', 'docs/adr/0008-first-launch-capability-commitment.md', 'docs/adr/0009-studio-design-and-registered-diner-personalisation.md']:
    assert frozen(path) == frozen(path, '2eb8e86'), ('protected source changed', path)
matrix = frozen(paths[6]).decode('utf-8')
parents = [row for row in matrix.splitlines() if re.match(r'^\| B\d\.\d{2} /', row)]
assert len(parents) == 72
scope = Counter(re.search(r'\| (Included|Configurable|Connection-dependent) \|', row).group(1) for row in parents)
assert scope == {'Included': 36, 'Configurable': 30, 'Connection-dependent': 6}
assert not subprocess.check_output(['git', 'status', '--porcelain'], cwd=root).strip()
subprocess.run(['git', 'diff', '--check', '2eb8e86', commit], cwd=root, check=True)
result = {'date': '2026-10-02', 'baseline': commit, 'git_lf_source_sha256': hashes, 'checkout_sha256': checkout_hashes,
          'normalized_checkout_matches_git': True, 'local_links_service_and_adr12': links,
          'states': 22, 'criterion_mappings': criteria, 'affected_capability_rows': caps, 'sc': 26, 'sw': 5,
          'states_and_sc_unchanged_from_2eb8e86': True, 'criteria_and_protected_sources_unchanged': True,
          'matrix_parents': 72, 'scope_counts': dict(scope), 'repo_clean': True, 'whitespace_check': True,
          'scope': 'Document integrity only. G1/G4 manual reasoning is separate; no software, service, UX or capability completion.'}
(out / 'document-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in result.items() if 'sha256' not in k}, ensure_ascii=False, indent=2))
