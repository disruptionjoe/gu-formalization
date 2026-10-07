#!/usr/bin/env python3
"""Independent hostile mutations for K1310."""
import copy,json,collections
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1310-para-polarization-admission-boundary.json").read_text())
def valid(x):
 c=x["certificate"]; q=x["decision"]; z=collections.Counter(r["state"] for r in c["rows"]); return c["row_count"]==len(c["rows"])==14 and (c["satisfied_count"],c["excluded_count"],c["conditional_count"],c["missing_count"])==(5,2,1,6) and (z["satisfied"],z["excluded"],z["conditional"],z["missing"])==(5,2,1,6) and q["k1304_noninvariant_polarization_horn_refined"] and q["invariant_real_polarization_exists"] and not q["invariant_complex_or_positive_kahler_polarization_exists"] and not q["neutral_para_geometry_resolves_physical_positivity"] and not q["charge_or_chamber_selected_by_source"] and not q["k1145_k1150_candidate_counts_move"] and not q["protected_status_change"]
mut=[(("certificate","row_count"),13),(("certificate","satisfied_count"),6),(("certificate","excluded_count"),1),(("decision","invariant_real_polarization_exists"),False),(("decision","invariant_complex_or_positive_kahler_polarization_exists"),True),(("decision","neutral_para_geometry_resolves_physical_positivity"),True),(("decision","charge_or_chamber_selected_by_source"),True),(("decision","k1145_k1150_candidate_counts_move"),True),(("decision","protected_status_change"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
