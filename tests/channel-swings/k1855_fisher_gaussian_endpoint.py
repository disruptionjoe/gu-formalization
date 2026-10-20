#!/usr/bin/env python3
"""Symbolic identities and whole-interval rational certificates for K1855."""
from pathlib import Path
import json,hashlib
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
def verify(d):
 x,a,s=S.symbols('x a s',real=True);checks=0
 def eq(p,q):
  nonlocal checks
  assert S.cancel(p-q)==0,(p,q);checks+=1
 den=1+S.Rational(d['denominator_quadratic'])*a*x*x
 g=x+a*(d['score_cubic']*x**3+d['score_linear']*x)/den
 P=2-x*x+a*(-2*x**4+12*x*x-6)-2*a*a*x**4
 rem=a**3*x**4*(sum(S.Integer(c)*x**(2*i) for i,c in enumerate(d['remainder_coefficients']))+a*x**4)/(2*den**2)
 eq(2*S.diff(g,x)-g*g-P,rem)
 eq(sum(S.Integer(c)*x**(2*i) for i,c in enumerate(d['remainder_coefficients'])),(x*x-1)**2+2)
 h4=sum(S.Integer(c)*x**i for i,c in enumerate(d['hermite']));h=1-s*h4
 def gaussian(poly):
  return S.expand(sum(coef*(S.factorial2(power-1) if power else 1) for (power,),coef in S.Poly(S.expand(poly),x).terms() if power%2==0))
 norm=gaussian(h*h);m2=gaussian(x*x*h*h);m4=gaussian(x**4*h*h)
 eq(norm,1+d['gaussian_h4_norm']*s*s)
 eq(m2,sum(S.Integer(c)*s**i for i,c in enumerate(d['m2_numerator'])))
 eq(m4,sum(S.Integer(c)*s**i for i,c in enumerate(d['m4_numerator'])))
 eq(gaussian(S.diff(h,x)**2),96*s*s)
 info=2-m2/norm+d['kinetic']*gaussian(S.diff(h,x)**2)/norm
 eq(info,m2/norm)
 q=3-m4*norm/m2**2;J=info*m2/norm-1
 eq(q,(48*s-1728*s*s+1152*s**3+69120*s**4)/(1+216*s*s)**2)
 eq(J,384*s*s*(1+120*s*s)/(1+24*s*s)**2)
 eq(S.limit(J/q**2,s,0),S.Rational(d['leading_coefficient']))
 eq(gaussian(x**4*((x*x-1)**2+2)/2),d['residual_gaussian_mean'])
 eq(S.Rational(1,18)+S.Rational(d['residual_gaussian_mean'],216),S.Rational(d['cubic_coefficient']))
 eq(S.limit((J-q*q/6)/q**3,s,0),S.Rational(d['cubic_coefficient']))
 eq(S.Rational(d['budget_correction'])/3+S.Rational(3,2),0)
 bounds={};m=S.Rational(d['s_max'])
 for name,expr,power in [('q_derivative',S.diff(q,s),0),('q_lower',q-46*s,1),('q_upper',48*s-q,2),('upper_window',q*q*(1+d['upper_factor']*q)-6*J,3)]:
  num,de=S.fraction(S.factor(expr));poly=S.Poly(S.cancel(num/s**power),s)
  # All denominators here are products of 1+c*s², positive by construction.
  assert de.subs(s,0)>0
  low=poly.nth(0)+sum(min(0,poly.nth(i))*m**i for i in range(1,poly.degree()+1))
  assert low>0,(name,low);bounds[name]=str(low);checks+=1
 assert q.subs(s,m)>S.Rational(d['q_max'])
 assert S.Rational(d['q_max'])==S.Rational(1,25)
 assert S.Rational(1,4000)<S.Rational(1,3700)
 assert not any(d[k] for k in ['optimizer_equals_trial','sixth_moment_required','novelty'])
 for dep in d['dependencies']:assert hashlib.sha256((ROOT/dep['path']).read_bytes()).hexdigest()==dep['sha256']
 return checks,bounds
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1855-fisher-gaussian-endpoint.json').read_text());n,b=verify(d)
 print(json.dumps(b,sort_keys=True));print('K1855 exact identity/interval groups PASS',n)
