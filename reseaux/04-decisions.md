# 04. Les décisions qui te reviennent

## Décidé le 01/11

- **D0** : objectif 150 joueurs, 300 au plus « quand on aura vraiment des terrains ». L'app règle 30 places par dimanche : réglage à revoir avec toi.
- **D1** : validée. Seuls les joueurs qui ont signé la charte apparaissent sur les réseaux.
- **D2** : en attente. Tu crées les comptes et tu me donnes les noms ; je recommande toujours `sundayfiveleague`.
- **D3** : validée. Comptes au nom de la SFL ; BOLA n'apparaît que comme l'appli qui fait les stats et les cartes.
- **D5** : validée. Le direct sur Twitch et YouTube en même temps ; la date de départ, c'est toi qui la fixes.
- **D6** : le tournage par une association partenaire, Poleed ; rôles à définir avec elle.
- **D7** : validée. Presque noir et blanc, avec le bleu SFL en accent, et l'or pour l'univers Pépite d'Or.
- **D8** : validée. Un seul compte TikTok.
- **D12a** : close. La SFL est une association : contrats, comptes pub et autorisations à son nom.
- **D9, D10, D11, D12b** : reportées (« on verra bien » ; la pub, pas avant décembre). Recommandations inchangées.

Tes mots exacts sont en fin de fichier.

---

Quatorze décisions, triées par urgence. Pour chacune : la question, ma recommandation, ce que ça change.

**Pour répondre vite** : écris le numéro et « oui », « non » ou ton choix. Par exemple : « D0 4 terrains, D6 oui, D5 le 15/11 ». Sans réponse, on part sur la recommandation pour ce qui ne coûte rien et se défait facilement ; on attend ton oui pour le reste (comptes, argent, contrats, droit).

| # | Urgence | Question courte | Ma recommandation | Statut |
|---|---|---|---|---|
| D0 | Cette semaine, avant toute pub | Combien de joueurs la ligue peut-elle faire jouer ? | Objectif 150 joueurs, 300 au plus avec plus de terrains ; l'app règle 30 places par dimanche : à revoir avec toi ; pas de pub au-delà des places réelles | Validée 01/11 (objectif) ; places de l'app en attente de Sabri |
| D1 | Chaque dimanche filmé | Avec quel accord on filme et on diffuse ? | Seuls les joueurs qui ont signé la charte (autorisation E3) apparaissent ; mineurs : le direct seulement, avec l'accord des parents | Validée 01/11 |
| D2 | Avant le 8/11 | Quel nom pour les comptes ? | `sundayfiveleague`, sinon `sundayfive_league` ; `sfl_lille` réservé en protection | En attente de Sabri (il crée les comptes) |
| D3 | — | Quelle marque se voit : SFL ou BOLA ? | Comptes au nom de la SFL ; BOLA seulement comme l'appli des stats et des cartes | Validée 01/11 |
| D4 | — | Le 1er novembre, J1 ou J4 ? | **J4**, d'après le code | Close |
| D5 | Avant le 1er direct YouTube | Le direct : Twitch seul ou Twitch + YouTube ? | Twitch et YouTube en simultané, dès que Sabri fixe la date | Validée 01/11 ; date en attente de Sabri |
| D6 | Cette semaine | Qui fait quoi, et quel rythme ? | Le niveau **Minimum** ; le tournage par l'association partenaire (Poleed), rôles à définir avec elle | En attente de Sabri |
| D7 | — | Quelle identité visuelle sur les réseaux ? | Presque noir et blanc, le bleu SFL `#3D9BFF` en accent, l'or seulement pour la Pépite d'Or ; le Studio = le mur déjà budgété | Validée 01/11 (avec le bleu) |
| D8 | — | Un ou deux comptes TikTok ? | Un | Validée 01/11 |
| D9 | Avant le 1er format star | Comment on traite les stars ? | Top 10 vérifié le 2/11, contrat par cycle, Ilyes ne saisit pas ses matchs | Reportée |
| D10 | Avant la prochaine facture sponsor | On corrige l'offre sponsors ? | D'abord : qui a signé quoi ? Ensuite seulement, corriger | Reportée |
| D11 | Novembre | Quels outils payer ? | Les outils gratuits d'abord ; 2 disques | Reportée |
| D12a | — | Association ou SAS ? | **Association** : tout se fait au nom de l'association SFL | Close |
| D12b | Pas avant décembre | Budget pub ? | Palier 0 par défaut | Reportée (pas avant décembre) |

---

