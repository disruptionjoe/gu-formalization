"""Independent symbolic ODE, algebraic contact and physical ripple probe."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k1969-scalar-continuum-separation.json'
x,t=s.symbols('x t',real=True)
def audit(fault=None):
    r=json.loads(REPORT.read_text());checks=0
    def ck(v,label):
        nonlocal checks
        assert v,label
        checks+=1
    # Reconstruct the positive-half ODE. The summed raw forcing's mean is 1.
    mu=s.S(0) if fault=='projection' else s.S(1)
    a,b,c=s.symbols('a b c')
    inside=-(1-mu)*x*x/2+a*x
    outside=mu*x*x/2+b*x+c
    solution=s.solve([inside.subs(x,t)-outside.subs(x,t),
        s.diff(inside,x).subs(x,t)-s.diff(outside,x).subs(x,t),
        outside.subs(x,1)],[a,b,c])
    gi=s.factor(inside.subs(solution));go=s.factor(outside.subs(solution))
    ck(s.simplify(gi+(1-t)**2*x/2)==0,'actual zero-area projected forcing')
    ck(s.simplify(go-(x-1)*(x-t*t)/2)==0,'ODE matching and endpoint')
    d,e=s.symbols('d e')
    tail=x*x/2+d*x+e
    tail=s.factor(tail.subs(s.solve([tail.subs(x,2),tail.subs(x,3)],[d,e])))
    ck(tail==(x-2)*(x-3)/2,'outer ODE')
    K=s.factor(-s.integrate(go,(x,t,1))-s.integrate(tail,(x,2,3)))
    norm=s.factor(2*(s.integrate(s.diff(gi,x)**2,(x,0,t))+
        s.integrate(s.diff(go,x)**2,(x,t,1))+
        s.integrate(s.diff(tail,x)**2,(x,2,3))))
    ck(s.simplify(norm-2*K)==0,'actual representer norm')
    factor=s.Rational(23,100) if fault=='physical_factor' else s.Rational(23,200)
    D=2-t*t/2-factor*(3-t)*(6+t)
    la=s.factor(D/K)
    if fault=='multiplier':la*=2
    P=101*t**4-102*t**3-168*t*t+392*t-138
    # Tangency at the contact point must vanish at the declared algebraic root.
    tangent=s.together(-t-la*gi.subs(x,t)+factor*(3+2*t))
    num=s.fraction(tangent)[0]
    ck(s.rem(num,P,t)==0,'continuum tangent contact and physical Jacobian')
    ck(s.simplify(D-la*K)==0,'contact multiplier')
    energy=s.factor(4+la*la*norm)
    ck(s.simplify(energy-(4+2*D*D/K))==0,'independent integrated energy')
    ck(s.Poly(P,t).count_roots(s.Rational(9,20),s.Rational(23,50))==1,'Sturm root count')
    l,h=map(s.Rational,r['root_interval'])
    ck(P.subs(t,l)<0<P.subs(t,h),'declared exact root bracket')
    ck(s.Poly(P,t).count_roots(l,h)==1,'tight bracket root count')
    # A rational center gives an independent conservative check of reported energy.
    mid=(l+h)/2;emid=energy.subs(t,mid)
    elo,ehi=map(s.Rational,r['energy_interval'])
    ck(elo<emid<ehi,'reported interval includes independent rational energy')
    ck(elo>s.Rational(1730979348830867,432645592385000),'prior lower bound improved')
    # Ripple is independently reconstructed as affine pieces and integrated.
    height=s.Rational(1,2) if fault=='ripple_height' else s.S(2)
    vertices=[(s.Rational(5,2),0),(s.Rational(41,16),height),
              (s.Rational(21,8),0),(s.Rational(43,16),-height),
              (s.Rational(11,4),0)]
    parts=[];areas=[]
    for (a,u),(b,v) in zip(vertices,vertices[1:]):
        q=u+(v-u)*(x-a)/(b-a);parts.append((a,b,q))
        areas.append(s.integrate(q,(x,a,b)))
    ck(sum(areas)==0,'ripple zero area')
    ck(sum(areas[:2])==s.Rational(1,8),'exact primitive bound')
    aa,bb=s.Rational(163,64),s.Rational(165,64)
    values=[]
    for a,b,q in parts:
        if max(a,aa)<=min(b,bb):
            values.extend([q.subs(x,max(a,aa)),q.subs(x,min(b,bb))])
    ck(min(values)==s.Rational(3,2),'actual triangular lobe on violated cut')
    lower=min(values)+aa-3
    violation=(bb-aa)*(lower-s.Rational(207,200))
    ck(violation==s.Rational(r['ripple']['violation_lower'])>0,'physical non-halfcut witness')
    # Direct all-cut path formula on a cut with positive and negative excursions.
    # A=[-3,-2] union [1,2], s=2, t_s=-2, W knots 0,1,-2,-1,-2.
    ws=[(s.S(0),s.S(0)),(s.S(1),s.S(1)),(s.S(4),s.S(-2)),
        (s.S(5),s.S(-1)),(s.S(6),s.S(-2))]
    dist_area=s.S(0)
    for (a,u),(b,v) in zip(ws,ws[1:]):
        w=u+(v-u)*(x-a)/(b-a);cuts=[a,b]
        for level in[-2,0]:
            for z in s.solve(w-level,x):
                if a<z<b:cuts.append(z)
        cuts=sorted(set(cuts))
        for lo,hi in zip(cuts,cuts[1:]):
            z=w.subs(x,(lo+hi)/2)
            integrand=w if z>0 else(-2-w if z<-2 else s.S(0))
            dist_area+=s.integrate(integrand,(x,lo,hi))
    signed_integral=9*2-(2 if fault=='path_factor' else 1)*dist_area
    # Direct sliding-window pieces: prefix 6, central rectangle 6, suffix 5.
    prefix=s.integrate(x-1,(x,1,2))+2+s.integrate(x-3,(x,4,5))+2
    suffix=s.integrate(2-x,(x,0,1))+3+s.integrate(5-x,(x,4,5))
    ck(signed_integral==prefix+6+suffix==17,'independent path-capacity identity')
    return checks
if __name__=='__main__':
    n=audit();caught=[]
    for f in ['projection','physical_factor','multiplier','ripple_height','path_factor']:
        try:audit(f)
        except AssertionError:caught.append(f)
        else:raise AssertionError('undetected mathematical fault '+f)
    r=json.loads(REPORT.read_text())
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    src=ROOT/'tests/channel-swings/k1969_scalar_continuum_separation.py'
    assert hashlib.sha256(src.read_bytes()).hexdigest()==r['source_sha256']
    print('PASS K1969 independent',n,'controls;',len(caught),'mathematical faults; pins separate')
