# 01. L'agence : qui fait quoi

L'agence, c'est **des agents IA** qui préparent (études, textes, faits, gabarits, calendriers, contrôles) et **des humains** qui filment, montent, publient et décident. Tu es le directeur artistique : rien ne sort sans passer par tes portes de validation.

---

## 1. Ce qu'un agent IA ne peut pas faire

À dire tout de suite, pour ne pas compter dessus :

- **Filmer, être au terrain, tenir un téléphone.** Toute la matière vient des humains.
- **Se connecter aux comptes et publier.** Aucun agent ne crée de compte ni ne saisit d'identifiant. C'est toi, ou la personne que tu désignes, qui publie. Tu crées toi-même les comptes, au nom de la SFL, et tu donnes les noms retenus (`04` D2).
- **Juger une vidéo.** Un agent ne sent pas le rythme d'un montage, la fluidité d'un ralenti, la justesse d'un son, l'émotion d'un but. Il peut relire un texte à l'écran ou vérifier un cadrage sur une image fixe ; le reste, c'est ton œil.
- **Monter.** Il peut proposer les coupes à partir du carnet des temps forts ; le montage reste humain.
- **Générer des images, des vidéos ou du son.** Interdit par ta règle. Les gabarits sont dessinés en code à partir de vraies données (comme le carrousel J3 ou la story « Ton dimanche » de l'app), jamais générés.
- **Lire la base réelle de la ligue.** Les agents n'ont pas accès à Supabase. Ils travaillent sur ce que tu exportes (classement, titres, feuilles, accords). L'admin n'a pas encore d'export CSV : à ajouter à l'app, sinon tu recopies chaque lundi.
- **Voir les statistiques des comptes.** Il faudra que tu exportes les chiffres de TikTok Studio, YouTube Studio, Instagram et Twitch.
- **Répondre en direct** dans le chat ou en DM, négocier avec une star ou un sponsor, signer.
- **Lire certaines sources officielles** : les pages d'aide des plateformes, Légifrance et la CNIL sont bloquées par le réseau de la session. Il faut les autoriser dans les réglages pour qu'un agent les lise.
- **Remplacer un avocat.** Les textes juridiques des agents sont des modèles à faire relire.

---

## 2. Les agents

| Agent | Ce qu'il produit | Ce qu'il lui faut | Quand |
|---|---|---|---|
| **Le Directeur** | Les synthèses, les dossiers de cadrage, la liste des décisions pour toi, le compte rendu court de chaque étape | Les rapports des autres agents, tes réponses | À chaque étape |
| **La Veille** | Les études (algorithmes, formats, concurrence), avec sources datées. Une veille mensuelle de ce qui change | L'accès web (et les domaines officiels autorisés) | Étape 1, puis chaque mois |
| **Le Stratège** | La plateforme de marque, le ton, les piliers, les séries, la charte d'écriture | L'étude, tes choix | Étape 1 |
| **L'Atelier visuel** | Le kit des réseaux (couleurs, typo, emplacement du sigle), les spécifications des gabarits, et les gabarits codés (HTML, SVG ou canvas) qui se remplissent avec les vraies données | Ta direction artistique, les logos, les polices, les vraies photos | Étape 2 |
| **Le Statisticien** | Chaque lundi : les faits de la journée (titres par terrain, écarts, montées, chiffre du jour, duels), le registre de couverture (qui a été montré), le tableau de bord du lundi | L'export du classement et des feuilles depuis l'app | Chaque semaine |
| **La Rédaction** | Légendes, accroches, textes à l'écran, titres et chapitres YouTube, questions d'interview, scripts des formats stars | Les faits du Statisticien, le carnet des temps forts | Chaque semaine |
| **Le Planning** | Le calendrier éditorial de la saison, la feuille de tournage de chaque dimanche, les listes de contrôle | Les décisions, les dates de l'app | Étape 3, puis chaque semaine |
| **Le Média** | Le plan de pub, les paliers de budget, les liens marqués (UTM), le rapport mensuel aux sponsors | Les chiffres des plateformes, ton budget, la capacité réelle d'accueil (places par dimanche) | Étapes 4 et 5 |
| **Le Contrôle** | La relecture de chaque lot avant publication : chiffres vérifiés, orthographe des prénoms, accords signés, liste rouge, mineurs, mention « Publicité », zones sûres, règles de marque | Le lot de la semaine, la liste des accords | Chaque semaine |

**Où ils travaillent.** Dans des sessions Claude Code, sur le dépôt `sfl-content`. Ils écrivent des fichiers texte (markdown, tableaux) et, avec ton accord, des gabarits en code. Ils ne publient rien.

---

## 3. Les humains

Les charges sont des **estimations**.

| Rôle | Ce qu'il fait | Charge | Peut se cumuler avec |
|---|---|---|---|
| **Sabri, directeur artistique** | Décide, valide, crée et possède les comptes (au nom de la SFL), tient le registre des accords, exporte les chiffres, finit les carrousels, gère les stars et les sponsors au début ; organise aussi la ligue | 5 à 8 h par semaine | — |
| **Régie** | OBS, le direct, l'enregistrement local, l'habillage ; les marqueurs à chaque action s'il n'y a pas de noteur | Le dimanche | Noteur |
| **Commentateur** | La voix du live. Promis aux sponsors, absent du budget | Le dimanche | — |
| **Noteur** | Note l'heure de chaque temps fort | Le dimanche | Régie, ou modération du chat |
| **Bord terrain** | Le téléphone à la main, interviews de 20 s, stories, portraits du Studio | Le dimanche | Sabri, quand vous n'êtes que deux (`05` A7) |
| **Monteur** | Le Résumé court (3 à 5 min, depuis les marqueurs), puis les clips des 3 à 5 joueurs mis en avant | 3 à 6 h le lundi | Publication |
| **Publication et communauté** | Publie, répond aux DM et aux commentaires, relaie les stories « Ton dimanche » des joueurs, gère les Collabs | Environ 30 min par jour, plus le dimanche soir | Monteur |
| **Modération du live** | Chat Twitch et YouTube | Le dimanche | Noteur |
| **Animateur** | La voix face caméra du Défi Pépite, du podcast Vestiaire et de l'After | Une demi-journée tous les 15 jours (niveau Complet) | Responsable des stars |
| **Responsable des stars** | Organise les tournages des formats stars, fait signer les contrats | Une demi-journée tous les 15 jours | Sabri au début |
| **Association partenaire Poleed** | La production : elle fournit de quoi tourner, dans le cadre d'un partenariat avec la SFL. Elle peut prendre tout ou partie de la régie, du bord terrain et du montage. Les rôles exacts sont à définir avec elle | À définir avec elle | Régie, Bord terrain, Monteur |
| **Avocat** | Relit les autorisations, le règlement, les contrats de l'association SFL | Ponctuel | — |

**L'équipe.** L'équipe réelle compte une à trois personnes, toi compris. Le tournage passera par l'association partenaire (`04` D6, 01/11) ; tant que ses rôles ne sont pas fixés, on compte sans elle. Le rythme se règle sur l'équipe : le tableau des niveaux de `04-decisions.md` D6 est le seul qui fait foi, et `05` A7 dit quoi faire à deux ou seul.

**La structure.** La SFL est une association, pas une société (`04` D12a, close le 01/11). Les contrats, les comptes pub, les autorisations et AdSense se font au nom de l'association SFL ([nom exact de l'association], [numéro RNA] : à compléter).

