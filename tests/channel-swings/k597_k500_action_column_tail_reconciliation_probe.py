#!/usr/bin/env python3
"""Independent controls and hostile mutations for K597."""

from __future__ import annotations
import copy, json
from k597_k500_action_column_tail_reconciliation import build


def controls(p):
    a,t,c,n,d=p["K456_representation_replay"],p["K574_tail_replay"],p["composition_theorem"],p["non_substitutability"],p["decision"]
    return [
        p["classification"]=="INTERNAL_STRUCTURAL_ONLY", p["direction"]=="observed_to_native",
        a["complete_continuum_action_column_serialized"] is True, a["coefficient_complete"] is True,
        a["all_order_tail_complete"] is True, a["complete_continuum_action_column_numerically_evaluated"] is False,
        a["resolved_orders"]==[2,12], a["resolved_term_count"]==2958, a["unresolved_required_field_instances"]==0,
        a["old_post_order_12_tail_norm_upper"]=="3011499/838860800",
        t["same_post_left_adjoint_location"] is True, t["same_geometric_tail_shape"] is True,
        t["resolved_through_order"]==12, t["sharp_post_order_12_tail_norm_upper"]=="9034497/33554432000",
        t["exact_improvement_factor"]=="40/3", t["sharp_tail_strictly_smaller"] is True,
        c["coefficient_serialization_already_complete"] is True, c["all_level_exchange_tail_already_serialized"] is True,
        c["K574_sharpens_but_does_not_create_representation_completeness"] is True,
        c["finite_vector_integrals_still_numerically_unevaluated"] is True,
        c["K595_support_only_diagnosis_preserved_for_K177"] is True, c["K595_global_next_input_corrected_by_K456_retrieval"] is True,
        c["minimum_remaining_numeric_payload"]==["||v_n||^2","<v_n,W_n v_n>","||W_n v_n||^2"],
        c["full_operator_matrix_not_required"] is True, c["full_spectrum_not_required"] is True,
        n["K575_is_a_K583_three_moment_evaluation"] is False, n["K575_interval_can_replace_K583_moments"] is False,
        d["K583_direct_vector_route_preserved"] is True, d["coefficient_reserialization_required"] is False,
        d["new_all_level_tail_derivation_required_before_numerics"] is False, d["numerical_three_moment_evaluation_required"] is True,
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
    muts=[]
    for i,ok in enumerate(controls(p)):
        assert ok, i
    muts=[
        (("classification",),"SUPPORTED"),(("direction",),"native_to_observed"),
        (("K456_representation_replay","complete_continuum_action_column_serialized"),False),
        (("K456_representation_replay","coefficient_complete"),False),(("K456_representation_replay","all_order_tail_complete"),False),
        (("K456_representation_replay","complete_continuum_action_column_numerically_evaluated"),True),
        (("K456_representation_replay","resolved_orders"),[2,11]),(("K456_representation_replay","resolved_term_count"),2957),
        (("K456_representation_replay","unresolved_required_field_instances"),1),
        (("K456_representation_replay","old_post_order_12_tail_norm_upper"),"0"),
        (("K574_tail_replay","same_post_left_adjoint_location"),False),(("K574_tail_replay","same_geometric_tail_shape"),False),
        (("K574_tail_replay","resolved_through_order"),11),(("K574_tail_replay","sharp_post_order_12_tail_norm_upper"),"0"),
        (("K574_tail_replay","exact_improvement_factor"),"1"),(("K574_tail_replay","sharp_tail_strictly_smaller"),False),
        (("composition_theorem","coefficient_serialization_already_complete"),False),
        (("composition_theorem","all_level_exchange_tail_already_serialized"),False),
        (("composition_theorem","K574_sharpens_but_does_not_create_representation_completeness"),False),
        (("composition_theorem","finite_vector_integrals_still_numerically_unevaluated"),False),
        (("composition_theorem","K595_support_only_diagnosis_preserved_for_K177"),False),
        (("composition_theorem","K595_global_next_input_corrected_by_K456_retrieval"),False),
        (("composition_theorem","minimum_remaining_numeric_payload"),[]),
        (("composition_theorem","full_operator_matrix_not_required"),False),(("composition_theorem","full_spectrum_not_required"),False),
        (("non_substitutability","K575_is_a_K583_three_moment_evaluation"),True),
        (("non_substitutability","K575_interval_can_replace_K583_moments"),True),
        (("decision","K583_direct_vector_route_preserved"),False),(("decision","coefficient_reserialization_required"),True),
        (("decision","new_all_level_tail_derivation_required_before_numerics"),True),
        (("decision","numerical_three_moment_evaluation_required"),False),
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
