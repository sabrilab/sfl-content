import sys; sys.path.insert(0,'.')
from tex import *
exec(open('b1.py').read().split("pal=[")[0].split("from tex import *")[1])
CIEL='#8DB8E8'; BRIQ='#9C4A33'; PEL='#4C7A35'; CR='#EEE6D3'
def schema(kind):
    # storyboard géométrique, pas une photo
    if kind=='contre':  # contre-plongée joueur, ciel, immeuble
        return f'<div style="position:absolute;inset:0;background:{CIEL}"></div><div style="position:absolute;right:0;top:30%;width:38%;bottom:0;background:{BRIQ};clip-path:polygon(20% 0,100% 0,100% 100%,0 100%)"></div><div style="position:absolute;left:30%;bottom:0;width:22%;height:78%;background:#16130F;border-radius:40% 40% 0 0"></div>'
    if kind=='large':
        return f'<div style="position:absolute;inset:0 0 55% 0;background:{CIEL}"></div><div style="position:absolute;left:0;right:0;top:30%;height:18%;background:{BRIQ}"></div><div style="position:absolute;inset:48% 0 0 0;background:{PEL}"></div><div style="position:absolute;left:0;right:0;top:70%;height:2px;background:{CR}"></div>'+''.join(f'<div style="position:absolute;left:{x}%;top:56%;width:4%;height:16%;background:#16130F"></div>' for x in (20,45,62,80))
    if kind=='detail':
        return f'<div style="position:absolute;inset:0;background:{PEL}"></div><div style="position:absolute;left:22%;top:38%;width:56%;height:26%;background:#16130F;border-radius:40% 60% 30% 30%"></div><div style="position:absolute;left:30%;top:60%;width:40%;height:4px;background:{CR}"></div>'
    if kind=='maillot':
        return f'<div style="position:absolute;inset:0;background:{BRIQ}"></div><div style="position:absolute;left:24%;top:18%;width:52%;height:66%;background:{CR};clip-path:polygon(0 12%,25% 0,75% 0,100% 12%,100% 35%,82% 35%,82% 100%,18% 100%,18% 35%,0 35%)"></div>'
    if kind=='portrait':
        return f'<div style="position:absolute;inset:0;background:{CIEL}"></div><div style="position:absolute;left:28%;top:22%;width:44%;height:30%;background:#16130F;border-radius:50%"></div><div style="position:absolute;left:14%;top:50%;width:72%;bottom:0;background:#1E3B2C;border-radius:30% 30% 0 0"></div>'
    if kind=='tribune':
        return f'<div style="position:absolute;inset:0 0 50% 0;background:{CIEL}"></div><div style="position:absolute;inset:30% 0 30% 0;background:#C9C1AE"></div>'+''.join(f'<div style="position:absolute;left:0;right:0;top:{32+k*6}%;height:1px;background:#16130F55"></div>' for k in range(6))+f'<div style="position:absolute;inset:70% 0 0 0;background:{PEL}"></div>'
shots=[('contre','01','Le héros','Contre-plongée, joueur debout, ciel bleu franc, un immeuble de brique qui entre dans le cadre.'),
('large','02','Le terrain','Plan large à hauteur d\'homme : ciel, façades, terrain, joueurs petits dans l\'image.'),
('detail','03','Le détail','Crampons, ballon, ligne de craie, au ras de la pelouse. Lumière rasante.'),
('maillot','04','Le maillot','Le maillot SFL accroché, posé, porté de dos (nom, numéro) contre un mur de brique.'),
('portrait','05','Le portrait','Buste, regard caméra, ciel derrière. Le visage net, rien de flou.'),
('tribune','06','Le lieu','L\'Hippodrome de Marcq : tribune, grillage, le ciel au-dessus. Sans joueurs.')]
frames=''.join(f'''<div><div style="position:relative;aspect-ratio:4/5;overflow:hidden;outline:1px solid #16130F33">{schema(k)}<div style="position:absolute;left:6px;top:6px;font:700 8px JetBrains Mono;color:#16130F;background:{CR};padding:2px 4px">{n}</div></div>
<div class="A" style="font-stretch:62%;font-size:15px;margin-top:6px">{t}</div><div style="font-size:11px;color:#5a5246;line-height:1.3">{d}</div></div>''' for k,n,t,d in shots)
rules=[('Lumière','Ciel bleu, soleil de midi ou fin d\'après-midi. Jamais la nuit.'),('Optique','35 mm ou 50 mm. Contre-plongée, ou à hauteur d\'homme.'),('Couleur','Chaude et douce, façon pellicule (Kodak Portra). Un grain léger.'),('Décor','Brique lilloise, immeubles, grillage, tribune. Le vrai lieu.'),('Joueurs','En maillot SFL, seulement ceux qui ont signé la charte.'),('Interdit','Fond studio, flou artistique sur les visages, filtres Instagram.')]
rl=''.join(f'<div style="display:grid;grid-template-columns:70px 1fr;gap:8px;border-top:1px solid #16130F22;padding:6px 0"><span class="A" style="font-stretch:62%;font-size:13px;color:#5E1A24">{a}</span><span style="font-size:12px">{b}</span></div>' for a,b in rules)
html=f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>
<div style="position:absolute;inset:0">{papier(600,2000)}</div><div class="w">
<div class="k">SFL · V2 · <span style="color:#5E1A24">la direction photo</span></div>
<div><div class="A" {A(125,40)}>La touche</div><div style="display:flex;align-items:baseline;gap:10px"><span class="S" style="font-size:40px;line-height:.9">du</span><span class="A" {A(62,40,"color:#0F5A43")}>photographe</span></div>
<p style="color:#5a5246;margin-top:8px;max-width:62ch">Ciel bleu, bâtiments, joueurs. Six plans à refaire chaque dimanche. Ici, des schémas de cadrage (pas des photos) : les vraies images viendront de Poleed, ou de toi.</p></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px 10px">{frames}</div>
<div>{rl}</div>
<div class="k" style="display:flex;justify-content:space-between"><span>Sunday Five League · V2 photo</span><span>Schémas de cadrage</span></div></div></body></html>'''
open('p3.html','w').write(html)
