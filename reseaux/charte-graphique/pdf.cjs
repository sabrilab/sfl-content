const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1123, height: 794 }, deviceScaleFactor: 2 });
 await p.goto('file:///tmp/sflv/charte/charte.html'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(2500);
 await p.pdf({ path: '/home/user/SFL-charte-graphique-reseaux.pdf', width: '297mm', height: '210mm', printBackground: true });
 const n = await p.evaluate(() => document.querySelectorAll('.pg').length);
 for (let i = 0; i < n; i++) { const el = (await p.$$('.pg'))[i]; await el.screenshot({ path: `/tmp/sflv/charte/p${String(i+1).padStart(2,'0')}.png` }); }
 await b.close(); })();
