#!/usr/bin/env python3
"""Hostile mutations for K1696."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    factor, uniform = data.get("factorization", {}), data.get("uniform_expansion", {})
    return all([
        data.get("claim_id") == "K1696",
        "Phi_X(r)=min" in factor.get("profile", ""),
        "tau_g(C)/4" in factor.get("shape_objective", ""),
        "Rademacher" in factor.get("seed_scope", ""),
        "unique global minimizer" in factor.get("global_branch", ""),
        "-(3/2)r^2" in uniform.get("legendre", ""),
        "ell_g^2/tau_g" in uniform.get("shape_ratios", ""),
        "432c_Xg^3S_g(C)" in uniform.get("objective", ""),
        "O(g) uniformly" in uniform.get("reason", ""),
        "does not classify every seed" in data.get("scope_guard", ""),
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1696-uniform-scalar-legendre-profile.json").read_text())
    mutations = [
        (("claim_id",), "K1695"),
        (("factorization", "profile"), "unknown"),
        (("factorization", "shape_objective"), "unfactored"),
        (("factorization", "seed_scope"), "all seeds"),
        (("factorization", "global_branch"), "local only"),
        (("uniform_expansion", "legendre"), "linear"),
        (("uniform_expansion", "shape_ratios"), "none"),
        (("uniform_expansion", "objective"), "fixed shape only"),
        (("uniform_expansion", "reason"), "unbounded"),
        (("scope_guard",), "finite strength solved"),
    ]
    assert valid(source)
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source)
        cursor = changed
        for key in path[:-1]: cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
