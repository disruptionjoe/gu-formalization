#!/usr/bin/env python3
"""Exact constants for the fourth-moment Fisher endpoint theorem.

The continuum proof is in the companion exploration; no quadrature runs.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / 'lab/process/k1827-endpoint-fisher-asymptotic.json'
INPUT = 'lab/process/k1825-global-q-fisher-transfer.json'
A = F(131, 54)
C = F(551, 27)


def scaled_lower(delta):
    delta = F(delta)
    if not 0 < delta < 2:
        raise ValueError('delta must belong to (0,2)')
    return max(F(0), 4*max(F(0), 1-A*delta)**2-delta)


def inverse_bracket(budget):
    budget = F(budget)
    if budget <= 0:
        raise ValueError('positive budget required')
    return 4/(budget+C), 2*(1+2*budget)/(1+budget)**2


def compute():
    prior = json.loads((ROOT/INPUT).read_text())
    if not prior['global_results']['unique_parameter_for_every_positive_fisher_budget']:
        raise ValueError('missing inverse-value theorem')
    assert A == F(1,2)+F(13,12)*F(16,9)
    assert C == 8*A+1
    endpoints = []
    for n in (2,4,8,16,64,256,1024):
        delta = F(1,n)
        lower, upper = scaled_lower(delta), 4-F(3,2)*delta
        assert 0 <= lower <= upper < 4
        assert 4-C*delta <= lower
        endpoints.append({'delta':str(delta), 'q':str(2-delta),
                          'delta_value_lower':str(lower), 'delta_value_upper':str(upper)})
    inverse = []
    for budget in (F(1,1000),F(1),F(10),F(100),F(1000),F(10**6)):
        lower,upper = inverse_bracket(budget)
        assert 0 < lower <= upper < 2
        assert upper < 4/budget
        assert 4/budget-lower == 4*C/(budget*(budget+C))
        inverse.append({'budget':str(budget), 'delta_lower':str(lower),
                        'delta_upper':str(upper),
                        'four_over_budget_error_upper':str(4*C/(budget*(budget+C)))})
    return {
        'schema_version':'1.0', 'claim_id':'K1827', 'status':'active_research',
        'scope':'uniform fourth-moment Fisher lower bound and endpoint envelopes; high-q Rademacher-face instability with existential threshold; no full optimizer characterization',
        'input_sha256':{INPUT:hashlib.sha256((ROOT/INPUT).read_bytes()).hexdigest()},
        'constants':{'A':str(A), 'C':str(C), 'clipped_threshold':'1/2',
                     'derivative_loss_max':'13/12', 'central_mass_factor':'16/9'},
        'identities':{
            'moment':'E(Y^2-1)^2=delta=2-q',
            'test':'f(y)=(y^2-1)*clip(2*y,-1,1)/2',
            'derivative':'3*y^2-1 for abs(y)<1/2; abs(y) for abs(y)>1/2; a.e. only',
            'weak_score':'E[s*f]=-E[fprime]',
            'ordinary_relative':'J=I-1 for E[Y^2]=1',
            'uniform_lower':'J>=max(0,4*max(0,1-A*delta)^2/delta-1)',
            'additive_bounds':'4/delta-C<=V(2-delta)<=4/delta-3/2',
            'inverse_bracket':'4/(B+C)<=2-q_B<=2*(1+2*B)/(1+B)^2',
        },
        'results':{
            'sharp_endpoint_coefficient':'4',
            'family_value':'V(q)=4/(2-q)+O(1)',
            'unrestricted_density_infimum':'U(delta)=4/delta+O(1); centered second moment 1, fourth moment 1+delta, finite weak-score Fisher',
            'inverse_rate':'2-q_B=4/B+O(B^-2)',
            'rademacher_value_ratio_to_minimum_tends_to_one':True,
            'all_admissible_symmetric_outputs_W2_squared_to_rademacher_at_most_delta':True,
            'exact_rademacher_minimizer_at_finite_q':False,
            'rademacher_face_excluded_for_all_sufficiently_high_q':True,
            'explicit_qstar_or_uniform_c_descent_step':None,
            'constant_term_asymptotic_identified':False,
            'unrestricted_density_infimum_attainment_or_uniqueness':False,
            'all_q_shape_uniqueness_or_interior_attainment':False,
            'effective_uniqueness_radius':None,
        },
        'endpoint_bounds':endpoints, 'inverse_bounds':inverse,
        'face_instability':{
            'fixed_z':'3/4', 'inner_to_outer_mean_ratio':'1/2',
            'weight_c_derivative':'16/9',
            'outer_mean_c_derivative':'19*m/24',
            'noise_c_derivative':'-t/4',
            'isolated_lobe_fisher_c_derivative':'-7*t/(36*v^2)',
            'overlap_identity':'G-Gplus=(T-1)*(2*m*y+m^2*(T+1))/v^2; T=tanh(m*y/v)',
            'overlap_error':'O(v^-4*exp(-1/(256*v))) for m>=1/2 and v sufficiently small',
            'full_fisher_c_derivative_negative_near_q_two':True,
            'threshold_computed':False,
            'other_boundary_z_one_excluded':False,
        },
        'contrary_family':{
            'definition':'Y=S*(1+h*Z)/sqrt(1+h^2*v), Z density proportional to (1-z^2)^m on (-1,1), m>=2, 0<h<1',
            'v':'1/(2*m+3)', 'EZ4':'3/((2*m+3)*(2*m+5))',
            'IZ':'m*(2*m+1)/(m-1)',
            'limit_delta_I':'4*m*(2*m+1)/((m-1)*(2*m+3))>4',
            'm2_limit':'40/7',
            'meaning':'W2 convergence to Rademacher does not prove asymptotic Fisher optimality',
        },
        'verification_boundary':{
            'new_quadrature':False, 'fixed_q_certificate_used':False,
            'continuum_proof_in_companion_note':True,
            'prior_art':'classical weak-score integration by parts and Cauchy-Schwarz; no novelty claim',
        },
        'claim_boundary':{'physical_claim':False,'source_or_physics_ledger_change':False,
                          'canon_promotion':False},
    }


def validate(data):
    if data != compute():
        raise ValueError('artifact differs from exact constants, bounds or analytic scope')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = compute()
    if args.write:
        ARTIFACT.write_text(json.dumps(data,indent=2)+'\n')
    validate(json.loads(ARTIFACT.read_text()))
    print('PASS: 7 endpoint bounds, 6 inverse bounds, exact constants and input digest; no quadrature')


if __name__ == '__main__':
    main()
