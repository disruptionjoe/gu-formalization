#!/usr/bin/env python3
"""Independent value/zero-set and centered-moment replay for the K232 SOS."""
from fractions import Fraction as F
from itertools import combinations, product
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRIOR = ROOT / "lab/process/k231-order-six-projected-diagonal-jet.json"
MANIFEST = ROOT / "lab/process/k232-order-six-quartic-sos.json"


def normal(x):
    m22 = sum((x[i]**2*x[j]**2 for i, j in combinations(range(6), 2)), F())
    m211 = sum((x[i]**2*x[j]*x[k] for i in range(6)
                for j, k in combinations([t for t in range(6) if t != i], 2)), F())
    m1111 = sum((x[i]*x[j]*x[k]*x[l]
                 for i, j, k, l in combinations(range(6), 4)), F())
    return m22 - m211/2 + m1111


def squares(x):
    return sum(((x[i]-x[j])**2*(x[k]-x[l])**2
                for a, b, c, d in combinations(range(6), 4)
                for (i, j), (k, l) in (((a, b), (c, d)),
                                        ((a, c), (b, d)),
                                        ((a, d), (b, c)))), F())/12


def centered(x):
    mean = sum(x, F())/6
    y = [v-mean for v in x]
    p2 = sum((v**2 for v in y), F())
    p4 = sum((v**4 for v in y), F())
    return (7*p2*p2-10*p4)/8


def main():
    manifest = json.loads(MANIFEST.read_text())
    assert manifest["input_sha256"]["k231"] == sha256(PRIOR.read_bytes()).hexdigest()
    checked = 0
    for values in product((-1, 0, 1), repeat=6):
        x = tuple(map(F, values))
        p = normal(x)
        assert p == squares(x) == centered(x)
        assert p >= 0
        assert (p == 0) == (max((values.count(v) for v in set(values))) >= 5)
        for t in (F(1, 3), F(-2, 7)):
            assert normal(tuple(v+t for v in x)) == p
        checked += 1
    assert checked == manifest["finite_control_count"] == 729
    two = (F(1), F(1), F(0), F(0), F(0), F(0))
    three = (F(1), F(1), F(1), F(0), F(0), F(0))
    assert normal(two) == 1 and normal(three) == F(3, 2)
    prior = json.loads(PRIOR.read_text())
    assert prior["orbit_direction_controls"]["3"]["degree_four_sign"] == 1
    assert manifest["two_to_three_ratio"] == "3/2"
    # A missing squared pairing cannot reproduce the one-outlier zero locus.
    damaged = squares(three) - (three[0]-three[3])**2*(three[1]-three[4])**2/12
    assert damaged != normal(three)
    print("[PASS] K232 independent 729-point centered/SOS/equality and hostile pairing")


if __name__ == "__main__":
    main()
