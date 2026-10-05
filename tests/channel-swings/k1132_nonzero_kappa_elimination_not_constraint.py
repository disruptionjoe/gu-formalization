#!/usr/bin/env python3
"""K1132: nonzero-kappa I1B distortion elimination is not a constraint owner."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1132-nonzero-kappa-elimination-not-constraint.json"


def load(name):
    return json.loads((ROOT / "lab/process" / name).read_text())


def build():
    k1131 = load("k1131-mixed-block-solvability-constraint-map.json")
    k129 = load("selected-k129-native-i1b-t0-ac-kernel-and-domain-classification.json")
    k133 = load("selected-k133-native-i1b-t0-flat-complex-kappa-pencil.json")
    k140 = load("selected-k140-native-i1b-t0-graph-parameter-cone-obstruction.json")
    return {
        "schema_version": "1.0",
        "result_id": "K1132-NONZERO-KAPPA-ELIMINATION-NOT-CONSTRAINT",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "inputs": [k1131["result_id"], k129["artifact_id"], k133["artifact_id"], k140["artifact_id"]],
        "rows": [
            {"regime": "zero_frequency_nonzero_kappa", "C_status": "invertible", "constraint_rank": 0, "disposition": "elimination_only"},
            {"regime": "generic_fixed_covector_nonzero_kappa", "C_status": "invertible_away_from_finite_exceptional_set", "constraint_rank": 0, "disposition": "elimination_only"},
            {"regime": "exceptional_shell", "C_status": "singular", "constraint_rank": None, "disposition": "shell_dependent_and_not_propagated"},
            {"regime": "fixed_frequency_graph", "C_status": "inverse_dependent", "constraint_rank": 0, "disposition": "not_homogeneous_constraint_projector"},
        ],
        "negative_floor": [6, 6, 4],
        "conclusion": "nonzero kappa supplies no generic non-gauge field constraint; Schur or graph elimination does not pay the 6/6/4 positivity budget",
        "scope_boundary": "selected I1B T=0 finite-symbol/frequency horn only; exceptional shells, domains and other source completions remain open",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["inputs"]) == 4
    assert len(d["rows"]) == 4
    assert [r["constraint_rank"] for r in d["rows"][:2]] == [0, 0]
    assert d["rows"][2]["constraint_rank"] is None
    assert d["rows"][3]["disposition"] == "not_homogeneous_constraint_projector"
    assert d["negative_floor"] == [6, 6, 4]
    assert "no generic non-gauge field constraint" in d["conclusion"]
    assert "does not pay" in d["conclusion"]
    assert "other source completions remain open" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1132 controls: 11/11")
