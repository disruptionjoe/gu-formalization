#!/usr/bin/env python3
"""Hostile mutations for K1644's logarithmic endpoint."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accept(d):
    q, z = d["logarithmic_endpoint"], d["decision"]
    return ("1/[n log^2 n]" in q["critical_failure"]
            and "1/[n log n]" in q["critical_failure"]
            and "every epsilon>0" in q["supercritical_sufficiency"]
            and "not a necessary characterization" in q["scope_guard"]
            and z["compact_ac_bv_counterexample"]
            and z["atom_free_ac_derivative"]
            and z["critical_log_endpoint_insufficient"]
            and z["every_supercritical_log_power_sufficient"]
            and not z["necessary_characterization"]
            and not z["source_owned_flow"]
            and not z["protected_status_change"])


def main():
    d = json.loads((ROOT / "lab/process/k1644-logarithmic-holonomy-endpoint.json").read_text())
    checks = [("baseline", accept(d))]
    for label, key, value in [
        ("counterexample loss", "compact_ac_bv_counterexample", False),
        ("atom loss", "atom_free_ac_derivative", False),
        ("endpoint loss", "critical_log_endpoint_insufficient", False),
        ("sufficiency loss", "every_supercritical_log_power_sufficient", False),
        ("necessity overclaim", "necessary_characterization", True),
        ("source overclaim", "source_owned_flow", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d); m["decision"][key] = value
        checks.append((label, not accept(m)))
    m = deepcopy(d); m["logarithmic_endpoint"]["scope_guard"] = "necessary and sufficient source theorem"
    checks.append(("scope deletion", not accept(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
