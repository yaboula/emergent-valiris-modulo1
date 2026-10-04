import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';

const root = 'D:/the next level/valiris-restaurants';
const read = p => fs.readFileSync(p, 'utf8').replace(/^\uFEFF/, '');
const report = { errors: [], markdownFiles: 0, localLinks: 0 };
const paths = execFileSync('rg', ['--files', '--hidden', '-g', '*.md', '-g', '!.git'], { cwd: root, encoding: 'utf8' }).trim().split(/\r?\n/);
const slug = s => s.replace(/[`*_]/g, '').toLowerCase().replace(/[^\p{L}\p{N}\s_-]/gu, '').replace(/ /g, '-');
for (const p of paths) {
  const absolute = path.join(root, p);
  const source = read(absolute);
  report.markdownFiles++;
  const stripped = source.replace(/```[\s\S]*?```/g, '');
  for (const match of stripped.matchAll(/\]\(([^)]+)\)/g)) {
    const target = match[1];
    if (/^(https?:|mailto:)/.test(target)) continue;
    report.localLinks++;
    const [location, anchor] = target.split('#');
    const dest = location ? path.resolve(path.dirname(absolute), decodeURIComponent(location)) : absolute;
    if (!fs.existsSync(dest)) { report.errors.push(`${p}: missing ${target}`); continue; }
    if (anchor && dest.endsWith('.md')) {
      const headings = [...read(dest).matchAll(/^#{1,6}\s+(.+)$/gm)].map(m => slug(m[1].trim()));
      if (!headings.includes(decodeURIComponent(anchor))) report.errors.push(`${p}: missing anchor ${target}`);
    }
  }
  let width;
  for (const line of stripped.split(/\r?\n/)) {
    if (!line.startsWith('|')) { width = undefined; continue; }
    const cells = line.split('|').length - 2;
    if (width === undefined) width = cells;
    else if (cells !== width) report.errors.push(`${p}: table cell mismatch: ${line}`);
  }
}

const ledger = read(path.join(root, 'docs/research/review-ledger.md'));
const reviews = ledger.split(/\r?\n/).filter(s => /^\| RM-\d{3} \|/.test(s)).map(s => s.split('|').slice(1,-1).map(v=>v.trim()));
assert.equal(reviews.length, 50);
assert.equal(new Set(reviews.map(r=>r[0])).size, 50);
assert.equal(new Set(reviews.map(r=>r[4])).size, 50);
const themes = {}, sentiments = {}, years = {};
for (let i=0;i<reviews.length;i++) {
  const r = reviews[i];
  assert.equal(r[0], `RM-${String(i+1).padStart(3,'0')}`);
  assert.match(r[1], /^\d{4}-\d{2}-\d{2}$/);
  assert.ok(r[1] <= '2026-09-28');
  assert.ok(Number(r[2]) >= 1 && Number(r[2]) <= 5);
  themes[r[5]] = (themes[r[5]] || 0)+1;
  sentiments[r[6]] = (sentiments[r[6]] || 0)+1;
  years[r[1].slice(0,4)] = (years[r[1].slice(0,4)] || 0)+1;
}
const method = read(path.join(root,'docs/research/review-mining.md'));
for (const [code, count] of Object.entries(themes)) {
  const row = method.split(/\r?\n/).find(l=>l.startsWith(`| ${code} |`));
  assert.ok(row, code);
  assert.equal(Number(row.split('|').at(-2).trim()), count, code);
}
assert.deepEqual(sentiments, {negative:31, mixed:13, positive:6});
assert.deepEqual(years, {'2017':1,'2022':10,'2023':2,'2024':6,'2025':16,'2026':15});

const feeds = ['thefork-es.json','covermanager-alt.json'].map(p=>JSON.parse(read(`D:/the next level/research-evidence/${p}`)).feed.entry);
for (let i=0;i<40;i++) {
  const r = reviews[i], feed = feeds[i<20?0:1];
  const id = r[4].replace('Apple review ID ', '');
  const entry = feed.find(e=>e.id.label===id);
  assert.ok(entry, `${r[0]} locator`);
  assert.equal(entry.updated.label.slice(0,10), r[1], `${r[0]} date`);
  assert.equal(entry['im:rating'].label,r[2],`${r[0]} rating`);
  assert.equal(entry['im:version'].label,r[3],`${r[0]} version`);
}
report.reviews = { total: reviews.length, appleMetadataMatches:40, sourceCounts:[20,20,10], themes,sentiments,years };

const dirce = JSON.parse(read('D:/the next level/research-evidence/dirce-39371.json'));
const series = dirce.filter(r=> /^DIR187(279|280|281|282|283|305|306|307|308|309)$/.test(r.COD)).sort((a,b)=>a.COD.localeCompare(b.COD));
assert.equal(series.length,10);
report.dirce = series.map(r=>({code:r.COD,name:r.Nombre,value:r.Data[0].Valor,year:r.Data[0].Anyo}));
const expected = [73296,6811,27092,23840,8147,146853,39420,64566,31738,7385];
assert.deepEqual(report.dirce.map(r=>r.value),expected);
assert.ok(report.dirce.every(r=>r.year===2025));
assert.equal(expected.slice(1,5).reduce((a,b)=>a+b),65890);
assert.equal(expected.slice(6,10).reduce((a,b)=>a+b),143109);

for (const file of ['neighbourhood-restaurant.md','cafe.md','tourist-restaurant.md']) {
  const body = read(path.join(root,'docs/research/interviews',file));
  assert.ok(body.includes('SIMULATED — FICTIONAL.'));
  assert.ok(body.includes('No interview took place.'));
}
assert.ok(read(path.join(root,'docs/research/synthesis.md')).includes('Pending — not passed'));
assert.match(read(path.join(root,'docs/adr/0006-discovery-evidence-boundary.md')), /^---\r?\nstatus: proposed/);
report.simulations=3;
report.gate='pending';
console.log(JSON.stringify(report,null,2));
if(report.errors.length) process.exitCode=1;
