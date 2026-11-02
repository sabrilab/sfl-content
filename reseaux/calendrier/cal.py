import datetime as dt, json
D=dt.date
J={D(2026,11,1):4}
d=D(2026,11,1); n=4
while d<=D(2027,1,24): J[d]=n; d+=dt.timedelta(7); n+=1
VERDICT={D(2026,11,30):'J8',D(2026,12,28):'J12',D(2027,1,25):'J16'}
# (jour, heure, plateforme, série, univers, format, gabarit, contenu)
SEM=[
(4,'19:00','Instagram','La Feuille','Compétition','Story','—','Les équipes de dimanche (l\'app les révèle à 19 h)'),
(5,'11:00','Instagram','Dans le sac','Lifestyle','Post 4:5','posts/14-dans-le-sac','Ce qu\'on prend pour dimanche'),
(5,'18:00','TikTok','Le Contrat','Compétition','Vidéo 9:16','—','Le duel de rivaux de demain, tiré de l\'app'),
(6,'12:30','Twitch','SFL Live · J{j}','Terrain','Live','bannieres/twitch','Le direct (+ YouTube en simultané dès que la date est fixée)'),
(6,'12:30','YouTube','SFL Live · J{j}','Terrain','Live','—','Même flux que Twitch (à activer)'),
(6,'19:00','Instagram','Le But du Dimanche','Terrain','Reel','reels/01-le-but','Le plus beau but de la journée'),
(6,'19:30','TikTok','Le But du Dimanche','Terrain','Vidéo 9:16','reels/01-le-but','Le même but, en moins de 2 h'),
(6,'20:00','YouTube','Short','Terrain','Short','reels/01-le-but','Le but, relié au Résumé'),
(0,'18:00','YouTube','Le Résumé · J{jp}','Terrain','Vidéo 3-5 min','youtube/miniature-resume','Le résumé de la journée'),
(0,'18:30','Instagram','Les Cartes · J{jp}','Compétition','Carrousel 4:5','posts/06-mvp + posts/01-podium','MVP, Impact, Défensive par terrain'),
(0,'19:00','TikTok','La Course en 30 s','Compétition','Vidéo 9:16','—','Le classement dit face caméra'),
(1,'18:30','Instagram','Le Top 5 · J{jp}','Terrain','Reel','—','Les cinq gestes de la journée'),
(1,'19:00','TikTok','Le Top 5','Terrain','Vidéo 9:16','—','Les cinq gestes'),
(1,'19:30','YouTube','Short','Terrain','Short','—','Un geste du Top 5'),
(2,'18:30','Instagram','La tenue / Coulisses','Lifestyle','Post 4:5 ou Reel','posts/13-la-tenue · reels/06-lifestyle','Lifestyle en noir et blanc, touche pastel'),
(2,'19:00','TikTok','POV / Vestiaire','Lifestyle','Vidéo 9:16','reels/06-lifestyle','« POV : t\'es venu seul… »'),
(3,'18:30','Instagram','La Course','Compétition','Carrousel 4:5','posts/02-classement + posts/03-ecarts','Top 10, écarts, duel le plus serré'),
(3,'19:00','TikTok','Ta note / Il te manque','Compétition','Vidéo 9:16','reels/02-il-te-manque','Un joueur et ce qu\'il lui manque'),
(3,'12:00','Instagram','Marque et infos','Marque','Story ou post','posts/07-ton-nom · reels/03-il-manque-1','Recrutement (s\'il reste des places) ou annonce'),
]
rows=[]
start=D(2026,11,2); end=D(2027,1,25)
d=start
def dimanche_suivant(x): return x+dt.timedelta((6-x.weekday())%7)
def dimanche_precedent(x): return x-dt.timedelta((x.weekday()+1)%7)
while d<=end:
    wd=d.weekday()
    fetes = D(2026,12,21)<=d<=D(2027,1,3)
    for (j,h,p,s,u,f,g,c) in SEM:
        if j!=wd: continue
        jn=J.get(dimanche_suivant(d)); jp=J.get(dimanche_precedent(d))
        if '{j}' in s and not jn: continue
        if '{jp}' in s and not jp: continue
        if fetes and u=='Lifestyle' and wd==2: s2='Spécial fêtes'; 
        ss=s.replace('{j}',str(jn)).replace('{jp}',str(jp))
        if d in VERDICT and 'Les Cartes' in ss:
            rows.append((d,h,'Instagram',f'Jour de Verdict · {VERDICT[d]}','Compétition','Carrousel 4:5','posts/08-verdict','Les cartes avant / après, temps fort')); continue
        if d==D(2027,1,24) and 'Live' in ss: c='La Nuit de la Pépite : finale et remise, live long'
        rows.append((d,h,p,ss,u,f,g,c))
    d+=dt.timedelta(1)
