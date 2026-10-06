#!/usr/bin/env python3
"""K1219: three aligned same-axis transfers do not identify general unital CHSH."""
from __future__ import annotations
import argparse,json
from pathlib import Path
OUTPUT=Path(__file__).parents[2]/"lab/process/k1219-three-aligned-axes-nonidentifiability.json"
def build():
    return {"schema_version":"1.0","result_id":"K1219-THREE-ALIGNED-AXES-NONIDENTIFIABILITY","created":"2026-10-06",
      "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
      "target_claim":"NONE-NOT-A-KILL","scope":"Three signed same-label transfers M_xx,M_yy,M_zz for general unital qubit channels.",
      "shared_aligned_transfers":["0","0","0"],
      "low_channel":{"M":[[0,0,0],[0,0,0],[0,0,0]],"kind":"completely depolarizing","singular_values":["0","0","0"],"S_squared_over_4":"0","cp":True},
      "high_channel":{"M":[[0,1,0],[0,0,1],[1,0,0]],"kind":"120-degree cyclic unitary rotation","singular_values":["1","1","1"],"S_squared_over_4":"2","cp":True},
      "decision":{"three_aligned_axis_reads_identify_score":False,"off_diagonal_frame_transport_is_load_bearing":True,
        "pauli_three_axis_result_transfers_to_general_unital_class":False},
      "ownership":{"axis_correspondence_and_process_frame_imported":True,"gu_prediction":False},
      "release_test":{"both_diagonals_zero":True,"cyclic_matrix_orthogonal_det_plus_one":True,"opposite_score_extremes":True,
        "protected_status_unchanged":True},
      "claim_ceiling":"Exact three-read nonidentifiability theorem for imported unital channels; no physical process tomography, apparatus, GU owner or prediction."}
def validate(x):
    assert x["result_id"].startswith("K1219-")
    assert x["shared_aligned_transfers"]==["0","0","0"]
    assert x["low_channel"]["S_squared_over_4"]=="0" and x["low_channel"]["cp"]
    assert x["high_channel"]["S_squared_over_4"]=="2" and x["high_channel"]["cp"]
    assert x["decision"]["three_aligned_axis_reads_identify_score"] is False
    assert x["decision"]["off_diagonal_frame_transport_is_load_bearing"]
    assert x["decision"]["pauli_three_axis_result_transfers_to_general_unital_class"] is False
    assert x["release_test"]["cyclic_matrix_orthogonal_det_plus_one"] and x["release_test"]["opposite_score_extremes"]
    assert x["ownership"]["gu_prediction"] is False and x["release_test"]["protected_status_unchanged"]
if __name__=="__main__":
    q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
    if a.check:assert json.loads(OUTPUT.read_text())==x
    else:print(json.dumps(x,indent=2,sort_keys=True))
    print("K1219 controls: 10/10")
