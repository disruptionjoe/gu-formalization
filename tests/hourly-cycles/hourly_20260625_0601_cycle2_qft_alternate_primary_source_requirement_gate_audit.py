#!/usr/bin/env python3
"""Audit QFTAlternatePrimarySourceRequirementGate_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle2-qft-alternate-primary-source-requirement-gate.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class QFTAlternatePrimarySourceRequirementGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "QFTAlternatePrimarySourceRequirementGate_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0601")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 4)
        identity = self.summary["artifact_identity"]
        self.assertEqual(identity["artifact_id"], "QFTAlternatePrimarySourceRequirementGate_V1")
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0601-cycle2-qft-alternate-primary-source-requirement-gate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0601_cycle2_qft_alternate_primary_source_requirement_gate_audit.py",
        )

    def test_required_object_and_receipt_status(self) -> None:
        self.assertEqual(
            self.summary["required_object"],
            "P_fin^b: F_phys^b(O) -> K_b",
        )
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_scoped_negative_is_not_global_no_go(self) -> None:
        scoped = self.summary["manuscript_scoped_negative"]
        self.assertTrue(scoped["valid_scoped_negative"])
        self.assertTrue(scoped["scoped_negative_not_global_no_go"])
        self.assertFalse(scoped["global_no_go_allowed"])
        self.assertFalse(scoped["global_demotion_allowed"])
        self.assertEqual(scoped["page_window"], "PDF pages 54-60")
        self.assertIn("scoped negative cannot trigger global", self.text.lower())

    def test_alternate_primary_source_bundle_is_required(self) -> None:
        bundle = self.summary["alternate_primary_source_bundle_required"]
        self.assertEqual(
            bundle["id"],
            "AlternatePrimarySourceQFTFiniteProjectorReceiptBundle_V1",
        )
        self.assertTrue(bundle["required_before_positive_restart"])
        for field in [
            "bundle_id",
            "family",
            "required_object",
            "primary_source_surfaces",
            "source_ids",
            "query_log",
            "inspected_hits",
            "accepted_receipts",
            "import_screen",
            "proof_restart_policy",
        ]:
            self.assertIn(field, bundle["required_fields"])

    def test_global_negative_bundle_required_before_demotion(self) -> None:
        bundle = self.summary["global_negative_bundle_required_before_global_demotion"]
        self.assertEqual(bundle["id"], "GlobalNegativeReceiptBundle_V1")
        self.assertTrue(bundle["missing"])
        self.assertTrue(bundle["required_before_qft_finite_projector_routes_demoted"])
        self.assertEqual(bundle["accepted_receipt_count_required_for_global_negative"], 0)
        self.assertIn("all primary GU source surfaces", bundle["must_cover"])
        for field in [
            "covered_primary_source_surfaces",
            "excluded_surfaces",
            "query_log_by_surface",
            "negative_decision_by_surface",
            "variant_coverage",
            "target_import_screen",
            "global_negative_decision",
        ]:
            self.assertIn(field, bundle["required_fields"])

    def test_strongest_positive_route_still_alive_requires_p_fin_b_payload(self) -> None:
        route = self.summary["strongest_positive_route_still_alive"]
        self.assertEqual(
            route["id"],
            "AlternatePrimarySourceQFTFiniteProjectorReceiptBundle_V1",
        )
        self.assertEqual(route["status"], "alive_but_not_instantiated")
        self.assertTrue(route["accepted_receipt_required"])
        must_emit = route["accepted_receipt_must_emit"]
        self.assertIn("F_phys", must_emit["domain"])
        self.assertIn("K_b", must_emit["target"])
        self.assertIn("P_fin", must_emit["map"])
        self.assertIn("SourceModeQuotientPacket", must_emit["local_mode_payload"])

    def test_first_exact_obstruction_is_accepted_primary_receipt(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "AcceptedPrimarySourceReceiptForQFTPFinB")
        self.assertTrue(obstruction["missing"])
        self.assertEqual(obstruction["required_object"], "P_fin^b: F_phys^b(O) -> K_b")
        components = set(obstruction["missing_components"])
        self.assertIn("physical-field domain equivalent to F_phys^b(O)", components)
        self.assertIn("finite target carrier equivalent to K_b", components)

    def test_impact_and_conditions_preserve_no_restart(self) -> None:
        impact = self.summary["impact_if_closed"]
        self.assertFalse(impact["current_global_qft_demotion_allowed"])
        self.assertTrue(impact["current_alternate_primary_source_route_alive"])
        self.assertIn("SourceModeQuotientPacket", impact["if_positive_alternate_receipt"])

        conditions = self.summary["falsification_and_demotion_conditions"]
        self.assertIn("AlternatePrimarySourceQFTFiniteProjectorReceiptBundle_V1", conditions["positive_restart_condition"])
        self.assertIn("GlobalNegativeReceiptBundle_V1", conditions["global_demotion_condition"])
        self.assertIn("zero accepted receipts", conditions["global_demotion_condition"])

    def test_next_computation_is_source_query_not_proof_restart(self) -> None:
        next_step = self.summary["next_meaningful_source_or_proof_computation"]
        self.assertEqual(next_step["source_computation"], "QFTAlternatePrimarySourceQueryBundle_V1")
        self.assertEqual(next_step["proof_computation_if_positive_receipt"], "SourceModeQuotientPacket(K_b)")
        self.assertFalse(next_step["proof_restart_currently_allowed"])
        self.assertIn("inspect candidate hits for domain, target, and map", next_step["steps"])


if __name__ == "__main__":
    unittest.main()
