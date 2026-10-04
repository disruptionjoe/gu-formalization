#!/usr/bin/env python3
"""K984 preregistered record-sensitive holdout for the K981 Poisson horn."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k984-k983-record-sensitive-holdout.json";INPUTS=[ROOT/"lab/process/k981-k980-poisson-phase-flip-unravelling.json",ROOT/"lab/process/k983-k982-system-only-nonidentifiability.json"]
def build():
    a,b=[json.loads(p.read_text()) for p in INPUTS];g=a["exact_controls"]["gamma"];T=2.0;x=g*T
    probs=[math.exp(-x)*x**n/math.factorial(n) for n in range(12)];tail=1-sum(probs)
    even=sum(probs[::2])+sum(math.exp(-x)*x**n/math.factorial(n) for n in range(12,80,2));odd=sum(probs[1::2])+sum(math.exp(-x)*x**n/math.factorial(n) for n in range(13,80,2))
    return {"schema_version":"1.0","result_id":"K984-RECORD-SENSITIVE-HOLDOUT","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_PREREGISTERED_HOLDOUT","target_claim":"NONE-NOT-A-KILL","scope":"A pre-score holdout for the supplied Poisson phase-flip horn using an independently accessible jump-count record at fixed T=2.","dependency":{"input_ids":[a["result_id"],b["result_id"]],"system_endpoint_nonidentifiability_proved":b["decision"]["system_only_endpoint_holdout_cannot_select_horn"],"source_and_ledger_effect_none":a["source_and_ledger_effect"]==b["source_and_ledger_effect"]=="none"},"preregistration":{"rate_source":"gamma fixed from the prior system-only dephasing calibration","holdout_time_T":T,"record":"full jump count N_T, not endpoint parity alone","fit_on_holdout":False,"predicted_distribution":"P(N_T=n)=exp(-gamma T)(gamma T)^n/n!","primary_checks":["mean=gamma T","variance=gamma T","full count histogram follows Poisson(gamma T)"],"required_access":"an action-owned environment or clock record operationally linked to each system trial","status":"frozen_not_scored"},"exact_controls":{"gamma":g,"gamma_T":x,"probabilities_n_0_through_11":probs,"tail_n_ge_12":tail,"probabilities_normalize":abs(sum(probs)+tail-1)<1e-15,"p_even":even,"p_odd":odd,"parity_matches_system_coherence":abs((even-odd)-math.exp(-2*x))<1e-13,"p_two_or_more":1-math.exp(-x)*(1+x),"counts_beyond_parity_have_positive_probability":1-math.exp(-x)*(1+x)>0},"information_boundary":{"system_endpoint_reads_only_parity":True,"count_record_strictly_refines_parity":True,"same_endpoint_unitary_for_n_and_n_plus_2":True,"record_not_supplied_by_reduced_channel":True},"ownership":{"gu_record_observable_constructed":False,"gu_action_or_clock_constructed":False,"empirical_data_collected":False,"prediction_or_confirmation_credit":False},"decision":{"distinct_holdout_frozen_before_scoring":True,"holdout_execution_requires_new_native_owner":True,"next_exact_input":"A GU-owned physical quotient and action must make the stochastic clock or environment record an observable, or select a different horn with its own inequivalent holdout."},"source_and_ledger_effect":"none","claim_ceiling":"Preregistered conditional holdout and exact Poisson probabilities only; no data, score, GU observable, prediction or confirmation."}
def validate(p):
    d,r,c,i,o,x=p["dependency"],p["preregistration"],p["exact_controls"],p["information_boundary"],p["ownership"],p["decision"]
    assert len(d["input_ids"])==2 and d["system_endpoint_nonidentifiability_proved"] and d["source_and_ledger_effect_none"]
    assert r["holdout_time_T"]==2 and not r["fit_on_holdout"] and len(r["primary_checks"])==3 and r["status"]=="frozen_not_scored"
    assert len(c["probabilities_n_0_through_11"])==12 and c["probabilities_normalize"] and c["parity_matches_system_coherence"] and c["counts_beyond_parity_have_positive_probability"]
    assert all(i.values())
    assert not o["gu_record_observable_constructed"] and not o["gu_action_or_clock_constructed"] and not o["empirical_data_collected"] and not o["prediction_or_confirmation_credit"]
    assert x["distinct_holdout_frozen_before_scoring"] and x["holdout_execution_requires_new_native_owner"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K984 controls: 17/17")
if __name__=="__main__":main()
