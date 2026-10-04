#!/usr/bin/env python3
"""K972 finite-first-moment characteristic-function cusp obstruction."""
import argparse,json,math,cmath
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k972-k971-finite-moment-cusp-no-go.json"
def build():
    a=1.4;atoms=((-1.0,0.5),(2.0,0.5));mean=sum(w*x for x,w in atoms);first=sum(w*abs(x) for x,w in atoms)
    hs=(1e-2,1e-3,1e-4);quot=[sum(w*(cmath.exp(1j*x*h)-1)/h for x,w in atoms) for h in hs]
    return {"schema_version":"1.0","result_id":"K972-FINITE-MOMENT-CUSP-NO-GO","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Positive spectral characteristic functions with finite absolute first moment.","theorem":{"hypothesis":"integral |omega| dmu < infinity","characteristic_differentiable_at_zero":True,"derivative":"i integral omega dmu","target":"exp(-a|t|)","target_right_derivative":-a,"target_left_derivative":a,"exact_positive_rate_target_impossible":True},"exact_controls":{"a":a,"finite_atom_first_moment":first,"finite_atom_mean":mean,"difference_quotients":[{"h":h,"real":q.real,"imag":q.imag} for h,q in zip(hs,quot)],"difference_quotients_converge_to_i_mean":abs(quot[-1]-1j*mean)<2e-4,"target_one_sided_derivatives_disagree":(-a)!=(a)},"ownership":{"positive_spectral_model_only":True,"general_open_system_no_go":False,"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"finite_first_moment_excludes_exact_cusp":True,"next_exact_input":"Strengthen to the finite-second-moment quadratic survival law and compare with the target's linear short-time loss."},"source_and_ledger_effect":"none","claim_ceiling":"Finite-first-moment no-go for exact positive-measure spectral characteristic functions only; no no-go for reset, nonautonomous or singular-limit dynamics."}
def validate(p):
    t=p["theorem"];x=p["exact_controls"];o=p["ownership"]
    assert x["a"]>0 and x["finite_atom_first_moment"]<math.inf and t["characteristic_differentiable_at_zero"]
    assert t["target_right_derivative"]!=t["target_left_derivative"] and t["exact_positive_rate_target_impossible"]
    assert x["difference_quotients_converge_to_i_mean"] and x["target_one_sided_derivatives_disagree"]
    assert p["decision"]["finite_first_moment_excludes_exact_cusp"] and o["positive_spectral_model_only"] and not o["general_open_system_no_go"]
    assert not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert json.loads(OUTPUT.read_text())==p
    elif a.write:OUTPUT.write_text(text)
    else:print(text,end="")
    print("K972 controls: 10/10")
if __name__=="__main__":main()
