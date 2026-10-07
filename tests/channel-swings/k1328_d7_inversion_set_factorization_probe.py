#!/usr/bin/env python3
"""Independent hostile mutations for K1328."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1328-d7-inversion-set-factorization.json").read_text())
def valid(x):
 r=x["d7_root_system"]; f=x["factorization"]; q=x["decision"]; return r["rank"]==7 and r["positive_root_count"]==42 and len(r["simple_roots"])==7 and len(r["adjacent_edges"])==6 and r["nonadjacent_pair_count"]==15 and r["longest_length"]==42 and f["root_sequence"].startswith("beta_j=") and "inversion set" in f["reduced_word_independence"] and q["d7_scalar_factorization_constructed"] and q["reduced_word_scalar_independence_constructed"] and not q["operator_valued_reduced_word_independence_constructed"]
mut=[(("d7_root_system","rank"),6),(("d7_root_system","positive_root_count"),41),(("d7_root_system","simple_roots"),[[1,-1]]),(("d7_root_system","adjacent_edges"),[[1,2]]),(("d7_root_system","nonadjacent_pair_count"),14),(("d7_root_system","longest_length"),41),(("factorization","root_sequence"),"constant"),(("factorization","reduced_word_independence"),"assumed"),(("decision","operator_valued_reduced_word_independence_constructed"),True)]
for i,(path,value) in enumerate(mut,1):
 x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x),path; print(f"REJECT {i:02d}: {path[1]}")
assert valid(D); print("RESULT: PASS 9/9 hostile mutations rejected")
