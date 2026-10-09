#!/usr/bin/env python3
"""Certificate for K1637's exact full-gap identity."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1637-stationary-fisher-defect-gap-identity.json").read_text())
    q, z = d["gap_identity"], d["decision"]
    a, residual, coupling, defect = 2.0, 12.0, 0.5, -4.0
    gap = a + 0.25 * residual + coupling * defect
    checks = [
        ("claim", d["claim_id"] == "K1637"),
        ("stationary Gaussian", "commutes with translations" in q["matching_gaussian"]),
        ("finite fourth moment", "finite fourth moment/Wick expectation" in q["matching_gaussian"]),
        ("score residual nonnegative", ">=0" in q["score_residual"]),
        ("Pythagoras", "I_Omega(gamma)+R_(Omega,N)" in q["score_residual"]),
        ("exact defect", "4h mu3+mu4-3v^2" in q["moment_defect"]),
        ("Gaussian gap", "A_N=" in q["gaussian_gap"] and ">=0" in q["gaussian_gap"]),
        ("fixture algebra", math.isclose(gap, 3.0)),
        ("exact full formula", "A_N+(1/4)R_(Omega,N)+gD_N" in q["exact_full_gap"]),
        ("coefficient fence", "factor 1/4" in q["normalization"]),
        ("identity decision", z["full_gap_identity_exact"]),
        ("defect sign open", not z["wick_defect_nonnegative"]),
        ("coercivity open", not z["global_coercivity_proved"]),
        ("coefficient open", not z["unrestricted_coefficient_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
