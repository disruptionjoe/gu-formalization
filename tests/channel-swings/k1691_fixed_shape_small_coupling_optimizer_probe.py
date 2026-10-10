#!/usr/bin/env python3
"""Hostile mutations for K1691."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    inputs, optimizer = data.get("inputs", {}), data.get("optimizer", {})
    return all([
        data.get("claim_id") == "K1691",
        "q^2/6" in inputs.get("matched_defect_law", ""),
        "A[j_X(q)-rq]" in inputs.get("fixed_shape_objective", ""),
        "Rademacher" in inputs.get("seed_scope", ""),
        optimizer.get("global_small_coupling") is True,
        "diverges" in optimizer.get("coercivity_reason", ""),
        "3r-81c_X r^2" in optimizer.get("branch", ""),
        "432c_X" in optimizer.get("minimum", ""),
        "does not cover moving shapes" in data.get("scope_guard", ""),
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1691-fixed-shape-small-coupling-optimizer.json").read_text())
    mutations = [
        (("claim_id",), "K1690"),
        (("inputs", "matched_defect_law"), "linear"),
        (("inputs", "fixed_shape_objective"), "unknown"),
        (("inputs", "seed_scope"), "all laws"),
        (("optimizer", "global_small_coupling"), False),
        (("optimizer", "coercivity_reason"), "local only"),
        (("optimizer", "branch"), "q=r"),
        (("optimizer", "minimum"), "zero"),
        (("scope_guard",), "global over all shapes"),
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
