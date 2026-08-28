#!/usr/bin/env python3
"""Coupled fail-closed probe for reproduction and status integrity."""

from __future__ import annotations

import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ReproductionStatusIntegrityWaveProbe(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.status = load_module(
            "frontmatter_status_schema_audit",
            ROOT / "process_gates" / "frontmatter_status_schema_audit.py",
        )
        cls.scope = load_module(
            "reproduce_harness_scope_audit",
            ROOT / "process_gates" / "reproduce_harness_scope_audit.py",
        )
        cls.harness = cls.scope.load_harness()

    def test_clean_status_baseline(self) -> None:
        self.assertEqual([], self.status.audit())

    def test_clean_reproduction_scope_baseline(self) -> None:
        suite = unittest.defaultTestLoader.loadTestsFromModule(self.scope)
        result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
        self.assertTrue(result.wasSuccessful())

    def test_nested_process_gate_certificate_is_discovered(self) -> None:
        nested = (ROOT / "tests" / "process_gates" / "candidate_citation_custody.py").resolve()
        discovered = {
            Path(path).resolve()
            for path in self.harness.discover([self.harness.TESTS_DIR])
        }
        self.assertIn(nested, discovered)

    def test_three_status_reference_mutations_are_caught(self) -> None:
        original_manifest = self.status.MANIFEST
        mutations = []
        for field in ("tracked_markdown", "status_bearing"):
            mutant = yaml.safe_load(original_manifest.read_text())
            mutant["counts"][field] -= 1
            mutations.append(mutant)
        mutant = yaml.safe_load(original_manifest.read_text())
        mutant["mapping_digest_sha256"] = "0" * 64
        mutations.append(mutant)

        caught = 0
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "manifest.yaml"
            try:
                for mutation in mutations:
                    path.write_text(yaml.safe_dump(mutation, sort_keys=False))
                    self.status.MANIFEST = path
                    if self.status.audit():
                        caught += 1
            finally:
                self.status.MANIFEST = original_manifest
        self.assertEqual(3, caught)

    def test_global_process_gates_pruning_mutation_is_caught(self) -> None:
        nested = (ROOT / "tests" / "process_gates" / "candidate_citation_custody.py").resolve()
        original = self.harness.SKIP_DIR_FRAGMENTS
        try:
            self.harness.SKIP_DIR_FRAGMENTS = (*original, "process_gates")
            discovered = {
                Path(path).resolve()
                for path in self.harness.discover([self.harness.TESTS_DIR])
            }
        finally:
            self.harness.SKIP_DIR_FRAGMENTS = original
        self.assertNotIn(nested, discovered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
