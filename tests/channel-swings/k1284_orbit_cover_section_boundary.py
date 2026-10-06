#!/usr/bin/env python3
"""Exact controls for K1284."""
import json, math
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1284-orbit-cover-section-boundary.json").read_text()); n=0
def c(label,x):
    global n; assert x,label; n+=1; print(f"PASS {n:02d}: {label}")
c("id",D["result_id"]=="K1284-ORBIT-COVER-SECTION-BOUNDARY")
for sigma in (-1,1):
    vals=[sigma*math.sqrt(q) for q in (0.25,1,4,9)]
    c(f"section sigma={sigma}",all(abs(p*p-q)<1e-12 for p,q in zip(vals,(0.25,1,4,9))))
    c(f"constant sign sigma={sigma}",all((p>0)==(sigma>0) for p in vals))
for h in (1e-2,1e-4,1e-6): c(f"difference quotient diverges h={h}",math.sqrt(h)/h>=1/math.sqrt(1e-2))
c("no equivariant section",D["cover_theorem"]["deck_equivariant_section_over_regular_base_exists"] is False)
c("component choice",D["decision"]["one_component_restriction_imports_orientation_choice"] is True)
c("continuous extension",D["cover_theorem"]["continuous_extension_to_branch_point"]=="p(0)=0")
c("not C1",D["cover_theorem"]["C1_extension_in_q_at_branch_point"] is False)
assert n==12; print("RESULT: PASS 12/12")
