#!/usr/bin/env python3
"""Hostile mutations for K1686."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("identity", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1686",
        "centered unit-variance" in claim.get("channel", ""),
        "sqrt(t)/(1-t)" in claim.get("relative_score", ""),
        "mmse_X(gamma)" in claim.get("fisher_mmse", ""),
        "gamma{1-(1+gamma)" in claim.get("fisher_mmse", ""),
        "mmse_X(gamma)<=1/(1+gamma)" in claim.get("nonnegativity", ""),
        "t^2 kappa_4(X)" in claim.get("cumulant_transport", ""),
        "does not identify" in claim.get("scope_guard", ""),
        decision.get("exact_score_identified") is True,
        decision.get("exact_fisher_mmse_identified") is True,
        decision.get("global_scalar_optimizer_identified") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1686-scalar-fisher-mmse-identity.json").read_text())
    mutations = [
        (("claim_id",), "K1685"),
        (("identity", "channel"), "arbitrary variance"),
        (("identity", "relative_score"), "wrong scale"),
        (("identity", "fisher_mmse"), "Fisher equals MMSE"),
        (("identity", "nonnegativity"), "assumed"),
        (("identity", "cumulant_transport"), "linear transport"),
        (("identity", "scope_guard"), "global optimizer"),
        (("decision", "exact_score_identified"), False),
        (("decision", "exact_fisher_mmse_identified"), False),
        (("decision", "global_scalar_optimizer_identified"), True),
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
