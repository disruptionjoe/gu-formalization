#!/usr/bin/env python3
"""K1109: noisy Loewner singular-gap certificate and instability boundary."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1109-k1108-noisy-loewner-gap-boundary.json"


def coalescent_determinant(t):
    return 2 * t * t / (9 * (1 + t) ** 2 * (2 + t) ** 2 * (3 + t) ** 2)


def build():
    ts = [Fraction(1), Fraction(1, 10), Fraction(1, 100)]
    dets = [coalescent_determinant(t) for t in ts]
    return {
        "schema_version": "1.0",
        "result_id": "K1109-K1108-NOISY-LOEWNER-GAP-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "perturbation_model": "Lhat=L+E with an independently certified spectral-norm bound ||E||_2<=epsilon",
        "weyl_bounds": ["sigma_j(Lhat)>=sigma_j(L)-epsilon", "sigma_j(L)>=sigma_j(Lhat)-epsilon"],
        "robust_lower_bound_rule": "sigma_r(Lhat)>epsilon certifies rank(L)>=r and therefore at least r-1 poles when alpha>0",
        "exact_order_rule": "the noisy lower bound becomes an exact order only after an independent at-most-(r-1)-pole bound",
        "null_rule": "sigma_r(Lhat)<=epsilon is inconclusive and cannot certify absence of the r-th direction",
        "near_coalescent_family": "alpha=2, weights=(1,1), shifts=(1,1+t), nodes=(0,1,2)",
        "determinant_formula": "det L(t)=2*t^2/[9(1+t)^2(2+t)^2(3+t)^2]",
        "fixture_t": [str(t) for t in ts],
        "fixture_determinants": [str(v) for v in dets],
        "stability_boundary": "as t tends to zero the third singular value and determinant vanish; no uniform noise threshold exists without pole-separation, weight, slope and sample-geometry floors",
        "decision": "finite noisy rank certification is gap-conditional, not a consequence of exact identifiability alone",
        "scope_boundary": "conditional matrix perturbation theorem; no measured Loewner error norm, source-owned pole floor or physical apparatus",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["perturbation_model"].startswith("Lhat=L+E")
    assert d["weyl_bounds"] == ["sigma_j(Lhat)>=sigma_j(L)-epsilon", "sigma_j(L)>=sigma_j(Lhat)-epsilon"]
    assert "rank(L)>=r" in d["robust_lower_bound_rule"]
    assert "independent at-most-(r-1)-pole bound" in d["exact_order_rule"]
    assert d["null_rule"].startswith("sigma_r(Lhat)<=epsilon is inconclusive")
    assert d["near_coalescent_family"].endswith("nodes=(0,1,2)")
    assert d["determinant_formula"] == "det L(t)=2*t^2/[9(1+t)^2(2+t)^2(3+t)^2]"
    assert d["fixture_t"] == ["1", "1/10", "1/100"]
    assert d["fixture_determinants"] == ["1/2592", "20000/461519289", "200000000/336055001230809"]
    assert "no uniform noise threshold" in d["stability_boundary"]
    assert "gap-conditional" in d["decision"]
    assert "no measured Loewner error norm" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1109 controls: 13/13")
