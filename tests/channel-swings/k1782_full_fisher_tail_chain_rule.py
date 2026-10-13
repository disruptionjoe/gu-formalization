#!/usr/bin/env python3
"""Replay finite chart-to-natural derivative bounds for K1782."""
import importlib.util,json
from fractions import Fraction as F
from pathlib import Path
from flint import arb
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1782-full-fisher-tail-chain-rule.json"
P=ROOT/"tests/channel-swings/k1781_full_fisher_compact_jet.py";s=importlib.util.spec_from_file_location("k1781",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)
SLABS=json.loads((ROOT/"lab/process/k1771-interior-survivor-topology.json").read_text())["topology"]["slabs"]
def mag(x): return max(abs(x.lower()),abs(x.upper()))
def compute():
 rows=[];global_max={"first":arb(0),"second":arb(0)}
 for index,slab in enumerate(SLABS,1):
  ta,tb=map(F,slab["t"]);za,zb=map(F,slab["z"]);t=k.J.var(k.ball(ta,tb),0);z=k.J.var(k.ball(za,zb),1)
  p,a,b,v=k.channel(t,z);fields={"p":p,"a":a,"b":b,"v":v,"mu_a":(t*a).sqrt(),"mu_b":(t*b).sqrt(),"sigma":v.sqrt(),"alpha_a":(t*a).sqrt()/v,"alpha_b":(t*b).sqrt()/v}
  first=max((mag(x) for f in fields.values() for x in f.g),default=arb(0));second=max((mag(x) for f in fields.values() for row in f.h for x in row),default=arb(0))
  global_max["first"]=max(global_max["first"],first);global_max["second"]=max(global_max["second"],second)
  rows.append({"slab":index,"t":slab["t"],"z":slab["z"],"minimum_p":k.enc(p.v.lower()),"minimum_one_minus_p":k.enc((1-p).v.lower()),"minimum_a":k.enc(a.v.lower()),"minimum_v":k.enc(v.v.lower()),"maximum_first_derivative_magnitude":k.enc(first),"maximum_second_derivative_magnitude":k.enc(second)})
 return {"slabs":rows,"global_maximum_first_derivative_magnitude":k.enc(global_max["first"]),"global_maximum_second_derivative_magnitude":k.enc(global_max["second"])}
def validate(d,got=None):
 got=compute() if got is None else got;x=d["chart_bounds"];z=d["decision"]
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1782"),("three slabs",len(x["slabs"])==3)]
 for old,new in zip(x["slabs"],got["slabs"]):
  checks += [(f"slab {new['slab']} identity",old["slab"]==new["slab"]),(f"slab {new['slab']} p positive",arb(old["minimum_p"])>0),(f"slab {new['slab']} mixture positive",arb(old["minimum_one_minus_p"])>0),(f"slab {new['slab']} variance positive",arb(old["minimum_v"])>0),(f"slab {new['slab']} first bound",arb(old["maximum_first_derivative_magnitude"]).contains(arb(new["maximum_first_derivative_magnitude"]))),(f"slab {new['slab']} second bound",arb(old["maximum_second_derivative_magnitude"]).contains(arb(new["maximum_second_derivative_magnitude"])))]
 checks += [("chart finite",z["chart_chain_rule_finite_on_three_slabs"]),("natural tails available",z["natural_derivative_tails_available_through_order_three"]),("quotient tails open",not z["whole_line_full_fisher_quotient_tail_composed"]),("Newton open",not z["three_slab_interval_newton_completed"])]
 return checks
def main():
 if not ARTIFACT.exists() or "--print" in __import__("sys").argv:print(json.dumps(compute(),indent=2));return
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
