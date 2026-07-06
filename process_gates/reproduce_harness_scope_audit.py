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


def discovered_paths(module: ModuleType, roots: list[str]) -> set[Path]:
    return {Path(path).resolve() for path in module.discover(roots)}


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
            exit_code = module.main(["--quick", "--list", "-k", "tests/pati-salam"])

        self.assertEqual(0, exit_code)
        lines = [line.strip() for line in output.getvalue().splitlines() if line.strip()]
        certificate_lines = [line for line in lines if line.startswith("tests/")]

        self.assertEqual(["tests/pati-salam/run_pati_salam_chain_checks.py"], certificate_lines)
        for line in certificate_lines:
            self.assertFalse(Path(line).is_absolute(), line)
            self.assertNotIn("\\", line)
            self.assertNotIn(str(ROOT), line)


if __name__ == "__main__":
    unittest.main(verbosity=2)
