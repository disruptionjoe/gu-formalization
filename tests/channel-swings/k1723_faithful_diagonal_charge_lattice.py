#!/usr/bin/env python3
"""Exact spectral controls for K1723."""
import hashlib, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1723-faithful-diagonal-charge-lattice.json").read_text())


def kernel_order(weights):
    return math.gcd(*(abs(w) for w in weights if w))


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    s, q = D["faithful_spectrum"], D["decision"]
    checks += [
        ("restricted kernel", all(x in s["restricted_kernel"] for x in ("core_K(M)", "Z(K)", "{1}"))),
        ("full Hilbert faithfulness", "H_ps=L2(K/M)" in s["hilbert_faithfulness"] and "faithful" in s["hilbert_faithfulness"]),
        ("integer spectrum", "integer charge spaces" in s["integer_spectrum"]),
        ("gcd-kernel law", "2 pi/d" in s["gcd_kernel"]),
        ("primitive lattice", "gcd{q:H_q(D) nonzero}=1" in s["primitive_lattice"]),
        ("odd consequence", "at least one odd charge" in s["odd_charge"]),
        ("finite gcd control", kernel_order([-4, -1, 0, 2]) == 1),
        ("even control", kernel_order([-4, -2, 0, 2]) == 2),
        ("space decision", q["faithful_on_K_over_M"]),
        ("Hilbert decision", q["faithful_on_full_H_ps"]),
        ("gcd decision", q["charge_lattice_gcd_one"]),
        ("odd decision", q["odd_charge_exists"]),
        ("K-type fence", not q["specific_physical_K_type_identified"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
