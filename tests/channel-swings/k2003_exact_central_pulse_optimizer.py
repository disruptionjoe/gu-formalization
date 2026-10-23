"""Exact renewal/quantile central optimizer and rational norm certificates.

Only stdlib exact arithmetic. Infinite-dimensional assertions are proved in
the accompanying artifact; finite controls do not replace those proofs.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import json
from k1969_scalar_continuum_separation import isolate

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'lab/process/k2003-exact-central-pulse-optimizer.json'
M = F(23, 100)
TERMS = 48
DEN = 10**25


def rounded(interval):
    lo, hi = interval
    return F((lo * DEN).__floor__(), DEN), F((hi * DEN).__ceil__(), DEN)


def clipped_second_moment(d):
    """E[min(1,S_d^2)], d odd, using one central Irwin-Hall piece."""
    assert d > 0 and d % 2
    deficit = F(0)
    for j in range((d + 1) // 2):
        a = d - 2*j
        def primitive(z):
            return (F((1-a*a)*z**d, d)
                    + F(2*a*z**(d+1), d+1)
                    - F(z**(d+2), d+2))
        deficit += (-1)**j * comb(d, j) * (primitive(a+1)-primitive(a-1))
    return 1 - deficit / (2**d * factorial(d-1))


def spline_cdf(d, x):
    return sum(F((-1)**j * comb(d, j)) * max(F(0), x+d-2*j)**d
               for j in range(d+1)) / (2**d * factorial(d))


def stopped_weights(alpha, n):
    return [(1-alpha)*alpha**j for j in range(n)] + [alpha**n]


def sinh_interval(x, terms=16):
    assert 0 < x <= 2
    partial=sum(x**(2*j+1)/factorial(2*j+1) for j in range(terms))
    first=x**(2*terms+1)/factorial(2*terms+1)
    ratio=x*x/F((2*terms+2)*(2*terms+3))
    return partial, partial+first/(1-ratio)


def mixture_cdf(alpha, n, x, extra=0):
    return sum(w*spline_cdf(2*j+1+extra, x)
               for j, w in enumerate(stopped_weights(alpha, n)))


def norm_interval(alpha, terms=TERMS):
    a, b = alpha
    lo = hi = F(0)
    cs = []
    for n in range(terms):
        c = clipped_second_moment(2*n+1)
        assert 0 < c < 1
        cs.append(c)
        l, h = rounded(((1-b)**2*(n+1)*a**n*c,
                        (1-a)**2*(n+1)*b**n*c))
        lo += l
        hi += h
    # Exact total omitted negative-binomial weight; increasing in alpha.
    tail = b**terms * ((terms+1)-terms*b)
    return rounded((lo, hi+tail)), cs, rounded((0, tail))[1]


def produce():
    t = isolate()
    alpha = tuple(4*x/(3+4*x) for x in t)
    norm, cs, tail = norm_interval(alpha)
    area = tuple(2*x*(3+4*x) for x in t)
    central = rounded((M*M*area[0]*norm[0], M*M*area[1]*norm[1]))
    uncapped = tuple(M*M*(2*x+F(16, 3)*x*x) for x in t)
    cap_cost = rounded((central[0]-uncapped[1], central[1]-uncapped[0]))
    whole_upper = rounded((0, M*M*(54-area[0])+central[1]))[1]
    inherited_lower = F(json.loads((ROOT/'lab/process/k1989-capped-pulse-dual-certificates.json').read_text())['certificate']['squared_norm_lower_bound'])
    checks = 0
    assert cs[0] == F(1, 3) and cs[1] == F(8, 15) and cs[2] == F(391, 630)
    checks += 3
    for a in [F(1, 4), F(3, 8), F(1, 2), F(3, 4)]:
        for n in range(8):
            ws = stopped_weights(a, n)
            assert sum(ws) == 1 and min(ws) > 0
            # Density renewal defect coefficients, in odd convolution powers.
            residual = [F(0)]*(n+2)
            residual[0] -= 1-a
            for j, w in enumerate(ws):
                residual[j] += w
                residual[j+1] -= a*w
            expected = [F(0)]*(n+2)
            expected[n] = a**(n+1)
            expected[n+1] = -a**(n+1)
            assert residual == expected
            assert sum((j+1)*(1-a)**2*a**j for j in range(n+1)) + a**(n+1)*((n+2)-(n+1)*a) == 1
            checks += 3
    for a in [F(3, 8), F(1, 2)]:
        for n in range(4):
            for x in [F(-3, 2), F(-1, 2), F(0), F(1, 2), F(3, 2)]:
                assert mixture_cdf(a, n, -x) == 1-mixture_cdf(a, n, x)
                # Integrated row defect from the exact renewal identity.
                defect = 2*a**(n+1)*(spline_cdf(2*n+3, x)-spline_cdf(2*n+1, x))
                assert abs(defect) <= 2*a**(n+1)
                checks += 2
    assert F(49, 100) < norm[0] < norm[1] < F(1, 2)
    assert whole_upper < F(274, 100) and inherited_lower < whole_upper
    assert central[1] < F(115, 1000)
    assert F(8, 1000) < cap_cost[0] < cap_cost[1] < F(9, 1000)
    checks += 4
    wing_margin_upper = ((3-t[0])-F(9, 2))/2 + 1/(8*M)
    assert wing_margin_upper < -F(397, 920)
    checks += 1
    kappa=(2+3/(2*t[1]),2+3/(2*t[0]))
    left=sinh_interval(F(2))
    right=sinh_interval(F(3,2))
    assert F(1,4)*left[0]**2 > kappa[1]/2
    assert F(4,9)*right[1]**2 < kappa[0]/2
    checks += 2
    # Rational, deliberately conservative replacement for the square-root factor.
    # alpha<2/5 gives variance<7/9<1, hence C(alpha)<27/5.
    assert alpha[1] < F(2, 5)
    consumers = []
    for n in [4, 8, 16, 32]:
        eps = alpha[1]**(n+1)
        consumers.append(dict(stopping_index=n,
                              row_uniform_error_upper=str(rounded((0, 2*eps))[1]),
                              normalized_strong_error_squared_upper=str(rounded((0, F(27, 5)*eps))[1])))
    refs = ['tests/channel-swings/k1969_scalar_continuum_separation.py',
            'explorations/conditional-build/k1991-tight-cut-pulse-factorization-2026-10-23.md',
            'lab/process/k1989-capped-pulse-dual-certificates.json']
    return dict(result_id='K2003', status='active_research',
                classification='INTERNAL_STRUCTURAL_ONLY', target_claim='NONE-NOT-A-KILL',
                root_interval=list(map(str, t)), alpha_interval=list(map(str, alpha)),
                normalized_central_minimum_squared_norm_interval=list(map(str, norm)),
                central_minimum_squared_norm_interval=list(map(str, central)),
                central_cap_cost_squared_norm_interval=list(map(str, cap_cost)),
                nondecreasing_wing_necessary_inequality_excess_upper=str(wing_margin_upper),
                wing_extension_scope='Excludes a common nondecreasing column direction for all rows, and separately a common nonincreasing direction. Does not exclude mixed row orientations, nonmonotone potentials or feasible wings.',
                leading_corner_model=dict(kappa_interval=list(map(str,kappa)),
                    c_bracket=['1/4','1/3'],
                    defining_equation='4*c^2*sinh(1/(2*c))^2=kappa/2',
                    formula='h(s,delta)=clip_[0,1](d+c*log(s/delta)); d=(1+c*log(2*kappa))/2',
                    cutoffs='Row kappa*s only when b*s<height; column deficit delta/2 only when delta/a<width. On wing row height=L+s and column width=L.',
                    row_only_quadratic_repair='chi(s)=s+(eta/kappa)*s^2 matches exact inner-row H but gives strictly insufficient column deficit, since ds/dr=1/sqrt(1+4*(eta/kappa)*r)<1 for r>0.',
                    scope='Leading half-plane boundary model / restricted inner traces only; does not match eta*s^2, all rows and columns of one finite rectangle, or global wing. No gluing or global dual certificate.'),
                whole_pulse_squared_norm_upper_bound=str(whole_upper),
                inherited_squared_norm_lower_bound=str(inherited_lower),
                whole_pulse_distance_to_k1989_squared_upper_bound=str(whole_upper-inherited_lower),
                convolution_terms=TERMS, norm_series_tail_upper=str(tail),
                first_clipped_moments=[str(x) for x in cs[:8]],
                approximation_consumers=consumers, exact_rational_controls=checks,
                scope='Exact unique central minimum-norm pulse by geometric convolution densities, inverse CDFs and clipping, with exact continuum marginals, attained dual potentials, finite-convolution cap-preserving approximants with exact columns and explicit row/strong errors. A common monotone column direction cannot extend this construction to the actual wing. Whole-pulse upper uses inherited wing existence; no explicit wings, full minimum norm, phase-energy change, novelty or GU verdict.',
                inputs={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = produce()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2)+'\n')
    else:
        assert result == json.loads(OUT.read_text())
    print('PASS K2003', result['exact_rational_controls'], 'exact controls; central',
          *[float(F(x)) for x in result['central_minimum_squared_norm_interval']],
          'whole upper', float(F(result['whole_pulse_squared_norm_upper_bound'])))
