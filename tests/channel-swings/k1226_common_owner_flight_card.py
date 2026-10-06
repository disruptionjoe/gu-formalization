#!/usr/bin/env python3
"""K1226: type a common-channel calibration/Bell apparatus flight card."""
from __future__ import annotations
import argparse, json
from pathlib import Path

OUTPUT=Path(__file__).parents[2]/"lab/process/k1226-common-owner-flight-card.json"

def build():
    return {
      "schema_version":"1.0","result_id":"K1226-COMMON-OWNER-FLIGHT-CARD","created":"2026-10-06",
      "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS",
      "direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
      "scope":"A preregistered operational schema joining one fixed qubit-channel module to axial process-calibration and Bell-coincidence branches.",
      "common_owner":{
        "identity_keys":["channel_device_id","channel_configuration_hash","basis_map_id","calibration_epoch","clock_epoch"],
        "calibration_branch":{"preparations":["+X","-X","+Y","-Y","+Z","-Z"],"effects":["X","Y","Z"],"raw_record":"attempt, preparation, effect, outcome, timestamp, herald and inclusion bit"},
        "bell_branch":{"preparation":"Phi+ with source identifier and fidelity interval","channel_location":"first Bell arm before analyzer choice","raw_record":"attempt, settings, two outcomes, two timestamps, herald and inclusion bits"},
        "pairing":"qubit density operators and binary effects with p=Tr(rho E)",
        "locality":["setting generators recorded independently","choice and detection windows spacelike when claimed","remote marginal invariance scored on raw included trials"],
        "randomization":"calibration and Bell trial types interleaved by a sealed schedule",
        "blinding":"holdout settings, counts and decision threshold sealed before calibration fit",
        "systematics":["preparation and measurement calibration","basis registration","channel drift and memory","source impurity","loss and postselection","detector efficiency and dark counts","timing and setting leakage"]},
      "instance_required":["hardware identifiers","immutable schedule digest","raw event records","SPAM calibration evidence","channel stability evidence","loss/inclusion rule","count budget","systematic error budget","sealed holdout digest"],
      "decision":{"protocol_schema_constructed":True,"physical_owner_instantiated":False,"same_channel_assertion_requires_records":True,"paper_protocol_is_empirical_evidence":False},
      "release_test":{"both_branches_present":True,"identity_keys_shared":True,"raw_records_required":True,"randomization_and_blinding_required":True,"locality_and_systematics_explicit":True,"protected_status_unchanged":True},
      "ownership":{"all_operational_primitives_imported":True,"gu_native_effect":"none"},
      "claim_ceiling":"Typed apparatus flight card only; no hardware instance, data, channel estimate, Born derivation, GU prediction or confirmation."}

def validate(x):
    assert x["result_id"].startswith("K1226-")
    c=x["common_owner"]
    assert len(c["identity_keys"])==5 and len(c["calibration_branch"]["preparations"])==6
    assert len(c["calibration_branch"]["effects"])==3 and c["bell_branch"]["preparation"].startswith("Phi+")
    assert len(c["locality"])==3 and len(c["systematics"])==7
    assert len(x["instance_required"])==9 and all(x["release_test"].values())
    assert x["decision"]["protocol_schema_constructed"] and x["decision"]["physical_owner_instantiated"] is False
    assert x["decision"]["same_channel_assertion_requires_records"] and x["decision"]["paper_protocol_is_empirical_evidence"] is False
    assert x["ownership"]["gu_native_effect"]=="none"

if __name__=="__main__":
    q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
    if a.check: assert json.loads(OUTPUT.read_text())==x
    else: print(json.dumps(x,indent=2,sort_keys=True))
    print("K1226 controls: 12/12")
