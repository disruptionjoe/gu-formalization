"""Independent full14-variable coefficient replay; no producer solver/reduction import."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from copy import deepcopy
import json,hashlib
from k1979_multicoordinate_symmetric_pairing_probe import data,decode
from k1967_paired_raw_coefficient_observation_probe import gamrow,mul,add,tr
ROOT=Path(__file__).resolve().parents[2]
FULL=(1<<14)-1
GROUPS=[list(range(1,7)),[7,8,9],[10,11,12,13]]
ZERO=(0,)*14

def cmul(a,b):
 sign=(-1)**sum((b&((1<<i)-1)).bit_count() for i in range(14) if a>>i&1)
 sign*=(-1)**((a&b)&(FULL^127)).bit_count()
 return a^b,sign

def tsign(mask):
 r=mask.bit_count();return (-1)**(r*(r-1)//2+(mask&(FULL^127)).bit_count())

def addterm(poly,ex,mask,value):
 if not value:return
 key=(ex,mask);poly[key]+=value
 if not poly[key]:del poly[key]

def lift(family,fault=None):
 out=defaultdict(F)
 for index,ex,value in family['terms']:
  v=F(value);mask=index%16
  xp=list(ZERO);xp[0]=ex[0]
  q={(tuple(xp),1 if mask&1 else 0):v}
  for g,axes in enumerate(GROUPS,1):
   odd=(mask>>g)&1;assert ex[g]>=odd and (ex[g]-odd)%2==0
   for _ in range((ex[g]-odd)//2):
    nxt=defaultdict(F)
    for (p,b),c in q.items():
     for k in axes:
      p2=list(p);p2[k]+=2;addterm(nxt,tuple(p2),b,c)
    q=nxt
   if odd:
    nxt=defaultdict(F)
    for (p,b),c in q.items():
     for k in axes:
      p2=list(p);p2[k]+=1;b2,s=cmul(b,1<<k);addterm(nxt,tuple(p2),b2,c*s)
    q=nxt
  if index>=16:
   nxt=defaultdict(F)
   for (p,b),c in q.items():
    b2,s=cmul(FULL,b);addterm(nxt,p,b2,c*s)
   q=nxt
  for (p,b),c in q.items():addterm(out,p,b,c)
 if fault=='certificate':
  key=next(iter(out));out[key]+=1
 return out

def raw_setup(fault=None):
 I,V,J,T,O=data();gam=[]
 for k in range(14):
  gam.append({(i,gamrow(k,i)[0]):F(gamrow(k,i)[1]) for i in range(128)})
 volume=I
 for g in gam:volume=mul(volume,g)
 assert volume==V,'actual ordered Clifford volume'
 X=mul({(j,i):1/v for (i,j),v in J[0].items()},gam[0])
 weights=[F(1) if k in [0,7,8,9] else F(-4,9) for k in range(14)]
 for k in range(14):assert mul(J[k],X)==add((((1 if k<7 else -1)*weights[k]),gam[k])),'actual raw transformed principal'
 assert mul(T,X)==add((-F(3,4),I),(-F(5,4),V)),'actual raw transformed target'
 pars=list(map(F,json.loads((ROOT/'lab/process/k1967-paired-raw-coefficient-observation.json').read_text())['scalar']['repair'][0]['parameters']))
 uv=[(pars[0],pars[2]) if k in [0,7,8,9] else (pars[1],pars[3]) for k in range(14)]
 for k in range(14):
  u,w=uv[k]
  assert tr(O[k])==mul(add((u,I),(w,V)),gam[k]),'actual coefficient transpose identity'
  for j in range(14):assert add((1,mul(gam[k],gam[j])),(1,mul(gam[j],gam[k])))==add(((2*(1 if k<7 else -1) if k==j else 0),I)),'full Clifford identity'
 if fault=='coefficient':uv[0]=(uv[0][0]+1,uv[0][1])
 return I,V,J,T,O,gam,X,weights,uv

def rstar_blade(mask,sign,weights,uv):
 parity=(-1)**mask.bit_count();alpha=F(3*sign,4);beta=F(5*sign,4)*parity
 for k,(u,w) in enumerate(uv):
  d=(1 if k<7 else -1)*parity*(-1 if mask>>k&1 else 1)
  alpha+=weights[k]*u*d;beta-=weights[k]*w*d
 comp,s=cmul(FULL,mask)
 return [(mask,alpha),(comp,beta*s)]

def verify_family(family,setup,fault=None):
 I,V,J,T,O,gam,X,weights,uv=setup;sign=family['sign']
 if fault=='mass_sign':sign=-sign
 Y=lift(family,fault);res=defaultdict(F)
 for (ex,mask),value in Y.items():
  for k in range(14):
   xp=list(ex);xp[k]+=1;bm,sgn=cmul(mask,1<<k)
   eta=1 if k<7 else -1
   if fault=='transpose' and k>=7:eta=1
   if tsign(bm)==1:addterm(res,tuple(xp),bm,value*weights[k]*eta*sgn)
  for bm,v in rstar_blade(mask,sign,weights,uv):
   if tsign(bm)==1:addterm(res,ex,bm,-value*v)
 assert dict(res)=={(ZERO,0):F(1)},'complete full14 polynomial matrix trace identity'
 # Verify universal algebraic adjoint formula directly on independent raw matrices
 # for every representative blade used, including adjoint invariance outside reduction.
 indices=sorted(set(index for index,ex,v in family['terms']))
 for index in indices:
  mask=sum(1<<k for b,k in enumerate([0,1,7,10]) if index%16>>b&1);c=F(1)
  if index>=16:mask,s=cmul(FULL,mask);c*=s
  A=I
  for k in range(14):
   if mask>>k&1:A=mul(A,gam[k])
  A=add((c,A));W=mul(A,tr(X))
  direct=add(*[((1 if k<7 else -1),mul(mul(O[k],W),tr(J[k]))) for k in range(14)],(-sign,mul(W,tr(T))))
  expect={}
  for bm,v in rstar_blade(mask,sign,weights,uv):
   B=I
   for k in range(14):
    if bm>>k&1:B=mul(B,gam[k])
   expect=add((1,expect),(c*v,B))
  assert direct==expect,'direct full raw adjoint with right transform'
 # Nonzero symmetric indefinite exact exponential (sign+) prevents an all-symmetric-zero overclaim.
 if family['sign']==1:
  G=mul(gam[0],gam[10]);A0=add((-3,G),(1,mul(V,G)));A1=add((F(23168,3267),gam[0]));lam2=F(54542565,67094528)
  def rawR(A):return add(*[((1 if k<7 else -1),mul(mul(tr(O[k]),A),J[k])) for k in range(14)],(-1,mul(A,T)))
  assert tr(A0)==A0 and tr(A1)==A1 and all(sum(A.get((i,i),F(0)) for i in range(128))==0 for A in [A0,A1])
  assert add((-lam2,mul(A1,J[10])))==rawR(A0)
  assert add((-1,mul(A0,J[10])))==rawR(A1)
 # Every represented Clifford monomial is a signed permutation with128 unit entries.
 # C_alpha=Y_alpha X^T. Triangle bound for its entrywise1-norm uses column sums of X.
 xbound=max(sum(abs(v) for (i,j),v in X.items() if j==k) for k in range(128))
 bound=128*xbound*sum(abs(v) for v in Y.values())
 # Genuine contrary controls: the existing full positive first jets solve only value equation.
 prior=json.loads((ROOT/'lab/process/k1979-multicoordinate-symmetric-pairing.json').read_text())['families']
 jets=next(f for f in prior if f['sign']==family['sign'])
 raw=add(*[((1 if k<7 else -1),mul(mul(tr(O[k]),I),J[k])) for k in range(14)],(-family['sign'],mul(I,T)))
 assert add(*[((1 if k<7 else -1),mul(decode(h),J[k])) for k,h in enumerate(jets['identity_first_jets'])])==raw
 return dict(sign=family['sign'],expanded_terms=len(Y),polynomial_coefficients=len(set(ex for ex,mask in Y)),raw_adjoint_blades=len(indices),raw_residual_dual_entry1_bound=str(bound),identity_residual_derivative_floor=str(F(128)/bound))

def check(report,fault=None):
 setup=raw_setup(fault);return [verify_family(f,setup,fault) for f in report['families']]
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2002-clifford-pairing-integrability.json').read_text());result=check(r);caught=[]
 for fault in ['certificate','mass_sign','transpose','coefficient']:
  try:check(r,fault)
  except AssertionError:caught.append(fault)
  else:raise AssertionError('undetected mathematical fault '+fault)
 print('PASS K2002 independent full14 coefficient identity:',json.dumps(result),'; rejected',caught)
