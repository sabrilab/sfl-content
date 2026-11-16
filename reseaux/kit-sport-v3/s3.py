# YouTube / Twitch v3 : une gamme de verts, des biais sportifs (l'angle du sigle, 21,8°), titres italiques en relief. Peu de mots.
import re,json,pathlib,base64
D=re.search(r' d="([^"]+)"',open('/home/user/SFL/public/bola/sfl.svg').read()).group(1)
PH='data:image/jpeg;base64,'+base64.b64encode(open('/home/user/visuels/photos-magnific/02-terrain.jpg','rb').read()).decode()
V={'nuit':'#0C1F16','foret':'#163826','pelouse':'#22573A','vif':'#2F7D4E','sauge':'#9CC5A6','menthe':'#E3EFE4'}
N='#0B0B0B'; B='#FFFFFF'; BX='#6E1F2E'
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@1,62..125,900&display=block">'
CSS='*{box-sizing:border-box;margin:0}'
def sig(col,h,ex=None):
    sh=f'<path d="{D}" fill="{ex}" transform="translate(9,12)"/><path d="{D}" fill="{ex}" transform="translate(6,8)"/><path d="{D}" fill="{ex}" transform="translate(3,4)"/>' if ex else ''
    return f'<svg viewBox="0 0 735 250" style="height:{h}px;width:auto;display:block;overflow:visible">{sh}<path d="{D}" fill="{col}"/></svg>'
def t3d(txt,sz,col=B,ex='#0C1F16',st=118,depth=4):
    sh=','.join(f'{k*.6}px {k*.8}px 0 {ex}' for k in range(1,depth+1))
    return f'<span style="font-family:Archivo;font-style:italic;font-weight:900;font-stretch:{st}%;font-size:{sz}px;line-height:.9;text-transform:uppercase;color:{col};text-shadow:{sh},{depth*.6+1}px {depth*.8+2}px 3px rgba(0,0,0,.35);white-space:nowrap">{txt}</span>'
def tonte(w,h,n,c1,c2,ang=0):
    b=''.join(f'<rect x="{k*w/n}" y="-{h}" width="{w/n+.5}" height="{h*3}" fill="{c1 if k%2 else c2}"/>' for k in range(-n,2*n))
    return f'<svg style="position:absolute;inset:0;width:100%;height:100%" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><g transform="skewX({-ang})">{b}</g><filter id="t"><feTurbulence type="fractalNoise" baseFrequency="1.3 .1" numOctaves="2" seed="5"/><feColorMatrix values="0 0 0 0 0 0 0 0 0 .1 0 0 0 0 0 0 0 0 .2 0"/></filter><rect width="{w}" height="{h}" filter="url(#t)"/></svg>'
def biais(x,w,h,col,band=None):  # bande en biais à l'angle du sigle (tan 21,8° = 0,4)
    return f'<div style="position:absolute;top:0;bottom:0;left:{x}px;width:{w}px;background:{band or col};transform:skewX(-21.8deg);transform-origin:bottom left"></div>'
def pitch(x,y,cw,ch,col='#ffffff',o=.22,sw=.7):
    cy=y+ch/2; r=ch*.16; pa=ch*.3; pd=cw*.12
    return f'<svg style="position:absolute;left:0;top:0;overflow:visible" width="1" height="1"><g fill="none" stroke="{col}" stroke-width="{sw}" opacity="{o}"><rect x="{x}" y="{y}" width="{cw}" height="{ch}"/><line x1="{x+cw/2}" y1="{y}" x2="{x+cw/2}" y2="{y+ch}"/><circle cx="{x+cw/2}" cy="{cy}" r="{r}"/><path d="M{x} {cy-pa} A{pd} {pa} 0 0 1 {x} {cy+pa}"/><path d="M{x+cw} {cy-pa} A{pd} {pa} 0 0 0 {x+cw} {cy+pa}"/></g></svg>'
JOBS=[]
def job(path,w,h,sc,inner,bg):
    f=pathlib.Path('html')/(path.replace('/','__')+'.html'); f.parent.mkdir(exist_ok=True)
    f.write_text(f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{width:{w}px;height:{h}px}}</style></head><body><div style="position:relative;overflow:hidden;width:{w}px;height:{h}px;background:{bg}">{inner}</div></body></html>')
    JOBS.append({'html':str(f.resolve()),'out':path,'w':w,'h':h,'scale':sc})
