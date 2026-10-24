"""Exact physical tail-transfer consumers; universal criterion is proved in note."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from k2010_countable_thermal_attainment import rate,shells
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2013-energy-sensitive-thermal-cutoff.json'
LAM,A=F(3,20),F(63,100)
def mean(s,p):return sum((x*y for x,y in zip(s,p)),F(0))
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,list):return [encode(v) for v in x]
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    return x

def case(a,s,p,t,N):
    E=mean(s,p);assert E<N and shells(a,s) and sum(p)==1
    q=sum((v for x,v in zip(s,p) if x>N),F(0));h=sum((x*v for x,v in zip(s,p) if x>N),F(0))
    ls=[x for x in s if x<=N];lp=[v/(1-q) for x,v in zip(s,p) if x<=N];la=[x for x in a if x<=N+3]
    ep=(E-N*q)/(1-q);actual=mean(ls,lp);before=rate(s,p,t);after=rate(ls,lp,t)
    assert h>=N*q and actual==(E-h)/(1-q)<=ep<=E
    assert ep>=1 and shells(la,ls) and len(la)<=2*N+7
    assert after<=before+q/(1-q)
    c=LAM*N-A-F(1,2)
    if t==F(1,2):assert c*q<=before-(A-LAM*E)
    return dict(spectrum=a,support=s,populations=p,t=t,N=N,energy=E,tail=q,tail_energy=h,low_spectrum=la,low_support=ls,low_populations=lp,energy_bound=ep,low_energy=actual,before=before,after=after,tail_coefficient=c)

def produce():
    rows=[]
    for t in [F(1,3),F(1,2),F(3,4)]:
      for ratio in [F(1,10),F(1,4),F(1,2)]:
       s=[F(2*i+1) for i in range(20)];a=list(map(F,range(41)));p=[(1-ratio)*ratio**i/(1-ratio**20) for i in range(20)]
       for N in [8,9,13,20]:rows.append(case(a,s,p,t,N))
    # Fractional coset pair, actual energy cost and positive minimum spacing.
    for delta in [F(1,20),F(1,4),F(1,2)]:
      for q in [F(1,10000),F(1,1000),F(1,100)]:
       a=list(map(F,range(5)))+[F(15)+delta,F(16)+delta,F(17)+delta]
       rows.append(case(a,[F(1),F(3),F(16)+delta],[(1-q)*F(9,10),(1-q)*F(1,10),q],F(1,2),13))
    consumers=[]
    for k in range(1,20):
      E=F(6,5)+F(k,20);kap=(3-E)/10
      assert kap>F(2,25) and F(1,10)*(13-E)-1==kap
      for eps in [F(0),F(1,10000),F(1,100)]:
       q=eps/(kap+eps);assert kap*q/(1-q)==eps
       consumers.append(dict(energy=E,epsilon=eps,kappa=kap,tail_upper=q))
    inputs=['explorations/conditional-build/k2008-effective-thermal-dimension-approximation-2026-10-24.md','explorations/conditional-build/k1950-global-catalyst-energy-certificates-2026-10-22.md','tests/channel-swings/k2010_countable_thermal_attainment.py']
    return encode(dict(result_id='K2013',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',physical_cases=rows,near_optimizer_consumers=consumers,counts={'physical_tail_transfers':len(rows),'conditional_tail_consumers':len(consumers)},scope='Universal energy-sensitive truncation and sufficient local-slope finite-attainment criterion by written proof. Physical examples are exact; near-optimizer numbers require the stated global finite-value/slope premises. No global threshold evaluated.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=produce()
    if args.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text())
    print('PASS K2013',d['counts'])
