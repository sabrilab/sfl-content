import sys,base64,glob; sys.path.insert(0,'.')
from tex import *
K='/home/user/sfl-content/reseaux/kit-v2/'
def im(p,m='image/png'): return f'data:{m};base64,'+base64.b64encode(open(p,'rb').read()).decode()
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500;700&family=Inter:wght@400;600;700&display=block">'
CSS='''@page{size:297mm 210mm;margin:0}*{box-sizing:border-box;margin:0}body{font:12px/1.45 Inter,sans-serif;color:#0B0B0B}
.pg{position:relative;width:1123px;height:794px;overflow:hidden;page-break-after:always;background:#fff;padding:48px 56px}
.tx{position:absolute;inset:0;width:100%;height:100%;display:block}
.A{font-family:Archivo;font-weight:900;text-transform:uppercase;line-height:.86}.S{font-family:"Instrument Serif";font-style:italic;line-height:1}
.M{font:700 10px "JetBrains Mono";letter-spacing:.16em;text-transform:uppercase}
.hd{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1.5px solid #0B0B0B;padding-bottom:10px;margin-bottom:24px}
.n{font:700 10px "JetBrains Mono";letter-spacing:.16em;color:#8A8A86}
.p{color:#4a4640;font-size:12.5px;max-width:60ch}.box{position:relative;overflow:hidden}
.ft{position:absolute;left:56px;right:56px;bottom:26px;display:flex;justify-content:space-between;font:700 8.5px "JetBrains Mono";letter-spacing:.16em;text-transform:uppercase;color:#8A8A86}
'''
def A(wd,sz,extra=''): return f'style="font-stretch:{wd}%;font-size:{sz}px;{extra}"'
def hd(n,t,s): return f'<div class="hd"><div><span class="n">{n}</span><div class="A" {A(125,34)}>{t}</div></div><div class="S" style="font-size:22px;color:#5C1F2A">{s}</div></div>'
FT='<div class="ft"><span>SFL · Sunday Five League · Charte graphique réseaux</span><span>v2 · novembre 2026</span></div>'
def plq(txt,kind,w,h,size,sub=None,stretch=110):
    sb=('<div style="margin-top:3px">'+grave(sub,kind,size*.38,100,400,'Instrument Serif',True)+'</div>') if sub else ''
    return f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:4px;overflow:hidden;box-shadow:0 4px 10px rgba(0,0,0,.55)">{metal(kind,w,h)}<div style="position:absolute;inset:0;display:grid;place-items:center;text-align:center"><div>{grave(txt,kind,size,stretch)}{sb}</div></div></div>'
