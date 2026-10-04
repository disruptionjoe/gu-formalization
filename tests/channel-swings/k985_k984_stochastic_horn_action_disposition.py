#!/usr/bin/env python3
"""K985 action/domain disposition after the Poisson stochastic horn."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k985-k984-stochastic-horn-action-disposition.json";INPUTS=[ROOT/f"lab/process/{n}.json" for n in ["k981-k980-poisson-phase-flip-unravelling","k982-k981-poisson-generator-resource-boundary","k983-k982-system-only-nonidentifiability","k984-k983-record-sensitive-holdout"]]
def build():
    ps=[json.loads(p.read_text()) for p in INPUTS]
    return {"schema_version":"1.0","result_id":"K985-STOCHASTIC-HORN-ACTION-DISPOSITION","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_REQUIREMENT_DISPOSITION","target_claim":"NONE-NOT-A-KILL","scope":"Composition of K981--K984 into the revised microscopic horn, identifiability and native-owner boundary for K956.","dependency_checks":{"input_ids":[p["result_id"] for p in ps],"all_source_and_ledger_effect_none":all(p["source_and_ledger_effect"]=="none" for p in ps),"all_prediction_or_confirmation_withheld":all(not p["ownership"]["prediction_or_confirmation_credit"] for p in ps),"record_holdout_frozen_not_scored":ps[3]["preregistration"]["status"]=="frozen_not_scored"},"revised_fork":{"bounded_autonomous_fixed_product_horn":"excluded by K976--K977","deterministic_fresh_grid_horn":"uniformly convergent with h^-1/2 coupling and 1/h refresh costs","poisson_phase_flip_horn":"exact reduced semigroup at finite event rate with imported stochastic clock and point jumps","unbounded_spectral_horn":"exact only on singular energy-domain state in K966--K975","classification_exhaustive":False},"identifiability":{"system_only_endpoint_data_selects_microscopic_horn":False,"record_or_environment_sensitive_holdout_required":True,"poisson_count_holdout_frozen":True,"empirical_score_assigned":False},"demand":{"gu_physical_quotient_and_positive_effect_pairing_required":True,"gu_action_owned_local_or_stochastic_coupling_required":True,"selected_horn_and_common_domain_required":True,"clock_reset_limit_or_record_accounting_required":True,"remote_marginal_and_locality_theorem_required":True,"inequivalent_native_holdout_and_observable_required":True},"ownership":{"repository_conditional_models_only":True,"gu_action_clock_record_or_physical_quotient_constructed":False,"source_claim_or_ledger_verdict_changed":False,"prediction_or_confirmation_credit":False},"decision":{"deterministic_grid_cost_not_promoted_to_universal_markov_cost":True,"stochastic_repair_does_not_supply_gu_owner":True,"next_exact_input":"A GU-owned physical quotient and positive state/effect pairing plus an action must select and control a microscopic horn, own its common domain, locality and clock/reset/record resources, and expose an inequivalent native holdout observable before scoring."},"source_and_ledger_effect":"none","claim_ceiling":"Non-exhaustive microscopic fork and unscored native-owner requirement only; no empirical score, GU derivation, prediction, confirmation or protected verdict."}
def validate(p):
    c,f,i,d,o,x=p["dependency_checks"],p["revised_fork"],p["identifiability"],p["demand"],p["ownership"],p["decision"]
    assert len(c["input_ids"])==4 and c["all_source_and_ledger_effect_none"] and c["all_prediction_or_confirmation_withheld"] and c["record_holdout_frozen_not_scored"]
    assert len(f)==5 and not f["classification_exhaustive"]
    assert not i["system_only_endpoint_data_selects_microscopic_horn"] and i["record_or_environment_sensitive_holdout_required"] and i["poisson_count_holdout_frozen"] and not i["empirical_score_assigned"]
    assert all(d.values())
    assert o["repository_conditional_models_only"] and not o["gu_action_clock_record_or_physical_quotient_constructed"] and not o["source_claim_or_ledger_verdict_changed"] and not o["prediction_or_confirmation_credit"]
    assert x["deterministic_grid_cost_not_promoted_to_universal_markov_cost"] and x["stochastic_repair_does_not_supply_gu_owner"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K985 controls: 18/18")
if __name__=="__main__":main()
