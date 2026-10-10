#!/usr/bin/env python3
"""Hostile mutations for K1688."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("comparison", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1688",
        "p_*=(15+sqrt(105))/60" in claim.get("three_point_seed", ""),
        "kappa_6(X_*)=0" in claim.get("three_point_cumulants", ""),
        "(1/4)q^3" in claim.get("three_point_law", ""),
        "(31/60)q^3" in claim.get("rademacher_law", ""),
        "(4/15)q^3" in claim.get("strict_local_order", ""),
        "pointwise weak-channel" in claim.get("scope_guard", ""),
        "neither proves a global" in claim.get("scope_guard", ""),
        decision.get("sixth_cumulant_canceled") is True,
        decision.get("rademacher_local_scalar_optimality_false") is True,
        decision.get("k1682_fixed_t_extremality_preserved") is True,
        decision.get("global_scalar_optimizer_identified") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1688-three-point-channel-dominance.json").read_text())
    mutations = [
        (("claim_id",), "K1687"),
        (("comparison", "three_point_seed"), "wrong seed"),
        (("comparison", "three_point_cumulants"), "nonzero kappa6"),
        (("comparison", "three_point_law"), "wrong coefficient"),
        (("comparison", "rademacher_law"), "wrong coefficient"),
        (("comparison", "strict_local_order"), "no strict order"),
        (("comparison", "scope_guard"), "global optimum"),
        (("decision", "sixth_cumulant_canceled"), False),
        (("decision", "rademacher_local_scalar_optimality_false"), False),
        (("decision", "k1682_fixed_t_extremality_preserved"), False),
        (("decision", "global_scalar_optimizer_identified"), True),
    ]
    assert valid(source)
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source)
        cursor = changed
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
