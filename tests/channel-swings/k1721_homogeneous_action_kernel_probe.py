#!/usr/bin/env python3
"""Hostile semantic mutations for K1721."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1721-homogeneous-action-kernel.json").read_text())


def errors(x):
    k, q = x.get("kernel_theorem", {}), x.get("decision", {})
    out = []
    for key, needles in (("group", ("connected",)), ("subgroup", ("finite",)), ("homogeneous_kernel", ("core_K(M)", "intersection_k")), ("core_to_center", ("finite normal", "singleton")), ("center_to_core", ("centralizes A", "every conjugate")), ("center", ("{1,z}", "z=[-1,1]")), ("hilbert_kernel", ("same kernel", "positive measure"))):
        if not all(n in k.get(key, "") for n in needles): out.append(key)
    for key in ("homogeneous_kernel_equals_center", "hilbert_kernel_equals_center", "kernel_has_order_two", "depends_on_connected_K_and_finite_M"):
        if not q.get(key): out.append(key)
    for key in ("physical_quotient_constructed", "protected_status_change"):
        if q.get(key): out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("connectedness", lambda x: x["kernel_theorem"].__setitem__("group", "K has several components")),
        ("finite M", lambda x: x["kernel_theorem"].__setitem__("subgroup", "positive dimensional M")),
        ("core identity", lambda x: x["kernel_theorem"].__setitem__("homogeneous_kernel", "unknown")),
        ("normal-core proof", lambda x: x["kernel_theorem"].__setitem__("core_to_center", "assumed")),
        ("reverse inclusion", lambda x: x["kernel_theorem"].__setitem__("center_to_core", "assumed")),
        ("center class", lambda x: x["kernel_theorem"].__setitem__("center", "trivial")),
        ("L2 lift", lambda x: x["kernel_theorem"].__setitem__("hilbert_kernel", "one K-type")),
        ("kernel decision", lambda x: x["decision"].__setitem__("homogeneous_kernel_equals_center", False)),
        ("hypothesis laundering", lambda x: x["decision"].__setitem__("depends_on_connected_K_and_finite_M", False)),
        ("physical overclaim", lambda x: x["decision"].__setitem__("physical_quotient_constructed", True)),
        ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D); mutate(x); assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
