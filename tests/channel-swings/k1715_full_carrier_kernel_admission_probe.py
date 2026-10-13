#!/usr/bin/env python3
"""Hostile semantic mutations for K1715."""
import copy
import json
from pathlib import Path

D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1715-full-carrier-kernel-admission.json").read_text())


def errors(x):
    a, q = x.get("admission", {}), x.get("decision", {})
    out = []
    for key, needle in (("original_circle_result", "exact kernel {1,z}"), ("effective_quotient_result", "acts faithfully"), ("source_effect", "SOURCE_REGISTER_UNCHANGED"), ("ledger_effect", "STANDING_LEDGER_UNCHANGED"), ("public_effect", "PUBLIC_POSTURE_UNCHANGED"), ("next_condition", "source/action-owned")):
        if needle not in a.get(key, ""):
            out.append(key)
    for key in ("full_carrier_original_circle_kernel_classified", "primitive_original_circle_route_excluded", "effective_quotient_escape_constructed"):
        if not q.get(key):
            out.append(key)
    for key in ("source_selection_constructed", "physical_positive_quotient_constructed", "source_register_changed", "standing_ledger_changed", "canon_or_public_posture_changed"):
        if q.get(key):
            out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("kernel", lambda x: x["admission"].__setitem__("original_circle_result", "sample only")),
        ("quotient", lambda x: x["admission"].__setitem__("effective_quotient_result", "open")),
        ("source effect", lambda x: x["admission"].__setitem__("source_effect", "changed")),
        ("ledger effect", lambda x: x["admission"].__setitem__("ledger_effect", "changed")),
        ("public effect", lambda x: x["admission"].__setitem__("public_effect", "changed")),
        ("next condition", lambda x: x["admission"].__setitem__("next_condition", "complete")),
        ("kernel decision", lambda x: x["decision"].__setitem__("full_carrier_original_circle_kernel_classified", False)),
        ("primitive decision", lambda x: x["decision"].__setitem__("primitive_original_circle_route_excluded", False)),
        ("quotient decision", lambda x: x["decision"].__setitem__("effective_quotient_escape_constructed", False)),
        ("source overclaim", lambda x: x["decision"].__setitem__("source_selection_constructed", True)),
        ("physical overclaim", lambda x: x["decision"].__setitem__("physical_positive_quotient_constructed", True)),
        ("source movement", lambda x: x["decision"].__setitem__("source_register_changed", True)),
        ("ledger movement", lambda x: x["decision"].__setitem__("standing_ledger_changed", True)),
        ("public movement", lambda x: x["decision"].__setitem__("canon_or_public_posture_changed", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D)
        mutate(x)
        assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
