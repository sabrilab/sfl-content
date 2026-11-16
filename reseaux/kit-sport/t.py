# Habillage YouTube / Twitch « court de tennis » : aplats, lignes de court, tableau de score. Le vrai sigle SFL.
import re,json,pathlib,base64
D=re.search(r' d="([^"]+)"',open('/home/user/SFL/public/bola/sfl.svg').read()).group(1)
PH='data:image/jpeg;base64,'+base64.b64encode(open('/home/user/visuels/photos-magnific/02-terrain.jpg','rb').read()).decode()
G='#1B4D35'; GD='#123826'; CL='#C4552A'; CR='#F4F1E8'; EN='#0B0B0B'; LI='#FFFFFF'; JA='#E9D86A'
def sig(col,h): return f'<svg viewBox="0 0 735 237" style="height:{h}px;width:auto;display:block"><path d="{D}" fill="{col}"/></svg>'
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,500..900;1,62..125,900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@700&display=block">'
CSS='*{box-sizing:border-box;margin:0}.A{font-family:Archivo;font-weight:900;text-transform:uppercase;line-height:.86}.S{font-family:"Instrument Serif";font-style:italic;line-height:1}.M{font-family:"JetBrains Mono";font-weight:700;text-transform:uppercase;letter-spacing:.16em}'
def grain(w,h,o=.07): return f'<svg style="position:absolute;inset:0;width:100%;height:100%" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3"/><feColorMatrix values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 {o} 0"/></filter><rect width="{w}" height="{h}" filter="url(#g)"/></svg>'
def court(w,h,x,y,cw,ch,col=LI,sw=1.2,o=.9):
    # demi-terrain vu de dessus : couloirs, ligne de service, ligne médiane
    al=cw*.125; sv=ch*.42
    return f'''<svg style="position:absolute;left:0;top:0" width="{w}" height="{h}"><g fill="none" stroke="{col}" stroke-width="{sw}" opacity="{o}">
<rect x="{x}" y="{y}" width="{cw}" height="{ch}"/><line x1="{x+al}" y1="{y}" x2="{x+al}" y2="{y+ch}"/><line x1="{x+cw-al}" y1="{y}" x2="{x+cw-al}" y2="{y+ch}"/>
<line x1="{x+al}" y1="{y+ch-sv}" x2="{x+cw-al}" y2="{y+ch-sv}"/><line x1="{x+cw/2}" y1="{y+ch-sv}" x2="{x+cw/2}" y2="{y+ch}"/><line x1="{x+cw/2}" y1="{y}" x2="{x+cw/2}" y2="{y+5}"/></g></svg>'''
def score(rows,fs=10,bg=GD):
    r=''.join(f'<tr><td style="padding:2px 8px 2px 4px;font:900 {fs}px Archivo;font-stretch:80%;text-transform:uppercase;color:{LI};white-space:nowrap">{n}</td>'+''.join(f'<td style="width:{fs*1.6}px;text-align:center;font:900 {fs}px Archivo;color:{JA if k==len(s)-1 else LI};border-left:1px solid #ffffff33">{v}</td>' for k,v in enumerate(s))+'</tr>' for n,s in rows)
    return f'<table style="border-collapse:collapse;background:{bg};border:1.5px solid {LI}">{r}</table>'
JOBS=[]
def job(path,w,h,scale,inner,bg):
    f=pathlib.Path('html')/(path.replace('/','__')+'.html'); f.parent.mkdir(exist_ok=True)
    f.write_text(f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{width:{w}px;height:{h}px}}</style></head><body><div style="position:relative;overflow:hidden;width:{w}px;height:{h}px;background:{bg}">{inner}</div></body></html>')
    JOBS.append({'html':str(f.resolve()),'out':path,'w':w,'h':h,'scale':scale})
