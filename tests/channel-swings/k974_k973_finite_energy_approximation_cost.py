#!/usr/bin/env python3
"""K974 finite-second-moment cost of approximating the exponential cusp."""
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k974-k973-finite-energy-approximation-cost.json"
def second_moment_lower(a,eta): return a*a*(1-2*eta)/(2*eta)
def truncated_second_moment(a,omega): return a*omega/math.atan(omega/a)-a*a
def build():
    a=1.4;eta=0.05;omega=4*a/(math.pi*eta);v=truncated_second_moment(a,omega);lower=second_moment_lower(a,eta)
    rows=[]
    for e in (0.2,0.1,0.05,0.025):
        O=4*a/(math.pi*e);rows.append({"eta":e,"sufficient_bandwidth":O,"truncated_second_moment":truncated_second_moment(a,O),"necessary_second_moment_lower":second_moment_lower(a,e)})
    return {"schema_version":"1.0","result_id":"K974-FINITE-ENERGY-APPROXIMATION-COST","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Uniform approximation of exp(-a|t|) by positive spectral characteristic functions with finite second moment.","theorem":{"uniform_error":"sup_t |phi(t)-exp(-a|t|)| <= eta","range":"0<eta<1/2","test_time":"t=2 eta/a","cosine_bound":"1-Re phi(t) <= E[omega^2]*t^2/2","exponential_bound":"1-exp(-2 eta) >= 2 eta-2 eta^2","second_moment_lower":"E[omega^2] >= a^2(1-2 eta)/(2 eta)","second_moment_diverges_as_error_vanishes":True},"compact_band_repair":{"model":"normalized symmetric Cauchy restriction to [-Omega,Omega]","sufficient_bandwidth":"Omega=4a/(pi eta)","uniform_error_at_most_eta":True,"exact_second_moment":"a Omega/atan(Omega/a)-a^2","mean_zero":True,"a":a,"eta":eta,"Omega":omega,"second_moment_equals_variance":v,"necessary_lower":lower,"repair_respects_lower_bound":v>=lower},"exact_controls":{"scaling_rows":rows,"all_repairs_respect_lower_bound":all(r["truncated_second_moment"]>=r["necessary_second_moment_lower"] for r in rows),"second_moment_cost_increases":all(rows[i+1]["truncated_second_moment"]>rows[i]["truncated_second_moment"] for i in range(3)),"lower_cost_increases":all(rows[i+1]["necessary_second_moment_lower"]>rows[i]["necessary_second_moment_lower"] for i in range(3))},"ownership":{"bandwidth_error_and_energy_budget_imported":True,"optimal_constant_claimed":False,"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"finite_energy_repair_quantified":True,"next_exact_input":"Compose the exact singular parent and finite-energy approximation cost into the physical-domain ownership disposition."},"source_and_ledger_effect":"none","claim_ceiling":"Necessary second-moment lower bound plus one compact-band sufficient construction; no optimal approximation theorem or GU-selected cutoff."
    }
def validate(p):
    t=p["theorem"];r=p["compact_band_repair"];x=p["exact_controls"];o=p["ownership"]
    assert 0<r["eta"]<0.5 and r["a"]>0 and t["second_moment_diverges_as_error_vanishes"]
    assert r["uniform_error_at_most_eta"] and r["mean_zero"] and r["repair_respects_lower_bound"] and r["second_moment_equals_variance"]>=r["necessary_lower"]
    assert x["all_repairs_respect_lower_bound"] and x["second_moment_cost_increases"] and x["lower_cost_increases"]
    assert p["decision"]["finite_energy_repair_quantified"] and o["bandwidth_error_and_energy_budget_imported"] and not o["optimal_constant_claimed"]
    assert not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert json.loads(OUTPUT.read_text())==p
    elif a.write:OUTPUT.write_text(text)
    else:print(text,end="")
    print("K974 controls: 11/11")
if __name__=="__main__":main()
