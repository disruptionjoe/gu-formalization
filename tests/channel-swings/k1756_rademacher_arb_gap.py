#!/usr/bin/env python3
"""Arb certificate separating the Rademacher face from K1753's candidate."""
import importlib.util,json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ARTIFACT=ROOT/"lab/process/k1756-rademacher-arb-gap.json"
P=ROOT/"tests/channel-swings/k1749_arb_finite_channel_boundary.py"
s=importlib.util.spec_from_file_location("k1749",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)

def channels():
 c=Q(3308164903,2000000000);z=Q(1127044207,2000000000)
 p=k.aq(c/(c+z*z));a=k.aq(1-z);b,u,_,_=k.chart_invariants(p,a);t=(k.aq(Q(1,1024))/u.v).sqrt()
 candidate={"p":p,"a":a,"b":b.v,"u":u.v,"t":t,"v":1-t}
 tr=k.aq(Q(1,2048)).sqrt()
 rademacher={"p":k.aq(0),"a":k.aq(0),"b":k.aq(1),"u":k.aq(2),"t":tr,"v":1-tr}
 return candidate,rademacher

def compute():
 candidate,rademacher=channels();gap,rem,cells=k.compact_integral(candidate,rademacher)
 tails=k.tail_bound(candidate)+k.tail_bound(rademacher);whole=gap+k.arb(0,tails.upper())
 return gap,tails,whole,rem,cells

def validate(d):
 gap,tails,whole,rem,cells=compute();c=d["comparison"];z=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1756"),
  ("backend",d["backend"]=="python-flint==0.9.0"),("cells",cells==352 and c["compact_cell_count"]==cells),
  ("compact containment",k.arb(c["compact_gap"]).contains(gap)),
  ("tail containment",k.arb(c["combined_tail_upper"]).contains(tails)),
  ("whole containment",k.arb(c["whole_line_gap"]).contains(whole)),
  ("remainder containment",k.arb(c["maximum_cell_remainder"]).contains(rem)),
  ("gap threshold",whole.lower()>k.aq(Q(22,10**11))),
  ("strict",z["rademacher_strictly_above_candidate"]),("threshold decision",z["certified_gap_exceeds_2_20e_minus_10"]),
  ("collar fenced",not z["rare_atom_collar_follows_without_stability_bound"]),
  ("global fenced",not z["global_optimizer_proved"]),("protected",not z["source_or_physical_status_change"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
