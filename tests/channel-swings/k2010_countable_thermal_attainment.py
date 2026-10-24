"""Exact controls; universal compactness/attainment is proved in the note."""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
import argparse, json, hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2010-countable-thermal-attainment.json'

def rate(s,p,t):
    inc=[F(0) for _ in p];z=sum(t**b for b in range(4))
    for i,j in combinations(range(len(s)),2):
        g=s[j]-s[i]
        if g in (1,2,3):
            g=int(g);L=sum(t**b for b in range(4-g))/z
            f=L*(p[j]-t**g*p[i]);inc[i]+=max(f,0);inc[j]+=max(-f,0)
    return sum((max(p[i]-inc[i],0) for i in range(len(p))),F(0))/2

def shells(a,s):
    return all(2*sum(e-x in (0,1,2,3) for x in s)<=sum(e-x in (0,1,2,3) for x in a)
               for e in {x+b for x in s for b in range(4)})

def check(a,s,p,t,delta,E):
    assert a[0]==0 and all(y-x>=delta for x,y in zip(a,a[1:])), 'spectrum/gap'
    assert len(set(a))==len(a) and set(s)<=set(a) and shells(a,s), 'shell completion'
    assert sum(p)==1 and all(x>=0 for x in p), 'probability normalization'
    assert sum(x*y for x,y in zip(s,p))<=E, 'energy budget'
    return rate(s,p,t)

def produce():
    merges=[];tails=[];geo=[];margins=[];prices=[]
    for t in (F(1,3),F(1,2),F(3,4)):
      for w in (F(1,5),F(1,2),F(4,5)):
        target=check(list(map(F,range(6))),[F(1),F(4)],[w,1-w],t,F(1),F(4))
        for n in (2,5,11):
          x=3+F(1,n);a=sorted([F(0),F(1),F(2),x,x+1,x+2]);s=[F(1),x+1]
          old=check(a,s,[w,1-w],t,F(1),F(5))
          assert target<=old==F(1,2)
          merges.append(dict(t=t,w=w,n=n,old=old,limit=target))
    for n in (4,8,16,32):
      x=F(n+3);q=F(1,n);a=[F(0),F(1),F(2),x,x+1,x+2];s=[F(1),x+1]
      r=check(a,s,[1-q,q],F(1,2),F(1),F(3));mean=sum(v*p for v,p in zip(s,[1-q,q]))
      assert mean==2+3*q and r==F(1,2)
      # Index and absolute-energy tail estimates, independent of moment convergence.
      for m in range(1,6):
        mass=sum((p for v,p in zip(s,[1-q,q]) if a.index(v)>=m),F(0))
        assert mass<=mean/F(m)
      tails.append(dict(n=n,tail=q,mean=mean,l1_to_limit=2*q))
    for t in (F(1,3),F(1,2),F(3,4)):
      for r in (F(1,4),F(1,2),F(3,4)):
        Z=sum(t**b for b in range(4));L=(1+t)/Z
        if r>=t*t:exact=(1-L*(r-t*t))/2
        else:exact=(1-r+max(r-L*(t*t-r),F(0)))/2
        for k in (4,8,12):
          s=[F(2*i+1) for i in range(k)];a=list(map(F,range(2*k+1)))
          p=[(1-r)*r**i/(1-r**k) for i in range(k)];E=(1+r)/(1-r)
          finite=check(a,s,p,t,F(1),E)
          assert abs(finite-exact)<=r**k/(1-r**k)
          geo.append(dict(t=t,r=r,k=k,finite=finite,infinite=exact,tail=r**k))
    for s in (F(8),F(81,10),F(9),F(20)):
      c=F(3,20)*s-F(63,100)-F(1,2);assert c>=F(7,100)
      margins.append(dict(energy=s,coefficient=c))
    for lam in (F(1,100),F(1,20),F(3,20)):
      N=(1+1/lam).__floor__()+1;offset=F(N+6);q=F(1,10000)
      a=list(map(F,range(5)))+[offset,offset+1,offset+2];support=[F(1),F(3),offset+1]
      populations=[(1-q)*F(2,5),(1-q)*F(3,5),q];mean=sum(x*p for x,p in zip(support,populations));t=F(1,2)
      before=check(a,support,populations,t,F(1),mean)+lam*mean;B=F(1,2)+lam
      final=rate([F(1),F(3)],[F(2,5),F(3,5)],t)+lam*F(11,5)
      bound=q*(B+F(1,2)-lam*N)/(1-q)
      assert before<=B and mean<N and final-before<=bound<0
      prices.append(dict(price=lam,N=N,remote_offset=offset,tail=q,before=before,after=final,difference_upper=bound,dimension_bound=2*N+7))
    inputs=['explorations/conditional-build/k2008-effective-thermal-dimension-approximation-2026-10-24.md','explorations/conditional-build/k1950-global-catalyst-energy-certificates-2026-10-22.md','lab/process/k1950-global-catalyst-energy-certificates.json','explorations/conditional-build/k2006-uniform-two-component-spacing-2026-10-24.md']
    return dict(result_id='K2010',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',resonance_mergers=merges,escaping_energy=tails,geometric_limits=geo,strict_tail_margins=margins,positive_price_transfers=prices,counts={'merger_protocols':len(merges),'escaping_sequences':len(tails),'geometric_prefixes':len(geo),'tail_coefficients':len(margins),'positive_price_transfers':len(prices)},scope='Proof-backed finite-or-countable attainment and strict all-dimension fixed-spacing exposed-line gap; finite arithmetic controls are not universal proofs; no finite optimizer, gap value, sharp rate or GU claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,list):return [encode(v) for v in x]
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    return x
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=encode(produce())
    if args.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text())
    print('PASS K2010 exact controls',d['counts'])
