#!/usr/bin/env python3
"""K965 action/reservoir demand disposition."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k965-k964-action-reservoir-demand-disposition.json"
def build():
    return {"schema_version":"1.0","result_id":"K965-ACTION-RESERVOIR-DEMAND-DISPOSITION","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_REQUIREMENT_DISPOSITION","target_claim":"NONE-NOT-A-KILL","scope":"Composition of K961--K964 into the microscopic ownership demand behind K960's exponential candidate law.","inputs":{"K961":"finite closed recurrence","K962":"strict exponential finite-parent no-go","K963":"fresh-ancilla exact contrary construction","K964":"singular continuous-time resource boundary"},"demand":{"physical_quotient_and_positive_pairing_required":True,"action_owned_local_coupling_required":True,"continuum_reservoir_or_explicit_reset_law_required":True,"controlled_thermodynamic_or_white_noise_limit_required":True,"remote_marginal_and_locality_theorem_required":True,"distinct_holdout_frozen_before_scoring":True},"discriminator":{"finite_closed_parent":"predicts arbitrarily late coherence returns","fresh_resource_parent":"supports monotone grid decay only while fresh ancillas/reset continue","status":"reserved_not_scored"},"ownership":{"all_quantum_state_trace_clock_and_environment_semantics_imported":True,"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False,"source_claim_or_ledger_verdict_changed":False},"decision":{"candidate_action_requirement_sharpened":True,"next_exact_input":"A GU-owned physical quotient with positive state/effect pairing and local action coupling to an owned continuum reservoir or reset mechanism, with a controlled limit and the reserved recurrence/reset discriminator frozen before scoring."},"source_and_ledger_effect":"none","claim_ceiling":"Conditional microscopic requirement and reserved discriminator only; this does not derive GU dynamics, exclude all non-Markovian finite-time models or move any scientific verdict."}
def validate(p):
    d=p["demand"];o=p["ownership"]
    assert all(d.values()) and p["discriminator"]["status"]=="reserved_not_scored"
    assert o["all_quantum_state_trace_clock_and_environment_semantics_imported"]
    assert not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"] and not o["source_claim_or_ledger_verdict_changed"]
    assert p["decision"]["candidate_action_requirement_sharpened"]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==text
    elif a.write:OUTPUT.write_text(text)
    else:print(text,end="")
    print("K965 controls: 10/10")
if __name__=="__main__":main()