def rgb(h): h=h.lstrip('#'); return ', '.join(str(int(h[i:i+2],16)) for i in (0,2,4))
P=[]
# 1 COUVERTURE
P.append(f'''<div class="pg" style="padding:0">{cuir('#151313',1123,794,3)}{couture('#C9A03A',22,6)}
<div style="position:absolute;left:0;right:0;top:230px;display:flex;justify-content:center">{plq('SFL','or',420,170,104,None,125)}</div>
<div style="position:absolute;left:0;right:0;top:450px;text-align:center;color:#fff"><div class="S" style="font-size:34px;color:#D8B04A">Charte graphique</div><div class="A" {A(125,40,"margin-top:6px")}>Réseaux sociaux</div>
<div class="M" style="margin-top:18px;color:#EEE6D3">Sunday Five League · Saison 1 · v2 · novembre 2026</div></div></div>''')
# 2 LOGO
P.append(f'''<div class="pg">{hd('01','Le logo','gravé, brodé, ou simple')}
<div style="display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:18px">
<div><div class="box" style="height:300px;border-radius:4px">{cuir('#151313',420,300,3)}<div style="position:absolute;inset:0;display:grid;place-items:center">{plq('SFL','or',230,92,56,None,125)}</div></div>
<div class="A" {A(62,18,"margin-top:10px")}>Principal : la plaque gravée</div><p class="p">Or gravé sur cuir noir. Photo de profil sur les quatre réseaux, couverture, grands moments.</p></div>
<div><div class="box" style="height:140px;border-radius:4px">{cuir('#5C1F2A',300,140,3)}<div style="position:absolute;inset:0;display:grid;place-items:center">{brode('#D8B04A','46px')}</div></div><div class="M" style="margin:6px 0 12px">Brodé or · cuir bordeaux</div>
<div class="box" style="height:140px;border-radius:4px">{tissu('#1F3B2E',300,140)}<div style="position:absolute;inset:0;display:grid;place-items:center">{brode('#EEE6D3','46px')}</div></div><div class="M" style="margin-top:6px">Brodé craie · maillot vert bouteille</div></div>
<div><div class="box" style="height:140px;border-radius:4px;background:#fff;outline:1px solid #0B0B0B22;display:grid;place-items:center"><svg viewBox="0 0 735 237" style="height:44px"><path d="{D}" fill="#0B0B0B"/></svg></div><div class="M" style="margin:6px 0 12px">Simple noir · sur blanc</div>
<div class="box" style="height:140px;border-radius:4px;background:#0B0B0B;display:grid;place-items:center"><svg viewBox="0 0 735 237" style="height:44px"><path d="{D}" fill="#fff"/></svg></div><div class="M" style="margin-top:6px">Simple blanc · sur noir</div></div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:22px">
<div><div class="A" {A(62,15)}>Zone de protection</div><p class="p">Autour du sigle, laisser un vide égal à la hauteur du F.</p></div>
<div><div class="A" {A(62,15)}>Taille minimale</div><p class="p">Sigle simple : 24 px de haut. Plaque et broderie : 60 px de haut, sinon on ne lit plus la matière.</p></div>
<div><div class="A" {A(62,15)}>Interdit</div><p class="p">Déformer, recolorer hors palette, ajouter une ombre portée sur le sigle simple, le poser sur une photo chargée.</p></div></div>{FT}</div>''')
# 3 COULEURS
groups=[('Les fonds','60 %',[('Noir','#0B0B0B','Fond des grands moments, texte'),('Blanc','#FFFFFF','Fond du quotidien, respiration'),('Craie','#EEE6D3','Papier, lignes, texte sur couleur')]),
('Le terrain','30 %',[('Bordeaux','#5C1F2A','Cuir, Pépite, Verdict'),('Vert bouteille','#1F3B2E','Maillot, écarts'),('Émeraude','#1D5B47','Montée, révélation'),('Olive','#64633A','Ta course, story'),('Terre','#9B5B3A','Recrutement'),('Pelouse','#4E7140','Cartes, hors ligne')]),
('La récompense','10 %',[('Or','#C9A03A','MVP, Pépite, 1er. Rare.'),('Fil or','#D8B04A','Broderies, accents serif')]),
('Les pastels','5 %',[('Rose poudré','#EDCFD4','Encart, citation'),('Sauge','#D2E4DB','Classement, liste'),('Pêche','#F2D8C9','Story « ta course »')])]
cols=''
for t,pct,cs in groups:
    cols+=f'<div><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px"><div class="A" {A(62,17)}>{t}</div><span class="M" style="color:#5C1F2A">{pct}</span></div>'
    cols+=''.join(f'<div style="display:grid;grid-template-columns:62px 1fr;gap:10px;align-items:center;margin-bottom:8px"><div style="height:44px;border-radius:3px;background:{c};outline:1px solid #0B0B0B22"></div><div><b style="font:700 12.5px Inter">{n}</b> <span class="M" style="font-size:8.5px;color:#8A8A86">{c} · RVB {rgb(c)}</span><div style="font-size:11px;color:#4a4640">{u}</div></div></div>' for n,c,u in cs)+'</div>'
