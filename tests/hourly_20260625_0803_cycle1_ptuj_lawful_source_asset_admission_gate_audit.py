#!/usr/bin/env python3
"""Audit LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle1-ptuj-lawful-source-asset-admission-gate.md"
)

EXPECTED_SOURCES = {
    "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
    "GU-POD-2021-KEATING-REVEALED-1",
    "GU-POD-2021-KEATING-REVEALED-2",
    "GU-MEDIA-2021-DRAFT-RELEASE",
}

REQUIRED_MISSING_OBJECTS = {
    "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
    "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
    "KeatingRevealed_ShiabProjectionSheet_V1",
    "manuscript_equivalence_proof_to_SourceForcedCodomainSelectorForK_IG",
}


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 10\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class PtujLawfulSourceAssetAdmissionGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_identity_and_verdict_class(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0803")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_NO_LAWFUL_LOCAL_EXTRACTOR_OR_FORMULA_SOURCE_ASSET",
        )
        self.assertEqual(self.summary["target_video_id"], "TzSEvmqxu48")
        self.assertEqual(
            self.summary["target_asset_id"],
            "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
        )
        self.assertEqual(
            self.summary["required_identity_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )

    def test_sources_read_first_and_coverage(self) -> None:
        for source in [
            "RESEARCH-POSTURE.md",
            "process/runbooks/five-lane-frontier-run.md",
            "explorations/hourly-20260625-0711-three-cycle-fifteen-hole-synthesis.md",
            "explorations/hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md",
            "explorations/hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md",
            "sources/media-index.md",
        ]:
            self.assertIn(source, self.summary["sources_read_first"])
            self.assertIn(source, self.text)

        self.assertEqual(set(self.summary["required_source_surfaces"]), EXPECTED_SOURCES)
        observed = set()
        for surface in self.summary["source_coverage"]:
            observed.update(surface["source_ids"])
            self.assertFalse(surface["accepted_receipt"], surface["surface_id"])
            self.assertFalse(
                surface["formula_bearing_source_asset_admitted"],
                surface["surface_id"],
            )
        self.assertTrue(EXPECTED_SOURCES.issubset(observed))

    def test_zero_accepted_receipts_and_no_formula_asset(self) -> None:
        receipt = self.summary["receipt_state"]
        self.assertEqual(receipt["accepted_receipt_count"], 0)
        self.assertEqual(receipt["accepted_for_routing_count"], 0)
        self.assertEqual(receipt["accepted_receipts"], [])
        self.assertEqual(receipt["accepted_formula_asset_count"], 0)
        self.assertEqual(receipt["accepted_frame_packet_count"], 0)
        self.assertEqual(receipt["family_identity_checks_passed"], 0)
        self.assertFalse(receipt["formula_asset_captured"])
        self.assertFalse(receipt["thumbnail_or_caption_receipt_accepted"])
        self.assertFalse(receipt["proof_restart_allowed"])
        self.assertFalse(receipt["claim_promotion_allowed"])
        self.assertFalse(receipt["global_no_go_promoted"])

        asset = self.summary["asset_state"]
        for key in [
            "direct_source_asset_package_found",
            "local_tzsevmqxu48_media_file_found",
            "formula_bearing_frame_captured",
            "formula_bearing_source_asset_admitted",
            "keating_missing_sheet_recovered",
            "manuscript_equivalence_proof_to_selector_found",
        ]:
            self.assertFalse(asset[key], key)

    def test_missing_toolchain_is_explicit(self) -> None:
        tools = self.summary["tool_state"]
        self.assertTrue(tools["python_available"])
        self.assertFalse(tools["yt_dlp_module_available"])
        self.assertFalse(tools["yt_dlp_executable_available"])
        self.assertFalse(tools["youtube_dl_executable_available"])
        self.assertFalse(tools["ffmpeg_available"])
        self.assertFalse(tools["lawful_local_extractor_admitted"])

        checks = {row["check_id"]: row for row in self.summary["current_lane_checks"]}
        self.assertIn("LOCAL_COMMAND_RESOLUTION_0803_C1_L1", checks)
        self.assertIn("PYTHON_YTDLP_MODULE_CHECK_0803_C1_L1", checks)
        self.assertIn("LOCAL_ASSET_SEARCH_0803_C1_L1", checks)
        self.assertIn("SOURCE_URL_HEAD_RECHECK_0803_C1_L1", checks)
        for row in checks.values():
            self.assertFalse(row["accepted_receipt"], row["check_id"])
        self.assertIn("No module named yt_dlp", checks["PYTHON_YTDLP_MODULE_CHECK_0803_C1_L1"]["result"])

    def test_first_obstruction_and_next_step(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
        )
        self.assertEqual(obstruction["obstruction_type"], "admission_gate_missing_object")
        self.assertEqual(set(obstruction["missing_objects"]), REQUIRED_MISSING_OBJECTS)
        self.assertEqual(
            self.summary["next_meaningful_step"]["next_object"],
            "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
        )

    def test_no_proof_restart_or_claim_promotion(self) -> None:
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
        self.assertIn("claim_promotion_allowed: false", self.text)

    def test_required_deliverable_sections_exist(self) -> None:
        for heading in [
            "## 1. Verdict.",
            "## 2. Specific GU claim or bridge under test.",
            "## 3. Owned output path and sources read first.",
            "## 4. What was derived directly from repo sources.",
            "## 5. Strongest positive construction/admission attempt.",
            "## 6. First exact obstruction or missing object.",
            "## 7. Impact if closed.",
            "## 8. Falsification/demotion condition.",
            "## 9. Next meaningful computation or proof/source step.",
            "## 10. Machine-readable JSON summary.",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
