#!/usr/bin/env python3
"""Hostile semantic mutations for K1714."""
import copy
import json
from pathlib import Path

D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1714-effective-quotient-reprimitiveization.json").read_text())


def errors(x):
    e, q = x.get("effective_quotient", {}), x.get("decision", {})
    out = []
    for key, needle in (("definition", "C_eff=C/{1,z}"), ("faithfulness", "exact original action kernel"), ("generator", "Q_eff=Q/2"), ("ktype_weights", "{-2,-1,0,1,2}"), ("topology", "not an automorphism"), ("kinetic_normalization", "1/4"), ("local_equivalence", "kappa_eff=kappa/4"), ("physical_ceiling", "Source/action ownership")):
        if needle not in e.get(key, ""):
            out.append(key)
    for key in ("effective_circle_action_faithful", "effective_charge_lattice_primitive", "fixed_ktype_parity_obstruction_removed_after_quotient", "local_rescaling_equivalent"):
        if not q.get(key):
            out.append(key)
    for key in ("quotient_is_original_circle_automorphism", "source_selects_effective_quotient", "physical_observed_intertwiner_constructed", "protected_status_change"):
        if q.get(key):
            out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("quotient", lambda x: x["effective_quotient"].__setitem__("definition", "unchanged circle")),
        ("faithfulness", lambda x: x["effective_quotient"].__setitem__("faithfulness", "assumed")),
        ("generator", lambda x: x["effective_quotient"].__setitem__("generator", "Q")),
        ("weights", lambda x: x["effective_quotient"].__setitem__("ktype_weights", "unchanged")),
        ("topology", lambda x: x["effective_quotient"].__setitem__("topology", "automorphism")),
        ("kinetic", lambda x: x["effective_quotient"].__setitem__("kinetic_normalization", "unchanged")),
        ("local", lambda x: x["effective_quotient"].__setitem__("local_equivalence", "none")),
        ("ceiling", lambda x: x["effective_quotient"].__setitem__("physical_ceiling", "physical")),
        ("faithful decision", lambda x: x["decision"].__setitem__("effective_circle_action_faithful", False)),
        ("primitive decision", lambda x: x["decision"].__setitem__("effective_charge_lattice_primitive", False)),
        ("repair decision", lambda x: x["decision"].__setitem__("fixed_ktype_parity_obstruction_removed_after_quotient", False)),
        ("automorphism overclaim", lambda x: x["decision"].__setitem__("quotient_is_original_circle_automorphism", True)),
        ("source overclaim", lambda x: x["decision"].__setitem__("source_selects_effective_quotient", True)),
        ("physical overclaim", lambda x: x["decision"].__setitem__("physical_observed_intertwiner_constructed", True)),
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
