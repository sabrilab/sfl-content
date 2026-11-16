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
def hero(h,refl=True,streak=True):
    st=f'<div style="position:absolute;left:50%;top:50%;width:{h*9}px;height:{h*.06}px;transform:translate(-50%,-50%);background:linear-gradient(90deg,transparent,rgba(255,255,255,.85) 50%,transparent);filter:blur({h*.03}px)"></div><div style="position:absolute;left:50%;top:50%;width:{h*2.2}px;height:{h*.9}px;transform:translate(-50%,-50%);background:radial-gradient(closest-side,rgba(255,255,255,.22),transparent)"></div>' if streak else ''
    rf=f'<img src="{CH}" style="position:absolute;left:0;top:100%;height:{h}px;transform:scaleY(-1);opacity:.28;-webkit-mask-image:linear-gradient(to top,rgba(0,0,0,.9),transparent 55%);mask-image:linear-gradient(to top,rgba(0,0,0,.9),transparent 55%);margin-top:{h*.04}px">' if refl else ''
    return f'<div style="position:relative">{st}<img src="{CH}" style="position:relative;height:{h}px;display:block;filter:drop-shadow(0 {h*.06}px {h*.1}px rgba(0,0,0,.9))">{rf}</div>'
def bug(a,b,sa,sb,fs=4):
    return f'<div style="display:flex;align-items:stretch;font:800 {fs}px Inter;letter-spacing:.14em;text-transform:uppercase;box-shadow:0 1px 4px rgba(0,0,0,.6)"><span style="background:#0A0A0A;color:#fff;padding:{fs*.7}px {fs}px">{a}</span><span style="background:#fff;color:#0A0A0A;padding:{fs*.7}px {fs*.9}px;font-family:Anton;font-size:{fs*1.6}px;letter-spacing:0;line-height:1">{sa}–{sb}</span><span style="background:#0A0A0A;color:#fff;padding:{fs*.7}px {fs}px">{b}</span></div>'
logo=lambda h,extra='':f'<img src="{CH}" style="height:{h}px;display:block;filter:drop-shadow(0 {h*.08}px {h*.12}px rgba(0,0,0,.85)){extra}">'
JOBS=[]
def job(path,w,h,sc,inner):
    f=pathlib.Path('html')/(path.replace('/','__')+'.html'); f.parent.mkdir(exist_ok=True)
    f.write_text(f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{width:{w}px;height:{h}px}}</style></head><body><div style="position:relative;overflow:hidden;width:{w}px;height:{h}px;background:#050505">{inner}{grain}</div></body></html>')
    JOBS.append({'html':str(f.resolve()),'out':path,'w':w,'h':h,'scale':sc})
# YouTube 2560x1440 -> 256x144 x10 ; zone sûre 154.6 x 42.3 au centre
job('youtube/banniere-2560x1440',256,144,10,photo(CG,'center 55%',.66)+f'<div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%)">{hero(34)}</div><div class="m" style="position:absolute;left:0;right:0;top:63%;text-align:center;font-size:3.6px;letter-spacing:.6em">Sunday · Five · League</div>')
job('twitch/banniere-1200x480',240,96,5,photo(BC,'center 60%',.6)+f'<div style="position:absolute;left:18px;top:50%;transform:translateY(-62%)">{hero(26,True,False)}</div><div class="H" style="position:absolute;right:14px;bottom:10px;font-size:40px">Live.</div><div class="m" style="position:absolute;right:16px;top:13px;display:flex;gap:4px;align-items:center"><span style="width:4px;height:4px;border-radius:50%;background:#e33;box-shadow:0 0 4px #e33"></span>Dimanche · 12 h 30</div>'+edge())
job('twitch/hors-ligne-1920x1080',192,108,10,photo(SI,'center',.5)+f'<div style="position:absolute;left:50%;top:30%;transform:translate(-50%,-50%)">{hero(20,False)}</div><div class="H" style="position:absolute;left:0;right:0;bottom:12px;font-size:30px;text-align:center">Dimanche.</div><div class="m" style="position:absolute;left:0;right:0;bottom:6px;text-align:center;font-size:2.4px;letter-spacing:.5em">On revient · 12 h 30</div>'+edge())
job('youtube/miniature-resume',160,90,8,photo(CO,'center 40%',.25)+f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,transparent 40%,rgba(0,0,0,.7))"></div><div style="position:absolute;left:6px;top:6px">{logo(10)}</div><div style="position:absolute;left:6px;bottom:7px">{bug("Noirs","Blancs",5,4,3.4)}</div><div class="H" style="position:absolute;right:6px;bottom:2px;font-size:64px">J6</div>')
job('youtube/filigrane',75,75,2,glow(.18)+f'<div style="position:absolute;inset:0;display:grid;place-items:center">{logo(22)}</div>')
job('profil/sfl-profil-chrome',180,180,6,f'<div style="position:absolute;inset:0;display:grid;place-items:center">{hero(46,False)}</div>')
for i,(n,t,img) in enumerate([('a-propos','La ligue',BC),('le-direct','Le direct',CG),('pepite-or',"Pépite d'or",None),('viens-jouer','Viens jouer',CO),('partenaires','Partenaires',None)]):
    inner=(photo(img,'center',.62) if img else '')+f'<div class="m" style="position:absolute;left:10px;top:8px;font-size:3.6px">0{i+1}</div><div class="H" style="position:absolute;left:10px;bottom:8px;font-size:24px">{t}</div>'+edge('rgba(255,255,255,.12)',3)+f'<div style="position:absolute;right:8px;top:7px">{logo(10)}</div>'
    if n=='pepite-or': inner+='<div style="position:absolute;left:20px;top:9.6px;width:14px;height:1.4px;background:#C9A03A"></div>'
    if n=='viens-jouer': inner+=f'<div style="position:absolute;left:20px;top:9.6px;width:14px;height:1.4px;background:{G}"></div>'
    job(f'twitch/panneau-{n}',160,50,2,inner)
# Instagram : post annonce + story
job('instagram/post-logo',180,225,6,photo(CG,'center 60%',.62)+f'<div style="position:absolute;left:50%;top:36%;transform:translate(-50%,-50%)">{hero(40)}</div><div class="H" style="position:absolute;left:0;right:0;bottom:22px;font-size:34px;text-align:center">Viens seul.</div><div class="m" style="position:absolute;left:0;right:0;bottom:12px;text-align:center;letter-spacing:.5em">getbola.app/sfl</div>'+edge())
job('instagram/story-logo',180,320,6,photo(SI,'center',.5)+f'<div style="position:absolute;left:50%;top:20%;transform:translateX(-50%)">{hero(34,False)}</div><div class="H" style="position:absolute;left:0;right:0;top:64%;font-size:36px;text-align:center">Dimanche.</div><div class="m" style="position:absolute;left:0;right:0;top:77%;text-align:center;letter-spacing:.5em">12 h 30</div>'+edge())
json.dump(JOBS,open('jobs.json','w')); print(len(JOBS))
