#!/usr/bin/env python3
"""Exact spherical K-type charge decomposition for K1357."""
import hashlib, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1357-spherical-ktype-nonuniform-charge-decomposition.json").read_text())
n = 0
def check(label, value):
    global n
    assert value, label; n += 1; print(f"PASS {n:02d}: {label}")

for key, pin in D["pinned_inputs"].items():
    check(f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"])
S, W, Q = D["spherical_ktype"], D["charge_decomposition"], D["decision"]
vector = [2, -2, 0, 0, 0, 0, 0]
sym = Counter(vector[i] + vector[j] for i in range(7) for j in range(i, 7))
traceless = dict(sym); traceless[0] -= 1
expected = {-4: 1, -2: 5, 0: 15, 2: 5, 4: 1}
check("dimension 27", S["dimension"] == 27)
check("M sign action", "sign changes" in S["M_action"])
check("M fixed dimension", S["M_fixed_dimension"] == 6)
check("multiplicity six", "=6" in S["occurrence"])
check("vector weights", Counter(vector) == Counter({2: 1, -2: 1, 0: 5}))
check("symmetric dimension", sum(sym.values()) == 28)
check("symmetric minus four", sym[-4] == 1)
check("symmetric minus two", sym[-2] == 5)
check("symmetric zero", sym[0] == 16)
check("symmetric plus two", sym[2] == 5)
check("symmetric plus four", sym[4] == 1)
check("trace removal", traceless[0] == 15)
check("tracefree decomposition", traceless == expected)
check("tracefree dimension", sum(traceless.values()) == 27)
check("five distinct charges", len(traceless) == 5)
check("spherical occurrence", Q["M_spherical_K_type_occurs_in_H_ps"])
check("nonuniform decision", Q["charge_decomposition_is_nonuniform"])
check("source field not identified", not Q["released_source_field_identified_with_V"])
check("protected fixed", not Q["protected_status_change"])
assert n == 21
print("RESULT: PASS 21/21")
