#!/usr/bin/env python3
"""Hostile mutations for K1076."""
from copy import deepcopy
from k1076_k1075_matrix_action_hamiltonian_composition import build, validate


def main():
    mutations = [
        ("canonical_momentum", "p=qdot"), ("generator", "arbitrary"),
        ("pairing", "indefinite"), ("identity", "commutator"),
        ("controls.0.defect_zero", False), ("positivity_boundary", "always positive"),
        ("ownership", "source-owned GU Hessian"), ("claim_ceiling", "all functional actions"),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); node = data; parts = path.split(".")
        for part in parts[:-1]: node = node[int(part)] if part.isdigit() else node[part]
        node[parts[-1]] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1076 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
