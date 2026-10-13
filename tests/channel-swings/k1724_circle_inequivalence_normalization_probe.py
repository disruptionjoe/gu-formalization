#!/usr/bin/env python3
"""Hostile kernel/normalization mutations for K1724."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1724-circle-inequivalence-normalization.json").read_text())


def errors(x):
    c, q = x.get("comparison", {}), x.get("decision", {})
    out = []
    for key, needles in (("original_kernel", ("order two", "{1,z}")), ("diagonal_kernel", ("trivial",)), ("automorphism_invariant", ("plus_or_minus beta", "preserves the kernel order")), ("inequivalence", ("genuinely different embedded circle",)), ("generators", ("T_C=(E,0)", "T_D=(E/2,F/2)")), ("norms", ("||T_D||^2=1/2",)), ("normalization_fence", ("does not supply a physical gauge coupling",))):
        if not all(n in c.get(key, "") for n in needles): out.append(key)
    if q.get("same_circle_automorphism_repair"): out.append("same_circle")
    for key in ("different_embedded_circle", "bare_norm_ratio_one_half"):
        if not q.get(key): out.append(key)
    for key in ("physical_gauge_coupling_derived", "source_hypercharge_identified", "protected_status_change"):
        if q.get(key): out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("original kernel", lambda x: x["comparison"].__setitem__("original_kernel", "trivial")),
        ("diagonal kernel", lambda x: x["comparison"].__setitem__("diagonal_kernel", "order two")),
        ("automorphism", lambda x: x["comparison"].__setitem__("automorphism_invariant", "degree two")),
        ("inequivalence", lambda x: x["comparison"].__setitem__("inequivalence", "same circle")),
        ("generators", lambda x: x["comparison"].__setitem__("generators", "equal")),
        ("norm ratio", lambda x: x["comparison"].__setitem__("norms", "equal norms")),
        ("coupling fence", lambda x: x["comparison"].__setitem__("normalization_fence", "physical coupling fixed")),
        ("same-circle overclaim", lambda x: x["decision"].__setitem__("same_circle_automorphism_repair", True)),
        ("coupling overclaim", lambda x: x["decision"].__setitem__("physical_gauge_coupling_derived", True)),
        ("hypercharge overclaim", lambda x: x["decision"].__setitem__("source_hypercharge_identified", True)),
        ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D); mutate(x); assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
