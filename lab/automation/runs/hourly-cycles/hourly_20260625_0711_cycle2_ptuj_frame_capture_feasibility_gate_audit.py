#!/usr/bin/env python3
"""Audit the 0711 cycle 2 PTUJ frame-capture feasibility gate."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md"
)

EXPECTED_SOURCES = {
    "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
    "GU-POD-2021-KEATING-REVEALED-1",
    "GU-POD-2021-KEATING-REVEALED-2",
    "GU-MEDIA-2021-DRAFT-RELEASE",
}


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class PtujFrameCaptureFeasibilityGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_identity_video_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureFeasibilityGate_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0711")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(self.summary["target_video_id"], "TzSEvmqxu48")
        self.assertEqual(
            self.summary["target_asset_id"],
            "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
        )
        self.assertEqual(
            self.summary["target_packet"],
            "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
        )
        self.assertEqual(
            self.summary["required_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )

    def test_source_ids_are_complete(self) -> None:
        self.assertEqual(set(self.summary["required_source_surfaces"]), EXPECTED_SOURCES)
        observed = set()
        for surface in self.summary["source_surfaces"]:
            observed.update(surface["source_ids"])
        self.assertTrue(EXPECTED_SOURCES.issubset(observed))
        youtube = next(
            row
            for row in self.summary["source_surfaces"]
            if row["surface_id"] == "YouTube_TzSEvmqxu48"
        )
        self.assertEqual(youtube["video_id"], "TzSEvmqxu48")
        self.assertIn("TzSEvmqxu48", youtube["watch_url"])
        self.assertIn("TzSEvmqxu48", youtube["oembed_url"])

    def test_retrieval_attempts_record_positive_and_negative_checks(self) -> None:
        attempts = {
            attempt["attempt_id"]: attempt for attempt in self.summary["retrieval_attempts"]
        }
        for attempt_id in [
            "PTUJ_HTML_SCAN_0711_C2",
            "YOUTUBE_OEMBED_0711_C2",
            "YOUTUBE_WATCH_HEAD_0711_C2",
            "YOUTUBE_THUMBNAIL_HEAD_0711_C2",
            "LOCAL_TOOL_CHECK_0711_C2",
            "LOCAL_ASSET_SEARCH_0711_C2",
        ]:
            self.assertIn(attempt_id, attempts)
            self.assertFalse(attempts[attempt_id]["accepted_receipt"], attempt_id)
        self.assertIn("no_mp4_no_webm", attempts["PTUJ_HTML_SCAN_0711_C2"]["result"])
        self.assertIn("yt_dlp_module_missing", attempts["LOCAL_TOOL_CHECK_0711_C2"]["result"])
        self.assertIn("ffmpeg", attempts["LOCAL_TOOL_CHECK_0711_C2"]["result"])

    def test_no_formula_asset_or_frame_packet_was_captured(self) -> None:
        capture = self.summary["capture_state"]
        self.assertFalse(capture["formula_bearing_frame_captured"])
        self.assertFalse(capture["source_asset_packet_captured"])
        self.assertFalse(capture["formula_asset_captured"])
        self.assertEqual(capture["accepted_formula_asset_count"], 0)
        self.assertEqual(capture["accepted_frame_packet_count"], 0)
        self.assertEqual(capture["accepted_receipt_count"], 0)
        self.assertEqual(capture["accepted_for_routing_count"], 0)
        self.assertEqual(capture["accepted_receipts"], [])
        self.assertFalse(capture["thumbnail_or_caption_receipt_accepted"])
        self.assertFalse(capture["proof_restart_allowed"])
        self.assertFalse(capture["claim_promotion_allowed"])

    def test_tools_missing_and_next_object_specific(self) -> None:
        tools = self.summary["tool_state"]
        self.assertFalse(tools["yt_dlp_module_available"])
        self.assertFalse(tools["yt_dlp_executable_available"])
        self.assertFalse(tools["youtube_dl_executable_available"])
        self.assertFalse(tools["ffmpeg_available"])
        self.assertFalse(tools["direct_mp4_or_webm_url_found"])

        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "LocalFrameExtractionToolchainForTzSEvmqxu48_V1",
        )
        self.assertEqual(obstruction["obstruction_type"], "tool_source_acquisition")
        self.assertIn("yt_dlp", obstruction["operational_obstruction"])
        self.assertEqual(
            obstruction["missing_next_object"],
            "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
        )
        self.assertIn(
            "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
            obstruction["missing_source_objects"],
        )
        self.assertEqual(
            self.summary["next_meaningful_acquisition_step"]["next_object"],
            "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
        )

    def test_target_import_guard_and_forbidden_promotions(self) -> None:
        guard = self.summary["target_import_guard"]
        self.assertEqual(guard["target_data_seen"], [])
        self.assertTrue(guard["target_import_clean"])
        self.assertFalse(guard["target_import_clean_sufficient_for_acceptance"])
        self.assertFalse(guard["target_outcome_used_to_select_or_normalize_source_object"])

        forbidden = self.summary["forbidden_promotions"]
        self.assertTrue(forbidden)
        for key, value in forbidden.items():
            self.assertFalse(value, key)
        self.assertIn("proof_restart_allowed: false", self.text)

    def test_required_sections_exist(self) -> None:
        for heading in [
            "## 1. Verdict",
            "## 2. What was derived directly from repo/source surfaces",
            "## 3. Strongest positive capture attempt",
            "## 4. First exact obstruction/missing object",
            "## 5. Impact if closed",
            "## 6. Falsification/demotion condition",
            "## 7. Next meaningful acquisition step",
            "## 8. Machine-readable JSON summary",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
