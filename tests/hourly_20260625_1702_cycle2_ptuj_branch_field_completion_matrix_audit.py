"""Audit PTUJ_BRANCH_FIELD_COMPLETION_MATRIX_1702_C2_L1_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "hourly-20260625-1702-cycle2-ptuj-branch-field-completion-matrix.md"

EXPECTED_ARTIFACT_ID = "PTUJ_BRANCH_FIELD_COMPLETION_MATRIX_1702_C2_L1_V1"
EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_OWNED_PATH = "explorations/hourly-20260625-1702-cycle2-ptuj-branch-field-completion-matrix.md"
EXPECTED_AUDIT = "tests/hourly_20260625_1702_cycle2_ptuj_branch_field_completion_matrix_audit.py"

EXPECTED_BRANCH_ROWS = {
    "official_custodian_formula_source_asset",
    "lawful_local_byte_toolchain_output_manifest",
}

OFFICIAL_FIELDS = {
    "custodian_source_asset_record",
    "asset_kind",
    "immutable_locator_or_path",
    "content_access",
    "checksum_or_custody_record",
    "formula_visibility_scope",
    "target_import_guard",
}

LOCAL_FIELDS = {
    "lawful_basis",
    "source_byte_object",
    "source_byte_checksum",
    "acquisition_tool_identity",
    "decoder_tool_identity",
    "decode_scope",
    "output_manifest",
    "output_checksums",
    "target_import_guard",
}


def load_text() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing PTUJ branch-field matrix artifact: {DOC}") from exc


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


class PTUJBranchFieldCompletionMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = load_text()
        cls.frontmatter = extract_frontmatter(cls.text)
        cls.summary = extract_json_summary(cls.text)
        cls.branch_rows = {row["row_id"]: row for row in cls.summary["branch_rows"]}
        cls.field_rows = cls.summary["field_rows"]
        cls.fields_by_branch: dict[str, dict[str, dict]] = {}
        for row in cls.field_rows:
            cls.fields_by_branch.setdefault(row["branch_row_id"], {})[row["field"]] = row

    def test_frontmatter_and_json_identity_match_assignment(self) -> None:
        self.assertEqual(self.frontmatter["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.frontmatter["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.frontmatter["cycle"], "2")
        self.assertEqual(self.frontmatter["lane"], "1")
        self.assertEqual(self.frontmatter["verdict"], "blocked")
        self.assertEqual(self.frontmatter["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.frontmatter["companion_audit"], EXPECTED_AUDIT)

        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["verdict"], "blocked")
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["target_video_id"], "TzSEvmqxu48")

    def test_two_branch_rows_and_zero_accepted_branch_count(self) -> None:
        self.assertEqual(set(self.branch_rows), EXPECTED_BRANCH_ROWS)
        self.assertEqual(len(self.summary["branch_rows"]), 2)
        self.assertEqual(self.summary["accepted_branch_count"], 0)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)

        for row in self.summary["branch_rows"]:
            self.assertEqual(row["status"], "rejected_blocked")
            self.assertFalse(row["accepted"])
            self.assertTrue(row["blocked"])
            self.assertEqual(row["accepted_receipt_count"], 0)
            self.assertFalse(row["formula_visibility_allowed"])
            self.assertFalse(row["keating_identity_allowed"])
            self.assertFalse(row["proof_restart_allowed"])

    def test_required_field_rows_are_complete_and_statused(self) -> None:
        self.assertEqual(len(self.field_rows), len(OFFICIAL_FIELDS) + len(LOCAL_FIELDS))
        self.assertEqual(set(self.fields_by_branch), EXPECTED_BRANCH_ROWS)
        self.assertEqual(set(self.fields_by_branch["official_custodian_formula_source_asset"]), OFFICIAL_FIELDS)
        self.assertEqual(set(self.fields_by_branch["lawful_local_byte_toolchain_output_manifest"]), LOCAL_FIELDS)

        allowed_statuses = {"present", "missing", "blocked", "metadata_only"}
        for row in self.field_rows:
            self.assertIn(row["status"], allowed_statuses)
            self.assertTrue(row["required"])
            self.assertFalse(row["receipt_promoted"])

    def test_required_missing_fields_match_branch_rows(self) -> None:
        official = self.branch_rows["official_custodian_formula_source_asset"]
        local = self.branch_rows["lawful_local_byte_toolchain_output_manifest"]

        self.assertEqual(set(official["required_fields_present"]), {"target_import_guard"})
        self.assertEqual(set(local["required_fields_present"]), {"target_import_guard"})
        self.assertEqual(set(official["required_fields_missing"]), OFFICIAL_FIELDS - {"target_import_guard"})
        self.assertEqual(set(local["required_fields_missing"]), LOCAL_FIELDS - {"target_import_guard"})

        for branch_id, branch in self.branch_rows.items():
            missing_from_fields = {
                field
                for field, row in self.fields_by_branch[branch_id].items()
                if row["status"] in {"missing", "blocked", "metadata_only"} and field != "target_import_guard"
            }
            self.assertEqual(missing_from_fields, set(branch["required_fields_missing"]))
            self.assertEqual(branch["missing_required_field_count"], len(branch["required_fields_missing"]))

    def test_restart_target_import_and_formula_visibility_are_false(self) -> None:
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_import_used_for_selection"])
        self.assertTrue(self.summary["target_import_guard"])
        self.assertFalse(self.summary["formula_visibility_allowed"])
        self.assertFalse(self.summary["keating_identity_allowed"])
        self.assertFalse(self.summary["ptuj_formula_promotion_allowed"])
        self.assertFalse(self.summary["ig_selector_route_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_first_obstruction_and_next_object_are_exact(self) -> None:
        self.assertEqual(
            self.summary["first_obstruction"],
            "no_branch_has_all_required_fields_present_without_metadata_as_receipt_promotion",
        )
        exact = self.summary["first_exact_obstruction"]
        self.assertEqual(set(exact["official_branch_missing_fields"]), OFFICIAL_FIELDS - {"target_import_guard"})
        self.assertEqual(set(exact["local_branch_missing_fields"]), LOCAL_FIELDS - {"target_import_guard"})

        self.assertEqual(self.summary["next_object"], "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT")
        self.assertEqual(self.summary["constructive_next_object"], "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT")
        self.assertTrue(self.summary["next_object_explicit"])
        self.assertIn("produce_one_complete_branch_field_completion_receipt", self.summary["next_computation_or_proof_step"])

    def test_no_metadata_as_receipt_promotion(self) -> None:
        self.assertFalse(self.summary["metadata_as_receipt_promotion"])
        rule = self.summary["admission_rule"]
        self.assertTrue(rule["accept_if_all_required_fields_present"])
        self.assertEqual(rule["accepted_branch_count_required_for_restart"], 1)
        self.assertTrue(rule["exactly_one_accepted_branch_required"])
        self.assertFalse(rule["branch_conflation_allowed"])
        self.assertFalse(rule["metadata_or_locator_can_satisfy_source_object"])
        self.assertFalse(rule["schema_can_satisfy_object"])

        firewall = self.summary["promotion_firewall"]
        for key in (
            "metadata_as_receipt_promotion",
            "locator_as_source_object",
            "oembed_as_source_object",
            "thumbnail_as_source_object",
            "caption_as_source_object",
            "storyboard_as_source_object",
            "schema_as_source_object",
            "target_physics_as_source_selector",
            "ptuj_formula_promotion",
            "keating_identity_promotion",
            "proof_restart",
        ):
            self.assertFalse(firewall[key])

        metadata_or_schema_rows = [row for row in self.field_rows if row["metadata_only"]]
        self.assertNotEqual(metadata_or_schema_rows, [])
        self.assertTrue(all(not row["receipt_promoted"] for row in metadata_or_schema_rows))

    def test_claim_consequence_blocks_identity_and_restart(self) -> None:
        consequence = self.summary["ptuj_gu_claim_consequence"]
        self.assertEqual(consequence["formula_packet_status"], "blocked_before_source_object_completion")
        self.assertFalse(consequence["visibility_audit_enabled"])
        self.assertEqual(
            consequence["keating_identity_status"],
            "not_evaluable_until_one_branch_field_set_is_complete",
        )
        self.assertEqual(
            consequence["ig_selector_route_status"],
            "not_admissible_without_PTUJ_source_packet_and_identity_bridge",
        )
        self.assertFalse(consequence["major_gu_claim_promoted"])
        self.assertFalse(consequence["global_no_go_promoted"])
        self.assertFalse(consequence["proof_restart_allowed"])


if __name__ == "__main__":
    unittest.main()
