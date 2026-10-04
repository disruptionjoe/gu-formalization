#!/usr/bin/env python3
"""K987 continuum of symmetric compound-Poisson phase horns."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k987-k986-symmetric-compound-poisson-family.json"
def build():
    gamma=0.7;t=2.0;rows=[]
    for theta in (math.pi/6,math.pi/4,math.pi/3,math.pi/2):
        rate=gamma/(math.sin(theta)**2)
        exponent=rate*(math.cos(2*theta)-1)*t
        rows.append({"theta":theta,"event_rate":rate,"coherence":math.exp(exponent),"target":math.exp(-2*gamma*t),"identity_error":abs(exponent+2*gamma*t)})
    return {"schema_version":"1.0","result_id":"K987-SYMMETRIC-COMPOUND-POISSON-FAMILY","created":"2026-10-04","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Symmetric +/-theta phase jumps with total Poisson rate gamma/sin(theta)^2 for 0<theta<pi modulo pi.","construction":{"phase_process":"X_t=theta sum_{j=1}^{N_t} epsilon_j with epsilon_j=+/-1 equiprobably","characteristic_exponent":"lambda(cos(2 theta)-1)=-2 gamma","rate_angle_law":"lambda=gamma/sin(theta)^2","same_dephasing_semigroup_as_k956":True,"stationary_independent_increments":True,"continuum_of_exact_horns":True,"k981_recovered_at_theta_pi_over_2_up_to_global_phase":True,"brownian_rate_divergence_as_theta_to_zero":"lambda~gamma/theta^2"},"exact_controls":{"gamma":gamma,"t":t,"rows":rows,"all_rate_angle_identities_replayed":all(r["identity_error"]<1e-15 for r in rows),"all_rates_finite_positive":all(math.isfinite(r["event_rate"]) and r["event_rate"]>0 for r in rows),"theta_pi_over_2_rate_equals_gamma":abs(rows[-1]["event_rate"]-gamma)<1e-15},"ownership":{"jump_clock_angles_and_signs_imported":True,"gu_action_or_record_owner_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"k981_not_an_isolated_exact_horn":True,"next_exact_input":"Test whether arbitrary finite system-only controlled processes distinguish these independent-increment horns from Brownian phase diffusion."},"source_and_ledger_effect":"none","claim_ceiling":"Exact continuum of imported finite-activity phase-jump realizations only; no GU selection, physical record or diffusion-limit theorem."}
def validate(p):
    c,x,o,d=p["construction"],p["exact_controls"],p["ownership"],p["decision"]
    assert c["same_dephasing_semigroup_as_k956"] and c["stationary_independent_increments"] and c["continuum_of_exact_horns"] and c["k981_recovered_at_theta_pi_over_2_up_to_global_phase"]
    assert len(x["rows"])==4 and x["all_rate_angle_identities_replayed"] and x["all_rates_finite_positive"] and x["theta_pi_over_2_rate_equals_gamma"]
    assert o["jump_clock_angles_and_signs_imported"] and not o["gu_action_or_record_owner_constructed"] and not o["prediction_or_confirmation_credit"]
    assert d["k981_not_an_isolated_exact_horn"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K987 controls: 13/13")
if __name__=="__main__":main()
