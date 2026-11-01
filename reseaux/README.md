# Réseaux sociaux de la SFL : dossier de cadrage

*01/11/2026, mis à jour avec tes décisions du jour. La J4 du 1er novembre est passée. Aucun compte n'est encore créé : tu les crées. Rien n'est commité.*

**L'objectif.** Passer d'environ 100 à 150 joueurs dans la ligue, puis jusqu'à 300 quand il y aura plus de terrains, et faire de la SFL une marque que les sponsors veulent. Par ordre : Instagram, TikTok, YouTube, Twitch.

**La limite à connaître d'abord.** La SFL vise 150 joueurs dans la ligue ; 300 au maximum, quand il y aura vraiment des terrains (`04` D0, ta réponse du 01/11). L'app, elle, est réglée sur 2 terrains de 15, soit 30 places par dimanche (`TERRAINS_MAX = 2`, `SFL/src/lib/sfl/equipes-division.ts`). Ce réglage ne correspond pas à ton objectif : il est à revoir avec toi, le code n'est pas touché. La pub reste conditionnée à la capacité réelle d'accueil : le nombre de places par dimanche est à confirmer avec l'app.

**La proposition en une phrase.** La SFL n'a pas d'équipes, elle a cent personnages : on raconte la course à la Pépite d'Or comme une série de 13 dimanches. Lisse dans le cadre, vrai dans l'image.

## Les fichiers

| Fichier | Ce qu'il contient | À lire si… |
|---|---|---|
| [`05-demarrage-48h.md`](05-demarrage-48h.md) | Le démarrage du **1er novembre** : ce qui est fait, ce qui est à reprendre pour le 8 novembre (comptes, bios, accords, plans à filmer, rangement, publications du soir, textes prêts) | **Tu prépares le 8 novembre** |
| [`04-decisions.md`](04-decisions.md) | Les 14 décisions qui te reviennent, avec ma recommandation : validées le 01/11, en attente de toi, reportées | Tu veux répondre vite |
| [`03-plateforme-de-marque.md`](03-plateforme-de-marque.md) | La proposition : mission, promesse, ton, piliers, séries par plateforme, stars et équité, visuel, indicateurs | Tu veux juger le fond |
| [`02-etude.md`](02-etude.md) | Ce que la recherche a établi, avec les sources : « Instagram = lisse », Twitch ou YouTube, un ou deux TikTok, Pitch Addict, les concurrents | Tu veux vérifier |
| [`01-agence.md`](01-agence.md) | L'agence : agents et humains, le workflow, tes portes de validation, la boucle d'un dimanche | Tu veux savoir qui fait quoi |

**Légende des sources** : [F] fait sourcé, [E] estimation, [A] avis de l'agence.

---

## La feuille de route

