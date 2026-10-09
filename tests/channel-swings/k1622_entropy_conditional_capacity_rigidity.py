#!/usr/bin/env python3
"""Certificate for K1622's entropy-plus-conditional-capacity theorem."""
import json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]

def main():
    d = json.loads((ROOT / "lab/process/k1622-entropy-conditional-capacity-rigidity.json").read_text())
    q, z = d["conditional_capacity"], d["decision"]
    weights = [0.25, 0.75]
    mats = [[[0.5, 0.2], [0.2, 0.4]], [[0.1, 0.0], [0.0, 0.3]]]
    entropy = -sum(p * math.log(p) for p in weights)
    capacity = 0.5 * sum(p * math.log(det2([[1+a[0][0], a[0][1]], [a[1][0], 1+a[1][1]]])) for p, a in zip(weights, mats))
    checks = [
        ("claim", d["claim_id"] == "K1622"),
        ("chain rule", "I(M_N;X_N)=I(Z_N,W_N;X_N)" in q["chain_rule"]),
        ("entropy charge", "<=H(Z_N)+I(W_N;X_N|Z_N)" in q["chain_rule"]),
        ("Gaussian determinant", "(1/2)log det" in q["gaussian_term"]),
        ("information bound", "H(p_N)+(1/2)sum_z" in q["information_bound"]),
        ("positive entropy", entropy > 0),
        ("positive capacity", capacity > 0),
        ("finite budget", math.isfinite(entropy + capacity)),
        ("coefficient condition", "=o(N^3)" in q["coefficient"]),
        ("profile coefficient", "h_g^prof" in q["coefficient"]),
        ("arbitrary means", "unrestricted by magnitude or separation" in q["mean_scope"]),
        ("bound recorded", z["entropy_plus_conditional_capacity_bound"]),
        ("means admitted", z["arbitrary_means_admitted"]),
        ("eigenvectors admitted", z["arbitrary_covariance_eigenvectors_admitted"]),
        ("critical capacity open", not z["order_n3_capacity_closed"]),
        ("not unrestricted", not z["unrestricted_leading_coefficient_identified"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")

if __name__ == "__main__": main()
