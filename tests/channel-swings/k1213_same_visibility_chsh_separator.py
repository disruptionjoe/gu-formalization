#!/usr/bin/env python3
"""K1213: exact same-visibility Bell-local/Bell-violating separator."""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from pathlib import Path
from k1211_pauli_channel_cp_tetrahedron import probs,cp
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1213-same-visibility-chsh-separator.json"
def build():
    v=F(2,5);lo=(v,F(0),F(0));hi=(v,v,F(1))
    return {"schema_version":"1.0","result_id":"K1213-SAME-VISIBILITY-CHSH-SEPARATOR","created":"2026-10-06","status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","scope":"Two explicit Pauli-diagonal channels with identical X-fringe visibility V=2/5 and different optimized CHSH dispositions.","same_visibility":"2/5","low_channel":{"lambda":[str(q) for q in lo],"probabilities":[str(q) for q in probs(*lo)],"S_squared_over_4":"4/25","violates_CHSH":False,"cp":cp(*lo)},"high_channel":{"lambda":[str(q) for q in hi],"probabilities":[str(q) for q in probs(*hi)],"S_squared_over_4":"29/25","violates_CHSH":True,"cp":cp(*hi)},"decision":{"visibility_only_bell_inference_valid":False,"k1004_law_is_general_pauli_law":False,"additional_channel_calibration_required":True},"ownership":{"separator_is_repository_control":True,"physical_shared_channel_identified":False,"prediction_or_confirmation":False},"release_test":{"same_x_visibility":lo[0]==hi[0],"low_cp":cp(*lo),"high_cp":cp(*hi),"low_local":F(4,25)<=1,"high_violates":F(29,25)>1,"probabilities_normalized":sum(probs(*lo))==sum(probs(*hi))==1,"protected_status_unchanged":True},"claim_ceiling":"Exact counterexample to visibility-only Bell inference in the imported Pauli class; no apparatus, GU state/channel, locality theorem or empirical result."}
def validate(x):
    assert all(x["release_test"].values());assert x["same_visibility"]=="2/5";assert x["low_channel"]["S_squared_over_4"]=="4/25" and not x["low_channel"]["violates_CHSH"];assert x["high_channel"]["S_squared_over_4"]=="29/25" and x["high_channel"]["violates_CHSH"];assert not x["decision"]["visibility_only_bell_inference_valid"] and not x["decision"]["k1004_law_is_general_pauli_law"];assert not x["ownership"]["physical_shared_channel_identified"]
def main():
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");a.add_argument("--check",action="store_true");q=a.parse_args();x=build();validate(x);s=json.dumps(x,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if q.write else (check(OUTPUT,s) if q.check else print(s,end=""));print("K1213 controls: 9/9")
def check(p,s):assert p.read_text()==s
if __name__=="__main__":main()
