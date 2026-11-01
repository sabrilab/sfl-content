import base64,re
P='/home/user/SFL/public/'
sig=re.sub(r'<!--.*?-->','',open(P+'bola/sfl.svg').read(),flags=re.S)
def svg(col,h): return sig.replace('#08090B',col).replace('<svg ',f'<svg style="height:{h};width:auto;display:block" ',1)
def b64(p,mime='image/webp'): return f'data:{mime};base64,'+base64.b64encode(open(p,'rb').read()).decode()
cov=lambda n: b64(P+f'actus/couvertures/{n}-1200.webp')
L='/home/user/bola-site/public/ligue/'
card={k:b64(L+k+'.webp') for k in ['souley','gail','sebovic','jouneid','coucoupops']}
CSS='''
:root{--noir:#070707;--craie:#F2F1EC;--gris:#8C8B86;--filet:#2A2A28;--or:#D9B242;--rouge:#E32B33;--def:#3077E8;--bleu:#3D9BFF;
--a:"Anton",Impact,sans-serif;--m:"JetBrains Mono",ui-monospace,monospace;--t:"Inter",sans-serif}
*{box-sizing:border-box;margin:0}body{background:var(--noir);color:var(--craie);font:13px/1.4 var(--t);width:560px}
.w{padding:28px 22px;display:grid;gap:20px}
.k{font:600 9.5px var(--m);letter-spacing:.18em;text-transform:uppercase;color:var(--gris)}
.k b{color:var(--bleu);font-weight:600}
.h{font-family:var(--a);font-size:54px;line-height:.88;text-transform:uppercase}
.h span{color:var(--bleu)}
.p{color:var(--gris);font-size:12.5px;max-width:60ch}
.sec{display:grid;gap:10px}.st{display:flex;justify-content:space-between;border-top:1px solid var(--filet);padding-top:8px}
/* le cadre commun */
.f{position:relative;overflow:hidden;background:var(--noir);outline:1px solid var(--filet)}
.f .ph{position:absolute;inset:0;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.08)}
.f .mk{position:absolute;inset:7px;pointer-events:none;
 background:linear-gradient(var(--gris),var(--gris)) 0 0/9px 1px no-repeat,linear-gradient(var(--gris),var(--gris)) 0 0/1px 9px no-repeat,
 linear-gradient(var(--gris),var(--gris)) 100% 0/9px 1px no-repeat,linear-gradient(var(--gris),var(--gris)) 100% 0/1px 9px no-repeat,
 linear-gradient(var(--gris),var(--gris)) 0 100%/9px 1px no-repeat,linear-gradient(var(--gris),var(--gris)) 0 100%/1px 9px no-repeat,
 linear-gradient(var(--gris),var(--gris)) 100% 100%/9px 1px no-repeat,linear-gradient(var(--gris),var(--gris)) 100% 100%/1px 9px no-repeat}
.f .top{position:absolute;left:14px;right:14px;top:14px;display:flex;justify-content:space-between;align-items:center;font:600 7px var(--m);letter-spacing:.14em;text-transform:uppercase}
.f .meta{font:500 6px var(--m);letter-spacing:.12em;text-transform:uppercase;color:var(--gris)}
.f .ttl{font-family:var(--a);text-transform:uppercase;line-height:.84}
.seal{width:44px;height:44px;border-radius:50%;border:1.5px solid currentColor;display:grid;place-items:center;font-family:var(--a);font-size:17px;position:relative}
.seal:after{content:"";position:absolute;inset:4px;border-radius:50%;border:1px dashed currentColor;opacity:.6}
.r45{aspect-ratio:4/5}.r916{aspect-ratio:9/16}.r169{aspect-ratio:16/9}
.cap{font:600 8.5px var(--m);letter-spacing:.16em;text-transform:uppercase;color:var(--gris);margin-top:6px}
.cap b{color:var(--craie);font-weight:600}
'''
HEAD='<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@500;600;700&display=block"><style>'+CSS+'</style></head><body><div class="w">'
END='<div class="st k"><span>Sunday Five League · Charte réseaux v2</span><span>Maquette, chiffres d\'exemple</span></div></div></body></html>'
def top(right='J4 · 08.11.26'): return f'<div class="top"><span>{svg("#F2F1EC","9px")}</span><span>{right}</span></div>'

