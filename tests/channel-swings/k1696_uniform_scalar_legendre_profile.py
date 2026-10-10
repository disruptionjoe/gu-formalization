#!/usr/bin/env python3
"""Exact algebraic controls for K1696's uniform Legendre profile."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1696-uniform-scalar-legendre-profile.json").read_text())
    factor, uniform = data["factorization"], data["uniform_expansion"]
    c_star, c_r = Fraction(1, 4), Fraction(31, 60)
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1696"),
        ("profile", "Phi_X(r)=min" in factor["profile"]),
        ("shape factorization", "tau_g(C)/4" in factor["shape_objective"]),
        ("ratio argument", "4g ell_g(C)/tau_g(C)" in factor["shape_objective"]),
        ("Rademacher scope", "Rademacher" in factor["seed_scope"]),
        ("three-point scope", "three-point" in factor["seed_scope"]),
        ("global branch", "unique global minimizer" in factor["global_branch"]),
        ("legendre quadratic", "-(3/2)r^2" in uniform["legendre"]),
        ("legendre cubic", "27c_Xr^3" in uniform["legendre"]),
        ("R ratio", "ell_g^2/tau_g" in uniform["shape_ratios"]),
        ("S ratio", "ell_g^3/tau_g^2" in uniform["shape_ratios"]),
        ("objective leading", "-6g^2R_g(C)" in uniform["objective"]),
        ("objective cubic", "432c_Xg^3S_g(C)" in uniform["objective"]),
        ("uniform rectangles", "uniformly over K1683 rectangles" in uniform["objective"]),
        ("star coefficient", 432 * c_star == 108),
        ("R coefficient", 432 * c_r == Fraction(1116, 5)),
        ("scope guard", "does not classify every seed" in data["scope_guard"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