**Une règle d'équité.** Les équipes sont composées automatiquement par l'app (vendredi 18 h, révélées à 19 h) ; les admins saisissent les feuilles, et Ilyes ne saisit pas celles des matchs qu'il joue. Ils ne choisissent ni les équipes ni qui passe à l'écran : c'est le classement et le registre de couverture.

**Le registre des accords**, tenu par Sabri, un seul : nom, autorisation papier (et sa case « publicité payante »), accord « hors de l'app », mineur, liste rouge, compte Instagram ou TikTok. Le Contrôle s'y réfère avant chaque lot. Règle validée le 01/11 (`04` D1) : seuls les joueurs qui ont signé la charte apparaissent sur les réseaux ; sans signature, on ne les montre pas. Les règles sur les mineurs restent.

---

## 4. Le workflow du projet

```
   ÉTAPE 0          ÉTAPE 1             ÉTAPE 2             ÉTAPE 3              ÉTAPE 4          ÉTAPE 5
   Démarrage   ──►  Marque et     ──►  Identité visuelle ──► Production et   ──►  Publicité   ──►  Pilotage,
   (1er nov.)       ligne éditoriale    et gabarits          calendrier            et budget        outils, mesure
   (fait)                                                                                         
       │              │                    │                    │                    │                │
   Directeur      Veille, Stratège    Atelier visuel       Planning, Rédaction   Média            Média, Statisticien
   Planning       Directeur           Contrôle             Statisticien          Contrôle         Directeur
       │              │                    │                    │                    │                │
       ▼              ▼                    ▼                    ▼                    ▼                ▼
     [V0]           [V1]                 [V2]                 [V3]                 [V4]             [V5]
   Sabri valide   Sabri valide         Sabri valide         Sabri valide         Sabri valide     Sabri valide
```