bar=''.join(f'<div style="flex:{f};background:{c}"></div>' for f,c in [(25,'#0B0B0B'),(25,'#FFFFFF'),(10,'#EEE6D3'),(7,'#5C1F2A'),(6,'#1F3B2E'),(3,'#1D5B47'),(3,'#64633A'),(3,'#9B5B3A'),(3,'#4E7140'),(10,'#C9A03A'),(2,'#EDCFD4'),(2,'#D2E4DB'),(1,'#F2D8C9')])
P.append(f'''<div class="pg">{hd('02','Les couleurs','harmonisées, avec une touche de pastel')}
<div style="display:grid;grid-template-columns:1fr 1.2fr .95fr .95fr;gap:24px">{cols}</div>
<div class="M" style="margin:16px 0 6px">Proportions dans le fil</div><div style="display:flex;height:26px;outline:1px solid #0B0B0B22">{bar}</div>
<p class="p" style="margin-top:12px">Harmonisées : les couleurs du terrain sont toutes sombres et un peu éteintes, de la même intensité. Les trois pastels sont leurs versions claires (rose du bordeaux, sauge du vert, pêche de la terre) : une touche par semaine, jamais deux dans le même visuel. Toujours à plat, jamais en dégradé (sauf la lumière d'un métal). L'or se gagne.</p>{FT}</div>''')
# 4 MÉTAUX & PIERRES
mets=''.join(f'<div><div style="display:flex;justify-content:center">{plq(t,k,220,84,34)}</div><div class="A" {A(62,16,"margin-top:12px")}>{t}</div><p class="p">{u}</p></div>' for k,t,u in [('or','Or','1er, MVP, Pépite d\'Or, Verdict.'),('argent','Argent','2e place, médaille.'),('bronze','Bronze','3e place, médaille.'),('noir','Noir','Plaque du quotidien : noms, séries.')])
stones=''.join(f'<div style="display:grid;grid-template-columns:44px 1fr;gap:10px;align-items:center">{pierre(k,40)}<div><b style="font:700 13px Inter">{n}</b><div style="font-size:11px;color:#4a4640">{u}</div></div></div>' for k,n,u in [('rubis','Rubis','Titre Impact'),('saphir','Saphir','Titre Défensive'),('emeraude','Émeraude','Révélation, plus grosse montée'),('diamant','Diamant','La Pépite d\'Or, le MVP')])
P.append(f'''<div class="pg">{hd('03','Métaux et pierres','gravé, avec parcimonie')}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:22px">{mets}</div>
<div class="A" {A(62,17,"margin:28px 0 10px")}>Les pierres</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:22px">{stones}</div>
<p class="p" style="margin-top:20px"><b>Règles.</b> Les noms et les titres se gravent : creux sombre, lèvre claire en dessous. Une seule pierre par visuel, et seulement quand un titre est gagné. Jamais de pierre pour décorer.</p>{FT}</div>''')
# 5 TYPO
P.append(f'''<div class="pg">{hd('04','La typographie','trois voix')}
<div style="display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:28px">
<div><div class="M" style="color:#5C1F2A">Titres · Archivo 900</div><div class="A" {A(125,64,"margin-top:8px")}>La course</div><div class="A" {A(62,64)}>Souley 82</div>
<p class="p" style="margin-top:10px">Une seule police qu'on étire : large (125 %) pour les titres et les chiffres, serrée (62 %) pour les noms et les listes. Toujours en capitales.</p></div>
<div><div class="M" style="color:#5C1F2A">Accent · Instrument Serif italique</div><div class="S" style="font-size:52px;margin-top:8px">et soudain,</div><div class="S" style="font-size:52px;color:#5C1F2A">à la Pépite d'Or</div>
<p class="p" style="margin-top:10px">Le mot qui donne l'émotion, juste avant ou après le titre. En minuscules. Une ligne, pas plus.</p></div>
<div><div class="M" style="color:#5C1F2A">Faits · JetBrains Mono 700</div><div class="M" style="font-size:16px;margin-top:12px;line-height:1.7">J4 · 08.11.26<br>Match 2 · Terrain 1<br>412 pts · 4 J</div>
<p class="p" style="margin-top:10px">Les faits : date, match, terrain, minute, points. Petit, en capitales, espacé.</p></div></div>
<div class="A" {A(62,17,"margin:26px 0 8px")}>Échelle sur un post 1080 × 1350</div>
<table style="border-collapse:collapse;width:100%;font-size:12px">{''.join(f'<tr style="border-top:1px solid #0B0B0B22"><td style="padding:6px 0;width:22%"><b>{a}</b></td><td style="width:30%">{b}</td><td style="width:16%" class="M">{c}</td><td style="color:#4a4640">{d}</td></tr>' for a,b,c,d in [('Titre','Archivo 900 · large 125 %','160–220 px','Un à trois mots'),('Nom, liste','Archivo 900 · serré 62 %','80–130 px','Prénoms, classements'),('Accent','Instrument Serif italique','80–100 px','Une ligne'),('Faits','JetBrains Mono 700','28–32 px','Espacement +14 %'),('Chiffre héros','Archivo 900 · 110–125 %','300–600 px','Note, score, J4')])}</table>
<p class="p" style="margin-top:12px">Les trois polices sont gratuites (Google Fonts) : Archivo, Instrument Serif, JetBrains Mono.</p>{FT}</div>''')
# 6 MATIÈRES
mt=[(cuir('#151313',230,170,3),'Cuir noir','Grands moments, MVP, profil'),(cuir('#5C1F2A',230,170,5),'Cuir bordeaux','Podium, Verdict, YouTube'),(tissu('#1F3B2E',230,170),'Maillot vert bouteille','Écarts, Twitch'),(tissu('#64633A',230,170),'Maillot olive','Ta course'),(pelouse(230,170,5),'Pelouse','MVP, cartes, hors ligne'),(terre(230,170),'Terre battue','Recrutement « Il manque 1. »'),(papier(230,170),'Papier craie','Classement, photo encadrée'),('<div class="tx" style="background:#fff;outline:1px solid #0B0B0B22"></div>','Blanc','Classement gravé, quotidien')]
P.append(f'''<div class="pg">{hd('05','Les matières','dessinées en code, sans IA')}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">{''.join(f'<div><div class="box" style="height:150px;border-radius:4px">{t}</div><div class="A" {A(62,15,"margin-top:8px")}>{n}</div><div style="font-size:11px;color:#4a4640">{u}</div></div>' for t,n,u in mt)}</div>
<p class="p" style="margin-top:16px">Une matière par visuel. Les coutures (pointillé fil or ou craie) cadrent les grands moments. Les matières sont générées par le code du kit (<span class="M" style="font-size:9px">kit-v2/tex.py</span>) : elles se refont à n'importe quelle taille.</p>{FT}</div>''')
# 7 COMPOSITION
P.append(f'''<div class="pg">{hd('06','Composition','les repères fixes')}
<div style="display:grid;grid-template-columns:300px 190px 1fr;gap:30px;align-items:start">
<div><div class="box" style="width:300px;height:375px;outline:1px solid #0B0B0B33;background:#fff">
<div style="position:absolute;inset:15px;border:1px dashed #5C1F2A"></div><div style="position:absolute;left:15px;right:15px;top:15px;height:22px;background:#5C1F2A18;display:flex;justify-content:space-between;align-items:center;padding:0 6px"><span class="M" style="font-size:7px">Sigle</span><span class="M" style="font-size:7px">J4 · date</span></div>
<div style="position:absolute;left:15px;right:15px;top:60px;height:80px;background:#0B0B0B10;display:grid;place-items:center" class="M">Titre + accent</div>
<div style="position:absolute;left:15px;right:15px;bottom:15px;height:120px;background:#0B0B0B08;display:grid;place-items:center" class="M">Sujet : carte, photo, liste</div></div>
<div class="M" style="margin-top:6px">Post 1080 × 1350 · marges 54 px</div></div>
<div><div class="box" style="width:190px;height:338px;outline:1px solid #0B0B0B33;background:#fff"><div style="position:absolute;left:0;right:0;top:0;height:13%;background:#9B5B3A22"></div><div style="position:absolute;left:0;right:0;bottom:0;height:20%;background:#9B5B3A22"></div><div style="position:absolute;right:0;top:13%;bottom:20%;width:15%;background:#9B5B3A22"></div>
<div style="position:absolute;left:12px;right:34px;top:20%;bottom:24%;border:1px dashed #5C1F2A;display:grid;place-items:center" class="M">Zone sûre</div></div><div class="M" style="margin-top:6px">Reel, TikTok 1080 × 1920</div></div>
<div><div class="A" {A(62,17)}>Les repères</div><ul style="margin:8px 0 0 16px;font-size:12.5px;line-height:1.7;color:#2a2622">
<li><b>En haut</b> : le sigle (brodé ou simple) à gauche, la journée et la date en machine à droite.</li>
<li><b>Le titre</b> en Archivo, l'accent en italique juste au-dessus ou en dessous.</li>
<li><b>Le sujet</b> en bas : la carte BOLA, la photo, la liste, le trophée.</li>
<li><b>Les rangs</b> : médailles gravées or, argent, bronze.</li>
<li><b>Les grands moments</b> : cuir noir ou bordeaux, coutures fil or, plaque gravée.</li>
<li><b>En vertical</b> : rien d'important dans le bas 20 %, ni sur la droite 15 % (boutons de l'appli).</li></ul></div></div>{FT}</div>''')
# 8 PHOTO
ph=''.join(f'<div class="box" style="height:250px;border-radius:3px;background:url({im("/home/user/visuels/photos-magnific/"+f+".jpg","image/jpeg")}) center/cover"></div>' for f in ['02-terrain','03-detail','04-maillot','06-lieu'])
P.append(f'''<div class="pg">{hd('07','La photo','la touche du photographe')}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px">{ph}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px 28px;margin-top:20px">{''.join(f'<div style="border-top:1px solid #0B0B0B22;padding-top:6px"><div class="A" {A(62,15,"color:#5C1F2A")}>{a}</div><div style="font-size:12px">{b}</div></div>' for a,b in [('Lumière','Ciel bleu, midi ou fin d\'après-midi. Jamais la nuit.'),('Optique','35 ou 50 mm. Contre-plongée ou hauteur d\'homme.'),('Couleur','Chaude, douce, façon pellicule. Un grain léger.'),('Décor','Brique, immeubles, grillage, tribune : le vrai lieu.'),('Joueurs','En maillot SFL, seulement s\'ils ont signé la charte.'),('Interdit','Fond studio, visages floutés, filtres.')])}</div>
<p class="p" style="margin-top:12px">Les photos ci-dessus sont des images d'ambiance provisoires (Magnific). Elles seront remplacées par les vraies photos des dimanches.</p>{FT}</div>''')
# 9 FORMATS & EXEMPLES
ex=['posts/06-mvp','posts/01-podium','posts/10-trophees-saison','posts/04-le-but','posts/02-classement']
exs=''.join(f'<img src="{im(K+e+".png")}" style="width:100%;display:block;outline:1px solid #0B0B0B22">' for e in ex)
P.append(f'''<div class="pg">{hd('08','Formats et exemples','le kit, prêt à remplir')}
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px">{exs}</div>
<table style="border-collapse:collapse;width:100%;font-size:12px;margin-top:18px">{''.join(f'<tr style="border-top:1px solid #0B0B0B22"><td style="padding:5px 0;width:26%"><b>{a}</b></td><td class="M" style="width:22%">{b}</td><td style="color:#4a4640">{c}</td></tr>' for a,b,c in [('Photo de profil','1080 × 1080','Plaque or gravée « SFL » sur cuir noir, partout'),('Post Instagram','1080 × 1350','Podium, classement, MVP, verdict, trophées, but'),('Reel, TikTok, Short, story','1080 × 1920','Le but, il te manque, il manque 1, Pépite d\'Or'),('Miniature YouTube','1280 × 720','Photo + cuir bordeaux, un chiffre, trois mots'),('Bannière YouTube','2560 × 1440','Texte dans la zone sûre centrale 1546 × 423'),('Bannière Twitch · hors ligne','1200 × 480 · 1920 × 1080','Maillot vert · pelouse « on revient dimanche »')])}</table>{FT}</div>''')
# 10 DO / DON'T
P.append(f'''<div class="pg">{hd('09','À faire, à éviter','en un coup d\'œil')}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:36px">
<div><div class="A" {A(62,20,"color:#1D5B47")}>À faire</div><ul style="margin:10px 0 0 16px;font-size:13.5px;line-height:1.8">
<li>Un titre, un accent, un sujet.</li><li>Les fonds à plat : noir, blanc, craie, ou une matière.</li><li>L'or seulement quand c'est gagné.</li><li>Les noms gravés, les rangs en médailles.</li><li>Les vrais trophées BOLA pour la saison.</li><li>Les vraies photos du dimanche.</li><li>Seulement les joueurs qui ont signé la charte.</li></ul></div>
<div><div class="A" {A(62,20,"color:#5C1F2A")}>À éviter</div><ul style="margin:10px 0 0 16px;font-size:13.5px;line-height:1.8">
<li>Les dégradés de fond.</li><li>Plus d'une pierre par visuel.</li><li>Plus de deux couleurs du terrain dans un même visuel.</li><li>Plus d'un pastel par visuel.</li><li>Une autre police que les trois de la charte.</li><li>Le sigle déformé ou recoloré.</li><li>Les photos de nuit, de studio, ou filtrées.</li><li>Une marque sponsor en or.</li></ul></div></div>{FT}</div>''')
open('charte.html','w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(P)}</body></html>')
print(len(P))
