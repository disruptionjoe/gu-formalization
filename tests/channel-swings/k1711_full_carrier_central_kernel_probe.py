#!/usr/bin/env python3
"""Hostile semantic mutations for K1711."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1711-full-carrier-central-kernel.json").read_text())


def errors(x):
    g, q = x.get("global_kernel", {}), x.get("decision", {})
    out = []
    for key, needle in (
        ("half_period", "z=C(pi)=[-1,1]"),
        ("membership", "z lies in M=Z_K(A)"),
        ("homogeneous_action", "z k M=k z M=k M"),
        ("hilbert_action", "U(pi)=I"),
    ):
        if needle not in g.get(key, ""):
            out.append(key)
    for key in ("half_period_element_is_global_central", "half_period_element_lies_in_M", "left_action_on_K_over_M_is_identity", "U_pi_is_identity_on_full_H_ps"):
        if not q.get(key):
            out.append(key)
    for key in ("source_selects_circle", "physical_GU_quotient_constructed", "protected_status_change"):
        if q.get(key):
            out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("central class", lambda x: x["global_kernel"].__setitem__("half_period", "ordinary rotation")),
        ("M membership", lambda x: x["global_kernel"].__setitem__("membership", "unknown")),
        ("coset action", lambda x: x["global_kernel"].__setitem__("homogeneous_action", "nontrivial")),
        ("Hilbert action", lambda x: x["global_kernel"].__setitem__("hilbert_action", "one K-type only")),
        ("central decision", lambda x: x["decision"].__setitem__("half_period_element_is_global_central", False)),
        ("membership decision", lambda x: x["decision"].__setitem__("half_period_element_lies_in_M", False)),
        ("coset decision", lambda x: x["decision"].__setitem__("left_action_on_K_over_M_is_identity", False)),
        ("full carrier decision", lambda x: x["decision"].__setitem__("U_pi_is_identity_on_full_H_ps", False)),
        ("source overclaim", lambda x: x["decision"].__setitem__("source_selects_circle", True)),
        ("physical overclaim", lambda x: x["decision"].__setitem__("physical_GU_quotient_constructed", True)),
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
