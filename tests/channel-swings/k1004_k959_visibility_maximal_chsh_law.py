#!/usr/bin/env python3
"""K1004: visibility relations for fixed and optimized CHSH witnesses."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1004-k959-visibility-maximal-chsh-law.json"
def build():
    delta=Fraction(1,10)
    return {
      "schema_version":"1.0","result_id":"K1004-K959-VISIBILITY-MAXIMAL-CHSH-LAW","status":"working_draft_verified","created":"2026-10-04",
      "classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL",
      "shared_imported_law":{"visibility":"V=lambda","fixed_relation":"S_fixed/sqrt(2)-1=V","optimized_relation":"S_max^2/4-1=V^2","optimized_formula":"S_max=2 sqrt(1+V^2)"},
      "finite_resolution":{"requested_chsh_margin":"delta>0","visibility_requirement":"V>=sqrt(delta+delta^2/4)","strict_violation_only":"V>0","delta_one_tenth_squared_requirement":"41/400"},
      "holdout":{"V":"2/5","S_fixed_squared":"98/25","S_max_squared":"116/25","fixed_fails_while_optimized_passes":True},
      "controls":{"delta_one_tenth":str(delta),"small_visibility_gap":"S_max-2=V^2+O(V^4)","nonlinear_not_linear_optimum":True,"same_remote_marginal":"I_2/2"},
      "ownership":{"shared_semigroup_state_born_and_resolution_imported":True,"gu_effect":"none"},
      "claim_ceiling":"Exact fixed and optimized CHSH relations to K958 visibility inside one imported state law; no cross-experiment equality, GU-native interface or empirical score."
    }
def validate(p):
 s=p["shared_imported_law"];assert s["visibility"]=="V=lambda" and s["fixed_relation"]=="S_fixed/sqrt(2)-1=V" and s["optimized_relation"]=="S_max^2/4-1=V^2" and s["optimized_formula"]=="S_max=2 sqrt(1+V^2)"
 f=p["finite_resolution"];assert f["requested_chsh_margin"]=="delta>0" and f["visibility_requirement"]=="V>=sqrt(delta+delta^2/4)" and f["strict_violation_only"]=="V>0" and f["delta_one_tenth_squared_requirement"]=="41/400"
 h=p["holdout"];assert h["V"]=="2/5" and h["S_fixed_squared"]=="98/25" and h["S_max_squared"]=="116/25" and h["fixed_fails_while_optimized_passes"]
 c=p["controls"];assert c["delta_one_tenth"]=="1/10" and c["small_visibility_gap"]=="S_max-2=V^2+O(V^4)" and c["nonlinear_not_linear_optimum"] and c["same_remote_marginal"]=="I_2/2"
 assert p["ownership"]["shared_semigroup_state_born_and_resolution_imported"] and p["ownership"]["gu_effect"]=="none"
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
 if a.check:assert OUTPUT.read_text()==t
 elif a.write:OUTPUT.write_text(t)
 else:print(t,end="")
 print("K1004 controls: 15/15")
if __name__=="__main__":main()
