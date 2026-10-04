"""Bounded author evidence checks. No application or integral accessibility audit."""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import math
import re
import struct
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OWNED = 'research-evidence/g2-06-restaurants-brand/'
GUIDE = 'docs/design/valiris-restaurants-brand-direction.md'
START = 'd44942ea7eee6471c8d6933dab91dcd9f6b37009'
TEXT = {'.md', '.js', '.json', '.py', '.svg', '.txt'}
failures = []
passed = Counter()


def check(condition, group, detail):
    if condition:
        passed[group] += 1
    else:
        failures.append(f'{group}: {detail}')


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, stderr=subprocess.PIPE)


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def lf(data):
    return data.replace(b'\r\n', b'\n')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def integrity(record, group):
    path = ROOT / record['path']
    check(path.is_file(), group, f"missing {record['path']}")
    if not path.is_file():
        return
    raw = path.read_bytes()
    data = lf(raw) if path.suffix in TEXT else raw
    expected = record.get('lfSha256', record['sha256'])
    expected_bytes = record.get('lfBytes', record['bytes'])
    check(digest(data) == expected and len(data) == expected_bytes, group, f"hash/bytes {record['path']}")
    if path.suffix == '.png':
        check(raw[:8] == b'\x89PNG\r\n\x1a\n', group, f'PNG header {path.name}')
        if 'dimensions' in record:
            check(list(struct.unpack('>II', raw[16:24])) == record['dimensions'], group, f'PNG dimensions {path.name}')
    if path.suffix == '.svg':
        try:
            parsed = ET.fromstring(data)
            check(parsed.tag.endswith('svg'), group, f'SVG root {path.name}')
        except ET.ParseError:
            check(False, group, f'SVG parse {path.name}')


