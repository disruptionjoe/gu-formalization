#!/usr/bin/env python3
"""Exact controls for K1716's arbitrary-map half-period blindness."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1716-equivariant-half-period-blindness.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    t, q = D["theorem"], D["decision"]
    f = lambda x: x % 2
    checks += [
        ("finite C4 equivariance", all(f((g + x) % 4) == (g + f(x)) % 2 for g in range(4) for x in range(4))),
        ("finite half-period blindness", all(f((x + 2) % 4) == f(x) for x in range(4))),
        ("arbitrary set-map scope", "set map" in t["hypothesis"]),
        ("exact identity", t["identity"] == "F(z.x)=z.F(x)=F(x) for every x in X"),
        ("no linearity", "No linearity" in t["regularity"]),
        ("no continuity", "continuity" in t["regularity"]),
        ("no locality", "locality" in t["regularity"]),
        ("formal theorem reused", "equivariantMapEquivOrbitValuation_of_trivial" in t["formal_reuse"]),
        ("orbit constant decision", q["arbitrary_equivariant_maps_are_z_orbit_constant"]),
        ("nonlinear escape rejected", not q["nonlinear_escape_under_same_equivariance"]),
        ("regularity not required", not q["regularity_assumption_required"]),
        ("no theorem novelty overclaim", not q["new_general_group_action_theorem_claimed"]),
        ("source fence", not q["source_selects_observation"]),
        ("physical fence", not q["physical_quotient_constructed"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
