#!/usr/bin/env python3
"""Independent controls and hostile mutations for K595."""

from __future__ import annotations
import copy, json
from k595_k500_action_vector_coefficient_sufficiency import build


def controls(p):
    n,t,c,d=p["native_K177_inventory"],p["theorem"],p["exact_controls"],p["decision"]
    return [
        p["classification"]=="INTERNAL_STRUCTURAL_ONLY", p["direction"]=="observed_to_native",
        len(n["rows"])==2, n["orders_resolved"]==[0,12], n["exchange_topology_and_CAR_signs_serialized"] is True,
        n["laplace_simplex_integral_representation_serialized"] is True, n["coefficient_complete_base_action_column_evaluated"] is False,
        n["outward_numerical_prefix_integrals_evaluated"] is False, n["all_levels_beyond_order_12_serialized"] is False,
        "||v_n||^2" in t["minimum_sufficient_data"], "do not bound" in t["topology_is_insufficient"],
        t["spectral_diameter_not_required"] is True, t["full_operator_matrix_not_required"] is True, t["coefficient_weighted_action_vector_required"] is True,
        len(c["fixed_support_family"])==3, c["all_rows_same_exchange_support_count"] is True,
        c["leakage_changes_with_amplitude"] is True, c["expected_square_law"] is True, c["leakage_squares"]==["1","4","25"],
        d["K583_direct_vector_route_preserved"] is True, d["K593_spectral_diameter_route_reopened"] is False,
        d["K177_support_census_alone_bounds_leakage"] is False, d["required_successor_narrowed_to_three_moments_or_action_vector"] is True,
        d["complete_K500_uniform_leakage_emitted"] is False, d["native_noncyclic_floor_emitted"] is False,
        d["K473_released"] is False, d["native_K152_interval_emitted"] is False,
        p["source_and_ledger_effect"]=="none", p["target_claim"]=="NONE-NOT-A-KILL",
    ]


def set_path(p,path,value):
    x=p
    for key in path[:-1]: x=x[key]
    x[path[-1]]=value


def main():
    p=build(); assert all(controls(p))
    muts=[
        (("classification",),"SUPPORTED"),(("direction",),"native_to_observed"),(("native_K177_inventory","rows"),[]),
        (("native_K177_inventory","orders_resolved"),[0,1]),(("native_K177_inventory","exchange_topology_and_CAR_signs_serialized"),False),
        (("native_K177_inventory","laplace_simplex_integral_representation_serialized"),False),
        (("native_K177_inventory","coefficient_complete_base_action_column_evaluated"),True),
        (("native_K177_inventory","outward_numerical_prefix_integrals_evaluated"),True),(("native_K177_inventory","all_levels_beyond_order_12_serialized"),True),
        (("theorem","minimum_sufficient_data"),"unknown"),(("theorem","topology_is_insufficient"),"counts do bound"),
        (("theorem","spectral_diameter_not_required"),False),(("theorem","full_operator_matrix_not_required"),False),
        (("theorem","coefficient_weighted_action_vector_required"),False),(("exact_controls","fixed_support_family"),[]),
        (("exact_controls","all_rows_same_exchange_support_count"),False),(("exact_controls","leakage_changes_with_amplitude"),False),
        (("exact_controls","expected_square_law"),False),(("exact_controls","leakage_squares"),["1"]),
        (("decision","K583_direct_vector_route_preserved"),False),(("decision","K593_spectral_diameter_route_reopened"),True),
        (("decision","K177_support_census_alone_bounds_leakage"),True),(("decision","required_successor_narrowed_to_three_moments_or_action_vector"),False),
        (("decision","complete_K500_uniform_leakage_emitted"),True),(("decision","native_noncyclic_floor_emitted"),True),
        (("decision","K473_released"),True),(("decision","native_K152_interval_emitted"),True),
        (("source_and_ledger_effect",),"moved"),(("target_claim",),"SC-META-53"),
    ]
    rejected=0
    for path,value in muts:
        q=copy.deepcopy(p); set_path(q,path,value); rejected+=int(not all(controls(q)))
    assert rejected==len(muts)
    print(json.dumps({"controls_passed":len(controls(p)),"hostile_mutations_rejected":rejected},sort_keys=True)); return 0


if __name__=="__main__": raise SystemExit(main())
