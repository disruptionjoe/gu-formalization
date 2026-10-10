#!/usr/bin/env python3
"""Certificate for K1660 protected admission."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1660-orbit-rigidity-admission.json").read_text())
    q, z = d["admission"], d["decision"]
    checks = [
        ("schema", d["schema_version"] == "1.0"),
        ("claim", d["claim_id"] == "K1660"),
        ("all amplitudes", "Every fixed admissible amplitude" in q["quantum_result"]),
        ("positive gap", "positive Theta(N^4)" in q["quantum_result"]),
        ("remaining class", "unequal mode amplitudes" in q["remaining_quantum_gate"]),
        ("coercivity open", "unrestricted Fisher/negative-defect" in q["remaining_quantum_gate"]),
        ("physical 0/7", "0/7" in q["physical_admission"]),
        ("census", "375 rows" in q["bridge_census"] and "296 satisfied" in q["bridge_census"]),
        ("source assertions", "SC-ACT-01/02/06 remain ASSERTS" in q["protected_state"]),
        ("ledger counts", "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in q["protected_state"]),
        ("scope", "Do not promote" in q["scope_guard"]),
        ("class closed", z["complete_cube_orbit_class_closed"]),
        ("anisotropic open", z["unrestricted_anisotropic_sector_open"]),
        ("source protected", not z["source_status_changed"]),
        ("ledger protected", not z["physics_ledger_changed"]),
        ("public protected", not z["canon_or_public_status_changed"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
