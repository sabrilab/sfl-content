# Kit réseaux SFL, v4 (pastel)

Validé par Sabri le 1er novembre 2026. Fichiers aux tailles exactes des plateformes, prêts à poster.
Les photos viennent de la banque d'images de l'app, en attendant les vraies photos de Poleed ; les chiffres et prénoms sont des exemples.

| Dossier | Fichiers | Taille | Où |
|---|---|---|---|
| `profil/` | `sfl-profil-ciel.png` (choisi), `-blanc`, `-encre` | 1080 × 1080 | Photo de profil Instagram, TikTok, YouTube, Twitch |
| `posts/` | la-course, le-but, portrait, il-manque-1, mvp, ta-note, top-5, pov, citation, verdict | 1080 × 1350 (4:5) | Instagram (fil), carrousels |
| `reels/` | le-but, pov, il-manque-1, ta-note | 1080 × 1920 (9:16) | Couvertures de Reels, TikTok, Shorts ; stories |
| `youtube/` | `miniature-resume.png` | 1280 × 720 | Miniature du Résumé du lundi |
| `bannieres/` | `youtube-2560x1440.png` (texte dans la zone sûre 1546 × 423), `twitch-1200x480.png`, `twitch-hors-ligne-1920x1080.png` | | Bannières de chaîne |

Couleurs : blanc `#FFFFFF`, papier `#F2F0E9`, encre `#0E0E10`, bleu SFL `#2563FF` (un mot, un chiffre), ciel `#CFE0FF` (terrain, course), pêche `#FFD8C4` (recrutement, brut), or doux `#F2DC9B` (Pépite, Verdict). Jamais de dégradé.
Typos (Google Fonts, gratuites) : Archivo (titres, étirée de 62 à 125 %), Instrument Serif italique (l'accent), JetBrains Mono (les faits).

Régénérer : `python3 kit.py && node render.cjs .` (Chromium de Playwright). Changer un texte = modifier `kit.py`.
