import sys; sys.path.insert(0,'.')
from tex import *
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500;700&family=Inter:wght@400;600;700&display=block">'
CSS='''*{box-sizing:border-box;margin:0}body{width:600px;background:#EEE6D3;color:#16130F;font:13px/1.4 Inter,sans-serif}
.tx{position:absolute;inset:0;width:100%;height:100%;display:block}
.A{font-family:Archivo;font-weight:900;text-transform:uppercase;line-height:.84}.S{font-family:"Instrument Serif";font-style:italic}
.M{font-family:"JetBrains Mono";font-weight:700;text-transform:uppercase;letter-spacing:.14em}
.k{font:700 9px "JetBrains Mono";letter-spacing:.18em;text-transform:uppercase;color:#7a7264}
.w{position:relative;padding:26px 22px;display:grid;gap:16px}
.sw{position:relative;overflow:hidden;border-radius:4px}
.lab{position:absolute;left:10px;bottom:9px;font:700 8px "JetBrains Mono";letter-spacing:.16em;text-transform:uppercase}
'''
def A(wd,sz,extra=''): return f'style="font-stretch:{wd}%;font-size:{sz}px;{extra}"'
pal=[('bordeaux','Bordeaux','#5E1A24','#EEE6D3'),('bouteille','Vert bouteille','#1E3B2C','#EEE6D3'),('emeraude','Émeraude','#0F5A43','#EEE6D3'),('olive','Olive','#6B6A34','#EEE6D3'),('terre','Terre','#A65A34','#EEE6D3'),('pelouse','Pelouse','#4C7A35','#EEE6D3'),('sable','Craie','#EEE6D3','#16130F'),('or','Or Pépite','#C9A03A','#16130F')]
pals=''.join(f'<div style="display:grid;gap:4px"><div style="position:relative;height:58px;overflow:hidden;border-radius:3px;outline:1px solid #16130F22">{cuir(c,100,58,k+1) if k<4 else (terre(100,58) if n=="terre" else pelouse(100,58,3) if n=="pelouse" else papier(100,58,c))}</div><b style="font:700 10.5px Inter">{t}</b><span class="k" style="font-size:7.5px">{c}</span></div>' for k,(n,t,c,f) in enumerate(pal))
html=f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>
<div style="position:absolute;inset:0">{papier(600,1400)}</div><div class="w">
<div class="k">SFL · Identité réseaux <span style="color:#5E1A24">V2</span> · les matières</div>
<div><div class="A" {A(125,46)}>Cuir, tissu,</div><div style="display:flex;align-items:baseline;gap:10px"><span class="S" style="font-size:46px;line-height:.9">terre</span><span class="A" {A(62,46,"color:#5E1A24")}>et pelouse</span></div>
<p style="color:#5a5246;margin-top:8px;max-width:62ch">Les couleurs du vestiaire et du terrain : le bordeaux d'un vieux cuir, le vert bouteille d'un maillot, l'olive, la terre, la pelouse tondue. Le sigle SFL est brodé, comme un écusson. Toutes les matières sont dessinées en code : pas d'image générée.</p></div>
<div style="display:grid;grid-template-columns:repeat(8,1fr);gap:6px">{pals}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
<div class="sw" style="aspect-ratio:1">{cuir('#5E1A24',280,280,3)}{couture('#C9A03A',10,6)}<div style="position:absolute;inset:0;display:grid;place-items:center">{brode('#D8B04A','62px')}</div><div class="lab" style="color:#EEE6D3">Cuir bordeaux · fil or</div></div>
<div class="sw" style="aspect-ratio:1">{tissu('#1E3B2C',280,280)}<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:150px;height:96px;border-radius:10px;overflow:hidden;box-shadow:0 4px 8px rgba(0,0,0,.45)">{cuir('#EEE6D3',150,96,8)}{couture('#1E3B2C',5,6)}<div style="position:absolute;inset:0;display:grid;place-items:center">{brode('#1E3B2C','36px',False)}</div></div><div class="lab" style="color:#EEE6D3">Maillot vert bouteille · écusson</div></div>
<div class="sw" style="aspect-ratio:1">{pelouse(280,280,7)}<div style="position:absolute;left:0;right:0;top:62%;height:5px;background:#EEE6D3;opacity:.85"></div><div style="position:absolute;inset:0;display:grid;place-items:center">{brode('#EEE6D3','50px')}</div><div class="lab" style="color:#EEE6D3">Pelouse · ligne de craie</div></div>
<div class="sw" style="aspect-ratio:1">{tissu('#6B6A34',280,280)}<div style="position:absolute;inset:0;display:grid;place-items:center">{brode('#5E1A24','56px')}</div><div class="lab" style="color:#EEE6D3">Maillot olive · fil bordeaux</div></div>
</div>
<div class="k" style="display:flex;justify-content:space-between"><span>Sunday Five League · V2 matières</span><span>Textures en code, sans IA</span></div>
</div></body></html>'''
open('p1.html','w').write(html)
