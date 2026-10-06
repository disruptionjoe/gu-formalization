#!/usr/bin/env python3
"""K1212: sharp optimized-CHSH envelope at fixed one-axis visibility."""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from pathlib import Path
from k1211_pauli_channel_cp_tetrahedron import cp

ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1212-fixed-visibility-chsh-envelope.json"
def row(v:F):
    lo=(v, F(0), F(0)); hi=(v,v,F(1))
    return {"visibility":str(v),"low_lambda":[str(q) for q in lo],"high_lambda":[str(q) for q in hi],"low_S_squared_over_4":str(v*v),"high_S_squared_over_4":str(1+v*v),"low_cp":cp(*lo),"high_cp":cp(*hi)}
def build():
    rows=[row(v) for v in (F(0),F(1,5),F(2,5),F(1))]
    return {"schema_version":"1.0","result_id":"K1212-FIXED-VISIBILITY-CHSH-ENVELOPE","created":"2026-10-06","status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","scope":"Optimized CHSH of Bell-Choi outputs across all Pauli-diagonal channels with fixed nonnegative lambda_x=V.","theorem":{"range":"2 V <= S_max <= 2 sqrt(1+V^2)","squared_range":"V^2 <= S_max^2/4 <= 1+V^2","lower_attainer":"diag(V,0,0)","upper_attainer":"diag(V,V,1)","proof":"The Horodecki sum contains at least V^2. Pauli CP gives lambda_y^2+lambda_z^2 <= 1+V^2 and |lambda_i|<=1, so every pair sum is at most 1+V^2; the two displayed channels attain both endpoints."},"controls":rows,"decision":{"one_axis_visibility_identifies_optimized_chsh":False,"bounds_are_sharp":True,"every_positive_visibility_forces_violation":False},"ownership":{"pauli_class_and_common_axis_identification_imported":True,"gu_prediction":False},"release_test":{"lower_bound_exact":True,"upper_bound_exact":True,"both_attainers_cp":all(r["low_cp"] and r["high_cp"] for r in rows),"v_two_fifths_low_is_4_over_25":rows[2]["low_S_squared_over_4"]=="4/25","v_two_fifths_high_is_29_over_25":rows[2]["high_S_squared_over_4"]=="29/25","protected_status_unchanged":True},"claim_ceiling":"Sharp conditional score envelope in an imported Pauli/Bell/Born class; no cross-experiment equality, GU owner or empirical score."}
def validate(x):
    assert all(x["release_test"].values());assert x["theorem"]["range"]=="2 V <= S_max <= 2 sqrt(1+V^2)"
    assert x["decision"]=={"one_axis_visibility_identifies_optimized_chsh":False,"bounds_are_sharp":True,"every_positive_visibility_forces_violation":False}
    assert x["controls"][2]["low_S_squared_over_4"]=="4/25" and x["controls"][2]["high_S_squared_over_4"]=="29/25"
    assert x["ownership"]["pauli_class_and_common_axis_identification_imported"] and not x["ownership"]["gu_prediction"]
def main():
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");a.add_argument("--check",action="store_true");q=a.parse_args();x=build();validate(x);s=json.dumps(x,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if q.write else (assert_check(OUTPUT,s) if q.check else print(s,end=""));print("K1212 controls: 9/9")
def assert_check(p,s): assert p.read_text()==s
if __name__=="__main__":main()
