#!/usr/bin/env python3
"""Replay K1776's exact derivative envelopes and mixture identities."""
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1776-full-fisher-semiconvexity.json"

def bernstein_min(coeffs,a,b):
    n=max(coeffs);power=[F(0)]*(n+1)
    for k,v in coeffs.items():
        for i in range(k+1):power[i]+=v*comb(k,i)*a**(k-i)*(b-a)**i
    return min(sum(power[k]*F(comb(i,k),comb(n,k)) for k in range(i+1)) for i in range(n+1))

def polynomial_bound():
    # (41/10)^2-[-16x+40x^3-24x^5]^2 is positive on [-1,1].
    p={0:F(1681,100),2:F(-256),4:F(1280),6:F(-2368),8:F(1920),10:F(-576)}
    return min(bernstein_min(p,F(-1)+F(i,16),F(-1)+F(i+1,16)) for i in range(32))

def validate(d):
    th=d["theorem"];mix=d["two_radius_identity"];dec=d["decision"]
    samples=[]
    for c,z in ((F(1,100),F(1,10)),(F(1,1000),F(1,20)),(F(4,100000),F(1,2**23))):
        p=c/(c+z*z);s1=1-z;s2=1+c/z
        samples += [p*s1+(1-p)*s2==1,p*(s1-1)**2+(1-p)*(s2-1)**2==c]
    return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1776"),
      ("tanh second",F(16,27)<F(77,100)**2),("square third",polynomial_bound()>0),
      ("mixture identities",all(samples)),("semiconvex constants","231/400" in th["semiconvexity"] and "41/80" in th["semiconvexity"]),
      ("corollary",mix["centered_second_moment"]=="E[(S-1)^2]=c"),
      ("proved",dec["global_semiconvexity_proved"]),("no raw division",not dec["raw_c_over_z_required"]),
      ("not optimizer",not dec["full_fisher_global_optimizer_proved"])]

def main():
    d=json.loads(ARTIFACT.read_text());checks=validate(d)
    for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
