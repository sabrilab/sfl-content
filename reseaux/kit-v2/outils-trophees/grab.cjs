const { chromium } = require('playwright'); const fs = require('fs'); const http = require('http'); const path = require('path');
const root = '/tmp/sflv/coupes/dist';
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]) === '/' ? 'index.html' : decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'Content-Type': f.endsWith('.js') ? 'text/javascript' : 'text/html' }); r.end(d); }); }).listen(8765);
(async () => { const b = await chromium.launch({ args: ['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'] }); const p = await b.newPage();
  p.on('console', m => console.log('console:', m.text().slice(0,200)));
  await p.goto('http://127.0.0.1:8765/'); await p.waitForFunction(() => document.body.dataset.ok === '1', null, { timeout: 120000 });
  const out = await p.evaluate(() => window.__coupes); fs.mkdirSync('/tmp/sflv/coupes/png', { recursive: true });
  for (const [k, v] of Object.entries(out)) { if (!v) { console.log('vide', k); continue; } fs.writeFileSync(`/tmp/sflv/coupes/png/${k}.png`, Buffer.from(v.split(',')[1], 'base64')); console.log('ok', k); }
  await b.close(); srv.close(); })();
