#!/usr/bin/env python3
"""Hostile semantic mutations for K1717."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1717-effective-quotient-factorization.json").read_text())


def errors(x):
    a, q = x.get("factorization", {}), x.get("decision", {})
    out = []
    for key, needle in (("subgroup", "ker(C->U(H_ps))"), ("factor", "unique set map"), ("well_defined_reason", "constant on every H-orbit"), ("effective_action", "C is abelian"), ("topological_scope", "quotient topology")):
        if needle not in a.get(key, ""): out.append(key)
    for key in ("unique_set_factorization", "effective_quotient_equivariance", "continuous_factor_for_quotient_topology"):
        if not q.get(key): out.append(key)
    for key in ("original_circle_automorphism", "source_selects_effective_quotient", "physical_domain_constructed", "protected_status_change"):
        if q.get(key): out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("kernel subgroup", lambda x: x["factorization"].__setitem__("subgroup", "unknown")),
        ("uniqueness", lambda x: x["factorization"].__setitem__("factor", "some map")),
        ("well defined", lambda x: x["factorization"].__setitem__("well_defined_reason", "assumed")),
        ("normality", lambda x: x["factorization"].__setitem__("effective_action", "not checked")),
        ("topology", lambda x: x["factorization"].__setitem__("topological_scope", "homeomorphism")),
        ("factor decision", lambda x: x["decision"].__setitem__("unique_set_factorization", False)),
        ("effective action decision", lambda x: x["decision"].__setitem__("effective_quotient_equivariance", False)),
        ("automorphism overclaim", lambda x: x["decision"].__setitem__("original_circle_automorphism", True)),
        ("source overclaim", lambda x: x["decision"].__setitem__("source_selects_effective_quotient", True)),
        ("domain overclaim", lambda x: x["decision"].__setitem__("physical_domain_constructed", True)),
        ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D); mutate(x); assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
