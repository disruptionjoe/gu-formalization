#!/usr/bin/env python3
"""Independent moment, one-dimensional integral, and hostile K216 controls."""
from __future__ import annotations

from fractions import Fraction as Q
import importlib.util
import json
from math import comb, factorial
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k216_order_six_analytic_angular_prefix.py"
MANIFEST = ROOT / "lab/process/k216-order-six-analytic-angular-prefix.json"
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
spec = importlib.util.spec_from_file_location("k216", SCRIPT)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def direct_moment(a: list[Q], n: int) -> Q:
    """Multinomial Dirichlet moment, unrelated to producer's power-sum recurrence."""
    beta0 = Q(14)
    denominator = Q(1)
    for k in range(n):
        denominator *= beta0 + k
    result = Q(0)

    def visit(i: int, left: int, multinomial: int, poch: Q, power: Q) -> None:
        nonlocal result
        if i == 14:
            if left == 0:
                result += multinomial * poch * power / denominator
            return
        for k in range(left + 1):
            rising = Q(1)
            for h in range(k):
                rising *= Q(1) + h
            visit(i + 1, left - k, multinomial * comb(left, k),
                  poch * rising, power * a[i]**k)

    visit(0, n, 1, Q(1), Q(1))
    return result


def main() -> None:
    data = json.loads(MANIFEST.read_text())
    source = json.loads(K185.read_text())
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    count = 0
    first = None
    for entry in source["complete_face_hypergraph"]["entries"]:
        for term in entry["terms"]:
            masks = [int(x, 16) for x in catalog[term["allocation_id"]]
                     ["support_masks_hex"].split(",")]
            loads = [sum((mask >> i) & 1 for mask in masks) for i in range(14)]
            assert len(masks) == 8 and (min(loads), max(loads)) == (1, 7)
            first = first or loads
            count += 1
    assert count == 1864 and first is not None

    # Independently expand the low angular moments by multinomial enumeration.
    for profile in (first, list(reversed(first)), [7]*13 + [1]):
        loads = [Q(x) for x in profile]
        top = max(loads)
        a = [(top - x)/(256 + top) for x in loads]
        coefficients = module.series_coefficients(tuple(loads), 3)
        for n in range(4):
            rising14 = Q(factorial(13+n), factorial(13))
            assert coefficients[n] == rising14 * direct_moment(a, n) / factorial(n)

    # One nonzero a reduces the angular average to an ordinary Beta integral.
    mp.mp.dps = 70
    single = [Q(7)]*13 + [Q(1)]
    a = mp.mpf(6)/263
    beta = mp.beta(1, 13)
    direct = mp.quad(lambda z: (1-z)**12 / (1-a*z)**14 / beta,
                     [0, 1])
    partial = module.series_coefficients(tuple(single), 20)
    summed = mp.mpf(0)
    for x in partial:
        summed += mp.mpf(x.numerator)/x.denominator
    q = Q(31, 1059)
    r = module.relative_remainder(q, 20)
    assert 0 < direct - summed < mp.mpf(r.numerator)/r.denominator

    # A deliberately wrong isolated residual changes the second angular
    # coefficient even though the first coefficient shares the same mean.
    a_profile = [Q(0)]*13 + [Q(6, 263)]
    raw_second = module.series_coefficients(tuple(single), 2)[2]
    weighted_second = Q(15*14, 2) * (Q(5, 3)*Q(8, 3) / (Q(70, 3)*Q(73, 3))) * a_profile[-1]**2
    assert raw_second != weighted_second
    # Hostile normalization and face controls: the envelope is raw K213,
    # not an isolated Dirichlet(5/3) residual or Gamma expectation.
    raw = Q(data["small_box"]["raw_term_absolute_error_ceiling"])
    all_terms = Q(data["small_box"]["whole_unsigned_1864_term_absolute_error_ceiling"])
    assert all_terms == 1864 * raw and raw > 0
    assert data["small_box"]["q_ceiling"] == str(q)
    assert data["example_loads_at_all_t_zero"] == first
    hostile = [0] + [1 << i for i in range(1, 8)]
    hostile_loads = [sum((mask >> i) & 1 for mask in hostile) for i in range(14)]
    assert min(hostile_loads) == 0  # rejected by the actual all-mask invariant
    assert (q * Q(35, 22)) < 1
    large_q = Q(data["large_box"]["uniform_q_at_that_box"])
    assert large_q * Q(35, 22) > 1
    print("[PASS] 1,864 independent support replays and low multinomial moments")
    assert "reference/residual cancellation" in data["small_box"]["normalization"]
    print("[PASS] independent uniform Beta integral, raw normalization and hostile weight/face")


if __name__ == "__main__":
    main()
