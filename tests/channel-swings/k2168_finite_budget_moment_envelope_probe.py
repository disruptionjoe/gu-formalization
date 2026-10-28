#!/usr/bin/env python3
"""Exact symbolic controls and rational outward scalar certificates; no float proof."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
class IV:
 def __init__(self,a,b=None):self.a=F(a);self.b=F(a if b is None else b);assert self.a<=self.b
 def __add__(self,o):
  o=iv(o);return IV(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return IV(-self.b,-self.a)
 def __sub__(self,o):return self+-iv(o)
 def __rsub__(self,o):return iv(o)+-self
 def __mul__(self,o):
  o=iv(o);v=[a*b for a in [self.a,self.b] for b in [o.a,o.b]];return IV(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=iv(o);assert o.a*o.b>0;return self*IV(1/o.b,1/o.a)
 def __rtruediv__(self,o):return iv(o)/self
 def __pow__(self,n):
  assert n>=0;r=IV(1)
  for _ in range(n):r=r*self
  return r
 def sign(self):return 1 if self.a>0 else -1 if self.b<0 else 0
 def pair(self):return [str(self.a),str(self.b)]
def iv(x):return x if isinstance(x,IV) else IV(x)
def sqrtq(q,bits=150):
 q=F(q);assert q>=0;den=1<<bits;k=isqrt((q.numerator*den*den)//q.denominator)
 return IV(F(k,den),F(k+1,den))
N=F(1,3);C=F(40,3);DM=F(25,3);DW=F(-5,6)
def aa(x):return F(41,6)*x*x+F(3,2)/(x*x)
def ap(x):return F(41,3)*x-3/(x*x*x)
def squeeze(target):
 lo,hi=F(1,16),F(16);assert (ap(IV(lo))-target).sign()==-1 and (ap(IV(hi))-target).sign()==1
 for _ in range(110):
  mid=(lo+hi)/2;v=(ap(IV(mid))-target).sign()
  if v<0:lo=mid
  elif v>0:hi=mid
  else:break
 return IV(lo,hi)
def ff(mu):
 mu=F(mu);r=mu+F(1,2);s=sqrtq(mu*(mu+1));x=squeeze(C*s/r)
 val=r*aa(x)-C*x*s+DM*mu+DW
 derivative=aa(x)-C*x*r/s+DM if mu else None
 return val,derivative

def ll(delta,w):
 d=N*delta;mu1=N+d/w;mu0=N-d/(1-w)
 f1,p1=ff(mu1);f0,p0=ff(mu0)
 return w*f1+(1-w)*f0, f1-(d/w)*p1-f0-(d/(1-w))*p0

def minimum(delta,lo,hi):
 delta,lo,hi=F(delta),F(lo),F(hi)
 assert ll(delta,lo)[1].sign()==-1 and ll(delta,hi)[1].sign()==1
 for _ in range(65):
  mid=(lo+hi)/2;sg=ll(delta,mid)[1].sign()
  if sg<0:lo=mid
  elif sg>0:hi=mid
  else:break
 mid=(lo+hi)/2;val,der=ll(delta,mid)
 # Convex supporting tangent: L(w*) >= L(mid)+L'(mid)(w*-mid).
 lower=(val+der*IV(lo-mid,hi-mid)).a
 return {'delta':str(delta),'w_bracket':[str(lo),str(hi)],'energy_bracket':[str(lower),str(val.b)]}
def symbolic(fault=None):
 out={};ck=lambda n,v:out.__setitem__(n,bool(v));zero=lambda e:S.simplify(e)==0
 m,x,al,be,c,dm,dw=S.symbols('m x al be c dm dw',positive=True);r=m+S.Rational(1,2);s=S.sqrt(m*(m+1))
 A=al*x*x+be/x**2
 G=r*A-(c if fault!='cross_coefficient' else 2*c)*x*s+dm*m+dw
 ck('exact_G_mumu',zero(S.diff(G,m,2)-c*x/(4*s**3)))
 gx=S.diff(G,m,x).subs(al,(c*s/r+2*be/x**3)/(2*x))
 ck('stationary_cross_derivative',zero(gx+c/(4*r*s)))
 ck('positive_curvature_margin',zero(x*S.diff(A,x,2)-S.diff(A,x)-8*be/x**3))
 # Schur determinant has the asserted positive form at the squeeze stationary point.
 h=S.diff(G,m,2)-S.diff(G,m,x)**2/S.diff(G,x,2)
 formula=c*x/(4*s**3)*(1-S.diff(A,x)/(4*r*r*x*S.diff(A,x,2)))
 ck('global_schur_formula',zero((h-formula).subs(c,r*S.diff(A,x)/s)))
 w,d,n=S.symbols('w d n',positive=True);f=S.Function('f')
 mu1=n+d/w;mu0=n-d/(1-w) if fault!='wrong_complement' else n+d/(1-w)
 L=w*f(mu1)+(1-w)*f(mu0)
 if fault=='omit_weight':L=f(mu1)+(1-w)*f(mu0)
 expected=f(n+d/w)-d/w*S.Subs(S.Derivative(f(S.Symbol('t')),S.Symbol('t')),S.Symbol('t'),n+d/w)-f(n-d/(1-w))-d/(1-w)*S.Subs(S.Derivative(f(S.Symbol('t')),S.Symbol('t')),S.Symbol('t'),n-d/(1-w))
 ck('perspective_first_derivative',zero(S.diff(L,w)-expected))
 a,b=S.symbols('a b',positive=True)
 # Hessian quadratic: a/(w)*(dd-d/w*dw)^2+b/(1-w)*(dd+d/(1-w)*dw)^2.
 Hdd=a/w+b/(1-w);Hdw=-d*a/w**2+d*b/(1-w)**2;Hww=d*d*(a/w**3+b/(1-w)**3)
 if fault=='hessian_cross':Hdw=-d*a/w**2-d*b/(1-w)**2
 ck('minimized_perspective_hessian',zero(Hdd-Hdw**2/Hww-a*b/(a*(1-w)**3+b*w**3)))
 # Fixture constants from physical moments, independent of interval implementation.
 eh=ej=S.Integer(5);nn=S.Rational(1,3)
 ck('fixture_energy_constants',[(nn*eh+(nn+1)*ej),((nn-1)*eh+nn*ej)/2]==[S.Rational(DM.numerator,DM.denominator),S.Rational(DW.numerator,DW.denominator)])
 moment_n=2 if fault=='bad_cauchy' else 1
 ck('geometric_cauchy_factor',S.expand((m+S.Rational(1,2))**2-m*(m+moment_n))==S.Rational(1,4))
 return out
FAULTS=['cross_coefficient','wrong_complement','omit_weight','hessian_cross','bad_cauchy']
def main():
 ap_=argparse.ArgumentParser();ap_.add_argument('--write',action='store_true');args=ap_.parse_args()
 checks=symbolic();assert all(checks.values()),checks
 faults={}
 for f in FAULTS:
  bad=[k for k,v in symbolic(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 cert=[minimum(F(1,2),F(1,5),F(3,10)),minimum(F(3,4),F(1,20),F(1,10))]
 for row,lo,hi in zip(cert,[F('0.5423370097'),F('1.2985788504')],[F('0.5423370099'),F('1.2985788507')]):
  assert lo<F(row['energy_bracket'][0])<=F(row['energy_bracket'][1])<hi
 # Transition lies above actual maximal contrast: L'(0+) remains negative at Delta=.75.
 xin=squeeze(IV(C));a=aa(xin)-C*xin+DM;b=(a-10)/2
 f0,p0=ff(N*(1-F(3,4)));B=a*N+b-f0-N*F(3,4)*p0
 assert B.b<0
 deps=['explorations/conditional-build/k2168-finite-budget-moment-envelope-2026-10-27.md','explorations/conditional-build/k2166-uniform-feedback-weak-budget-2026-10-27.md','explorations/conditional-build/k2162-feedback-detector-frontier-2026-10-27.md']
 report=dict(result_id='K2168',status='conditional_exact_controls',symbolic_checks=checks,fault_failures=faults,rational_certificates=cert,endpoint_derivative_at_max_contrast=B.pair(),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written convexity, recession, strictness and inverse-bound proofs independently reviewed. Rational intervals certify fixture bounds, not a full detector optimum.')
 dest=ROOT/'lab/process/k2168-finite-budget-moment-envelope.json'
 if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==report
 print(json.dumps(dict(result='K2168',symbolic_checks=len(checks),faults=faults,energy_display=[[float(F(q)) for q in row['energy_bracket']] for row in cert])))
if __name__=='__main__':main()
