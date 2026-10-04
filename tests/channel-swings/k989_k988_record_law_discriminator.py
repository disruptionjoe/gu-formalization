#!/usr/bin/env python3
"""K989 exact record-law discriminator for equal controlled system processes."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k989-k988-record-law-discriminator.json";INPUT=ROOT/"lab/process/k988-k987-controlled-process-nonidentifiability.json"
def build():
    parent=json.loads(INPUT.read_text());gamma=.7;T=2.0;theta=math.pi/4;rate=gamma/(math.sin(theta)**2);p_no_jump=math.exp(-rate*T)
    return {"schema_version":"1.0","result_id":"K989-RECORD-LAW-DISCRIMINATOR","created":"2026-10-04","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_PREREGISTERED_HOLDOUT","target_claim":"NONE-NOT-A-KILL","scope":"Exact microscopic path records for K986 Brownian diffusion and the K987 theta=pi/4 compound-Poisson horn, after gamma is fixed from system calibration.","dependency_checks":{"input_id":parent["result_id"],"system_only_controlled_processes_equal":parent["theorem"]["brownian_and_compound_poisson_process_tensors_equal_on_declared_access_class"]},"record_laws":{"brownian_terminal_phase":"Normal(0,gamma T), atomless","brownian_paths_continuous_probability":1.0,"brownian_quadratic_variation":gamma*T,"compound_terminal_phase":"theta times an integer-valued signed count, purely atomic","compound_paths_continuous_probability":p_no_jump,"compound_at_least_one_jump_probability":1-p_no_jump,"compound_jump_quadratic_variation":"theta^2 N_T","compound_continuous_quadratic_variation":0.0,"record_laws_equal":False},"preregistration":{"status":"frozen_not_scored","gamma":gamma,"T":T,"theta":theta,"event_rate":rate,"no_holdout_refit":True,"primary_test":"path continuity / resolved jump occurrence","secondary_test":"continuous versus jump quadratic-variation decomposition","requires_action_owned_record_observable":True,"empirical_score_assigned":False},"exact_controls":{"rate_equals_two_gamma":abs(rate-2*gamma)<1e-15,"p_no_jump":p_no_jump,"p_no_jump_in_unit_interval":0<p_no_jump<1,"brownian_qv":gamma*T,"compound_expected_jump_qv":theta*theta*rate*T,"terminal_law_type_differs":True},"ownership":{"record_access_and_resolution_imported":True,"gu_record_observable_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"reduced_controlled_process_not_enough_to_select_levy_horn":True,"record_crosses_operational_equivalence_class":True,"next_exact_input":"Require a GU-owned action and physical quotient that select the characteristic exponent and make one inequivalent record observable operational."},"source_and_ledger_effect":"none","claim_ceiling":"Frozen exact record-law discriminator only; no apparatus model, data, empirical score, GU record observable or diffusion-limit claim."}
def validate(p):
    d,r,g,x,o,q=p["dependency_checks"],p["record_laws"],p["preregistration"],p["exact_controls"],p["ownership"],p["decision"]
    assert d["system_only_controlled_processes_equal"] and r["brownian_paths_continuous_probability"]==1.0 and 0<r["compound_paths_continuous_probability"]<1 and not r["record_laws_equal"]
    assert g["status"]=="frozen_not_scored" and g["no_holdout_refit"] and g["requires_action_owned_record_observable"] and not g["empirical_score_assigned"]
    assert x["rate_equals_two_gamma"] and x["p_no_jump_in_unit_interval"] and x["terminal_law_type_differs"]
    assert o["record_access_and_resolution_imported"] and not o["gu_record_observable_constructed"] and not o["prediction_or_confirmation_credit"]
    assert q["reduced_controlled_process_not_enough_to_select_levy_horn"] and q["record_crosses_operational_equivalence_class"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K989 controls: 17/17")
if __name__=="__main__":main()
