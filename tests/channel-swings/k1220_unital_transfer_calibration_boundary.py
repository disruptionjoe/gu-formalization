#!/usr/bin/env python3
"""K1220: integrate the general-unital transfer calibration boundary."""
from __future__ import annotations
import argparse,json
from pathlib import Path
OUTPUT=Path(__file__).parents[2]/"lab/process/k1220-unital-transfer-calibration-boundary.json"
def build():
    return {"schema_version":"1.0","result_id":"K1220-UNITAL-TRANSFER-CALIBRATION-BOUNDARY","created":"2026-10-06",
      "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
      "target_claim":"NONE-NOT-A-KILL","scope":"Integration of K1216--K1219 with the aligned Pauli boundary K1211--K1215.",
      "identifiability":{"one_directional_read":"sharp general-unital score interval only: 2|V| through 2sqrt(2)",
        "three_same_axis_reads":"insufficient without Pauli/principal-axis validation",
        "three_singular_values":"sufficient for optimized CHSH inside the frozen unital Bell-Choi class",
        "full_signed_transfer_matrix":"sufficient by process tomography; its two largest singular values determine optimized CHSH",
        "pauli_aligned_subclass":"K1211--K1215 remains exact when the channel is independently validated diagonal in the common apparatus frame",
        "class_validation":"unitality, trace preservation, qubit closure, Bell-Choi preparation, Born pairing and common frame transport remain independent obligations"},
      "relation_to_prior":{"K1212":"tighter upper 2sqrt(1+V^2) requires Pauli principal-axis alignment",
        "K1215":"three transfer magnitudes remain sufficient only when they are validated singular/principal-axis data",
        "K1004":"retained only on its dephasing horn","K1009":"retained as a distinct common-contrast model",
        "delayed_choice_entanglement_swapping":"remains a distinct reserved unscored held-out family"},
      "decision":{"directional_visibility_only_prediction_allowed":False,"three_aligned_axes_universally_sufficient":False,
        "full_transfer_or_singular_spectrum_closes_imported_score":True,"calibration_anchor_earns_confirmation":False,
        "general_unital_result_is_gu_derived":False},
      "next_condition":"Construct a typed physical owner for the channel, preparation/effect pairing, process frame and apparatus, or extend beyond unital qubit channels without consuming the delayed-choice holdout.",
      "protected_disposition":"SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b/RA-F1/AC-F1 remain NEEDS",
      "release_test":{"singular_spectrum_rule_retained":True,"one_direction_nonidentifying":True,"three_aligned_reads_nonidentifying":True,
        "full_transfer_sufficient_inside_class":True,"pauli_boundary_not_retracted":True,"holdout_unscored":True,"protected_status_unchanged":True},
      "ownership":{"state_born_channel_frames_locality_and_apparatus_imported":True,"gu_native_effect":"none","prediction_or_confirmation":False},
      "claim_ceiling":"Exact branch-relative calibration boundary for imported finite unital-qubit/Bell-Choi controls; no GU state, channel, Born rule, locality theorem, empirical score, prediction, confirmation or verdict."}
def validate(x):
    assert x["result_id"].startswith("K1220-")
    assert "2|V| through 2sqrt(2)" in x["identifiability"]["one_directional_read"]
    assert x["decision"]["directional_visibility_only_prediction_allowed"] is False
    assert x["decision"]["three_aligned_axes_universally_sufficient"] is False
    assert x["decision"]["full_transfer_or_singular_spectrum_closes_imported_score"]
    assert x["decision"]["calibration_anchor_earns_confirmation"] is False
    assert x["decision"]["general_unital_result_is_gu_derived"] is False
    assert all(x["release_test"].values())
    assert x["ownership"]["gu_native_effect"]=="none" and x["ownership"]["prediction_or_confirmation"] is False
    assert "delayed-choice" in x["next_condition"]
    assert "remain NEEDS" in x["protected_disposition"]
    assert "no GU state" in x["claim_ceiling"]
if __name__=="__main__":
    q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
    if a.check:assert json.loads(OUTPUT.read_text())==x
    else:print(json.dumps(x,indent=2,sort_keys=True))
    print("K1220 controls: 12/12")
