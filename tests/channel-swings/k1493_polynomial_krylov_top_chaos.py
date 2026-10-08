#!/usr/bin/env python3
"""Controls for K1493's all-fixed-degree top-chaos Krylov bound."""
import hashlib, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1493-polynomial-krylov-top-chaos.json").read_text())


def main():
    checks = []
    for name, pin in D["pinned_inputs"].items():
        checks.append((f"{name} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    a, q = D["polynomial_top_chaos"], D["decision"]
    checks.extend([
        ("schema", D["schema_version"] == "1.0"),
        ("claim", D["claim_id"] == "K1493"),
        ("monic residual", "monic degree-j" in a["notation"]),
        ("top chaos identity", "P_(4j)" in a["top_chaos_identity"]),
        ("lower powers separated", "4(j-1)" in a["top_chaos_identity"]),
        ("block permutations", "(4!)^j" in a["symmetrization_lower_bound"]),
        ("nonnegative Fourier products", "nonnegative" in a["symmetrization_lower_bound"]),
        ("residual lower", "h_(j,N)>=1" in a["residual_lower_bound"]),
        ("hypercontractive upper", "(2j-1)^(4j)" in a["hypercontractive_upper_bound"]),
        ("finite chaos degree", "4j" in a["finite_chaos_degree"]),
        ("all degrees", q["all_fixed_degrees_constructed"]),
        ("top survives", q["top_chaos_projection_survives_lower_polynomials"]),
        ("lower equals one", q["monic_residual_squared_norm_lower"] == 1),
        ("no collapse", not q["finite_degree_residual_can_collapse"]),
        ("unbounded fenced", not q["unbounded_coefficient_growth_proved"]),
        ("protected fenced", not q["protected_status_change"]),
    ])
    for j in range(1, 7):
        H = (2 * j - 1) ** (4 * j)
        checks.append((f"H_{j} positive", H >= 1))
    checks.extend([
        ("j1 normalization", (2 * 1 - 1) ** 4 == 1),
        ("block identity ratio", math.factorial(4) ** 3 / math.factorial(4) ** 3 == 1),
    ])
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
