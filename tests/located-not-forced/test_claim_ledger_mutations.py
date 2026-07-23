#!/usr/bin/env python3
"""Mutation tests for the LNF current claim-and-premise ledger."""

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PAPER_DIR = ROOT / "papers/candidates/located-not-forced"
VALIDATOR_PATH = PAPER_DIR / "validate_release_evidence.py"
LEDGER_PATH = PAPER_DIR / "CLAIM-AND-PREMISE-LEDGER.json"
PAPER_PATH = PAPER_DIR / "located-not-forced-generation-count-2026-06-29.md"

spec = importlib.util.spec_from_file_location("lnf_release_validator", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ClaimLedgerMutationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
        self.paper_text = PAPER_PATH.read_text(encoding="utf-8")
        self.current_surface_text = "\n".join(
            (ROOT / path).read_text(encoding="utf-8")
            for path in self.ledger["current_surfaces"]
            if path != "papers/candidates/located-not-forced/CLAIM-AND-PREMISE-LEDGER.json"
        )

    def errors_for(self, ledger: dict) -> list[str]:
        errors: list[str] = []
        validator.validate_claim_ledger(
            ledger,
            ROOT,
            self.paper_text,
            self.current_surface_text,
            errors,
        )
        return errors

    def test_current_ledger_passes(self) -> None:
        self.assertEqual(self.errors_for(self.ledger), [])

    def test_missing_premise_fails(self) -> None:
        mutated = copy.deepcopy(self.ledger)
        mutated["claims"][2]["premises"].append("LNF-PR-999")
        self.assertTrue(any("unknown premise" in error for error in self.errors_for(mutated)))

    def test_full_class_order_three_fails(self) -> None:
        mutated = copy.deepcopy(self.ledger)
        mutated["claims"][6]["statement"] = "The full class has order 3."
        self.assertTrue(any("forbidden formulation" in error for error in self.errors_for(mutated)))

    def test_necessary_externality_fails(self) -> None:
        mutated = copy.deepcopy(self.ledger)
        mutated["claims"][14]["statement"] = "External backgrounds are necessary."
        self.assertTrue(any("forbidden formulation" in error for error in self.errors_for(mutated)))

    def test_family_unit_as_count_fails(self) -> None:
        mutated = copy.deepcopy(self.ledger)
        mutated["claims"][12]["statement"] = "16 // 16 is a generation count."
        self.assertTrue(any("forbidden formulation" in error for error in self.errors_for(mutated)))


if __name__ == "__main__":
    unittest.main()
