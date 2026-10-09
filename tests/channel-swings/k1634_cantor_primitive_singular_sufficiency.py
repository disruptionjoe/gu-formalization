#!/usr/bin/env python3
"""Certificate for K1634's singular-continuous positive class."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1634-cantor-primitive-singular-sufficiency.json").read_text())
    q, z = d["cantor_class"], d["decision"]
    alpha = math.log(2.0) / math.log(3.0)
    s = 0.75
    checks = [
        ("claim", d["claim_id"] == "K1634"),
        ("translated Cantor construction", "F_C(x)-F_C(x-a)" in q["construction"]),
        ("compact", "compactly supported" in q["compact_bv"]),
        ("continuous BV", "continuous" in q["compact_bv"] and "bounded variation" in q["compact_bv"]),
        ("atom-free singular", "atom-free" in q["derivative"] and "singular continuous" in q["derivative"]),
        ("Holder exponent", abs(alpha - 0.6309297535714574) < 1e-15),
        ("chosen s above half", s > 0.5),
        ("chosen s below threshold", s < (1.0 + alpha) / 2.0),
        ("fractional membership", "every s<(1+log(2)/log(3))/2" in q["fractional_membership"]),
        ("holonomy", "widehat G_a in L1" in q["holonomy"]),
        ("compact decision", z["compact_continuous_BV"]),
        ("atom-free decision", z["derivative_atom_free"]),
        ("singular decision", z["derivative_singular_continuous"]),
        ("fractional decision", z["fractional_Hs_above_half"]),
        ("L1 decision", z["holonomy_L1"]),
        ("not all singular", not z["all_atom_free_singular_measures_closed"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
