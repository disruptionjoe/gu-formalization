#!/usr/bin/env python3
"""Hostile mutations for K1649."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accepts(d):
    q, z = d["radial_rigidity"], d["decision"]
    return all([
        "orthogonally invariant" in q["law"], "d(d+2)" in q["exact_cumulant"],
        "Jensen" in q["negative_floor"], "-6" in q["negative_floor"],
        "D_N>=-O(N)" in q["fourier_bound"], "does not control" in q["scope_guard"],
        z["radial_macroscopic_coefficient_rigidity"], not z["all_macroscopic_blocks_controlled"],
        not z["angular_anisotropy_excluded"],
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1649-radial-macroscopic-block-rigidity.json").read_text())
    mutations = [
        ("no invariance", "radial_rigidity", "law", "Arbitrary X."),
        ("wrong sphere moment", "radial_rigidity", "exact_cumulant", "kappa=-2||u||^4"),
        ("no Jensen", "radial_rigidity", "negative_floor", "Assumed floor."),
        ("leading radial defect", "radial_rigidity", "fourier_bound", "D_N=-Theta(N^4)"),
        ("scope erased", "radial_rigidity", "scope_guard", "All laws."),
        ("rigidity false", "decision", "radial_macroscopic_coefficient_rigidity", False),
        ("all blocks overclaim", "decision", "all_macroscopic_blocks_controlled", True),
        ("anisotropy excluded", "decision", "angular_anisotropy_excluded", True),
    ]
    assert accepts(source)
    for i, (label, section, key, value) in enumerate(mutations, 1):
        d = json.loads(json.dumps(source)); d[section][key] = value
        assert not accepts(d), label
        print(f"PASS {i:02d}: rejected {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
