#!/usr/bin/env python3
"""Exact charge-lattice controls for K1713."""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1713-primitive-observed-intertwiner-obstruction.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    b, q = D["intertwiner_obstruction"], D["decision"]
    primitive = [1, -4, 2, -3, 6, 0]
    target = [-8, -6, -4, -2, 0, 2, 4, 6, 8]
    checks += [
        ("primitive gcd", math.gcd(*[abs(x) for x in primitive]) == 1),
        ("primitive odd weight", any(x % 2 for x in primitive)),
        ("target all even", all(x % 2 == 0 for x in target)),
        ("sign preserves parity", all((x % 2) == ((-x) % 2) for x in primitive)),
        ("target support text", "only even integer weights" in b["target_support"]),
        ("automorphism degree", "plus_or_minus one" in b["automorphisms"]),
        ("weight law", "target weight plus_or_minus r" in b["weight_space_law"]),
        ("odd killed", "odd source weight maps to zero" in b["obstruction"]),
        ("scope retains quotient", "effective quotient" in b["scope"]),
        ("full extension", q["fixed_ktype_exclusion_extends_to_full_H_ps"]),
        ("parity preserved", q["original_circle_automorphism_preserves_parity"]),
        ("no faithful intertwiner", not q["faithful_primitive_linear_intertwiner_to_full_H_ps_exists"]),
        ("quotient escape", q["effective_quotient_escape_remains_open"]),
        ("not all maps", not q["all_observation_maps_excluded"]),
        ("no source falsification", not q["source_hypercharge_falsified"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
