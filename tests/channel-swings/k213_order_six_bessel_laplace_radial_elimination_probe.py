#!/usr/bin/env python3
"""Independent low-factor quadrature and hostile normalization controls for K213."""
from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
mp.mp.dps = 45


def radial(supports: tuple[mp.mpf, ...]) -> mp.mpf:
    n = len(supports)
    c = mp.mpf(256)**6 / math.factorial(5)
    return c * mp.quad(lambda r: r**(5+n)*mp.exp(-256*r)*
                       mp.fprod(2*mp.besselk(1, r*s) for s in supports),
                       [0, mp.mpf("0.025"), mp.mpf("0.1"), 1, mp.inf])


def transformed(supports: tuple[mp.mpf, ...], *, power_shift: int = 0,
                factor_shift: int = 0) -> mp.mpf:
    n = len(supports)
    c = mp.mpf(2)**(n+factor_shift) * 256**6 * math.factorial(5+n)/math.factorial(5)
    power = 6+n+power_shift
    def integrate(i: int, total: mp.mpf) -> mp.mpf:
        if i == n:
            return (256+total)**(-power)
        return mp.quad(lambda t: mp.cosh(t)*integrate(i+1, total+supports[i]*mp.cosh(t)),
                       [0, 2, 5, 12, mp.inf])
    return c * integrate(0, mp.mpf(0))


def main() -> None:
    record = json.loads((P / "k213-order-six-bessel-laplace-radial-elimination.json").read_text())
    assert record["counts"]["factor_occurrences"] == 14912
    for supports in ((mp.mpf("0.2"),), (mp.mpf("0.17"), mp.mpf("0.31"))):
        lhs = radial(supports)
        rhs = transformed(supports)
        assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-30")), (lhs, rhs)
        # Two independent hostile edits must fail before the all-eight-factor
        # formula is trusted: dropped factor two and wrong Gamma exponent.
        assert abs(transformed(supports, factor_shift=-1)/lhs-1) > mp.mpf("0.4")
        assert abs(transformed(supports, power_shift=-1)/lhs-1) > mp.mpf("0.1")
        print("[PASS] independent radial/cosh integral, n =", len(supports))
    # Independent rational weighted-AM/GM normalization check at the equal
    # point and a deliberately asymmetric point (the bound is termwise).
    for values in ((mp.mpf(256),)+(mp.mpf(1),)*8,
                   (mp.mpf(256),)+tuple(mp.mpf(i+1)/7 for i in range(8))):
        d = sum(values)
        rhs = (values[0]/(mp.mpf(2)/14))**2 * mp.fprod(
            (v/(mp.mpf(3)/28))**(mp.mpf(3)/2) for v in values[1:])
        assert d**14 >= rhs*(1-mp.mpf("1e-40"))
    assert record["core_tail"]["first_even_T_sufficient_for_per_term_1e_minus_21_under_coarse_bound"] > 4000
    print("[PASS] weighted-AM/GM constant and intentionally loose core tail scope")


if __name__ == "__main__":
    main()
