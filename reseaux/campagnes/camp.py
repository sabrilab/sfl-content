import openpyxl
from openpyxl.styles import Font,PatternFill,Alignment
L='https://getbola.app/inscription'
def utm(src,camp,content): return f'{L}?utm_source={src}&utm_medium=paid&utm_campaign={camp}&utm_content={content}'
META=[
('M1 · Il manque 1','reels/03-il-manque-1 (9:16) + posts/07-ton-nom (4:5)',
 "Il manque un joueur dimanche. Foot à 5 dans la métropole lilloise, 12 h 30. Pas besoin d'équipe : tu viens seul, l'app te place. Tes stats, ta carte, ta place au classement.",
 'Il manque 1. Viens seul.','S\'inscrire','il-manque-1'),
('M2 · Ton nom ici','posts/07-ton-nom (4:5) + reels/03-il-manque-1 (9:16)',
 "Ton nom dans le dos, ta carte qui monte chaque dimanche. La Sunday Five League, c'est la ligue de foot à 5 du dimanche de la métropole lilloise. 100 places, tu viens seul.",
 'Ta place t\'attend dimanche.','S\'inscrire','ton-nom-ici'),
('M3 · Le But du Dimanche','reels/01-le-but (9:16), avec une vraie vidéo de but dès qu\'on l\'a',
 "Chaque dimanche, un but devient le But du Dimanche. Le prochain, c'est peut-être le tien. Foot à 5, métropole lilloise. Viens seul.",
 'Le prochain but, c\'est le tien.','En savoir plus','le-but'),
]
TT=[('T1 · Spark Ad du meilleur « But du Dimanche » de novembre','Le TikTok organique qui a le mieux marché en novembre (code d\'autorisation Spark à générer depuis le compte SFL)','Foot à 5 le dimanche, métropole lilloise. Viens seul. #foota5 #sundayfiveleague','le-but-spark'),
('T2 · Spark Ad « Il manque 1. »','Le TikTok « Il manque 1. » publié début décembre','Il manque un joueur dimanche. Viens seul. #foota5','il-manque-1-spark')]
H=['Foot à 5 le dimanche','Viens seul, on te place','La ligue du dimanche','Le five du dimanche','Pas besoin d\'équipe','100 places chaque dimanche','Métropole lilloise','Tes stats, ta carte','Vise la Pépite d\'Or','Inscription en 2 minutes','Sunday Five League','Joue chaque dimanche','Le dimanche, 12 h 30','Rejoins la SFL','70 € la saison']
DSC=['Foot à 5 le dimanche, métropole lilloise. Tu viens seul, l\'app te place.','Tes buts, tes passes et ta carte de joueur, mis à jour après chaque dimanche.','13 dimanches, un classement, une Pépite d\'Or. Inscris-toi sur getbola.app.','Chaque dimanche à 12 h 30. 100 places. 70 € la saison.']
KW=['"foot à 5 lille"','"five lille"','"foot 5 lille"','"foot dimanche lille"','"ligue foot lille"','"match de foot lille"','"futsal lille"','"jouer au foot lille"','[foot a 5 lille]','[five lille]']
NEG=['emploi','recrutement club','urban soccer tarif','location terrain','anniversaire','enfant','école de foot','stage','pro','billet','losc']
for h in H: assert len(h)<=30,(h,len(h))
for d in DSC: assert len(d)<=90,(d,len(d))
wb=openpyxl.Workbook(); ws=wb.active; ws.title='Meta'
W=Font(bold=True,color='FFFFFF'); NO=PatternFill('solid',fgColor='0B0B0B')
def head(w,h):
    w.append(h)
    for c in w[w.max_row]: c.font=W; c.fill=NO
ws.append(['Campagne Meta « Recrutement décembre » · objectif Trafic (vues de la page de destination) · 200 € du 1er au 20/12 (≈ 10 €/jour) · 18–35 ans · métropole lilloise · placements Reels, Stories, fil · français']); ws['A1'].font=Font(bold=True)
head(ws,['Annonce','Visuels du kit','Texte principal','Titre','Bouton','Lien (avec suivi)','Caractères du texte'])
for a,v,t,ti,b,c in META: ws.append([a,v,t,ti,b,utm('meta','recrutement-dec26',c),len(t)])
w2=wb.create_sheet('TikTok'); w2.append(['Campagne TikTok « Spark décembre » · objectif Trafic · 100 € du 1er au 5/12 (20 €/jour, minimum par groupe) · 18–34 ans · région Hauts-de-France, Nord · français']); w2['A1'].font=Font(bold=True)
head(w2,['Annonce','Vidéo','Texte','Lien (avec suivi)'])
for a,v,t,c in TT: w2.append([a,v,t,utm('tiktok','spark-dec26',c)])
w3=wb.create_sheet('Google'); w3.append(['Campagne Google « Recherche foot à 5 Lille » · Réseau de recherche seul · 100 € du 1er au 31/12 (≈ 3,20 €/jour) · CPC max 1 € · métropole lilloise · français']); w3['A1'].font=Font(bold=True)
head(w3,['Type','Texte','Caractères'])
for h in H: w3.append(['Titre (≤ 30)',h,len(h)])
for d in DSC: w3.append(['Description (≤ 90)',d,len(d)])
for k in KW: w3.append(['Mot-clé',k,''])
for n in NEG: w3.append(['Mot-clé négatif',n,''])
w3.append(['Lien final',utm('google','recherche-dec26','rsa'),''])
w4=wb.create_sheet('Suivi décembre'); head(w4,['Date','Plateforme','Annonce','Dépensé (€)','Impressions','Clics','Inscrits (question « Comment as-tu connu la SFL ? »)','Coût par inscrit (€)'])
for r in range(2,32): w4.cell(r,8,f'=IFERROR(D{r}/G{r},"")')
for w in (ws,w2,w3,w4):
    for col in 'ABCDEFGH': w.column_dimensions[col].width=26
    for row in w.iter_rows(min_row=2):
        for c in row: c.alignment=Alignment(wrap_text=True,vertical='top')
ws.column_dimensions['C'].width=60; ws.column_dimensions['F'].width=70; w2.column_dimensions['D'].width=70; w3.column_dimensions['B'].width=80
wb.save('/home/user/sfl-content/reseaux/SFL-campagnes-decembre.xlsx')
import json; json.dump({'META':META,'TT':TT,'H':H,'DSC':DSC,'KW':KW,'NEG':NEG},open('c.json','w'),ensure_ascii=False)
print('ok')
