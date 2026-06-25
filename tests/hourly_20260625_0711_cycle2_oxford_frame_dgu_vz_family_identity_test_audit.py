#!/usr/bin/env python3
"""Audit BosonicOxfordReplacementToDGU01IdentityTest_0711_Cycle2_Lane1_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-cycle2-oxford-frame-dgu-vz-family-identity-test.md"
)

REQUIRED_ANCHORS = {
    "OxfordPortal_PPT_023510_Swervature": "02:35:10",
    "OxfordPortal_PPT_023612_Displasion": "02:36:12",
}

REQUIRED_NEXT_FIELDS = {
    "sector_rule",
    "domain",
    "codomain",
    "coefficient_packet",
    "projectors_import_maps",
    "principal_symbol_or_sufficient_first_order_data",
    "target_import_cleanliness",
    "family_identity",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class OxfordFrameDGUVZFamilyIdentityAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "BosonicOxfordReplacementToDGU01IdentityTest_0711_Cycle2_Lane1_V1",
        )
        self.assertEqual(
            self.summary["base_test"],
            "BosonicOxfordReplacementToDGU01IdentityTest_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0711")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0711-cycle2-oxford-frame-dgu-vz-family-identity-test.md",
        )

    def test_frame_anchors_are_exact(self) -> None:
        self.assertEqual(set(self.summary["oxford_anchor_ids"]), set(REQUIRED_ANCHORS))
        self.assertEqual(
            set(self.summary["oxford_anchor_timestamps"]),
            set(REQUIRED_ANCHORS.values()),
        )
        rows = self.summary["frame_anchor_results"]
        self.assertEqual(len(rows), 2)
        by_id = {row["anchor_id"]: row for row in rows}
        self.assertEqual(set(by_id), set(REQUIRED_ANCHORS))
        for anchor_id, timestamp in REQUIRED_ANCHORS.items():
            row = by_id[anchor_id]
            self.assertEqual(row["timestamp"], timestamp)
            self.assertIn(timestamp, self.text)
            self.assertIn(anchor_id, self.text)
            self.assertIn("verified_official_source_hosted_png", row["source_status"])
            self.assertFalse(row["family_identity_passed"])
            self.assertFalse(row["accepted_for_routing"])

    def test_required_object_and_identity_fields_are_recorded(self) -> None:
        self.assertEqual(
            self.summary["required_object"],
            "actual D_GU^epsilon 0/1 action/operator/EL/principal-symbol data",
        )
        self.assertEqual(
            self.summary["required_packet"],
            "OxfordBosonicTwoAnchorDGU01FamilyIdentityPacket_V1",
        )
        fields = self.summary["identity_field_status"]
        self.assertEqual(fields["sector_rule"], "missing")
        self.assertIn("missing", fields["operator_source_primary_action_or_EL"])
        self.assertEqual(fields["domain"], "missing")
        self.assertEqual(fields["codomain"], "missing")
        self.assertIn("missing", fields["principal_symbol_or_sufficient_first_order_data"])
        coeffs = fields["coefficient_packet"]
        self.assertEqual(coeffs["status"], "missing")
        self.assertEqual(coeffs["a"], "missing")
        self.assertEqual(coeffs["b"], "missing")
        self.assertEqual(coeffs["lambda_d"], "missing")
        projectors = fields["projectors_import_maps"]
        self.assertEqual(projectors["status"], "missing")
        self.assertEqual(projectors["Q_in"], "missing")
        self.assertEqual(projectors["Q_out"], "missing")
        self.assertEqual(projectors["I_Q_in"], "missing")
        self.assertEqual(projectors["P_Q_out"], "missing")
        self.assertIn("quarantined_locator", fields["target_import_cleanliness"])
        self.assertEqual(fields["family_identity"], "missing")

    def test_family_identity_is_not_accepted(self) -> None:
        family = self.summary["family_identity"]
        self.assertEqual(family["candidate_family"], "DGU_VZ")
        self.assertEqual(family["status"], "not_established")
        self.assertFalse(family["passes"])
        self.assertIn("no sector rule", family["reason"])
        attempt = self.summary["strongest_positive_identity_attempt"]
        self.assertFalse(attempt["accepted_as_identity"])
        self.assertEqual(attempt["failure_mode"], "category_change_without_identity_certificate")

    def test_zero_accepted_receipts_and_restart_guard(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing"], [])
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertIn("accepted_receipt_count: 0", self.text)
        self.assertIn("proof_restart_allowed: false", self.text)
        self.assertIn(
            "accepted_receipt_count > 0 and family_identity_checks_passed > 0",
            self.summary["proof_restart_rule"],
        )

    def test_obstruction_and_next_object_are_exact(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "missing_source_clean_family_identity_from_verified_Oxford_bosonic_frames_to_actual_D_GU_epsilon_0_1_action_operator_EL_principal_symbol_data",
        )
        self.assertEqual(
            obstruction["missing_object"],
            "OxfordBosonicTwoAnchorDGU01FamilyIdentityPacket_V1",
        )
        self.assertIn("accepted_DGU_01_receipt", obstruction["blocks"])
        self.assertIn("proof_restart", obstruction["blocks"])
        self.assertIn("domain/codomain", obstruction["description"])
        self.assertIn("coefficient packet", obstruction["description"])
        self.assertIn("family identity", obstruction["description"])
        next_step = self.summary["next_meaningful_proof_or_source_step"]
        self.assertEqual(
            next_step["object"],
            "OxfordBosonicTwoAnchorDGU01FamilyIdentityPacket_V1",
        )
        self.assertEqual(set(next_step["must_include"]), REQUIRED_NEXT_FIELDS)

    def test_demotion_condition_names_all_required_missing_objects(self) -> None:
        demotion = set(self.summary["falsification_or_demotion_condition"])
        self.assertIn("no_source_emitted_D_GU_epsilon_0_1_sector_rule", demotion)
        self.assertIn(
            "no_source_emitted_actual_D_GU_epsilon_0_1_action_operator_EL_formula",
            demotion,
        )
        self.assertIn("no_source_emitted_0_1_domain_codomain", demotion)
        self.assertIn("no_source_emitted_coefficient_packet_a_b_lambda_d", demotion)
        self.assertIn("no_source_emitted_Q_in_Q_out_import_projector_packet", demotion)
        self.assertIn("no_source_emitted_principal_symbol_or_first_order_data", demotion)
        self.assertIn(
            "no_source_emitted_family_identity_from_Oxford_bosonic_equations_to_actual_DGU_VZ_family",
            demotion,
        )
        self.assertEqual(
            self.summary["demotion_candidate_if_full_source_pass_negative"],
            "NegativePrimarySourceReceiptInstance_V1:DGU_01:OXFORD_PORTAL_2013:anchors_023510_023612",
        )

    def test_required_deliverable_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict",
            "## 2. What was derived directly from repo/source surfaces",
            "## 3. Strongest positive identity attempt",
            "## 4. First exact obstruction/missing object",
            "## 5. Impact if closed",
            "## 6. Falsification/demotion condition",
            "## 7. Next meaningful proof/source step",
            "## 8. Machine-readable JSON summary",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
