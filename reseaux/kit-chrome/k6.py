import json,pathlib,base64
L=lambda n:'data:image/png;base64,'+base64.b64encode(open(f'/tmp/sflv/l3/{n}.png','rb').read()).decode()
CH=L('chromeT')
ph=lambda n:'data:image/webp;base64,'+base64.b64encode(open(f'/home/user/SFL/public/actus/couvertures/{n}-1200.webp','rb').read()).decode()
CG,BC,SI,CO=ph('cage-1'),ph('banc-1'),ph('silhouette-1'),ph('course-2')
B='#FFFFFF'; G='#2F7D4E'
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@800&display=block">'
CSS='*{box-sizing:border-box;margin:0}.H{font-family:Anton,sans-serif;text-transform:uppercase;line-height:.84;white-space:nowrap;color:#fff;letter-spacing:-.005em}.O{color:transparent;-webkit-text-stroke:.35px rgba(255,255,255,.55)}.m{font:800 3.2px Inter;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.7)}'
grain='<svg style="position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:overlay;pointer-events:none"><filter id="gr"><feTurbulence type="fractalNoise" baseFrequency="1.5" numOctaves="3" seed="9"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 .28"/></feComponentTransfer></filter><rect width="100%" height="100%" filter="url(#gr)"/></svg>'
def photo(src,pos='center',dark=.55): return f'<div style="position:absolute;inset:0;background:url({src}) {pos}/cover;filter:grayscale(1) contrast(1.22) brightness(.95)"></div><div style="position:absolute;inset:0;background:rgba(0,0,0,{dark})"></div>'+vig
vig='<div style="position:absolute;inset:0;background:radial-gradient(120% 90% at 50% 45%,transparent 45%,rgba(0,0,0,.75))"></div>'
edge=lambda c='rgba(255,255,255,.18)',i=4:f'<div style="position:absolute;inset:{i}px;border:.5px solid {c}"></div>'
glow=lambda o=.22:f'<div style="position:absolute;left:50%;top:50%;width:70%;height:80%;transform:translate(-50%,-50%);background:radial-gradient(closest-side,rgba(255,255,255,{o}),transparent)"></div>'
logo=lambda h,extra='':f'<img src="{CH}" style="height:{h}px;display:block;filter:drop-shadow(0 {h*.08}px {h*.12}px rgba(0,0,0,.85)){extra}">'
JOBS=[]
def job(path,w,h,sc,inner):
    f=pathlib.Path('html')/(path.replace('/','__')+'.html'); f.parent.mkdir(exist_ok=True)
    f.write_text(f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{width:{w}px;height:{h}px}}</style></head><body><div style="position:relative;overflow:hidden;width:{w}px;height:{h}px;background:#050505">{inner}{grain}</div></body></html>')
    JOBS.append({'html':str(f.resolve()),'out':path,'w':w,'h':h,'scale':sc})
# YouTube 2560x1440 -> 256x144 x10 ; zone sûre 154.6 x 42.3 au centre
job('youtube/banniere-2560x1440',256,144,10,photo(CG,'center 55%',.6)+glow(.1)+f'<div class="H O" style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-size:52px;opacity:.5">Dimanche</div><div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:9px">{logo(32)}<div style="width:.5px;height:22px;background:rgba(255,255,255,.4)"></div><div class="H" style="font-size:11px">Sunday<br>Five League</div></div>')
job('twitch/banniere-1200x480',240,96,5,photo(BC,'center 60%',.55)+f'<div style="position:absolute;left:16px;top:50%;transform:translateY(-50%)">{logo(30)}</div><div class="H" style="position:absolute;right:14px;bottom:12px;font-size:34px">Live.</div><div class="m" style="position:absolute;right:16px;top:14px;display:flex;gap:4px;align-items:center"><span style="width:4px;height:4px;border-radius:50%;background:#e33"></span>Dimanche · 12 h 30</div>'+edge())
job('twitch/hors-ligne-1920x1080',192,108,10,photo(SI,'center',.45)+f'<div style="position:absolute;left:50%;top:22%;transform:translateX(-50%)">{logo(24)}</div><div class="H" style="position:absolute;left:0;right:0;bottom:9px;font-size:28px;text-align:center">Dimanche.</div><div class="m" style="position:absolute;left:0;right:0;bottom:4px;text-align:center;font-size:2.4px">On revient · 12 h 30</div>'+edge())
job('youtube/miniature-resume',160,90,8,photo(CO,'center 40%',.2)+f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,transparent 45%,rgba(0,0,0,.6))"></div><div style="position:absolute;left:6px;top:6px">{logo(11)}</div><div class="H" style="position:absolute;right:6px;bottom:2px;font-size:62px">J6</div>')
job('youtube/filigrane',75,75,2,glow(.18)+f'<div style="position:absolute;inset:0;display:grid;place-items:center">{logo(22)}</div>')
job('profil/sfl-profil-chrome',180,180,6,glow(.2)+f'<div style="position:absolute;inset:0;display:grid;place-items:center">{logo(52)}</div>')
for n,t,img in [('a-propos','La ligue',BC),('le-direct','Le direct',CG),('pepite-or',"Pépite d'or",None),('viens-jouer','Viens jouer',CO),('partenaires','Partenaires',None)]:
    inner=(photo(img,'center',.62) if img else '')+f'<div class="H" style="position:absolute;left:10px;bottom:8px;font-size:24px">{t}</div>'+edge('rgba(255,255,255,.12)',3)+f'<div style="position:absolute;right:8px;top:7px">{logo(10)}</div>'
    if n=='pepite-or': inner+='<div style="position:absolute;left:10px;top:9px;width:16px;height:2px;background:#C9A03A"></div>'
    if n=='viens-jouer': inner+=f'<div style="position:absolute;left:10px;top:9px;width:16px;height:2px;background:{G}"></div>'
    job(f'twitch/panneau-{n}',160,50,2,inner)
# Instagram : post annonce + story
job('instagram/post-logo',180,225,6,photo(CG,'center 60%',.6)+glow(.14)+f'<div style="position:absolute;left:50%;top:40%;transform:translate(-50%,-50%)">{logo(44)}</div><div class="H" style="position:absolute;left:0;right:0;bottom:16px;font-size:30px;text-align:center">Viens seul.</div>')
job('instagram/story-logo',180,320,6,photo(SI,'center',.45)+f'<div style="position:absolute;left:50%;top:22%;transform:translateX(-50%)">{logo(40)}</div><div class="H" style="position:absolute;left:0;right:0;top:64%;font-size:34px;text-align:center">Dimanche.</div>')
json.dump(JOBS,open('jobs.json','w')); print(len(JOBS))
