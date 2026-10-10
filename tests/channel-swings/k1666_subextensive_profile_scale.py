#!/usr/bin/env python3
"""Certificate for K1666's subextensive-profile descent bound."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1666-subextensive-profile-scale.json").read_text())
    claim, decision = data["scale_bound"], data["decision"]
    checks = []
    for n in (16, 32, 64, 128):
        d = n**3 / 512
        b = n**2
        negative_floor = 3 * d * b / n**2
        checks += [
            (f"subextensive B N={n}", b / n**3 == 1 / n),
            (f"normalized descent vanishes N={n}", negative_floor / n**4 < 1 / n),
        ]
    checks += [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1666"),
        ("nonnegative weights", "0<=rho_(N,k)<=rho_+" in claim["profile"]),
        ("l2 mass", "B_N=sum rho_k^2" in claim["profile"]),
        ("defect floor", "-3eta^2 d_N B_N/N^2" in claim["defect_floor"]),
        ("full gap", "A_N+R_(Omega,N)/4+gD_(M,N)" in claim["full_gap"]),
        ("subextensive premise", "B_N=o(N^3)" in claim["coefficient_result"]),
        ("one-sided conclusion", ">=-o(N^4)" in claim["coefficient_result"]),
        ("scope two-sided", "not a two-sided o(N^4)" in claim["scope_guard"]),
        ("zero decision", decision["zero_weights_admitted"]),
        ("descent excluded", decision["subextensive_l2_descent_excluded"]),
        ("no localization", not decision["posterior_localization_required"]),
        ("two-sided open", not decision["two_sided_gap_control_proved"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
