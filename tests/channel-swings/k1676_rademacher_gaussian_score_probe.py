#!/usr/bin/env python3
"""Hostile mutations for K1676."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    c, d = data.get("scalar_channel", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1676", "tanh" in c.get("relative_score", ""),
        "(2/3)t^4" in c.get("fisher", ""), "-2t^2 exactly" in c.get("fourth_cumulant", ""),
        "scalar channel identity" in c.get("scope_guard", ""),
        d.get("mean_and_variance_matched") is True,
        d.get("fisher_starts_at_order_t4") is True,
        d.get("negative_cumulant_starts_at_order_t2") is True,
        d.get("alone_proves_field_descent") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1676-rademacher-gaussian-score.json").read_text())
    mutations = [
        (("claim_id",), "K1675"), (("scalar_channel", "relative_score"), "linear"),
        (("scalar_channel", "fisher"), "order t2"), (("scalar_channel", "fourth_cumulant"), "zero"),
        (("scalar_channel", "scope_guard"), "proves everything"),
        (("decision", "mean_and_variance_matched"), False),
        (("decision", "fisher_starts_at_order_t4"), False),
        (("decision", "negative_cumulant_starts_at_order_t2"), False),
        (("decision", "alone_proves_field_descent"), True),
    ]
    assert valid(source)
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source); cursor = changed
        for key in path[:-1]: cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
