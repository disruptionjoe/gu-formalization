#!/usr/bin/env python3
"""Hostile mutations for K1621's common-floor and Gaussian scope."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def reject(d):
    q, z = d["common_floor_reduction"], d["decision"]
    return (
        "common stationary diagonal profiled Loewner floor is load-bearing" in q["scope_guard"]
        and z["label_dependent_covariances_reduced"]
        and not z["shared_covariance_eigenvectors_required"]
        and z["common_profiled_floor_required"]
        and not z["non_gaussian_components_controlled"]
        and not z["unrestricted_state_theorem"]
        and not z["protected_status_change"]
    )

def main():
    d = json.loads((ROOT / "lab/process/k1621-common-floor-covariance-reduction.json").read_text())
    checks = [("baseline", reject(d))]
    m = deepcopy(d); m["common_floor_reduction"]["scope_guard"] = m["common_floor_reduction"]["scope_guard"].replace("is load-bearing", "is optional")
    checks.append(("drop floor", not reject(m)))
    for key in ("label_dependent_covariances_reduced", "shared_covariance_eigenvectors_required", "common_profiled_floor_required", "non_gaussian_components_controlled", "unrestricted_state_theorem", "protected_status_change"):
        m = deepcopy(d); m["decision"][key] = not m["decision"][key]
        checks.append((f"flip {key}", not reject(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")

if __name__ == "__main__": main()
