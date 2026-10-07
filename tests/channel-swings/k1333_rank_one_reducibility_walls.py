#!/usr/bin/env python3
"""Exact mode-wall controls for K1333."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1333-rank-one-reducibility-walls.json").read_text()); ncheck=0
def check(label,value):
 global ncheck; assert value,label; ncheck+=1; print(f"PASS {ncheck:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
N=D["normalized_divisor"]; R=D["reducibility"]; B=D["normalization_boundary"]; Q=D["decision"]
def factors(mode): return list(range(1,2*abs(mode),2))
for mode in range(1,8):
 check(f"mode {mode} wall count",len(factors(mode))==mode and factors(mode)[-1]==2*mode-1)
for r in range(5):
 wall=2*r+1
 killed=[mode for mode in range(8) if wall in factors(mode)]
 check(f"wall {wall} kernel",killed==list(range(r+1,8)))
check("positive wall prose","|n|>=r+1" in N["positive_wall_kernel"])
check("negative wall prose","simple normalized pole" in N["negative_wall_pole"])
check("zero regular",N["zero_parameter"]=="z=0 is regular and a_n(0)=1 for every n")
check("odd reducibility",R["rank_one_spherical_principal_series"].startswith("reducible exactly at nonzero odd"))
check("imaginary axis clear",R["imaginary_axis"]=="no zero, pole or kernel for z in iR")
check("D7 trivial stabilizer","Weyl stabilizer is trivial" in R["regular_imaginary_d7"])
check("raw-normalized distinction","K1327" in B["raw_spherical_divisor"] and "operator-mode" in B["normalized_operator_divisor"])
check("wall decision",Q["all_rank_one_normalized_mode_walls_classified"] and Q["rank_one_kernel_and_pole_modes_classified"])
check("D7 decision",Q["regular_imaginary_d7_reducibility_excluded"])
check("scope ceiling",not Q["singular_or_nonspherical_M_type_classified"] and not Q["physical_reducibility_statement"] and not Q["protected_status_change"])
assert ncheck==24; print("RESULT: PASS 24/24")
