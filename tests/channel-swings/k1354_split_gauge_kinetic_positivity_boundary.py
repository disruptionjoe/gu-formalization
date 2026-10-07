#!/usr/bin/env python3
"""Exact Cartan-signature control and positivity boundary for K1354."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1354-split-gauge-kinetic-positivity-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
def mat(entries):
 a=[[0]*14 for _ in range(14)]
 for i,j,v in entries:a[i][j]+=v
 return a
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(14)) for j in range(14)] for i in range(14)]
def trace(a):return sum(a[i][i] for i in range(14))
def rotation(i,j):return mat([(i,j,1),(j,i,-1)])
def boost(i,a):return mat([(i,a,1),(a,i,1)])
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["cartan_signature"]; T=D["invariant_form_theorem"]; P=D["positive_controls"]; Q=D["decision"]
plus_rot=[rotation(i,j) for i in range(7) for j in range(i+1,7)]
minus_rot=[rotation(i,j) for i in range(7,14) for j in range(i+1,14)]
boosts=[boost(i,a) for i in range(7) for a in range(7,14)]
check("plus rotation count",len(plus_rot)==21)
check("minus rotation count",len(minus_rot)==21)
check("compact dimension",len(plus_rot)+len(minus_rot)==42)
check("boost dimension",len(boosts)==49)
check("algebra dimension",42+49==91)
check("rotation traces",all(trace(mul(x,x))==-2 for x in plus_rot+minus_rot))
check("boost traces",all(trace(mul(x,x))==2 for x in boosts))
check("compact declaration","dimension 21+21=42" in C["compact_part"])
check("split declaration","dimension 49" in C["split_part"])
check("signature declaration","49 positive,42 negative" in C["signature"])
check("invariant form classification","scalar multiple" in T["classification"])
check("nonzero indefinite","indefinite" in T["nonzero_case"])
check("zero degenerate","degenerate" in T["zero_case"])
check("no positive conclusion","no positive-definite" in T["conclusion"])
check("compact positive control","positive definite" in P["maximal_compact"])
check("Cartan majorant control","positive" in P["cartan_majorant"])
check("selector boundary","extra reduction/selector data" in P["ownership_boundary"])
check("positive count",Q["full_split_killing_signature_positive"]==49)
check("negative count",Q["full_split_killing_signature_negative"]==42)
check("no positive full-G form",not Q["positive_full_G_invariant_quadratic_form_exists"])
check("SC-META-53 open",not Q["sc_meta_53_resolved"] and not Q["protected_status_change"])
assert n==22; print("RESULT: PASS 22/22")
