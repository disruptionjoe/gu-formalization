#!/usr/bin/env python3
"""Hostile mutations for K1689."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("envelope", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1689",
        "L_N/d_N" in claim.get("exchangeable_weights", ""),
        "T_N/d_N" in claim.get("exchangeable_weights", ""),
        "sum_j j_(X_j)(t_j)" in claim.get("exact_gap", ""),
        "arithmetic mean" in claim.get("heterogeneity_reduction", ""),
        "h_g^scalar-card-up" in claim.get("widened_functional", ""),
        "h_g^scalar-card-up<=h_g^card-up<h_g^prof" in claim.get("comparison", ""),
        "fixed exchangeable rectangular cardinal block" in claim.get("scope_guard", ""),
        decision.get("heterogeneous_independent_channels_reduced") is True,
        decision.get("scalar_seed_envelope_widened") is True,
        decision.get("strict_global_envelope_improvement_proved") is False,
        decision.get("unrestricted_coefficient_identified") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1689-heterogeneous-cardinal-channel-envelope.json").read_text())
    mutations = [
        (("claim_id",), "K1688"),
        (("envelope", "exchangeable_weights"), "unequal weights"),
        (("envelope", "exact_gap"), "missing Fisher"),
        (("envelope", "heterogeneity_reduction"), "heterogeneity strictly improves"),
        (("envelope", "widened_functional"), "old functional"),
        (("envelope", "comparison"), "strict new global improvement"),
        (("envelope", "scope_guard"), "arbitrary correlated law"),
        (("decision", "heterogeneous_independent_channels_reduced"), False),
        (("decision", "scalar_seed_envelope_widened"), False),
        (("decision", "strict_global_envelope_improvement_proved"), True),
        (("decision", "unrestricted_coefficient_identified"), True),
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
