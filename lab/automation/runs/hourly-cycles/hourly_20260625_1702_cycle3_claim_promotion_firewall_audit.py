"""Audit CLAIM_PROMOTION_FIREWALL_AFTER_1702_C3_L4_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "hourly-20260625-1702-cycle3-claim-promotion-firewall.md"

EXPECTED_ARTIFACT_ID = "CLAIM_PROMOTION_FIREWALL_AFTER_1702_C3_L4_V1"
EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_OWNED_PATH = "explorations/hourly-20260625-1702-cycle3-claim-promotion-firewall.md"
EXPECTED_AUDIT = "tests/hourly_20260625_1702_cycle3_claim_promotion_firewall_audit.py"

REQUIRED_CLAIM_IDS = {
    "ptuj_formula_packet",
    "keating_identity",
    "ig_selector_theorem",
    "ig_family_identity",
    "dgu_actual_0_1_packet",
    "dgu_vz_replay",
    "rs_typed_operator",
    "qft_raw_branch_packet",
    "qft_quotient_descent",
    "qft_bell_chsh_rho_ab",
    "major_gu_claim",
    "global_no_go",
}

REQUIRED_SUBSTITUTES = {
    "metadata",
    "chirality_only_checks",
    "typed_spines",
    "transcript_locators",
    "schema_only_packets",
    "scoped_blockers",
}


def load_text() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing claim promotion firewall artifact: {DOC}") from exc


def extract_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError("missing YAML frontmatter block")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def extract_json_summary(text: str) -> dict:
    blocks = re.findall(r"```json\n(.*?)\n```", text, re.DOTALL)
    if not blocks:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(blocks[-1])


class ClaimPromotionFirewallAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = load_text()
        cls.frontmatter = extract_frontmatter(cls.text)
        cls.summary = extract_json_summary(cls.text)
        cls.promotion_rows = cls.summary["promotion_rows"]
        cls.rows_by_claim = {row["claim_id"]: row for row in cls.promotion_rows}

    def test_frontmatter_and_json_identity_match_assignment(self) -> None:
        self.assertEqual(self.frontmatter["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.frontmatter["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.frontmatter["cycle"], "3")
        self.assertEqual(self.frontmatter["lane"], "4")
        self.assertEqual(self.frontmatter["verdict"], "NO_PROMOTIONS_ALLOWED_PROOF_RESTART_BLOCKED")
        self.assertEqual(self.frontmatter["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.frontmatter["companion_audit"], EXPECTED_AUDIT)

        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)

    def test_all_required_promotion_rows_exist(self) -> None:
        self.assertEqual(set(self.summary["required_claim_ids"]), REQUIRED_CLAIM_IDS)
        self.assertEqual(set(self.rows_by_claim), REQUIRED_CLAIM_IDS)
        self.assertEqual(len(self.promotion_rows), len(REQUIRED_CLAIM_IDS))

    def test_global_zero_promotion_invariants(self) -> None:
        self.assertEqual(self.summary["promotions_allowed_count"], 0)
        self.assertFalse(self.summary["proof_restart"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["major_GU_claim_promoted"])
        self.assertFalse(self.summary["global_no_go"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertFalse(self.summary["target_import"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)

    def test_each_forbidden_promotion_has_missing_object(self) -> None:
        for row in self.promotion_rows:
            self.assertTrue(row["forbidden"], row["claim_id"])
            self.assertFalse(row["promotion_allowed"], row["claim_id"])
            self.assertIsInstance(row["missing_object"], str, row["claim_id"])
            self.assertNotEqual(row["missing_object"].strip(), "", row["claim_id"])
            self.assertIsInstance(row["reason"], str, row["claim_id"])
            self.assertNotEqual(row["reason"].strip(), "", row["claim_id"])

    def test_required_substitute_rejections_are_explicit(self) -> None:
        substitutes = {row["id"]: row for row in self.summary["forbidden_substitutes"]}
        self.assertEqual(set(substitutes), REQUIRED_SUBSTITUTES)
        for row in substitutes.values():
            self.assertFalse(row["promotion_allowed"])
            self.assertIsInstance(row["reason"], str)
            self.assertNotEqual(row["reason"].strip(), "")

    def test_promotion_rows_reject_expected_substitutes(self) -> None:
        expected_by_claim = {
            "ptuj_formula_packet": "metadata",
            "keating_identity": "metadata",
            "ig_selector_theorem": "chirality_only_checks",
            "ig_family_identity": "chirality_only_checks",
            "dgu_actual_0_1_packet": "typed_spines",
            "dgu_vz_replay": "typed_spines",
            "rs_typed_operator": "transcript_locators",
            "qft_raw_branch_packet": "schema_only_packets",
            "qft_quotient_descent": "schema_only_packets",
            "qft_bell_chsh_rho_ab": "schema_only_packets",
            "major_gu_claim": "scoped_blockers",
            "global_no_go": "scoped_blockers",
        }
        for claim_id, substitute in expected_by_claim.items():
            self.assertEqual(self.rows_by_claim[claim_id]["forbidden_substitute_rejected"], substitute)

    def test_downstream_claims_are_individually_locked(self) -> None:
        locked_claims = {
            "ptuj_formula_packet",
            "keating_identity",
            "ig_selector_theorem",
            "ig_family_identity",
            "dgu_actual_0_1_packet",
            "dgu_vz_replay",
            "rs_typed_operator",
            "qft_raw_branch_packet",
            "qft_quotient_descent",
            "qft_bell_chsh_rho_ab",
        }
        for claim_id in locked_claims:
            row = self.rows_by_claim[claim_id]
            self.assertFalse(row["promotion_allowed"])
            self.assertTrue(row["missing_object"])

    def test_text_names_firewall_rejections(self) -> None:
        for phrase in (
            "metadata",
            "chirality-only checks",
            "typed spines",
            "transcript locators",
            "schema-only packets",
            "scoped blockers",
        ):
            self.assertIn(phrase, self.text)

    def test_next_objects_are_named_for_producer_work(self) -> None:
        next_objects = self.summary["next_objects"]
        self.assertEqual(next_objects["PTUJ"], "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT")
        self.assertEqual(next_objects["IG"], "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1")
        self.assertEqual(next_objects["DGU_VZ"], "SourceEmittedActualDGU01SameOperatorPacket_V1")
        self.assertEqual(next_objects["RS"], "UCSDCaptureStackExecutionLedgerForRolledOperatorWindow_V1")
        self.assertEqual(next_objects["QFT"], "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1")


if __name__ == "__main__":
    unittest.main()
