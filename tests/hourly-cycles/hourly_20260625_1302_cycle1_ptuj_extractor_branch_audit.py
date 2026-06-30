#!/usr/bin/env python3
"""Audit the 1302 cycle 1 PTUJ extractor branch decision."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1302-cycle1-ptuj-extractor-branch.md"
)

EXPECTED_ARTIFACT = "LawfulLocalTzSEvmqxu48FrameExtractorBranchDecision_V1"
EXPECTED_VERDICT = (
    "BLOCKED_NO_CURRENT_REPO_LOCAL_LAWFUL_REPRODUCIBLE_EXTRACTOR_BRANCH"
)
EXPECTED_RUN_ID = "hourly-20260625-1302"

NON_RECEIPT_TYPES = {
    "PTUJ_caption_text",
    "YouTube_oEmbed_JSON",
    "YouTube_watch_page_or_embed_reachability",
    "YouTube_thumbnail",
    "low_resolution_storyboard_frames",
    "Keating_missing_sheet_locator",
}

DISALLOWED_PROMOTION_PATTERNS = [
    r"\baccepted_receipt_count:\s*[1-9]",
    r'"accepted_receipt_count"\s*:\s*[1-9]',
    r"\bproof_restart_allowed:\s*true\b",
    r'"proof_restart_allowed"\s*:\s*true',
    r"\bclaim_promotion_allowed:\s*true\b",
    r'"claim_promotion_allowed"\s*:\s*true',
    r"\bformula_asset_captured:\s*true\b",
    r'"formula_asset_captured"\s*:\s*true',
    r"\bSourceForcedCodomainSelectorForK_IG_accepted:\s*true\b",
    r'"SourceForcedCodomainSelectorForK_IG_accepted"\s*:\s*true',
    r"\bfamily_identity_passed:\s*true\b",
    r'"family_identity_passed"\s*:\s*true',
    r"\bglobal_no_go:\s*true\b",
    r'"global_no_go"\s*:\s*true',
    r"\bmetadata accepted as formula receipt\b",
    r"\boEmbed accepted as formula receipt\b",
    r"\bcaption accepted as formula receipt\b",
    r"\bstoryboard accepted as formula receipt\b",
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


class PtujExtractorBranchAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_identity_and_verdict(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(
            self.summary["target_branch"],
            "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
        )
        self.assertEqual(self.summary["target_video_id"], "TzSEvmqxu48")
        self.assertFalse(
            self.summary["repo_local_lawful_reproducible_extractor_branch_exists"]
        )

    def test_required_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict: blocked.",
            "## 2. What was derived directly from repo sources.",
            "## 3. The strongest positive result.",
            "## 4. The first exact obstruction or missing proof/source object.",
            "## 5. The constructive next object that would remove or test the obstruction.",
            "## 6. What this means for PTUJ/Keating and IG selector routing.",
            "## 7. Next meaningful proof/source computation step.",
            "## 8. Machine-readable JSON summary.",
        ]:
            self.assertIn(heading, self.text)

    def test_zero_receipts_unless_fully_source_backed_extractor_present(self) -> None:
        branch_fields = self.summary["branch_fields"]
        fully_source_backed_extractor_present = all(
            [
                self.summary["repo_local_lawful_reproducible_extractor_branch_exists"],
                branch_fields["lawful_basis_present"],
                branch_fields["toolchain_identity_present"],
                branch_fields["decode_scope_present"],
                branch_fields["output_manifest_present"],
                branch_fields["source_asset_checksums_present"],
            ]
        )
        if not fully_source_backed_extractor_present:
            self.assertEqual(self.summary["accepted_receipt_count"], 0)
            self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_extractor_and_official_asset_branches_not_conflated(self) -> None:
        distinctions = self.summary["branch_distinctions"]
        self.assertEqual(
            distinctions["extractor_branch_id"],
            "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
        )
        self.assertEqual(
            distinctions["official_asset_branch_id"],
            "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1",
        )
        self.assertTrue(distinctions["extractor_branch_is_not_official_asset_branch"])
        self.assertFalse(distinctions["extractor_branch_accepted"])
        self.assertFalse(distinctions["official_asset_branch_accepted"])
        self.assertFalse(self.summary["branches_conflated"])
        self.assertFalse(self.summary["official_asset_branch_tested_by_this_lane"])
        forbidden = self.summary["forbidden_promotions"]
        self.assertFalse(
            forbidden["extractor_branch_conflated_with_official_asset_branch"]
        )
        self.assertFalse(
            forbidden["official_asset_branch_conflated_with_extractor_branch"]
        )

    def test_metadata_oembed_caption_storyboard_are_not_receipts(self) -> None:
        rows = {
            row["object_type"]: row for row in self.summary["non_receipt_evidence"]
        }
        self.assertEqual(set(rows), NON_RECEIPT_TYPES)
        for object_type in NON_RECEIPT_TYPES:
            self.assertFalse(
                rows[object_type]["accepted_as_formula_receipt"],
                object_type,
            )
        self.assertFalse(
            self.summary["forbidden_promotions"][
                "metadata_oembed_caption_storyboard_accepted_as_formula_receipt"
            ]
        )
        self.assertFalse(
            self.summary["forbidden_promotions"][
                "metadata_converted_to_formula_packet_without_source_asset"
            ]
        )

    def test_toolchain_and_asset_branch_fields_remain_missing(self) -> None:
        toolchain = self.summary["toolchain_availability"]
        self.assertTrue(toolchain["python_available"])
        for key in [
            "yt_dlp_module_available",
            "yt_dlp_executable_available",
            "youtube_dl_executable_available",
            "ffmpeg_available",
            "admitted_extraction_command_present",
        ]:
            self.assertFalse(toolchain[key], key)

        assets = self.summary["repo_local_asset_availability"]
        for key in [
            "local_tzsevmqxu48_media_file_found",
            "official_formula_source_asset_package_found",
            "decoded_frame_manifest_found",
            "formula_bearing_frame_or_source_asset_found",
        ]:
            self.assertFalse(assets[key], key)

        fields = self.summary["branch_fields"]
        self.assertTrue(fields["input_locator_present"])
        self.assertTrue(fields["target_import_guard_present"])
        for key in [
            "lawful_basis_present",
            "toolchain_identity_present",
            "decode_scope_present",
            "output_manifest_present",
            "source_asset_checksums_present",
            "formula_visibility_evidence_present",
        ]:
            self.assertFalse(fields[key], key)

    def test_first_obstruction_and_next_object(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
        )
        self.assertEqual(
            obstruction["missing_object"],
            "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
        )
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "LawfulLocalTzSEvmqxu48FrameExtractor_V1")
        self.assertTrue(next_object["would_remove_or_test_obstruction"])
        self.assertFalse(next_object["would_create_receipt_by_itself"])

    def test_ig_routing_closed(self) -> None:
        routing = self.summary["ptuj_keating_ig_routing"]
        self.assertEqual(routing["ptuj_keating_route_status"], "blocked_before_routing")
        self.assertTrue(routing["formula_packet_required_before_identity_review"])
        self.assertFalse(routing["keating_sheet_identity_passed"])
        self.assertFalse(routing["source_forced_codomain_selector_for_k_ig_accepted"])
        self.assertFalse(routing["ig_selector_routing_allowed"])

    def test_disallowed_promotion_phrases_absent(self) -> None:
        for pattern in DISALLOWED_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                pattern,
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
