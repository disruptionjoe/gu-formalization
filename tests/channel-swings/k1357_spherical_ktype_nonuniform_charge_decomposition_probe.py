#!/usr/bin/env python3
"""Data-mutation probe for K1357."""
import copy, json
from pathlib import Path
D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1357-spherical-ktype-nonuniform-charge-decomposition.json").read_text())

def validate(x):
    s, w, q = x["spherical_ktype"], x["charge_decomposition"], x["decision"]; e = []
    if s["dimension"] != 27: e.append("dimension")
    if s["M_fixed_dimension"] != 6: e.append("M fixed")
    if "=6" not in s["occurrence"]: e.append("occurrence")
    if w["trace_free_weights"] != {"minus_4":1,"minus_2":5,"zero":15,"plus_2":5,"plus_4":1}: e.append("weights")
    if q["charge_set"] != [-4,-2,0,2,4]: e.append("charge set")
    if not q["M_spherical_K_type_occurs_in_H_ps"]: e.append("spherical")
    if not q["charge_decomposition_is_nonuniform"]: e.append("nonuniform")
    if q["single_nonzero_charge_sector_preserves_full_G"]: e.append("full G overclaim")
    if q["released_source_field_identified_with_V"]: e.append("source overclaim")
    if q["protected_status_change"]: e.append("protected movement")
    return e

assert not validate(D), validate(D)
mutations = [
    ("dimension", lambda x: x["spherical_ktype"].__setitem__("dimension", 28)),
    ("M fixed", lambda x: x["spherical_ktype"].__setitem__("M_fixed_dimension", 7)),
    ("occurrence", lambda x: x["spherical_ktype"].__setitem__("occurrence", "unknown")),
    ("weights", lambda x: x["charge_decomposition"]["trace_free_weights"].__setitem__("zero", 16)),
    ("charge set", lambda x: x["decision"].__setitem__("charge_set", [-2,0,2])),
    ("spherical", lambda x: x["decision"].__setitem__("M_spherical_K_type_occurs_in_H_ps", False)),
    ("nonuniform", lambda x: x["decision"].__setitem__("charge_decomposition_is_nonuniform", False)),
    ("full G overclaim", lambda x: x["decision"].__setitem__("single_nonzero_charge_sector_preserves_full_G", True)),
    ("source overclaim", lambda x: x["decision"].__setitem__("released_source_field_identified_with_V", True)),
    ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
]
for i, (label, mutate) in enumerate(mutations, 1):
    x = copy.deepcopy(D); mutate(x); errors = validate(x); assert errors, label
    print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
