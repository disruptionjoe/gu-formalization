#!/usr/bin/env python3
"""Certificate for K1631's full-energy shell identity."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1631-critical-shell-all-term-identity.json").read_text())
    q, z = d["all_term_identity"], d["decision"]
    g, kappa = 1.0, 2.0
    radii = [0.5, 1.0, 1.5]
    weights = [0.2, 0.15, 0.1]
    s0 = [r / math.sqrt(r * r + kappa) for r in radii]
    A0 = 0.5 * sum(w * s / r for w, s, r in zip(weights, s0, radii))
    c_c = A0 + kappa / (24.0 * g)
    rho, shell = 0.4, {1}
    s1 = [(1.0 + rho) * s if i in shell else s for i, s in enumerate(s0)]

    def A(s):
        return 0.5 * sum(w * x / r for w, x, r in zip(weights, s, radii))

    def F(s):
        return 0.25 * sum(w * r * (x + 1.0 / x - 2.0) for w, r, x in zip(weights, radii, s))

    def J(s):
        a = A(s)
        return F(s) + 6.0 * g * a * (2.0 * c_c - a)

    bregman = 0.25 * sum(
        w * r * (x - y) ** 2 / (x * y * y)
        for w, r, x, y in zip(weights, radii, s1, s0)
    ) - 6.0 * g * (A(s1) - A0) ** 2
    W = sum(weights[i] * math.sqrt(radii[i] ** 2 + kappa) for i in shell)
    B = sum(weights[i] / math.sqrt(radii[i] ** 2 + kappa) for i in shell)
    shell_formula = rho * rho * (W / (4.0 * (1.0 + rho)) - 1.5 * g * B * B)
    checks = [
        ("claim", d["claim_id"] == "K1631"),
        ("functional", "J_g(s)=F(s)+6gA(s)(2c_C-A(s))" in q["functional"]),
        ("profile", "kappa_g=24g" in q["profile"]),
        ("bregman text", "(s-s_*)^2" in q["bregman"]),
        ("numeric Bregman identity", abs((J(s1) - J(s0)) - bregman) < 1e-12),
        ("numeric shell identity", abs(bregman - shell_formula) < 1e-12),
        ("all term", z["full_free_plus_wick_balance_computed"]),
        ("no Fisher verdict", not z["missing_fisher_alone_used_as_energy_verdict"]),
        ("stationary scope", z["stationary_diagonal_scope_only"]),
        ("not unrestricted", not z["unrestricted_coefficient_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
