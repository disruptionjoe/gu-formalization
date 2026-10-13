#!/usr/bin/env python3
"""Symbolic rare-face limit and fail-closed pilot accounting for K1764."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1764-interval-cover-pilot.json"

def rare_limit():
 c,z,t,q=s.symbols("c z t q",positive=True);p=c/(c+z**2);a=1-z;b=1+c/z
 raw=lambda r:s.cancel(p*a**r+(1-p)*b**r)
 def h(n):return s.factor(t**(n//2)*sum((-1)**k*s.factorial(n)/(s.factorial(k)*s.factorial(n-2*k)*2**k)*raw((n-2*k)//2) for k in range(n//2+1)))
 hh={n:h(n) for n in (4,6,8,10)};G11=hh[6]+9*hh[4]+6;G12=hh[8]+15*hh[6]+60*hh[4];G22=hh[10]+25*hh[8]+200*hh[6]+600*hh[4]+120
 L=s.factor((hh[4]**2*G22-2*hh[4]*hh[6]*G12+hh[6]**2*G11)/(G11*G22-G12**2))
 return s.factor(s.limit(L,z,0,dir='+').subs(c,2-q/t**2))

def validate(d):
 expected=2*s.Symbol('t',positive=True)**4/(3-2*s.Symbol('q',positive=True)+2*s.Symbol('q',positive=True)*s.Symbol('t',positive=True)-5*s.Symbol('t',positive=True)**2+4*s.Symbol('t',positive=True)**3)
 # Rebuild with shared symbols to avoid assumption-identity ambiguity.
 got=rare_limit();symbols={x.name:x for x in got.free_symbols};t,q=symbols["t"],symbols["q"]
 expected=2*t**4/(3-2*q+2*q*t-5*t**2+4*t**3)
 p=d["fail_closed_pilot"];z=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1764"),("limit",s.simplify(got-expected)==0),("formula",d["rare_face_limit"]["formula"]=="lim_(z->0+) L5(t,z)=2t^4/(3-2q+2qt-5t^2+4t^3)"),("budget partition",p["pruned_leaves"]+p["unresolved_or_unvisited_leaves"]==p["leaf_budget"]),("degree sum",sum(p["degree_counts"].values())==p["pruned_leaves"]),("fail closed",not p["coverage_complete"] and not p["scientific_exclusions_claimed_from_pilot"]),("reject naive",z["naive_independent_ball_global_engine_rejected"]),("removable",not z["rare_face_is_a_mathematical_singularity_of_L5"]),("next engine",z["next_engine_requires_symbolic_cancellation_or_correlated_coordinates"]),("not global",not z["global_interval_cover_completed"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
