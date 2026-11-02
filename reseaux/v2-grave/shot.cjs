const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 600, height: 800 }, deviceScaleFactor: 2.5 });
 await p.goto('file:///tmp/sflv/grave/board.html'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(1500);
 const h = await p.evaluate(() => document.querySelector('.w').getBoundingClientRect().height); await p.setViewportSize({ width: 600, height: Math.ceil(h) }); await p.waitForTimeout(400);
 await p.screenshot({ path: '/home/user/visuels/sfl-v2-grave.png', fullPage: true }); await b.close(); })();
