#!/usr/bin/env python3
"""Hostile mutations for K1634's singular-continuous scope."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def reject(d):
    q, z = d["cantor_class"], d["decision"]
    return (
        "does not prove that every atom-free singular" in q["scope_guard"]
        and z["compact_continuous_BV"]
        and z["derivative_atom_free"]
        and z["derivative_singular_continuous"]
        and z["fractional_Hs_above_half"]
        and z["holonomy_L1"]
        and not z["all_atom_free_singular_measures_closed"]
        and not z["protected_status_change"]
    )


def main():
    d = json.loads((ROOT / "lab/process/k1634-cantor-primitive-singular-sufficiency.json").read_text())
    checks = [("baseline", reject(d))]
    for label, key, value in [
        ("drop compact BV", "compact_continuous_BV", False),
        ("drop atom-free", "derivative_atom_free", False),
        ("drop singular", "derivative_singular_continuous", False),
        ("drop fractional", "fractional_Hs_above_half", False),
        ("drop L1", "holonomy_L1", False),
        ("all-singular overclaim", "all_atom_free_singular_measures_closed", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d)
        m["decision"][key] = value
        checks.append((label, not reject(m)))
    m = deepcopy(d)
    m["cantor_class"]["scope_guard"] = "all atom-free measures"
    checks.append(("scope deletion", not reject(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
