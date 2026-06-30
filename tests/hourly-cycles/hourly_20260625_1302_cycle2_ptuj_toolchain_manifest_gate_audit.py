#!/usr/bin/env python3
"""Audit the 1302 cycle 2 PTUJ toolchain manifest gate."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1302-cycle2-ptuj-toolchain-manifest-gate.md"
)

EXPECTED_ARTIFACT = "LawfulLocalTzSEvmqxu48ToolchainManifestGate_V1"
EXPECTED_RUN_ID = "hourly-20260625-1302"
EXPECTED_VERDICT = "BLOCKED_NO_ADMISSIBLE_TOOLCHAIN_SOURCE_BYTE_MANIFEST"

NON_RECEIPT_TYPES = {
    "PTUJ_caption_text",
    "YouTube_oEmbed_JSON",
    "YouTube_thumbnail",
    "low_resolution_storyboard_frames",
    "Keating_missing_sheet_locator",
}

DISALLOWED_PROMOTION_PATTERNS = [
    r"\badmitted_toolchain_count:\s*[1-9]",
    r'"admitted_toolchain_count"\s*:\s*[1-9]',
    r"\badmitted_manifest_count:\s*[1-9]",
    r'"admitted_manifest_count"\s*:\s*[1-9]',
    r"\baccepted_receipt_count:\s*[1-9]",
    r'"accepted_receipt_count"\s*:\s*[1-9]',
    r"\bproof_restart_allowed:\s*true\b",
    r'"proof_restart_allowed"\s*:\s*true',
    r"\big_selector_routing_allowed:\s*true\b",
    r'"ig_selector_routing_allowed"\s*:\s*true',
    r"\bformula_asset_captured:\s*true\b",
    r'"formula_asset_captured"\s*:\s*true',
    r"\bSourceForcedCodomainSelectorForK_IG_accepted:\s*true\b",
    r'"SourceForcedCodomainSelectorForK_IG_accepted"\s*:\s*true',
    r"\bfamily_identity_passed:\s*true\b",
    r'"family_identity_passed"\s*:\s*true',
    r"\bglobal_no_go:\s*true\b",
    r'"global_no_go"\s*:\s*true',
    r"\bcaption accepted as formula receipt\b",
    r"\boEmbed accepted as formula receipt\b",
    r"\bstoryboard accepted as formula receipt\b",
    r"\bthumbnail accepted as formula receipt\b",
    r"\bmetadata accepted as formula receipt\b",
]


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class PtujToolchainManifestGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_identity_and_verdict(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(
            self.summary["target_branch"],
            "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
        )
        self.assertEqual(
            self.summary["target_manifest"],
            "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
        )
        self.assertEqual(self.summary["target_video_id"], "TzSEvmqxu48")

    def test_required_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict: blocked.",
            "## 2. What was derived directly from repo sources and local environment checks.",
            "## 3. The strongest positive result.",
            "## 4. The first exact obstruction or missing source/tool object.",
            "## 5. The constructive next object that would remove or test the obstruction.",
            "## 6. What this means for PTUJ formula packet and IG selector routing.",
            "## 7. Next meaningful proof/source computation step.",
            "## 8. Machine-readable JSON summary.",
        ]:
            self.assertIn(heading, self.text)

    def test_checked_tools_are_not_admitted_toolchain(self) -> None:
        tools = {tool["name"]: tool for tool in self.summary["checked_tools"]}
        self.assertEqual(
            set(tools),
            {"python", "yt-dlp", "youtube-dl", "ffmpeg", "yt_dlp"},
        )
        self.assertTrue(tools["python"]["available"])
        self.assertFalse(tools["python"]["admitted_for_extraction"])
        for tool_name in ["yt-dlp", "youtube-dl", "ffmpeg", "yt_dlp"]:
            self.assertFalse(tools[tool_name]["available"], tool_name)
            self.assertFalse(tools[tool_name]["admitted_for_extraction"], tool_name)
        self.assertEqual(self.summary["admitted_toolchain_count"], 0)

    def test_source_bytes_and_manifests_absent(self) -> None:
        self.assertFalse(self.summary["repo_local_source_bytes_present"])
        self.assertEqual(self.summary["repo_local_source_byte_objects"], [])
        self.assertFalse(self.summary["repo_local_decoded_output_manifest_present"])
        self.assertEqual(self.summary["repo_local_decoded_output_manifests"], [])
        self.assertFalse(self.summary["repo_local_formula_bearing_packet_present"])
        self.assertFalse(self.summary["official_source_asset_branch_present"])
        self.assertEqual(self.summary["admitted_manifest_count"], 0)

    def test_no_accepted_receipt_without_toolchain_and_manifest(self) -> None:
        if not (
            self.summary["admitted_toolchain_count"] > 0
            and self.summary["admitted_manifest_count"] > 0
        ):
            self.assertEqual(self.summary["accepted_receipt_count"], 0)
            self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["ig_selector_routing_allowed"])

    def test_metadata_storyboard_caption_thumbnail_are_not_receipts(self) -> None:
        rows = {
            row["object_type"]: row for row in self.summary["non_receipt_evidence"]
        }
        self.assertEqual(set(rows), NON_RECEIPT_TYPES)
        for object_type in NON_RECEIPT_TYPES:
            self.assertFalse(rows[object_type]["accepted_as_formula_receipt"])
        self.assertTrue(self.summary["metadata_storyboard_caption_not_accepted"])
        forbidden = self.summary["forbidden_promotions"]
        self.assertFalse(
            forbidden["metadata_oembed_caption_storyboard_accepted_as_formula_receipt"]
        )
        self.assertFalse(
            forbidden["metadata_converted_to_formula_packet_without_source_bytes"]
        )
        self.assertFalse(forbidden["storyboard_preview_promoted_to_full_route_fail"])

    def test_no_external_download_required_or_performed(self) -> None:
        self.assertFalse(self.summary["external_download_required_for_this_gate"])
        self.assertFalse(self.summary["external_download_performed"])
        self.assertFalse(self.summary["network_acquisition_attempted"])
        self.assertIn("No external media was downloaded", self.text)

    def test_first_obstruction_and_minimum_manifest(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
        )
        self.assertEqual(
            set(obstruction["missing_source_tool_objects"]),
            {
                "admitted_acquisition_tool_identity",
                "admitted_decoder_tool_identity",
                "repo_local_TzSEvmqxu48_source_bytes_or_source_package",
                "decoded_frame_or_source_output_manifest_with_checksums",
            },
        )
        manifest = self.summary["minimum_manifest_to_close_gate"]
        self.assertEqual(manifest["id"], obstruction["id"])
        self.assertTrue(manifest["would_close_this_gate"])
        self.assertFalse(manifest["would_create_formula_receipt_by_itself"])
        for field in [
            "lawful_basis",
            "source_byte_object",
            "acquisition_tool_identity",
            "decoder_tool_identity",
            "input_locator",
            "decode_scope",
            "output_manifest",
            "visibility_audit_status",
            "target_import_guard",
        ]:
            self.assertIn(field, manifest["required_fields"])

    def test_formula_packet_and_ig_routing_closed(self) -> None:
        routing = self.summary["ptuj_formula_packet_and_ig_routing"]
        self.assertEqual(routing["formula_packet_status"], "blocked_before_construction")
        self.assertTrue(routing["formula_packet_required_before_keating_identity_review"])
        self.assertFalse(routing["keating_sheet_identity_passed"])
        self.assertFalse(routing["source_forced_codomain_selector_for_k_ig_accepted"])
        self.assertFalse(routing["routing_allowed"])

    def test_disallowed_promotion_phrases_absent(self) -> None:
        for pattern in DISALLOWED_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                pattern,
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
