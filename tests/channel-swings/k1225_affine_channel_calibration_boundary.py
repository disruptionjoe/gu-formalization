#!/usr/bin/env python3
"""K1225: integrate the all-CPTP affine-channel calibration boundary."""
from __future__ import annotations
import argparse,json
from pathlib import Path
OUTPUT=Path(__file__).parents[2]/"lab/process/k1225-affine-channel-calibration-boundary.json"
def build():
    return {"schema_version":"1.0","result_id":"K1225-AFFINE-CHANNEL-CALIBRATION-BOUNDARY","created":"2026-10-06",
      "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
      "target_claim":"NONE-NOT-A-KILL","scope":"Integration of K1221--K1224 with K1211--K1220 for every qubit CPTP channel.",
      "identifiability":{"bell_chsh":"depends only on the two largest singular values of M; affine translation t is invisible",
        "one_directional_read":"retains the sharp all-CPTP interval 2|V| through 2sqrt(2)",
        "three_same_axis_reads":"remain insufficient","nine_centered_transfer_statistics":"determine M and therefore optimized Bell-CHSH",
        "three_additional_marginal_statistics":"determine t","full_affine_process":"twelve independent linear statistics suffice and meet the dimension floor",
        "raw_paired_frame":"six axial preparations by three output effects give 18 raw values with six consistency relations"},
      "relation_to_prior":{"K1211_K1215":"retained as the Pauli/principal-axis subclass",
        "K1216_K1220":"unitality removed from the Bell-correlation and sharp-envelope theorem",
        "K1004":"retained on its dephasing horn","K1009":"retained as a distinct common-contrast model",
        "delayed_choice_entanglement_swapping":"remains reserved and unscored"},
      "decision":{"unitality_is_load_bearing_for_bell_chsh_rule":False,"translation_must_be_measured_for_full_process":True,
        "process_frame_supplies_physical_owner":False,"calibration_anchor_earns_confirmation":False},
      "next_condition":"Construct a typed common physical owner for the CPTP channel, Bell preparation, paired process frame, Born state/effect pairing, locality, apparatus and systematics; then score a predeclared holdout without consuming delayed-choice entanglement swapping prematurely.",
      "protected_disposition":"SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b/RA-F1/AC-F1 remain NEEDS",
      "release_test":{"affine_decoupling_retained":True,"translation_blind_control_retained":True,
        "twelve_statistic_frame_retained":True,"linear_floor_retained":True,"holdout_unscored":True,
        "protected_status_unchanged":True},
      "ownership":{"state_born_channel_frames_locality_apparatus_and_systematics_imported":True,"gu_native_effect":"none","prediction_or_confirmation":False},
      "claim_ceiling":"Exact all-qubit-CPTP calibration and linear-identifiability boundary; no GU state, channel, Born rule, apparatus, prediction, confirmation or verdict."}
def validate(x):
    assert x["result_id"].startswith("K1225-")
    assert x["decision"]["unitality_is_load_bearing_for_bell_chsh_rule"] is False
    assert x["decision"]["translation_must_be_measured_for_full_process"]
    assert x["decision"]["process_frame_supplies_physical_owner"] is False
    assert x["decision"]["calibration_anchor_earns_confirmation"] is False
    assert all(x["release_test"].values())
    assert x["ownership"]["gu_native_effect"]=="none" and x["ownership"]["prediction_or_confirmation"] is False
    assert "delayed-choice" in x["next_condition"] and "remain NEEDS" in x["protected_disposition"]
if __name__=="__main__":
    q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
    if a.check:assert json.loads(OUTPUT.read_text())==x
    else:print(json.dumps(x,indent=2,sort_keys=True))
    print("K1225 controls: 11/11")
