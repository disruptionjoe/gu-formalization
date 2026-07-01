#!/usr/bin/env python3
"""Audit the Cycle 3 Freed-Hopkins X_obs / IC4 verification gate.

This audit checks the dependency-gate contract, not the underlying mathematics.
It enforces that the artifact keeps the FH Option B survivor parked at
lane-narrowed CONDITIONALLY_RESOLVED until IC4 C/D/F, F3/F5, RC4, and the
same-session guard are discharged, and that it does not promote to a closed
GENUINE_OBSTRUCTION.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-cycle3-freed-hopkins-xobs-ic4-verification-gate-2026-06-24.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Dependency chain and same-session circularity guard",
    "## 3. What current FH/IC4 sources establish",
    "## 4. Strongest positive verification attempt",
    "## 5. First exact obstruction or missing proof object",
    "## 6. Reopen/promote/park decision",
    "## 7. Rollback/falsification conditions",
    "## 8. Machine-readable JSON summary",
]

REQUIRED_DEPENDENCIES = {
    "IC4_C",
    "IC4_D",
    "IC4_F",
    "IC4_F3",
    "IC4_F5",
    "RC4",
    "FH_root_no_go_theorem",
    "same_session_guard",
}

REQUIRED_PROMOTION_OBJECTS = {
    "IC4_C_component_Einstein_reduction_certificate",
    "IC4_D_F3_no_trace_free_GU_source_certificate",
    "IC4_F5_K3_topology_forcing_certificate",
    "IC4_F_moduli_level_Ricci_flat_K3_Yau_certificate",
    "RC4_KSp0_KO4_arithmetic_orbifold_or_equivariant_certificate",
    "FH_root_no_go_theorem_for_current_GU_observer_data",
    "later_session_independent_verification_record",
}

REQUIRED_REOPEN_CONDITIONS = {
    "IC4_C_fails",
    "IC4_D_or_F3_fails_with_surviving_trace_free_source",
    "IC4_F5_fails_K3_topology_not_forced",
    "IC4_F_changes_solution_moduli_from_M_RF_K3",
    "RC4_fails_or_requires_nonrelabeling_equivariant_KSp_class",
    "proper_GU_solution_sublocus_has_nonextendable_KO4_class",
    "independent_non_gauge_non_metric_Sp64_or_H_observer_structure_constructed",
    "same_session_conditional_promotion_to_GENUINE_OBSTRUCTION_attempted",
}

FORBIDDEN_PROMOTION_PATTERNS = [
    r"(?<!no )(?<!not )(?<!NOT )\bVerdict:\s*\*\*GENUINE_OBSTRUCTION\*\*",
    r'"genuine_obstruction_promotion"\s*:\s*true',
    r'"closed_no_go_promoted"\s*:\s*true',
    r"\bOption B survivor is verified as a closed no-go\b",
    r"\bFreed-Hopkins Option B .* closed GENUINE_OBSTRUCTION\b",
]


def read_artifact() -> str:
    try:
        return ARTIFACT.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing FH X_obs / IC4 gate artifact: {ARTIFACT}") from exc


def extract_json_summary(text: str) -> dict[str, Any]:
    marker = "## 8. Machine-readable JSON summary"
    if marker not in text:
        raise AssertionError("missing machine-readable JSON summary heading")
    tail = text.split(marker, 1)[1]
    match = re.search(r"```json\s*(\{.*?\})\s*```", tail, flags=re.DOTALL)
    if not match:
        raise AssertionError("missing fenced JSON summary block")
    return json.loads(match.group(1))


class FreedHopkinsXobsIc4VerificationGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.summary = extract_json_summary(cls.text)

    def test_required_deliverable_sections_exist(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_parks_conditionally_resolved_without_closed_promotion(self) -> None:
        self.assertEqual(self.summary["verdict"], "PARK_CONDITIONALLY_RESOLVED_NOT_CLOSED")
        self.assertFalse(self.summary["closed_no_go_promoted"])
        self.assertFalse(self.summary["genuine_obstruction_promotion"])
        self.assertTrue(self.summary["no_GENUINE_OBSTRUCTION_promotion"])
        self.assertIn("PARK_CONDITIONALLY_RESOLVED_NOT_CLOSED", self.text)
        self.assertIn("no GENUINE_OBSTRUCTION promotion", self.text)

    def test_required_dependency_gates_are_machine_readable(self) -> None:
        deps = set(self.summary["required_dependencies"])
        self.assertTrue(REQUIRED_DEPENDENCIES.issubset(deps))

        chain_ids = {row["id"] for row in self.summary["dependency_chain"]}
        for gate in ["IC4_C", "IC4_D_F3", "IC4_F5", "IC4_F", "RC4", "FH_root"]:
            self.assertIn(gate, chain_ids)

        for term in ["IC4-C", "IC4-D/F3", "IC4-F5", "IC4-F", "RC4"]:
            self.assertIn(term, self.text)

    def test_xobs_ksp_and_relabeling_are_conditional(self) -> None:
        status = self.summary["status_by_claim"]
        self.assertEqual(
            status["X_obs_sol_equals_M_RF_K3"],
            "conditional_on_IC4_C_D_F_and_F3_F5",
        )
        self.assertEqual(status["KSp0_over_arithmetic_orbifold_base"], "conditional_on_RC4")
        self.assertEqual(
            status["gravitational_background_relabeling"],
            "conditional_on_XOBS_identification_and_RC4",
        )
        self.assertEqual(status["Option_B_closed_no_go"], "not_currently_verified")

    def test_same_session_guard_is_explicit_and_blocks_promotion(self) -> None:
        self.assertTrue(self.summary["same_session_guard_required"])
        self.assertIn("same-session", self.summary["same_session_guard"])
        self.assertIn("Same-session guard", self.text)
        self.assertIn("later-session or independently checked proof objects", self.text)

    def test_no_forbidden_closed_genuine_obstruction_promotion_language(self) -> None:
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE | re.DOTALL),
                pattern,
            )

    def test_promotion_proof_objects_are_exact(self) -> None:
        proof_objects = set(self.summary["required_promotion_proof_objects"])
        self.assertTrue(REQUIRED_PROMOTION_OBJECTS.issubset(proof_objects))
        self.assertEqual(
            self.summary["first_missing_proof_object"],
            "IC4_C_D_F3_VERIFICATION_CERTIFICATE",
        )
        for phrase in [
            "[G^Y_T]^TF",
            "C_Gauss = 1",
            "T^{GU,TF}_{mu nu} = 0",
            "index split",
            "Rokhlin",
            "equivariant/orbifold",
        ]:
            self.assertIn(phrase, self.text)

    def test_reopen_conditions_are_clear_and_cover_required_failures(self) -> None:
        reopen = set(self.summary["reopen_conditions"])
        self.assertTrue(REQUIRED_REOPEN_CONDITIONS.issubset(reopen))
        self.assertGreaterEqual(len(reopen), 8)
        self.assertIn("Reopen if any one of these happens", self.text)
        self.assertIn("surviving trace-free GU source", self.text)
        self.assertIn("K3 topology", self.text)
        self.assertIn("non-extendable", self.text)

    def test_rollback_conditions_prevent_common_overclaims(self) -> None:
        rollback = set(self.summary["rollback_conditions"])
        for condition in [
            "promotion_without_IC4_C_D_F_F3_F5_RC4",
            "promotion_without_FH_root_theorem",
            "promotion_from_same_session_conditional_chain",
            "claiming_noncontractibility_alone_closes_Option_B",
            "claiming_gravitational_relabeling_without_X_obs_sol_equals_M_RF_K3",
        ]:
            self.assertIn(condition, rollback)
        self.assertIn("not sufficient for promotion", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
