#!/usr/bin/env python3
"""Audit the recovery-certification assessment and shared certificate schema.

This is a process and claim-boundary gate. It does not validate GU physics.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "lab" / "process" / "recovery-certification-matrix.json"
ASSESSMENT = (
    ROOT / "lab" / "process" / "recovery-certification-assessment-2026-07-15.md"
)
PORTFOLIO = ROOT / "lab" / "process" / "research-portfolio.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class RecoveryCertificationMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.matrix = json.loads(read(MATRIX))
        cls.portfolio = json.loads(read(PORTFOLIO))
        cls.items = cls.matrix["items"]
        cls.by_id = {item["id"]: item for item in cls.items}
        cls.lane = next(
            item
            for item in cls.portfolio["work_items"]
            if item["id"] == "RECOVERY-CERTIFICATION"
        )
        cls.portfolio_by_id = {
            item["id"]: item for item in cls.portfolio["work_items"]
        }

    def test_exact_contract_plus_seven_conditions(self) -> None:
        expected = {
            "RECOVERY-CONTRACT",
            "ADAPTER-RETURN-CERTIFICATION",
            "QM-PHYSICAL-SECTOR",
            "SM-CONSISTENT-SECTOR",
            "GR-DYNAMICAL-BENCHMARKS",
            "COSMO-PERTURBATIONS",
            "FIXED-NATIVE-QUANTITY",
            "BLIND-QUANTITATIVE-CONFRONTATION",
        }
        self.assertEqual(expected, set(self.by_id))
        self.assertEqual(list(range(8)), sorted(i["condition_number"] for i in self.items))
        self.assertEqual(len(self.items), len(self.by_id))

    def test_scores_and_dependencies_are_well_formed(self) -> None:
        score_fields = (
            "impact",
            "completion_difficulty",
            "completion_readiness",
            "first_test_difficulty",
            "first_test_readiness",
            "dependency_leverage",
        )
        for item in self.items:
            with self.subTest(item=item["id"]):
                self.assertTrue(all(1 <= item[field] <= 5 for field in score_fields))
                self.assertTrue(set(item["depends_on"]).issubset(self.by_id))
                self.assertTrue(item["first_decisive_test"])
                self.assertTrue(item["kill_condition"])
                self.assertTrue(item["current_honest_ceiling"])
                self.assertTrue(item["low_hanging_completed"])

    def test_shared_schema_is_complete_but_construction_is_not(self) -> None:
        setup = self.matrix["shared_setup"]
        required_definitions = {
            "native",
            "forced",
            "external_datum",
            "calibration_datum",
            "target_datum",
            "holdout",
            "retuning",
            "distinctive",
            "independent_adapter",
        }
        required_manifest_fields = {
            "git revision and content manifest",
            "source action and coefficient ledger",
            "operator and domain",
            "variation space and constraints",
            "adapter axioms and external inputs",
            "reduction map to each tested sector",
        }
        grades = [entry["grade"] for entry in setup["recovery_ladder"]]

        self.assertEqual("COMPLETE_AT_SCHEMA_GRADE", setup["status"])
        self.assertFalse(setup["scientific_claim_advanced"])
        self.assertEqual(required_definitions, set(setup["definitions"]))
        self.assertEqual("UNDERDEFINED", setup["construction_identity_manifest"]["status"])
        self.assertTrue(
            required_manifest_fields.issubset(
                setup["construction_identity_manifest"]["required_fields"]
            )
        )
        self.assertEqual(
            [
                "NOT_LOCATED",
                "LOCATED",
                "KINEMATICALLY_EMBEDDED",
                "DYNAMICALLY_CLOSED",
                "QUANTUM_CONSISTENT",
                "PHENOMENOLOGICALLY_REPRODUCED",
                "BLINDLY_CONFIRMED",
            ],
            grades,
        )

    def test_negative_controls_cover_every_promotion_risk(self) -> None:
        controls = {
            control["id"] for control in self.matrix["shared_setup"]["negative_controls"]
        }
        required = {
            "SM-SUBGROUP-CONTAINMENT",
            "QM-KREIN-ARENA",
            "GR-IMPORTED-SOLUTION",
            "GR-ASSUMED-EINSTEIN-PPN",
            "COSMO-BACKGROUND-ONLY",
            "PRED-FLAVOR-RESIDUAL",
            "PRED-NORM-NO-ABSOLUTE-SCALE",
            "DE-AMP-DIAGNOSTIC",
            "F1-TRIPWIRE",
            "GU-002-PACKET-CONTROL",
        }
        self.assertEqual(required, controls)

    def test_claim_chain_acceptance_tests_are_predeclared(self) -> None:
        tests = self.matrix["shared_setup"]["claim_chain_acceptance_tests"]
        required_fragments = (
            "missing provenance",
            "circular premise",
            "sector-specific retuning",
            "free tangent",
            "target calibration",
            "post-data freeze",
            "equal-freedom standard mimic",
            "claim-chain hashes",
        )
        self.assertEqual(8, len(tests))
        for fragment in required_fragments:
            with self.subTest(fragment=fragment):
                self.assertTrue(any(fragment in test for test in tests))

    def test_all_evidence_paths_exist(self) -> None:
        paths = []
        paths.extend(
            control["evidence"]
            for control in self.matrix["shared_setup"]["negative_controls"]
        )
        for conflict in self.matrix["shared_setup"]["construction_identity_manifest"][
            "known_variant_conflicts"
        ]:
            paths.extend(conflict["evidence"])
        for item in self.items:
            paths.extend(item["evidence"])

        missing = [path for path in paths if not (ROOT / path).is_file()]
        self.assertEqual([], missing)

    def test_portfolio_consumes_the_assessment_without_opening_gates(self) -> None:
        internal = {item["id"]: item for item in self.lane["internal_work_items"]}
        self.assertEqual("lab/process/recovery-certification-matrix.json", self.lane["assessment_source"])
        lane_one_matrix_items = set(self.by_id) - {
            "FIXED-NATIVE-QUANTITY",
            "BLIND-QUANTITATIVE-CONFRONTATION",
        }
        self.assertTrue(lane_one_matrix_items.issubset(internal))
        self.assertEqual({"NO-GO-SCOPE-CHALLENGE"}, set(internal) - lane_one_matrix_items)
        self.assertEqual("READY", internal["NO-GO-SCOPE-CHALLENGE"]["state"])
        self.assertIn("HISTORY_AUDIT_READY", internal["NO-GO-SCOPE-CHALLENGE"]["next_swing"])
        self.assertIn("three-swing sequence", internal["NO-GO-SCOPE-CHALLENGE"]["next_swing"])
        self.assertEqual("GATED_P2C", internal["ADAPTER-RETURN-CERTIFICATION"]["state"])
        self.assertEqual("2", self.portfolio_by_id["FIXED-NATIVE-QUANTITY"]["lane_id"])
        self.assertEqual("GATED_NEW_STRUCTURE", self.portfolio_by_id["FIXED-NATIVE-QUANTITY"]["state"])
        self.assertEqual("2", self.portfolio_by_id["BLIND-QUANTITATIVE-CONFRONTATION"]["lane_id"])
        self.assertEqual("GATED_FIXED_QUANTITY", self.portfolio_by_id["BLIND-QUANTITATIVE-CONFRONTATION"]["state"])
        self.assertEqual(
            "BRANCH_NO_GO_DEFENSE_DUE",
            internal["GR-DYNAMICAL-BENCHMARKS"]["state"],
        )
        self.assertEqual(
            "BRANCH_NO_GO_DEFENSE_DUE",
            internal["COSMO-PERTURBATIONS"]["state"],
        )
        self.assertEqual(
            "BRANCH_NO_GO_DEFENSE_DUE",
            internal["SM-CONSISTENT-SECTOR"]["state"],
        )
        self.assertIn("NO-GO-SCOPE-CHALLENGE", internal["GR-DYNAMICAL-BENCHMARKS"]["next_swing"])
        self.assertIn("scalar-truncation no-go", internal["COSMO-PERTURBATIONS"]["next_swing"])
        self.assertIn("SM selector no-go", internal["SM-CONSISTENT-SECTOR"]["next_swing"])

    def test_assessment_files_do_not_leak_local_paths_or_em_dashes(self) -> None:
        windows_home = "C:" + "\\Users\\joe"
        slash_home = "C:" + "/Users/" + "joe"
        for path in (MATRIX, ASSESSMENT):
            text = read(path)
            with self.subTest(path=path.name):
                self.assertNotIn("\u2014", text)
                self.assertNotIn(windows_home, text)
                self.assertNotIn(slash_home, text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
