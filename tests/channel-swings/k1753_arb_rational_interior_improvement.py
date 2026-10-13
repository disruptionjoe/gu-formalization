#!/usr/bin/env python3
"""Arb whole-line certificate for K1753's rational interior point."""
import importlib.util,json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ARTIFACT=ROOT/"lab/process/k1753-arb-rational-interior-improvement.json"
P=ROOT/"tests/channel-swings/k1749_arb_finite_channel_boundary.py"
s=importlib.util.spec_from_file_location("k1749",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)

def compute():
    selected,_,_=k.channels();c=Q(3308164903,2000000000);z=Q(1127044207,2000000000)
    p=k.aq(c/(c+z*z));a=k.aq(1-z);b,u,_,_=k.chart_invariants(p,a);t=(k.aq(Q(1,1024))/u.v).sqrt()
    candidate={"p":p,"a":a,"b":b.v,"u":u.v,"t":t,"v":1-t}
    gap,rem,cells=k.compact_integral(candidate,selected)
    tails=k.tail_bound(candidate)+k.tail_bound(selected)
    whole=gap+k.arb(0,tails.upper())
    return candidate,whole,tails,rem,cells

def validate(d):
    ch,gap,tails,rem,cells=compute();cert=d["certificate"];dec=d["decision"]
    return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1753"),
      ("backend",d["backend"]=="python-flint==0.9.0"),("cells",cells==352),
      ("u exact",ch["u"].contains(k.aq(Q(691835097,2000000000)))),
      ("positive gap",gap.lower()>k.aq(Q(656,10**17))),
      ("small gap",gap.upper()<k.aq(Q(658,10**17))),
      ("tail",tails.upper()<k.aq(Q(582,10**29))),
      ("remainder",rem.upper()<k.aq(Q(826,10**28))),
      ("comparison",cert["comparison"]=="J_k1749_selected_linear-J_rational_candidate"),
      ("strict decision",dec["rational_candidate_strictly_better"]),
      ("linear not optimal",not dec["k1749_selected_linear_finite_strength_optimality"]),
      ("not global",not dec["whole_chart_global_optimizer_proved"]),
      ("scope","two named channels" in d["scope_guard"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
