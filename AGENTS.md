# Instructions projet — dpo-ct

Les règles globales du vault de mémoire de l'auteur (`ClaudeMemory/AGENTS.md`,
hors dépôt) s'appliquent à ce dépôt lorsqu'il est disponible.

## Mémoire projet

Avant toute modification non triviale, consulter — **si le vault de mémoire est
monté** (poste de l'auteur ; il n'est pas disponible dans un environnement
distant, où le dépôt se suffit à lui-même) :

- `ClaudeMemory/02-Projects/Dpo-ct/overview.md`
- `ClaudeMemory/02-Projects/Dpo-ct/conventions.md`
- `ClaudeMemory/02-Projects/Dpo-ct/decisions.md` si ce fichier existe
- `ClaudeMemory/02-Projects/Dpo-ct/journal.md` si ce fichier existe

Sans ce vault, les sources de vérité sont dans le dépôt : `README.md`,
`CHANGELOG.md`, `JOURNAL.md`.

## Contraintes du skill

- Communiquer et rédiger en français.
- Traiter le skill comme une aide à la décision, jamais comme une source
  autonome de droit positif (RGPD, doctrine CNIL/CEPD).
- Vérifier toute règle reposant sur un texte à la source officielle avant
  conclusion, ou la marquer explicitement comme non vérifiée.
- Revue humaine obligatoire avant toute sortie externe (réponse à un
  administré, mention d'information publiée, notification CNIL, courrier à
  un tiers) — `SKILL.md` §8, indépendamment du marquage `[INCOMPLET]`.
- Ne pas déplacer les frontières métier : vidéoprotection opérationnelle →
  `dpm-fpt` ; traitements RH statutaires → `drh-fpt`.
- Ne pas réécrire l'historique des décisions ; ajouter une entrée qui
  supersède la précédente (`JOURNAL.md`, `CHANGELOG.md`).

## État du dépôt

Ce dépôt est un **versement à l'identique** de la copie du skill déployée sur
le compte de l'auteur (v0.2.1, 2026-07-22), sans retouche de fond. Aucun
script de validation ni CI n'existe encore : c'est un chantier distinct,
non engagé lors de la création du dépôt (2026-09-17).
