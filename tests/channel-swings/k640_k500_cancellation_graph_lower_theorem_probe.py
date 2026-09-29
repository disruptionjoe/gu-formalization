#!/usr/bin/env python3
"""Independent controls and hostile mutations for K640."""

from __future__ import annotations

import copy

from k640_k500_cancellation_graph_lower_theorem import build


def controls(p: dict) -> list[bool]:
    t = p["trace_and_domain_theorem"]
    q = p["parameterized_lower_theorem"]
    n = p["native_interface_status"]
    d = p["decision"]
    return [
        p["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        p["direction"] == "observed_to_native",
        p["source_and_ledger_effect"] == "none",
        t["channel_dimension"] == 6,
        t["base_domain_dense"] is True,
        t["cancellation_domain_dense"] is True,
        t["cancellation_domain_strictly_larger"] is True,
        t["decomposition_unique"] is True,
        t["coefficient_projection_continuous_with_norm"] == "1",
        t["matched_trace_continuous"] is True,
        t["beta_squared_integral_test_upper"] == "258/66049",
        t["beta_squared_simple_upper"] == "1/256",
        t["beta_squared_strictly_below_one_over_256"] is True,
        len(t["finite_controls"]) == 5,
        all(row["below_one_over_256"] for row in t["finite_controls"]),
        q["young_parameter"] == "1/2",
        q["floor_function"] == "min(1/2,m-1/128)",
        q["all_finite_Hermitian_boundary_matrices_semibounded_on_same_graph"] is True,
        q["separate_singular_factor_estimates_used"] is False,
        q["diagonal_weight_graph_splice_used"] is False,
        q["reference_control_m"] == "-2",
        q["reference_control_floor"] == "-257/128",
        q["reference_control_is_actual_K139_K168_floor"] is False,
        n["K639_actual_six_channel_coordinate_consumed"] is True,
        n["non_equivalent_cancellation_graph_consumed"] is True,
        n["same_domain_lower_method_constructed"] is True,
        n["actual_complete_regular_core_matrix_identified"] is False,
        n["actual_complete_regular_core_lower_m_identified"] is False,
        n["actual_K139_K168_form_equal_to_parameterized_q_B_proved"] is False,
        n["named_complete_sector_floor_emitted"] is False,
        n["K473_released"] is False,
        n["native_K152_interval_emitted"] is False,
    ]


def mutations(payload: dict):
    specs = [
        (("classification",), "SOURCE_RESULT"),
        (("trace_and_domain_theorem", "channel_dimension"), 16),
        (("trace_and_domain_theorem", "base_domain_dense"), False),
        (("trace_and_domain_theorem", "cancellation_domain_dense"), False),
        (("trace_and_domain_theorem", "cancellation_domain_strictly_larger"), False),
        (("trace_and_domain_theorem", "decomposition_unique"), False),
        (("trace_and_domain_theorem", "coefficient_projection_continuous_with_norm"), "infinite"),
        (("trace_and_domain_theorem", "matched_trace_continuous"), False),
        (("trace_and_domain_theorem", "beta_squared_integral_test_upper"), "1"),
        (("trace_and_domain_theorem", "beta_squared_simple_upper"), "1"),
        (("trace_and_domain_theorem", "beta_squared_strictly_below_one_over_256"), False),
        (("trace_and_domain_theorem", "finite_controls"), []),
        (("parameterized_lower_theorem", "young_parameter"), "2"),
        (("parameterized_lower_theorem", "floor_function"), "m"),
        (("parameterized_lower_theorem", "all_finite_Hermitian_boundary_matrices_semibounded_on_same_graph"), False),
        (("parameterized_lower_theorem", "separate_singular_factor_estimates_used"), True),
        (("parameterized_lower_theorem", "diagonal_weight_graph_splice_used"), True),
        (("parameterized_lower_theorem", "reference_control_floor"), "-2"),
        (("parameterized_lower_theorem", "reference_control_is_actual_K139_K168_floor"), True),
        (("native_interface_status", "K639_actual_six_channel_coordinate_consumed"), False),
        (("native_interface_status", "non_equivalent_cancellation_graph_consumed"), False),
        (("native_interface_status", "same_domain_lower_method_constructed"), False),
        (("native_interface_status", "actual_complete_regular_core_matrix_identified"), True),
        (("native_interface_status", "actual_complete_regular_core_lower_m_identified"), True),
        (("native_interface_status", "actual_K139_K168_form_equal_to_parameterized_q_B_proved"), True),
        (("native_interface_status", "named_complete_sector_floor_emitted"), True),
        (("source_and_ledger_effect",), "moved"),
    ]
    for path, value in specs:
        mutant = copy.deepcopy(payload)
        target = mutant
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        yield mutant


def main() -> int:
    payload = build()
    base = controls(payload)
    assert len(base) == 32 and all(base)
    rejected = sum(not all(controls(mutant)) for mutant in mutations(payload))
    assert rejected == 27
    print("K640 independent controls: 32/32 passed")
    print("K640 hostile mutations: 27/27 rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
