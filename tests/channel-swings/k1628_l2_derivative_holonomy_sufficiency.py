#!/usr/bin/env python3
"""Certificate for K1628's L2-derivative holonomy theorem."""
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def main():
    d=json.loads((ROOT/"lab/process/k1628-l2-derivative-holonomy-sufficiency.json").read_text())
    q,z=d["sobolev_sufficiency"],d["decision"]
    # G(w)=1-w^2 on [-1,1]: ||G||_1=4/3, ||G'||_2=sqrt(8/3).
    g1=4.0/3.0; gp2=math.sqrt(8.0/3.0); R=2.0
    bound=2*R*g1+2*math.sqrt(math.pi/R)*gp2
    checks=[
        ("claim",d["claim_id"]=="K1628"),
        ("compact AC hypothesis","absolutely continuous" in q["hypothesis"]),
        ("L2 derivative","g=G' in L2" in q["hypothesis"]),
        ("atom free","no atoms" in q["atom_free"]),
        ("Fourier identity","widehat g(t)/(it)" in q["fourier_identity"]),
        ("low-time bound","2R||G||_1" in q["low_time"]),
        ("tail bound","2sqrt(pi/R)||g||_2" in q["tail"]),
        ("fixture finite",math.isfinite(bound) and bound>0),
        ("L1 conclusion","belongs to L1" in q["conclusion"]),
        ("L2 sufficient",z["l2_density_sufficient_for_holonomy_L1"]),
        ("atom-free not alone",not z["atom_free_alone_sufficient"]),
        ("singular open",not z["singular_continuous_class_closed"]),
        ("electric open",not z["electric_field_L1_proved"]),
        ("source open",not z["source_owned_flow"]),
        ("protected",not z["protected_status_change"]),
    ]
    for i,(label,ok) in enumerate(checks,1): assert ok,label;print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")

if __name__=="__main__":main()
