#!/usr/bin/env python3
"""Audit DGUIdentityFieldProtocolGate_V1.

The audit enforces that the protocol stays source-clean: zero accepted actual
identity fields, no VZ replay or symbol certificate from adjacent data, and no
scoped negative receipt before complete source coverage exists.
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
    / "hourly-20260625-1302-cycle2-dgu-identity-field-protocol-gate.md"
)

REQUIRED_PROTOCOL_FIELDS = {
    "declared_source_scope",
    "query_variant_log",
    "source_locator",
    "sector_rule",
    "domain",
    "codomain",
    "epsilon_0_1_meaning",
    "coefficient_convention",
    "Q_projector_relation",
    "principal_symbol_or_first_order_data",
    "family_identity",
    "target_import_screen",
}

ADJACENT_ONLY_FIELDS = {
    "source_locator",
    "domain",
    "codomain",
    "principal_symbol_or_first_order_data",
    "target_import_screen",
}

FORBIDDEN_PROMOTIONS = {
    "actual_operator_identity_from_Oxford_bosonic_anchors",
    "actual_operator_identity_from_manuscript_bosonic_action_EL_adjacency",
    "actual_operator_identity_from_UCSD_rolled_up_family_language",
    "accepted_certificate_fields_from_adjacent_only_anchors",
    "DGU_symbol_certificate",
    "VZ_replay",
    "FC_VZ_1_closure",
    "FC_VZ_4_closure",
    "VZ_evasion_proof",
    "hyperbolicity_or_causality_promotion",
    "dark_energy_recovery_promotion",
    "three_family_recovery_promotion",
    "proof_restart",
    "scoped_negative_receipt_from_incomplete_source_coverage",
    "global_no_go_from_scoped_or_blocked_DGU_searches",
}

PROMOTION_PHRASES = [
    r"actual identity witness present:\s*true",
    r"actual operator identity from (?:Oxford|manuscript|UCSD).*accepted",
    r"accepted(?: actual)? identity fields?:\s*[1-9]",
    r"accepted_field_count:\s*[1-9]",
    r"accepted certificate fields?:\s*[1-9]",
    r"VZ replay allowed:\s*true",
    r"symbol certificate (?:is )?allowed:\s*true",
    r"scoped negative (?:primary )?receipt (?:is )?justified:\s*true",
    r"proof restart allowed:\s*true",
    r"VZ evasion (?:is |has been )?(?:proved|established|closed)",
    r"FC-VZ-1 (?:is |has been )?closed",
    r"FC-VZ-4 (?:is |has been )?closed",
]


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section-8 machine-readable JSON summary")
    return json.loads(match.group(1))


class DGUIdentityFieldProtocolGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact_id"], "DGUIdentityFieldProtocolGate_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-1302-cycle2-dgu-identity-field-protocol-gate.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_1302_cycle2_dgu_identity_field_protocol_gate.py",
        )

    def test_required_protocol_fields_are_present(self) -> None:
        fields = self.summary["protocol_fields"]
        self.assertEqual(self.summary["protocol_field_count"], len(REQUIRED_PROTOCOL_FIELDS))
        self.assertEqual({row["field"] for row in fields}, REQUIRED_PROTOCOL_FIELDS)
        for row in fields:
            self.assertIn("must_emit", row, row["field"])
            self.assertIn("check", row, row["field"])
            self.assertIn("repo_anchor", row, row["field"])
            self.assertFalse(row["accepted"], row["field"])

    def test_no_accepted_fields_and_adjacent_only_accounting(self) -> None:
        fields = self.summary["protocol_fields"]
        self.assertEqual(self.summary["accepted_fields"], [])
        self.assertEqual(self.summary["accepted_field_count"], 0)
        self.assertEqual(set(self.summary["adjacent_only_fields"]), ADJACENT_ONLY_FIELDS)
        self.assertEqual(self.summary["adjacent_only_field_count"], len(ADJACENT_ONLY_FIELDS))
        self.assertEqual(
            {row["field"] for row in fields if row["adjacent_only"]},
            ADJACENT_ONLY_FIELDS,
        )
        self.assertTrue(
            all(row["current_status"] in {"missing", "missing_for_negative_receipt", "adjacent_only"} for row in fields)
        )

    def test_source_clean_data_required_before_vz_or_symbol_replay(self) -> None:
        self.assertFalse(self.summary["actual_identity_witness_present"])
        self.assertFalse(self.summary["vz_replay_allowed"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["symbol_certificate_allowed"])
        self.assertFalse(self.summary["actual_operator_certificate_allowed"])
        self.assertFalse(self.summary["dgu_vz_replay"]["allowed"])
        self.assertFalse(self.summary["symbol_certificate"]["allowed"])
        self.assertIn("zero_accepted_actual_identity_fields", self.summary["dgu_vz_replay"]["reason"])
        self.assertIn("adjacent_only", self.summary["symbol_certificate"]["reason"])

    def test_scoped_negative_receipt_not_justified_from_incomplete_coverage(self) -> None:
        self.assertFalse(self.summary["scoped_negative_receipt_justified"])
        self.assertIn("incomplete_source_coverage", self.summary["scoped_negative_receipt_reason"])
        self.assertEqual(
            self.summary["scoped_negative_receipt_candidate"],
            "NegativePrimarySourceReceiptInstance_V1:DGU_01:actual_identity_witness",
        )
        self.assertIn(
            "not_justified_until_complete_source_scope",
            self.summary["scoped_negative_receipt_candidate_status"],
        )
        self.assertEqual(
            self.summary["first_exact_obstruction"],
            "missing_complete_DGUIdentityFieldReceiptBundle_V1_for_actual_D_GU_epsilon_0_1",
        )
        self.assertEqual(
            self.summary["constructive_next_object"],
            "DGUIdentityFieldReceiptBundle_V1",
        )

    def test_forbidden_promotions_declared(self) -> None:
        self.assertEqual(set(self.summary["forbidden_promotions"]), FORBIDDEN_PROMOTIONS)

    def test_no_actual_operator_promotion_phrases(self) -> None:
        for pattern in PROMOTION_PHRASES:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion phrase matched: {pattern}",
            )

    def test_required_deliverable_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict: blocked.",
            "## 2. What was derived directly from repo sources.",
            "## 3. The strongest positive result.",
            "## 4. The first exact obstruction or missing source/proof object.",
            "## 5. The constructive next object that would remove or test the obstruction.",
            "## 6. What this means for DGU/VZ replay, symbol certificate, and scoped negative receipt.",
            "## 7. Next meaningful proof/source computation step.",
            "## 8. Machine-readable JSON summary.",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
