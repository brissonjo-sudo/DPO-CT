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
  `dpm-fpt` ; traitements RH statutaires → `drh-fpt` ; mise en œuvre
  technique de la sécurité → `dsi-fpt` ; fond budgétaire et comptable →
  `dirfi-fpt` ; passation et exécution des marchés → `dcp-fpt`.
- Ne jamais citer un fichier d'un dépôt voisin : nommer le skill.
- Garder l'ancre `## 1. Déclenchement` unique dans `SKILL.md` : le plugin
  `collectivite-territoriale` y accroche une surcharge d'instructions.
- Ne pas réécrire l'historique des décisions ; ajouter une entrée qui
  supersède la précédente (`JOURNAL.md`, `CHANGELOG.md`).

## État du dépôt

Dépôt créé le 2026-09-17 par versement à l'identique de la copie déployée
(v0.2.1, 2026-07-22). La v0.2.2 (2026-10-07) met les frontières à jour
(`dsi-fpt`, `dirfi-fpt`, `dcp-fpt`) et ajoute une validation statique
(`scripts/validate_repo.py`, `tests/`, `validate.yml`). Aucune campagne de
mesure n'existe pour ce skill. Une mise à jour de version suppose de
re-épingler le skill dans le plugin : voir `docs/note-plugin-0.2.2.md`.
