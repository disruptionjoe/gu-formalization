#!/usr/bin/env python3
"""Exact rational polynomial controls; not a smooth Stokes proof.
Box polynomials have sufficient vanishing boundary jets, not global C-infinity
cutoffs. The universal support argument is written/reviewed separately.
"""
import argparse
from fractions import Fraction as Q
import json
import time

class P(dict):
    def __init__(self,d=None):
        super().__init__({k:Q(v) for k,v in (d or {}).items() if v})
    def __add__(self,b):
        d=dict(self)
        for k,v in b.items():d[k]=d.get(k,Q(0))+v
        return P(d)
    def __neg__(self):return P({k:-v for k,v in self.items()})
    def __sub__(self,b):return self+-b
    def __mul__(self,b):
        d={}
        for a,v in self.items():
            for c,w in b.items():
                k=tuple(x+y for x,y in zip(a,c));d[k]=d.get(k,Q(0))+v*w
        return P(d)
    def __pow__(self,n):
        r=P({(0,0):1})
        for _ in range(n):r=r*self
        return r
    def diff(self,i):
        d={}
        for k,v in self.items():
            if k[i]:
                j=list(k);j[i]-=1;d[tuple(j)]=v*k[i]
        return P(d)
    def at(self,i,a):
        d={}
        for k,v in self.items():
            j=list(k);j[i]=0;j=tuple(j);d[j]=d.get(j,Q(0))+v*Q(a)**k[i]
        return P(d)
    def integral_x(self):
        d={}
        for (i,j),v in self.items():
            if j%2==0:d[(i,0)]=d.get((i,0),Q(0))+v*Q(2,j+1)
        return P(d)
    def scalar(self):
        assert all(k==(0,0) for k in self)
        return self.get((0,0),Q(0))

def run():
    one=P({(0,0):1});t=P({(1,0):1});x=P({(0,1):1});checks={};charges=[]
    # Independent hand-calculated arithmetic checks for this tiny polynomial engine.
    checks['engine_derivative']=((x**3).diff(1)==P({(0,2):3}))
    checks['engine_integral']=(x*x).integral_x().scalar()==Q(2,3)
    checks['engine_substitution']=(x-t).at(0,2)==x-P({(0,0):2})
    for p in range(4):
        f=(one-t*t)**4*(one-x*x)**4*x**p
        energy=f.diff(1).diff(1);flux=-f.diff(0).diff(1)
        checks[f'improvement_{p}_divergence']=not energy.diff(0)+flux.diff(1)
        q=energy.integral_x();charges.append('0' if not q else str(q))
        checks[f'improvement_{p}_charge_zero']=not q
        checks[f'improvement_{p}_side_flux']=all(not flux.at(1,a) for a in [-1,1])
        checks[f'improvement_{p}_future_zero']=not energy.at(0,1)
        checks[f'improvement_{p}_nonzero_local']=bool(energy)
    e=((one-x*x)**4).diff(1).diff(1)
    checks['improvement_both_signs']=e.at(1,0).scalar()<0 and e.at(1,Q(1,2)).scalar()>0
    # Compact right-moving wave, zero outside |x-t|<=1. It has sufficient
    # differentiability for these controls; smooth bumps obey the same identity.
    phi=(one-(x-t)**2)**4
    energy=phi.diff(1)**2;flux=energy
    checks['on_shell_wave_equation']=not phi.diff(0).diff(0)-phi.diff(1).diff(1)
    checks['on_shell_current_conserved']=not energy.diff(0)+flux.diff(1)
    q=energy.at(0,0).integral_x().scalar()
    checks['on_shell_compact_charge_positive']=q>0
    cut=(one-t*t)*phi
    checks['on_shell_cutoff_not_admissible']=bool(cut.diff(0).diff(0)-cut.diff(1).diff(1))
    beta=t*(one-x*x)**2
    checks['planted_positive_readout_not_conserved']=bool((beta*beta).diff(0))
    return {'checks':checks,'grouped_checks':len(checks),'improvement_charges':charges,
            'positive_wave_charge':str(q),'scope':'Finite exact boundary/known-answer controls; no GU physical state or universal smooth proof inferred.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--verify',action='store_true');p.parse_args()
    start=time.perf_counter();r=run();r['runtime_seconds']=time.perf_counter()-start
    print(json.dumps(r,indent=2));raise SystemExit(0 if all(r['checks'].values()) else 1)
