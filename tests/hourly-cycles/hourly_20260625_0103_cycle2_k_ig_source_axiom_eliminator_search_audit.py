"""Audit the Cycle 2 K_IG source axiom and eliminator search artifact.

The audit is structural: it parses the machine-readable JSON block, requires
all candidate classes and source-search statuses, keeps target inputs empty,
rejects dark-energy/FLRW promotion, and verifies the first obstruction plus
constructive next object.
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
    / "hourly-20260625-0103-cycle2-k-ig-source-axiom-eliminator-search.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct source derivations",
    "## 3. Strongest positive result",
    "## 4. Source axiom / theorem / eliminator search",
    "## 5. First exact obstruction",
    "## 6. Constructive next object",
    "## 7. GU claim impact",
    "## 8. Next proof step",
    "## 9. Machine-readable JSON summary",
]

EXPECTED_CLASSES = {
    "EXT_DERIVATIVE",
    "CODERIVATIVE_TRACE",
    "SYMMETRIC_DERIVATIVE",
    "PROJECTED_DERIVATIVE",
    "LOWER_ORDER_DRESSED_EXTERIOR",
}

EXPECTED_SOURCE_FAMILIES = {
    "research_posture_and_runbook",
    "typed_operator_action_spine",
    "cycle1_source_forced_finality_artifact",
    "cycle3_codomain_finality_certificate",
    "source_claim_ledger",
    "media_claim_mining_report",
    "repo_local_grep",
}

FORBIDDEN_POSITIVE_PATTERNS = [
    r"\bGU\s+(currently\s+)?derives\s+(dark energy|Lambda|Z_theta|C_Rtheta|xi_eff)\b",
    r"\bBranch 3\s+(currently\s+)?emits\s+(a\s+)?theta/FLRW coefficient packet\b",
    r"\bD_A U\s+is\s+(now\s+)?source-forced\b",
    r"\btarget performance\s+selects\s+K_IG\b",
    r"\bthe alternatives have been eliminated\b",
    r'"GU_derives_dark_energy"\s*:\s*true',
    r'"GU_derives_Lambda"\s*:\s*true',
    r'"GU_derives_Z_theta"\s*:\s*true',
    r'"GU_derives_C_Rtheta"\s*:\s*true',
    r'"GU_derives_xi_eff"\s*:\s*true',
    r'"theta_FLRW_coefficient_work_performed"\s*:\s*true',
    r'"dark_energy_or_FLRW_promotion"\s*:\s*true',
    r'"alternatives_eliminated_before_targets"\s*:\s*true',
]


def load_artifact() -> tuple[str, dict[str, object]]:
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(
        r"## 9\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return text, json.loads(match.group(1))


class KIGSourceAxiomEliminatorSearchAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text, cls.summary = load_artifact()

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_and_decision_are_blocked_multiple(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "K_IGSourceAxiomAndEliminatorSearch_V1",
        )
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_NO_REPO_LOCAL_SOURCE_AXIOM_OR_ELIMINATOR",
        )
        self.assertEqual(self.summary["verdict_vocabulary"], "blocked")
        self.assertEqual(
            self.summary["decision"],
            {
                "FINAL": False,
                "AXIOMATIC": False,
                "ELIMINATED_ALTERNATIVES": False,
                "MULTIPLE": True,
                "NONE": False,
            },
        )
        self.assertIn("| `ELIMINATED_ALTERNATIVES` | no |", self.text)

    def test_source_search_statuses_cover_required_families(self) -> None:
        statuses = {
            row["source_family"]: row for row in self.summary["source_search_statuses"]
        }
        self.assertEqual(set(statuses), EXPECTED_SOURCE_FAMILIES)
        for row in statuses.values():
            self.assertTrue(row["status"].startswith("searched_"))
            self.assertTrue(row["result"])
        self.assertEqual(
            statuses["typed_operator_action_spine"]["status"],
            "searched_admissible_host_only",
        )
        self.assertEqual(
            statuses["repo_local_grep"]["status"],
            "searched_no_current_eliminator",
        )

    def test_all_candidate_classes_and_source_statuses_are_present(self) -> None:
        classes = {row["id"]: row for row in self.summary["candidate_classes"]}
        self.assertEqual(set(classes), EXPECTED_CLASSES)
        for row in classes.values():
            self.assertIn("source_search_status", row)
            self.assertIn("missing_eliminator", row)
            self.assertIs(row["eliminated_before_targets"], False)
            self.assertIs(row["survives"], True)

        self.assertEqual(
            classes["EXT_DERIVATIVE"]["source_search_status"],
            "admissible_host_found_not_source_forced",
        )
        for class_id in EXPECTED_CLASSES - {"EXT_DERIVATIVE"}:
            self.assertEqual(classes[class_id]["source_search_status"], "no_eliminator_found")

        self.assertIn("Omega^0", classes["CODERIVATIVE_TRACE"]["codomain"])
        self.assertIn("Sym", classes["SYMMETRIC_DERIVATIVE"]["schematic_operator"])
        self.assertIn("Pi_s_epsilon", classes["PROJECTED_DERIVATIVE"]["schematic_operator"])
        self.assertIn(
            "lower_order_rigidity",
            classes["LOWER_ORDER_DRESSED_EXTERIOR"]["missing_eliminator"],
        )

    def test_strongest_positive_result_is_not_selection(self) -> None:
        result = self.summary["strongest_positive_result"]
        self.assertEqual(result["candidate"], "K_ext(U;A)=D_A U")
        self.assertEqual(result["codomain"], "Omega^2(Y,ad P)")
        self.assertEqual(result["parent_slot"], "int_Y <P_IG,D_A U>_{Q_IG}")
        self.assertEqual(result["positive_claim"], "admissible_coherent_exterior_template")
        self.assertIs(result["selection_claim"], False)
        self.assertIs(result["source_forced"], False)

    def test_target_inputs_empty_and_no_flrw_promotion(self) -> None:
        self.assertEqual(self.summary["target_inputs_seen"], [])
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
            "alternatives_eliminated_before_targets",
        ]:
            self.assertIn(key, anti)
            self.assertIs(anti[key], False)

    def test_first_obstruction_and_next_object_are_exact(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "SourceForcedCodomainSelectorForK_IG")
        self.assertIs(obstruction["missing"], True)
        self.assertIn("no_repo_local_source_axiom", obstruction["description"])
        self.assertIn("alternatives_not_eliminated_before_targets", obstruction["earliest_failure"])
        self.assertIn("theta_FLRW_coefficients", obstruction["blocks_before"])

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "SourceForcedCodomainSelectorForK_IG_V1")
        required = set(next_object["required_outputs"])
        for item in [
            "source_only_codomain_selector",
            "coderivative_trace_eliminator",
            "symmetric_derivative_eliminator",
            "projected_derivative_eliminator",
            "lower_order_dressed_exterior_eliminator",
            "projection_loss_theorem",
            "target_replacement_check",
        ]:
            self.assertIn(item, required)

    def test_text_does_not_smuggle_positive_target_or_elimination_claims(self) -> None:
        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                pattern,
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
