#!/usr/bin/env python3
"""Hostile mutations for K1669."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("survivor_geometry", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1669",
        "B_N=Omega(N^3)" in claim.get("l2_necessity", ""),
        "B_N<=rho_+^2|supp rho|" in claim.get("support_floor", ""),
        "tau^2=b/(2c_1)" in claim.get("threshold_lemma", ""),
        "no such anchor" in claim.get("remaining_geometry", ""),
        "necessary survivor classification" in claim.get("scope_guard", ""),
        decision.get("positive_density_threshold_support_necessary") is True,
        decision.get("extensive_anchor_free_sector_open") is True,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1669-profile-survivor-geometry.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1666"),
        (("survivor_geometry", "l2_necessity"), "B_N=o(N^3) survives"),
        (("survivor_geometry", "support_floor"), "no support bound"),
        (("survivor_geometry", "threshold_lemma"), "tau=0"),
        (("survivor_geometry", "remaining_geometry"), "contains a macroscopic anchor"),
        (("survivor_geometry", "scope_guard"), "existence theorem"),
        (("decision", "positive_density_threshold_support_necessary"), False),
        (("decision", "extensive_anchor_free_sector_open"), False),
        (("decision", "protected_status_change"), True),
        (("survivor_geometry", "remaining_geometry"), "unknown non-orbit laws classified"),
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
