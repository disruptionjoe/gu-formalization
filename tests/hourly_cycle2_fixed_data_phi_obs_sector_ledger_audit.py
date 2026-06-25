#!/usr/bin/env python3
"""Audit the Cycle 2 fixed-data Phi_obs sector ledger.

This is a structural audit, not a mathematical proof. It checks that the
artifact names the fixed-data selector fields, includes the sector-ledger rows,
runs the n=2 and n=4 replacement tests, records non-promoted target statuses for
T_A/T_G/T_1/T_3, and does not promote current SM or generation selector claims.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOC = (
    ROOT
    / "explorations"
    / "hourly-cycle2-fixed-data-phi-obs-sector-ledger-2026-06-24.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Fixed-data selector ledger fields",
    "## 3. What current Type II1 candidates establish",
    "## 4. Strongest positive ledger construction attempt",
    "## 5. First exact obstruction or missing proof object",
    "## 6. Impact for Phi_obs and Type II1 selector claims",
    "## 7. Rollback/falsification conditions",
    "## 8. Next meaningful computation",
    "## 9. Machine-readable JSON summary",
]

REQUIRED_X_FIELDS = {
    "N_subset_M",
    "tau",
    "A",
    "H",
    "D",
    "J",
    "gamma",
    "Phi_obs",
}

REQUIRED_LEDGER_FIELDS = {
    "X_fixedness_certificate",
    "sector_idempotents",
    "Markov_traces",
    "fusion_equivalence",
    "spectral_compatibility",
    "Connes_channel_image",
    "anomaly_shadow",
    "replacement_n2_n4_tests",
    "target_statuses",
}

REQUIRED_TARGETS = {"T_A", "T_G", "T_1", "T_3"}

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bSM is derived\b",
    r"\bStandard Model is derived\b",
    r"\bthe SM has been derived\b",
    r"\bthe Standard Model has been derived\b",
    r"\bSM gauge group is derived\b",
    r"\bthree generations are derived\b",
    r"\bType II1 selects three generations\b",
    r"\bType II_1 selects three generations\b",
    r"\bC3/D4 selects three generations\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing fixed-data Phi_obs sector ledger: {DOC}") from exc


def extract_json_summary(text: str) -> dict[str, Any]:
    marker = "## 9. Machine-readable JSON summary"
    if marker not in text:
        raise AssertionError("missing JSON summary heading")
    tail = text.split(marker, 1)[1]
    match = re.search(r"```json\s*(\{.*?\})\s*```", tail, flags=re.DOTALL)
    if not match:
        raise AssertionError("missing fenced JSON summary block")
    return json.loads(match.group(1))


class FixedDataPhiObsSectorLedgerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_json_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_is_negative_for_current_data(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "NO_CURRENT_FIXED_DATA_PHI_OBS_SELECTOR",
        )
        self.assertIn("NO_CURRENT_FIXED_DATA_PHI_OBS_SELECTOR", self.text)
        self.assertIn("fixed_data_rigidity_remains_open_empty", self.summary["explicit_verdict"])
        self.assertIs(self.summary["no_sm_generation_selector_promotion"], True)

    def test_fixed_data_and_sector_ledger_fields_are_complete(self) -> None:
        self.assertEqual(set(self.summary["fixed_data_X_fields"]), REQUIRED_X_FIELDS)
        self.assertEqual(
            set(self.summary["required_sector_ledger_fields"]),
            REQUIRED_LEDGER_FIELDS,
        )
        for field in REQUIRED_LEDGER_FIELDS:
            self.assertIn(field, self.text)

    def test_target_statuses_cover_TA_TG_T1_T3_without_promotion(self) -> None:
        statuses = self.summary["target_selection_status"]
        self.assertEqual(set(statuses), REQUIRED_TARGETS)

        for target, row in statuses.items():
            self.assertNotIn(row["status"], {"selected", "derived"}, target)
            self.assertTrue(row["reason"], target)
            self.assertTrue(row["required_promotion_object"], target)

        self.assertIn("not_selected", statuses["T_A"]["status"])
        self.assertIn("not_selected", statuses["T_G"]["status"])
        self.assertIn("not_selected", statuses["T_1"]["status"])
        self.assertIn("failed_for_current_instantiated_candidates", statuses["T_3"]["status"])

    def test_replacement_tests_require_n2_and_n4_and_show_no_obstruction(self) -> None:
        replacement = self.summary["replacement_tests"]
        self.assertIn("n_equals_2", replacement)
        self.assertIn("n_equals_4", replacement)
        self.assertIn("n_arbitrary", replacement)

        for key in ["n_equals_2", "n_equals_4"]:
            self.assertEqual(replacement[key]["result"], "same_proof_works_no_obstruction")
            self.assertEqual(replacement[key]["selector_effect"], "fails_T3_selection")

        self.assertIn("n = 2", self.text)
        self.assertIn("n = 4", self.text)
        self.assertIn("C_n", self.text)

    def test_current_candidates_keep_C3_D4_as_no_go_negative_control(self) -> None:
        candidates = self.summary["current_candidates"]
        self.assertEqual(candidates["C3_D4_visible_three"], "NO_GO_FOR_C3D4")
        self.assertEqual(candidates["C_n_crossed_product"], "NO_GO_CARDINALITY_TRANSPORT")
        self.assertEqual(candidates["equal_trace_projection_split"], "NO_GO_TRACE_EQUIVALENCE")
        self.assertEqual(candidates["fixed_data_standard_invariant"], "OPEN_EMPTY")

        attempt = self.summary["strongest_attempt"]
        self.assertEqual(attempt["candidate"], "C3_D4_negative_control")
        self.assertEqual(attempt["verdict"], "negative_control_not_selector")
        self.assertIn("external_attachment", attempt["Connes_channel_image"])

    def test_forbidden_inputs_and_rollback_conditions_are_machine_readable(self) -> None:
        forbidden = set(self.summary["forbidden_target_inputs"])
        for item in [
            "A_F",
            "finite_CC_tuple",
            "G_SM",
            "central_Z6",
            "K_SM",
            "n_equals_3",
            "C3",
            "index_3",
            "D4_arms",
            "three_projections",
            "dim_H_F_96",
            "ordinary_anomaly_free_SM_shadow",
            "physical_Higgs_data",
        ]:
            self.assertIn(item, forbidden)

        rollback = set(self.summary["rollback_conditions"])
        for condition in [
            "target_data_used_as_selector_input",
            "trace_or_Murray_von_Neumann_equivalence_only",
            "external_K_SM_or_A_F_attachment",
            "n2_or_n4_replacement_proof_still_works",
            "sectorwise_spectral_compatibility_not_checked",
            "extra_visible_modes_without_anomaly_computation",
        ]:
            self.assertIn(condition, rollback)

    def test_missing_proof_objects_are_exact(self) -> None:
        missing = set(self.summary["first_missing_proof_objects"])
        for item in [
            "FIXED_DATA_X_CERTIFICATE",
            "PHI_OBS_IMAGE_WITHOUT_TARGET_INPUT",
            "N_NEQ_3_REPLACEMENT_OBSTRUCTION",
            "SECTORWISE_SPECTRAL_COMPATIBILITY_PROOF",
            "ACTUAL_OBSERVER_MODE_ANOMALY_SHADOW",
        ]:
            self.assertIn(item, missing)

    def test_claim_impacts_do_not_promote_typeii1_selector(self) -> None:
        impacts = self.summary["claim_impacts"]
        self.assertEqual(impacts["PHI_OBS"], "contract_only_underdefined")
        self.assertEqual(impacts["TYPEII1_HOST"], "conditional_host")
        self.assertEqual(impacts["TYPEII1_SELECTOR"], "negative_filter_current_classes")
        self.assertEqual(impacts["C3_D4"], "toy_failure_negative_control")
        self.assertEqual(impacts["fixed_data_rigidity"], "open_empty")
        self.assertEqual(impacts["SM_gauge_Higgs_anomaly"], "not_promoted")

    def test_no_sm_or_generation_selector_promotion_language(self) -> None:
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(re.search(pattern, self.text), pattern)


if __name__ == "__main__":
    unittest.main(verbosity=2)
