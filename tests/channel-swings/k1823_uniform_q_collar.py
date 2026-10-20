#!/usr/bin/env python3
"""Exact constants for a uniform-q compactness and optimizer-persistence proof.

The analytic proof is in the companion note. This replays rational inequalities
and pins inherited certificates; it does not regenerate numerical quadrature.
"""
import argparse
import hashlib
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / 'lab/process/k1823-uniform-q-collar.json'
INPUTS = (
    'lab/process/k1753-arb-rational-interior-improvement.json',
    'lab/process/k1756-rademacher-arb-gap.json',
    'lab/process/k1757-ou-variational-stability.json',
    'lab/process/k1758-zero-noise-entropy-collar.json',
    'lab/process/k1759-rare-atom-quantitative-collar.json',
    'lab/process/k1820-full-fisher-global-optimizer-admission.json',
    'lab/process/k1820-independent-certificate-audit.json',
)


def ball_lower(text):
    match = re.fullmatch(r'\[([+\-0-9.eE]+) \+/- ([+\-0-9.eE]+)\]', text)
    if not match:
        raise ValueError('unsupported decimal ball')
    center, radius = map(F, match.groups())
    if radius < 0:
        raise ValueError('negative radius')
    return center - radius


def constants():
    q0, half_width = F(1, 1024), F(1, 10**13)
    qlo, qhi = q0-half_width, q0+half_width
    ustar = F(691835097, 2000000000)
    zstar = F(1127044207, 2000000000)
    derivative = 1024 * (F(1, 15)+F(1, 225)+F(768, 50625))
    rounded_derivative = F(89)
    gap = F(220, 10**12)
    moving_gap = gap-2*rounded_derivative*half_width
    rare_loss = F(6, 10**12)
    zmin = F(1, 10**34)
    cmax = 2-F(1024, 961)*qlo
    common_lipschitz = F(32+1024+3*1024*1089)/(2*qlo)
    return {
        'q0': q0, 'half_width': half_width, 'q_min': qlo, 'q_max': qhi,
        'candidate_u': ustar, 'candidate_c': 2-ustar, 'candidate_z': zstar,
        'comparison_derivative_bound': derivative,
        'comparison_derivative_rounded': rounded_derivative,
        'inherited_gap_floor': gap, 'uniform_comparison_gap_floor': moving_gap,
        'rare_loss_upper': rare_loss, 'uniform_rare_gap_floor': moving_gap-rare_loss,
        'common_z_min': zmin, 'common_c_max': cmax,
        'common_noise_lower': F(1, 33), 'value_lipschitz_constant': common_lipschitz,
    }


def checks(c):
    return [
        ('nonzero positive q interval', 0 < c['q_min'] < c['q0'] < c['q_max']),
        ('comparison q denominator', c['q_min'] > c['q0']/2),
        ('candidate signal below 1/16', 256*c['q_max'] < c['candidate_u']),
        ('Rademacher signal below 1/16', 256*c['q_max'] < 2),
        ('candidate signal below 1/17', 289*c['q_max'] < c['candidate_u']),
        ('derivative rounding', c['comparison_derivative_bound'] < 89),
        ('uniform named gap', c['uniform_comparison_gap_floor'] == F(1011, 5*10**12)),
        ('strict rare loss via squares', 400000**2*2*c['common_z_min'] < c['rare_loss_upper']**2),
        ('uniform rare gap positive', c['uniform_rare_gap_floor'] == F(981, 5*10**12) > 0),
        ('common compact lies in every chart', 0 < c['common_c_max'] < 2-c['q_max']),
        ('common positive noise via squares', c['q_max']/(2-c['common_c_max']) < F(32, 33)**2),
        ('candidate in common compact', 0 < c['candidate_c'] < c['common_c_max'] and c['common_z_min'] < c['candidate_z'] < 1),
        ('explicit global value Lipschitz bound', c['value_lipschitz_constant'] == F(5577440000000000000, 3255208333)),
    ]