## D0. Combien de joueurs la ligue peut-elle faire jouer ?

**Ta précision (02/11)** : « on a vraiment 100 places ». Lu comme : 100 places par dimanche. Avec ~150 inscrits, et tout le monde ne venant pas chaque dimanche, ça tient. Le réglage de l'app (`TERRAINS_MAX = 2`, 15 par terrain, soit 30 places, `SFL/src/lib/sfl/equipes-division.ts`) est à mettre à jour : 100 places, c'est environ 7 terrains de 15.

**Ce que dit le code.** `TERRAINS_MAX = 2` et `maxParTerrain: 15` (`SFL/src/lib/sfl/equipes-division.ts`, commit du 29/10, « À CONFIRMER PAR SABRI ») : **30 places par dimanche**. Au-delà, les joueurs restent remplaçants, dans l'ordre d'arrivée. Avec 2 terrains, des divisions voisines jouent ensemble (sous 8 joueurs, une division rejoint sa voisine).

**Ta décision (01/11).** La SFL vise **150 joueurs**. **300 au maximum**, « quand on aura vraiment des terrains ». Ma lecture : 150 joueurs dans la ligue, et 300 places au plus le jour où les terrains suivent.

**Un réglage de l'app à revoir avec toi.** Les 30 places par dimanche de l'app ne correspondent pas à cet objectif. À 15 par terrain, 150 joueurs le même dimanche demandent 10 terrains, et 300 en demandent 20. Je n'ai pas touché au code : le réglage (`TERRAINS_MAX`, aujourd'hui 2) suit ta réponse, avec ton accord.

**Ce que ça change.**
- L'objectif devient **150 joueurs** ; il remplace « 200 actifs au 24/01 ».
- Un « joueur actif » a joué au moins un dimanche sur les quatre derniers. Avec 30 places, il y a **au plus 120 actifs** (30 × 4), et moins en pratique. Sans plus de places, une partie des 150 reste remplaçante chaque dimanche.
- Tant que l'app règle 2 terrains, les contenus « par division » (Les Cartes, l'Équipe de la semaine) deviennent « par terrain » : au plus 2 matchs par dimanche (un par terrain), donc 2 MVP sauf égalité.
- La pub reste conditionnée à la **capacité réelle d'accueil** : les places par dimanche, à confirmer avec l'app.

**Quatre réponses qu'il me faut, cette semaine.**
1. **Les terrains** : combien de terrains ou de créneaux as-tu pour accueillir les 150, et à partir de quand ? Combien de places par dimanche l'app doit-elle ouvrir ?
2. **Le prix d'un nouveau en cours de saison** (le budget compte 70 € la saison) : je propose un premier dimanche d'essai, puis un prorata.
3. **Le maillot des nouveaux** : les 110 maillots portent nom et numéro. Pour 150 joueurs, il en manque au moins 40 : une réserve à commander ?
4. **La date de la saison 2**, pour lancer les pré-inscriptions du 10/01 au 24/01.

**Ma recommandation.** Viser 150 joueurs, et 300 au plus quand les terrains suivent. Tant que l'app règle 30 places, suivre le **taux de remplissage** (30 sur 30 chaque dimanche) et la **liste d'attente**. Aucune pub au-delà des places réelles (D12b).

---

## D1. Avec quel accord on filme et on diffuse ? (validée le 01/11)

