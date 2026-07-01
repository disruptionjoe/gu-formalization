#!/usr/bin/env python3
"""Audit DGUIdentityFieldReceiptBundle_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1503-cycle1-dgu-identity-field-receipt-bundle.md"
)

EXPECTED_FIELDS = {
    "declared_source_scope",
    "query_variants",
    "source_locator",
    "sector_rule",
    "domain",
    "codomain",
    "epsilon_0_1_convention",
    "coefficient_convention",
    "Q_projector_relation",
    "principal_symbol_first_order_data",
    "family_identity",
    "target_import_screen",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class DGUIdentityFieldReceiptBundleAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_exists_with_frontmatter(self) -> None:
        self.assertTrue(ARTIFACT.exists())
        self.assertTrue(self.text.startswith("---\n"))
        self.assertIn('artifact_id: "DGUIdentityFieldReceiptBundle_V1"', self.text)
        self.assertIn(
            'verdict: "SCOPED_REPO_LOCAL_NEGATIVE_ACTUAL_DGU_01_IDENTITY_WITNESS_ABSENT"',
            self.text,
        )
        self.assertIn(
            'owned_path: "explorations/hourly-20260625-1503-cycle1-dgu-identity-field-receipt-bundle.md"',
            self.text,
        )
        self.assertIn(
            'companion_audit: "tests/hourly_20260625_1503_cycle1_dgu_identity_field_receipt_bundle_audit.py"',
            self.text,
        )

    def test_json_identity(self) -> None:
        self.assertEqual(self.summary["artifact_id"], "DGUIdentityFieldReceiptBundle_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1503")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-1503-cycle1-dgu-identity-field-receipt-bundle.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_1503_cycle1_dgu_identity_field_receipt_bundle_audit.py",
        )

    def test_protocol_fields_and_counts(self) -> None:
        fields = self.summary["protocol_fields"]
        self.assertGreaterEqual(self.summary["protocol_field_count"], 12)
        self.assertEqual(self.summary["protocol_field_count"], len(EXPECTED_FIELDS))
        self.assertEqual({row["field"] for row in fields}, EXPECTED_FIELDS)
        self.assertEqual(self.summary["accepted_field_count"], 0)
        self.assertEqual(self.summary["accepted_fields"], [])
        self.assertEqual(self.summary["adjacent_only_field_count"], 5)
        self.assertGreaterEqual(self.summary["missing_field_count"], 7)
        self.assertEqual(
            {row["field"] for row in fields if row["accepted"]},
            set(),
        )

    def test_hit_classification_present(self) -> None:
        self.assertEqual(self.summary["accepted_hits"], [])
        self.assertGreaterEqual(len(self.summary["adjacent_only_hits"]), 8)
        self.assertGreaterEqual(self.summary["rejected_hit_count"], 8)
        self.assertGreaterEqual(self.summary["out_of_scope_hit_count"], 3)
        self.assertIn("OXFORD_023510", self.summary["adjacent_only_hits"])
        self.assertIn("UCSD_003427_003613", self.summary["adjacent_only_hits"])
        self.assertIn("VZ_BACKEND_ROWS", self.summary["rejected_hits"])
        self.assertIn("unacquired_Oxford_visual_frames", self.summary["out_of_scope_hits"])

    def test_negative_receipt_and_no_replay_decisions(self) -> None:
        self.assertFalse(self.summary["actual_identity_witness_present"])
        self.assertFalse(self.summary["actual_identity_witness_can_instantiate"])
        self.assertTrue(self.summary["scoped_negative_receipt_justified"])
        self.assertFalse(self.summary["global_negative_receipt_justified"])
        self.assertFalse(self.summary["vz_replay_allowed"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["symbol_certificate_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertTrue(self.summary["target_import_screen_passed_for_declared_bundle"])

    def test_source_scope_is_bounded(self) -> None:
        scope = self.summary["declared_source_scope"]
        self.assertEqual(scope["scope_id"], "RepoLocalDGUIdentityScope_20260625_1503_C1")
        self.assertTrue(scope["complete_for_declared_repo_local_bundle"])
        self.assertFalse(scope["global_gu_scope"])
        self.assertFalse(scope["new_web_acquisition_performed"])
        self.assertGreaterEqual(scope["included_source_count"], 12)
        self.assertIn("non_repo_primary_sources", scope["excluded_surfaces"])

    def test_first_obstruction_and_next_object(self) -> None:
        self.assertEqual(
            self.summary["first_exact_obstruction"],
            "missing_source_emitted_actual_D_GU_epsilon_0_1_identity_packet",
        )
        self.assertEqual(self.summary["first_missing_field"], "sector_rule")
        self.assertEqual(
            self.summary["constructive_next_object"],
            "DGUActual01SectorIdentityPacket_V1",
        )
        self.assertIn("Acquire_or_inspect", self.summary["next_meaningful_step"])

    def test_required_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict.",
            "## 2. What was derived directly from repo sources.",
            "## 3. The strongest positive result.",
            "## 4. The first exact obstruction or missing proof/source object.",
            "## 5. The constructive next object that would remove or test the obstruction.",
            "## 6. What this means for DGU symbol certificate, VZ replay, and scoped negative receipt.",
            "## 7. Next meaningful proof/source computation step.",
            "## 8. Machine-readable JSON summary.",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
