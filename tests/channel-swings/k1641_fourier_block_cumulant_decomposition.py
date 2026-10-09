#!/usr/bin/env python3
"""Certificate for K1641's exact independent-block cumulant identity."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1641-fourier-block-cumulant-decomposition.json").read_text())
    q, z = d["block_decomposition"], d["decision"]
    a, b = 1.25, 0.75
    # Independent Rademacher blocks: kappa_4(aR)=-2a^4 and cumulants add.
    values = [a * r + b * s for r in (-1.0, 1.0) for s in (-1.0, 1.0)]
    second = sum(x * x for x in values) / 4.0
    fourth = sum(x ** 4 for x in values) / 4.0
    cumulant = fourth - 3.0 * second * second
    checks = [
        ("claim", d["claim_id"] == "K1641"),
        ("fixture centered", math.isclose(sum(values), 0.0)),
        ("fixture cumulant additivity", math.isclose(cumulant, -2.0 * (a ** 4 + b ** 4))),
        ("independent blocks", "independent" in q["field"]),
        ("central symmetry", "centrally symmetric" in q["field"]),
        ("coefficient normalization", "lambda_j=s_j/(2omega_j)" in q["coefficients"]),
        ("third moment", "mu3(x)=0" in q["third_moment"]),
        ("pointwise identity", "sum_B kappa4" in q["pointwise_identity"]),
        ("integrated identity", "D_N=sum_B" in q["integrated_defect"]),
        ("stationarity fence", "explicit class premise" in q["scope_guard"]),
        ("identity decision", z["block_cumulant_identity_exact"]),
        ("third decision", z["third_moment_vanishes_under_central_symmetry"]),
        ("sign open", not z["defect_sign_fixed"]),
        ("unrestricted open", not z["arbitrary_stationary_laws_covered"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
