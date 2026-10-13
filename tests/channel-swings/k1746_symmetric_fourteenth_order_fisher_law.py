#!/usr/bin/env python3
"""Exact rational Hermite-contraction certificate for K1746."""
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def padd(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0)) for i in range(n)]


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def pscale(c, a):
    return [c * x for x in a]


def pder(a):
    return [F(i) * a[i] for i in range(1, len(a))] or [F(0)]


def hermite(n):
    if n == 0:
        return [F(1)]
    h0, h1 = [F(1)], [F(0), F(1)]
    for k in range(1, n):
        h0, h1 = h1, padd([F(0)] + h1, pscale(F(-k), h0))
    return h1


def gaussian_expectation(poly):
    out = F(0)
    for n, c in enumerate(poly):
        if n % 2 == 0:
            out += c * factorial(n) / (2 ** (n // 2) * factorial(n // 2))
    return out


def coefficient(moment, order):
    density = {n: pscale(F(moment[n - 2], factorial(2 * n)), hermite(2 * n)) for n in range(2, 8)}
    derivatives = {n: pder(v) for n, v in density.items()}
    inverse = {0: [F(1)]}
    for n in range(1, order + 1):
        acc = [F(0)]
        for i in range(1, n + 1):
            if i in density:
                acc = padd(acc, pmul(density[i], inverse[n - i]))
        inverse[n] = pscale(F(-1), acc)
    total = [F(0)]
    for i, left in derivatives.items():
        for j, right in derivatives.items():
            remainder = order - i - j
            if remainder >= 0:
                total = padd(total, pmul(pmul(left, right), inverse[remainder]))
    return gaussian_expectation(total)


def formula13(k4, k6, h8, h10, h12, _h14):
    return F(13, 5443200) * (
        441485100*k4**5*k6 - 16895130*k4**2*k6**3 - 13524840*k4**3*k6*h8
        - 508725*k4**4*h10 + 73206*k6**3*h8 + 92070*k4*k6*h8**2
        + 36330*k4*k6**2*h10 + 16245*k4**2*h8*h10 + 1680*k4**2*k6*h12
        - 63*h8**2*h10 - 30*k6*h10**2 - 18*k6*h8*h12 - 5*k4*h10*h12
    )


def formula14(k4, k6, h8, h10, h12, h14):
    return F(1, 6227020800) * (
        h14**2 - 2002*k4*h10*h14 - 6006*k6*h8*h14 + 420420*k4**2*k6*h14
        - 6006*k4*h12**2 - 90090*k6*h10*h12 - 84084*h8**2*h12 - 210210*h8*h10**2
        + 18078060*k4**2*h8*h12 + 26027001*k4**2*h10**2 + 37585548*k4*k6**2*h12
        + 486137652*k4*k6*h8*h10 + 181621440*k4*h8**3 + 181621440*k6**3*h10
        + 627810183*k6**2*h8**2 - 460359900*k4**4*h12 - 30603212640*k4**3*k6*h10
        - 36786719970*k4**3*h8**2 - 259246947960*k4**2*k6**2*h8
        - 103188977892*k4*k6**4 + 2083500619200*k4**5*h8
        + 12723722681670*k4**4*k6**2 - 38476131794100*k4**7
    )


def main():
    data = json.loads((ROOT / "lab/process/k1746-symmetric-fourteenth-order-fisher-law.json").read_text())
    law, decision = data["hermite_law"], data["decision"]
    samples = [
        (F(-1), F(0), F(35), F(7), F(-11), F(13)),
        (F(-2), F(4), F(9), F(-3), F(5), F(-7)),
        (F(1, 3), F(-5, 2), F(11, 7), F(13, 5), F(-17, 6), F(19, 4)),
        (F(-7, 4), F(3, 8), F(-2), F(6), F(19, 3), F(-23, 5)),
    ]
    checks = [("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1746")]
    for i, moment in enumerate(samples, 1):
        checks += [
            (f"thirteenth tuple {i}", coefficient(moment, 13) == formula13(*moment)),
            (f"fourteenth tuple {i}", coefficient(moment, 14) == formula14(*moment)),
        ]
    checks += [
        ("classification", data["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("not a kill", data["target_claim"] == "NONE-NOT-A-KILL"),
        ("bounded scope", "fixed bounded symmetric" in data["scope"]),
        ("h14 density", "h_14/87178291200" in law["density_ratio"]),
        ("thirteenth denominator", "/5443200" in law["thirteenth_coefficient"]),
        ("fourteenth h14 square", "h_14^2" in law["fourteenth_coefficient"]),
        ("fourteenth denominator", "/6227020800" in law["fourteenth_coefficient"]),
        ("score quotient", "(r_t')^2/r_t" in law["derivation"]),
        ("probabilists normalization", "probabilists' Hermite" in law["normalization"]),
        ("thirteenth decision", decision["thirteenth_order_term_identified"]),
        ("fourteenth decision", decision["fourteenth_order_term_identified"]),
        ("h14 absent at thirteen", decision["h_14_absent_at_thirteenth_order"]),
        ("new moment", decision["new_moment_first_enters_at_fourteenth_order"] == "h_14"),
        ("moving uniformity fenced", not decision["uniform_remainder_for_moving_or_growing_seeds"]),
        ("finite optimizer open", not decision["finite_strength_optimizer_identified"]),
        ("physical status fixed", not decision["source_or_physical_status_changed"]),
        ("complete branch guarded", "no complete branch" in data["scope_guard"]),
        ("physical guard", "source-owned Hamiltonian" in data["scope_guard"]),
    ]
    assert len(checks) == 28
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
