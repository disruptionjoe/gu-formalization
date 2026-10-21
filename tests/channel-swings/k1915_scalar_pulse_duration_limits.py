"""Exact finite algebra for the analytic duration theorem; no sampled proof."""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def calculate(steering_sign=-1, triangle_height=4):
    n=0
    def ck(v,label):
        nonlocal n
        assert bool(v),label
        n+=1
    u,t,z,c,T=s.symbols('u t z c T',positive=True)
    F=(1-u*u)**3;phi=s.diff(F,u);f=steering_sign*F/(2*c)
    g=6*t*(T-t)/T**3
    V=s.diff(g,t)*f+g*phi
    ck(s.simplify(s.integrate(V,(t,0,T))-phi)==0,'right exact phase')
    ck(s.simplify(s.integrate(V.subs(u,z-2*c*t),(t,0,T)))==0,'left exact cancellation')
    ck(s.integrate(phi,(u,-1,1))==0,'zero total phase')
    ck(s.integrate(phi,(u,-1,0))==1,'primitive maximum')
    P=96/(25*s.sqrt(5))
    ck(s.simplify(-phi.subs(u,1/s.sqrt(5))-P)==0,'exact interior peak')
    ck(s.expand(s.diff(phi,u)+6*(u-1)*(u+1)*(5*u*u-1))==0,'all stationary points')
    energy=s.integrate(s.diff(phi,u)**2,(u,-1,1))
    ck(energy>0,'finite phase-gradient energy')
    hleft=triangle_height*t/T**2;hright=triangle_height*(T-t)/T**2
    ck(s.simplify(s.integrate(hleft,(t,0,T/2))+s.integrate(hright,(t,T/2,T))-1)==0,'triangle normalization')
    ck(s.simplify(hleft.subs(t,T/2)-2/T)==0,'triangle peak')
    d=s.symbols('d',positive=True)
    cut=s.integrate(z,(z,0,d/2))+s.integrate(d-z,(z,d/2,d))
    ck(s.simplify(cut-d*d/4)==0,'untruncated cut capacity')
    ck(s.simplify(2*c/cut.subs(d,2*c*T)-2/(c*T*T))==0,'physical cut coefficient')
    A,P0,M,L=s.symbols('A P M L',positive=True)
    bound=2*A/(c*T*T)+2*P0/T
    ck(s.limit(T*T*bound,T,0)==2*A/c,'short squeeze upper constant')
    ck(s.limit(T*P0/(T-L/c),T,s.oo)==P0,'long squeeze upper constant')
    ts=(P0+s.sqrt(P0**2+2*M*A/c))/M
    ck(s.simplify(bound.subs(T,ts)-M)==0,'duration quadratic')
    # Long-time common rectangle: take L=1,d=4 and normalized quadratic z density.
    h=s.Rational(3,4)*(z-1)*(3-z)
    ck(s.integrate(h,(z,1,3))==1,'common rectangle density')
    ck(s.simplify(s.integrate(phi*h,(z,1,3))-phi)==0,'long pulse right marginal')
    ck(s.integrate(phi*h,(u,-1,1))==0,'long pulse left marginal')
    # Expanded-plateau primitive: exact polygon before endpoint-preserving smoothing.
    ell=s.Rational(1);eps=s.Rational(1,10);theta=s.Rational(1)
    Ae=theta*(ell+2*eps)/4
    ck(Ae==s.Rational(3,10),'expanded primitive norm')
    ck(-Ae+theta*(ell+2*eps)/2==Ae,'plateau derivative integrates between extrema')
    ck(theta*ell/4< Ae,'strict primitive slack')
    ck(s.limit(theta*(ell+2*s.Symbol('e'))/2,s.Symbol('e'),0)==theta*ell/2,'optimized short coefficient')
    ck((3+ell)/ell==4,'energy-profile versus peak-profile ratio')
    hh,tt=s.symbols('hh tt',positive=True)
    transition=hh*(1-t/tt)**2
    area=s.integrate(transition,(t,0,tt));eng=s.integrate(s.diff(transition,t)**2,(t,0,tt))
    ck(s.simplify(area*eng-4*hh**3/9)==0,'sharp transition area-energy constant')
    ck(s.simplify(16*(theta/2)**3/9-2*theta**3/9)==0,'four-transition centered coefficient')
    return {'math_checks':n,'polynomial_energy':str(energy),'polynomial_peak':str(P),'short_constant':'2*||F||_infinity/c','long_constant':'||phi||_infinity','scope':'fixed smooth zero-area phase; infima, not smooth threshold attainment'}
def pins():
    p='explorations/conditional-build/k1914-scalar-control-transport-cuts-2026-10-21.md'
    return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');a=ap.parse_args();r=calculate();r['dependency_sha256']=pins()
    if a.write_report:(ROOT/'lab/process/k1915-scalar-pulse-duration-limits.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r))
