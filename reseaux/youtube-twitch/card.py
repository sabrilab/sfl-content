import base64,html as H
CH='data:image/png;base64,'+base64.b64encode(open('/tmp/sflv/l3/chromeT.png','rb').read()).decode()
K='/home/user/sfl-content/reseaux/kit-chrome/'
img=lambda p:'data:image/png;base64,'+base64.b64encode(open(K+p,'rb').read()).decode()
G='#2F7D4E'
CSS='''*{box-sizing:border-box;margin:0}body{width:600px;background:#070707;color:#F4F4F2;font:14px/1.45 Inter,sans-serif}
.w{position:relative;padding:30px 26px 26px;display:grid;gap:14px;overflow:hidden}
.glow{position:absolute;left:50%;top:-120px;width:700px;height:420px;transform:translateX(-50%);background:radial-gradient(closest-side,rgba(255,255,255,.10),transparent)}
.H{font-family:Anton,Impact,sans-serif;text-transform:uppercase;line-height:.86;letter-spacing:-.005em}
.k{font:700 10px Inter;letter-spacing:.32em;text-transform:uppercase;color:#8d8d8a}
.top{position:relative;display:flex;justify-content:space-between;align-items:center}
.pill{font:700 10px Inter;letter-spacing:.2em;text-transform:uppercase;border:1px solid #ffffff33;border-radius:99px;padding:5px 11px;color:#ddd}
.hero{position:relative;display:flex;justify-content:space-between;align-items:flex-end;gap:14px;padding:6px 0 4px}
.prog{display:flex;gap:4px;margin-top:2px}.prog i{flex:1;height:3px;border-radius:2px;background:#ffffff1f}.prog i.on{background:#fff}
.st{position:relative;background:linear-gradient(180deg,#141414,#0e0e0e);border:1px solid #ffffff14;border-radius:16px;padding:14px 16px;display:grid;grid-template-columns:34px 1fr;gap:12px}
.n{width:34px;height:34px;border-radius:50%;border:1px solid #ffffff2e;display:grid;place-items:center;font:400 17px Anton;color:#fff}
.t{font:700 15px Inter;color:#fff}.d{font-size:13px;color:#a9a9a5;margin-top:3px}
.path{display:flex;flex-wrap:wrap;gap:5px;margin-top:7px}.path span{font:600 11.5px Inter;color:#e8e8e5;background:#ffffff0d;border:1px solid #ffffff17;border-radius:7px;padding:3px 8px}
.cp{margin-top:9px;position:relative;background:#000;border:1px solid #ffffff1a;border-radius:10px;padding:11px 12px 11px 12px;font:500 12.5px/1.5 "JetBrains Mono",monospace;color:#f0f0ee;white-space:pre-wrap}
.cp.f:before{content:"FICHIER"}.cp:before{content:"À COPIER";position:absolute;right:10px;top:-8px;background:#070707;padding:0 6px;font:700 8.5px Inter;letter-spacing:.2em;color:#2F7D4E}
.warn{border-color:#e3333355}.warn .n{border-color:#e33;color:#e33}
.end{position:relative;border-radius:16px;padding:16px 18px;background:#F4F4F2;color:#070707;display:flex;justify-content:space-between;align-items:center;gap:14px}
.thumbs{display:flex;gap:6px}.thumbs img{border-radius:8px;border:1px solid #ffffff22;display:block}
'''
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@500;600;700;800&family=JetBrains+Mono:wght@500&display=block">'
def card(num,total,plat,titre,sous,steps,fin,thumbs=''):
    prog=''.join(f'<i class="{"on" if k<int(num) else ""}"></i>' for k in range(int(total)))
    st=''
    for i,s in enumerate(steps):
        t,path,copy=s[:3]; warn=len(s)>3 and s[3]
        p=''.join(f'<span>{H.escape(x)}</span>' for x in path) if path else ''
        st+=f'<div class="st{" warn" if warn else ""}"><div class="n">{i+1}</div><div><div class="t">{H.escape(t)}</div>{f"<div class=path>{p}</div>" if p else ""}{f"<div class='cp{' f' if all(('-' in l or l.endswith('.mp4')) and ' ' not in l for l in copy.splitlines()) else ''}'>{H.escape(copy)}</div>" if copy else ""}</div></div>'
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body><div class="w"><div class="glow"></div>
<div class="top"><img src="{CH}" style="height:26px;filter:drop-shadow(0 3px 6px #000)"><span class="pill">{plat} · mission {num}/{total}</span></div>
<div class="hero"><div><div class="H" style="font-size:64px">{titre}</div><div class="k" style="margin-top:8px;color:#cfcfcb">{sous}</div></div><div class="thumbs">{thumbs}</div></div>
<div class="prog">{prog}</div>{st}
<div class="end"><span class="H" style="font-size:22px">Quand c'est fait</span><span style="font:600 13px Inter;text-align:right">{fin}</span></div></div></body></html>'''
yt=card(1,2,'YouTube','YouTube','@SFLfr · la chaîne',[
('Photo de profil',['Studio','Personnalisation','Branding','Photo'],'profil-sfl-profil-chrome'),
('Bannière',['Branding','Image de bannière'],'youtube-banniere-2560x1440'),
('Filigrane',['Branding','Filigrane vidéo','Toute la vidéo'],'youtube-filigrane'),
('Nom',['Informations de base','Nom'],'SFL · Sunday Five League'),
('Description',['Informations de base','Description'],"La Sunday Five League : la ligue de foot à 5 du dimanche de la métropole lilloise. Tu viens seul, l'app BOLA fait les équipes, compte tes stats et fait évoluer ta carte. 4 mois, une Pépite d'Or.\nLe direct chaque dimanche à 12 h 30, le résumé chaque lundi.\nViens jouer : getbola.app/sfl"),
('Liens',['Informations de base','Liens'],'Viens jouer · getbola.app/sfl\nInstagram · instagram.com/sundayfiveleague\nTwitch · twitch.tv/sflfrance'),
('4 playlists',['Contenu','Playlists','Nouvelle'],'SFL Live\nLe Résumé\nLe Top 5\nLe Défi Pépite'),
('Active le direct (24 h d’attente)',['Créer','Passer au direct','Vérifier le téléphone'],''),
],'Envoie-moi une capture de la chaîne',f'<img src="{img("profil/sfl-profil-chrome.png")}" style="width:56px;height:56px;border-radius:50%"><img src="{img("youtube/banniere-2560x1440.png")}" style="height:56px">')
tw=card(2,2,'Twitch','Twitch','sflfrance · la chaîne',[
('Photo et bannière',['Paramètres','Profil'],'profil-sfl-profil-chrome\ntwitch-banniere-1200x480'),
('Écran hors ligne',['Tableau de bord','Paramètres','Stream','Vidéo hors ligne'],'twitch-hors-ligne-1920x1080'),
('Nom d’affichage',['Paramètres','Profil'],'SFLfrance'),
('Bio',['Paramètres','Profil','Bio'],'La ligue de foot à 5 du dimanche de la métropole lilloise. En direct chaque dimanche à 12 h 30. Viens jouer : getbola.app/sfl'),
('Les 5 panneaux, de 01 à 05',['Ta chaîne','À propos','Modifier les panneaux','+ Image'],'Lien de « Viens jouer » :\nhttps://getbola.app/sfl?utm_source=twitch'),
('Titre et catégorie du direct',['Infos du stream','Sports','Français · Football'],'SFL Live · J6 · la course à la Pépite d’Or'),
('Générique en ouverture',['OBS','Scène d’ouverture','+ Média'],'sfl-generique-logo.mp4'),
('Clé de stream : à toi seul',['Paramètres','Stream'],'',True),
],'Envoie-moi une capture de la chaîne',f'<img src="{img("twitch/banniere-1200x480.png")}" style="height:56px"><img src="{img("twitch/panneau-pepite-or.png")}" style="height:56px">')
open('yt.html','w').write(yt); open('tw.html','w').write(tw)
