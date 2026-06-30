"""Audit PTUJToolchainSourceByteOutputManifestDecision_1503_Cycle1_Lane1_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "hourly-20260625-1503-cycle1-ptuj-toolchain-source-byte-manifest.md"

EXPECTED_ARTIFACT_ID = "PTUJToolchainSourceByteOutputManifestDecision_1503_Cycle1_Lane1_V1"
EXPECTED_OWNED_PATH = "explorations/hourly-20260625-1503-cycle1-ptuj-toolchain-source-byte-manifest.md"
EXPECTED_AUDIT = "tests/hourly_20260625_1503_cycle1_ptuj_toolchain_source_byte_manifest_audit.py"


def load_text() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing PTUJ manifest artifact: {DOC}") from exc


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


class PTUJToolchainSourceByteManifestAudit(unittest.TestCase):
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
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["verdict"], "blocked")
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["target_video_id"], "TzSEvmqxu48")

    def test_explicit_booleans_block_source_bytes_toolchain_and_output_manifest(self) -> None:
        booleans = self.summary["explicit_manifest_booleans"]
        for key in (
            "source_bytes_present",
            "toolchain_present",
            "toolchain_admitted",
            "output_manifest_present",
            "output_manifest_admitted",
            "visibility_audit_enabled",
        ):
            self.assertIn(key, booleans)
            self.assertIs(booleans[key], False, key)
        self.assertFalse(self.summary["source_byte_manifest"]["present"])
        self.assertFalse(self.summary["toolchain_manifest"]["present"])
        self.assertFalse(self.summary["output_manifest"]["present"])

    def test_first_obstruction_and_distinct_official_branch_are_recorded(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
        )
        self.assertIn(
            "repo_local_TzSEvmqxu48_source_bytes_or_source_package_with_checksum",
            obstruction["missing_objects"],
        )
        official_branch = self.summary["official_custodian_source_asset_branch"]
        self.assertEqual(official_branch["id"], "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1")
        self.assertTrue(official_branch["remains_distinct"])
        self.assertFalse(official_branch["present"])

    def test_no_target_import_or_non_receipt_promotion(self) -> None:
        self.assertFalse(self.summary["target_import_promotion"])
        self.assertTrue(self.summary["target_import_guard"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        forbidden = self.summary["forbidden_promotions"]
        for key, value in forbidden.items():
            self.assertIs(value, False, key)
        for non_receipt in (
            "metadata",
            "captions",
            "thumbnails",
            "storyboards",
            "oEmbed",
            "Python availability",
            "locator evidence",
        ):
            self.assertIn(non_receipt, self.summary["non_receipt_objects"])

    def test_tool_identity_check_does_not_promote_python_to_extractor(self) -> None:
        identities = {row["name"]: row for row in self.summary["command_identities_checked"]}
        self.assertTrue(identities["python"]["available"])
        self.assertFalse(identities["python"]["admitted_for_extraction"])
        for name in ("yt-dlp", "youtube-dl", "ffmpeg", "ffprobe", "yt_dlp", "youtube_dl"):
            self.assertFalse(identities[name]["available"], name)
            self.assertFalse(identities[name]["admitted_for_extraction"], name)


if __name__ == "__main__":
    unittest.main()
