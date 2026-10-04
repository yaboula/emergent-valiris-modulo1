"""Refresh the explicitly owned v2 evidence inventory after intentional edits."""
from pathlib import Path
import hashlib
import json
import struct

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OLD = HERE.parent
TEXT = {'.md', '.js', '.json', '.py', '.svg', '.txt'}


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')


def record(path, kind, status, rights):
    data = path.read_bytes()
    if path.suffix in TEXT:
        data = data.replace(b'\r\n', b'\n')
    out = {'path': path.relative_to(ROOT).as_posix(), 'kind': kind,
           'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
           'state': status, 'rights': rights}
    if path.suffix == '.png':
        assert data[:8] == b'\x89PNG\r\n\x1a\n'
        out['dimensions'] = list(struct.unpack('>II', data[16:24]))
    if path.suffix in TEXT:
        out['hashPolicy'] = 'UTF-8, LF-equivalent text; binaries hashed exactly'
    return out


def main():
    # Normalize only new v2 texts and intentionally revised active entry points.
    active = [ROOT / 'docs/design/valiris-restaurants-brand-direction.md',
              OLD / 'README.md', OLD / 'RETORNO_G1.es.md']
    for p in [*HERE.rglob('*'), *active]:
        if p.is_file() and p.suffix in TEXT:
            text = p.read_text(encoding='utf-8-sig').replace('\r\n', '\n').rstrip() + '\n'
            if p.parent == HERE / 'sources':
                text = '\n'.join(line.rstrip() for line in text.splitlines()) + '\n'
            p.write_text(text, encoding='utf-8', newline='\n')
    legacy = read_json(OLD / 'manifest.json')
    audit = read_json(HERE / 'figma-validation.json')
    prompts = read_json(HERE / 'prompts.json')
    states = {p['output']: p['status'] for p in prompts['records']}
    assets = []
    for directory in ('assets', 'boards', 'reference-evidence', 'sources'):
        for path in sorted((HERE / directory).iterdir()):
            if not path.is_file():
                continue
            local = path.relative_to(HERE).as_posix()
            if directory == 'assets':
                kind = 'authored-lettering-vector' if path.suffix == '.svg' else 'generated-concept-raster'
                status = states.get(local, 'Authored lettering concept; optical production pending')
                rights = 'AI-assisted evaluation concept; no exclusivity, trademark clearance or production approval asserted'
            elif directory == 'boards':
                kind, status = 'figma-board-export', 'Author-reviewed v2 proposal; not approved'
                rights = 'Mixed authored layout, generated concepts and identified reference quotations; see individual source states'
            elif directory == 'reference-evidence':
                kind, status = 'supplied-reference-review-derivative', 'Evaluation reference only; not an owned production resource'
                rights = 'Reference authors retain rights; production permission/clearance not established; Gorilla authorship unknown'
            else:
                kind, status = 'font-source-license-notice', 'Verified source notice, not a font binary'
                rights = 'Retained SIL Open Font License 1.1 source notice; actual Figma binary version unknown'
            assets.append(record(path, kind, status, rights))
    skip = {'manifest.json', 'checks.json', 'publication.json'}
    docs = [p for p in HERE.iterdir() if p.is_file() and p.suffix in TEXT and p.name not in skip]
    docs.extend(active[:3])
    manifest = {
        'schemaVersion': 2, 'edition': '2026-10-03 / v2',
        'status': 'General creative direction idea, not definitive branding; positive founder feedback on direction; palette, details, hierarchy and final identity approval pending',
        'recommendation': {'direction': 'A / Carácter a la mesa — kitchen family',
                           'sampleCharacters': ['Plate', 'Pear', 'Aubergine', 'Cup'],
                           'repertoire': 'Freely open to any food, cooking or restaurant-related subject; no numerical limit or fixed cast',
                           'alternative': 'B / Sala viva', 'hierarchy': 'R1 / restaurant-led endorsement'},
        'founderSteering': 'General idea positively received and direction clear; current colors imperfect; many details to refine. Explicit request: direction idea, not definitive branding; repertoire freely open beyond four samples. No final identity/palette/hierarchy approval inferred.',
        'history': {'v1': 'Rejected; recommendation withdrawn; old assets retained',
                    'sensoryExploration': 'Superseded after founder kitchen steering; retained as process evidence'},
        'git': {'branch': 'docs/m1-g2-06-restaurants-brand',
                'baseline': '27861fd94dafd51889e2f223000320d66fd39dae',
                'revisionStart': 'd44942ea7eee6471c8d6933dab91dcd9f6b37009',
                'pullRequest': 'https://github.com/yaboula/valiris-restaurants/pull/26',
                'basePullRequest': 'https://github.com/yaboula/valiris-restaurants/pull/25',
                'ownedPaths': legacy['git']['ownedPaths'], 'publicationRecord': 'publication.json'},
        'figma': {'fileKey': 'uJSv4mj3oi9Br8Za9WuZAz', 'team': 'Valiris', 'page': audit['pageId'],
                  'url': 'https://www.figma.com/design/uJSv4mj3oi9Br8Za9WuZAz?node-id=20-2',
                  'pageName': audit['pageName'], 'directionDeclarations': audit['directionDeclarations'],
                  'boards': audit['checks'], 'nativeTextCount': sum(b['textCount'] for b in audit['checks']),
                  'contentImages': len(audit['images']), 'oldPage': '0:1 / rejected; preserved',
                  'fontBinaryVersions': 'Unavailable; native Gabarito Black/Bold and Source Sans 3 Regular/Bold loaded; no binaries distributed'},
        'orilla': legacy['orilla'], 'repositorySources': legacy['repositorySources'],
        'providedOriginals': [
            {'name': 'screencapture-eat-curious-2026-10-03-17_04_54.pdf', 'bytes': 4651690, 'sha256': '7374e114355ca2dcb9717401e59ec09cafc9dcb211478a6bf82a904ba8fb7461', 'review': 'All 3 pages rendered and inspected'},
            {'name': 'screencapture-duolingo-2026-10-03-17_07_05.pdf', 'bytes': 2440590, 'sha256': '634044da11fb71a4b1855896210615a2fd57c85ab68dfadd1a33c7a2e4a04e29', 'review': 'All 4 pages rendered and inspected'},
            {'name': 'scroll-recording-1791039658228.webm', 'bytes': 11707828, 'sha256': '026529e3e6450cc2f39a6b420d647519a7639735930a2922956e2dc22154d8eb', 'durationSecondsApprox': 41.290, 'decodedFrames': 1217, 'review': 'Full timeline at 0.5-second sampling; logo and type sequences at 0.125 seconds; VP9 1920x1080, no audio'},
            {'name': 'scroll-recording-1791039983148.webm', 'bytes': 7533263, 'sha256': '012a7abd78e49c85743dfb42a93f0c102af5c236beea1b44bbcef869bc5eebe8', 'durationSecondsApprox': 25.869, 'decodedFrames': 777, 'review': 'Full timeline at 0.5-second sampling; chat and footer sequences at 0.125 seconds; VP9 1920x1080, no audio'},
            {'name': 'codex-clipboard-2ff12ceb-c0dc-488e-b86d-e092da4ac596.png', 'bytes': 822694, 'sha256': '4bd9e3f8edd316fb6d5d71ca8be7c227f7d946dfb6e72bd01dc9a874e7531ed6', 'dimensions': [1200, 1370], 'review': 'Gorilla anatomy/pose sheet; authorship and production rights unknown'}
        ],
        'referenceAvailability': 'Original supplied PDF/WebM files remain local outside Git; all page renders/contact sheets and selected frames are archived here. Derivatives support visual review, not implementation/interaction claims.',
        'fontSources': {'googleFontsCommit': '9710da1eacb3be272583c3224dcb70f9da6eadbb',
                        'projects': [{'family': 'Gabarito', 'project': 'https://github.com/naipefoundry/gabarito', 'licenseSource': 'https://github.com/google/fonts/blob/9710da1eacb3be272583c3224dcb70f9da6eadbb/ofl/gabarito/OFL.txt'},
                                     {'family': 'Source Sans 3', 'project': 'https://github.com/adobe-fonts/source-sans', 'licenseSource': 'https://github.com/google/fonts/blob/9710da1eacb3be272583c3224dcb70f9da6eadbb/ofl/sourcesans3/OFL.txt'}],
                        'license': 'Retained notices state SIL OFL 1.1; LF/trailing-space normalization only; identify/check production binaries later', 'binaryDistribution': False},
        'generation': {'tool': prompts['tool'], 'prompts': 'prompts.json', 'outputs': len(prompts['records']), 'rights': 'Concept images identified as generated; no real dishes/restaurants, precise regeneration or rights clearance claimed'},
        'pending': ['Founder A/B and R1/R2/R3 selection', 'G1 consolidation', 'G6 offer truthfulness', 'G2.04 copy/SEO/GEO same version', 'G2.05 actual localisation', 'G2.08 production/rights', 'G2.07/G2.03 applications/behaviour', 'G2.09 purposeful motion', 'G4 independent application review'],
        'assets': assets,
        'documents': [record(p, 'proposal-document-or-construction-evidence', 'Revised author evidence', 'Authored evaluation material; source/asset rights remain as individually stated') for p in sorted(docs)],
        'dynamicRecordsExcludedFromInventory': ['manifest.json (self)', 'checks.json (generated report)', 'publication.json (post-content-commit snapshot)'],
        'limits': 'Author evidence only. No full accessibility, interaction, user research, translation, legal/exclusivity, conversion or implementation test.'
    }
    write_json(HERE / 'manifest.json', manifest)
    print(f"Manifest refreshed: {len(assets)} assets; {len(docs)} documents; {len(legacy['repositorySources'])} frozen source records")


if __name__ == '__main__':
    main()
