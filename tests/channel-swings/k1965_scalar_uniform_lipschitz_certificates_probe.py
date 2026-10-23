"""Independent piecewise ODE reconstruction of actual slopes, dual mass and repair."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2];x=s.symbols('x',real=True)
def audit(fault=None):
    r=json.loads((ROOT/'lab/process/k1965-scalar-uniform-lipschitz-certificates.json').read_text());checks=0
    for row in r['certificates']:
        t=s.Rational(row['halfcut']);cuts=[-t,t];free=[(-3,-2),(-1,1),(2,3)];Gs=[]
        for cut in cuts:
            raw=[];mu=0
            for a,b in free:
                knots=sorted({s.Rational(a),s.Rational(b)}|({cut} if a<cut<b else set()))
                length=s.Rational(b-a);v=max(s.S(0),min(length,cut-a));z=x-a
                for l,h in zip(knots,knots[1:]):
                    y=s.expand((v-v*v/(2*length))*z-z*z/2) if h<=cut else s.expand(v*v/(2*length)*(length-z))
                    raw.append((a,b,l,h,y));mu+=s.integrate(y,(x,l,h))
            projected=[(l,h,s.expand(y-(0 if fault=='projection' else mu/s.Rational(5,6))*(x-a)*(b-x)/2)) for a,b,l,h,y in raw]
            assert sum(s.integrate(y,(x,l,h)) for l,h,y in projected)==0,'projected zero area'
            Gs.append(projected);checks+=1
        def integral_to(parts,t):return sum(s.integrate(y,(x,l,min(h,t))) for l,h,y in parts if l<t)
        K=s.Matrix([[integral_to(g,c) for g in Gs] for c in cuts]);D=s.Matrix([2-c*c/2-s.Rational(23,200)*(3-abs(c))*(6+abs(c)) for c in cuts]);la=K.inv()*D
        if fault=='multiplier':la[0]*=2
        slopes=[];energy=0;area=0
        for a,b,base in [(-3,-2,x+3),(-2,-1,s.S(1)),(-1,1,-x),(1,2,s.S(-1)),(2,3,x-3)]:
            knots=sorted({s.Rational(a),s.Rational(b)}|{c for c in cuts if a<c<b})
            for l,h in zip(knots,knots[1:]):
                phi=base
                for w,g in zip(la,Gs):
                    yy=next((y for ll,hh,y in g if ll<=l and h<=hh),s.S(0));phi-=w*yy
                der=s.diff(phi,x);slopes += [abs(der.subs(x,l)),abs(der.subs(x,h))]
                energy+=s.integrate(der**2,(x,l,h));area+=s.integrate(phi,(x,l,h))
        assert area==0 and energy==s.Rational(row['energy']),'ODE and actual multiplier'
        bound=s.Rational(row['slope'])/(2 if fault=='slope' else 1)
        assert max(slopes)<=bound,'actual pointwise slope'
        M=s.Rational(23,100);M0=s.Rational(r['constants']['M0']);eps=s.Rational(row['amplitude_allowance']);theta=eps/(M-M0+eps)
        if fault=='mixing':theta/=2
        assert eps==s.Rational(2,3)*s.Rational(row['h'])*(bound+M),'linear transfer constant'
        assert (1-theta)*(M+eps)+theta*M0<=M,'amplitude after repair';checks+=4
    # Worst-case dual-mass maximization, and kernel projection constants.
    z,R=s.symbols('z R',real=True)
    assert s.expand(R**2/4-(z*R-z*z)-(z-R/2)**2)==0
    assert F(1,3)+F(1,2)/F(5,6)*F(1,3)==F(8,15)
    checks+=2
    return checks
if __name__=='__main__':
    n=audit();caught=[]
    for f in ['projection','multiplier','slope','mixing']:
        try:audit(f)
        except AssertionError:caught.append(f)
        else:raise AssertionError('undetected mathematical fault '+f)
    r=json.loads((ROOT/'lab/process/k1965-scalar-uniform-lipschitz-certificates.json').read_text())
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K1965 independent',n,'controls;',len(caught),'mathematical faults; pins separate')
