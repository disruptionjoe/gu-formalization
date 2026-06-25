"""Audit PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT_1802_C1_L1_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "hourly-20260625-1802-cycle1-ptuj-branch-field-completion-receipt.md"

EXPECTED_RUN_ID = "hourly-20260625-1802"
EXPECTED_ARTIFACT_ID = "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT_1802_C1_L1_V1"
EXPECTED_OWNED_PATH = "explorations/hourly-20260625-1802-cycle1-ptuj-branch-field-completion-receipt.md"
EXPECTED_AUDIT = "tests/hourly_20260625_1802_cycle1_ptuj_branch_field_completion_receipt_audit.py"

EXPECTED_BRANCH_ROWS = {
    "official_custodian_formula_source_asset",
    "lawful_local_byte_toolchain_output_manifest",
}


def load_text() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing PTUJ receipt artifact: {DOC}") from exc


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


class PTUJBranchFieldCompletionReceiptAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = load_text()
        cls.frontmatter = extract_frontmatter(cls.text)
        cls.summary = extract_json_summary(cls.text)
        cls.branches = {row["row_id"]: row for row in cls.summary["branch_rows"]}

    def test_identity_fields_match_assignment(self) -> None:
        self.assertEqual(self.frontmatter["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.frontmatter["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.frontmatter["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.frontmatter["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.frontmatter["verdict"], "blocked")

        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["target_video_id"], "TzSEvmqxu48")
        self.assertEqual(self.summary["receipt_id"], "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT")

    def test_exactly_two_branch_rows_and_counts(self) -> None:
        self.assertEqual(len(self.summary["branch_rows"]), 2)
        self.assertEqual(set(self.branches), EXPECTED_BRANCH_ROWS)
        self.assertEqual(self.summary["accepted_branch_count"], 0)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)

        accepted = [row for row in self.summary["branch_rows"] if row["accepted"]]
        self.assertEqual(len(accepted), self.summary["accepted_branch_count"])
        self.assertEqual(
            sum(row["accepted_receipt_count"] for row in self.summary["branch_rows"]),
            self.summary["accepted_receipt_count"],
        )

    def test_proof_restart_false_unless_exactly_one_branch_is_accepted(self) -> None:
        exactly_one_branch_accepted = self.summary["accepted_branch_count"] == 1
        if exactly_one_branch_accepted:
            self.assertTrue(self.summary["proof_restart_allowed"])
        else:
            self.assertFalse(self.summary["proof_restart_allowed"])

        self.assertTrue(self.summary["exactly_one_accepted_branch_required_for_restart"])
        self.assertEqual(
            self.summary["proof_restart_allowed_rule"],
            "false_unless_exactly_one_branch_is_accepted",
        )

    def test_metadata_as_receipt_is_false(self) -> None:
        self.assertFalse(self.summary["metadata_as_receipt"])
        self.assertFalse(self.summary["metadata_as_receipt_promotion"])
        for row in self.summary["field_rows"]:
            self.assertFalse(row["receipt_promoted"])
        self.assertTrue(any(row["metadata_only"] for row in self.summary["field_rows"]))

    def test_blocked_missing_fields_are_nonempty(self) -> None:
        self.assertEqual(self.summary["verdict_class"], "blocked")
        if self.summary["verdict_class"] == "blocked":
            for row in self.summary["branch_rows"]:
                self.assertTrue(row["blocked"])
                self.assertFalse(row["accepted"])
                self.assertGreater(row["missing_required_field_count"], 0)
                self.assertNotEqual(row["required_fields_missing"], [])

            obstruction = self.summary["first_exact_obstruction"]
            self.assertNotEqual(obstruction["official_branch_missing_fields"], [])
            self.assertNotEqual(obstruction["local_branch_missing_fields"], [])

    def test_missing_fields_match_branch_and_field_rows(self) -> None:
        fields_by_branch: dict[str, set[str]] = {}
        for row in self.summary["field_rows"]:
            if row["status"] in {"missing", "blocked", "metadata_only"}:
                fields_by_branch.setdefault(row["branch_row_id"], set()).add(row["field"])

        for branch_id, branch in self.branches.items():
            self.assertEqual(set(branch["required_fields_missing"]), fields_by_branch[branch_id])
            self.assertEqual(branch["missing_required_field_count"], len(branch["required_fields_missing"]))
            self.assertEqual(branch["required_fields_present"], ["target_import_guard"])

        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            set(obstruction["official_branch_missing_fields"]),
            set(self.branches["official_custodian_formula_source_asset"]["required_fields_missing"]),
        )
        self.assertEqual(
            set(obstruction["local_branch_missing_fields"]),
            set(self.branches["lawful_local_byte_toolchain_output_manifest"]["required_fields_missing"]),
        )

    def test_downstream_gates_remain_closed(self) -> None:
        self.assertFalse(self.summary["target_import_used"])
        self.assertTrue(self.summary["target_import_guard"])
        self.assertFalse(self.summary["formula_visibility_allowed"])
        self.assertFalse(self.summary["keating_comparison_allowed"])
        self.assertFalse(self.summary["ig_selector_route_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertEqual(
            self.summary["first_obstruction"],
            "no_branch_has_every_required_field_without_metadata_as_receipt_promotion",
        )
        self.assertIn(
            "produce_one_complete_PTUJ_branch_receipt",
            self.summary["next_meaningful_step"],
        )


if __name__ == "__main__":
    unittest.main()
