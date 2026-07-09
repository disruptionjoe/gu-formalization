#!/usr/bin/env python3
"""Audit the public reproduction harness discovery scope.

This is a process gate, not a mathematical certificate. It checks that
scripts/reproduce_all.py sweeps the intended certificate roots without pulling
governance gates, caches, or local operation records into the public
reproduction run.
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import subprocess
import unittest
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
HARNESS = ROOT / "scripts" / "reproduce_all.py"
TESTS_DIR = ROOT / "tests"
PROCESS_GATES_DIR = ROOT / "process_gates"
SKIP_DIR_NAMES = {"__pycache__", ".cache", ".pytest_cache", ".git", "hourly-cycles"}


def load_harness() -> ModuleType:
    spec = importlib.util.spec_from_file_location("gu_reproduce_all", HARNESS)
    if spec is None or spec.loader is None:
        raise AssertionError(f"could not load {HARNESS}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expected_python_files(root: Path) -> set[Path]:
    if not root.is_dir():
        return set()
    files: set[Path] = set()
    for path in root.rglob("*.py"):
        rel_parts = path.relative_to(root).parts
        if path.name == "__init__.py":
            continue
        if any(part in SKIP_DIR_NAMES for part in rel_parts):
            continue
        files.add(path.resolve())
    return files


def expected_tracked_python_files(roots: list[Path]) -> set[Path]:
    pathspecs = [
        relpath(root).rstrip("/")
        for root in roots
        if root.is_dir()
    ]
    if not pathspecs:
        return set()

    result = subprocess.run(
        ["git", "ls-files", "-z", "--", *pathspecs],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stderr.strip() or "git ls-files failed")

    files: set[Path] = set()
    for rel in result.stdout.split("\0"):
        if not rel or not rel.endswith(".py") or Path(rel).name == "__init__.py":
            continue
        parts = Path(rel).parts
        if any(part in SKIP_DIR_NAMES for part in parts):
            continue
        files.add((ROOT / rel).resolve())
    return files


def discovered_paths(module: ModuleType, roots: list[str], tracked_only: bool = False) -> set[Path]:
    return {Path(path).resolve() for path in module.discover(roots, tracked_only=tracked_only)}


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


class ReproduceHarnessScopeAudit(unittest.TestCase):
    def test_quick_scope_matches_live_tests_tree(self) -> None:
        module = load_harness()

        discovered = discovered_paths(module, [module.TESTS_DIR])
        expected = expected_python_files(TESTS_DIR)

        self.assertGreaterEqual(len(discovered), 1)
        self.assertEqual(
            sorted(relpath(path) for path in expected),
            sorted(relpath(path) for path in discovered),
        )

    def test_full_scope_adds_only_declared_paper_certificate_roots(self) -> None:
        module = load_harness()

        quick = discovered_paths(module, [module.TESTS_DIR])
        full = discovered_paths(module, [module.TESTS_DIR, *module.PAPER_CERT_DIRS])
        paper_roots = [Path(root).resolve() for root in module.PAPER_CERT_DIRS]
        expected_paper = set().union(*(expected_python_files(root) for root in paper_roots))

        self.assertTrue(quick.issubset(full))
        self.assertGreaterEqual(len(expected_paper), 1)
        self.assertEqual(
            sorted(relpath(path) for path in expected_paper),
            sorted(relpath(path) for path in full - quick),
        )

    def test_tracked_only_scope_matches_git_tracked_tests_tree(self) -> None:
        module = load_harness()

        discovered = discovered_paths(module, [module.TESTS_DIR], tracked_only=True)
        expected = expected_tracked_python_files([TESTS_DIR])
        default_scope = discovered_paths(module, [module.TESTS_DIR])

        self.assertGreaterEqual(len(discovered), 1)
        self.assertTrue(discovered.issubset(default_scope))
        self.assertEqual(
            sorted(relpath(path) for path in expected),
            sorted(relpath(path) for path in discovered),
        )

    def test_process_gates_and_skip_directories_are_out_of_certificate_scope(self) -> None:
        module = load_harness()

        full = discovered_paths(module, [module.TESTS_DIR, *module.PAPER_CERT_DIRS])
        for path in full:
            rel_parts = path.relative_to(ROOT).parts
            self.assertNotIn(PROCESS_GATES_DIR.name, rel_parts, relpath(path))
            self.assertFalse(any(part in SKIP_DIR_NAMES for part in rel_parts), relpath(path))

    def test_list_mode_prints_repository_relative_slash_paths(self) -> None:
        module = load_harness()

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exit_code = module.main([
                "--quick",
                "--tracked-only",
                "--list",
                "-k",
                "tests/pati-salam",
            ])

        self.assertEqual(0, exit_code)
        lines = [line.strip() for line in output.getvalue().splitlines() if line.strip()]
        certificate_lines = [line for line in lines if line.startswith("tests/")]

        self.assertEqual(["tests/pati-salam/run_pati_salam_chain_checks.py"], certificate_lines)
        self.assertIn("tracked only", output.getvalue())
        for line in certificate_lines:
            self.assertFalse(Path(line).is_absolute(), line)
            self.assertNotIn("\\", line)
            self.assertNotIn(str(ROOT), line)

    def test_filter_matches_repository_relative_paths_only(self) -> None:
        module = load_harness()

        quick_tracked = module.discover([module.TESTS_DIR], tracked_only=True)
        matched = module.filter_certificates(quick_tracked, "tests/pati-salam")

        self.assertEqual(
            ["tests/pati-salam/run_pati_salam_chain_checks.py"],
            sorted(relpath(Path(path)) for path in matched),
        )
        self.assertEqual([], module.filter_certificates(quick_tracked, ROOT.as_posix()))
        self.assertEqual([], module.filter_certificates(quick_tracked, str(ROOT).replace("\\", "/")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
