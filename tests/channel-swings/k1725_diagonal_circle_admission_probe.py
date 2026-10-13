#!/usr/bin/env python3
"""Hostile protected-surface mutations for K1725."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1725-diagonal-circle-admission.json").read_text())


def errors(x):
    a, q = x.get("admission", {}), x.get("decision", {})
    out = []
    for key, needles in (("classification", ("circle-specific", "C has kernel {1,z}", "D is faithful")), ("positive_result", ("gcd-one", "odd charge")), ("ownership_boundary", ("does not select D", "hypercharge", "positive quotient")), ("source_effect", ("SOURCE_REGISTER_UNCHANGED", "UNCERTAIN")), ("ledger_effect", ("STANDING_LEDGER_UNCHANGED",)), ("public_effect", ("UNCHANGED",)), ("next_condition", ("source/action ownership", "Wider finite-strength scalar optimization"))):
        if not all(n in a.get(key, "") for n in needles): out.append(key)
    for key in ("different_circle_reopener_classified", "original_parity_obstruction_is_not_all_circles"):
        if not q.get(key): out.append(key)
    for key in ("source_selects_diagonal_circle", "physical_positive_quotient_constructed", "source_register_changed", "standing_ledger_changed", "canon_or_public_posture_changed"):
        if q.get(key): out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("classification", lambda x: x["admission"].__setitem__("classification", "all circles obstructed")),
        ("positive result", lambda x: x["admission"].__setitem__("positive_result", "none")),
        ("ownership boundary", lambda x: x["admission"].__setitem__("ownership_boundary", "D is hypercharge")),
        ("source movement", lambda x: x["admission"].__setitem__("source_effect", "changed")),
        ("ledger movement", lambda x: x["admission"].__setitem__("ledger_effect", "changed")),
        ("public movement", lambda x: x["admission"].__setitem__("public_effect", "changed")),
        ("next condition", lambda x: x["admission"].__setitem__("next_condition", "none")),
        ("reopener unclassified", lambda x: x["decision"].__setitem__("different_circle_reopener_classified", False)),
        ("universal-obstruction overclaim", lambda x: x["decision"].__setitem__("original_parity_obstruction_is_not_all_circles", False)),
        ("source overclaim", lambda x: x["decision"].__setitem__("source_selects_diagonal_circle", True)),
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
