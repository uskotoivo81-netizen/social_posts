---
title: Connecteur MCP SpeedyIndex pour Claude : guide de connexion
seo_title: Connecteur MCP SpeedyIndex pour Claude : guide SEO
meta_description: Découvrez le connecteur MCP SpeedyIndex pour Claude : connexion, 22 outils, indexation Google/Yandex, vérifications d'index en masse et suivi de positions.
keyword: connecteur mcp (110/KD18 (fr))
tags: SEO, Artificial Intelligence, Marketing
cover: /home/claude/differ/fr_connector_cover.png
video: b87UiIprQ0M
---

# Connecteur MCP SpeedyIndex pour Claude : guide de connexion

Un connecteur MCP relie Claude à des services externes via le Model Context Protocol (MCP), un standard ouvert d'Anthropic (novembre 2024). Le connecteur MCP SpeedyIndex applique ce protocole au SEO : il permet à Claude de lancer des tâches d'indexation Google/Yandex, de vérifier l'indexation sur Google, Yandex et Bing, et de suivre des positions Google, en gardant vos données SpeedyIndex à portée de main dans la conversation. Pour les spécialistes SEO, cela évite les copier-coller entre outils.

Le connecteur MCP SpeedyIndex existe en version hébergée (`mcp.speedyindex.com/mcp`, OAuth avec clé API) et en version locale (npm `speedyindex-mcp`, Node.js 18+). Le connecteur est gratuit ; les tâches sont payées avec des jetons SpeedyIndex, sans abonnement. Chaque nouveau compte reçoit 100 jetons gratuits. La vidéo ci-dessous (38 secondes, sans son) montre la connexion à Claude.

![SpeedyIndex + Claude — video](https://img.youtube.com/vi/b87UiIprQ0M/hqdefault.jpg)

## Connexion à Claude (web et desktop)

1. Ouvrez Claude et allez dans Plugins (claude.ai/plugins) → Add → Add custom connector.
2. Nommez le connecteur « SpeedyIndex » et saisissez l'URL `mcp.speedyindex.com/mcp`. Continuez, puis Connectez.
3. Collez votre clé API sur la page de connexion SpeedyIndex (section API de votre compte). La clé n'est jamais tapée dans le chat.
4. Dans une conversation, cliquez sur le « + » → Connectors et activez SpeedyIndex.
5. Testez avec « What is my SpeedyIndex balance? » : si Claude affiche jetons et crédits, c'est connecté.

Le plan gratuit de Claude autorise un connecteur personnalisé ; les plans payants permettent d'en ajouter plusieurs. Sur Team/Enterprise, un propriétaire ajoute le connecteur dans les paramètres de l'organisation. Pour un guide de connexion étape par étape, consultez la [documentation du connecteur MCP SpeedyIndex](https://fr.speedyindex.com/mcp/).

Claude Code, Cursor et VS Code sont également pris en charge : `claude mcp add` puis `/mcp` et Authenticate ; Cursor via `.cursor/mcp.json` ou `~/.cursor/mcp.json` ; VS Code via la commande « MCP: Add Server » ou un fichier `.mcp.json` d'espace de travail.

```bash
claude mcp add --transport http --scope user speedyindex https://mcp.speedyindex.com/mcp
```

## Outils et capacités

Le serveur distant propose 22 outils : 15 en lecture seule sont gratuits (solde, listes, statuts, rapports, positions). Les 7 outils qui modifient le compte demandent confirmation (sauf réglage « Always allow ») ; 5 dépensent des jetons.

- Indexation Google et Yandex : jusqu'à 10 000 URLs par tâche. Google : payé par URL indexée (jetons restitués si non indexée). Étalement possible sur 2 à 30 jours.
- Vérification d'index sur Google, Yandex, Bing : jusqu'à 10 000 URLs, listes indexées/non indexées (titres pour Google).
- Vérificateur de backlinks : ouvre les pages donatrices, vérifie le lien (HTTP, ancre, nofollow, Moz DA, spam score, 50 domaines cibles).
- Rank Tracker Google : projets, 5 régions, 10 concurrents, positions, tendances (90 contrôles), présence AI Overview.

Avant une campagne, vous pouvez contrôler en masse si vos pages sont déjà dans Google avec le [vérificateur d'indexation en lot](https://fr.speedyindex.com/verificateur-index-google/).

## Sécurité, coûts et confirmations

Aucune base de données côté serveur ; clé API stockée dans un jeton chiffré ; jeton d'accès valable 1 heure, connexion renouvelée jusqu'à 90 jours ; changer la clé révoque tout. Le connecteur ne paie pas, ne crée pas de factures, ne supprime rien.

Le connecteur est gratuit ; les tâches coûtent des jetons SpeedyIndex (pas d'abonnement). Les 15 outils en lecture seule sont gratuits ; créer un projet Rank Tracker et ajouter des mots-clés est gratuit, lancer un contrôle est payant (coût affiché à l'avance). Claude demande approbation avant chaque appel ; les 7 outils de modification demandent confirmation sauf « Always allow ».

## Comparaison avec d'autres MCP SEO

Les documentations d'Ahrefs, Semrush, SE Ranking, DataForSEO, Keyword.com et Screaming Frog (consultées le 19 novembre 2026) ne mentionnent pas de vérification d'index en masse ; la soumission d'indexation n'est pas documentée chez ces fournisseurs. Moz API MCP (bêta) ne documente pas le suivi de positions ni l'indexation (comparaison du hub SpeedyIndex, novembre 2026). Seul SpeedyIndex documente la vérification d'index en masse et la soumission d'indexation Google/Yandex.

## FAQ

### Le connecteur MCP SpeedyIndex est-il payant ?
Le connecteur est gratuit. Les tâches sont facturées en jetons SpeedyIndex, sans abonnement. 100 jetons gratuits à l'inscription.

### Quels clients MCP sont officiellement pris en charge ?
Claude (web et desktop), Claude Code, Cursor et VS Code. Le serveur distant `mcp.speedyindex.com/mcp` utilise OAuth ; une version npm locale existe.

### Comment fonctionne la confirmation des outils ?
Claude demande approbation avant chaque appel d'outil. Les 7 outils de modification demandent confirmation, sauf si réglés sur « Always allow ». Claude n'accède qu'aux autorisations accordées lors de la connexion.