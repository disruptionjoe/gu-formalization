#!/usr/bin/env python3
"""Audit the recovery-contract action fingerprint.

This is a process and overclaim boundary gate. It checks that the
W203/W229/W230/W236 action fingerprint stays branch-local and conditional.
It does not validate GU physics or move claim status.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FINGERPRINT = ROOT / "lab" / "process" / "recovery-contract-action-fingerprint-2026-07-16.json"
NOTE = ROOT / "explorations" / "recovery-contract-action-fingerprint-2026-07-16.md"

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


class RecoveryContractActionFingerprintAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fingerprint_text = read(FINGERPRINT)
        cls.fingerprint = json.loads(cls.fingerprint_text)
        cls.note_text = read(NOTE)

    def test_fingerprint_is_process_grade_only(self) -> None:
        self.assertEqual("RECOVERY-CERTIFICATION", self.fingerprint["selected_lane"])
        self.assertEqual("RECOVERY-CONTRACT", self.fingerprint["internal_item"])
        self.assertEqual("CONDITIONAL", self.fingerprint["operational_result"])
        self.assertFalse(self.fingerprint["scientific_claim_advanced"])
        self.assertFalse(self.fingerprint["claim_status_changed"])
        self.assertFalse(self.fingerprint["public_posture_changed"])
        self.assertFalse(self.fingerprint["portfolio_changed"])
        self.assertIn("does not establish recovery", self.fingerprint["artifact_role"])

    def test_branch_local_object_is_conditional_not_primary_theory(self) -> None:
        obj = self.fingerprint["branch_local_testing_object"]
        self.assertEqual("CONDITIONAL_BRANCH_LOCAL_TEST_OBJECT", obj["status"])
        self.assertTrue(obj["not_a_primary_theory"])
        self.assertEqual("UNDERDEFINED_OUTSIDE_THIS_BRANCH", obj["downstream_sector_combination_status"])
        forbidden = set(obj["must_not_enable"])
        self.assertIn("exact GR recovery", forbidden)
        self.assertIn("blind prediction", forbidden)
        self.assertIn("claim-status movement", forbidden)
        self.assertIn("canon verdict movement", forbidden)

    def test_exact_source_family_is_w203_w229_w230_w236(self) -> None:
        sources = {source["id"]: source for source in self.fingerprint["source_documents"]}
        self.assertEqual({"W203", "W229", "W230", "W236"}, set(sources))
        self.assertIn("Ultralocal", sources["W203"]["role"])
        self.assertIn("Nonlocal induced-YM", sources["W229"]["role"])
        self.assertIn("required posit", sources["W230"]["role"])
        self.assertIn("imported Schwarzschild", sources["W236"]["role"])

    def test_action_terms_and_field_equations_name_the_fingerprint(self) -> None:
        action = self.fingerprint["action_family"]
        terms = {term["term_id"]: term for term in action["action_terms"]}
        self.assertEqual(
            {
                "record_action",
                "ultralocal_bridge",
                "first_order_Z_U_parent",
                "nonlocal_gradient_sector",
            },
            set(terms),
        )
        equations = {row["equation_id"]: row for row in action["field_equations"]}
        self.assertEqual(
            {
                "P_IG_elimination",
                "theta_screened_source_law",
                "connection_induced_YM_law",
            },
            set(equations),
        )
        self.assertIn("(-Z_U D_A* D_A + c_theta eta) theta = J[Psi]", equations["theta_screened_source_law"]["equation"])
        self.assertIn("record-current construction side", equations["theta_screened_source_law"]["conditions"])
        self.assertIn("W154 / c_kin = 0 posit active", equations["theta_screened_source_law"]["conditions"])

    def test_source_law_preserves_w154_posit_boundary(self) -> None:
        source_law = self.fingerprint["source_law"]
        self.assertEqual("W154_POSIT_REQUIRED", source_law["status"])
        self.assertIn("J^a[Psi]", source_law["record_current"])
        self.assertIn("Psi = 0 implies J[Psi] = 0", source_law["vacuum_rule"])
        self.assertEqual(
            {"Noether II / equivariance", "gauge structure", "shiab or other equivariant linear maps"},
            set(source_law["not_forced_by"]),
        )
        self.assertIn("c_kin > 0 branch is a different construction", source_law["w230_boundary"])

    def test_variation_space_excludes_bare_or_retuned_branches(self) -> None:
        variation = self.fingerprint["variation_space"]
        self.assertEqual("FINGERPRINTED_FOR_BRANCH_LOCAL_TESTING", variation["status"])
        constraints = " ".join(variation["constraints"])
        self.assertIn("Do not vary a bare Psi-independent theta", constraints)
        self.assertIn("Do not add a fundamental c_kin > 0 stiffness", constraints)
        self.assertIn("Do not change kappa or Z_U after inspecting a sector target", constraints)
        self.assertIn("native normalization of kappa and Z_U", variation["not_frozen"])

    def test_quantity_ledger_separates_forced_free_and_imported(self) -> None:
        ledger = self.fingerprint["quantity_ledger"]
        forced = {row["quantity"]: row["status"] for row in ledger["forced_or_fixed_in_shape"]}
        free = {row["quantity"]: row["status"] for row in ledger["free_or_unbuilt"]}
        self.assertEqual("geometry_forced_up_to_scale", forced["eta kernel / fiber pairing"])
        self.assertEqual("exact_zero", forced["Psi=0 source"])
        self.assertEqual("normalization_unbuilt", free["kappa magnitude"])
        self.assertEqual("normalization_unbuilt", free["Z_U magnitude"])
        self.assertEqual("named_posit", free["c_kin = 0 induced-vs-fundamental status"])
        self.assertIn("imported exact Schwarzschild metric", ledger["imported_or_comparator_only"])
        self.assertIn("imported Schwarzschild or Kerr compatibility alone", ledger["forbidden_as_recovery_evidence"])

    def test_allowed_reductions_are_limited_and_safe(self) -> None:
        reductions = {row["id"]: row for row in self.fingerprint["allowed_reductions"]}
        self.assertEqual(
            {
                "W229_TO_W203_ULTRALOCAL_LIMIT",
                "W236_IMPORTED_VACUUM_THETA_CLEARANCE",
                "STANDARD_MACHINERY_AS_COMPARATOR",
            },
            set(reductions),
        )
        self.assertIn("Z_U -> 0", reductions["W229_TO_W203_ULTRALOCAL_LIMIT"]["condition"])
        self.assertIn("Psi = 0", reductions["W236_IMPORTED_VACUUM_THETA_CLEARANCE"]["condition"])
        self.assertIn("Declare exact GR recovery", reductions["W236_IMPORTED_VACUUM_THETA_CLEARANCE"]["invalid_use"])
        self.assertIn("standard EFT mimicry", reductions["STANDARD_MACHINERY_AS_COMPARATOR"]["invalid_use"])

    def test_conflict_boundary_stays_open_where_required(self) -> None:
        conflicts = {row["id"]: row for row in self.fingerprint["conflict_boundary"]}
        self.assertEqual(
            {
                "PRIMARY-ACTION-VARIANTS",
                "W154_SOURCE_IDENTIFICATION",
                "ULTRALOCAL_VS_NONLOCAL_STIFFNESS",
                "IMPORTED_GRAVITY_EVIDENCE",
                "SECTOR_COMBINATION",
            },
            set(conflicts),
        )
        self.assertEqual("OPEN", conflicts["PRIMARY-ACTION-VARIANTS"]["status"])
        self.assertEqual("NAMED_POSIT", conflicts["W154_SOURCE_IDENTIFICATION"]["status"])
        self.assertEqual("ORDERED_WITH_RESIDUES", conflicts["ULTRALOCAL_VS_NONLOCAL_STIFFNESS"]["status"])
        self.assertEqual("UNDERDEFINED_PENDING_TESTS", conflicts["SECTOR_COMBINATION"]["status"])
        self.assertIn("Do not call the record-current source law unconditional", conflicts["W154_SOURCE_IDENTIFICATION"]["must_not_do"])

    def test_downstream_contract_names_first_residual_and_kill_condition(self) -> None:
        downstream = self.fingerprint["downstream_use_contract"]
        self.assertIn("O(M^2) Schwarzschild/Kerr", downstream["valid_next_test_object"])
        self.assertIn("W154 / c_kin = 0", downstream["first_residual"])
        self.assertIn("changing the action, source law, variation space, or free-quantity ledger", downstream["first_kill_condition"])
        self.assertIn("state the branch-local action id", downstream["required_before_sector_combination"])

    def test_statuses_remain_unchanged(self) -> None:
        statuses = set(self.fingerprint["statuses_unchanged"])
        required = {
            "bar(b) OPEN",
            "H59 OPEN",
            "generation count OPEN",
            "no canon movement",
            "no RESEARCH-STATUS movement",
            "no public-posture movement",
            "no portfolio movement",
        }
        self.assertTrue(required.issubset(statuses))

    def test_all_referenced_repo_paths_exist(self) -> None:
        missing = []
        for relpath in collect_path_strings(self.fingerprint):
            if not (ROOT / relpath).is_file():
                missing.append(relpath)
        self.assertEqual([], sorted(set(missing)))

    def test_note_records_the_same_boundary(self) -> None:
        required_phrases = (
            "Operational result: `CONDITIONAL`",
            "branch-local testing object",
            "sector combination remains `UNDERDEFINED`",
            "W154 / `c_kin = 0` posit",
            "No claim status, canon verdict, public posture, paper surface, or portfolio surface changed.",
            "Next recovery work",
        )
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.note_text)

    def test_new_public_files_do_not_leak_local_paths_or_em_dashes(self) -> None:
        for path, text in ((FINGERPRINT, self.fingerprint_text), (NOTE, self.note_text)):
            with self.subTest(path=path.relative_to(ROOT).as_posix()):
                self.assertNotIn("\u2014", text)
                for pattern in HOME_PATH_PATTERNS:
                    self.assertIsNone(pattern.search(text))


if __name__ == "__main__":
    unittest.main(verbosity=2)
