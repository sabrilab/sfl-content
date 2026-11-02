const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const OUT = process.argv[2]; const jobs = JSON.parse(fs.readFileSync('jobs.json'));
(async () => { const b = await chromium.launch();
 for (const j of jobs) { const p = await b.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: j.scale });
  await p.goto('file://' + j.html); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(700);
  const out = path.join(OUT, j.out + '.png'); fs.mkdirSync(path.dirname(out), { recursive: true });
  await p.screenshot({ path: out, clip: { x: 0, y: 0, width: j.w, height: j.h } }); await p.close(); console.log(j.out, j.w*j.scale+'x'+j.h*j.scale); }
 await b.close(); })();
