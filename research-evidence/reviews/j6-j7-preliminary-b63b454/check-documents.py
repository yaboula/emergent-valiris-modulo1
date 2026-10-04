"""Immutable documentary integrity for G1/G4 J6-J7; not product tests."""
from pathlib import Path
from collections import Counter
import hashlib,json,re,subprocess,sys

root=Path(r'D:\the next level\valiris-restaurants')
commit='120903f138a798e957b26498f2a3efb5d5e6521a'
assert re.fullmatch(r'[0-9a-f]{40}',commit)
out=Path(__file__).parent
out.mkdir(parents=True,exist_ok=True)
fo='docs/design/m1-food-register-and-outputs.md'
criteria='docs/product/m0-journeys-and-criteria.md'
matrix='docs/product/m0-capability-matrix.md'
def frozen(path,rev=commit):
    if path==fo:
        return (out/'m1-food-register-and-outputs.snapshot.md').read_bytes()
    return subprocess.check_output(['git','show',f'{rev}:{path}'],cwd=root)
def anchors(s):
    return [re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in re.findall(r'^#{1,6} (.+)$',s,re.M)]
hashes={}
for p in [fo,criteria,matrix]:
    raw=frozen(p);hashes[p]=hashlib.sha256(raw).hexdigest()
    (out/(Path(p).stem+'.snapshot.md')).write_bytes(raw)
s=frozen(fo).decode('utf-8')
assert len(anchors(s))==len(set(anchors(s))) and s.count('```')%2==0
assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)',s,re.M)
width=None
for line in s.splitlines():
    if line.startswith('|'):
        n=len(line.split('|'));assert width is None or width==n,line
        width=n
    else:width=None
links=0
for link in re.findall(r'\]\(([^)]+)\)',s):
    if link.startswith(('http://','https://','mailto:')):continue
    dest,_,fragment=link.partition('#')
    path=((root/fo).parent/dest if dest else root/fo).resolve().relative_to(root).as_posix()
    target=frozen(path).decode('utf-8')
    if fragment:assert fragment in anchors(target),link
    links+=1
cards=dict(re.findall(r'^### (FO-[FOQX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)',s,re.M|re.S))
expected=[f'FO-F{i:02}' for i in range(1,7)]+[f'FO-O{i:02}' for i in range(1,7)]+[f'FO-Q{i:02}' for i in range(1,4)]+[f'FO-X{i:02}' for i in range(1,4)]
assert list(cards)==expected and len(re.findall(r'^### FO-[FOQX]\d{2}:',s,re.M))==18
assert set(re.findall(r'FO-[FOQX]\d{2}',s))<=set(cards)
for name,card in cards.items():
    for field in ['**Actor / objective / entry / version:','**Composition / copy:','**Actions / effect:','**Errors / recovery / check:']:
        assert field in card,(name,field)
cr=[f'J6.{i}' for i in range(1,4)]+[f'J7.{i}' for i in range(1,5)]
assert re.findall(r'^\| (J[67]\.\d) \|',s,re.M)==cr
source=frozen(criteria).decode('utf-8')
criterion_rows=lambda t:re.findall(r'^- \*\*J\d+\.\d:.*$',t,re.M)
assert criterion_rows(source)==criterion_rows(frozen(criteria,'120903f').decode('utf-8'))
assert set(cr)<=set(re.findall(r'^- \*\*(J\d+\.\d):',source,re.M))
caps=re.findall(r'^\| (B\d\.\d{2}) \|',s,re.M)
assert caps==['B4.05','B4.06','B4.08','B4.09','B4.11']+[f'B5.{i:02}' for i in range(1,10)]+[f'B6.{i:02}' for i in range(1,7)]+['B6.10','B7.07']
for tag,n in [('FC',24),('FW',5)]:
    assert re.findall(r'^\| ('+tag+r'\d{2}) ',s,re.M)==[f'{tag}{i:02}' for i in range(1,n+1)]
protected=[matrix,'docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md']
protected+=['docs/adr/'+p.name for p in (root/'docs/adr').glob('*.md') if re.match(r'0005-|0008-|0009-|0010-|0011-|0012-',p.name)]
for path in protected:assert frozen(path)==frozen(path,'120903f'),path
parents=[r for r in frozen(matrix).decode('utf-8').splitlines() if re.match(r'^\| B\d\.\d{2} /',r)]
scope=Counter(re.search(r'\| (Included|Configurable|Connection-dependent) \|',r).group(1) for r in parents)
assert len(parents)==72 and scope=={'Included':36,'Configurable':30,'Connection-dependent':6}
prior=['m1-connected-journey.md','m1-content-preparation.md','m1-extended-journeys.md','m1-service-and-maintenance.md','m1-public-presence-and-discovery.md','m1-scheduling-and-service-continuity.md']
previous_rows=0
for name in prior:
    path='docs/design/'+name
    old=frozen(path,'120903f').decode('utf-8');now=frozen(path).decode('utf-8')
    contrasts=lambda t:re.findall(r'^\| (?:V\d{2}|Q\d{2}|PC\d{2}|DS\d{2}|SC\d{2}|LC\d{2}|VC\d{2}|TC\d{2}) .*$',t,re.M)
    assert contrasts(old)==contrasts(now),path
    previous_rows+=len(contrasts(now))
    state_bodies=lambda t:re.findall(r'^### ((?:CP|PV|JT)-[A-Z]\d{2}|J(?:1[0-5]|[89])-[A-Z]\d{2}|[OPX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)',t,re.M|re.S)
    assert state_bodies(old)==state_bodies(now),('prior card bodies',path)
assert previous_rows==152
subprocess.run(['git','diff','--check','120903f',commit],cwd=root,check=True)
result={'date':'2026-10-02','source_baseline':commit,'fo_snapshot_sha256':'b63b4545ba6a5fa481054d8c3448a5a5d72951bbd261559db83ca4c2960f5c38','fo_not_committed':True,'review_status':'Preliminary; G2 authoring interrupted before final delivery','source_sha256':hashes,'fo_lines':len(s.splitlines()),'fo_local_links':links,'states':expected,'criteria':cr,'affected_caps':caps,'fc':24,'fw':5,'unchanged_prior_contrast_rows':previous_rows,'prior_card_bodies_preserved':True,'source_criteria_and_protected_sources_preserved':True,'matrix_parents':72,'scope_counts':dict(scope),'whitespace_check':True,'scope':'Frozen-document integrity only. Manual G1/G4 semantic review separate; no software, food, file, print, QR or real-use validation.'}
(out/'document-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['states','affected_caps','source_sha256']},ensure_ascii=False,indent=2))
