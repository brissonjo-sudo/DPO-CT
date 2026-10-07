# Note de passation — ré-épinglage de `dpo-ct` 0.2.2 dans le plugin

Destinataire : la session qui conduit le candidat 1.2.0 de
`collectivite-territoriale` (PR #9). Rien n'est modifié dans le plugin par cette
PR.

## Ce qui change côté plugin

1. `upstream.json`, entrée `dpo-ct` : `commit` = nouveau commit de `main` après
   fusion de la PR `dpo-ct`, `version` = `0.2.2`.
2. Surcharge d'instructions (`overlays/dpo-ct.md`) : le `SKILL.md` a changé,
   donc `base_sha256` doit être **recalculé**. L'ancre `## 1. Déclenchement`
   est inchangée et unique ; à revérifier.
3. `python3 scripts/sync_skills.py` puis `python3 scripts/check_sync.py`.
4. Le titre du `SKILL.md` suit le motif `# Skill : dpo-ct (v0.2.2)`.
5. `CHANGELOG`, `tests/evidence/release-1.2.0.json` : le candidat reste soumis à
   la barrière de release (`upstream_commits` change).

## Points de vigilance

- Les renvois à `dsi-fpt` et `dcp-fpt` n'ont de sens que si ces skills sont
  embarqués dans le même candidat ; sinon la règle de repli s'applique
  (« signaler la limite et s'arrêter »).
- `upstream.json` pointe vers `.../DPO-CT.git`. Si le dépôt est renommé,
  l'ancienne adresse est redirigée par GitHub ; corriger l'URL dans la même PR.
- Aucune campagne n'a été rejouée pour `dpo-ct`.
