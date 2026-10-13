#!/usr/bin/env python3
"""Exact structural controls for K1711's full-carrier central kernel."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1711-full-carrier-central-kernel.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    g, q = D["global_kernel"], D["decision"]
    checks += [
        ("quotient group", "diagonal{plus_or_minus_one}" in g["compact_group"]),
        ("circle period", "2 pi" in g["circle"]),
        ("half period class", "z=C(pi)=[-1,1]" in g["half_period"]),
        ("order two", "order two" in g["half_period"]),
        ("M centralizer", "M=Z_K(A)" in g["spherical_subgroup"]),
        ("central membership", "z lies in M=Z_K(A)" in g["membership"]),
        ("coset identity", "z k M=k z M=k M" in g["homogeneous_action"]),
        ("full Hilbert identity", "U(pi)=I" in g["hilbert_action"] and "complete Hilbert carrier" in g["hilbert_action"]),
        ("central decision", q["half_period_element_is_global_central"]),
        ("membership decision", q["half_period_element_lies_in_M"]),
        ("coset decision", q["left_action_on_K_over_M_is_identity"]),
        ("full carrier decision", q["U_pi_is_identity_on_full_H_ps"]),
        ("source fence", not q["source_selects_circle"]),
        ("physical fence", not q["physical_GU_quotient_constructed"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
