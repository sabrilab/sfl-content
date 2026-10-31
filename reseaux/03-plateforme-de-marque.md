# 03. Plateforme de marque des réseaux SFL

**Statut : première proposition, à valider par Sabri.** Rien n'est publié, aucun compte n'est créé.

Les fréquences, durées et parts données ici sont des **choix à tester**, pas des faits. Les faits et leurs sources sont dans `02-etude.md`. Les chiffres de la ligue viennent du code de l'app (`/home/user/SFL`), pas de la base réelle : à revérifier avant publication.

---

## 0. Comment cette proposition a été construite

Trois stratèges ont proposé trois angles :
- **« L'Or du Dimanche »** (premium) : la SFL tenue comme une grande compétition.
- **« Le Feuilleton du Dimanche »** (divertissement) : la SFL comme une série en 13 épisodes.
- **« Viens seul. »** (communauté) : la SFL comme le dimanche de tout le monde.

### La base retenue : « Le Feuilleton du Dimanche »

Pourquoi celle-là :
1. C'est la seule qui couvre **les quatre plateformes** que tu demandes avec des séries nommées et un rendez-vous chaque jour.
2. Elle parle **ta langue**. Dans le code de l'app, tu parles déjà d'« arc 1 », d'« outsider » à « gonfler dans l'actu », de saisons « façon Fortnite ». C'est une logique de série et de personnages.
3. Elle donne une vraie place aux **stars façon Pitch Addict**, sans casser l'équité : c'est le classement qui fait le casting.
4. Ses séries correspondent **une à une** à ce qui est déjà vendu aux sponsors (Résumé, Top 5, Portrait du MVP).

Ses faiblesses : elle risquait de faire de cinq visages la marque, et ta vitrine Instagram y était moins soignée. D'où les greffes.

### Les greffes

