from pathlib import Path
import json, hashlib, re, subprocess, urllib.parse, unicodedata
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'coordination/storage-migration-2026-10-03.json').read_text(encoding='utf-8'))
failures=[]
preserved=0
changed=[]
for r in data['files']:
    p=root/r['destination']
    if r['status']=='archived-only':
        assert not p.exists()
        continue
    sha=hashlib.sha256(p.read_bytes()).hexdigest()
    if sha!=r['current_sha256']: failures.append(dict(path=r['destination'], error='inventory-current-hash-mismatch'))
    if r['kind'] in ['immutable-original','immutable-evidence','supplied-recording','superseded-concept']:
        if sha!=r['source_sha256']: failures.append(dict(path=r['destination'],error='original-bytes-changed'))
        else: preserved+=1
    else: changed.append(r['destination'])

files=[root/'AGENTS.md',root/'HANDOFF.md',root/'README.md',root/'CONTRIBUTING.md',root/'docs/README.md',root/'coordination/README.md',root/'research-evidence/README.md']
files+=list((root/'coordination/valiris-restaurants').glob('*.md'))
files+=list((root/'docs').rglob('*.md'))
files=list(dict.fromkeys(files))
links=0
for p in files:
    text=p.read_text(encoding='utf-8-sig')
    for m in re.finditer(r'!?\[[^\]\n]*\]\((<[^>]+>|[^\)\n]+)\)',text):
        ref=m[1].strip().strip('<>')
        if re.match(r'^[a-zA-Z][\w+.-]*:',ref) or ref.startswith('//'): continue
        path,_,frag=ref.partition('#')
        target=(p.parent/urllib.parse.unquote(path)).resolve() if path else p
        links+=1
        if not target.exists():
            failures.append(dict(path=str(p.relative_to(root)),line=text[:m.start()].count('\n')+1,link=ref,error='missing-local-target'))

secret_files=[]
token=re.compile(r'\bgh[pousr]_[A-Za-z0-9]{30,}\b|\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')
for parent in ['coordination','research-evidence']:
    for p in (root/parent).rglob('*'):
        if not p.is_file() or p.suffix.lower() in ['.png','.jpg','.jpeg','.mp4','.pdf']:continue
        try: text=p.read_text(encoding='utf-8-sig')
        except UnicodeDecodeError:continue
        if token.search(text): secret_files.append(str(p.relative_to(root)))
if secret_files: failures.append(dict(error='credential-pattern-files',paths=secret_files))

protected=['docs/product/m0-capability-matrix.md','docs/product/m0-journeys-and-criteria.md','docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md']
protected+=subprocess.check_output(['git','ls-files','docs/adr'],cwd=root,text=True).splitlines()
protected_changed=subprocess.check_output(['git','diff','--name-only','b28ee63','--',*protected],cwd=root,text=True).splitlines()
if protected_changed: failures.append(dict(error='protected-product-source-changed',paths=protected_changed))
result=dict(date='2026-10-03',preserved_original_files=preserved,inventory_records=len(data['files']),operating_files_checked=len(files),local_link_targets_checked=links,failures=failures,secret_pattern_file_count=len(secret_files),protected_source_changes=protected_changed,scope='Migration integrity and local link targets only; no new UX, independent design, runtime, software or external URL validation.')
(root/'.cache').mkdir(exist_ok=True)
(root/'.cache/storage-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(failures))
