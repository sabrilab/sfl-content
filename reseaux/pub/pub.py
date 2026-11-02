import openpyxl
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
wb=openpyxl.Workbook(); ws=wb.active; ws.title='Simulateur'
B=Font(bold=True); W=Font(bold=True,color='FFFFFF'); NO=PatternFill('solid',fgColor='0B0B0B'); IN=PatternFill('solid',fgColor='F2E4E7'); OUT=PatternFill('solid',fgColor='EEE6D3')
ws['A1']='SFL · Simulateur pub (estimations à remplacer par les vrais chiffres après le test)'; ws['A1'].font=Font(bold=True,size=13)
ws['A2']='Cases roses : à modifier. Le reste se calcule.'
hdr=['Campagne','Plateforme','Objectif','Budget (€)','CPM (€)','Taux de clic','Taux d\'inscription','Impressions','Clics','Inscrits','Coût par inscrit (€)']
ws.append([]); ws.append(hdr)
for c in ws[4]: c.font=W; c.fill=NO
data=[('Recrutement Reels (Lille, 18-35)','Meta (Instagram)','Inscriptions',200,9,0.008,0.08),
('Spark Ads : le meilleur TikTok de la semaine','TikTok','Inscriptions',100,6,0.007,0.05),
('Recherche « foot à 5 Lille »','Google Search','Inscriptions',100,None,None,0.10),
('Pré-inscriptions saison 2 (janvier)','Meta (Instagram)','Liste d\'attente',300,9,0.008,0.10)]
r=5
for d in data:
    ws.cell(r,1,d[0]); ws.cell(r,2,d[1]); ws.cell(r,3,d[2])
    for k,v in enumerate(d[3:]):
        c=ws.cell(r,4+k,v); c.fill=IN
    if d[1]=='Google Search':
        ws.cell(r,5,'CPC 0,80 €'); ws.cell(r,6,0.8); ws.cell(r,6).fill=IN; ws.cell(r,6).number_format='0.00 "€/clic"'
        ws.cell(r,8,'—'); ws.cell(r,9,f'=D{r}/F{r}')
    else:
        ws.cell(r,8,f'=D{r}/E{r}*1000'); ws.cell(r,9,f'=H{r}*F{r}')
        ws.cell(r,6).number_format='0.0%'
    ws.cell(r,7).number_format='0%'
    ws.cell(r,10,f'=I{r}*G{r}'); ws.cell(r,11,f'=IFERROR(D{r}/J{r},"—")')
    for c in (8,9,10,11): ws.cell(r,c).fill=OUT
    ws.cell(r,8).number_format='# ##0'; ws.cell(r,9).number_format='# ##0'; ws.cell(r,10).number_format='0'; ws.cell(r,11).number_format='0.0'
    r+=1
ws.cell(r,1,'Total').font=B; ws.cell(r,4,f'=SUM(D5:D{r-1})').font=B; ws.cell(r,10,f'=SUM(J5:J{r-1})').font=B; ws.cell(r,11,f'=D{r}/J{r}').font=B; ws.cell(r,11).number_format='0.0'
ws.cell(r+2,1,'Prix de la saison pour un joueur (€)'); ws.cell(r+2,4,70).fill=IN
ws.cell(r+3,1,'Recette des inscrits attendus (€)'); ws.cell(r+3,4,f'=J{r}*D{r+2}'); ws.cell(r+3,4).fill=OUT
ws.cell(r+4,1,'Rentable si le coût par inscrit est sous le prix de la saison').font=Font(italic=True)
for col,w in zip('ABCDEFGHIJK',[44,18,16,11,11,12,15,12,9,9,18]): ws.column_dimensions[col].width=w
# Paliers
w2=wb.create_sheet('Paliers'); w2.append(['Palier','Quand','Pub','Total pub (€)','Condition'])
for c in w2[1]: c.font=W; c.fill=NO
for row in [('0 · organique','Novembre','Aucune : on apprend ce qui marche',0,'Par défaut'),
('1 · test','1er au 20 décembre','Meta 200 € + TikTok Spark 100 € + Google 100 €',400,'Places disponibles le dimanche ; comptes pub au nom de l\'association'),
('2 · saison 2','10 au 24 janvier','Test gagnant ×2 + pré-inscriptions 300 €',900,'Coût par inscrit du test < 70 €'),
('3 · ambitieux','Décembre à janvier','Palier 2 + boosts sponsors (payés par eux)',1500,'Un sponsor de plus signé')]: w2.append(row)
for col,w in zip('ABCDE',[16,20,50,14,60]): w2.column_dimensions[col].width=w
# Calendrier pub
w3=wb.create_sheet('Calendrier pub'); w3.append(['Dates','Plateforme','Campagne','Budget (€)','Visuel du kit'])
for c in w3[1]: c.font=W; c.fill=NO
for row in [('1–20 déc.','Meta','Recrutement : « Il manque 1. » / « Ton nom ici. »',200,'reels/03-il-manque-1 · posts/07-ton-nom'),
('1–5 déc.','TikTok','Spark Ads : le meilleur « But du Dimanche » de novembre',100,'reels/01-le-but'),
('1–31 déc.','Google Search','Mots-clés : foot à 5 Lille, five Lille, foot dimanche Lille, ligue foot Lille',100,'Annonce texte'),
('21 déc.–3 janv.','—','Pause (fêtes)',0,'—'),
('10–24 janv.','Meta + TikTok','Pré-inscriptions saison 2, liste d\'attente',500,'posts/07-ton-nom · reels/05-pepite-or'),
('24 janv.','Meta','Boost de la Nuit de la Pépite (si sponsor)','payé par le sponsor','posts/11-pepite-or')]: w3.append(row)
for col,w in zip('ABCDE',[16,16,62,20,40]): w3.column_dimensions[col].width=w
wb.save('/home/user/sfl-content/reseaux/SFL-budget-pub.xlsx'); print('ok')
