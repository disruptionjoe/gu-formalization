#!/usr/bin/env python3
"""Exact parity and kernel controls for K1712."""
import cmath
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1712-even-charge-spectrum-effective-kernel.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    s, q = D["spectral_kernel"], D["decision"]
    checks += [
        ("integer spectrum", "integer charge spaces" in s["integer_spectrum"]),
        ("even character law", all(abs(cmath.exp(1j * math.pi * n) - 1) < 1e-12 for n in range(-20, 21, 2))),
        ("odd character rejected", all(abs(cmath.exp(1j * math.pi * n) - 1) > 1 for n in range(-19, 20, 2))),
        ("parity conclusion", "q is even" in s["parity"]),
        ("charge-two witness", "q=2" in s["nontrivial_witness"]),
        ("kernel angles", all(abs(cmath.exp(2j * a) - 1) < 1e-12 for a in (0, math.pi))),
        ("quarter period excluded", abs(cmath.exp(2j * math.pi / 2) - 1) > 1),
        ("exact kernel text", "{1,z}" in s["kernel"]),
        ("all charges even", q["all_full_carrier_charges_even"]),
        ("charge two occurs", q["charge_two_occurs"]),
        ("exact order two", q["circle_kernel_exactly_order_two"]),
        ("not faithful", not q["original_circle_action_faithful"]),
        ("full carrier", q["statement_is_full_Hilbert_carrier"]),
        ("source fence", not q["source_charge_assignment_constructed"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
