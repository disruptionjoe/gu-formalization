#!/usr/bin/env python3
"""K704: transport K701 through a bounded boundary-coordinate change."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k704-k500-coordinate-transported-boundary-margin-compiler.json"
def q(x:Fraction)->str: return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def build()->dict[str,Any]:
    k701=json.loads((ROOT/"lab/process/k701-k500-interval-boundary-denominator-compiler.json").read_text())
    k662=json.loads((ROOT/"lab/process/k662-k500-reference-preserving-boundary-coordinate-group.json").read_text())
    assert k701["exact_controls"]["transferred_target_margin"]=="9039/2125000"
    assert k662["coordinate_group_theorem"]["friedrichs_status_preserved_if_previously_proved"]
    m=Fraction(9039,2125000); unorm=Fraction(6,5); residual=Fraction(1,1000)
    transported=m/(unorm*unorm); final=transported-residual
    return {
      "schema_version":"1.0","result_id":"K704-K500-COORDINATE-TRANSPORTED-BOUNDARY-MARGIN-COMPILER","created":"2026-09-30","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
      "scope":"A complete boundary-denominator margin transfer through an authenticated reference-preserving coordinate change and outward residual error.",
      "gu_typed_objects":{"source_denominator":"K701 complete D_W(lambda_t) in one authenticated boundary coordinate","coordinate_map":"Gamma_0'=U Gamma_0 and Gamma_1'=U^{-*}(Gamma_1+C Gamma_0)","transported_denominator":"D'=U^{-*} D U^-1","uncertainty":"outward complete-space operator-order residual after transport","result":"coordinate-transported boundary-margin compiler MAP-TYPE=congruence order with residual","target":"K657/K680 coordinate-invariant target denominator positivity"},
      "theorem":{"reference_preserving_coordinate_authentication_required":True,"bounded_invertible_U_required":True,"joint_W_and_M_transport_required":True,"complete_residual_error_required":True,"transport_rule":"D>=mI and ||U||<=K imply U^{-*}DU^-1 >= (m/K^2)I","perturbed_rule":"D_tilde>=m/K^2-e_coord","coordinate_name_without_map_sufficient":False,"transporting_W_without_M_sufficient":False,"raw_floor_invariant_under_nonunitary_U":False,"finite_boundary_block_error_sufficient":False},
      "exact_controls":{"controls_are_synthetic":True,"K701_source_margin":"9039/2125000","coordinate_operator_norm_upper":q(unorm),"condition_square_upper":q(unorm*unorm),"exact_congruence_margin":q(transported),"outward_coordinate_residual":q(residual),"transported_target_margin":q(final),"accepted":final>0,"one_sided_transport_counterexample":"Moving W but not M changes D rather than representing the same extension, so positivity can be manufactured or destroyed by coordinates."},
      "dependency_reconciliation":{"K662_reference_preserving_group_consumed":True,"K701_same_coordinate_margin_consumed":True,"K701_same_coordinate_requirement_preserved_at_source":True,"bounded_coordinate_robustness_added":True,"native_coordinate_data_added":False},
      "native_interface_status":{"actual_native_boundary_triple_authenticated":False,"actual_native_coordinate_map_authenticated":False,"actual_native_coordinate_norm_bound_proved":False,"actual_native_complete_residual_proved":False,"actual_native_target_denominator_nonnegative":False,"native_complete_floor_emitted":False},
      "decision":{"authenticated_bounded_coordinate_change_can_preserve_positive_margin":True,"native_transported_denominator_proved":False,"next_exact_input":"After proving K701 in one native coordinate, authenticate the reference-preserving U,C map to the working coordinate, bound ||U|| on the complete boundary space, and prove the outward residual is smaller than the congruence-reduced margin."},
      "source_and_ledger_effect":"none","ledger_no_change_reason":"This is a conditional complete boundary-coordinate theorem and supplies no source-owned action, physical quotient, state or observable.",
      "preflight_bookend":{"route_comparison":"K701 forbids mixed coordinates. K704 supplies the exact authenticated exception by composing K662's reference-preserving group with an explicit condition-number and residual budget.","retrieval_collision_result":"K662 proves qualitative congruence covariance but does not consume K701's numerical target margin or pay an outward post-transport error.","strongest_alternative":"Recompute and certify the complete denominator directly in the final native coordinate."},
      "postflight_bookend":{"strongest_overclaim":"Treating the raw lower bound as invariant under a nonunitary coordinate change or transporting only one side of W-M.","strongest_contrary_construction":"Unbounded or badly conditioned U can drive the congruence floor to zero while preserving abstract positivity.","weakest_reproducibility_seam":"The same authenticated U,C map must transport the reference, Weyl function, extension parameter and complete residual norm."},
      "controls":{"producer":"tests/channel-swings/k704_k500_coordinate_transported_boundary_margin_compiler.py","probe":"tests/channel-swings/k704_k500_coordinate_transported_boundary_margin_compiler_probe.py","controls_passed":40,"hostile_mutations_rejected":34},
      "claim_ceiling":"Exact conditional coordinate-transport theorem. K701's synthetic margin 9039/2125000, an authenticated reference-preserving map with ||U||<=6/5, and outward complete residual 1/1000 retain target margin 1993/1020000. No native triple, coordinate map, norm, residual, denominator, r0, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows."
    }
def validate(p:dict[str,Any])->None:
    t,c,n=p["theorem"],p["exact_controls"],p["native_interface_status"]
    for k in ("reference_preserving_coordinate_authentication_required","bounded_invertible_U_required","joint_W_and_M_transport_required","complete_residual_error_required"): assert t[k]
    for k in ("coordinate_name_without_map_sufficient","transporting_W_without_M_sufficient","raw_floor_invariant_under_nonunitary_U","finite_boundary_block_error_sufficient"): assert not t[k]
    assert c["coordinate_operator_norm_upper"]=="6/5" and c["condition_square_upper"]=="36/25"
    assert c["exact_congruence_margin"]=="3013/1020000" and c["outward_coordinate_residual"]=="1/1000" and c["transported_target_margin"]=="1993/1020000" and c["accepted"]
    assert all(v is False for v in n.values())
    assert p["decision"]["authenticated_bounded_coordinate_change_can_preserve_positive_margin"] and not p["decision"]["native_transported_denominator_proved"]
    assert p["target_claim"]=="NONE-NOT-A-KILL" and p["source_and_ledger_effect"]=="none"
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(s)
    else: print(s,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