# Temps forts et lancement
EXTRA=[
(D(2026,11,2),'—','Tous','Création des comptes','Marque','—','profil/sfl-profil-plaque','@sundayfiveleague partout, photo plaque gravée, bios, bannières'),
(D(2026,11,3),'18:30','Instagram','Lancement : la saison','Marque','Post 4:5','posts/12-annonce-saison','Saison 1, 13 dimanches, Hippodrome de Marcq'),
(D(2026,11,4),'12:00','Instagram','Lancement : le lieu','Terrain','Post 4:5','posts/09-le-lieu','« Ici, tout le monde commence inconnu. »'),
(D(2026,11,5),'12:00','Instagram','Lancement : les trophées','Compétition','Post 4:5','posts/10-trophees-saison','Ce qui se gagne cette saison'),
(D(2026,11,5),'19:30','TikTok','Lancement : il manque 1','Marque','Vidéo 9:16','reels/03-il-manque-1','Recrutement'),
(D(2026,12,6),'—','Interne','Point Twitch / YouTube','—','—','—','Bilan du direct, réglages'),
(D(2027,1,10),'18:30','Instagram','Pré-inscriptions saison 2','Marque','Post 4:5','posts/07-ton-nom','Ouverture de la liste d\'attente (jusqu\'au 24/01)'),
(D(2027,1,17),'19:00','Instagram','J-7 : la Pépite d\'Or','Compétition','Reel','reels/05-pepite-or','« 13 dimanches. Une seule. »'),
(D(2027,1,23),'18:30','Instagram','Veille de finale','Compétition','Post 4:5','posts/11-pepite-or','La nuit de la Pépite d\'Or, demain'),
(D(2027,1,24),'21:00','Instagram','Le vainqueur','Compétition','Post 4:5','posts/11-pepite-or','La Pépite d\'Or de la saison 1, plaque gravée'),
]
rows=[r for r in rows if not (r[0]==D(2026,11,5) and r[3]=='Marque et infos')]
rows+=EXTRA
rows.sort(key=lambda r:(r[0],r[1]))
JOURS=['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
json.dump([[r[0].isoformat()]+list(r[1:]) for r in rows],open('rows.json','w'),ensure_ascii=False)
import openpyxl
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
wb=openpyxl.Workbook(); ws=wb.active; ws.title='Calendrier'
H=['Date','Jour','Heure','Plateforme','Série','Univers','Format','Gabarit du kit','Contenu','Statut']
ws.append(H)
UC={'Compétition':'FFFFFF','Marque':'E8DCC3','Lifestyle':'F2E4E7','Terrain':'DCE9DE','—':'FFFFFF'}
for r in rows:
    ws.append([r[0],JOURS[r[0].weekday()],r[1],r[2],r[3],r[4],r[5],r[6],r[7],'À préparer'])
for c in ws[1]: c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor='0B0B0B')
thin=Side(style='thin',color='DDDDDD')
for row in ws.iter_rows(min_row=2):
    u=row[5].value; fill=PatternFill('solid',fgColor=UC.get(u,'FFFFFF'))
    for c in row: c.fill=fill; c.border=Border(bottom=thin); c.alignment=Alignment(vertical='top',wrap_text=True)
    row[0].number_format='DD/MM/YYYY'
for col,w in zip('ABCDEFGHIJ',[12,10,8,11,26,13,15,30,48,12]): ws.column_dimensions[col].width=w
ws.freeze_panes='A2'; ws.auto_filter.ref=ws.dimensions
w2=wb.create_sheet('Semaine type'); w2.append(['Jour','Heure','Plateforme','Série','Univers','Format','Gabarit'])
for (j,h,p,s,u,f,g,c) in sorted(SEM,key=lambda x:((x[0]-4)%7,x[1])): w2.append([JOURS[j],h,p,s.replace(' · J{j}','').replace(' · J{jp}',''),u,f,g])
for c in w2[1]: c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor='0B0B0B')
for col,w in zip('ABCDEFG',[10,8,11,26,13,15,34]): w2.column_dimensions[col].width=w
w3=wb.create_sheet('Temps forts'); w3.append(['Date','Quoi'])
for a,b in [('02/11','Création des comptes, lancement'),('08/11','J5 · premier dimanche publié'),('30/11','Jour de Verdict (J8)'),('06/12','Point Twitch / YouTube'),('21/12 → 03/01','Fêtes : rythme allégé'),('28/12','Jour de Verdict (J12)'),('10/01 → 24/01','Pré-inscriptions saison 2'),('24/01','La Nuit de la Pépite d\'Or (J16)'),('25/01','Jour de Verdict (J16), bilan de saison')]: w3.append([a,b])
for c in w3[1]: c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor='0B0B0B')
w3.column_dimensions['A'].width=16; w3.column_dimensions['B'].width=50
wb.save('/home/user/sfl-content/reseaux/SFL-calendrier-editorial.xlsx')
from collections import Counter
print(len(rows), Counter(r[2] for r in rows))
