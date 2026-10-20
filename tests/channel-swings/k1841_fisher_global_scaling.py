#!/usr/bin/env sage-python
"""Exact algebra supporting the written uniform compactness and endpoint proof.

Symbolic identities are algebraic evidence; the analytic inequalities and
quantifiers are proved in the accompanying research note, not by these totals.
"""
import argparse
import hashlib
import json
from pathlib import Path
from sage.all import QQ, PolynomialRing, PowerSeriesRing, QuadraticField, matrix, SR, sqrt

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'lab/process/k1841-fisher-global-scaling.json'


def produce():
    checks = {}
    def ck(name, value):
        checks[name] = bool(value)
        assert value, name

    P = PolynomialRing(QQ, ['alpha', 'beta', 'gamma', 'xi'])
    alpha, beta, gamma, xi = P.gens()
    F = P.fraction_field()
    moments = [P(1), P(0), P(1), alpha, 3 + beta,
               10 * alpha + gamma, 15 + 15 * beta + 10 * alpha**2 + xi]
    q2 = {2: P(1), 0: P(-1), 1: -alpha}
    q3 = {3: P(1), 1: -3-beta, 0: -alpha}
    def ex(poly):
        return sum(co * moments[n] for n, co in poly.items())
    def inner(poly, other):
        return sum(co * do * moments[n+m]
                   for n, co in poly.items() for m, do in other.items())
    for number, poly, cov in [(2, q2, alpha), (3, q3, beta)]:
        ck(f'q{number}_centered', ex(poly) == 0)
        ck(f'q{number}_orthogonal_linear', inner(poly, {1: 1}) == 0)
        ck(f'q{number}_score_covariance',
           -sum(n * co * moments[n-1] for n, co in poly.items() if n) == cov)
    A = inner(q2, q2)
    B = inner(q2, q3)
    C = inner(q3, q3)
    ck('Gram_A', A == 2+beta-alpha**2)
    ck('Gram_B', B == 6*alpha+gamma-alpha*beta)
    ck('Gram_C', C == 6+9*beta+9*alpha**2+xi-beta**2)
    G = matrix(F, [[A, B], [B, C]])
    cov = matrix(F, 2, 1, [alpha, beta])
    ck('Schur_projection_identity',
       (cov.transpose()*G.inverse()*cov)[0, 0]
       == F(alpha**2)/A + (beta-F(alpha*B)/A)**2/(C-F(B**2)/A))
    ck('Gaussian_Gram_limit', A(alpha=0,beta=0,gamma=0,xi=0) == 2
       and B(alpha=0,beta=0,gamma=0,xi=0) == 0
       and C(alpha=0,beta=0,gamma=0,xi=0) == 6)

    P2 = PolynomialRing(QQ, ['p', 'gap'])
    p, gap = P2.gens()
    lat = lambda n: p*(-(1-p)*gap)**n + (1-p)*(p*gap)**n
    k3 = lat(3)
    k4 = lat(4)-3*lat(2)**2
    k5 = lat(5)-10*lat(2)*lat(3)
    ck('two_atom_cumulant3', k3 == p*(1-p)*(2*p-1)*gap**3)
    ck('two_atom_cumulant4', k4 == p*(1-p)*(1-6*p*(1-p))*gap**4)
    ck('two_atom_cumulant5_ratio',
       k5 == k3*(1-12*p*(1-p))*gap**2)

    P3 = PolynomialRing(QQ, ['z', 'r', 't', 'L', 'S', 'delta'])
    z, r, t, L, S, delta = P3.gens()
    FF = P3.fraction_field()
    pp = FF(r/(z+r))
    ck('radius_fifth_ratio_numerator',
       (1-12*pp*(1-pp))*(z+r)**2 == (z-r)**2-8*z*r)
    ell = FF(z*r*(z-r)/delta**2)
    Q = FF(t*t*delta**2/(L**4*S*S))
    beta_exact = FF(t*t*z*r*((z-r)**2-2*z*r)/(L**4*S*S))
    ck('exact_fourth_coercivity', beta_exact == Q*ell*((z-r)-2*z*r/(z-r)))
    ck('third_normalization',
       FF(t**3*(z*r*(z-r))**2/(2*L**6*S**4))
       == FF(t**3*ell**2*delta**4/(2*L**6*S**4)))
    ck('third_leading_constant', QQ(1)/(2*2**6*(QQ(1)/4)**4) == 2)
    ck('fourth_leading_constant', QQ(1)/(2**4*(QQ(1)/4)**2) == 1)

    H, c = SR.var('H c')
    ll = 2-H+2*sqrt(1-H-c)
    fac = (1-c/ll)/sqrt(1-c/2)
    ck('variance_factor_at_c0', fac.subs(c=0).simplify_full() == 1)
    ck('variance_first_c_zero', fac.diff(c).subs(H=0,c=0) == 0)
    ck('variance_mixed_Hc', fac.diff(c).diff(H).subs(H=0,c=0) == -QQ(1)/8)

    P4 = PolynomialRing(QQ, ['ell', 'x', 'y', 'b', 'd', 'k', 'C'])
    ell, x, y, b, d, k, const = P4.gens()
    FF = P4.fraction_field()
    ck('additive_square', -QQ(3)/2-2*ell+2*ell**2 == -2+2*(ell-QQ(1)/2)**2)
    ck('square_lower_remainder', (b-d)**2-(b*b/2-d*d) == (b-2*d)**2/2)
    ck('young_absorption_positive_horn',
       FF(k*b*b/(2*d)+const**2*d/(2*k)-const*b) == FF((k*b-const*d)**2/(2*k*d)))
    ck('coercivity_small_x', 2*x*x*y-x**3 == x*x*(2*y-x))
    ck('coercivity_small_y', 2*x*x*y-(2*y)**3 == 2*y*(x-2*y)*(x+2*y))
    ck('unique_limit_elimination', 2*x*x*(x/2)-1 == x**3-1)

    K = QuadraticField(3, 's3')
    s3 = K.gen()
    PS = PowerSeriesRing(K, 'e', default_prec=14)
    e = PS.gen()
    aa = PS(QQ(1)/2)-e**2/2
    hh = -PS(1)-e**2
    # Positive branch has constant sqrt(3); the unit series sqrt has constant1.
    bb = (-hh+s3*((hh*hh+4*aa)/3).sqrt())/2
    rr = bb+hh
    weight = rr/(bb+rr)
    noise = 1-((1-e**6/2)/(1-aa*e**8/2)).sqrt()
    ck('z_limit', bb[0] == (1+s3)/2)
    ck('z_next', bb[2] == QQ(1)/2)
    ck('r_limit', rr[0] == (s3-1)/2)
    ck('r_next', rr[2] == -QQ(1)/2)
    ck('weight_limit', weight[0] == (1-1/s3)/2)
    ck('weight_next', weight[2] == -1/(2*s3))
    ck('noise_delta', noise[6] == QQ(1)/4)
    ck('noise_delta_four_thirds', noise[8] == -QQ(1)/8)
    ck('noise_delta_five_thirds', noise[10] == QQ(1)/8)
    ck('inverse_fractional_coefficient_cube', (QQ(3)/8)**3*4**5 == 54)
    ck('inverse_shifted_integer_coefficient', 16*(-QQ(6)/5) == -QQ(96)/5)
    ck('inverse_unshifted_integer_coefficient', 16-QQ(96)/5 == -QQ(16)/5)
    ck('optimized_value_delta', QQ(3)/10-2*(QQ(3)/2)+QQ(2)/3*(QQ(3)/2)**2 == -QQ(6)/5)

    inputs = ['lab/process/k1825-global-q-fisher-transfer.json',
              'lab/process/k1835-fisher-next-endpoint-coefficient.json',
              'lab/process/k1839-fisher-global-merging-coercivity.json']
    return {
        'result_id': 'K1841', 'status': 'active_research',
        'classification': 'INTERNAL_STRUCTURAL_ONLY', 'target_claim': 'NONE-NOT-A-KILL',
        'results': {
            'global_compact_scaling_proved': True,
            'eventual_unique_global_shape_proved': True,
            'global_next_coefficients_proved': True,
            'global_c_asymptotic': 'delta^(4/3)/2-delta^(5/3)/2+O(delta^2)',
            'global_z_asymptotic': '(1+sqrt(3))*delta^(2/3)/2+delta/2+O(delta^(4/3))',
            'global_value_asymptotic': '4/delta-2+3*delta^(2/3)/8-6*delta/5+O(delta^(4/3))',
            'inverse_budget_asymptotic': '4/B-8/B^2+3*cuberoot(2)*B^(-8/3)-16*B^(-3)/5+O(B^(-10/3))',
            'stability_scope': 'fixed small convex (u,y) neighborhood only',
            'effective_onset_proved': False, 'all_q_uniqueness_proved': False,
            'arbitrary_near_minimizer_localization_proved': False,
            'GU_physics_claim': False,
        },
        'Gram': {'A': str(A), 'B': str(B), 'C': str(C)},
        'evidence_kind': 'exact algebra supporting a separately written uniform analytic proof',
        'checks': checks,
        'inputs': {path: hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in inputs},
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    payload = produce()
    if args.write:
        OUT.write_text(json.dumps(payload, indent=2)+'\n')
    else:
        assert payload == json.loads(OUT.read_text()), 'certificate drift'
    print('PASS K1841', len(payload['checks']), 'exact algebraic identity groups')
