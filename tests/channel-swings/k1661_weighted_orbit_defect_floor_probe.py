#!/usr/bin/env python3
"""Hostile mutations for K1661."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("weighted_floor", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1661",
        "positive weights" in claim.get("profile", ""),
        "int|R_N|^4>=0" in claim.get("floor", ""),
        "d_N sum rho_k^2" in claim.get("l2_conversion", ""),
        "not an equality" in claim.get("scope_guard", ""),
        decision.get("weighted_defect_floor_proved") is True,
        decision.get("l1_to_l2_conversion_proved") is True,
        decision.get("unrestricted_defect_formula_proved") is False,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1661-weighted-orbit-defect-floor.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1657"),
        (("weighted_floor", "profile"), "signed arbitrary weights"),
        (("weighted_floor", "floor"), "no nonnegative moment"),
        (("weighted_floor", "l2_conversion"), "l1 equals l2"),
        (("weighted_floor", "scope_guard"), "exact unrestricted formula"),
        (("decision", "weighted_defect_floor_proved"), False),
        (("decision", "l1_to_l2_conversion_proved"), False),
        (("decision", "unrestricted_defect_formula_proved"), True),
        (("decision", "protected_status_change"), True),
        (("weighted_floor", "profile"), "equal magnitudes only"),
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
