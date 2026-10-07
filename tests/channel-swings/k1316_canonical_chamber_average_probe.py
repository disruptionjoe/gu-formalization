#!/usr/bin/env python3
"""Independent hostile mutations for K1316."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1316-canonical-chamber-average.json").read_text())
def valid(x):
 c=x["construction"]; q=x["decision"]; return c["chamber_count"]==322560 and c["self_adjoint"] and c["idempotent"] and c["positive_contraction"] and c["operator_norm"]==1 and c["chamber_factor_rank"]==1 and c["raw_multiplicity_reduced_to"]==1 and q["canonical_finite_Hilbert_average_exists_after_identifications"] and not q["average_is_automatically_G_equivariant"] and not q["source_or_physical_status_moves"]
mut=[(("construction","chamber_count"),161280),(("construction","self_adjoint"),False),(("construction","idempotent"),False),(("construction","positive_contraction"),False),(("construction","operator_norm"),2),(("construction","chamber_factor_rank"),2),(("construction","raw_multiplicity_reduced_to"),322560),(("decision","average_is_automatically_G_equivariant"),True),(("decision","source_or_physical_status_moves"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