# ---------- Planche 1 : le système
sw=[('--noir','#070707','Noir','Le fond. Toujours plat.'),('--craie','#F2F1EC','Craie','Le texte, les titres du quotidien.'),('--gris','#8C8B86','Gris','Les infos en machine.'),
('--bleu','#3D9BFF','Bleu SFL','La marque : un trait, un chiffre, une flèche.'),('--or','#D9B242','Or','Se gagne : MVP, Pépite, Verdict.'),('--rouge','#E32B33','Rouge','Se gagne : Impact.'),('--def','#3077E8','Bleu Défensive','Se gagne : Défensive.')]
pal=''.join(f'<div style="display:grid;grid-template-columns:54px 1fr;gap:10px;align-items:center;border-bottom:1px solid var(--filet);padding:6px 0"><div style="height:34px;background:var({v});outline:1px solid var(--filet)"></div><div><b style="font-family:var(--a);font-size:17px;font-weight:400;text-transform:uppercase">{n}</b> <span class="k" style="margin-left:6px">{h}</span><div class="p" style="font-size:11.5px">{d}</div></div></div>' for v,h,n,d in sw)
p1=HEAD+f'''<div><div class="k">SFL · <b>Charte réseaux v2</b> · direction C + l'or de A</div>
<div class="h" style="margin-top:8px">Le langage<br><span>du dimanche</span></div>
<p class="p" style="margin-top:8px">On part de tes visuels de la J3. Photo en noir et blanc, titre énorme, carte BOLA, ligne en machine, coins de cadrage. Le fond est toujours plat : jamais de dégradé.</p></div>
<div class="sec"><div class="st k"><span>01 · Couleurs</span><span>la couleur se gagne</span></div>{pal}</div>
<div class="sec"><div class="st k"><span>02 · Typo</span><span>trois voix</span></div>
<div style="display:grid;grid-template-columns:1.2fr 1fr;gap:10px">
<div style="border:1px solid var(--filet);padding:12px"><div style="font-family:var(--a);font-size:64px;line-height:.84;text-transform:uppercase">But.</div><div class="k" style="margin-top:8px">Anton · le titre, un mot, énorme</div></div>
<div style="border:1px solid var(--filet);padding:12px;display:grid;gap:8px;align-content:start"><div style="font:600 10px var(--m);letter-spacing:.14em;text-transform:uppercase">N° 01 / 12 · Match 3 · Terrain 1</div><div class="k">JetBrains Mono · les faits</div>
<div style="font:800 14px var(--t)">Inter, pour les phrases.</div><div class="k">Inter · légendes, sous-titres</div></div></div></div>
<div class="sec"><div class="st k"><span>03 · Les signes</span><span>toujours au même endroit</span></div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;text-align:center" class="k">
<div style="border:1px solid var(--filet);padding:12px;display:grid;place-items:center;gap:8px">{svg('#F2F1EC','18px')}<span>Sigle<br>en haut à gauche</span></div>
<div style="border:1px solid var(--filet);padding:12px;display:grid;place-items:center;gap:8px"><div class="seal" style="color:var(--or)">J4</div><span>Sceau<br>de la journée</span></div>
<div style="border:1px solid var(--filet);padding:12px;display:grid;place-items:center;gap:8px"><div class="f" style="width:46px;height:46px;outline:0"><div class="mk"></div></div><span>Coins<br>de cadrage</span></div>
<div style="border:1px solid var(--filet);padding:12px;display:grid;place-items:center;gap:8px"><div style="width:46px;height:4px;background:var(--bleu)"></div><span>Le trait<br>bleu SFL</span></div></div></div>
<div class="sec"><div class="st k"><span>04 · Photos de profil</span><span>Instagram, TikTok, YouTube, Twitch</span></div>
<div style="display:flex;gap:18px;align-items:center">
<div style="width:96px;height:96px;border-radius:50%;flex:none;background:var(--noir);outline:1px solid var(--filet);display:grid;place-items:center">{svg('#F2F1EC','17px')}</div>
<div style="width:96px;height:96px;border-radius:50%;flex:none;background:var(--craie);display:grid;place-items:center">{svg('#070707','17px')}</div>
<div style="width:96px;height:96px;border-radius:50%;flex:none;background:var(--bleu);display:grid;place-items:center">{svg('#070707','17px')}</div>
<p class="p" style="font-size:11.5px">Ma reco : <b style="color:var(--craie)">le noir</b>, partout pareil. Le bleu pour les moments de recrutement.</p></div></div>
<div class="sec"><div class="st k"><span>05 · Les règles</span><span>ce qui fait « SFL » et pas « IA »</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px 14px;font-size:12px">
<span>Fond <b>plat</b>, noir ou photo. Jamais de dégradé.</span><span>Photos de terrain <b>vraies</b>, en noir et blanc.</span>
<span><b>Un</b> titre, <b>un</b> mot si possible.</span><span>La couleur vive seulement quand un titre est <b>gagné</b>.</span>
<span>Les faits en machine : match, terrain, minute.</span><span>La carte BOLA, c'est la signature.</span></div></div>'''+END
open('p1.html','w').write(p1)

