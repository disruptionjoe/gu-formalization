#!/usr/bin/env python3
"""Extremal convex repair, geometric error budgets and maximal-contrast endpoint."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import argparse,json,hashlib
import sympy as S
from k2178_effective_detector_approximation_probe import p,B,D,H,tau,energy,contrast,cases,sqrt_iv
ROOT=Path(__file__).resolve().parents[2]
DMAX=F(3,4);WIDTH=F(602,45)
def rho(k,margin,fault=None):
    assert margin>0
    return (F(1) if fault=='range_width' else WIDTH)*B(k)/(2*margin)
def repair(head,target,threshold=False,fault=None):
    k=len(head)-1
    c=sum((3*n-1)*x for n,x in enumerate(head))+(F(0) if fault=='half_tail' else B(k)/2)
    if c==target or (threshold and c>=target):return list(head),F(1,2),F(0),c
    upward=c<target
    extreme=DMAX if upward else -DMAX
    alpha=(target-c)/(extreme-c)
    if fault=='repair_sign':alpha=-alpha
    choose_up=not upward if fault=='extreme_direction' else upward
    r=[F(0) if n==0 else p(n) for n in range(k+1)] if choose_up else [p(0)]+[F(0)]*k
    result=[(1-alpha)*x+alpha*y for x,y in zip(head,r)]
    tail=(1-alpha)/2+alpha*(1 if choose_up else 0)
    if fault=='tail_mix':tail=F(1,2)
    return result,tail,alpha,c

def admissible(head,target,threshold=False,fault=None):
    h=sum((3*n-1)*x for n,x in enumerate(head));k=len(head)-1
    lower=target-(B(k)/2 if fault=='relaxed_width' else B(k))
    box=all(0<=x<=p(n) for n,x in enumerate(head))
    if threshold:return box and (h<=lower if fault=='threshold_direction' else h>=lower)
    return box and lower<=h<=target

def input_cases():
    rows=[]
    for d in [F(-7,10),F(-1,2),F(0),F(1,2),F(7,10)]:
        k=2;lo=max(d-B(k),-DMAX);hi=min(d,DMAX-B(k))
        for h in sorted(set([lo,hi,(lo+hi)/2])):
            lam=(h+DMAX)/(2*DMAX-B(k))
            rows.append((d,[(1-lam)*p(0)]+[lam*p(n) for n in range(1,k+1)]))
    rows.extend((F(1,2),x) for x in cases())
    return rows

def epsilon_plan(eps,d=F(1,2)):
    assert eps>0 and abs(d)<DMAX
    k=2
    while tau(k)+rho(k,DMAX-abs(d))>eps/2:k+=1
    j=0
    while F(15,2**j)>eps/2:j+=1
    return k,j,tau(k)+rho(k,DMAX-abs(d))+F(15,2**j)

def endpoint_certificate():
    # The polynomial has a unique positive root by strict monotonicity of A'.
    f=lambda s:451*s**4-280*s**3-99
    lo=F(2,3);hi=F(113,100)
    assert f(lo)<0<f(hi)
    for _ in range(90):
        mid=(lo+hi)/2
        if f(mid)<0:lo=mid
        else:hi=mid
    root41=sqrt_iv(F(41),10**35)
    amin=F(41,6)*lo**2+F(3,2)/hi**2;amax=F(41,6)*hi**2+F(3,2)/lo**2
    el=F(11,24)*amin+F(3,8)*root41[0]-F(35,9)*hi+F(35,18)
    eh=F(11,24)*amax+F(3,8)*root41[1]-F(35,9)*lo+F(35,18)
    assert eh-el<F(1,10**24)
    return dict(s1_interval=[str(lo),str(hi)],energy_interval=[str(el),str(eh)],width=str(eh-el),meaning='Maximum-contrast step optimum only; not a new half-contrast optimum enclosure.')

def controls(fault=None):
    cs={};ck=lambda n,v:cs.__setitem__(n,bool(v))
    ck('contrast_extreme',F(3)*(F(1,3))-F(1,4)==DMAX)
    ck('width',F(185,18)+F(31,10)==WIDTH)
    s=S.symbols('s',positive=True);A=41*s*s/6+S.Rational(3,2)/(s*s);der=S.diff(A,s)
    ck('uniform_squeeze_lower',der.subs(s,S.Rational(2,3))==-S.Rational(73,72))
    ck('uniform_squeeze_upper',der.subs(s,S.Rational(113,100))>S.Rational(40,3))
    ck('uniform_squeeze_convexity',S.simplify(S.diff(A,s,2)-(S.Rational(41,3)+9/s**4))==0)
    ck('edge_R_weight',all(F(n+1,2)+F(n,2)==n+F(1,2) for n in range(20)))
    ck('half_contrast_rho',rho(2,F(1,4),fault)==F(1204,45)*B(2))
    for i,(d,x) in enumerate(input_cases()):
        k=len(x)-1;eta=DMAX-abs(d)
        ck(f'admission_{i}',admissible(x,d,fault=fault))
        y,tail,alpha,before=repair(x,d,fault=fault)
        ck(f'caps_{i}',all(0<=v<=p(n) for n,v in enumerate(y)) and 0<=tail<=1)
        ck(f'contrast_{i}',contrast(y,tail)==d)
        ck(f'alpha_{i}',0<=alpha<=1 and alpha<=B(k)/(2*eta))
        if 0<alpha<=1 and cs[f'caps_{i}']:
            for j,(s1,s0) in enumerate([(F(2,3),F(113,100)),(F(1),F(1))]):
                e0=energy(x,F(1,2),s1,s0);e1=energy(y,tail,s1,s0)
                ck(f'energy_bound_{i}_{j}',e1[1]-e0[0]<=WIDTH*alpha)
    # Threshold is independently constrained and is not assumed to saturate.
    for label,x in [('high',[F(0),p(1),p(2)]),('low',input_cases()[9][1])]:
        if label=='low':
            d=F(1,2);h=d-B(2);lam=(h+DMAX)/(2*DMAX-B(2));x=[(1-lam)*p(0),lam*p(1),lam*p(2)]
        ck(label+'_threshold_admission',admissible(x,F(1,2),True,fault))
        y,c,alpha,old=repair(x,F(1,2),True,fault)
        ck(label+'_threshold_feasible',contrast(y,c)>=F(1,2))
        if label=='high':ck('high_threshold_no_repair',y==x and c==F(1,2) and alpha==0 and old>F(1,2))
        else:ck('low_threshold_repaired',alpha>0 and contrast(y,c)==F(1,2))
    r1=F(1,3)+F(1,8);r0=F(5,6)-r1;t1=F(7,24)+(F(1,24) if fault=='endpoint_coherence' else 0)
    ck('endpoint_moments',r1==F(11,24) and r0==F(3,8) and t1==F(7,24))
    eq=S.expand(72*s**3*(S.Rational(r1.numerator,r1.denominator)*der-S.Rational(40,3)*S.Rational(t1.numerator,t1.denominator)))
    ck('endpoint_polynomial',eq==451*s**4-280*s**3-99)
    ck('endpoint_zero_coherence_squeeze',S.simplify((der*s**3).subs(s**4,S.Rational(9,41)))==0)
    # Exact full-tail formula at the extremal step agrees with independent branch moments.
    ev=energy([F(0),p(1),p(2)],F(1),F(1),F(1));ex=r1*F(25,3)+r0*F(25,3)-F(40,3)*t1+F(35,18)
    ck('endpoint_energy_transfer',ev[0]<=ex<=ev[1] and ev[1]-ev[0]<F(1,10**40))
    for eps,k0,j0 in [(F(1,10**4),12,19),(F(1,10**6),16,25),(F(1,10**60),107,205)]:
        k,j,g=epsilon_plan(eps);ck('epsilon_'+str(eps),k==k0 and j==j0 and g<eps)
    return cs

FAULTS=['range_width','half_tail','repair_sign','extreme_direction','tail_mix','relaxed_width','threshold_direction','endpoint_coherence']
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    cs=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
    faults={}
    for f in FAULTS:
        bad=[n for n,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
    plans=[]
    for eps in [F(1,1000),F(1,10000),F(1,1000000),F(1,10**60)]:
        k,j,g=epsilon_plan(eps);plans.append(dict(epsilon=str(eps),K=k,bisections=j,real_variables=3*k+7,conditional_width_upper=str(g)))
    deps=['explorations/conditional-build/k2180-detector-contrast-frontier-2026-10-28.md','tests/channel-swings/k2178_effective_detector_approximation_probe.py','explorations/conditional-build/k2178-effective-detector-approximation-2026-10-28.md','explorations/conditional-build/k2174-joint-coherence-detector-2026-10-27.md']
    report=dict(result_id='K2180',status='conditional_exact_controls',checks=cs,fault_failures=faults,certificate=dict(epsilon_plans=plans,maximal_contrast=endpoint_certificate()),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written cap/convexity/compactness proofs independently reconstructed; finite exact controls and rigorous maximum-contrast root enclosure. Finite optimization at other contrasts not implemented; no apparatus energy claim.')
    dst=ROOT/'lab/process/k2180-detector-contrast-frontier.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report
    print(json.dumps(dict(result='K2180',checks=len(cs),faults_detected=len(faults),endpoint=report['certificate']['maximal_contrast']['meaning'])))
if __name__=='__main__':main()
