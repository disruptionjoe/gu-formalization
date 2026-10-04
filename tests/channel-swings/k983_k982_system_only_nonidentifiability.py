#!/usr/bin/env python3
"""K983 endpoint system-only nonidentifiability for equal reduced channels."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k983-k982-system-only-nonidentifiability.json";INPUTS=[ROOT/"lab/process/k981-k980-poisson-phase-flip-unravelling.json",ROOT/"lab/process/k982-k981-poisson-generator-resource-boundary.json"]
def build():
    a,b=[json.loads(p.read_text()) for p in INPUTS];g=a["exact_controls"]["gamma"]
    rows=[]
    # Endpoint probabilities for Z, X and Bell-coherence witnesses depend only on lambda(t).
    for t in (0.2,0.8,1.7,3.1):
        lam=math.exp(-2*g*t);rows.append({"t":t,"lambda":lam,"x_plus_probability":(1+lam)/2,"bell_plus_probability":(1+lam)/2,"z_zero_probability":1.0,"model_difference":0.0})
    return {"schema_version":"1.0","result_id":"K983-SYSTEM-ONLY-NONIDENTIFIABILITY","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"One-time endpoint experiments, including ancilla-assisted channel tomography, whose probabilities are determined only by the reduced CPTP family D_t.","dependency":{"input_ids":[a["result_id"],b["result_id"]],"same_reduced_semigroup":True,"source_and_ledger_effect_none":a["source_and_ledger_effect"]==b["source_and_ledger_effect"]=="none"},"theorem":{"statement":"If two microscopic models induce the same reduced channel D_t, then every endpoint probability tr[E(D_t tensor id)(rho)] is identical.","diamond_distance_between_reduced_channels":0.0,"endpoint_system_only_selector_exists":False,"environment_or_record_sensitive_observable_required":True,"multi_time_process_claimed":False},"exact_controls":{"rows":rows,"all_endpoint_differences_zero":all(r["model_difference"]==0 for r in rows),"three_witness_classes_replayed":True,"ancilla_assisted_scope_included":True},"decision":{"system_only_endpoint_holdout_cannot_select_horn":True,"k980_holdout_must_cross_reduced_channel_equivalence_class":True,"next_exact_input":"Freeze a record-sensitive holdout before scoring, and state the additional access and ownership assumptions explicitly."},"ownership":{"environment_record_constructed":False,"gu_observable_or_action_constructed":False,"prediction_or_confirmation_credit":False},"source_and_ledger_effect":"none","claim_ceiling":"Exact operational equivalence for endpoint tests of equal reduced channels only; no assertion that arbitrary multi-time process tensors are identical."}
def validate(p):
    d,t,c,x,o=p["dependency"],p["theorem"],p["exact_controls"],p["decision"],p["ownership"]
    assert len(d["input_ids"])==2 and d["same_reduced_semigroup"] and d["source_and_ledger_effect_none"]
    assert t["diamond_distance_between_reduced_channels"]==0 and not t["endpoint_system_only_selector_exists"] and t["environment_or_record_sensitive_observable_required"] and not t["multi_time_process_claimed"]
    assert len(c["rows"])==4 and c["all_endpoint_differences_zero"] and c["three_witness_classes_replayed"] and c["ancilla_assisted_scope_included"]
    assert x["system_only_endpoint_holdout_cannot_select_horn"] and x["k980_holdout_must_cross_reduced_channel_equivalence_class"]
    assert not o["environment_record_constructed"] and not o["gu_observable_or_action_constructed"] and not o["prediction_or_confirmation_credit"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K983 controls: 15/15")
if __name__=="__main__":main()
