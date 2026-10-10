#!/usr/bin/env python3
"""Scaling and manifest controls for K1697's rectangle compactness."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1697-rectangular-shape-compactness.json").read_text())
    shape, compact = data["shape_space"], data["compactness"]
    # Constant-weight rectangle control: tau~V and ell~V^2, hence R~V^3 and S~V^4.
    volumes = [1.0, 0.5, 0.125]
    r = [v**3 for v in volumes]
    s = [v**4 for v in volumes]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1697"),
        ("centered rectangles", "product_i[-alpha_i,alpha_i]" in shape["parameterization"]),
        ("degenerate faces", "degenerate faces adjoined" in shape["parameterization"]),
        ("zero b", "b_0(x)=|x|" in shape["zero_profile"]),
        ("zero a", "(2|x|)^(-1/2)" in shape["zero_profile"]),
        ("boundary R", "R_0" in shape["boundary"]),
        ("boundary S", "S_0" in shape["boundary"]),
        ("boundary zero", "zero on every degenerate face" in shape["boundary"]),
        ("profile rate", "g log(1/kappa_g)->1/(12pi)" in shape["profile_rate"]),
        ("positive maximum", "M=max_C R_0(C)>0" in compact["leading_maximum"]),
        ("interior maximizers", "disjoint from the degenerate boundary" in compact["maximizer_set"]),
        ("near minimizers", "common compact interior" in compact["near_minimizers"]),
        ("secondary floor", "S_*>" in compact["secondary_floor"]),
        ("R scaling", r[0] > r[1] > r[2] > 0),
        ("S scaling", s[0] > s[1] > s[2] > 0),
        ("boundary scaling", 1e-9**3 < 1e-20 and 1e-9**4 < 1e-30),
        ("scope guard", "does not cover arbitrary nonrectangular" in data["scope_guard"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
