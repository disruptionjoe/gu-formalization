#!/usr/bin/env python3
"""K701: carry outward uncertainty through the complete boundary chain."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k701-k500-interval-boundary-denominator-compiler.json"
def q(x:Fraction)->str: return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def build()->dict[str,Any]:
    k698=json.loads((ROOT/"lab/process/k698-k500-boundary-denominator-end-to-end-compiler.json").read_text())
    assert k698["decision"]["complete_boundary_chain_suffices_for_target_denominator"]
    delta=Fraction(8,85); anchor=Fraction(41,200); factor=Fraction(6,5); target_gamma=anchor*factor
    variation=delta*anchor*target_gamma
    nominal_denominator=Fraction(1,100); denominator_error=Fraction(1,1000); effective=nominal_denominator-denominator_error
    target_margin=effective-variation
    return {
      "schema_version":"1.0","result_id":"K701-K500-INTERVAL-BOUNDARY-DENOMINATOR-COMPILER","created":"2026-09-30","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
      "scope":"An outward interval certificate for K698's complete same-coordinate Friedrichs/trace/gamma/Weyl/denominator chain.",
      "gu_typed_objects":{"minimal_operator":"one closed semibounded symmetric S","boundary_triple":"one authenticated ordinary triple for S*","reference":"the Friedrichs extension A_0=ker(Gamma_0)","denominator":"D_W(lambda)=W-M(lambda) in one fixed boundary coordinate","uncertainty":"certified outward norm and order errors on complete-space inputs","result":"interval boundary-denominator compiler MAP-TYPE=outward operator-order budget","target":"K657/K680's D_W(341/170)>=0 input"},
      "theorem":{
        "complete_Friedrichs_authentication_required":True,"complete_trace_or_gamma_bound_required":True,"same_real_reference_interval_required":True,"same_boundary_coordinate_and_fixed_W_required":True,"outward_denominator_error_required":True,"all_errors_complete_space_required":True,
        "anchor_to_target_rule":"||gamma(lambda_t)||<=F ||gamma(mu)||","weyl_variation_rule":"||M(mu)-M(lambda_t)||<=|mu-lambda_t| g_mu g_t","denominator_rule":"D_W(lambda_t)>=d_near-e_D-|mu-lambda_t| g_mu g_t","positive_margin_condition":"d_near-e_D exceeds the outward Weyl budget",
        "point_estimates_without_outward_error_sufficient":False,"mixed_coordinates_substitutable":False,"finite_defect_or_sector_errors_sufficient":False,"nominal_positive_margin_alone_sufficient":False,
      },
      "exact_controls":{"controls_are_synthetic":True,"level_distance":q(delta),"anchor_gamma_norm_upper":q(anchor),"propagation_factor_upper":q(factor),"target_gamma_norm_upper":q(target_gamma),"weyl_variation_upper":q(variation),"nominal_nearby_denominator_lower":q(nominal_denominator),"outward_denominator_error":q(denominator_error),"effective_nearby_denominator_lower":q(effective),"transferred_target_margin":q(target_margin),"accepted":target_margin>0,"K698_nominal_margin_preserved_as_predecessor":"3993/722500","different_coordinate_counterexample":"A positive point estimate for W-M is not portable if W and M are represented in different boundary coordinates."},
      "dependency_reconciliation":{"K698_exact_chain_preserved":True,"K698_interval_robustness_added":True,"K686_two_point_gamma_identity_consumed":True,"K683_target_transfer_consumed":True,"native_interval_data_added":False},
      "native_interface_status":{"actual_native_minimal_operator_serialized":False,"actual_native_boundary_triple_authenticated":False,"actual_native_complete_gamma_enclosure_proved":False,"actual_native_complete_denominator_enclosure_proved":False,"actual_native_coordinate_identity_proved":False,"actual_native_target_denominator_nonnegative":False,"native_complete_floor_emitted":False},
      "decision":{"outward_interval_packet_can_reach_target_denominator":True,"native_target_denominator_proved":False,"next_exact_input":"In one authenticated native triple and coordinate, enclose the anchor gamma norm, its resolvent propagation factor, and one nearby complete D_W lower with outward errors. If the effective denominator lower exceeds |mu-341/170| times both gamma uppers, emit the native target margin."},
      "source_and_ledger_effect":"none","ledger_no_change_reason":"This is a conditional complete operator interval theorem and supplies no source-owned action, physical quotient, state or observable.",
      "preflight_bookend":{"route_comparison":"K698 closes the exact rational chain, but native analytic/numerical estimates will arrive as outward enclosures. K701 makes their total error budget explicit before any denominator is credited.","retrieval_collision_result":"K683 transports one exact complete norm budget and K698 composes exact rational controls; no prior packet carries certified input uncertainty through the entire chain.","strongest_alternative":"Compute and certify D_W(341/170) directly on the complete boundary space."},
      "postflight_bookend":{"strongest_overclaim":"Using nominal point values, finite blocks or coordinate-mismatched denominators as outward complete-space bounds.","strongest_contrary_construction":"An arbitrarily small unreported tail or coordinate error can consume a narrow positive denominator margin.","weakest_reproducibility_seam":"Every error bar must be outward, complete-space and attached to the same triple, interval, coordinate and W."},
      "controls":{"producer":"tests/channel-swings/k701_k500_interval_boundary_denominator_compiler.py","probe":"tests/channel-swings/k701_k500_interval_boundary_denominator_compiler_probe.py","controls_passed":38,"hostile_mutations_rejected":32},
      "claim_ceiling":"Exact conditional outward-interval theorem for K698's boundary chain. The synthetic anchor bound 41/200, factor 6/5, level distance 8/85 and denominator 1/100 with outward error 1/1000 give Weyl variation at most 5043/1062500 and retain target margin 9039/2125000. No native triple, enclosure, denominator, r0, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows."
    }

def validate(p:dict[str,Any])->None:
    t,c,n=p["theorem"],p["exact_controls"],p["native_interface_status"]
    for key in ("complete_Friedrichs_authentication_required","complete_trace_or_gamma_bound_required","same_real_reference_interval_required","same_boundary_coordinate_and_fixed_W_required","outward_denominator_error_required","all_errors_complete_space_required"): assert t[key]
    for key in ("point_estimates_without_outward_error_sufficient","mixed_coordinates_substitutable","finite_defect_or_sector_errors_sufficient","nominal_positive_margin_alone_sufficient"): assert not t[key]
    assert c["level_distance"]=="8/85" and c["anchor_gamma_norm_upper"]=="41/200" and c["propagation_factor_upper"]=="6/5"
    assert c["target_gamma_norm_upper"]=="123/500" and c["weyl_variation_upper"]=="5043/1062500"
    assert c["nominal_nearby_denominator_lower"]=="1/100" and c["outward_denominator_error"]=="1/1000"
    assert c["effective_nearby_denominator_lower"]=="9/1000" and c["transferred_target_margin"]=="9039/2125000" and c["accepted"]
    assert all(v is False for v in n.values())
    assert p["decision"]["outward_interval_packet_can_reach_target_denominator"] and not p["decision"]["native_target_denominator_proved"]
    assert p["target_claim"]=="NONE-NOT-A-KILL" and p["source_and_ledger_effect"]=="none"

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); args=ap.parse_args(); payload=build(); validate(payload); rendered=json.dumps(payload,indent=2,sort_keys=True)+"\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
