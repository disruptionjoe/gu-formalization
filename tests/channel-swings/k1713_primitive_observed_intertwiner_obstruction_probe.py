#!/usr/bin/env python3
"""Hostile semantic mutations for K1713."""
import copy
import json
from pathlib import Path

D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1713-primitive-observed-intertwiner-obstruction.json").read_text())


def errors(x):
    b, q = x.get("intertwiner_obstruction", {}), x.get("decision", {})
    out = []
    for key, needle in (("target_support", "only even integer weights"), ("automorphisms", "plus_or_minus one"), ("weight_space_law", "target weight plus_or_minus r"), ("obstruction", "odd source weight maps to zero"), ("scope", "effective quotient")):
        if needle not in b.get(key, ""):
            out.append(key)
    for key in ("fixed_ktype_exclusion_extends_to_full_H_ps", "original_circle_automorphism_preserves_parity", "effective_quotient_escape_remains_open"):
        if not q.get(key):
            out.append(key)
    for key in ("faithful_primitive_linear_intertwiner_to_full_H_ps_exists", "all_observation_maps_excluded", "source_hypercharge_falsified", "protected_status_change"):
        if q.get(key):
            out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("target parity", lambda x: x["intertwiner_obstruction"].__setitem__("target_support", "all weights")),
        ("automorphism", lambda x: x["intertwiner_obstruction"].__setitem__("automorphisms", "degree two")),
        ("weight law", lambda x: x["intertwiner_obstruction"].__setitem__("weight_space_law", "untyped")),
        ("obstruction", lambda x: x["intertwiner_obstruction"].__setitem__("obstruction", "none")),
        ("scope", lambda x: x["intertwiner_obstruction"].__setitem__("scope", "all maps excluded")),
        ("full extension", lambda x: x["decision"].__setitem__("fixed_ktype_exclusion_extends_to_full_H_ps", False)),
        ("parity", lambda x: x["decision"].__setitem__("original_circle_automorphism_preserves_parity", False)),
        ("intertwiner overclaim", lambda x: x["decision"].__setitem__("faithful_primitive_linear_intertwiner_to_full_H_ps_exists", True)),
        ("quotient erased", lambda x: x["decision"].__setitem__("effective_quotient_escape_remains_open", False)),
        ("global no-go", lambda x: x["decision"].__setitem__("all_observation_maps_excluded", True)),
        ("source kill", lambda x: x["decision"].__setitem__("source_hypercharge_falsified", True)),
        ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D)
        mutate(x)
        assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
