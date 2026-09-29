#!/usr/bin/env python3
"""Independent controls and hostile mutations for K634."""

from __future__ import annotations

import copy
import json

from k634_k500_equivalent_domain_repair_obstruction import build


def controls(p: dict) -> list[bool]:
    w = p["reciprocity_witness"]
    t = p["equivalent_norm_theorem"]
    c = p["bounded_correlation_corollary"]
    s = p["surviving_domain_class"]
    r = p["dependency_reconciliation"]
    d = p["decision"]
    return [
        p["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(w["samples"]) == 4,
        w["lower_is_unbounded"] is True,
        w["positive_diagonal_domain_with_both_requirements_exists"] is False,
        t["underlying_domain_set_is_unchanged"] is True,
        t["membership_of_boundary_profile_is_unchanged"] is True,
        t["continuity_of_every_linear_trace_is_invariant"] is True,
        t["unbounded_trace_cannot_become_bounded"] is True,
        len(t["excluded_repairs"]) == 4,
        c["chart_membership_repaired"] is False,
        c["point_trace_continuity_repaired"] is False,
        c["same_domain_K611_product_well_typed"] is False,
        c["bounded_correlation_is_genuinely_new_domain"] is False,
        s["unbounded_or_noninvertible_change_of_topology_not_excluded"] is True,
        s["genuinely_non_equivalent_correlated_domain_not_excluded"] is True,
        s["constraint_graph_encoding_cross_channel_cancellation_not_excluded"] is True,
        s["complete_matched_form_estimated_before_factor_separation_not_excluded"] is True,
        s["coefficient_specific_native_tail_not_excluded"] is True,
        s["named_quantitative_floor_constructed"] is False,
        r["K174_diagonal_weight_obstruction_retracted"] is False,
        r["K611_mixed_graph_splice_obstruction_retracted"] is False,
        r["K612_quantitative_custody_gap_retracted"] is False,
        r["positive_diagonal_repair_class_strictly_extended"] is True,
        d["bounded_equivalent_domain_repair_route_closed"] is True,
        d["all_correlated_domains_ruled_out"] is False,
        d["named_complete_sector_floor_emitted"] is False,
        d["K473_released"] is False,
        p["source_and_ledger_effect"] == "none",
    ]


def set_path(p: dict, path: tuple[object, ...], value: object) -> None:
    cursor = p
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def main() -> int:
    payload = build()
    assert all(controls(payload))
    mutations = [
        (("classification",), "SUPPORTED"),
        (("direction",), "native_to_observed"),
        (("target_claim",), "SC-META-53"),
        (("reciprocity_witness", "samples"), []),
        (("reciprocity_witness", "lower_is_unbounded"), False),
        (("reciprocity_witness", "positive_diagonal_domain_with_both_requirements_exists"), True),
        (("equivalent_norm_theorem", "underlying_domain_set_is_unchanged"), False),
        (("equivalent_norm_theorem", "membership_of_boundary_profile_is_unchanged"), False),
        (("equivalent_norm_theorem", "continuity_of_every_linear_trace_is_invariant"), False),
        (("equivalent_norm_theorem", "unbounded_trace_cannot_become_bounded"), False),
        (("equivalent_norm_theorem", "excluded_repairs"), []),
        (("bounded_correlation_corollary", "chart_membership_repaired"), True),
        (("bounded_correlation_corollary", "point_trace_continuity_repaired"), True),
        (("bounded_correlation_corollary", "same_domain_K611_product_well_typed"), True),
        (("bounded_correlation_corollary", "bounded_correlation_is_genuinely_new_domain"), True),
        (("surviving_domain_class", "unbounded_or_noninvertible_change_of_topology_not_excluded"), False),
        (("surviving_domain_class", "genuinely_non_equivalent_correlated_domain_not_excluded"), False),
        (("surviving_domain_class", "constraint_graph_encoding_cross_channel_cancellation_not_excluded"), False),
        (("surviving_domain_class", "complete_matched_form_estimated_before_factor_separation_not_excluded"), False),
        (("surviving_domain_class", "named_quantitative_floor_constructed"), True),
        (("dependency_reconciliation", "K174_diagonal_weight_obstruction_retracted"), True),
        (("dependency_reconciliation", "K611_mixed_graph_splice_obstruction_retracted"), True),
        (("dependency_reconciliation", "positive_diagonal_repair_class_strictly_extended"), False),
        (("decision", "all_correlated_domains_ruled_out"), True),
        (("decision", "named_complete_sector_floor_emitted"), True),
    ]
    caught = 0
    for path, value in mutations:
        case = copy.deepcopy(payload)
        set_path(case, path, value)
        caught += int(not all(controls(case)))
    assert caught == len(mutations)
    print(json.dumps({"controls_passed": len(controls(payload)), "hostile_mutations_rejected": caught}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
