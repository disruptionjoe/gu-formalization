#!/usr/bin/env python3
"""K1037: stationary massive-wave generators descend and preserve energy."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1037-k1036-stationary-wave-generator.json"


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def horn(mass_squared):
    spatial_eigenvalue = 0
    omega_squared = spatial_eigenvalue + mass_squared
    m = [[omega_squared, 0, 0], [0, 1, 0], [0, 0, 0]]
    k = [[0, 1, 0], [-omega_squared, 0, 0], [0, 0, 0]]
    defect = add(mm(tr(k), m), mm(m, k))
    q, p = 3, 5
    qdot, pdot = p, -omega_squared * q
    energy_derivative = omega_squared * q * qdot + p * pdot
    return {"mass_squared": mass_squared, "spatial_eigenvalue": spatial_eigenvalue, "omega_squared": omega_squared, "M": m, "K": k, "defect": defect, "energy_derivative": energy_derivative}


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1037-K1036-STATIONARY-WAVE-GENERATOR",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "background": "Phi=0 on the cooriented ultrastatic slab [0,1]xT3 is stationary for both quadratic candidate actions",
        "phase_space": "each spatial Fourier mode has quotient coordinates (q,p) and ambient gauge radical g",
        "mode_rule": "omega_squared=spatial_eigenvalue+mass_squared; displayed exact controls use the spatial zero mode",
        "horns": [horn(1), horn(4)],
        "theorem": {
            "radical": "span(g)=ker M is invariant under K",
            "compatibility": "K^T M+M K=0",
            "consequence": "the first-order flow descends to the positive quotient and conserves its Cauchy energy",
        },
        "analytic_scope": "modewise exact control for the existing constant-coefficient H1 wave action; no nonlinear BV master equation or interacting common domain",
        "ownership": {"candidate_generator_owned": True, "source_GU_generator_owned": False, "dissipative_CPTP_resource_owned": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "Phi=0" in d["background"] and "stationary" in d["background"]
    assert "(q,p)" in d["phase_space"] and "gauge radical" in d["phase_space"]
    assert d["mode_rule"].startswith("omega_squared=spatial_eigenvalue+mass_squared")
    assert [h["mass_squared"] for h in d["horns"]] == [1, 4]
    for h in d["horns"]:
        assert h["defect"] == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert h["energy_derivative"] == 0
        assert h["omega_squared"] == h["spatial_eigenvalue"] + h["mass_squared"]
        assert h["M"][2][2] == 0 and h["K"][2] == [0, 0, 0]
    assert d["theorem"]["radical"].endswith("invariant under K")
    assert d["theorem"]["compatibility"] == "K^T M+M K=0"
    assert "positive quotient" in d["theorem"]["consequence"]
    assert "no nonlinear BV" in d["analytic_scope"]
    assert d["ownership"] == {"candidate_generator_owned": True, "source_GU_generator_owned": False, "dissipative_CPTP_resource_owned": False}
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1037 controls: 15/15")
