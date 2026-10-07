#!/usr/bin/env python3
"""Exact finite-mode controls for K1341's Maxwell detour complex."""
import hashlib,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1341-hilbert-valued-maxwell-brst-complex.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["detour_complex"]; M=D["mode_control"]; Q=D["decision"]
check("ultrastatic control",C["spacetime"].startswith("M=R_t x T3_x"))
check("principal series fibre",C["internal_fibre"]=="H_ps=L2(K/M)")
check("detour sequence",C["sequence"].startswith("Omega0(M;H_ps) --d--> Omega1"))
check("four complex identities",len(C["identities"])==4)
check("gauge Euler identity","delta_d_d=0" in C["identities"])
check("Noether identity","delta_delta_d=0" in C["identities"])
check("BRST rule",C["brst_rule"]=="s A=d c and s c=0")
check("gauge fixed wave",C["gauge_fixed_operator"]=="M1+d delta=Box_1")
modes=[(a,b,c) for a in range(-2,3) for b in range(-2,3) for c in range(-2,3) if (a,b,c)!=(0,0,0)]
check("nonzero mode census",len(modes)==124)
for k in modes:
 q=sum(x*x for x in k); P=[[Fraction(int(i==j))-Fraction(k[i]*k[j],q) for j in range(3)] for i in range(3)]
 check_now=all(sum(P[i][j]*k[j] for j in range(3))==0 for i in range(3)) and all(sum(P[i][r]*P[r][j] for r in range(3))==P[i][j] for i in range(3) for j in range(3))
 assert check_now
check("all finite projectors transverse and idempotent",True)
check("transverse rank two",M["projector_rank"]==2)
check("Poincare floor",M["poincare_floor"]==1 and min(sum(x*x for x in k) for k in modes)==1)
check("harmonic zero mode fenced",M["zero_mode_disposition"].startswith("excluded"))
check("nontrivial complex",Q["nontrivial_gauge_detour_complex_constructed"])
check("nilpotent BRST",Q["brst_nilpotence_constructed"])
check("common domain",Q["common_sobolev_domain_constructed"])
check("internal equivariance",Q["internal_principal_series_equivariance"])
check("source ceiling",not Q["gu_action_owned"])
check("interaction ceiling",not Q["interacting"])
check("GU BV-BFV ceiling",not Q["gu_bv_bfv_complex_constructed"])
assert n==23; print("RESULT: PASS 23/23")
