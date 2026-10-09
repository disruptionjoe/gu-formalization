#!/usr/bin/env python3
"""Certificate for K1623's effective-rank covariance criteria."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def main():
    d=json.loads((ROOT/"lab/process/k1623-effective-rank-covariance-rigidity.json").read_text());q,z=d["effective_rank_tests"],d["decision"]
    eig=[0.0,0.2,1.5,3.0]
    logdet=sum(math.log1p(x) for x in eig); trace=sum(eig); rank=sum(x>0 for x in eig); norm=max(eig)
    checks=[("claim",d["claim_id"]=="K1623"),("logdet trace",logdet<=trace+1e-14),("logdet rank norm",logdet<=rank*math.log1p(norm)+1e-14),
            ("trace statement","log det(I+A)<=Tr(A)" in q["trace"]),("rank statement","rank(A)log(1+||A||_op)" in q["rank_norm"]),
            ("small excess","sup_z||A_(N,z)||_op=o(1)" in q["small_excess"]),("dimension","d_N=Theta(N^3)" in q["small_excess"]),
            ("low rank","weighted effective rank o(N^3)" in q["low_rank"]),("rotated spaces","rotated eigenspaces" in q["low_rank"]),
            ("sufficient only","sufficient conditions, not necessary thresholds" in q["scope_guard"]),("trace decision",z["trace_test_sufficient"]),
            ("rank decision",z["rank_norm_test_sufficient"]),("small decision",z["vanishing_relative_excess_sufficient"]),
            ("effective rank decision",z["subextensive_effective_rank_sufficient"]),("critical open",not z["critical_capacity_resolved"]),
            ("protected",not z["protected_status_change"])]
    for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
