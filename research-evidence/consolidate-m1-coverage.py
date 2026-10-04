from pathlib import Path
import re,json,subprocess

root=Path(r'D:\the next level\valiris-restaurants')
baseline='a0583e0ec04e310f6736f1d763ca4d7a78191973'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=root).decode().strip()==baseline
matrix=(root/'docs/product/m0-capability-matrix.md').read_text(encoding='utf-8')
caps={}
for line in matrix.splitlines():
    if re.match(r'^\| B\d\.\d{2} /',line):
        cols=[x.strip() for x in line.split('|')[1:-1]]
        caps[cols[0].split(' /')[0]]={'origin':cols[0],'name':cols[1],'treatment':cols[3]}
assert len(caps)==72
def slug(text):return re.sub(r'[^\w\- ]','',text.lower()).replace(' ','-')
states={};cases={}
for p in (root/'docs/design').glob('*.md'):
    current=''
    for line in p.read_text(encoding='utf-8').splitlines():
        if re.match(r'^#{1,6} ',line):current=slug(line.split(' ',1)[1])
        m=re.match(r'^### ((?:FO|JT|PV|CP|J\d+)-[A-Z]\d{2}|[OPX]\d{2}):',line)
        if m:states[m[1]]=(p.name,current)
        m=re.match(r'^\| ((?:V|Q|PC|DS|SC|LC|VC|TC|FC)\d{2})(?:\s|\|)',line)
        if m:cases[m[1]]=(p.name,current)
def state_link(key):
    file,anchor=states[key];return f'[{key}]({file}#{anchor})'
def case_link(key):
    file,anchor=cases[key];return f'[{key}]({file}#{anchor})'
