#!/usr/bin/env python3
"""Exact D7 root-sequence controls for K1328."""
import hashlib,json,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1328-d7-inversion-set-factorization.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
R=D["d7_root_system"]; A=[tuple(x) for x in R["simple_roots"]]; E={tuple(x) for x in R["adjacent_edges"]}
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
def refl(v,a): return tuple(x-dot(v,a)*y for x,y in zip(v,a))
def seq(word):
 out=[]
 for j,i in enumerate(word):
  v=A[i-1]
  for h in reversed(word[:j]): v=refl(v,A[h-1])
  out.append(v)
 return out
positive=[]
for i,j in itertools.combinations(range(7),2):
 for s in (-1,1):
  v=[0]*7; v[i]=1; v[j]=s; positive.append(tuple(v))
check("rank seven",R["rank"]==len(A)==7)
check("simple norms",all(dot(a,a)==2 for a in A))
derived_edges={(i+1,j+1) for i,j in itertools.combinations(range(7),2) if dot(A[i],A[j])==-1}
check("D7 edges",derived_edges==E and len(E)==6)
check("nonadjacent count",R["nonadjacent_pair_count"]==15)
check("positive roots",len(set(positive))==R["positive_root_count"]==42)
for i,j in itertools.combinations(range(1,8),2):
 left=seq([i,j,i]) if (i,j) in E else seq([i,j])
 right=seq([j,i,j]) if (i,j) in E else seq([j,i])
 check(f"pair {i}{j} root multiset",sorted(left)==sorted(right))
F=D["factorization"]; Q=D["decision"]
check("inversion-set rule",F["reduced_word_independence"].endswith("once"))
check("scalar factorization",Q["d7_scalar_factorization_constructed"] and Q["reduced_word_scalar_independence_constructed"])
check("operator ceiling",not Q["operator_valued_reduced_word_independence_constructed"] and not Q["physical_chamber_descent_constructed"])
assert n==31; print("RESULT: PASS 31/31")
