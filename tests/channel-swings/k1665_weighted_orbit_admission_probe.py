#!/usr/bin/env python3
"""Hostile mutations for K1665."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("admission", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1665",
        "bounded positive amplitude profile" in claim.get("quantum_result", ""),
        "sparse or degenerating profile" in claim.get("remaining_quantum_gate", ""),
        "K1145/K1150 remain 0/7" in claim.get("physical_admission", ""),
        "380 rows" in claim.get("bridge_census", ""),
        "Do not promote" in claim.get("scope_guard", ""),
        decision.get("bounded_profile_orbit_class_closed") is True,
        decision.get("degenerating_and_nonorbit_sectors_open") is True,
        decision.get("source_status_changed") is False,
        decision.get("physics_ledger_changed") is False,
        decision.get("canon_or_public_status_changed") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1665-weighted-orbit-admission.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1660"),
        (("admission", "quantum_result"), "all anisotropic laws"),
        (("admission", "remaining_quantum_gate"), "none"),
        (("admission", "physical_admission"), "physical admission complete"),
        (("admission", "bridge_census"), "all satisfied"),
        (("admission", "scope_guard"), "promote to canon"),
        (("decision", "bounded_profile_orbit_class_closed"), False),
        (("decision", "degenerating_and_nonorbit_sectors_open"), False),
        (("decision", "source_status_changed"), True),
        (("decision", "physics_ledger_changed"), True),
        (("decision", "canon_or_public_status_changed"), True),
        (("admission", "quantum_result"), "unknown profiles covered"),
    ]
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