def listed(keys,link):return ', '.join(link(k) for k in keys.split())
def gap_link(key):return f'[{key}](m1-coverage-and-evidence.md#{key.lower().replace(".","")})'
data='''B1.01;S;PV-P01 PV-O02 PV-O05;J1.1 J2.1;VC01 VC02;RV05;CG04 CG05
B1.02;S;PV-P02 PV-O01 JT-O02 JT-O09;J1.1 J1.2 J4.2;VC03 VC04 TC04 TC14;RV05 RV06;CG04 CG05 CG08
B1.03;S;PV-P02 PV-O01;J1.1;VC07;RV05;CG04 CG05
B1.04;S;PV-P01 PV-O02 PV-O05;J1.1 J3.5;VC21;RV05;CG04 CG05
B1.05;P;PV-P01 PV-P04 PV-O02;J1.1 J2.1;VC01 VC02;RV05;CG01 CG04 CG05
B1.06;P;J8-S01 J8-S05 J8-S06;J3.1 J8.2;SC02 SC06;RV04;CG02 CG05 CG10
B1.07;P;J8-S01 J8-S02 J8-S06;J3.1 J8.1 J8.2;SC01 SC02;RV04;CG03 CG05 CG10
B1.08;S;PV-P09 PV-O04 J8-S11;J1.5 J7.4 J8.4;VC22 VC23 SC15;RV05 RV04;CG04 CG05 CG08 CG10 CG12
B1.09;S;PV-P02 J14-C01 J14-O02;J1.4 J14.1 J14.2;VC06 Q12 Q13;RV05 RV02;CG05 CG08 CG09.1
B2.01;S;CP-S01 CP-S04 PV-P05 JT-O04;J3.1 J3.3 J2.1;PC01 PC14 PC18;RV03 RV05 RV06;CG04 CG05 CG08
B2.02;S;CP-R01 PV-P06 FO-F02;J1.3 J2.2 J3.3;PC05 VC08 FC03;RV03 RV05 RV07;CG04 CG05 CG08
B2.03;S;PV-P06 FO-O02;J1.3 J2.2 J7.1;VC09 FC13;RV05 RV07;CG04 CG05 CG07 CG08
B2.04;S;CP-I02 CP-R03 JT-P01 FO-O02;J1.2 J3.6 J7.1;PC06 TC03 FC12;RV03 RV06 RV07;CG04 CG05 CG07 CG08
B2.05;S;CP-S04 PV-P04 JT-P01;J3.1 J2.2 J1.5;PC18 VC05;RV03 RV05 RV06;CG04 CG05 CG08
B2.06;S;JT-O02 JT-O05 JT-O07 JT-X04;J4.2 J4.3 J1.2;TC03 TC05 TC08 TC28;RV06;CG04 CG05 CG08
B2.07;S;PV-P04 PV-P06 JT-O11;J2.2 J5.2;VC08 TC19;RV05 RV06;CG04 CG05 CG08
B2.08;S;JT-O10 JT-O12 JT-O14 JT-P02;J5.1 J5.2 J5.3;TC17 TC20 TC23;RV06;CG04 CG05 CG08
B2.09;S;JT-O03 JT-O09 JT-P01;J4.2 J5.3 J1.1;TC04 TC07 TC14;RV06;CG04 CG05 CG08
B2.10;S;J14-C02 J14-O01 J14-O02;J14.1 J14.2;Q12 Q13;RV02;CG05 CG08 CG09.2
B3.01;S;PV-P05 PV-P06;J2.1 J2.5;VC01 VC12;RV05;CG05
B3.02;S;PV-P05 PV-P10;J2.3;VC10 VC13;RV05;CG04 CG05 CG06 CG08
B3.03;S;PV-P05 PV-P06;J2.3 J2.4;VC10 VC11;RV05;CG04 CG05 CG08
B3.04;S;PV-P05 PV-P06 FO-F02;J2.4 J3.4;VC11 FC01 FC04;RV05 RV07;CG04 CG05 CG08
B3.05;S;PV-P06;J2.5;VC09 VC12;RV05;CG05
B3.06;S;PV-P06 PV-O02 CP-A02;J1.3 J3.5;VC21 PC09;RV05 RV03;CG04 CG05 CG06
B3.07;S;PV-P07 PV-O03 PV-O05;J2.5 J4.1;VC14 VC20;RV05;CG04 CG05 CG08
B3.08;S;PV-P09 PV-P11 PV-O04;J1.5 J2.5;VC22 VC23;RV05;CG04 CG05 CG08 CG12
B3.09;S;J10-P01 J10-P02 J10-P05;J10.1 J10.4;Q01 Q04;RV02;CG05 CG08
B3.10;S;PV-P08 PV-O03 PV-O05;J2.2 J2.5 J4.1;VC15 VC16 VC17 VC19 VC20;RV05;CG04 CG05 CG08
B3.11;S;J10-P03 J10-O01;J10.2;Q02;RV02;CG04 CG05 CG08
B4.01;S;CP-I01 CP-I02 CP-I03 CP-I04 CP-I07;J3.2;PC02 PC03 PC04 PC06;RV03;CG04 CG05 CG08
B4.02;S;CP-I05 CP-R01 CP-R02;J3.3 J3.4;PC05 PC07 PC08;RV03;CG04 CG05 CG08
B4.03;S;CP-M01 JT-O10;J3.1 J5.1 J8.2;PC19 TC17 SC02;RV03 RV06 RV04;CG04 CG05 CG08
B4.04;S;CP-S03 CP-S04 CP-B02 CP-B03 CP-B04;J3.3 J5.2 J5.4;PC17 PC18 PC20 PC21 PC23;RV03;CG05 CG08
B4.05;S;CP-R03 JT-O04 FO-F05;J3.6 J4.1;DS01 DS02 TC01 FC11;RV01 RV03 RV06 RV07;CG05 CG08
B4.06;S;O05 O06 JT-O04 JT-X02;J4.1 J4.3;TC01 TC11 DS04;RV01 RV06;CG05 CG08
B4.07;S;JT-O05 JT-O06 JT-O07 JT-O08;J4.2 J4.3;TC06 TC09 TC12 TC29;RV06;CG05 CG08
B4.08;S;CP-B04 JT-O13 JT-O15;J5.4 J4.4;PC23 TC21 TC25;RV03 RV06;CG05 CG08
B4.09;S;CP-X03 JT-X03 FO-X03;J4.1 J5.2;DS04 TC22 FC21;RV03 RV06 RV07;CG05 CG08
B4.10;S;CP-A01 CP-A02 CP-A03;J3.5;PC09 PC10 PC11 PC12;RV03;CG04 CG05 CG08
B4.11;S;CP-S02 FO-F03 FO-F04 JT-O06;J3.4 J6.2 J6.3;PC15 PC16 FC05 FC06 FC07 TC06;RV03 RV07 RV06;CG04 CG05 CG08
B4.12;S;J14-C03 J14-O02;J14.1 J14.2;Q12 Q13;RV02;CG05 CG08 CG09.3
B5.01;S;PV-P10 FO-F04 FO-O01;J1.4 J6.1 J7.2;VC13 FC09 FC15;RV05 RV07;CG04 CG05 CG06 CG08
B5.02;S;CP-A02 CP-R02 FO-F04;J3.5 J6.2;PC10 FC09;RV03 RV07;CG04 CG05 CG06 CG08
B5.03;S;CP-G01 CP-G02 FO-F04;J6.3;PC13 FC07;RV03 RV07;CG04 CG05 CG06 CG08
B5.04;S;FO-F04 FO-F05 JT-P02;J6.1 J5.1;FC08 TC17;RV07 RV06;CG05 CG08
B5.05;S;PV-P10 FO-F04 FO-F05;J6.2 J7.2;VC13 FC09;RV05 RV07;CG04 CG05 CG06 CG08
B5.06;S;FO-F01 FO-F02 FO-F03;J3.4 J6.2;FC01 FC02 FC03 FC05;RV07;CG04 CG05 CG08
B5.07;S;PV-P02 FO-F02 FO-F06 J15-O01;J2.4 J6.3 J15.4;VC07 FC04 FC10 Q18;RV05 RV07 RV02;CG04 CG05 CG08
B5.08;S;FO-F01 FO-F06 FO-O01 FO-O02;J6.3 J7.2;FC10 FC11 FC12;RV07;CG04 CG05 CG07 CG08
B5.09;S;J11-O01 J11-O02 J11-P01 J11-O03;J11.1 J11.2;Q05 Q06 FC06;RV02 RV07;CG04 CG05 CG07 CG08
B6.01;S;FO-Q01 FO-Q02 FO-Q03;J7.4;FC22 FC23;RV07;CG04 CG05 CG07 CG08
B6.02;S;PV-P01 PV-P04 FO-Q01;J2.1 J7.4;VC01 FC22;RV05 RV07;CG04 CG05 CG07 CG08
B6.03;S;PV-P04 FO-Q03 J15-P01;J2.1 J15.1;VC01 Q15 FC24;RV05 RV02 RV07;CG05 CG08
B6.04;S;FO-Q02 FO-O04 FO-O06;J7.2 J7.4;FC18 FC20 FC22;RV07;CG04 CG05 CG07 CG08
B6.05;S;FO-O01 FO-O02 FO-O04;J7.1 J7.2;FC12 FC13 FC14 FC18;RV07;CG04 CG05 CG07 CG08
B6.06;S;FO-F04 FO-O01 FO-O02;J7.1 J7.2;FC09 FC11 FC15;RV07;CG04 CG05 CG06 CG07 CG08
B6.07;S;J14-C04 J14-O02;J14.1 J14.2;Q12 Q13;RV02;CG05 CG08 CG09.4
B6.08;S;J14-C05 J14-O02;J14.1 J14.2;Q12 Q13;RV02;CG05 CG08 CG09.5
B6.09;S;J12-O01 J12-P01 J12-O02 J12-P02;J12.1 J12.2 J12.3;Q07 Q08 Q09;RV02;CG04 CG05 CG07 CG08
B6.10;S;J10-P04 J10-P05 FO-Q03;J2.6 J10.3 J10.4;Q03 Q04 FC24;RV02 RV07;CG05 CG08
B6.11;S;J8-S09 J8-S10 J8-S11;J8.4;SC12 SC13 SC14 SC15 SC16;RV04;CG04 CG05 CG08 CG10
B7.01;S;J9-U01 J9-U02 J9-U04;J9.2;SC21 SC24;RV04;CG05 CG08
B7.02;S;J9-U02 J9-U04;J9.2;SC21 SC24;RV04;CG05 CG08
B7.03;S;J9-U03 J9-U04;J9.3;SC23 SC24;RV04;CG05 CG08
B7.04;S;J9-U02 J9-U04;J9.2;SC21 SC25;RV04;CG05 CG08
B7.05;S;PV-P02 J9-U02;J1.4 J9.2;VC06 SC22;RV05 RV04;CG04 CG05 CG08
B7.06;S;J14-C06 J14-O02 J9-U04;J14.3 J9.3;Q14 SC22;RV02 RV04;CG05 CG08 CG09.6
B7.07;S;J9-M01 J9-M02 J9-M03 J9-M04 FO-O05;J9.1 J7.3;SC17 SC18 SC19 SC20 FC19;RV04 RV07;CG04 CG05 CG07 CG08
B7.08;S;J13-O01 J13-O02 J13-O03;J13.1 J13.2;Q10 Q11 SC25;RV02 RV04;CG05 CG08
B7.09;S;J8-S01 J8-S03 J8-S04 J8-S05 J8-S06;J8.1 J8.2 J8.3;SC01 SC03 SC04 SC05 SC06;RV04;CG04 CG05 CG10
B7.10;S;J8-S07 J8-S08 J9-X02;J8.3;SC07 SC08 SC09 SC10 SC11;RV04;CG05 CG08 CG10'''
rows=[]
for line in data.splitlines():
    key,status,path,criteria,contrast,review,gaps=line.split(';')
    assert key in caps
    rows.append({'id':key,'status':status,'states':path,'criteria':criteria,'cases':contrast,'reviews':review,'gaps':gaps})
