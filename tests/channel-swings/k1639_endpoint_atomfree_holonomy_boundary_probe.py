#!/usr/bin/env python3
"""Hostile mutations for K1639's endpoint boundary."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accept(d):
    q, z = d["endpoint_boundary"], d["decision"]
    return ("sufficient, not necessary" in q["scope_guard"]
            and z["compact_ac_bv_counterexample"]
            and z["atom_free_ac_derivative"]
            and z["endpoint_h_half_insufficient"]
            and z["endpoint_besov_type_sufficient"]
            and not z["endpoint_besov_type_necessary"]
            and not z["electric_field_L1_proved"]
            and not z["source_owned_flow"]
            and not z["protected_status_change"])


def main():
    d = json.loads((ROOT / "lab/process/k1639-endpoint-atomfree-holonomy-boundary.json").read_text())
    checks = [("baseline", accept(d))]
    for label, key, value in [
        ("counterexample loss", "compact_ac_bv_counterexample", False),
        ("atom-free loss", "atom_free_ac_derivative", False),
        ("endpoint loss", "endpoint_h_half_insufficient", False),
        ("sufficient loss", "endpoint_besov_type_sufficient", False),
        ("necessity overclaim", "endpoint_besov_type_necessary", True),
        ("electric overclaim", "electric_field_L1_proved", True),
        ("source overclaim", "source_owned_flow", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d); m["decision"][key] = value
        checks.append((label, not accept(m)))
    m = deepcopy(d); m["endpoint_boundary"]["scope_guard"] = "necessary source theorem"
    checks.append(("scope deletion", not accept(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
