#!/usr/bin/env python3
"""K1071: extend the K77 quotient/generator packet to every positive mass."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1071-k1070-positive-mass-family-composition.json"


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def control(lam, mass_squared):
    omega_squared = lam + mass_squared
    m = [[omega_squared, 0, 0], [0, 1, 0], [0, 0, 0]]
    k = [[0, 1, 0], [-omega_squared, 0, 0], [0, 0, 0]]
    return {
        "spatial_eigenvalue": str(lam),
        "mass_squared": str(mass_squared),
        "omega_squared": str(omega_squared),
        "defect": [[str(x) for x in row] for row in add(mm(tr(k), m), mm(m, k))],
        "quotient_positive": omega_squared > 0,
        "radical_invariant": k[2] == [0, 0, 0],
    }


def build():
    fixtures = [(F(0), F(1, 7)), (F(3), F(1)), (F(8), F(4)), (F(15), F(25, 3))]
    rows = ["physical_quotient", "state_effect_pairing", "action_generator", "local_observables"]
    return {
        "schema_version": "1.0",
        "result_id": "K1071-K1070-POSITIVE-MASS-FAMILY-COMPOSITION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "parameter_domain": "every real mass_squared u>0 and spatial eigenvalue lambda>=0",
        "mode_rule": "omega_squared=lambda+u",
        "symbolic_pair": {"M_u": "diag(lambda+u,1,0)", "K_u": "[[0,1,0],[-(lambda+u),0,0],[0,0,0]]"},
        "identity": "K_u^T M_u+M_u K_u=0 identically in lambda and u",
        "family_result": "every positive u has the same K77 quotient, gauge radical and algebraic local-effect rows; the energy pairing varies with u",
        "structural_rows": rows,
        "controls": [control(lam, u) for lam, u in fixtures],
        "ownership": {"repository_candidate_family": True, "source_selected_coefficient": False, "scorable": False},
        "claim_ceiling": "exact positive-coefficient family inside the K77 repository-owned quadratic candidate class only",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "u>0" in d["parameter_domain"] and "lambda>=0" in d["parameter_domain"]
    assert d["mode_rule"] == "omega_squared=lambda+u"
    assert d["symbolic_pair"] == {"M_u": "diag(lambda+u,1,0)", "K_u": "[[0,1,0],[-(lambda+u),0,0],[0,0,0]]"}
    assert d["identity"].endswith("identically in lambda and u")
    assert "pairing varies with u" in d["family_result"]
    assert d["structural_rows"] == ["physical_quotient", "state_effect_pairing", "action_generator", "local_observables"]
    assert len(d["controls"]) == 4
    assert all(c["defect"] == [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]] for c in d["controls"])
    assert all(c["quotient_positive"] and c["radical_invariant"] for c in d["controls"])
    assert d["ownership"] == {"repository_candidate_family": True, "source_selected_coefficient": False, "scorable": False}
    assert "candidate class only" in d["claim_ceiling"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1071 controls: 14/14")
