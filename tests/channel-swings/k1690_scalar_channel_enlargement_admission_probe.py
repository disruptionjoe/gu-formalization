#!/usr/bin/env python3
"""Hostile mutations for K1690."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("admission", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1690",
        "three-point seed locally beats Rademacher" in claim.get("quantum_result", ""),
        "exact finite-t scalar infimum" in claim.get("remaining_quantum_gate", ""),
        "non-product cumulant tensor" in claim.get("remaining_quantum_gate", ""),
        "K1145/K1150 remain 0/7" in claim.get("physical_admission", ""),
        "405 rows" in claim.get("bridge_census", ""),
        "SC-ACT-01/02/06 remain ASSERTS" in claim.get("protected_state", ""),
        "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in claim.get("protected_state", ""),
        "Do not promote" in claim.get("scope_guard", ""),
        decision.get("scalar_channel_enlargement_integrated") is True,
        decision.get("true_unrestricted_coefficient_open") is True,
        decision.get("source_status_changed") is False,
        decision.get("physics_ledger_changed") is False,
        decision.get("canon_or_public_status_changed") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1690-scalar-channel-enlargement-admission.json").read_text())
    mutations = [
        (("claim_id",), "K1689"),
        (("admission", "quantum_result"), "Rademacher globally optimal"),
        (("admission", "remaining_quantum_gate"), "closed"),
        (("admission", "physical_admission"), "physical theory supplied"),
        (("admission", "bridge_census"), "404 rows"),
        (("admission", "protected_state"), "ledger moved"),
        (("admission", "scope_guard"), "promote"),
        (("decision", "scalar_channel_enlargement_integrated"), False),
        (("decision", "true_unrestricted_coefficient_open"), False),
        (("decision", "source_status_changed"), True),
        (("decision", "physics_ledger_changed"), True),
        (("decision", "canon_or_public_status_changed"), True),
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
