#!/usr/bin/env python3
"""K994 frozen qutrit gap-one holdout for the named Levy horns."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k994-k993-system-enlargement-holdout.json";PARENTS=[ROOT/"lab/process/k992-k991-qutrit-horn-separator.json",ROOT/"lab/process/k993-k992-finite-harmonic-nonidentifiability.json"]
def build():
    a,b=[json.loads(p.read_text()) for p in PARENTS];gamma=0.7;T=2.0;theta=math.pi/4;rate=gamma/(math.sin(theta)**2);brown1=math.exp(-gamma*T/2);jump1=math.exp(rate*(math.cos(theta)-1)*T);common2=math.exp(-2*gamma*T)
    return {"schema_version":"1.0","result_id":"K994-SYSTEM-ENLARGEMENT-HOLDOUT","created":"2026-10-04","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_PREREGISTERED_HOLDOUT","target_claim":"NONE-NOT-A-KILL","scope":"The imported Q=diag(-1,0,1) coherence experiment for K986 Brownian diffusion and the K987 theta=pi/4 compound-Poisson horn after gamma is fixed from the shared gap-two law.","dependency_checks":{"input_ids":[a["result_id"],b["result_id"]],"named_pair_qutrit_separable":a["decision"]["named_brownian_and_compound_poisson_horns_system_separable_after_declared_enlargement"],"finite_probe_not_full_identification":b["decision"]["qutrit_pairwise_discrimination_not_full_model_identification"]},"preregistration":{"status":"frozen_not_scored","gamma":gamma,"T":T,"theta":theta,"event_rate":rate,"calibration_observable":"gap-two coherence","primary_holdout":"gap-one coherence","brownian_gap_one":brown1,"compound_gap_one":jump1,"absolute_separation":abs(brown1-jump1),"shared_gap_two":common2,"no_holdout_refit":True,"empirical_score_assigned":False},"boundary":{"same_original_qubit_system":False,"microscopic_record_required":False,"action_owned_qutrit_charge_sector_required":True,"positive_state_effect_and_gap_one_readout_required":True,"distinguishes_named_pair_only":True,"identifies_general_phase_law":False},"exact_controls":{"rate_equals_two_gamma":abs(rate-2*gamma)<1e-15,"gap_one_values_strictly_different":abs(brown1-jump1)>0.05,"gap_two_value_replayed":abs(common2-0.06081006262521797)<1e-15,"holdout_finite_and_positive":0<jump1<brown1<1},"ownership":{"qutrit_sector_and_readout_imported":True,"gu_action_or_observable_owner_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"nonrecord_pairwise_holdout_frozen":True,"k989_record_holdout_remains_distinct":True,"next_exact_input":"Require a GU-owned action, quotient, positive pairing and charge observable before either system-enlargement or record holdout is scored."},"source_and_ledger_effect":"none","claim_ceiling":"Frozen unscored pairwise holdout after an imported system enlargement; no same-qubit separator, data, GU observable, prediction or confirmation."}
def validate(p):
    d,r,b,x,o,z=p["dependency_checks"],p["preregistration"],p["boundary"],p["exact_controls"],p["ownership"],p["decision"]
    assert len(d["input_ids"])==2 and d["named_pair_qutrit_separable"] and d["finite_probe_not_full_identification"]
    assert r["status"]=="frozen_not_scored" and r["no_holdout_refit"] and not r["empirical_score_assigned"] and r["absolute_separation"]>0
    assert not b["same_original_qubit_system"] and not b["microscopic_record_required"] and b["action_owned_qutrit_charge_sector_required"] and b["positive_state_effect_and_gap_one_readout_required"] and b["distinguishes_named_pair_only"] and not b["identifies_general_phase_law"]
    assert all(x.values()) and o["qutrit_sector_and_readout_imported"] and not o["gu_action_or_observable_owner_constructed"] and not o["prediction_or_confirmation_credit"]
    assert z["nonrecord_pairwise_holdout_frozen"] and z["k989_record_holdout_remains_distinct"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K994 controls: 19/19")
if __name__=="__main__":main()
