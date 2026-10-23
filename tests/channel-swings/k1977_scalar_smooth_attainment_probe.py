"""Independent symbolic marginal, corner and integrated-gap reconstruction."""
from pathlib import Path
import json,hashlib
from fractions import Fraction as F
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def check(fault=None):
    x,y,l,L,h=s.symbols('x y l L h',real=True);a=1+l/2
    phi=x-3+l*(x-2)*(3-x)/2
    if fault=='phase_sign':phi=x-3-l*(x-2)*(3-x)/2
    assert s.diff(phi,x).subs(x,2)==a
    assert s.simplify(s.diff(phi,x).subs(x,2+y)-(a-l*y))==0
    gap=2*s.integrate((a-(L+l)*y)**2,(y,0,h))
    expected=2*a**3/(3*(L+l))
    if fault=='gap_factor':expected*=2
    assert s.simplify(gap.subs(h,a/(L+l))-expected)==0
    # Leibniz identity on actual moving integration limits and characteristic pullback.
    u,z=s.symbols('u z',real=True);V=u*u+3*u*z+2*z*z
    marginal=s.integrate(V,(z,u,u+9))/2
    directional=s.diff(V,u,2)+2*s.diff(V,u,z)+s.diff(V,z,2)
    if fault=='mixed_derivative':directional=s.diff(V,u,2)+s.diff(V,z,2)
    assert s.diff(marginal,u,2)==s.integrate(directional,(z,u,u+9))/2
    # A C1 plateau imposes derivative zero; its Lipschitz ramp reaches area <=L/2.
    assert s.integrate(L*y,(y,0,1))==L/2
    t=s.symbols('t');P=101*t**4-102*t**3-168*t**2+392*t-138
    r=json.loads((ROOT/'lab/process/k1977-scalar-smooth-attainment.json').read_text())
    lo,hi=map(s.Rational,r['root_interval']);assert P.subs(t,lo)<0<P.subs(t,hi)
    if fault=='root':assert P.subs(t,s.Rational(1,2))<0
    la,lb=map(F,r['lambda_interval']);amin=1+la/2;count=6
    for row in r['controls']:
        q=F(row['phase_curvature']);h=F(row['radius']);g=F(row['energy_gap_lower'])
        assert q>=2 and h==amin/(q+lb) and g==2*amin**3/(3*(q+lb));count+=1
    for p,d in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d
    return count
if __name__=='__main__':
    n=check();faults=['phase_sign','gap_factor','mixed_derivative','root']
    for f in faults:
        try:check(f)
        except AssertionError:pass
        else:raise AssertionError('fault survived '+f)
    print('PASS K1977 independent',n,'symbolic/rational obligations;',len(faults),'mathematical faults rejected')
