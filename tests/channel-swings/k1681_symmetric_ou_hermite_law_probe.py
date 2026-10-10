#!/usr/bin/env python3
"""Hostile mutations for K1681."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    c, d = data.get("channel_law", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1681", "bounded, symmetric" in c.get("seed_class", ""),
        "sum_(n>=3)" in c.get("mehler_expansion", ""), "t^2H_3" in c.get("score_expansion", ""),
        "kappa_4(X)^2/6" in c.get("fisher_expansion", ""),
        "t^2 kappa_4(X)" in c.get("cumulant_transport", ""),
        "not a global exact Fisher optimizer" in c.get("scope_guard", ""),
        d.get("mean_and_variance_match_exactly") is True,
        d.get("fisher_leading_coefficient_identified") is True,
        d.get("global_scalar_optimizer_identified") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1681-symmetric-ou-hermite-law.json").read_text())
    mutations = [
        (("claim_id",), "K1680"), (("channel_law", "seed_class"), "unbounded asymmetric"),
        (("channel_law", "mehler_expansion"), "starts at H2"),
        (("channel_law", "score_expansion"), "order t"),
        (("channel_law", "fisher_expansion"), "order t2"),
        (("channel_law", "cumulant_transport"), "linear"),
        (("channel_law", "scope_guard"), "global optimizer"),
        (("decision", "mean_and_variance_match_exactly"), False),
        (("decision", "fisher_leading_coefficient_identified"), False),
        (("decision", "global_scalar_optimizer_identified"), True),
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
