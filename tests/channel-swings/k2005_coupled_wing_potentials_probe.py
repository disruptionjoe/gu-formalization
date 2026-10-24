"""Independent symbolic integrals, exact coefficient tests, and hostile inputs.

Does not import producer code. Checked mathematical identities and rigorous
interval containment are distinct from the exploration's continuum proof.
"""
from copy import deepcopy
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT/'lab/process/k2005-coupled-wing-potentials.json').read_text())
COUNTS = {'symbolic_integrals': 0, 'rational_identities': 0, 'interval_certificates': 0}


def check(ok, label, kind='rational_identities'):
    if not ok:
        raise AssertionError('[FAIL] '+label)
    COUNTS[kind] += 1


def exponential_bounds(x):
    # Independent 120-term positive series, including the last term in sum.
    last = F(1)
    partial = last
    for j in range(1, 121):
        last *= x/j
        partial += last
    first = last*x/121
    return partial, partial+first/(1-x/122)


def cosh_bounds(x):
    partial = sum(x**(2*j)/factorial(2*j) for j in range(80))
    first = x**160/factorial(160)
    return partial, partial+first/(1-x*x/F(161*162))


def interval(key):
    return tuple(map(F, DATA[key]))


def poly(c, x):
    return sum(a*x**i for i, a in enumerate(c))


