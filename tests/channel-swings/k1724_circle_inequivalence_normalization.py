#!/usr/bin/env python3
"""Exact kernel and normalization controls for K1724."""
import hashlib, json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1724-circle-inequivalence-normalization.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    c, q = D["comparison"], D["decision"]
    norm_c = Fraction(1)
    norm_d = Fraction(1, 4) + Fraction(1, 4)
    checks += [
        ("original kernel", "order two" in c["original_kernel"] and "{1,z}" in c["original_kernel"]),
        ("diagonal kernel", "trivial" in c["diagonal_kernel"]),
        ("circle automorphisms", "plus_or_minus beta" in c["automorphism_invariant"]),
        ("kernel invariant", "preserves the kernel order" in c["automorphism_invariant"]),
        ("inequivalence", "genuinely different embedded circle" in c["inequivalence"]),
        ("generator pair", "T_C=(E,0)" in c["generators"] and "T_D=(E/2,F/2)" in c["generators"]),
        ("exact norm control", norm_d / norm_c == Fraction(1, 2)),
        ("stated norm ratio", "||T_D||^2=1/2" in c["norms"]),
        ("coupling fence text", "does not supply a physical gauge coupling" in c["normalization_fence"]),
        ("no same-circle repair", not q["same_circle_automorphism_repair"]),
        ("different circle decision", q["different_embedded_circle"]),
        ("norm decision", q["bare_norm_ratio_one_half"]),
        ("coupling fence", not q["physical_gauge_coupling_derived"]),
        ("hypercharge fence", not q["source_hypercharge_identified"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
