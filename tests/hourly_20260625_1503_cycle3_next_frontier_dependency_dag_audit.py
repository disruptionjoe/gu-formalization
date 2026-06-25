"""Audit NextFrontierDependencyDagAfter1503_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1503-cycle3-next-frontier-dependency-dag.md"
)

EXPECTED_ARTIFACT_ID = "NextFrontierDependencyDagAfter1503_V1"
EXPECTED_RUN_ID = "hourly-20260625-1503"
EXPECTED_VERDICT = "UPSTREAM_SOURCE_OBJECTS_NO_RECEIPTS_NO_PROOF_RESTART"
EXPECTED_NEXT_FIVE = {
    "PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION",
    "IG_D7_PROOF_TRANSCRIPT_OBJECT",
    "DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE",
    "RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET",
    "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET",
}
EXPECTED_ROUTE_FAMILIES = {"PTUJ", "IG", "DGU", "RS", "QFT"}


def read_artifact() -> str:
    try:
        return ARTIFACT.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {ARTIFACT}") from exc


def extract_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        raise AssertionError("missing frontmatter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def extract_summary(text: str) -> dict:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class NextFrontierDependencyDagAfter1503Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.frontmatter = extract_frontmatter(cls.text)
        cls.summary = extract_summary(cls.text)
        cls.candidates = cls.summary["candidates"]
        cls.by_id = {candidate["id"]: candidate for candidate in cls.candidates}

    def test_artifact_exists_and_declares_exact_identity(self) -> None:
        self.assertTrue(ARTIFACT.exists())
        self.assertEqual(self.frontmatter["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.frontmatter["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.frontmatter["cycle"], "3")
        self.assertEqual(self.frontmatter["lane"], "5")
        self.assertEqual(self.frontmatter["verdict"], EXPECTED_VERDICT)

        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)

    def test_quality_candidate_claim_and_no_receipts(self) -> None:
        quality_candidates = [
            candidate for candidate in self.candidates if candidate.get("quality") is True
        ]
        self.assertGreaterEqual(self.summary["quality_candidates_claimed"], 25)
        self.assertEqual(self.summary["quality_candidates_claimed"], len(quality_candidates))
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_next_five_recommended_lanes_are_exact_and_parallel_safe(self) -> None:
        next_five = set(self.summary["next_five_recommended_lanes"])
        self.assertEqual(next_five, EXPECTED_NEXT_FIVE)
        immediate = self.summary["immediate_parallel_safe_lanes"]
        self.assertEqual({lane["id"] for lane in immediate}, EXPECTED_NEXT_FIVE)
        self.assertEqual({lane["route_family"] for lane in immediate}, EXPECTED_ROUTE_FAMILIES)

        write_scopes = [lane["write_scope"] for lane in immediate]
        self.assertEqual(len(write_scopes), len(set(write_scopes)))
        for lane in immediate:
            candidate = self.by_id[lane["id"]]
            self.assertTrue(candidate["parallel_safe"], lane["id"])
            self.assertFalse(candidate["sequential"], lane["id"])
            self.assertFalse(candidate["demoted_backup"], lane["id"])

    def test_all_five_route_families_are_present(self) -> None:
        self.assertEqual(set(self.summary["route_families"]), EXPECTED_ROUTE_FAMILIES)
        candidate_families = {candidate["route_family"] for candidate in self.candidates}
        self.assertTrue(EXPECTED_ROUTE_FAMILIES.issubset(candidate_families))
        for family in EXPECTED_ROUTE_FAMILIES:
            self.assertIn(f'"{family}"', self.text)
            self.assertIn(family, self.summary["run_learning_summary"])

    def test_upstream_source_object_no_target_import_firewall(self) -> None:
        self.assertTrue(self.summary["upstream_source_object_no_target_import_firewall"])
        self.assertEqual(
            self.summary["firewall_label"],
            "upstream-source-object/no target-import firewall",
        )
        self.assertIn("upstream-source-object/no target-import firewall", self.text)
        self.assertIn("target-import", self.text)
        self.assertIn("upstream source objects/no receipts/no proof restart", self.text)

    def test_1503_cycle_specific_facts_are_recorded(self) -> None:
        self.assertEqual(self.summary["cycle_commits"]["cycle_1"], "b1a2cc5")
        self.assertEqual(self.summary["cycle_commits"]["cycle_2"], "74090c4")
        learning = self.summary["run_learning_summary"]
        self.assertIn("metadata-only", learning["PTUJ"])
        self.assertIn("proof-object admission blocked", learning["IG"])
        self.assertIn("scoped source-window negative", learning["DGU"])
        self.assertIn("stable locator but no frames/crops/OCR", learning["RS"])
        self.assertIn("underdefined", learning["QFT"])

    def test_dependencies_reference_known_objects(self) -> None:
        known = set(self.summary["known_objects"])
        for candidate in self.candidates:
            self.assertIn(candidate["id"], known)
            for dependency in candidate.get("dependencies", []):
                self.assertIn(
                    dependency,
                    known,
                    f"{candidate['id']} references unknown dependency {dependency}",
                )

    def test_sequential_and_demoted_lanes_are_not_next_five(self) -> None:
        next_five = set(self.summary["next_five_recommended_lanes"])
        for lane_id in self.summary["sequential_lanes"]:
            self.assertNotIn(lane_id, next_five)
            self.assertTrue(self.by_id[lane_id]["sequential"], lane_id)
            self.assertFalse(self.by_id[lane_id]["parallel_safe"], lane_id)
        for lane_id in self.summary["demoted_backups"]:
            self.assertNotIn(lane_id, next_five)
            self.assertTrue(self.by_id[lane_id]["demoted_backup"], lane_id)

    def test_proof_replay_forbidden_until_all_source_objects_exist(self) -> None:
        replay_gates = self.summary["proof_replay_forbidden_until"]
        self.assertEqual(len(replay_gates), 5)
        for phrase in [
            "accepted_PTUJ_formula_source_asset_or_lawful_frame_packet",
            "accepted_IG_D7_proof_transcript_object_and_K_IG_family_identity",
            "accepted_DGU_actual_01_identity_packet",
            "accepted_RS_visual_typed_operator_packet",
            "accepted_QFT_source_defined_raw_branch_and_restriction_stable_gauge_groupoid",
        ]:
            self.assertIn(phrase, replay_gates)


if __name__ == "__main__":
    unittest.main()
