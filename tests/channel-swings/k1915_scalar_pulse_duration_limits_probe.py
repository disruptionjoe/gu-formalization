"""Separately derived characteristic derivative and rational truncated-cut controls."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
import sympy as s
import k1915_scalar_pulse_duration_limits as producer
ROOT=Path(__file__).resolve().parents[2]
def independent():
    # Reconstruct the potential as an opposite-characteristic total derivative.
    t,x,z,u=s.symbols('t x z u',real=True)
    G=t*t*(1-t)**2*30;primitive=(1-u*u)**3
    H=G*(-primitive.subs(u,x-t)/2)
    V=s.diff(H,t)-s.diff(H,x)
    right=s.integrate(V.subs(x,u+t),(t,0,1))
    assert s.expand(right-s.diff(primitive,u))==0,'independent right characteristic'
    assert s.integrate(V.subs(x,z-t),(t,0,1))==0,'independent left characteristic'
    # Integrate piecewise-linear min of section lengths exactly from breakpoints.
    def cut(L,d,a):
        pts=sorted(set([-L,L,-L+d,L+d,a,a+d]))
        def sec(z):
            low=max(-L,z-d);high=min(L,z)
            return max(Q(0),min(a,high)-low),max(Q(0),high-max(a,low))
        total=Q(0)
        for l,r in zip(pts,pts[1:]):
            if r==l:continue
            a0,b0=sec(l);a1,b1=sec(r);extra=[]
            v0=a0-b0;v1=a1-b1
            if v0*v1<0:extra=[l+(r-l)*v0/(v0-v1)]
            pp=[l]+extra+[r]
            for q,w in zip(pp,pp[1:]):total+=(w-q)*(min(sec(q))+min(sec(w)))/2
        return total
    checked=0
    for L in [Q(1),Q(2)]:
        for d in [Q(1,4),Q(1),Q(2),Q(5)]:
            for a in [-L,-L/2,Q(0),L/2,L]:
                value=cut(L,d,a)
                assert 0<=value<=d*d/4,'truncated-cut upper bound'
                if a==0 and d<=L:assert value==d*d/4,'interior equality'
                checked+=1
    assert s.integrate(s.diff(right,u)**2,(u,-1,1))==s.Rational(1024,35),'independent gradient energy'
    # Independent monomial integration of h*(1-t/tau)^2 at h=3,tau=2.
    coeff=[Q(3),Q(-3),Q(3,4)]
    area=sum(a*Q(2)**(i+1)/Q(i+1) for i,a in enumerate(coeff))
    deriv=[coeff[1],2*coeff[2]]
    en=sum(a*b*Q(2)**(i+j+1)/Q(i+j+1) for i,a in enumerate(deriv) for j,b in enumerate(deriv))
    assert area*en==Q(4,9)*27,'sharp area-energy product'
    return checked+4

def caught(fn,label):
    try:fn()
    except AssertionError as e:
        assert str(e), 'empty failure'
        print('CAUGHT',label,':',str(e));return
    raise AssertionError('missed '+label)
def report(r):
    assert r['polynomial_energy']=='1024/35','report energy'
    assert r['scope']=='fixed smooth zero-area phase; infima, not smooth threshold attainment','scope'
    for p,h in r['dependency_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency bytes'
if __name__=='__main__':
    n=independent();producer.calculate()
    caught(lambda:producer.calculate(steering_sign=1),'mathematical: wrong steering sign')
    caught(lambda:producer.calculate(triangle_height=2),'mathematical: triangle area defect')
    r=json.loads((ROOT/'lab/process/k1915-scalar-pulse-duration-limits.json').read_text());report(r)
    caught(lambda:report(dict(r,polynomial_energy='0')),'report corruption')
    bad=json.loads(json.dumps(r));bad['dependency_sha256'][next(iter(bad['dependency_sha256']))]='0'*64
    caught(lambda:report(bad),'pin corruption')
    print(json.dumps({'independent_exact_checks':n,'mathematical_faults':2,'report_faults':1,'pin_faults':1,'universal_scope':'analytic squeeze and construction proofs'}))
