#!/usr/bin/env python3
"""Exact algebra only; K1859's written argument owns the analytic transfers."""
from pathlib import Path
import hashlib
import json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
m=json.loads((ROOT/'lab/process/k1859-fisher-optimizer-tail-response.json').read_text())
x,s,t=S.symbols('x s t',real=True)
H=lambda n:S.hermite_prob(n,x)
def G(p):
    return sum(c*(0 if n%2 else S.factorial2(n-1)) for (n,),c in S.Poly(S.expand(p),x).terms())
u=sum(S.Rational(c)*H(int(n)) for n,c in m['u_hermite'].items())
v=sum(S.Rational(c)*H(int(n)) for n,c in m['v_hermite'].items())
h=1+s*u+s*s*v
N=G(h*h);B=G(x*x*h*h);C=G(x**4*h*h);D=G(S.diff(h,x)**2)
q=3-C*N/B**2;J=B/N*(2-B/N+4*D/N)-1
checks={}
for name,value in {'N':N,'B':B,'C':C,'D':D,'q':q,'J':J}.items():
    expected=sum(S.Rational(c)*s**i for i,c in enumerate(m['jets'][name]))
    checks['jet_'+name]=S.series(value,s,0,5).removeO()-expected
r0=(x**8-2*x**6+3*x**4)/2;r1=(-x**10+3*x**8-3*x**6)/2
d=1+t*x*x/2;R=t**3*(r0+t*x**8/2)/d**2
checks.update({
    'residual_series':S.series(R,t,0,5).removeO()-t**3*r0-t**4*r1,
    'residual_leading':G(r0)-42,
    'residual_response':-G(r0*H(4))/24+S.Rational(183,2),
    'residual_next':G(r1)+S.Rational(675,2),
    'residual_quartic':-G(r0*H(4))/24/216+G(r1)/1296-S.Rational(m['constants']['residual_quartic']),
    'h3_square_response':-G(H(3)**2*H(4))/24+9,
    'x2h3_square':G(x*x*H(3)**2)-42,
    'projection_x':-S.Rational(1,6)-S.Rational(6,72)-S.Rational(m['constants']['projection_x']),
    'projection_h3':-S.Rational(9,6)-S.Rational(42,72)-S.Rational(m['constants']['projection_h3']),
    'score_profile_norm':G((-x/4-S.Rational(25,72)*H(3))**2)-S.Rational(679,864),
    'square_floor':S.Rational(m['constants']['projection_x'])**2+S.Rational(m['constants']['projection_h3'])**2/6-S.Rational(m['constants']['square_quartic']),
    'lower_quartic':S.Rational(m['constants']['square_quartic'])+S.Rational(m['constants']['residual_quartic'])-S.Rational(m['constants']['quartic']),
    'upper_quartic':S.series(J-q*q/6-q**3/4-S.Rational(m['constants']['quartic'])*q**4,s,0,5).removeO(),
    'normalization_second':G(2*v+u*u),
    'moment2_second':G(x*x*(2*v+u*u)),
    'moment4_second':G(x**4*(2*v+u*u)),
    'sixth_response':-G(x**6*H(4))/24+15,
    'eighth_response':-G(x**8*H(4))/24+210,
    'tenth_response':-G(x**10*H(4))/24+3150,
})
z=S.symbols('z');qb=S.sqrt(6)*z-S.Rational(9,2)*z*z+S.Rational(m['constants']['inverse_b32'])*S.sqrt(6)*z**3
checks['budget_inverse']=S.series(qb**2/6+qb**3/4+S.Rational(m['constants']['quartic'])*qb**4-z*z,z,0,5).removeO()
tail_e=S.Rational(m['constants']['tail_exponent'])
tail_w=S.exp(-tail_e*x*x/2)
checks['tail_schrodinger_derivative']=-4*S.diff(tail_w,x,2)/tail_w-(4*tail_e-4*tail_e**2*x*x)
for name,value in checks.items():
    assert S.simplify(value)==0,(name,value)
qmax=S.Rational(m['constants']['q_window'])
assert 0<qmax and 2*qmax<=S.Rational(1,25)
assert S.Rational(2,3)*(1+4*qmax)<1
assert 1-6*qmax>=S.Rational(1,2)
assert 2*(1+qmax*qmax*(1+2*qmax)/6)<3
assert tail_e>0 and S.Rational(1,2)-4*tail_e**2>=0
assert 4*tail_e-3+9*(S.Rational(1,2)-4*tail_e**2)>=0,'exterior supersolution at |x|=3'
assert S.Rational(m['constants']['tail_prefactor_log'])>=9*tail_e,'boundary comparison normalization'
for p,digest in m['dependencies'].items():
    assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest,p
assert m['scope']=={'exact_optimizer_only_for_tail_and_moment_response':True,'quartic_value_asymptotic':True,'finite_q_quartic_error_bound':False,'second_density_profile':False,'gu_physics':False,'novelty':False,'formal_proof':False,'second_score_defect':True}
print(f'PASS K1859: {len(checks)} exact identity/jet groups; uniform-window inequalities, dependency hashes and reporting scope checked separately')
