#!/usr/bin/env python3
"""K1140: compile the sharpened I1B constraint admission boundary."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1140-i1b-constraint-admission-compiler.json"


def load(name): return json.loads((ROOT / "lab/process" / name).read_text())


def build():
    census = load("k1134-source-i1b-current-constraint-owner-census.json")
    shell = load("k1137-nonzero-kappa-exceptional-shell-constraint-boundary.json")
    inertia = load("k1138-constraint-projector-inertia-certificate.json")
    capture = load("k1139-sharp-negative-capture-graph-criterion.json")
    gates = [
        {"gate": "action_owned_non_gauge_local_map", "acceptance": "typed source-action derivation; shell spectral support or fitted projector is insufficient"},
        {"gate": "causal_rank_floor", "acceptance": "typewise rank at least 6/6/4"},
        {"gate": "negative_capture", "acceptance": "full capture of the negative block, not rank alone"},
        {"gate": "graph_contraction_or_exact_inertia", "acceptance": "H_plus-B*D_minus B nonnegative or an equivalent exact ker(Q) inertia certificate"},
        {"gate": "propagation", "acceptance": "intertwining or closed evolution on the same native carrier"},
        {"gate": "common_closed_domain", "acceptance": "one domain for Hessian, constraint, adjoint and boundary traces"},
        {"gate": "nonzero_positive_cohomology", "acceptance": "positive pairing on at least one nonzero physical class"},
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1140-I1B-CONSTRAINT-ADMISSION-COMPILER",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "inputs": [census["result_id"], shell["result_id"], inertia["result_id"], capture["result_id"]],
        "admission_gates": gates,
        "current_candidates_meeting_all_gates": 0,
        "rank_floor_retyped": "necessary_not_sufficient",
        "exceptional_shell_retyped": "spectral_compatibility_not_homogeneous_local_constraint",
        "current_source_and_ledger_effect": "none",
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "construct one source-action-owned non-gauge map and pass all seven gates, or supply the actual boundary coupling, a stationary global background, or a different source-owned differential/completion",
        "scope_boundary": "admission compiler for future candidates; no candidate is constructed and no GU falsification, physical quotient, prediction, confirmation, canon or public move follows",
        "scorable_rows_added": 0,
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["inputs"]) == 4
    assert len(d["admission_gates"]) == 7
    assert [g["gate"] for g in d["admission_gates"]][1:4] == ["causal_rank_floor", "negative_capture", "graph_contraction_or_exact_inertia"]
    assert d["current_candidates_meeting_all_gates"] == 0
    assert d["rank_floor_retyped"] == "necessary_not_sufficient"
    assert d["exceptional_shell_retyped"] == "spectral_compatibility_not_homogeneous_local_constraint"
    assert d["current_source_and_ledger_effect"] == "none"
    assert "remain ASSERTS" in d["protected_disposition"]
    assert "all seven gates" in d["next_condition"]
    assert "no candidate is constructed" in d["scope_boundary"]
    assert d["scorable_rows_added"] == 0
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1140 controls: 12/12")
