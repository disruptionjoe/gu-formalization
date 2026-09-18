#!/usr/bin/env python3
"""K232: exact six-variable polynomial certificate for the K231 quartic."""
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRIOR = ROOT / "lab/process/k231-order-six-projected-diagonal-jet.json"
MANIFEST = ROOT / "lab/process/k232-order-six-quartic-sos.json"
ZERO = (0,) * 6


def term(indices):
    exponents = [0] * 6
    for i in indices:
        exponents[i] += 1
    return tuple(exponents)


def mul(left, right):
    output = defaultdict(F)
    for a, va in left.items():
        for b, vb in right.items():
            output[tuple(x+y for x, y in zip(a, b))] += va*vb
    return {key: value for key, value in output.items() if value}


def difference(i, j):
    return {term((i,)): F(1), term((j,)): F(-1)}


def polynomials():
    normal = defaultdict(F)
    for i, j in combinations(range(6), 2):
        normal[term((i, i, j, j))] += 1
    for i in range(6):
        for j, k in combinations((x for x in range(6) if x != i), 2):
            normal[term((i, i, j, k))] -= F(1, 2)
    for subset in combinations(range(6), 4):
        normal[term(subset)] += 1
    sos = defaultdict(F)
    count = 0
    for a, b, c, d in combinations(range(6), 4):
        for (i, j), (k, l) in (((a, b), (c, d)),
                                  ((a, c), (b, d)),
                                  ((a, d), (b, c))):
            square = mul(mul(difference(i, j), difference(i, j)),
                         mul(difference(k, l), difference(k, l)))
            for key, value in square.items():
                sos[key] += value / 12
            count += 1
    return dict(normal), {k: v for k, v in sos.items() if v}, count


def main():
    prior = json.loads(PRIOR.read_text())
    manifest = json.loads(MANIFEST.read_text())
    assert sha256(PRIOR.read_bytes()).hexdigest() == manifest["input_sha256"]["k231"]
    normal, sos, count = polynomials()
    assert normal == sos and count == 45 and len(normal) == 90
    assert manifest["square_count"] == count
    assert manifest["monomial_count"] == len(normal)
    assert prior["orbit_direction_controls"]["2"]["degree_four_sign"] == 1
    assert prior["orbit_direction_controls"]["3"]["degree_four_sign"] == 1
    print("[PASS] K232 exact 90-monomial SOS identity and K231 positive finite A control")


if __name__ == "__main__":
    main()
