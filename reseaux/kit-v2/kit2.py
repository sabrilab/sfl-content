# Kit réseaux SFL V2 : matières en code (cuir, maillot, pelouse, papier), sigle brodé, classements façon BOLA, photos Magnific.
import sys,base64,json,pathlib; sys.path.insert(0,'.')
from tex import *
def b64(p,m='image/webp'): return f'data:{m};base64,'+base64.b64encode(open(p,'rb').read()).decode()
PH={k:b64(f'/home/user/visuels/photos-magnific/{k}.jpg','image/jpeg') for k in ['02-terrain','03-detail','04-maillot','06-lieu']}
L='/home/user/bola-site/public/ligue/'
C={k:b64(L+k+'.webp') for k in ['souley','jouneid','coucoupops','gail','sebovic']}
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500;700&display=block">'
CSS='''*{box-sizing:border-box;margin:0}.tx{position:absolute;inset:0;width:100%;height:100%;display:block}
.A{font-family:Archivo;font-weight:900;text-transform:uppercase;line-height:.84}.S{font-family:"Instrument Serif";font-style:italic;line-height:1}
.ph{position:absolute;background-size:cover;background-position:center}'''
CR='#EEE6D3'; OR='#D8B04A'; EN='#16130F'; BX='#5E1A24'; VB='#1E3B2C'; OL='#6B6A34'; EM='#0F5A43'
def mono(t,col,sz=5): return f'<span style="font:700 {sz}px JetBrains Mono;letter-spacing:.14em;text-transform:uppercase;color:{col}">{t}</span>'
def top(col,r,thread=None): return f'<div style="position:absolute;left:9px;right:9px;top:9px;display:flex;justify-content:space-between;align-items:center;z-index:2">{brode(thread or col,"6.5px",False)}{mono(r,col,4.8)}</div>'
def A(wd,sz,extra=''): return f'style="font-stretch:{wd}%;font-size:{sz}px;{extra}"'
JOBS=[]
T='/home/user/sfl-content/reseaux/kit-v2/trophees/'
TR=lambda n: 'data:image/png;base64,'+base64.b64encode(open(T+n+'.png','rb').read()).decode()
NOIR='#0B0B0B'; BLANC='#FFFFFF'
def plaque(txt,kind,w,h,size,sub=None,stretch=110):
    sb=('<div style="margin-top:2px">'+grave(sub,kind,size*.38,100,400,'Instrument Serif',True)+'</div>') if sub else ''
    return f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:3px;overflow:hidden;box-shadow:0 3px 6px rgba(0,0,0,.55)">{metal(kind,w,h)}<div style="position:absolute;inset:0;display:grid;place-items:center;text-align:center"><div>{grave(txt,kind,size,stretch)}{sb}</div></div></div>'
def medaille(r,kind,s=16): return f'<div style="position:relative;width:{s}px;height:{s}px;border-radius:50%;overflow:hidden">{metal(kind,s,s,s/2)}<div style="position:absolute;inset:0;display:grid;place-items:center">{grave(r,kind,s*.55,110)}</div></div>'

def job(path,w,h,scale,inner):
    html=f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{width:{w}px;height:{h}px}}</style></head><body><div style="position:relative;overflow:hidden;width:{w}px;height:{h}px">{inner}</div></body></html>'
    f=pathlib.Path('html')/(path.replace('/','__')+'.html'); f.parent.mkdir(exist_ok=True); f.write_text(html)
    JOBS.append({'html':str(f.resolve()),'out':path,'w':w,'h':h,'scale':scale})
