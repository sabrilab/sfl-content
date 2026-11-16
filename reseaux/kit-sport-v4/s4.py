# YouTube / Twitch v4 : à plat, sans relief ni barres. Une texture par support : herbe fine, maille de maillot, liseré or.
import re,json,pathlib,base64,math
D=re.search(r' d="([^"]+)"',open('/home/user/SFL/public/bola/sfl.svg').read()).group(1)
PH='data:image/jpeg;base64,'+base64.b64encode(open('/home/user/visuels/photos-magnific/02-terrain.jpg','rb').read()).decode()
V={'nuit':'#0C1F16','foret':'#163826','pelouse':'#22573A','vif':'#2F7D4E','sauge':'#9CC5A6','menthe':'#E3EFE4'}
N='#0B0B0B'; B='#FFFFFF'; BX='#6E1F2E'; OR='#C9A03A'
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,500..900;1,62..125,900&display=block">'
CSS='*{box-sizing:border-box;margin:0}.T{font-family:Archivo;font-style:italic;font-weight:900;text-transform:uppercase;line-height:.9;white-space:nowrap}.L{font-family:Archivo;font-weight:600;font-stretch:110%;text-transform:uppercase;letter-spacing:.22em;white-space:nowrap}'
def sig(col,h): return f'<svg viewBox="0 0 735 237" style="height:{h}px;width:auto;display:block"><path d="{D}" fill="{col}"/></svg>'
U=[0]
def uid(): U[0]+=1; return f'f{U[0]}'
def herbe(w,h,base,o=.28):  # herbe fine : brins verticaux serrés + tonte très douce
    i=uid(); bands=''.join(f'<rect x="{k*w/6}" y="0" width="{w/6}" height="{h}" fill="#fff" opacity="{.025 if k%2 else 0}"/>' for k in range(6))
    return f'''<svg style="position:absolute;inset:0;width:100%;height:100%" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><rect width="{w}" height="{h}" fill="{base}"/>{bands}
<filter id="{i}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="3.2 .35" numOctaves="3" seed="7"/><feColorMatrix values="0 0 0 0 .55  0 0 0 0 .8  0 0 0 0 .55  0 0 0 {o} -.06"/></filter><rect width="{w}" height="{h}" filter="url(#{i})"/></svg>'''
def maille(w,h,base):  # maille de maillot, très fine
    i=uid(); p=uid()
    return f'''<svg style="position:absolute;inset:0;width:100%;height:100%" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><defs><pattern id="{p}" width="1.6" height="1.6" patternUnits="userSpaceOnUse"><rect width="1.6" height="1.6" fill="{base}"/><circle cx=".8" cy=".8" r=".38" fill="#000" opacity=".22"/></pattern></defs><rect width="{w}" height="{h}" fill="url(#{p})"/></svg>'''
def papier(w,h,base):
    i=uid(); return f'<svg style="position:absolute;inset:0;width:100%;height:100%" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><rect width="{w}" height="{h}" fill="{base}"/><filter id="{i}"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="2"/><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .08 0"/></filter><rect width="{w}" height="{h}" filter="url(#{i})"/></svg>'
def guilloche(w,h,base,col=OR,o=.16):  # rosace fine, comme un billet ou un trophée gravé
    cx,cy=w*.82,h*.5; R=max(w,h)*.7
    paths=''.join(f'<circle cx="{cx}" cy="{cy}" r="{R*(k/34)}" fill="none" stroke="{col}" stroke-width=".25" opacity="{o}"/>' for k in range(2,34))
    rays=''.join(f'<ellipse cx="{cx}" cy="{cy}" rx="{R*.55}" ry="{R*.18}" transform="rotate({a} {cx} {cy})" fill="none" stroke="{col}" stroke-width=".22" opacity="{o*.8}"/>' for a in range(0,180,12))
    return f'<svg style="position:absolute;inset:0;width:100%;height:100%" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><rect width="{w}" height="{h}" fill="{base}"/>{paths}{rays}</svg>'
def liseré(col=OR,inset=4,sw=.8): return f'<div style="position:absolute;inset:{inset}px;border:{sw}px solid {col}"></div>'
def pitch(x,y,cw,ch,col='#ffffff',o=.14,sw=.6):
    cy=y+ch/2; r=ch*.16; pa=ch*.3; pd=cw*.12
    return f'<svg style="position:absolute;left:0;top:0;overflow:visible" width="1" height="1"><g fill="none" stroke="{col}" stroke-width="{sw}" opacity="{o}"><rect x="{x}" y="{y}" width="{cw}" height="{ch}"/><line x1="{x+cw/2}" y1="{y}" x2="{x+cw/2}" y2="{y+ch}"/><circle cx="{x+cw/2}" cy="{cy}" r="{r}"/><path d="M{x} {cy-pa} A{pd} {pa} 0 0 1 {x} {cy+pa}"/><path d="M{x+cw} {cy-pa} A{pd} {pa} 0 0 0 {x+cw} {cy+pa}"/></g></svg>'