def compute():
    c = constants()
    for label, okay in checks(c):
        if not okay:
            raise ValueError(label)
    inputs = {path: json.loads((ROOT/path).read_text()) for path in INPUTS}
    candidate = inputs[INPUTS[0]]['rational_candidate']
    if F(candidate['c']) != c['candidate_c'] or F(candidate['z']) != c['candidate_z']:
        raise ValueError('candidate identity changed')
    inherited_lower = ball_lower(inputs[INPUTS[1]]['comparison']['whole_line_gap'])
    if inherited_lower <= c['inherited_gap_floor']:
        raise ValueError('inherited gap insufficient')
    if not inputs[INPUTS[2]]['decision']['explicit_stability_modulus_proved']:
        raise ValueError('missing inherited stability')
    if not inputs[INPUTS[3]]['decision']['rare_atom_zero_noise_joint_corner_covered']:
        raise ValueError('missing inherited corner argument')
    if not inputs[INPUTS[5]]['decision']['global_optimizer_proved']:
        raise ValueError('missing fixed-q global theorem')
    audit = inputs[INPUTS[6]]['result']
    if not (audit['unresolved'] == 0 and audit['single_convex_rectangle']
            and F(audit['a_lower']) > 0 and F(audit['determinant_lower']) > 0):
        raise ValueError('missing fixed-q Hessian evidence')
    return {
        'schema_version': '1.0', 'claim_id': 'K1823', 'status': 'active_research',
        'scope': 'symmetric unit-variance two-radius scalar Gaussian channels, including continuous Rademacher and three-point faces',
        'input_sha256': {path: hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in INPUTS},
        'constants': {key: str(value) for key, value in c.items()},
        'inherited_gap_lower_endpoint': str(inherited_lower),
        'identities': {
            'signal': 't=sqrt(q/(2-c)); v=1-t',
            'relative_score_derivative': "r'=-t/v+t Var(X|Y)/v^2",
            'q_derivative': "dJ/dq=(J+E[(r')^2])/(2q)",
            'moment_bound': 'E[Var(X|Y)^2]<=E[X^4]=1+c<=3',
            'output_fourth_cumulant': '-q',
        },
        'explicit_interval_results': {
            'common_compact_minimizer_domain': True,
            'uniform_boundary_escape_exclusion': True,
            'boundary_inclusive_minimum_attained': True,
            'equals_regular_open_chart_infimum': True,
            'regular_open_chart_attainment_on_entire_interval': False,
            'value_continuous_and_lipschitz': True,
            'value_strictly_increasing': True,
            'unique_minimizer_on_entire_explicit_interval': False,
        },
        'qualitative_neighborhood_result': {
            'there_exists_positive_delta': True,
            'delta_upper_bound': str(c['half_width']),
            'delta_value': None,
            'unique_smooth_global_minimizer': True,
            'uses_fixed_q_unique_global_minimum': True,
            'uses_compact_exterior_gap': True,
            'uses_positive_local_hessian': True,
        },
        'verification_boundary': {
            'new_numeric_integration': False,
            'inherited_certificates_recomputed': False,
            'upstream_quadrature_and_global_cover_reused': True,
            'new_analytic_proof_in_companion_note': True,
            'new_exact_rational_inequalities': len(checks(c)),
        },
        'claim_boundary': {
            'arbitrary_channel_optimizer': False, 'source_action_or_physical_state': False,
            'source_or_physics_ledger_change': False, 'canon_promotion': False,
        },
    }


def validate(data):
    if data != compute():
        raise ValueError('artifact differs from exact constants or declared proof boundary')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = compute()
    if args.write:
        ARTIFACT.write_text(json.dumps(data, indent=2)+'\n')
    validate(json.loads(ARTIFACT.read_text()))
    for label, okay in checks(constants()):
        assert okay, label
        print('PASS:', label)
    print('PASS: inherited input identities/hashes and exact artifact boundary; no quadrature replay')


if __name__ == '__main__':
    main()
