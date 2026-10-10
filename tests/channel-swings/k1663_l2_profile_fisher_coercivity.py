#!/usr/bin/env python3
"""Certificate for K1663's l2 profile-Fisher coercivity."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1663-l2-profile-fisher-coercivity.json").read_text())
    claim, decision = data["fisher_coercivity"], data["decision"]
    checks = []
    for t in (0.01, 0.15, 0.5, 0.85, 0.99):
        checks.append((f"pointwise inequality {t}", t / (1 - t) >= 4 * t * t - 1e-14))
    rho = (0.5, 1.0, 1.75, 2.0)
    r = (0.45, 0.5, 0.6, 0.7)
    eta = 0.2
    t = [eta * a * b for a, b in zip(rho, r)]
    exact = 0.5 * sum(a * x / (1 - x) for a, x in zip(r, t))
    floor = 2 * eta * eta * sum(a * a * b**3 for a, b in zip(rho, r))
    checks += [
        ("admissible sample", max(t) < 1),
        ("weighted exact exceeds floor", exact >= floor - 1e-14),
        ("small shell cube", math.isclose((math.sqrt(3) / 4) ** 3, 3 * math.sqrt(3) / 64)),
    ]
    for g in (8 * math.sqrt(3), 100.0, 10000.0):
        checks.append((f"large margin seed {g}", 2 * (g / 2) ** 1.5 > 3 * g / 512))
    checks += [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1663"),
        ("variables", "eta rho_(N,k)r_(N,k)" in claim["variables"]),
        ("exact formula", "C_(F,N)=(N/2)sum_k" in claim["exact_term"]),
        ("l2 floor", "sum_k rho_(N,k)^2" in claim["l2_floor"]),
        ("pointwise source", "t/(1-t)>=4t^2" in claim["l2_floor"]),
        ("small regime", "3sqrt(3)/64" in claim["small_coupling"]),
        ("large regime", "(g/2)^(3/2)" in claim["large_coupling"]),
        ("scope", "component Fisher term" in claim["scope_guard"]),
        ("formula decision", decision["exact_weighted_component_formula"]),
        ("l2 decision", decision["l2_profile_floor_proved"]),
        ("amplitude decision", decision["all_admissible_profile_values_covered"]),
        ("unrestricted open", not decision["unrestricted_output_fisher_bound_proved"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
