#!/usr/bin/env python3
"""Audit the recovery-contract construction manifest.

This is a process and overclaim boundary gate. It does not validate GU
physics or move claim status.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "lab" / "process" / "recovery-contract-construction-manifest-2026-07-16.json"
NOTE = ROOT / "explorations" / "recovery-contract-first-manifest-2026-07-16.md"

HOME_PATH_PATTERNS = (
    re.compile(r"[A-Za-z]:[\\/]+Users[\\/]+[A-Za-z0-9._-]+"),
    re.compile(r"/Users/[A-Za-z0-9._-]+"),
    re.compile(r"/home/[A-Za-z0-9._-]+"),
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def collect_path_strings(value: Any) -> list[str]:
    paths: list[str] = []
    if isinstance(value, dict):
        for child in value.values():
            paths.extend(collect_path_strings(child))
    elif isinstance(value, list):
        for child in value:
            paths.extend(collect_path_strings(child))
    elif isinstance(value, str):
        if value.endswith((".md", ".py", ".json", ".lean")) and "/" in value:
            paths.append(value)
    return paths


class RecoveryContractManifestAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest_text = read(MANIFEST)
        cls.manifest = json.loads(cls.manifest_text)
        cls.note_text = read(NOTE)

    def test_manifest_is_process_grade_only(self) -> None:
        self.assertEqual("RECOVERY-CERTIFICATION", self.manifest["selected_lane"])
        self.assertEqual("RECOVERY-CONTRACT", self.manifest["internal_item"])
        self.assertEqual("CONDITIONAL", self.manifest["operational_result"])
        self.assertFalse(self.manifest["scientific_claim_advanced"])
        self.assertFalse(self.manifest["claim_status_changed"])
        self.assertFalse(self.manifest["public_posture_changed"])
        self.assertFalse(self.manifest["portfolio_changed"])
        self.assertIn(
            "does not establish recovery",
            self.manifest["artifact_role"],
        )

    def test_construction_identity_remains_underdefined_for_combination(self) -> None:
        identity = self.manifest["construction_identity"]
        self.assertEqual(
            "PARTIAL_PROCESS_FREEZE_UNDERDEFINED_FOR_SECTOR_COMBINATION",
            identity["status"],
        )
        self.assertTrue(identity["not_a_primary_theory"])
        self.assertEqual("UNDERDEFINED", identity["operator_and_domain"]["status"])
        self.assertEqual("UNDERDEFINED", identity["variation_space_and_constraints"]["status"])
        self.assertEqual("NOT_FROZEN", identity["boundary_and_initial_data"]["status"])
        self.assertEqual("UNDERDEFINED", identity["gauge_quotient_and_observables"]["status"])

    def test_source_action_fingerprint_preserves_all_four_boundaries(self) -> None:
        ledger = self.manifest["construction_identity"]["source_action_and_coefficient_ledger"]
        self.assertEqual(
            {
                "ultralocal_limit",
                "nonlocal_completion",
                "w154_boundary",
                "gravity_theta_sector",
            },
            set(ledger),
        )
        self.assertEqual("ULTRALOCAL_TRUNCATION", ledger["ultralocal_limit"]["status"])
        self.assertEqual(
            "STRUCTURAL_COMPLETION_WITH_ONE_FREE_MAGNITUDE",
            ledger["nonlocal_completion"]["status"],
        )
        self.assertEqual("COMPLETED_POSIT", ledger["w154_boundary"]["status"])
        self.assertEqual(
            "CONDITIONAL_IMPORTED_METRIC_CLEARANCE",
            ledger["gravity_theta_sector"]["status"],
        )
        combined = " ".join(entry["boundary"] for entry in ledger.values())
        for required in ("Conditional on W154", "Z_U remains", "named assumption", "Not an exact GR recovery"):
            with self.subTest(required=required):
                self.assertIn(required, combined)

    def test_unresolved_conflicts_are_explicit_and_not_consumed(self) -> None:
        conflicts = {conflict["id"]: conflict for conflict in self.manifest["unresolved_conflicts"]}
        self.assertEqual(
            {
                "PRIMARY-ACTION-VARIANTS",
                "ULTRALOCAL-VS-STIFFNESS",
                "FINALITY-POLARITY-ADAPTER",
                "CPTT-TRIALITY-NATIVE-ACTION",
            },
            set(conflicts),
        )
        self.assertEqual("OPEN", conflicts["PRIMARY-ACTION-VARIANTS"]["status"])
        self.assertEqual("OPEN", conflicts["FINALITY-POLARITY-ADAPTER"]["status"])
        self.assertEqual("UNDERDEFINED", conflicts["CPTT-TRIALITY-NATIVE-ACTION"]["status"])
        self.assertIn("Do not cite evidence from different branches", conflicts["PRIMARY-ACTION-VARIANTS"]["must_not_do"])
        self.assertIn("Do not consume this as a frozen p2c adapter return", conflicts["FINALITY-POLARITY-ADAPTER"]["must_not_do"])
        self.assertIn("Do not treat a supplied three-generation organization", conflicts["CPTT-TRIALITY-NATIVE-ACTION"]["must_not_do"])

    def test_adapter_correction_is_not_an_independent_return(self) -> None:
        adapter = self.manifest["construction_identity"]["adapter_axioms_and_external_inputs"]
        finality = adapter["finality_polarity_adapter"]
        self.assertEqual("none", adapter["adapter_p2c_return"])
        self.assertEqual("OPEN_CONJECTURAL_BRIDGE", finality["status"])
        self.assertIn("polarity fiber over a finality profile", finality["content"])
        self.assertEqual(
            {
                "independent adapter return",
                "positive-norm selector",
                "bar(b) closure",
                "H59 closure",
                "physical issuance direction",
            },
            set(finality["must_not_consume_as"]),
        )

    def test_reduction_map_does_not_inflate_sector_grades(self) -> None:
        sectors = {
            row["sector"]: row["current_grade"]
            for row in self.manifest["construction_identity"]["reduction_map_to_tested_sectors"]
        }
        self.assertEqual(
            {
                "quantum": "CONDITIONAL_ONLY",
                "standard_model": "KINEMATICALLY_HOSTED_OR_BRANCH_LOCAL",
                "gravity": "CONDITIONAL_COMPATIBILITY_ON_IMPORTED_METRICS",
                "cosmology": "BACKGROUND_DIAGNOSTIC_ONLY",
                "blind_prediction": "GATED_NO_FIXED_NATIVE_QUANTITY",
            },
            sectors,
        )
        forbidden_grade_words = ("RESOLVED", "RECOVERED", "BLINDLY_CONFIRMED", "PREDICTED")
        rendered = json.dumps(sectors)
        for word in forbidden_grade_words:
            with self.subTest(word=word):
                self.assertNotIn(word, rendered)

    def test_statuses_remain_unchanged(self) -> None:
        statuses = set(self.manifest["statuses_unchanged"])
        required = {
            "bar(b) OPEN",
            "H59 OPEN",
            "generation count OPEN",
            "no canon movement",
            "no RESEARCH-STATUS movement",
            "no public-posture movement",
        }
        self.assertTrue(required.issubset(statuses))

    def test_all_referenced_repo_paths_exist(self) -> None:
        missing = []
        for relpath in collect_path_strings(self.manifest):
            if not (ROOT / relpath).is_file():
                missing.append(relpath)
        self.assertEqual([], sorted(set(missing)))

    def test_note_records_the_same_boundary(self) -> None:
        required_phrases = (
            "Operational result: `CONDITIONAL`",
            "No claim status, canon verdict, public posture, paper surface, or portfolio surface changed.",
            "sector combination remains `UNDERDEFINED`",
            "polarity fiber over a finality profile",
            "Next-work handoff",
        )
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.note_text)

    def test_new_public_files_do_not_leak_local_paths_or_em_dashes(self) -> None:
        for path, text in ((MANIFEST, self.manifest_text), (NOTE, self.note_text)):
            with self.subTest(path=path.relative_to(ROOT).as_posix()):
                self.assertNotIn("\u2014", text)
                for pattern in HOME_PATH_PATTERNS:
                    self.assertIsNone(pattern.search(text))


if __name__ == "__main__":
    unittest.main(verbosity=2)
