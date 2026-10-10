#!/usr/bin/env python3
"""Hostile mutations for K1667."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("localization", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1667",
        "complete lattice subcube Q_N" in claim.get("anchor_hypothesis", ""),
        "rho_(N,k)>=rho_->0" in claim.get("anchor_hypothesis", ""),
        "division by sqrt(rho_k)" in claim.get("normalization", ""),
        "O(N^3)" in claim.get("score_saturation", ""),
        "anchor-free" in claim.get("scope_guard", ""),
        decision.get("macroscopic_anchor_localizes") is True,
        decision.get("arbitrary_dense_support_classified") is False,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1667-anchor-cube-localization.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1662"),
        (("localization", "anchor_hypothesis"), "positive-density set"),
        (("localization", "anchor_hypothesis"), "rho may vanish on anchor"),
        (("localization", "normalization"), "unknown profile"),
        (("localization", "score_saturation"), "O(N^4)"),
        (("localization", "scope_guard"), "all dense supports covered"),
        (("decision", "macroscopic_anchor_localizes"), False),
        (("decision", "arbitrary_dense_support_classified"), True),
        (("decision", "protected_status_change"), True),
        (("localization", "anchor_hypothesis"), "one isolated mode"),
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
