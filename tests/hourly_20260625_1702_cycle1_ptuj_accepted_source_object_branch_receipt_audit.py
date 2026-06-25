"""Audit PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT_1702_C1_L1_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "hourly-20260625-1702-cycle1-ptuj-accepted-source-object-branch-receipt.md"

EXPECTED_ARTIFACT_ID = "PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT_1702_C1_L1_V1"
EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_OWNED_PATH = "explorations/hourly-20260625-1702-cycle1-ptuj-accepted-source-object-branch-receipt.md"
EXPECTED_AUDIT = "tests/hourly_20260625_1702_cycle1_ptuj_accepted_source_object_branch_receipt_audit.py"

EXPECTED_BRANCH_ROWS = {
    "official_custodian_formula_source_asset",
    "lawful_local_byte_toolchain_output_manifest",
}

OFFICIAL_MISSING = {
    "custodian_source_asset_record",
    "asset_kind",
    "immutable_locator_or_path",
    "content_access",
    "checksum_or_custody_record",
    "formula_visibility_scope",
}

LOCAL_MISSING = {
    "lawful_basis",
    "source_byte_object",
    "source_byte_checksum",
    "acquisition_tool_identity",
    "decoder_tool_identity",
    "decode_scope",
    "output_manifest",
    "output_checksums",
}


def load_text() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing PTUJ branch receipt artifact: {DOC}") from exc


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


class PTUJAcceptedSourceObjectBranchReceiptAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = load_text()
        cls.frontmatter = extract_frontmatter(cls.text)
        cls.summary = extract_json_summary(cls.text)
        cls.branch_rows = {row["row_id"]: row for row in cls.summary["branch_rows"]}

    def test_frontmatter_and_json_identity_match_assignment(self) -> None:
        self.assertEqual(self.frontmatter["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.frontmatter["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.frontmatter["cycle"], "1")
        self.assertEqual(self.frontmatter["lane"], "1")
        self.assertEqual(self.frontmatter["verdict"], "blocked")
        self.assertEqual(self.frontmatter["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.frontmatter["companion_audit"], EXPECTED_AUDIT)

        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["verdict"], "blocked")
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["target_video_id"], "TzSEvmqxu48")

    def test_global_receipt_restart_and_target_import_booleans(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_branch_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_import_used_for_selection"])
        self.assertTrue(self.summary["target_import_guard"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_branch_rows_are_rejected_and_missing_required_fields(self) -> None:
        self.assertEqual(set(self.branch_rows), EXPECTED_BRANCH_ROWS)

        official = self.branch_rows["official_custodian_formula_source_asset"]
        self.assertEqual(official["status"], "rejected_blocked")
        self.assertFalse(official["accepted"])
        self.assertTrue(official["blocked"])
        self.assertEqual(official["accepted_receipt_count"], 0)
        self.assertFalse(official["proof_restart_allowed"])
        self.assertTrue(OFFICIAL_MISSING.issubset(set(official["required_fields_missing"])))
        self.assertIn("target_import_guard", official["required_fields_present"])

        local = self.branch_rows["lawful_local_byte_toolchain_output_manifest"]
        self.assertEqual(local["status"], "rejected_blocked")
        self.assertFalse(local["accepted"])
        self.assertTrue(local["blocked"])
        self.assertEqual(local["accepted_receipt_count"], 0)
        self.assertFalse(local["proof_restart_allowed"])
        self.assertTrue(LOCAL_MISSING.issubset(set(local["required_fields_missing"])))
        self.assertIn("target_import_guard", local["required_fields_present"])

    def test_missing_fields_summary_matches_branch_rows(self) -> None:
        missing_by_branch = self.summary["missing_fields_by_branch"]
        self.assertEqual(set(missing_by_branch), EXPECTED_BRANCH_ROWS)
        for row_id, row in self.branch_rows.items():
            self.assertEqual(missing_by_branch[row_id], row["required_fields_missing"])
            self.assertNotEqual(row["required_fields_missing"], [])

    def test_admission_rule_requires_exactly_one_complete_branch(self) -> None:
        rule = self.summary["admission_rule"]
        self.assertTrue(rule["accept_if_required_fields_missing_is_empty"])
        self.assertEqual(rule["accepted_branch_count_required_for_restart"], 1)
        self.assertTrue(rule["exactly_one_accepted_branch_required"])
        self.assertFalse(rule["branch_conflation_allowed"])
        self.assertFalse(rule["metadata_or_locator_can_satisfy_source_object"])

        accepted_rows = [row for row in self.summary["branch_rows"] if row["accepted"]]
        self.assertEqual(accepted_rows, [])

    def test_first_obstruction_next_object_and_promotion_firewall(self) -> None:
        self.assertEqual(
            self.summary["first_obstruction"],
            "no_current_repo_object_satisfies_either_official_custodian_source_asset_manifest_or_lawful_local_byte_toolchain_output_manifest",
        )
        exact = self.summary["first_exact_obstruction"]
        self.assertEqual(
            exact["official_branch_missing"],
            "official_or_custodian_TzSEvmqxu48_formula_source_asset_manifest_with_content_access_checksum_or_custody_and_formula_visibility_scope",
        )
        self.assertEqual(
            exact["local_branch_missing"],
            "lawful_repo_local_TzSEvmqxu48_source_byte_object_plus_admitted_toolchain_decode_scope_and_checksummed_output_manifest",
        )

        self.assertEqual(self.summary["next_object"], "PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT")
        self.assertEqual(self.summary["constructive_next_object"], "PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT")
        self.assertTrue(self.summary["next_object_explicit"])
        self.assertIn("construct_one_accepted_PTUJ_source_object_branch_receipt", self.summary["next_meaningful_proof_or_source_computation"])

        firewall = self.summary["promotion_firewall"]
        for key in (
            "ptuj_formula_promotion",
            "keating_identity_promotion",
            "ig_selector_promotion",
            "claim_promotion",
            "proof_restart",
            "metadata_as_formula_receipt",
            "locator_as_source_object",
            "oembed_as_source_object",
            "thumbnail_as_source_object",
            "caption_as_source_object",
            "target_physics_as_source_selector",
        ):
            self.assertFalse(firewall[key])

    def test_claim_consequence_blocks_formula_identity_and_restart(self) -> None:
        self.assertFalse(self.summary["ptuj_formula_promotion_allowed"])
        self.assertFalse(self.summary["keating_identity_promotion_allowed"])
        self.assertFalse(self.summary["ig_selector_promotion_allowed"])

        consequence = self.summary["ptuj_gu_claim_consequence"]
        self.assertEqual(consequence["formula_packet_status"], "blocked_before_construction")
        self.assertFalse(consequence["visibility_audit_enabled"])
        self.assertEqual(
            consequence["keating_identity_status"],
            "not_evaluable_without_ptuj_formula_source_asset_or_frame_packet",
        )
        self.assertEqual(
            consequence["ig_selector_route_status"],
            "not_admissible_without_ptuj_source_packet_and_identity_bridge",
        )
        self.assertFalse(consequence["major_gu_claim_promoted"])
        self.assertFalse(consequence["global_no_go_promoted"])
        self.assertFalse(consequence["proof_restart_allowed"])


if __name__ == "__main__":
    unittest.main()
