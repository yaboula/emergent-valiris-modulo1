from pathlib import Path, PurePosixPath
import subprocess, re, json, hashlib, collections, posixpath

root = Path(r'D:\the next level')
repo = root / 'valiris-restaurants'
out = root / 'research-evidence/reviews/coverage-d71d3de'
base = 'd71d3de81d611b76d2d80aab86ead119b34b0a0d'
previous = 'a0583e0ec04e310f6736f1d763ca4d7a78191973'
out.mkdir(parents=True, exist_ok=True)

def git(*args):
    return subprocess.check_output(['git', *args], cwd=repo)
tree = git('ls-tree', '-r', '--name-only', base).decode().splitlines()
cache = {}
def raw(name, ref=base):
    if (ref, name) not in cache:
        cache[(ref, name)] = git('show', ref + ':' + name)
    return cache[(ref, name)]
def text(name, ref=base):
    return raw(name, ref).decode('utf-8').replace('\r\n', '\n')
def anchors(s):
    return [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in re.findall(r'^#{1,6} (.+)$', s, re.M)]
paths = [p for p in tree if p.startswith('docs/design/') and p.endswith('.md')] + [
    'docs/README.md', 'CHANGELOG.md', 'docs/product/m1-design-briefs.md',
    'docs/product/m0-journeys-and-criteria.md', 'docs/project/roadmap.md',
    'docs/project/m0-closeout.md', 'docs/adr/README.md',
    'docs/adr/0010-diner-account-and-display-recovery.md',
    'docs/adr/0011-shared-menu-content-and-contextual-maintenance.md',
    'docs/adr/0012-confirm-delegated-updates-per-assignment.md']
state_rx = r'^### ((?:FO|PV|CP|JT|J\d+)-[A-Z]\d{2}|[OPX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)'
link_count = 0
case_links = []
states = {}
for name in paths:
    s = text(name)
    dest = out / 'snapshots' / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        assert dest.read_bytes() == raw(name), ('Snapshot collision', name)
    else:
        dest.write_bytes(raw(name))
    a = anchors(s)
    assert len(a) == len(set(a)), ('Duplicate anchor', name)
    assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)', s, re.M)
    assert s.count('```') % 2 == 0, ('Fence', name)
    width = None
    for line in s.splitlines():
        if line.startswith('|') and line.endswith('|'):
            w = len(re.split(r'(?<!\\)\|', line))
            assert width is None or width == w, ('Table width', name, line)
            width = w
        else:
            width = None
    for match in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', s):
        label, ref = match.groups()
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', ref):
            continue
        filename, _, fragment = ref.strip('<>').partition('#')
        target = posixpath.normpath(str(PurePosixPath(name).parent / filename)) if filename else name
        assert target in tree, ('Missing Git target', name, ref)
        if fragment:
            assert fragment in anchors(text(target)), ('Missing Git fragment', name, ref)
        link_count += 1
        if name in ('docs/design/m1-connected-journey.md', 'docs/design/m1-coverage-and-evidence.md') and re.fullmatch(r'(?:V|Q|PC|DS|SC|LC|VC|TC|FC)\d{2}', label):
            found = re.findall(r'^\| ' + re.escape(label) + r'(?:\s|\|).*$', text(target), re.M)
            assert len(found) == 1, ('Case label not an actual unique case in target', name, label, target, len(found))
            case_links.append({'source': name, 'source_line': s[:match.start()].count('\n') + 1, 'case': label, 'target': target, 'target_line': text(target)[:text(target).index(found[0])].count('\n') + 1})
    for sid, body in re.findall(state_rx, s, re.M | re.S):
        assert sid not in states, ('Repeated state ID', sid)
        states[sid] = {'source': name, 'body': body}

matrix_name = 'docs/product/m0-capability-matrix.md'
definition_name = 'docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md'
matrix = {}
for line in text(matrix_name).splitlines():
    if re.match(r'^\| B\d\.\d{2} /', line):
        cells = [c.strip() for c in line.split('|')[1:-1]]
        matrix[cells[0].split(' /')[0]] = {'name': cells[1], 'treatment': cells[3], 'source_commitment': cells[4]}
