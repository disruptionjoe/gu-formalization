#!/usr/bin/env python3
"""Hostile mutations for K1072."""
from copy import deepcopy
from k1072_k1071_common_pairing_obstruction import build, validate


def main():
    mutations = [
        ("general_pairing", "diagonal assumed"), ("generator", "w=0"),
        ("defect_formula", "zero"), ("single_generator_solution", "a=c"),
        ("two_generator_theorem", "common identity exists"), ("positive_consequence", "common positive pairing exists"),
        ("controls.0.defect", [["1"]]), ("contrary_boundary", "all pairings forbidden"),
        ("claim_ceiling", "all GU actions"), ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for path, value in mutations:
        data=deepcopy(build()); node=data; parts=path.split(".")
        for part in parts[:-1]: node=node[int(part)] if part.isdigit() else node[part]
        node[parts[-1]]=value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1072 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
