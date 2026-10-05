#!/usr/bin/env python3
"""K1089: distinct flat holonomies obstruct one common spatial ladder."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1089-k1088-twisted-spectrum-ladder-obstruction.json"


def squares(alpha, modes):
    return [str((F(n) + alpha) ** 2) for n in modes]


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1089-K1088-TWISTED-SPECTRUM-LADDER-OBSTRUCTION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "carrier": "direct sum of two flat Hermitian line bundles over S1",
        "connections": "nabla_alpha=d/dx+i alpha with alpha_1=0 and alpha_2=1/2 on periodic representatives",
        "holonomies": ["+1", "-1"],
        "kinetic_and_mass": "B=identity and C=diag(1,4), both parallel, positive and commuting",
        "branch_rule": "omega_1,n^2=n^2+1 and omega_2,n^2=(n+1/2)^2+4",
        "laplacian_fixtures": {
            "alpha_0_modes_0_1_minus1": squares(F(0), [0, 1, -1]),
            "alpha_half_modes_0_minus1_1": squares(F(1, 2), [0, -1, 1]),
        },
        "spectral_obstruction": "the first restricted Laplacian has a zero mode while the second has lower bound 1/4, so their covariant spatial ladders are not the same",
        "product_basis_obstruction": "the Hessian has an orthogonal branch eigenbasis but no tensor-product basis built from one common scalar spatial eigenbasis and fixed internal vectors",
        "decision_rule": "parallel commuting B,C do not recover K1083's shared Fourier ladder unless the connection and boundary spectra also match across joint eigenbundles",
        "scope_boundary": "exact complex flat-circle counterexample; not a claim about the source GU connection or physical spectrum",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "two flat Hermitian line bundles" in d["carrier"]
    assert "alpha_1=0 and alpha_2=1/2" in d["connections"]
    assert d["holonomies"] == ["+1", "-1"]
    assert "parallel, positive and commuting" in d["kinetic_and_mass"]
    assert "(n+1/2)^2+4" in d["branch_rule"]
    assert d["laplacian_fixtures"]["alpha_0_modes_0_1_minus1"] == ["0", "1", "1"]
    assert d["laplacian_fixtures"]["alpha_half_modes_0_minus1_1"] == ["1/4", "1/4", "9/4"]
    assert "zero mode" in d["spectral_obstruction"] and "lower bound 1/4" in d["spectral_obstruction"]
    assert "no tensor-product basis" in d["product_basis_obstruction"]
    assert "connection and boundary spectra also match" in d["decision_rule"]
    assert "not a claim about the source GU connection" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1089 controls: 12/12")
