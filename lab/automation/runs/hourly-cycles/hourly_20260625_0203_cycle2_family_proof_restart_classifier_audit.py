#!/usr/bin/env python3
"""Audit FamilyProofRestartClassifier_V1.

The audit parses the embedded JSON summary and verifies that the classifier is
family-specific, sequential, and non-promotional: all four families remain
restart-blocked, each names an accepted-receipt prerequisite and identity check,
allowed work is source/acquisition only, and forbidden proof work covers the
known target-facing branches.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0203-cycle2-family-proof-restart-classifier.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Source Derivations",
    "## 3. Classifier Rule",
    "## 4. Family Rows",
    "## 5. Strongest Positive Result",
    "## 6. First Exact Obstruction",
    "## 7. GU Claim Impact and Forbidden Promotions",
    "## 8. Next Meaningful Computation/Proof/Source Step",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}

REQUIRED_OBJECT_SUBSTRINGS = {
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "RS": "d_RS,-1",
    "QFT": "P_fin^b",
    "DGU_VZ": "D_GU^epsilon 0/1",
}

REQUIRED_FORBIDDEN = {
    "IG": "IG coefficients",
    "RS": "RS rank/generation arithmetic",
    "QFT": "QFT Gram/CHSH",
    "DGU_VZ": "DGU/VZ actual-operator closure",
}

REQUIRED_NO_PROMOTIONS = {
    "IG_K_IG_selected",
    "RS_d_RS_minus_1_source_derived",
    "QFT_P_fin_b_supplied",
    "DGU_actual_operator_identified",
    "VZ_evasion_closed",
    "dark_energy_or_FLRW_recovered",
    "QFT_state_or_CHSH_recovered",
    "physical_rank_or_generation_readout",
    "family_proof_restart_allowed",
    "source_surface_as_formula_receipt",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing family proof-restart classifier: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class FamilyProofRestartClassifierAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)
        cls.rows = {
            row["family"]: row
            for row in cls.summary["family_rows"]  # type: ignore[index]
        }

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "FamilyProofRestartClassifier_V1")
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_NO_FAMILY_CAN_RESTART_DOWNSTREAM_PROOF_WORK",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0203-cycle2-family-proof-restart-classifier.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0203_cycle2_family_proof_restart_classifier_audit.py",
        )

    def test_four_families_exactly(self) -> None:
        self.assertEqual(set(self.rows), REQUIRED_FAMILIES)
        self.assertEqual(len(self.rows), 4)

    def test_restart_false_for_all_families(self) -> None:
        for family, row in self.rows.items():
            self.assertIs(row["restart_allowed"], False, family)
            self.assertEqual(row["restart_decision"], "blocked", family)
            self.assertIs(row["promotion_allowed"], False, family)

    def test_each_family_names_receipt_and_identity_check(self) -> None:
        for family, row in self.rows.items():
            self.assertIn("accepted", row["required_receipt"], family)
            self.assertIn(
                REQUIRED_OBJECT_SUBSTRINGS[family],
                row["required_receipt"] + " " + row["sequential_prerequisite"],
                family,
            )
            self.assertIn("identity check", row["family_identity_check"], family)
            self.assertIn("accepted PrimarySourceReceiptInstance_V1", row["sequential_prerequisite"], family)
            self.assertIn("identity check", row["sequential_prerequisite"], family)

    def test_forbidden_proof_work_covers_required_branches(self) -> None:
        global_forbidden = set(self.summary["forbidden_parallel_proof_work"])
        self.assertEqual(global_forbidden, set(REQUIRED_FORBIDDEN.values()))
        for family, required in REQUIRED_FORBIDDEN.items():
            self.assertIn(required, self.rows[family]["forbidden_proof_work"], family)

    def test_allowed_parallel_work_is_source_acquisition_only(self) -> None:
        self.assertEqual(
            self.summary["allowed_parallel_work_policy"],
            "source/acquisition only",
        )
        for family, row in self.rows.items():
            allowed = row["allowed_parallel_work"]
            self.assertIn("source_acquisition_only", allowed, family)
            joined = " ".join(allowed).lower()
            forbidden_terms = [
                "rank_arithmetic",
                "gram",
                "chsh",
                "actual_operator_closure",
                "coefficients",
            ]
            for term in forbidden_terms:
                self.assertNotIn(term, joined, family)

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        self.assertEqual(set(promotions), REQUIRED_NO_PROMOTIONS)
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertIn("No GU claim is promoted by this classifier.", self.text)

    def test_classifier_rule_is_sequential(self) -> None:
        rule = self.summary["classifier_rule"]
        self.assertIn(
            "family_mathematical_identity_check_passed",
            rule["restart_allowed_requires"],
        )
        self.assertEqual(
            rule["sequential_gate"],
            [
                "source_intake_acceptance",
                "family_mathematical_identity_check",
                "family_limited_downstream_restart",
                "proof_worker_attempts_closure",
                "normal_proof_or_canon_promotion_gate",
            ],
        )
        self.assertIs(rule["if_any_condition_fails"]["restart_allowed"], False)
        self.assertEqual(
            rule["if_any_condition_fails"]["allowed_parallel_work"],
            "source_acquisition_only",
        )

    def test_first_obstruction_and_next_step_are_source_gate(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "FamilyProofRestartReceiptGate_V1")
        self.assertIs(obstruction["missing"], True)
        self.assertEqual(obstruction["families_open_for_restart"], 0)
        self.assertIn("family mathematical identity check", obstruction["description"])

        next_step = self.summary["next_meaningful_step"]
        self.assertEqual(next_step["kind"], "source_acquisition_not_proof")
        joined_steps = " ".join(next_step["steps"])
        self.assertIn("RepoLocalPrimaryGUSourceReceiptMap_V1", joined_steps)
        self.assertIn("PrimarySourceReceiptInstance_V1", joined_steps)


if __name__ == "__main__":
    unittest.main()
