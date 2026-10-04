from pathlib import Path
from collections import Counter
import re, subprocess

root = Path(r'D:\the next level\valiris-restaurants')
paths = [
 'docs/design/m1-public-presence-and-discovery.md',
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

baseline='2eb8e86'
def original(name): return subprocess.check_output(['git','show',f'{baseline}:{name}'],cwd=root).decode('utf-8')
def doc(name): return (root/name).read_text(encoding='utf-8')
name='docs/design/m1-public-presence-and-discovery.md'
s=doc(name)
cards=dict(re.findall(r'^### (PV-[POX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)',s,re.M|re.S))
expected=[f'PV-P{i:02}' for i in range(1,12)]+[f'PV-O{i:02}' for i in range(1,6)]+['PV-X01']
assert list(cards)==expected and len(cards)==17,cards.keys()
assert set(re.findall(r'PV-[POX]\d{2}',s))<=set(cards),'undefined PV state'
for key,body in cards.items():
 for field in ['**Actor / objective / entry / version:', '**Composition / copy:', '**Actions / effect:', '**Errors / recovery / check:']:
  assert field in body,(key,field)
 assert '→' in body,('destination',key)
criteria=re.findall(r'^\| (J[12]\.\d) \|',s,re.M)
expected_criteria=[f'J1.{i}' for i in range(1,6)]+[f'J2.{i}' for i in range(1,7)]
assert criteria==expected_criteria,criteria
source=doc('docs/product/m0-journeys-and-criteria.md')
assert set(criteria)<=set(re.findall(r'^- \*\*(J\d+\.\d):',source,re.M))
capabilities=re.findall(r'^\| (B\d\.\d{2}) \|',s,re.M)
expected_caps=[f'B1.{i:02}' for i in range(1,6)]+['B1.08','B1.09']+[f'B3.{i:02}' for i in range(1,9)]+['B3.10','B5.01','B5.04','B5.05','B5.07','B6.01','B6.02','B6.03']
assert capabilities==expected_caps and len(capabilities)==23,capabilities
for tag,count in [('VC',26),('VW',6),('VF',4)]:
 found=re.findall(r'^\| ('+tag+r'\d{2}) ',s,re.M)
 assert found==[f'{tag}{i:02}' for i in range(1,count+1)],found
prior=0
for filename,tag,count in [('docs/design/m1-connected-journey.md','V',16),('docs/design/m1-extended-journeys.md','Q',20),('docs/design/m1-content-preparation.md','PC',24),('docs/design/m1-content-preparation.md','DS',4),('docs/design/m1-service-and-maintenance.md','SC',26),('docs/design/m1-extended-journeys.md','LC',6)]:
 pattern=r'^\| '+tag+r'\d{2} .*$'
 old,new=re.findall(pattern,original(filename),re.M),re.findall(pattern,doc(filename),re.M)
 assert old==new and len(new)==count,(filename,tag)
 prior+=count
assert prior==96
for filename,pattern in [('docs/design/m1-connected-journey.md',r'^### ([OPX]\d{2}):'),('docs/design/m1-extended-journeys.md',r'^### (J\d{2}-[POAC]\d{2}):'),('docs/design/m1-content-preparation.md',r'^### (CP-[A-Z]\d{2}):'),('docs/design/m1-service-and-maintenance.md',r'^### (J[89]-[A-Z]\d{2}):')]:
 def states(d):return dict(re.findall(pattern+r'[^\n]*\n(.*?)(?=^### |^## |\Z)',d,re.M|re.S))
 assert states(doc(filename))==states(original(filename)),('prior card changed',filename)
# All conceptual J/CP and original O/P/X destinations in the new document must exist.
defined=set()
for filename,pattern in [('docs/design/m1-connected-journey.md',r'^### ([OPX]\d{2}):'),('docs/design/m1-extended-journeys.md',r'^### (J\d{2}-[POAC]\d{2}):'),('docs/design/m1-content-preparation.md',r'^### (CP-[A-Z]\d{2}):'),('docs/design/m1-service-and-maintenance.md',r'^### (J[89]-[A-Z]\d{2}):')]:defined.update(re.findall(pattern,doc(filename),re.M))
references=set(re.findall(r'(?<![\w-])(?:J\d{1,2}-[A-Z]\d{2}|CP-[A-Z]\d{2}|[OPX]\d{2})(?![\w-])',s))
assert references<=defined,('undefined inherited destination',references-defined)
rows=lambda d:re.findall(r'^- \*\*J\d+\.\d:.*$',d,re.M)
assert rows(source)==rows(original('docs/product/m0-journeys-and-criteria.md'))
for filename in ['docs/product/m0-capability-matrix.md','docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md']+[f'docs/adr/{n}' for n in ['0005-repository-and-product-language.md','0008-first-launch-capability-commitment.md','0009-studio-design-and-registered-diner-personalisation.md','0010-diner-account-and-display-recovery.md','0011-shared-menu-content-and-contextual-maintenance.md','0012-confirm-delegated-updates-per-assignment.md']]: assert doc(filename)==original(filename),filename
coverage=doc('docs/design/m1-connected-journey.md').split('## 7.',1)[1].split('## 8.',1)[0]
expanded=[]
for line in coverage.splitlines():
 if not line.startswith('| B'):continue
 field=line.split('|')[1]
 def expand(m):
  a,b,c,d=m.groups();assert a==c;expanded.extend(f'{a}.{i:02}' for i in range(int(b),int(d)+1));return ''
 remaining=re.sub(r'(B\d)\.(\d{2})–(B\d)\.(\d{2})',expand,field)
 expanded.extend(re.findall(r'B\d\.\d{2}',remaining))
assert len(expanded)==len(set(expanded))==72
assert set(expanded)==set(re.findall(r'B\d\.\d{2}',doc('docs/product/m0-capability-matrix.md')))
assert 'Separate S1:' in coverage and 'Separate S2:' in coverage
for marker in ['Owner-selected directed pairings','VR1','VP1','Independent review continuity','resolves documentary G4-J15-01','Late public response','M2/#4']:
 assert marker in s,marker
print(f'PASS: {links} local/internal links in 15 docs; headings/fragments/fences/tables; 17 defined PV cards/all fields; 11 source criteria, 23 capabilities, six VW/26 VC; all inherited destinations defined.')
print('PASS: all 96 prior contrast rows and original state cards/source criteria/matrix/definition/ADR-0005,0008–0012 unchanged; 72 parents exactly once and S1/S2 separate. Documentary integrity, not software/independent/real evidence.')
