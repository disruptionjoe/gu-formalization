#!/usr/bin/env python3
"""Independent rational controls, not a numerical continuum propagation test."""
from fractions import Fraction as F
from pathlib import Path
from math import comb
import json,copy
ROOT=Path(__file__).resolve().parents[2]

def validate_report(d):
    return (d['scope']=='conditional_scalar_response_only' and
      all(d['mathematical_checks'].values()) and not d['source_owned'] and
      not d['all_nonlocal_theories_excluded'] and not d['causal_repair_exact_projector'] and
      not d['causal_repair_erases_history'] and not d['ledger_changes'])

def main():
    controls=0
    def ck(v):
        nonlocal controls
        assert v;controls+=1
    for n in (3,4,7):
        def Q(v):
            av=sum(v)/n;return [x-av for x in v]
        for j in range(n):
            f=[F(int(i==j)) for i in range(n)];q=Q(f)
            ck(Q(q)==q);ck(sum(q)==0);ck(q[(j+1)%n]==-F(1,n))
            f[(j+1)%n]-=1
            ck(Q(f)==f)
        v=[F(i*i,7) for i in range(n)]
        ck(Q(v)[0]-Q(v)[1]==v[0]-v[1]);ck(Q([F(1)]*n)==[0]*n)
    # Independently integrate eta=s^a(1-s)^b against (t-s) on [0,1].
    for a,b in ((1,1),(2,2),(3,4)):
        coeff={a+j:F((-1)**j*comb(b,j)) for j in range(b+1)}
        area=sum(v/F(i+1) for i,v in coeff.items())
        first=sum(v/F(i+2) for i,v in coeff.items())
        ck(area>0);ck(0<first<area)
        for t in (F(1),F(3,2),F(2)):
            ck(t*area-first>0)
        if a==b==2:ck(area-first==F(1,60))
    for mu in (F(1),F(2),F(3,2)):
        for z in (F(0),F(1),F(2)):
            N=z*z+2*mu*z;q=N/(N+mu*mu)
            ck(q*q-q==-mu*mu*N/(N+mu*mu)**2)
            if z:ck(0<q<1)
            else:ck(q==0)
        # Laplace residual for critical damping: (s+2mu)/(s+mu)^2.
        ck((2*mu)/(mu*mu)==2/mu)
    report=json.loads((ROOT/'lab/process/k1842-screening-causal-response.json').read_text());assert validate_report(report)
    fields=['source_owned','all_nonlocal_theories_excluded','causal_repair_exact_projector','causal_repair_erases_history','ledger_changes']
    faults=0
    for field in fields:
        d=copy.deepcopy(report);d[field]=True;assert not validate_report(d);faults+=1
    print(f'K1842 independent rational controls: {controls}; reporting faults rejected: {faults}')
if __name__=='__main__':main()
