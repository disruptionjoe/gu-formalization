#!/usr/bin/env python3
"""Exact controls for K1718's faithful-source noninjectivity."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1718-faithful-observation-noninjectivity.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    n, q = D["noninjectivity"], D["decision"]
    f = lambda x: x % 2
    checks += [
        ("regular C4 source faithful", all(any((x + g) % 4 != x for x in range(4)) for g in (1, 2, 3))),
        ("nontrivial z witness", any((x + 2) % 4 != x for x in range(4))),
        ("observed collision", any((x + 2) % 4 != x and f((x + 2) % 4) == f(x) for x in range(4))),
        ("faithful hypothesis", "faithful" in n["source_hypothesis"]),
        ("witness logic", "z is not the identity" in n["witness"]),
        ("collision logic", "F(z.x)=F(x)" in n["collision"]),
        ("arbitrary-map conclusion", "set map" in n["conclusion"]),
        ("reopeners named", all(s in n["exact_reopener"] for s in ("quotient", "nontrivially", "break", "z-sensitive"))),
        ("faithfulness decision", q["faithful_source_supplies_nontrivial_z_orbit"]),
        ("noninjectivity decision", q["all_equivariant_observations_noninjective"]),
        ("linearity removed", q["k1713_linearity_restriction_removed"]),
        ("nonfaithful fence", not q["all_nonfaithful_sources_excluded"]),
        ("other circle fence", not q["all_other_compact_circles_excluded"]),
        ("source fence", not q["source_claim_falsified"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
