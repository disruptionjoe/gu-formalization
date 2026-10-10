#!/usr/bin/env python3
"""Hostile mutations for K1694."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    witness, conclusion = data.get("witness", {}), data.get("conclusion", {})
    return all([
        data.get("claim_id") == "K1694",
        "nonzero" in witness.get("active_coordinate_cumulant", ""),
        "sum_j v_j^4<1" in witness.get("mixing_row", ""),
        "differs" in witness.get("transformed_cumulant", ""),
        witness.get("noninvariance") is True,
        conclusion.get("strict_finite_cutoff_fisher_saving") is True,
        conclusion.get("covariance_preserved") is True,
        conclusion.get("integrated_wick_defect_preserved") is True,
        conclusion.get("order_N4_saving_proved") is False,
        "does not determine its leading scale" in data.get("scope_guard", ""),
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1694-translation-haar-strictness-boundary.json").read_text())
    mutations = [
        (("claim_id",), "K1693"),
        (("witness", "active_coordinate_cumulant"), "zero"),
        (("witness", "mixing_row"), "permutation"),
        (("witness", "transformed_cumulant"), "equal"),
        (("witness", "noninvariance"), False),
        (("conclusion", "strict_finite_cutoff_fisher_saving"), False),
        (("conclusion", "covariance_preserved"), False),
        (("conclusion", "integrated_wick_defect_preserved"), False),
        (("conclusion", "order_N4_saving_proved"), True),
        (("scope_guard",), "leading coefficient proved"),
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
