#!/usr/bin/env python3
"""Hostile mutations for K1660."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(d):
    q, z = d.get("admission", {}), d.get("decision", {})
    return all([
        d.get("claim_id") == "K1660",
        "Every fixed admissible amplitude" in q.get("quantum_result", ""),
        "unequal mode amplitudes" in q.get("remaining_quantum_gate", ""),
        "0/7" in q.get("physical_admission", ""),
        "375 rows" in q.get("bridge_census", ""),
        "SC-ACT-01/02/06 remain ASSERTS" in q.get("protected_state", ""),
        "Do not promote" in q.get("scope_guard", ""),
        z.get("complete_cube_orbit_class_closed") is True,
        z.get("unrestricted_anisotropic_sector_open") is True,
        z.get("source_status_changed") is False,
        z.get("physics_ledger_changed") is False,
        z.get("canon_or_public_status_changed") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1660-orbit-rigidity-admission.json").read_text())
    assert valid(source)
    changes = [
        (("claim_id",), "K1659"),
        (("admission", "quantum_result"), "small only"),
        (("admission", "remaining_quantum_gate"), "closed"),
        (("admission", "physical_admission"), "7/7"),
        (("admission", "bridge_census"), "370 rows"),
        (("admission", "protected_state"), "resolved"),
        (("admission", "scope_guard"), "promote"),
        (("decision", "complete_cube_orbit_class_closed"), False),
        (("decision", "unrestricted_anisotropic_sector_open"), False),
        (("decision", "source_status_changed"), True),
        (("decision", "physics_ledger_changed"), True),
        (("decision", "canon_or_public_status_changed"), True),
    ]
    for i, (path, value) in enumerate(changes, 1):
        m = copy.deepcopy(source)
        cur = m
        for key in path[:-1]:
            cur = cur[key]
        cur[path[-1]] = value
        assert not valid(m), i
        print(f"REJECT {i:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(changes)}/{len(changes)}")


if __name__ == "__main__":
    main()
