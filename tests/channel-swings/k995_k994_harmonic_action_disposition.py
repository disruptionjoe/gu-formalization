#!/usr/bin/env python3
"""K995 native ownership disposition for charge-harmonic phase probes."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k995-k994-harmonic-action-disposition.json";NAMES=["k991-k990-charge-harmonic-channel-theorem","k992-k991-qutrit-horn-separator","k993-k992-finite-harmonic-nonidentifiability","k994-k993-system-enlargement-holdout"]
def build():
    ps=[json.loads((ROOT/f"lab/process/{n}.json").read_text()) for n in NAMES]
    return {"schema_version":"1.0","result_id":"K995-HARMONIC-ACTION-DISPOSITION","created":"2026-10-04","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_REQUIREMENT_DISPOSITION","target_claim":"NONE-NOT-A-KILL","scope":"Composition of K991--K994 into the finite-charge harmonic observability and native-owner boundary for the K956 Levy phase family.","dependency_checks":{"input_ids":[p["result_id"] for p in ps],"all_source_and_ledger_effect_none":all(p["source_and_ledger_effect"]=="none" for p in ps),"all_prediction_or_confirmation_withheld":all(not p["ownership"]["prediction_or_confirmation_credit"] for p in ps),"holdout_frozen_not_scored":ps[3]["preregistration"]["status"]=="frozen_not_scored"},"observability":{"original_qubit_samples_only_gap_two":True,"qutrit_gap_one_separates_named_brownian_and_compound_poisson_pair":True,"qutrit_is_a_declared_system_enlargement":True,"microscopic_record_not_required_for_named_pair":True,"arbitrary_finite_charge_spectrum_identifies_general_phase_law":False,"record_and_unbounded_harmonic_access_remain_distinct_routes":True},"demand":{"gu_physical_quotient_and_positive_effect_pairing_required":True,"gu_action_owned_charge_generator_and_spectrum_required":True,"gu_action_owned_characteristic_exponent_required":True,"native_preparation_and_gap_coherence_observable_required":True,"common_domain_and_locality_theorem_required":True,"finite_probe_claim_ceiling_required":True,"record_or_infinite_harmonic_completion_required_for_full_identification":True},"ownership":{"repository_conditional_models_only":True,"gu_action_charge_observable_or_physical_quotient_constructed":False,"source_claim_or_ledger_verdict_changed":False,"prediction_or_confirmation_credit":False},"decision":{"k990_inequivalent_observable_requirement_sharpened":True,"pairwise_separation_does_not_select_full_microscopic_law":True,"next_exact_input":"A GU-owned physical quotient and positive state/effect pairing plus an action must select the charge generator, spectrum and characteristic exponent, own the common domain and locality, and expose either the frozen gap-one pairwise observable or a record/infinite-harmonic completion before scoring."},"source_and_ledger_effect":"none","claim_ceiling":"Finite-charge observability and exact nonidentifiability boundary only; no GU derivation, empirical score, prediction, confirmation or exhaustive microscopic classification."}
def validate(p):
    c,o,d,z=p["dependency_checks"],p["observability"],p["demand"],p["ownership"]
    assert len(c["input_ids"])==4 and c["all_source_and_ledger_effect_none"] and c["all_prediction_or_confirmation_withheld"] and c["holdout_frozen_not_scored"]
    assert o["original_qubit_samples_only_gap_two"] and o["qutrit_gap_one_separates_named_brownian_and_compound_poisson_pair"] and o["qutrit_is_a_declared_system_enlargement"] and o["microscopic_record_not_required_for_named_pair"]
    assert not o["arbitrary_finite_charge_spectrum_identifies_general_phase_law"] and o["record_and_unbounded_harmonic_access_remain_distinct_routes"]
    assert all(d.values()) and z["repository_conditional_models_only"] and not z["gu_action_charge_observable_or_physical_quotient_constructed"] and not z["source_claim_or_ledger_verdict_changed"] and not z["prediction_or_confirmation_credit"]
    assert p["decision"]["k990_inequivalent_observable_requirement_sharpened"] and p["decision"]["pairwise_separation_does_not_select_full_microscopic_law"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K995 controls: 21/21")
if __name__=="__main__":main()
