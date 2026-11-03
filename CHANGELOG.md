# CHANGELOG — dpo-ct

Versionnage sémantique MAJEUR.MINEUR.PATCH.

## [0.2.3] — 2026-11-03

### Contexte
Veille juridique delta du 2026-09-17 au 2026-11-03. Sources lues sur
Légifrance le 2026-11-03 : loi 78-17, art. 22 (LEGIARTI000054928123, version
du 2026-10-01) ; décision CC n° 2025-1154 QPC du 8 août 2025
(CONSTEXT000052086215) ; CSI, art. R. 253-6 (LEGIARTI000048476439, version
du 2023-11-30) ; loi 78-17, art. 105, 107, 108 (LEGIARTI000037817686,
...690, ...692) ; CE 16/10/2026 n° 499597 (CETATEXT000054993121) et CE
20/10/2026 n° 511156 (CETATEXT000055005485), tous deux inédits au recueil
Lebon.

### Modifié
- `references/relations-cnil.md` : procédure de sanction — droit de se
  taire devant la formation restreinte, art. 22 modifié au 2026-10-01,
  CE n° 499597 ; déclencheur de vérification précisé.
- `references/droits-personnes.md` : **correction** — sous le titre III, les
  droits s'exercent directement auprès du responsable ; la voie CNIL n'est
  ouverte qu'en cas de restriction (§4, §5.9). Nouveau §5.10 (personnes
  filmées, CSI R. 253-6) ; CE n° 511156 au §5.2 (accès et données non
  conservées).
- `references/secteur-collectivites.md` §5.6, `references/analyse-situation.md`
  §1 et §2 : renvois à R. 253-6 (information du public, droits).
- `references/socle-sources-verification.md` : R. 253-6 au noyau (§3) ;
  §8 « Revues datées » (veille du 2026-11-03).
- `tests/test_validate_repo.py` : version de référence du test de
  désalignement.

### Non intégré
Lignes directrices CEPD 04/2026 (en consultation jusqu'au 2026-11-13) et
avis CNIL du 2026-10-01 sur des projets de texte : pas du droit positif.

### Inchangé
Ancre `## 1. Déclenchement` conservée. Version **non mesurée** : aucune
campagne rejouée. Le skill doit être ré-épinglé dans le plugin.

## Non publié : licence EUPL 1.2 (2026-11-01)

### Contexte
Le dépôt ne comportait aucun fichier ni mention de licence. Il est désormais
diffusé sous licence publique de l'Union européenne (EUPL) 1.2.

### Ajouté
- `LICENSE` : texte officiel anglais de l'EUPL 1.2 (Commission européenne),
  précédé de la mention de copyright.
- `LICENCE.fr.txt` : texte officiel français de l'EUPL 1.2.
- `README.md` : section « Licence ».

### Inchangé
Versions antérieures inchangées : aucune réécriture de l'historique. Aucun
changement de comportement du skill.

## [0.2.2] — 2026-10-07

### Contexte
`dsi-fpt`, `dirfi-fpt` et `dcp-fpt` existent désormais. `dpo-ct` renvoyait
encore vers un « futur skill DSI » et un « futur skill finances », et traitait
le droit de la commande publique comme « hors skill ».

### Modifié
- `SKILL.md` : `description` (exclusions `dsi-fpt` et `dcp-fpt`, 1 002
  caractères), dépendances, table des frontières §5.4 (ligne **commande
  publique**), hiérarchie de co-activation §5.5, auto-vérification §7, règle
  de repli (skill nommé absent : signaler la limite et s'arrêter).
- `references/securite-traitements.md` : renvoi `dsi-fpt` ; la DSI fournit les
  mesures techniques de l'AIPD, le DPO la conduit.
- `references/sous-traitance-transferts.md` : renvoi `dcp-fpt` pour le fond de
  la passation, de l'exécution et de la modification du marché.
- `README.md` : écosystème à jour.

### Ajouté
- `scripts/validate_repo.py`, `tests/test_validate_repo.py` et
  `.github/workflows/validate.yml` : validation statique en CI.
- `.gitattributes` (fins de ligne LF, repris des dépôts frères), `vault/`.

### Inchangé
Aucun changement de fond RGPD, aucune nouvelle référence juridique. L'ancre
`## 1. Déclenchement` est conservée (surcharge d'instructions du plugin).
Version **non mesurée** : aucune campagne n'a été rejouée.

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
