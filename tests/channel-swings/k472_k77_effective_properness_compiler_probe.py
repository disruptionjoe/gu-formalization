#!/usr/bin/env python3
"""Independent controls and hostile mutations for K472."""

from __future__ import annotations

import copy

from k472_k77_effective_properness_compiler import compile_packet, demo


def controls(packet):
    contract = packet["decision_contract"]
    positive, obstruction = packet["positive_control"], packet["obstruction_control"]
    small, native = packet["smallness_counterexample"], packet["native_status"]
    return [
        ("schema", packet["schema_version"] == "1.0"),
        ("id", packet["result_id"] == "K472-K77-EFFECTIVE-PROPERNESS-COMPILER"),
        ("classification", packet["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet["direction"] == "observed_to_native"),
        ("inputs", len(contract["required_inputs"]) == 5 and "complete action-owned coefficients" in contract["required_inputs"]),
        ("rule", "transferred homology complex is acyclic" in contract["properness_rule"]),
        ("obstruction", "rejects properness" in contract["obstruction_rule"]),
        ("no smallness", contract["coefficient_smallness_alone_is_sufficient"] is False),
        ("control not native", contract["finite_control_is_native_action"] is False),
        ("positive effective", positive["effective_differential"] == "17/18"),
        ("positive determinant", positive["determinant"] == "17/12"),
        ("positive acyclic", positive["cohomology_dimensions"] == [0, 0] and positive["admitted"] is True),
        ("zero effective", obstruction["effective_differential"] == "0"),
        ("zero determinant", obstruction["determinant"] == "0"),
        ("obstruction survives", obstruction["cohomology_dimensions"] == [1, 1] and obstruction["admitted"] is False),
        ("small effective", small["effective_differential"] == "0"),
        ("small homology", small["cohomology_dimensions"] == [1, 1]),
        ("smallness boundary", small["small_coefficients_do_not_remove_base_homology"] is True),
        ("no action", native["actual_action_packet_present"] is False),
        ("no properness", native["native_properness_emitted"] is False),
        ("no physics", native["physical_cohomology_claimed"] is False),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["decision_contract"].__setitem__("required_inputs", []),
        lambda d: d["decision_contract"].__setitem__("properness_rule", "small coefficients"),
        lambda d: d["decision_contract"].__setitem__("obstruction_rule", "ignore"),
        lambda d: d["decision_contract"].__setitem__("coefficient_smallness_alone_is_sufficient", True),
        lambda d: d["decision_contract"].__setitem__("finite_control_is_native_action", True),
        lambda d: d["positive_control"].__setitem__("effective_differential", "0"),
        lambda d: d["positive_control"].__setitem__("determinant", "0"),
        lambda d: d["positive_control"].__setitem__("admitted", False),
        lambda d: d["obstruction_control"].__setitem__("effective_differential", "1"),
        lambda d: d["obstruction_control"].__setitem__("determinant", "1"),
        lambda d: d["obstruction_control"].__setitem__("admitted", True),
        lambda d: d["smallness_counterexample"].__setitem__("effective_differential", "1"),
        lambda d: d["smallness_counterexample"].__setitem__("cohomology_dimensions", [0, 0]),
        lambda d: d["smallness_counterexample"].__setitem__("small_coefficients_do_not_remove_base_homology", False),
        lambda d: d["native_status"].__setitem__("actual_action_packet_present", True),
        lambda d: d["native_status"].__setitem__("native_properness_emitted", True),
        lambda d: d["native_status"].__setitem__("physical_cohomology_claimed", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(ok for _, ok in controls(candidate))
    invalid = 0
    try:
        compile_packet(-1, 0, 0, 0)
    except ValueError:
        invalid += 1
    print(f"K472 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K472 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K472 INVALID INPUTS: {invalid}/1 rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) and invalid == 1 else 1


if __name__ == "__main__":
    raise SystemExit(main())
