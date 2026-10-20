#!/usr/bin/env python3
"""Exact rational Sturm certificate and Gaussian moment primal bound for F(2)."""
from pathlib import Path
import sympy as s
import json
ROOT=Path(__file__).resolve().parents[2]
report_path=ROOT/'lab/process/k1845-fisher-certified-moment-bounds.json'
r=json.loads(report_path.read_text());cfg=r['certificate'];R=s.Rational
x,y,t=s.symbols('x y t');checks={}
def ck(name,v):
    assert bool(v),name
    checks[name]=True

a,b,d,c,e=map(R,cfg['score']);A,B,C=map(R,cfg['minorant'])
N=a+b*y+d*y*y;D=1+c*y+e*y*y
g=x*N.subs(y,x*x)/D.subs(y,x*x)
H=s.expand(2*N*D+4*y*(s.diff(N,y)*D-N*s.diff(D,y))-y*N*N)
ck('rational score identity',s.cancel(2*s.diff(g,x)-g*g-(H/D**2).subs(y,x*x))==0)
P=s.Poly(s.expand(H-(A+B*y+C*y*y)*D*D),y)
ck('positive denominator coefficients',c>0 and e>0)
ck('positive residual at zero',P.eval(0)>0)
ck('no positive residual root',P.count_roots(0,s.oo)==0)
ck('exact lower value',A+B+2*C==R(r['lower']))
co=[t if v=='t' else R(v) for v in cfg['primal']]
p=sum(co[i]*x**(2*i) for i in range(len(co)))
def mean(q):
 return s.expand(sum(v*(s.factorial2(i-1) if i else 1) for (i,),v in s.Poly(s.expand(q),x).terms()))
Z=mean(p*p);M=mean(x*x*p*p);Q=mean(x**4*p*p);E=mean((2*s.diff(p,x)-x*p)**2)
T=s.Poly(Q*Z-2*M*M,t);lo,hi=map(R,cfg['root_interval'])
ck('positive root interval',0<lo<hi)
ck('root existence',T.eval(lo)*T.eval(hi)<0)
ck('unique root in bracket',T.count_roots(lo,hi)==1)
ck('trial polynomial positive',all(v>0 for v in co if v!=t))
# Exact rational interval polynomial evaluation; no floating-point endpoints.
def bound(expr):
 low=high=R(0)
 for (j,),v in s.Poly(expr,t).terms():
  u,w=v*lo**j,v*hi**j;low+=min(u,w);high+=max(u,w)
 return low,high
zl,zh=bound(Z);ml,mh=bound(M);el,eh=bound(E)
ck('normalization and variance positive',zl>0 and ml>0 and el>0)
vl=el*ml/zh**2;vh=eh*mh/zl**2
ck('certified upper',vh<R(r['upper']))
ck('nonempty interval',R(r['lower'])<vl)
ck('width',R(r['upper'])-R(r['lower'])==R(243,200000))
# Dual operator is -4d2 - Bx2 - Cx4, bounded below by A.
ck('confining dual',-C>0)
# Weak integration-by-parts identity: 4u'^2 - (2g'-g^2)u^2 = (2u'+gu)^2 - 2(gu^2)'.
u,v,w=s.symbols('u v w')
ck('completed square identity',s.expand(4*v*v-(2*w-g*g)*u*u-((2*v+g*u)**2-2*w*u*u-4*g*u*v))==0)
# Positive degree10 Gaussian trial cannot be a confining quartic ground state.
Rp=s.cancel(-4*(s.diff(p,x,2)-x*s.diff(p,x)+(x*x/4-s.Rational(1,2))*p)/p)
ck('trial quartic tail absent',s.limit(Rp/x**4,x,s.oo)==0)
ck('trial quadratic tail',s.limit(Rp/x**2,x,s.oo)==-1)
r['mathematical_checks']=checks
r['residual_polynomial_low_to_high']=[str(v) for v in reversed(P.all_coeffs())]
r['moment_polynomial_low_to_high']=[str(v) for v in reversed(T.all_coeffs())]
r['trial_value_interval']=[str(vl),str(vh)]
r['strict_bounds']=True
report_path.write_text(json.dumps(r,indent=2)+'\n')
print('K1845 exact groups:',len(checks),'lower',r['lower'],'upper',r['upper'])
print('trial numerical display only:',s.N(vl,15),s.N(vh,15))
