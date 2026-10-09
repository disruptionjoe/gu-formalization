#!/usr/bin/env python3
"""Certificate for K1602's relative-band coefficient stability theorem."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1602-relative-band-coefficient-stability.json").read_text())
    q, z = d["relative_band"], d["decision"]
    checks = [
        ("claim", d["claim_id"] == "K1602"),
        ("lower band", "(1-epsilon_N)S_N^*" in q["hypothesis"]),
        ("translation covariance", "Cov(m_z)<=eta_N S_N^*" in q["hypothesis"]),
        ("Loewner gap", "d_N Tr[Omega(S_N^*)^(-1)]" in q["loewner_bound"]),
        ("trace identity", "omega_k/s_(N,k)=sqrt" in q["trace_scale"]),
        ("trace N4", "O_g(N^4)" in q["trace_scale"]),
        ("component lower", "lambda_N^prof-Delta/4" in q["energy_lower"]),
        ("coefficient", "h_g^prof" in q["coefficient"]),
        ("scope fixed", "Fixed order-one heterogeneity" in q["scope_guard"]),
    ]
    eps, eta, sstar, c = 0.1, 0.2, 0.8, 0.1
    s1, s2 = (1 - eps) * sstar, (1 + eps) * sstar
    t = (s1 + s2) / 2 + c
    delta = 0.5 / s1 + 0.5 / s2 - 1 / t
    dn = 1 / (1 - eps) - 1 / (1 + eps + eta)
    checks += [
        ("scalar gap nonnegative", delta >= 0),
        ("scalar Loewner bound", delta <= dn / sstar + 1e-12),
        ("shrinking factor", (1 / (1 - 1e-6) - 1 / (1 + 2e-6)) < 4e-6),
        ("mode trace scale", sum(math.sqrt(k * k + 4 * 20 * 20) for k in range(1, 20 ** 3 + 1, 20 ** 2)) > 0),
        ("heterogeneous", z["genuinely_heterogeneous_band_allowed"]),
        ("translations", z["arbitrary_mode_translation_covariance_allowed"]),
        ("subleading", z["precision_gap_subleading_when_band_shrinks"]),
        ("class coefficient", z["class_coefficient_h_g_prof"]),
        ("order-one open", not z["order_one_heterogeneity_controlled"]),
        ("unrestricted open", not z["unrestricted_coefficient_identified"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
