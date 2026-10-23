"""Independent polynomial integration of renewal, clipping and norm identities."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT/'lab/process/k2003-exact-central-pulse-optimizer.json').read_text())


def cdf(d, x):
    total = F(0)
    for j in range(d+1):
        if x+d-2*j > 0:
            total += (-1)**j*comb(d, j)*(x+d-2*j)**d
    return total/F(2**d*factorial(d))


def density_coefficients(d, interior):
    out = [F(0)]*d
    for j in range(d+1):
        if interior+d-2*j > 0:
            for k in range(d):
                out[k] += F((-1)**j*comb(d, j)*comb(d-1, k)*(d-2*j)**(d-1-k), 2**d*factorial(d-1))
    return out


def integrate(c, lo, hi):
    return sum(v*(hi**(i+1)-lo**(i+1))/(i+1) for i, v in enumerate(c))


def clipped_mean(d, shift):
    pts = sorted({F(-d+2*j) for j in range(d+1)} | {x for x in [-1-shift, 1-shift] if -d < x < d})
    total = F(0)
    for lo, hi in zip(pts, pts[1:]):
        mid = (lo+hi)/2
        p = density_coefficients(d, mid)
        if mid+shift <= -1:
            total -= integrate(p, lo, hi)
        elif mid+shift >= 1:
            total += integrate(p, lo, hi)
        else:
            total += shift*integrate(p, lo, hi)+integrate([F(0)]+p, lo, hi)
    return total


def moment(d):
    # Independent expanded polynomial integral: int_-1^1 (1-s^2)s^k.
    p = density_coefficients(d, F(0))
    return 1-sum(p[k]*F(4, (k+1)*(k+3)) for k in range(0, d, 2))


def weights(a, n):
    return [(1-a)*a**j for j in range(n)]+[a**n]


def mixcdf(a, n, x, extra=0):
    return sum(w*cdf(2*j+1+extra, x) for j, w in enumerate(weights(a, n)))


def main():
    checks = 0
    for d in range(1, 12):
        for b in [F(-5, 4), F(-1, 3), F(0), F(2, 3), F(7, 4)]:
            assert clipped_mean(d, b) == 2*cdf(d+1, b)-1
            checks += 1
    for a in [F(1, 4), F(3, 8), F(2, 3)]:
        for n in range(4):
            ws = weights(a, n)
            for z in [F(-3, 2), F(-1, 4), F(1, 2), F(5, 4)]:
                column = sum(w*clipped_mean(2*j+1, z) for j, w in enumerate(ws))
                assert column == 2*mixcdf(a, n, z, 1)-1
                row = (1-a)*max(F(-1), min(F(1), z))+a*sum(w*clipped_mean(2*j+2, z) for j, w in enumerate(ws))
                defect = row-(2*mixcdf(a, n, z)-1)
                expected = 2*a**(n+1)*(cdf(2*n+3, z)-cdf(2*n+1, z))
                assert defect == expected and abs(defect) <= 2*a**(n+1)
                checks += 2
    a, b = map(F, DATA['alpha_interval'])
    cs = [moment(2*n+1) for n in range(DATA['convolution_terms'])]
    assert list(map(str, cs[:8])) == DATA['first_clipped_moments']
    lo = (1-b)**2*sum((n+1)*a**n*c for n, c in enumerate(cs))
    hi = (1-a)**2*sum((n+1)*b**n*c for n, c in enumerate(cs))
    count = len(cs)
    hi += b**count*((count+1)-count*b)
    published_lo, published_hi = map(F, DATA['normalized_central_minimum_squared_norm_interval'])
    assert published_lo <= lo < hi <= published_hi
    checks += len(cs)+2
    # Independently assemble finite stopped-mixture norms, then test the
    # total-variation consumer against a rigorous infinite-series enclosure.
    for aa in [F(1, 4), F(3, 8), F(2, 3)]:
        partial=(1-aa)**2*sum((j+1)*aa**j*c for j,c in enumerate(cs))
        tail=aa**len(cs)*((len(cs)+1)-len(cs)*aa)
        for n in range(5):
            ws=weights(aa,n)
            finite=(1-aa)*sum(w*cs[i] for i,w in enumerate(ws))
            finite+=aa*sum(w*v*cs[i+j+1] for i,w in enumerate(ws) for j,v in enumerate(ws))
            error=(1+aa)*aa**(n+1)
            assert finite-partial <= error+tail
            assert partial-finite <= error
            checks += 2
    # Independent exact integration of the actual outer-wing polynomial.
    # Its lambda coefficient is negative, so lambda>=0 only strengthens
    # the monotone-extension obstruction at y0=1/2.
    for tt in [F(9,20), F(23,50)]:
        for lam in [F(0), F(1,100), F(1,10)]:
            ell=3-tt; mm=F(23,100); y0=F(1,2)
            h=[2*ell-F(9,2), (1-lam/2)/mm-1, lam/(2*mm)]
            actual=integrate(h,F(0),y0)
            required=(2*ell-y0)*y0/2
            simple=(ell-F(9,2))/2+1/(8*mm)-lam/(24*mm)
            assert actual-required == simple <= -F(397,920)
            checks += 1
    assert F(DATA['nondecreasing_wing_necessary_inequality_excess_upper']) < -F(397,920)
    checks += 1
    # Direct symbolic integration of the restricted clipped-log corner model.
    z=sp.symbols('z',positive=True)
    aa,bb=sp.symbols('aa bb',positive=True)
    cc=1/sp.log(bb/aa)
    dd=cc*sp.log(bb)
    row=aa+sp.integrate(dd-cc*sp.log(z),(z,aa,bb))
    column=1/bb+sp.integrate(1-dd-cc*sp.log(z),(z,1/bb,1/aa))
    assert sp.simplify(sp.expand_log(row-cc*(bb-aa),force=True))==0
    assert sp.simplify(sp.expand_log(column-cc*(1/aa-1/bb),force=True))==0
    checks += 2
    for j in range(1,9):
        # Coefficients of z*cosh(z)-sinh(z) are positive, proving
        # strict increase of sinh(z)/z for z>0, not a sampled derivative.
        assert F(1,factorial(2*j))-F(1,factorial(2*j+1)) == F(2*j,factorial(2*j+1)) > 0
        checks += 1
    ss,beta,rr=sp.symbols('ss beta rr',positive=True)
    chi=ss+beta*ss**2
    inverse=(sp.sqrt(1+4*beta*rr)-1)/(2*beta)
    assert sp.simplify(1+4*beta*chi-(1+2*beta*ss)**2)==0
    assert sp.simplify(sp.diff(inverse,rr)-1/sp.sqrt(1+4*beta*rr))==0
    checks += 2
    # Pointwise projection and dual equality on all three clipping regimes.
    for s in [F(-3), F(-1), F(-1, 4), F(0), F(3, 4), F(1), F(5)]:
        q = max(F(-1), min(F(1), s))
        conjugate = s*s if abs(s) <= 1 else 2*abs(s)-1
        assert 2*s*q-q*q == conjugate
        for v in [F(-1), F(-1, 3), F(0), F(2, 3), F(1)]:
            assert (q-s)*(v-q) >= 0
            checks += 1
    # Four genuine mathematical corruptions, after the green baseline.
    faults = []
    def rejected(name, fn):
        try:
            fn()
        except AssertionError:
            faults.append(name)
        else:
            raise AssertionError('mathematical mutation escaped: '+name)
    def wrong_column_sign():
        assert clipped_mean(3, F(1, 2)) == 1-2*cdf(4, F(1, 2))
    def wrong_cubic_moment():
        assert moment(3) == F(17, 30)
    def wrong_renewal_power():
        aa=F(3, 8); n=2; z=F(1, 2); ws=weights(aa, n)
        row=(1-aa)*z+aa*sum(w*clipped_mean(2*j+2,z) for j,w in enumerate(ws))
        assert row-(2*mixcdf(aa,n,z)-1) == 2*aa**n*(cdf(2*n+3,z)-cdf(2*n+1,z))
    def missing_norm_multiplicity():
        aa=F(3,8)
        # The first-order coefficient of c3 receives BOTH the middle and ramp contribution.
        direct=(1-aa)**2*aa*cs[1]+aa*(1-aa)**2*cs[1]
        assert direct == (1-aa)**2*aa*cs[1]
    for name, fn in [('column sign',wrong_column_sign),('clipped moment',wrong_cubic_moment),('renewal tail power',wrong_renewal_power),('norm multiplicity',missing_norm_multiplicity)]:
        rejected(name,fn)
    assert len(faults)==4
    print('PASS K2003 probe', checks, 'independent exact integration/renewal/dual controls;', len(faults), 'mathematical faults rejected')


if __name__ == '__main__':
    main()
