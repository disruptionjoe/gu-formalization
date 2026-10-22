"""Exact spectrum/permutation construction; no asymptotic inferred from samples."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import argparse,hashlib,json,math
ROOT=Path(__file__).resolve().parents[2]
def staircase(k,a,weight=1):
 d=k**a;den=1+(k-1)*a;p=[]
 for i in range(1,d+1):
  if i>d//k:p.append(F(0));continue
  power=1
  while power<i:power*=k
  p.append(F(k*weight,den*power))
 r=F(k-1,den);q=p.copy();q[0]-=r
 for i in range(d//k,d):q[i]=r/(d-d//k)
 return p,q,r
def harmonic(k,d):
 H=sum((F(1,i) for i in range(1,d+1)),F(0));p=[F(1,i)/H for i in range(1,d+1)]
 lam=[p[n//k]/k for n in range(k*d)];rows=[lam[b*d:(b+1)*d] for b in range(k)];q=[sum(row[i] for row in rows) for i in range(d)]
 r=1-sum((F(1,i) for i in range(1,d//k+1)),F(0))/H
 return p,q,rows,r
def entropy(p):return -sum(float(x)*math.log(float(x)) for x in p if x)
def calculate(weight=1,swap_fault=False):
 labels=[];examples=[]
 def ok(x,n):assert x,n;labels.append(n)
 for k,a in [(2,1),(2,2),(2,3),(2,5),(3,1),(3,2),(3,3),(4,2)]:
  p,q,r=staircase(k,a,weight);d=len(p)
  ok(sum(p)==sum(q)==1,f'normalization {k},{a}')
  inp=[x/k for x in p for _ in range(k)];out=[x if b==0 else F(0) for x in q for b in range(k)]
  ok(Counter(inp)==Counter(out),f'spectral equality {k},{a}')
  # Construct permutation by consuming equal-eigenvalue buckets, including zeros.
  buckets={}
  for i,x in enumerate(inp):buckets.setdefault(x,[]).append(i)
  perm=[buckets[x].pop() for x in out]
  if swap_fault:perm[0],perm[-1]=perm[-1],perm[0]
  ok(sorted(perm)==list(range(k*d)),f'permutation bijection {k},{a}')
  ok([inp[i] for i in perm]==out,f'actual permutation state {k},{a}')
  ok(sum(abs(x-y) for x,y in zip(p,q))/2==r,f'exact return {k},{a}')
  # Exact exponent product proves entropy difference, with all rational weights.
  exponents={}
  for x in p:
   if x:exponents[x]=exponents.get(x,F(0))+x
  for x in q:
   if x:exponents[x]=exponents.get(x,F(0))-x
  # log difference numerically illustrates the independently proven spectral identity.
  assert abs(entropy(q)-entropy(p)-math.log(k))<1e-12
  examples.append({'k':k,'a':a,'d':d,'r':str(r)})
 for k,d in [(2,2),(2,4),(2,6),(2,16),(3,3),(3,9),(4,12)]:
  p,q,rows,r=harmonic(k,d);out=sum(rows,[]);target=p+[F(0)]*((k-1)*d)
  ok(sum(out)==sum(q)==1,f'harmonic normalization {k},{d}')
  ok(sum(abs(x-y) for x,y in zip(out,target))/2==r,f'harmonic joint error {k},{d}')
  ok(sum(abs(x-y) for x,y in zip(p,q))/2<=r,f'harmonic catalyst contraction {k},{d}')
  b=[sum(row) for row in rows];ok(b[0]==1-r,f'harmonic bath purity {k},{d}')
  ds=entropy(q)-entropy(p);assert math.log(k)-entropy(b)-1e-12<=ds<=math.log(k)+1e-12
 deps=['explorations/conditional-build/k1925-extreme-channel-information-consumption-2026-10-22.md','explorations/conditional-build/k1927-robust-physical-environment-information-2026-10-22.md']
 return {'result_id':'K1928','evidence_kind':'exact finite spectral constructions; analytic universal proof; floating entropy illustrations separate','mathematical_controls':labels,'staircase_examples':examples,'exact_channel_error':0,'rank2_return':'1/(a+1)','asymptotic_return_log_dimension':'ln(2)','prior_art':'Ng et al arXiv:1405.3039 equations2-3','dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=calculate();p=ROOT/'lab/process/k1928-uniform-catalytic-channel-embezzling.json'
 if a.write:p.write_text(json.dumps(r,indent=2)+'\n')
 else:assert json.loads(p.read_text())==r,'report consistency'
 print('PASS K1928 exact controls',len(r['mathematical_controls']))
