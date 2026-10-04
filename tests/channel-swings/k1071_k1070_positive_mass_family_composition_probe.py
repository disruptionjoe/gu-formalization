#!/usr/bin/env python3
"""Hostile mutations for K1071."""
from copy import deepcopy
from k1071_k1070_positive_mass_family_composition import build, validate


def main():
    mutations = [
        ("parameter_domain", "u=1 only"), ("mode_rule", "omega_squared=u"),
        ("symbolic_pair.M_u", "identity"), ("identity", "checked fixtures only"),
        ("family_result", "mass one selected"), ("structural_rows", []),
        ("controls.0.defect", [[1]]), ("controls.1.quotient_positive", False),
        ("controls.2.radical_invariant", False), ("ownership.repository_candidate_family", False),
        ("ownership.source_selected_coefficient", True), ("ownership.scorable", True),
        ("claim_ceiling", "global GU theorem"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); node = data; parts = path.split(".")
        for part in parts[:-1]: node = node[int(part)] if part.isdigit() else node[part]
        key = parts[-1]
        if key.isdigit(): node[int(key)] = value
        else: node[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1071 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
