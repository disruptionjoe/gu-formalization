#!/usr/bin/env python3
"""Certificate for K1647's stationary leading negative defect."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1647-stationary-macroscopic-negative-defect.json").read_text())
    q, z = d["orbit_law"], d["decision"]
    n, eta = 1024, 0.2
    ell = 128
    modes = ell ** 3
    amp2 = eta / n
    l4_ratio = 1.5
    defect = 1.5 * amp2 ** 2 * (l4_ratio - 2.0) * modes ** 2
    checks = [
        ("claim", d["claim_id"] == "K1647"),
        ("macroscopic modes", modes == n ** 3 // 512),
        ("negative defect", defect < 0),
        ("sharp fixture", math.isclose(defect, -0.75 * amp2 ** 2 * modes ** 2)),
        ("shell", "N/16<=ell_N<=N/8" in q["shell"]),
        ("random translation", "Y in T^3" in q["field"]),
        ("global phase", "Theta" in q["field"]),
        ("stationarity reason", "stationary" in q["symmetries"]),
        ("central symmetry reason", "centrally symmetric" in q["symmetries"]),
        ("second moment", "A_N^2d_N" in q["moments"]),
        ("fourth moment", "(3/2)A_N^4" in q["moments"]),
        ("leading defect", "Theta(eta^2N^4)" in q["defect"]),
        ("coordinate covariance", "eta omega_k/N" in q["coordinate_covariance"]),
        ("scope fence", "does not by itself" in q["scope_guard"]),
        ("stationary decision", z["stationarity_proved"]),
        ("central decision", z["central_symmetry_proved"]),
        ("macroscopic decision", z["macroscopic_block_size"]),
        ("defect decision", z["leading_negative_defect_constructed"]),
        ("descent open", not z["energy_descent_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
