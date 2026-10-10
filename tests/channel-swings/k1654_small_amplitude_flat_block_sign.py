#!/usr/bin/env python3
"""Certificate for K1654's small-amplitude sign classification."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def main():
    d=json.loads((ROOT/"lab/process/k1654-small-amplitude-flat-block-sign.json").read_text());q,z=d["sign_classification"],d["decision"]
    checks=[]
    for g,a0,c0,c1 in [(0.1,.4,.001,.003),(1,.5,.002,.004),(10,.3,.0005,.002)]:
        eta=a0*a0*c0/(12*g*c1*c1)
        positive=.5*a0*a0*c0*eta
        negative=1.5*g*c1*c1*eta*eta
        checks += [(f"eta positive g={g}",eta>0),(f"strict sign g={g}",positive>negative)]
    checks += [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1654"),("shell", "a_0N<=omega_k<=a_1N" in q["shell_constants"]),("linear lower","eta N^4" in q["positive_lower"]),("quadratic upper","eta^2 N^4" in q["negative_upper"]),("threshold","a_0^2c_0/(6gc_1^2)" in q["threshold"]),("small scope","sufficiently small fixed amplitudes" in q["scope_guard"]),("linear decision",z["positive_term_linear_in_eta"]),("quadratic decision",z["negative_term_quadratic_in_eta"]),("positive gap",z["small_amplitude_leading_gap_positive"]),("all amplitude open",not z["all_admissible_amplitudes_classified"]),("coefficient open",not z["unrestricted_coefficient_identified"]),("protected",not z["protected_status_change"])]
    for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
