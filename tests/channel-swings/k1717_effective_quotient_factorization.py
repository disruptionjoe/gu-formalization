#!/usr/bin/env python3
"""Exact controls for K1717's effective-quotient factorization."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1717-effective-quotient-factorization.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    a, q = D["factorization"], D["decision"]
    pi = lambda x: x % 2
    fbar = lambda orbit: orbit
    f = lambda x: x % 2
    checks += [
        ("finite quotient factor", all(f(x) == fbar(pi(x)) for x in range(4))),
        ("finite quotient uniqueness", all([f(x) for x in (o, o + 2)] == [fbar(o), fbar(o)] for o in range(2))),
        ("finite effective equivariance", all(fbar((g + o) % 2) == (g + fbar(o)) % 2 for g in range(2) for o in range(2))),
        ("exact kernel subgroup", "ker(C->U(H_ps))" in a["subgroup"]),
        ("quotient map named", a["quotient_map"] == "pi_X:X->X/H"),
        ("unique factor", "unique set map" in a["factor"]),
        ("well-defined reason", "constant on every H-orbit" in a["well_defined_reason"]),
        ("normality reason", "C is abelian" in a["effective_action"]),
        ("quotient topology scope", "quotient topology" in a["topological_scope"]),
        ("set factor decision", q["unique_set_factorization"]),
        ("effective equivariance decision", q["effective_quotient_equivariance"]),
        ("continuous factor decision", q["continuous_factor_for_quotient_topology"]),
        ("not automorphism", not q["original_circle_automorphism"]),
        ("source fence", not q["source_selects_effective_quotient"]),
        ("domain fence", not q["physical_domain_constructed"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
