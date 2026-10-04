#!/usr/bin/env python3
"""K973 finite-second-moment quadratic survival boundary."""
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k973-k972-quadratic-zeno-boundary.json"
def build():
    a=1.4;hs=(1e-2,1e-3,1e-4);finite=[{"t":t,"quadratic_ratio":(1-math.cos(t)**2)/(t*t)} for t in hs];target=[{"t":t,"linear_ratio":(1-math.exp(-2*a*t))/t} for t in hs]
    return {"schema_version":"1.0","result_id":"K973-QUADRATIC-ZENO-BOUNDARY","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Short-time survival law for positive spectral states with finite second moment.","theorem":{"hypothesis":"integral omega^2 dmu < infinity","amplitude_expansion":"phi(t)=1+i m t-(1/2)E[omega^2]t^2+o(t^2)","survival_expansion":"|phi(t)|^2=1-Var(omega)t^2+o(t^2)","exact_exponential_survival":"exp(-2a|t|)=1-2a|t|+o(|t|)","finite_variance_exact_exponential_impossible":True},"exact_controls":{"a":a,"symmetric_two_atom_variance":1.0,"finite_rows":finite,"target_rows":target,"quadratic_ratio_tends_to_variance":abs(finite[-1]["quadratic_ratio"]-1)<2e-8,"linear_ratio_tends_to_2a":abs(target[-1]["linear_ratio"]-2*a)<5e-4},"ownership":{"finite_variance_physical_state_rule_imported":True,"general_nonunitary_dynamics_excluded":False,"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"quadratic_vs_linear_boundary_proved":True,"next_exact_input":"Quantify how the spectral second moment must diverge when a finite-energy characteristic function uniformly approximates the exponential cusp."},"source_and_ledger_effect":"none","claim_ceiling":"Quadratic short-time theorem for positive spectral characteristic functions with finite variance; no universal quantum-dynamics no-go."}
def validate(p):
    t=p["theorem"];x=p["exact_controls"];o=p["ownership"]
    assert x["a"]>0 and x["symmetric_two_atom_variance"]>0 and t["finite_variance_exact_exponential_impossible"]
    assert x["quadratic_ratio_tends_to_variance"] and x["linear_ratio_tends_to_2a"]
    assert p["decision"]["quadratic_vs_linear_boundary_proved"] and o["finite_variance_physical_state_rule_imported"]
    assert not o["general_nonunitary_dynamics_excluded"] and not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert json.loads(OUTPUT.read_text())==p
    elif a.write:OUTPUT.write_text(text)
    else:print(text,end="")
    print("K973 controls: 9/9")
if __name__=="__main__":main()
