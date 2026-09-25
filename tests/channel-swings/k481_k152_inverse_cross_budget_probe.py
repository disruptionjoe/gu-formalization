#!/usr/bin/env python3
"""Independent controls and hostile mutations for K481."""

from __future__ import annotations

import copy

from k477_k152_multilevel_complement_tree import CertificateError
from k481_k152_inverse_cross_budget import demo, inverse_cross_budget


def checks(packet):
    theorem, control, native = packet["theorem"], packet["exact_control"], packet["native_release"]
    return [
        packet["result_id"] == "K481-K152-INVERSE-CROSS-BUDGET",
        packet["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        packet["direction"] == "observed_to_native",
        "mu^2<" in theorem["inverse_budget"],
        "before numerical evaluation" in theorem["use"],
        "supplies no native" in theorem["ceiling"],
        control["alpha_lower"] == "5",
        control["gamma_lower"] == "8",
        control["requested_floor"] == "3",
        control["maximum_cross_norm_squared_strict"] == "10",
        control["selected_cross_norm"] == "3",
        control["strict_budget_slack"] == "1",
        control["same_fixed_form"] is True,
        control["complete_partition"] is True,
        len(control["proof_refs"]) == 3,
        control["released"] is True,
        native["native_inputs_present"] is False,
        native["K457_evaluation_released"] is False,
        native["K152_interval_emitted"] is False,
    ]


def main() -> int:
    packet = demo()
    base = checks(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d["theorem"].__setitem__("inverse_budget", "mu arbitrary"),
        lambda d: d["theorem"].__setitem__("ceiling", "native K152 interval"),
        lambda d: d["exact_control"].__setitem__("maximum_cross_norm_squared_strict", "9"),
        lambda d: d["exact_control"].__setitem__("strict_budget_slack", "0"),
        lambda d: d["exact_control"].__setitem__("same_fixed_form", False),
        lambda d: d["exact_control"].__setitem__("proof_refs", []),
        lambda d: d["native_release"].__setitem__("K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(checks(candidate))
    kwargs = dict(alpha=5, gamma=8, target_floor=3, selected_mu=3,
                  proof_refs=["a", "g", "t"], same_fixed_form=True,
                  complete_partition=True)
    invalid = 0
    for update in ({"alpha": 3}, {"gamma": 3}, {"selected_mu": -1},
                   {"selected_mu": 4}, {"proof_refs": []},
                   {"complete_partition": False}):
        candidate = dict(kwargs)
        candidate.update(update)
        try:
            inverse_cross_budget(**candidate)
        except CertificateError:
            invalid += 1
    print(f"K481 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K481 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K481 INVALID INPUTS: {invalid}/6 rejected")
    return 0 if all(base) and rejected == len(mutations) and invalid == 6 else 1


if __name__ == "__main__":
    raise SystemExit(main())