**Ta décision (01/11) : validée.** Seuls les joueurs qui ont signé la charte (l'autorisation E3) apparaissent sur les réseaux. Sans signature, on ne les montre pas : « sinon c'est pas la peine ». Les règles sur les mineurs restent.

**Conséquence pour le direct.** Un joueur qui n'a pas signé ne joue pas sur le terrain filmé ; sinon, ce match ne passe pas en direct. C'est la même règle que pour les mineurs sans l'accord des parents.

**Le constat.** La case « hors de l'app » de l'app ne couvre que la carte et la photo, seulement si elle est cochée, et seulement dans « les vidéos et les visuels que Bola publie » (`consentement.ts`, `politique.tsx`). Elle ne couvre ni la captation, ni le direct, ni les clips, ni les comptes au nom de la SFL. L'inscription est ouverte dès 12 ans. Or l'habillage du live affiche le prénom, la note et la carte de chaque joueur : la CNIL demande un consentement distinct qui nomme les supports et la durée (`02-etude.md` §7).

**Démarrage (1er novembre) : fait / à reprendre pour le 8 novembre.** Je ne sais pas encore ce qui a été fait dimanche : dis-moi combien d'autorisations sont signées. Pour le 8 novembre, on reprend la même méthode, avec la règle validée.
1. Le message aux joueurs la veille (E1) et la pancarte (E2).
2. **L'autorisation E3, signée à la table d'accueil par chaque joueur du terrain filmé, à son arrivée.** Elle couvre le direct, les extraits, les rubriques présentées par un partenaire ; la publicité payante a sa case à part.
3. Qui ne signe pas **n'apparaît pas** : ni dans le live, ni dans un extrait, une story ou un visuel de la SFL.
4. **Mineurs** : aucun extrait, aucune interview, aucun gros plan cette saison. Le direct seulement avec l'accord écrit des deux parents ; sinon, leur match ne passe pas en direct (`05`, A4).
5. **Un seul contact** dans tous les textes : Sabri, à la table d'accueil, et une adresse de contact réelle.
6. **Un seul registre des accords**, tenu par Sabri (`01-agence.md` §6).

**Et cette semaine.** Une nouvelle version de l'accord de l'app (`VERSION_ACCEPTEE`) : une case « vidéos de match », et « Bola et l'association SFL » nommées toutes les deux. Une ligne dans le règlement de la ligue. Une relecture par un avocat.

**Impact.** Sans ça, chaque clip, Collab ou pub qui montre un joueur est juridiquement exposé. Avec ça, on perd peut-être quelques gros plans, pas la saison.

---

## D2. Quel nom pour les comptes ?

**Ta décision (01/11) : en attente.** Tu crées toi-même les comptes et tu me donnes les noms retenus. Ma recommandation ne change pas.

**Urgence : avant le 8/11**, avant que quelqu'un prenne le nom.

**Ma recommandation.**
- **`sundayfiveleague`, sinon `sundayfive_league`**, identique sur les quatre plateformes (donné à Sabri le 31/10, visuel `reseaux/visuels/sfl-a-faire-avant-dimanche.png`). Pas de point : Twitch n'accepte que lettres, chiffres et tiret bas. Le nom entier se trouve en recherche, « SFL » seul est très pris, et il ne dépend pas d'une ville si la ligue s'étend.
- **`sfl_lille` réservé en protection** sur Instagram et TikTok, sans publier, pour qu'aucun autre compte ne se fasse passer pour la ligue.
- **Nom affiché** : « SFL · Foot à 5 Lille » sur Instagram, TikTok et YouTube (le nom compte dans la recherche). Sur Twitch, le nom affiché ne diffère de l'identifiant que par les majuscules : `SundayFiveLeague`. Le nom affiché se change à tout moment ; l'identifiant, beaucoup moins.
- Type de compte : **Entreprise** sur Instagram et TikTok (musique commerciale, pub, planification).
- Réserver aussi le nom sur Facebook et X, sans les animer. Threads reprend automatiquement l'identifiant Instagram.

**Ce qu'il faut de toi.** Vérifier la disponibilité sur les quatre avant d'en créer un seul, puis créer les comptes, et me dire lesquels tu as créés. **C'est toi qui crées les comptes** : l'agence n'en crée aucun et ne saisit aucun identifiant.

---

## D3. Quelle marque se voit : SFL ou BOLA ? (validée le 01/11)

**Ta décision (01/11) : validée.** Les comptes sont au nom de la SFL. BOLA n'apparaît que comme l'appli qui fait les stats et les cartes.

**Ma recommandation.** **SFL la compétition, BOLA la technologie.** Les comptes sont au nom de la SFL. Les contenus signent « Stats et cartes : BOLA » avec le lien getbola.app.

**Pourquoi.** Le maillot est « SFL » dans l'offre sponsors et « BOLA » dans les maquettes 3D ; l'adresse des sponsors est sur sfl-lille.fr, la story des joueurs finit sur getbola.app. BOLA se dit « un mouvement, pas une institution » ; la SFL est une ligue. Les deux tiennent si chacun garde son rôle.

**Conséquence.** On garde le côté « ligue officielle » qui rassure les sponsors. Pas d'offre sponsors à réécrire pour ce point.

---

## D4. Le 1er novembre, c'était la J4 (close)

Le code tranche : « J4 · Dimanche 1er novembre » (`annonces-ligue.ts`, `api/ligue/annoncer/route.ts`), `DEFIS_DEPUIS = { saison: 1, j: 4 }` (`defis.ts`), divisions `depuis: 4` (`divisions.ts`), et le carrousel `public/actus/j3` existe. **Le 1er novembre = J4, le 24/01 = J16.** Pour les sponsors, on parle de « 13 dimanches filmés ».

**La conséquence.** Les cartes se mettent à jour toutes les 4 journées jouées, comptées depuis la J1 de la saison 1 (`saisie/evolution.ts`, `JOURNEES_PAR_MAJ = 4`). Les **Jours de Verdict** tombent donc après J4 (1/11), J8 (29/11), J12 (27/12) et J16 (24/01), publiés les lundis 2/11, 30/11, 28/12 et 25/01. Lundi 2/11 est le premier, si J1 à J3 ont bien leurs résultats en base : l'app affiche la prochaine mise à jour, un coup d'œil suffit. Un dimanche annulé décale tout.

---

## D5. Le direct : Twitch seul, ou Twitch + YouTube ? (validée le 01/11)

**Ta décision (01/11) : validée sur le principe.** Le direct passe sur Twitch **et** YouTube en même temps. La date de départ n'est pas encore fixée : c'est toi qui la fixes.

**Ma recommandation.**
- **Démarrage (1er novembre)** : Twitch seul était prévu, avec la régie que tu as testée, et un **enregistrement local** en pleine qualité. On ne change pas une régie la veille du lancement.
- **Avant le premier direct YouTube** : activer le direct sur la chaîne YouTube. L'activation peut prendre jusqu'à 24 h.
- **Dès que tu fixes la date, et jusqu'à la fin de la saison 1** : le même flux en simultané sur Twitch et YouTube, en même qualité, après un test. Jusque-là, Twitch seul. Le direct Twitch est promis aux sponsors pour les 13 dimanches.
- **Environ un mois après le premier direct simultané** (6/12 indicatif, à recaler sur la date que tu fixes) : le point d'étape décide seulement où mettre la modération et les animations (le Flair, le banc), et prépare le choix de la saison 2.

**Pourquoi.** Twitch apporte presque aucune découverte à une petite chaîne et efface ses archives en 7 à 14 jours. YouTube garde tout et fait découvrir. Twitch autorise le simultané si on ne renvoie pas les spectateurs ailleurs (`02-etude.md` §4 et §5).

**À vérifier sur place.** Le débit montant du terrain : environ 6 Mb/s par flux 1080p60 (estimation). Pour deux plateformes, soit le double, soit un service qui relaie. Le budget a déjà une ligne « Diffusion sur plusieurs réseaux, 3 × 20 € » : elle sert à ça (Restream ou équivalent, prix à revérifier sur la page officielle). Un plugin OBS à installer, c'est ton accord d'abord.

---

## D6. Qui fait quoi, et quel rythme ?

**Ta décision (01/11).** La production (le tournage) sera assurée par une **association partenaire**, **Poleed**, avec qui la SFL fait un partenariat. Elle fournit de quoi tourner. Les rôles exacts sont à définir avec elle. Statut : en attente.

**Le constat.** L'équipe réelle compte une à trois personnes, toi compris, et tu organises aussi la ligue. Le budget n'a ni monteur ni commentateur (2 bénévoles), alors que le commentateur est promis aux sponsors. **Ce tableau est le seul qui fait foi** ; `01` et `03` y renvoient.

| Niveau | Équipe (estimation) | Instagram (fil) | TikTok | YouTube | Twitch |
|---|---|---|---|---|---|
| **Minimum** | Toi + 1 personne le dimanche ; toi 5 à 8 h par semaine | 3/sem. : L'Action, Les Cartes (ou Jour de Verdict), Le Top 5 ; stories du dimanche | 3/sem. | Live + Résumé court (3 à 5 min) + 1 à 2 Shorts | Live |
| **Recommandé** | 3 personnes le dimanche + 1 monteur 4 à 6 h le lundi | 5/sem. : + Portrait, La Course ; 1 Trial Reel | 5 à 6/sem. | Live + Résumé + 3 Shorts | Live + commentateur |
| **Complet** | Le recommandé + 1 personne pour les stars et la communauté + 1 animateur | 6 à 7/sem. : + Venu seul, Défi Pépite ; 2 Trial Reels | 7/sem. | + Défi Pépite tous les 15 jours, podcast mensuel | + le banc, l'After |

**Dû aux sponsors, à tous les niveaux** (offre du 23/10) : le Résumé « présenté par » (Principal), le Top 5 ou le Portrait du MVP « à votre nom » (Officiel), le logo et le spot mi-temps dans le live, le nom cité au live (Partenaire), 1 vidéo par mois (Principal), et jusqu'à **5 « publications SFL » par mois** (1 Partenaire + 2 par place Officiel). Au Minimum, ces 5 publications pèseraient près de 40 % du fil : voir D10.

**Ce qui allège.**
- Par défaut, un Résumé court, monté à partir des marqueurs posés pendant le live, avec une seule miniature.
- Le visuel de chaque joueur montré : la story « Ton dimanche » que l'app génère déjà pour tous (`story-dimanche.ts`). Y ajouter le compte SFL à côté de getbola.app dès que D2 est choisi.
- Les clips faits à la main restent réservés aux 3 à 5 joueurs mis en avant.
- Un export CSV de l'admin (classement, feuilles, titres, accords) éviterait que tu recopies tout chaque lundi : à ajouter à l'app.

**Ma recommandation.** Le **Minimum** tant que les rôles n'ont pas de noms ; le Recommandé si tu les trouves. Mieux vaut un rythme tenu 13 dimanches qu'un rythme lâché à la J6.

**Ce qu'il faut de toi.**
- Le nom exact de l'association partenaire, et ce qu'elle fournit : du matériel, des personnes, ou les deux.
- Un accord écrit avec elle : à qui sont les images, qui les publie, qui fait signer les autorisations (D1).
- Les noms : la régie, le commentateur, le bord terrain, le monteur, la personne qui publie et modère, l'animateur des formats stars. Certains rôles peuvent revenir à l'association.

---

## D7. Quelle identité visuelle sur les réseaux ? (validée le 01/11, avec le bleu)

**Ta décision (01/11) : validée, avec une modification.** Une DA presque noir et blanc, **avec du bleu** : « même si on joue en noir et blanc, tu rajoutes du bleu ». Et l'or pour l'univers Pépite d'Or.

**Les deux options de départ.**
- **SFL « bleu nuit »** des brochures sponsors : fond `#05080F`, accent bleu `#3D9BFF`, polices Saira Condensed et Barlow.
- **BOLA « nuit »** de l'app : Noir Nuit `#08090B`, Blanc Craie, Gris Béton ; Inter et Anton ; l'or, le rouge et le bleu réservés aux cartes à titre.

**Ma recommandation, après ta décision.** **La nuit BOLA, presque noir et blanc, avec le sigle SFL en signature.**
- Le bleu SFL `#3D9BFF` **n'est plus retiré** : il devient la couleur d'accent de la marque sur les réseaux.
- L'or reste réservé à la Pépite d'Or et à la carte MVP.
- La braise `#FF8A4C` n'est plus la couleur du recrutement : le bleu SFL prend ce rôle (ma lecture de « presque noir et blanc »).
- Les brochures sponsors, déjà en bleu, s'alignent ensuite.

**Point de vigilance.** Le bleu SFL est la couleur de la marque ; le bleu cobalt est celui du titre Défensive gagné, sur la carte. Sur un visuel qui montre une carte Défensive, le bleu SFL reste hors de la carte (texte, cadre), pour qu'on ne lise pas un titre là où il n'y en a pas.

**Trois points en plus.**
- **Le trophée physique de la Pépite d'Or** : tu le choisis ou tu le fais fabriquer ? (Un vrai objet, pas de rendu IA.)
- **Le Studio du dimanche, sans dépense en plus** : le « Mur pour photos et interviews » déjà budgété (220 €). Une face noire unie pour les portraits, sans logo ; l'autre face aux logos des sponsors pour les interviews de 20 s (à prévoir à la commande).
- **Le son** : une signature faite de vrais sons du terrain (sifflet, frappe, filet), enregistrés un dimanche et montés en interne. Gratuit, et cohérent avec « vrai dans l'image ».

---

## D8. Un ou deux comptes TikTok ? (validée le 01/11)

**Ta décision (01/11) : validée.** Un seul compte.

**Ma recommandation.** **Un seul**, avec trois registres : vitrine ~25 %, match ~45 %, vestiaire ~30 %.

**Pourquoi.** Le For You ne dépend pas des abonnés : un registre n'abîme pas l'autre. Deux comptes neufs, c'est deux fois le travail pour deux fois moins de signaux. L'underground le plus crédible viendra des comptes perso des joueurs, qu'on relaie avec leur accord.

**Quand en ouvrir un second.** Au-delà d'environ 2 publications par jour, ou pour un public distinct (un compte de clips du live, par exemple).

---

## D9. Comment on traite les stars ? (reportée)

**Ta décision (01/11) : reportée** (« on verra bien »). Ma recommandation ne change pas.

**Ma recommandation.**
1. **Le casting suit le classement.** Cinq Têtes d'affiche prises dans le top 10 du Pépite d'Or, **vérifié sur l'export du lundi 2/11**. Ton premier choix (Zachary, Junaid, Ilyes, Selim, Abdel) passe pour ceux qui y sont ; sinon, le suivant du classement qui accepte. L'affiche est revue à chaque Jour de Verdict.
2. **Le siège ouvert** : chaque format star oppose une Tête d'affiche à un inconnu (outsider, nouveau, plus grosse montée).
3. **Un contrat écrit par star**, même sous 1 000 €, **pour un cycle de 4 journées** renouvelable : droit à l'image, propriété des contenus, co-crédit, mention « Collaboration commerciale » s'il y a une dotation. (Le contrat serait obligatoire au-delà de 1 000 € HT depuis le 01/01/2026 [à vérifier sur Légifrance : décret d'application de l'art. 8 de la loi 2023-451] ; la recommandation n'en dépend pas.)
4. **Aucun mineur** dans les formats stars.
5. **Ilyes est admin** (`admin.ts` donne l'accès à Ilyes et à Sabri). Je recommande l'option **B** : il est dans les formats stars, mais **il ne saisit ni ne corrige la feuille d'un match qu'il joue** ; l'autre admin le fait. Les équipes sont déjà composées par l'app (cron du vendredi 18 h). Toute correction manuelle, et tout point donné à la main, est publiée avec son motif. La phrase publique : « Ilyes joue, il ne juge pas. » (Option A : il reste hors des formats sponsorisés.)

**Deux réponses qu'il me faut.**
- **L'orthographe exacte** : Junaid ou Jouneid ? Zachary, Zakaria ou Zakary ? Selim ou Selim Laouadi ? Ilyes (pas Ilies) ? Abdel (pas Hassan Abdel) ?
- **« Pitch addict »**, c'est bien le duo Pitch Addict (Victor et Thibault) ?

---

## D10. On corrige l'offre sponsors ? (reportée)

**Ta décision (01/11) : reportée** (« on verra bien »). Tu as relevé le point : l'offre promet un direct Instagram, impossible avant 1 000 abonnés. Ma recommandation ne change pas. Elle colle à D5 : « Twitch et YouTube en direct ».

**D'abord, une question.** **Qui a déjà signé, quelle formule, sur quelle version de l'offre ?** Tant que je n'ai pas la réponse, aucune promesse de l'offre (3 réseaux en direct, vidéos IA, commentateur) ne peut être retirée sans renégociation.

**Un écart à trancher.** L'offre en ligne annonce « Officiel · 2 places » ; le tableau des formules du budget en compte 1, alors que la ligne des maillots du même budget compte « 2 manches (2 sponsors Officiel) ». L'écart vaut 1 300 € de recettes et 2 publications par mois. Je n'ai pas modifié le budget : c'est ton choix (2 dans le budget, ou 1 dans l'offre).

**Ensuite, mes recommandations.**

| Dans l'offre aujourd'hui | Problème | Ma recommandation |
|---|---|---|
| « 3 réseaux en direct : YouTube, Twitch, Instagram » | Le live Instagram demande 1 000 abonnés | « Twitch et YouTube en direct, Instagram et TikTok en clips » |
| TikTok absent | C'est notre 2e plateforme | L'ajouter, en bonus |
| « 1 / 2 publications SFL par mois » | 5 par mois au total, près de 40 % du fil au Minimum | Une rubrique présentée par la marque compte comme une publication (« Le Top 5 · J# présenté par X »), ou une story avec la mention « Publicité » |
| « 1 vidéo IA dédiée par mois », option « Vidéo IA » | Une vidéo IA à côté d'images de match vraies brouille l'offre | La remplacer par un format tourné (un Portrait ou un plan produit au Studio), par cohérence de l'offre |
| Option « Dotation » au MVP | La carte MVP est la seule carte en or | La dotation va au meilleur buteur du mois ou au MVP, mais la photo de remise ne montre jamais la carte MVP ni la Pépite |
| « Logo sur les affiches » | Le prompt de l'affiche du match interdit tout sponsor | Préciser quelles affiches |
| Commentateur cité au live | Absent du budget | Le budgéter ou le retirer |

**Et l'IA dans nos propres images.** La photo de chaque carte BOLA est faite par l'IA (Seedream, `api/photo-studio`), et la politique de confidentialité prévoit déjà de confier cette photo à Magnific pour des vidéos (`politique.tsx`, « Hors de l'app »). L'affiche du match et les couvertures des Actus sont aussi générées. Ma proposition : les images de match et de terrain restent vraies ; la carte est un portrait de marque assumé, signé BOLA. Deux choix te reviennent : garder les cartes IA ou passer aux photos du Studio ; garder ou retirer la phrase sur Magnific.

---

## Coût du plan réseaux, saison 1

Le budget par défaut (`budget/index.html`) fait **10 671 €** avec 10 % d'imprévus. Il est couvert par 100 joueurs × 70 € et 4 600 € de sponsors (Principal, 1 Officiel, Partenaire) : **environ 929 € de marge**, si ces sponsors ont signé. Le plan réseaux n'y est pas. L'objectif de 150 joueurs (D0) n'ajoute des recettes que si les places suivent ; je n'ai pas modifié le budget. Les dépenses et les recettes passent par l'association SFL (D12a).

| Palier | Ce qu'il contient (estimation) | Coût en plus | Ce qui le finance |
|---|---|---|---|
| **0 : organique** | Outils gratuits, multidiffusion et logiciels déjà budgétés, le mur comme Studio, le son du terrain | 0 € | — |
| **≈ 600 €** | 2 disques de 4 To (≈ 200 €), un test de pub de 200 € en décembre, le trophée et les petits frais (≈ 200 €) | ≈ 600 € | La marge, **seulement après la signature d'un sponsor de plus** que le budget par défaut |
| **≈ 2 500 €** | Le palier 600 €, plus la pub de décembre et janvier (≈ 1 600 €) et un outil de planification payant | ≈ 2 500 € | Deux sponsors de plus, ou la 2e place Officiel et des options |

Non chiffrés : l'avocat, un monteur, un commentateur. La structure existe déjà : c'est l'association (D12a). **Ma recommandation : le palier 0 par défaut.**

---

## D11. Quels outils payer ? (reportée)

**Ta décision (01/11) : reportée** (« on verra bien »). Ma recommandation ne change pas : rien n'est payé ni installé sans ton oui.

**Ma recommandation : partir des lignes déjà budgétées.**
- **« Diffusion sur plusieurs réseaux », 3 × 20 €** : le relais Twitch + YouTube (D5).
- **« Disque dur externe 1 To », 80 €** : insuffisant. Les rushs font 100 à 200 Go par dimanche (estimation), soit 1,3 à 2,6 To sur la saison. Prévoir **2 disques de 4 To** (environ 90 à 100 € pièce, estimation), avec ton accord (`05`, C1).
- **« Logiciels », 70 €**, et **« Stockage des vidéos en ligne », 3 × 10 €**.
- **« IA pour monter les vidéos » et « Vidéos générées par IA (Seedance) »** : à arbitrer avec D10.

**Les outils gratuits d'abord** : Meta Business Suite (Instagram), la planification de TikTok Studio sur le web, YouTube Studio, DaVinci Resolve gratuit sur le Mac, CapCut pour les Shorts (fonctions de génération désactivées), Notion gratuit pour le calendrier. **Metricool** (environ 20 à 25 $/mois, prix tiers à vérifier) seulement si la planification à la main ne tient pas.

**Ce qu'il faut de toi.** Un oui outil par outil. Chaque installation et chaque abonnement passe par toi. Le découpage et le recadrage par IA ne génèrent rien, mais ils reposent sur de l'IA : dis-moi si tu les acceptes.

---

## D12a. Association ou SAS ? (close : association)

**Ta décision (01/11) : close.** « Pour l'instant, on est en association, pas en société. » La SFL est une **association**. La question « association ou SAS » ne se pose plus.

**Ce que ça change.**
- Les **factures des sponsors**, les **contrats des stars**, les **autorisations** (E2, E3), les **comptes publicitaires** Meta, TikTok ou Google, et **AdSense** se font au nom de l'association SFL, pas au tien.
- Dans les textes (`05`, E2 et E3), « Sabri [NOM], organisateur de la SFL, et toute structure qu'il créera pour l'organiser » devient : **« l'association SFL ([nom exact de l'association]) »**.
- À compléter : le nom exact de l'association et son numéro (RNA, et SIRET s'il existe).
- BOLA, l'appli, reste à part : le code parle encore du « jour où Bola devient une société ». Ça ne change rien aux comptes de la SFL.

---

## D12b. Le budget pub (validée le 02/11 : palier 1)

**Ta décision (02/11)** : « palier 1, 70 € oui ». Test de 400 € du 1er au 20 décembre (Meta 200 €, TikTok 100 €, Google 100 €), détail dans `07-pub-et-budget.md`. Prix de la saison confirmé : 70 € par joueur.


**Ta décision (01/11) : reportée**, « pas avant décembre ». Ma recommandation ne change pas.

**Les préalables.** La capacité réelle d'accueil (D0 : les places par dimanche, à confirmer avec l'app). La structure est réglée : les comptes pub s'ouvrent au nom de l'association (D12a). On ne paie pas pour recruter des joueurs qui resteront remplaçants.

**Ma recommandation.**
- **Pas de pub en novembre.** On laisse 3 à 4 dimanches à l'organique pour savoir ce qui marche.
- **Palier 0 par défaut** ; le test de 200 € en décembre seulement après un sponsor de plus (tableau ci-dessus).
- **Ciblage** : 18 ans et plus, métropole lilloise, toujours (le DSA interdit la pub ciblée par profilage pour les mineurs).
- **Un Reel n'est boosté que si chaque joueur visible a coché « publicité payante : oui »** sur son autorisation (`05`, E3).
- **Mesure sans traceur** (liens marqués), ce qui respecte la politique actuelle de l'app. On mesure des **inscrits** et la **liste d'attente**, pas des actifs : ceux-là sont plafonnés par les places.

**La question qu'il me faut.** Le prix payé par un joueur : le budget compte 70 € la saison. C'est bien ça ? On le compare au coût d'un inscrit, mesuré au premier test.

---

## Petites questions, quand tu as une minute

- **L'heure de fin d'un dimanche** : le code fait jouer de 12 h 30 à 16 h environ à l'Hippodrome de Marcq (`annonces-ligue.ts`, `convocation-temps.ts`). On filme donc de jour : la direction visuelle suit (`03` §10).
- **« Le » ou « la » Pépite d'Or ?** L'app écrit surtout « le Pépite d'Or » pour le classement (« points au Pépite d'Or »), et « la Pépite d'Or » pour le titre. Je propose de garder les deux : **le** Pépite d'Or, le classement ; **la** Pépite d'Or, le titre et le trophée.
- **Le nombre de mineurs** dans l'effectif, pour savoir combien de matchs risquent de ne pas passer en direct.
- **« SFL Time »** (victoire à +3) : son sens, avant de l'expliquer en public.

---

## Les mots de Sabri, 01/11

Dictés à la voix, en réponse à ce dossier :

> « pour la D1. Donc on va mettre que des joueurs qui ont signé la charte, sinon c'est pas la peine. En D2, le nom des comptes, ben, je vais les créer et je te dirai quel compte j'ai créé. Les comptes sont nom de la SFL. Et voilà, ça apparaît seulement comme l'appli qui fait les stats, exactement. Et du coup, en D5, le direct il passera sur Twitch et sur YouTube en même temps. À partir de quelle date, je ne sais pas encore. Mais pour l'instant, on met en place des zéros. Combien de joueurs par dimanche? Le vrai nombre de places, c'est 300 personnes. Maximum quand on aura vraiment des terrains. Mais sinon, la SFL, elle tend là à avoir 150 joueurs. Qui fait quoi? Ce sera l'association sûrement Polide [Poleed] avec laquelle on va faire un partenariat. Elle va nous fournir de quoi faire un tournage. La SFL, tu peux faire une DA presque noir-blanc, mais rajoute un bleu. On veut quand même, même si on joue en noir et blanc, tu rajoutes du bleu. Avec le délire de pépites d'or et tout, tu vois. La D8, combien de comptes TikTok Marocco? Un seul. Bah oui, ce sera un seul. Pour l'instant, on est en association, pas en société. Donc les stars, ouais, voilà, en D9, en D10, corriger l'offre au sponsor, elle promet un direct Instagram possible avant 1000 abonnés. On verra bien. D11, les outils payants, on verra bien. D12B, le budget pub, pas avant décembre. Voilà, bon, fais ce que je te dis. »

**Les mots incertains, et ma lecture.**
- « la charte » : l'autorisation E3.
- « Les comptes sont nom de la SFL » : « au nom de la SFL ».
- « on met en place des zéros » : sans doute « on met en place les deux » (Twitch et YouTube), sans date.
- « 300 personnes […] 150 joueurs » : 300 places au plus avec assez de terrains ; 150 joueurs dans la ligue.
- « Polide » : le nom de l'association partenaire. Sabri a corrigé le 01/11 : **Poleed**.
- « TikTok Marocco » : non élucidé ; la question portait sur le nombre de comptes TikTok.
