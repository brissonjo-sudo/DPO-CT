"""Validation statique reproductible du dépôt dpo-ct (stdlib uniquement)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_DIRS = ("references", "assets")
EXPECTED_REFERENCE_FILES = 11  # dont _gabarit-branche.md
EXPECTED_ASSET_FILES = 6
DESCRIPTION_MAX = 1024
FRONTMATTER_KEYS = ("name", "description", "metadata")
ANCHOR = "## 1. Déclenchement"

# Skills voisins qui doivent être nommés dans SKILL.md (frontières §5.4).
EXPECTED_BOUNDARIES = (
    "recherche-juridique",
    "dpm-fpt",
    "drh-fpt",
    "dsi-fpt",
    "dirfi-fpt",
    "dcp-fpt",
)

# Noms des dépôts voisins : un chemin de fichier qui commence par l'un d'eux
# n'existe que dans un clonage multi-dépôts à plat. On nomme le skill voisin,
# jamais le chemin d'un de ses fichiers.
SIBLING_REPO_NAMES = frozenset(
    {
        "dpm-fpt",
        "drh-fpt",
        "dpo-ct",
        "dirfi-fpt",
        "dsi-fpt",
        "dcp-fpt",
        "droit-francais-skill",
    }
)

FORBIDDEN_PATTERNS = {
    "renvoi vers un skill encore « futur »": re.compile(
        r"futurs? skills?", re.IGNORECASE
    ),
}


class Validation:
    """Collecte les erreurs sans interrompre les contrôles suivants."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.checks = 0

    def require(self, condition: bool, message: str) -> None:
        """Enregistre une exigence et son éventuel échec."""
        self.checks += 1
        if not condition:
            self.errors.append(message)


def read_text(path: Path) -> str:
    """Lit un fichier UTF-8."""
    return path.read_text(encoding="utf-8")


def split_frontmatter(text: str) -> tuple[str, str]:
    """Sépare le frontmatter YAML du corps. Renvoie ('', texte) s'il manque."""
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return "", text
    return match.group(1), text[match.end():]


def frontmatter_keys(front: str) -> list[str]:
    """Clés de premier niveau du frontmatter."""
    return re.findall(r"(?m)^([A-Za-z_][\w-]*):", front)


def frontmatter_description(front: str) -> str:
    """Description repliée sur une ligne (bloc `>-`)."""
    match = re.search(r"(?m)^description:\s*>-?\n((?:[ \t]+.*\n?)+)", front + "\n")
    if not match:
        return ""
    return " ".join(line.strip() for line in match.group(1).splitlines())


def frontmatter_version(front: str) -> str | None:
    """Version déclarée dans `metadata.version`."""
    match = re.search(r"(?m)^[ \t]+version:\s*(\S+)\s*$", front)
    return match.group(1) if match else None


def runtime_markdown_files(root: Path) -> list[Path]:
    """SKILL.md et tous les fichiers Markdown du runtime."""
    files = [root / "SKILL.md"]
    for name in RUNTIME_DIRS:
        files.extend(sorted((root / name).glob("*.md")))
    return [path for path in files if path.is_file()]


def validate_frontmatter(validation: Validation, root: Path) -> str | None:
    """Contrôle le frontmatter ; renvoie la version déclarée."""
    path = root / "SKILL.md"
    validation.require(path.is_file(), "SKILL.md absent")
    if not path.is_file():
        return None
    front, _ = split_frontmatter(read_text(path))
    validation.require(bool(front), "SKILL.md : frontmatter absent")
    keys = frontmatter_keys(front)
    unknown = [key for key in keys if key not in FRONTMATTER_KEYS]
    validation.require(
        not unknown, f"SKILL.md : clés de frontmatter non autorisées {unknown}"
    )
    validation.require(
        re.search(r"(?m)^name:\s*dpo-ct\s*$", front) is not None,
        "SKILL.md : `name: dpo-ct` attendu",
    )
    description = frontmatter_description(front)
    validation.require(bool(description), "SKILL.md : description absente")
    validation.require(
        len(description) <= DESCRIPTION_MAX,
        f"SKILL.md : description trop longue ({len(description)} > {DESCRIPTION_MAX})",
    )
    return frontmatter_version(front)


