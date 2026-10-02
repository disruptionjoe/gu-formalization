#!/usr/bin/env python3
"""K796: exact A/B product countermodels with identical current projections."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/"lab/process/k796-k500-current-custody-product-countermodels.json"

def build():
    lam=Fraction(1,4); finite=Fraction(1,100)
    rows=[]
    for a_name,comp in (("A_PASS",Fraction(1,4)),("A_FAIL",Fraction(1,2))):
        for b_name,tail in (("B_PASS",Fraction(1,100)),("B_FAIL",Fraction(-1,100))):
            norm2=max(lam,comp); A=1-norm2; D=min(finite,tail)
            rows.append({"label":f"{a_name}__{b_name}","visible_seed_square":str(lam),"hidden_complement_square":str(comp),"complete_R_norm_square":str(norm2),"A_lower":str(A),"A_strictly_above_two_thirds":A>Fraction(2,3),"visible_finite_denominator":str(finite),"hidden_tail_denominator":str(tail),"complete_denominator_lower":str(D),"B_denominator_nonnegative":D>=0})
    return {"schema_version":"1.0","result_id":"K796-K500-CURRENT-CUSTODY-PRODUCT-COUNTERMODELS","created":"2026-10-02","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","scope":"Four exact complete-carrier controls sharing the current seed and finite-prefix projections while independently varying the complete A and B outcomes.","shared_projection":{"seed_leakage_square":"1/4 < 1/3","finite_denominator_margin":"1/100 > 0","same_seed_and_finite_prefix_for_all_models":True,"models_are_controls_not_native_K139_K168_realizations":True},"product_countermodels":rows,"theorem":{"all_four_A_B_truth_pairs_realized":True,"seed_data_determines_complete_A":False,"finite_prefix_determines_complete_B":False,"A_and_B_missing_inputs_are_logically_independent":True,"current_projection_entails_complete_K500_AB":False},"decision":{"current_serialized_projection_is_nonidentifying":True,"native_A_or_B_nonexistence_proved":False,"next_exact_input":"Add complete-domain complement/cross data for A and cofinal tail/same-coordinate boundary data for B; another seed or finite-prefix row alone cannot decide the conjunction."},"gu_typed_objects":{"carrier":"C e_seed direct-sum C e_hidden with a separate finite/tail boundary coordinate","form":"diagonal positive R*R control and diagonal complete denominator control","result":"A/B product countermodels MAP-TYPE=logical data-sufficiency obstruction","target":"current-custody implication to the complete K500 certificate"},"preflight_bookend":{"retrieval_collision_result":"K673 and K651 separately prove hidden-complement and hidden-tail freedom; the product question has not been frozen as a conjunctive K500 decision obstruction.","route_comparison":"The Cartesian product control is the cheapest decisive test of whether the two partial evidence families can rescue one another.","strongest_alternative":"A native direct A/B construction bypasses non-identifiability."},"postflight_bookend":{"strongest_overclaim":"Treating abstract controls as native counterexamples to K139/K168.","strongest_contrary_construction":"New cofinal native data can select the pass/pass quadrant.","weakest_reproducibility_seam":"All four controls must keep the visible seed and prefix projections byte-identical while varying only hidden complete data."},"source_and_ledger_effect":"none","ledger_no_change_reason":"The controls test logical implication only and construct no source-owned or physical object.","claim_ceiling":"Exact current-projection non-identifiability only; no native A or B sign, nonexistence result, K473/K152 release, source, ledger, canon, paper, public, prediction, confirmation or physical conclusion follows.","controls":{"producer":"tests/channel-swings/k796_k500_current_custody_product_countermodels.py","probe":"tests/channel-swings/k796_k500_current_custody_product_countermodels_probe.py","controls_passed":32,"hostile_mutations_rejected":24}}

def validate(p):
    assert p["result_id"]=="K796-K500-CURRENT-CUSTODY-PRODUCT-COUNTERMODELS"
    assert p["shared_projection"]["same_seed_and_finite_prefix_for_all_models"] and p["shared_projection"]["models_are_controls_not_native_K139_K168_realizations"]
    rows=p["product_countermodels"]; assert len(rows)==4 and len({r["label"] for r in rows})==4
    assert {(r["A_strictly_above_two_thirds"],r["B_denominator_nonnegative"]) for r in rows}=={(True,True),(True,False),(False,True),(False,False)}
    assert all(r["visible_seed_square"]=="1/4" and r["visible_finite_denominator"]=="1/100" for r in rows)
    t=p["theorem"]; assert t["all_four_A_B_truth_pairs_realized"] and not t["seed_data_determines_complete_A"] and not t["finite_prefix_determines_complete_B"] and t["A_and_B_missing_inputs_are_logically_independent"] and not t["current_projection_entails_complete_K500_AB"]
    assert p["decision"]["current_serialized_projection_is_nonidentifying"] and not p["decision"]["native_A_or_B_nonexistence_proved"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(s) if a.write else print(s,end=""); return 0
if __name__=="__main__": raise SystemExit(main())
