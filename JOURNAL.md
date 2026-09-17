# Journal des cas — dpo-ct

> Matière première de l'amélioration du skill. À chaque échange significatif,
> consigner ce qui mérite d'être intégré dans une future version. **Aucune
> donnée nominative** (agent, administré ou tiers) : décrire les cas de façon
> anonymisée.

## Comment consigner

Une entrée par cas, au format ci-dessous.

```
### AAAA-MM-JJ — [titre court]
- Type : lacune | erreur | cas nouveau | écrit récurrent
- Branche : analyse-situation | aipd | droits-personnes | gouvernance-registre
  | relations-cnil | secteur-collectivites | securite-traitements |
  sous-traitance-transferts | violations | (posture)
- Contexte (anonymisé) : ...
- Constat : ce qui a manqué ou mal fonctionné.
- Action proposée : ce qu'il faudrait ajouter/corriger, et dans quel fichier.
- Statut : à traiter | intégré (vX.Y.Z)
```

## Entrées

### 2026-09-17 — Création du dépôt versionné
- Type : cas nouveau
- Branche : (transverse) — gouvernance du dépôt
- Contexte (anonymisé) : le skill `dpo-ct` (v0.2.1) n'existait que comme
  copie synchronisée sur le compte de l'auteur, sans dépôt Git : aucun
  historique, aucune réversibilité, aucun audit possible. Le constat est
  survenu à l'occasion de la planification d'un plugin Claude Code
  regroupant les skills métier de la fonction publique territoriale
  (`dpm-fpt`, `drh-fpt`, `dpo-ct`, `DirFi-fpt`), qui suppose que chaque
  skill embarqué ait sa propre source de vérité versionnée.
- Constat : un skill de conformité RGPD sans dépôt est un risque en soi —
  il ne peut être ni corrigé de façon traçable, ni audité, ni comparé d'une
  version à l'autre.
- Action : création de ce dépôt par versement à l'identique de la copie
  déployée (v0.2.1), sans retouche de fond. Gouvernance reprise du patron
  `Dpm-fpt` (`README.md`, `CHANGELOG.md`, `JOURNAL.md`, `AGENTS.md`).
- Statut : intégré (v0.2.1) — aucun audit de fond réalisé à ce stade ; c'est
  un chantier distinct, non engagé ici.
