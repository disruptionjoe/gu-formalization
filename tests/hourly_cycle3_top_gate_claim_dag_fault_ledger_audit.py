#!/usr/bin/env python3
"""Audit the hourly Cycle 3 top-gate claim DAG / fault-finality ledger.

This is a governance audit, not a mathematical proof. It checks that the
artifact covers every assigned top gate, records dependency and supersession
edges, includes forbidden inputs and finality rules for every node, and makes no
positive claim upgrades.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-cycle3-top-gate-claim-dag-fault-ledger-2026-06-24.md"
)

EXPECTED_VERDICT = (
    "COARSE_DAG_EXISTS_BUT_CYCLE3_TOP_GATE_DAG_REMAINS_REQUIRED_GOVERNANCE_ARTIFACT"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. DAG node schema",
    "## 3. Top-gate node table",
    "## 4. Dependency/supersession edges",
    "## 5. Fault/finality model",
    "## 6. First exact obstruction or missing proof object",
    "## 7. Impact for next frontier ordering",
    "## 8. Machine-readable JSON summary",
]

TOP_GATES = {
    "THETA_IG_ACTION",
    "RS_GENERATION",
    "PHI_OBS_TYPEII1",
    "QFT_CHSH",
    "VZ_ACTUAL_OPERATOR",
    "META_PROOF_PROCESS",
}

NODE_FIELDS = {
    "id",
    "claim_surface",
    "owner_files",
    "accepted_inputs",
    "forbidden_inputs",
    "dependencies",
    "supersessions_demotions",
    "closure_condition",
    "current_status",
    "current_proof_grade",
    "invalid_message_fault_model",
    "finality_rule",
    "first_missing_object",
    "claim_upgrade_allowed",
}

EXPECTED_FIRST_MISSING = {
    "THETA_IG_ACTION": "K_IG_selector",
    "RS_GENERATION": "d_RS,-1",
    "PHI_OBS_TYPEII1": "FIXED_DATA_X_CERTIFICATE",
    "QFT_CHSH": "SourceProjectorPFinBWithLocalModeRecords",
    "VZ_ACTUAL_OPERATOR": "ActualDGU01OperatorCertificate",
    "META_PROOF_PROCESS": "canon_facing_top_gate_maintenance_rule_and_audit_adoption",
}

REQUIRED_DEPENDENCY_EDGES = {
    ("META_PROOF_PROCESS", "THETA_IG_ACTION", "governance_guard"),
    ("META_PROOF_PROCESS", "RS_GENERATION", "governance_guard"),
    ("META_PROOF_PROCESS", "PHI_OBS_TYPEII1", "governance_guard"),
    ("META_PROOF_PROCESS", "QFT_CHSH", "governance_guard"),
    ("META_PROOF_PROCESS", "VZ_ACTUAL_OPERATOR", "governance_guard"),
    ("PHI_OBS_TYPEII1", "QFT_CHSH", "observer_shadow_dependency"),
    ("THETA_IG_ACTION", "QFT_CHSH", "future_measurement_action_dependency"),
    ("VZ_ACTUAL_OPERATOR", "RS_GENERATION", "operator_provenance_analogy"),
}

REQUIRED_SUPERSESSION_BY_NODE = {
    "THETA_IG_ACTION",
    "RS_GENERATION",
    "PHI_OBS_TYPEII1",
    "QFT_CHSH",
    "VZ_ACTUAL_OPERATOR",
    "META_PROOF_PROCESS",
}

REQUIRED_FORBIDDEN_INPUTS = {
    "THETA_IG_ACTION": {
        "DESI_Rubin_windows_upstream",
        "xi_eff_threshold_or_target_used_upstream",
        "bare_Lambda",
        "Branch_3_template_promoted_without_selector",
    },
    "RS_GENERATION": {
        "ind_H_D_RS_equals_8",
        "ind_H_D_GU_equals_24",
        "three_generations",
        "raw_96_C_promoted_to_physical_H_rank",
        "BRST_subtraction_without_source_ghost_data",
    },
    "PHI_OBS_TYPEII1": {
        "A_F",
        "finite_CC_tuple",
        "G_SM",
        "K_SM",
        "n_equals_3",
        "C3",
        "D4_arms",
        "dim_H_F_96",
        "equal_trace_alone",
    },
    "QFT_CHSH": {
        "identity_Gram_as_GU_derivation",
        "Bell_state",
        "Pauli_controls",
        "free_vacuum",
        "target_fitted_covariance_or_CHSH_state",
        "direct_sum_as_tensor_product",
    },
    "VZ_ACTUAL_OPERATOR": {
        "typed_spine_matrix_as_actual_operator",
        "Phi_F_as_source_of_F_xi",
        "hidden_first_order_terms_in_Z_A",
        "pure_covector_only_audit",
        "verified_VZ_language_before_FC_VZ_1_and_FC_VZ_4",
    },
    "META_PROOF_PROCESS": {
        "consensus_as_mathematical_proof",
        "stale_canon_drift",
        "same_session_upgrade_laundering",
        "compatibility_as_derivation",
        "process_discipline_as_physics_evidence",
    },
}

REQUIRED_FINALITY_SUBSTRINGS = {
    "THETA_IG_ACTION": "not_final",
    "RS_GENERATION": "not_final",
    "PHI_OBS_TYPEII1": "no_positive_selector_finality",
    "QFT_CHSH": "control_finality_only",
    "VZ_ACTUAL_OPERATOR": "typed_template_finality_only",
    "META_PROOF_PROCESS": "governance_finality_only",
}

REQUIRED_FAULT_CLASSES = {
    "F_TARGET",
    "F_RAW",
    "F_HOST",
    "F_CONTROL",
    "F_TYPED_SPINE",
    "F_STALE",
    "F_CONSENSUS",
}

FORBIDDEN_POSITIVE_UPGRADE_JSON = {
    "GU_derives_dark_energy",
    "GU_derives_Lambda",
    "rank_4_promoted",
    "rank_8_promoted",
    "three_generations_derived",
    "Phi_obs_positive_selector_constructed",
    "Type_II1_selects_SM_or_three_generations",
    "H_phys_computed_from_current_sources",
    "rho_AB_GU_derived",
    "CHSH_violation_GU_derived",
    "Actual_GU_RS_operator_identified",
    "FC_VZ_1_closed",
    "FC_VZ_4_closed",
    "full_VZ_evasion_closed",
}

FORBIDDEN_TEXT_PATTERNS = [
    r'"claim_upgrade_allowed"\s*:\s*true',
    r'"mathematical_claim_upgrades_made_here"\s*:\s*true',
    r'"all_nodes_claim_upgrade_allowed"\s*:\s*true',
    r"\bthree generations are derived\b",
    r"\bGU derives dark energy\b",
    r"\bCHSH violation is GU-derived\b",
    r"\bfull VZ evasion is closed\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Cycle 3 top-gate ledger: {DOC}") from exc


def load_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing fenced JSON summary after section 8")
    return json.loads(match.group(1))


class HourlyCycle3TopGateClaimDAGFaultLedgerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = load_summary(cls.text)
        cls.nodes = {node["id"]: node for node in cls.summary["nodes"]}

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_says_coarse_dag_exists_but_cycle3_top_gate_dag_was_required(self) -> None:
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        decision = self.summary["usable_dag_decision"]
        self.assertIs(decision["repo_has_coarse_live_DAG"], True)
        self.assertIs(
            decision["repo_has_cycle3_top_gate_DAG_after_cycles_1_2_before_this_file"],
            False,
        )
        self.assertIs(decision["this_artifact_supplies_cycle3_top_gate_DAG_v0"], True)
        self.assertIs(decision["mathematical_claim_upgrades_made_here"], False)
        self.assertEqual(
            decision["governance_status"],
            "required_artifact_now_available_as_exploration_v0",
        )

    def test_all_top_gates_are_present_once(self) -> None:
        self.assertEqual(set(self.summary["top_gates"]), TOP_GATES)
        self.assertEqual(set(self.nodes), TOP_GATES)
        self.assertEqual(len(self.summary["nodes"]), len(TOP_GATES))

    def test_each_node_has_required_schema_and_no_empty_core_fields(self) -> None:
        for node_id, node in self.nodes.items():
            self.assertEqual(set(node), NODE_FIELDS, node_id)
            for list_field in [
                "owner_files",
                "accepted_inputs",
                "forbidden_inputs",
                "dependencies",
                "supersessions_demotions",
                "invalid_message_fault_model",
            ]:
                self.assertTrue(node[list_field], f"{node_id} missing {list_field}")
            for string_field in [
                "claim_surface",
                "closure_condition",
                "current_status",
                "current_proof_grade",
                "finality_rule",
                "first_missing_object",
            ]:
                self.assertTrue(node[string_field], f"{node_id} missing {string_field}")
            self.assertIs(node["claim_upgrade_allowed"], False, node_id)

    def test_first_missing_objects_match_cycle1_cycle2_refinements(self) -> None:
        self.assertEqual(self.summary["first_exact_obstructions"], EXPECTED_FIRST_MISSING)
        for node_id, expected in EXPECTED_FIRST_MISSING.items():
            self.assertEqual(self.nodes[node_id]["first_missing_object"], expected)
            self.assertIn(expected, self.text)

    def test_dependency_edges_include_all_required_top_gate_edges(self) -> None:
        edges = {
            (edge["from"], edge["to"], edge["edge_type"])
            for edge in self.summary["dependency_edges"]
        }
        missing = REQUIRED_DEPENDENCY_EDGES - edges
        self.assertFalse(missing, f"missing dependency edges: {sorted(missing)}")

        for edge_from, edge_to, _edge_type in edges:
            self.assertIn(edge_from, TOP_GATES)
            self.assertIn(edge_to, TOP_GATES)

    def test_supersession_edges_cover_each_top_gate(self) -> None:
        by_nodes = {edge["by"] for edge in self.summary["supersession_edges"]}
        self.assertEqual(by_nodes, REQUIRED_SUPERSESSION_BY_NODE)
        edge_types = {edge["edge_type"] for edge in self.summary["supersession_edges"]}
        self.assertIn("refined_obstruction", edge_types)
        self.assertIn("demotion", edge_types)
        self.assertIn("refined_governance", edge_types)

    def test_required_forbidden_inputs_are_recorded_for_each_node(self) -> None:
        for node_id, required in REQUIRED_FORBIDDEN_INPUTS.items():
            actual = set(self.nodes[node_id]["forbidden_inputs"])
            missing = required - actual
            self.assertFalse(missing, f"{node_id} missing forbidden inputs: {sorted(missing)}")

    def test_finality_rules_are_present_and_status_specific(self) -> None:
        for node_id, substring in REQUIRED_FINALITY_SUBSTRINGS.items():
            finality_rule = self.nodes[node_id]["finality_rule"]
            self.assertIn(substring, finality_rule, node_id)

        self.assertIn("global_finality_rule", self.summary)
        self.assertIn("governance_may_block_but_not_upgrade_claims", self.summary["global_finality_rule"])

    def test_fault_classes_cover_target_raw_host_control_typed_stale_and_consensus_faults(self) -> None:
        self.assertEqual(set(self.summary["fault_classes"]), REQUIRED_FAULT_CLASSES)
        for fault_id, row in self.summary["fault_classes"].items():
            self.assertTrue(row["affected_nodes"], fault_id)
            self.assertTrue(row["guard"], fault_id)
            for node_id in row["affected_nodes"]:
                self.assertIn(node_id, TOP_GATES)

    def test_no_claim_upgrades_are_allowed_or_made(self) -> None:
        no_upgrades = self.summary["no_claim_upgrades"]
        self.assertIs(no_upgrades["all_nodes_claim_upgrade_allowed"], False)
        self.assertEqual(set(no_upgrades["forbidden_positive_claims"]), FORBIDDEN_POSITIVE_UPGRADE_JSON)
        for node_id, node in self.nodes.items():
            self.assertIs(node["claim_upgrade_allowed"], False, node_id)
            self.assertNotIn("closed", node["current_status"].lower(), node_id)
            self.assertNotIn("verified", node["current_proof_grade"].lower(), node_id)

        for pattern in FORBIDDEN_TEXT_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden upgrade pattern present: {pattern}",
            )

    def test_next_frontier_ordering_covers_only_top_gates(self) -> None:
        ordering = self.summary["next_frontier_ordering"]
        self.assertEqual(set(ordering), TOP_GATES)
        self.assertEqual(ordering[0], "VZ_ACTUAL_OPERATOR")
        self.assertEqual(ordering[-1], "META_PROOF_PROCESS")


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = load_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "top_gates": summary["top_gates"],
        "dependency_edge_count": len(summary["dependency_edges"]),
        "supersession_edge_count": len(summary["supersession_edges"]),
        "claim_upgrades_made": summary["usable_dag_decision"][
            "mathematical_claim_upgrades_made_here"
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the hourly Cycle 3 top-gate claim DAG fault-finality ledger."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle3TopGateClaimDAGFaultLedgerAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
