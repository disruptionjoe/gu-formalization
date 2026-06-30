#!/usr/bin/env python3
"""Audit ReceiptStateMachineRestartPolicy_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle3-receipt-state-machine-restart-policy.md"
)

EXPECTED_STATE_ORDER = [
    "source_locator",
    "quarantined_candidate",
    "accepted_for_routing",
    "family_identity_passed",
    "proof_restart_allowed",
]

EXPECTED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}

EXPECTED_FORBIDDEN_SKIPS = {
    ("source_locator", "accepted_for_routing"),
    ("source_locator", "family_identity_passed"),
    ("source_locator", "proof_restart_allowed"),
    ("quarantined_candidate", "family_identity_passed"),
    ("quarantined_candidate", "proof_restart_allowed"),
    ("accepted_for_routing", "proof_restart_allowed"),
    ("target_data_seen_nonempty", "accepted_for_routing"),
    ("target_clean_only", "proof_restart_allowed"),
    ("manuscript_formula_adjacency", "proof_restart_allowed"),
    ("blocked_negative_source_pass", "proof_restart_allowed"),
}

EXPECTED_CURRENT_STATES = {
    "IG": "quarantined_candidate",
    "RS": "quarantined_candidate_underdefined",
    "QFT": "blocked_negative_source_pass",
    "DGU_VZ": "quarantined_candidate",
}

REQUIRED_NO_PROMOTIONS = {
    "IG_K_IG_selected",
    "SourceForcedCodomainSelectorForK_IG_accepted",
    "RS_d_RS_minus_1_source_derived",
    "QFT_P_fin_b_supplied",
    "DGU_actual_operator_identified",
    "DGU_actual_principal_symbol_source_derived",
    "DGU_coefficient_packet_source_derived",
    "DESI_or_dark_energy_recovered",
    "FLRW_coefficients_recovered",
    "rank_or_generation_counts_derived",
    "QFT_Gram_CHSH_Bell_or_rho_AB_recovered",
    "VZ_evasion_or_closure_established",
    "proof_restart_allowed_now",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class ReceiptStateMachineRestartPolicyAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "ReceiptStateMachineRestartPolicy_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_NO_CURRENT_CANDIDATE_CAN_REACH_PROOF_RESTART",
        )
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle3-receipt-state-machine-restart-policy.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle3_receipt_state_machine_restart_policy_audit.py",
        )

    def test_state_order_is_sequential(self) -> None:
        self.assertEqual(self.summary["state_order"], EXPECTED_STATE_ORDER)
        transitions = [(row["from"], row["to"]) for row in self.summary["allowed_transitions"]]
        self.assertEqual(
            transitions,
            list(zip(EXPECTED_STATE_ORDER, EXPECTED_STATE_ORDER[1:])),
        )

    def test_state_invariants_block_early_restart_and_promotion(self) -> None:
        invariants = self.summary["state_invariants"]
        self.assertFalse(invariants["source_locator"]["accepted_for_routing"])
        self.assertFalse(invariants["source_locator"]["proof_restart_allowed"])
        self.assertFalse(invariants["quarantined_candidate"]["accepted_for_routing"])
        self.assertFalse(invariants["quarantined_candidate"]["family_identity_passed"])
        self.assertFalse(invariants["accepted_for_routing"]["proof_restart_allowed"])
        self.assertFalse(invariants["family_identity_passed"]["proof_restart_allowed_by_itself"])
        for state, row in invariants.items():
            self.assertFalse(row["claim_promotion_allowed"], state)

    def test_forbidden_skips_are_explicit(self) -> None:
        forbidden = {
            (row["from"], row["to"]): row["reason"]
            for row in self.summary["forbidden_transitions"]
        }
        self.assertEqual(set(forbidden), EXPECTED_FORBIDDEN_SKIPS)
        for edge, reason in forbidden.items():
            self.assertIsInstance(reason, str, edge)
            self.assertGreater(len(reason), 20, edge)

    def test_target_import_guard_is_preserved(self) -> None:
        guard = self.summary["target_import_guard_preserved"]
        self.assertTrue(guard["target_data_seen_nonempty_blocks_accepted_for_routing"])
        self.assertTrue(guard["target_cleanliness_is_not_acceptance"])
        self.assertTrue(guard["target_cleanliness_is_not_family_identity"])
        self.assertTrue(guard["target_cleanliness_is_not_proof_restart"])
        self.assertTrue(guard["downstream_success_cannot_select_source_object"])

        forbidden = {(row["from"], row["to"]) for row in self.summary["forbidden_transitions"]}
        self.assertIn(("target_data_seen_nonempty", "accepted_for_routing"), forbidden)
        self.assertIn(("target_clean_only", "proof_restart_allowed"), forbidden)

    def test_current_candidate_states_and_blocked_decisions(self) -> None:
        rows = {row["family"]: row for row in self.summary["current_candidate_states"]}
        self.assertEqual(set(rows), EXPECTED_FAMILIES)
        for family, expected_state in EXPECTED_CURRENT_STATES.items():
            row = rows[family]
            self.assertEqual(row["state"], expected_state)
            self.assertFalse(row["accepted_for_routing"], family)
            self.assertFalse(row["family_identity_passed"], family)
            self.assertFalse(row["proof_restart_allowed"], family)
            self.assertFalse(row["claim_promotion_allowed"], family)
            self.assertIn("->", row["first_missing_transition"])
            self.assertTrue(row["first_missing_object"])

    def test_global_decision_allows_no_restart_or_claim_promotion(self) -> None:
        decision = self.summary["global_decision"]
        self.assertEqual(decision["accepted_receipt_count_current_candidates"], 0)
        self.assertEqual(decision["families_with_family_identity_passed"], 0)
        self.assertEqual(decision["families_with_proof_restart_allowed"], 0)
        self.assertFalse(decision["proof_restart_allowed"])
        self.assertFalse(decision["claim_promotion_allowed"])

    def test_no_claim_promotion_map_is_all_false(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        self.assertEqual(set(promotions), REQUIRED_NO_PROMOTIONS)
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertIn("No GU mathematical or physical claim is promoted.", self.text)

    def test_forbidden_promotions_include_process_inflation_controls(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        for claim in [
            "target_clean_candidate_accepted_without_intake",
            "accepted_for_routing_row_restarts_proof_without_family_identity",
            "current_candidate_restarts_proof_now",
            "DESI_dark_energy_FLRW_rank_generation_QFT_covariance_rho_AB_Bell_CHSH_or_VZ_closure_derived",
        ]:
            self.assertIn(claim, forbidden)

    def test_next_computation_targets_first_missing_transition_only(self) -> None:
        rows = {
            row["family"]: row
            for row in self.summary["next_meaningful_state_transition_computation"]
        }
        self.assertEqual(set(rows), EXPECTED_FAMILIES)
        self.assertEqual(
            rows["IG"]["attempted_transition"],
            "quarantined_candidate->accepted_for_routing",
        )
        self.assertEqual(
            rows["RS"]["attempted_transition"],
            "quarantined_candidate_underdefined->accepted_for_routing",
        )
        self.assertEqual(
            rows["QFT"]["attempted_transition"],
            "source_locator_or_negative_pass->quarantined_candidate",
        )
        self.assertEqual(
            rows["DGU_VZ"]["attempted_transition"],
            "quarantined_candidate->accepted_for_routing",
        )
        for row in rows.values():
            self.assertNotEqual(row["attempted_transition"].split("->")[1], "proof_restart_allowed")


if __name__ == "__main__":
    unittest.main()
