#!/usr/bin/env python3
"""Effective detector tail bounds, exact repair and error budgets; no optimization."""
from fractions import Fraction as F
from math import isqrt

Z=F(1,4); C=F(40,3); SLO=F(2,3); SHI=F(113,100)
PREC=10**45
def sqrt_iv(x,prec=PREC):
    assert x>=0
    a=isqrt(x.numerator*prec*prec//x.denominator)
    return F(a,prec),F(a+1,prec)
def ivadd(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,b):return (a*b[0],a*b[1]) if a>=0 else (a*b[1],a*b[0])
def point(x):return x,x
def p(n):return F(3,4)*Z**n
def A(s):return F(41,6)*s*s+F(3,2)/(s*s)
def B(k):return 3*(k+1)*Z**(k+1)
def D(k):return (F(k)+F(11,6))*Z**(k+1)
def H(k):return (F(k)+F(4,3))*Z**k/2
def tau(k):return 4*D(k)+F(452,15)*H(k)
def rho_iv(k,prec=PREC):return ivadd(point(F(2453,45)*B(k)),scale(F(452,15),sqrt_iv(F(3,32)*B(k),prec)))
def total_gap_iv(k,j,prec=PREC):return ivadd(point(tau(k)+F(15,2**j)),rho_iv(k,prec))
def contrast(x,c):
    k=len(x)-1
    return sum((3*n-1)*v for n,v in enumerate(x))+c*B(k)
def admissible(x,k,fault=None):
    h=sum((3*n-1)*v for n,v in enumerate(x))
    low=F(1,2)-B(k)*(F(1,2) if fault=='head_endpoint' else 1)
    return all(0<=v<=p(n) for n,v in enumerate(x)) and low<=h<=F(1,2)
def repair(x,fault=None):
    k=len(x)-1;t=(1 if fault=='repair_margin' else 4)*B(k)
    u=[(1-t)*v+t*p(n)*(F(1,6) if n==0 else F(5,6)) for n,v in enumerate(x)]
    c=F(1,2)+t/3
    delta=contrast(u,c)-F(1,2)
    u[0]+=(-delta if fault=='repair_sign' else delta)
    return u,c,t,delta
def energy(x,c,s1,s0,fault=None):
    k=len(x)-1
    w=sum(x)+c*Z**(k+1)
    m=sum(n*v for n,v in enumerate(x))+c*Z**(k+1)*(k+1+(F(0) if fault=='tail_mean' else F(1,3)))
    out=point((m+w/2)*A(s1)+(F(1,3)-m+(1-w)/2)*A(s0)+F(35,18))
    for vals,tail,s in [(x,c,s1),([p(n)-v for n,v in enumerate(x)],1-c,s0)]:
        tt=point(tail*H(k+1)*(2 if fault=='tail_coherence' else 1))
        for n in range(k+1):
            nxt=vals[n+1] if n<k else tail*p(k+1)
            tt=ivadd(tt,scale(n+1,sqrt_iv(vals[n]*nxt)))
        out=ivadd(out,scale(-C*s,tt))
    return out
def cases():
    k=2;out=[]
    for h in [F(1,2)-B(k),F(1,2)]:
        out.append([sum((3*n-1)*p(n) for n in range(1,k+1))-h,p(1),p(2)])
        out.append([F(0),(h-5*p(2))/2,p(2)])
    return out
def controls(fault=None):
    ans={}
    for k in [2,9,16,20]:
        # Tail identities from closed geometric sums, separately differentiated.
        q=Z**(k+1);tail_mass=q;tail_mean=q*(k+1+Z/(1-Z))
        ans[f'contrast_tail_{k}']=3*tail_mean-tail_mass==B(k)
        ans[f'radius_tail_{k}']=tail_mean+tail_mass/2==D(k)
        edge=F(1,2)*F(3,4)*Z**k*((k+1)/(1-Z)+Z/(1-Z)**2)
        ans[f'edge_tail_{k}']=edge==H(k)
        ans[f'mix_fraction_{k}']=0<4*B(k)<1
    ans['squeeze_bounds']=all(6<A(s)<10 for s in [SLO,SHI]) and 41>36
    ans['range_constant']=F(185,18)-F(-31,10)==F(602,45)
    ans['repair_constant']=4*F(602,45)+1==F(2453,45)
    for i,x in enumerate(cases()):
        ans[f'admission_{i}']=admissible(x,2,fault)
        y,c,t,d=repair(x,fault)
        ans[f'repair_feasible_{i}']=all(0<v<p(n) for n,v in enumerate(y)) and 0<c<1
        ans[f'repair_contrast_{i}']=contrast(y,c)==F(1,2)
        if ans[f'repair_feasible_{i}']:
            for j,(s1,s0) in enumerate([(SLO,SHI),(SHI,SLO),(F(1),F(1))]):
                before=energy(x,F(1,2),s1,s0,fault);after=energy(y,c,s1,s0,fault)
                ans[f'repair_energy_{i}_{j}']=after[1]-before[0]<rho_iv(2)[1]
    for k in [2,9]:
        x=[p(n)/2 for n in range(k+1)]
        e=energy(x,F(1,2),F(1),F(1),fault)
        ans[f'constant_zero_energy_{k}']=e[0]<=0<=e[1] and e[1]-e[0]<F(1,10**40)
        c=F(1,3);x=[c*p(n) for n in range(k+1)]
        e=energy(x,c,SLO,SHI,fault)
        exact=F(5,6)*(c*A(SLO)+(1-c)*A(SHI))-C*F(2,3)*(c*SLO+(1-c)*SHI)+F(35,18)
        ans[f'constant_asymmetric_energy_{k}']=e[0]<=exact<=e[1] and e[1]-e[0]<F(1,10**40)
    ans['k20_epsilon']=total_gap_iv(20,18)[1]<F(1,10000)
    ans['k16_epsilon']=total_gap_iv(16,15)[1]<F(1,1000)
    return ans
def epsilon_plan(eps):
    assert eps>0
    precision_ratio=F(1000)/eps
    prec=max(PREC,-(-precision_ratio.numerator//precision_ratio.denominator))
    k=2
    while tau(k)+rho_iv(k,prec)[1]>eps/2:k+=1
    j=0
    while F(15,2**j)>eps/2:j+=1
    return k,j,total_gap_iv(k,j,prec)[1]

from pathlib import Path
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 cs=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
 faults={}
 for fault in FAULTS:
  bad=[n for n,v in controls(fault).items() if not v];assert bad,('undetected',fault);faults[fault]=bad
 extra={'epsilon_plans':[],'conditional_widths':[]}
 for eps in [F(1,1000),F(1,10000),F(1,1000000),F(1,10**60)]:
  k,j,g=epsilon_plan(eps);assert g<eps
  extra['epsilon_plans'].append(dict(epsilon=str(eps),K=k,bisections=j,real_variables=3*k+7,width_upper=str(g)))
 for k,j in [(16,15),(20,18)]:
  extra['conditional_widths'].append(dict(K=k,bisections=j,tau=str(tau(k)),rho_interval=list(map(str,rho_iv(k))),width_upper=str(total_gap_iv(k,j)[1])))
 deps=['explorations/conditional-build/k2178-effective-detector-approximation-2026-10-28.md', 'explorations/conditional-build/k2176-detector-certified-convergence-2026-10-27.md', 'explorations/conditional-build/k2174-joint-coherence-detector-2026-10-27.md']
 report=dict(result_id='K2178',status='conditional_exact_controls',checks=cs,fault_failures=faults,certificate=extra,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written proof independently reconstructed; finite formula controls supplement rather than replace universal acceptance. No proof-assistant, physical quotient or apparatus cost claim.')
 dst=ROOT/'lab/process/k2178-effective-detector-approximation.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2178',checks=len(cs),faults=faults)))
FAULTS=['repair_sign', 'repair_margin', 'head_endpoint', 'tail_mean', 'tail_coherence']
if __name__=='__main__':main()