JOBS=[]
def job(path,w,h,sc,inner,bg=N):
    f=pathlib.Path('html')/(path.replace('/','__')+'.html'); f.parent.mkdir(exist_ok=True)
    f.write_text(f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{width:{w}px;height:{h}px}}</style></head><body><div style="position:relative;overflow:hidden;width:{w}px;height:{h}px;background:{bg}">{inner}</div></body></html>')
    JOBS.append({'html':str(f.resolve()),'out':path,'w':w,'h':h,'scale':sc})
# YouTube : herbe fine, terrain à peine visible, logo et nom à plat
job('youtube/banniere-2560x1440',256,144,10,herbe(256,144,V['foret'])+pitch(40,30,176,84)+f'''
<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:9px">{sig(B,16)}<div style="width:.6px;height:18px;background:#ffffff88"></div><div class="T" style="font-size:9px;font-stretch:105%;color:{B}">Sunday Five League</div></div>''')
# Twitch : photo, un bloc nuit net à gauche
job('twitch/banniere-1200x480',240,96,5,f'<div style="position:absolute;inset:0 0 0 40%;background:url({PH}) center/cover"></div><div style="position:absolute;inset:0 60% 0 0">{herbe(96,96,V["nuit"],.22)}</div>'+f'''
<div style="position:absolute;left:14px;top:50%;transform:translateY(-50%)">{sig(B,14)}<div class="T" style="font-size:12px;color:{B};margin-top:8px">Live</div><div class="T" style="font-size:12px;color:{V['sauge']}">dimanche</div></div>''')
# Hors ligne : herbe fine, texte à plat
job('twitch/hors-ligne-1920x1080',192,108,10,herbe(192,108,V['pelouse'],.25)+pitch(14,12,164,84,'#fff',.12)+f'''
<div style="position:absolute;inset:0;display:grid;place-items:center;text-align:center"><div><div style="display:flex;justify-content:center">{sig(B,11)}</div><div class="T" style="font-size:14px;color:{B};margin-top:10px">On revient dimanche</div></div></div>''')
# Miniature : photo + panneau nuit net, J6 à plat
job('youtube/miniature-resume',160,90,8,f'<div style="position:absolute;inset:0 38% 0 0;background:url({PH}) center/cover"></div><div style="position:absolute;inset:0 0 0 62%">{herbe(61,90,V["nuit"],.22)}</div>'+f'''
<div style="position:absolute;left:6px;top:6px">{sig(B,6)}</div><div style="position:absolute;right:0;width:38%;top:50%;transform:translateY(-50%);text-align:center" class="T"><span style="font-size:34px;color:{B}">J6</span></div>''')
# Panneaux : une matière par sujet
P=[('a-propos','À propos',herbe(160,50,V['foret'],.25),B,''),
   ('le-direct','Le direct',maille(160,50,BX),B,''),
   ('pepite-or',"Pépite d'Or",guilloche(160,50,N),OR,liseré(OR,3,.7)),
   ('viens-jouer','Viens jouer',herbe(160,50,V['vif'],.2),B,''),
   ('partenaires','Partenaires',papier(160,50,V['menthe']),V['nuit'],liseré(V['sauge'],3,.6))]
for n,t,tex,fg,extra in P:
    job(f'twitch/panneau-{n}',160,50,2,tex+extra+f'<div class="T" style="position:absolute;left:12px;top:50%;transform:translateY(-50%);font-size:14px;color:{fg}">{t}</div><div style="position:absolute;right:11px;top:50%;transform:translateY(-50%)">{sig(fg,7)}</div>')
job('youtube/filigrane',75,75,2,herbe(75,75,V['foret'])+f'<div style="position:absolute;inset:0;display:grid;place-items:center">{sig(B,16)}</div>')
job('profil/sfl-profil-herbe',180,180,6,herbe(180,180,V['foret'],.25)+f'<div style="position:absolute;inset:0;display:grid;place-items:center">{sig(B,40)}</div>')
json.dump(JOBS,open('jobs.json','w')); print(len(JOBS))
