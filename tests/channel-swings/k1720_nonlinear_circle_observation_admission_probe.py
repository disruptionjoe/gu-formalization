#!/usr/bin/env python3
"""Hostile protected-surface mutations for K1720."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1720-nonlinear-circle-observation-admission.json").read_text())


def errors(x):
    a, q = x.get("admission", {}), x.get("decision", {})
    out = []
    for key, needle in (("obstruction", "randomized"), ("factorization", "uniquely through X/{1,z}"), ("faithful_source", "faithful"), ("source_effect", "SOURCE_REGISTER_UNCHANGED"), ("ledger_effect", "STANDING_LEDGER_UNCHANGED"), ("public_effect", "UNCHANGED"), ("next_condition", "source/action-owned reopener")):
        if needle not in a.get(key, ""): out.append(key)
    if len(a.get("exact_reopeners", [])) != 4: out.append("reopeners")
    for key in ("typed_nonlinear_alternative_classified", "same_kernel_joint_and_randomized_escape_excluded"):
        if not q.get(key): out.append(key)
    for key in ("effective_quotient_selected_by_source", "physical_positive_quotient_constructed", "source_register_changed", "standing_ledger_changed", "canon_or_public_posture_changed"):
        if q.get(key): out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("randomized scope", lambda x: x["admission"].__setitem__("obstruction", "deterministic only")),
        ("unique factor", lambda x: x["admission"].__setitem__("factorization", "unknown")),
        ("faithful scope", lambda x: x["admission"].__setitem__("faithful_source", "all sources")),
        ("reopener loss", lambda x: x["admission"].__setitem__("exact_reopeners", [])),
        ("source movement", lambda x: x["admission"].__setitem__("source_effect", "changed")),
        ("ledger movement", lambda x: x["admission"].__setitem__("ledger_effect", "changed")),
        ("public movement", lambda x: x["admission"].__setitem__("public_effect", "changed")),
        ("next condition loss", lambda x: x["admission"].__setitem__("next_condition", "none")),
        ("nonlinear unclassified", lambda x: x["decision"].__setitem__("typed_nonlinear_alternative_classified", False)),
        ("source quotient overclaim", lambda x: x["decision"].__setitem__("effective_quotient_selected_by_source", True)),
        ("physical overclaim", lambda x: x["decision"].__setitem__("physical_positive_quotient_constructed", True)),
        ("source register overclaim", lambda x: x["decision"].__setitem__("source_register_changed", True)),
        ("ledger overclaim", lambda x: x["decision"].__setitem__("standing_ledger_changed", True)),
        ("public overclaim", lambda x: x["decision"].__setitem__("canon_or_public_posture_changed", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D); mutate(x); assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
