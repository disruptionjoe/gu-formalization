#!/usr/bin/env python3
"""Exact symbolic controls for K1762's two-radius Hermite closure."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1762-two-radius-hermite-moments.json"

def formulas():
 c,z,t=s.symbols("c z t", positive=True);p=c/(c+z**2);a=1-z;b=1+c/z
 raw=lambda r:s.cancel(p*a**r+(1-p)*b**r)
 def h(n):return s.factor(t**(n//2)*sum((-1)**k*s.factorial(n)/(s.factorial(k)*s.factorial(n-2*k)*2**k)*raw((n-2*k)//2) for k in range(n//2+1)))
 return c,z,t,{n:h(n) for n in (4,6,8,10)}

def validate(d):
 c,z,t,h=formulas();f=d["closed_forms"];q=s.symbols("q",positive=True);dec=d["decision"]
 expected={4:"t^2*(c-2)",6:"t^3*(c^2-c*z^2-12*c*z+16*z)/z",
  8:"t^4*(c^3-c^2*z^2-24*c^2*z+c*z^4+24*c*z^3+132*c*z^2-132*z^2)/z^2",
  10:"t^5*(c^4-c^3*z^2-40*c^3*z+c^2*z^4+40*c^2*z^3+460*c^2*z^2-c*z^6-40*c*z^5-460*c*z^4-1520*c*z^3+1216*z^3)/z^3"}
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1762"),
  ("recurrence",d["central_moment_recurrence"]=="mu_0=1, mu_1=0, mu_2=c, mu_r=(c/z-z)mu_(r-1)+c mu_(r-2)"),
  ("raw conversion",d["raw_moment_conversion"]=="E[(X^2)^r]=sum_(k=0)^r binom(r,k) mu_k")]
 for n,expr in expected.items():
  parsed=s.sympify(expr.replace('^','**'),locals={"c":c,"z":z,"t":t})
  checks.append((f"h{n}",s.simplify(h[n]-parsed)==0 and f["h"+str(n)]==expr))
 checks += [("matched defect",s.simplify(h[4].subs(t**2,q/(2-c))+q)==0),
  ("finite closure",dec["degree_nine_gram_data_closed_exactly"]),("no quadrature",dec["moment_lower_bounds_require_density_quadrature"] is False),
  ("not Fisher equality",not dec["moments_determine_full_fisher_exactly"])]
 return checks
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
