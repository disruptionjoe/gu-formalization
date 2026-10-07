#!/usr/bin/env python3
"""Independent hostile mutations for K1315."""
import collections,copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1315-principal-series-admission-boundary.json").read_text())
def valid(x):
 c=x["certificate"]; q=x["decision"]; z=collections.Counter(r["state"] for r in c["rows"]); return c["row_count"]==len(c["rows"])==17 and (c["satisfied_count"],c["excluded_count"],c["conditional_count"],c["missing_count"])==(6,3,2,6) and (z["satisfied"],z["excluded"],z["conditional"],z["missing"])==(6,3,2,6) and q["positive_mathematical_Hilbert_control_constructed"] and not q["positive_physical_pairing_constructed"] and not q["prequantization_selects_or_discretizes_mu"] and not q["canonical_or_source_selected_chamber_constructed"] and not q["k1145_k1150_candidate_counts_move"] and not q["protected_status_change"]
mut=[(("certificate","row_count"),16),(("certificate","satisfied_count"),7),(("certificate","missing_count"),5),(("decision","positive_mathematical_Hilbert_control_constructed"),False),(("decision","positive_physical_pairing_constructed"),True),(("decision","prequantization_selects_or_discretizes_mu"),True),(("decision","canonical_or_source_selected_chamber_constructed"),True),(("decision","k1145_k1150_candidate_counts_move"),True),(("decision","protected_status_change"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
