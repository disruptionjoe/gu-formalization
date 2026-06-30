#!/usr/bin/env python3
"""Audit CandidateCongruenceGeneratorsForLocalGUPhysicalFieldEquivalence_V1."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1302-cycle1-qft-congruence-generators.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What was derived directly from repo sources",
    "## 3. The strongest positive result",
    "## 4. The first exact obstruction or missing proof object",
    "## 5. The constructive next object that would remove or test the obstruction",
    "## 6. What this means for QFT quotient/restriction, P_raw/P_fin descent, rho_AB, and CHSH work",
    "## 7. Next meaningful proof or computation step",
    "## 8. Machine-readable JSON summary",
]

EXPECTED_GENERATORS = {
    "equation_generators",
    "gauge_orbit_generators",
    "constraint_generators",
    "null_zero_mode_generators",
    "support_locality_generators",
    "observer_section_change_generators",
}

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bderived\s+rho_AB\b",
    r"\brho_AB\s+is\s+derived\b",
    r"\bBell\s+state\s+is\s+source[- ]defined\b",
    r"\bBell\s+state\s+as\s+source\s+generator\b",
    r"\bCHSH\s+state\s+is\s+source[- ]defined\b",
    r"\bCHSH\s+state\s+as\s+source\s+generator\b",
    r"\bPauli\s+observables?\s+are\s+source[- ]defined\b",
    r"\btarget\s+Hilbert\s+state\s+is\s+source[- ]defined\b",
    r"\bQFT[- ]state\s+proof\s+restart\s+allowed\b",
    r"\bF_phys\^b\(O\)\s+is\s+defined\b",
    r"\brepresentation[- ]carrier\s+labels?\s+define\s+physical\s+equivalence\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class QFTCongruenceGeneratorsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact_id"],
            "CandidateCongruenceGeneratorsForLocalGUPhysicalFieldEquivalence_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(
            self.summary["verdict"],
            "UNDERDEFINED_GENERATOR_TAXONOMY_ONLY_SOURCE_MAPS_ABSENT",
        )
        self.assertEqual(self.summary["verdict_class"], "underdefined")

    def test_candidate_generators_are_schema_slots_only(self) -> None:
        generators = self.summary["candidate_generators"]
        self.assertEqual({item["id"] for item in generators}, EXPECTED_GENERATORS)
        for item in generators:
            self.assertEqual(item["class"], "schema_slot", item["id"])
            self.assertIs(item["source_defined"], False, item["id"])
            self.assertIs(item["restriction_stable"], False, item["id"])
            self.assertIn("restriction_compatibility_proof", item["required_source_data"])
            self.assertIn("forbidden_source", item)

    def test_counts_are_not_inflated(self) -> None:
        generators = self.summary["candidate_generators"]
        source_defined_count = sum(1 for item in generators if item["source_defined"])
        restriction_stable_count = sum(1 for item in generators if item["restriction_stable"])
        self.assertEqual(self.summary["source_defined_generator_count"], source_defined_count)
        self.assertEqual(self.summary["restriction_stable_count"], restriction_stable_count)
        self.assertEqual(source_defined_count, 0)
        self.assertEqual(restriction_stable_count, 0)
        self.assertFalse(self.summary["all_source_generators_present"])

    def test_no_target_import_and_no_downstream_restart(self) -> None:
        self.assertIs(self.summary["target_import_used"], False)
        for key in [
            "F_phys_defined",
            "physical_equivalence_relation_defined",
            "restriction_functoriality_defined",
            "P_raw_defined",
            "P_fin_defined",
            "rho_AB_work_allowed",
            "CHSH_work_allowed",
            "proof_restart_allowed",
        ]:
            self.assertIs(self.summary[key], False, key)

    def test_fphys_and_restart_require_all_source_generators(self) -> None:
        all_present = self.summary["all_source_generators_present"]
        if not all_present:
            self.assertFalse(self.summary["F_phys_defined"])
            self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertLess(
            self.summary["source_defined_generator_count"],
            len(self.summary["candidate_generators"]),
        )
        self.assertLess(
            self.summary["restriction_stable_count"],
            len(self.summary["candidate_generators"]),
        )

    def test_forbidden_promotions_are_explicit(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        for item in [
            "target_Hilbert_state_as_source_congruence_generator",
            "target_density_matrix_as_source_congruence_generator",
            "Bell_or_CHSH_state_as_source_congruence_generator",
            "Pauli_observable_as_source_congruence_generator",
            "representation_carrier_label_as_source_congruence_generator",
            "ordinary_QFT_recovery_target_as_generator_selector",
        ]:
            self.assertIn(item, forbidden)

    def test_first_obstruction_blocks_expected_downstream_objects(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "source_defined_generator_maps_on_typed_R_raw_b_O_with_restriction_stability_proofs",
        )
        self.assertTrue(obstruction["missing"])
        for item in [
            "tilde_phys_b_O",
            "F_phys^b(O)",
            "restriction_maps_on_F_phys",
            "P_raw_descent_test",
            "P_fin^b",
            "rho_AB",
            "CHSH",
        ]:
            self.assertIn(item, obstruction["blocks"])

    def test_next_step_is_one_source_generator_restriction_test(self) -> None:
        next_step = self.summary["next_meaningful_step"]
        self.assertEqual(next_step["id"], "GaugeOrbitGeneratorRestrictionTest_V1")
        self.assertEqual(
            next_step["first_promotable_output"],
            "one_source_defined_restriction_stable_congruence_generator_family",
        )

    def test_no_bell_chsh_qft_state_promotion_phrases(self) -> None:
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion phrase matched: {pattern}",
            )


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "artifact_id": summary["artifact_id"],
        "verdict": summary["verdict"],
        "source_defined_generator_count": summary["source_defined_generator_count"],
        "restriction_stable_count": summary["restriction_stable_count"],
        "F_phys_defined": summary["F_phys_defined"],
        "proof_restart_allowed": summary["proof_restart_allowed"],
        "target_import_used": summary["target_import_used"],
        "next_step": summary["next_meaningful_step"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the QFT congruence generator candidate artifact."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(QFTCongruenceGeneratorsAudit)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
