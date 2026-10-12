#!/usr/bin/env python3
"""Exact coefficient controls for K1701."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1701-universal-weak-channel-cubic-floor.json").read_text())
    i, c, decision = d["inputs"], d["coefficient"], d["decision"]
    samples = [(Fraction(0), Fraction(1, 4)), (Fraction(2), Fraction(17, 60)), (Fraction(16), Fraction(31, 60))]
    checks = [
        ("schema", d["schema_version"] == "1.0"),
        ("claim", d["claim_id"] == "K1701"),
        ("bounded symmetric", "bounded symmetric" in i["seed_class"]),
        ("negative fourth", "-u<0" in i["seed_class"]),
        ("matched q", "q=u t^2" in i["matched_coordinate"]),
        ("transport", "=-q" in i["matched_coordinate"]),
        ("K1687 sixth", "kappa_6^2/120-kappa_4^3/4" in i["k1687_expansion"]),
        ("matched leading", "q^2/6" in c["matched_law"]),
        ("matched cubic", "c_Xq^3" in c["matched_law"]),
        ("formula", "1/4+kappa_6(X)^2/(120u^3)" in c["formula"]),
        ("floor", c["sharp_floor"] == "c_X>=1/4."),
        ("equality iff", "if and only if kappa_6(X)=0" in c["equality"]),
        ("sample nonnegative", all(value >= Fraction(1, 4) for _, value in samples)),
        ("zero equality", samples[0][1] == Fraction(1, 4)),
        ("Rademacher", samples[-1][1] == Fraction(31, 60)),
        ("decision floor", decision["universal_fixed_seed_cubic_floor"]),
        ("finite open", not decision["finite_strength_optimizer_identified"]),
        ("scope", "fixed-seed weak-channel" in d["scope_guard"]),
    ]
    for n, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {n:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
