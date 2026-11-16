import base64,re,pathlib,json
D=re.search(r' d="([^"]+)"',open('/home/user/SFL/public/bola/sfl.svg').read()).group(1)
im=lambda f:'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()
P=[('Jouneid','Jouneid.jpg'),("Coucoupop's",'Coucou.jpg'),('Sidali','Sidali.jpg'),('Ilyes','Ilyes.jpg')]
G='#2F7D4E'
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@700;800&display=block">'
CSS='*{box-sizing:border-box;margin:0}.H{font-family:Anton,sans-serif;text-transform:uppercase;line-height:.84;white-space:nowrap;color:#fff}'
sig=lambda c,h:f'<svg viewBox="0 0 735 237" style="height:{h}px;width:auto;display:block"><path d="{D}" fill="{c}"/></svg>'
grain='<svg style="position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:overlay;pointer-events:none"><filter id="gr"><feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="3" seed="9"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 .3"/></feComponentTransfer></filter><rect width="100%" height="100%" filter="url(#gr)"/></svg>'
def card(n,f,fs):
    sz='cover' if f=='Coucou.jpg' else 'auto 128%'
    return f'''<div style="position:relative;overflow:hidden;background:#111"><div style="position:absolute;inset:0;background:url({im(f)}) center 22%/{sz};filter:grayscale(1) contrast(1.18) brightness(.95)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(transparent 55%,rgba(0,0,0,.85))"></div><div class="H" style="position:absolute;left:8%;bottom:5%;font-size:{fs}px">{n}</div></div>'''
def page(w,h,inner): return f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{width:{w}px;height:{h}px}}</style></head><body><div style="position:relative;width:{w}px;height:{h}px;background:#0A0A0A;overflow:hidden">{inner}{grain}</div></body></html>'
# Bannière 1600x900
grid=''.join(card(n,f,40) for n,f in P)
open('banniere.html','w').write(page(1600,900,f'''<div style="position:absolute;left:0;right:0;top:170px;bottom:0;display:grid;grid-template-columns:repeat(4,1fr);gap:4px">{grid}</div>
<div style="position:absolute;left:44px;top:40px">{sig('#fff',30)}</div><div class="H" style="position:absolute;left:44px;top:84px;font-size:72px">Ils visent la Pépite.</div>
<div style="position:absolute;right:44px;top:48px;background:{G};color:#fff;font:800 15px Inter;letter-spacing:.18em;text-transform:uppercase;padding:8px 12px">Saison 1</div>'''))
# Post 1080x1350 : grille 2x2
grid2=''.join(card(n,f,46) for n,f in P)
open('post.html','w').write(page(1080,1350,f'''<div style="position:absolute;left:0;right:0;top:250px;bottom:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:4px">{grid2}</div>
<div style="position:absolute;left:48px;top:44px">{sig('#fff',30)}</div><div class="H" style="position:absolute;left:48px;top:100px;font-size:104px">Ils visent la Pépite.</div>'''))
