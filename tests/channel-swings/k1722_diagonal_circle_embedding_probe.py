#!/usr/bin/env python3
"""Hostile quotient-loop mutations for K1722."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1722-diagonal-circle-embedding.json").read_text())


def errors(x):
    c, q = x.get("diagonal_circle", {}), x.get("decision", {})
    out = []
    for key, needles in (("generators", ("E^2=F^2=-1",)), ("definition", ("(beta/2)E", "(beta/2)F", "2 pi")), ("closure", ("diagonal(-1,-1)",)), ("embedding", ("only at beta=0 modulo 2 pi",)), ("center_intersection", ("D intersection Z(K)={1}",)), ("half_period", ("D(pi) is noncentral",))):
        if not all(n in c.get(key, "") for n in needles): out.append(key)
    for key in ("well_defined_circle_in_quotient", "primitive_embedding", "trivial_center_intersection", "half_period_is_noncentral"):
        if not q.get(key): out.append(key)
    for key in ("source_selects_diagonal_circle", "protected_status_change"):
        if q.get(key): out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("Clifford sign", lambda x: x["diagonal_circle"].__setitem__("generators", "square plus one")),
        ("half lift", lambda x: x["diagonal_circle"].__setitem__("definition", "full generators")),
        ("global closure", lambda x: x["diagonal_circle"].__setitem__("closure", "Lie algebra only")),
        ("embedding", lambda x: x["diagonal_circle"].__setitem__("embedding", "unknown")),
        ("center intersection", lambda x: x["diagonal_circle"].__setitem__("center_intersection", "contains z")),
        ("half period", lambda x: x["diagonal_circle"].__setitem__("half_period", "central")),
        ("quotient decision", lambda x: x["decision"].__setitem__("well_defined_circle_in_quotient", False)),
        ("primitive decision", lambda x: x["decision"].__setitem__("primitive_embedding", False)),
        ("intersection decision", lambda x: x["decision"].__setitem__("trivial_center_intersection", False)),
        ("source overclaim", lambda x: x["decision"].__setitem__("source_selects_diagonal_circle", True)),
        ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D); mutate(x); assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
