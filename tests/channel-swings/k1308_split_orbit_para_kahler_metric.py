#!/usr/bin/env python3
"""Exact controls for K1308's neutral para-Kahler metric."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1308-split-orbit-para-kahler-metric.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["theorem"]; Q=D["decision"]
mu=tuple(range(1,8)); roots=[]
for i in range(7):
 for j in range(i+1,7):
  for sj in (-1,1):
   r=[0]*7; r[i]=1; r[j]=sj; roots.append(tuple(r))
coeff=[sum(a*b for a,b in zip(mu,r)) for r in roots]
eigenvalues=[v for c in coeff for v in (-abs(c),abs(c))]
for label,key in [("symmetric","metric_symmetric"),("nondegenerate","metric_nondegenerate"),("invariant","metric_g_invariant"),("para Kahler","para_kahler")]: check(label,T[key])
check("root planes",T["root_plane_count"]==len(coeff)==42)
check("positive inertia",T["positive_inertia"]==sum(v>0 for v in eigenvalues)==42)
check("negative inertia",T["negative_inertia"]==sum(v<0 for v in eigenvalues)==42)
check("zero inertia",T["zero_inertia"]==sum(v==0 for v in eigenvalues)==0)
check("dimension",T["positive_inertia"]+T["negative_inertia"]==84)
check("not positive definite",not T["metric_positive_definite"])
check("KKS not positive",not T["kks_form_is_positive_pairing"])
check("no Hilbert pairing",not Q["physical_hilbert_pairing_constructed"])
assert n==14; print("RESULT: PASS 14/14")
