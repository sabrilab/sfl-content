import sys,base64; sys.path.insert(0,'.')
from tex import *
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500;700&family=Inter:wght@400;600;700&display=block">'
CSS='''*{box-sizing:border-box;margin:0}body{width:600px;background:#fff;color:#0B0B0B;font:13px/1.4 Inter,sans-serif}.tx{position:absolute;inset:0;width:100%;height:100%;display:block}
.A{font-family:Archivo;font-weight:900;text-transform:uppercase;line-height:.84}.S{font-family:"Instrument Serif";font-style:italic;line-height:1}
.k{font:700 9px "JetBrains Mono";letter-spacing:.18em;text-transform:uppercase;color:#7a7264}.w{position:relative;padding:26px 22px;display:grid;gap:16px}.box{position:relative;overflow:hidden}'''
def A(wd,sz,extra=''): return f'style="font-stretch:{wd}%;font-size:{sz}px;{extra}"'
def mono(t,col,sz=5): return f'<span style="font:700 {sz}px JetBrains Mono;letter-spacing:.14em;text-transform:uppercase;color:{col}">{t}</span>'
NOIR='#0B0B0B'; BLANC='#FFFFFF'; CR='#EEE6D3'
L='/home/user/bola-site/public/ligue/'
def b64(p): return 'data:image/webp;base64,'+base64.b64encode(open(p,'rb').read()).decode()
sou=b64(L+'souley.webp')
pal=[('Noir','#0B0B0B'),('Blanc','#FFFFFF'),('Craie','#EEE6D3'),('Bordeaux','#5E1A24'),('Vert bouteille','#1E3B2C'),('Olive','#6B6A34'),('Terre','#A65A34'),('Pelouse','#4C7A35')]
pals=''.join(f'<div style="display:grid;gap:3px"><div style="height:40px;background:{c};outline:1px solid #0B0B0B22"></div><b style="font:700 10px Inter">{n}</b><span class="k" style="font-size:7px">{c}</span></div>' for n,c in pal)
mets=''.join(f'<div class="box" style="height:56px;border-radius:3px">{metal(k,120,56)}<div style="position:absolute;inset:0;display:grid;place-items:center">{grave(t,k,18,110)}</div></div>' for k,t in [('or','Or'),('argent','Argent'),('bronze','Bronze'),('noir','Noir')])
stones=''.join(f'<div style="display:grid;justify-items:center;gap:4px">{pierre(k,40)}<b style="font:700 10px Inter">{n}</b><span class="k" style="font-size:7px;text-align:center">{u}</span></div>' for k,n,u in [('rubis','Rubis','Impact'),('saphir','Saphir','Défensive'),('emeraude','Émeraude','Révélation'),('diamant','Diamant','Pépite d\'Or')])
# Applications
plaque=f'''<div class="box" style="aspect-ratio:4/5">{cuir('#151313',180,225,3)}{couture('#C9A03A',6,4)}
<div style="position:absolute;left:9px;right:9px;top:9px;display:flex;justify-content:space-between">{brode('#D8B04A','6.5px',False)}{mono('Les cartes · J4','#C9A03A',4.8)}</div>
<div style="position:absolute;left:18px;right:18px;top:24%;height:64px;border-radius:3px;overflow:hidden;box-shadow:0 3px 6px rgba(0,0,0,.6)">{metal('or',144,64)}<div style="position:absolute;inset:0;display:grid;place-items:center;text-align:center"><div>{grave('MVP','or',26,125)}<div style="margin-top:3px">{grave('le patron du terrain 1','or',8,100,400,'Instrument Serif',True)}</div></div></div>
<div style="position:absolute;left:5px;top:50%;transform:translateY(-50%)">{pierre('diamant',9)}</div><div style="position:absolute;right:5px;top:50%;transform:translateY(-50%)">{pierre('diamant',9)}</div></div>
<img src="{sou}" style="position:absolute;right:8%;bottom:-8%;width:38%;transform:rotate(4deg);filter:drop-shadow(0 4px 6px rgba(0,0,0,.6))">
<div style="position:absolute;left:10px;bottom:10px;color:{BLANC}"><div class="A" {A(62,18)}>Souley</div>{mono('7 buts · 3 passes',BLANC,4.6)}</div></div>'''
rows=[('or','1','Souley','412'),('argent','2','Jouneiid','398'),('bronze','3',"Coucoupop's",'377')]
podium=''.join(f'''<div style="display:grid;grid-template-columns:30px 1fr 40px;gap:6px;align-items:center;margin:5px 0"><div class="box" style="height:30px;border-radius:50%">{metal(k,30,30,15)}<div style="position:absolute;inset:0;display:grid;place-items:center">{grave(r,k,15,110)}</div></div>
<span class="A" {A(62,15)}>{n}</span><span class="A" {A(110,13,"text-align:right")}>{p}</span></div>''' for k,r,n,p in rows)
classement=f'''<div class="box" style="aspect-ratio:4/5;background:{BLANC};outline:1px solid #0B0B0B18">
<div style="position:absolute;left:9px;right:9px;top:9px;display:flex;justify-content:space-between">{brode(NOIR,'6.5px',False)}{mono('Après la J4',NOIR,4.8)}</div>
<div style="position:absolute;left:12px;right:12px;top:26px"><div class="S" style="font-size:13px">La course à la</div><div class="A" {A(125,22)}>Pépite d'Or</div><div style="margin-top:10px">{podium}</div>
{''.join(f'<div style="display:grid;grid-template-columns:30px 1fr 40px;gap:6px;border-top:1px solid #0B0B0B1a;padding:3px 0"><span class="A" {A(100,10,"text-align:center;color:#8E9194")}>{r}</span><span class="A" {A(62,11)}>{n}</span><span class="A" {A(110,10,"text-align:right")}>{p}</span></div>' for r,n,p in [(4,'Gaïl',361),(5,'Sebovic',355),(6,'Ilyes',349)])}</div></div>'''
pepite=f'''<div class="box" style="aspect-ratio:4/5;background:{NOIR}">
<div style="position:absolute;left:9px;right:9px;top:9px;display:flex;justify-content:space-between">{brode(BLANC,'6.5px',False)}{mono('24.01.27',BLANC,4.8)}</div>
<div style="position:absolute;left:0;right:0;top:20%;text-align:center;color:{BLANC}"><div class="S" style="font-size:15px">La nuit de la</div></div>
<div style="position:absolute;left:16px;right:16px;top:31%;height:58px;border-radius:2px;overflow:hidden">{metal('or',148,58,2)}<div style="position:absolute;inset:0;display:grid;place-items:center">{grave("Pépite d'Or",'or',15,95)}</div></div>
<div style="position:absolute;left:0;right:0;top:63%;display:flex;justify-content:center">{pierre('diamant',22)}</div>
<div style="position:absolute;left:0;right:0;bottom:16px;text-align:center;color:{BLANC}"><div class="A" {A(100,11)}>13 dimanches. Une seule.</div><div style="margin-top:4px">{mono('Saison 1 · gravé à vie',BLANC,4.4)}</div></div></div>'''
def sc(x,h): return f'<div style="width:180px;height:{h}px;transform:scale(1);"></div>'
html=f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body><div class="w">
<div class="k">SFL · V2 · <span style="color:#8A6A1E">gravé</span> · métaux nobles, pierres, noir et blanc</div>
<div><div class="A" {A(125,44)}>Gravé</div><div style="display:flex;align-items:baseline;gap:10px"><span class="S" style="font-size:44px;line-height:.9">dans le</span>{grave('métal','or',44,62)}</div>
<p style="color:#55554f;margin-top:8px;max-width:62ch">Les noms et les titres se gravent dans l'or, l'argent et le bronze, comme une plaque de trophée. Les pierres sont rares : une seule par visuel, et seulement quand un titre est gagné. Ton noir et ton blanc reviennent comme fonds principaux, avec les couleurs du terrain.</p></div>
<div><div class="k" style="margin-bottom:6px">La palette, avec ton noir et ton blanc</div><div style="display:grid;grid-template-columns:repeat(8,1fr);gap:6px">{pals}</div></div>
<div><div class="k" style="margin-bottom:6px">Les métaux : un rang, un métal</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">{mets}</div>
<div class="k" style="margin-top:6px;font-size:7.5px">Or : 1er, MVP, Pépite · Argent : 2e · Bronze : 3e · Noir : la plaque de tous les jours</div></div>
<div><div class="k" style="margin-bottom:8px">Les pierres : avec parcimonie</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">{stones}</div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px">
<div><div style="width:180px;zoom:.96">{plaque}</div><div class="k" style="margin-top:4px">MVP · plaque or sur cuir noir</div></div>
<div><div style="width:180px;zoom:.96">{classement}</div><div class="k" style="margin-top:4px">Classement · médailles gravées</div></div>
<div><div style="width:180px;zoom:.96">{pepite}</div><div class="k" style="margin-top:4px">La Pépite d'Or · noir, or, diamant</div></div></div>
<div class="k" style="display:flex;justify-content:space-between"><span>Sunday Five League · V2 gravé</span><span>Métaux et pierres en code, sans IA</span></div>
</div></body></html>'''
open('board.html','w').write(html)
