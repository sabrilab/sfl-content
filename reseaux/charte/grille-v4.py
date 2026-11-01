import base64,re
P='/home/user/SFL/public/'
sig=re.sub(r'<!--.*?-->','',open(P+'bola/sfl.svg').read(),flags=re.S)
def svg(col,h): return sig.replace('#08090B',col).replace('<svg ',f'<svg style="height:{h};width:auto;display:block" ',1)
def b64(p): return 'data:image/webp;base64,'+base64.b64encode(open(p,'rb').read()).decode()
cov=lambda n: b64(P+f'actus/couvertures/{n}-720.webp')
sou=b64('/home/user/bola-site/public/ligue/souley.webp')
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500;700&family=Inter:wght@400;600;700&display=block">'
CSS='''
:root{--blanc:#FFFFFF;--papier:#F2F0E9;--encre:#0E0E10;--bleu:#2563FF;--ciel:#3D9BFF;--corail:#FF5A3C;--citron:#E6F24A;--vert:#12B76A;--or:#E9B10B;--pciel:#CFE0FF;--ppeche:#FFD8C4;--por:#F2DC9B;--gris:#8A8A86}
*{box-sizing:border-box;margin:0}body{background:var(--papier);color:var(--encre);font:13px/1.4 Inter,sans-serif;width:600px}
.w{padding:26px 22px;display:grid;gap:18px}
.A{font-family:Archivo;font-weight:900;text-transform:uppercase;line-height:.84}
.S{font-family:"Instrument Serif";font-style:italic;font-weight:400}
.M{font-family:"JetBrains Mono";font-weight:700;text-transform:uppercase;letter-spacing:.12em}
.k{font:700 9px "JetBrains Mono";letter-spacing:.18em;text-transform:uppercase;color:var(--gris)}
.t{position:relative;overflow:hidden;aspect-ratio:4/5}
.ph{position:absolute;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.1)}
.mini{position:absolute;left:7px;right:7px;top:7px;display:flex;justify-content:space-between;align-items:center;font:700 4.6px "JetBrains Mono";letter-spacing:.12em;text-transform:uppercase}
'''
def mini(col,r='J4'): return f'<div class="mini" style="color:{col}"><span>{svg(col,"5px")}</span><span>{r}</span></div>'
def A(wd,sz,extra=''): return f'style="font-stretch:{wd}%;font-size:{sz}px;{extra}"'
tiles=[
# 1 La Course, blanc
f'''<div class="t" style="background:var(--blanc)">{mini('#0E0E10','S1 · J4')}<div style="position:absolute;left:8px;top:16px"><div class="A" {A(125,25)}>La<br>Course</div><div class="S" style="font-size:12px;color:var(--bleu)">vers la Pépite d'Or</div></div>
<div style="position:absolute;left:8px;right:8px;bottom:8px;display:grid;gap:2px">{''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid #0E0E1022;padding-top:2px"><span class="A" {A(62,13)}>{i} {n}</span><span class="M" style="font-size:5px;color:{c}">{a}</span></div>' for i,n,a,c in [(1,'Souley','▲2','#2563FF'),(2,'Jouneiid','▼1','#8A8A86'),(3,"Coucoupop's",'▲4','#2563FF')])}</div></div>''',
# 2 But, bleu
f'''<div class="t" style="background:var(--pciel)">{mini('#0E0E10','J4 · 14:23')}<div class="ph" style="left:8px;right:8px;top:16px;height:48%;background-image:url({cov('cage-1')})"></div>
<div style="position:absolute;left:8px;bottom:8px"><div class="S" style="font-size:13px">et soudain,</div><div class="A" {A(125,34)}>But.</div><div class="M" style="font-size:4.6px;margin-top:3px">Jouneiid · Terrain 1</div></div></div>''',
# 3 Portrait, papier blanc
f'''<div class="t" style="background:var(--blanc)">{mini('#0E0E10','Portrait')}<div class="ph" style="right:8px;top:16px;width:52%;bottom:8px;background-image:url({cov('silhouette-1')})"></div>
<div style="position:absolute;left:8px;top:22px;width:40%"><div class="S" style="font-size:12.5px;line-height:1.05">« Je suis venu seul. Maintenant je connais tout le monde. »</div></div>
<div style="position:absolute;left:8px;bottom:8px"><div class="A" {A(62,18)}>Ayman</div><div class="M" style="font-size:4.6px;color:var(--gris)">3 dimanches · D2</div></div></div>''',
# 4 Il manque 1, corail
f'''<div class="t" style="background:var(--ppeche)">{mini('#0E0E10','Dimanche 12 h 30')}<div style="position:absolute;left:8px;right:8px;top:30%"><div class="A" {A(125,26)}>Il manque</div><div class="A" {A(125,92,"line-height:.8")}>1.</div></div>
<div style="position:absolute;left:8px;bottom:8px" class="M"><span style="font-size:5px">Viens seul · getbola.app</span></div></div>''',
# 5 photo pleine
f'''<div class="t" style="background:#000">{''}<div class="ph" style="inset:0;background-image:url({cov('ombres-1')})"></div>{mini('#fff','J4')}
<div style="position:absolute;left:8px;bottom:8px;background:var(--pciel);padding:3px 5px" class="A" {A(100,10)}>Hippodrome · Marcq</div></div>''',
# 6 Les cartes
f'''<div class="t" style="background:var(--papier)">{mini('#0E0E10','Les cartes · J4')}<div style="position:absolute;left:8px;top:16px"><div class="A" {A(125,30)}>MVP</div><div class="S" style="font-size:12px">le patron du terrain 1</div></div>
<img src="{sou}" style="position:absolute;right:10px;bottom:-6%;width:46%;transform:rotate(5deg)"><div style="position:absolute;left:8px;bottom:8px"><div class="A" {A(62,20)}>Souley</div><div class="M" style="font-size:4.6px">7 buts · 3 passes</div></div>
</div>''',
# 7 Ta note, vert
f'''<div class="t" style="background:var(--pciel)">{mini('#0E0E10','Ta note')}<div style="position:absolute;left:8px;top:20px" class="A" {A(62,18)}>Sebovic<br>monte.</div>
<div style="position:absolute;left:8px;right:8px;bottom:10px;display:flex;align-items:baseline;gap:4px"><span class="A" {A(125,26,"opacity:.55")}>77</span><span class="S" style="font-size:22px">→</span><span class="A" {A(125,52,"color:var(--bleu)")}>78</span></div></div>''',
# 8 Top 5 blanc
f'''<div class="t" style="background:var(--blanc)">{mini('#0E0E10','Le top 5')}<div style="position:absolute;left:8px;right:8px;top:18px;bottom:8px;display:grid;align-content:space-between">{''.join(f'<div style="display:flex;gap:6px;align-items:baseline;border-bottom:1px solid #0E0E1022"><span class="A" {A(125,16)} style="color:var(--bleu)">{n}</span><span class="A" {A(62,11)}>{t}</span></div>' for n,t in [(5,'La talonnade'),(4,'Le petit pont'),(3,"L'arrêt réflexe"),(2,'La reprise'),(1,'La lucarne')])}</div></div>''',
# 9 POV citron
f'''<div class="t" style="background:var(--ppeche)">{mini('#0E0E10','POV')}<div style="position:absolute;left:8px;right:8px;top:24%"><div class="M" style="font-size:6px">POV :</div><div class="A" {A(62,24,"line-height:.9")}>T'es venu seul et t'es 7e de la ligue.</div></div></div>''',
# 10 phrase bleu ciel
f'''<div class="t" style="background:var(--papier)">{mini('#0E0E10','SFL')}<div style="position:absolute;left:8px;right:8px;top:34%"><div class="S" style="font-size:22px;line-height:1">Ici, tout le monde commence</div><div class="A" {A(125,22,"color:var(--bleu)")}>inconnu.</div></div></div>''',
# 11 photo crampons papier
f'''<div class="t" style="background:var(--papier)"><div class="ph" style="left:8px;right:8px;top:8px;bottom:30%;background-image:url({cov('crampons-3')})"></div>
<div style="position:absolute;left:8px;bottom:8px;right:8px;display:flex;justify-content:space-between;align-items:end"><span class="S" style="font-size:13px">Dimanche, 12 h 30.</span><span class="M" style="font-size:4.6px;color:var(--gris)">J5</span></div></div>''',
# 12 Verdict or
f'''<div class="t" style="background:var(--por)">{mini('#0E0E10','30.11.26')}<div style="position:absolute;left:8px;right:8px;top:22%"><div class="S" style="font-size:13px">Jour de</div><div class="A" {A(125,27)}>Verdict</div><div class="M" style="font-size:5px;margin-top:6px">Les cartes changent lundi</div></div></div>''',
]
grid=''.join(tiles)
pal=[('--blanc','Blanc','le fond'),('--papier','Papier','le 2e fond'),('--encre','Encre','le texte'),('--bleu','Bleu SFL','un mot, un chiffre'),('--pciel','Ciel','le terrain, la course'),('--ppeche','Pêche','le recrutement, le brut'),('--por','Or doux','la Pépite, le Verdict')]
pals=''.join(f'<div style="display:grid;gap:4px"><div style="height:46px;background:var({v});outline:1px solid #0E0E1018"></div><b style="font:700 10.5px Inter">{n}</b><span style="font-size:9.5px;color:var(--gris);line-height:1.2">{d}</span></div>' for v,n,d in pal)
html=f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body><div class="w">
<div><div class="k">SFL · Identité réseaux <span style="color:var(--bleu)">v4</span> · pastel, blanc, Archivo + italique</div>
<div class="A" {A(125,44,"margin-top:8px")}>Le fil</div><div style="display:flex;align-items:baseline;gap:10px"><span class="S" style="font-size:44px;line-height:.9">du dimanche,</span><span class="A" {A(62,44,"color:var(--bleu)")}>en pastel</span></div>
<p style="color:#55554f;margin-top:8px;max-width:62ch">Deux pastels et un or doux, à plat. Le blanc fait respirer la grille, le texte reste en encre, le bleu SFL ne sert qu'à souligner un mot ou un chiffre. Les photos restent en noir et blanc.</p></div>
<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:6px">{pals}</div>
<div style="background:var(--blanc);border:1px solid #0E0E1018;padding:12px 10px 10px">
<div style="display:flex;gap:12px;align-items:center;margin-bottom:10px"><div style="width:54px;height:54px;border-radius:50%;background:var(--pciel);display:grid;place-items:center;flex:none">{svg('#0E0E10','12px')}</div>
<div><b style="font:700 13px Inter">sundayfiveleague</b><div style="font-size:11px">SFL · Foot à 5 Lille</div><div style="font-size:10.5px;color:#55554f">Ligue de foot à 5 du dimanche · Lille · Marcq<br>Pas d'équipe : viens seul. Une Pépite d'Or.</div></div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2px">{grid}</div></div>
<div style="display:flex;justify-content:space-between" class="k"><span>Sunday Five League · grille Instagram, maquette</span><span>Photos : banque de l'app, à remplacer</span></div>
</div></body></html>'''
open('feed.html','w').write(html)
