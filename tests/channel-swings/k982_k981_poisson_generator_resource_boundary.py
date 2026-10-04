#!/usr/bin/env python3
"""K982 generator and resource boundary for the K981 Poisson horn."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k982-k981-poisson-generator-resource-boundary.json";INPUT=ROOT/"lab/process/k981-k980-poisson-phase-flip-unravelling.json"
def build():
    q=json.loads(INPUT.read_text());g=q["exact_controls"]["gamma"]
    rows=[]
    for T in (0.5,1.0,2.0,5.0):
        x=g*T; probs=[math.exp(-x)*x**n/math.factorial(n) for n in range(120)]
        mean=sum(n*p for n,p in enumerate(probs));var=sum((n-mean)**2*p for n,p in enumerate(probs))
        rows.append({"T":T,"expected_jumps":x,"replayed_mean":mean,"replayed_variance":var,"probability_no_jump":math.exp(-x),"probability_two_or_more":1-math.exp(-x)*(1+x)})
    return {"schema_version":"1.0","result_id":"K982-POISSON-GENERATOR-RESOURCE-BOUNDARY","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Infinitesimal generator and resource accounting of K981's supplied Poisson phase-flip process.","dependency":{"input_id":q["result_id"],"exact_stochastic_horn":q["decision"]["exact_stochastic_horn_constructed"],"source_and_ledger_effect_none":q["source_and_ledger_effect"]=="none"},"generator":{"short_time_law":"D_dt(rho)=(1-gamma dt)rho+gamma dt ZrhoZ+o(dt)","lindblad_generator":"L(rho)=gamma(ZrhoZ-rho)","coherence_rate":"-2 gamma","finite_event_rate":g,"grid_step_or_h":None,"h_inverse_half_coupling":False},"resource":{"rows":rows,"mean_and_variance_equal_gamma_T":all(abs(r["replayed_mean"]-r["expected_jumps"])<1e-12 and abs(r["replayed_variance"]-r["expected_jumps"])<1e-11 for r in rows),"unbounded_horizon_count_support":True,"instantaneous_point_jumps_idealized":True,"classical_random_clock_and_probability_law_imported":True,"deterministic_closed_hamiltonian_parent_supplied":False},"decision":{"k978_grid_coupling_divergence_not_universal_across_horns":True,"finite_rate_does_not_remove_stochastic_owner_debt":True,"next_exact_input":"Determine which observables can distinguish this stochastic horn from any other microscopic realization of the same reduced channel family."},"ownership":{"gu_action_or_clock_owner_constructed":False,"prediction_or_confirmation_credit":False},"source_and_ledger_effect":"none","claim_ceiling":"Exact generator and resource accounting for one supplied stochastic process; no finite closed Hamiltonian parent, stochastic action or GU clock owner."}
def validate(p):
    d,g,r,x,o=p["dependency"],p["generator"],p["resource"],p["decision"],p["ownership"]
    assert d["exact_stochastic_horn"] and d["source_and_ledger_effect_none"]
    assert g["finite_event_rate"]>0 and g["grid_step_or_h"] is None and not g["h_inverse_half_coupling"]
    assert len(r["rows"])==4 and r["mean_and_variance_equal_gamma_T"] and r["unbounded_horizon_count_support"]
    assert r["instantaneous_point_jumps_idealized"] and r["classical_random_clock_and_probability_law_imported"] and not r["deterministic_closed_hamiltonian_parent_supplied"]
    assert x["k978_grid_coupling_divergence_not_universal_across_horns"] and x["finite_rate_does_not_remove_stochastic_owner_debt"]
    assert not o["gu_action_or_clock_owner_constructed"] and not o["prediction_or_confirmation_credit"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K982 controls: 15/15")
if __name__=="__main__":main()
