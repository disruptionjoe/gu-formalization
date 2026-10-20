#!/usr/bin/env python3
"""Independent exact moment integration, density-jet and OU controls."""
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[2]
def derive(p,n=1):
    for _ in range(n):p={i-1:i*v for i,v in p.items() if i}
    return p
def integral(p):return sum(2*v/F(i+1) for i,v in p.items() if i%2==0)
def shift(p,j):return {i+j:v for i,v in p.items()}
def value(p,x):return sum(v*x**i for i,v in p.items())
def valid(d):
    return (d['scope']=='even_densities_second_moment_1_fourth_k_between_1_and_3' and
      all(d['mathematical_checks'].values()) and d['unique_positive_quartic_ground_state'] and
      not d['finite_common_variance_mixtures_stationary'] and not d['effective_gap'] and
      not d['unrestricted_endpoint_expansion'] and not d['GU_physics_credit'] and not d['canon_promotion'])
def main():
    controls=0
    def ck(v):
        nonlocal controls
        assert v;controls+=1
    for order in (7,8,9):
        phi={2*j:F((-1)**j*comb(order,j)) for j in range(order+1)};h=derive(phi,6)
        for j in (0,2,4):ck(integral(shift(h,j))==0)
        for j in range(6):ck(value(derive(phi,j),F(1))==value(derive(phi,j),F(-1))==0)
        ck(integral(shift(h,6))==factorial(6)*integral(phi)>0)
        # With R=x^6 choose -h: exact negative first variation.
        ck(-integral(shift(h,6))<0)
    # Independently expand the rational density-jet integrand in epsilon.
    for p in (F(1,2),F(1),F(3)):
      for dp,h,dh in ((F(2),F(1),F(3)),(F(-1),F(2),F(1)),(F(1,3),F(-2),F(5))):
        # epsilon² coefficient from geometric expansion of denominator.
        e2=dh*dh/p-2*dp*dh*h/p**2+dp*dp*h*h/p**3
        ck(2*e2==2*(dh*p-h*dp)**2/p**3)
        ck(e2>=0)
        q=F(2);dq=F(3)
        defect=(dp*dp/p+dq*dq/q)/2-(dp+dq)**2/(2*(p+q))
        ck(defect==(dp*q-dq*p)**2/(2*p*q*(p+q))>=0)
    for a2 in (F(1,4),F(1,2),F(3,4)):
        v=1-a2;k=a2*a2+6*a2*v+3*v*v
        ck(k==3-2*a2*a2);ck(1<k<3)
        for r2 in (F(1,4),F(1,2),F(3,4)):
            new=r2*r2*k+6*r2*(1-r2)+3*(1-r2)**2
            ck(new==3+r2*r2*(k-3));ck(k<new<3)
    for M in (F(1,2),F(1),F(2)):
      for v in (F(1,3),F(1),F(2)):
        # Gaussian log score directly yields R=2/v-score².
        linear=2*M/v**2;ck(linear!=0)
        for x in (F(2),F(3)):
            rp=2/v-(x-M)**2/v**2;rn=2/v-(-x-M)**2/v**2
            ck(rp-rn==2*linear*x)
    # D + 8 C epsilon <= D/2 at the asserted finite-step threshold.
    for D,C in ((F(-1),F(1)),(F(-2),F(3)),(F(-3,7),F(5,2))):
        eps=-D/(16*C);ck(D+8*C*eps==D/2<0)
    d=json.loads((ROOT/'lab/process/k1843-unrestricted-fisher-variational-gap.json').read_text());assert valid(d)
    mutations={'unique_positive_quartic_ground_state':False,'finite_common_variance_mixtures_stationary':True,'effective_gap':True,'unrestricted_endpoint_expansion':True,'GU_physics_credit':True,'canon_promotion':True}
    for key,v in mutations.items():
        bad=copy.deepcopy(d);bad[key]=v;assert not valid(bad)
    print(f'K1843 independent rational controls: {controls}; reporting faults rejected: {len(mutations)}')
if __name__=='__main__':main()
