#!/usr/bin/env python3
"""Audit GLOBAL_NEGATIVE_PRECONDITION_MATRIX_1702_C3_L3_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = (
    ROOT
    / "explorations"
    / "hourly-20260625-1702-cycle3-global-negative-precondition-matrix.md"
)

EXPECTED_ARTIFACT_ID = "GLOBAL_NEGATIVE_PRECONDITION_MATRIX_1702_C3_L3_V1"
EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1702-cycle3-global-negative-precondition-matrix.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1702_cycle3_global_negative_precondition_matrix_audit.py"
)

REQUIRED_PRECONDITIONS = {
    "theorem_class_assumptions",
    "route_coverage",
    "source_coverage",
    "proof_object_coverage",
    "branch_closure",
    "target_import_guard",
    "falsification_conditions",
}

REQUIRED_LANES = {"PTUJ", "IG", "DGU", "RS", "QFT"}

REQUIRED_BUNDLE_COMPONENTS = {
    "named_theorem_class_or_new_obstruction_class",
    "explicit_assumptions_and_proof_GU_route_lies_inside_class",
    "complete_source_coverage_for_PTUJ_RS_DGU_IG_and_QFT_surfaces",
    "branch_closure_rows_for_each_admissible_branch",
    "proof_object_decisions_showing_structural_failure_not_missing_data",
    "target_import_audit",
    "falsification_or_reopening_conditions",
}


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


class GlobalNegativePreconditionMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.frontmatter = extract_frontmatter(cls.text)
        cls.summary = extract_json_summary(cls.text)
        cls.preconditions = {
            row["precondition"]: row for row in cls.summary["precondition_rows"]
        }
        cls.lane_rows = {
            row["lane_family"]: row for row in cls.summary["lane_promotion_rows"]
        }

    def test_frontmatter_and_json_identity(self) -> None:
        self.assertEqual(self.frontmatter["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.frontmatter["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.frontmatter["cycle"], "3")
        self.assertEqual(self.frontmatter["lane"], "3")
        self.assertEqual(
            self.frontmatter["verdict"],
            "BLOCKED_NO_GLOBAL_OR_CLASS_RELATIVE_NO_GO_PROMOTED",
        )
        self.assertEqual(self.frontmatter["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.frontmatter["companion_audit"], EXPECTED_AUDIT)

        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)

    def test_no_global_or_class_relative_no_go_promoted(self) -> None:
        self.assertIs(self.summary["global_no_go_promoted"], False)
        self.assertIs(self.summary["class_relative_no_go_promoted"], False)
        self.assertIs(self.summary["scoped_blockers_promoted"], False)
        self.assertEqual(
            self.summary["decision"],
            "do_not_promote_1702_blockers_to_global_or_class_relative_no_go",
        )
        self.assertIs(self.summary["major_GU_claim_promoted"], False)
        self.assertIs(self.summary["claim_promotion_allowed"], False)
        self.assertIs(self.summary["proof_restart_allowed"], False)

    def test_required_precondition_rows_and_incomplete_coverage(self) -> None:
        self.assertEqual(set(self.preconditions), REQUIRED_PRECONDITIONS)
        for name in (
            "theorem_class_assumptions",
            "route_coverage",
            "source_coverage",
            "proof_object_coverage",
            "branch_closure",
        ):
            with self.subTest(precondition=name):
                row = self.preconditions[name]
                self.assertEqual(row["status"], "incomplete")
                self.assertIs(row["satisfied"], False)
                self.assertTrue(row["required_for_promotion"])

        self.assertIs(self.summary["theorem_class_coverage"], False)
        self.assertEqual(self.summary["theorem_class_coverage_status"], "incomplete")
        self.assertIs(self.summary["route_coverage_complete"], False)
        self.assertEqual(self.summary["route_coverage_status"], "incomplete")
        self.assertIs(self.summary["source_coverage_complete"], False)
        self.assertIs(self.summary["proof_object_coverage_complete"], False)
        self.assertIs(self.summary["branch_closure_complete"], False)

    def test_target_import_guard_passes_but_does_not_promote(self) -> None:
        guard = self.preconditions["target_import_guard"]
        self.assertEqual(guard["status"], "passed")
        self.assertIs(guard["satisfied"], True)
        self.assertIs(self.summary["target_import_used"], False)
        self.assertIs(self.summary["target_import_guard_passed"], True)
        self.assertIs(self.summary["global_no_go_promoted"], False)

    def test_falsification_conditions_partial_not_closing(self) -> None:
        row = self.preconditions["falsification_conditions"]
        self.assertEqual(row["status"], "partial")
        self.assertIs(row["satisfied"], False)
        self.assertGreaterEqual(len(self.summary["falsification_conditions_for_current_decision"]), 4)

    def test_all_lane_blockers_remain_scoped_and_unpromoted(self) -> None:
        self.assertEqual(set(self.lane_rows), REQUIRED_LANES)
        expected_next_objects = {
            "PTUJ": "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT",
            "IG": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
            "DGU": "SourceEmittedActualDGU01SameOperatorPacket_V1",
            "RS": "UCSDCaptureStackExecutionLedgerForRolledOperatorWindow_V1",
            "QFT": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
        }
        for lane, row in self.lane_rows.items():
            with self.subTest(lane=lane):
                self.assertIs(row["scoped_blocker"], True)
                self.assertIs(row["promote_to_no_go"], False)
                self.assertEqual(row["exact_next_object"], expected_next_objects[lane])

    def test_exact_next_global_negative_bundle_object(self) -> None:
        self.assertEqual(
            self.summary["first_missing_bundle_object"],
            "CompleteGlobalNegativeBundle_1702_V1",
        )
        bundle = self.summary["exact_next_object_for_complete_global_negative_bundle"]
        self.assertEqual(bundle["id"], "CompleteGlobalNegativeBundle_1702_V1")
        self.assertEqual(set(bundle["required_components"]), REQUIRED_BUNDLE_COMPONENTS)
        self.assertIn("NoGlobalNegativeBundle_1702", self.summary["first_obstruction"])

    def test_read_sources_include_all_ten_prior_artifacts_and_canon(self) -> None:
        sources = set(self.summary["read_sources"])
        self.assertIn("canon/no-go-class-relative-map.md", sources)
        cycle1 = {source for source in sources if "cycle1" in source and source.endswith(".md")}
        cycle2 = {source for source in sources if "cycle2" in source and source.endswith(".md")}
        self.assertEqual(len(cycle1), 5)
        self.assertEqual(len(cycle2), 5)

    def test_gu_claim_consequence_is_not_falsified(self) -> None:
        consequence = self.summary["gu_claim_consequence"]
        self.assertEqual(consequence["global_status_from_1702"], "not_falsified")
        self.assertEqual(consequence["negative_status"], "strict_scoped_blockers")
        self.assertIn("prevents_premature_no_go_promotion", consequence["decision_grade_use"])


if __name__ == "__main__":
    unittest.main()
