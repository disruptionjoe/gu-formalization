#!/usr/bin/env python3
"""Replay K1796's exact fixed-cutoff degree-eleven Bernstein bank."""
from fractions import Fraction
from hashlib import sha256
from math import comb
import json
from pathlib import Path
import sys

from flint import fmpq as Q
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1796-full-fisher-retained-box-enclosure-bank.json"
K1791 = ROOT / "lab/process/k1791-full-fisher-three-slab-tail-cover.json"
DEGREE = 11
MAX_DEPTH = 4
Q0 = sp.Rational(1, 1024)
UPPER = sp.Rational(31835729061, 200000000000000000)

RETAINED = """
3 6 887855469/17179869184 14713917917/274877906944 73/128 293/512
3 6 887855469/17179869184 14713917917/274877906944 293/512 147/256
3 6 887855469/17179869184 14713917917/274877906944 147/256 295/512
3 6 887855469/17179869184 14713917917/274877906944 295/512 37/64
3 5 887855469/17179869184 14713917917/274877906944 9/16 289/512
3 5 887855469/17179869184 14713917917/274877906944 289/512 145/256
3 5 887855469/17179869184 14713917917/274877906944 145/256 291/512
3 5 887855469/17179869184 14713917917/274877906944 291/512 73/128
3 4 14713917917/274877906944 7611074165/137438953472 71/128 285/512
3 4 14713917917/274877906944 7611074165/137438953472 285/512 143/256
3 4 887855469/17179869184 14713917917/274877906944 143/256 287/512
3 4 887855469/17179869184 14713917917/274877906944 287/512 9/16
3 4 14713917917/274877906944 7611074165/137438953472 143/256 287/512
3 4 14713917917/274877906944 7611074165/137438953472 287/512 9/16
3 3 14713917917/274877906944 7611074165/137438953472 281/512 141/256
3 3 14713917917/274877906944 7611074165/137438953472 141/256 283/512
3 3 14713917917/274877906944 7611074165/137438953472 283/512 71/128
2 3 13697457091/274877906944 887855469/17179869184 75/128 301/512
2 3 13697457091/274877906944 887855469/17179869184 301/512 151/256
2 2 13697457091/274877906944 887855469/17179869184 37/64 297/512
2 2 13697457091/274877906944 887855469/17179869184 297/512 149/256
2 2 13697457091/274877906944 887855469/17179869184 149/256 299/512
2 2 13697457091/274877906944 887855469/17179869184 299/512 75/128
2 1 13697457091/274877906944 887855469/17179869184 147/256 295/512
2 1 13697457091/274877906944 887855469/17179869184 295/512 37/64
"""


