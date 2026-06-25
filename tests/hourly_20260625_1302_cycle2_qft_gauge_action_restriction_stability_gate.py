#!/usr/bin/env python3
"""Audit QFTGaugeActionRestrictionStabilityGate_V1."""

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
    / "hourly-20260625-1302-cycle2-qft-gauge-action-restriction-stability-gate.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What was derived directly from repo sources",
    "## 3. The strongest positive result",
    "## 4. The first exact obstruction or missing proof object",
    "## 5. The constructive next object that would remove or test the obstruction",
    "## 6. What this means for F_phys, P_raw/P_fin descent, rho_AB, and CHSH",
    "## 7. Next meaningful proof or computation step",
    "## 8. Machine-readable JSON summary",
]

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bderived\s+rho_AB\b",
    r"\brho_AB\s+is\s+derived\b",
    r"\bBell\s+state\s+is\s+source[- ]defined\b",
    r"\bBell\s+control\s+defines\s+the\s+gauge\s+equivalence\b",
    r"\bCHSH\s+control\s+defines\s+the\s+gauge\s+equivalence\b",
    r"\bCHSH\s+state\s+is\s+source[- ]defined\b",
    r"\bPauli\s+observables?\s+select\s+the\s+gauge\s+quotient\b",
    r"\btarget\s+Hilbert\s+state\s+selects\s+the\s+gauge\s+quotient\b",
    r"\btarget\s+density\s+matrix\s+selects\s+the\s+gauge\s+quotient\b",
    r"\bQFT[- ]state\s+proof\s+restart\s+allowed\b",
    r"\bF_phys\^b\(O\)\s+is\s+defined\b",
    r"\brepresentation[- ]carrier\s+labels?\s+select\s+the\s+gauge\s+quotient\b",
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


class QFTGaugeActionRestrictionStabilityGateAudit(unittest.TestCase):
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
            "QFTGaugeActionRestrictionStabilityGate_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["verdict_class"], "underdefined")

    def test_gauge_candidate_present_but_not_promoted(self) -> None:
        self.assertIs(self.summary["gauge_action_candidate_present"], True)
        self.assertIs(self.summary["local_groupoid_defined"], False)
        self.assertIs(self.summary["restriction_stability_proved"], False)
        self.assertIs(self.summary["gauge_action_generator_source_defined"], False)

    def test_candidate_not_counted_without_groupoid_and_restriction(self) -> None:
        candidate_closed = (
            self.summary["gauge_action_candidate_present"]
            and self.summary["local_groupoid_defined"]
            and self.summary["restriction_stability_proved"]
        )
        if not candidate_closed:
            self.assertEqual(self.summary["source_defined_generator_count"], 0)
            self.assertEqual(self.summary["restriction_stable_generator_count"], 0)
            self.assertFalse(self.summary["gauge_action_generator_source_defined"])

    def test_fphys_and_restart_remain_false_unless_generator_closes(self) -> None:
        generator_closes = (
            self.summary["gauge_action_generator_source_defined"]
            and self.summary["restriction_stability_proved"]
            and self.summary["source_defined_generator_count"] >= 1
        )
        if not generator_closes:
            for key in [
                "F_phys_defined",
                "physical_equivalence_relation_defined",
                "P_raw_descent_allowed",
                "P_fin_defined",
                "rho_AB_work_allowed",
                "CHSH_work_allowed",
                "proof_restart_allowed",
            ]:
                self.assertIs(self.summary[key], False, key)

    def test_no_target_import(self) -> None:
        self.assertIs(self.summary["target_import_used"], False)
        self.assertTrue(
            self.summary["strongest_positive_result"]["does_not_use_target_data"]
        )

    def test_forbidden_promotions_are_explicit(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        for item in [
            "target_Hilbert_state_as_gauge_congruence_selector",
            "target_density_matrix_as_gauge_congruence_selector",
            "Bell_or_CHSH_control_as_gauge_congruence_selector",
            "Pauli_observable_as_gauge_congruence_selector",
            "representation_carrier_label_as_gauge_congruence_selector",
            "ordinary_QFT_recovery_target_as_gauge_generator_selector",
        ]:
            self.assertIn(item, forbidden)

    def test_first_obstruction_blocks_expected_downstream_objects(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "LocalGaugeActionGroupoidOnObservedRawGUFields_V1",
        )
        self.assertTrue(obstruction["missing"])
        for item in [
            "gauge_orbit_generator_promotion",
            "tilde_phys_b_O",
            "F_phys^b(O)",
            "P_raw_descent_test",
            "P_fin^b",
            "rho_AB",
            "CHSH",
        ]:
            self.assertIn(item, obstruction["blocks"])

    def test_next_step_targets_restriction_stability(self) -> None:
        next_step = self.summary["next_meaningful_step"]
        self.assertEqual(next_step["id"], "GaugeOrbitGeneratorRestrictionTest_V1")
        self.assertEqual(
            next_step["first_promotable_output"],
            "one_source_defined_restriction_stable_gauge_orbit_generator_family",
        )

    def test_no_qft_state_bell_chsh_promotion_phrases(self) -> None:
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
        "gauge_action_candidate_present": summary["gauge_action_candidate_present"],
        "local_groupoid_defined": summary["local_groupoid_defined"],
        "restriction_stability_proved": summary["restriction_stability_proved"],
        "source_defined_generator_count": summary["source_defined_generator_count"],
        "F_phys_defined": summary["F_phys_defined"],
        "proof_restart_allowed": summary["proof_restart_allowed"],
        "target_import_used": summary["target_import_used"],
        "next_step": summary["next_meaningful_step"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the QFT gauge action restriction stability gate."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            QFTGaugeActionRestrictionStabilityGateAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
