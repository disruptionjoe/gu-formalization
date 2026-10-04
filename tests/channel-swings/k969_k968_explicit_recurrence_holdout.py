#!/usr/bin/env python3
"""K969 exact recurrence witness for K968's equally spaced finite spectrum."""
import argparse,cmath,json,math
from pathlib import Path
import k968_k967_finite_window_atomic_approximation as k968
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k969-k968-explicit-recurrence-holdout.json"
def build():
    gamma,T,epsilon,Omega,N=k968.parameters();aa=k968.atoms(gamma,Omega,N);tau=2*math.pi*N/Omega
    value=sum(w*cmath.exp(1j*om*tau) for om,w in aa);target=math.exp(-2*gamma*tau);gap=abs(value-target)
    return {"schema_version":"1.0","result_id":"K969-EXPLICIT-RECURRENCE-HOLDOUT","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Exact common-period recurrence of K968's equally spaced midpoint spectrum.","theorem":{"frequency_spacing":2*Omega/N,"recurrence_time":"tau_rec=2 pi N/Omega","all_phases_one":True,"atomic_coherence_at_recurrence":"1","continuum_coherence_at_recurrence":"exp(-2 gamma tau_rec)","not_a_minimal_recurrence_claim":True},"exact_controls":{"gamma":gamma,"T":T,"epsilon":epsilon,"Omega":Omega,"atom_count":N,"tau_rec":tau,"recurrence_after_calibration":tau>T,"atomic_real":value.real,"atomic_imag":value.imag,"atomic_return_error":abs(value-1),"continuum_target":target,"late_gap":gap,"late_gap_above_0_999":gap>0.999},"holdout":{"calibration_window":"[0,T]","score_window":"a predeclared neighborhood of tau_rec","status":"reserved_not_scored"},"ownership":{"finite_grid_and_holdout_location_imported":True,"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"bounded_fit_cannot_decide_parent":True,"next_exact_input":"Compose continuum exactness, finite-window mimicry and late recurrence into the unscored owner/discriminator disposition."},"source_and_ledger_effect":"none","claim_ceiling":"Exact recurrence witness for the named grid construction only; no universal lower bound on recurrence time and no empirical or GU prediction."}
def validate(p):
    t=p["theorem"];x=p["exact_controls"];h=p["holdout"];o=p["ownership"]
    assert t["all_phases_one"] and t["not_a_minimal_recurrence_claim"] and x["recurrence_after_calibration"]
    assert x["atomic_return_error"]<1e-8 and abs(x["atomic_imag"])<1e-8 and x["late_gap_above_0_999"]
    assert h["status"]=="reserved_not_scored" and p["decision"]["bounded_fit_cannot_decide_parent"]
    assert o["finite_grid_and_holdout_location_imported"] and not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==text
    elif a.write:OUTPUT.write_text(text)
    else:print(text,end="")
    print("K969 controls: 11/11")
if __name__=="__main__":main()
