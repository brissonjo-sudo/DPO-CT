"""Tests du validateur : le dépôt réel passe, chaque défaut est détecté."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

import validate_repo  # noqa: E402

COPIED = ("SKILL.md", "CHANGELOG.md", "JOURNAL.md", "references", "assets", "vault")


class ValidateRepoTests(unittest.TestCase):
    """Chaque test travaille sur une copie temporaire du dépôt."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        for name in COPIED:
            source = REPO / name
            target = self.root / name
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                shutil.copy2(source, target)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def edit(self, relative: str, old: str, new: str) -> None:
        path = self.root / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def errors(self) -> list[str]:
        return validate_repo.validate(self.root).errors

    def test_depot_reel_valide(self) -> None:
        self.assertEqual(validate_repo.validate(REPO).errors, [])

    def test_copie_intacte_valide(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_futur_skill_reintroduit(self) -> None:
        self.edit("references/securite-traitements.md", "skill `dsi-fpt`", "futur skill DSI")
        self.assertTrue(any("futur" in e for e in self.errors()))

    def test_pointeur_depot_frere(self) -> None:
        self.edit(
            "references/aipd.md",
            "`relations-cnil.md`",
            "`Dsi-fpt/references/securite-si.md`",
        )
        self.assertTrue(any("inter-dépôts" in e for e in self.errors()))

    def test_ancre_dupliquee(self) -> None:
        path = self.root / "SKILL.md"
        path.write_text(
            path.read_text(encoding="utf-8") + "\n## 1. Déclenchement\n",
            encoding="utf-8",
        )
        self.assertTrue(any("ancre" in e for e in self.errors()))

    def test_version_desalignee(self) -> None:
        self.edit("CHANGELOG.md", "## [0.2.2]", "## [0.2.9]")
        self.assertTrue(any("CHANGELOG" in e for e in self.errors()))

    def test_frontiere_non_nommee(self) -> None:
        path = self.root / "SKILL.md"
        text = path.read_text(encoding="utf-8").replace("dcp-fpt", "xxx-fpt")
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("dcp-fpt" in e for e in self.errors()))

    def test_description_trop_longue(self) -> None:
        self.edit("SKILL.md", "la passation des marchés (dcp-fpt)", "x" * 200)
        self.assertTrue(any("description trop longue" in e for e in self.errors()))

    def test_lien_local_casse(self) -> None:
        self.edit("references/aipd.md", "`relations-cnil.md`", "`inexistant.md`")
        self.assertTrue(any("introuvable" in e for e in self.errors()))


if __name__ == "__main__":
    unittest.main()
