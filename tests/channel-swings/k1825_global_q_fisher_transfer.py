#!/usr/bin/env python3
"""Exact constants for global-q two-radius attainment and Fisher transfer.

The analytic proof is in the companion exploration. No quadrature is run.
"""
import argparse
import hashlib
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / 'lab/process/k1825-global-q-fisher-transfer.json'
INPUTS = (
    'lab/process/k1757-ou-variational-stability.json',
    'lab/process/k1758-zero-noise-entropy-collar.json',
    'lab/process/k1787-full-fisher-stationary-krawczyk.json',
    'lab/process/k1820-full-fisher-global-optimizer-admission.json',
    'lab/process/k1823-uniform-q-collar.json',
)
Q0 = F(1, 1024)


def ball_endpoints(text):
    match = re.fullmatch(r'\[([+\-0-9.eE]+) \+/- ([+\-0-9.eE]+)\]', text)
    if not match:
        raise ValueError('unsupported decimal ball')
    center, radius = map(F, match.groups())
    if radius < 0:
        raise ValueError('negative radius')
    return center-radius, center+radius


def transfer(scale, value):
    scale, value = F(scale), F(value)
    denominator = 1+(1-scale)*value
    if not (scale > 0 and value >= 0 and denominator > 0):
        raise ValueError('inadmissible transfer denominator or sign')
    return scale*value/denominator


