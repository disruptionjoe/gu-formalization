"""Directed tail deletion and sharp unrestricted thermal onset, exact controls.

Universal claims use the accompanying proof and the existing complete K2015
low-support certificate. Physical samples check transfers, not universality.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse, json, hashlib
from k2014_unrestricted_ten_level_onset import witness, G, B
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2017-sharp-unrestricted-thermal-transition.json'
A=Q(6,5);Z=Q(11,5);D=Q(4,15)
def encode(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def sharp(s,p,t):
    inc=[Q(0)]*len(s);z=sum(t**j for j in range(4))
    for i in range(len(s)):
      for j in range(i+1,len(s)):
        d=s[j]-s[i]
        if d in (1,2,3):
          d=int(d);lo=sum(t**k for k in range(4-d))/z;v=t**d*lo*p[i]-lo*p[j]
          inc[i]+=max(-v,0);inc[j]+=max(v,0)
    return sum(max(x-y,0) for x,y in zip(p,inc))/2

def deletion_case(s,p,t,N):
    q=sum(x for a,x in zip(s,p) if a>N);h=sum(a*x for a,x in zip(s,p) if a>N)
    e=sum(a*x for a,x in zip(s,p));rr=sharp(s,p,t)
    pp=[x if a<=N else Q(0) for a,x in zip(s,p)];rl=sharp(s,pp,t)
    boundary=sum(sum(t**j for j in range(4-int(b-a)))/sum(t**j for j in range(4))*p[k]/2
       for i,a in enumerate(s) for k,b in enumerate(s) if a<=N<b and b-a in (1,2,3))
    C=sum(t**j for j in range(3))/(2*sum(t**j for j in range(4)))
    assert rl<=rr+boundary<=rr+C*q
    assert q<1 and sum(pp)==1-q
    ss=[a for a in s if a<=N];low=[x/(1-q) for a,x in zip(s,pp) if a<=N]
    assert sharp(ss,low,t)==rl/(1-q)
    spectrum=sorted({Q(k)+a-int(a) for a in s for k in range(int(a)+4)})
    # Full integer completion for each congruence class preserves every shell.
    return dict(support=s,populations=p,spectrum=spectrum,t=t,cutoff=N,return_value=rr,
       tail_mass=q,tail_energy=h,mean=e,unnormalized_low_return=rl,boundary_loss=boundary,coarse_loss_coefficient=C,
       low_support=ss,low_populations=low,low_spectrum=[a for a in spectrum if a<=N+3])

def kappa(d,E):return Q(3,20)/(1+d)*(9-E)-G(d,E)-Q(7,15)
def produce():
    prior=json.loads((ROOT/'lab/process/k2015-finite-thermal-ray-separation.json').read_text())
    assert Q(prior['census']['compatible_interval_certificate']['delta_max'])==D
    cases=[]
    # Long paths exercise multiple incoming edges, deficit clipping and tail crossings.
    for ds in [(2,2,2,2,2,2),(1,3,1,3,1,3),(3,1,3,1,3,1),(3,3,3,3),(2,3,2,3,2)]:
      s=[Q(max(1,3-ds[0]))]
      for d in ds:s.append(s[-1]+d)
      for t in [Q(1,4),Q(1,2),Q(3,4)]:
       for mode in range(4):
        w=[Q(1) if mode==0 else Q((i+1)**2) if mode==1 else Q(9)**(-i) if mode==2 else Q(3)**i for i in range(len(s))];p=[x/sum(w) for x in w]
        for N in sorted(set([int(s[1]),9,int(s[-2])])):
         if N>=s[-1]:continue
         cases.append(deletion_case(s,p,t,N))
    # Disconnected classes, with occupied energies crossing one common cutoff.
    for t in [Q(1,4),Q(1,2),Q(3,4)]:
      s=[Q(1),Q(6,5),Q(3),Q(16,5),Q(10),Q(51,5),Q(12),Q(61,5)];w=[81,81,9,9,3,3,1,1];p=[Q(x,sum(w)) for x in w]
      cases.append(deletion_case(s,p,t,9))
    witnesses=[];algebra=[]
    for d in [Q(1,1000),Q(1,15),Q(1,5),D]:
      for E in [A+Q(1,10**6),Q(113,91),Q(3,2),Q(17,10)+d/2,Q(2),Z-Q(1,10**6)]:
        w=witness(d,E,'B' if E-A<=(1+d)/2 else 'A');assert w['return_value']==G(d,E)
        kap=kappa(d,E);assert kap>=Q(2,285)
        w['certified_global_optimum']=True;w['tail_mass_per_return_error']=1/kap;w['tail_energy_per_return_error']=9/kap
        w['bath_TV_gap_radius']=(G(d,E)-B(E))/2;witnesses.append(w)
        # Includes retained budgets below A, eliminating the former prebound.
        for q in [Q(0),(E-A)/(9-A), (E-1)/8]:
          x=(E-9*q)/(1-q);f=B(x) if x<=A else G(d,x);m=Q(3,20)/(1+d)
          assert x>=1 and f>=G(d,E)+m*(E-x)
          assert (1-q)*f-Q(7,15)*q>=G(d,E)+kap*q
          algebra.append(dict(delta=d,energy=E,tail_mass=q,retained_budget=x,lower_return=(1-q)*f-Q(7,15)*q,kappa=kap))
    # Exact worst-parameter rational identity: no sampling substitutes for it.
    assert Q(3,20)/(1+D)*(9-A)-Q(9,20)-Q(7,15)==Q(2,285)
    inputs=['lab/process/k2015-finite-thermal-ray-separation.json','explorations/conditional-build/k1943-arbitrary-preparation-catalyst-energy-2026-10-22.md','explorations/conditional-build/k2008-effective-thermal-dimension-approximation-2026-10-24.md','explorations/conditional-build/k2012-thermal-duality-gap-and-bath-stability-2026-10-24.md']
    return encode(dict(result_id='K2017',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',sharp_uniform_endpoint=D,uniform_tail_coefficient=Q(2,285),physical_deletions=cases,optimal_witnesses=witnesses,secant_controls=algebra,counts=dict(physical_deletions=len(cases),optimal_witnesses=len(witnesses),secant_controls=len(algebra)),scope='Exact finite-or-countable independent thermal class at t=1/2; no GU identification, all-spacing frontier or novelty claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text()),'certificate drift'
    print('PASS K2017',r['counts'])