| Idée greffée | Vient de | Pourquoi |
|---|---|---|
| Le mythe de la Pépite en cinq règles (l'or est rare, un objet, une course, un calendrier sacré, une lignée) | Premium | Donne le prestige « vitrine » que tu veux sur Instagram, sans budget |
| L'architecture « SFL la compétition, BOLA la technologie » | Premium | Règle la confusion actuelle : maillot « SFL » dans l'offre, « BOLA » dans les maquettes |
| Le Studio du dimanche : le portrait officiel de chaque nouveau joueur | Premium | De belles images vraies pour la grille, le « Portrait du MVP » vendu aux sponsors et le recrutement |
| L'esthétique « hiver de midi » | Premium | La saison se joue dehors, à midi, de novembre à janvier : lumière basse, ciel gris. La contrainte devient la signature |
| La valeur « exigence » et la règle « le sponsor ne touche jamais l'or » | Premium | Le barème récompense déjà la présence à l'heure ; l'or garde son sens |
| Les indicateurs « des joueurs, pas des vues » et le tableau de bord du lundi | Communauté | Ton objectif, ce sont des joueurs ; on les mesure dans la limite des places (§12) |
| « Une tête pour trois visages » et la couverture de tous les joueurs | Communauté | Protège l'équité et fait de 100 joueurs 100 diffuseurs |
| La braise réservée au recrutement (« Il manque 1. ») | Communauté | Une couleur, un sens : orange veut dire « une place pour toi » |
| Le parcours en cinq étapes (voir, se projeter, oser, revenir, ramener) | Communauté | Chaque série a un rôle précis dans le recrutement |
| « Le programme du jour » le samedi, les chapitres du Résumé envoyés en famille, l'Équipe de la semaine par terrain | Communauté | Fait venir les proches sur le live, montre les deux terrains |
| La capacité d'abord | Communauté | 30 places par dimanche dans le code (`04` D0) : ne pas recruter plus vite que la ligue ne peut faire jouer |

Les deux options écartées sont résumées en annexe, pour que tu puisses changer d'avis.

---

## 1. L'idée

La SFL n'a pas d'équipes fixes. Elle a mieux : **cent personnages et un classement qui écrit leur histoire chaque dimanche.**

On ne filme pas des matchs. On tourne une série de 13 dimanches dont le scénario s'appelle **la Pépite d'Or**. Les ligues de créateurs achètent leur public avec des streamers ; la SFL fabrique ses têtes d'affiche avec de vraies stats.

**La règle de forme : lisse dans le cadre, vrai dans l'image.**

---

## 2. La plateforme

- **Mission.** Faire du foot du dimanche un spectacle où n'importe qui, même venu seul, peut devenir quelqu'un.
- **Promesse.** *Ici, tout le monde commence inconnu. Le dimanche décide qui devient quelqu'un.*
- **Appel unique, à la fin de chaque contenu.** *Viens seul.* + getbola.app (lien marqué par plateforme).
- **Valeurs.**
  1. **Vrai.** Chaque chiffre vient de la feuille de match. On ne monte jamais une note pour le spectacle. La justesse des notes est notre premier actif. Les images de match et de terrain sont vraies, jamais générées ni modifiées par IA. La carte BOLA, elle, est un portrait de marque : une illustration assumée, signée BOLA.
  2. **Mérité.** Le classement fait le casting, pas l'agence.
  3. **Ouvert.** Chaque format garde une place pour un inconnu. On peut passer de la D3 à la D1 en un dimanche (`divisions.ts`).
  4. **Exigeant.** Venir, et être à l'heure. C'est déjà dans le barème : un retard coûte un point, trois dimanches à l'heure donnent des crans de PHY.
  5. **Chambreur, mais réglo.** On rit avec les joueurs, jamais d'eux.
- **Personnalité.** Le pote au bord du terrain qui connaît toutes les stats. Il commente avec l'énergie d'un speaker, mais il écrit avec la sécheresse de BOLA : phrases courtes, un point.
- **Les ennemis.**
  - **L'anonymat** : le five du jeudi où ton plus beau but n'existe que dans ta tête.
  - **Le faux** : les comptes de faux scores qui inondent TikTok, les notes gonflées.
  - La tension à raconter : « Personne ne te regarde jouer. » → « Ici, tout est filmé. Tout compte. »

### Le mythe de la Pépite d'Or

Une pépite ne sort pas d'un centre de formation. Elle se trouve dans la boue. Personne ne la reçoit : on la déterre, dimanche après dimanche. Treize dimanches, une seule pépite. Et chaque dimanche, quelqu'un est **trouvé** : un MVP de D3, un défenseur élu « Défensive », un nouveau qui monte.

Cinq règles pour le tenir :
1. **L'or est rare.** Il n'apparaît que quand il est mérité : la Pépite d'Or, la carte MVP. Jamais pour décorer, jamais pour un sponsor. La charte BOLA réserve déjà l'or aux cartes MVP (`SFL/src/app/tokens.css`).
2. **Un objet.** Un trophée réel à photographier, en plus de l'écusson à vie prévu dans l'app. C'est à toi de le choisir ou de le faire fabriquer. Il est là chaque dimanche, sur une table au bord du terrain ; seul le vainqueur le touche.
3. **Une course.** Le classement se raconte comme un championnat de pilotes : écarts, dépassements, dimanches qui restent.
4. **Un calendrier sacré.** L'app compose les équipes, révélées le vendredi à 19 h. On joue le dimanche à 12 h 30. Les votes ferment à minuit. Le classement sort le lundi. La remise a lieu le 24 janvier.
5. **Une lignée.** Les écussons, le Wall of Fame et la saison 0 existent déjà. Chaque vainqueur entre dans une liste qui s'allonge.

---

## 3. SFL la compétition, BOLA la technologie

- **Les comptes sont au nom de la SFL.** La ligue est le héros.
- **BOLA est le fournisseur officiel**, comme une grande ligue affiche « données par… ». Signature des contenus : « Stats et cartes : BOLA », lien getbola.app.
- BOLA garde son ton de « mouvement » dans l'app et sur son site.
- Le nom exact des comptes est une décision à toi (`04-decisions.md`, D2).

---

## 4. « Instagram = lisse » : la réponse

**Juste pour le cadre, faux pour l'image.** (Détail et sources : `02-etude.md` §1.2.)

| Au cordeau (le cadre) | Vrai (l'image) |
|---|---|
| Typo, couleurs, grille, sigle | Les buts filmés à l'iPhone |
| Gabarits de carrousel, cartes BOLA | Les réactions du banc |
| Ouverture et fermeture des vidéos | Les interviews de 20 s |
| Miniatures, couvertures de Reels | Le chambrage d'après-match |
| Bio, stories à la une | Les coulisses |

- Sur la grille Instagram : environ **60 % de vitrine, 40 % de vivant**, monté proprement.
- Le plus brut passe d'abord en **Trial Reels** (montrés aux seuls non-abonnés) et sur TikTok. Seuls les gagnants rejoignent la grille.
- Les pubs très produites, s'il y en a, restent pour plus tard (étape 4).

---

## 5. Ligne éditoriale : cinq piliers

| Pilier | Part | Ce qu'on raconte | Ce que ça sert |
|---|---|---|---|
| **Le Terrain** | 30 % | Buts, gestes, arrêts, résumés | Faire découvrir : « ça joue, et c'est à Lille » |
| **La Course** | 25 % | Classement Pépite, écarts, duels, mouvements D1/D2/D3, Jours de Verdict | Faire revenir, enregistrer, débattre |
| **Les Visages** | 20 % | Têtes d'affiche **et** inconnus : portraits, nouveaux, révélations, formats stars | Faire partager par les joueurs |
| **Le Vestiaire** | 15 % | Le brut : POV, chambrage, coulisses, réactions au téléphone | Montrer le vrai, surtout sur TikTok |
| **La Porte** | 10 % | « Il manque 1. », « Venu seul », mode d'emploi, parrainage | Recruter directement |

**Les rebondissements** existent déjà dans l'app, sans toucher au classement : les **contrats** (« tiens-le », « finis devant lui ») et **le Flair** (pronostics sans argent). Ils donnent de l'XP, jamais des points Pépite.

**Les temps forts de la saison**
- **Les Jours de Verdict** : la mise à jour officielle des cartes, toutes les 4 journées jouées (`saisie/evolution.ts`). Après **J4 (1/11), J8 (29/11), J12 (27/12) et J16 (24/01)**, publiés les lundis 2/11, 30/11, 28/12 et 25/01, si J1 à J3 ont bien leurs résultats en base (`04` D4). Un dimanche annulé décale tout.
- **La Nuit de la Pépite** : la dernière journée, le 24/01/2027. Remise filmée, live long.
- **Les fêtes** : les dimanches du 27/12 et du 3/01 sont dans les 13 promis aux sponsors. Le 27/12 est un Jour de Verdict : on ne l'allège pas. Seule la semaine du 3/01 passe en « Spécial fêtes ».
- **Les pré-inscriptions de la saison 2** : du 10/01 au 24/01, avec la liste d'attente visible (date de la saison 2 : `04` D0).

---

## 6. La semaine type

Le niveau **Recommandé** de `04` D6 (3 personnes le dimanche, un monteur le lundi). **Le tableau des niveaux de D6 est le seul qui fait foi** ; au Minimum, on garde les lignes en gras.

| Jour | Instagram | TikTok | YouTube | Twitch |
|---|---|---|---|---|
| **Vendredi** | Story « La Feuille » à 19 h (les équipes révélées) | — | Post « La Feuille » | — |
| **Samedi** | Story « Le programme » (heures de passage) ; 1 Trial Reel | « Le Contrat » (le duel annoncé) | — | — |
| **Dimanche** | Stories en direct du terrain ; **Reel « L'Action »** ; à minuit, story « Les votes ferment » | **« Le But du Dimanche »**, moins de 2 h après | **« SFL Live · J# »** (même flux) ; 1 Short à chaud | **« SFL Live · J# »** |
| **Lundi** | **Carrousel « Les Cartes · J# »** (la semaine d'un Verdict : « Jour de Verdict ») | **« La Course en 30 s »** ; « Il manque 1. » s'il reste des places | **« Le Résumé · J# »** à 18 h | — |
| **Mardi** | **Reel « Le Top 5 · J# »** | **« Le Top 5 »** ou Vestiaire | Short | — |
| **Mercredi** | « Portrait » | POV ou Vestiaire | Short | — |
| **Jeudi** | Carrousel « La Course » | « Ta note » ou un geste | « Le Défi Pépite » (Complet) | Option : rediffusion commentée par une star |
| **Dû aux sponsors** | Résumé « présenté par », Top 5 ou Portrait « à votre nom », jusqu'à 5 « publications SFL » par mois (`04` D10) | | Résumé « présenté par » | Logo, spot mi-temps, nom cité au live |

Total au Recommandé : 5 publications dans le fil Instagram (L'Action, Les Cartes ou Verdict, Top 5, Portrait, La Course) et 1 Trial Reel ; 5 à 6 TikTok ; 1 Résumé et 3 Shorts ; 1 live. Venu seul et le Défi Pépite s'ajoutent au niveau Complet.

---

## 7. Le rôle de chaque plateforme et ses séries

### Instagram : la vitrine officielle du feuilleton

**Rôle.** Rassurer le joueur qui hésite et le sponsor qui regarde. Circuler en DM.

**Réglages.**
- Compte **Entreprise** (Sound Collection, pub, planification).
- Nom et bio avec « foot à 5 », « Lille », « dimanche » : ils comptent dans la recherche.
- Chaque publication géolocalisée. 5 hashtags au plus.
- Fichiers en 1080×1440 (3:4), l'essentiel dans le 1080×1350 central.
- Chaque publication centrée sur un joueur l'invite en **Collab** (s'il a signé l'accord).
- Pas de live avant 1 000 abonnés ; ensuite, au téléphone (remise du titre du mois : meilleur buteur).

| Série | Format | Quand | Pilier |
|---|---|---|---|
| **L'Action** | Reel 10 à 25 s, la carte du joueur en dernière image | Dimanche soir | Terrain |
| **Les Cartes · J#** | Carrousel : MVP, Impact, Défensive **par terrain** (2 terrains, des divisions qui jouent parfois ensemble) ; l'Équipe de la semaine | Lundi | Visages |
| **Le Top 5 · J#** | Reel : les cinq plus beaux gestes | Mardi | Terrain |
| **Portrait** | Photo du Studio en noir et blanc, trois phrases du joueur. C'est le « Portrait du MVP » vendu aux sponsors | Mercredi | Visages |
| **La Course** | Carrousel : top 10, flèches, écarts, puis la plus grosse montée de chaque division | Jeudi | Course |
| **Jour de Verdict** | Carrousel : les cartes avant et après (joueurs avec l'accord « hors de l'app ») | 2/11, 30/11, 28/12, 25/01 | Course |
| **Venu seul** | Reel : un nouveau, sa carte au 1er puis au 4e dimanche, trois phrases face caméra | Un dimanche sur deux | Porte |
| **Le Défi Pépite** | Reel en Collab avec la tête d'affiche et le challenger | Une semaine sur deux | Visages |
| **Stories** | « La Feuille », « Le programme », Matchday, sondage MVP, « Minuit. Les votes ferment. », republication des stories « Ton dimanche » des joueurs | Chaque semaine | Tous |
| **Stories à la une** | « Comment ça marche », « La Pépite », « Viens seul », « Partenaires » | Fixes | Porte |
| **Trial Reels** | Le brut, à tester | 1 à 2 par semaine | Vestiaire |

### TikTok : la tribune

**Rôle.** Faire découvrir la ligue, surtout aux Lillois, via le fil « À proximité » et la recherche.

**Réglages.**
- **Un seul compte**, trois registres : vitrine ~25 %, match ~45 %, vestiaire ~30 %.
- L'underground le plus crédible vient des comptes perso des joueurs : on les relaie, crédités, avec leur accord.
- Lieu identifié à chaque vidéo. Mots-clés **dits, écrits à l'écran et légendés** : « foot à 5 Lille », « ligue du dimanche », « Pépite d'Or ».
- Musique : la bibliothèque commerciale de TikTok, et le son original de la SFL.
- Une seconde de signature sonore, les mêmes sous-titres partout.

| Série | Ce que c'est | Quand |
|---|---|---|
| **Le But du Dimanche** | Le plus beau but, en ligne moins de 2 h après le dernier match | Dimanche soir |
| **La Course en 30 s** | Le classement dit face caméra ; le débat en commentaires | Lundi |
| **Le Top 5** | Les cinq gestes de la journée | Mardi |
| **Ta note** | Un joueur découvre sa nouvelle note devant l'objectif. Le format qui n'appartient qu'à nous | Jours de Verdict, et le jeudi |
| **Le Contrat** | Le duel de rivaux tiré de l'app, annoncé le samedi, tranché le dimanche | Samedi |
| **POV** | « POV : t'es venu seul et t'es 7e de la ligue. » | Mercredi |
| **Il manque 1.** | Occasionnel : seulement s'il reste des places, publié le lundi ou le mardi (« Dimanche prochain. Inscris-toi avant jeudi. »), pour qu'un inconnu ait le temps d'être accepté et de répondre avant vendredi minuit. Le vendredi, il ne vise que les inscrits (désistement, extra time). Sinon, on montre la liste d'attente | Lundi ou mardi |
| **Venu seul** | Le premier dimanche d'un nouveau | Un dimanche sur deux |
| **Le Défi Pépite** | Extrait de 45 s | Une semaine sur deux |

**Plus tard** : un live vertical au téléphone (le banc, l'annonce du classement), après 1 000 abonnés.

### YouTube : la chaîne

**Rôle.** L'archive de la ligue, l'information et le divertissement. C'est là que vivent les formats longs des stars.

**Objectif de saison** : **500 abonnés et 3 000 h de visionnage public** (les directs archivés en public y contribuent, à vérifier dans YouTube Studio). Les abonnements de chaîne et le Super Chat ne s'ouvrent qu'aux deux conditions réunies, avec 3 vidéos en 90 jours, puis une candidature acceptée et un compte AdSense (`04` D12a). Pas de pari sur la pub : le seuil doublerait pour les nouvelles chaînes le 01/02/2027 [à vérifier sur blog.youtube / support.google.com].

| Série | Format | Quand |
|---|---|---|
| **SFL Live · J#** | Le même flux que Twitch, en simultané | Dimanche |
| **Le Résumé · J#** | 3 à 5 min par défaut, monté depuis les marqueurs, une miniature ; 8 à 12 min au niveau Complet (un chapitre par match, un chapitre « La Course », trois miniatures testées). « Présenté par » le sponsor Principal. Chaque joueur envoie à sa famille le lien horodaté de *son* match | Lundi 18 h |
| **Shorts** | Buts, Top 5, extraits de défis, chacun relié au Résumé | Dimanche à mercredi |
| **Le Défi Pépite** | 12 à 20 min + 4 à 6 Shorts. Une tête d'affiche contre le siège ouvert (§8) | Une semaine sur deux |
| **Face-à-Face** | Les deux premiers du classement, assis l'un devant l'autre avant un dimanche décisif | Avant un Jour de Verdict |
| **Vestiaire** | Podcast vidéo chapitré : une tête d'affiche, un nouveau, un fidèle, un animateur | Mensuel |
| **La Nuit de la Pépite** | La finale et la remise | 24/01 |

- Chaque lundi, on demande aux joueurs d'« hyper » le Résumé, si la fonction Hype est ouverte en France pour la chaîne (à vérifier dans YouTube Studio).
- La chaîne perso d'une star est co-créditée (Collaborations, jusqu'à 5 chaînes).
- Les Posts servent au sondage MVP et aux convocations.

### Twitch : le stade

**Rôle.** Le direct du dimanche, comme tu le veux. Son public réel : les joueurs, leurs proches, les habitués.

- **SFL Live · J#** : un commentateur fixe, et **« le banc »** : une tête d'affiche qui ne joue pas ce match et le commente.
- **Habillage** : score, chrono, prénom et note BOLA du joueur, bandeau de sa carte (seulement pour les joueurs qui ont signé l'autorisation, `04` D1), classement en direct. Signature neutre : « SFL », « getbola.app ».
- **Le Flair en direct** : pronostics du prochain buteur avec les points de chaîne, sans argent, **quand les points de chaîne seront visibles sur la chaîne SFL**. Jusqu'en 2025, ils étaient réservés aux Affiliés ; l'ouverture à tous en 2026 n'est pas vérifiée (`02` §4).
- **Le statut d'Affilié** : à suivre dans le tableau de bord Twitch (Succès → Chemin vers Affilié). Si 7 jours de diffusion sur 30 sont exigés, le seul dimanche n'y suffit pas : ajouter un live en semaine (l'After, ou la rediffusion du jeudi).
- **L'After** : 30 min de débrief si un animateur s'en charge. Raid de fin vers une star qui streame.
- **Les règles** : la même qualité que sur YouTube ; jamais « va sur YouTube » à l'écran ; aucune musique commerciale (y compris la sono du complexe) ; modération dès le premier live ; la case « contenu de marque » cochée à chaque live (naming, spot mi-temps).
- **Toute la saison 1, en simultané avec YouTube** : c'est promis aux sponsors. Le point du 6 décembre décide seulement où mettre la modération et les animations, et prépare la saison 2.

---

## 8. Les stars : les « Têtes d'affiche », et la règle d'équité

Le risque est double : une ligue individuelle qui paraît servir cinq joueurs, et l'« attention empruntée » qui a coûté cher à la Baller League. Sept règles :

1. **Le classement fait le casting.** Cinq Têtes d'affiche, prises dans le **top 10 du Pépite d'Or**, revues à chaque Jour de Verdict. Ton premier choix (Zachary, Junaid, Ilyes, Selim, Abdel) est vérifié sur l'export du lundi 2/11 ; qui n'est pas dans le top 10 laisse sa place au suivant du classement qui accepte. Orthographe à confirmer (« Jouneid » dans l'app ; « Zakaria » ou « Zakary » ; Ilyes à ne pas confondre avec Ilies ; Abdel avec Hassan Abdel). Qui sort du top 10 quitte l'affiche, et c'est un épisode.
2. **Le siège ouvert.** Chaque format star oppose une Tête d'affiche à quelqu'un qui n'en est pas une : l'outsider (déjà dans l'app), la plus grosse montée de la semaine, ou un inscrit récent et majeur tiré au sort. C'est l'argument de recrutement : *ici, tu peux passer à l'écran contre le n° 1*.
3. **Une tête pour trois visages.** L'unité, c'est l'**épisode** : ses déclinaisons (Shorts, Reel, TikTok) comptent pour un. Sur un mois, pour chaque épisode centré sur un joueur du top 10, trois sont centrés sur d'autres ; l'invité du siège ouvert compte comme « autre visage ». Contrôle mensuel, dans le registre de couverture. Pour que le mérite ne serve pas toujours les mêmes :
   - le Top 5 contient au moins 2 actions de D2 ou D3 ;
   - « Le But du Dimanche » change de division chaque semaine ;
   - la feuille de tournage fait tourner le vertical entre les terrains et les divisions.
4. **La couverture.** Chaque joueur actif est **nommé dans une publication du fil ou un Reel** (une story ne compte pas) au moins une fois toutes les 4 journées ; toutes les 6 au-delà de 120 actifs. Les mineurs, la liste rouge et les joueurs sans accord « hors de l'app » sortent du compte.
5. **La séparation des pouvoirs.** Un format star ne donne jamais un point Pépite ni un cran de carte. Les équipes sont composées par l'app. Les points donnés à la main (`pepiteBonus`) et toute correction de feuille ont un motif public et un plafond. **Ilyes est admin** (`admin.ts`) : il ne saisit ni ne corrige la feuille d'un match qu'il joue (`04` D9).
6. **Un contrat écrit par Tête d'affiche**, même sous 1 000 €, pour un cycle de 4 journées renouvelable : droit à l'image, propriété des contenus, co-crédit, et la mention « Collaboration commerciale » dès qu'il y a une dotation. **Aucun mineur** dans ces formats.
7. **La marque, c'est la Pépite et la carte, pas cinq personnes.** Si une star part, la série continue avec le n° 6.

### Le Défi Pépite, notre « Pitch Addict »

Ce qu'on reprend du duo Victor et Thibault : un exercice signature, les mêmes visages, un invité, et TikTok comme moteur.

- **L'exercice signature proposé : « Le Coffre ».** Une cible de 40 cm à 15 m. Trois manches. Il a son propre classement, **hors Pépite**. À tester sur le terrain avant de le figer.
- **Le principe** : « le n° 1 de la ligue contre un inscrit de mardi ».
- **Le tournage** : en marge d'un dimanche ou un soir de semaine, deux téléphones, un animateur fixe.
- **Ce que ça donne** : une vidéo longue, 4 à 6 Shorts, un Reel en Collab, un TikTok.

---

## 9. Ton de voix

**Les règles**
- Tutoiement. Phrases courtes, au présent, finies par un point.
- Des chiffres vrais, tirés de l'app et vérifiés.
- Un prénom dans chaque publication.
- Pas d'emoji dans les textes de la marque.
- Le chambrage vise le geste, jamais la personne.
- Le speaker peut monter en voix dans le live. L'écrit reste sec.

*Les exemples ci-dessous sont des modèles : leurs chiffres et leurs places sont inventés pour l'exemple et seront remplacés par les vrais, tirés de l'app.*

**Les mots de la maison** : **le** Pépite d'Or (le classement, comme dans l'app : « points au Pépite d'Or ») et **la** Pépite d'Or (le titre et le trophée), à confirmer par toi (`04`, petites questions) ; La Course, Jour de Verdict, Têtes d'affiche, le siège ouvert, D1/D2/D3, les Noirs et les Blancs, le contrat, le Flair, « Il manque 1. », « Viens seul. ».

**Accroches (première seconde)**
- « Il est arrivé seul il y a trois dimanches. Il est 7e. »
- « Cet homme a un contrat sur la tête. »
- « 30 places en D1. Dimanche, il en restait une. »
- « Minuit. Les votes ferment. »
- « L'or ne se donne pas. »

**Légendes Instagram**
- « J#. Premier dimanche en divisions. Il a tenu la D1. Toi, t'es où ? Classement complet en story. »
- « Venu seul il y a trois dimanches. Ce soir, il joue en D1. [Prénom], on t'a trouvé. »
- « Note 76 → 79 en quatre dimanches. Ça a débloqué. »

**Titres YouTube** (l'accroche d'abord, la journée à la fin)
- « Le n° 1 de la ligue contre un inscrit de mardi | Le Défi Pépite #1 »
- « Il lui a pris la 1re place. On les a assis face à face. | Face-à-Face #1 »
- « 30 joueurs, une seule D1 : le dimanche qui a tout changé | Le Résumé SFL J# »

**Interdits**
- Les insultes, l'humiliation, un raté publié sans l'accord du joueur.
- Un chiffre non vérifié, un superlatif sans preuve (« le meilleur joueur de Lille »).
- Le registre publicitaire (« découvrez », « rejoignez l'aventure »).
- Un sponsor d'alcool : la loi Évin interdit le parrainage sportif en faveur de l'alcool (Code de la santé publique, art. L3323-2). Un sponsor de paris : la loi influence (2023-451) encadre leur promotion, et l'inscription est ouverte dès 12 ans.
- Sur Twitch, tout renvoi vers une autre plateforme.
- Les noms restent entre crochets tant que leur orthographe n'est pas confirmée.

---

## 10. Direction visuelle des réseaux

### Une couleur, un sens

| Couleur | Code | Usage sur les réseaux |
|---|---|---|
| Noir Nuit | `#08090B` | Le fond |
| Blanc Craie | `#F4F5F2` | Le texte, le sigle |
| Gris Béton | `#8F908B` | Le texte secondaire |
| Or | (couleur de la carte MVP) | **Seulement** la Pépite d'Or et la carte MVP |
| Rouge Impact, bleu cobalt Défensive | (couleurs des cartes) | **Seulement** quand le titre est gagné |
| Braise | `#FF8A4C` | **Seulement** le recrutement : « Il manque 1. » |
| ~~Bleu SFL~~ | ~~`#3D9BFF`~~ | **Retiré des réseaux** : il se confond avec la carte Défensive. À trancher (D7) |

### Les signes fixes
- **Typo** : Inter très grasse en capitales pour les titres ; Anton pour tous les chiffres (score, note, points, rang) ; Barlow Condensed sur les cartes, comme dans l'app.
- **Le sigle SFL** en italique (`SFL/public/bola/sfl.svg`), toujours au même coin.
- **Le cartouche de série** : « S1 · J# · LA COURSE ». On reconnaît la rubrique et l'épisode en une seconde.
- **Ouverture** de 0,5 s ; **fermeture** d'1 s sur la carte du joueur, « Viens seul. » et getbola.app.
- **Le son** : de vrais sons du terrain (sifflet, frappe, filet), enregistrés un dimanche et montés en interne, sans IA ni dépense ; une signature d'1 s, publiée comme son original sur TikTok.

### Les images
- **L'hiver de midi.** On joue de 12 h 30 à 16 h environ, de jour, en plein air (Hippodrome de Marcq). Lumière basse et rasante, ciel gris, pluie, buée. Noir et blanc contrasté, contre-plongée (comme l'écran 1 du site), grain assumé. La seule couleur vive, c'est le titre gagné.
- **Des images de match vraies**, à l'iPhone, jamais générées ni modifiées par IA. Miniatures YouTube : un vrai visage, un chiffre en Anton, trois mots au plus.
- **La carte BOLA** est un portrait de marque : sa photo est faite par l'IA dans l'app (`api/photo-studio`), et c'est assumé. Elle signe nos contenus ; elle ne remplace jamais une image du terrain.
- **Le Studio du dimanche.** Le « Mur pour photos et interviews » déjà budgété : une face noire unie pour les portraits, l'autre aux logos des sponsors pour les interviews (`04` D7). Chaque nouveau joueur y fait son portrait officiel à son premier dimanche, s'il a signé l'accord. Ce portrait nourrit « Portrait » et le recrutement.
- **La question de l'IA ailleurs.** L'affiche du match (Seedream) et les couvertures des Actus (Magnific) sont générées ; les sponsors achètent des « vidéos IA » ; la politique de l'app prévoit de confier la photo de carte à Magnific. À trancher (D10).

### Les fichiers maîtres
- 1080×1440 pour la grille (l'essentiel dans le 1080×1350 central) ; 1080×1920 pour la vidéo verticale. Jusqu'aux gabarits de l'étape 2, les carrousels de l'app restent en 4:5 (1080×1350).
- Zones sûres d'un Reel : rien d'important dans les ~250 px du haut, ~440 px du bas, ~120 px de droite (estimation, sources tierces).
- **Un seul fichier maître 9:16** par vidéo, sous-titres incrustés dans la zone sûre commune, sans filigrane ni musique, publié en natif sur YouTube Shorts, Reels et TikTok. Seuls la légende, la couverture et, si on veut, le son changent d'une plateforme à l'autre.

### Les gabarits à produire (étape 2)
Carrousel 3:4 (cartes, course, verdict), couverture de Reel, story (feuille, programme, résultat), miniature YouTube, cartouche de série, sous-titres, ouverture et fermeture, habillage du live (score, noms, notes, classement), avatar et bannières.

---

## 11. Recruter, et servir les sponsors

### Le parcours d'un futur joueur

| Étape | Ce qu'il se dit | Les séries qui le servent |
|---|---|---|
| Voir | « Ça joue bien, et c'est à Lille. » | L'Action, Le But du Dimanche, Le Top 5 |
| Se projeter | « Même un nouveau peut monter. » | Venu seul, La Course, POV, le siège ouvert |
| Oser | « Je peux venir seul ? À mon niveau ? » | Il manque 1. (s'il reste des places), la liste d'attente, stories à la une « Comment ça marche » |
| Revenir | « Ma carte a bougé. » | Les Cartes, Ta note, Jour de Verdict, « Ton dimanche » |
| Ramener | « Je fais venir mes potes. » | Le parrainage : dix potes, carte Fondateur sur 500 |

- **Après le clic.** Le lien en bio mène à `getbola.app/inscription`, marqué par plateforme (« / » ouvre le site BOLA dans un cadre, et la marque s'y perd). Puis : identité et 4 photos, compte « en attente » jusqu'à ce qu'un admin l'accepte (un admin nommé, en moins de 24 h), convocation ouverte du lundi au vendredi minuit. Plus tard, une entrée courte de la SFL (où, quand, prix, niveau, « tu viens seul », bouton d'inscription). Parcours à tester sur un téléphone avant chaque campagne.
- **La braise ne promet que ce que l'app permet dans le délai annoncé.** Pas de « place libre dimanche » pour un inconnu le vendredi.
- **Cent joueurs, cent diffuseurs.** Chaque joueur montré reçoit son visuel prêt à poster (la story « Ton dimanche » de l'app) et, pour les mis en avant, une invitation en Collab.
- **Mesure sans traceur, dès la semaine 1.** Les paramètres `utm_*` gardés à l'arrivée et enregistrés avec le compte, et le champ « Comment as-tu connu la SFL ? » (deux changements dans l'app, `05` A2). La politique actuelle de l'app exclut tout pixel : on la respecte.
- **La capacité d'abord.** 30 places par dimanche dans le code (`04` D0). Au-delà, les remplaçants (déjà dans l'app, dans l'ordre d'arrivée) et une liste d'attente visible, qui devient elle-même un argument.

### Les sponsors : les séries sont l'inventaire

| Formule (offre du 23/10) | Ce qui est promis | La série qui le tient |
|---|---|---|
| Principal | Naming, « Résumé du dimanche présenté par » | « Le Résumé · J# présenté par… », le naming du live, et en option « La Nuit de la Pépite » |
| Officiel (2 places dans l'offre, 1 dans le budget) | « Top 5 de la journée » ou « Portrait du MVP », **2 publications SFL par mois** | « Le Top 5 · J# » ou « Portrait » |
| Partenaire | 1 publication par mois | Une publication en Collab, et la dotation remise et filmée un Jour de Verdict |
| À vendre en plus | — | « Le Défi Pépite présenté par… », TikTok. Le Flair en direct, seulement quand les points de chaîne Twitch seront visibles sur la chaîne |

**Les règles.**
- Le sponsor ne touche jamais l'or : une dotation va au meilleur buteur du mois ou au MVP, mais la photo de remise ne montre jamais la carte MVP ni la Pépite.
- Son logo a une zone fixe ; la mention « Publicité » est toujours là.
- **Chaque contenu sponsorisé est déclaré avec l'outil de la plateforme** : « Partenariat rémunéré » sur Instagram, « contenu de marque » sur TikTok, « promotion payée » sur YouTube, « contenu de marque » sur Twitch, à chaque live (naming, spot mi-temps).
- Ce qu'on doit aux sponsors est inscrit chaque semaine dans le calendrier (§6, ligne « Dû aux sponsors »).

**À corriger dans l'offre** (D10) : d'abord savoir qui a signé quoi ; puis le live Instagram (impossible avant 1 000 abonnés), TikTok absent, les « vidéos IA », le nombre de places Officiel.

---

## 12. Les indicateurs

### Les indicateurs maîtres : des joueurs, dans la limite des places

Le code fixe 2 terrains de 15, soit **30 places par dimanche** (`04` D0). Un joueur actif a joué au moins un dimanche sur les quatre derniers : avec 30 places, il y en a **au plus 120**. Viser 200 actifs n'a de sens que si tu ouvres des terrains ou des créneaux.
- **Remplissage** : 30 places sur 30, chaque dimanche.
- **Inscrits** : environ 100 aujourd'hui ; l'objectif chiffré dépend de D0.
- **Liste d'attente** : elle grandit, et elle devient la réserve de la saison 2 (pré-inscriptions du 10/01 au 24/01).
- 200 à 300 joueurs : l'objectif de l'ouverture de la saison 2, si la capacité suit.

### Trois indicateurs par plateforme

| Plateforme | 1 | 2 | 3 |
|---|---|---|---|
| Instagram | Envois en DM pour 1 000 comptes touchés | Inscriptions BOLA attribuées (UTM) | Part des joueurs identifiés qui republient |
| TikTok | Taux de visionnage complet | Part des vues venant d'« À proximité » et de la recherche | Inscriptions BOLA attribuées (UTM) |
| YouTube | Durée moyenne de visionnage du Résumé | Abonnés et heures de visionnage public (500 et 3 000 h) | Part des vues des formats stars venant de non-abonnés |
| Twitch | Spectateurs simultanés moyens | Heures vues, face à YouTube Live | Chemin vers Affilié |

### Les objectifs pour le point du 6/12 (estimation, à recaler sur nos chiffres de novembre)

| | Au 6/12 | Au 24/01 |
|---|---|---|
| Remplissage | 30/30 chaque dimanche | 30/30, et une liste d'attente |
| Inscriptions attribuées (UTM ou « Comment as-tu connu ») | 10 | 40 |
| Instagram | 300 abonnés | 1 000 (le live s'ouvre) |
| TikTok | 500 abonnés | 1 500 |
| YouTube | 100 abonnés, 500 h | 500 abonnés, 3 000 h |
| Twitch | 10 spectateurs simultanés en moyenne | 20 |

### Le tableau de bord du lundi (une page)
Remplissage et remplaçants · nouveaux inscrits, et d'où ils viennent · liste d'attente · part des nouveaux revenus au 3e dimanche · couverture (part des actifs nommés depuis 4 journées) · ratio « une tête pour trois visages » · inscrits venus par parrainage · ce qui est dû aux sponsors, fait ou pas.

---

## Annexe A. Option écartée : « L'Or du Dimanche » (premium)

**L'idée.** La SFL se tient comme une grande compétition : la retenue de Nike Football, le rituel de la Ligue des Champions, la mise en page d'un magazine, les images d'un iPhone au bord du terrain.

**Promesse.** « Ici, chacun gagne un nom, et un seul repart avec l'Or. »

**Ce qui change si tu la choisis.**
- Le ton est plus sobre et plus cérémonieux ; l'humour reste dans le registre Vestiaire, sur TikTok.
- Piliers : Le Dimanche 35 %, La Course à l'Or 20 %, Les Visages 20 %, Le Vestiaire 15 %, Rejoins 10 %.
- Instagram devient « le programme officiel » ; la photo noir et blanc et le Studio sont au centre.
- Moins de mécaniques de jeu à l'écran (contrats, Flair), plus de rituel (le trophée, la Nuit de l'Or).

**Pourquoi elle n'est pas la base.** Elle sert très bien ta vitrine Instagram et les sponsors, mais moins ton ambition YouTube et TikTok « à la Pitch Addict ». Le risque de grandiloquence est réel avec 100 joueurs. Ses meilleures idées sont déjà greffées (§0).

## Annexe B. Option écartée : « Viens seul. » (communauté)

**L'idée.** La SFL n'a pas d'équipes : personne ne peut répondre « je n'ai pas d'équipe ». Les réseaux montrent cent joueurs qui progressent, pour que le cent-unième se dise « pourquoi pas moi ».

**Promesse.** « Viens seul. Ici, chaque dimanche compte. »

**Ce qui change si tu la choisis.**
- Les stars n'ont plus de pilier à elles : elles vivent dans La Course.
- Piliers : Le Dimanche 35 %, Les Héros (cartes de toutes les divisions, nouveaux, fidèles) 25 %, La Course 20 %, Le Vestiaire 10 %, Rejoins 10 %.
- Le ton est celui du capitaine de vestiaire qui connaît chacun par son prénom.
- Plus d'« Équipe de la semaine » par division, moins de formats longs avec les stars.

**Pourquoi elle n'est pas la base.** C'est la plus directe pour passer de 100 à 300 joueurs, mais elle met en retrait la ligne « stars » que tu veux sur YouTube. Son indicateur maître, ses garde-fous d'équité et sa braise du recrutement sont greffés (§0).
