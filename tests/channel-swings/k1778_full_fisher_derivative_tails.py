#!/usr/bin/env python3
"""Replay Gaussian value/parameter-derivative tail budgets for K1778."""
import json
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1778-full-fisher-derivative-tails.json"
ctx.dps=100;ctx.threads=1
def compute():
 L=arb(11);phi=(-L**2/2).exp()/(2*arb.pi()).sqrt()
 moments=[2*phi/L,2*phi,2*(L+1/L)*phi,2*(L**2+2)*phi]
 derivatives={"tanh":[arb(1),arb(1),arb(77)/100,arb(2)],"tanh_squared":[arb(1),arb(77)/100,arb(2),arb(41)/10]}
 largest=max((derivatives[f][n]*moments[j] for f in derivatives for n in range(4) for j in range(n+1)),key=lambda x:x.upper())
 return moments,derivatives,largest
def validate(d):
 m,ds,largest=compute();x=d["contract"];z=d["decision"]
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1778"),("window",x["compact_window"]=="[-11,11]"),("order",x["maximum_total_derivative_order"]==3)]
 for i,name in enumerate(("M0","M1","M2","M3")):checks.append((name,arb(x["gaussian_tail_moment_uppers"][name]).contains(m[i])))
 checks += [("tanh bounds",[F(v) for v in x["derivative_sup_uppers"]["tanh"]]==[F(1),F(1),F(77,100),F(2)]),
  ("square bounds",[F(v) for v in x["derivative_sup_uppers"]["tanh_squared"]]==[F(1),F(77,100),F(2),F(41,10)]),
  ("largest",arb(x["largest_admitted_tail"]).contains(largest)),("tails certified",z["value_gradient_hessian_and_third_natural_derivative_tails_certified"]),
  ("compact open",not z["compact_window_derivative_evaluator_completed"]),("Newton open",not z["three_slab_interval_newton_completed"])]
 return checks
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
