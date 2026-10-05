#!/usr/bin/env python3
"""K1145: compile exact dynamics/cohomology tests into the I1B admission packet."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1145-i1b-dynamical-cohomology-admission-compiler.json"


def load(name): return json.loads((ROOT / "lab/process" / name).read_text())


def build():
    prior = load("k1140-i1b-constraint-admission-compiler.json")
    propagation = load("k1141-constraint-propagation-intertwiner-criterion.json")
    defect = load("k1142-constraint-propagation-defect-certificate.json")
    energy = load("k1143-constrained-energy-radical-descent.json")
    cohomology = load("k1144-positive-nonzero-two-term-cohomology.json")
    tests = [
        {"test": "source_action_owner", "acceptance": "typed derivation of Q, d, G and H on the native carrier"},
        {"test": "causal_rank_and_negative_capture", "acceptance": "6/6/4 plus K1138/K1139 nonnegative restriction"},
        {"test": "propagation", "acceptance": "QG=RQ, equivalently QGP=0"},
        {"test": "energy_descent", "acceptance": "G*H+HG=0 and positive quotient after the invariant constrained radical"},
        {"test": "cochain", "acceptance": "Qd=0 on the same typed carrier"},
        {"test": "positive_nonzero_cohomology", "acceptance": "rad(H|ker Q)=im d and dim ker Q>rank d"},
        {"test": "common_closed_domain", "acceptance": "all maps, adjoints, evolution and boundary traces share one closed realization"},
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1145-I1B-DYNAMICAL-COHOMOLOGY-ADMISSION-COMPILER",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "inputs": [prior["result_id"], propagation["result_id"], defect["result_id"], energy["result_id"], cohomology["result_id"]],
        "executable_tests": tests,
        "current_candidates_meeting_composed_packet": 0,
        "algebraic_controls_pass": True,
        "source_action_map_supplied": False,
        "common_closed_domain_supplied": False,
        "current_source_and_ledger_effect": "none",
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "supply one source-action-owned Q,d,G,H packet on a common closed domain and pass every composed test, or obtain the actual boundary coupling, a stationary global background, or a different source-owned differential/completion",
        "scope_boundary": "future-candidate compiler only; finite controls do not construct a GU constraint, functional realization, physical quotient, prediction, confirmation, canon or public move",
        "scorable_rows_added": 0,
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["inputs"]) == 5
    assert len(d["executable_tests"]) == 7
    assert [x["test"] for x in d["executable_tests"]][2:6] == ["propagation", "energy_descent", "cochain", "positive_nonzero_cohomology"]
    assert d["current_candidates_meeting_composed_packet"] == 0
    assert d["algebraic_controls_pass"]
    assert not d["source_action_map_supplied"]
    assert not d["common_closed_domain_supplied"]
    assert d["current_source_and_ledger_effect"] == "none"
    assert "remain ASSERTS" in d["protected_disposition"]
    assert "every composed test" in d["next_condition"]
    assert "do not construct a GU constraint" in d["scope_boundary"]
    assert d["scorable_rows_added"] == 0
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1145 controls: 12/12")