# ---------- Planche 2 : le quotidien
rows=[(1,'Souley','412','▲ 2'),(2,'Jouneiid','398','▼ 1'),(3,'Coucoupop\'s','377','▲ 4'),(4,'Ilyes','361','—'),(5,'Abdel','355','▲ 1')]
lst=''.join(f'<div style="display:grid;grid-template-columns:24px 1fr auto 34px;gap:8px;align-items:baseline;border-bottom:1px solid var(--filet);padding:5px 0"><span style="font-family:var(--a);font-size:20px;color:{"var(--or)" if r==1 else "var(--craie)"}">{r}</span><span style="font:800 13px var(--t);text-transform:uppercase">{n}</span><span style="font:600 9px var(--m)">{pts} PTS</span><span style="font:700 8.5px var(--m);color:{"var(--bleu)" if "▲" in a else "var(--gris)"};text-align:right">{a}</span></div>' for r,n,pts,a in rows)
course=f'''<div class="f r45">{top()}<div class="mk"></div>
<div style="position:absolute;left:14px;right:14px;top:34px"><div class="meta">Sunday Five League · Pépite d'Or · après la J4</div><div class="ttl" style="font-size:50px;margin-top:6px">La course</div></div>
<div style="position:absolute;left:14px;right:14px;bottom:16px">{lst}<div class="meta" style="margin-top:6px">9 dimanches restants · verdict le 30.11</div></div></div>'''
but=f'''<div class="f r916"><div class="ph" style="background-image:url({cov('cage-1')})"></div>{top('J4 · 14:23')}<div class="mk"></div>
<div style="position:absolute;left:14px;right:14px;bottom:16px"><div class="ttl" style="font-size:96px">But.</div>
<div style="width:40px;height:4px;background:var(--bleu);margin:8px 0"></div><div style="font:800 13px var(--t);text-transform:uppercase">Jouneiid</div><div class="meta" style="color:var(--craie)">Match 2 · Terrain 1 · Noirs</div></div></div>'''
yt=f'''<div class="f r169"><div class="ph" style="background-image:url({cov('silhouette-1')});right:42%"></div><div class="mk"></div>
<div style="position:absolute;left:14px;top:12px">{svg('#F2F1EC','10px')}</div>
<div style="position:absolute;right:16px;top:14px;bottom:14px;width:36%;display:flex;flex-direction:column;justify-content:space-between">
<div class="meta">Le résumé · S1 · 08.11.26</div><div class="ttl" style="font-size:118px;line-height:.78">J4</div>
<div style="font:800 17px var(--t);text-transform:uppercase;line-height:1">Personne<br>ne lâche.</div></div>
</div>'''
note=f'''<div class="f r916">{top()}<div class="mk"></div>
<div style="position:absolute;left:14px;right:14px;top:36px"><div class="meta">Ta note · Jour de verdict</div><div class="ttl" style="font-size:44px;margin-top:6px">Sebovic<br>monte.</div></div>
<img src="{card['sebovic']}" style="position:absolute;left:50%;top:34%;width:46%;transform:translateX(-50%)">
<div style="position:absolute;left:14px;right:14px;bottom:14px;display:flex;justify-content:space-between;align-items:end">
<div style="font-family:var(--a);font-size:46px;line-height:.8"><span style="color:var(--gris);font-size:28px">77</span> <span style="color:var(--bleu);font-size:24px">→</span> 78</div><div class="meta" style="text-align:right">Viens seul<br>getbola.app</div></div></div>'''
p2=HEAD+f'''<div><div class="k">SFL · <b>Les gabarits du quotidien</b> · chaque semaine</div>
<div class="h" style="margin-top:8px">Noir, blanc,<br><span>un trait de bleu</span></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
<div>{course}<div class="cap"><b>La Course</b> · carrousel 4:5 · jeudi</div></div>
<div>{but}<div class="cap"><b>Le But du Dimanche</b> · Reel, TikTok · dimanche soir</div></div></div>
<div>{yt}<div class="cap"><b>Le Résumé</b> · miniature YouTube 16:9 · lundi 18 h</div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;align-items:start">
<div>{note}<div class="cap"><b>Ta note</b> · story 9:16</div></div>
<div class="p" style="display:grid;gap:10px;font-size:12px;padding-top:4px">
<div><b style="color:var(--craie)">Les cartes du dimanche</b> : tes visuels J3 restent tels quels. C'est le modèle.</div>
<div><b style="color:var(--craie)">Les photos</b> : celles du terrain, en noir et blanc. Ici, des images de ta banque de l'app en attendant celles de Poleed.</div>
<div><b style="color:var(--craie)">Le bleu SFL</b> n'est jamais un fond : un trait, une flèche qui monte, un chiffre.</div>
<div><b style="color:var(--craie)">Une seule idée</b> par image. Le reste en petit, en machine.</div></div></div>'''+END
open('p2.html','w').write(p2)

