#!/usr/bin/env python3
"""Arb replay of K1780's strict rational descent and entry-state ceiling."""
import importlib.util,json
from fractions import Fraction as F
from pathlib import Path
from flint import arb
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1780-full-fisher-entry-admission.json"
P=ROOT/"tests/channel-swings/k1749_arb_finite_channel_boundary.py";s=importlib.util.spec_from_file_location("k1749",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)
def channel(c,z):
 p=k.aq(c/(c+z*z));a=k.aq(1-z);b,u,_,_=k.chart_invariants(p,a);t=(k.aq(F(1,1024))/u.v).sqrt();return {"p":p,"a":a,"b":b.v,"u":u.v,"t":t,"v":1-t}
def compute(d):
 x=d["rational_descent"];o=x["old_candidate"];n=x["new_candidate"];old=channel(F(o["c"]),F(o["z"]));new=channel(F(n["c"]),F(n["z"]));gap,rem,cells=k.compact_integral(new,old);tails=k.tail_bound(new)+k.tail_bound(old);return gap+arb(0,tails.upper()),cells
def validate(d):
 gap,cells=compute(d);x=d["rational_descent"];e=d["entry_state"];z=d["decision"];c=d["bridge_census"];p=d["protected_state"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1780"),("q",x["q"]=="1/1024"),
  ("inputs",d["inputs"]==["K1775","K1776","K1777","K1778","K1779"]),("census",c=={"total":480,"satisfied":401,"conditional":10,"excluded":65,"missing":4}),
  ("protected",all(v is False for key,v in p.items() if key.endswith("_changed"))),
  ("cells",x["compact_cell_count"]==cells==352),("gap containment",arb(x["whole_line_gap"]).contains(gap)),("gap positive",arb(x["whole_line_gap"])>0),
  ("boundary closed",e["boundary_cells_remaining"]==0 and z["boundary_cells_excluded"]),("three slabs",e["interior_slabs_remaining"]==3),
  ("tails",e["derivative_tail_order_available"]==3),("z1",e["z1_atom_chart_available"]),("compact open",not e["compact_window_value_gradient_hessian_evaluator_available"]),
  ("Newton open",not e["full_fisher_interval_newton_completed"]),("old not optimal",not z["k1753_candidate_locally_optimal"] and z["strict_rational_descent_certified"]),
  ("no stationarity",not z["stationary_point_proved"]),("no uniqueness",not z["unique_component_proved"]),("no global",not z["global_optimizer_proved"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
