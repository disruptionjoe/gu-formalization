#!/usr/bin/env python3
"""Exact Hermite-contraction certificate for K1706."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def hermite(n):
    if n == 0:
        return [1]
    h0, h1 = [1], [0, 1]
    for k in range(1, n):
        h0, h1 = h1, add([0] + h1, [-k * x for x in h0])
    return h1


def gaussian_expectation(poly):
    def odd_double_factorial(k):
        out = 1
        for value in range(1, k + 1, 2):
            out *= value
        return out
    return sum(Fraction(c) * odd_double_factorial(i - 1) for i, c in enumerate(poly) if i % 2 == 0)


def contraction(*orders):
    poly = [1]
    for order in orders:
        poly = mul(poly, hermite(order))
    return gaussian_expectation(poly)


def main():
    d = json.loads((ROOT / "lab/process/k1706-symmetric-eighth-order-fisher-law.json").read_text())
    h, z = d["hermite_law"], d["decision"]
    expected = {(4, 3, 5): 1440, (6, 3, 3): 720, (4, 5, 5): 14400,
                (4, 3, 7): 5040, (6, 3, 5): 10800, (8, 3, 3): 0,
                (4, 4, 3, 3): 30672}
    checks = [("schema", d["schema_version"] == "1.0"), ("claim", d["claim_id"] == "K1706")]
    checks += [("contraction " + "-".join(map(str, orders)), contraction(*orders) == value)
               for orders, value in expected.items()]
    checks += [
        ("symmetric scope", "bounded symmetric" in h["scope"]),
        ("h8 typed", "h_8=E H_8(X)" in h["moments"]),
        ("density H8", "h_8/40320" in h["density_ratio"]),
        ("seventh", "-(7/36)kappa_4^2kappa_6 t^7" in h["fisher"]),
        ("eighth square", "h_8^2/5040" in h["fisher"]),
        ("eighth mixed", "-kappa_4^2h_8/72" in h["fisher"]),
        ("eighth quartic", "71kappa_4^4/48" in h["fisher"]),
        ("seventh decision", z["seventh_order_term_identified"]),
        ("eighth decision", z["eighth_order_term_identified"]),
        ("all seed open", not z["all_seed_finite_strength_optimizer_identified"]),
        ("scope guard", "growing support" in d["scope_guard"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
