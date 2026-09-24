import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const context=vm.createContext({});
const scripts=['data.js','data-extended.js','data-reviewed.js','data-modern.js','data-expansion.js'];
for(const file of scripts) vm.runInContext(fs.readFileSync(path.join(root,file),'utf8'),context,{filename:file});
const {rows,meta,eras}=vm.runInContext('({rows:PHYSICS_DATA,meta:FIELD_META,eras:ERAS})',context);
const ids=new Set();
const titles=new Map();
for(const row of rows){
 assert(!ids.has(row.id),'Duplicate ID: '+row.id); ids.add(row.id);
 assert(/^[a-z0-9-]+$/.test(row.id),'Unsafe ID: '+row.id);
 for(const key of ['field','topic','title','date','people','formula','summary','conditions','variables','application','significance','context','kind','editorial']) assert(typeof row[key]==='string'&&row[key].trim(),`${row.id}: missing ${key}`);
 const normalizedTitle=row.title.toLowerCase().replace(/[\s·—–-]/g,'');
 assert(!titles.has(normalizedTitle),`Duplicate title: ${row.title} / ${titles.get(normalizedTitle)}`); titles.set(normalizedTitle,row.id);
 assert(meta[row.field],row.id+': unknown field');
 assert(Number.isInteger(row.year),row.id+': year');
 assert.equal(eras.filter(e=>e.test(row.year)).length,1,row.id+': ambiguous era');
 assert(Array.isArray(row.sources)&&Array.isArray(row.related));
 for(const s of row.sources){assert(typeof s.title==='string'&&s.title.trim(),`${row.id}: source title`);assert.equal(new URL(s.url).protocol,'https:');}
 assert.equal(new Set(row.sources.map(s=>s.url)).size,row.sources.length,`${row.id}: duplicate source`);
}
for(const row of rows)for(const id of row.related)assert(ids.has(id),`${row.id}: missing relation ${id}`);
const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
for(const file of [...scripts,'app.js'])assert(html.includes(`src="./${file}"`),`Missing script ${file}`);
for(const field of Object.keys(meta))assert(rows.some(row=>row.field===field),'Empty field '+field);
assert.equal(rows.length,240,'Unexpected record count');
assert.equal(Object.keys(meta).length,17,'Unexpected field count');
assert.equal(rows.filter(r=>r.editorial.startsWith('第二轮新增')).length,60,'Second expansion count');
assert(rows.filter(r=>r.editorial.startsWith('第二轮新增')).every(r=>r.sources.length),'Unsourced second expansion');
console.log(JSON.stringify({records:rows.length,fields:Object.keys(meta).length,sourced:rows.filter(r=>r.sources.length).length,added:rows.filter(r=>r.editorial.startsWith('本次新增')).length,corrected:rows.filter(r=>r.editorial.includes('局部修正')).length}));
