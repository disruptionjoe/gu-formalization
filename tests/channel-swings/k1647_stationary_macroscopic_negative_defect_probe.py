#!/usr/bin/env python3
"""Hostile mutations for K1647."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accepts(d):
    q, z = d["orbit_law"], d["decision"]
    return all([
        "uniform Y" in q["field"], "Theta" in q["field"],
        "stationary" in q["symmetries"], "centrally symmetric" in q["symmetries"],
        "Theta(eta^2N^4)" in q["defect"], "eta omega_k/N" in q["coordinate_covariance"],
        "does not by itself" in q["scope_guard"], z["leading_negative_defect_constructed"],
        not z["energy_descent_proved"],
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1647-stationary-macroscopic-negative-defect.json").read_text())
    mutations = [
        ("no translation", "orbit_law", "field", "Theta only"),
        ("no phase", "orbit_law", "field", "uniform Y only"),
        ("nonstationary", "orbit_law", "symmetries", "No invariance."),
        ("subleading defect", "orbit_law", "defect", "D_N=O(N)."),
        ("wrong covariance", "orbit_law", "coordinate_covariance", "delta s_k=eta."),
        ("scope erased", "orbit_law", "scope_guard", "Global theorem."),
        ("defect false", "decision", "leading_negative_defect_constructed", False),
        ("descent overclaim", "decision", "energy_descent_proved", True),
    ]
    assert accepts(source)
    for i, (label, section, key, value) in enumerate(mutations, 1):
        d = json.loads(json.dumps(source)); d[section][key] = value
        assert not accepts(d), label
        print(f"PASS {i:02d}: rejected {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
