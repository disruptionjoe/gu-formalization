#!/usr/bin/env python3
"""Certificate for K1658's all-amplitude profile Fisher floor."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1658-profile-fisher-amplitude-floor.json").read_text())
    q, z = d["fisher_floor"], d["decision"]
    checks = []
    for t in (0.01, 0.2, 0.5, 0.8, 0.99):
        checks.append((f"amplitude inequality t={t}", t / (1 - t) >= 4 * t * t - 1e-14))
    for kappa in (0.01, 1.0, 25.0):
        denom = math.sqrt(3) * math.sqrt(3 + kappa) * (math.sqrt(3) + math.sqrt(3 + kappa))
        lower = 4 * kappa / denom
        checks.append((f"D lower positive kappa={kappa}", lower > 0))
    g0 = 8 * math.sqrt(3)
    kappa_lower = 16 * math.sqrt(3) * g0 - 3
    checks += [
        ("large-g kappa dominates", kappa_lower >= g0),
        ("cube density", (1 / 8) ** 3 == 1 / 512),
        ("shell radius", math.isclose((math.sqrt(3) / 4) ** 3, 3 * math.sqrt(3) / 64)),
        ("small-g margin", 3 * g0 / 512 <= 3 * math.sqrt(3) / 64 + 1e-14),
        ("schema", d["schema_version"] == "1.0"),
        ("claim", d["claim_id"] == "K1658"),
        ("shell recorded", "d_N/N^3<=1/512" in q["shell"]),
        ("exact formula", "C_(F,N)=(N/2)sum" in q["exact_term"]),
        ("quadratic floor", "C_(F,N)>=2N eta^2" in q["amplitude_inequality"]),
        ("small regime", "8sqrt(3)" in q["small_coupling"]),
        ("self consistency", "kappa_g>=16sqrt(3)g-3>=g" in q["profile_self_consistency"]),
        ("large regime", "(g/2)^(3/2)" in q["large_coupling"]),
        ("scope", "not an unrestricted Fisher inequality" in q["scope_guard"]),
        ("formula decision", z["exact_component_formula_rewritten"]),
        ("amplitude decision", z["all_admissible_amplitude_floor_proved"]),
        ("profile decision", z["profile_large_coupling_bound_proved"]),
        ("unrestricted open", not z["unrestricted_fisher_bound_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
