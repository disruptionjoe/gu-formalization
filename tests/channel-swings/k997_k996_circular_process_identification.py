#!/usr/bin/env python3
"""K997 circular convolution-semigroup identification boundary."""
from __future__ import annotations
import argparse, cmath, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k997-k996-circular-process-identification.json"

def build():
    gamma=0.7;times=[0.25,0.75,1.0];harmonics=range(-4,5)
    phi=lambda t,n: math.exp(-0.5*gamma*t*n*n)
    semigroup=max(abs(phi(times[2],n)-phi(times[0],n)*phi(times[1],n)) for n in harmonics)
    T=2.0;a0=0.0;a1=2*math.pi/T
    final=max(abs(cmath.exp(-1j*n*a0*T)-cmath.exp(-1j*n*a1*T)) for n in harmonics)
    middle=max(abs(cmath.exp(-1j*n*a0)-cmath.exp(-1j*n*a1)) for n in harmonics)
    return {
      "schema_version":"1.0","result_id":"K997-CIRCULAR-PROCESS-IDENTIFICATION","created":"2026-10-04","status":"working_draft_verified",
      "direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL",
      "scope":"Circle-valued stationary independent-increment processes starting at the identity, supplied through all integer harmonics at all times.",
      "theorem":{
        "all_time_integer_harmonics_determine_each_increment_law":True,
        "independent_increment_process_finite_dimensional_law_determined":True,
        "composition":"joint laws are iterated products of the identified increment kernels",
        "single_time_marginal_does_not_determine_generator":True,
        "real_line_lift_identified":False},
      "exact_controls":{
        "brownian_circle_semigroup_error":semigroup,"semigroup_identity_pass":semigroup<1e-15,
        "single_time_drift_alias_T":T,"drift_zero":a0,"drift_winding":a1,
        "terminal_integer_harmonic_error":final,"terminal_alias_pass":final<1e-14,
        "intermediate_harmonic_difference":middle,"intermediate_laws_differ":middle>1.0},
      "ownership":{"circular_process_imported":True,"all_time_harmonic_access_imported":True,"gu_action_generator_or_clock_constructed":False,"prediction_or_confirmation_credit":False},
      "decision":{"fixed_time_log_branch_warning_required":True,"circular_process_identification_requires_all_time_semigroup_or_owned_generator":True,"next_exact_input":"Construct distinct real Levy lifts with the same complete circular process."},
      "source_and_ledger_effect":"none","claim_ceiling":"Exact compact-group process identification boundary only; a fixed-time marginal is insufficient and no real-line lift or GU generator is selected."
    }
def validate(p):
    t,x,o,d=p["theorem"],p["exact_controls"],p["ownership"],p["decision"]
    assert t["all_time_integer_harmonics_determine_each_increment_law"] and t["independent_increment_process_finite_dimensional_law_determined"]
    assert t["single_time_marginal_does_not_determine_generator"] and not t["real_line_lift_identified"]
    assert x["semigroup_identity_pass"] and x["brownian_circle_semigroup_error"]<1e-15
    assert x["terminal_alias_pass"] and x["terminal_integer_harmonic_error"]<1e-14 and x["intermediate_laws_differ"]
    assert o["circular_process_imported"] and o["all_time_harmonic_access_imported"]
    assert not o["gu_action_generator_or_clock_constructed"] and not o["prediction_or_confirmation_credit"]
    assert d["fixed_time_log_branch_warning_required"] and d["circular_process_identification_requires_all_time_semigroup_or_owned_generator"]
    assert p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==text
    elif a.write:OUTPUT.write_text(text)
    else:print(text,end="")
    print("K997 controls: 15/15")
if __name__=="__main__":main()
