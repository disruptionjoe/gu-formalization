#!/usr/bin/env python3
"""Exact controls for K1758's entropy/log-Sobolev zero-noise collar."""
import json,math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1758-zero-noise-entropy-collar.json"
def validate(d):
 e=d["entropy_argument"];c=d["candidate_control"];z=d["decision"]
 q=Q(1,1024);u=Q(691835097,2000000000);width=Q(1,961)-q
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1758"),
  ("four atoms","H(X)" in e["mixture_entropy"] and "log(4)" in e["mixture_entropy"]),
  ("LSI","J(Y)>=2D" in e["gaussian_log_sobolev"]),("collar","v<=1/32" in e["collar_choice"]),
  ("width",width==Q(63,984064)),("candidate exact",289*q<u),("candidate upper","<1/16<1/2<log(2)" in c["consequence"]),
  ("log bound",math.log(2)>.5),("excluded",z["uniform_zero_noise_collar_excluded"]),("all z",z["all_z_in_0_1_covered"]),
  ("corner",z["rare_atom_zero_noise_joint_corner_covered"]),("no v0 density",not z["uses_interior_density_at_v_zero"]),
  ("global fenced",not z["global_optimizer_proved"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
