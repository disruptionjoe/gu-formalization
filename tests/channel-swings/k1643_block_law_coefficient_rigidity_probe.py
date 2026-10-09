#!/usr/bin/env python3
"""Hostile mutations for K1643's conditional coefficient theorem."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accept(d):
    q, z = d["coefficient_theorem"], d["decision"]
    return ("finite-Fisher" in q["class"] and "central symmetry" in q["class"]
            and "b_N=o(N^3)" in q["class"] and "fixed g>0" in q["lower_bound"]
            and "does not control one macroscopic" in q["scope_guard"]
            and z["submacroscopic_block_coefficient_proved"]
            and z["independent_mode_boundary_crossed"]
            and not z["macroscopic_endpoint_closed"]
            and not z["unrestricted_coefficient_proved"]
            and not z["protected_status_change"])


def main():
    d = json.loads((ROOT / "lab/process/k1643-block-law-coefficient-rigidity.json").read_text())
    checks = [("baseline", accept(d))]
    for label, key, value in [
        ("coefficient loss", "submacroscopic_block_coefficient_proved", False),
        ("boundary loss", "independent_mode_boundary_crossed", False),
        ("macroscopic overclaim", "macroscopic_endpoint_closed", True),
        ("unrestricted overclaim", "unrestricted_coefficient_proved", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d); m["decision"][key] = value
        checks.append((label, not accept(m)))
    for label, key, value in [
        ("symmetry deletion", "class", "arbitrary stationary laws"),
        ("coupling deletion", "lower_bound", "arbitrary coupling"),
        ("scope deletion", "scope_guard", "unrestricted theorem"),
    ]:
        m = deepcopy(d); m["coefficient_theorem"][key] = value
        checks.append((label, not accept(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
