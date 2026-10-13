#!/usr/bin/env python3
"""Exact rational Hermite-contraction certificate for K1741."""
import json
from fractions import Fraction as F
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
        if n % 2:
            continue
        double_factorial = 1
        for k in range(1, n, 2):
            double_factorial *= k
        out += c * double_factorial
    return out


def coefficient(moment, order):
    d = {
        2: pscale(F(moment[0], 24), hermite(4)),
        3: pscale(F(moment[1], 720), hermite(6)),
        4: pscale(F(moment[2], 40320), hermite(8)),
        5: pscale(F(moment[3], 3628800), hermite(10)),
        6: pscale(F(moment[4], 479001600), hermite(12)),
    }
    derivatives = {i: pder(v) for i, v in d.items()}
    inverse = {0: [F(1)]}
    for n in range(1, order + 1):
        acc = [F(0)]
        for i in range(1, n + 1):
            if i in d and n - i in inverse:
                acc = padd(acc, pmul(d[i], inverse[n - i]))
        inverse[n] = pscale(F(-1), acc)
    total = [F(0)]
    for i, left in derivatives.items():
        for j, right in derivatives.items():
            remainder = order - i - j
            if remainder >= 0 and remainder in inverse:
                total = padd(total, pmul(pmul(left, right), inverse[remainder]))
    return gaussian_expectation(total)


def formula11(k4, k6, h8, h10, _h12):
    return -F(11, 302400) * (
        20*h10*h8*k4 - 700*h10*k4**3 + 21*h10*k6**2 + 70*h8**2*k6
        - 22960*h8*k4**2*k6 + 1162350*k4**4*k6 - 21210*k4*k6**3
    )


def formula12(k4, k6, h8, h10, h12):
    return F(1, 39916800) * (
        h12**2 - 990*h12*h8*k4 + 23100*h12*k4**3 - 924*h12*k6**2
        - 2970*h10**2*k4 - 27720*h10*h8*k6 + 3437280*h10*k4**2*k6
        - 11550*h8**3 + 5174235*h8**2*k4**2 - 406340550*h8*k4**4
        + 25391520*h8*k4*k6**2 + 10313399250*k4**6
        - 2184571620*k4**3*k6**2 + 5416026*k6**4
    )


def main():
    data = json.loads((ROOT / "lab/process/k1741-symmetric-twelfth-order-fisher-law.json").read_text())
    law, decision = data["hermite_law"], data["decision"]
    tuples = [
        (F(-1), F(0), F(35), F(7), F(-11)),
        (F(-2), F(4), F(9), F(-3), F(5)),
        (F(1, 3), F(-5, 2), F(11, 7), F(13, 5), F(-17, 6)),
        (F(-7, 4), F(3, 8), F(-2), F(6), F(19, 3)),
    ]
    checks = [("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1741")]
    for i, moment in enumerate(tuples, 1):
        checks += [
            (f"eleventh tuple {i}", coefficient(moment, 11) == formula11(*moment)),
            (f"twelfth tuple {i}", coefficient(moment, 12) == formula12(*moment)),
        ]
    checks += [
        ("classification", data["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("not a kill", data["target_claim"] == "NONE-NOT-A-KILL"),
        ("bounded scope", "fixed bounded symmetric" in data["scope"]),
        ("h12 density", "h_12/479001600" in law["density_ratio"]),
        ("eleventh factor", "-11[" in law["eleventh_coefficient"]),
        ("eleventh denominator", "/302400" in law["eleventh_coefficient"]),
        ("twelfth h12 square", "h_12^2" in law["twelfth_coefficient"]),
        ("twelfth denominator", "/39916800" in law["twelfth_coefficient"]),
        ("score quotient", "(r_t')^2/r_t" in law["derivation"]),
        ("probabilists normalization", "probabilists' Hermite" in law["normalization"]),
        ("eleventh decision", decision["eleventh_order_term_identified"]),
        ("twelfth decision", decision["twelfth_order_term_identified"]),
        ("new moment", decision["new_moment_first_enters_at_twelfth_order"] == "h_12"),
        ("moving uniformity fenced", not decision["uniform_remainder_for_moving_or_growing_seeds"]),
        ("finite optimizer open", not decision["finite_strength_optimizer_identified"]),
        ("physical status fixed", not decision["source_or_physical_status_changed"]),
        ("singular guard", "singular chart boundaries" in data["scope_guard"]),
        ("physical guard", "source-owned Hamiltonian" in data["scope_guard"]),
    ]
    assert len(checks) == 28
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
