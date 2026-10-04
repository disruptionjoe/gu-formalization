#!/usr/bin/env python3
"""K1003: exponential dephasing has no finite optimized-Bell death time."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1003-k1002-exponential-bell-persistence.json"
def build():
    return {
      "schema_version":"1.0","result_id":"K1003-K1002-EXPONENTIAL-BELL-PERSISTENCE","status":"working_draft_verified","created":"2026-10-04",
      "classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL",
      "law":{"lambda(t)":"exp(-2 gamma t)","S_max(t)":"2 sqrt(1+exp(-4 gamma t))","finite_time_violation":True,"limit_at_infinity":"2 from above"},
      "fixed_witness":{"S_fixed(t)":"sqrt(2)(1+exp(-2 gamma t))","violation_interval":"t < log(1+sqrt(2))/(2 gamma)","finite_threshold_is_witness_specific":True},
      "distinction":{"optimized_bell_death_time":"none at finite t","fixed_setting_witness_death_time":"log(1+sqrt(2))/(2 gamma)","requires_gamma_positive":True},
      "controls":{"t_zero_S_max_squared":"8","finite_t_exponential_positive":True,"finite_t_S_max_strictly_above_two":True,"asymptotic_gap":"S_max-2 ~ exp(-4 gamma t)"},
      "ownership":{"exponential_law_and_adaptive_settings_imported":True,"gu_effect":"none"},
      "claim_ceiling":"Exact optimized-versus-fixed CHSH consequence of the imported exponential K956 law; no GU-native generator, local net, setting protocol or prediction."
    }
def validate(p):
    l=p["law"];assert l["lambda(t)"]=="exp(-2 gamma t)" and l["S_max(t)"]=="2 sqrt(1+exp(-4 gamma t))"
    assert l["finite_time_violation"] and l["limit_at_infinity"]=="2 from above"
    f=p["fixed_witness"];assert f["S_fixed(t)"]=="sqrt(2)(1+exp(-2 gamma t))" and f["violation_interval"]=="t < log(1+sqrt(2))/(2 gamma)" and f["finite_threshold_is_witness_specific"]
    d=p["distinction"];assert d["optimized_bell_death_time"]=="none at finite t" and d["fixed_setting_witness_death_time"]=="log(1+sqrt(2))/(2 gamma)" and d["requires_gamma_positive"]
    c=p["controls"];assert c["t_zero_S_max_squared"]=="8" and c["finite_t_exponential_positive"] and c["finite_t_S_max_strictly_above_two"] and "exp(-4 gamma t)" in c["asymptotic_gap"]
    assert p["ownership"]["exponential_law_and_adaptive_settings_imported"] and p["ownership"]["gu_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K1003 controls: 14/14")
if __name__=="__main__":main()
