#!/usr/bin/env python3
"""K1888 exact coefficient controls; analytic text carries domain/continuum claims."""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s

INPUTS = [
    'lab/process/k1832-k77-common-energy-form.json',
    'lab/process/k1836-k77-differential-dirac-quotient.json',
    'lab/process/k1840-k77-conservative-variable-observation.json',
    'lab/process/k1883-compact-support-observation-range.json',
    'lab/process/k1886-support-bounded-observation-approximation.json',
]
OUT = 'lab/process/k1888-bounded-support-energy-inverse.json'
GAMMA, UPPER, ALPHA = s.Rational(1584, 625), s.Rational(7182, 625), s.Rational(138, 25)


def matrix(v):
    out = s.zeros(v.get('rows', 16), v.get('columns', 16))
    for i, j, x in v['entries']:
        out[i, j] = s.Rational(x)
    return out


def encode(M):
    return {'rows': M.rows, 'columns': M.cols,
            'entries': [[i, j, str(M[i, j])] for i in range(M.rows)
                        for j in range(M.cols) if M[i, j]]}


def zero(M):
    return all(s.expand(v) == 0 for v in M)


def produce(root):
    energy, observation, variable, _, _ = [json.loads((root / p).read_text()) for p in INPUTS]
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError('FAIL ' + name)

    blocks = []
    expected_cross = s.Rational(1866, 625) * s.Matrix([
        [0, 0, -1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0]])
    xi = s.symbols('x1 x2 x3', real=True)
    mass = s.symbols('R', real=True)
    for j, (er, ob, vr) in enumerate(zip(energy['blocks'], observation['blocks'], variable['blocks'])):
        H = matrix(er['H'])
        Hi = H.inv()
        T = list(map(matrix, ob['T']))
        S = matrix(vr['repairs'][0]['S'])
        K = s.diag(1, -1, -1, 1)
        Z = s.Matrix.vstack(*T)
        G = Z * Hi * Z.T
        I = s.eye(12)
        upper_projector = (G - GAMMA * I) / (UPPER - GAMMA)
        N = Hi * Z.T * G.inv()
        check(f'gram_symmetric_{j}', G == G.T)
        check(f'gram_minimal_polynomial_{j}', (G-GAMMA*I)*(G-UPPER*I) == s.zeros(12))
        check(f'upper_projector_rank4_{j}', upper_projector**2 == upper_projector and s.trace(upper_projector) == 4)
        check(f'positive_bounds_{j}', 0 < GAMMA < ALPHA < UPPER)
        check(f'all_diagonal_blocks_alpha_{j}', all(G[4*i:4*i+4, 4*i:4*i+4] == ALPHA*s.eye(4) for i in range(3)))
        check(f'nonzero_boundary_cross_block_{j}', G[:4, 4:8] == expected_cross)
        check(f'weighted_flux_right_inverse_{j}', Z*N == I)
        check(f'minimum_flux_energy_{j}', N.T*H*N == G.inv())
        check(f'flux_projection_H_selfadjoint_{j}', H*N*Z == (N*Z).T*H and (N*Z)**2 == N*Z)
        check(f'mass_factorization_{j}', S == 24*K*T[0])
        O = sum((xi[i]*T[i] for i in range(3)), s.zeros(4, 16)) + mass*S
        Od = Hi*(-sum((xi[i]*T[i].T for i in range(3)), s.zeros(16, 4)) + mass*S.T)
        check(f'interior_scalar_operator_only_{j}', zero(O*Od-ALPHA*(-sum(x*x for x in xi)+576*mass*mass)*s.eye(4)))
        check(f'scalar_Neumann_countercontrol_{j}', expected_cross*s.eye(4)[:, 0] != s.zeros(4, 1))
        blocks.append({'flux_gram': encode(G), 'flux_right_inverse': encode(N),
                       'upper_spectral_projector': encode(upper_projector)})
    check('four_types_same_gram', all(b['flux_gram'] == blocks[0]['flux_gram'] for b in blocks))
    # The scalar auxiliary eigen-equation, not the coupled operator spectrum.
    x, k, w = s.symbols('x k w', real=True, nonzero=True)
    u = s.cos(w*x) + k/w*s.sin(w*x)
    check('auxiliary_ODE', s.simplify(-s.diff(u,x,2)+k*k*u-(k*k+w*w)*u) == 0)
    check('auxiliary_left_endpoint', s.simplify((s.diff(u,x)-k*u).subs(x,0)) == 0)
    for n in (1, 2, 3):
        check(f'auxiliary_right_endpoint_{n}', s.simplify((s.diff(u,x)-k*u).subs(x,n*s.pi/w)) == 0)
    check('auxiliary_ground', s.diff(s.exp(k*x),x)-k*s.exp(k*x) == 0)
    return {
        'result_id': 'K1888', 'status': 'active_research',
        'classification': 'INTERNAL_STRUCTURAL_ONLY', 'target_claim': 'NONE-NOT-A-KILL',
        'coefficients': {'gamma': str(GAMMA), 'Gamma': str(UPPER), 'alpha': str(ALPHA),
                         'gamma_multiplicity': 8, 'Gamma_multiplicity': 4,
                         'kappa_over_R': 24, 'gram_cross_coefficient': '1866/625'},
        'formulas': {
            'gap_lower': 'gamma*min(kappa^2+pi^2/(2L1)^2,pi^2/(2L2)^2,pi^2/(2L3)^2)',
            'source_energy': '<z,K_Omega^-1 z>',
            'budget_convention': 'B is source norm; energy budget is B^2',
            'cube_inverse_bounds': '2L/(pi*sqrt(alpha)) <= norm(R_Omega) <= 2L/(pi*sqrt(gamma))',
            'primitive_bound': 'exp(2*abs(kappa)*L1)*C_prim/sqrt(gamma)',
        },
        'scope': {
            'coupled_conormal_domain_required': True,
            'auxiliary_scalar_gap_is_actual_gap': False,
            'compact_error_floor_requires_energy_blowup': False,
            'smooth_compatible_exact_compact_lift_energy_inf': True,
            'arbitrary_L2_has_exact_smooth_compact_lift': False,
            'compact_infimum_always_attained': False,
            'budget_zero_and_pure_charge_endpoints_explicit': True,
            'instantaneous_repaired_frame_transfer': True,
            'fixed_box_dynamical_intertwining': False,
            'native_GU': False,
            'general_spectral_budget_calculus_new': False,
        },
        'blocks': blocks, 'checks': checks,
        'inputs': {p: hashlib.sha256((root/p).read_bytes()).hexdigest() for p in INPUTS},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output', type=Path)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = produce(args.root)
    output = args.output or args.root/OUT
    if args.write:
        output.write_text(json.dumps(data, indent=2)+'\n')
    elif data != json.loads(output.read_text()):
        raise AssertionError('FAIL certificate drift')
    print('PASS K1888', len(data['checks']), 'exact algebra groups;', len(INPUTS), 'pins; continuum claims analytic')


if __name__ == '__main__':
    main()
