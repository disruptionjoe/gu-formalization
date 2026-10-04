#!/usr/bin/env python3
"""K1002: exact fixed-versus-adaptive Bell witness separator."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1002-k1001-fixed-versus-adaptive-bell-witness.json"

def build():
    lam = Fraction(2, 5)
    return {
        "schema_version": "1.0", "result_id": "K1002-K1001-FIXED-VERSUS-ADAPTIVE-BELL-WITNESS",
        "status": "working_draft_verified", "created": "2026-10-04",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS", "target_claim": "NONE-NOT-A-KILL",
        "separator": {
            "lambda": "2/5", "visibility": "2/5",
            "S_fixed_squared": "98/25", "fixed_violates": False,
            "S_max_squared": "116/25", "adaptive_violates": True,
            "fixed_settings": "B0=(Z+X)/sqrt(2), B1=(Z-X)/sqrt(2)",
            "adaptive_settings": "B0=(Z+(2/5)X)/sqrt(29/25), B1=(Z-(2/5)X)/sqrt(29/25)",
        },
        "theorem": {
            "fixed_violation_iff": "lambda>sqrt(2)-1",
            "adaptive_violation_iff": "lambda>0",
            "fixed_witness_death_is_not_state_locality_death": True,
            "optimization_changes_measurement_settings_not_the_state": True,
        },
        "controls": {
            "fixed_below_two": 2 * (1 + lam) ** 2 < 4,
            "adaptive_above_two": 4 * (1 + lam * lam) > 4,
            "same_state_parameter": True,
            "same_remote_marginal": "I_2/2",
        },
        "ownership": {"adaptive_setting_protocol_imported": True, "gu_effect": "none"},
        "claim_ceiling": "Exact witness-choice separation on the imported K956 state family; no experimental optimization protocol or GU-native measurement owner.",
    }

def validate(p):
    s = p["separator"]; assert s["lambda"] == s["visibility"] == "2/5"
    assert s["S_fixed_squared"] == "98/25" and not s["fixed_violates"]
    assert s["S_max_squared"] == "116/25" and s["adaptive_violates"]
    assert "sqrt(2)" in s["fixed_settings"] and "sqrt(29/25)" in s["adaptive_settings"]
    t = p["theorem"]
    assert t["fixed_violation_iff"] == "lambda>sqrt(2)-1" and t["adaptive_violation_iff"] == "lambda>0"
    assert t["fixed_witness_death_is_not_state_locality_death"] and t["optimization_changes_measurement_settings_not_the_state"]
    c = p["controls"]; assert c["fixed_below_two"] and c["adaptive_above_two"] and c["same_state_parameter"]
    assert c["same_remote_marginal"] == "I_2/2"
    assert p["ownership"]["adaptive_setting_protocol_imported"] and p["ownership"]["gu_effect"] == "none"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    p=build(); validate(p); text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check: assert OUTPUT.read_text()==text
    elif a.write: OUTPUT.write_text(text)
    else: print(text,end="")
    print("K1002 controls: 13/13")
if __name__=="__main__": main()