# ---------- Planche 3 : les grands moments
verdict=f'''<div class="f r45" style="color:var(--craie)">{top('Jour de verdict · 30.11.26')}<div class="mk"></div>
<div style="position:absolute;left:14px;right:14px;top:30px"><div class="ttl" style="font-size:80px;color:var(--or)">Verdict</div><div class="meta" style="margin-top:4px">Les cartes changent · ta carte avant, ta carte après</div></div>
<img src="{card['souley']}" style="position:absolute;left:12%;bottom:12%;width:34%;transform:rotate(-6deg);filter:grayscale(1) brightness(.55)">
<img src="{card['souley']}" style="position:absolute;right:12%;bottom:9%;width:38%;transform:rotate(4deg)">
<div class="seal" style="position:absolute;left:50%;bottom:30%;transform:translateX(-50%);color:var(--or);background:var(--noir)">J8</div>
<div style="position:absolute;left:14px;right:14px;bottom:12px;display:flex;justify-content:space-between" class="meta"><span>Avant</span><span style="color:var(--or)">Après</span></div></div>'''
pepite=f'''<div class="f r916"><div class="ph" style="background-image:url({cov('ombres-1')});opacity:.55"></div>{top('S1 · 24.01.27')}<div class="mk"></div>
<div style="position:absolute;left:14px;right:14px;top:40px"><div class="meta">La nuit de la Pépite</div><div class="ttl" style="font-size:62px;color:var(--or);margin-top:16px">Pépite<br>d'or</div></div>
<div class="seal" style="position:absolute;left:50%;top:52%;transform:translate(-50%,-50%) scale(1.8);color:var(--or)">S1</div>
<div style="position:absolute;left:14px;right:14px;bottom:16px"><div style="font:800 15px var(--t);text-transform:uppercase">13 dimanches.<br>Une seule.</div><div class="meta" style="margin-top:6px">Hippodrome de Marcq · en direct sur Twitch et YouTube</div></div></div>'''
banner=f'''<div class="f" style="aspect-ratio:16/4"><div class="ph" style="background-image:url({cov('cage-2')});left:64%"></div><div class="mk"></div>
<div style="position:absolute;left:16px;top:50%;transform:translateY(-50%);display:flex;gap:16px;align-items:center">{svg('#F2F1EC','28px')}
<div><div class="ttl" style="font-size:22px">Le dimanche décide.</div><div class="meta" style="color:var(--craie);margin-top:4px">Foot à 5 · Lille · Marcq · Live chaque dimanche 12 h 30</div></div></div>
<div style="position:absolute;left:64%;top:0;bottom:0;width:4px;background:var(--bleu)"></div></div>'''
p3=HEAD+f'''<div><div class="k">SFL · <b>Les grands moments</b> · l'or entre en scène</div>
<div class="h" style="margin-top:8px">L'or<br><span style="color:var(--or)">se gagne</span></div>
<p class="p" style="margin-top:8px">Quatre fois dans la saison (les Jours de verdict) et un soir (la Pépite d'Or). Même cadre noir, mais le titre passe en or. Le reste de l'année, l'or n'existe que sur les cartes MVP.</p></div>
<div style="display:grid;grid-template-columns:1.12fr 1fr;gap:12px;align-items:start">
<div>{verdict}<div class="cap"><b>Jour de verdict</b> · carrousel 4:5 · 4 lundis</div></div>
<div>{pepite}<div class="cap"><b>La Pépite d'Or</b> · Reel, affiche · 24 janvier</div></div></div>
<div>{banner}<div class="cap"><b>Bannière</b> · YouTube, Twitch · le bleu en un seul trait</div></div>'''+END
open('p3.html','w').write(p3)
