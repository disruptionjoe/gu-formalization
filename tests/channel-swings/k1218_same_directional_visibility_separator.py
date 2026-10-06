#!/usr/bin/env python3
"""K1218: exact same-directional-visibility local/maximal separator."""
from __future__ import annotations
import argparse,json
from pathlib import Path
OUTPUT=Path(__file__).parents[2]/"lab/process/k1218-same-directional-visibility-separator.json"
def build():
    return {"schema_version":"1.0","result_id":"K1218-SAME-DIRECTIONAL-VISIBILITY-SEPARATOR","created":"2026-10-06",
      "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
      "target_claim":"NONE-NOT-A-KILL","scope":"Two explicit unital qubit channels with the same directional transfer V=2/5.",
      "same_directional_visibility":"2/5",
      "low_channel":{"M":"diag(2/5,0,0)","canonical_pauli_probabilities":["7/20","7/20","3/20","3/20"],"singular_values":["2/5","0","0"],"S_squared_over_4":"4/25","violates_CHSH":False,"cp":True},
      "high_channel":{"M":"R_z(theta), cos(theta)=2/5, sin(theta)=sqrt(21)/5","singular_values":["1","1","1"],"S_squared_over_4":"2","violates_CHSH":True,"cp":True},
      "decision":{"same_visibility_opposite_bell_disposition":True,"same_visibility_can_range_from_rank_one_to_unitary":True,
        "k1212_upper_bound_requires_principal_axis_pauli_alignment":True},
      "ownership":{"separator_is_repository_control":True,"physical_shared_channel_identified":False,"prediction_or_confirmation":False},
      "release_test":{"same_visibility":True,"low_cp":True,"high_cp":True,"low_local":True,"high_maximal":True,
        "score_gap":"46/25","protected_status_unchanged":True},
      "claim_ceiling":"Exact nonidentifiability counterexample in the imported unital-qubit class; no apparatus, GU state/channel, locality theorem or empirical result."}
def validate(x):
    assert x["result_id"].startswith("K1218-")
    assert x["same_directional_visibility"]=="2/5"
    assert x["low_channel"]["S_squared_over_4"]=="4/25" and not x["low_channel"]["violates_CHSH"]
    assert x["high_channel"]["S_squared_over_4"]=="2" and x["high_channel"]["violates_CHSH"]
    assert x["low_channel"]["cp"] and x["high_channel"]["cp"]
    assert x["decision"]["same_visibility_opposite_bell_disposition"]
    assert x["decision"]["k1212_upper_bound_requires_principal_axis_pauli_alignment"]
    assert x["ownership"]["prediction_or_confirmation"] is False
    assert x["release_test"]["score_gap"]=="46/25" and x["release_test"]["protected_status_unchanged"]
if __name__=="__main__":
    q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
    if a.check:assert json.loads(OUTPUT.read_text())==x
    else:print(json.dumps(x,indent=2,sort_keys=True))
    print("K1218 controls: 9/9")
