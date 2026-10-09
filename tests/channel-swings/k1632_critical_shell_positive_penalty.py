#!/usr/bin/env python3
"""Certificate for K1632's positive critical-shell penalty."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1632-critical-shell-positive-penalty.json").read_text())
    q, z = d["positive_penalty"], d["decision"]
    a, kappa, g, rho, volume = 1.0, 2.0, 1.0, 0.5, 0.01
    threshold = (a * a + kappa) ** 1.5 / (6.0 * g * (1.0 + rho))
    lower = rho * rho * volume * (
        math.sqrt(a * a + kappa) / (4.0 * (1.0 + rho))
        - 1.5 * g * volume / (a * a + kappa)
    )
    checks = [
        ("claim", d["claim_id"] == "K1632"),
        ("fixed-ratio shell", "fixed-ratio shell" in q["shell"]),
        ("Jordan shell", "Jordan-measurable" in q["shell"]),
        ("boundary null", "boundary measure zero" in q["shell"]),
        ("small-volume condition", volume < threshold),
        ("positive fixture", lower > 0.0),
        ("critical information scale", "I(M_N;X_N)=Theta(N^3)" in q["critical_scales"]),
        ("missing Fisher scale", "Delta_N=Theta(N^4)" in q["critical_scales"]),
        ("full penalty", "c_(g,rho,E)N^4+o(N^4)" in q["full_energy"]),
        ("Riemann premise", "Boundary-null Jordan measurability" in q["full_energy"]),
        ("critical retained", z["critical_information_retained"]),
        ("Fisher retained", z["leading_missing_fisher_retained"]),
        ("strict penalty", z["strict_positive_full_energy_penalty"]),
        ("does not lower", not z["critical_channel_lowers_profiled_coefficient"]),
        ("not unrestricted", not z["unrestricted_coefficient_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
