# Kit réseaux SFL v4 (pastel) : chaque fichier est dessiné sur une petite page logique puis agrandi à la taille exacte.
import base64,re,json,pathlib
P='/home/user/SFL/public/'
sig=re.sub(r'<!--.*?-->','',open(P+'bola/sfl.svg').read(),flags=re.S)
def svg(col,h): return sig.replace('#08090B',col).replace('<svg ',f'<svg style="height:{h};width:auto;display:block" ',1)
def b64(p): return 'data:image/webp;base64,'+base64.b64encode(open(p,'rb').read()).decode()
cov=lambda n: b64(P+f'actus/couvertures/{n}-1200.webp')
sou=b64('/home/user/bola-site/public/ligue/souley.webp')
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500;700&family=Inter:wght@400;600;700&display=block">'
CSS='''
:root{--blanc:#FFFFFF;--papier:#F2F0E9;--encre:#0E0E10;--bleu:#2563FF;--ciel:#CFE0FF;--peche:#FFD8C4;--or:#F2DC9B;--gris:#8A8A86}
*{box-sizing:border-box;margin:0}html,body{background:transparent}
.A{font-family:Archivo;font-weight:900;text-transform:uppercase;line-height:.84}
.S{font-family:"Instrument Serif";font-style:italic;font-weight:400}
.M{font-family:"JetBrains Mono";font-weight:700;text-transform:uppercase;letter-spacing:.12em}
.t{position:relative;overflow:hidden;color:var(--encre)}
.ph{position:absolute;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.1)}
.mini{position:absolute;left:7px;right:7px;top:7px;display:flex;justify-content:space-between;align-items:center;font:700 4.6px "JetBrains Mono";letter-spacing:.12em;text-transform:uppercase}
'''
def mini(r,col='#0E0E10'): return f'<div class="mini" style="color:{col}"><span>{svg(col,"5px")}</span><span>{r}</span></div>'
def A(wd,sz,extra=''): return f'style="font-stretch:{wd}%;font-size:{sz}px;{extra}"'
JOBS=[]
def job(path,w,h,scale,inner,bg):
    html=f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{width:{w}px;height:{h}px}}</style></head><body><div class="t" style="width:{w}px;height:{h}px;background:{bg}">{inner}</div></body></html>'
    f=pathlib.Path('html')/(path.replace('/','__')+'.html'); f.parent.mkdir(exist_ok=True); f.write_text(html)
    JOBS.append({'html':str(f.resolve()),'out':path,'w':w,'h':h,'scale':scale})
W45,H45,S45=180,225,6      # 1080 x 1350
W916,H916,S916=180,320,6   # 1080 x 1920

# ---------- PROFIL
for name,bg,col in [('profil/sfl-profil-ciel','var(--ciel)','#0E0E10'),('profil/sfl-profil-blanc','var(--blanc)','#0E0E10'),('profil/sfl-profil-encre','var(--encre)','#FFFFFF')]:
    job(name,180,180,6,f'<div style="position:absolute;inset:0;display:grid;place-items:center">{svg(col,"34px")}</div>',bg)

