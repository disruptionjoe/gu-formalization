#!/usr/bin/env python3
"""Audit the public README entrypoint map.

This is a process/documentation gate, not a research-content check. It keeps the
root README's Start Here pointers and Repository Layers map complete and
non-duplicative so the public entrypoint does not drift as repo surfaces evolve.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

START_HERE_REQUIRED = (
    "RESEARCH-PROGRAM.md",
    "papers/candidates/located-not-forced/",
    "RESEARCH-POSTURE.md",
    "CANON.md",
    "RESEARCH-STATUS.md",
    "lab/roadmap/tri-repo-division-of-labor-2026-07-02.md",
    "NEXT-STEPS.md",
    "docs/OVERVIEW.md",
    "papers/candidates/six-axis-testability/",
)

TOP_LEVEL_LAYER_BULLETS = (
    "papers",
    "canon",
    "tests",
    "explorations",
    "docs",
)

REQUIRED_LAYER_CONTEXT = (
    "lab/README.md",
    "Lean/",
)


def readme_text() -> str:
    return README.read_text(encoding="utf-8")


def section(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^## {re.escape(heading)}\s*$\n(?P<body>.*?)(?=^## |\Z)",
        flags=re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise AssertionError(f"missing section: {heading}")
    return match.group("body")


def bullet_count(section_text: str, layer: str) -> int:
    pattern = re.compile(rf"^- `{re.escape(layer)}/`", flags=re.MULTILINE)
    return len(pattern.findall(section_text))


class ReadmeEntrypointMapAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = readme_text()

    def test_start_here_keeps_current_public_pointers(self) -> None:
        start_here = section(self.text, "Start Here")
        missing = [pointer for pointer in START_HERE_REQUIRED if pointer not in start_here]
        self.assertEqual([], missing)

    def test_repository_layers_have_one_bullet_per_top_level_surface(self) -> None:
        layers = section(self.text, "Repository Layers")
        counts = {layer: bullet_count(layers, layer) for layer in TOP_LEVEL_LAYER_BULLETS}
        self.assertEqual(
            {layer: 1 for layer in TOP_LEVEL_LAYER_BULLETS},
            counts,
        )

    def test_repository_layers_route_non_root_surfaces_without_extra_bullets(self) -> None:
        layers = section(self.text, "Repository Layers")
        missing = [pointer for pointer in REQUIRED_LAYER_CONTEXT if pointer not in layers]
        self.assertEqual([], missing)
        self.assertIn("Everything else", layers)

    def test_current_center_of_gravity_keeps_force_three_narrowing_guard(self) -> None:
        center = section(self.text, "Current Center Of Gravity")
        normalized = " ".join(center.split())
        self.assertIn("information gain about what is true", center)
        self.assertIn("does bare GU force three generations?", normalized)


if __name__ == "__main__":
    unittest.main(verbosity=2)
