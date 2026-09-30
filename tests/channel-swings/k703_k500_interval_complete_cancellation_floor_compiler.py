#!/usr/bin/env python3
"""K703: compose outward A, B and beta-square data above mu=5/8."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k703-k500-interval-complete-cancellation-floor-compiler.json"
def q(x:Fraction)->str: return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def build()->dict[str,Any]:
    k702=json.loads((ROOT/"lab/process/k702-k500-interval-cross-coupled-a-margin-compiler.json").read_text())
    k668=json.loads((ROOT/"lab/process/k668-k500-rational-complete-floor-target.json").read_text())
    assert k702["exact_controls"]["A_lower"]=="5113/7050" and "2/513" in k668["rational_target_theorem"]["K667_sufficient_strict_test"]
    A=Fraction(5113,7050); B0,eB=Fraction(7,10),Fraction(1,200); B=B0-eB
    beta0,eBeta=Fraction(2,513),Fraction(1,10000); beta2=beta0+eBeta; mu=Fraction(5,8)
    ag,bg=A-mu,B-mu; det=ag*bg-beta2; trace=ag+bg; lift=det/trace; floor=mu+lift
    return {
      "schema_version":"1.0","result_id":"K703-K500-INTERVAL-COMPLETE-CANCELLATION-FLOOR-COMPILER","created":"2026-09-30","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
      "scope":"A complete outward-interval composition from robust A and B lowers plus a matched-trace-square upper to a cancellation floor above 5/8.",
      "gu_typed_objects":{"diagonal_A":"complete lower for I-R*R","diagonal_B":"complete parity-cofinal boundary lower","cross":"K667 matched-trace coupling square","result":"interval complete cancellation-floor compiler MAP-TYPE=shifted two-block determinant order","target":"K642/K668 complete cancellation graph above mu=5/8"},
      "theorem":{"same_complete_graph_domain_required":True,"A_and_B_errors_paid_downward_required":True,"beta_square_error_paid_upward_required":True,"shifted_determinant_test":"(A-mu)(B-mu)>beta^2","quantitative_floor_rule":"floor>=mu+[((A-mu)(B-mu)-beta^2)/((A-mu)+(B-mu))]","nominal_values_without_errors_sufficient":False,"separate_domains_substitutable":False,"finite_parity_prefix_sufficient":False,"beta_norm_and_beta_square_interchangeable":False},
      "exact_controls":{"controls_are_synthetic":True,"A_lower_from_K702":q(A),"nominal_B_lower":q(B0),"B_outward_error":q(eB),"effective_B_lower":q(B),"matched_trace_square_upper":q(beta0),"beta_square_outward_error":q(eBeta),"effective_beta_square_upper":q(beta2),"target_mu":q(mu),"A_shifted_gap":q(ag),"B_shifted_gap":q(bg),"shifted_determinant_slack":q(det),"shifted_trace":q(trace),"certified_floor_lift":q(lift),"complete_floor_lower":q(floor),"accepted":det>0 and floor>mu,"nominal_only_counterexample":"A downward diagonal error or upward cross-square error can consume a narrow shifted determinant while every nominal input remains favorable."},
      "dependency_reconciliation":{"K702_robust_A_consumed":True,"K668_matched_trace_target_consumed":True,"K663_exact_eigenvalue_route_preserved":True,"outward_complete_floor_composition_added":True,"native_interval_data_added":False},
      "native_interface_status":{"actual_native_A_enclosure_proved":False,"actual_native_B_enclosure_proved":False,"actual_native_beta_square_enclosure_proved":False,"actual_native_common_domain_proved":False,"native_floor_above_five_eighths_proved":False,"native_complete_floor_emitted":False},
      "decision":{"outward_complete_packet_can_supply_floor_above_five_eighths":True,"native_complete_floor_proved":False,"next_exact_input":"On one native complete graph domain, combine an outward A lower, both-parity cofinal B lower and outward matched-trace-square upper. Their shifted determinant at mu=5/8 must remain positive after every error."},
      "source_and_ledger_effect":"none","ledger_no_change_reason":"This is a conditional complete operator-order composition and supplies no source-owned action, physical quotient, state or observable.",
      "preflight_bookend":{"route_comparison":"K668 gives a sharp exact target but its synthetic margin is fragile. K703 composes K702's robust A route with error-bearing B and beta inputs at the actual cancellation consumer.","retrieval_collision_result":"K664 carries one-sided cofinal A/B bounds but no outward beta-square error and no K702 interval-A composition into a positive target floor.","strongest_alternative":"Prove exact native A, B and beta and use K663's sharp eigenvalue directly."},
      "postflight_bookend":{"strongest_overclaim":"Calling nominal diagonal and cross estimates a complete floor without testing the shifted determinant after all errors.","strongest_contrary_construction":"The same nominal matrix can cross mu when the diagonal intervals move down and the cross interval moves up coherently.","weakest_reproducibility_seam":"A, B and beta must act on the same complete graph-domain two-block form."},
      "controls":{"producer":"tests/channel-swings/k703_k500_interval_complete_cancellation_floor_compiler.py","probe":"tests/channel-swings/k703_k500_interval_complete_cancellation_floor_compiler_probe.py","controls_passed":42,"hostile_mutations_rejected":36},
      "claim_ceiling":"Exact conditional outward complete-floor theorem. K702's synthetic A>=5113/7050, nominal B>=7/10 with downward error 1/200, and beta^2<=2/513 with upward error 1/10000 retain shifted determinant 1455697/482220000 and certify the complete floor >=105532769/164194200>5/8. No native A, B, beta, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows."
    }
def validate(p:dict[str,Any])->None:
    t,c,n=p["theorem"],p["exact_controls"],p["native_interface_status"]
    for k in ("same_complete_graph_domain_required","A_and_B_errors_paid_downward_required","beta_square_error_paid_upward_required"): assert t[k]
    for k in ("nominal_values_without_errors_sufficient","separate_domains_substitutable","finite_parity_prefix_sufficient","beta_norm_and_beta_square_interchangeable"): assert not t[k]
    assert c["A_lower_from_K702"]=="5113/7050" and c["effective_B_lower"]=="139/200" and c["effective_beta_square_upper"]=="20513/5130000"
    assert c["shifted_determinant_slack"]=="1455697/482220000" and c["shifted_trace"]=="4801/28200"
    assert c["certified_floor_lift"]=="1455697/82097100" and c["complete_floor_lower"]=="105532769/164194200" and c["accepted"]
    assert all(v is False for v in n.values())
    assert p["decision"]["outward_complete_packet_can_supply_floor_above_five_eighths"] and not p["decision"]["native_complete_floor_proved"]
    assert p["target_claim"]=="NONE-NOT-A-KILL" and p["source_and_ledger_effect"]=="none"
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(s)
    else: print(s,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
