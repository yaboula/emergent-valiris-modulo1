from pathlib import Path
from collections import Counter
import re, subprocess

root = Path(r'D:\the next level\valiris-restaurants')
paths = [
 'docs/design/m1-service-and-maintenance.md',
 'docs/design/m1-connected-journey.md', 'docs/design/m1-content-preparation.md',
 'docs/design/m1-extended-journeys.md',
 'docs/adr/0012-confirm-delegated-updates-per-assignment.md',
 'docs/adr/0011-shared-menu-content-and-contextual-maintenance.md',
 'docs/adr/0010-diner-account-and-display-recovery.md',
 'docs/adr/README.md', 'docs/README.md', 'CHANGELOG.md',
 'docs/product/m1-design-briefs.md', 'docs/product/m0-journeys-and-criteria.md',
 'docs/project/roadmap.md', 'docs/project/m0-closeout.md',
]
def anchors(s):
 return [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in re.findall(r'^#{1,6} (.+)$', s, re.M)]
links=0
for name in paths:
 p=root/name
 s=p.read_text(encoding='utf-8')
 assert s.count('```')%2==0, ('fences',name)
 a=anchors(s)
 assert len(a)==len(set(a)), ('headings',name)
 assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)',s,re.M),name
 width=None
 for line in s.splitlines():
  if line.startswith('|'):
   current=len(line.split('|'))
   if width is None: width=current
   assert current==width,('table',name,line)
  else: width=None
 for link in re.findall(r'\]\(([^)]+)\)',s):
  if link.startswith(('https://','http://','mailto:')): continue
  dest,_,frag=link.partition('#')
  target=p.parent/dest if dest else p
  assert target.exists(),(name,link)
  if frag: assert frag in anchors(target.read_text(encoding='utf-8')),(name,link)
  links+=1
s=(root/paths[0]).read_text(encoding='utf-8')
states=re.findall(r'^### (J[89]-[SMUX]\d{2}):',s,re.M)
assert len(states)==len(set(states))==22,states
assert set(re.findall(r'J[89]-[SMUX]\d{2}',s))<=set(states),'undefined state'
for name,body in re.findall(r'^### (J[89]-[SMUX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)',s,re.M|re.S):
 for label in ['**Actor / objective / entry / version:', '**Composition / copy:', '**Actions / effect:', '**Errors / recovery / check:']:
  assert label in body,(name,label)
 assert '→' in body,('destination',name)
criteria=re.findall(r'^\| (J[89]\.\d) \|',s,re.M)
expected=[f'J8.{i}' for i in range(1,5)]+[f'J9.{i}' for i in range(1,4)]
assert criteria==expected,criteria
source=(root/'docs/product/m0-journeys-and-criteria.md').read_text(encoding='utf-8')
assert set(expected)<=set(re.findall(r'^- \*\*(J\d+\.\d):',source,re.M))
capabilities=re.findall(r'^\| (B[167]\.\d{2}) \|',s,re.M)
assert capabilities==['B1.06','B1.07','B1.08','B6.11']+[f'B7.{i:02}' for i in range(1,11)],capabilities
for prefix,count in [('SC',26),('SW',5)]:
 found=re.findall(r'^\| ('+prefix+r'\d{2}) ',s,re.M)
 assert found==[f'{prefix}{i:02}' for i in range(1,count+1)],found
for marker in ['SR01','SR02','SR03','G4-J15-01','G4-01','64']:
 assert marker in s,marker
baseline='c4f219c'
def original(name):
 return subprocess.check_output(['git','show',f'{baseline}:{name}'],cwd=root).decode('utf-8')
prior=0
for name,prefix,count in [
 ('docs/design/m1-connected-journey.md','V',16),
 ('docs/design/m1-extended-journeys.md','Q',20),
 ('docs/design/m1-content-preparation.md','PC',24),
 ('docs/design/m1-content-preparation.md','DS',4)]:
 pattern=r'^\| '+prefix+r'\d{2} .*$'
 old=re.findall(pattern,original(name),re.M)
 new=re.findall(pattern,(root/name).read_text(encoding='utf-8'),re.M)
 assert old==new and len(old)==count,('prior contrast changed',name,prefix)
 prior+=count
assert prior==64
rows=lambda s: re.findall(r'^- \*\*J\d+\.\d:.*$',s,re.M)
assert rows(source)==rows(original('docs/product/m0-journeys-and-criteria.md')),'changed source criteria'
for name in ['docs/product/m0-capability-matrix.md',
 'docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md',
 'docs/adr/0008-first-launch-capability-commitment.md',
 'docs/adr/0009-studio-design-and-registered-diner-personalisation.md',
 'docs/adr/0010-diner-account-and-display-recovery.md',
 'docs/adr/0011-shared-menu-content-and-contextual-maintenance.md']:
 assert (root/name).read_text(encoding='utf-8')==original(name),('changed source/decision',name)
doc=(root/'docs/design/m1-connected-journey.md').read_text(encoding='utf-8')
coverage=doc.split('## 7.',1)[1].split('## 8.',1)[0]
expanded=[]
for line in coverage.splitlines():
 if not line.startswith('| B'): continue
 field=line.split('|')[1]
 def expand(m):
  a,b,c,d=m.groups()
  assert a==c
  expanded.extend(f'{a}.{i:02}' for i in range(int(b),int(d)+1))
  return ''
 remaining=re.sub(r'(B\d)\.(\d{2})–(B\d)\.(\d{2})',expand,field)
 expanded.extend(re.findall(r'B\d\.\d{2}',remaining))
matrix=(root/'docs/product/m0-capability-matrix.md').read_text(encoding='utf-8')
assert len(expanded)==len(set(expanded))==72
assert set(expanded)==set(re.findall(r'B\d\.\d{2}',matrix))
assert 'Separate S1:' in coverage and 'Separate S2:' in coverage
print(f'PASS: 22 defined state cards/all fields; seven unchanged-source criteria; 14 capability rows; 26 cases/five walkthroughs; {links} local/internal links across 14 documents; valid headings/fences/tables.')
print('PASS: all 64 prior V/Q/PC/DS rows preserved, source criteria/matrix/definition/ADRs 0008-0011 unchanged; 72 parents once and S1/S2 separate; pending G4-J15-01 retained. Documentary integrity only.')
