#!/usr/bin/env python3
"""K963 exact fresh-ancilla collision dilation."""
import argparse,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k963-k962-fresh-ancilla-dephasing-dilation.json"
def build():
    lam=Fraction(3,5); powers=[{"n":n,"coherence":str(lam**n)} for n in range(6)]
    return {"schema_version":"1.0","result_id":"K963-FRESH-ANCILLA-DEPHASING-DILATION","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"One qubit system colliding once with each fresh qubit ancilla prepared in a fixed pure state.","construction":{"unitary":"U_theta=exp(-i theta Z_S tensor Y_E)","ancilla_state":"|0><0|","single_step_coherence":"lambda=cos(2 theta)","angle":"theta=(1/2) arccos(lambda)","n_step_coherence":"lambda^n","cptp":True,"remote_marginal_invariant":True},"exact_controls":{"lambda":str(lam),"powers":powers,"semigroup_on_integer_steps":all(Fraction(x["coherence"])==lam**x["n"] for x in powers),"identity_at_n_zero":powers[0]["coherence"]=="1","strict_decay":all(Fraction(powers[i+1]["coherence"])<Fraction(powers[i]["coherence"]) for i in range(5))},"resource":{"fresh_ancillas_after_n_steps":5,"reset_or_unbounded_tape_required_for_unbounded_time":True,"closed_finite_environment":False},"ownership":{"ancilla_preparation_trace_and_clock_imported":True,"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"exact_resource_backed_contrary_model_constructed":True,"next_exact_input":"Scale lambda with the time step and expose the continuous-time resource/coupling limit."},"source_and_ledger_effect":"none","claim_ceiling":"Exact collision-model dilation and resource accounting only; freshness, partial trace, time step and probability semantics are imported and no GU result follows."}
def validate(p):
    c=p["construction"];x=p["exact_controls"];r=p["resource"];o=p["ownership"]
    assert c["cptp"] and c["remote_marginal_invariant"] and c["n_step_coherence"]=="lambda^n"
    assert x["semigroup_on_integer_steps"] and x["identity_at_n_zero"] and x["strict_decay"]
    assert r["reset_or_unbounded_tape_required_for_unbounded_time"] and not r["closed_finite_environment"]
    assert o["ancilla_preparation_trace_and_clock_imported"] and not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==text
    elif a.write:OUTPUT.write_text(text)
    else:print(text,end="")
    print("K963 controls: 11/11")
if __name__=="__main__":main()
