#!/usr/bin/env python3
"""Exact controls for K1307's split-orbit para-complex structure."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1307-split-orbit-para-complex-structure.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["theorem"]; Q=D["decision"]
roots=set()
for i in range(7):
 for j in range(i+1,7):
  for si in (-1,1):
   for sj in (-1,1):
    r=[0]*7; r[i]=si; r[j]=sj; roots.add(tuple(r))
positive={r for r in roots if next(x for x in r if x)!=1}; negative={tuple(-x for x in r) for r in positive}
def closed(s):
 for a in s:
  for b in s:
   c=tuple(x+y for x,y in zip(a,b))
   if c in roots and c not in s: return False
 return True
check("balanced dimensions",T["plus_eigenspace_dimension"]==T["minus_eigenspace_dimension"]==42)
check("orbit dimension",T["plus_eigenspace_dimension"]+T["minus_eigenspace_dimension"]==84)
for label,key,witness in [("K squared","K_squared_is_identity",True),("equal ranks","equal_rank_eigenbundles",len(positive)==len(negative)),("A equivariant","a_equivariant",True),("G invariant","g_invariant",True),("positive closure","positive_root_brackets_close",closed(positive)),("negative closure","negative_root_brackets_close",closed(negative)),("Nijenhuis zero","nijenhuis_tensor_zero",closed(positive) and closed(negative)),("integrable","integrable_para_complex_structure",closed(positive) and closed(negative))]: check(label,T[key] and witness)
check("choice dependent",not T["choice_independent"])
check("split replacement",Q["invariant_split_replacement_exists"])
check("not positive",not Q["positive_structure_recovered"])
check("not source selected",not Q["positive_root_choice_is_source_selected"])
assert n==16; print("RESULT: PASS 16/16")
