#!/usr/bin/env python3
"""Independent controls and hostile mutations for K455."""

from __future__ import annotations

import copy

from k455_k152_native_residual_readiness import demo


EXPECTED_MISSING = [
    "complete_continuum_action_column_ref",
    "complete_shifted_form_dual_residual_ref",
    "coercivity_ref",
    "next_distinct_spectrum_ref",
    "native_left_floor_ref",
]


def controls(packet):
    ready = packet.get("native_K152_readiness", {})
    decision = packet.get("decision", {})
    finite = packet.get("finite_diagnostic_disposition", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K455-K152-NATIVE-RESIDUAL-READINESS"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("form transfer", ready.get("same_family_form_transfer_complete") is True),
        ("Gram transfer", ready.get("same_family_physical_Gram_transfer_complete") is True),
        ("finite audit", ready.get("finite_independent_consumer_audit_complete") is True),
        ("finite joint transfer", ready.get("finite_joint_form_Gram_transfer_complete") is True),
        ("no column", ready.get("complete_continuum_action_column_serialized") is False),
        ("no residual", ready.get("complete_shifted_form_dual_residual_serialized") is False),
        ("missing exact", ready.get("missing_native_fields") == EXPECTED_MISSING),
        ("interface incomplete", ready.get("native_K152_interface_complete") is False),
        ("no interval", ready.get("native_K152_interval_emitted") is False),
        ("no substitute form", finite.get("may_substitute_for_fixed_limiting_K139_form") is False),
        ("no substitute column", finite.get("may_substitute_for_complete_K162_continuum_action_column") is False),
        ("finite no close", decision.get("finite_diagnostics_close_native_residual") is False),
        ("next input", "complete K156/K171 continuum action column" in decision.get("next_exact_input", "")),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K454"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["native_K152_readiness"].__setitem__("same_family_form_transfer_complete", False),
        lambda d: d["native_K152_readiness"].__setitem__("same_family_physical_Gram_transfer_complete", False),
        lambda d: d["native_K152_readiness"].__setitem__("finite_independent_consumer_audit_complete", False),
        lambda d: d["native_K152_readiness"].__setitem__("finite_joint_form_Gram_transfer_complete", False),
        lambda d: d["native_K152_readiness"].__setitem__("complete_continuum_action_column_serialized", True),
        lambda d: d["native_K152_readiness"].__setitem__("complete_shifted_form_dual_residual_serialized", True),
        lambda d: d["native_K152_readiness"].__setitem__("missing_native_fields", []),
        lambda d: d["native_K152_readiness"].__setitem__("native_K152_interface_complete", True),
        lambda d: d["native_K152_readiness"].__setitem__("native_K152_interval_emitted", True),
        lambda d: d["finite_diagnostic_disposition"].__setitem__("may_substitute_for_fixed_limiting_K139_form", True),
        lambda d: d["finite_diagnostic_disposition"].__setitem__("may_substitute_for_complete_K162_continuum_action_column", True),
        lambda d: d["decision"].__setitem__("finite_diagnostics_close_native_residual", True),
        lambda d: d["decision"].__setitem__("next_exact_input", "repeat finite audit"),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        if not all(ok for _, ok in controls(candidate)):
            rejected += 1
    print(f"K455 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K455 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
