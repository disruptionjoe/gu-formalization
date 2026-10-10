#!/usr/bin/env python3
"""Hostile mutations for K1678."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    c, d = data.get("composition", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1678", "exactly S_(g,N)" in c.get("covariance", ""),
        "(j(t)/4)T_N" in c.get("fisher", ""), "D_N=-2t^2L_N exactly" in c.get("defect", ""),
        "-2g t^2L_N" in c.get("gap_identity", ""), d.get("exact_covariance_match") is True,
        d.get("bregman_term_zero") is True, d.get("weighted_fisher_order_n4_times_j") is True,
        d.get("negative_defect_order_n4_times_t2") is True,
        d.get("stationarity_before_averaging") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1678-product-block-fisher-defect.json").read_text())
    mutations = [
        (("claim_id",), "K1677"), (("composition", "covariance"), "approximate"),
        (("composition", "fisher"), "unknown"), (("composition", "defect"), "bounded"),
        (("composition", "gap_identity"), "positive only"), (("decision", "exact_covariance_match"), False),
        (("decision", "bregman_term_zero"), False), (("decision", "weighted_fisher_order_n4_times_j"), False),
        (("decision", "negative_defect_order_n4_times_t2"), False),
        (("decision", "stationarity_before_averaging"), True),
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
