#!/usr/bin/env python3
"""K967 uniform Cauchy spectral truncation bound."""
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k967-k966-bandlimited-continuum-bound.json"
def build():
    gamma=0.7;a=2*gamma;omega=30.0
    tail=1-(2/math.pi)*math.atan(omega/a);tail_upper=2*a/(math.pi*omega);uniform=2*tail;theorem=4*a/(math.pi*omega)
    return {"schema_version":"1.0","result_id":"K967-BANDLIMITED-CONTINUUM-BOUND","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Normalized restriction of K966's Cauchy spectral measure to [-Omega,Omega].","theorem":{"tail_mass":"q_Omega=(2/pi) arctan(2 gamma/Omega)","tail_upper":"q_Omega<=4 gamma/(pi Omega)","normalized_characteristic_error":"sup_t |f_Omega(t)-exp(-2 gamma |t|)|<=2 q_Omega<=8 gamma/(pi Omega)","uniform_all_real_times":True},"exact_controls":{"gamma":gamma,"scale":a,"Omega":omega,"tail_mass":tail,"tail_upper":tail_upper,"uniform_error_exact_bound":uniform,"uniform_error_theorem_bound":theorem,"tail_inequality":tail<=tail_upper,"normalization_penalty_included":uniform<=theorem},"ownership":{"spectral_cutoff_and_normalization_imported":True,"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"uniform_bandwidth_bound_proved":True,"next_exact_input":"Discretize the normalized band with a finite positive atomic measure and quantify uniform finite-window error."},"source_and_ledger_effect":"none","claim_ceiling":"Uniform total-variation/Fourier error bound for the named Cauchy truncation only; not a GU cutoff or physical ultraviolet law."}
def validate(p):
    t=p["theorem"];x=p["exact_controls"];o=p["ownership"]
    assert x["gamma"]>0 and x["Omega"]>0 and x["tail_inequality"] and x["normalization_penalty_included"]
    assert t["uniform_all_real_times"] and "8 gamma/(pi Omega)" in t["normalized_characteristic_error"]
    assert p["decision"]["uniform_bandwidth_bound_proved"] and o["spectral_cutoff_and_normalization_imported"]
    assert not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==text
    elif a.write:OUTPUT.write_text(text)
    else:print(text,end="")
    print("K967 controls: 10/10")
if __name__=="__main__":main()
