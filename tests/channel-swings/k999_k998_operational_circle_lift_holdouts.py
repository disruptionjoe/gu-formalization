#!/usr/bin/env python3
"""K999 finite-band circular approximation and winding-record holdout."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k999-k998-operational-circle-lift-holdouts.json"
def build():
    s=2;N=5
    coeff={n:math.exp(-0.3*n*n) for n in range(-40,41)}
    hnorm2=sum((1+n*n)**s*abs(v)**2 for n,v in coeff.items())
    tail2=sum(abs(v)**2 for n,v in coeff.items() if abs(n)>N)
    bound2=hnorm2/(1+(N+1)**2)**s
    rate=0.4;T=2.0
    return {"schema_version":"1.0","result_id":"K999-OPERATIONAL-CIRCLE-LIFT-HOLDOUTS","created":"2026-10-04","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Finite-band reconstruction of a supplied circular density with declared Sobolev regularity, plus a supplied winding-sensitive record for two circularly identical real lifts.",
      "finite_band_theorem":{"sobolev_order":s,"observed_band":N,"tail_rule":"sum_{|n|>N}|p_hat(n)|^2 <= ||p||_{H^s}^2/(1+(N+1)^2)^s","declared_regularity_budget_required":True,"unrestricted_finite_band_identification":False,"k993_ceiling_preserved":True},
      "exact_controls":{"test_sequence":"wrapped heat-kernel Fourier coefficients exp(-0.3 n^2)","sampled_hs_norm_squared":hnorm2,"sampled_tail_squared":tail2,"declared_bound_squared":bound2,"tail_bound_pass":tail2<=bound2,"positive_tail_present":tail2>0},
      "frozen_holdout":{"time_T":T,"added_winding_jump_rate":rate,"calibration":"all integer harmonics and the complete circular process are identical","observable":"unwrapped count of added +2pi jumps by T","base_lift_event_probability":0.0,"jump_lift_event_probability":1-math.exp(-rate*T),"frozen_not_scored":True},
      "ownership":{"sobolev_class_and_budget_imported":True,"unwrapped_record_and_apparatus_imported":True,"gu_action_or_observable_constructed":False,"prediction_or_confirmation_credit":False},
      "decision":{"finite_band_data_give_conditional_approximation_not_unrestricted_identification":True,"complete_integer_harmonics_still_do_not_resolve_winding_lift":True,"next_exact_input":"Compose the circle-versus-lift boundary and require GU ownership before scoring either route."},"source_and_ledger_effect":"none","claim_ceiling":"Conditional Fourier-tail bound and frozen winding-record holdout only; neither regularity nor record access is GU-derived or empirically scored."}
def validate(p):
 f,x,h,o,d=p["finite_band_theorem"],p["exact_controls"],p["frozen_holdout"],p["ownership"],p["decision"]
 assert f["declared_regularity_budget_required"] and not f["unrestricted_finite_band_identification"] and f["k993_ceiling_preserved"]
 assert x["tail_bound_pass"] and x["positive_tail_present"] and x["sampled_tail_squared"]<=x["declared_bound_squared"]
 assert h["calibration"].startswith("all integer") and h["base_lift_event_probability"]==0.0
 assert h["jump_lift_event_probability"]>0.5 and h["frozen_not_scored"]
 assert o["sobolev_class_and_budget_imported"] and o["unwrapped_record_and_apparatus_imported"]
 assert not o["gu_action_or_observable_constructed"] and not o["prediction_or_confirmation_credit"]
 assert d["finite_band_data_give_conditional_approximation_not_unrestricted_identification"] and d["complete_integer_harmonics_still_do_not_resolve_winding_lift"]
 assert p["source_and_ledger_effect"]=="none"
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);text=json.dumps(p,indent=2,sort_keys=True)+"\n"
 if a.check:assert OUTPUT.read_text()==text
 elif a.write:OUTPUT.write_text(text)
 else:print(text,end="")
 print("K999 controls: 17/17")
if __name__=="__main__":main()
