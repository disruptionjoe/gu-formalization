#!/usr/bin/env python3
"""K968 finite positive atomic approximation on a declared time window."""
import argparse,cmath,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k968-k967-finite-window-atomic-approximation.json"
def parameters():
    gamma=0.7;T=3.0;epsilon=0.05;Omega=16*gamma/(math.pi*epsilon);N=math.ceil(2*T*Omega/epsilon)
    return gamma,T,epsilon,Omega,N
def atoms(gamma,Omega,N):
    a=2*gamma;delta=2*Omega/N;z=(2/math.pi)*math.atan(Omega/a);out=[]
    cdf=lambda w: math.atan(w/a)/math.pi+0.5
    for j in range(N):
        lo=-Omega+j*delta;hi=lo+delta;mid=(lo+hi)/2;out.append((mid,(cdf(hi)-cdf(lo))/z))
    return out
def build():
    gamma,T,epsilon,Omega,N=parameters();aa=atoms(gamma,Omega,N);trunc=8*gamma/(math.pi*Omega);disc=T*Omega/N;bound=trunc+disc
    samples=[]
    for t in (0.0,0.5,1.5,3.0):
        value=sum(w*cmath.exp(1j*om*t) for om,w in aa);target=math.exp(-2*gamma*t);samples.append({"t":t,"atomic_real":value.real,"atomic_imag":value.imag,"target":target,"absolute_error":abs(value-target)})
    return {"schema_version":"1.0","result_id":"K968-FINITE-WINDOW-ATOMIC-APPROXIMATION","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Positive midpoint discretization of K967 on one declared finite observation window.","construction":{"gamma":gamma,"T":T,"epsilon":epsilon,"Omega":Omega,"atom_count":N,"cell_width":2*Omega/N,"weights_positive":all(w>0 for _,w in aa),"weights_sum":sum(w for _,w in aa),"finite_autonomous_reservoir":True},"theorem":{"truncation_bound":trunc,"discretization_bound":disc,"combined_uniform_bound":bound,"bound_below_epsilon":bound<=epsilon,"dimension_sufficient":"N>=32 gamma T/(pi epsilon^2)","uniform_window":"0<=t<=T"},"exact_controls":{"samples":samples,"sample_errors_below_bound":all(x["absolute_error"]<=bound+1e-12 for x in samples),"imaginary_parts_cancel":all(abs(x["atomic_imag"])<1e-12 for x in samples)},"ownership":{"cutoff_partition_and_error_budget_imported":True,"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"finite_window_indistinguishability_constructed":True,"next_exact_input":"Expose the finite grid's exact recurrence time and freeze it as a held-out discriminator rather than treating finite-window fit as a derivation."},"source_and_ledger_effect":"none","claim_ceiling":"Constructive sufficient finite-window approximation bound only; no optimal dimension lower bound and no GU dynamics or empirical fit."}
def validate(p):
    c=p["construction"];t=p["theorem"];x=p["exact_controls"];o=p["ownership"]
    assert c["gamma"]>0 and c["T"]>0 and 0<c["epsilon"]<1 and c["atom_count"]>0
    assert c["weights_positive"] and abs(c["weights_sum"]-1)<1e-12 and c["finite_autonomous_reservoir"]
    assert t["bound_below_epsilon"] and t["combined_uniform_bound"]<=c["epsilon"]
    assert x["sample_errors_below_bound"] and x["imaginary_parts_cancel"] and p["decision"]["finite_window_indistinguishability_constructed"]
    assert o["cutoff_partition_and_error_budget_imported"] and not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==text
    elif a.write:OUTPUT.write_text(text)
    else:print(text,end="")
    print("K968 controls: 12/12")
if __name__=="__main__":main()
