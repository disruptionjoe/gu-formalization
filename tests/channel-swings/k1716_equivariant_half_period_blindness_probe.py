#!/usr/bin/env python3
"""Hostile semantic mutations for K1716."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1716-equivariant-half-period-blindness.json").read_text())


def errors(x):
    t, q = x.get("theorem", {}), x.get("decision", {})
    out = []
    if t.get("identity") != "F(z.x)=z.F(x)=F(x) for every x in X": out.append("identity")
    if "No linearity" not in t.get("regularity", ""): out.append("regularity")
    if "equivariantMapEquivOrbitValuation_of_trivial" not in t.get("formal_reuse", ""): out.append("reuse")
    for key in ("arbitrary_equivariant_maps_are_z_orbit_constant",):
        if not q.get(key): out.append(key)
    for key in ("nonlinear_escape_under_same_equivariance", "regularity_assumption_required", "new_general_group_action_theorem_claimed", "source_selects_observation", "physical_quotient_constructed", "protected_status_change"):
        if q.get(key): out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("identity", lambda x: x["theorem"].__setitem__("identity", "F(z.x) unknown")),
        ("linearity dependency", lambda x: x["theorem"].__setitem__("regularity", "Linear maps only")),
        ("formal reuse", lambda x: x["theorem"].__setitem__("formal_reuse", "new theorem")),
        ("orbit decision", lambda x: x["decision"].__setitem__("arbitrary_equivariant_maps_are_z_orbit_constant", False)),
        ("nonlinear escape", lambda x: x["decision"].__setitem__("nonlinear_escape_under_same_equivariance", True)),
        ("regularity burden", lambda x: x["decision"].__setitem__("regularity_assumption_required", True)),
        ("novelty overclaim", lambda x: x["decision"].__setitem__("new_general_group_action_theorem_claimed", True)),
        ("source overclaim", lambda x: x["decision"].__setitem__("source_selects_observation", True)),
        ("physical overclaim", lambda x: x["decision"].__setitem__("physical_quotient_constructed", True)),
        ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D); mutate(x); assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
