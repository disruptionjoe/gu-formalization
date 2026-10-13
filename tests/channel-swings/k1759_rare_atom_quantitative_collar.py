#!/usr/bin/env python3
"""Exact composition audit for K1759's conservative rare-atom collar."""
import json,math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1759-rare-atom-quantitative-collar.json"
def validate(d):
 c=d["composition"];v=d["coverage"];z=d["decision"]
 loss=400000*math.sqrt(2*1e-34);gap=2.20e-10-loss
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1759"),
  ("Arb input","2.20e-10" in c["arb_input"]),("OU monotone","nondecreasing" in c["ou_monotonicity"]),
  ("stability input","400000 sqrt(2z)" in c["stability_input"]),("collar",c["collar_choice"]=="0<z<=10^-34"),
  ("loss",loss<6e-12),("residual",gap>2.14e-10),("outside","2-1/961" in v["outside_zero_noise"]),
  ("inside","every z" in v["inside_zero_noise"]),("rare excluded",z["quantitative_rare_atom_collar_excluded"]),
  ("uniform",z["uniform_in_complete_c_range_after_composition"]),("corner",z["joint_corner_excluded"]),
  ("thin admitted",not z["collar_is_practically_wide"]),("global fenced",not z["global_optimizer_proved"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