Les étapes 3, 4 et 5 se chevauchent : la boucle du dimanche (partie 6) tourne depuis le 1er novembre, pendant que le reste se construit.

**Une étape = un aller-retour court.** Les agents produisent, le Directeur te fait un compte rendu en dix lignes et quelques questions, tu réponds, on passe à la suite.

---

## 5. Tes portes de validation

| Porte | Ce que tu valides | Quand |
|---|---|---|
| **V0** | Le nom des comptes, les accords pour filmer, l'équipe du dimanche (`05` A7) | Démarrage (1er novembre) : fait, sauf le nom des comptes ; à reprendre pour le 8 novembre |
| **V1** | La plateforme de marque (`03`), les décisions (`04`), dont la capacité (D0) et la structure juridique (D12a) | En partie validée le 01/11 ; le reste avant le 8/11 |
| **V2** | Le kit visuel, les gabarits, l'habillage du live, l'identité sonore | Mi-novembre |
| **V3** | Le calendrier de la saison, le premier format star, la charte de modération | Fin novembre |
| **V4** | Le budget pub, l'offre sponsors corrigée | Avant toute dépense ; pas de budget pub avant décembre (D12b) |

**État au 01/11.**
- **V0.** Accords : validé, seuls les signataires de la charte sont montrés (D1). Nom des comptes : en attente, tu crées les comptes et tu donnes les noms ; la recommandation reste @sundayfiveleague (D2). Équipe : le tournage passera par l'association partenaire, rôles à définir avec elle (D6).
- **V1, validé.** Comptes au nom de la SFL, BOLA seulement comme l'appli des stats et des cartes (D3). Direct sur Twitch et YouTube en simultané, date à fixer par toi (D5). DA presque noir et blanc, avec le bleu SFL #3D9BFF en accent et l'or pour la Pépite d'Or (D7). Un seul compte TikTok (D8). La SFL est une association (D12a).
- **V1, capacité (D0).** Objectif : 150 joueurs dans la ligue ; 300 au maximum quand il y aura plus de terrains. Le réglage actuel de l'app (2 terrains, 15 par terrain, soit 30 places par dimanche) ne correspond pas à cet objectif : réglage à revoir avec toi. La pub reste conditionnée à la capacité réelle d'accueil (places par dimanche, à confirmer avec l'app).
- **Reportées** (« on verra bien ») : D9 (stars), D10 (offre sponsors, dont le direct Instagram impossible avant 1 000 abonnés), D11 (outils payants), D12b (budget pub). Les recommandations restent inchangées.
| **V5** | Les outils, le tableau de bord, le premier rapport sponsors | Fin novembre, puis chaque mois |

### La porte de chaque semaine

Chaque lundi, en 15 minutes, tu valides le lot de la semaine. Pour ne pas tout faire remonter :

**Peut partir sans toi** (une fois les gabarits validés) :
- un contenu fait sur un gabarit validé ;
- avec des chiffres vérifiés par le Contrôle ;
- avec des joueurs qui ont signé.

**Passe toujours par toi** :
- un nouveau format, ou un gabarit modifié ;
- tout ce qui touche une star, un sponsor ou de l'argent ;
- un chambrage à la limite, un raté ;
- tout contenu avec un mineur ;
- toute réponse publique à une polémique.

---

## 6. La boucle d'un dimanche

```
 VENDREDI 19 h       SAMEDI            DIMANCHE              DIMANCHE SOIR          LUNDI                 MARDI → JEUDI
 La feuille tombe ─► Teasers ──────►  Live + tournage ────► Rangement + clips ──►  Faits + Résumé ────►  Shorts, Portrait,
                                       + carnet               à chaud                + Cartes              La Course, défi
                                                                                                             │
                                          ◄──────────────── bilan du lundi, réglages ◄──────────────────────┘
```

### Avant le match

| Quand | Quoi | Qui |
|---|---|---|
| Lundi ou mardi | TikTok « Il manque 1. », seulement s'il reste des places pour le dimanche suivant | Publication |
| Vendredi 19 h | Les équipes, composées par l'app à 18 h, sont révélées. Story « La Feuille » | Publication |
| Samedi | Story « Le programme » : à quelle heure passe chaque match (c'est ce qui fait venir les proches sur le live). TikTok « Le Contrat » : le duel de rivaux | Rédaction prépare, Publication publie |
| Samedi | La feuille de tournage du dimanche : quel terrain suivre en vertical (à tour de rôle), quels portraits faire, quelles interviews, quels matchs comptent un mineur sans double accord | Planning |
| Samedi soir | Test de la régie, batteries, place sur les téléphones, autorisations imprimées | Régie, Bord terrain |

### Pendant le match

| Quoi | Qui |
|---|---|
| Le live Twitch et YouTube en simultané (D5), dès que Sabri fixe la date ; l'enregistrement local | Régie (ou l'association partenaire, à définir) |
| Le commentaire, avec « le banc » (une Tête d'affiche qui ne joue pas ce match) quand c'est possible | Commentateur |
| Le carnet des temps forts, à l'heure près | Noteur |
| Le vertical, les interviews de 20 s, les portraits du Studio, les stories | Bord terrain |
| Les autorisations, à la table d'accueil, avant le coup d'envoi | Sabri |
| La modération du chat | Noteur ou Publication |

### Après le match

| Quand | Quoi | Qui |
|---|---|---|
| Dimanche, juste après | Deux copies des rushs, rangées dans l'arborescence (`05-demarrage-48h.md`, C1) | Régie, Bord terrain |
| Dimanche, moins de 2 h après | « Le But du Dimanche » (TikTok), « L'Action » (Reel), un Short à chaud | Bord terrain ou Monteur, puis Publication |
| Dimanche, minuit | Les votes ferment. Story « Minuit. Les votes ferment. » | Publication |
| Lundi matin | Export du classement et des titres depuis l'app, mise à jour du registre des signatures de la charte (autorisation E3, `04` D1), qui fait référence ; en plus, pour information, la liste des accords « hors de l'app » (Admin → Activité → Confidentialité) | Sabri |
| Lundi matin | Les faits de la journée, le registre de couverture | Statisticien |
| Lundi midi | Les légendes, « La Course en 30 s », le titre et les chapitres du Résumé | Rédaction |
| Lundi | Le carrousel « Les Cartes · J# » (gabarit rempli avec les vraies données) | Atelier visuel prépare, Sabri ou Monteur finit |
| Lundi | Relecture du lot : chiffres, prénoms, accords, mineurs, mentions. Le Contrôle refuse tout contenu (carte, extrait, visuel) d'un joueur qui n'a pas signé la charte (autorisation E3, `04` D1) | Contrôle |
| Lundi | **Ta porte de la semaine** (15 min) | Sabri |
| Lundi 18 h | « Le Résumé · J# » sur YouTube | Monteur, puis Publication |
| Lundi soir | Chaque joueur montré a sa story « Ton dimanche » dans l'app ; les 3 à 5 mis en avant reçoivent leur clip | Publication |
| Mardi | « Le Top 5 · J# » (Reel, TikTok, Short) | Monteur, Publication |
| Mercredi | « Portrait » (Instagram), POV ou Vestiaire (TikTok), un Short | Monteur, Rédaction, Publication |
| Jeudi | Carrousel « La Course », « Ta note », « Le Défi Pépite » une semaine sur deux | Atelier, Rédaction, Monteur |
| Jeudi | Le bilan de la semaine : ce qui a marché, ce qu'on change | Statisticien, Directeur |

**Le chemin d'un même but, du terrain à quatre plateformes**

```
 Le but (dimanche 14 h 23)
   ├─ live Twitch / YouTube ............ en direct
   ├─ carnet : « 14:23 T2 M3 BUT *** »
   ├─ vertical (bord terrain) ──► « Le But du Dimanche » TikTok + « L'Action » Reel  (dimanche soir)
   ├─ enregistrement OBS ──────► chapitre du Résumé YouTube                          (lundi 18 h)
   ├─ ralenti + carte du joueur ► « Le Top 5 » Reel, TikTok, Short                   (mardi)
   └─ le buteur reçoit son clip ► il le republie : ses proches découvrent la SFL      (lundi soir)
```

**Un seul fichier maître 9:16** par vidéo : sous-titres incrustés dans la zone sûre commune, sans filigrane ni musique, publié en natif sur YouTube Shorts, Reels et TikTok. Seuls la légende, la couverture et, si on veut, le son changent d'une plateforme à l'autre. Ce sont nos propres images, sans filigrane d'une autre plateforme : les règles d'originalité ne les visent pas (`02-etude.md` §1.1).
