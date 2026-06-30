"""Audit PTUJLawfulByteManifestContinuation_1602_Cycle1_Lane1_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "hourly-20260625-1602-cycle1-ptuj-lawful-byte-manifest-continuation.md"

EXPECTED_ARTIFACT_ID = "PTUJLawfulByteManifestContinuation_1602_Cycle1_Lane1_V1"
EXPECTED_RUN_ID = "hourly-20260625-1602"
EXPECTED_OWNED_PATH = "explorations/hourly-20260625-1602-cycle1-ptuj-lawful-byte-manifest-continuation.md"
EXPECTED_AUDIT = "tests/hourly_20260625_1602_cycle1_ptuj_lawful_byte_manifest_continuation_audit.py"

REQUIRED_1503_SURFACES = {
    "explorations/hourly-20260625-1503-three-cycle-fifteen-hole-synthesis.md",
    "explorations/hourly-20260625-1503-cycle1-ptuj-toolchain-source-byte-manifest.md",
    "explorations/hourly-20260625-1503-cycle2-ptuj-official-source-asset-branch.md",
    "tests/hourly_20260625_1503_cycle2_ptuj_official_source_asset_branch_audit.py",
}

VALID_VERDICT_CLASSES = {"closed", "conditional", "blocked", "fail", "no-go", "underdefined"}


def load_text() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing PTUJ continuation artifact: {DOC}") from exc


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


class PTUJLawfulByteManifestContinuationAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = load_text()
        cls.frontmatter = extract_frontmatter(cls.text)
        cls.summary = extract_json_summary(cls.text)

    def test_frontmatter_declares_expected_identity(self) -> None:
        self.assertEqual(self.frontmatter["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.frontmatter["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.frontmatter["verdict"], "blocked")
        self.assertEqual(self.frontmatter["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.frontmatter["companion_audit"], EXPECTED_AUDIT)

    def test_json_declares_required_identity_and_verdict_class(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["verdict"], "blocked")
        self.assertIn(self.summary["verdict_class"], VALID_VERDICT_CLASSES)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["target_video_id"], "TzSEvmqxu48")

    def test_receipt_and_restart_firewall_remains_closed(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        findings = self.summary["current_repo_findings"]
        self.assertFalse(findings["official_asset_manifest_present"])
        self.assertFalse(findings["lawful_byte_manifest_present"])
        self.assertFalse(findings["source_bytes_present"])
        self.assertFalse(findings["decoded_output_manifest_present"])
        self.assertFalse(findings["formula_bearing_source_packet_present"])

    def test_source_surfaces_include_1503_prior_artifacts(self) -> None:
        surfaces = set(self.summary["source_surfaces_checked"])
        self.assertTrue(REQUIRED_1503_SURFACES.issubset(surfaces))
        checks = self.summary["source_surface_checks"]
        self.assertTrue(checks["prior_1503_synthesis_checked"])
        self.assertTrue(checks["prior_1503_toolchain_artifact_checked"])
        self.assertTrue(checks["prior_1503_official_asset_artifact_checked"])
        self.assertTrue(checks["prior_1503_official_asset_audit_checked"])
        self.assertTrue(checks["repo_file_surface_scan_checked"])
        self.assertTrue(checks["repo_text_scan_checked"])

    def test_first_obstruction_and_next_object_are_explicit(self) -> None:
        self.assertIn("no_inspectable_official_or_custodian_source_asset_manifest", self.summary["first_obstruction"])
        exact = self.summary["first_exact_obstruction"]
        self.assertEqual(
            exact["official_branch_missing"],
            "official_or_custodian_TzSEvmqxu48_source_asset_with_content_access_and_checksum_or_custody_record",
        )
        self.assertEqual(
            exact["local_branch_missing"],
            "lawful_repo_local_TzSEvmqxu48_source_bytes_or_source_package_with_checksum_plus_admitted_decoder_output_manifest",
        )
        self.assertEqual(self.summary["next_object"], "PTUJ_SourceObjectAdmissionPacket_1602_V1")
        next_object = self.summary["constructive_next_object"]
        self.assertTrue(next_object["explicit"])
        self.assertEqual(next_object["accepted_branch_count_required"], 1)
        self.assertIn(
            "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
            next_object["allowed_branches"],
        )
        self.assertIn(
            "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
            next_object["allowed_branches"],
        )

    def test_promotion_firewall_booleans_reject_non_receipts(self) -> None:
        firewall = self.summary["promotion_firewall"]
        for key, value in firewall.items():
            self.assertIs(value, False, key)
        booleans = self.summary["promotion_firewall_booleans"]
        for key, value in booleans.items():
            self.assertIs(value, True, key)
        consequence = self.summary["ptuj_gu_claim_consequence"]
        self.assertFalse(consequence["visibility_audit_enabled"])
        self.assertFalse(consequence["major_gu_claim_promoted"])
        self.assertFalse(consequence["global_no_go_promoted"])


if __name__ == "__main__":
    unittest.main()