assert [x['id'] for x in rows]==list(caps)
def review_links(keys):return ', '.join(f'[{k}](m1-coverage-and-evidence.md#{k.lower()})' for k in keys.split())
table='| Capability / accepted treatment | Written coverage | Concrete states | Related source criteria / author contrasts | Applicable bounded package review | Pending evidence / checkpoint |\n| --- | --- | --- | --- | --- | --- |\n'
for row in rows:
    cap=caps[row['id']]
    table+='| '+row['id']+' · '+cap['name']+' / '+cap['treatment']+' | '+('Sufficient written path' if row['status']=='S' else 'Partial: visual expression missing')+' | '+listed(row['states'],state_link)+' | '+row['criteria'].replace(' ', ', ')+'; '+listed(row['cases'],case_link)+' | '+review_links(row['reviews'])+' | '+listed(row['gaps'],gap_link)+' |\n'
p=root/'docs/design/m1-connected-journey.md'
s=p.read_text(encoding='utf-8')
start=s.index('**A** =',s.index('## 7.')) if '**A** =' in s else s.index('The [matrix]',s.index('## 7.'))
end=s.index('Separate S1:',start)
intro='''The [matrix](../product/m0-capability-matrix.md) remains the accepted scope ledger. This is the **single individual M1 design map**, consolidated at a0583e0: 72 parents once, with 36 included/30 configurable/six connection-dependent. The [coverage and evidence report](m1-coverage-and-evidence.md) records the 59 criteria, gaps, review limits and next assignment; it does not duplicate this inventory.

**Sufficient written path** means the author located a task, normal/error/recovery behavior and applicable source meaning for proceeding to further design evidence. **Partial** means a necessary capability contribution remains undescribed or unexpressed; **Absent** would mean no adequate path found. These judgments are bounded author consolidation, not global independent approval. A related source criterion need not exhaust the capability (especially identity/templates/bespoke); visual execution, interaction, factual inputs, technical enforcement and real evidence remain separate. Every listed contrast is an authored documentary case, not a product test. Package-review codes name the actual previously reviewed states/commit and never certify every row or this consolidation.

Original A/N/D shorthand meant annotated/further-design/input-dependent. The explicit statuses and gap checkpoints below supersede that grouped shorthand without changing scope or existing journey/card bodies. Original continuation [criteria and walkthroughs](m1-extended-journeys.md#9-criteria-traceability-and-reader-led-walkthroughs), [preparation](m1-content-preparation.md), [service](m1-service-and-maintenance.md), [presence](m1-public-presence-and-discovery.md), [scheduling](m1-scheduling-and-service-continuity.md) and [food/outputs](m1-food-register-and-outputs.md) remain canonical source packages.

'''
s=s[:start]+intro+table+'\n'+s[end:]
s=s.replace('register/staff/menu/daily/print/QR lifecycle and physical freshness described; independent FO/technical/material/visual/interaction proof pending','register/staff/menu/daily/print/QR lifecycle described; final bounded G1/G4 review on a0583e0 requests no documentary correction; technical/material/visual/interaction proof pending',1)
s=s.replace('| Next: coverage consolidation and visual/interaction evidence plan | Audit remaining source/capability/criterion gaps across all packages, then specify template/bespoke/public/mobile/staff/paper/screen/accessibility and actual interaction/participant evidence; reviews/contracts/real inputs remain at each checkpoint |','| Coverage consolidation | [Report](m1-coverage-and-evidence.md): individual72/59-source-criterion mapping,176 prior contrasts preserved; author consolidation, new independent review pending |\n| Next: visual and interaction evidence | Resolve CG01–CG03 expression gaps with C1–C3 public/management compositions; then staff/paper/display/QR, locale and accessibility/interaction evidence under CG04–CG12; no milestone closure inferred |',1)
marker='## 8. Specialist questions and review tasks'
current='''**Current consolidated continuity, 2 October:** all 72 parents are individually traced, with 69 sufficient written paths and three partial visual-expression contributions (B1.05–B1.07); no absent written path was identified by this bounded author comparison. All 59 source criteria have concrete path/contrast references. This is not 69 completed capabilities, 100% design or an overall M1 percentage. Final G1/G4 FO review on a0583e0 requests no bounded documentary correction and supersedes earlier FO-pending entries at that scope only. All 176 earlier contrasts and card bodies remain intact. New [CG/RV report](m1-coverage-and-evidence.md) fixes remaining evidence/checkpoints and the next G2 visual/interaction assignment; its independent review is pending.

'''
if '**Current consolidated continuity, 2 October:**' not in s:s=s.replace(marker,current+marker,1)
p.write_text(s,encoding='utf-8',newline='\n')
(Path(r'D:\the next level\research-evidence')/'m1-consolidated-coverage-data.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Build the criterion correspondence from explicit primary paths; no source criteria are rewritten.
criterion_data='''J1.1;PV-P01 PV-P02 PV-O01 JT-O02;VC02 VC03 VC04;RV05 RV06;CG04 CG05
J1.2;PV-P03 JT-P01;VC03 VC05 TC03;RV05 RV06;CG04 CG05 CG08
J1.3;PV-P06 FO-F02;VC09 FC01;RV05 RV07;CG04 CG05
J1.4;PV-P02 PV-P10 J14-C01;VC06 VC13 Q12;RV05 RV02;CG04 CG05 CG06 CG09.1
J1.5;PV-P09 PV-P11;VC22 VC23;RV05;CG04 CG05 CG12
J2.1;PV-P04 PV-P05;VC01;RV05;CG01 CG02 CG05
J2.2;PV-P04 PV-P06 PV-P08;VC08 VC16;RV05;CG04 CG05
J2.3;PV-P05 PV-P10;VC10 VC13;RV05;CG05 CG06
J2.4;PV-P05 PV-P06 FO-F02;VC11 FC04;RV05 RV07;CG04 CG05
J2.5;PV-P06 PV-P07 PV-P08 PV-P11;VC12 VC14 VC17;RV05;CG05
J2.6;J10-P04 J10-P05;Q03 Q04;RV02;CG05 CG08
J3.1;CP-I01 CP-M01 J8-S06;PC01 PC19 SC02;RV03 RV04;CG02 CG03 CG05
J3.2;CP-I01 CP-I03 CP-I04 CP-I07;PC02 PC03 PC04;RV03;CG04 CG05 CG08
J3.3;CP-I05 CP-R01 CP-S01 CP-S03;PC05 PC08 PC14 PC17;RV03;CG04 CG05 CG08
J3.4;CP-R02 FO-F02 FO-F03;PC07 PC15 FC01 FC05;RV03 RV07;CG04 CG05
J3.5;CP-A01 CP-A02 CP-A03;PC09 PC10 PC11 PC12;RV03;CG04 CG05
J3.6;CP-R03 JT-O04;PC06 TC02;RV03 RV06;CG05 CG08
J4.1;O05 O06 JT-O04;TC01 TC02 TC22;RV01 RV06;CG05 CG08
J4.2;JT-O02 JT-O03 JT-O05 JT-O06;TC03 TC06 TC07 TC08;RV06;CG04 CG05 CG08
J4.3;JT-O07 JT-O08 JT-X02;TC09 TC10 TC11 TC12 TC15 TC29;RV06;CG05 CG08
J4.4;O02 O03 JT-X01 CP-X02;DS01 DS02 DS03 DS04 TC16;RV01 RV03 RV06;CG05 CG08
J5.1;JT-O10 JT-O12 JT-P02;TC17 TC18;RV06;CG05 CG08
J5.2;JT-O11 JT-O12 JT-X03;TC19 TC20 TC21 TC22;RV06;CG05 CG08
J5.3;JT-O14 JT-O09;TC23 TC24 TC14;RV06;CG04 CG05 CG08
J5.4;JT-O13 JT-O15 CP-B04;TC18 TC21 TC25 PC23;RV06 RV03;CG05 CG08
J6.1;FO-F04 FO-F05;FC08;RV07;CG04 CG05 CG06 CG08
J6.2;FO-F02 FO-F03 FO-F04 FO-F05;FC01 FC05 FC06 FC09;RV07;CG04 CG05 CG06 CG08
J6.3;FO-F01 FO-F04 FO-F06 FO-O02;FC07 FC10 FC11;RV07;CG04 CG05 CG07
J7.1;FO-O01 FO-O02;FC12 FC13 FC14;RV07;CG02 CG03 CG05 CG07
J7.2;FO-O01 FO-O03 FO-O04;FC11 FC15 FC16 FC17 FC18;RV07;CG04 CG05 CG06 CG07 CG08
J7.3;FO-O05 FO-O06;FC19 FC20 FC21;RV07;CG04 CG05 CG07 CG08
J7.4;FO-Q01 FO-Q02 FO-Q03;FC22 FC23 FC24;RV07;CG04 CG05 CG07 CG08
J8.1;J8-S01 J8-S02;SC01;RV04;CG03 CG05 CG10
J8.2;J8-S03 J8-S04 J8-S05 J8-S06;SC02 SC03 SC04 SC05 SC06;RV04;CG02 CG03 CG04 CG05 CG10
J8.3;J8-S06 J8-S07 J8-S08 J9-X02;SC07 SC08 SC09 SC10 SC11;RV04;CG05 CG08 CG10
J8.4;J8-S09 J8-S10 J8-S11;SC12 SC13 SC14 SC15 SC16;RV04;CG04 CG05 CG08 CG10
J9.1;J9-M01 J9-M02 J9-M03 J9-M04;SC17 SC18 SC19 SC20;RV04;CG05 CG07 CG08
J9.2;J9-U01 J9-U02 J9-U04;SC21 SC22 SC24;RV04;CG05 CG08
J9.3;J9-U03 J9-U04 J14-C06;SC23 SC24 Q14;RV04 RV02;CG05 CG08 CG09.6
J10.1;J10-P01 J10-P02;Q01;RV02;CG05 CG08
J10.2;J10-P03 J10-O01;Q02;RV02;CG04 CG05 CG08
J10.3;J10-P04;Q03;RV02;CG05 CG08
J10.4;J10-P05;Q04;RV02;CG05 CG08
J11.1;J11-O01 J11-P01;Q05;RV02;CG04 CG05
J11.2;J11-O02 J11-O03 FO-F03;Q06 FC06;RV02 RV07;CG04 CG05 CG07 CG08
J12.1;J12-O01 J12-P01;Q07;RV02;CG04 CG05 CG07
J12.2;J12-O02 J12-P02;Q08;RV02;CG05 CG07 CG08
J12.3;J12-O01 J12-P01;Q09;RV02;CG05 CG07
J13.1;J13-O01 J13-O03;Q10;RV02;CG05 CG08
J13.2;J13-O02 J13-O03;Q11;RV02;CG05 CG08
J14.1;J14-O01 J14-C01 J14-C02 J14-C03 J14-C04 J14-C05 J14-C06;Q12;RV02;CG08 CG09.1 CG09.2 CG09.3 CG09.4 CG09.5 CG09.6
J14.2;J14-O01 J14-O02;Q13;RV02;CG05 CG08 CG09.1 CG09.2 CG09.3 CG09.4 CG09.5 CG09.6
J14.3;J14-C06 J14-O02;Q14;RV02;CG05 CG08 CG09.6
J15.1;J15-P01;Q15;RV02;CG05
J15.2;J15-A01 J15-A02 J15-A03 J15-A04 J15-A05 J15-A09;Q16;RV02;CG05 CG06 CG08
J15.3;J15-A06 J15-P02 J15-P03;Q17 LC01 LC02 LC03 LC04 LC05 LC06;RV02;CG05 CG08
J15.4;J15-P02 J15-O01 J10-P05;Q18 LC04 LC05;RV02;CG04 CG05 CG08
J15.5;J15-P03 J15-A09;Q19 LC06;RV02;CG05 CG08
J15.6;J15-A07 J15-A08;Q20;RV02;CG05 CG08'''
criterion_rows=[line.split(';') for line in criterion_data.splitlines()]
original=re.findall(r'^- \*\*(J\d+\.\d):',(root/'docs/product/m0-journeys-and-criteria.md').read_text(encoding='utf-8'),re.M)
assert [r[0] for r in criterion_rows]==original and len(original)==59
header='''# M1 — consolidated coverage, gaps and evidence

2 October 2026 · G2 author consolidation · baseline a0583e0 · existing M1 #5 / draft PR #21.

**Status:** author documentary consolidation, not independently reviewed. No prototype, rendered visual/UI, software, verified food/translation/measurement, working connection, physical output/device or participant result is created by this report. M1 remains open; technical contracts remain M2/#4.

## 1. Sources, method and bounded result

The [single individual72 map](m1-connected-journey.md#7-compact-coverage-and-remaining-work) is the only consolidated capability inventory. The [accepted matrix](../product/m0-capability-matrix.md), [59 original criteria](../product/m0-journeys-and-criteria.md#3-journeys-and-verifiable-initial-criteria), [functional definition](../research/storefront-digital-menu/functional-definition/functional-definition.es.md), [briefs](../product/m1-design-briefs.md) and [roadmap](../project/roadmap.md) retain their original authority. The original scope is36 included/30 configurable/six connection-dependent. No capability is postponed through a missing input. Existing state packages remain the source of written behavior; this report does not replace their cards or create another backlog.

Read each source commitment against actual linked state bodies and authored contrasts, reusing complete prior readings of unchanged packages. Distinguish entry/task, normal result, permission/conflict/failed-or-unknown recovery, factual/context/private/output meaning and missing essential contribution. Linking a state alone is not sufficient; a nearby source criterion may cover only part of a capability. Package independent review cannot automatically certify a new aggregate judgment or everything in the package.

**Author indicators:**72/72 parents individually traced;59/59 unchanged source criteria have located concrete paths and authored contrasts;69/72 have sufficient written paths to proceed to further design evidence,3/72 have partial essential visual-expression contributions (identity/base templates/bespoke),0/72 have an absent written path identified within this comparison. Sufficient is a limited documentary judgment, not completed capability delivery. All176 previous contrast rows and existing card bodies are preserved. These denominators do not produce an overall M1 percentage, a full independent audit or user validation. Rendered/interactive/real-source/technical evidence remains separately pending.

**S1** stays excluded (free-form restaurant page builder): studio design plus routine content autonomy in J8-S06/CP-M01. **S2** stays accepted and separate from72: [J15-A06](m1-extended-journeys.md#j15-a06-venue-preferences), J15-P02/P03, verification/recovery/logout/removal and J15-O01; Q15–Q20/LC01–LC06, RV02 and CG04/CG05/CG06/CG08. Audio-only and3D are deferred B3.11 subparts, not extra parents; video accessible equivalents remain launch obligations.

## 2. Source-criterion correspondence

Each row records where the author located the existing written criterion, not that it has passed interaction or milestone acceptance. Original criterion text remains in the source document. All rows still require applicable CG evidence; the three visual-expression capabilities are not exhausted by their related criteria.

| Source criterion | Concrete current state path | Author contrasts located | Prior package review / current evidence gap |
| --- | --- | --- | --- |
'''
for key,path,contrast,review,gaps in criterion_rows:
    header+='| '+key+' | '+listed(path,state_link)+' | '+listed(contrast,case_link)+' | '+review_links(review)+'; '+listed(gaps,gap_link)+' |\n'
# Append the authored report's review/gap/assignment sections maintained in a separate input text.
body=Path(r'D:\the next level\research-evidence\m1-coverage-report-body.md').read_text(encoding='utf-8')
(root/'docs/design/m1-coverage-and-evidence.md').write_text(header+'\n'+body,encoding='utf-8',newline='\n')
(Path(r'D:\the next level\research-evidence')/'m1-consolidated-criteria-data.json').write_text(json.dumps(criterion_rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Written: individual72 map and59-criterion report; no source card/criterion edits.')
