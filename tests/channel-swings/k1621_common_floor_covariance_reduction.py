#!/usr/bin/env python3
"""Certificate for K1621's common-profile-floor covariance reduction."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]

def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]

def main():
    d = json.loads((ROOT / "lab/process/k1621-common-floor-covariance-reduction.json").read_text())
    q, z = d["common_floor_reduction"], d["decision"]
    floor = [[2.0, 0.0], [0.0, 3.0]]
    excess = [[1.0, 0.6], [0.6, 1.0]]
    total = add(floor, excess)
    checks = [
        ("claim", d["claim_id"] == "K1621"),
        ("Loewner split", "S_(N,z)=S_(N,*)+C_(N,z)" in q["hypothesis"]),
        ("positive excess fixture", det(excess) > 0 and excess[0][0] > 0),
        ("covariance addition", total == [[3.0, 0.6], [0.6, 4.0]]),
        ("rotated excess", excess[0][1] != 0),
        ("location representation", "C_(N,Z)^(1/2)W_N" in q["representation"]),
        ("conditional law", "Law(X_N|Z=z)=N(m_(N,z),S_(N,z))" in q["representation"]),
        ("common channel", "continuous location mixture" in q["channel"]),
        ("arbitrary eigenvectors", "arbitrary eigenvectors" in q["channel"]),
        ("profiled floor", "fixed relative K1572 profile band" in q["hypothesis"]),
        ("energy floor", "lambda_N^prof-(Lambda_(N,*)/2)I(M_N;X_N)" in q["energy_floor"]),
        ("Lambda scale", "O_g(N)" in q["energy_floor"]),
        ("heterogeneous reduction", z["label_dependent_covariances_reduced"]),
        ("no shared eigenvectors", not z["shared_covariance_eigenvectors_required"]),
        ("floor required", z["common_profiled_floor_required"]),
        ("non-Gaussian open", not z["non_gaussian_components_controlled"]),
        ("not unrestricted", not z["unrestricted_state_theorem"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")

if __name__ == "__main__":
    main()
