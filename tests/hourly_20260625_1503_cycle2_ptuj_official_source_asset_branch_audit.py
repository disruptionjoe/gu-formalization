"""Audit OfficialTzSEvmqxu48FormulaSourceAssetPacketDecision_1503_Cycle2_Lane1_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "hourly-20260625-1503-cycle2-ptuj-official-source-asset-branch.md"

EXPECTED_ARTIFACT_ID = "OfficialTzSEvmqxu48FormulaSourceAssetPacketDecision_1503_Cycle2_Lane1_V1"
EXPECTED_OWNED_PATH = "explorations/hourly-20260625-1503-cycle2-ptuj-official-source-asset-branch.md"
EXPECTED_AUDIT = "tests/hourly_20260625_1503_cycle2_ptuj_official_source_asset_branch_audit.py"

REQUIRED_EXPLICIT_FIELDS = {
    "official_asset_present": False,
    "custodian_source_asset_present": False,
    "locator_only_count": 5,
    "metadata_receipt_count": 4,
    "source_asset_packet_accepted": False,
    "local_extractor_required": True,
    "visibility_audit_enabled": False,
    "target_import_used": False,
    "proof_restart_allowed": False,
}


def load_text() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing PTUJ official source asset artifact: {DOC}") from exc


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


class PTUJOfficialSourceAssetBranchAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = load_text()
        cls.frontmatter = extract_frontmatter(cls.text)
        cls.summary = extract_json_summary(cls.text)

    def test_frontmatter_declares_expected_identity_and_paths(self) -> None:
        self.assertEqual(self.frontmatter["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.frontmatter["verdict"], "blocked")
        self.assertEqual(self.frontmatter["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.frontmatter["companion_audit"], EXPECTED_AUDIT)

    def test_json_summary_declares_expected_identity_and_paths(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["verdict"], "blocked")
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["target_video_id"], "TzSEvmqxu48")
        self.assertEqual(self.summary["target_branch"], "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1")

    def test_required_explicit_fields_are_present_and_consistent(self) -> None:
        explicit = self.summary["explicit_fields"]
        for key, expected in REQUIRED_EXPLICIT_FIELDS.items():
            self.assertIn(key, explicit)
            self.assertEqual(explicit[key], expected, key)
            self.assertIn(key, self.summary)
            self.assertEqual(self.summary[key], expected, key)

    def test_lookup_objects_are_locator_or_metadata_only(self) -> None:
        self.assertTrue(self.summary["source_safe_lookup_performed"])
        self.assertFalse(self.summary["large_media_downloaded"])
        self.assertFalse(self.summary["binary_asset_created"])
        self.assertEqual(len(self.summary["source_safe_lookups"]), 5)
        for row in self.summary["source_safe_lookups"]:
            self.assertFalse(row["accepted_as_source_asset"], row["check_id"])
        self.assertIn(
            "https://www.youtube.com/embed/TzSEvmqxu48?feature=oembed",
            self.summary["inspected_remote_locators"],
        )
        self.assertIn("youtube_oembed_json", self.summary["non_source_asset_objects"])
        self.assertIn("youtube_thumbnail", self.summary["non_source_asset_objects"])

    def test_first_missing_object_blocks_visibility_and_formula_packet(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object",
        )
        self.assertEqual(
            obstruction["missing_object"],
            "official_or_custodian_TzSEvmqxu48_source_asset_with_content_access_and_checksum_or_custody_record",
        )
        visibility = self.summary["ptuj_visibility_audit"]
        self.assertFalse(visibility["enabled"])
        self.assertTrue(visibility["enabled_if_official_source_asset_manifest_exists"])
        self.assertTrue(visibility["enabled_if_local_extractor_manifest_exists"])
        self.assertEqual(self.summary["formula_packet_status"], "blocked_before_construction")
        self.assertEqual(
            self.summary["keating_identity_status"],
            "not_evaluable_without_ptuj_formula_source_asset_or_frame_packet",
        )

    def test_no_target_import_or_forbidden_source_asset_promotion(self) -> None:
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_import_guard"]["target_import_used"])
        self.assertFalse(
            self.summary["target_import_guard"]["target_outcome_used_to_select_or_normalize_source_object"]
        )
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        forbidden = self.summary["forbidden_promotions"]
        for key, value in forbidden.items():
            self.assertIs(value, False, key)

    def test_constructive_next_object_can_bypass_local_extractor_if_supplied(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(
            next_object["id"],
            "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
        )
        self.assertTrue(next_object["would_bypass_local_extractor_requirement"])
        for field in (
            "custodian",
            "asset_kind",
            "immutable_locator",
            "content_access",
            "checksums_or_custody_record",
            "formula_visibility_scope",
            "target_import_guard",
        ):
            self.assertIn(field, next_object["required_fields"])


if __name__ == "__main__":
    unittest.main()
