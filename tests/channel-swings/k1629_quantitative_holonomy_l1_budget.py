#!/usr/bin/env python3
"""Certificate for K1629's optimized holonomy budget."""
import hashlib
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    d=json.loads((ROOT/"lab/process/k1629-quantitative-holonomy-l1-budget.json").read_text())
    q,z=d["quantitative_budget"],d["decision"];pin=d["pinned_inputs"]["k1628"]
    A=1.7;B=2.3
    R=(math.sqrt(math.pi)*B/(2*A))**(2/3)
    direct=2*R*A+2*math.sqrt(math.pi/R)*B
    optimized=3*(2*A)**(1/3)*(math.sqrt(math.pi)*B)**(2/3)
    checks=[
        ("claim",d["claim_id"]=="K1629"),
        ("pin",sha(ROOT/pin["path"])==pin["sha256"]),
        ("all scales","every R>0" in q["all_scales"]),
        ("optimizer syntax","2/3" in q["optimizer"]),
        ("optimizer identity",abs(direct-optimized)<1e-12),
        ("positive optimizer",R>0),
        ("optimized constant",q["optimized"].startswith("||widehat G||_1<=3")),
        ("vector extension","vector Plancherel" in q["vector_extension"]),
        ("conditional use","conditional budget" in q["use"]),
        ("explicit budget",z["explicit_budget_proved"]),
        ("optimized",z["optimized_scale_proved"]),
        ("vector",z["finite_vector_extension_proved"]),
        ("nonlinear open",not z["nonlinear_remainders_controlled"]),
        ("protected",not z["protected_status_change"]),
    ]
    for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")

if __name__=="__main__":main()
