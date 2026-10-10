#!/usr/bin/env python3
"""Hostile mutations for K1670."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("admission", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1670",
        "subextensive l2 mass" in claim.get("quantum_result", ""),
        "macroscopic positive anchor cube" in claim.get("quantum_result", ""),
        "anchor-free support geometry" in claim.get("remaining_quantum_gate", ""),
        "K1145/K1150 remain 0/7" in claim.get("physical_admission", ""),
        "385 rows" in claim.get("bridge_census", ""),
        "Do not promote" in claim.get("scope_guard", ""),
        decision.get("subextensive_profile_descent_closed") is True,
        decision.get("extensive_anchor_free_sector_open") is True,
        decision.get("source_status_changed") is False,
        decision.get("physics_ledger_changed") is False,
        decision.get("canon_or_public_status_changed") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1670-sparse-anchor-admission.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1665"),
        (("admission", "quantum_result"), "all sparse laws classified"),
        (("admission", "quantum_result"), "no anchor required"),
        (("admission", "remaining_quantum_gate"), "none"),
        (("admission", "physical_admission"), "physical admission complete"),
        (("admission", "bridge_census"), "all satisfied"),
        (("admission", "scope_guard"), "promote to canon"),
        (("decision", "subextensive_profile_descent_closed"), False),
        (("decision", "extensive_anchor_free_sector_open"), False),
        (("decision", "source_status_changed"), True),
        (("decision", "physics_ledger_changed"), True),
        (("decision", "canon_or_public_status_changed"), True),
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
