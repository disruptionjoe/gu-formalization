"""Separate column-action tensor reconstruction; imports no producer code."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
N=1920;eta=[1]*7+[-1]*7

def gam(k,j):
 b=k%7;mask=1<<(6-b);s=(-1)**(j>>(7-b)).bit_count()
 if k>=7:s*=1 if j&mask else -1
 return j^mask,s

def word(ks,j):
 s=1
 for k in reversed(ks):j,t=gam(k,j);s*=t
 return j,s

def ident():return [{j:Q(1)} for j in range(N)]
def plus(a,b,c=1):
 out=[]
 for aa,bb in zip(a,b):
  d=aa.copy()
  for i,v in bb.items():d[i]=d.get(i,Q(0))+c*v
  out.append({i:v for i,v in d.items() if v})
 return out

def scale(a,c):return [{i:c*v for i,v in col.items() if c*v} for col in a]
def compose(a,b):
 out=[]
 for col in b:
  d={}
  for k,v in col.items():
   for i,w in a[k].items():d[i]=d.get(i,Q(0))+v*w
  out.append({i:v for i,v in d.items() if v})
 return out

def transpose(a):
 b=[{} for _ in range(N)]
 for j,col in enumerate(a):
  for i,v in col.items():b[i][j]=v
 return b

def empty(a):return all(not c for c in a)
def hmatrix():
 h=[]
 for j in range(N):
  c,k=divmod(j,128);r,s=word(tuple(range(7,14)),k);h.append({128*c+r:Q(s*(eta[c] if c<14 else 1))})
 return h

def dmatrix(k,wrong_lower=False,wrong_weight=False):
 cols=[]
 for j in range(N):
  c,b=divmod(j,128);z={}
  if c==14:z[128*k+b]=Q(1)
  else:
   _,vol=word(tuple(range(14)),b);w=Q(3+(vol if wrong_weight else -vol),2)
   if c==k:z[1792+b]=Q(eta[c] if wrong_lower else -eta[c])
   for r in range(14):
    if r!=k and c not in [r,k]:
     i,s=word((r,k,c),b);z[128*r+i]=eta[r]*s*w
  cols.append(z)
 return cols

def cmat(x,derivative=False):
 c=[]
 for j in range(N):
  if j<1792:c.append({} if derivative else {j:Q(1)})
  else:
   b=j-1792;r,s=gam(7,b)
   z={1792+r:Q(s)*(1 if derivative else x)}
   if not derivative:
    r,s=gam(0,b);z[1792+r]=z.get(1792+r,Q(0))+s
   c.append({i:v for i,v in z.items() if v})
 return c

def run():
 h=hmatrix();assert h==transpose(h);count=0
 for k in range(14):
  d=dmatrix(k);hd=compose(h,d);assert empty(plus(hd,transpose(hd)));count+=1
  # Real wrong lower sign must fail every direction.
  bad=compose(h,dmatrix(k,wrong_lower=True));assert not empty(plus(bad,transpose(bad)))
 for x in [Q(1,3),Q(-2,5)]:
  c=cmat(x);cp=cmat(x,True);r=compose(transpose(c),h);rp=compose(transpose(cp),h);d=dmatrix(7)
  s=compose(r,compose(d,c));t=compose(r,compose(d,plus(cp,c)))
  ds=plus(scale(s,2),plus(compose(rp,compose(d,c)),compose(r,compose(d,cp))))
  assert empty(plus(plus(t,transpose(t),-1),ds,-1));count+=1
  for missing in [compose(r,compose(d,c)),compose(r,compose(d,cp))]:assert not empty(plus(plus(missing,transpose(missing),-1),ds,-1))
  # Full half-support check from tensor volume, without the producer's matrices.
  for k in range(14):
   z=compose(r,compose(dmatrix(k),c))
   for j,col in enumerate(z):
    sj=word(tuple(range(14)),j%128)[1]
    assert all(word(tuple(range(14)),i%128)[1]==sj for i in col)
   count+=1
 report=json.loads((ROOT/'lab/process/k2021-common-degree-dual-operator.json').read_text())
 for p,d in report['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d
 print('PASS K2021 separate tensor action',count,'complete identities; 18 actual sign/derivative/density faults; 3 provenance hashes')
if __name__=='__main__':run()