def product(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def fixture(q, r, eta, count):
    # The factor arises from the independently integrated layer-cake formula.
    eigen = [F(0)]+[2*(q**n-1)*(1-q**(-n))/(n*n*r*r) for n in range(1, count+1)]
    coeff = [F(0), F(1)]
    for n in range(2, count+1):
        squared = product(coeff, coeff)
        coeff.append(eta*squared[n]/(eigen[n]-eigen[1]))
    dcoeff = [F(0)]+[2*coeff[n]*(q**n-1)/(n*r) for n in range(1, count+1)]
    sq = product(coeff, coeff)
    return dict(q=q, r=r, eta=eta, count=count, eigen=eigen, coeff=coeff,
                dcoeff=dcoeff, defect=[F(0)]*(count+1)+[eta*x for x in sq[count+1:]])


def verify_fixture(data):
    q, r, eta, count = (data[k] for k in ['q', 'r', 'eta', 'count'])
    c, d, eig = (data[k] for k in ['coeff', 'dcoeff', 'eigen'])
    sq = product(c, c)
    for n in range(1, count+1):
        # Column layer-cake integrates S(w exp(rt)), independently of D.
        check(c[n]*(q**n-1)/(n*r) == d[n]/2, 'exact column multiplier')
        # Row integrates D(z exp(-rt)); compare directly with its spectrum.
        check(d[n]*(1-q**(-n))/(n*r) == eig[n]*c[n], 'exact row multiplier')
        check((eig[n]-eig[1])*c[n] == eta*sq[n], 'nonlinear coefficient recurrence')
    for n in range(1, 2*count+1):
        row = d[n]*(1-q**(-n))/(n*r) if n <= count else 0
        target = eig[1]*(c[n] if n <= count else 0)+eta*sq[n]
        check(target-row == data['defect'][n], 'finite row shortfall polynomial')
    check(all(x>0 for x in data['defect'][count+1:]), 'strict positive finite shortfall')
    if count >= 2:
        U = -c[2]/r
        V = d[2]/(r*d[1]*d[1])
        a, b = d[1]/q, d[1]
        check(U*(b-a)+V*(b*b-a*a)/2 == eta, 'coupled quadratic row correction')
        check(U*(1/a**2-1/b**2)/2+V*(1/a-1/b) == 0, 'coupled quadratic column cancellation')


def symbolic_checks():
    u, k = sp.symbols('u k', real=True, positive=True)
    value = 2*(sp.integrate((1+u)*sp.exp(k*u), (u, -1, 0))
               +sp.integrate((1-u)*sp.exp(k*u), (u, 0, 1)))
    check(sp.simplify(value-2*(sp.exp(k)+sp.exp(-k)-2)/k**2) == 0,
          'triangular spectral integral', 'symbolic_integrals')
    v = sp.symbols('v', real=True)
    check(sp.simplify(sp.integrate(sp.exp(-k*v), (v, 0, 1))-(1-sp.exp(-k))/k) == 0,
          'row layer-cake integral', 'symbolic_integrals')
    check(sp.simplify(sp.integrate(sp.exp(k*v), (v, 0, 1))-(sp.exp(k)-1)/k) == 0,
          'column layer-cake integral', 'symbolic_integrals')
    rho = sp.symbols('rho', real=True)
    for n in [1, 2, 4, 8, 16]:
        # Differentiating the geometric series gives the infinite shortfall bound.
        tail = sp.diff(rho**n/(1-rho), rho)
        expected = rho**(n-1)*(n-(n-1)*rho)/(1-rho)**2
        check(sp.simplify(tail-expected) == 0, 'differentiated geometric tail', 'symbolic_integrals')


def interval_checks():
    tl, th = interval('t_interval')
    kap = interval('kappa_interval')
    eta = interval('eta_interval')
    rr, qq = interval('r_interval'), interval('exp_r_interval')
    p = list(map(F, [-138, 392, -168, -102, 101]))
    check(poly(p, tl)<0<poly(p, th), 'algebraic t sign enclosure', 'interval_certificates')
    check(F(9,20)<tl<th<F(23,50), 'actual root bracket', 'interval_certificates')
    check(kap[0]<=2+3/(2*th)<=2+3/(2*tl)<=kap[1], 'kappa enclosure', 'interval_certificates')
    # Independent positive/negative monomial enclosures for K(t),D(t).
    # These are broader than Horner bounds; certify eta's required uniform bound.
    kval=(F(1,6)-th**2/2+2*tl**3/3-th**4/4,
          F(1,6)-tl**2/2+2*th**3/3-tl**4/4)
    dval=(-F(7,100)+F(69,200)*tl-F(77,200)*th**2,
          -F(7,100)+F(69,200)*th-F(77,200)*tl**2)
    check(0<dval[0]/kval[1]/F(23,50)<dval[1]/kval[0]/F(23,50)<F(4,25),
          'independent eta bound', 'interval_certificates')
    # Pin the narrow certificate to the actual rational function, not just
    # its coarse positive bound. Sign-certify D'K-DK' on the root bracket.
    kp=[F(1,6),F(0),-F(1,2),F(2,3),-F(1,4)]
    dp=[-F(7,100),F(69,200),-F(77,200)]
    left=product([i*dp[i] for i in range(1,len(dp))],kp)
    right=product(dp,[i*kp[i] for i in range(1,len(kp))])
    numerator=[left[i]-right[i] for i in range(len(left))]
    derivative_lo=sum(c*(tl if c>=0 else th)**i for i,c in enumerate(numerator))
    check(derivative_lo>0, 'actual eta derivative sign', 'interval_certificates')
    elo=poly(dp,tl)/poly(kp,tl)/F(23,50)
    ehi=poly(dp,th)/poly(kp,th)/F(23,50)
    check(eta[0]<=elo<=ehi<=eta[1], 'recorded actual eta enclosure', 'interval_certificates')
    for endpoint, side in [(rr[0], 'lower'), (rr[1], 'upper')]:
        cb=cosh_bounds(endpoint)
        spectral=(4*(cb[0]-1)/endpoint**2, 4*(cb[1]-1)/endpoint**2)
        check(spectral[1]<kap[0] if side=='lower' else spectral[0]>kap[1],
              'independent cosh root endpoint '+side, 'interval_certificates')
    check(qq[0]<exponential_bounds(rr[0])[0] and exponential_bounds(rr[1])[1]<qq[1],
          'independent exponential enclosure', 'interval_certificates')
    check(3<rr[0]<rr[1]<4 and 20<qq[0]<qq[1]<55,
          'coarse actual transcendental bounds', 'interval_certificates')
    cs=[(F(0),F(0))]+[tuple(map(F,x)) for x in DATA['coefficient_intervals']]
    ds=[(F(0),F(0))]+[tuple(map(F,x)) for x in DATA['D_coefficient_intervals']]
    check(cs[1]==(F(1),F(1)), 'coefficient normalization c1', 'interval_certificates')
    check(all(0<x[0]<=x[1] for x in cs[1:]+ds[1:]),
          'positive ordered coefficient enclosures', 'interval_certificates')
    for n in range(2,len(cs)):
        lo=2*(qq[0]**n+qq[0]**(-n)-2)/(n*n*rr[1]**2)-kap[1]
        hi=2*(qq[1]**n+qq[1]**(-n)-2)/(n*n*rr[0]**2)-kap[0]
        convlo=sum(cs[i][0]*cs[n-i][0] for i in range(1,n))
        convhi=sum(cs[i][1]*cs[n-i][1] for i in range(1,n))
        check(cs[n][0]<=eta[0]*convlo/hi<=eta[1]*convhi/lo<=cs[n][1],
              'certificate nonlinear enclosure '+str(n), 'interval_certificates')
    for n in range(1,len(cs)):
        check(ds[n][0]<=2*cs[n][0]*(qq[0]**n-1)/(n*rr[1])
              <=2*cs[n][1]*(qq[1]**n-1)/(n*rr[0])<=ds[n][1],
              'certificate D enclosure '+str(n), 'interval_certificates')
        check(cs[n][1]<=F(comb(2*n-2,n-1),n)/125**(n-1),
              'Catalan majorant '+str(n), 'interval_certificates')
    z0=F(DATA['z0'])
    check(z0==F(1,1000) and z0/(1-4*z0/125)<F(1,999)<3-th,
          'actual row support cutoff', 'interval_certificates')
    check(z0/55==F(1,55000) and F(2,3)*z0/(1-4*z0/125)<3-th,
          'actual terminal column support cutoff', 'interval_certificates')
    check(F(19,40000)>F(1,2500) and F(1,55000)<1-th,
          'simultaneous rational trace intervals', 'interval_certificates')
    for row in DATA['truncation_consumers']:
        n=row['terms']; rho=4*z0/125
        check(F(row['S_at_z0_tail_upper'])>=z0*rho**n/(1-rho),
              'S tail consumer '+str(n), 'interval_certificates')
        dz=55*z0/qq[0]; drho=4*dz/125
        check(F(row['D_at_z0_over_q_tail_upper'])>=F(2,3)*dz*drho**n/(1-drho),
              'D tail consumer '+str(n), 'interval_certificates')
        check(F(row['finite_row_shortfall_at_z0_upper'])>=F(4,25)*z0*z0*rho**(n-1)*(n-(n-1)*rho)/(1-rho)**2,
              'finite row shortfall consumer '+str(n), 'interval_certificates')
    excess=((3-tl)-F(9,2))/2+1/(8*F(23,100))
    check(F(DATA['common_monotone_cut_excess_upper'])==excess<-F(397,920),
          'actual global monotone cut failure', 'interval_certificates')


def main():
    symbolic_checks()
    for q in [F(2), F(7), F(30)]:
        for count in [1, 2, 4, 8, 12]:
            verify_fixture(fixture(q, F(3), F(1,7), count))
    interval_checks()
    baseline=dict(COUNTS)
    print('PASS K2005 probe clean baseline: '+json.dumps(baseline, sort_keys=True))
    clean=fixture(F(7),F(3),F(1,7),8)
    mutations=[]
    bad=deepcopy(clean); bad['dcoeff'][2]/=2
    mutations.append(('missing D factor two',bad))
    bad=deepcopy(clean); bad['eigen'][3]*=3
    mutations.append(('missing spectral denominator factor n',bad))
    bad=deepcopy(clean); bad['coeff'][2]*=-1; bad['dcoeff'][2]*=-1
    mutations.append(('wrong nonlinear coefficient sign',bad))
    bad=deepcopy(clean); bad['defect'][9]=0
    mutations.append(('omitted high-order finite row product',bad))
    for name,bad in mutations:
        try:
            verify_fixture(bad)
        except AssertionError as exc:
            if not str(exc).startswith('[FAIL] '):
                raise
            print('CAUGHT '+name+': '+str(exc))
        else:
            raise AssertionError('mutation escaped: '+name)
    print('PASS K2005 mathematical corruptions: 4/4; baseline '+str(sum(baseline.values()))+' controls')


if __name__=='__main__':
    main()
