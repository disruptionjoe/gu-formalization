#!/usr/bin/env python3
"""Audit TargetImportGuardReceiptAudit_V1.

The audit parses the embedded JSON summary and checks the cycle 3 target-import
guard contract: target data cannot select source receipts, all specified target
families are covered, source-side objects emitted before target comparison can
only be quarantined or routed after intake, no proof restart is currently
allowed, and no claim is promoted.
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
    / "hourly-20260625-0203-cycle3-target-import-guard-receipt-audit.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Source Derivations",
    "## 3. Guard Rule Set",
    "## 4. Target-Import Forbidden Examples by Family",
    "## 5. Allowed Source-Side Uses",
    "## 6. Strongest Positive Result",
    "## 7. First Exact Obstruction",
    "## 8. GU Claim Impact and Forbidden Promotions",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_TARGET_COVERAGE = {
    "DESI_dark_energy",
    "FLRW_coefficients",
    "ranks_generation_counts",
    "VZ_closure_targets",
    "QFT_Gram_CHSH_rho_AB",
    "downstream_target_outcomes_as_source_selection_evidence",
}

REQUIRED_FORBIDDEN_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}

REQUIRED_NO_PROMOTIONS = {
    "IG_K_IG_selected",
    "RS_d_RS_minus_1_source_derived",
    "QFT_P_fin_b_supplied",
    "DGU_actual_operator_identified",
    "DESI_or_dark_energy_recovered",
    "FLRW_coefficients_recovered",
    "rank_or_generation_counts_derived",
    "VZ_evasion_or_closure_established",
    "QFT_Gram_CHSH_Bell_or_rho_AB_recovered",
    "target_success_selects_source_object",
    "candidate_with_target_data_seen_nonempty_accepted",
    "proof_restart_allowed_now",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing target-import guard artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class TargetImportGuardReceiptAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "TargetImportGuardReceiptAudit_V1")
        self.assertEqual(self.summary["version"], "2026-06-25")
        self.assertEqual(self.summary["run"], "hourly-20260625-0203")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_NO_PROOF_RESTART_GUARD_READY_FOR_FUTURE_RECEIPTS",
        )
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0203-cycle3-target-import-guard-receipt-audit.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0203_cycle3_target_import_guard_receipt_audit.py",
        )

    def test_guard_covers_required_target_families(self) -> None:
        coverage = self.summary["target_families_covered"]
        self.assertEqual(set(coverage), REQUIRED_TARGET_COVERAGE)
        for key, value in coverage.items():
            self.assertIs(value, True, key)

    def test_guard_ready_but_no_proof_restart(self) -> None:
        self.assertIs(self.summary["guard_ready"], True)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        sequence_rule = next(
            rule for rule in self.summary["guard_rules"] if rule["rule_id"] == "TIG-07-restart-sequential"
        )
        self.assertEqual(
            sequence_rule["restart_sequence"],
            [
                "target_import_guard_pass",
                "source_intake_acceptance",
                "family_mathematical_identity_check",
                "family_limited_proof_restart",
            ],
        )
        self.assertIs(sequence_rule["proof_restart_allowed_now"], False)

    def test_target_data_seen_nonempty_blocks_acceptance(self) -> None:
        policy = self.summary["candidate_acceptance_policy"]["target_data_seen_nonempty"]
        self.assertIs(policy["candidate_can_be_accepted_for_routing"], False)
        self.assertEqual(set(policy["allowed_statuses"]), {"quarantined", "rejected"})
        self.assertIs(policy["proof_restart_allowed"], False)
        self.assertIs(policy["promotion_allowed"], False)

        rule = next(
            rule for rule in self.summary["guard_rules"] if rule["rule_id"] == "TIG-01-empty-target-data"
        )
        self.assertEqual(
            rule["if_violated"]["candidate_can_be_accepted_for_routing"],
            False,
        )
        self.assertEqual(set(rule["if_violated"]["allowed_statuses"]), {"quarantined", "rejected"})

    def test_source_side_object_before_target_can_only_route_after_intake(self) -> None:
        policy = self.summary["candidate_acceptance_policy"][
            "source_side_action_or_operator_emitted_before_target_comparison"
        ]
        self.assertIs(policy["candidate_can_be_quarantined"], True)
        self.assertIs(policy["candidate_can_be_routed_only_after_intake"], True)
        self.assertIs(policy["requires_exact_locator"], True)
        self.assertIs(policy["requires_representation_context"], True)
        self.assertIs(policy["requires_target_data_seen_empty_for_acceptance"], True)
        self.assertIs(policy["proof_restart_allowed_at_intake"], False)
        self.assertIs(policy["requires_family_identity_check_before_restart"], True)

    def test_forbidden_examples_cover_four_families(self) -> None:
        rows = {
            row["family"]: row
            for row in self.summary["forbidden_examples_by_family"]
        }
        self.assertEqual(set(rows), REQUIRED_FORBIDDEN_FAMILIES)
        required_terms = {
            "IG": ["DESI", "dark_energy", "FLRW"],
            "RS": ["rank_count", "generation_count"],
            "QFT": ["Gram", "CHSH", "rho_AB"],
            "DGU_VZ": ["VZ_closure", "dark_energy_recovery", "FLRW_recovery"],
        }
        for family, terms in required_terms.items():
            examples = " ".join(rows[family]["target_import_examples"])
            for term in terms:
                self.assertIn(term, examples, family)
            self.assertIs(rows[family]["candidate_can_be_accepted_for_routing"], False)

    def test_allowed_source_side_use_does_not_promote_claims(self) -> None:
        uses = self.summary["allowed_source_side_uses"]
        self.assertIs(uses["DESI_or_dark_energy_segments_can_prioritize_search"], True)
        self.assertIs(uses["target_facing_segment_can_be_quarantined_for_review"], True)
        self.assertIs(
            uses["source_side_object_emitted_before_target_comparison_can_be_routed_after_intake"],
            True,
        )
        self.assertIs(uses["allowed_use_is_not_claim_promotion"], True)

        limited_rule = next(
            rule for rule in self.summary["guard_rules"] if rule["rule_id"] == "TIG-05-source-side-use-limited"
        )
        self.assertIs(limited_rule["claim_promotion_allowed"], False)

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        self.assertEqual(set(promotions), REQUIRED_NO_PROMOTIONS)
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertIn("No GU claim is promoted.", self.text)
        self.assertIn("Forbidden promotions", self.text)

    def test_first_obstruction_blocks_target_leakage_before_intake(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "TargetImportGuardReceiptGate_V1")
        self.assertIn("target-import cleanliness", obstruction["description"])
        self.assertIs(
            obstruction["candidate_rows_with_target_data_seen_nonempty_blocked_before_intake"],
            True,
        )


if __name__ == "__main__":
    unittest.main()
