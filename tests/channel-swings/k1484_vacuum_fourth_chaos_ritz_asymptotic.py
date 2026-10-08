#!/usr/bin/env python3
"""Controls for K1484's exact two-dimensional Ritz asymptotic."""
import hashlib, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1484-vacuum-fourth-chaos-ritz-asymptotic.json").read_text())


def validate(d):
    a, q = d["ritz_asymptotic"], d["decision"]
    return [
        d["claim_id"] == "K1484",
        "e0=1 and e1=V_N/sigma_N" in a["basis"],
        "[[0,g sigma_N],[g sigma_N,d_N]]" in a["centered_matrix"],
        "d_N=O(N)" in a["diagonal_order"],
        "sqrt(d_N^2+4g^2 sigma_N^2)" in a["lower_eigenvalue"],
        "lambda_N^-=-g sigma_N+O(N)" in a["leading_order"],
        "E_N<=6gC_N^2-g sigma_N+O(N)" in a["ground_energy_upper"],
        "alpha_N->1/sqrt(2)" in a["eigenvector"],
        "nonzero vacuum vector" in a["weak_limit"],
        q["exact_two_by_two_compression_constructed"],
        q["ritz_lower_eigenvalue_ratio_limit"] == -1,
        q["ground_energy_upper_leading_correction"] == "-g sigma_N",
        q["ritz_eigenvector_has_nonzero_weak_vacuum_limit"],
        not q["matching_ground_energy_lower_bound_proved"],
        not q["ground_energy_asymptotic_determined"],
        not q["ground_energy_recentered_limit_constructed"],
        not q["protected_status_change"],
    ]


def main():
    checks = []
    for name, pin in D["pinned_inputs"].items():
        checks.append((f"{name} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    checks.extend((f"serialized invariant {i}", ok) for i, ok in enumerate(validate(D), 1))
    g = 0.3; ratios = []
    for n in (8, 16, 32, 64, 128):
        sigma = n ** 2.5; diagonal = 3 * n
        lam = (diagonal - math.sqrt(diagonal * diagonal + 4 * g * g * sigma * sigma)) / 2
        ratio = lam / (g * sigma); ratios.append(ratio)
        beta_over_alpha = lam / (g * sigma)
        alpha = 1 / math.sqrt(1 + beta_over_alpha * beta_over_alpha)
        beta = beta_over_alpha * alpha
        checks.extend([
            (f"negative lower eigenvalue N={n}", lam < 0),
            (f"eigenvector normalization N={n}", abs(alpha * alpha + beta * beta - 1) < 1e-12),
            (f"first row eigen-equation N={n}", abs(g * sigma * beta - lam * alpha) < 1e-9 * sigma),
        ])
    checks.append(("Ritz ratio tends toward minus one", all(abs(x + 1) > abs(y + 1) for x, y in zip(ratios, ratios[1:]))))
    checks.append(("Ritz error is lower order", abs(ratios[-1] + 1) < 0.01))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