map_name = 'docs/design/m1-connected-journey.md'
report_name = 'docs/design/m1-coverage-and-evidence.md'
capabilities = []
for n, line in enumerate(text(map_name).splitlines(), 1):
    if not re.match(r'^\| B\d\.\d{2} ', line):
        continue
    cells = [c.strip() for c in line.split('|')[1:-1]]
    cap = cells[0].split(' ')[0]
    assert cells[0] == cap + ' · ' + matrix[cap]['name'] + ' / ' + matrix[cap]['treatment'], cap
    concrete = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', cells[2])
    for sid, ref in concrete:
        assert sid in states, (cap, sid)
        filename = ref.split('#')[0]
        assert states[sid]['source'] == 'docs/design/' + filename, (cap, sid, ref)
    capabilities.append({'id': cap, 'map_line': n, **matrix[cap], 'author_status': cells[1], 'states': [v[0] for v in concrete], 'criteria': re.findall(r'J\d+\.\d', cells[3]), 'cases': re.findall(r'\[((?:V|Q|PC|DS|SC|LC|VC|TC|FC)\d{2})\]', cells[3]), 'review_refs': re.findall(r'\[(RV\d{2})\]', cells[4]), 'gap_refs': re.findall(r'\[(CG\d{2}(?:\.\d)?)\]', cells[5])})
assert [c['id'] for c in capabilities] == list(matrix) and len(capabilities) == 72
assert collections.Counter(c['treatment'] for c in capabilities) == {'Included': 36, 'Configurable': 30, 'Connection-dependent': 6}
assert collections.Counter(c['author_status'] for c in capabilities) == {'Sufficient written path': 69, 'Partial: visual expression missing': 3}

source = 'docs/product/m0-journeys-and-criteria.md'
criteria = re.findall(r'^- \*\*(J\d+\.\d):', text(source), re.M)
criterion_rows = []
for n, line in enumerate(text(report_name).splitlines(), 1):
    if re.match(r'^\| J\d+\.\d \|', line):
        cells = [c.strip() for c in line.split('|')[1:-1]]
        labels = lambda c: re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', c)
        criterion_rows.append({'id': cells[0], 'report_line': n, 'states': labels(cells[1]), 'cases': labels(cells[2]), 'review_and_gaps': labels(cells[3])})
assert [c['id'] for c in criterion_rows] == criteria and len(criteria) == 59
review_ids = re.findall(r'^### (RV\d{2})$', text(report_name), re.M)
gap_ids = re.findall(r'^### (CG\d{2}(?:\.\d)?)$', text(report_name), re.M)
assert len(review_ids) == 7 and len(gap_ids) == 17
for c in capabilities:
    assert all(i in criteria for i in c['criteria'])
    assert c['review_refs'] and set(c['review_refs']) <= set(review_ids)
    assert c['gap_refs'] and set(c['gap_refs']) <= set(gap_ids)

prior_cases = 0
for name in [p for p in paths if p.startswith('docs/design/') and p != report_name]:
    old_cards = dict(re.findall(state_rx, text(name, previous), re.M | re.S))
    new_cards = dict(re.findall(state_rx, text(name), re.M | re.S))
    assert old_cards == new_cards, ('Inherited state body changed', name)
    rx = r'^\| (?:V|Q|PC|DS|SC|LC|VC|TC|FC)\d{2}(?:\s|\|).*$'
    earlier = re.findall(rx, text(name, previous), re.M)
    assert earlier == re.findall(rx, text(name), re.M), ('Inherited contrast changed', name)
    prior_cases += len(earlier)
assert prior_cases == 176, prior_cases
original_criteria = lambda s: re.findall(r'^- \*\*J\d+\.\d:.*$', s, re.M)
assert original_criteria(text(source)) == original_criteria(text(source, previous))
protected = [matrix_name, definition_name] + [p for p in tree if p.startswith('docs/adr/') and p.endswith('.md')]
for name in protected:
    assert raw(name) == raw(name, previous), ('Protected source changed', name)
    dest = out / 'snapshots' / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw(name))
assert 'Separate S1:' in text(map_name) and 'Separate S2:' in text(map_name)
subprocess.run(['git', 'diff', '--check', previous, base], cwd=repo, check=True, capture_output=True)
checks = {'date': '2026-10-02', 'baseline': base, 'compared_to': previous, 'documents_checked': len(paths), 'local_git_links': link_count, 'actual_case_label_target_checks': len(case_links), 'capability_rows': 72, 'source_criteria': 59, 'status_counts_author_only': dict(collections.Counter(c['author_status'] for c in capabilities)), 'scope_counts': dict(collections.Counter(c['treatment'] for c in capabilities)), 'bounded_reviews': 7, 'gap_locators': 17, 'inherited_state_bodies': len(states), 'inherited_contrasts_preserved': 176, 'source_criteria_protected_sources_unchanged': True, 'whitespace_check': True, 'source_sha256': {name: hashlib.sha256(raw(name)).hexdigest() for name in paths + protected}, 'limits': 'Frozen-document structural preservation and actual reference checks; manual G1/G4 semantic audit separate. Not UX, food, software, rendered accessibility or M1 acceptance.'}
for name, value in [('document-checks.json', checks), ('capability-reference-checks.json', capabilities), ('criterion-reference-checks.json', criterion_rows), ('actual-case-link-checks.json', case_links)]:
    (out / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in checks.items() if k != 'source_sha256'}, ensure_ascii=False))
