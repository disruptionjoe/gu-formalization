#!/usr/bin/env python3
"""Hostile semantic mutations for K1718."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1718-faithful-observation-noninjectivity.json").read_text())


def errors(x):
    n, q = x.get("noninjectivity", {}), x.get("decision", {})
    out = []
    for key, needle in (("source_hypothesis", "faithful"), ("witness", "z is not the identity"), ("collision", "F(z.x)=F(x)"), ("conclusion", "set map"), ("exact_reopener", "z-sensitive")):
        if needle not in n.get(key, ""): out.append(key)
    for key in ("faithful_source_supplies_nontrivial_z_orbit", "all_equivariant_observations_noninjective", "k1713_linearity_restriction_removed"):
        if not q.get(key): out.append(key)
    for key in ("all_nonfaithful_sources_excluded", "all_other_compact_circles_excluded", "source_claim_falsified", "protected_status_change"):
        if q.get(key): out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("faithfulness", lambda x: x["noninjectivity"].__setitem__("source_hypothesis", "arbitrary source")),
        ("witness", lambda x: x["noninjectivity"].__setitem__("witness", "assumed")),
        ("collision", lambda x: x["noninjectivity"].__setitem__("collision", "unknown")),
        ("arbitrary map", lambda x: x["noninjectivity"].__setitem__("conclusion", "linear only")),
        ("reopener", lambda x: x["noninjectivity"].__setitem__("exact_reopener", "none")),
        ("noninjectivity decision", lambda x: x["decision"].__setitem__("all_equivariant_observations_noninjective", False)),
        ("linearity retention", lambda x: x["decision"].__setitem__("k1713_linearity_restriction_removed", False)),
        ("nonfaithful overclaim", lambda x: x["decision"].__setitem__("all_nonfaithful_sources_excluded", True)),
        ("other-circle overclaim", lambda x: x["decision"].__setitem__("all_other_compact_circles_excluded", True)),
        ("source overclaim", lambda x: x["decision"].__setitem__("source_claim_falsified", True)),
        ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D); mutate(x); assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
