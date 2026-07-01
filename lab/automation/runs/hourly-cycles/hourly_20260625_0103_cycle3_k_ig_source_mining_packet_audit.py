#!/usr/bin/env python3
"""Audit K_IGSourceMiningPacket_V1.

This structural audit checks that the packet is a source-mining contract, not a
claim that a source exists. It requires accept/reject conditions, mining fields,
absorber and target-import checks, no FLRW/dark-energy promotion, and an explicit
sequential dependency before target-facing IG work.
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
    / "hourly-20260625-0103-cycle3-k-ig-source-mining-packet.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct source derivations",
    "## 3. What would count as a source receipt",
    "## 4. Accept conditions",
    "## 5. Reject conditions",
    "## 6. Strongest positive mining packet",
    "## 7. First exact obstruction",
    "## 8. Absorber and target-import checks",
    "## 9. Task contract for future source mining",
    "## 10. GU impact",
    "## 11. Next step",
    "## 12. Machine-readable JSON summary",
]

REQUIRED_RECEIPT_KINDS = {
    "EXPLICIT_SELECTOR_AXIOM",
    "DERIVATION_CELL",
    "PRIMARY_ACTION_SLOT",
    "PROJECTION_LOSS_RULE",
    "LOWER_ORDER_RIGIDITY_RULE",
}

REQUIRED_MINIMUM_FIELDS = {
    "source_id",
    "primary_locator",
    "source_status",
    "receipt_kind",
    "exact_excerpt_or_derivation_cell",
    "source_context_before_after",
    "emitted_operator_or_rule",
    "selected_codomain",
    "selected_parent_momentum_degree",
    "principal_symbol_or_finality_class",
    "projector_policy",
    "lower_order_policy",
    "boundary_or_variation_class",
    "eliminated_competitor_classes",
    "target_inputs_seen",
    "absorber_check",
    "target_import_check",
    "promotion_decision",
    "rollback_condition",
}

REQUIRED_ACCEPT_CONDITIONS = {
    "primary_locator_present",
    "exact_evidence_with_context_present",
    "source_native_data_not_target_labels",
    "one_codomain_selected_before_targets",
    "parent_degree_fixed_by_same_source_evidence",
    "four_competitor_classes_eliminated_or_ruled_irrelevant",
    "projection_loss_check_passes",
    "lower_order_rigidity_passes",
    "target_import_check_passes_with_no_target_inputs",
    "absorber_check_passes",
    "target_label_replacement_check_passes",
}

REQUIRED_REJECT_CONDITIONS = {
    "SECONDARY_ONLY",
    "NO_OPERATOR_OR_RULE",
    "TARGET_IMPORTED_SELECTOR",
    "MULTIPLE_SURVIVORS",
    "PROJECTOR_AMBIGUITY",
    "LOWER_ORDER_FREEDOM",
    "ABSORBER_ONLY",
    "NO_SEQUENTIAL_GATE",
}

EXPECTED_CLASSES = {
    "EXT_DERIVATIVE",
    "CODERIVATIVE_TRACE",
    "SYMMETRIC_DERIVATIVE",
    "PROJECTED_DERIVATIVE",
    "LOWER_ORDER_DRESSED_EXTERIOR",
}

REQUIRED_TASK_FIELDS = {
    "source_id",
    "locator",
    "receipt_kind",
    "exact_excerpt_or_cell",
    "emitted_rule",
    "candidate_class_effect",
    "absorber_check",
    "target_import_check",
    "accept_reject_decision",
    "sequential_dependency",
}

FORBIDDEN_POSITIVE_PATTERNS = [
    r"\bwe\s+(found|supply|prove)\s+the\s+source\s+receipt\b",
    r"\btherefore\s+K_IG\s*=\s*D_A U\s+is\s+source-forced\b",
    r"\btherefore\s+target performance selects K_IG\b",
    r"\bthis\s+(packet|artifact)\s+derives\s+(dark energy|Lambda|Z_theta|C_Rtheta|xi_eff)\b",
    r'"source_receipt_exists"\s*:\s*true',
    r'"K_IG_D_A_U_source_forced"\s*:\s*true',
    r'"naturalness_eliminates_alternatives"\s*:\s*true',
    r'"target_performance_selects_K_IG"\s*:\s*true',
    r'"Branch_3_emits_theta_FLRW_coefficients"\s*:\s*true',
    r'"GU_derives_dark_energy"\s*:\s*true',
    r'"GU_derives_Lambda"\s*:\s*true',
    r'"GU_derives_Z_theta"\s*:\s*true',
    r'"GU_derives_C_Rtheta"\s*:\s*true',
    r'"GU_derives_xi_eff"\s*:\s*true',
    r'"target_work_allowed_next"\s*:\s*true',
]


def load_artifact() -> tuple[str, dict[str, object]]:
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(
        r"## 12\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return text, json.loads(match.group(1))


class KIGSourceMiningPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text, cls.summary = load_artifact()

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_identity_and_no_source_receipt_claim(self) -> None:
        self.assertEqual(self.summary["artifact"], "K_IGSourceMiningPacket_V1")
        self.assertEqual(
            self.summary["verdict"],
            "CONDITIONAL_PACKET_READY_NO_SOURCE_RECEIPT_CLAIMED",
        )
        self.assertEqual(self.summary["verdict_class"], "conditional")
        self.assertIs(self.summary["source_receipt_claimed"], False)
        self.assertIs(self.summary["packet_ready"], True)
        self.assertEqual(
            self.summary["target_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )
        self.assertIn("| `SOURCE_RECEIPT_FOUND` | no |", self.text)

    def test_required_mining_fields_are_complete(self) -> None:
        countable = self.summary["what_would_count"]
        self.assertEqual(set(countable["receipt_kinds"]), REQUIRED_RECEIPT_KINDS)
        self.assertEqual(set(countable["minimum_fields"]), REQUIRED_MINIMUM_FIELDS)
        for field in REQUIRED_MINIMUM_FIELDS:
            self.assertIn(field, self.text)

    def test_accept_and_reject_conditions_are_decisive(self) -> None:
        self.assertEqual(
            set(self.summary["accept_conditions"]),
            REQUIRED_ACCEPT_CONDITIONS,
        )
        self.assertEqual(
            set(self.summary["reject_conditions"]),
            REQUIRED_REJECT_CONDITIONS,
        )
        for decision in [
            "ACCEPT_SOURCE_FORCED_SELECTOR",
            "REJECT_SELECTOR_ROUTE",
            "INSUFFICIENT_RECEIPT_CONTINUE_MINING",
        ]:
            self.assertIn(decision, self.text)

    def test_strongest_positive_packet_is_mining_not_promotion(self) -> None:
        packet = self.summary["strongest_positive_packet"]
        self.assertIn("GU-MEDIA-2013-OXFORD", packet["source_surface_priority"])
        self.assertIn("GU-MEDIA-2020-PORTAL-SPECIAL", packet["source_surface_priority"])
        self.assertIn("GU-MEDIA-2021-DRAFT-RELEASE", packet["source_surface_priority"])
        self.assertIn("K_IG_D_A_U", packet["desired_emitted_rule"])
        self.assertEqual(
            packet["positive_status_if_found"],
            "candidate_source_receipt_found_pending_formal_audit",
        )
        self.assertIs(packet["not_a_promotion"], True)

    def test_candidate_classes_must_be_decided(self) -> None:
        rows = {
            row["id"]: row for row in self.summary["candidate_class_decisions_required"]
        }
        self.assertEqual(set(rows), EXPECTED_CLASSES)
        self.assertIn("selected_by_source", rows["EXT_DERIVATIVE"]["required_decision"])
        for class_id in EXPECTED_CLASSES - {"EXT_DERIVATIVE"}:
            self.assertIn("eliminated_by_source", rows[class_id]["required_decision"])

    def test_first_obstruction_and_blocks_before_are_explicit(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "SourceForcedCodomainSelectorForK_IG")
        self.assertIs(obstruction["still_missing"], True)
        self.assertIn("no primary source receipt", obstruction["description"])
        for blocked in [
            "theta_FLRW_coefficients",
            "dark_energy_or_Lambda_claims",
            "physical_reduction",
        ]:
            self.assertIn(blocked, obstruction["blocks_before"])

    def test_absorber_and_target_import_checks_are_required(self) -> None:
        checks = self.summary["absorber_target_checks"]
        self.assertIs(checks["absorber_check_required"], True)
        self.assertIs(checks["target_import_check_required"], True)
        self.assertEqual(checks["target_inputs_allowed_before_selector"], [])
        forbidden = set(checks["forbidden_target_inputs_before_selector"])
        for item in [
            "theta",
            "FLRW",
            "dark_energy",
            "Lambda",
            "DESI",
            "Z_theta",
            "C_Rtheta",
            "xi_eff",
            "target_coefficient_fit",
            "observational_performance",
        ]:
            self.assertIn(item, forbidden)
        self.assertIn("neutral_labels", checks["replacement_check"])

    def test_future_task_contract_has_fields_and_sequential_dependency(self) -> None:
        contract = self.summary["future_task_contract"]
        self.assertIn("without claiming it exists", contract["task"])
        self.assertEqual(set(contract["required_output_fields"]), REQUIRED_TASK_FIELDS)
        self.assertEqual(
            set(contract["accepted_decisions"]),
            {
                "ACCEPT_SOURCE_FORCED_SELECTOR",
                "REJECT_SELECTOR_ROUTE",
                "INSUFFICIENT_RECEIPT_CONTINUE_MINING",
            },
        )
        self.assertIn("Source mining -> selector receipt audit", contract["sequential_dependency"])
        self.assertIn("target-facing theta/FLRW", contract["sequential_dependency"])

    def test_no_flrw_or_dark_energy_promotion(self) -> None:
        anti = self.summary["anti_overclaim"]
        for key in [
            "source_receipt_exists",
            "K_IG_D_A_U_source_forced",
            "naturalness_eliminates_alternatives",
            "target_performance_selects_K_IG",
            "Branch_3_emits_theta_FLRW_coefficients",
            "GU_derives_dark_energy",
            "GU_derives_Lambda",
            "GU_derives_Z_theta",
            "GU_derives_C_Rtheta",
            "GU_derives_xi_eff",
        ]:
            self.assertIn(key, anti)
            self.assertIs(anti[key], False)

        impact = self.summary["claim_impact"]
        self.assertEqual(impact["Branch_3_status"], "coherent_host_not_selected_dynamics")
        self.assertEqual(
            impact["next_gate"],
            "primary_source_mining_and_receipt_audit_for_K_IG",
        )
        self.assertIs(impact["target_work_allowed_next"], False)

    def test_text_does_not_smuggle_positive_source_or_target_claims(self) -> None:
        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                pattern,
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
