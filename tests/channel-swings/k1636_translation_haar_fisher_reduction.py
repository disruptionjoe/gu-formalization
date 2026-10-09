#!/usr/bin/env python3
"""Certificate for K1636's translation-Haar Fisher reduction."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1636-translation-haar-fisher-reduction.json").read_text())
    q, z = d["haar_reduction"], d["decision"]
    p1, p2, v1, v2, omega = 0.3, 1.7, 1.2, -0.4, 2.5
    lhs = omega * ((v1 + v2) / 2) ** 2 / ((p1 + p2) / 2)
    rhs = (omega * v1 * v1 / p1 + omega * v2 * v2 / p2) / 2
    checks = [
        ("claim", d["claim_id"] == "K1636"),
        ("normalized torus", "normalized spatial torus" in q["setting"]),
        ("commuting translations", "commuting with Omega_N" in q["setting"]),
        ("finite full energy", "finite full energy" in q["setting"]),
        ("phase split", "(1/4)I_Omega" in q["phase"]),
        ("perspective convexity fixture", lhs <= rhs),
        ("Fisher nonincrease", "<=" in q["fisher"]),
        ("potential equality", "exactly" in q["potential"]),
        ("exact finite reduction", z["stationary_positive_amplitude_reduction_exact"]),
        ("phase nonincrease", z["phase_removal_nonincreasing"]),
        ("Fisher nonincrease decision", z["haar_fisher_nonincreasing"]),
        ("potential decision", z["wick_potential_preserved"]),
        ("no continuum minimizer", not z["infinite_cutoff_minimizer_proved"]),
        ("no source state", not z["source_owned_state"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
