#!/usr/bin/env python3
"""Derivative-rank and K1728 representative controls for K1732."""
import json, math
from pathlib import Path
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[2]

def vals(p,a):
    b=(1-p*a)/(1-p); m2=p*a*a+(1-p)*b*b; m3=p*a**3+(1-p)*b**3
    return b,3-m2,m3-15*m2+30

def derivative(f,x,h=1e-6): return (f(x+h)-f(x-h))/(2*h)

def main():
    d=json.loads((ROOT/"lab/process/k1732-quartic-optimal-tangent-family.json").read_text())
    u0=brentq(lambda u:17*u**3-38*u**2+84*u-24,0,1); s=2*(6-7*u0)/(2-u0);r=s-(3-u0)
    a0=(s-(s*s-4*r)**.5)/2;b0=(s+(s*s-4*r)**.5)/2;p0=(b0-1)/(b0-a0)
    gp=derivative(lambda p:vals(p,a0)[2],p0);ga=derivative(lambda a:vals(p0,a)[2],a0)
    target=(35/3)*u0**1.5; beta=-0.480253485638498; vfix=(beta,beta*a0*(b0-a0))
    dot=gp*vfix[0]+ga*vfix[1]; null=(ga,-gp)
    checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1732"),
      ("gradient nonzero",math.hypot(gp,ga)>1),("target positive",target>0),
      ("fixed tangent",abs(dot-target)<2e-7),("null orthogonal",abs(gp*null[0]+ga*null[1])<1e-12),
      ("affine line","affine one-dimensional" in d["title"]),("constraint","kappa6_p" in d["tangent"]["constraint"]),
      ("null text","kappa6_a,-kappa6_p" in d["tangent"]["null_direction"]),
      ("minimum norm","grad kappa6" in d["tangent"]["minimum_norm_representative"]),
      ("K1728 preserved",d["decision"]["k1728_attainment_preserved"]),
      ("not unique",not d["decision"]["quartic_optimal_tangent_unique"]),
      ("finite open",not d["decision"]["finite_strength_optimizer_identified"]),
      ("next order",d["decision"]["next_order_required_to_select_tangent"]),
      ("local scope","first-order" in d["scope_guard"]),("global scope","globally" in d["scope_guard"])]
    for i,(label,ok) in enumerate(checks,1): assert ok,label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__": main()
