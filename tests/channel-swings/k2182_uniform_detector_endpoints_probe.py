#!/usr/bin/env python3
"""Endpoint boundary expansion, cusp and uniform exact-contrast repair controls."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
import sympy as S
from k2178_effective_detector_approximation_probe import p,A,B,tau,energy,contrast,sqrt_iv,ivadd,scale,point
ROOT=Path(__file__).resolve().parents[2]
C=F(40,3);M=F(369,10);LO=F(2,3);HI=F(113,100)
def defect(x,fault=None):
    return x[0]+sum(((3*n-2) if fault=='defect_weight' else (3*n-1))*(p(n)-x[n]) for n in range(1,len(x)))
def leading(x,s1,s0,fault=None):
    return scale(C,ivadd(scale(s1,sqrt_iv(p(1)*x[0])),scale(0 if fault=='missing_noclick' else s0,sqrt_iv(p(0)*(p(1)-x[1])))))
def rational_rho(k):return 3*B(k)/2+90*F(k+1,2**(k+1))
def epsilon_plan(eps):
    k=2
    while tau(k)+rational_rho(k)>eps/2:k+=1
    j=0
    while F(15,2**j)>eps/2:j+=1
    return dict(K=k,bisections=j,width_upper=str(tau(k)+rational_rho(k)+F(15,2**j)))
def controls(fault=None):
    cs={};ck=lambda n,v:cs.__setitem__(n,bool(v))
    ck('moment_weight_all_n',S.simplify(S.Rational(3,4)*(3*S.Symbol('n')-1)-(S.Symbol('n')+S.Rational(1,2)))==5*(S.Symbol('n')-1)/4)
    n=S.symbols('n',integer=True,positive=True)
    ck('click_bulk_ratio',S.expand(S.Rational(11,10)*(3*n-1)-(5*n+1)/2)==S.Rational(4,5)*(n-2))
    ck('click_edge_gap',(F(2,5))**2>F(1,8))
    ck('M_from_actual_bounds',3+C*HI*(F(3,2)+F(3,4))==M)
    ck('strong_convexity',F(3,8)*F(41,3)==F(41,8))
    ck('complete_square_cost',F(200,3)/(2*F(41,8))==F(800,123))
    ck('endpoint_modulus',M+F(800,123)<44 and 10*HI<12)
    ck('strict_neighborhood_margin',F(20,3)-5*M/32==F(173,192)>0)
    a,b,d=S.symbols('a b d',positive=True);den=a*a+2*b*b
    weight=1 if fault=='allocation_weight' else 2
    x0=d*a*a/den;y1=d*b*b/den
    ck('allocation_defect',S.simplify(x0+weight*y1-d)==0)
    ck('allocation_coefficient',C*C*(S.Rational(3,16)*a*a+S.Rational(3,8)*b*b)==S.Rational(100,3)*den)
    ck('allocation_caps',F(3,8)<p(0) and F(3,8)/2==p(1))
    # Full infinite tail is exactly geometric; only these head coordinates are altered.
    endpoint=[F(0),p(1),p(2),p(3)]
    for i,delta in enumerate([F(1,10**8),F(1,1024),F(1,16),F(3,8)]):
        profiles=[('x0',[delta,p(1),p(2),p(3)]),('y1',[F(0),p(1)-delta/2,p(2),p(3)]),('balanced',[delta/3,p(1)-delta/3,p(2),p(3)])]
        if delta<=F(1,16):profiles.append(('far',[F(0),p(1),p(2),p(3)-delta/8]))
        for label,x in profiles:
            ck(f'defect_{i}_{label}',defect(x,fault)==F(3,4)-contrast(x,F(1))==delta)
            ck(f'caps_{i}_{label}',all(0<=v<=p(n) for n,v in enumerate(x)))
            for j,(s1,s0) in enumerate([(LO,HI),(HI,LO),(F(1),F(1))]):
                e=energy(x,F(1),s1,s0);e0=energy(endpoint,F(1),s1,s0)
                rem=ivadd(ivadd(e,scale(-1,e0)),leading(x,s1,s0,fault))
                ck(f'expansion_{i}_{label}_{j}',-M*delta<=rem[0] and rem[1]<=M*delta)
    # Correct edge moment totals are derived from geometric generating functions.
    z=S.symbols('z');mass=S.Rational(3,4)/(1-z);weighted=S.diff(z*mass,z)
    ck('edge_totals',weighted.subs(z,S.Rational(1,4))==S.Rational(4,3) and (z*weighted).subs(z,S.Rational(1,4))==S.Rational(1,3))
    ck('uniform_constant30',452**2*(F(3)+F(20,7))<450**2*6 and F(10,7)**2>2)
    for n in range(1,20):
        ck('repair_moment_'+str(n),F(n)+F(1,2)<=F(3,4)*(3*n-1))
        ck('repair_edges_'+str(n),n+1<=3*n-1 and n<=F(3*n-1,2))
    head=[p(n)/3 for n in range(4)];tail=F(1,3);old=contrast(head,tail)
    for sign in [-1,1]:
        r=[p(0),F(0),F(0),F(0)] if sign<0 else endpoint;rt=F(sign>0)
        for alpha in [F(1,1000),F(1,3),F(1)]:
            w=[(1-alpha)*x+alpha*y for x,y in zip(head,r)];wt=(1-alpha)*tail+alpha*rt
            target=(1-alpha)*old+alpha*sign*F(3,4);h=abs(target-old)
            ck(f'actual_contrast_{sign}_{alpha}',contrast(w,wt)==target)
            # Exact tail absolute moment (sign is constant on the tail).
            hcalc=sum(abs(3*n-1)*abs(w[n]-head[n]) for n in range(4))+abs(wt-tail)*B(3)
            if fault=='repair_tail':hcalc-=abs(wt-tail)*B(3)
            ck(f'absolute_defect_{sign}_{alpha}',hcalc==h)
            if fault=='repair_direction':w=list(head);wt=tail
            ck(f'repair_hits_{sign}_{alpha}',contrast(w,wt)==target)
            for j,(s1,s0) in enumerate([(LO,HI),(HI,LO)]):
                before=energy(head,tail,s1,s0);after=energy(w,wt,s1,s0)
                bound=3*h+30*sqrt_iv(2*h)[0]
                ck(f'uniform_energy_{sign}_{alpha}_{j}',max(after[1]-before[0],before[1]-after[0])<bound)
    for k in [2,6,15,100]:ck('rational_sqrt_'+str(k),B(k)<=F(3*(k+1),2**(k+1))**2)
    return cs
FAULTS=['defect_weight','missing_noclick','allocation_weight','repair_tail','repair_direction']
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    cs=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
    faults={}
    for f in FAULTS:
        bad=[n for n,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
    plans={str(e):epsilon_plan(e) for e in [F(1,10000),F(1,10**12),F(1,10**60)]}
    for e,plan in plans.items():assert F(plan['width_upper'])<F(e)
    deps=['explorations/conditional-build/k2182-uniform-detector-endpoints-2026-10-28.md','explorations/conditional-build/k2180-detector-contrast-frontier-2026-10-28.md','tests/channel-swings/k2178_effective_detector_approximation_probe.py','tests/channel-swings/k2180_detector_contrast_frontier_probe.py']
    report=dict(result_id='K2182',status='conditional_exact_controls',checks=cs,fault_failures=faults,uniform_epsilon_plans=plans,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Independent written infinite-sum, coercivity, convex-mixture and optimizer-localization proofs; finite exact and rational interval controls supplement them. Finite optimizer unimplemented, no new numerical optimum, physical quotient or apparatus accounting.')
    dst=ROOT/'lab/process/k2182-uniform-detector-endpoints.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report
    print(json.dumps(dict(result='K2182',checks=len(cs),faults=len(faults),plans=plans)))
if __name__=='__main__':main()
