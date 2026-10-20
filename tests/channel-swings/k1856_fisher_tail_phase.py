#!/usr/bin/env python3
"""Exact algebra only; continuum proof is in the K1856 note."""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[2]
import sympy as S
m=json.loads((ROOT/'lab/process/k1856-fisher-tail-phase.json').read_text());C=m['constants']
t,c,R,D,M=S.symbols('t c R D M',positive=True)
e=t**C['tail_weight_power']/(c+t**C['tail_weight_power']);v=1-t;w=1+C['tail_variance_coefficient']*c/t
checks={
 'second_moment':(1-e)*v+e*w-1,
 'fourth_moment':C['gaussian_fourth']*((1-e)*v**2+e*w**2)-3*(1+c),
 'fisher_upper_identity':(1-e)/v+e/w-1-c*t/((1-t)*(c+t)),
 'tail_fourth_limit':S.limit(e*w**2,t,0)-c,
 'tail_sixth_scale':S.limit(t*C['gaussian_sixth']*e*w**3,t,0)-15*c**2,
 'weight_limit':S.limit(e,t,0),
 'core_variance_limit':S.limit(v,t,0)-1,
 'fisher_limit':S.limit((1-e)/v+e/w,t,0)-1,
 'sixth_cap_constant':D**2/(4*(2*(M+15)/D)**4)-D**6/(C['sixth_cap_denominator']*(M+15)**4),
 'cap_split':2*(2*(M+15)/D)**2*(D/(4*(2*(M+15)/D)**2))+(M+15)/(2*(M+15)/D)-D,
}
for name,value in checks.items():
 assert S.simplify(value)==0,(name,value)
for p,h in m['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
assert m['scope']['gu_physics'] is False
print(f'PASS K1856: {len(checks)} exact algebra/limit groups; dependency and scope checks separate')
