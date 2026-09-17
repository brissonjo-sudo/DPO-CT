# dpo-ct — DPO en collectivité territoriale

Système expert d'aide à la décision pour un **Délégué à la Protection des
Données** de collectivité territoriale française (commune, EPCI).

## Ce que fait le skill

- Avis DPO sur un projet, un traitement, un marché, un logiciel.
- AIPD : opportunité et réalisation (méthode CNIL), consultation préalable.
- Registre des activités de traitement (art. 30) : création et mise à jour.
- Violations de données : qualification, registre, notification CNIL (72 h),
  communication aux personnes.
- Droits des personnes : instruction des demandes, délais, refus motivés.
- Sous-traitance (art. 28), transferts hors UE, clauses des marchés publics.
- Sécurité des traitements (art. 32) — exigences de conformité.
- Traitements sectoriels : état civil, élections, scolaire, action sociale,
  vidéoprotection (volet données), téléservices, open data, archives.
- Relations CNIL : plainte, contrôle, mise en demeure.

## Architecture

```
dpo-ct/
├── SKILL.md                  Posture, garde-fous, routeur, auto-vérification
├── references/
│   ├── analyse-situation.md  Couche 1 — Decision Engine (lire en premier)
│   ├── _gabarit-branche.md   Gabarit de conception des branches
│   ├── socle-sources-verification.md
│   └── <8 branches métier>   Couche 2
└── assets/                   Couche 3 — générateurs interactifs de livrables
```

## Écosystème

Complémentaire de : `recherche-juridique` (validation de vigueur et
citation), `dpm-fpt` (police municipale — frontière vidéoprotection),
`drh-fpt` (RH statutaire — frontière traitements RH), et des futurs skills
**DSI** (mise en œuvre technique de la sécurité) et **finances**.
Les frontières sont documentées dans `SKILL.md` §5.4.

## Maintenance

Voir `SKILL.md` §9 (JOURNAL, CHANGELOG, revue de rentrée du 1er septembre).
