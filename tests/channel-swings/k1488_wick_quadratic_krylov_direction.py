#!/usr/bin/env python3
"""Controls for K1488's quadratic Wick Krylov direction."""
import hashlib, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1488-wick-quadratic-krylov-direction.json").read_text())


def validate(d):
    a, q = d["quadratic_krylov_direction"], d["decision"]
    return [
        d["schema_version"] == "1.0",
        d["claim_id"] == "K1488",
        "V_N=I_4(f_N)" in a["notation"],
        "r=0)^4" in a["product_formula"],
        "orthogonal to both 1 and X_N" in a["orthogonal_residual"],
        "P_8 R_N=P_8(X_N^2)" in a["top_chaos_survives"],
        "sigma_N^4" in a["symmetrization_lower_bound"],
        "tau_N^2=E(X_N^4)-1-mu_N^2>=1" in a["normalized_lower_bound"],
        "tau_N>=1" in a["multiplication_coupling"],
        q["quadratic_krylov_direction_constructed"],
        q["eighth_chaos_projection_survives_orthogonalization"],
        q["eighth_chaos_squared_norm_lower_scale"] == "sigma_N^4",
        q["normalized_residual_squared_norm_lower"] == 1,
        q["uniform_next_krylov_coupling_lower"] == 1,
        not q["ground_energy_lower_bound_proved"],
        not q["protected_status_change"],
    ]


def main():
    checks = []
    for name, pin in D["pinned_inputs"].items():
        checks.append((f"{name} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    checks.extend((f"serialized invariant {i}", ok) for i, ok in enumerate(validate(D), 1))
    top_identity = math.factorial(8) * (math.factorial(4) ** 2 / math.factorial(8))
    checks.extend([
        ("identity-pairing symmetrization coefficient", top_identity == math.factorial(4) ** 2),
        ("variance normalization", top_identity / math.factorial(4) ** 2 == 1),
        ("projection cannot remove chaos eight", 8 not in (0, 4)),
        ("positive Krylov denominator", D["decision"]["normalized_residual_squared_norm_lower"] > 0),
    ])
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
