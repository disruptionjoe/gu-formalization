#!/usr/bin/env python3
"""Cocycle and chamber-descent reporting controls for K1334."""
import hashlib,itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1334-d7-normalized-operator-cocycle-descent.json").read_text()); ncheck=0
def check(label,value):
 global ncheck; assert value,label; ncheck+=1; print(f"PASS {ncheck:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F=D["normalized_family"]; G=D["d7_descent"]; Q=D["decision"]
roots=[(1,-1,0,0,0,0,0),(0,1,-1,0,0,0,0),(0,0,1,-1,0,0,0),(0,0,0,1,-1,0,0),(0,0,0,0,1,-1,0),(0,0,0,0,0,1,-1),(0,0,0,0,0,1,1)]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
edges={(i+1,j+1) for i,j in itertools.combinations(range(7),2) if dot(roots[i],roots[j])==-1}
check("D7 edge count",len(edges)==6)
check("D7 nonedges",sum(1 for i,j in itertools.combinations(range(7),2) if (i+1,j+1) not in edges)==15)
check("simple operator type",F["simple_operator"]=="R_i(lambda):I(lambda)->I(s_i lambda)")
check("common core",F["common_core"]=="C[K/M]_K-finite")
check("G intertwining","pi_lambda(g)" in F["intertwining_law"])
check("cocycle","w1 w2" in F["cocycle"] and "w2 lambda" in F["cocycle"])
check("inverse",F["inverse"].endswith("=I"))
check("commutation","R_i(s_j lambda)" in F["nonadjacent_relation"])
check("braid","length-three" in F["adjacent_relation"])
check("reduced words",F["reduced_word_independence"])
check("unitary products","unitary" in F["regular_imaginary_extension"])
check("D7 size",G["rank"]==7 and G["positive_roots"]==42 and G["weyl_chambers"]==322560)
check("path independent",G["path_independent_G_intertwiners"])
check("actions coincide",G["transported_chamber_actions_coincide"])
check("projection commutes",G["average_projection_commutes_with_block_G_action"])
check("G subrepresentation",G["coherent_diagonal_is_G_subrepresentation"])
check("full-copy ceiling","not a one-dimensional" in G["descended_representation"])
check("no chamber selected",not G["single_chamber_selected"])
check("operator decision",Q["full_normalized_simple_operator_family_constructed"] and Q["operator_valued_coxeter_relations_constructed"])
check("descent decision",Q["G_equivariant_chamber_descent_constructed"])
check("physical ceiling",not Q["canonical_physical_chamber_constructed"] and not Q["physical_GU_state_space_constructed"] and not Q["protected_status_change"])
assert ncheck==25; print("RESULT: PASS 25/25")
