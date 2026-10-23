"""Rational whole-strip point evaluation of actual continuum pulse iterates."""
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import argparse,json,hashlib
from k1969_scalar_continuum_separation import isolate,ip,iv,K,D,P,poly
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1983-certified-continuum-pulse-evaluation.json';M=F(23,100);G=M
TL,TR=isolate();T=(TL+TR)/2;LL,LR=iv(ip(D,(TL,TR)),ip(K,(TL,TR)));LAM=(LL+LR)/2
DG=F(2,9)*((LR-LL)/4+F(7,100)*(TR-TL)/2)
def polyint(c,x):return sum(a*x**(i+1)/(i+1) for i,a in enumerate(c))
PIECES=[(F(0),T,[0,-1+LAM*(1-T)**2/2]),(T,F(1),[-LAM*T*T/2,-1+LAM*(1+T*T)/2,-LAM/2]),(F(1),F(2),[-1]),(F(2),F(3),[-3-3*LAM,1+5*LAM/2,-LAM/2])]
def phi(x):
 if x<0:return -phi(-x)
 for a,b,c in PIECES:
  if x<=b:return sum(v*x**i for i,v in enumerate(c))
 raise ValueError('phase domain')
def primitive(x):
 x=abs(x);return sum(polyint(c,min(x,b))-polyint(c,a) for a,b,c in PIECES if x>a)
def g(u):return F(2,9)*phi(u)
def bounds(z):return max(F(-3),z-9),min(F(3),z)
def avg(z):
 a,b=bounds(z)
 return g(a) if a==b else F(2,9)*(primitive(b)-primitive(a))/(b-a)
def clip(v):return max(-M,min(M,v))
def midpoint(fun,a,b,n):return sum(fun(a+(b-a)*F(2*i+1,2*n)) for i in range(n))/n
@lru_cache(None)
def evaluate(k,u,z,eps,n):
 assert -3<=u<=3 and u<=z<=u+9 and eps>0 and n>0 and k>=0
 a=2+eps
 if k==0:return F(0)
 if k==1:return g(u)/a
 if k==2:return ((a+1)*g(u)-avg(z))/(a*a)
 if k==3:return clip(((a*a+a+1)*g(u)+midpoint(avg,u,u+9,n)-(a+2)*avg(z))/a**3)
 p=midpoint(lambda w:evaluate(k-1,u,w,eps,n),u,u+9,n);l,h=bounds(z)
 q=midpoint(lambda w:evaluate(k-1,w,z,eps,n),l,h,n)
 return clip((2*evaluate(k-1,u,z,eps,n)-p-q+g(u))/a)
def lipschitz(k,eps):
 U=Z=F(0);a=2+eps
 for _ in range(k):U,Z=(3*U+Z+G)/a,(U+3*Z)/a
 return U,Z
def error(k,eps,n):
 a=2+eps
 if k==0:return F(0)
 if k==1:return DG/a
 if k==2:return (a+2)*DG/a**2
 if k==3:return ((a*a+2*a+4)*DG+9*G/(4*n))/a**3
 U,Z=lipschitz(k-1,eps)
 return (4*error(k-1,eps,n)+(9*Z+6*U)/(4*n)+DG)/a
def configure(bits=96):
 global TL,TR,T,LL,LR,LAM,DG,PIECES
 assert bits>=16
 TL,TR=F(9,20),F(23,50)
 for _ in range(bits):
  mid=(TL+TR)/2
  if poly(P,mid)<0:TL=mid
  else:TR=mid
 T=(TL+TR)/2;LL,LR=iv(ip(D,(TL,TR)),ip(K,(TL,TR)));LAM=(LL+LR)/2
 DG=F(2,9)*((LR-LL)/4+F(7,100)*(TR-TL)/2)
 PIECES=[(F(0),T,[0,-1+LAM*(1-T)**2/2]),(T,F(1),[-LAM*T*T/2,-1+LAM*(1+T*T)/2,-LAM/2]),(F(1),F(2),[-1]),(F(2),F(3),[-3-3*LAM,1+5*LAM/2,-LAM/2])]
 evaluate.cache_clear()
def produce():
 assert 0<TL<TR<1 and 0<LL<LR<F(7,100) and DG<F(1,10**27)
 coarse=DG;configure(128);assert DG<coarse/2**30;configure(96)
 controls=[]
 for eps in [F(1,100),F(1,2),F(1)]:
  for u,z in [(F(-2),F(7)),(F(-1),F(8)),(F(0),F(3)),(F(5,2),F(10)),(F(-3),F(-3)),(F(3),F(12))]:
   v=evaluate(3,u,z,eps,128);w=evaluate(3,-u,9-z,eps,128)
   assert v==-w and abs(v)<=M,'amplitude/reflection'
   err=error(3,eps,128);fine=evaluate(3,u,z,eps,256)
   assert abs(v-fine)<=err+error(3,eps,256),'nested certified enclosure consistency'
   controls.append(dict(epsilon=str(eps),u=str(u),z=str(z),iterate=3,midpoints=128,value=str(v),absolute_error=str(err),enclosure=list(map(str,[max(-M,v-err),min(M,v+err)]))))
 # Execute the genuinely recursive path as well; this is a coarse control, not high accuracy.
 v=evaluate(4,F(-2),F(7),F(1,2),4);assert abs(v)<=M
 return dict(result_id='K1983',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',root_interval=list(map(str,[TL,TR])),lambda_interval=list(map(str,[LL,LR])),forcing_uniform_error=str(DG),controls=controls,recursive_control=dict(iterate=4,epsilon='1/2',midpoints=4,u='-2',z='7',value=str(v),absolute_error=str(error(4,F(1,2),4))),scope='Certified pointwise evaluation on the entire actual continuum strip; explicit rational first two iterates and clipped third iterate, all finite iterates computable with a uniform error bound. No finite exact endpoint, phase-energy or effective error-to-limit certificate.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1969-scalar-continuum-separation.json','explorations/conditional-build/k1974-scalar-excursion-separation-2026-10-23.md','explorations/conditional-build/k1980-constructive-minimum-norm-pulse-2026-10-23.md']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K1983',len(r['controls']),'actual continuum point enclosures; recursive k4 control')