# ---------- POSTS 4:5
D={'j':'J4','date':'08.11.26'}
job('posts/la-course',W45,H45,S45,f'''{mini('S1 · '+D['j'])}<div style="position:absolute;left:9px;top:18px"><div class="A" {A(125,27)}>La<br>Course</div><div class="S" style="font-size:13px;color:var(--bleu)">vers la Pépite d'Or</div></div>
<div style="position:absolute;left:9px;right:9px;bottom:9px;display:grid;gap:2px">{''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid #0E0E1022;padding-top:2px"><span class="A" {A(62,13.5)}>{i} {n}</span><span class="M" style="font-size:5px;color:{c}">{p} pts {a}</span></div>' for i,n,p,a,c in [(1,'Souley',412,'▲2','#2563FF'),(2,'Jouneiid',398,'▼1','#8A8A86'),(3,"Coucoupop's",377,'▲4','#2563FF'),(4,'Ilyes',361,'—','#8A8A86'),(5,'Abdel',355,'▲1','#2563FF')])}</div>''','var(--blanc)')
job('posts/le-but',W45,H45,S45,f'''{mini(D['j']+' · 14:23')}<div class="ph" style="left:9px;right:9px;top:18px;height:50%;background-image:url({cov('cage-1')})"></div>
<div style="position:absolute;left:9px;bottom:9px"><div class="S" style="font-size:14px">et soudain,</div><div class="A" {A(125,36)}>But.</div><div class="M" style="font-size:4.8px;margin-top:3px">Jouneiid · Match 2 · Terrain 1</div></div>''','var(--ciel)')
job('posts/portrait',W45,H45,S45,f'''{mini('Portrait')}<div class="ph" style="right:9px;top:18px;width:52%;bottom:9px;background-image:url({cov('silhouette-1')})"></div>
<div style="position:absolute;left:9px;top:22px;width:36%"><div class="S" style="font-size:12px;line-height:1.05">« Je suis venu seul. Maintenant je connais tout le monde. »</div></div>
<div style="position:absolute;left:9px;bottom:9px"><div class="A" {A(62,19)}>Ayman</div><div class="M" style="font-size:4.8px;color:var(--gris)">3 dimanches · D2</div></div>''','var(--blanc)')
job('posts/il-manque-1',W45,H45,S45,f'''{mini('Dimanche 12 h 30')}<div style="position:absolute;left:9px;right:9px;top:30%"><div class="A" {A(125,27)}>Il manque</div><div class="A" {A(125,96,"line-height:.8")}>1.</div></div>
<div style="position:absolute;left:9px;bottom:9px" class="M"><span style="font-size:5.2px">Viens seul · getbola.app</span></div>''','var(--peche)')
job('posts/mvp',W45,H45,S45,f'''{mini('Les cartes · '+D['j'])}<div style="position:absolute;left:9px;top:18px"><div class="A" {A(125,32)}>MVP</div><div class="S" style="font-size:13px">le patron du terrain 1</div></div>
<img src="{sou}" style="position:absolute;right:10px;bottom:-6%;width:46%;transform:rotate(5deg)"><div style="position:absolute;left:9px;bottom:9px"><div class="A" {A(62,21)}>Souley</div><div class="M" style="font-size:4.8px">7 buts · 3 passes</div></div>''','var(--papier)')
job('posts/ta-note',W45,H45,S45,f'''{mini('Ta note')}<div style="position:absolute;left:9px;top:20px" class="A" {A(62,20)}>Sebovic<br>monte.</div>
<div style="position:absolute;left:9px;right:9px;bottom:11px;display:flex;align-items:baseline;gap:4px"><span class="A" {A(125,27,"opacity:.55")}>77</span><span class="S" style="font-size:24px">→</span><span class="A" {A(125,56,"color:var(--bleu)")}>78</span></div>''','var(--ciel)')
job('posts/top-5',W45,H45,S45,f'''{mini('Le top 5 · '+D['j'])}<div style="position:absolute;left:9px;right:9px;top:20px;bottom:9px;display:grid;align-content:space-between">{''.join(f'<div style="display:flex;gap:6px;align-items:baseline;border-bottom:1px solid #0E0E1022"><span class="A" {A(125,17)} style="color:var(--bleu)">{n}</span><span class="A" {A(62,12)}>{t}</span></div>' for n,t in [(5,'La talonnade'),(4,'Le petit pont'),(3,"L'arrêt réflexe"),(2,'La reprise'),(1,'La lucarne')])}</div>''','var(--blanc)')
job('posts/pov',W45,H45,S45,f'''{mini('POV')}<div style="position:absolute;left:9px;right:9px;top:24%"><div class="M" style="font-size:6.5px">POV :</div><div class="A" {A(62,25,"line-height:.9")}>T'es venu seul et t'es 7e de la ligue.</div></div>''','var(--peche)')
job('posts/citation',W45,H45,S45,f'''{mini('SFL')}<div style="position:absolute;left:9px;right:9px;top:34%"><div class="S" style="font-size:23px;line-height:1">Ici, tout le monde commence</div><div class="A" {A(125,23,"color:var(--bleu)")}>inconnu.</div></div>''','var(--papier)')
job('posts/verdict',W45,H45,S45,f'''{mini('30.11.26')}<div style="position:absolute;left:9px;right:9px;top:22%"><div class="S" style="font-size:14px">Jour de</div><div class="A" {A(125,23)}>Verdict</div><div class="M" style="font-size:5.2px;margin-top:6px">Les cartes changent lundi</div></div>''','var(--or)')