W,H=180,225; V=320
# PROFIL
job('profil/sfl-profil-cuir',180,180,6,cuir(BX,180,180,3)+f'<div style="position:absolute;inset:0;display:grid;place-items:center">{brode(OR,"40px")}</div>')
job('profil/sfl-profil-plaque',180,180,6,cuir('#151313',180,180,3)+f'<div style="position:absolute;left:30px;top:66px">{plaque("SFL","or",120,48,30,None,125)}</div>')
job('profil/sfl-profil-maillot',180,180,6,tissu(VB,180,180)+f'<div style="position:absolute;inset:0;display:grid;place-items:center">{brode(CR,"40px")}</div>')
# POSTS
MK={1:'or',2:'argent',3:'bronze'}
pod=lambda img,w,rk,n,p,j: f'<div style="display:grid;justify-items:center;gap:2px"><img src="{img}" style="width:{w}px;display:block;filter:drop-shadow(0 3px 4px rgba(0,0,0,.5))">{medaille(str(rk),MK[rk],14 if rk==1 else 11)}<div class="A" style="font-stretch:62%;font-size:{9 if rk==1 else 7}px;color:{CR}">{n}</div>{mono(f"{p} pts · {j} J",OR if rk==1 else CR,4.2)}</div>'
job('posts/01-podium',W,H,6,cuir(BX,W,H,3)+couture(OR,6,4)+top(OR,'S1 · après la J4')+f'''<div style="position:absolute;left:12px;top:24px"><div class="A" {A(125,17,f"color:{CR}")}>La course</div><div class="S" style="font-size:15px;color:{OR}">à la Pépite d'Or</div></div>
<div style="position:absolute;left:8px;right:8px;bottom:14px;display:flex;align-items:flex-end;justify-content:center;gap:6px">{pod(C['jouneid'],40,2,'Jouneiid',398,4)}{pod(C['souley'],62,1,'Souley',412,4)}{pod(C['coucoupops'],40,3,"Coucoupop's",377,3)}</div>''')
rows=[(1,'souley','Souley',412,4,'▲2'),(2,'jouneid','Jouneiid',398,4,'▼1'),(3,'coucoupops',"Coucoupop's",377,3,'▲4'),(4,'gail','Gaïl',361,4,'—'),(5,'sebovic','Sebovic',355,4,'▲1')]
rangcol=['#C9A03A','#A9A9A2','#A65A34','#16130F55','#16130F55']; G='10px 16px 1fr 18px 26px 14px'
lines=''.join(f'''<div style="display:grid;grid-template-columns:{G};gap:4px;align-items:center;padding:3px 0;border-bottom:1px solid #16130F1c"><span class="A" style="font-size:9px;color:{rangcol[i]}">{r}</span><img src="{C[k]}" style="width:14px;display:block"><span class="A" style="font-stretch:62%;font-size:9.5px">{n}</span><span style="font:700 6px Archivo;color:#7a7264;text-align:right">{j} J</span><span class="A" style="font-stretch:110%;font-size:9px;text-align:right">{p}</span>{mono(a,EM if "▲" in a else "#7a7264",4.6)}</div>''' for i,(r,k,n,p,j,a) in enumerate(rows))
job('posts/02-classement',W,H,6,papier(W,H)+top(BX,'Classement · J4')+f'''<div style="position:absolute;left:10px;right:10px;top:24px;color:{EN}"><div class="S" style="font-size:12px;color:{BX}">Classement</div><div class="A" {A(125,19)}>Pépite d'Or</div>
<div style="display:grid;grid-template-columns:{G};gap:4px;margin-top:7px">{''.join(f'<span style="font:700 4.2px JetBrains Mono;letter-spacing:.12em;color:#7a7264;text-align:{al}">{t}</span>' for t,al in [('#','left'),('','left'),('Joueur','left'),('J','right'),('PTS','right'),('','left')])}</div>{lines}
<div style="margin-top:6px">{mono('Divisions refaites chaque dimanche · verdict le 30.11','#7a7264',4.2)}</div></div>''')
ec=[('Souley',412),('Jouneiid',398),("Coucoupop's",377),('Gaïl',361),('Sebovic',355),('Ilyes',349)]
bars=''.join(f'<div style="display:grid;grid-template-columns:44px 1fr 22px;gap:5px;align-items:center;margin:3px 0"><span class="A" style="font-stretch:62%;font-size:8.5px;color:{CR}">{n}</span><div style="height:7px;background:#ffffff1a;position:relative"><div style="position:absolute;inset:0 {100-(p-320)/(412-320)*100:.1f}% 0 0;background:{OR if i==0 else CR}"></div></div>{mono("tête" if i==0 else f"−{412-p}",OR if i==0 else CR,4.6)}</div>' for i,(n,p) in enumerate(ec))
job('posts/03-ecarts',W,H,6,tissu(VB,W,H)+top(CR,'Les écarts · J4')+f'''<div style="position:absolute;left:10px;right:10px;top:24px"><div class="A" {A(125,17,f"color:{CR}")}>14 points.</div><div class="S" style="font-size:12px;color:{OR}">L'avance de Souley sur Jouneiid.</div><div style="margin-top:12px">{bars}</div>
<div style="margin-top:10px;border-top:1px dashed #EEE6D366;padding-top:6px">{mono('Le duel le plus serré','#EEE6D3aa',4.4)}<div class="A" {A(62,13,f"color:{CR}")}>Sebovic − Ilyes : 6 pts</div></div></div>''')
job('posts/04-le-but',W,H,6,papier(W,H)+f'''<div class="ph" style="left:9px;right:9px;top:9px;height:62%;background-image:url({PH['02-terrain']})"></div>{top(CR,'J4 · 14:23')}
<div style="position:absolute;left:10px;right:10px;bottom:10px;color:{EN}"><div class="S" style="font-size:15px;color:{BX}">et soudain,</div><div class="A" {A(125,36)}>But.</div><div style="margin-top:3px">{mono('Jouneiid · Match 2 · Terrain 1',EN,4.8)}</div></div>''')
job('posts/05-dimanche',W,H,6,f'''<div class="ph" style="inset:0;background-image:url({PH['03-detail']})"></div>{top(CR,'J5 · 15.11.26')}
<div style="position:absolute;left:10px;right:10px;bottom:12px;color:{CR}"><div class="S" style="font-size:22px">Dimanche,</div><div class="A" {A(125,30)}>12 h 30.</div><div style="margin-top:4px">{mono('Hippodrome de Marcq · viens seul',CR,4.8)}</div></div>''')
job('posts/06-mvp',W,H,6,cuir('#151313',W,H,3)+couture(OR,6,4)+top(OR,'Les cartes · J4')+f'''<div style="position:absolute;left:18px;top:24%">{plaque('MVP','or',144,62,26,'le patron du terrain 1',125)}</div>
<div style="position:absolute;left:21px;top:calc(24% + 27px)">{pierre('diamant',8)}</div><div style="position:absolute;left:151px;top:calc(24% + 27px)">{pierre('diamant',8)}</div>
<img src="{C['souley']}" style="position:absolute;right:8%;bottom:-8%;width:38%;transform:rotate(4deg);filter:drop-shadow(0 4px 6px rgba(0,0,0,.6))"><div style="position:absolute;left:10px;bottom:10px;color:{BLANC}"><div class="A" {A(62,18)}>Souley</div>{mono('7 buts · 3 passes',BLANC,4.6)}</div>''')
job('posts/07-ton-nom',W,H,6,f'''<div class="ph" style="inset:0;background-image:url({PH['04-maillot']});background-position:50% 30%"></div>{top(CR,'Recrutement')}
<div style="position:absolute;left:0;right:0;bottom:0;height:40%">{cuir(BX,W,90,5)}{couture(OR,5,3)}<div style="position:absolute;left:12px;right:12px;top:12px;color:{CR}"><div class="S" style="font-size:14px;color:{OR}">Il manque un joueur.</div><div class="A" {A(100,20)}>Ton nom ici.</div><div style="margin-top:3px">{mono('Inscription · getbola.app',CR,4.6)}</div></div></div>''')
job('posts/08-verdict',W,H,6,cuir(BX,W,H,7)+couture(OR,6,4)+top(OR,'30.11.26')+f'''<div style="position:absolute;left:0;right:0;top:24%;text-align:center"><div class="S" style="font-size:16px;color:{OR}">Jour de</div></div>
<div style="position:absolute;left:18px;top:34%">{plaque('Verdict','or',144,50,24)}</div><div style="position:absolute;left:0;right:0;top:62%;text-align:center">{mono('Les cartes changent lundi',CR,5)}</div>
<div style="position:absolute;left:50%;bottom:22px;transform:translateX(-50%)">{brode(OR,"20px")}</div>''')
job('posts/09-le-lieu',W,H,6,f'''<div class="ph" style="inset:0;background-image:url({PH['06-lieu']})"></div>{top(EN,'SFL · saison 1',EN)}
<div style="position:absolute;left:10px;right:10px;bottom:10px;padding:8px 9px;overflow:hidden">{papier(161,60)}<div style="position:relative;color:{EN}"><div class="S" style="font-size:13px;color:{EM}">Ici, tout le monde commence</div><div class="A" {A(125,20)}>inconnu.</div></div></div>''')
coupes=[('coupe-pepite',"Pépite d'Or"),('coupe-buteur','Buteur'),('coupe-passeur','Passeur'),('coupe-defenseur','Défenseur'),('coupe-mvp','MVP')]
row=''.join(f'<div style="display:grid;justify-items:center;gap:5px"><img src="{TR(c+"-or")}" style="height:{74 if i==0 else 54}px;display:block;filter:drop-shadow(0 3px 4px rgba(0,0,0,.5))"><div class="A" style="font-stretch:62%;font-size:{8 if i==0 else 6.5}px;color:{OR if i==0 else BLANC};text-align:center;white-space:nowrap">{n}</div></div>' for i,(c,n) in enumerate(coupes))
job('posts/10-trophees-saison',W,H,6,f'<div style="position:absolute;inset:0;background:{NOIR}"></div>'+top(BLANC,'Saison 1 · 24.01.27',BLANC)+f'''<div style="position:absolute;left:12px;right:12px;top:26px;color:{BLANC}"><div class="S" style="font-size:14px;color:{OR}">Ce qui se gagne cette saison</div><div class="A" {A(125,20)}>Les trophées</div></div>
<div style="position:absolute;left:6px;right:6px;bottom:40px;display:flex;justify-content:space-around;align-items:flex-end">{row}</div>
<div style="position:absolute;left:12px;right:12px;bottom:12px;text-align:center">{mono("L'or au 1er · l'argent au 2e · le bronze au 3e · gardés à vie",'#ffffffaa',4.2)}</div>''')
job('posts/11-pepite-or',W,H,6,f'<div style="position:absolute;inset:0;background:{NOIR}"></div>'+top(BLANC,'24.01.27',BLANC)+f'''<div style="position:absolute;left:0;right:0;top:20px;text-align:center"><div class="S" style="font-size:14px;color:{OR}">La nuit de la</div></div>
<img src="{TR('coupe-pepite-or')}" style="position:absolute;left:50%;top:38px;height:112px;transform:translateX(-50%);filter:drop-shadow(0 6px 8px rgba(0,0,0,.6))">
<div style="position:absolute;left:28px;top:156px">{plaque("Pépite d'Or",'or',124,30,13,'Saison 1',95)}</div><div style="position:absolute;left:0;right:0;top:192px;display:flex;justify-content:center">{pierre('diamant',10)}</div>
<div style="position:absolute;left:0;right:0;bottom:10px;text-align:center">{mono('13 dimanches · une seule',BLANC,4.6)}</div>''')
# REELS 9:16
job('reels/01-le-but',W,V,6,f'''<div class="ph" style="left:0;right:0;top:0;height:60%;background-image:url({PH['02-terrain']})"></div><div style="position:absolute;left:0;right:0;top:60%;bottom:0">{papier(W,128)}</div>{top(CR,'J4 · 14:23')}
<div style="position:absolute;left:12px;right:30px;top:63%;color:{EN}"><div class="S" style="font-size:22px;color:{BX}">et soudain,</div><div class="A" {A(125,52)}>But.</div><div style="margin-top:5px">{mono('Jouneiid · Terrain 1',EN,6)}</div></div>''')
job('reels/02-il-te-manque',W,V,6,tissu(OL,W,V)+top(CR,'Ta course')+f'''<div style="position:absolute;left:12px;right:20px;top:24%;color:{CR}"><div class="S" style="font-size:20px">Il te manque</div><div class="A" {A(110,52)}>9 pts</div><div class="S" style="font-size:20px">pour passer Ilyes.</div>
<div style="margin-top:14px;display:flex;gap:6px;align-items:center"><img src="{C['sebovic']}" style="width:34px"><div>{mono('Toi · 8e · 340 pts',CR,4.8)}<br>{mono('Prochain match : dim. 12 h 30','#EEE6D3bb',4.4)}</div></div></div>''')
job('reels/03-il-manque-1',W,V,6,terre(W,V)+top(CR,'Dimanche 12 h 30')+f'''<div style="position:absolute;left:12px;right:20px;top:24%;color:{CR}"><div class="A" {A(125,27)}>Il manque</div><div class="A" {A(125,150,"line-height:.8")}>1.</div><div style="margin-top:10px">{mono('Viens seul · getbola.app',CR,7)}</div></div>''')
job('reels/04-podium',W,V,6,cuir(BX,W,V,3)+couture(OR,6,4)+top(OR,'S1 · après la J4')+f'''<div style="position:absolute;left:12px;top:26px"><div class="A" {A(110,19,f"color:{CR}")}>La course</div><div class="S" style="font-size:18px;color:{OR}">à la Pépite d'Or</div></div>
<div style="position:absolute;left:8px;right:8px;top:40%;display:flex;align-items:flex-end;justify-content:center;gap:6px">{pod(C['jouneid'],42,2,'Jouneiid',398,4)}{pod(C['souley'],66,1,'Souley',412,4)}{pod(C['coucoupops'],42,3,"Coucoupop's",377,3)}</div>''')
job('reels/05-pepite-or',W,V,6,f'<div style="position:absolute;inset:0;background:{NOIR}"></div>'+top(BLANC,'S1 · 24.01.27',BLANC)+f'''<div style="position:absolute;left:0;right:0;top:34px;text-align:center"><div class="S" style="font-size:20px;color:{OR}">13 dimanches.</div><div class="A" {A(110,22,f"color:{BLANC}")}>Une seule.</div></div>
<img src="{TR('coupe-pepite-or')}" style="position:absolute;left:50%;top:90px;height:150px;transform:translateX(-50%);filter:drop-shadow(0 6px 8px rgba(0,0,0,.6))">
<img src="{TR('pepite-or')}" style="position:absolute;right:16px;top:200px;width:46px;transform:rotate(-12deg)">
<div style="position:absolute;left:28px;top:250px">{plaque("Pépite d'Or",'or',124,30,13,'Saison 1',95)}</div>''')
# YOUTUBE miniature 1280x720
job('youtube/miniature-resume',160,90,8,f'''<div class="ph" style="left:0;top:0;bottom:0;width:58%;background-image:url({PH['02-terrain']})"></div><div style="position:absolute;left:58%;top:0;right:0;bottom:0">{cuir(BX,68,90,4)}</div>
<div style="position:absolute;left:5px;top:5px">{brode(CR,"4.5px",False)}</div>
<div style="position:absolute;right:7px;top:6px;bottom:6px;width:36%;display:flex;flex-direction:column;justify-content:space-between;align-items:flex-end;text-align:right;color:{CR}">
{mono('Le résumé · S1',OR,3)}<div class="A" {A(110,34,"line-height:.8")}>J4</div><div><div class="S" style="font-size:8px;color:{OR}">personne</div><div class="A" {A(75,8)}>ne lâche.</div></div></div>''')
# BANNIÈRES
job('bannieres/youtube-2560x1440',256,144,10,cuir(BX,256,144,6)+f'''<div style="position:absolute;left:50%;top:50%;width:154.6px;height:42.3px;transform:translate(-50%,-50%);display:flex;align-items:center;justify-content:space-between;color:{CR}">
<div>{brode(OR,"12px")}</div><div style="text-align:right"><div class="S" style="font-size:9px;color:{OR}">le dimanche</div><div class="A" {A(125,13)}>décide.</div><div style="margin-top:2px">{mono('Foot à 5 · Lille · Marcq · chaque dimanche',CR,2.6)}</div></div></div>
<div style="position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);height:58px">{couture(OR,0,0)}</div>''')
job('bannieres/twitch-1200x480',240,96,5,f'''<div style="position:absolute;inset:0 32% 0 0">{tissu(VB,164,96)}</div><div class="ph" style="right:0;top:0;bottom:0;width:32%;background-image:url({PH['02-terrain']})"></div>
<div style="position:absolute;left:14px;top:50%;transform:translateY(-50%);color:{CR}"><div class="S" style="font-size:12px;color:{OR}">en direct, le dimanche</div><div class="A" {A(62,17)}>Sunday Five League</div><div style="margin-top:4px">{mono('12 h 30 · Hippodrome de Marcq',CR,4)}</div></div>''')
job('bannieres/twitch-hors-ligne-1920x1080',192,108,10,pelouse(192,108,8)+f'''<div style="position:absolute;inset:0;display:grid;place-items:center;text-align:center;color:{CR}"><div><div style="display:flex;justify-content:center;margin-bottom:6px">{brode(CR,"11px")}</div>
<div class="S" style="font-size:11px;color:{OR}">on revient</div><div class="A" {A(125,19)}>dimanche.</div><div style="margin-top:4px">{mono('12 h 30 · Twitch et YouTube · getbola.app',CR,3)}</div></div></div>''')
json.dump(JOBS,open('jobs.json','w')); print(len(JOBS))
