#!/usr/bin/env python3
"""Hostile mutations for K1636's reduction and scope."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accept(d):
    q, z = d["haar_reduction"], d["decision"]
    return ("finite-cutoff reduction" in q["scope_guard"]
            and "finite full energy" in q["setting"]
            and z["phase_removal_nonincreasing"]
            and z["haar_fisher_nonincreasing"]
            and z["wick_potential_preserved"]
            and z["stationary_positive_amplitude_reduction_exact"]
            and not z["infinite_cutoff_minimizer_proved"]
            and not z["source_owned_state"]
            and not z["protected_status_change"])


def main():
    d = json.loads((ROOT / "lab/process/k1636-translation-haar-fisher-reduction.json").read_text())
    checks = [("baseline", accept(d))]
    for label, key, value in [
        ("phase reversal", "phase_removal_nonincreasing", False),
        ("Fisher reversal", "haar_fisher_nonincreasing", False),
        ("potential loss", "wick_potential_preserved", False),
        ("reduction loss", "stationary_positive_amplitude_reduction_exact", False),
        ("continuum overclaim", "infinite_cutoff_minimizer_proved", True),
        ("source overclaim", "source_owned_state", True),
        ("protected mutation", "protected_status_change", True),
    ]:
        m = deepcopy(d); m["decision"][key] = value
        checks.append((label, not accept(m)))
    m = deepcopy(d); m["haar_reduction"]["scope_guard"] = "continuum theorem"
    checks.append(("scope deletion", not accept(m)))
    m = deepcopy(d); m["haar_reduction"]["setting"] = "arbitrary finite-Fisher states"
    checks.append(("energy-domain deletion", not accept(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
