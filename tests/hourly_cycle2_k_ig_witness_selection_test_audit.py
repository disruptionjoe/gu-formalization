"""Audit the Cycle 2 K_IG witness selection test artifact.

The audit checks that the artifact makes the promised FINAL/AXIOMATIC/MULTIPLE/NONE
decision, preserves the anti-overclaim guardrails, and exposes a parseable JSON summary.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-cycle2-k-ig-witness-selection-test-2026-06-25.md"


def load_summary() -> tuple[str, dict]:
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return text, json.loads(match.group(1))


class KIGWitnessSelectionTestAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text, cls.summary = load_summary()

    def test_verdict_is_multiple_not_final_axiomatic_or_none(self) -> None:
        self.assertEqual(self.summary["artifact"], "K_IGWitnessSelectionTest_V1")
        self.assertEqual(self.summary["verdict"], "MULTIPLE")
        self.assertEqual(
            self.summary["decision"],
            {
                "FINAL": False,
                "AXIOMATIC": False,
                "MULTIPLE": True,
                "NONE": False,
            },
        )
        self.assertFalse(self.summary["target_comparison_permitted"])
        self.assertEqual(self.summary["target_inputs_seen_before_selector"], [])

    def test_minimal_surviving_candidate_classes_are_explicit(self) -> None:
        classes = {row["id"]: row for row in self.summary["surviving_candidate_classes"]}
        expected = {
            "EXT_DERIVATIVE",
            "CODERIVATIVE_TRACE",
            "SYMMETRIC_DERIVATIVE",
            "PROJECTED_DERIVATIVE",
            "LOWER_ORDER_DRESSED_EXTERIOR",
        }
        self.assertEqual(set(classes), expected)
        self.assertTrue(all(row["survives"] for row in classes.values()))
        self.assertEqual(classes["EXT_DERIVATIVE"]["schematic_operator"], "D_A U")
        self.assertIn("D_A^*", classes["CODERIVATIVE_TRACE"]["schematic_operator"])
        self.assertIn("Sym", classes["SYMMETRIC_DERIVATIVE"]["schematic_operator"])

    def test_first_obstruction_blocks_downstream_coefficients(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "K_IGWitnessFinalityCertificate")
        self.assertTrue(obstruction["missing"])
        for blocked in ["Q_IG", "theta_eff", "Z_theta", "C_Rtheta", "xi_eff"]:
            self.assertIn(blocked, obstruction["blocks_before"])

    def test_anti_overclaim_guardrails_are_false(self) -> None:
        anti = self.summary["anti_overclaim"]
        for key in [
            "GU_derives_dark_energy",
            "GU_derives_Lambda",
            "GU_derives_Z_theta",
            "GU_derives_C_Rtheta",
            "GU_derives_xi_eff",
            "Branch_3_emits_theta_FLRW_packet",
            "D_A_U_source_forced_by_naturalness",
            "target_performance_selects_K_IG",
        ]:
            self.assertIn(key, anti)
            self.assertIs(anti[key], False)

    def test_text_does_not_smuggle_positive_cosmology_claims(self) -> None:
        forbidden_positive_claims = [
            "GU derives dark energy",
            "GU derives Lambda",
            "GU derives Z_theta",
            "GU derives C_Rtheta",
            "GU derives xi_eff",
            "Branch 3 emits a theta/FLRW coefficient packet",
        ]
        allowed_guardrail_section = self.text.split("Forbidden current claims:", 1)[-1]
        body_before_guardrails = self.text.split("Forbidden current claims:", 1)[0]
        for phrase in forbidden_positive_claims:
            self.assertNotIn(phrase, body_before_guardrails)
            self.assertIn(phrase, allowed_guardrail_section)

    def test_next_object_is_finality_not_cosmology(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "K_IGCodomainAndFinalityCertificate_V1")
        self.assertEqual(
            self.summary["claim_impact"]["next_gate"],
            "codomain_finality_selection_not_cosmology",
        )


if __name__ == "__main__":
    unittest.main()
