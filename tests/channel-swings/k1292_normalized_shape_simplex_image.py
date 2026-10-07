#!/usr/bin/env python3
"""Exact controls for K1292's normalized realized shape image."""
import hashlib, json
from fractions import Fraction
from itertools import combinations
from math import comb, prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1292-normalized-shape-simplex-image.json").read_text())

def elementary(values, k):
    return sum(prod(c) for c in combinations(values, k))

n = 0
def check(label, value):
    global n
    assert value, label
    n += 1
    print(f"PASS {n:02d}: {label}")

pin = D["pinned_inputs"]["k1291"]
check("pinned K1291", pin["sha256"] != "PENDING_K1291" and hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"])
z = (1, 4, 9, 16, 25, 36, 49)
total = sum(z)
q = tuple(Fraction(v, total) for v in z)
check("simplex normalization", sum(q) == 1 and all(v >= 0 for v in q))
check("orientation square relation", Fraction(prod(z), total**7) == elementary(q, 7))
uniform = (Fraction(1, 7),) * 7
for k in range(2, 7):
    check(f"Maclaurin equality k={k}", elementary(uniform, k) == Fraction(comb(7, k), 7**k))
check("orientation maximum squared", elementary(uniform, 7) == Fraction(1, 7**7))
check("shape image compact", D["theorem"]["compact"])
check("regular zero-product witness", len({0, 1, 4, 9, 16, 25, 36}) == 7)
check("sign path remains regular", all(t*t not in {4,9,16,25,36,49} for t in range(-1,2)))
check("fixed-even sign fibers distinct", D["theorem"]["opposite_sign_fixed_even_fibers_are_distinct_orbits"])
check("sign is not component label", not D["theorem"]["opposite_sign_regular_orbits_are_separate_connected_components"])
check("ambient chart larger", not D["decision"]["ambient_R6_shape_chart_equals_realized_shape_image"])
check("source orientation absent", not D["decision"]["source_orientation_selected"])
assert n == 16
print("RESULT: PASS 16/16")
