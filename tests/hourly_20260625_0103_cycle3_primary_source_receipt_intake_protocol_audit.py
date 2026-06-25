#!/usr/bin/env python3
"""Audit PrimarySourceReceiptIntakeProtocol_V1.

The audit parses the embedded JSON summary and checks the protocol invariants:
required receipt schema, accepted source kinds, import/rejection controls,
four-family routing, no claim promotion, and sequential downstream restart
gating.
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
    / "hourly-20260625-0103-cycle3-primary-source-receipt-intake-protocol.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Source Derivations",
    "## 3. Strongest Positive Protocol",
    "## 4. Family-Specific Routing",
    "## 5. First Exact Obstruction",
    "## 6. Constructive Next Object",
    "## 7. GU Impact and Sequential Gate",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_SCHEMA_FIELDS = {
    "receipt_id",
    "family",
    "required_object",
    "source_kind",
    "source_id",
    "locator",
    "source_status",
    "exact_fragment",
    "emitted_object_type",
    "emitted_formula_or_rule",
    "representation_context",
    "normalization_choices",
    "target_data_seen",
    "import_status",
    "acceptance_status",
    "promotion_allowed",
    "restart_gate",
    "audit_notes",
}

REQUIRED_SOURCE_KINDS = {
    "official_transcript",
    "official_video_or_audio_with_timestamp",
    "author_manuscript_or_draft",
    "official_site_page",
    "archived_primary_fragment",
    "source_attached_visual",
}

REQUIRED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}

REQUIRED_NO_PROMOTIONS = {
    "IG_K_IG_selected",
    "RS_d_RS_minus_1_source_derived",
    "QFT_P_fin_b_supplied",
    "DGU_actual_operator_identified",
    "VZ_evasion_closed",
    "dark_energy_or_FLRW_recovered",
    "QFT_state_or_CHSH_recovered",
    "physical_rank_or_generation_readout",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing intake protocol: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class PrimarySourceReceiptIntakeProtocolAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)
        cls.routes = {
            row["family"]: row for row in cls.summary["family_routing"]  # type: ignore[index]
        }

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_identity_and_process_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "PrimarySourceReceiptIntakeProtocol_V1",
        )
        self.assertEqual(
            self.summary["verdict"],
            "CONDITIONAL_PROTOCOL_READY_RECEIPTS_STILL_MISSING",
        )
        self.assertEqual(self.summary["verdict_class"], "conditional")
        self.assertIs(self.summary["not_a_claim_promotion"], True)
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "PrimarySourceReceiptInstance_V1")
        self.assertIs(obstruction["missing"], True)

    def test_required_receipt_schema_fields(self) -> None:
        fields = set(self.summary["receipt_schema_required_fields"])
        self.assertEqual(fields, REQUIRED_SCHEMA_FIELDS)
        for field in ["target_data_seen", "import_status", "promotion_allowed"]:
            self.assertIn(field, self.text)

    def test_accepted_source_kinds_are_primary_only(self) -> None:
        source_kinds = set(self.summary["accepted_source_kinds"])
        self.assertEqual(source_kinds, REQUIRED_SOURCE_KINDS)
        rejected_terms = [
            "secondary_or_ai_summary_only",
            "commentary_or_reception_only",
            "unverified_paraphrase",
        ]
        controls = self.summary["import_controls"]
        triggers = (
            controls["rejection_triggers"]  # type: ignore[index]
            + controls["quarantine_triggers"]  # type: ignore[index]
        )
        for term in rejected_terms:
            self.assertIn(term, triggers)

    def test_import_controls_block_target_imports(self) -> None:
        controls = self.summary["import_controls"]
        statuses = set(controls["allowed_import_statuses"])
        self.assertIn("source_emitted", statuses)
        self.assertIn("target_import", statuses)
        self.assertIn("target_coefficients_or_outputs_used", controls["rejection_triggers"])
        self.assertIn("target_data_seen_empty", controls["accepted_for_restart_requires"])
        self.assertIn(
            "family_mathematical_identity_check_passed",
            controls["accepted_for_restart_requires"],
        )

    def test_four_family_routing_present_and_specific(self) -> None:
        self.assertEqual(set(self.routes), REQUIRED_FAMILIES)
        self.assertEqual(len(self.routes), 4)
        self.assertEqual(
            self.routes["IG"]["required_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )
        self.assertIn("d_RS,-1", self.routes["RS"]["required_object"])
        self.assertIn("P_fin^b", self.routes["QFT"]["required_object"])
        self.assertIn("D_GU^epsilon", self.routes["DGU_VZ"]["required_object"])
        for family, route in self.routes.items():
            self.assertIn("receipt_queue", route, family)
            self.assertIn("downstream_restart_blocked_until", route, family)
            self.assertIs(route["promotion_allowed"], False, family)

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        self.assertEqual(set(promotions), REQUIRED_NO_PROMOTIONS)
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertIn("No GU claim is promoted by this protocol.", self.text)

    def test_sequential_gating_before_restart(self) -> None:
        gate = self.summary["sequential_gate"]
        self.assertEqual(
            gate,
            [
                "source_intake_acceptance",
                "family_mathematical_identity_check",
                "family_limited_downstream_restart",
                "proof_worker_attempts_closure",
                "normal_proof_or_canon_promotion_gate",
            ],
        )
        policy = self.summary["downstream_restart_policy"]
        self.assertEqual(set(policy), REQUIRED_FAMILIES)
        for family, rule in policy.items():
            self.assertIn("after", rule, family)

    def test_constructive_next_object_is_map_entry_protocol(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "RepoLocalPrimaryGUSourceReceiptMap_V1")
        self.assertEqual(next_object["entry_type"], "PrimarySourceReceiptInstance_V1")
        self.assertIn("run intake", next_object["next_step"])


if __name__ == "__main__":
    unittest.main()
