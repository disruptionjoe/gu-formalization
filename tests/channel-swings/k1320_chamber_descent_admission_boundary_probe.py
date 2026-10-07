#!/usr/bin/env python3
"""Independent hostile mutations for K1320."""
import collections,copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1320-chamber-descent-admission-boundary.json").read_text())
def valid(x):
 c=x["certificate"]; q=x["decision"]; z=collections.Counter(r["state"] for r in c["rows"]); return c["row_count"]==len(c["rows"])==18 and (c["satisfied_count"],c["excluded_count"],c["conditional_count"],c["missing_count"])==(7,3,2,6) and (z["satisfied"],z["excluded"],z["conditional"],z["missing"])==(7,3,2,6) and q["raw_chamber_multiplicity_has_canonical_Hilbert_projection"] and not q["G_equivariant_chamber_descent_constructed"] and not q["analytic_normalized_intertwiner_family_constructed"] and not q["projective_relator_phase_is_harmless"] and not q["canonical_or_source_selected_chamber_constructed"] and not q["positive_physical_pairing_constructed"] and not q["protected_status_change"]
mut=[(("certificate","row_count"),17),(("certificate","satisfied_count"),8),(("certificate","missing_count"),5),(("decision","raw_chamber_multiplicity_has_canonical_Hilbert_projection"),False),(("decision","G_equivariant_chamber_descent_constructed"),True),(("decision","analytic_normalized_intertwiner_family_constructed"),True),(("decision","projective_relator_phase_is_harmless"),True),(("decision","positive_physical_pairing_constructed"),True),(("decision","protected_status_change"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