# ---------- REELS / TIKTOK 9:16 (zone sûre : rien d'important dans le bas 20 % ni la droite 15 %)
job('reels/le-but',W916,H916,S916,f'''{mini(D['j']+' · 14:23')}<div class="ph" style="left:0;right:0;top:0;height:58%;background-image:url({cov('cage-1')})"></div>
<div style="position:absolute;left:12px;right:30px;top:61%"><div class="S" style="font-size:22px">et soudain,</div><div class="A" {A(125,52)}>But.</div><div class="M" style="font-size:6px;margin-top:5px">Jouneiid · Terrain 1</div></div>''','var(--ciel)')
job('reels/pov',W916,H916,S916,f'''{mini('POV')}<div style="position:absolute;left:12px;right:30px;top:22%"><div class="M" style="font-size:8px">POV :</div><div class="A" {A(62,40,"line-height:.9")}>T'es venu seul et t'es 7e de la ligue.</div></div>''','var(--peche)')
job('reels/il-manque-1',W916,H916,S916,f'''{mini('Dimanche 12 h 30')}<div style="position:absolute;left:12px;right:20px;top:24%"><div class="A" {A(125,27)}>Il manque</div><div class="A" {A(125,150,"line-height:.8")}>1.</div><div class="M" style="font-size:7px;margin-top:10px">Viens seul · getbola.app</div></div>''','var(--peche)')
job('reels/ta-note',W916,H916,S916,f'''{mini('Ta note · Verdict')}<div style="position:absolute;left:12px;top:24px" class="A" {A(62,34)}>Sebovic<br>monte.</div>
<img src="{b64('/home/user/bola-site/public/ligue/sebovic.webp')}" style="position:absolute;left:50%;top:21%;width:42%;transform:translateX(-50%) rotate(-3deg)">
<div style="position:absolute;left:12px;top:64%;display:flex;align-items:baseline;gap:6px"><span class="A" {A(100,30,"opacity:.55")}>77</span><span class="S" style="font-size:26px">→</span><span class="A" {A(100,48,"color:var(--bleu)")}>78</span></div>''','var(--ciel)')

# ---------- YOUTUBE miniature 1280x720
job('youtube/miniature-resume',160,90,8,f'''<div class="ph" style="left:0;top:0;bottom:0;width:56%;background-image:url({cov('silhouette-1')})"></div>
<div style="position:absolute;left:5px;top:5px">{svg('#fff','4px')}</div>
<div style="position:absolute;right:7px;top:6px;bottom:6px;width:36%;display:flex;flex-direction:column;justify-content:space-between;align-items:flex-end;text-align:right">
<div class="M" style="font-size:3px">Le résumé · S1</div><div class="A" {A(110,34,"line-height:.8")}>J4</div><div><div class="S" style="font-size:8px;line-height:1">personne</div><div class="A" {A(75,8)}>ne lâche.</div></div></div>''','var(--ciel)')

# ---------- BANNIÈRES
# YouTube 2560x1440, zone sûre 1546x423 au centre
job('bannieres/youtube-2560x1440',256,144,10,f'''<div style="position:absolute;left:50%;top:50%;width:154.6px;height:42.3px;transform:translate(-50%,-50%);display:flex;align-items:center;justify-content:space-between">
<div>{svg('#0E0E10','11px')}</div><div style="text-align:right"><div class="S" style="font-size:9px;line-height:1">le dimanche</div><div class="A" {A(125,13)}>décide.</div><div class="M" style="font-size:2.6px;margin-top:2px">Foot à 5 · Lille · Marcq · chaque dimanche</div></div></div>
<div class="ph" style="left:0;top:0;bottom:0;width:16%;background-image:url({cov('cage-2')})"></div><div class="ph" style="right:0;top:0;bottom:0;width:16%;background-image:url({cov('ombres-1')})"></div>''','var(--ciel)')
# Twitch bannière 1200x480
job('bannieres/twitch-1200x480',240,96,5,f'''<div style="position:absolute;left:14px;top:50%;transform:translateY(-50%)"><div class="S" style="font-size:13px;line-height:1">en direct, le dimanche</div><div class="A" {A(62,17)}>Sunday Five League</div><div class="M" style="font-size:4px;margin-top:4px">12 h 30 · Hippodrome de Marcq</div></div>
<div class="ph" style="right:0;top:0;bottom:0;width:30%;background-image:url({cov('cage-1')})"></div>''','var(--ciel)')
# Twitch écran hors ligne 1920x1080
job('bannieres/twitch-hors-ligne-1920x1080',192,108,10,f'''<div style="position:absolute;inset:0;display:grid;place-items:center;text-align:center"><div><div style="display:flex;justify-content:center;margin-bottom:6px">{svg('#0E0E10','9px')}</div>
<div class="S" style="font-size:11px">on revient</div><div class="A" {A(125,19)}>dimanche.</div><div class="M" style="font-size:3px;margin-top:4px">12 h 30 · Twitch et YouTube · getbola.app</div></div></div>''','var(--papier)')
json.dump(JOBS,open('jobs.json','w'))
print(len(JOBS))