# YouTube 2560x1440 (zone sûre 1546x423 au centre) -> 256x144 x10
yb=court(256,144,-20,22,180,140,LI,.5,.35)+court(256,144,150,-40,160,150,LI,.5,.25)
job('youtube/banniere-2560x1440',256,144,10,grain(256,144)+yb+f'''<div style="position:absolute;left:50.7px;top:60.85px;width:154.6px;height:42.3px;display:flex;align-items:center;justify-content:center;gap:9px;color:{LI}">
{sig(LI,13)}<div style="width:1px;height:26px;background:#ffffff66"></div><div><div class="S" style="font-size:7.5px;color:{CR}">foot à 5, le dimanche</div><div class="A" style="font-stretch:70%;font-size:10px;white-space:nowrap">Sunday Five League</div><div class="M" style="font-size:2.7px;margin-top:3px;color:{CR}">Direct 12 h 30 · Résumés · Défis</div></div></div>''',G)
# Twitch banniere 1200x480 -> 240x96 x5
job('twitch/banniere-1200x480',240,96,5,f'<div style="position:absolute;left:0;top:0;bottom:0;width:58%;background:{G}"></div><div style="position:absolute;left:58%;top:0;bottom:0;right:0;background:url({PH}) center/cover"></div><div style="position:absolute;left:58%;top:0;bottom:0;width:3px;background:{LI}"></div>'+grain(240,96)+court(240,96,-30,8,150,110,LI,.6,.3)+f'''
<div style="position:absolute;left:14px;top:16px;color:{LI}">{sig(LI,13)}<div class="S" style="font-size:11px;color:{CR};margin-top:8px">en direct, le dimanche</div><div class="A" style="font-stretch:70%;font-size:14px;white-space:nowrap">Sunday Five League</div>
<div style="margin-top:7px;display:inline-block;background:{CL};padding:3px 6px" class="M"><span style="font-size:4px">Live · 12 h 30</span></div></div>''',G)
# Twitch hors ligne 1920x1080 -> 192x108 x10
job('twitch/hors-ligne-1920x1080',192,108,10,grain(192,108)+court(192,108,46,10,100,92,LI,.6,.45)+f'''
<div style="position:absolute;left:0;right:0;top:14px;display:flex;justify-content:center">{sig(LI,9)}</div>
<div style="position:absolute;left:0;right:0;top:36px;text-align:center;color:{LI}"><div class="S" style="font-size:11px;color:{CR}">fin du set</div><div class="A" style="font-stretch:80%;font-size:13px;white-space:nowrap">On revient dimanche.</div></div>
<div style="position:absolute;left:50%;top:66px;transform:translateX(-50%)">{score([('Noirs',['3','2','5']),('Blancs',['1','4','4'])],5.5)}</div>
<div class="M" style="position:absolute;left:0;right:0;bottom:6px;text-align:center;font-size:2.8px;color:{CR}">12 h 30 · Twitch et YouTube · getbola.app/sfl</div>''',G)
# Panneaux Twitch 320x100 -> 160x50 x2
for n,t,s,bg in [('a-propos','À propos','la ligue',G),('le-direct','Le direct','dimanche 12 h 30',CL),('pepite-or',"Pépite d'Or",'le classement',EN),('viens-jouer','Viens jouer','getbola.app/sfl',G),('partenaires','Partenaires','ils nous suivent',EN)]:
    job(f'twitch/panneau-{n}',160,50,2,grain(160,50)+court(160,50,104,-6,70,62,LI,.6,.35)+f'<div style="position:absolute;left:10px;top:50%;transform:translateY(-50%);color:{LI}"><div class="A" style="font-stretch:80%;font-size:15px">{t}</div><div class="S" style="font-size:9px;color:{CR if bg!=CL else LI}">{s}</div></div><div style="position:absolute;right:8px;top:7px">{sig(LI,6)}</div>',bg)
# Miniature YouTube 1280x720 -> 160x90 x8
job('youtube/miniature-resume',160,90,8,f'<div style="position:absolute;inset:0 44% 0 0;background:url({PH}) center/cover"></div><div style="position:absolute;inset:0 0 0 56%;background:{G}"></div>'+court(160,90,96,8,56,74,LI,.5,.35)+f'''<div style="position:absolute;left:56%;top:0;bottom:0;width:2px;background:{LI}"></div>
<div style="position:absolute;left:5px;top:5px">{sig(LI,5)}</div><div style="position:absolute;right:8px;top:6px;text-align:right;color:{LI}"><div class="M" style="font-size:3px;color:{CR}">Le résumé · S1</div><div class="A" style="font-stretch:110%;font-size:26px;margin-top:6px">J6</div></div>
<div style="position:absolute;right:8px;bottom:8px">{score([('Noirs',['5']),('Blancs',['4'])],6)}</div>''',G)
# Filigrane 150x150
job('youtube/filigrane',75,75,2,f'<div style="position:absolute;inset:0;display:grid;place-items:center">{sig(LI,18)}</div>',G)
# Photo de profil sport (variante)
job('profil/sfl-profil-court',180,180,6,grain(180,180)+court(180,180,40,24,100,132,LI,1,.35)+f'<div style="position:absolute;inset:0;display:grid;place-items:center">{sig(LI,40)}</div>',G)
json.dump(JOBS,open('jobs.json','w')); print(len(JOBS))
