"""Read-only checks for G1's bounded acf35c9 consolidation, not a live UI audit."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import urllib.parse

ROOT = Path(__file__).resolve().parents[3]
SOURCE = 'acf35c9a2d89646ce1222ec10c9435578748205c'
failures = []
source_paths = subprocess.check_output(
    ['git', 'ls-tree', '-r', '--name-only', SOURCE, '--',
     'research-evidence/g2-06-restaurants-brand',
     'docs/design/valiris-restaurants-brand-direction.md'], cwd=ROOT, text=True
).splitlines()
for relative in source_paths:
    original = subprocess.check_output(['git', 'show', f'{SOURCE}:{relative}'], cwd=ROOT)
    current = ROOT / relative
    if not current.exists() or current.read_bytes() != original:
        failures.append({'path': relative, 'error': 'author-delivery-changed'})

receipt = json.loads((Path(__file__).parent/'author-check-reproduced.json').read_text(encoding='utf-8'))
if receipt['script_sha256'] != hashlib.sha256((ROOT/'research-evidence/g2-06-restaurants-brand/v2/verify.py').read_bytes()).hexdigest():
    failures.append({'error': 'reproduction-script-mismatch'})
files = list(Path(__file__).parent.glob('*.md'))
files += list((ROOT/'coordination/valiris-restaurants').glob('*Brand*Prompt.md'))
links = 0
for file in files:
    for target in re.findall(r'\]\((<[^>]+>|[^)\n]+)\)', file.read_text(encoding='utf-8-sig')):
        target = target.strip('<>')
        if re.match(r'^[\w+.-]+:', target):
            continue
        path = urllib.parse.unquote(target.split('#', 1)[0])
        links += 1
        if not (file.parent/path).exists():
            failures.append({'path': str(file.relative_to(ROOT)), 'link': target, 'error': 'missing-target'})

print(json.dumps({'date':'2026-10-03','source_sha':SOURCE,
                 'author_files_checked_unchanged':len(source_paths),
                 'additional_review_prompt_local_targets':links,'failures':failures,
                 'limits':'Exact author-delivery bytes and local targets; original G4 pending, no final identity approval.'}, ensure_ascii=False, indent=2))
raise SystemExit(bool(failures))