def validate_versions(validation: Validation, root: Path, version: str | None) -> None:
    """La version est la même dans SKILL.md, CHANGELOG et l'index du vault."""
    validation.require(version is not None, "SKILL.md : metadata.version absente")
    if version is None:
        return
    skill = read_text(root / "SKILL.md")
    validation.require(
        re.search(rf"(?m)^# Skill : dpo-ct \(v{re.escape(version)}\)$", skill) is not None,
        f"SKILL.md : titre `# Skill : dpo-ct (v{version})` attendu",
    )
    changelog = root / "CHANGELOG.md"
    validation.require(changelog.is_file(), "CHANGELOG.md absent")
    if changelog.is_file():
        first = re.search(r"(?m)^## \[([^\]]+)\]", read_text(changelog))
        validation.require(
            first is not None and first.group(1) == version,
            f"CHANGELOG.md : l'entrée la plus récente doit être [{version}]",
        )
    index = root / "vault" / "index-dpo-ct.md"
    validation.require(index.is_file(), "vault/index-dpo-ct.md absent")
    if index.is_file():
        validation.require(
            re.search(rf"(?m)^version:\s*{re.escape(version)}\s*$", read_text(index))
            is not None,
            f"vault/index-dpo-ct.md : version {version} attendue",
        )


def validate_inventory(validation: Validation, root: Path) -> None:
    """Nombre exact de fichiers de référence et de générateurs."""
    references = sorted((root / "references").glob("*.md"))
    assets = sorted((root / "assets").glob("*.md"))
    validation.require(
        len(references) == EXPECTED_REFERENCE_FILES,
        f"references/ : {EXPECTED_REFERENCE_FILES} fichiers attendus, {len(references)} trouvés",
    )
    validation.require(
        len(assets) == EXPECTED_ASSET_FILES,
        f"assets/ : {EXPECTED_ASSET_FILES} fichiers attendus, {len(assets)} trouvés",
    )


def validate_boundaries(validation: Validation, root: Path) -> None:
    """Frontières nommées, ancre unique, aucun renvoi « futur skill »."""
    skill = read_text(root / "SKILL.md")
    for name in EXPECTED_BOUNDARIES:
        validation.require(
            f"`{name}`" in skill or f"({name})" in skill or f" {name}" in skill,
            f"SKILL.md : frontière `{name}` non nommée",
        )
    validation.require(
        skill.count(ANCHOR) == 1,
        f"SKILL.md : l'ancre `{ANCHOR}` doit apparaître une seule fois "
        f"(surcharge du plugin), trouvée {skill.count(ANCHOR)} fois",
    )
    for path in runtime_markdown_files(root):
        text = read_text(path)
        for label, pattern in FORBIDDEN_PATTERNS.items():
            validation.require(
                pattern.search(text) is None,
                f"{path.relative_to(root)} : {label}",
            )


def extract_markdown_targets(text: str) -> set[str]:
    """Chemins Markdown locaux cités dans le contenu."""
    targets = set(re.findall(r"`([^`\n]+\.md(?:#[^`\n]+)?)`", text))
    targets.update(re.findall(r"\[[^\]]+\]\(([^)\n]+\.md(?:#[^)\n]+)?)\)", text))
    return targets


def target_exists(root: Path, source: Path, target: str) -> bool:
    """Résout un lien selon les conventions du dépôt."""
    clean = target.split("#", 1)[0].replace("\\", "/")
    if not clean or "*" in clean or clean.startswith(("http://", "https://")):
        return True
    candidates = (
        source.parent / clean,
        root / clean,
        root / "references" / clean,
        root / "assets" / clean,
    )
    return any(candidate.resolve().is_file() for candidate in candidates)


def sibling_repo_pointer(target: str) -> str | None:
    """Nom du dépôt voisin visé par un chemin, ou None."""
    clean = target.split("#", 1)[0].replace("\\", "/")
    if "/" not in clean:
        return None
    head = clean.split("/", 1)[0]
    return head if head.lower() in SIBLING_REPO_NAMES else None


def validate_links(validation: Validation, root: Path) -> None:
    """Liens internes résolus, aucun pointeur vers un dépôt voisin."""
    for path in runtime_markdown_files(root):
        for target in sorted(extract_markdown_targets(read_text(path))):
            sibling = sibling_repo_pointer(target)
            validation.require(
                sibling is None,
                f"{path.relative_to(root)} : pointeur inter-dépôts interdit "
                f"({target}) — nommer le skill `{sibling}`, jamais le chemin d'un "
                "de ses fichiers",
            )
            if sibling is not None:
                continue
            validation.require(
                target_exists(root, path, target),
                f"{path.relative_to(root)} : lien local introuvable ({target})",
            )


def validate(root: Path = ROOT) -> Validation:
    """Exécute tous les contrôles sur le dépôt `root`."""
    validation = Validation()
    version = validate_frontmatter(validation, root)
    validate_versions(validation, root, version)
    validate_inventory(validation, root)
    validate_boundaries(validation, root)
    validate_links(validation, root)
    return validation


def main() -> int:
    """Retourne un code compatible CI."""
    validation = validate()
    if validation.errors:
        for error in validation.errors:
            print(f"[FAIL] {error}")
        print(f"[FAIL] {len(validation.errors)} erreur(s), {validation.checks} contrôles")
        return 1
    print(f"[OK] {validation.checks} contrôles statiques réussis")
    return 0


if __name__ == "__main__":
    sys.exit(main())
