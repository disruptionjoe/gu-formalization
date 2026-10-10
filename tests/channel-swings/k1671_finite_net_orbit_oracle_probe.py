#!/usr/bin/env python3
"""Hostile mutations for K1671."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("oracle", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1671",
        "T^4" in claim.get("channel", ""),
        "C N^11" in claim.get("net", ""),
        "O(log N)" in claim.get("finite_model_risk", ""),
        "posterior mean minimizes" in claim.get("posterior_transfer", ""),
        "aliases and stabilizers" in claim.get("scope_guard", ""),
        decision.get("prediction_risk_logarithmic") is True,
        decision.get("latent_identifiability_required") is False,
        decision.get("support_geometry_required") is False,
        decision.get("unknown_or_growing_latent_classified") is False,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1671-finite-net-orbit-oracle.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1670"),
        (("oracle", "channel"), "unknown infinite-dimensional family"),
        (("oracle", "net"), "exponential net"),
        (("oracle", "finite_model_risk"), "O(N^4)"),
        (("oracle", "posterior_transfer"), "posterior ignored"),
        (("oracle", "scope_guard"), "unique recovery always"),
        (("decision", "prediction_risk_logarithmic"), False),
        (("decision", "latent_identifiability_required"), True),
        (("decision", "unknown_or_growing_latent_classified"), True),
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
