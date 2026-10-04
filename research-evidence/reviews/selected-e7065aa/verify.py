"""Read-only selected-source integrity check; run in the consolidation checkout."""
from pathlib import Path
import hashlib, json, subprocess, struct

root = Path(__file__).resolve().parents[3]
source = 'e7065aaa92acdf223628f9d7099301d766810ad3'
prefix = 'research-evidence/g2-06-restaurants-brand/refinement/'
inputs = [
    ('signature-and-first-model/02-expresion-sin-personajes.png', '36dc3ca72e8f7653675002c99a616598f8d8ed56e910e30a45226e17070346cb', 'codex-clipboard-1c224dd4-c2ed-4dbc-95ba-a841d5faed04.png'),
    ('polish-v2/01-cafeteria-refinada-v2.png', '737882f3adb19a5fe12533fe73d31b9e73fab3d7919683028103a2a5a0030a06', 'codex-clipboard-f995d598-8207-45bb-9a38-8fda39cbc508.png'),
    ('polish-v2/02-campana-refinada-v2.png', '53501d4e70749f988c74c963597415ced959d494b74b2fa5fa03a0cd44ec29ff', 'codex-clipboard-4ad28d7e-b3d1-4816-842b-bacfe64629e8.png'),
]
rows=[]
failures=[]
for rel, expected, attachment in inputs:
    p=root/prefix/rel
    data=p.read_bytes()
    sha=hashlib.sha256(data).hexdigest()
    assert data[:8] == b'\x89PNG\r\n\x1a\n'
    width,height=struct.unpack('>II',data[16:24])
    ap=Path('C:/Users/aboul/AppData/Local/Temp')/attachment
    attached=ap.exists()
    match=hashlib.sha256(ap.read_bytes()).hexdigest()==sha if attached else None
    rows.append(dict(path=prefix+rel,sha256=sha,expected_sha256=expected,bytes=len(data),width=width,height=height,attachment_available=attached,attachment_match_reproduced=match))
    if sha!=expected or match is False: failures.append(rel)

orilla='research-evidence/g2-06-art-direction-2026-10-03/storefront-v0.2/02-cartel-revisado-v0.2.png'
orilla_sha=hashlib.sha256((root/orilla).read_bytes()).hexdigest()
if orilla_sha!='4f576dd2156f9361abee8338df13704cfd4dc70a4e5e2a47d11de8fbf567f989': failures.append('orilla-original-hash')
protected=[
    'research-evidence/g2-06-restaurants-brand',
    'research-evidence/g2-06-art-direction-2026-10-03',
    'docs/design/valiris-restaurants-brand-direction.md',
    'docs/design/valiris-restaurants-brand-refinement.md',
    'docs/product/m0-capability-matrix.md',
    'docs/product/m0-journeys-and-criteria.md',
    'docs/research/storefront-digital-menu/functional-definition',
    'docs/adr',
]
modified=subprocess.check_output(['git','diff','--name-only',source,'--',*protected],cwd=root,text=True).splitlines()
if modified: failures.append('protected-source-diff')
print(json.dumps(dict(source_sha=source,selected_assets=rows,orilla_original_sha256=orilla_sha,protected_source_changes=modified,failures=failures,scope='Selected-source integrity, dimensions and available attachment matching only. No UX, software, independent G4, licence or external URL verification.'),ensure_ascii=False,indent=2))
raise SystemExit(bool(failures))
