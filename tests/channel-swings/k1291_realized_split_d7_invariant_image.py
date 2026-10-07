#!/usr/bin/env python3
"""Exact controls for K1291's realized split-D7 invariant image."""
import hashlib, json
from itertools import combinations
from math import prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1291-realized-split-d7-invariant-image.json").read_text())

def elementary(values, k):
    return sum(prod(c) for c in combinations(values, k))

def poly(coeffs, t):
    value = 0
    for coefficient in coeffs:
        value = value * t + coefficient
    return value

n = 0
def check(label, value):
    global n
    assert value, label
    n += 1
    print(f"PASS {n:02d}: {label}")

pin = D["pinned_inputs"]["k1269"]
check("pinned K1269", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"])
x = (1, 2, 3, 4, 5, 6, 7)
z = tuple(v * v for v in x)
e = tuple(elementary(z, k) for k in range(1, 8))
p = prod(x)
coefficients = (1, -e[0], e[1], -e[2], e[3], -e[4], e[5], -(p * p))
check("constant term is minus p squared", e[6] == p * p)
check("all seven squared coordinates are roots", all(poly(coefficients, root) == 0 for root in z))
check("sample roots are nonnegative", all(root >= 0 for root in z))
check("sample roots counted seven", len(z) == 7)
check("invariant map formula", "e1(z)" in D["theorem"]["invariant_map"])
check("root image criterion", "seven nonnegative real roots" in D["theorem"]["image_iff"])
check("reconstruction specifies product sign", "product_i x_i=I7" in D["theorem"]["reconstruction"])
check("complete connected Weyl invariant", D["theorem"]["complete_connected_weyl_orbit_invariant"])
check("zero-product sign rule retained", "zero coordinate" in D["theorem"]["zero_product_sign_rule"])
check("formal base is larger", not D["theorem"]["ambient_formal_base_equals_realized_image"])
check("arbitrary formal target rejected", not D["decision"]["arbitrary_formal_target_is_realized"])
check("source target not selected", not D["decision"]["source_target_selected"])
check("functional phase space absent", not D["decision"]["functional_phase_space_constructed"])
assert n == 14
print("RESULT: PASS 14/14")
