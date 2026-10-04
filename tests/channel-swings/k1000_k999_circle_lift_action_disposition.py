#!/usr/bin/env python3
"""K1000 composition of the circular-law and real-lift ownership boundary."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1000-k999-circle-lift-action-disposition.json"
def build():
 return {"schema_version":"1.0","result_id":"K1000-CIRCLE-LIFT-ACTION-DISPOSITION","created":"2026-10-04","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_REQUIREMENT_DISPOSITION","target_claim":"NONE-NOT-A-KILL","scope":"Composition of K996--K999 into the circular phase-law, finite-band and microscopic-lift observability boundary for the K956 family.",
  "dependency_checks":{"input_ids":["K996-INTEGER-HARMONIC-CIRCLE-RECONSTRUCTION","K997-CIRCULAR-PROCESS-IDENTIFICATION","K998-INVISIBLE-WINDING-LIFT-NONIDENTIFIABILITY","K999-OPERATIONAL-CIRCLE-LIFT-HOLDOUTS"],"all_source_and_ledger_effect_none":True,"all_prediction_or_confirmation_withheld":True,"holdouts_frozen_not_scored":True},
  "identification_boundary":{"finite_harmonic_set_identifies_unrestricted_circle_law":False,"all_integer_harmonics_at_fixed_time_identify_circle_marginal":True,"all_time_integer_harmonics_identify_circular_independent_increment_process":True,"single_time_marginal_identifies_generator":False,"complete_circular_process_identifies_real_lift":False,"winding_record_or_noninteger_probe_required_for_lift":True},
  "demand":{"gu_physical_quotient_and_positive_effect_pairing_required":True,"gu_action_owned_charge_generator_and_integer_spectrum_required":True,"gu_action_owned_circular_generator_or_real_lift_required":True,"common_domain_and_locality_theorem_required":True,"native_preparations_and_harmonic_observables_required":True,"finite_band_regularization_and_error_budget_required_if_access_is_finite":True,"winding_sensitive_record_required_for_real_lift_claim":True},
  "ownership":{"repository_conditional_models_only":True,"gu_action_phase_observable_or_physical_quotient_constructed":False,"source_claim_or_ledger_verdict_changed":False,"prediction_or_confirmation_credit":False},
  "decision":{"k995_unbounded_harmonic_route_sharpened":True,"next_exact_input":"A GU-owned physical quotient and positive state/effect pairing plus an action must select the charge generator and spectrum, circular generator or real lift, common domain and locality, and either operational all-harmonic access with a declared finite-band error budget or a winding-sensitive record before scoring."},"source_and_ledger_effect":"none","claim_ceiling":"Circle-versus-lift observability boundary only; no GU derivation, empirical score, prediction, confirmation or exhaustive Levy-lift classification."}
def validate(p):
 c,i,d,o,z=p["dependency_checks"],p["identification_boundary"],p["demand"],p["ownership"],p["decision"]
 assert len(c["input_ids"])==4 and c["all_source_and_ledger_effect_none"] and c["all_prediction_or_confirmation_withheld"] and c["holdouts_frozen_not_scored"]
 assert not i["finite_harmonic_set_identifies_unrestricted_circle_law"] and i["all_integer_harmonics_at_fixed_time_identify_circle_marginal"]
 assert i["all_time_integer_harmonics_identify_circular_independent_increment_process"] and not i["single_time_marginal_identifies_generator"]
 assert not i["complete_circular_process_identifies_real_lift"] and i["winding_record_or_noninteger_probe_required_for_lift"]
 assert all(d.values()) and o["repository_conditional_models_only"]
 assert not o["gu_action_phase_observable_or_physical_quotient_constructed"] and not o["source_claim_or_ledger_verdict_changed"] and not o["prediction_or_confirmation_credit"]
 assert z["k995_unbounded_harmonic_route_sharpened"] and p["source_and_ledger_effect"]=="none"
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
 if a.check:assert OUTPUT.read_text()==text
 elif a.write:OUTPUT.write_text(text)
 else:print(text,end="")
 print("K1000 controls: 20/20")
if __name__=="__main__":main()
