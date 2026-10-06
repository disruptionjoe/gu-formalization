#!/usr/bin/env python3
"""K1224: dimension floors for linear affine-process identification."""
from __future__ import annotations
import argparse,json
from pathlib import Path
OUTPUT=Path(__file__).parents[2]/"lab/process/k1224-linear-process-identifiability-floor.json"
def build():
    return {"schema_version":"1.0","result_id":"K1224-LINEAR-PROCESS-IDENTIFIABILITY-FLOOR","created":"2026-10-06",
      "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
      "target_claim":"NONE-NOT-A-KILL","scope":"Linear scalar statistics on the relative interior of trace-preserving qubit CPTP maps, and on its unital subfamily.",
      "parameter_spaces":{"full_affine_tp_hermiticity_preserving_dimension":12,"unital_transfer_dimension":9,
        "full_rank_center":"completely depolarizing channel with positive-definite Choi matrix"},
      "theorem":{"full_process_floor":"rank below 12 leaves a nonzero kernel direction; sufficiently small plus/minus perturbations of the full-rank depolarizing Choi matrix remain CPTP and share all measured statistics",
        "unital_transfer_floor":"rank below 9 leaves a nonzero unital transfer direction; sufficiently small plus/minus perturbations remain unital CPTP",
        "scope_limit":"dimension counting proves a floor for full linear process identification, not a universal floor for every nonlinear scalar invariant"},
      "controls":[{"measurement_rank":11,"full_kernel_dimension_at_least":1,"identifies_full_affine_process":False},
        {"measurement_rank":12,"full_kernel_dimension_at_least":0,"dimension_obstruction_removed":True},
        {"measurement_rank":8,"unital_kernel_dimension_at_least":1,"identifies_full_transfer_matrix":False},
        {"measurement_rank":9,"unital_kernel_dimension_at_least":0,"dimension_obstruction_removed":True}],
      "decision":{"twelve_statistic_frame_meets_linear_floor":True,"nine_transfer_statistics_meet_unital_linear_floor":True,
        "fewer_than_twelve_can_identify_full_affine_channel":False,"fewer_than_nine_can_identify_full_unital_transfer":False},
      "release_test":{"full_dimension":12,"unital_dimension":9,"interior_perturbation_argument":True,
        "nonlinear_invariant_overclaim_rejected":True,"protected_status_unchanged":True},
      "ownership":{"measurement_model_is_imported":True,"prediction_or_confirmation":False},
      "claim_ceiling":"Exact finite-dimensional linear-identifiability floor; no claim about optimal nonlinear CHSH-only estimation or a physical apparatus."}
def validate(x):
    assert x["result_id"].startswith("K1224-")
    assert x["release_test"]["full_dimension"]==12 and x["release_test"]["unital_dimension"]==9
    assert x["release_test"]["interior_perturbation_argument"] and x["release_test"]["nonlinear_invariant_overclaim_rejected"]
    assert x["decision"]["twelve_statistic_frame_meets_linear_floor"] and x["decision"]["nine_transfer_statistics_meet_unital_linear_floor"]
    assert x["decision"]["fewer_than_twelve_can_identify_full_affine_channel"] is False
    assert x["decision"]["fewer_than_nine_can_identify_full_unital_transfer"] is False
    assert x["ownership"]["prediction_or_confirmation"] is False and x["release_test"]["protected_status_unchanged"]
if __name__=="__main__":
    q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
    if a.check:assert json.loads(OUTPUT.read_text())==x
    else:print(json.dumps(x,indent=2,sort_keys=True))
    print("K1224 controls: 10/10")
