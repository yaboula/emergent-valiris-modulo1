const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const assert = require('node:assert/strict');
const base = process.argv[2] || 'origin/main';
const git = (...args) => execFileSync('git', args, { encoding: 'utf8' }).trimEnd();
const read = p => fs.readFileSync(p, 'utf8').replace(/\r\n/g, '\n');
const original = p => git('show', `${base}:${p}`).replace(/\r\n/g, '\n');
const changed = git('diff', base, '--name-only').split('\n').filter(Boolean);
assert.equal(changed.length, 10);
assert(changed.every(p => p.endsWith('.md') && !/docs\/(adr|research)\//.test(p)));
const matrixPath = 'docs/product/m0-capability-matrix.md';
const matrix = read(matrixPath);
const block = s => s.slice(s.indexOf('## 2. Complete capability matrix'), s.indexOf('## 5. Review and continuity'));
assert.equal(block(matrix), block(original(matrixPath)), 'Capability rows, prose boundaries and decisions changed');
const rows = [...matrix.matchAll(/^\| (B\d\.\d{2}) \/ L\d+ \|[^\n]+/gm)];
assert.equal(rows.length, 72);
assert.equal(new Set(rows.map(r => r[1])).size, 72);
for (const [treatment, count] of [['Included', 36], ['Configurable', 30], ['Connection-dependent', 6]]) {
  assert.equal(rows.filter(r => r[0].split('|')[4].trim() === treatment).length, count);
}
const criteriaPath = 'docs/product/m0-journeys-and-criteria.md';
const criterionBody = s => s.slice(0, s.indexOf('Next deliverable:'));
assert.equal(criterionBody(read(criteriaPath)), criterionBody(original(criteriaPath)), 'Journey criteria changed');
const briefsPath = 'docs/product/m1-design-briefs.md';
const scopes = s => [...s.matchAll(/\*\*Scope:\*\*[\s\S]+?(?=\*\*Dependencies and pending decisions:\*\*)/g)].map(r => r[0]);
assert.equal(scopes(read(briefsPath)).length, 2);
assert.deepEqual(scopes(read(briefsPath)), scopes(original(briefsPath)), 'Scope, outputs or review criteria changed');
const handoff = read('../HANDOFF.md');
for (let i = 1; i <= 18; i++) assert(new RegExp(`^### ${i}\\. `, 'm').test(handoff), `History section ${i} missing`);
for (const sha of ['b36dfe2', 'f5d459c', '186ca62', 'b44510b', '3ef9d6f']) assert(handoff.includes(sha));
assert(handoff.indexOf('## Estado vigente') < handoff.indexOf('## Historial conservado'));
let links = 0;
for (const p of [...changed, '../HANDOFF.md']) {
  const text = read(p);
  assert(!/^(<<<<<<< |=======\s*$|>>>>>>> )/m.test(text), `Conflict marker: ${p}`);
  if (p !== '../HANDOFF.md') {
    assert(!/Co-authored-by:|Generated with|AI agent|Codex|ChatGPT/i.test(text), `Attribution: ${p}`);
    assert(!/Complete authorised integration\/tracker closure|Prepare the formal closure|Close the assignment after M0|Next action: M0|Full M0 closure still requires|M0 preparation\/dependencies still open/.test(text), `Stale instruction: ${p}`);
  }
  let width = 0;
  for (const line of text.split('\n')) {
    if (!line.startsWith('|')) { width = 0; continue; }
    const next = (line.match(/\|/g) || []).length;
    assert(!width || width === next, `Table width: ${p}`);
    width = next;
  }
  for (const match of text.matchAll(/\]\(([^)]+)\)/g)) {
    const target = match[1];
    if (/^(https?:|mailto:|#)/.test(target)) continue;
    const resolved = path.resolve(path.dirname(p), target.split('#')[0]);
    assert(fs.existsSync(resolved), `Missing local target: ${p} -> ${target}`);
    links++;
  }
}
const report = { documentationFiles: changed.length, handoffFiles: 1, localTargets: links, sourceRows: 72, treatments: [36,30,6], preservedHistorySections: 18, result: 'PASS', scopeAndCriteriaUnchanged: true, sourcesAndADRsUnchanged: true };
fs.writeFileSync('../research-evidence/operational-handover-checks.json', JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report));
