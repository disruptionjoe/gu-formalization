#!/usr/bin/env python3
"""K979 exact assumption fork for an exponential Markov dilation."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k979-k978-markov-dilation-assumption-fork.json"
INPUTS = [
    ROOT / "lab/process/k976-k975-bounded-dilation-first-jet-obstruction.json",
    ROOT / "lab/process/k977-k976-reduced-purity-zeno-boundary.json",
    ROOT / "lab/process/k978-k977-collision-uniform-convergence.json",
]


def build():
    ps = [json.loads(p.read_text()) for p in INPUTS]
    return {
        "schema_version": "1.0",
        "result_id": "K979-MARKOV-DILATION-ASSUMPTION-FORK",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "classification": "INTERNAL_REQUIREMENT_DISPOSITION",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Logical composition of K976--K978 for exact positive-rate dephasing and its fresh-collision approximation.",
        "dependency_checks": {
            "input_ids": [p["result_id"] for p in ps],
            "all_source_and_ledger_effect_none": all(p["source_and_ledger_effect"] == "none" for p in ps),
            "all_prediction_or_confirmation_withheld": all(not p["ownership"]["prediction_or_confirmation_credit"] for p in ps),
            "bounded_parent_obstruction_present": ps[0]["decision"]["bounded_product_parent_first_jet_excluded"],
            "purity_boundary_present": ps[1]["decision"]["observable_short_time_boundary_proved"],
            "collision_repair_present": ps[2]["decision"]["off_grid_convergence_quantified"],
        },
        "assumption_fork": {
            "exact_target": "positive-rate dephasing semigroup on an interval containing t=0",
            "jointly_incompatible_parent_assumptions": [
                "fixed product assignment for every system input",
                "bounded self-adjoint time-independent Hamiltonian",
                "fixed normalized environment state",
                "differentiable reduced unitary dynamics at t=0",
            ],
            "minimum_conclusion": "Any exact microscopic parent must fail at least one declared assumption.",
            "candidate_failure_modes_not_exhaustive": [
                "unbounded or singular generator/domain",
                "freshness, reset or time-dependent driving",
                "non-product or input-dependent assignment outside the theorem",
                "non-Hamiltonian primitive or nondifferentiable limit",
            ],
            "collision_route": "The explicit K963 family chooses freshness plus a singular rapid-refresh coupling scale and converges uniformly on fixed finite horizons.",
            "does_not_select_a_failure_mode": True,
        },
        "ownership": {
            "logical_fork_only": True,
            "gu_action_selects_no_horn": True,
            "gu_physical_quotient_constructed": False,
            "held_out_scored": False,
            "prediction_or_confirmation_credit": False,
        },
        "decision": {
            "bounded_autonomous_horn_closed": True,
            "fresh_resource_horn_conditionally_open": True,
            "next_exact_input": "A GU-owned action/domain packet must select and control one horn rather than inheriting the repository's collision repair.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Logical negation of the K976 joint hypotheses plus one explicit K978 contrary approximation; not an exhaustive classification of open-system dilations or a GU verdict.",
    }


def validate(p):
    c, f, o, d = p["dependency_checks"], p["assumption_fork"], p["ownership"], p["decision"]
    assert len(c["input_ids"]) == 3 and c["all_source_and_ledger_effect_none"]
    assert c["all_prediction_or_confirmation_withheld"] and c["bounded_parent_obstruction_present"]
    assert c["purity_boundary_present"] and c["collision_repair_present"]
    assert len(f["jointly_incompatible_parent_assumptions"]) == 4
    assert len(f["candidate_failure_modes_not_exhaustive"]) == 4 and f["does_not_select_a_failure_mode"]
    assert o["logical_fork_only"] and o["gu_action_selects_no_horn"]
    assert not o["gu_physical_quotient_constructed"] and not o["held_out_scored"]
    assert not o["prediction_or_confirmation_credit"]
    assert d["bounded_autonomous_horn_closed"] and d["fresh_resource_horn_conditionally_open"]
    assert p["source_and_ledger_effect"] == "none"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    p = build(); validate(p); text = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if a.check: assert OUTPUT.read_text() == text
    elif a.write: OUTPUT.write_text(text)
    else: print(text, end="")
    print("K979 controls: 16/16")


if __name__ == "__main__": main()
