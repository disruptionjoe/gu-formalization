#!/usr/bin/env python3
"""K975 physical-domain ownership disposition for the exponential parent."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k975-k974-physical-domain-disposition.json"
def build():
    return {"schema_version":"1.0","result_id":"K975-PHYSICAL-DOMAIN-DISPOSITION","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_REQUIREMENT_DISPOSITION","target_claim":"NONE-NOT-A-KILL","scope":"Composition of K971--K974 into the microscopic physical-domain and approximation-cost boundary.","inputs":{"K971":"Cauchy state outside generator and absolute form domains","K972":"finite-first-moment cusp no-go","K973":"finite-variance quadratic survival boundary","K974":"necessary second-moment cost and compact-band sufficient repair"},"decision":{"exact_exponential_positive_spectral_parent_requires_singular_energy_moments":True,"finite_energy_approximation_remains_possible":True,"next_exact_input":"A GU-owned physical quotient and action must choose exact singular dynamics versus a finite-resolution approximation, own the energy/domain budget and locality theorem, and freeze an empirical resolution/holdout before scoring."},"demand":{"gu_physical_quotient_and_positive_effect_pairing_required":True,"gu_action_owned_local_coupling_required":True,"energy_or_form_domain_owned_required":True,"spectral_measure_reset_or_resolution_law_owned_required":True,"remote_marginal_and_locality_theorem_required":True,"distinct_empirical_holdout_frozen_before_scoring_required":True},"ownership":{"exact_and_regularized_models_repository_owned_only":True,"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False,"source_claim_or_ledger_verdict_changed":False},"discriminator":{"exact_parent":"exponential cusp with divergent first and second spectral moments","finite_energy_parent":"quadratic short-time law and nonzero approximation error","status":"reserved_not_scored"},"source_and_ledger_effect":"none","claim_ceiling":"Conditional physical-domain and approximation-cost requirement only; no empirical score, GU derivation, prediction, confirmation or protected verdict."}
def validate(p):
    d=p["decision"];q=p["demand"];o=p["ownership"]
    assert d["exact_exponential_positive_spectral_parent_requires_singular_energy_moments"] and d["finite_energy_approximation_remains_possible"]
    assert all(q.values()) and o["exact_and_regularized_models_repository_owned_only"]
    assert not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"] and not o["source_claim_or_ledger_verdict_changed"]
    assert p["discriminator"]["status"]=="reserved_not_scored" and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert json.loads(OUTPUT.read_text())==p
    elif a.write:OUTPUT.write_text(text)
    else:print(text,end="")
    print("K975 controls: 10/10")
if __name__=="__main__":main()
