#!/usr/bin/env python3
"""Audit tests/big-swing/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the big-swing
certificates and does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BIG_SWING_DIR = ROOT / "tests" / "big-swing"
README = BIG_SWING_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "big-swing",
    "exploration",
    "certificate",
    "not-a-verdict-change",
    "generation count",
    "source action",
    "claim status",
    "verdicts",
    "public posture",
}


def live_direct_certificate_files() -> set[str]:
    return {
        path.name
        for path in BIG_SWING_DIR.iterdir()
        if path.is_file() and path.name.lower() != "readme.md"
    }


def documented_big_swing_file_names(text: str) -> set[str]:
    """Return big-swing certificate basenames documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.(?:py|lean))`", text, flags=re.IGNORECASE):
        raw = match.group(1).replace("\\", "/")
        if "/" in raw and not raw.startswith("tests/big-swing/"):
            continue
        names.add(Path(raw).name)
    return names


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class BigSwingReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_live_direct_big_swing_certificate(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        live = live_direct_certificate_files()
        documented = documented_big_swing_file_names(text)

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_direct_certificate_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_direct_certificate_files()
        documented = documented_big_swing_file_names(text)
        local_certificate_names = {
            name
            for name in documented
            if (BIG_SWING_DIR / name).suffix.lower() in {".py", ".lean"}
        }

        self.assertEqual([], sorted(local_certificate_names - live))

    def test_readme_preserves_exploration_not_verdict_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_helpers_parse_basename_from_paths(self) -> None:
        text = (
            "`tests/big-swing/foo.py` and `bar.lean` "
            "and `process_gates/gate.py`"
        )
        self.assertEqual(
            {"foo.py", "bar.lean"},
            documented_big_swing_file_names(text),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
