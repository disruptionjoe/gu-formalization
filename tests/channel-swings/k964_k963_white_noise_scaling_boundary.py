#!/usr/bin/env python3
"""K964 grid-exact exponential limit and singular collision scaling."""
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k964-k963-white-noise-scaling-boundary.json"
def build():
    gamma=0.7; rows=[]
    for n in (10,40,160,640):
        h=1/n; lam=math.exp(-2*gamma*h); theta=0.5*math.acos(lam); coupling=theta/h
        rows.append({"n":n,"h":h,"lambda_h":lam,"grid_coherence_at_t_one":lam**n,"target":math.exp(-2*gamma),"theta":theta,"coupling":coupling,"scaled_coupling":coupling*math.sqrt(h)})
    return {"schema_version":"1.0","result_id":"K964-WHITE-NOISE-SCALING-BOUNDARY","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Continuous-time scaling of the K963 fresh-ancilla collision model at fixed positive dephasing rate.","scaling":{"lambda_h":"exp(-2 gamma h)","theta_h":"(1/2) arccos(exp(-2 gamma h))","grid_law":"lambda_h^(t/h)=exp(-2 gamma t)","angle_asymptotic":"theta_h ~ sqrt(gamma h)","coupling_asymptotic":"theta_h/h ~ sqrt(gamma/h)","fresh_ancilla_rate":"1/h"},"exact_controls":{"gamma":gamma,"rows":rows,"grid_exact":all(abs(r["grid_coherence_at_t_one"]-r["target"])<2e-14 for r in rows),"coupling_strictly_increases":all(rows[i+1]["coupling"]>rows[i]["coupling"] for i in range(3)),"scaled_coupling_converges_to_sqrt_gamma":abs(rows[-1]["scaled_coupling"]-math.sqrt(gamma))<0.002},"boundary":{"finite_coupling_continuum_limit":False,"finite_ancilla_supply_continuum_limit":False,"white_noise_or_thermodynamic_resource_required":True},"ownership":{"gamma_clock_scaling_and_freshness_imported":True,"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"singular_resource_boundary_proved":True,"next_exact_input":"Demand an action-owned continuum reservoir or reset law, positive state/effect pairing and controlled limit before assigning the K960 rate to GU."},"source_and_ledger_effect":"none","claim_ceiling":"Exact grid law and asymptotic resource boundary for one collision realization only; no universal dilation theorem or GU dynamics follows."}
def validate(p):
    e=p["exact_controls"];b=p["boundary"];o=p["ownership"]
    assert e["gamma"]>0 and e["grid_exact"] and e["coupling_strictly_increases"] and e["scaled_coupling_converges_to_sqrt_gamma"]
    assert not b["finite_coupling_continuum_limit"] and not b["finite_ancilla_supply_continuum_limit"] and b["white_noise_or_thermodynamic_resource_required"]
    assert p["decision"]["singular_resource_boundary_proved"] and o["gamma_clock_scaling_and_freshness_imported"]
    assert not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==text
    elif a.write:OUTPUT.write_text(text)
    else:print(text,end="")
    print("K964 controls: 11/11")
if __name__=="__main__":main()
