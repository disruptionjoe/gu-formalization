#!/usr/bin/env python3
"""Audit the unified marble/wood same-source closure map.

This is a structural closure-map audit, not a proof of GU. It checks that the
artifact keeps Einstein's marble/wood distinction explicit, requires one
source action/operator/reduction package for both sides, includes the requested
closure matrix and route taxonomy, and preserves the current open/conditional
status rather than overclaiming a solution.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "cycle-gates-and-audits" / "unified-marble-wood-source-closure-map-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Same-Source Closure Criterion In Plain English And Formal Terms",
    "## 3. Pipeline From G_src/S_GU/D_GU To Metric/Einstein Shadow And Stress-Energy/Matter/QFT Shadow",
    "## 4. Closure Status Matrix",
    "## 5. Allowed Route Taxonomy",
    "## 6. Forbidden Shortcuts And Rollback Conditions",
    "## 7. First Exact Missing Proof Packet",
    "## 8. Machine-Readable Closure Map",
    "## 9. Next Meaningful Proof/Computation Step",
]

REQUIRED_MATRIX_TARGETS = {
    "GR_SHADOW",
    "LAMBDA_PATCH_DARK_ENERGY",
    "QFT_SHADOW",
    "SM_MATTER",
    "FINITE_CONTROL",
    "MEASUREMENT",
    "GENERATION_COUNT",
    "BLACK_HOLE_GATE",
    "COSMOLOGY_THETA_XI",
}

REQUIRED_ROUTES = {
    "source_both",
    "metric_shadow_first",
    "matter_shadow_first",
    "lambda_patch_dynamic_source",
    "ordinary_qft_import",
    "compact_control",
    "phenomenological_control",
}

REQUIRED_FORBIDDEN_SHORTCUTS = {
    "left_geometric_right_imported",
    "stress_energy_named_not_derived",
    "branch_mismatch",
    "compatibility_as_recovery",
    "host_as_selector",
    "weak_field_as_exact_GR",
    "hidden_matter_relabeling",
    "qft_recovery_by_slogan",
    "representation_labels_as_state",
    "ansatz_state_as_measurement",
    "compact_control_as_physical_index",
    "phenomenological_term_without_source",
    "bare_Lambda_as_marble",
    "dark_energy_fit_as_derivation",
    "free_beta_nonzero_theta",
}

REQUIRED_PACKET_OUTPUTS = {
    "source_EL_tuple",
    "marble_reduction",
    "lambda_patch_status",
    "wood_QFT_reduction",
    "matter_gauge_finite_selector_status",
    "stress_energy_bridge",
    "conservation_theorem",
    "known_physics_gate_results",
    "provenance_and_rollback_ledger",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing closure map: {DOC}") from exc


def extract_closure_map(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable Closure Map\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable closure map JSON block")
    return json.loads(match.group(1))


class UnifiedMarbleWoodClosureAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.map = extract_closure_map(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_marble_and_wood_are_both_load_bearing(self) -> None:
        lower = self.text.lower()
        self.assertGreaterEqual(lower.count("marble"), 8)
        self.assertGreaterEqual(lower.count("wood"), 8)
        self.assertIn("Einstein's marble/wood complaint", self.text)
        self.assertIn("both marble and wood", self.text)
        self.assertIn("Lambda g_mu_nu", self.text)
        self.assertIn("metric/geometric marble itself is premature", self.text)

    def test_same_source_and_source_action_operator_are_required(self) -> None:
        self.assertEqual(
            self.map["artifact"],
            "UNIFIED_MARBLE_WOOD_SOURCE_CLOSURE_MAP",
        )
        self.assertTrue(self.map["not_solved"])
        self.assertEqual(self.map["status"], "open")
        self.assertIn("same-source", self.text)
        self.assertIn("source action/operator", self.text)

        criterion = self.map["same_source_criterion"]
        source_package = set(criterion["source_package"])
        for required in ["G_src", "S_GU", "D_GU", "branch", "variation_space"]:
            self.assertIn(required, source_package)
        for required in ["R_GR", "R_Lambda", "R_QFT", "R_SM", "R_MEAS", "R_T"]:
            self.assertIn(required, criterion["required_reductions"])

        strict = set(criterion["strict_closure_requires"])
        self.assertIn("same_branch_for_marble_and_wood", strict)
        self.assertIn("source_action_operator_closed", strict)
        self.assertIn("lambda_patch_zero_imported_control_or_source_derived", strict)
        self.assertIn("stress_energy_derived_or_declared_import", strict)

    def test_pipeline_mentions_both_einstein_shadow_and_stress_energy(self) -> None:
        pipeline = {stage["stage"]: stage for stage in self.map["pipeline"]}
        for stage in [
            "source_package",
            "source_equations",
            "marble_metric_einstein_shadow",
            "lambda_patch_dark_energy",
            "wood_qft_matter_shadow",
            "stress_energy_bridge",
            "known_physics_gates",
        ]:
            self.assertIn(stage, pipeline)

        self.assertIn("G[g] + Lambda_eff g - kappa_eff T_shadow", self.text)
        self.assertIn("T_shadow", self.text)
        self.assertEqual(pipeline["lambda_patch_dark_energy"]["current_status"], "open_patch_control")
        self.assertEqual(pipeline["stress_energy_bridge"]["current_status"], "open")

    def test_closure_matrix_covers_requested_targets_and_stays_open(self) -> None:
        matrix = {row["target"]: row for row in self.map["closure_matrix"]}
        self.assertTrue(REQUIRED_MATRIX_TARGETS.issubset(matrix))

        for target in REQUIRED_MATRIX_TARGETS:
            row = matrix[target]
            self.assertEqual(row["same_source_status"], "not_closed", target)
            self.assertNotEqual(row["status"], "closed", target)
            self.assertTrue(row["first_missing_object"], target)
            self.assertTrue(row["rollback_condition"], target)

        self.assertEqual(matrix["GR_SHADOW"]["status"], "specified_open")
        self.assertEqual(matrix["LAMBDA_PATCH_DARK_ENERGY"]["status"], "open_patch_control")
        self.assertEqual(matrix["QFT_SHADOW"]["status"], "blocked")
        self.assertEqual(matrix["GENERATION_COUNT"]["status"], "open")

    def test_allowed_route_taxonomy_is_complete_and_guarded(self) -> None:
        routes = {route["id"]: route for route in self.map["route_taxonomy"]}
        self.assertEqual(set(routes), REQUIRED_ROUTES)

        self.assertEqual(routes["source_both"]["current_status"], "not_instantiated")
        self.assertEqual(routes["lambda_patch_dynamic_source"]["current_status"], "open_patch_control")
        self.assertEqual(routes["ordinary_qft_import"]["closure_strength"], "import")
        self.assertIn("ordinary_QFT_import_as_same_source", routes["metric_shadow_first"]["forbidden_claim"])
        self.assertIn("source_derived_coefficient_without_S_GU", routes["phenomenological_control"]["forbidden_claim"])

    def test_forbidden_shortcuts_and_rollbacks_are_machine_readable(self) -> None:
        shortcuts = set(self.map["forbidden_shortcuts"])
        self.assertTrue(REQUIRED_FORBIDDEN_SHORTCUTS.issubset(shortcuts))
        for shortcut in REQUIRED_FORBIDDEN_SHORTCUTS:
            self.assertIn(shortcut, self.text)

        rollbacks = self.map["rollback_conditions"]
        self.assertGreaterEqual(len(rollbacks), 10)
        rollback_blob = " ".join(rollbacks)
        for required in [
            "S_GU_or_D_GU_only_slot_for_cited_branch",
            "Schwarzschild_or_Kerr_full_EL_failure",
            "no_positive_QFT_state_space_state_or_observables",
            "matter_selector_consumes_target_data",
            "branch_changes_between_GR_and_QFT_legs",
        ]:
            self.assertIn(required, rollback_blob)

    def test_first_missing_packet_is_decision_grade(self) -> None:
        packet = self.map["first_missing_proof_packet"]
        self.assertEqual(packet["id"], "SameSourceReductionPacket_V0")
        self.assertTrue(REQUIRED_PACKET_OUTPUTS.issubset(set(packet["must_emit"])))
        for required in ["G_src", "D_GU", "S_GU", "variation_space", "provenance_rules"]:
            self.assertIn(required, packet["requires"])
        self.assertIn("conditional", packet["allowed_result"])
        self.assertIn("blocked", packet["allowed_result"])
        self.assertIn("fail", packet["allowed_result"])

    def test_verdict_and_next_step_do_not_overclaim_solution(self) -> None:
        verdict = self.map["verdict"]
        self.assertIn("OPEN", verdict)
        self.assertIn("CONDITIONAL", verdict)
        self.assertIn("PARTIAL", verdict)
        self.assertNotIn("SOLVED", verdict)
        self.assertNotIn("CLOSED", verdict)
        self.assertIn("not currently closed", self.text)
        self.assertIn("same_source_closed = false", self.text)
        self.assertIn("SameSourceReductionPacket_V0", self.map["next_step"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
