#!/usr/bin/env python3
"""Audit tests/threads/README.md inventory and boundary wording.

This is a documentation/process gate. It does not run the thread scripts and
does not evaluate or change their scientific verdicts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THREADS_DIR = ROOT / "tests" / "threads"
README = THREADS_DIR / "README.md"

REQUIRED_BOUNDARY_TERMS = {
    "exploration",
    "canon",
    "claim status",
    "verdicts",
    "public posture",
    "source-action",
    "oq2-a",
    "gimmel/dewitt",
    "a13",
}


def live_direct_scripts() -> set[str]:
    return {
        path.name
        for path in THREADS_DIR.glob("*.py")
        if path.name != "__init__.py"
    }


def documented_thread_script_names(text: str) -> set[str]:
    """Return thread script basenames documented in Markdown code spans."""
    names: set[str] = set()
    for match in re.finditer(r"`([^`]+\.py)`", text):
        raw = match.group(1).replace("\\", "/")
        if "<" in raw or ">" in raw:
            continue
        if "/" in raw and not raw.startswith("tests/threads/"):
            continue
        names.add(Path(raw).name)
    return names


def local_markdown_links(text: str) -> set[str]:
    return {
        target
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
        if "://" not in target and not target.startswith("#")
    }


def missing_boundary_terms(text: str) -> list[str]:
    folded = text.casefold()
    return sorted(term for term in REQUIRED_BOUNDARY_TERMS if term not in folded)


class ThreadsReadmeInventoryAudit(unittest.TestCase):
    def test_readme_names_every_live_direct_thread_script(self) -> None:
        self.assertTrue(README.is_file(), f"missing {README}")
        text = README.read_text(encoding="utf-8")
        live = live_direct_scripts()
        documented = documented_thread_script_names(text)

        self.assertEqual([], sorted(live - documented))

    def test_readme_has_no_stale_direct_script_entries(self) -> None:
        text = README.read_text(encoding="utf-8")
        live = live_direct_scripts()
        documented = documented_thread_script_names(text)
        local_script_names = {
            name
            for name in documented
            if (THREADS_DIR / name).suffix == ".py"
        }

        self.assertEqual([], sorted(local_script_names - live))

    def test_readme_preserves_exploration_and_no_status_boundary(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertEqual([], missing_boundary_terms(text))

    def test_readme_local_markdown_links_resolve(self) -> None:
        text = README.read_text(encoding="utf-8")
        broken = [
            target
            for target in sorted(local_markdown_links(text))
            if not (THREADS_DIR / target).resolve().exists()
        ]
        self.assertEqual([], broken)

    def test_helpers_parse_basename_from_paths(self) -> None:
        text = "`tests/threads/foo.py` and `bar.py` and `process_gates/gate.py`"
        self.assertEqual({"foo.py", "bar.py"}, documented_thread_script_names(text))


if __name__ == "__main__":
    unittest.main(verbosity=2)
