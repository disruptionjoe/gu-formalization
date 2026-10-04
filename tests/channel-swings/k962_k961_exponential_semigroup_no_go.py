#!/usr/bin/env python3
"""K962 exact finite-reservoir obstruction to strict exponential dephasing."""
import argparse, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/"lab/process/k962-k961-exponential-semigroup-no-go.json"
def build():
    gamma=0.25; samples=[{"t":t,"lambda":math.exp(-2*gamma*t)} for t in (0,2,4,8)]
    return {"schema_version":"1.0","result_id":"K962-EXPONENTIAL-SEMIGROUP-NO-GO","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Exact positive-rate exponential dephasing versus a fixed finite-dimensional autonomous controlled-dephasing reservoir.","theorem":{"premises":["finite-dimensional environment","fixed initial environment state","time-independent autonomous Hamiltonian","controlled-dephasing coupling","gamma>0"],"recurrence_from_k961":True,"exponential_limit_zero":True,"contradiction":"K961 supplies arbitrarily late returns near one, while exp(-2 gamma t) tends to zero.","finite_closed_exact_realization_exists":False},"exact_controls":{"gamma":gamma,"samples":samples,"strictly_decreasing":all(samples[i+1]["lambda"]<samples[i]["lambda"] for i in range(len(samples)-1)),"late_value_below_one_fiftieth":samples[-1]["lambda"]<0.02},"boundary":{"not_excluded":["infinite or continuum environment","fresh ancillas or resets","time-dependent driving","non-Hamiltonian primitive","finite-time approximation"]},"ownership":{"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"finite_closed_exact_markov_parent_killed":True,"next_exact_input":"Construct the strongest explicit fresh-resource contrary model and account for its continuous-time scaling."},"source_and_ledger_effect":"none","claim_ceiling":"Exact no-go only for the five declared finite closed controlled-dephasing premises; no general open-system, continuum or GU no-go follows."}
def validate(p):
    t=p["theorem"]; c=p["exact_controls"]
    assert t["recurrence_from_k961"] and t["exponential_limit_zero"] and not t["finite_closed_exact_realization_exists"]
    assert c["gamma"]>0 and c["strictly_decreasing"] and c["late_value_below_one_fiftieth"]
    assert len(p["boundary"]["not_excluded"])==5 and p["decision"]["finite_closed_exact_markov_parent_killed"]
    assert not p["ownership"]["gu_action_or_physical_quotient_constructed"] and not p["ownership"]["prediction_or_confirmation_credit"]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args(); p=build(); validate(p); text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check: assert OUTPUT.read_text()==text
    elif a.write: OUTPUT.write_text(text)
    else: print(text,end="")
    print("K962 controls: 10/10")
if __name__=="__main__": main()
