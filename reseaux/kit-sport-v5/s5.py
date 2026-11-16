# YouTube / Twitch v5 : l'école des marques de sport (Nike, Adidas, Reebok). Photo plein cadre, typo condensée énorme, noir et blanc, un vert en accent.
import re,json,pathlib,base64
D=re.search(r' d="([^"]+)"',open('/home/user/SFL/public/bola/sfl.svg').read()).group(1)
ph=lambda n:'data:image/jpeg;base64,'+base64.b64encode(open(f'/home/user/visuels/photos-magnific/{n}.jpg','rb').read()).decode()
T,DT,M,L=ph('02-terrain'),ph('03-detail'),ph('04-maillot'),ph('06-lieu')
N='#0A0A0A'; B='#FFFFFF'; G='#2F7D4E'; GN='#0C1F16'
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@600;800&display=block">'
CSS='*{box-sizing:border-box;margin:0}.H{font-family:Anton,Impact,sans-serif;text-transform:uppercase;line-height:.84;letter-spacing:-.005em;white-space:nowrap}.s{font:800 4px Inter;letter-spacing:.18em;text-transform:uppercase}'
def sig(col,h): return f'<svg viewBox="0 0 735 237" style="height:{h}px;width:auto;display:block"><path d="{D}" fill="{col}"/></svg>'
def photo(src,pos='center',bw=True,dark=.35): return f'<div style="position:absolute;inset:0;background:url({src}) {pos}/cover;filter:{"grayscale(1) contrast(1.15)" if bw else "contrast(1.05)"}"></div><div style="position:absolute;inset:0;background:rgba(0,0,0,{dark})"></div>'+trame()
TEX=True
def grain(o=.16):
    if not TEX: return ''
    return f'<svg style="position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:overlay;pointer-events:none"><filter id="gr"><feTurbulence type="fractalNoise" baseFrequency="1.6" numOctaves="3" seed="9"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 {o*2}"/></feComponentTransfer></filter><rect width="100%" height="100%" filter="url(#gr)"/></svg>'
def trame(o=.14):  # trame d'impression (points) sur les photos, façon affiche
    if not TEX: return ''
    return f'<div style="position:absolute;inset:0;background-image:radial-gradient(circle,rgba(0,0,0,{o}) .45px,transparent .6px);background-size:1.6px 1.6px;mix-blend-mode:multiply"></div>'
def encre():  # léger voile sur les aplats noirs
    if not TEX: return ''
    return '<svg style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none"><filter id="ek"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="3" seed="4"/><feColorMatrix values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .07 0"/></filter><rect width="100%" height="100%" filter="url(#ek)"/></svg>'
JOBS=[]
def job(path,w,h,sc,inner,bg=N):
    f=pathlib.Path('html')/(path.replace('/','__')+'.html'); f.parent.mkdir(exist_ok=True)
    f.write_text(f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{width:{w}px;height:{h}px}}</style></head><body><div style="position:relative;overflow:hidden;width:{w}px;height:{h}px;background:{bg}">{encre() if bg in (N,) else ''}{inner}{grain()}</div></body></html>')
    JOBS.append({'html':str(f.resolve()),'out':path,'w':w,'h':h,'scale':sc})
# YouTube 2560x1440 : photo N&B plein cadre, titre énorme dans la zone sûre (154.6 x 42.3 au centre)
job('youtube/banniere-2560x1440',256,144,10,photo(T,'center 60%',True,.45)+f'''
<div style="position:absolute;left:50.7px;top:60.85px;width:154.6px;height:42.3px;display:flex;align-items:center;justify-content:center;gap:7px">
<div class="H" style="font-size:20px;color:{B}">Viens seul.</div><div style="width:2.2px;height:22px;background:{G}"></div>{sig(B,9)}</div>''')
# Twitch 1200x480 : photo couleur, mot énorme
job('twitch/banniere-1200x480',240,96,5,photo(T,'center 55%',False,.25)+f'''
<div class="H" style="position:absolute;left:12px;bottom:10px;font-size:44px;color:{B}">Live.</div>
<div style="position:absolute;left:14px;top:12px">{sig(B,9)}</div><div class="s" style="position:absolute;right:12px;top:14px;color:{B};background:{G};padding:3px 5px">Dimanche 12 h 30</div>''')
# Hors ligne : noir, un mot énorme coupé
job('twitch/hors-ligne-1920x1080',192,108,10,f'''<div class="H" style="position:absolute;left:-4px;right:-4px;top:50%;transform:translateY(-52%);font-size:46px;color:{B};text-align:center">Dimanche.</div>
<div style="position:absolute;left:10px;top:10px">{sig(B,7)}</div><div class="s" style="position:absolute;right:10px;top:12px;color:{G}">On revient</div>''')
# Miniature : photo plein cadre, J6 énorme en bas à droite
job('youtube/miniature-resume',160,90,8,photo(T,'center',False,.15)+f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,transparent 45%,rgba(0,0,0,.55))"></div>'+f'''
<div class="H" style="position:absolute;right:6px;bottom:2px;font-size:62px;color:{B}">J6</div><div style="position:absolute;left:6px;top:6px">{sig(B,6)}</div>''')
# Panneaux : noir, blanc, vert ; un mot énorme
for n,t,bg,fg,img in [('a-propos','La ligue',N,B,None),('le-direct','Le direct',None,B,T),('pepite-or',"Pépite d'or",N,B,None),('viens-jouer','Viens jouer',G,B,None),('partenaires','Partenaires',B,N,None)]:
    inner=(photo(img,'center',True,.5) if img else '')+f'<div class="H" style="position:absolute;left:10px;bottom:7px;font-size:26px;color:{fg}">{t}</div><div style="position:absolute;right:9px;top:8px">{sig(fg,6)}</div>'
    if n=='pepite-or': inner+=f'<div style="position:absolute;left:10px;top:9px;width:16px;height:2px;background:#C9A03A"></div>'
    job(f'twitch/panneau-{n}',160,50,2,inner,bg or N)
job('youtube/filigrane',75,75,2,f'<div style="position:absolute;inset:0;display:grid;place-items:center">{sig(B,16)}</div>')
job('profil/sfl-profil-noir',180,180,6,f'<div style="position:absolute;inset:0;display:grid;place-items:center">{sig(B,38)}</div>')
import sys
if len(sys.argv)>1: TEX=False
json.dump(JOBS,open('jobs.json','w')); print(len(JOBS))
