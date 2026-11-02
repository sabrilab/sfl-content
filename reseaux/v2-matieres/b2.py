import sys,base64; sys.path.insert(0,'.')
from tex import *
exec(open('b1.py').read().split("pal=[")[0].split("from tex import *")[1])  # FONTS, CSS, A
def b64(p): return 'data:image/webp;base64,'+base64.b64encode(open(p,'rb').read()).decode()
L='/home/user/bola-site/public/ligue/'
C={k:b64(L+k+'.webp') for k in ['souley','jouneid','coucoupops','gail','sebovic']}
mono=lambda t,col,sz=5: f'<span style="font:700 {sz}px JetBrains Mono;letter-spacing:.14em;text-transform:uppercase;color:{col}">{t}</span>'
def tile(inner,bgtex,w=180,h=225): return f'<div style="position:relative;width:{w}px;height:{h}px;overflow:hidden">{bgtex}{inner}</div>'
def top(col,r): return f'<div style="position:absolute;left:8px;right:8px;top:8px;display:flex;justify-content:space-between;align-items:center">{brode(col,"6px",False)}{mono(r,col,4.6)}</div>'
CR='#EEE6D3'; OR='#D8B04A'
# (a) podium sur cuir bordeaux
pod=lambda img,w,rk,n,p,j: f'<div style="display:grid;justify-items:center;gap:2px"><img src="{img}" style="width:{w}px;display:block;filter:drop-shadow(0 3px 4px rgba(0,0,0,.5))"><div class="A" style="font-stretch:62%;font-size:{9 if rk==1 else 7}px;color:{CR}">{rk} · {n}</div>{mono(f"{p} pts · {j} J",OR if rk==1 else CR,4.2)}</div>'
a=tile(f'''{couture(OR,6,4)}{top(OR,'S1 · après la J4')}
<div style="position:absolute;left:12px;top:22px"><div class="A" style="font-stretch:125%;font-size:17px;color:{CR}">La course</div><div class="S" style="font-size:15px;color:{OR};line-height:1">à la Pépite d'Or</div></div>
<div style="position:absolute;left:8px;right:8px;bottom:14px;display:flex;align-items:flex-end;justify-content:center;gap:6px">{pod(C['jouneid'],40,2,'Jouneiid',398,4)}{pod(C['souley'],62,1,'Souley',412,4)}{pod(C['coucoupops'],40,3,"Coucoupop's",377,3)}</div>''',cuir('#5E1A24',180,225,3))
# (b) classement lignes sur craie
rows=[(1,'souley','Souley',412,4,'▲2'),(2,'jouneid','Jouneiid',398,4,'▼1'),(3,'coucoupops',"Coucoupop's",377,3,'▲4'),(4,'gail','Gaïl',361,4,'—'),(5,'sebovic','Sebovic',355,4,'▲1')]
metal=['#C9A03A','#A9A9A2','#A65A34','#16130F33','#16130F33']
lines=''.join(f'''<div style="display:grid;grid-template-columns:10px 16px 1fr 18px 26px 14px;gap:4px;align-items:center;padding:3px 0;border-bottom:1px solid #16130F1c">
<span class="A" style="font-stretch:100%;font-size:9px;color:{metal[i]}">{r}</span><img src="{C[k]}" style="width:14px;display:block"><span class="A" style="font-stretch:62%;font-size:9.5px">{n}</span>
<span style="font:700 6px Inter;color:#7a7264;text-align:right">{j}<span style="font:700 4.5px JetBrains Mono"> J</span></span><span class="A" style="font-stretch:110%;font-size:9px;text-align:right">{p}</span>{mono(a,"#0F5A43" if "▲" in a else "#7a7264",4.6)}</div>''' for i,(r,k,n,p,j,a) in enumerate(rows))
b=tile(f'''{top('#5E1A24','Classement · J4')}<div style="position:absolute;left:10px;right:10px;top:22px"><div class="S" style="font-size:12px;color:#5E1A24">Classement</div><div class="A" style="font-stretch:125%;font-size:19px">Pépite d'Or</div>
<div style="display:grid;grid-template-columns:10px 16px 1fr 18px 26px 14px;gap:4px;margin-top:7px">{''.join(f'<span style="font:700 4.2px JetBrains Mono;letter-spacing:.12em;color:#7a7264;text-align:{al}">{t}</span>' for t,al in [('#','left'),('','left'),('Joueur','left'),('J','right'),('PTS','right'),('','left')])}</div>{lines}
<div style="margin-top:6px">{mono('Divisions refaites chaque dimanche · verdict le 30.11','#7a7264',4.2)}</div></div>''',papier(180,225))
# (c) les écarts sur maillot vert bouteille
ec=[('Souley',412),('Jouneiid',398),("Coucoupop's",377),('Gaïl',361),('Sebovic',355),('Ilyes',349)]
bars=''.join(f'<div style="display:grid;grid-template-columns:44px 1fr 22px;gap:5px;align-items:center;margin:3px 0"><span class="A" style="font-stretch:62%;font-size:8.5px;color:{CR}">{n}</span><div style="height:7px;background:#ffffff1a;position:relative"><div style="position:absolute;inset:0 {100-(p-320)/(412-320)*100:.1f}% 0 0;background:{OR if i==0 else CR}"></div></div>{mono("tête" if i==0 else f"−{412-p}",OR if i==0 else CR,4.6)}</div>' for i,(n,p) in enumerate(ec))
c=tile(f'''{top(CR,'Les écarts · J4')}<div style="position:absolute;left:10px;right:10px;top:22px"><div class="A" style="font-stretch:125%;font-size:17px;color:{CR}">14 points.</div><div class="S" style="font-size:12px;color:{OR}">L'avance de Souley sur Jouneiid.</div>
<div style="margin-top:12px">{bars}</div>
<div style="margin-top:10px;border-top:1px dashed #EEE6D366;padding-top:6px">{mono('Le duel le plus serré','#EEE6D3aa',4.4)}<div class="A" style="font-stretch:62%;font-size:13px;color:{CR}">Sebovic − Ilyes : 6 pts</div></div></div>''',tissu('#1E3B2C',180,225))
# (d) story ce qu'il te manque, olive
d=tile(f'''{top(CR,'Ta course')}<div style="position:absolute;left:12px;right:12px;top:26%"><div class="S" style="font-size:18px;color:{CR};line-height:1">Il te manque</div><div class="A" style="font-stretch:110%;font-size:52px;color:{CR};line-height:.82">9 pts</div><div class="S" style="font-size:18px;color:{CR};line-height:1">pour passer Ilyes.</div>
<div style="margin-top:14px;display:flex;gap:6px;align-items:center"><img src="{C['sebovic']}" style="width:34px"><div>{mono('Toi · 8e · 340 pts',CR,4.8)}<br>{mono('Prochain match : dim. 12 h 30','#EEE6D3aa',4.4)}</div></div></div>
<div style="position:absolute;left:12px;bottom:14px">{mono('Viens seul · getbola.app',CR,4.8)}</div>''',tissu('#6B6A34',180,320),180,320)
html=f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}.g{{transform-origin:0 0}}</style></head><body>
<div style="position:absolute;inset:0">{papier(600,2000)}</div><div class="w">
<div class="k">SFL · V2 · <span style="color:#5E1A24">la course à la Pépite d'Or</span></div>
<div><div class="A" {A(125,40)}>Les classements</div><div style="display:flex;align-items:baseline;gap:10px"><span class="S" style="font-size:40px;line-height:.9">façon</span><span class="A" {A(62,40,"color:#0F5A43")}>BOLA</span></div>
<p style="color:#5a5246;margin-top:8px;max-width:62ch">Comme dans l'app : le podium avec la carte du n° 1 plus grande, puis les lignes avec la carte en vignette, les journées jouées (J) et les points. On ajoute les écarts, et « ce qu'il te manque » pour chaque joueur.</p></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
<div><div style="transform:scale(1.522);transform-origin:0 0;width:180px;height:225px">{a}</div><div style="height:118px"></div><div class="k">Podium · cuir bordeaux · post 4:5</div></div>
<div><div style="transform:scale(1.522);transform-origin:0 0;width:180px;height:225px">{b}</div><div style="height:118px"></div><div class="k">Classement · craie · post 4:5</div></div>
<div><div style="transform:scale(1.522);transform-origin:0 0;width:180px;height:225px">{c}</div><div style="height:118px"></div><div class="k">Les écarts · maillot vert bouteille · 4:5</div></div>
<div><div style="transform:scale(1.522);transform-origin:0 0;width:180px;height:320px">{d}</div><div style="height:167px"></div><div class="k">Ce qu'il te manque · story olive · 9:16</div></div>
</div>
<div class="k" style="display:flex;justify-content:space-between"><span>Sunday Five League · V2 classements</span><span>Chiffres d'exemple</span></div></div></body></html>'''
open('p2.html','w').write(html)
