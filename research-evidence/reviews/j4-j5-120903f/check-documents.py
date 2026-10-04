from pathlib import Path
from collections import Counter
import hashlib,json,re,subprocess
root=Path(r'D:\the next level\valiris-restaurants')
out=Path(__file__).parent
commit='120903f138a798e957b26498f2a3efb5d5e6521a'
jt='docs/design/m1-scheduling-and-service-continuity.md'
criteria='docs/product/m0-journeys-and-criteria.md'
matrix='docs/product/m0-capability-matrix.md'
def frozen(path,rev=commit):
    return subprocess.check_output(['git','show',f'{rev}:{path}'],cwd=root)
def anchors(s):
    return [re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in re.findall(r'^#{1,6} (.+)$',s,re.M)]
hashes={}
for p in [jt,criteria,matrix]:
    raw=frozen(p)
    hashes[p]=hashlib.sha256(raw).hexdigest()
    (out/(Path(p).stem+'.snapshot.md')).write_bytes(raw)
s=frozen(jt).decode('utf-8')
assert len(s.splitlines())==394
assert len(anchors(s))==len(set(anchors(s))) and s.count('```')%2==0
assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)',s,re.M)
width=None
for line in s.splitlines():
    if line.startswith('|'):
        n=len(line.split('|'))
        assert width is None or width==n,line
        width=n
    else: width=None
links=0
for link in re.findall(r'\]\(([^)]+)\)',s):
    if link.startswith(('http://','https://','mailto:')): continue
    dest,_,fragment=link.partition('#')
    target=((root/jt).parent/dest if dest else root/jt).resolve().relative_to(root).as_posix()
    target_text=frozen(target).decode('utf-8')
    if fragment: assert fragment in anchors(target_text),link
    links+=1
states=dict(re.findall(r'^### (JT-[OPX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)',s,re.M|re.S))
expected=[f'JT-O{i:02}' for i in range(1,16)]+['JT-P01','JT-P02']+[f'JT-X{i:02}' for i in range(1,5)]
assert list(states)==expected and len(re.findall(r'^### JT-[OPX]\d{2}:',s,re.M))==21
assert set(re.findall(r'JT-[OPX]\d{2}',s))<=set(states)
for name,card in states.items():
    for field in ['**Actor / objective / entry / version:','**Composition / copy:','**Actions / effect:','**Errors / recovery / check:']:
        assert field in card,(name,field)
cr=[f'J4.{i}' for i in range(1,5)]+[f'J5.{i}' for i in range(1,5)]
assert re.findall(r'^\| (J[45]\.\d) \|',s,re.M)==cr
source=frozen(criteria).decode('utf-8')
criterion_rows=lambda t:re.findall(r'^- \*\*J\d+\.\d:.*$',t,re.M)
assert criterion_rows(source)==criterion_rows(frozen(criteria,'9cfe77b').decode('utf-8'))
assert set(cr)<=set(re.findall(r'^- \*\*(J\d+\.\d):',source,re.M))
caps=re.findall(r'^\| (B\d\.\d{2}) \|',s,re.M)
assert caps==['B1.02']+[f'B2.{i:02}' for i in range(1,10)]+[f'B4.{i:02}' for i in range(3,10)]+['B4.11','B5.04','B7.07']
for tag,n in [('TC',30),('TW',6),('TF',3)]:
    assert re.findall(r'^\| ('+tag+r'\d{2}) ',s,re.M)==[f'{tag}{i:02}' for i in range(1,n+1)]
protected=[matrix,'docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md']
protected+=['docs/adr/'+p.name for p in (root/'docs/adr').glob('*.md') if re.match(r'0005-|0008-|0009-|0010-|0011-|0012-',p.name)]
for p in protected: assert frozen(p)==frozen(p,'9cfe77b'),p
parents=[r for r in frozen(matrix).decode('utf-8').splitlines() if re.match(r'^\| B\d\.\d{2} /',r)]
scope=Counter(re.search(r'\| (Included|Configurable|Connection-dependent) \|',r).group(1) for r in parents)
assert len(parents)==72 and scope=={'Included':36,'Configurable':30,'Connection-dependent':6}
prior=['m1-connected-journey.md','m1-content-preparation.md','m1-extended-journeys.md','m1-service-and-maintenance.md','m1-public-presence-and-discovery.md']
previous_rows=0
for name in prior:
    path='docs/design/'+name
    old=frozen(path,'9cfe77b').decode('utf-8'); now=frozen(path).decode('utf-8')
    contrasts=lambda t:re.findall(r'^\| (?:V\d{2}|Q\d{2}|PC\d{2}|DS\d{2}|SC\d{2}|LC\d{2}|VC\d{2}) .*$',t,re.M)
    assert contrasts(old)==contrasts(now),path
    previous_rows+=len(contrasts(now))
assert previous_rows==122
subprocess.run(['git','diff','--check','9cfe77b',commit],cwd=root,check=True)
result={'date':'2026-10-02','baseline':commit,'source_sha256':hashes,'jt_lines':394,'jt_local_links':links,'states':expected,'criteria':cr,'affected_caps':caps,'tc':30,'tw':6,'tf':3,'unchanged_prior_contrast_rows':previous_rows,'source_criteria_and_protected_sources_preserved':True,'matrix_parents':72,'scope_counts':dict(scope),'whitespace_check':True,'scope':'Frozen-document integrity and preservation; manual G1/G4 semantic review separate. No software or real-use tests.'}
(out/'document-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['states','affected_caps','source_sha256']},ensure_ascii=False,indent=2))
