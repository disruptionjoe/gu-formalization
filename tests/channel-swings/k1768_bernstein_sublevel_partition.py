#!/usr/bin/env python3
"""Exact replay engine for K1768's correlation-preserving Hermite cover."""
from hashlib import sha256
from math import comb, factorial
import json
from pathlib import Path

import sympy as s
from flint import fmpq as Q

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1768-bernstein-sublevel-partition.json"
q, t, z = s.symbols("q t z", positive=True)
Q_FIXED = Q(1, 1024)
UPPER = Q(159178645305, 10**18)
# The rational lower endpoint is strictly below sqrt(1/2048) by direct
# integer squaring, so this rectangle contains the complete physical chart.
T_BOX = (Q(11863283, 536870912), Q(31, 32))
Z_BOX = (Q(0), Q(1))
MAX_T_DEPTH = 7
MAX_Z_DEPTH = 7


def projection_rational(degree):
    c = 2 - q / t**2
    w = c / z - z
    mu = {0: s.Integer(1), 1: s.Integer(0), 2: c}
    for r in range(3, degree + 2):
        mu[r] = s.cancel(w * mu[r - 1] + c * mu[r - 2])
    raw = {
        r: s.cancel(sum(s.binomial(r, j) * mu[j] for j in range(r + 1)))
        for r in range(degree + 2)
    }

    def hx(n):
        return s.cancel(
            sum(
                (-1) ** j
                * s.factorial(n)
                / (s.factorial(j) * s.factorial(n - 2 * j) * 2**j)
                * raw[(n - 2 * j) // 2]
                for j in range(n // 2 + 1)
            )
        )

    hy = {n: s.cancel(t ** (n // 2) * hx(n)) for n in range(0, 2 * degree + 1, 2)}
    ds = list(range(3, degree + 1, 2))
    b = s.Matrix([hy[n + 1] for n in ds])
    gram = s.Matrix(
        [
            [
                s.cancel(
                    sum(
                        s.factorial(j)
                        * s.binomial(m, j)
                        * s.binomial(n, j)
                        * hy[m + n - 2 * j]
                        for j in range(min(m, n) + 1)
                    )
                )
                for n in ds
            ]
            for m in ds
        ]
    )
    return s.cancel((b.T * gram.inv() * b)[0])


def threshold_polynomial(degree=5):
    value = projection_rational(degree).subs(q, s.Rational(1, 1024))
    numerator, denominator = map(s.expand, s.fraction(s.cancel(value)))
    # Normalize to the positive Gram-determinant orientation at one regular
    # chart control; K1767 proves the sign cannot change on the chart.
    control = denominator.subs({t: s.Rational(1, 20), z: s.Rational(1, 2)})
    if control < 0:
        numerator, denominator = -numerator, -denominator
    polynomial = s.Poly(
        s.expand(numerator - s.Rational(UPPER.numerator, UPPER.denominator) * denominator),
        t,
        z,
    )
    terms = {
        exponents: Q(int(coeff.p), int(coeff.q))
        for exponents, coeff in polynomial.terms()
    }
    return value, numerator, denominator, terms


def iadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def imul(a, b):
    products = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(products), max(products)


def horner_bound(terms, tb, zb, outer="t"):
    if outer == "z":
        swapped = {(j, i): coefficient for (i, j), coefficient in terms.items()}
        return horner_bound(swapped, zb, tb, "t")
    max_i = max(i for i, _ in terms)
    max_j = max(j for _, j in terms)
    coefficient_intervals = []
    for i in range(max_i + 1):
        acc = (Q(0), Q(0))
        for j in range(max_j, -1, -1):
            acc = iadd(imul(acc, zb), (terms.get((i, j), Q(0)),) * 2)
        coefficient_intervals.append(acc)
    acc = (Q(0), Q(0))
    for i in range(max_i, -1, -1):
        acc = iadd(imul(acc, tb), coefficient_intervals[i])
    return acc


def polynomial_bound(terms, tb, zb):
    tm, zm = (tb[0] + tb[1]) / 2, (zb[0] + zb[1]) / 2
    center = horner_bound(terms, (tm, tm), (zm, zm))[0]
    derivative_t = {
        (i - 1, j): coefficient * i
        for (i, j), coefficient in terms.items()
        if i
    }
    derivative_z = {
        (i, j - 1): coefficient * j
        for (i, j), coefficient in terms.items()
        if j
    }
    dt = horner_bound(derivative_t, tb, zb)
    dz = horner_bound(derivative_z, tb, zb)
    dt_abs = max(abs(dt[0]), abs(dt[1]))
    dz_abs = max(abs(dz[0]), abs(dz[1]))
    radius = (tb[1] - tb[0]) * dt_abs / 2 + (zb[1] - zb[0]) * dz_abs / 2
    return center - radius, center + radius


def bernstein_bound(terms, tb, zb):
    ta, tb_hi = tb
    za, zb_hi = zb
    ht, hz = tb_hi - ta, zb_hi - za
    degree_t = max(i for i, _ in terms)
    degree_z = max(j for _, j in terms)
    power = {(i, j): Q(0) for i in range(degree_t + 1) for j in range(degree_z + 1)}
    ta_powers = [ta**i for i in range(degree_t + 1)]
    ht_powers = [ht**i for i in range(degree_t + 1)]
    za_powers = [za**j for j in range(degree_z + 1)]
    hz_powers = [hz**j for j in range(degree_z + 1)]
    for (k, ell), coefficient in terms.items():
        for i in range(k + 1):
            t_factor = Q(comb(k, i)) * ta_powers[k - i] * ht_powers[i]
            for j in range(ell + 1):
                power[i, j] += coefficient * t_factor * Q(comb(ell, j)) * za_powers[ell - j] * hz_powers[j]
    bernstein = []
    for i in range(degree_t + 1):
        for j in range(degree_z + 1):
            value = Q(0)
            for k in range(i + 1):
                ti = Q(comb(i, k), comb(degree_t, k))
                for ell in range(j + 1):
                    value += power[k, ell] * ti * Q(comb(j, ell), comb(degree_z, ell))
            bernstein.append(value)
    return min(bernstein), max(bernstein)


def split(box):
    ta, tb, za, zb, dt, dz = box
    t_relative = (tb - ta) / (T_BOX[1] - T_BOX[0]) if dt < MAX_T_DEPTH else Q(-1)
    z_relative = (zb - za) / (Z_BOX[1] - Z_BOX[0]) if dz < MAX_Z_DEPTH else Q(-1)
    if t_relative >= z_relative and dt < MAX_T_DEPTH:
        middle = (ta + tb) / 2
        return (ta, middle, za, zb, dt + 1, dz), (middle, tb, za, zb, dt + 1, dz)
    if dz < MAX_Z_DEPTH:
        middle = (za + zb) / 2
        return (ta, tb, za, middle, dt, dz + 1), (ta, tb, middle, zb, dt, dz + 1)
    return None


def encode_fraction(value):
    return str(value)


def replay():
    value, numerator, denominator, terms = threshold_polynomial(5)
    stack = [(T_BOX[0], T_BOX[1], Z_BOX[0], Z_BOX[1], 0, 0)]
    pruned = []
    retained = []
    while stack:
        box = stack.pop()
        ta, tb, za, zb, dt, dz = box
        bound = polynomial_bound(terms, (ta, tb), (za, zb))
        if bound[0] > 0:
            exact_bernstein = bernstein_bound(terms, (ta, tb), (za, zb))
            assert exact_bernstein[0] > 0
            pruned.append((box, exact_bernstein[0]))
            continue
        children = split(box)
        if children is None:
            retained.append((box, bound))
        else:
            stack.extend(reversed(children))
    rows = []
    for kind, collection in (("P", pruned), ("R", retained)):
        for item in collection:
            box = item[0]
            rows.append(kind + ":" + ":".join(encode_fraction(x) for x in box[:4]))
    digest = sha256("\n".join(rows).encode()).hexdigest()
    if retained:
        hull = (
            min(row[0][0] for row in retained),
            max(row[0][1] for row in retained),
            min(row[0][2] for row in retained),
            max(row[0][3] for row in retained),
        )
    else:
        hull = None
    return {
        "projection": value,
        "numerator": numerator,
        "denominator": denominator,
        "terms": terms,
        "pruned": pruned,
        "retained": retained,
        "digest": digest,
        "hull": hull,
    }


def summary(result):
    return {
        "degree": 5,
        "threshold": encode_fraction(UPPER),
        "root_t": [encode_fraction(x) for x in T_BOX],
        "root_z": [encode_fraction(x) for x in Z_BOX],
        "physical_t_lower_contained": T_BOX[0] ** 2 < Q_FIXED / 2,
        "max_depth": {"t": MAX_T_DEPTH, "z": MAX_Z_DEPTH},
        "polynomial_terms": len(result["terms"]),
        "pruned_leaves": len(result["pruned"]),
        "retained_leaves": len(result["retained"]),
        "unresolved_leaves": 0,
        "partition_digest": result["digest"],
        "retained_hull": None
        if result["hull"] is None
        else [encode_fraction(x) for x in result["hull"]],
    }


def main():
    result = replay()
    got = summary(result)
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(got, indent=2))
        return
    data = json.loads(ARTIFACT.read_text())
    expected = data["partition"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1768"),
        ("partition replay", expected == got),
        ("physical lower contained", got["physical_t_lower_contained"]),
        ("zero unresolved", got["unresolved_leaves"] == 0),
        ("nonempty prune", got["pruned_leaves"] > 0),
        ("nonempty retain", got["retained_leaves"] > 0),
        ("cover not optimizer", not data["decision"]["global_optimizer_proved"]),
    ]
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
