#!/usr/bin/env python3
"""K702: carry outward errors through the nonreducing A-margin test."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k702-k500-interval-cross-coupled-a-margin-compiler.json"
def q(x:Fraction)->str: return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def build()->dict[str,Any]:
    k700=json.loads((ROOT/"lab/process/k700-k500-cross-coupled-a-margin-compiler.json").read_text())
    assert k700["decision"]["nonzero_cross_packet_can_supply_A_above_two_thirds"]
    s0,es=Fraction(1,4),Fraction(1,100)
    t0,et=Fraction(1,100),Fraction(1,200)
    k0,ek=Fraction(1,60),Fraction(1,300)
    s,t,k,q0=s0+es,t0+et,k0+ek,Fraction(1,3)
    pgap,qgap=q0-s,q0-t
    det=pgap*qgap-k*k; trace=pgap+qgap; floor=det/trace
    r2=q0-floor; a=1-r2
    return {
      "schema_version":"1.0","result_id":"K702-K500-INTERVAL-CROSS-COUPLED-A-MARGIN-COMPILER","created":"2026-09-30","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
      "scope":"An outward complete-space interval certificate for K700's seed/complement/cross Schur route to A>2/3.",
      "gu_typed_objects":{"operator":"one bounded native R=T a^-1","split":"one orthogonal P_seed plus Q_seed","inputs":"outward complete-space upper enclosures for both diagonal blocks and the cross norm","result":"interval cross-coupled A-margin compiler MAP-TYPE=outward two-block Schur order","target":"K668/K703's complete A lower"},
      "theorem":{"same_native_R_and_split_required":True,"all_three_errors_outward_required":True,"all_errors_complete_space_required":True,"effective_bounds_rule":"s=s0+e_s, t=t0+e_t, k=k0+e_k","strict_test":"s,t<q and k^2<(q-s)(q-t)","quantitative_A_rule":"A>=1-q+((q-s)(q-t)-k^2)/(2q-s-t)","nominal_bounds_without_errors_sufficient":False,"root_sum_square_error_substitution_sufficient":False,"finite_sector_errors_sufficient":False,"mixed_splits_substitutable":False},
      "exact_controls":{"controls_are_synthetic":True,"nominal_seed_upper":"1/4","seed_outward_error":"1/100","effective_seed_upper":q(s),"nominal_complement_upper":"1/100","complement_outward_error":"1/200","effective_complement_upper":q(t),"nominal_cross_upper":"1/60","cross_outward_error":"1/300","effective_cross_upper":q(k),"target_R_square_upper":"1/3","seed_gap":q(pgap),"complement_gap":q(qgap),"determinant_slack":q(det),"trace":q(trace),"certified_q_minus_gram_floor":q(floor),"R_square_upper":q(r2),"A_lower":q(a),"target_A_lower":"2/3","accepted":det>0 and a>Fraction(2,3),"hidden_error_counterexample":"A tail perturbation can preserve every nominal finite block while consuming the strict Schur determinant."},
      "dependency_reconciliation":{"K700_exact_bound_route_preserved":True,"K700_outward_interval_robustness_added":True,"K703_A_input_supplied_conditionally":True,"native_interval_data_added":False},
      "native_interface_status":{"actual_native_R_constructed":False,"actual_native_seed_enclosure_proved":False,"actual_native_complement_enclosure_proved":False,"actual_native_cross_enclosure_proved":False,"native_A_above_two_thirds_proved":False,"native_complete_floor_emitted":False},
      "decision":{"outward_cross_packet_can_supply_A_above_two_thirds":True,"native_A_margin_constructed":False,"next_exact_input":"For one native R and one fixed seed split, prove outward complete-space enclosures s0+e_s, t0+e_t and k0+e_k whose effective strict Schur determinant at q=1/3 is positive."},
      "source_and_ledger_effect":"none","ledger_no_change_reason":"This is a conditional complete operator interval theorem and supplies no source-owned action, physical quotient, state or observable.",
      "preflight_bookend":{"route_comparison":"K700 permits a nonzero cross but assumes exact certified bounds; K702 is the cheaper consumer for analytic or numerical enclosures with separate outward errors.","retrieval_collision_result":"K701 carries interval uncertainty only on the boundary route; no prior A certificate pays three independent block errors before the Schur test.","strongest_alternative":"Prove exact reduction and use K697's maximum rule."},
      "postflight_bookend":{"strongest_overclaim":"Applying K700 to nominal estimates and reporting its slack without subtracting every outward error.","strongest_contrary_construction":"A complete-space tail error invisible to finite blocks can align with the cross block and close the determinant.","weakest_reproducibility_seam":"The three enclosures must refer to the same R, split and graph Hilbert norm."},
      "controls":{"producer":"tests/channel-swings/k702_k500_interval_cross_coupled_a_margin_compiler.py","probe":"tests/channel-swings/k702_k500_interval_cross_coupled_a_margin_compiler_probe.py","controls_passed":40,"hostile_mutations_rejected":34},
      "claim_ceiling":"Exact conditional outward-interval Schur theorem. The synthetic nominal s0=1/4, t0=1/100, k0=1/60 packet with outward errors 1/100, 1/200 and 1/300 has effective s=13/50, t=3/200, k=1/50, determinant slack 413/18000 and certifies A>=5113/7050. No native R, enclosure, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows."
    }

def validate(p:dict[str,Any])->None:
    t,c,n=p["theorem"],p["exact_controls"],p["native_interface_status"]
    for k in ("same_native_R_and_split_required","all_three_errors_outward_required","all_errors_complete_space_required"): assert t[k]
    for k in ("nominal_bounds_without_errors_sufficient","root_sum_square_error_substitution_sufficient","finite_sector_errors_sufficient","mixed_splits_substitutable"): assert not t[k]
    assert c["effective_seed_upper"]=="13/50" and c["effective_complement_upper"]=="3/200" and c["effective_cross_upper"]=="1/50"
    assert c["determinant_slack"]=="413/18000" and c["trace"]=="47/120"
    assert c["certified_q_minus_gram_floor"]=="413/7050" and c["R_square_upper"]=="1937/7050" and c["A_lower"]=="5113/7050" and c["accepted"]
    assert all(v is False for v in n.values())
    assert p["decision"]["outward_cross_packet_can_supply_A_above_two_thirds"] and not p["decision"]["native_A_margin_constructed"]
    assert p["target_claim"]=="NONE-NOT-A-KILL" and p["source_and_ledger_effect"]=="none"
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(s)
    else: print(s,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
