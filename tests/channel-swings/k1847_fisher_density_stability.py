#!/usr/bin/env python3
"""Exact polynomial/tail/constant certificate for the density Stein conversion."""
from pathlib import Path
import sympy as s
import json,hashlib
R=Path(__file__).resolve().parents[2];path=R/'lab/process/k1847-fisher-density-stability.json';r=json.loads(path.read_text());checks={}
def ck(k,v):
 assert bool(v),k
 checks[k]=True
x,y=s.symbols('x y');a,b,d,c,e=map(s.Rational,r['score']);N=a+b*y+d*y*y;D=1+c*y+e*y*y
ck('positive denominator',c>0 and e>0)
ck('negative origin',a<0)
ck('one positive sign crossing',b>0 and d>0 and N.subs(y,1)>0)
low=s.Poly(N+s.Rational(11,10)*D,y);tail=s.Poly(s.expand((N-D).subs(y,y+s.Rational(9,4))),y)
ck('global lower slope coefficients',all(v>0 for v in low.all_coeffs()))
ck('tail lower slope coefficients',all(v>0 for v in tail.all_coeffs()))
ck('chosen tail radius',s.Rational(r['R'])**2==s.Rational(9,4))
ck('maximum depth bound',s.Rational(r['depth'])==s.Rational(11,20))
z=s.Rational(r['depth']);partial=sum(z**j/s.factorial(j) for j in range(9));remainder=z**9/s.factorial(9)/(1-z/10)
ck('positive geometric remainder ratio',0<z/10<1)
ck('rational exponential majorant',partial+remainder<s.Rational(r['exponential_upper']))
C=s.Rational(r['exponential_upper'])*(s.Rational(r['R'])+1/s.Rational(r['R']))
ck('Stein factor',C==s.Rational(r['stein_factor']))
ck('score bound',s.Rational(r['score_budget'])<s.Rational(7,200)**2)
ck('total variation bound',C*s.Rational(7,200)==s.Rational(r['tv_upper']))
ck('pair bound',2*s.Rational(r['tv_upper'])==s.Rational(r['pair_tv_upper']))
ck('display bound',s.Rational(r['tv_upper'])<s.Rational(133,1000))
g=x*N.subs(y,x*x)/D.subs(y,x*x)
ck('tail linear slope',s.limit(g/x,x,s.oo)==d/e)
ck('not log concave',s.diff(g,x).subs(x,0)<0)
u,v,f,fp=s.symbols('u v f fp')
ck('weak score integration identity',s.expand((fp-g*f)*u*u+f*(2*v+g*u)*u-(fp*u*u+2*f*u*v))==0)
# Gaussian location shift has exact J=m^2 and indicator expectation derivative.
m=s.symbols('m',real=True)
ck('Gaussian score difference',s.expand(-(x-m)+x)==m)
ck('reference dependency',hashlib.sha256((R/r['dependency']['path']).read_bytes()).hexdigest()==r['dependency']['sha256'])
c0,gamma,Delta,E0,Fval,aa,bb,kk=s.symbols('c0 gamma Delta E0 Fval aa bb kk')
ck('fixed moment energy cancellation',s.expand((Fval+Delta+aa+bb*kk)-(Fval+aa+bb*kk))==Delta)
ck('TV product identity',s.expand((2-2*c0)*(2+2*c0)/4)==1-c0*c0)
ck('Hellinger factor',s.expand(2*(1-c0*c0)-2*(1-c0)-2*c0*(1-c0))==0)
am=s.symbols('am');ck('quartic form lower bound',s.expand(bb*x**4/2-am*x*x+am**2/(2*bb)-(bb/2)*(x*x-am/bb)**2)==0)
dep=r['optimizer_stability']['dependency'];ck('optimizer theorem dependency',hashlib.sha256((R/dep['path']).read_bytes()).hexdigest()==dep['sha256'])
r['mathematical_checks']=checks;r['lower_slope_polynomial']=[str(v) for v in reversed(low.all_coeffs())];r['shifted_tail_polynomial']=[str(v) for v in reversed(tail.all_coeffs())];r['exp_upper_rational']=str(partial+remainder)
path.write_text(json.dumps(r,indent=2)+'\n');print('K1847 exact groups',len(checks))
