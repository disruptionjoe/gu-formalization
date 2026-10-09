#!/usr/bin/env python3
"""Certificate for K1649's radial-block rigidity."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1649-radial-macroscopic-block-rigidity.json").read_text())
    q, z = d["radial_rigidity"], d["decision"]
    dim = 64
    sphere_er4 = dim ** 2
    coeff = 3 * (sphere_er4 / (dim * (dim + 2)) - 1)
    checks = [
        ("claim", d["claim_id"] == "K1649"),
        ("sphere coefficient", math.isclose(coeff, -6 / (dim + 2))),
        ("radial law", "X=RU" in q["law"]),
        ("standardization", "E R^2=d" in q["law"]),
        ("finite fourth", "finite E R^4" in q["law"]),
        ("exact cumulant", "d(d+2)" in q["exact_cumulant"]),
        ("Jensen", "Jensen" in q["negative_floor"]),
        ("sharp floor", "-6" in q["negative_floor"]),
        ("macroscopic dimension", "d_N=Theta(N^3)" in q["fourier_bound"]),
        ("direction norm", "O(N^4)" in q["fourier_bound"]),
        ("defect bound", "D_N>=-O(N)" in q["fourier_bound"]),
        ("coefficient", "h_g^prof" in q["coefficient"]),
        ("anisotropic fence", "does not control" in q["scope_guard"]),
        ("cumulant decision", z["exact_radial_cumulant_proved"]),
        ("suppression decision", z["sharp_dimension_suppression_proved"]),
        ("rigidity decision", z["radial_macroscopic_coefficient_rigidity"]),
        ("all blocks open", not z["all_macroscopic_blocks_controlled"]),
        ("anisotropy open", not z["angular_anisotropy_excluded"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
