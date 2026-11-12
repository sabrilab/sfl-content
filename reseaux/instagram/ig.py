import base64
K='/home/user/sfl-content/reseaux/kit-v2/'
def im(p): return 'data:image/png;base64,'+base64.b64encode(open(K+p,'rb').read()).decode()
AV=im('profil/sfl-profil-plaque.png')
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500;700&family=Inter:wght@400;500;600;700&display=block">'
CSS='''*{box-sizing:border-box;margin:0}body{width:390px;height:844px;overflow:hidden;font:14px/1.3 Inter,system-ui,sans-serif;color:#000;background:#fff}
.A{font-family:Archivo;font-weight:900;text-transform:uppercase;line-height:.86}.S{font-family:"Instrument Serif";font-style:italic;line-height:1}.M{font:700 9px "JetBrains Mono";letter-spacing:.14em;text-transform:uppercase}
.sb{height:44px;display:flex;justify-content:space-between;align-items:center;padding:0 22px;font-weight:600;font-size:15px}
.ic{width:24px;height:24px;display:inline-block}
.btn{flex:1;background:#EFEFEF;border-radius:8px;text-align:center;font-weight:600;font-size:13px;padding:7px 0}
.tab{position:absolute;left:0;right:0;bottom:0;height:78px;border-top:1px solid #dbdbdb;background:#fff;display:flex;justify-content:space-around;padding-top:12px}
'''
SB='<div class="sb"><span>12:30</span><span style="font-size:12px">●●● 5G ▮</span></div>'
def svgi(path,size=24,fill='none',stroke='#000',sw=2): return f'<svg class="ic" style="width:{size}px;height:{size}px" viewBox="0 0 24 24" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'
HOME=svgi('<path d="M3 11l9-8 9 8v10h-6v-6H9v6H3z"/>'); SEARCH=svgi('<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>'); REEL=svgi('<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M10 9l5 3-5 3z"/>'); SEND=svgi('<path d="M22 3L11 13M22 3l-7 19-4-9-9-4z"/>'); PLUS=svgi('<rect x="3" y="3" width="18" height="18" rx="5"/><path d="M12 8v8M8 12h8"/>')
HEART=svgi('<path d="M12 21s-8-5-8-11a4.5 4.5 0 018-3 4.5 4.5 0 018 3c0 6-8 11-8 11z"/>'); COM=svgi('<path d="M21 12a8 8 0 01-11.6 7.1L4 20l1-4.6A8 8 0 1121 12z"/>'); SAVE=svgi('<path d="M6 3h12v18l-6-5-6 5z"/>')
TAB=f'<div class="tab">{HOME}{SEARCH}{PLUS}{REEL}<img src="{AV}" style="width:26px;height:26px;border-radius:50%;outline:1.5px solid #000;outline-offset:1px"></div>'
GRID=['posts/06-mvp','posts/13-la-tenue','posts/04-le-but','posts/02-classement','posts/12-annonce-saison','posts/14-dans-le-sac','posts/05-dimanche','posts/10-trophees-saison','posts/09-le-lieu']
HL=[('Le principe','#0B0B0B','<span class="A" style="font-stretch:110%;font-size:22px;color:#fff">?</span>'),
('Pépite d\'Or','#0B0B0B',f'<img src="{im("trophees/pepite-or.png")}" style="width:34px">'),
('Viens seul','#0B0B0B','<span class="A" style="font-stretch:125%;font-size:24px;color:#fff">1.</span>'),
('Dimanche','#0B0B0B','<span class="S" style="font-size:22px;color:#fff">dim.</span>'),
('Partenaires','#0B0B0B','<span class="M" style="color:#D8B04A;font-size:8px">SFL ×</span>')]
hl=''.join(f'<div style="display:grid;justify-items:center;gap:5px;width:62px;flex:none"><div style="width:62px;height:62px;border-radius:50%;border:1px solid #dbdbdb;padding:3px"><div style="width:100%;height:100%;border-radius:50%;background:{bg};display:grid;place-items:center;overflow:hidden">{c}</div></div><span style="font-size:11px;text-align:center;line-height:1.15;white-space:nowrap">{n}</span></div>' for n,bg,c in HL)
grid=''.join(f'<div style="aspect-ratio:3/4;background:url({im(g+".png")}) center/cover"></div>' for g in GRID)
profil=f'''{SB}
<div style="display:flex;justify-content:space-between;align-items:center;padding:4px 16px 10px"><span style="font-weight:700;font-size:20px">sundayfiveleague <span style="font-size:13px">▾</span></span><span style="display:flex;gap:18px">{PLUS}<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg></span></div>
<div style="display:flex;align-items:center;gap:18px;padding:0 16px">
<img src="{AV}" style="width:86px;height:86px;border-radius:50%;outline:1px solid #dbdbdb">
<div style="flex:1;display:flex;justify-content:space-around;text-align:center">{''.join(f'<div><b style="font-size:16px">{a}</b><div style="font-size:13px">{b}</div></div>' for a,b in [('9','publications'),('1 248','followers'),('112','suivi(e)s')])}</div></div>
<div style="padding:10px 16px 0;font-size:13.5px;line-height:1.35"><b>SFL · Foot à 5 Lille</b><div style="color:#737373">Ligue sportive</div>
Ligue de foot à 5 du dimanche · Lille · Marcq<br>Pas d'équipe : viens seul. 13 dimanches, une Pépite d'Or.<br>Stats et cartes : BOLA ↓<div style="color:#00376B;font-weight:600">🔗 getbola.app/inscription</div></div>
<div style="display:flex;gap:6px;padding:12px 16px 4px"><span class="btn">Modifier</span><span class="btn">Partager le profil</span><span class="btn" style="flex:none;width:34px">+</span></div>
<div style="display:flex;gap:14px;padding:10px 14px 8px;overflow:hidden">{hl}</div>
<div style="display:flex;justify-content:space-around;border-top:1px solid #efefef;padding:9px 0 7px">{svgi('<rect x="4" y="4" width="16" height="16"/><path d="M4 10h16M4 15h16M10 4v16M15 4v16"/>')}{REEL}{svgi('<circle cx="12" cy="9" r="3"/><path d="M5 20c1-4 4-6 7-6s6 2 7 6"/>',stroke='#8e8e8e')}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2px">{grid}</div>{TAB}'''
post=f'''{SB}
<div style="display:flex;align-items:center;gap:10px;padding:6px 12px"><img src="{AV}" style="width:32px;height:32px;border-radius:50%"><div style="flex:1;font-size:13px"><b>sundayfiveleague</b> et <b>souley</b><div style="font-size:11.5px;color:#262626">Hippodrome de Marcq</div></div><span style="font-weight:700">···</span></div>
<div style="position:relative"><img src="{im('posts/06-mvp.png')}" style="width:390px;display:block"><span style="position:absolute;right:10px;top:10px;background:#000a;color:#fff;font-size:12px;padding:3px 8px;border-radius:12px">1/4</span></div>
<div style="display:flex;justify-content:space-between;padding:10px 12px 4px"><span style="display:flex;gap:14px">{HEART}{COM}{SEND}</span><span style="display:flex;gap:4px;align-items:center">{''.join(f'<span style="width:6px;height:6px;border-radius:50%;background:{"#0095F6" if i==0 else "#c7c7c7"}"></span>' for i in range(4))}</span>{SAVE}</div>
<div style="padding:2px 12px;font-size:13.5px;line-height:1.4"><b>412 J'aime</b><br><b>sundayfiveleague</b> Les cartes de la J4. Souley, carte MVP du terrain 1 : 7 buts, 3 passes. Glisse pour Impact et Défensive →<br><span style="color:#00376B">#foota5 #lille #sundayfiveleague</span>
<div style="color:#737373;margin-top:4px">Afficher les 38 commentaires</div><div style="color:#737373;font-size:11px;margin-top:4px">LUNDI</div></div>{TAB}'''
# story La Feuille
teams=[('Match 1 · Terrain 1','Blancs','Noirs'),('Match 2 · Terrain 1','Blancs','Noirs'),('Match 1 · Terrain 2','Blancs','Noirs'),('Match 2 · Terrain 2','Blancs','Noirs')]
story=f'''<div style="position:absolute;inset:0;background:#0B0B0B"></div>
<div style="position:absolute;left:8px;right:8px;top:50px;display:flex;gap:3px">{''.join(f'<div style="flex:1;height:2px;background:{"#fff" if i<2 else "#ffffff55"};border-radius:2px"></div>' for i in range(4))}</div>
<div style="position:absolute;left:12px;right:12px;top:62px;display:flex;align-items:center;gap:8px;color:#fff"><img src="{AV}" style="width:30px;height:30px;border-radius:50%"><b style="font-size:13px">sundayfiveleague</b><span style="font-size:13px;opacity:.7">2 h</span><span style="margin-left:auto">✕</span></div>
<div style="position:absolute;left:26px;right:26px;top:140px;color:#fff"><div class="M" style="color:#fff;opacity:.7">J7 · dimanche 22.11 · 12 h 30</div><div class="S" style="font-size:38px;margin-top:14px">La</div><div class="A" style="font-stretch:125%;font-size:58px">Feuille</div>
<div style="margin-top:24px">{''.join(f'<div style="display:flex;justify-content:space-between;border-top:1px solid #ffffff33;padding:12px 0"><span class="M" style="color:#fff">{a}</span><span class="A" style="font-stretch:62%;font-size:16px">{b} · {c}</span></div>' for a,b,c in teams)}</div>
<div class="S" style="font-size:20px;margin-top:22px">Ta compo est dans l'app.</div></div>
<div style="position:absolute;left:26px;right:26px;bottom:110px;background:#fff;color:#0B0B0B;border-radius:12px;padding:12px 14px;display:flex;justify-content:space-between;align-items:center"><b>🔗 Voir ta compo</b><span class="M" style="color:#0B0B0B">getbola.app</span></div>
<div style="position:absolute;left:12px;right:12px;bottom:28px;display:flex;gap:10px;align-items:center;color:#fff"><div style="flex:1;border:1px solid #ffffff88;border-radius:22px;padding:10px 14px;font-size:14px">Envoyer un message</div>{svgi('<path d="M12 21s-8-5-8-11a4.5 4.5 0 018-3 4.5 4.5 0 018 3c0 6-8 11-8 11z"/>',stroke='#fff')}{svgi('<path d="M22 3L11 13M22 3l-7 19-4-9-9-4z"/>',stroke='#fff')}</div>'''
PH='data:image/jpeg;base64,'+base64.b64encode(open('/home/user/visuels/photos-magnific/02-terrain.jpg','rb').read()).decode()
reel=f'''<div style="position:absolute;inset:0;background:url({PH}) center/cover"></div>
<div style="position:absolute;left:0;right:0;top:44px;display:flex;justify-content:space-between;padding:0 16px;color:#fff;font-weight:700;font-size:20px;text-shadow:0 1px 3px #0006"><span>Reels</span></div>
<div style="position:absolute;left:18px;right:18px;top:120px;color:#fff;text-shadow:0 2px 8px #0007"><div class="S" style="font-size:26px">et soudain,</div><div class="A" style="font-stretch:125%;font-size:64px">But.</div><div class="M" style="color:#fff;margin-top:6px">Jouneiid · J4 · 14:23</div></div>
<div style="position:absolute;right:12px;bottom:120px;display:grid;gap:18px;justify-items:center;color:#fff;font-size:12px;font-weight:600;text-shadow:0 1px 3px #0008">{''.join(f'<div style="display:grid;justify-items:center;gap:3px">{ic}<span>{t}</span></div>' for ic,t in [(svgi('<path d="M12 21s-8-5-8-11a4.5 4.5 0 018-3 4.5 4.5 0 018 3c0 6-8 11-8 11z"/>',28,stroke='#fff'),'2 431'),(svgi('<path d="M21 12a8 8 0 01-11.6 7.1L4 20l1-4.6A8 8 0 1121 12z"/>',28,stroke='#fff'),'86'),(svgi('<path d="M22 3L11 13M22 3l-7 19-4-9-9-4z"/>',28,stroke='#fff'),'312')])}</div>
<div style="position:absolute;left:14px;right:70px;bottom:96px;color:#fff;font-size:13.5px;text-shadow:0 1px 3px #000a"><div style="display:flex;align-items:center;gap:8px"><img src="{AV}" style="width:30px;height:30px;border-radius:50%"><b>sundayfiveleague</b><span style="border:1px solid #fff;border-radius:6px;padding:2px 8px;font-size:12px;font-weight:600">Suivre</span></div>
<div style="margin-top:8px">Le But du Dimanche · J4. Le prochain, c'est le tien ? Viens seul.</div><div style="margin-top:6px;font-size:12px">♫ Son original · sundayfiveleague</div></div>{TAB}'''
for n,b in [('profil',profil),('post',post),('story',story),('reel',reel)]:
    open(f'{n}.html','w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body style="position:relative">{b}</body></html>')
