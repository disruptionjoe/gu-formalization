#!/usr/bin/env python3
"""Hostile mutations for K879."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k879_sc_act_06_full_field_quotient_injection.py"
def load():
    s=importlib.util.spec_from_file_location("k879",SCRIPT); assert s and s.loader;m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main()->int:
    m=load();base=m.build();mut=[
      lambda p:p.__setitem__("target_claim","SC-ACT-05"),lambda p:p.__setitem__("classification","CONDITIONAL_COMPARATOR"),lambda p:p.__setitem__("pinned_inputs",{}),lambda p:p["injection_theorem"].__setitem__("pure_connection_kernel_embeds_in_full_kernel",False),lambda p:p["injection_theorem"].__setitem__("internal_gauge_image_is_radial",False),lambda p:p["injection_theorem"].__setitem__("radial_tangential_intersection_dimension",1),lambda p:p["injection_theorem"].__setitem__("metric_diffeomorphism_rank_at_nonzero_covector",3),lambda p:p["injection_theorem"].__setitem__("metric_diffeomorphism_symbol_is_injective",False),lambda p:p["injection_theorem"]["metric_diffeomorphism_injectivity_proof"].__setitem__("contract_one_leg","v=0"),lambda p:p["injection_theorem"].__setitem__("metric_diffeomorphism_connection_component_at_flat_T0",1),lambda p:p["injection_theorem"].__setitem__("fermionic_gauge_tangent_dimension_at_zero_background",1),lambda p:p["injection_theorem"].__setitem__("induced_map_on_quotients_is_injective",False),lambda p:p["injection_theorem"].__setitem__("common_stabilizer_equivariant",False),lambda p:p["exact_consequence"].__setitem__("connection_kernel_dimension",106511),lambda p:p["exact_consequence"].__setitem__("owned_radial_gauge_dimension",16383),lambda p:p["exact_consequence"].__setitem__("injected_tangential_quotient_dimension",90124),lambda p:p["exact_consequence"].__setitem__("complete_full_field_cohomology_dimension_computed",True),lambda p:p["exact_consequence"].__setitem__("uniform_on_positive_negative_and_null_real_covectors",False),lambda p:p["decision"].__setitem__("metric_diffeomorphisms_reduce_the_pure_tangential_quotient",True),lambda p:p["decision"].__setitem__("complete_full_field_cohomology_equals_the_injected_submodule",True)]
    rejected=0
    for f in mut:
        q=copy.deepcopy(base);f(q)
        try:m.validate(q)
        except (AssertionError,KeyError,ValueError):rejected+=1
    assert rejected==len(mut)==20;print("K879 probe: 20/20 hostile mutations rejected");return 0
if __name__=="__main__":raise SystemExit(main())
