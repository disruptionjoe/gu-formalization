"""Separate exact derivation and hostile probes; no producer import."""
from pathlib import Path
import copy,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
COUNT=0
def check(ok,name):
    global COUNT
    assert bool(ok),name
    COUNT+=1
def eq(a,b,name):check(s.simplify(a-b)==0,name)
def mat(a,b,name):check((a-b).applyfunc(s.simplify)==s.zeros(*a.shape),name)
def reject(fn,label):
    try:fn()
    except AssertionError:return label
    raise AssertionError('fault survived: '+label)
def pinned(d):
    expected=hashlib.sha256((ROOT/'explorations/conditional-build/k1900-sharp-phase-noise-cost-2026-10-21.md').read_bytes()).hexdigest()
    check(d['dependency_sha256']==expected,'dependency pin')

def algebra(area_factor=1,steering_sign=-1):
    x,A,d1,d2,d3,lam=s.symbols('x A d1 d2 d3 lam',real=True)
    # Solve the independent constrained variational problem at l=g=r=w0=1,w1=2,X=1.
    cost=A*A+1+(A+1)**2+(d1*d1+d2*d2+d3*d3)/12
    area=5*A+3+area_factor*(d1+d2+d3)/12
    obj=cost+lam*area;vars=[A,d1,d2,d3,lam]
    sol=s.solve([s.diff(obj,v) for v in vars],vars,dict=True)[0]
    eq(cost.subs(sol),s.Rational(155,102),'independent constrained energy')
    eq(area.subs(sol),0,'zero area')
    eq(sol[A],-s.Rational(61,102),'optimal left phase')
    # Direct symmetric geometry L5,b2,a1 with unit contrast.
    left=-(x+5)/6;middle=x/2;right=(5-x)/6
    en=s.integrate(s.diff(left,x)**2,(x,-5,-2))+s.integrate(s.diff(middle,x)**2,(x,-1,1))+s.integrate(s.diff(right,x)**2,(x,2,5))
    eq(en,s.Rational(2,3),'symmetric exact energy')
    eq(s.integrate(left,(x,-5,-2))-s.Rational(1,2)+s.integrate(middle,(x,-1,1))+s.Rational(1,2)+s.integrate(right,(x,2,5)),0,'symmetric zero area')
    t,z,c=s.symbols('t z c',real=True);g=30*t**2*(1-t)**2;f=x**3+x
    V=s.diff(g,t)*f+steering_sign*2*c*g*s.diff(f,x)
    # Here x denotes the comoving coordinate; left characteristics substitute z-2ct.
    minus=s.integrate(s.expand(V.subs(x,z-2*c*t)),(t,0,1))
    plus=s.integrate(s.expand(V.subs(x,z)),(t,0,1))
    eq(minus,0,'opposite characteristic cancellation')
    eq(plus,-2*c*(3*z*z+1),'selected characteristic phase')
    eq((s.pi/2)/2,s.pi/4,'complete dephasing necessary MT')
def reporting(d):
    eq(s.sympify(d['asymmetric_example']),s.Rational(155,102),'report asymmetric cost')
    eq(s.sympify(d['example_energy']),s.pi/288,'report energy')
    eq(s.sympify(d['necessary_MT_factor']),s.Rational(1,2),'report amplitude bound')
if __name__=='__main__':
    d=json.loads((ROOT/'lab/process/k1902-fixed-support-scalar-noise.json').read_text());algebra();n=COUNT;reporting(d);pinned(d)
    faults=[reject(lambda:algebra(area_factor=2),'area functional coefficient'),reject(lambda:algebra(steering_sign=1),'wrong characteristic sign')]
    bad=copy.deepcopy(d);bad['asymmetric_example']='3/2';faults.append(reject(lambda:reporting(bad),'omitted area cost report'))
    badpin=copy.deepcopy(d);badpin['dependency_sha256']='0'*64;faults.append(reject(lambda:pinned(badpin),'dependency pin'))
    print(json.dumps({'baseline_math_checks':n,'faults_rejected':faults}))
