#!/usr/bin/env python3
"""Data-mutation probe for K1358."""
import copy, json
from pathlib import Path
D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1358-principal-series-charge-generator-domain.json").read_text())

def validate(x):
    s, u, q = x["stone_generator"], x["unboundedness_witness"], x["decision"]; e=[]
    if "self-adjoint" not in s["generator"]: e.append("Stone")
    if "q^2" not in s["operator_domain"]: e.append("domain")
    if "K-finite" not in s["core"]: e.append("core")
    if "4n" not in u["extreme_charges"]: e.append("unbounded witness")
    if not q["charge_generator_self_adjoint"]: e.append("self-adjoint decision")
    if not q["charge_spectrum_unbounded_above"] or not q["charge_spectrum_unbounded_below"]: e.append("two-sided")
    if q["charge_generator_bounded_on_full_H_ps"]: e.append("bounded overclaim")
    if q["operator_domain_equals_full_H_ps"]: e.append("domain overclaim")
    if q["protected_status_change"]: e.append("protected movement")
    return e

assert not validate(D), validate(D)
mutations = [
    ("Stone", lambda x:x["stone_generator"].__setitem__("generator", "symmetric only")),
    ("domain", lambda x:x["stone_generator"].__setitem__("operator_domain", "all H")),
    ("core", lambda x:x["stone_generator"].__setitem__("core", "unknown")),
    ("unbounded witness", lambda x:x["unboundedness_witness"].__setitem__("extreme_charges", "bounded")),
    ("self-adjoint decision", lambda x:x["decision"].__setitem__("charge_generator_self_adjoint", False)),
    ("two-sided", lambda x:x["decision"].__setitem__("charge_spectrum_unbounded_below", False)),
    ("bounded overclaim", lambda x:x["decision"].__setitem__("charge_generator_bounded_on_full_H_ps", True)),
    ("domain overclaim", lambda x:x["decision"].__setitem__("operator_domain_equals_full_H_ps", True)),
    ("protected movement", lambda x:x["decision"].__setitem__("protected_status_change", True)),
]
for i,(label,mutate) in enumerate(mutations,1):
    x=copy.deepcopy(D); mutate(x); errors=validate(x); assert errors,label
    print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 9/9")
