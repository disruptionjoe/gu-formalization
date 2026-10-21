"""Exact finite controls; analytic scope is in the linked research note."""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
COUNT=0
def check(ok, name):
    global COUNT
    assert bool(ok), name
    COUNT+=1
def eq(a,b,name): check(s.simplify(a-b)==0,name)
def mat(a,b,name): check((a-b).applyfunc(s.simplify)==s.zeros(*a.shape),name)
def pin(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

def calculate(tail_factor=2,steering_factor=2):
    global COUNT
    COUNT=0
    x,a,b,L,X,Y,c,T=s.symbols('x a b L X Y c T',positive=True)
    ell=L-b;A=Y-X/2;B=Y+X/2
    cost=A*A/ell+X*X/(2*a)+B*B/ell
    eq(s.expand(cost-X*X*(1/(2*a)+1/(tail_factor*ell))),2*Y*Y/ell,'common phase minimization')
    neg=-X*(x+L)/(2*ell);mid=X*x/(2*a);pos=X*(L-x)/(2*ell)
    derivative_cost=s.integrate(s.diff(neg,x)**2,(x,-L,-b))+s.integrate(s.diff(mid,x)**2,(x,-a,a))+s.integrate(s.diff(pos,x)**2,(x,b,L))
    eq(derivative_cost,X*X*(1/(2*a)+1/(2*ell)),'exact ramp integral')
    half_area=s.integrate(-neg,(x,-L,-b))+X*(b-a)/2+s.integrate(-mid,(x,-a,0))
    eq(half_area,X*(L+b-a)/4,'negative half area')
    eq(half_area/(steering_factor*c),X*(L+b-a)/(8*c),'antiderivative amplitude')
    eq((1/(2*a)+1/(2*ell))/(1/(2*a)),1+a/ell,'fixed support penalty')
    # Direct scalar transport on a compact-endpoint polynomial scout. This is an
    # exact characteristic identity, not a claim that this polynomial is C-infinity.
    t,z=s.symbols('t z',real=True);f=s.Function('f');g=s.Function('g')
    F=g(t)*f(x-c*t);V=s.diff(F,t)-c*s.diff(F,x)
    mat(s.Matrix([s.expand(V)]),s.Matrix([s.diff(g(t),t)*f(x-c*t)-2*c*g(t)*s.diff(f(x-c*t),x)]),'steering differential identity')
    h=30*t**2*(1-t)**2
    eq(s.integrate(h,(t,0,1)),1,'unit-integral scout')
    eq(s.integrate(s.diff(h,t),(t,0,1)),0,'vanishing endpoint scout')
    eq(s.Rational(1,24)/(2*s.pi)*(s.Rational(1,2)+s.Rational(1,6))*(s.pi/2)**2,s.pi/288,'L5 b2 a1 complete decoherence energy')
    l,gg,rr,u,v,Q=s.symbols('l gg rr u v Q',positive=True)
    J=A*A/l+X*X/gg+B*B/rr+(u*A+v*B)**2/Q
    D=1/l+1/rr+(u+v)**2/Q;EE=-1/l+1/rr+(v*v-u*u)/Q
    FF=1/gg+(1/l+1/rr)/4+(v-u)**2/(4*Q)
    eq(J,D*Y*Y+EE*X*Y+FF*X*X,'asymmetric quadratic decomposition')
    d0,e0,f0=s.symbols('d0 e0 f0',nonzero=True)
    eq((d0*Y*Y+e0*X*Y+f0*X*X).subs(Y,-e0*X/(2*d0)),X*X*(f0-e0*e0/(4*d0)),'asymmetric Schur minimum')
    subs={l:1,gg:1,rr:1,u:2,v:3,Q:s.Rational(1,4)}
    eq((FF-EE*EE/(4*D)).subs(subs),s.Rational(155,102),'asymmetric scalar penalty')
    dd=s.symbols('dd',positive=True);bubble=x*(dd-x)/2
    eq(s.integrate(bubble,(x,0,dd)),dd**3/12,'gap Green integral')
    eq(s.integrate(s.diff(bubble,x)**2,(x,0,dd)),dd**3/12,'gap Green norm')
    return {'kappa':'1/(2*a)+1/(2*(L-b))','support_penalty':'1+a/(L-b)','f_norm_factor':'(L+b-a)/(8*c)','necessary_MT_factor':'1/2','example_energy':'pi/288','asymmetric_example':'155/102','math_checks':COUNT}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args()
    result=calculate();result['dependency_sha256']=pin('explorations/conditional-build/k1900-sharp-phase-noise-cost-2026-10-21.md')
    if args.write_report: (ROOT/'lab/process/k1902-fixed-support-scalar-noise.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