def projection_terms():
    t, z = sp.symbols("t z", positive=True)
    c = 2 - Q0 / t**2
    w = c / z - z
    mu = {0: sp.Integer(1), 1: sp.Integer(0), 2: c}
    for r in range(3, 2 * DEGREE + 2):
        mu[r] = sp.cancel(w * mu[r - 1] + c * mu[r - 2])
    raw = {
        r: sp.cancel(sum(sp.binomial(r, j) * mu[j] for j in range(r + 1)))
        for r in range(2 * DEGREE + 2)
    }

    def hx(n):
        return sp.cancel(sum(
            (-1)**j * sp.factorial(n)
            / (sp.factorial(j) * sp.factorial(n - 2*j) * 2**j)
            * raw[(n - 2*j)//2]
            for j in range(n//2 + 1)
        ))

    hy = {n: sp.cancel(t**(n//2) * hx(n)) for n in range(0, 2*DEGREE + 1, 2)}
    degrees = list(range(3, DEGREE + 1, 2))
    b = sp.Matrix([hy[n + 1] for n in degrees])
    gram = sp.Matrix([[
        sp.cancel(sum(
            sp.factorial(j) * sp.binomial(m, j) * sp.binomial(n, j) * hy[m+n-2*j]
            for j in range(min(m, n) + 1)
        ))
        for n in degrees] for m in degrees])
    value = sp.cancel((b.T * (gram.inv(method="DM") * b))[0])
    numerator, denominator = map(sp.expand, sp.fraction(value))
    if denominator.subs({t: sp.Rational(1, 20), z: sp.Rational(1, 2)}) < 0:
        numerator, denominator = -numerator, -denominator
    rows = sp.Poly(sp.expand(numerator - UPPER * denominator), t, z).terms()
    digest = sha256("\n".join(
        f"{exponents[0]},{exponents[1]}:{coefficient}"
        for exponents, coefficient in rows
    ).encode()).hexdigest()
    terms = {}
    for exponents, coefficient in rows:
        rational = Fraction(str(coefficient))
        terms[exponents] = Q(rational.numerator, rational.denominator)
    return terms, digest


def bernstein_bound(terms, box):
    ta, tb, za, zb = box
    ht, hz = tb - ta, zb - za
    dt = max(i for i, _ in terms)
    dz = max(j for _, j in terms)
    t_power, ht_power = [Q(1)], [Q(1)]
    z_power, hz_power = [Q(1)], [Q(1)]
    for _ in range(dt):
        t_power.append(t_power[-1] * ta)
        ht_power.append(ht_power[-1] * ht)
    for _ in range(dz):
        z_power.append(z_power[-1] * za)
        hz_power.append(hz_power[-1] * hz)
    affine_t = [[Q(0) for _ in range(dz + 1)] for _ in range(dt + 1)]
    for (k, ell), coefficient in terms.items():
        for i in range(k + 1):
            affine_t[i][ell] += coefficient * Q(comb(k, i)) * t_power[k-i] * ht_power[i]
    affine = [[Q(0) for _ in range(dz + 1)] for _ in range(dt + 1)]
    for i in range(dt + 1):
        for ell in range(dz + 1):
            if affine_t[i][ell]:
                for j in range(ell + 1):
                    affine[i][j] += affine_t[i][ell] * Q(comb(ell, j)) * z_power[ell-j] * hz_power[j]
    t_bernstein = [[Q(0) for _ in range(dz + 1)] for _ in range(dt + 1)]
    for big_i in range(dt + 1):
        for i in range(big_i + 1):
            factor = Q(comb(big_i, i), comb(dt, i))
            for j in range(dz + 1):
                t_bernstein[big_i][j] += affine[i][j] * factor
    lower = upper = None
    for big_i in range(dt + 1):
        for big_j in range(dz + 1):
            value = sum(
                (t_bernstein[big_i][j] * Q(comb(big_j, j), comb(dz, j)) for j in range(big_j + 1)),
                Q(0),
            )
            lower = value if lower is None or value < lower else lower
            upper = value if upper is None or value > upper else upper
    return lower, upper


def roots():
    out = []
    for line in RETAINED.splitlines():
        if line.strip():
            slab, cell, *values = line.split()
            out.append((int(slab), int(cell), tuple(Q(value) for value in values)))
    return out


def replay():
    prior = json.loads(K1791.read_text())["partition"]
    terms, coefficient_digest = projection_terms()
    root_boxes = roots()
    pruned, retained = [], []
    stack = [(slab, cell, box, 0) for slab, cell, box in root_boxes]
    while stack:
        slab, cell, box, depth = stack.pop()
        lower, _ = bernstein_bound(terms, box)
        if lower > 0:
            pruned.append((slab, cell, box, depth))
            continue
        if depth == MAX_DEPTH:
            retained.append((slab, cell, box, depth))
            continue
        ta, tb, za, zb = box
        if depth % 2 == 0:
            middle = (ta + tb) / 2
            children = ((ta, middle, za, zb), (middle, tb, za, zb))
        else:
            middle = (za + zb) / 2
            children = ((ta, tb, za, middle), (ta, tb, middle, zb))
        stack.extend((slab, cell, child, depth + 1) for child in reversed(children))
    rows = []
    for kind, collection in (("P", pruned), ("R", retained)):
        for slab, cell, box, depth in collection:
            rows.append(f"{kind}:{slab}:{cell}:{depth}:" + ":".join(map(str, box)))
    input_area = sum((box[1]-box[0])*(box[3]-box[2]) for _, _, box in root_boxes)
    retained_area = sum((box[1]-box[0])*(box[3]-box[2]) for _, _, box, _ in retained)
    by_slab = []
    for slab in (2, 3):
        slab_roots = [row for row in root_boxes if row[0] == slab]
        slab_retained = [row for row in retained if row[0] == slab]
        root_area = sum((row[2][1]-row[2][0])*(row[2][3]-row[2][2]) for row in slab_roots)
        residual_area = sum((row[2][1]-row[2][0])*(row[2][3]-row[2][2]) for row in slab_retained)
        original_fraction = Q(8 if slab == 2 else 17, 944) * residual_area / root_area
        by_slab.append({
            "slab": slab,
            "input_leaves": len(slab_roots),
            "pruned_leaves": sum(row[0] == slab for row in pruned),
            "retained_leaves": len(slab_retained),
            "retained_fraction_of_slab_input_area": str(residual_area / root_area),
            "retained_fraction_of_original_input_area": str(original_fraction),
        })
    original_retained = Q(25, 944) * retained_area / input_area
    return {
        "cutoff_q": "1/1024",
        "degree": DEGREE,
        "odd_basis_dimension": 5,
        "threshold": str(Q(31835729061, 200000000000000000)),
        "polynomial_terms": len(terms),
        "coefficient_digest": coefficient_digest,
        "input_partition_digest": prior["partition_digest"],
        "input_retained_leaves": len(root_boxes),
        "adaptive_split_order": ["t", "z", "t", "z"],
        "max_depth": MAX_DEPTH,
        "pruned_leaves": len(pruned),
        "retained_leaves": len(retained),
        "terminal_leaves": len(pruned) + len(retained),
        "retained_fraction_of_k1791_area": str(retained_area / input_area),
        "excluded_fraction_of_k1791_area": str(1 - retained_area / input_area),
        "retained_fraction_of_original_input_area": str(original_retained),
        "excluded_fraction_of_original_input_area": str(1 - original_retained),
        "by_slab": by_slab,
        "partition_digest": sha256("\n".join(rows).encode()).hexdigest(),
    }


def validate(data, got=None):
    got = replay() if got is None else got
    decision = data["decision"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1796"),
        ("input", data["inputs"] == ["K1791"]),
        ("exact replay", data["enclosure"] == got),
        ("degree eleven", got["degree"] == 11 and got["odd_basis_dimension"] == 5),
        ("fixed cutoff", got["cutoff_q"] == "1/1024"),
        ("25 input leaves", got["input_retained_leaves"] == 25),
        ("complete partition", got["terminal_leaves"] == got["pruned_leaves"] + got["retained_leaves"]),
        ("strict contraction", Fraction(got["excluded_fraction_of_k1791_area"]) == Fraction(63, 80)),
        ("original residual", Fraction(got["retained_fraction_of_original_input_area"]) == Fraction(85, 15104)),
        ("slab split", sum(row["retained_leaves"] for row in got["by_slab"]) == 85),
        ("inversion completed", decision["fixed_cutoff_exact_inversion_completed"]),
        ("contraction admitted", decision["strict_retained_area_contraction"]),
        ("frontier open", not decision["complete_retained_frontier_excluded"]),
        ("retention not membership", not decision["retained_leaf_means_below_threshold"]),
        ("not global", not decision["global_optimizer_proved"]),
    ]


def main():
    got = replay()
    if "--print" in sys.argv:
        print(json.dumps(got, indent=2))
        return
    data = json.loads(ARTIFACT.read_text())
    checks = validate(data, got)
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
