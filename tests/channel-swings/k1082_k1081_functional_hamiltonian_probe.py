#!/usr/bin/env python3
"""Hostile mutations for K1082."""
from copy import deepcopy
from k1082_k1081_functional_hamiltonian import build, validate


def main():
    mutations = [
        ("energy_space", "L2"), ("generator_domain", "H1"), ("generator", "K=H"),
        ("pairing", "indefinite"), ("identity", "no conservation"),
        ("controls", []), ("controls.1.defect", [[1, 0], [0, 0]]),
        ("controls.2.omega_squared", 8), ("positivity", "automatic"),
        ("scope_boundary", "full nonlinear BV domain"), ("ownership", "GU source"),
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
    print(f"K1082 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
