# CHANGELOG — dpo-ct

Versionnage sémantique MAJEUR.MINEUR.PATCH.

## [0.2.1] — 2026-07-22

### Contexte
Deux points soulevés en revue : conformité à la politique d'usage
d'Anthropic (domaines à haut risque, dont le juridique) et taille des
fichiers de référence les plus consultés.

### Modifié
- `SKILL.md` §8 : ajout de la règle « revue humaine obligatoire avant sortie
  externe » — tout document quittant la collectivité (réponse à un
  administré, mention d'information publiée, notification CNIL, courrier à
  un tiers) doit être relu et validé par le DPO humain avant envoi, y
  compris quand le skill ne l'a pas marqué `[INCOMPLET]`. Complète le
  garde-fou « conseil, pas décision » côté exigence de relecture humaine
  (politique d'usage Anthropic, domaines à haut risque).
- `references/secteur-collectivites.md` : ajout d'une table des matières en
  tête de fichier (350 lignes, la branche la plus longue) pour permettre de
  lire directement la famille de traitement concernée (§5.x) sans relire
  l'intégralité du fichier à chaque cas.
- `references/socle-sources-verification.md` : ajout d'un accès rapide
  distinguant le cas courant (§6+§7 seulement) du cas de fond (§1+§4), ce
  fichier étant consulté dans la quasi-totalité des cas.

### Mesure de comparaison (taille)
dpo-ct : 3696 lignes au total (SKILL.md + references + assets), à comparer
à drh-fpt (2395 lignes) et dpm-fpt (11585 lignes) dans le même écosystème —
taille proportionnée, pas hors norme. SKILL.md lui-même reste sous le seuil
recommandé de 500 lignes (376, puis +8 pour ce correctif).

## [0.2.0] — 2026-07-22

### Contexte
Version issue de la batterie de tests « sujets compliqués » (10 cas, agents
en contexte frais) : 59/60, 0 hallucination de référence. Comparatif Gemini
via bundle : 39/60, 3 hallucinations. Correctifs ciblés sur les manques
observés.

### Modifié
- `references/gouvernance-registre.md` (§5.2 Positionnement et moyens) :
  le seul point perdu de la batterie (cas 9, cumul DPO/adjoint DSI) —
  ajout de la référence explicite aux lignes directrices G29/CEPD WP243
  (fonctions incompatibles, « responsable du service informatique » cité)
  et d'une règle « précédents de sanction » : signaler leur existence et
  les rechercher en session, jamais de numéro de décision de mémoire
  (l'attribution erronée d'une jurisprudence étant l'erreur la plus
  dommageable observée chez les IA testées sans discipline de sourcing).
- Bundle autoportant (hors paquet) : bloc « instructions à coller » séparé
  du fichier de connaissance, portant la règle dure de sourcing — leçon du
  test Gemini, qui ignorait la règle noyée dans le fichier joint.

## [0.1.0] — 2026-07-22

### Ajouté
- Version initiale du skill, architecture en 3 couches sur le modèle
  `dpm-fpt` / `drh-fpt` :
  - Couche 1 — Decision Engine : `references/analyse-situation.md`
    (qualification du traitement, garde-fou double régime RGPD /
    Police-Justice, désignation du responsable de traitement).
  - Couche 2 — 8 branches métier : gouvernance & registre, AIPD, violations,
    droits des personnes, sous-traitance & transferts, sécurité des
    traitements, traitements sectoriels des collectivités, relations CNIL.
  - Couche 3 — 6 générateurs interactifs : avis DPO, AIPD, fiche de registre,
    notification de violation, réponse à une demande de droits, mention
    d'information.
- Deux garde-fous métier : « conseil, pas décision » (rôle consultatif du
  DPO) et « double régime » (RGPD vs directive Police-Justice).
- Socle-sources autonome (RGPD, loi 78-17, doctrine CNIL/CEPD datée) avec
  règle de provenance des identifiants.
- Frontières documentées avec `recherche-juridique`, `dpm-fpt`, `drh-fpt` et
  les futurs skills DSI et finances (`SKILL.md` §5.4).
