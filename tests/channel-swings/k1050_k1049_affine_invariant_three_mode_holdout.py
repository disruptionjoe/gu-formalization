#!/usr/bin/env python3
"""K1050: an exact nonzero three-mode affine-invariant mass-horn holdout."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1050-k1049-affine-invariant-three-mode-holdout.json"
def build():
    d4=(math.sqrt(19)-2*math.sqrt(3))/(2*math.sqrt(3)-math.sqrt(7)); gap=d4-1
    rows=[("fixed_common_spatial_ruler","required_open"),("three_mode_preparation","required_open"),("common_affine_readout_stability","required_open"),("difference_ratio_resolution","required_open"),("measured_record_and_complete_systematics","required_open"),("source_selected_mass_coefficient","required_open")]
    return {"schema_version":"1.0","result_id":"K1050-K1049-AFFINE-INVARIANT-THREE-MODE-HOLDOUT","status":"working_draft_verified","created":"2026-10-04","modes":[3,8,15],"statistic":"D=(omega_3-omega_2)/(omega_2-omega_1)","affine_invariance":"for y_i=g*omega_i+b with common g>0, both differences gain the same factor g and D is unchanged","horns":{"mass1":{"frequencies":["2","3","4"],"D":"1"},"mass4":{"frequencies":["sqrt(7)","2*sqrt(3)","sqrt(19)"],"D":"(sqrt(19)-2*sqrt(3))/(2*sqrt(3)-sqrt(7))","D_decimal":f"{d4:.15f}"}},"separation":{"exact_gap":"(sqrt(19)+sqrt(7)-4*sqrt(3))/(2*sqrt(3)-sqrt(7))","gap_decimal":f"{gap:.15f}","proof":"the denominator is positive and sqrt(19)+sqrt(7)>4*sqrt(3) because sqrt(133)>11"},"sharp_additive_D_radius":"half the exact gap","requirements":[{"id":i,"candidate_grade":g,"gu_source_owned":False,"scorable":False} for i,g in rows],"route_comparison":"two-mode Q needs offset control but only two prepared modes; three-mode D cancels common gain and offset but needs a third prepared mode and calibrated difference resolution","score_gate":"closed -- no owned ruler, three-mode preparation, stable affine transfer, measured record or complete systematic audit","source_scope":{"SC-ACT-01":"ASSERTS","SC-ACT-02":"ASSERTS","SC-ACT-06":"ASSERTS","SC-META-53":"UNCERTAIN"},"ledger_effect":"none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS","target_claim":"NONE-NOT-A-KILL"}
def validate(d):
    assert d["modes"]==[3,8,15] and d["statistic"].startswith("D=(omega_3")
    assert "common g>0" in d["affine_invariance"] and "unchanged" in d["affine_invariance"]
    assert d["horns"]["mass1"]=={"frequencies":["2","3","4"],"D":"1"}
    assert d["horns"]["mass4"]["frequencies"]==["sqrt(7)","2*sqrt(3)","sqrt(19)"]
    assert d["horns"]["mass4"]["D"].startswith("(sqrt(19)-2*sqrt(3))") and float(d["horns"]["mass4"]["D_decimal"])>1
    assert d["separation"]["exact_gap"].startswith("(sqrt(19)+sqrt(7)") and float(d["separation"]["gap_decimal"])>0
    assert "sqrt(133)>11" in d["separation"]["proof"] and d["sharp_additive_D_radius"]=="half the exact gap"
    assert len(d["requirements"])==6 and all(r["candidate_grade"]=="required_open" and not r["gu_source_owned"] and not r["scorable"] for r in d["requirements"])
    assert "two-mode Q needs offset control" in d["route_comparison"] and "third prepared mode" in d["route_comparison"]
    assert d["score_gate"].startswith("closed") and "complete systematic audit" in d["score_gate"]
    assert d["source_scope"]=={"SC-ACT-01":"ASSERTS","SC-ACT-02":"ASSERTS","SC-ACT-06":"ASSERTS","SC-META-53":"UNCERTAIN"}
    assert d["ledger_effect"].startswith("none") and d["ledger_effect"].endswith("NEEDS")
    assert d["target_claim"]=="NONE-NOT-A-KILL"
if __name__=="__main__":
    data=build(); validate(data); OUTPUT.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n"); print("K1050 controls: 13/13")
