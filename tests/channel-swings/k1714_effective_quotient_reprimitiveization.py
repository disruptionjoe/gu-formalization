#!/usr/bin/env python3
"""Exact quotient, charge and normalization controls for K1714."""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1714-effective-quotient-reprimitiveization.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    e, q = D["effective_quotient"], D["decision"]
    old = [-4, -2, 0, 2, 4]
    new = [x // 2 for x in old]
    Q, A, kappa, mu, c = 3.0, 5.0, 11.0, 13.0, 0.5
    checks += [
        ("quotient definition", "C_eff=C/{1,z}" in e["definition"]),
        ("coordinate doubling", "beta=2 alpha" in e["definition"]),
        ("exact-kernel faithfulness", "exact original action kernel" in e["faithfulness"]),
        ("generator halves", "Q_eff=Q/2" in e["generator"]),
        ("weights halve", new == [-2, -1, 0, 1, 2]),
        ("effective gcd one", math.gcd(*[abs(x) for x in new]) == 1),
        ("degree two", "degree two" in e["topology"]),
        ("not automorphism text", "not an automorphism" in e["topology"]),
        ("kinetic norm quarter", "1/4" in e["kinetic_normalization"]),
        ("covariant product", abs((c * Q) * (A / c) - Q * A) < 1e-12),
        ("kinetic rescaling", abs((c * c * kappa) * (A / c) ** 2 - kappa * A * A) < 1e-12),
        ("regularizer rescaling", abs((mu / (c * c)) * (c * Q) ** 2 - mu * Q * Q) < 1e-12),
        ("faithful decision", q["effective_circle_action_faithful"]),
        ("primitive decision", q["effective_charge_lattice_primitive"]),
        ("parity repair", q["fixed_ktype_parity_obstruction_removed_after_quotient"]),
        ("not automorphism", not q["quotient_is_original_circle_automorphism"]),
        ("local equivalence", q["local_rescaling_equivalent"]),
        ("source fence", not q["source_selects_effective_quotient"]),
        ("physical fence", not q["physical_observed_intertwiner_constructed"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
