#!/usr/bin/env python3
"""Exact rational Hermite-contraction certificate for K1736."""
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
        df = 1
        for k in range(1, n, 2):
            df *= k
        out += c * df
    return out


def coefficient(moment, order):
    d = {
        2: pscale(F(moment[0], 24), hermite(4)),
        3: pscale(F(moment[1], 720), hermite(6)),
        4: pscale(F(moment[2], 40320), hermite(8)),
        5: pscale(F(moment[3], 3628800), hermite(10)),
    }
    rp = {i: pder(v) for i, v in d.items()}
    inv = {0: [F(1)]}
    for n in range(1, order + 1):
        acc = [F(0)]
        for i in range(1, n + 1):
            if i in d and n - i in inv:
                acc = padd(acc, pmul(d[i], inv[n - i]))
        inv[n] = pscale(F(-1), acc)
    total = [F(0)]
    for i, vi in rp.items():
        for j, vj in rp.items():
            m = order - i - j
            if m >= 0 and m in inv:
                total = padd(total, pmul(pmul(vi, vj), inv[m]))
    return gaussian_expectation(total)


def formula9(k4, k6, h8, _h10):
    return -F(k6) * (9 * h8 * k4 - 855 * k4**3 + 5 * k6**2) / 360


def formula10(k4, k6, h8, h10):
    return (h10**2 - 420*h10*k4*k6 - 1260*h8**2*k4 + 138600*h8*k4**3
            - 3150*h8*k6**2 - 5658660*k4**5 + 680190*k4**2*k6**2) / F(362880)


def main():
    d = json.loads((ROOT / "lab/process/k1736-symmetric-tenth-order-fisher-law.json").read_text())
    h, z = d["hermite_law"], d["decision"]
    tuples = [(F(-1), F(0), F(35), F(7)), (F(-2), F(4), F(9), F(-3)),
              (F(1, 3), F(-5, 2), F(11, 7), F(13, 5)), (F(-7, 4), F(3, 8), F(-2), F(6))]
    checks = [("schema", d["schema_version"] == "1.0"), ("claim", d["claim_id"] == "K1736")]
    for i, m in enumerate(tuples, 1):
        checks += [(f"ninth tuple {i}", coefficient(m, 9) == formula9(*m)),
                   (f"tenth tuple {i}", coefficient(m, 10) == formula10(*m))]
    checks += [
        ("bounded symmetric scope", "bounded symmetric" in h["scope"]),
        ("h10 typed", "h_10=E H_10(X)" in h["moments"]),
        ("density h10", "h_10/3628800" in h["density_ratio"]),
        ("ninth k6 factor", "kappa_6(" in h["ninth_coefficient"]),
        ("ninth 855", "855kappa_4^3" in h["ninth_coefficient"]),
        ("tenth h10 square", "h_10^2" in h["tenth_coefficient"]),
        ("tenth denominator", "/362880" in h["tenth_coefficient"]),
        ("derivation score quotient", "(r_t')^2/r_t" in h["derivation"]),
        ("ninth decision", z["ninth_order_term_identified"]),
        ("tenth decision", z["tenth_order_term_identified"]),
        ("new moment", z["new_moment_first_enters_at_tenth_order"] == "h_10"),
        ("bounded decision", z["bounded_symmetric_scope_only"]),
        ("all seed open", not z["all_seed_finite_strength_optimizer_identified"]),
        ("growing support guard", "growing support" in d["scope_guard"]),
    ]
    assert len(checks) == 24
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
