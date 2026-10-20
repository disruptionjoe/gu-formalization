#!/usr/bin/env python3
"""Exact identities only; K1857 sections2-3 own the Sobolev proof."""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[2]
import sympy as S
m=json.loads((ROOT/'lab/process/k1857-fisher-gaussian-profile.json').read_text());C=m['constants']
x,q,a=S.symbols('x q a',real=True);H3=x**3-3*x;H4=x**4-6*x*x+3
def G(p):
 p=S.Poly(S.expand(p),x)
 return sum(coef*(0 if power[0]%2 else S.factorial2(power[0]-1)) for power,coef in p.terms())
g=x+a*H3/(1+a*x*x/2);P=2-x*x+a*(-2*x**4+12*x*x-6)-2*a*a*x**4
res=a**3*x**4*((x*x-1)**2+2+a*x**4)/(2*(1+a*x*x/2)**2)
e=q**C['tail_weight_power'];w=q**C['tail_variance_power'];v=(1-e*w)/(1-e);k0=(3-q-3*e*w*w)/((1-e)*v*v)
checks={
 'dual_residual':2*S.diff(g,x)-g*g-P-res,
 'profile_derivative':S.diff(-H4/C['profile_denominator'],x)+H3/12,
 'profile_mean':G(H4), 'second_tangent':G(x*x*H4),
 'fourth_tangent':G(x**4*(-H4/C['density_denominator']))+1,
 'derivative_norm':G((H3/12)**2)-S.Rational(1,C['derivative_norm_denominator']),
 'sqrt_distance':G((H4/C['profile_denominator'])**2)-S.Rational(1,C['sqrt_distance_denominator']),
 'affinity':G((H4/C['profile_denominator'])**2)/2-S.Rational(1,C['affinity_denominator']),
 'cdf_coefficient':S.diff(H3/24,x)-x*H3/24+H4/24,
 'absolute_integral_primitive':S.diff(H3,x)-x*H3+H4,
 'contamination_second':(1-e)*v+e*w-1,
 'contamination_fourth':(1-e)*v*v*k0+3*e*w*w-(3-q),
 'contamination_k0':k0-(3-q-3*q*q)*(1-q**10)/(1-q**6)**2,
 'q0_leading':S.limit((3-k0)/q,q,0)-1,
 'q0_second':S.limit((3-k0-q)/q**2,q,0)-3,
 'core_weight_cost':S.limit(((1-e)/v-1)/q**2,q,0),
 'sixth_escape':15*e*w**3-C['tail_sixth_coefficient']/q**2,
 'dual_polynomial_mean':(1+2*a*q-2*a*a*(3-q)).subs(a,q/6)-(1+q*q/6+q**3/18),
 'cubic_exhaustion':S.Rational(1,4)-S.Rational(1,18)-S.Rational(7,36),
}
for name,value in checks.items():assert S.simplify(value)==0,(name,value)
for p,h in m['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
assert m['scope']['gu_physics'] is False
print(f'PASS K1857: {len(checks)} exact polynomial/rational/limit groups; dependency and scope checks separate')
