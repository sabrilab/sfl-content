import json,datetime as dt
rows=json.load(open('rows.json'))
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500;700&family=Inter:wght@400;600;700&display=block">'
CSS='''*{box-sizing:border-box;margin:0}body{font:12px/1.35 Inter,sans-serif;color:#0B0B0B;background:#fff}
.A{font-family:Archivo;font-weight:900;text-transform:uppercase;line-height:.86}.S{font-family:"Instrument Serif";font-style:italic;line-height:1}
.M{font:700 9px "JetBrains Mono";letter-spacing:.14em;text-transform:uppercase}.w{padding:36px 40px;display:grid;gap:18px}
.chip{border-radius:3px;padding:5px 6px;margin-bottom:4px;font-size:10.5px;line-height:1.2}
.chip b{display:block;font:800 10.5px Inter}.chip span{font:700 7.5px "JetBrains Mono";letter-spacing:.1em;text-transform:uppercase;opacity:.8}'''
UV={'Compétition':('#0B0B0B','#fff'),'Marque':('#5C1F2A','#EEE6D3'),'Lifestyle':('#EDCFD4','#0B0B0B'),'Terrain':('#4E7140','#fff'),'—':('#E5E5E2','#0B0B0B')}
leg=''.join(f'<span style="display:inline-flex;gap:6px;align-items:center;margin-right:16px"><span style="width:14px;height:14px;border-radius:3px;background:{UV[k][0]};outline:1px solid #0002"></span><b>{n}</b> <span style="color:#666">{d}</span></span>' for k,n,d in [('Compétition','Compétition','noir et blanc'),('Marque','Marque et infos','couleurs sur texture'),('Lifestyle','Lifestyle','noir et blanc + pastel'),('Terrain','Terrain','vraies photos')])
P=['Instagram','TikTok','YouTube','Twitch']
JOURS=['Vendredi','Samedi','Dimanche','Lundi','Mardi','Mercredi','Jeudi']
wd={'Lundi':0,'Mardi':1,'Mercredi':2,'Jeudi':3,'Vendredi':4,'Samedi':5,'Dimanche':6}
# semaine type = semaine du 9 au 15 nov (sans extras)
wk=[r for r in rows if '2026-11-13'<=r[0]<='2026-11-19']
def chip(r):
    bg,fg=UV.get(r[4],UV['—']); return f'<div class="chip" style="background:{bg};color:{fg}"><b>{r[3]}</b><span>{r[1]} · {r[5]}</span></div>'
grid='<div style="display:grid;grid-template-columns:90px repeat(7,1fr);gap:6px">'+'<div></div>'+''.join(f'<div class="A" style="font-stretch:62%;font-size:15px;border-bottom:2px solid #0B0B0B;padding-bottom:4px">{j}</div>' for j in JOURS)
for p in P:
    grid+=f'<div class="A" style="font-stretch:62%;font-size:14px;padding-top:4px">{p}</div>'
    for j in JOURS:
        cell=[r for r in wk if r[2]==p and dt.date.fromisoformat(r[0]).weekday()==wd[j]]
        grid+='<div style="border-top:1px solid #0001;padding-top:4px">'+''.join(chip(r) for r in cell)+'</div>'
grid+='</div>'
html1=f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body><div class="w" style="width:1400px">
<div style="display:flex;justify-content:space-between;align-items:baseline"><div><div class="M" style="color:#888">SFL · calendrier éditorial</div><div class="A" style="font-stretch:125%;font-size:42px;margin-top:6px">La semaine type</div></div><div class="S" style="font-size:26px;color:#5C1F2A">du vendredi au jeudi, autour du dimanche</div></div>
<div>{leg}</div>{grid}
<div style="display:flex;gap:30px;font-size:12px;color:#333;border-top:1px solid #0002;padding-top:10px"><span><b>Par semaine</b> : 7 Instagram (fil, Reels, stories), 7 TikTok, 1 Résumé + 2 Shorts YouTube, 1 live Twitch.</span><span><b>Heures</b> : 18 h 30 – 19 h 30 en semaine, à recaler avec les stats après 3 semaines.</span></div>
</div></body></html>'''
open('semaine.html','w').write(html1)
# Mois de novembre
start=dt.date(2026,11,2)
cells=''
for k in range(35):
    d=start+dt.timedelta(k)
    if d.month!=11 and d>dt.date(2026,11,30): 
        if d>dt.date(2026,12,6): break
    rs=[r for r in rows if r[0]==d.isoformat()]
    tag=''
    if d.weekday()==6: tag=f'<span class="M" style="background:#0B0B0B;color:#fff;padding:2px 4px">J{4+((d-dt.date(2026,11,1)).days)//7}</span>'
    if d==dt.date(2026,11,30): tag='<span class="M" style="background:#C9A03A;color:#0B0B0B;padding:2px 4px">Verdict</span>'
    dots=''.join(f'<div style="display:flex;gap:4px;align-items:center;margin-top:2px"><span style="width:8px;height:8px;border-radius:2px;flex:none;background:{UV.get(r[4],UV["—"])[0]};outline:1px solid #0002"></span><span style="font-size:9.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis"><b style="font:700 7px JetBrains Mono">{ {'Instagram':'IN','TikTok':'TI','YouTube':'YO','Twitch':'TW'}.get(r[2],'··') }</b> {r[3]}</span></div>' for r in rs)
    cells+=f'<div style="border:1px solid #0001;padding:6px;min-height:150px;overflow:hidden;{"background:#F6F5F1;" if d.month!=11 else ""}"><div style="display:flex;justify-content:space-between;align-items:center"><span class="A" style="font-stretch:110%;font-size:16px">{d.day}</span>{tag}</div>{dots}</div>'
html2=f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body><div class="w" style="width:1400px">
<div style="display:flex;justify-content:space-between;align-items:baseline"><div><div class="M" style="color:#888">SFL · calendrier éditorial</div><div class="A" style="font-stretch:125%;font-size:42px;margin-top:6px">Novembre 2026</div></div><div class="S" style="font-size:26px;color:#5C1F2A">lancement, J5 à J8, premier Verdict</div></div>
<div>{leg} <span class="M" style="color:#666">IN Instagram · TI TikTok · YO YouTube · TW Twitch</span></div>
<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:4px">{''.join(f'<div class="A" style="font-stretch:62%;font-size:14px">{j}</div>' for j in ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche'])}{cells}</div></div></body></html>'''
open('novembre.html','w').write(html2)
