#!/usr/bin/env python3
"""Independent K212: integrate the transport cost, test scope and perturbations."""
from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k212-order-six-radial-transport-limit.json"
mp.mp.dps = 65


def direct_cost(a, b, p):
    density = lambda x: 256**6*x**5*mp.exp(-256*x)/mp.factorial(5)
    cdf = lambda x: mp.gammainc(6, 0, 256*x)/mp.factorial(5)
    t = mp.findroot(lambda x: cdf(x)-p, (a, b))
    assert a < t < b
    return (t, mp.quad(lambda x: abs(x-a)*density(x), [0, a, t])
            + mp.quad(lambda x: abs(x-b)*density(x), [t, b, mp.inf]))


def check():
    d = json.loads(MANIFEST.read_text())
    s = mp.sqrt(7)
    a, b, p = (7-s)/256, (7+s)/256, (1+1/s)/2
    t, w = direct_cost(a, b, p)
    qlo, qhi = map(lambda x: mp.mpf(Q(x).numerator)/Q(x).denominator,
                   d["quantile_open_rational_interval"])
    wlo, whi = map(lambda x: mp.mpf(Q(x).numerator)/Q(x).denominator,
                   d["w1_open_rational_interval"])
    assert qlo < t < qhi and wlo < w < whi
    radial = json.loads((ROOT / "lab/process/k205-order-six-radial-normal-form.json").read_text())
    old = Q(radial["all_groups_radial_only_error_upper_rational"])
    lip = Q(d["k205_lipschitz_aggregate_rational"])
    assert lip*Q(7, 512) == old
    assert d["necessary_positive_radial_node_count_for_this_certificate"] == (
        lip / (180*Q(1, 10**21))).__floor__()+1
    # Different independently integrated rule parameters cannot masquerade
    # as the certified K203 transport value.
    for shift in (mp.mpf("0.001"), -mp.mpf("0.001")):
        _, changed = direct_cost(a, b+shift, p)
        assert not (wlo < changed < whi)
    # The lower bound applies to the supremum over 1-Lipschitz functions,
    # not to each function: a constant has exactly zero quadrature error.
    assert mp.quad(lambda x: 0*mp.exp(-x), [0, mp.inf]) == 0
    # A uniform interval of density M exactly saturates 1/(4MN) at
    # equal-mass midpoint atoms.  This separately challenges the factor 4.
    M = mp.mpf(3)
    for n in (1, 2, 7):
        width = 1/(M*n)
        cell_cost = n*mp.quad(lambda x: M*abs(x-width/2),
                              [0, width/2, width])
        assert mp.almosteq(cell_cost, 1/(4*M*n))
    print("[PASS] independent incomplete-Gamma CDF, direct L1 integral and two hostile node shifts")
    print("[PASS] K205 constant, node floor and actual-error scope")


if __name__ == "__main__":
    check()
