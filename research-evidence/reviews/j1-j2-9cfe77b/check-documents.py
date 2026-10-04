from pathlib import Path
from collections import Counter
import hashlib, json, re, subprocess

root = Path(r'D:\the next level\valiris-restaurants')
out = Path(__file__).parent
commit = '9cfe77ba652d8b22b412f69a93d24987a9201098'
pv = 'docs/design/m1-public-presence-and-discovery.md'
criteria_path = 'docs/product/m0-journeys-and-criteria.md'
matrix_path = 'docs/product/m0-capability-matrix.md'
paths = [pv, criteria_path, matrix_path,
    'docs/design/m1-connected-journey.md', 'docs/design/m1-content-preparation.md',
    'docs/design/m1-extended-journeys.md', 'docs/design/m1-service-and-maintenance.md',
    'docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md',
    'docs/adr/0005-repository-and-product-language.md',
    'docs/adr/0008-first-launch-capability-commitment.md',
    'docs/adr/0009-studio-design-and-registered-diner-personalisation.md']
def frozen(path, rev=commit):
    return subprocess.check_output(['git', 'show', f'{rev}:{path}'], cwd=root)
def anchors(s):
    return [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
            for h in re.findall(r'^#{1,6} (.+)$', s, re.M)]
hashes, checkout_matches = {}, {}
for i, path in enumerate(paths):
    raw, local = frozen(path), (root / path).read_bytes()
    checkout_matches[path] = raw.replace(b'\r\n', b'\n') == local.replace(b'\r\n', b'\n')
    hashes[path] = {'git_sha256': hashlib.sha256(raw).hexdigest(),
                    'checkout_sha256': hashlib.sha256(local).hexdigest()}
    if i < 3:
        (out / (Path(path).stem + '.snapshot.md')).write_bytes(raw)
text = frozen(pv).decode('utf-8')
assert len(text.splitlines()) == 342
assert len(anchors(text)) == len(set(anchors(text)))
assert text.count('```') % 2 == 0
assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)', text, re.M)
width = None
for line in text.splitlines():
    if line.startswith('|'):
        current = len(line.split('|'))
        assert width is None or width == current, line
        width = current
    else:
        width = None
links = 0
for link in re.findall(r'\]\(([^)]+)\)', text):
    if link.startswith(('http://', 'https://', 'mailto:')):
        continue
    dest, _, frag = link.partition('#')
    target = (root / pv).parent / dest if dest else root / pv
    target_path = target.resolve().relative_to(root).as_posix()
    target_text = frozen(target_path).decode('utf-8')
    if frag:
        assert frag in anchors(target_text), link
    links += 1
cards = lambda s: dict(re.findall(r'^### (PV-[POX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)', s, re.M | re.S))
states = cards(text)
expected_states = [f'PV-P{i:02}' for i in range(1, 12)] + [f'PV-O{i:02}' for i in range(1, 6)] + ['PV-X01']
assert list(states) == expected_states
assert len(re.findall(r'^### PV-[POX]\d{2}:', text, re.M)) == 17
assert set(re.findall(r'PV-[POX]\d{2}', text)) <= set(states)
for name, card in states.items():
    for field in ['**Actor / objective / entry / version:', '**Composition / copy:', '**Actions / effect:', '**Errors / recovery / check:']:
        assert field in card, (name, field)
expected_criteria = [f'J1.{i}' for i in range(1, 6)] + [f'J2.{i}' for i in range(1, 7)]
assert re.findall(r'^\| (J[12]\.\d) \|', text, re.M) == expected_criteria
source = frozen(criteria_path).decode('utf-8')
assert set(expected_criteria) <= set(re.findall(r'^- \*\*(J\d+\.\d):', source, re.M))
caps = re.findall(r'^\| (B\d\.\d{2}) \|', text, re.M)
assert caps == ['B1.01','B1.02','B1.03','B1.04','B1.05','B1.08','B1.09',
    'B3.01','B3.02','B3.03','B3.04','B3.05','B3.06','B3.07','B3.08','B3.10',
    'B5.01','B5.04','B5.05','B5.07','B6.01','B6.02','B6.03']
for tag, count in [('VC',26),('VW',6),('VF',4)]:
    assert re.findall(r'^\| ('+tag+r'\d{2}) ', text, re.M) == [f'{tag}{i:02}' for i in range(1,count+1)]
assert states == cards(frozen(pv, 'c5e0a5b').decode('utf-8'))
criterion_rows = lambda s: re.findall(r'^- \*\*J\d+\.\d:.*$',s,re.M)
assert criterion_rows(source) == criterion_rows(frozen(criteria_path,'2eb8e86').decode('utf-8'))
for path in [matrix_path] + paths[7:]:
    assert frozen(path) == frozen(path, '2eb8e86'), ('protected source changed', path)
parents = [r for r in frozen(matrix_path).decode('utf-8').splitlines() if re.match(r'^\| B\d\.\d{2} /',r)]
assert len(parents) == 72
scope = Counter(re.search(r'\| (Included|Configurable|Connection-dependent) \|',r).group(1) for r in parents)
assert scope == {'Included':36,'Configurable':30,'Connection-dependent':6}
subprocess.run(['git','diff','--check','c5e0a5b',commit],cwd=root,check=True)
status = subprocess.check_output(['git','status','--porcelain'],cwd=root).decode('utf-8').strip()
result = {'date':'2026-10-02','baseline':commit,'hashes':hashes,
    'normalized_checkout_matches_git_by_file':checkout_matches,'pv_local_links':links,'states':expected_states,
    'criterion_mappings':expected_criteria,'affected_capability_rows':caps,'vc':26,'vw':6,'vf':4,
    'state_bodies_unchanged_from_c5e0a5b':True,'source_criterion_rows_unchanged_from_2eb8e86':True,
    'matrix_functional_definition_and_accepted_adrs_unchanged_from_2eb8e86':True,
    'matrix_parents':72,'scope_counts':dict(scope),'whitespace_check':True,'observed_git_status':status,
    'scope':'Document integrity only. No software/UX/accessibility/real-use validation. Concurrent work preserved.'}
(out/'document-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k != 'hashes'},ensure_ascii=False,indent=2))
