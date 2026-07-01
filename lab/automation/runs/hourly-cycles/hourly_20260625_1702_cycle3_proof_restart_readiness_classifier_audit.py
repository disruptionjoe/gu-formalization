"""Audit PROOF_RESTART_READINESS_CLASSIFIER_1702_C3_L1_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1702-cycle3-proof-restart-readiness-classifier.md"
)

EXPECTED_ARTIFACT_ID = "PROOF_RESTART_READINESS_CLASSIFIER_1702_C3_L1_V1"
EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1702-cycle3-proof-restart-readiness-classifier.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1702_cycle3_proof_restart_readiness_classifier_audit.py"
)
EXPECTED_ROUTES = {
    "PTUJ",
    "IG",
    "DGU/VZ",
    "RS",
    "QFT",
    "major GU claim",
    "global no-go",
}


def load_text() -> str:
    return ARTIFACT.read_text(encoding="utf-8")


def extract_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError("missing YAML frontmatter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def extract_json_summary(text: str) -> dict:
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not blocks:
        raise AssertionError("missing JSON summary block")
    return json.loads(blocks[-1])


class ProofRestartReadinessClassifierAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = load_text()
        cls.frontmatter = extract_frontmatter(cls.text)
        cls.summary = extract_json_summary(cls.text)
        cls.route_rows = {row["route"]: row for row in cls.summary["route_rows"]}

    def test_identity_and_scope(self) -> None:
        self.assertEqual(self.frontmatter["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.frontmatter["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.frontmatter["cycle"], "3")
        self.assertEqual(self.frontmatter["lane"], "1")
        self.assertEqual(self.frontmatter["verdict"], "NO_ROUTE_READY_FOR_PROOF_RESTART")
        self.assertEqual(self.frontmatter["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.frontmatter["companion_audit"], EXPECTED_AUDIT)

        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertTrue(self.summary["source_scope"]["cycle_artifacts_only"])
        self.assertEqual(self.summary["source_scope"]["cycle_artifact_count"], 10)
        self.assertFalse(self.summary["source_scope"]["external_evidence_used"])

    def test_all_required_route_rows_exist(self) -> None:
        self.assertEqual(set(self.route_rows), EXPECTED_ROUTES)
        self.assertEqual(set(self.summary["route_names"]), EXPECTED_ROUTES)
        self.assertEqual(len(self.summary["route_rows"]), len(EXPECTED_ROUTES))

    def test_all_counts_are_zero_and_restart_is_forbidden(self) -> None:
        decision = self.summary["global_decision"]
        self.assertEqual(decision["accepted_receipt_count_total"], 0)
        self.assertEqual(decision["accepted_for_routing_count_total"], 0)
        self.assertFalse(decision["proof_restart_allowed"])
        self.assertFalse(decision["claim_promotion"])
        self.assertFalse(decision["target_import"])
        self.assertFalse(decision["global_no_go_promoted"])
        self.assertFalse(decision["scoped_blockers_promoted"])
        self.assertFalse(decision["schema_only_work_promoted"])

        for row in self.summary["route_rows"]:
            self.assertEqual(row["accepted_receipt_count"], 0)
            self.assertEqual(row["accepted_for_routing_count"], 0)
            self.assertFalse(row["route_ready"])
            self.assertFalse(row["proof_restart_allowed"])
            self.assertFalse(row["claim_promotion"])
            self.assertFalse(row["target_import"])

    def test_exact_blockers_and_next_objects_are_present(self) -> None:
        for route, row in self.route_rows.items():
            self.assertIsInstance(row["exact_blocker"], str, route)
            self.assertGreater(len(row["exact_blocker"].strip()), 20, route)
            self.assertIsInstance(row["next_object"], str, route)
            self.assertGreater(len(row["next_object"].strip()), 10, route)

    def test_specific_blockers_match_cycle_artifacts(self) -> None:
        self.assertIn("no_branch_has_all_required_fields", self.route_rows["PTUJ"]["exact_blocker"])
        self.assertIn("ProductBFullSummandMultiplicityDimensionTableMissing", self.route_rows["IG"]["exact_blocker"])
        self.assertIn("missing_source_emitted_sector_rule", self.route_rows["DGU/VZ"]["exact_blocker"])
        self.assertIn("source_bytes_or_lawful_acquisition_route", self.route_rows["RS"]["exact_blocker"])
        self.assertIn("SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1_absent", self.route_rows["QFT"]["exact_blocker"])
        self.assertIn("zero_accepted_route_objects", self.route_rows["major GU claim"]["exact_blocker"])
        self.assertIn("scoped_admission_failures", self.route_rows["global no-go"]["exact_blocker"])

    def test_promotion_firewall_rules_are_explicit(self) -> None:
        rule = self.summary["classification_rule"]
        self.assertTrue(rule["route_ready_requires_accepted_route_object"])
        self.assertTrue(rule["route_ready_requires_proof_restart_allowed_by_source_artifacts"])
        self.assertFalse(rule["locator_metadata_counts_as_routing"])
        self.assertFalse(rule["schema_only_counts_as_routing"])
        self.assertFalse(rule["scoped_blocker_counts_as_global_no_go"])
        self.assertFalse(rule["target_physics_counts_as_source_selector"])


if __name__ == "__main__":
    unittest.main()
