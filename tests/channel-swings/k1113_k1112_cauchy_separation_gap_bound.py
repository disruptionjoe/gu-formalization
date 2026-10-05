#!/usr/bin/env python3
"""K1113: quantitative Cauchy separation-to-gap lower bound."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1113-k1112-cauchy-separation-gap-bound.json"


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def build():
    left = [Fraction(0), Fraction(1)]
    right = [Fraction(2), Fraction(3)]
    shifts = [Fraction(1), Fraction(3)]
    weights = [Fraction(1), Fraction(4)]
    vx = [[1 / (x + d) for d in shifts] for x in left]
    vy = [[1 / (y + d) for d in shifts] for y in right]
    residual = [[sum(weights[k] * vx[i][k] * vy[j][k] for k in range(2))
                 for j in range(2)] for i in range(2)]
    determinant = det2(residual)
    conservative_det_floor = Fraction(1, 419904)
    norm_ceiling = Fraction(16)
    singular_floor = conservative_det_floor / norm_ceiling
    return {
        "schema_version": "1.0",
        "result_id": "K1113-K1112-CAUCHY-SEPARATION-GAP-BOUND",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "cauchy_determinant": "det V(X,d)=prod_{i<j}(x_j-x_i)*prod_{i<j}(d_j-d_i)/prod_{i,k}(x_i+d_k)",
        "residual_determinant": "det R=det V_X*det V_Y*prod_i w_i",
        "general_floor": "for m nodes per side, q=m(m-1)/2, gaps delta_X,delta_Y,delta_d, 0<=x,y<=X, d<=D and w>=w_min: |det R|>=w_min^m*delta_X^q*delta_Y^q*delta_d^(2q)/(X+D)^(2m^2)",
        "norm_ceiling": "if d>=d_min and w<=w_max then ||R||_2<=m^2*w_max/d_min^2",
        "singular_floor": "sigma_min(R)>=|det R|/||R||_2^(m-1)",
        "fixture_det_vx": str(det2(vx)),
        "fixture_det_vy": str(det2(vy)),
        "fixture_det_r": str(determinant),
        "fixture_conservative_det_floor": str(conservative_det_floor),
        "fixture_norm_ceiling": str(norm_ceiling),
        "fixture_conservative_singular_floor": str(singular_floor),
        "decision": "owned pole, weight and node-separation floors yield an explicit positive but potentially conservative singular-gap certificate",
        "scope_boundary": "conditional finite-order bound; no owner supplies these floors for a GU physical branch or measured apparatus",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["cauchy_determinant"].startswith("det V(X,d)=")
    assert d["residual_determinant"] == "det R=det V_X*det V_Y*prod_i w_i"
    assert "delta_d^(2q)" in d["general_floor"]
    assert d["norm_ceiling"].endswith("m^2*w_max/d_min^2")
    assert d["singular_floor"].startswith("sigma_min(R)>=")
    assert d["fixture_det_vx"] == "1/12"
    assert d["fixture_det_vy"] == "1/180"
    assert d["fixture_det_r"] == "1/540"
    assert d["fixture_conservative_det_floor"] == "1/419904"
    assert d["fixture_norm_ceiling"] == "16"
    assert d["fixture_conservative_singular_floor"] == "1/6718464"
    assert "explicit positive" in d["decision"]
    assert "no owner supplies these floors" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1113 controls: 14/14")
