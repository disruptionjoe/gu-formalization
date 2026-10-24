"""Exact rational certificates for the coupled nonlinear wing corner.

The continuum theorem is proved in the exploration. Finite algebraic controls
and interval certificates below are not a substitute for that proof.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import json

from k1969_scalar_continuum_separation import isolate, ip, iv, K, D

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'lab/process/k2005-coupled-wing-potentials.json'
DEN = 10**250
TERMS = 16


def rounded(x):
    return F((x[0]*DEN).__floor__(), DEN), F((x[1]*DEN).__ceil__(), DEN)


def plus(a, b):
    return rounded((a[0]+b[0], a[1]+b[1]))


def times(a, b):
    assert min(a+b) >= 0
    return rounded((a[0]*b[0], a[1]*b[1]))


def divide(a, b):
    assert a[0] >= 0 and b[0] > 0
    return rounded((a[0]/b[1], a[1]/b[0]))


def exponential(x):
    """Positive Taylor series, geometric bound on its entire omitted tail."""
    assert 0 <= x <= 4
    count = 100
    value = sum(x**j/factorial(j) for j in range(count))
    first = x**count/factorial(count)
    return rounded((value, value+first/(1-x/F(count+1))))


def spectral_at(r):
    q = exponential(r)
    # q+1/q is increasing above one, so use paired endpoints.
    return rounded((2*(q[0]+1/q[0]-2)/(r*r),
                    2*(q[1]+1/q[1]-2)/(r*r)))


def parameters():
    t = isolate()
    kappa = rounded((2+3/(2*t[1]), 2+3/(2*t[0])))
    eta = divide(iv(ip(D, t), ip(K, t)), (F(23, 50), F(23, 50)))
    low, high = F(3), F(4)
    assert spectral_at(low)[1] < kappa[0]
    assert spectral_at(high)[0] > kappa[1]
    for _ in range(70):
        mid = (low+high)/2
        val = spectral_at(mid)
        if val[1] < kappa[0]:
            low = mid
        elif val[0] > kappa[1]:
            high = mid
        else:
            raise AssertionError('root interval precision exhausted')
    r = (low, high)
    q = (exponential(low)[0], exponential(high)[1])
    return t, kappa, eta, r, q


def spectrum(n, r, q):
    return rounded((2*(q[0]**n+q[0]**(-n)-2)/(n*n*r[1]**2),
                    2*(q[1]**n+q[1]**(-n)-2)/(n*n*r[0]**2)))


def coefficients(kappa, eta, r, q, count=TERMS):
    cs = [(F(0), F(0)), (F(1), F(1))]
    ds = [(F(0), F(0))]
    for n in range(2, count+1):
        lam = spectrum(n, r, q)
        gap = (lam[0]-kappa[1], lam[1]-kappa[0])
        convolution = (F(0), F(0))
        for i in range(1, n):
            convolution = plus(convolution, times(cs[i], cs[n-i]))
        cs.append(divide(times(eta, convolution), gap))
    for n in range(1, count+1):
        factor = (2*(q[0]**n-1)/(n*r[1]), 2*(q[1]**n-1)/(n*r[0]))
        ds.append(times(cs[n], factor))
    return cs, ds


def evaluate(cs, z):
    total = (F(0), F(0))
    for n, c in enumerate(cs[1:], 1):
        total = plus(total, times(c, (z[0]**n, z[1]**n)))
    return total


def s_tail(z, count=TERMS):
    ratio = 4*z/125
    assert 0 <= ratio < 1
    return rounded((F(0), z*ratio**count/(1-ratio)))[1]


def d_tail(z, count=TERMS):
    # q<55, r>3, 1/n<=1, and c_n<=(4/125)^(n-1).
    return rounded((F(0), F(2, 3)*s_tail(55*z, count)))[1]


def row_shortfall_bound(z, count):
    rho = 4*z/125
    assert 0 <= rho < 1 and count >= 1
    return rounded((F(0), F(4, 25)*z*z*rho**(count-1)
                    *(count-(count-1)*rho)/(1-rho)**2))[1]


def rational_coefficients(q, r_squared, eta, count):
    """Algebra controls at rational symbolic-parameter substitutions.

    q and r_squared are independent here; these are coefficient identities,
    not a claim that log(q)^2 equals the supplied rational r_squared.
    """
    lam = lambda n: 2*(q**n+q**(-n)-2)/(n*n*r_squared)
    cs = [F(0), F(1)]
    for n in range(2, count+1):
        cs.append(eta*sum(cs[i]*cs[n-i] for i in range(1, n))/(lam(n)-lam(1)))
    return cs, lam


def produce():
    t, kappa, eta, r, q = parameters()
    cs, ds = coefficients(kappa, eta, r, q)
    gap = (spectrum(2, r, q)[0]-kappa[1], spectrum(2, r, q)[1]-kappa[0])
    checks = 0
    assert F(0) < eta[0] < eta[1] < F(4, 25)
    assert gap[0] > 20 and 20 < q[0] < q[1] < 55
    assert 3 < r[0] < r[1] < 4
    checks += 3
    for n in range(1, TERMS+1):
        majorant = F(comb(2*n-2, n-1), n)*F(1, 125)**(n-1)
        assert cs[n][0] > 0 and cs[n][1] <= majorant
        checks += 1
    for q0 in [F(2), F(5), F(20), F(40)]:
        for eta0 in [F(1, 10), F(1, 7)]:
            cc, lam = rational_coefficients(q0, F(11), eta0, 12)
            for n in range(2, 13):
                assert (lam(n)-lam(1))*cc[n] == eta0*sum(cc[i]*cc[n-i] for i in range(1, n))
                assert lam(n) > lam(n-1)
                checks += 2
    z0 = F(1, 1000)
    s0 = evaluate(cs, (z0, z0))
    s0 = (s0[0], s0[1]+s_tail(z0))
    w0 = (z0/q[1], z0/q[0])
    d0 = evaluate(ds, w0)
    d0 = (d0[0], d0[1]+d_tail(w0[1]))
    inner_s = evaluate(cs, w0)
    inner_s = (inner_s[0], inner_s[1]+s_tail(w0[1]))
    assert s0[1] < F(1, 999) < 3-t[1]
    assert F(19, 40000) < d0[0] < d0[1] < F(2, 2997) < 3-t[1]
    assert F(1, 55000) < inner_s[0] < 1-t[1]
    assert F(1, 2500) < d0[0]
    checks += 4
    consumers = []
    for count in [2, 4, 8, 16]:
        consumers.append(dict(terms=count, S_at_z0_tail_upper=str(s_tail(z0, count)),
                              D_at_z0_over_q_tail_upper=str(d_tail(w0[1], count)),
                              finite_row_shortfall_at_z0_upper=str(row_shortfall_bound(z0, count))))
        assert s_tail(z0, count) > 0 and d_tail(w0[1], count) > 0
        checks += 2
    # Known strict cut mismatch of any globally nondecreasing-in-y wing.
    cut_upper = ((3-t[0])-F(9, 2))/2+1/(8*F(23, 100))
    assert cut_upper < -F(397, 920)
    checks += 1
    refs = ['tests/channel-swings/k1969_scalar_continuum_separation.py',
            'explorations/conditional-build/k1991-tight-cut-pulse-factorization-2026-10-23.md',
            'explorations/conditional-build/k2003-exact-central-pulse-optimizer-2026-10-23.md']
    return dict(result_id='K2005', status='active_research', classification='INTERNAL_STRUCTURAL_ONLY',
                target_claim='NONE-NOT-A-KILL',
                t_interval=list(map(str, t)), kappa_interval=list(map(str, kappa)),
                eta_interval=list(map(str, eta)), r_interval=list(map(str, r)),
                exp_r_interval=list(map(str, q)), spectral_gap_2_interval=list(map(str, gap)),
                coefficient_intervals=[list(map(str, c)) for c in cs[1:]],
                D_coefficient_intervals=[list(map(str, d)) for d in ds[1:]],
                S_z0_interval=list(map(str, s0)), D_z0_over_exp_r_interval=list(map(str, d0)),
                S_z0_over_exp_r_interval=list(map(str, inner_s)),
                certified_actual_row_interval=['0', '1/55000'],
                certified_actual_terminal_column_interval=['0', '1/2500'],
                z0=str(z0), coefficient_majorant='Catalan(n-1)/125^(n-1)',
                truncation_consumers=consumers,
                common_monotone_cut_excess_upper=str(cut_upper),
                exact_rational_controls=checks,
                scope='Exact entire inverse-potential construction for quadratic half-plane row mass and linear column deficit; simultaneous restricted actual wing rows and columns. Global restriction fails the inherited monotone cut. Endpoint-singularity theorem applies to any finite-a.e clipped-additive feasible wing; it does not assert such a global representation exists. No full wing feasibility, global dual attainment, whole-pulse norm improvement, smoothness, GU verdict or novelty.',
                inputs={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = produce()
    if args.check:
        assert json.loads(OUT.read_text()) == data, 'certificate differs from exact replay'
    else:
        OUT.write_text(json.dumps(data, indent=2)+'\n')
    print(f"PASS K2005 producer: {data['exact_rational_controls']} exact rational controls")