def contrast(foreground, background):
    def luminance(h):
        values = [int(h[i:i+2], 16) / 255 for i in (1, 3, 5)]
        linear = [v / 12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in values]
        return sum(v*w for v,w in zip(linear, (.2126,.7152,.0722)))
    light, dark = sorted([luminance(foreground), luminance(background)], reverse=True)
    return (light+.05)/(dark+.05)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-checks', action='store_true')
    args = parser.parse_args()
    manifest = read_json(HERE/'manifest.json')
    audit = read_json(HERE/'figma-validation.json')
    old = read_json(HERE.parent/'manifest.json')
    prompts = read_json(HERE/'prompts.json')
    check(git('branch','--show-current').decode().strip() == manifest['git']['branch'], 'scope', 'unexpected branch')
    gitroot = Path(git('rev-parse','--show-toplevel').decode().strip()).resolve()
    check(gitroot == ROOT, 'scope', 'unexpected repository root')
    paths = set(git('diff','--name-only',START).decode().splitlines())
    paths.update(git('ls-files','--others','--exclude-standard').decode().splitlines())
    check(all(p == GUIDE or p.startswith(OWNED) for p in paths), 'scope', 'changed/untracked paths outside ownership')
    for r in manifest['repositorySources']:
        data = git('show', f"{r['commit']}:{r['path']}")
        check(digest(data) == r['sha256'] and len(data) == r['bytes'], 'frozen_sources', r['path'])
        if r['commit'] == manifest['git']['baseline']:
            path = ROOT/r['path']
            working = path.read_bytes()
            check(digest(lf(working) if path.suffix in TEXT else working) == r['sha256'], 'frozen_sources', f"working source changed: {r['path']}")
    integrity(manifest['orilla'], 'orilla') if 'path' in manifest['orilla'] else integrity({**manifest['orilla'], 'path':manifest['orilla']['sourcePath']}, 'orilla')
    for r in old['assets']:
        integrity(r, 'v1_preservation')
    archives = {'brand-direction-v1.md': GUIDE,
                'README-v1.md': OWNED+'README.md',
                'RETORNO_G1-v1.es.md': OWNED+'RETORNO_G1.es.md'}
    for filename, original in archives.items():
        archived = lf((HERE.parent/filename).read_bytes())
        if filename == 'brand-direction-v1.md':
            # One sibling link is rebased to the original docs directory after archival.
            archived = archived.replace(b'](../../docs/design/m1-storefront-visual-direction.md)', b'](m1-storefront-visual-direction.md)')
        check(archived == lf(git('show',f'{START}:{original}')), 'v1_preservation', filename)
    check('rejected' in old['status'].lower() and old.get('supersededBy') == 'v2/manifest.json', 'approval', 'v1 active status')
    for r in [*manifest['assets'], *manifest['documents']]:
        integrity(r, 'v2_inventory')
    boards = sorted((HERE/'boards').glob('*.png'))
    check(len(boards) == 8 and len(audit['checks']) == 8, 'native_audit', 'eight boards required')
    check(sum(b['textCount'] for b in audit['checks']) == 129, 'native_audit', 'native text count')
    for board, node in zip(boards, audit['checks']):
        size = list(struct.unpack('>II',board.read_bytes()[16:24]))
        check(size == [math.ceil(node['width']),math.ceil(node['height'])], 'native_audit', f'export/node size {board.name}')
        check(not node['failures'] and node['minimumTextContrast'] >= 4.5, 'native_audit', node['id'])
    for pair in audit['pairs']:
        actual = contrast(pair['foreground'],pair['background'])
        check(round(actual,2) == pair['ratio'] and actual >= 4.5, 'contrast', str(pair))
    check(len(audit['images']) == 12, 'native_audit', 'content-image count')
    for image in audit['images']:
        fills = image['fills']
        check(len(fills) == 1 and fills[0]['type'] == 'IMAGE' and bool(fills[0].get('imageHash')) and fills[0]['scaleMode'] == 'FIT', 'native_audit', f"unfilled image {image['id']}")
    orilla_fill = next(n for n in audit['images'] if n['id'] == '20:250')['fills'][0]
    check(all(v == 0 for v in orilla_fill['filters'].values()), 'orilla', 'comparison recolored')
    facts = Counter(t['characters'] for t in audit['texts'])
    expected_facts = ['Ver carta','Café con leche','Carta general · 1,90 €','Contiene leche declarada.',
                      'Resto de información alimentaria pendiente. Consulta al personal antes de elegir.',
                      'Powered by Valiris Restaurants']
    for fact in expected_facts:
        check(facts[fact] == 4, 'factual_parity', fact)
    check(facts['Casa del Patio y de la Huerta Mediterránea de San Sebastián'] == 2, 'factual_parity', 'long name preserved')
    check(any('Speisekarte ansehen' in t['characters'] and 'no traducción aprobada' in t['characters'] for t in audit['texts']), 'localisation', 'DE sample/boundary absent')
    check(len(prompts['records']) == 11, 'provenance', '11 generation records')
    for record in prompts['records']:
        check(bool(record['prompt']) and (HERE/record['output']).is_file(), 'provenance', record['output'])
        for reference in record['references']:
            check((HERE/reference).is_file(), 'provenance', reference)
    for path in (HERE/'sources').glob('*.txt'):
        text = path.read_text(encoding='utf-8-sig')
        check('SIL OPEN FONT LICENSE' in text and 'Version 1.1' in text, 'font_notices', path.name)
    check(len(list((HERE/'reference-evidence').iterdir())) == 33, 'provenance', 'complete archived review derivatives')
    documents = [*HERE.glob('*.md'), ROOT/GUIDE, HERE.parent/'README.md', HERE.parent/'RETORNO_G1.es.md', *[HERE.parent/n for n in archives]]
    link_count = 0
    for document in documents:
        for target in re.findall(r'\]\(([^)]+)\)', document.read_text(encoding='utf-8-sig')):
            target = target.strip('<>').split('#',1)[0]
            if not target or re.match(r'^[a-z]+:', target, re.I):
                continue
            link_count += 1
            check((document.parent/target).exists(), 'local_links', f'{document.name}: {target}')
    guide = (ROOT/GUIDE).read_text(encoding='utf-8-sig')
    for phrase in ('Carácter a la mesa', 'Sala viva', 'Powered by Valiris Restaurants', 'G2.08', 'G2.09', 'G6', 'G2.04', 'G2.05', 'not approved', 'autonomous'):
        check(phrase.lower() in guide.lower(), 'handoff', phrase)
    check(manifest['figma']['nativeTextCount'] == 129 and manifest['figma']['contentImages'] == 12 and manifest['figma']['boards'] == audit['checks'], 'handoff', 'manifest/audit correspondence')
    declarations = '\n'.join(n['characters'] for n in audit.get('directionDeclarations', []))
    check('no branding definitivo' in declarations and 'no se limita a estos cuatro' in declarations, 'approval', 'native direction/open repertoire declaration')
    check('Not final branding' in audit.get('pageName', ''), 'approval', 'page direction state')
    check('Freely open' in manifest['recommendation'].get('repertoire', '') and 'characters' not in manifest['recommendation'], 'approval', 'samples presented as fixed roster')
    check('not definitive branding' in guide and 'not limited to plate, pear, aubergine and cup' in guide, 'approval', 'guide direction/repertoire declaration')
    rejected_red = round(contrast('#251E2E','#F83E49'),2)
    check(rejected_red < 4.5, 'contrast', 'red reading fix evidence')
    report = {'result':'PASS' if not failures else 'FAIL','date':'2026-10-03',
              'branch':manifest['git']['branch'],'revisionStart':START,
              'passedByGroup':dict(passed),'failures':failures,
              'summary':{'boards':8,'nativeTexts':129,'contentImages':12,
                         'minimumNativeTextContrast':min(b['minimumTextContrast'] for b in audit['checks']),
                         'rejectedInkOnRedContrast':rejected_red,'verifiedTextPairs':audit['pairs'],
                         'assets':len(manifest['assets']),'frozenSourceRecords':len(manifest['repositorySources']), 'localLinks':link_count},
              'limits':'Recorded native solid text and immediate-parent bounds; raster/generated content excluded. Integrity checks, not integral accessibility, interaction, localisation, legal, user research or independent review.',
              'softwareTests':'Not applicable: no application/configuration changes',
              'gitWhitespaceReview':'git -c core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol diff --cached --check; CRLF accepted for preserved historical manifest, no configuration change'}
    if args.write_checks:
        (HERE/'checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