### Étape 0. Démarrage (1er novembre) : passée
- **Statut** : la J4 du 1er novembre est passée. Ce qui est fait, et ce qui est à reprendre pour le 8 novembre : `05`.
- **Livrables prévus** : les comptes réservés sous le même nom ; les bios, la photo de profil et le lien marqué vers l'inscription ; le message aux joueurs, la pancarte et les autorisations signées ; les rushs du 1er novembre (J4) rangés en deux copies ; le carnet ou les marqueurs des temps forts ; le premier Jour de Verdict, le lundi 2/11.
- **Qui** : toi (comptes, signatures, à la table d'accueil) ; la régie, et selon l'équipe réelle le bord terrain, le commentateur, le noteur (`05` A6 et A7) ; agents Directeur et Planning (textes, listes, déjà prêts dans `05`).
- **À reprendre pour le 8 novembre** : les comptes, que tu crées toi-même (D2) ; le direct, dès que tu fixes la date (D5) ; les autorisations, car seuls les joueurs qui ont signé la charte apparaissent (D1).
- **Tu as validé (01/11)** : D1 (seuls les joueurs qui ont signé la charte apparaissent ; les règles sur les mineurs restent) ; D3 (comptes au nom de la SFL ; BOLA n'apparaît que comme l'appli qui fait les stats et les cartes) ; D5 sur le principe (le direct en simultané sur Twitch et YouTube, date à fixer par toi). D2 attend les noms des comptes que tu crées. D4 est close.
- **Fin** : le 1er novembre est filmé et rangé, sans joueur publié sans accord, et la première boucle du lundi a tourné.

### Étape 1. Cadrage de la marque et ligne éditoriale (→ 8/11)
- **Livrables** : la plateforme de marque validée ; la charte d'écriture (ton, mots de la maison, interdits) ; la liste des séries v1 ; la règle d'équité des stars, publiée ; la capacité et l'offre d'arrivée (D0 : 150 joueurs visés, places par dimanche à confirmer avec l'app) ; le nom exact et le numéro de l'association SFL (D12a est close : association, pas société).
- **Dans l'app, avant le 8/11** : la case « vidéos de match » (nouvelle version de l'accord, D1 : seuls ceux qui l'ont signée apparaissent) ; les liens marqués enregistrés à l'inscription et le champ « Comment as-tu connu la SFL ? » (`05` A2).
- **Qui** : agents Veille, Stratège, Directeur ; toi.
- **Tu valides** : `03` (ou une des deux options de l'annexe) ; D0 (le nombre de places par dimanche) ; D6 (les rôles avec l'association partenaire, et le rythme).
- **Tranchées le 01/11** : D7 (voir l'étape 2), D8 (un seul compte TikTok), D12a (association). D9 est reportée (« on verra bien ») : recommandation inchangée.
- **Fin** : on peut dire en une phrase ce qu'est la SFL sur les réseaux, et chaque série a un nom, un jour, un rôle.

### Étape 2. Identité visuelle réseaux et gabarits (→ mi-novembre)
- **Livrables** : le kit (couleurs, typo, place du sigle, cartouche de série) ; les gabarits codés qui se remplissent avec les vraies données (carrousel 3:4, couverture de Reel, story, miniature YouTube, sous-titres, ouverture et fermeture) ; l'habillage du live ; avatar et bannières ; la signature sonore (de vrais sons du terrain, montés en interne).
- **Qui** : agent Atelier visuel (spécifications, gabarits en code) ; toi (direction artistique) ; agent Contrôle.
- **Validé le 01/11 (D7)** : une DA presque noir et blanc, avec le bleu SFL `#3D9BFF` en couleur d'accent de la marque, et l'or réservé à l'univers Pépite d'Or (la carte MVP).
- **Point de vigilance** : le bleu SFL, c'est la marque ; le bleu cobalt, c'est le titre Défensive gagné. Les gabarits ne les mélangent pas.
- **Tu valides** : le trophée et le Studio (les deux autres points de D7), chaque gabarit sur rendu.
- **Fin** : un contenu de chaque série sort d'un gabarit validé, sans retouche à la main.

### Étape 3. Production et calendrier éditorial (→ fin novembre, puis chaque semaine)
- **Livrables** : le calendrier jusqu'au 24/01 (13 dimanches, Jours de Verdict les 2/11, 30/11, 28/12 et 25/01, fêtes, Nuit de la Pépite, pré-inscriptions de la saison 2 du 10/01 au 24/01), avec ce qui est dû aux sponsors chaque semaine ; la feuille de tournage type ; le premier « Défi Pépite » tourné ; la charte de modération ; le contrat type des stars, au nom de l'association SFL, relu par un avocat.
- **Qui** : agents Planning, Rédaction, Statisticien, Contrôle ; pour le tournage, l'association partenaire Poleed, qui fournit de quoi tourner, rôles à définir avec elle ; le monteur, la personne qui publie ; toi et le responsable des stars ; un avocat.
- **Tu valides** : le calendrier, le premier format star, les contrats, D9 (reportée : « on verra bien »).
- **Fin** : trois semaines de suite au rythme choisi, sans trou, avec le tableau de couverture à jour.

### Étape 4. Publicité et budget (préparée en novembre, pas de dépense avant décembre)
- **Livrables** : le plan de pub par palier (`04`, coût du plan réseaux) ; l'offre sponsors corrigée, une fois connu qui a signé quoi (dont le direct Instagram promis, impossible avant 1 000 abonnés).
- **Préalables** : la capacité réelle d'accueil (D0 : places par dimanche à confirmer avec l'app). La structure est tranchée (D12a) : comptes pub, contrats, autorisations et AdSense au nom de l'association SFL ([nom exact de l'association], numéro à compléter).
- **Qui** : agent Média ; toi.
- **Tu valides** : D10 et D12b, reportées (« on verra bien ») : recommandations inchangées ; le budget pub, pas avant décembre.
- **Fin** : un budget signé, une première vague mesurée en inscrits et en liste d'attente, pas en vues.

### Étape 5. Pilotage, outils et mesure (dès novembre, puis chaque mois)
- **Livrables** : les outils choisis ; le tableau de bord du lundi ; le rapport mensuel aux sponsors ; le point d'étape du direct simultané Twitch et YouTube (prévu le 6/12, à recaler sur sa date de départ) ; le bilan de saison le 24/01 et les choix pour la saison 2.
- **Qui** : agents Média, Statisticien, Directeur ; la personne qui publie (exports des statistiques) ; toi.
- **Tu valides** : D11 (reportée : « on verra bien »), chaque outil payant, le format du rapport sponsors.
- **Fin** : chaque lundi, une page dit si le dimanche était plein, d'où viennent les nouveaux inscrits, où en est la liste d'attente, et qui a été montré.

---

## La suite

1. **Créer les comptes** au nom de la SFL sur les quatre plateformes (un seul compte TikTok), et **me donner les noms retenus** (D2 ; ma recommandation reste @sundayfiveleague). Activer le direct YouTube dès la création de la chaîne : jusqu'à 24 h d'attente.
2. **Fixer la date du direct**, en simultané sur Twitch et YouTube (D5).
3. **Caler le partenariat avec Poleed et confirmer le nombre de places par dimanche** (D0 ; l'app est réglée sur 30).

Quand tu peux : le nom exact et le numéro de l'association SFL (D12a), pour les autorisations, les contrats et les comptes pub. Reportées, recommandations inchangées : D9, D10, D11, D12b (pas de pub avant décembre).
