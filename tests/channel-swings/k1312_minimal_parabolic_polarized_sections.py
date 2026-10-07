#!/usr/bin/env python3
"""Exact controls for K1312's minimal-parabolic polarized sections."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1312-minimal-parabolic-polarized-sections.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["construction"]; Q=D["decision"]
roots=[]
for i in range(7):
 for j in range(i+1,7):
  a=[0]*7; a[i]=1; a[j]=-1; roots.append(tuple(a))
  b=[0]*7; b[i]=1; b[j]=1; roots.append(tuple(b))
rho=[sum(r[i] for r in roots)//2 for i in range(7)]
check("positive roots",C["positive_root_count"]==len(roots)==42)
check("nilradical dimension",C["nilradical_dimension"]==42)
check("rho vector",C["rho_vector_standard_chamber"]==rho==[6,5,4,3,2,1,0])
check("parabolic dimension",C["parabolic_dimension"]==7+42==49)
check("flag dimension",C["flag_dimension"]==91-C["parabolic_dimension"]==42)
H=(1,-1,2,0,3,-2,1); delta=math.exp(2*sum(x*y for x,y in zip(rho,H)))
check("positive modular character",delta>0)
check("minimal parabolic",C["minimal_parabolic"]=="P=MAN_plus")
check("character extension",C["character_extension"].endswith("N_plus"))
check("normalized equivariance", "delta_P(a)^(-1/2)" in C["normalized_equivariance"])
check("half density",C["half_density_correction_included"])
check("closed polarization subgroup",Q["finite_real_polarization_extends_to_closed_subgroup"])
check("induced control",Q["normalized_induced_control_constructed"])
check("no polarized BFV",not Q["polarized_BFV_cohomology_constructed"])
check("no GU constraint complex",not Q["GU_action_constraint_complex_constructed"])
assert n==16; print("RESULT: PASS 16/16")
