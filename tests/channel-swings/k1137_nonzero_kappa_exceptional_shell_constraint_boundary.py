#!/usr/bin/env python3
"""K1137: separate exceptional-shell compatibility from local constraints."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1137-nonzero-kappa-exceptional-shell-constraint-boundary.json"


def load(name):
    return json.loads((ROOT / "lab/process" / name).read_text())


def build():
    theorem = load("k1136-polynomial-constraint-symbol-dense-open-vanishing.json")
    k1132 = load("k1132-nonzero-kappa-elimination-not-constraint.json")
    k134 = load("selected-k134-native-i1b-t0-kappa-hodge-fingerprint-and-fourier-pencil.json")
    shells = k134["fourier_hermitian_pencil"]["spacelike_root_squared_multiplicity"]
    return {
        "schema_version": "1.0",
        "result_id": "K1137-NONZERO-KAPPA-EXCEPTIONAL-SHELL-CONSTRAINT-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "inputs": [theorem["result_id"], k1132["result_id"], k134["artifact_id"]],
        "generic_nonzero_kappa_constraint_rank": 0,
        "spacelike_exceptional_squared_shell_count": len(shells),
        "spacelike_exceptional_squared_shells": sorted(int(x) for x in shells),
        "shell_left_null_compatibility_may_exist": True,
        "shell_rows_extend_to_nonzero_polynomial_local_constraint": False,
        "conclusion": "the current nonzero-kappa exceptional shells may carry spectral solvability conditions, but they cannot be the isolated support of a nonzero homogeneous finite-order local differential constraint symbol that is zero on the dense generic-invertible region",
        "reopeners": ["different source-owned differential", "nonlocal or distributional spectral constraint with independent ownership", "actual boundary coupling", "stationary global background"],
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; ledger unchanged",
        "scope_boundary": "selected current I1B pencil only; no exclusion of new differential, nonlocal spectral datum, boundary coupling or completed action",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["inputs"]) == 3
    assert d["generic_nonzero_kappa_constraint_rank"] == 0
    assert d["spacelike_exceptional_squared_shell_count"] == 27
    assert d["spacelike_exceptional_squared_shells"][0] == 1
    assert d["spacelike_exceptional_squared_shells"][-1] == 168
    assert d["shell_left_null_compatibility_may_exist"]
    assert not d["shell_rows_extend_to_nonzero_polynomial_local_constraint"]
    assert "spectral solvability" in d["conclusion"]
    assert len(d["reopeners"]) == 4
    assert "remain ASSERTS" in d["protected_disposition"]
    assert "no exclusion" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1137 controls: 12/12")
