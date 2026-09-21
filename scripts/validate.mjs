import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const context=vm.createContext({});
const scripts=['data.js','data-extended.js','data-reviewed.js','data-modern.js'];
for(const file of scripts) vm.runInContext(fs.readFileSync(path.join(root,file),'utf8'),context,{filename:file});
const {rows,meta,eras}=vm.runInContext('({rows:PHYSICS_DATA,meta:FIELD_META,eras:ERAS})',context);
const ids=new Set();
for(const row of rows){
 assert(!ids.has(row.id),'Duplicate ID: '+row.id); ids.add(row.id);
 assert(/^[a-z0-9-]+$/.test(row.id),'Unsafe ID: '+row.id);
 for(const key of ['field','topic','title','date','people','formula','summary','conditions','variables','application','significance','context','kind','editorial']) assert(typeof row[key]==='string'&&row[key].trim(),`${row.id}: missing ${key}`);
 assert(meta[row.field],row.id+': unknown field');
 assert(Number.isInteger(row.year),row.id+': year');
 assert.equal(eras.filter(e=>e.test(row.year)).length,1,row.id+': ambiguous era');
 assert(Array.isArray(row.sources)&&Array.isArray(row.related));
 for(const s of row.sources){assert(s.title);assert.equal(new URL(s.url).protocol,'https:');}
}
for(const row of rows)for(const id of row.related)assert(ids.has(id),`${row.id}: missing relation ${id}`);
const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
for(const file of [...scripts,'app.js'])assert(html.includes(`src="./${file}"`),`Missing script ${file}`);
for(const field of Object.keys(meta))assert(rows.some(row=>row.field===field),'Empty field '+field);
console.log(JSON.stringify({records:rows.length,fields:Object.keys(meta).length,sourced:rows.filter(r=>r.sources.length).length,added:rows.filter(r=>r.editorial.startsWith('本次新增')).length,corrected:rows.filter(r=>r.editorial.includes('局部修正')).length}));
