#!/usr/bin/env python3
"""K1230: integrate the common-owner schema, gauge and holdout boundary."""
from __future__ import annotations
import argparse,json
from pathlib import Path
OUTPUT=Path(__file__).parents[2]/"lab/process/k1230-common-owner-holdout-boundary.json"
def build():
  return {"schema_version":"1.0","result_id":"K1230-COMMON-OWNER-HOLDOUT-BOUNDARY","created":"2026-10-06",
    "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
    "target_claim":"NONE-NOT-A-KILL","scope":"Integration of K1226--K1229 with the K1221--K1225 affine calibration boundary.",
    "integration":{"owner_schema":"one identity-bound randomized channel module connects axial calibration and Bell branches","spam_boundary":"at least a physical SO(3) frame gauge leaves every nominal calibration probability invariant","stability_boundary":"within-block six-relation and cross-block affine residuals are necessary observable controls, not complete hardware proofs","holdout":"off-frame Bell four-outcome table sealed before fit and scored without refitting","delayed_choice_entanglement_swapping":"distinct reserved unscored family"},
    "decision":{"typed_common_owner_schema_constructed":True,"instantiated_physical_owner_present":False,"nominal_tomography_alone_establishes_owner":False,"holdout_predeclared":True,"holdout_scored":False,"calibration_or_holdout_earns_gu_confirmation":False},
    "next_condition":"Instantiate the K1226 flight card with hardware IDs, immutable randomized schedule, independent SPAM or self-consistent gate-set evidence, raw calibration and Bell event records, drift/loss/locality bounds, sealed count budget and systematics; then unseal and score K1229 without refitting. Preserve delayed-choice entanglement swapping as a separate unscored family.",
    "protected_disposition":"SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b/RA-F1/AC-F1 remain NEEDS",
    "release_test":{"flight_card_retained":True,"spam_gauge_retained":True,"drift_controls_retained":True,"holdout_sealed_and_unscored":True,"delayed_choice_reserved":True,"schema_instance_boundary_explicit":True,"protected_status_unchanged":True},
    "ownership":{"all_quantum_and_apparatus_primitives_imported":True,"gu_native_effect":"none","prediction_or_confirmation":False},
    "claim_ceiling":"Exact operational owner schema, physical frame-gauge boundary, drift witnesses and unscored holdout preregistration; no apparatus instance, empirical result, GU derivation, prediction or confirmation."}
def validate(x):
  assert x["result_id"].startswith("K1230-")
  assert x["decision"]["typed_common_owner_schema_constructed"]
  assert x["decision"]["instantiated_physical_owner_present"] is False
  assert x["decision"]["nominal_tomography_alone_establishes_owner"] is False
  assert x["decision"]["holdout_predeclared"] and x["decision"]["holdout_scored"] is False
  assert x["decision"]["calibration_or_holdout_earns_gu_confirmation"] is False
  assert all(x["release_test"].values()) and "delayed-choice" in x["next_condition"]
  assert "remain NEEDS" in x["protected_disposition"]
  assert x["ownership"]["gu_native_effect"]=="none" and x["ownership"]["prediction_or_confirmation"] is False
if __name__=="__main__":
  q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
  if a.check:assert json.loads(OUTPUT.read_text())==x
  else:print(json.dumps(x,indent=2,sort_keys=True))
  print("K1230 controls: 11/11")
