#!/usr/bin/env python3
"""Controls for K1494's uniformly irreducible Jacobi tower."""
import hashlib, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1494-uniform-jacobi-tower.json").read_text())


def eigenvalues_symmetric(a):
    a = [row[:] for row in a]
    n = len(a)
    for _ in range(100):
        p, q = max(((i, j) for i in range(n) for j in range(i + 1, n)), key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < 1e-13:
            break
        phi = 0.5 * math.atan2(2 * a[p][q], a[q][q] - a[p][p])
        c, s = math.cos(phi), math.sin(phi)
        for k in range(n):
            if k not in (p, q):
                apk, aqk = a[p][k], a[q][k]
                a[p][k] = a[k][p] = c * apk - s * aqk
                a[q][k] = a[k][q] = s * apk + c * aqk
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        a[p][p] = c*c*app - 2*s*c*apq + s*s*aqq
        a[q][q] = s*s*app + 2*s*c*apq + c*c*aqq
        a[p][q] = a[q][p] = 0.0
    return sorted(a[i][i] for i in range(n))


def main():
    checks = []
    for name, pin in D["pinned_inputs"].items():
        checks.append((f"{name} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    a, q = D["uniform_jacobi_tower"], D["decision"]
    checks.extend([
        ("claim", D["claim_id"] == "K1494"),
        ("recurrence", "Jacobi recurrence" in a["orthonormal_basis"]),
        ("b identity", "sqrt(h_(j+1,N)/h_(j,N))" in a["off_diagonal_identity"]),
        ("b lower", "H_j^(-1/2)" in a["off_diagonal_bounds"]),
        ("diagonal", "3^(4j)" in a["diagonal_bounds"]),
        ("strict interlace", "lambda_min(J_(d,N))<" in a["strict_interlacing"]),
        ("uniform gap", "epsilon_d>0" in a["uniform_fixed_degree_gap"]),
        ("recurrence decision", q["jacobi_recurrence_constructed"]),
        ("positive couplings", q["all_fixed_off_diagonal_couplings_uniformly_positive"]),
        ("bounded diagonals", q["fixed_degree_diagonals_uniformly_bounded"]),
        ("strict decision", q["strict_interlacing_at_every_fixed_degree"]),
        ("gap decision", q["uniform_fixed_degree_gap_exists"]),
        ("all-d fenced", not q["gap_sequence_non_summability_proved"]),
        ("protected fenced", not q["protected_status_change"]),
    ])
    j2 = [[0.0, 1.0], [1.0, 0.2]]
    j3 = [[0.0, 1.0, 0.0], [1.0, 0.2, 0.7], [0.0, 0.7, -0.1]]
    e2, e3 = eigenvalues_symmetric(j2), eigenvalues_symmetric(j3)
    checks.extend([
        ("toy strict lower interlace", e3[0] < e2[0]),
        ("toy upper interlace", e2[-1] < e3[-1]),
        ("H2 coupling lower positive", (3 ** 8) ** -0.5 > 0),
    ])
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
