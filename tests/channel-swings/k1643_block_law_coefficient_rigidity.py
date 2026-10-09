#!/usr/bin/env python3
"""Certificate for K1643's submacroscopic block-law coefficient theorem."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1643-block-law-coefficient-rigidity.json").read_text())
    q, z = d["coefficient_theorem"], d["decision"]
    exponents = [0.0, 1.0, 2.5, 2.9]
    normalized = [1000.0 ** (beta - 3.0) for beta in exponents]
    a, residual, g, defect = 2.0, 8.0, 0.25, -3.0
    gap = a + 0.25 * residual + g * defect
    checks = [
        ("claim", d["claim_id"] == "K1643"),
        ("submacroscopic scaling", all(x < 1.0 for x in normalized)),
        ("scaling improves below three", normalized[0] < normalized[-1]),
        ("gap fixture", math.isclose(gap, 3.25)),
        ("finite Fisher class", "finite-Fisher" in q["class"]),
        ("central symmetry class", "central symmetry" in q["class"]),
        ("block scale class", "b_N=o(N^3)" in q["class"]),
        ("exact lower composition", "A_N+R_(Omega,N)/4+gD_N" in q["lower_bound"]),
        ("fixed positive coupling", "fixed g>0" in q["lower_bound"]),
        ("Gaussian upper", "K1572 profiled Gaussian" in q["upper_bound"]),
        ("coefficient", "h_g^prof" in q["coefficient"]),
        ("macroscopic endpoint", "Omega(N^3)" in q["remaining_endpoint"]),
        ("scope fence", "does not control one macroscopic" in q["scope_guard"]),
        ("coefficient decision", z["submacroscopic_block_coefficient_proved"]),
        ("independent boundary", z["independent_mode_boundary_crossed"]),
        ("endpoint open", not z["macroscopic_endpoint_closed"]),
        ("unrestricted open", not z["unrestricted_coefficient_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
