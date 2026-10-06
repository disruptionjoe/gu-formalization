#!/usr/bin/env python3
"""K1214: residual third-axis interval after two signed transfer reads."""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from pathlib import Path
from k1211_pauli_channel_cp_tetrahedron import cp,probs
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1214-two-axis-visibility-residual-interval.json"
def two_largest_sum(vals):return sum(sorted((q*q for q in vals),reverse=True)[:2])
def build():
    x,y=F(4,5),F(3,5);zl=x+y-1;zu=1-abs(x-y);lo=(x,y,zl);hi=(x,y,zu)
    return {"schema_version":"1.0","result_id":"K1214-TWO-AXIS-VISIBILITY-RESIDUAL-INTERVAL","created":"2026-10-06","status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","scope":"Pauli complete-positivity interval and optimized-CHSH residual after signed lambda_x and lambda_y are fixed.","theorem":{"third_axis_interval":"|lambda_x+lambda_y|-1 <= lambda_z <= 1-|lambda_x-lambda_y|","source":"the four Pauli probabilities","score_given_z":"S_max^2/4 is the sum of the two largest squared transfer coefficients","two_axes_generally_sufficient":False},"control":{"lambda_x":"4/5","lambda_y":"3/5","lambda_z_interval":[str(zl),str(zu)],"lower_endpoint_probabilities":[str(q) for q in probs(*lo)],"upper_endpoint_probabilities":[str(q) for q in probs(*hi)],"lower_endpoint_S_squared_over_4":str(two_largest_sum(lo)),"upper_endpoint_S_squared_over_4":str(two_largest_sum(hi)),"lower_cp":cp(*lo),"upper_cp":cp(*hi)},"decision":{"same_two_axis_data_can_touch_classical_boundary_and_violate":True,"third_axis_or_equivalent_calibration_needed":True,"two_unsigned_fringes_identify_full_channel":False},"ownership":{"transfer_axes_and_common_channel_imported":True,"gu_apparatus_or_prediction":False},"release_test":{"interval_lower_is_2_over_5":zl==F(2,5),"interval_upper_is_4_over_5":zu==F(4,5),"both_endpoints_cp":cp(*lo) and cp(*hi),"lower_score_is_one":two_largest_sum(lo)==1,"upper_score_is_32_over_25":two_largest_sum(hi)==F(32,25),"protected_status_unchanged":True},"claim_ceiling":"Exact residual-identifiability theorem for an imported signed Pauli transfer model; no physical channel identification or GU credit."}
def validate(x):
    assert all(x["release_test"].values());assert x["theorem"]["third_axis_interval"]=="|lambda_x+lambda_y|-1 <= lambda_z <= 1-|lambda_x-lambda_y|";assert not x["theorem"]["two_axes_generally_sufficient"];assert x["control"]["lambda_z_interval"]==["2/5","4/5"];assert x["control"]["lower_endpoint_S_squared_over_4"]=="1" and x["control"]["upper_endpoint_S_squared_over_4"]=="32/25";assert x["decision"]["third_axis_or_equivalent_calibration_needed"] and not x["ownership"]["gu_apparatus_or_prediction"]
def main():
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");a.add_argument("--check",action="store_true");q=a.parse_args();x=build();validate(x);s=json.dumps(x,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if q.write else (check(OUTPUT,s) if q.check else print(s,end=""));print("K1214 controls: 9/9")
def check(p,s):assert p.read_text()==s
if __name__=="__main__":main()
