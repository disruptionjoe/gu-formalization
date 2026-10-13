#!/usr/bin/env python3
"""Hostile semantic mutations for K1712."""
import copy
import json
from pathlib import Path

D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1712-even-charge-spectrum-effective-kernel.json").read_text())


def errors(x):
    s, q = x.get("spectral_kernel", {}), x.get("decision", {})
    out = []
    for key, needle in (("parity", "q is even"), ("nontrivial_witness", "q=2"), ("exactness", "0 or pi"), ("kernel", "{1,z}")):
        if needle not in s.get(key, ""):
            out.append(key)
    for key in ("all_full_carrier_charges_even", "charge_two_occurs", "circle_kernel_exactly_order_two", "statement_is_full_Hilbert_carrier"):
        if not q.get(key):
            out.append(key)
    for key in ("original_circle_action_faithful", "source_charge_assignment_constructed", "protected_status_change"):
        if q.get(key):
            out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("parity", lambda x: x["spectral_kernel"].__setitem__("parity", "all integers")),
        ("witness", lambda x: x["spectral_kernel"].__setitem__("nontrivial_witness", "none")),
        ("exactness", lambda x: x["spectral_kernel"].__setitem__("exactness", "unknown")),
        ("kernel", lambda x: x["spectral_kernel"].__setitem__("kernel", "larger")),
        ("even decision", lambda x: x["decision"].__setitem__("all_full_carrier_charges_even", False)),
        ("charge decision", lambda x: x["decision"].__setitem__("charge_two_occurs", False)),
        ("kernel decision", lambda x: x["decision"].__setitem__("circle_kernel_exactly_order_two", False)),
        ("faithful overclaim", lambda x: x["decision"].__setitem__("original_circle_action_faithful", True)),
        ("sample-only regression", lambda x: x["decision"].__setitem__("statement_is_full_Hilbert_carrier", False)),
        ("source overclaim", lambda x: x["decision"].__setitem__("source_charge_assignment_constructed", True)),
        ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D)
        mutate(x)
        assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
