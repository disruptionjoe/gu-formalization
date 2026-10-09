#!/usr/bin/env python3
"""Hostile mutations for K1645's protected closeout."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accept(d):
    a, z = d["admission"], d["decision"]
    c = a["bridge_census"]
    return (c["rows"] == c["satisfied"] + c["conditional"] + c["excluded"] + c["missing"]
            and c["rows"] == 360 and c["satisfied"] == 281
            and a["source_claims"]["SC-META-53"] == "UNCERTAIN"
            and set(a["protected_rows"].values()) == {"0/7"}
            and "No source" in a["scope_guard"]
            and z["conditional_block_coefficient_advance"]
            and z["logarithmic_endpoint_advance"]
            and not z["macroscopic_correlated_endpoint_closed"]
            and not z["source_owned_action_supplied"]
            and not z["physical_admission_complete"]
            and not z["protected_status_change"])


def main():
    d = json.loads((ROOT / "lab/process/k1645-block-cumulant-log-holonomy-admission.json").read_text())
    checks = [("baseline", accept(d))]
    for label, key, value in [
        ("block loss", "conditional_block_coefficient_advance", False),
        ("log loss", "logarithmic_endpoint_advance", False),
        ("macroscopic overclaim", "macroscopic_correlated_endpoint_closed", True),
        ("source overclaim", "source_owned_action_supplied", True),
        ("physical overclaim", "physical_admission_complete", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d); m["decision"][key] = value
        checks.append((label, not accept(m)))
    m = deepcopy(d); m["admission"]["bridge_census"]["satisfied"] += 1
    checks.append(("census mutation", not accept(m)))
    m = deepcopy(d); m["admission"]["source_claims"]["SC-META-53"] = "SETTLED"
    checks.append(("source mutation", not accept(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
