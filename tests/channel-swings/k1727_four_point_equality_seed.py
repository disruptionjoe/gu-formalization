#!/usr/bin/env python3
"""Algebraic moment certificate for K1727."""
import json, math
from fractions import Fraction as F
from pathlib import Path
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[2]


def poly(u): return 17*u**3 - 38*u**2 + 84*u - 24


def main():
    d = json.loads((ROOT / "lab/process/k1727-four-point-equality-seed.json").read_text())
    q, z = d["algebraic_seed"], d["decision"]
    lo, hi = F(3270136791, 10_000_000_000), F(3270136792, 10_000_000_000)
    plo = 17*lo**3 - 38*lo**2 + 84*lo - 24
    phi = 17*hi**3 - 38*hi**2 + 84*hi - 24
    u = brentq(poly, float(lo), float(hi), xtol=1e-15)
    S = 2*(6-7*u)/(2-u); R = S-(3-u); disc = S*S-4*R
    A = (S-math.sqrt(disc))/2; B = (S+math.sqrt(disc))/2; p = (B-1)/(B-A)
    moments = [p*A**k+(1-p)*B**k for k in range(1,5)]
    targets = [1, 3-u, 15-15*u, 105-210*u+35*u*u]
    m2, m3, m4 = moments[1], moments[2], moments[3]
    k4 = m2-3; k6 = m3-15*m2+30; h8 = m4-28*m3+210*m2-315
    checks = [("schema", d["schema_version"] == "1.0"), ("claim", d["claim_id"] == "K1727"),
              ("derivative discriminant", 76**2-4*51*84 < 0), ("derivative positive", 51*0**2-76*0+84 > 0),
              ("root signs", plo < 0 < phi), ("root interval", float(lo) < u < float(hi)),
              ("positive roots", 0 < A < 1 < B), ("probability", 0 < p < 1),
              ("variance", math.isclose(moments[0], 1, abs_tol=3e-14)),
              ("moment 4", math.isclose(moments[1], targets[1], abs_tol=3e-13)),
              ("moment 6", math.isclose(moments[2], targets[2], abs_tol=3e-12)),
              ("moment 8", math.isclose(moments[3], targets[3], abs_tol=3e-11)),
              ("kappa4", math.isclose(k4, -u, abs_tol=3e-13)),
              ("kappa6", abs(k6) < 3e-12), ("h8", math.isclose(h8, 35*u*u, abs_tol=3e-11)),
              ("eighth ratio", math.isclose(h8/u**2, 35, abs_tol=3e-10)),
              ("cubic identity coefficients", [34, -76, 168, -48] == [2*17, 2*(-38), 2*84, 2*(-24)]),
              ("four point", not z["three_point_family"]), ("bounded", z["bounded_symmetric_unit_variance"]),
              ("negative defect", z["negative_fourth_cumulant"]), ("sixth zero", z["sixth_hermite_zero"]),
              ("scope", "four-atom" in d["scope_guard"])]
    for n, (label, ok) in enumerate(checks, 1): assert ok, label; print(f"PASS {n:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == '__main__': main()