def compact_constants(q):
    q = F(q)
    if not 0 < q < 2:
        raise ValueError('q must belong to (0,2)')
    bound = 4/(2-q)
    n = -(-(2*bound+10).numerator // (2*bound+10).denominator)
    epsilon = F(1, 2**n)
    cmax = 2-q/(1-epsilon)**2
    assert n >= 2*bound+10
    assert 2**n >= n+1 > bound+1
    assert epsilon < 1/(bound+1)
    assert q/2 < (bound/(1+bound))**2  # t0 < B/(1+B)
    assert 0 < cmax < 2-q
    assert F(n-4, 2) >= bound+3
    return {'q': str(q), 'candidate_upper': str(bound), 'noise_exponent': n,
            'noise_floor': str(epsilon), 'compact_c_max': str(cmax),
            'entropy_floor': str(F(n-4, 2))}


def compute():
    inputs = {path: json.loads((ROOT/path).read_text()) for path in INPUTS}
    lower, upper = ball_endpoints(inputs[INPUTS[2]]['certificate']['stationary_value_enclosure'])
    if not inputs[INPUTS[3]]['decision']['global_optimizer_proved']:
        raise ValueError('fixed-q global minimizer is not certified')
    if not inputs[INPUTS[0]]['decision']['explicit_stability_modulus_proved']:
        raise ValueError('missing same-sign coupling input')
    if not inputs[INPUTS[1]]['decision']['rare_atom_zero_noise_joint_corner_covered']:
        raise ValueError('missing entropy collar input')
    if not 0 < lower < upper < F(1, 10**6):
        raise ValueError('unexpected fixed-q value')
    # sqrt(2/q0) < 46, so the lower transfer denominator stays positive
    # on the entire asserted q range, including nonsquare ratios.
    assert 46**2 > 2/Q0 and (46-1)*lower < 1
    lower_rows = [{'q': str(Q0*n*n), 'scale': str(n),
                   'strict_lower': str(transfer(n, lower))}
                  for n in (2, 4, 8, 16, 32, 45)]
    upper_rows = [{'q': str(Q0/F(n*n)), 'scale': str(F(1, n)),
                   'strict_upper': str(transfer(F(1, n), upper))}
                  for n in (2, 4, 8, 16, 32, 64)]
    budgets = []
    for budget in (lower, 2*lower, F(1, 10**6)):
        cap = Q0*(budget/(1+budget)/(lower/(1+lower)))**2
        budgets.append({'budget': str(budget), 'q_cap': str(cap),
                        'meaning': 'q>q0 and V(q)<=budget imply q<q_cap; q=q0 handled separately'})
    inverse_lower = []
    for budget in (upper/2, upper/4, F(1, 10**8)):
        scale = budget*(1+upper)/(upper*(1+budget))
        assert 0 < scale < 1
        inverse_lower.append({'budget': str(budget), 'strict_q_lower': str(Q0*scale*scale)})
    return {
        'schema_version': '1.0', 'claim_id': 'K1825', 'status': 'active_research',
        'scope': 'centered unit-variance symmetric two-radius scalar Gaussian channels; Rademacher and three-point faces included; 0<q<2',
        'input_sha256': {path: hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in INPUTS},
        'fixed_q': {'q0': str(Q0), 'value_lower': str(lower), 'value_upper': str(upper)},
        'identities': {
            'shape_domain': '0<=c<2-q, 0<z<=1; c=0 is Rademacher',
            'signal': 't=sqrt(q/(2-c)); v=1-t',
            'variational_fisher': 'J(mu)=sup_{f in C_c^infty} integral(2*y*f-2*fprime-f^2) dmu',
            'score_mean_derivative': 'E[rprime]=-J for centered unit-variance outputs',
            'strict_derivative': 'J_q>J*(1+J)/(2*q) for every finite-mixture shape with q>0',
            'normalized_value': 'W(q)=V(q)/(1+V(q))/sqrt(q) is strictly increasing on (0,2)',
            'transfer': 'T_lambda(x)=lambda*x/(1+(1-lambda)*x)',
            'weak_boundary': 'W2(X_(c,z),R)^2<=2*z; z=0 compactification is Rademacher at t(c)',
            'entropy_collar': 'B=4/(2-q); N=ceil(2*B+10); epsilon=2^-N; C=2-q/(1-epsilon)^2',
        },
        'global_results': {
            'boundary_inclusive_minimum_attained_for_every_q_in_0_2': True,
            'equals_regular_open_chart_infimum': True,
            'value_positive_continuous_locally_lipschitz': True,
            'normalized_value_strictly_increasing': True,
            'a_e_value_derivative_lower': 'Vprime>=V*(1+V)/(2*q)',
            'all_q_regular_open_chart_attainment': False,
            'all_q_uniqueness_or_smooth_optimizer_branch': False,
            'effective_uniqueness_radius': None,
            'endpoint_q_zero_or_two_included': False,
            'value_limit_at_q_zero': '0',
            'value_limit_at_q_two': '+infinity',
            'unique_parameter_for_every_positive_fisher_budget': True,
            'inverse_value_continuous_strictly_increasing': True,
            'universal_inverse_bracket': '2*(B/(1+B))^2<=q_B<=2*(1-exp(-B)/16)^2',
        },
        'compact_constant_controls': [compact_constants(q) for q in
                                     (F(1,10**6), Q0, F(1,64), F(1,4), F(1), F(3,2), F(15,8))],
        'inherited_value_transfers': {'higher_q_strict_lower': lower_rows,
                                     'lower_q_strict_upper': upper_rows,
                                     'inverse_budget_exclusions': budgets,
                                     'lower_budget_inverse_strict_lower': inverse_lower},
        'verification_boundary': {
            'new_numeric_integration': False, 'fixed_q_certificate_recomputed': False,
            'inherited_quadrature_tails_and_global_cover_reused': True,
            'continuum_proof_in_companion_note': True,
            'prior_art': 'Gaussian OU dissipation and Stam Fisher inequality specialized to nested two-radius domains; no novelty claim',
        },
        'claim_boundary': {'arbitrary_channel_optimizer': False, 'physical_claim': False,
                           'source_or_physics_ledger_change': False, 'canon_promotion': False},
    }


def validate(data):
    if data != compute():
        raise ValueError('artifact differs from exact transfer or analytic scope')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = compute()
    if args.write:
        ARTIFACT.write_text(json.dumps(data, indent=2)+'\n')
    validate(json.loads(ARTIFACT.read_text()))
    print('PASS: 7 rational compactification controls, 12 exact value transfers, 6 inverse budget bounds')
    print('PASS: fixed-q input identities/digests and scope; no quadrature replay')


if __name__ == '__main__':
    main()
