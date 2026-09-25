#!/usr/bin/env python3
"""Independent controls and hostile mutations for K457."""

from __future__ import annotations

import copy

from k457_k152_shifted_residual_gram_reduction import demo


def controls(packet):
    gram = packet.get("finite_gram_payload", {})
    tail = packet.get("tail_budget", {})
    exact = packet.get("exact_control", {})
    release = packet.get("release_test", {})
    decision = packet.get("decision", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K457-K152-M-DUAL-RESIDUAL-GRAM-REDUCTION"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("vectors", gram.get("resolved_vectors") == 2958),
        ("groups", gram.get("coherent_groups") == 201),
        ("entries", gram.get("self_and_cross_entries") == 59586),
        ("high entries", gram.get("orders_7_through_12_entries_reused_from_K279") == 59234),
        ("low entries", gram.get("orders_2_through_6_entries") == 352),
        ("coefficients", gram.get("all_K179_coefficients_retained") is True),
        ("cross terms", gram.get("all_cross_terms_within_coherent_groups_required") is True),
        ("epsilon", tail.get("epsilon") == "3011499/838860800"),
        ("post adjoint", tail.get("post_left_adjoint") is True),
        ("control", exact.get("contains_finite_square") is True),
        ("M residual serialized", release.get("complete_M_dual_residual_serialized") is True),
        ("M residual not evaluated", release.get("complete_M_dual_residual_numerically_evaluated") is False),
        ("shifted residual not serialized", release.get("complete_shifted_form_dual_residual_serialized") is False),
        ("no coercivity", release.get("coercivity_serialized") is False),
        ("no interval", release.get("native_K152_interval_emitted") is False),
        ("column released", decision.get("K455_column_reference_released") is True),
        ("M residual released", decision.get("K455_M_dual_residual_reference_released") is True),
        ("shifted residual held", decision.get("K455_shifted_form_dual_residual_reference_released") is False),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K456"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["finite_gram_payload"].__setitem__("resolved_vectors", 2957),
        lambda d: d["finite_gram_payload"].__setitem__("coherent_groups", 200),
        lambda d: d["finite_gram_payload"].__setitem__("self_and_cross_entries", 59234),
        lambda d: d["finite_gram_payload"].__setitem__("orders_7_through_12_entries_reused_from_K279", 0),
        lambda d: d["finite_gram_payload"].__setitem__("orders_2_through_6_entries", 0),
        lambda d: d["finite_gram_payload"].__setitem__("all_K179_coefficients_retained", False),
        lambda d: d["finite_gram_payload"].__setitem__("all_cross_terms_within_coherent_groups_required", False),
        lambda d: d["tail_budget"].__setitem__("epsilon", "0"),
        lambda d: d["tail_budget"].__setitem__("post_left_adjoint", False),
        lambda d: d["exact_control"].__setitem__("contains_finite_square", False),
        lambda d: d["release_test"].__setitem__("complete_M_dual_residual_serialized", False),
        lambda d: d["release_test"].__setitem__("complete_M_dual_residual_numerically_evaluated", True),
        lambda d: d["release_test"].__setitem__("complete_shifted_form_dual_residual_serialized", True),
        lambda d: d["release_test"].__setitem__("coercivity_serialized", True),
        lambda d: d["release_test"].__setitem__("native_K152_interval_emitted", True),
        lambda d: d["decision"].__setitem__("K455_column_reference_released", False),
        lambda d: d["decision"].__setitem__("K455_M_dual_residual_reference_released", False),
        lambda d: d["decision"].__setitem__("K455_shifted_form_dual_residual_reference_released", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        if not all(ok for _, ok in controls(candidate)):
            rejected += 1
    print(f"K457 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K457 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