# Palette : la gamme de verts, puis noir, blanc, bordeaux
items=list(V.items())+[('noir',N),('blanc',B),('bordeaux',BX)]
sw=''.join(f'<div style="height:30px;display:flex;align-items:center;justify-content:space-between;padding:0 10px;background:{c};font:italic 900 9px Archivo;text-transform:uppercase;color:{N if k in ("sauge","menthe","blanc") else B};{"outline:1px solid #0002;" if k=="blanc" else ""}"><span>{k}</span><span>{c}</span></div>' for k,c in items)
job('palette-verts',160,270,4,f'<div style="position:absolute;inset:0">{sw}</div>',B)
# YouTube banner 2560x1440 (zone sûre centrale) : fond nuit, une bande de pelouse en biais derrière le logo
yb=biais(80,96,144,'',f'linear-gradient(90deg,{V["pelouse"]} 0 50%,{V["vif"]} 50%)')+biais(184,14,144,V['sauge'])+biais(206,5,144,V['menthe'])
job('youtube/banniere-2560x1440',256,144,10,yb+pitch(30,22,196,100)+f'''<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:10px">{sig(B,22,V['nuit'])}{t3d('Sunday Five League',10,B,V['nuit'],100,3)}</div>''',V['nuit'])
# Twitch banner 1200x480 : photo à droite, biais nuit à gauche
job('twitch/banniere-1200x480',240,96,5,f'<div style="position:absolute;inset:0;background:url({PH}) right center/cover"></div>'+biais(-60,190,96,V['nuit'])+biais(128,10,96,V['vif'])+biais(142,4,96,V['menthe'])+f'''
<div style="position:absolute;left:16px;top:50%;transform:translateY(-50%)">{sig(B,20,V['foret'])}<div style="margin-top:9px">{t3d('Live dimanche',13,B,V['foret'],100,3)}</div></div>''',V['nuit'])
# Écran hors ligne
job('twitch/hors-ligne-1920x1080',192,108,10,tonte(192,108,12,V['foret'],V['pelouse'],21.8)+pitch(14,12,164,84,'#fff',.25,.6)+f'''
<div style="position:absolute;inset:0;display:grid;place-items:center;text-align:center"><div><div style="display:flex;justify-content:center">{sig(B,14,V['nuit'])}</div><div style="margin-top:12px">{t3d('On revient',15,B,V['nuit'],110,3)}</div><div style="margin-top:2px">{t3d('dimanche',15,V['menthe'],V['nuit'],110,3)}</div></div></div>''',V['foret'])
# Miniature YouTube : photo + biais nuit + J6 en relief
job('youtube/miniature-resume',160,90,8,f'<div style="position:absolute;inset:0;background:url({PH}) left center/cover"></div>'+biais(98,120,90,V['nuit'])+biais(90,6,90,V['vif'])+f'''
<div style="position:absolute;left:6px;top:6px">{sig(B,7,V['nuit'])}</div><div style="position:absolute;right:10px;top:50%;transform:translateY(-50%)">{t3d('J6',40,B,V['vif'],105,4)}</div>''',V['nuit'])
# Panneaux Twitch : une teinte de la gamme chacun
for n,t,bg,fg,ex in [('a-propos','À propos',V['nuit'],B,V['vif']),('le-direct','Le direct',BX,B,'#3d0f18'),('pepite-or',"Pépite d'Or",N,B,'#333'),('viens-jouer','Viens jouer',V['vif'],B,V['nuit']),('partenaires','Partenaires',V['menthe'],V['nuit'],'#c4dcc8')]:
    job(f'twitch/panneau-{n}',160,50,2,biais(118,22,50,'#ffffff14')+biais(146,6,50,'#ffffff22')+f'<div style="position:absolute;left:12px;top:50%;transform:translateY(-50%)">{t3d(t,16,fg,ex,100,3)}</div>',bg)
# Filigrane, profil
job('youtube/filigrane',75,75,2,biais(20,30,75,V['pelouse'])+f'<div style="position:absolute;inset:0;display:grid;place-items:center">{sig(B,20,V["nuit"])}</div>',V['nuit'])
job('profil/sfl-profil-pelouse',180,180,6,biais(40,70,180,V['pelouse'])+biais(118,10,180,V['sauge'])+f'<div style="position:absolute;inset:0;display:grid;place-items:center">{sig(B,44,"#05120c")}</div>',V['nuit'])
json.dump(JOBS,open('jobs.json','w')); print(len(JOBS))
