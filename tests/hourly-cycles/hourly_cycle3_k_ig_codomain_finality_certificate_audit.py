"""Audit the Cycle 3 K_IG codomain/finality certificate artifact.

This is a structural audit. It checks that the certificate keeps the selector
underdefined, handles all candidate classes explicitly, identifies the exact missing
codomain/finality rule, and preserves anti-overclaim guardrails.
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
    / "hourly-cycle3-k-ig-codomain-finality-certificate-2026-06-25.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What was derived directly from repo sources",
    "## 3. Strongest positive construction attempt",
    "## 4. First exact obstruction or missing proof object",
    "## 5. Constructive next object",
    "## 6. Impact on GU claim",
    "## 7. Next meaningful proof/computation step",
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


class KIGCodomainFinalityCertificateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text, cls.summary = load_artifact()

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_is_multiple_due_to_missing_codomain_finality_rule(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "K_IGCodomainAndFinalityCertificate_V1",
        )
        self.assertEqual(
            self.summary["verdict"],
            "MULTIPLE_NO_CODOMAIN_FINALITY_RULE",
        )
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

    def test_strongest_positive_construction_is_admissible_not_selected(self) -> None:
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
        self.assertFalse(construction["selection_claim"])

    def test_all_candidate_classes_survive_with_missing_rules(self) -> None:
        classes = {
            row["id"]: row for row in self.summary["surviving_candidate_classes"]
        }
        self.assertEqual(set(classes), EXPECTED_CLASSES)
        for row in classes.values():
            self.assertIs(row["eliminated"], False)
            self.assertIs(row["survives"], True)
            self.assertTrue(row["missing_rule"])

        self.assertEqual(classes["EXT_DERIVATIVE"]["codomain"], "Omega^2(Y,ad P)")
        self.assertIn("Omega^0", classes["CODERIVATIVE_TRACE"]["codomain"])
        self.assertIn("Sym", classes["SYMMETRIC_DERIVATIVE"]["schematic_operator"])
        self.assertIn("Pi_s_epsilon", classes["PROJECTED_DERIVATIVE"]["schematic_operator"])
        self.assertIn(
            "lower_order_policy",
            classes["LOWER_ORDER_DRESSED_EXTERIOR"]["missing_rule"],
        )

    def test_first_obstruction_is_exact_codomain_finality_rule(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "CodomainFinalityRuleForK_IG")
        self.assertTrue(obstruction["missing"])
        self.assertIn("selected codomain", obstruction["description"])
        self.assertIn("parent_action_normalization", obstruction["blocks_before"])
        self.assertIn("physical_reduction", obstruction["blocks_before"])

    def test_constructive_next_object_is_source_side_not_target_facing(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(
            next_object["id"],
            "SourceForcedK_IGCodomainFinalityTheorem_V1",
        )
        required = set(next_object["required_outputs"])
        for item in [
            "codomain_selector",
            "parent_momentum_degree_selector",
            "elimination_lemmas_for_non_exterior_classes",
            "projection_loss_theorem",
            "lower_order_policy",
            "finality_or_axiom_certificate",
            "replacement_target_check",
        ]:
            self.assertIn(item, required)
        self.assertEqual(
            self.summary["claim_impact"]["next_gate"],
            "source_side_codomain_finality_not_target_computation",
        )

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

    def test_text_does_not_smuggle_positive_claims(self) -> None:
        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                pattern,
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
