#!/usr/bin/env python3
"""Hostile mutations for K1672."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("localization", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1672",
        "O(log N)" in claim.get("prediction_metric", ""),
        "O(N)" in claim.get("score_weight", ""),
        "O(N log N)" in claim.get("missing_fisher", ""),
        "anchor-free" in claim.get("support_scope", ""),
        "Known coefficients" in claim.get("scope_guard", ""),
        decision.get("anchor_free_profiles_localized_in_prediction") is True,
        decision.get("anchor_cube_required") is False,
        decision.get("unique_parameter_recovery_claimed") is False,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1672-anchor-free-score-localization.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1671"),
        (("localization", "prediction_metric"), "O(N^3)"),
        (("localization", "score_weight"), "O(N^4)"),
        (("localization", "missing_fisher"), "O(N^4)"),
        (("localization", "support_scope"), "anchor cube only"),
        (("localization", "scope_guard"), "unknown coefficients allowed"),
        (("decision", "anchor_free_profiles_localized_in_prediction"), False),
        (("decision", "anchor_cube_required"), True),
        (("decision", "unique_parameter_recovery_claimed"), True),
        (("decision", "protected_status_change"), True),
    ]
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source)
        cursor = changed
        for key in path[:-1]: cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
