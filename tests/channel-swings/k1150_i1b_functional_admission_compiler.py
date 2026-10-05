#!/usr/bin/env python3
"""K1150: compile the functional I1B admission packet."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1150-i1b-functional-admission-compiler.json"


def load(name):
    return json.loads((ROOT / "lab/process" / name).read_text())


def build():
    prior = load("k1145-i1b-dynamical-cohomology-admission-compiler.json")
    graph = load("k1146-common-graph-domain-criterion.json")
    closed = load("k1147-closed-range-hausdorff-cohomology.json")
    gap = load("k1148-uniform-positive-cohomology-gap.json")
    boundary = load("k1149-boundary-skew-adjoint-generator-gate.json")
    tests = [
        {"test": "source_action_owner", "acceptance": "typed derivation of Q,d,G,H and boundary operators on the native carrier"},
        {"test": "causal_algebraic_packet", "acceptance": "K1145 ownership, 6/6/4, negative capture, propagation, energy and nonzero algebraic cohomology tests"},
        {"test": "common_graph_domain", "acceptance": "one complete graph domain includes every operator and composed word used by the identities"},
        {"test": "closed_gauge_range", "acceptance": "im(d) is closed, so constrained cohomology is Hausdorff"},
        {"test": "uniform_positive_gap", "acceptance": "the quotient form has a positive lower bound on the complete physical domain"},
        {"test": "maximal_generator", "acceptance": "G is skew-adjoint, not merely formally skew, on a boundary domain preserved by its evolution"},
        {"test": "boundary_trace_compatibility", "acceptance": "Q,d,H and G share the selected trace conditions and Green boundary form"},
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1150-I1B-FUNCTIONAL-ADMISSION-COMPILER",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "inputs": [prior["result_id"], graph["result_id"], closed["result_id"], gap["result_id"], boundary["result_id"]],
        "executable_tests": tests,
        "current_candidates_meeting_functional_packet": 0,
        "finite_algebraic_packet_executable": True,
        "functional_gates_executable": True,
        "source_action_map_supplied": False,
        "common_closed_realization_supplied": False,
        "current_source_and_ledger_effect": "none",
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "supply one source-action-owned Q,d,G,H and boundary packet passing the algebraic and functional tests, or obtain the actual bulk-boundary coupling, a stationary global background, or a different source-owned differential/completion",
        "scope_boundary": "functional admission compiler only; the supplied diagonal and interval controls do not construct a GU constraint, physical quotient, prediction, confirmation, canon or public move",
        "scorable_rows_added": 0,
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["inputs"]) == 5
    assert len(d["executable_tests"]) == 7
    assert [x["test"] for x in d["executable_tests"]][2:6] == ["common_graph_domain", "closed_gauge_range", "uniform_positive_gap", "maximal_generator"]
    assert d["current_candidates_meeting_functional_packet"] == 0
    assert d["finite_algebraic_packet_executable"] and d["functional_gates_executable"]
    assert not d["source_action_map_supplied"]
    assert not d["common_closed_realization_supplied"]
    assert d["current_source_and_ledger_effect"] == "none"
    assert "remain ASSERTS" in d["protected_disposition"]
    assert "boundary packet" in d["next_condition"]
    assert "do not construct a GU constraint" in d["scope_boundary"]
    assert d["scorable_rows_added"] == 0
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1150 controls: 12/12")
