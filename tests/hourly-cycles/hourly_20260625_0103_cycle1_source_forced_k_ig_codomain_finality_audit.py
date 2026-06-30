"""Audit the source-forced K_IG codomain/finality theorem attempt.

This structural audit checks that the artifact makes a FINAL/AXIOMATIC/
MULTIPLE/NONE decision, classifies all five surviving candidate classes,
keeps target and FLRW inputs out, and exposes the exact next selector object
and obstruction.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0103-cycle1-source-forced-k-ig-codomain-finality-theorem.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What was derived directly from repo sources",
    "## 3. The strongest positive result",
    "## 4. The first exact obstruction or missing proof object",
    "## 5. The constructive next object that would remove or test the obstruction",
    "## 6. What this means for the relevant GU claim",
    "## 7. Next meaningful proof or computation step",
    "## 8. Machine-readable JSON summary",
]

EXPECTED_CLASSES = {
    "EXT_DERIVATIVE",
    "CODERIVATIVE_TRACE",
    "SYMMETRIC_DERIVATIVE",
    "PROJECTED_DERIVATIVE",
    "LOWER_ORDER_DRESSED_EXTERIOR",
}

FORBIDDEN_POSITIVE_PATTERNS = [
    r"\bGU\s+(currently\s+)?derives\s+(dark energy|Lambda|Z_theta|C_Rtheta|xi_eff)\b",
    r"\bBranch 3\s+(currently\s+)?emits\s+(a\s+)?theta/FLRW coefficient packet\b",
    r"\bD_A U\s+is\s+(now\s+)?source-forced\b",
    r"\btarget performance\s+selects\s+K_IG\b",
    r'"GU_derives_dark_energy"\s*:\s*true',
    r'"GU_derives_Lambda"\s*:\s*true',
    r'"GU_derives_Z_theta"\s*:\s*true',
    r'"GU_derives_C_Rtheta"\s*:\s*true',
    r'"GU_derives_xi_eff"\s*:\s*true',
    r'"theta_FLRW_coefficient_work_performed"\s*:\s*true',
    r'"dark_energy_or_FLRW_promotion"\s*:\s*true',
]


def load_artifact() -> tuple[str, dict[str, object]]:
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return text, json.loads(match.group(1))


class SourceForcedKIGCodomainFinalityAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text, cls.summary = load_artifact()

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_decision_table_and_json_decision_are_multiple(self) -> None:
        self.assertIn("| `FINAL` | no |", self.text)
        self.assertIn("| `AXIOMATIC` | no |", self.text)
        self.assertIn("| `MULTIPLE` | yes |", self.text)
        self.assertIn("| `NONE` | no |", self.text)
        self.assertTrue(self.summary["decision_table_required"])
        self.assertEqual(
            self.summary["decision"],
            {
                "FINAL": False,
                "AXIOMATIC": False,
                "MULTIPLE": True,
                "NONE": False,
            },
        )
        self.assertEqual(
            self.summary["verdict"],
            "UNDERDEFINED_MULTIPLE_NO_SOURCE_FORCED_FINALITY",
        )
        self.assertEqual(self.summary["verdict_vocabulary"], "underdefined")

    def test_all_five_candidate_classes_are_classified(self) -> None:
        classes = {
            row["id"]: row for row in self.summary["surviving_candidate_classes"]
        }
        self.assertEqual(set(classes), EXPECTED_CLASSES)
        for row in classes.values():
            self.assertIs(row["eliminated"], False)
            self.assertIs(row["survives"], True)
            self.assertTrue(row["classification"])
            self.assertTrue(row["missing_rule"])

        self.assertEqual(classes["EXT_DERIVATIVE"]["codomain"], "Omega^2(Y,ad P)")
        self.assertIn("Omega^0", classes["CODERIVATIVE_TRACE"]["codomain"])
        self.assertIn("Sym", classes["SYMMETRIC_DERIVATIVE"]["schematic_operator"])
        self.assertIn("Pi_s_epsilon", classes["PROJECTED_DERIVATIVE"]["schematic_operator"])
        self.assertIn(
            "lower_order_rigidity",
            classes["LOWER_ORDER_DRESSED_EXTERIOR"]["missing_rule"],
        )

    def test_strongest_positive_construction_is_not_selection(self) -> None:
        construction = self.summary["strongest_positive_construction"]
        self.assertEqual(construction["candidate"], "K_ext(U;A)=D_A U")
        self.assertEqual(construction["codomain"], "Omega^2(Y,ad P)")
        self.assertEqual(
            construction["parent_degree_if_chosen"],
            "P_IG in Omega^2(Y,ad P)",
        )
        self.assertEqual(
            construction["positive_claim"],
            "admissible_coherent_exterior_template",
        )
        self.assertIn("conditional_theorem", construction)
        self.assertIs(construction["selection_claim"], False)

    def test_no_target_inputs_or_flrw_promotion(self) -> None:
        self.assertEqual(self.summary["target_inputs_seen_before_selector"], [])
        self.assertIs(self.summary["target_comparison_permitted"], False)
        self.assertIs(self.summary["theta_FLRW_coefficient_work_performed"], False)
        self.assertIs(self.summary["dark_energy_or_FLRW_promotion"], False)
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

    def test_obstruction_and_next_object_are_explicit(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "SourceForcedCodomainSelectorForK_IG")
        self.assertIs(obstruction["missing"], True)
        self.assertIn("category_or_preorder", obstruction["description"])
        self.assertIn(
            "finality_claim_not_well_formed",
            obstruction["earliest_failure"],
        )
        self.assertIn("parent_action_normalization", obstruction["blocks_before"])
        self.assertIn("theta_FLRW_coefficients", obstruction["blocks_before"])

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "SourceForcedCodomainSelectorForK_IG_V1")
        required = set(next_object["required_outputs"])
        for item in [
            "admissible_witness_category_or_preorder",
            "source_only_codomain_selector",
            "parent_momentum_degree_selector",
            "projection_loss_theorem",
            "lower_order_rigidity_policy",
            "finality_or_axiom_certificate",
            "target_replacement_check",
        ]:
            self.assertIn(item, required)

    def test_text_does_not_smuggle_positive_target_or_flrw_claims(self) -> None:
        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                pattern,
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
