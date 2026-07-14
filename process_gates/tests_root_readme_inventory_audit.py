#!/usr/bin/env python3
"""Audit the loose root tests/README.md script inventory.

This is a publication-manifest hygiene gate, not a mathematical certificate.
It keeps the root-level `tests/*.py` sector map synchronized with the tracked
root test scripts after governance/process gates moved under `process_gates/`.
"""

from __future__ import annotations

import fnmatch
import re
import subprocess
import unittest
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "tests" / "README.md"

README_ROW = re.compile(
    r"^\| \*\*(?P<label>[^*]+)\*\* \| (?P<tokens>[^|]+) \| (?P<count>\d+) \|",
    re.MULTILINE,
)
CODE_SPAN = re.compile(r"`([^`]+)`")


@dataclass(frozen=True)
class CoverageGroup:
    label: str
    patterns: tuple[str, ...]


COVERAGE_GROUPS: tuple[CoverageGroup, ...] = (
    CoverageGroup("RS / BV-BRST sector", ("rs_*.py",)),
    CoverageGroup("shiab selector / codifferential", ("shiab_*.py",)),
    CoverageGroup("Cycle audits", ("cycle1_*.py", "cycle2_*.py")),
    CoverageGroup(
        "Generation count & K3",
        (
            "gen_*.py",
            "sp64_octic_trace_i16.py",
            "ahat_genus_y14_i16.py",
            "c2_holonomy_*.py",
        ),
    ),
    CoverageGroup("Bell / QFT / measurement", ("h3_*.py", "h3-*.py")),
    CoverageGroup("Velo-Zwanziger", ("vz_*.py",)),
    CoverageGroup(
        "GR / cosmology / dark energy",
        ("theta_flrw_desi_sign.py", "willmore_el_schwarzschild_order.py"),
    ),
    CoverageGroup("Source / selector / control", ("oq_rk1_*.py",)),
    CoverageGroup(
        "Temporal issuance / source-action steelman",
        ("temporal_issuance_source_action_steelmen_checker.py",),
    ),
    CoverageGroup("W-series frontier packets", ("W*.py",)),
)


def run_git_ls_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "tests"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stderr.strip() or "git ls-files tests failed")
    return [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]


def tracked_direct_root_test_scripts() -> set[str]:
    scripts: set[str] = set()
    for relpath in run_git_ls_files():
        path = Path(relpath)
        if path.parent.as_posix() == "tests" and path.suffix == ".py":
            scripts.add(path.name)
    return scripts


def matches(group: CoverageGroup, script_name: str) -> bool:
    return any(fnmatch.fnmatchcase(script_name, pattern) for pattern in group.patterns)


def readme_rows(text: str) -> dict[str, tuple[tuple[str, ...], int]]:
    rows: dict[str, tuple[tuple[str, ...], int]] = {}
    for match in README_ROW.finditer(text):
        label = match.group("label")
        tokens = tuple(CODE_SPAN.findall(match.group("tokens")))
        rows[label] = (tokens, int(match.group("count")))
    return rows


class TestsRootReadmeInventoryAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = README.read_text(encoding="utf-8")
        cls.root_scripts = tracked_direct_root_test_scripts()
        cls.rows = readme_rows(cls.text)

    def test_readme_table_declares_expected_groups_and_patterns(self) -> None:
        expected = {group.label: group.patterns for group in COVERAGE_GROUPS}
        documented = {label: tokens for label, (tokens, _) in self.rows.items()}
        self.assertEqual(expected, documented)

    def test_readme_counts_match_tracked_root_scripts(self) -> None:
        mismatches: list[str] = []
        for group in COVERAGE_GROUPS:
            _, documented_count = self.rows[group.label]
            actual_count = sum(1 for script in self.root_scripts if matches(group, script))
            if documented_count != actual_count:
                mismatches.append(
                    f"{group.label}: README says {documented_count}, actual {actual_count}"
                )

        self.assertEqual([], mismatches)
        self.assertEqual(len(self.root_scripts), sum(count for _, count in self.rows.values()))

    def test_every_tracked_root_script_has_exactly_one_group(self) -> None:
        classification_errors: list[str] = []
        for script in sorted(self.root_scripts):
            labels = [group.label for group in COVERAGE_GROUPS if matches(group, script)]
            if len(labels) != 1:
                rendered = ", ".join(labels) if labels else "none"
                classification_errors.append(f"{script}: {rendered}")

        self.assertEqual([], classification_errors)

    def test_helpers_classify_representative_scripts(self) -> None:
        group = CoverageGroup("sample", ("alpha_*.py", "beta.py"))
        self.assertTrue(matches(group, "alpha_one.py"))
        self.assertTrue(matches(group, "beta.py"))
        self.assertFalse(matches(group, "gamma.py"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
