#!/usr/bin/env python3
"""Hostile mutations for K1662."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("localization", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1662",
        "0<rho_-<=rho_(N,k)<=rho_+" in claim.get("profile_hypothesis", ""),
        "1-epsilon" in claim.get("profile_hypothesis", ""),
        "division by sqrt(rho_k)" in claim.get("normalization", ""),
        "O(N^3)" in claim.get("score_saturation", ""),
        "vanishing profile floor" in claim.get("scope_guard", ""),
        decision.get("known_unequal_amplitudes_localized") is True,
        decision.get("degenerating_profiles_classified") is False,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1662-bounded-profile-localization.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1653"),
        (("localization", "profile_hypothesis"), "rho_k may vanish"),
        (("localization", "profile_hypothesis"), "no residual margin"),
        (("localization", "normalization"), "unknown profile"),
        (("localization", "score_saturation"), "O(N^4)"),
        (("localization", "scope_guard"), "all sparse profiles covered"),
        (("decision", "known_unequal_amplitudes_localized"), False),
        (("decision", "degenerating_profiles_classified"), True),
        (("decision", "protected_status_change"), True),
        (("localization", "normalization"), "estimate every amplitude"),
    ]
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
