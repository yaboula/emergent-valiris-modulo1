// Offline raster export of static SVG boards. No application or server.
import { createRequire } from 'node:module';
import { readFile, writeFile, mkdir, copyFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import crypto from 'node:crypto';
const require = createRequire(path.join(process.argv[2], 'package.json'));
const sharp = require('sharp');
const out = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const root = path.resolve(out, '../..');
const manifest = JSON.parse(await readFile(path.join(out, 'manifest.json'), 'utf8'));
await mkdir(path.join(out, 'exports'), { recursive: true });
const result = [];
for (const f of manifest.frames) {
  const input = path.join(root, f.svg), output = path.join(root, f.png);
  await sharp(input, { limitInputPixels: false }).png().toFile(output);
  const metadata = await sharp(output).metadata();
  const bytes = await readFile(output);
  result.push({ frame:f.frame, width:metadata.width, height:metadata.height, format:metadata.format,
    png_sha256:crypto.createHash('sha256').update(bytes).digest('hex'),
    svg_sha256:crypto.createHash('sha256').update(await readFile(input)).digest('hex') });
}
await writeFile(path.join(out,'checks','exports.json'),JSON.stringify({renderer:'sharp '+sharp.versions.sharp,
  svg_renderer:'rsvg '+sharp.versions.rsvg, font_embedding:false, results:result},null,2));
if(manifest.frames.length === 1){
  await mkdir(path.join(out,'iterations'),{recursive:true});
  await copyFile(path.join(out,'sources/UI-P01.svg'),path.join(out,'iterations/pc-v0.1.svg'));
  await copyFile(path.join(out,'exports/UI-P01.png'),path.join(out,'iterations/pc-v0.1.png'));
}
// Review crops are evidence, not responsive resizing.
await mkdir(path.join(out,'checks','crops'),{recursive:true});
for(const name of ['UI-P01','UI-T01','UI-Z390','UI-W768','UI-W1024','UI-L844']){
  const f = manifest.frames.find(f=>f.frame===name);if(!f)continue;
  const input=path.join(root,f.png);
  await sharp(input).extract({left:0,top:0,width:f.width,height:Math.min(f.height,1200)}).png().toFile(path.join(out,'checks','crops',name+'-entry.png'));
  if(name==='UI-P01'||name==='UI-T01'){
    for(const source of ['ORI-COPY-H02-01','ORI-COPY-H03-01','ORI-COPY-H04-01']){
      const t=f.text.find(t=>t.source===source && t.size>=26);const top=Math.max(0,Math.floor(t.y-36));
      await sharp(input).extract({left:0,top,width:f.width,height:Math.min(f.height-top,1400)}).png().toFile(path.join(out,'checks','crops',name+'-'+source+'.png'));
    }
  }
}
console.log(JSON.stringify({exported:result.length,renderer:sharp.versions.sharp,rsvg:sharp.versions.rsvg}));
