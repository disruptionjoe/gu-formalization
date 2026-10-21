#!/usr/bin/env python3
"""Exact K1884 budgets; the exploration owns the continuum entropy proof."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
import os
from pathlib import Path

ROOT = Path(os.environ.get('GU_ROOT', Path(__file__).resolve().parents[2]))
OUTPUT = Path(os.environ.get('GU_OUTPUT_ROOT', ROOT))
REL = 'lab/process/k1884-hard-cell-fisher-entropy.json'
INPUTS = ['lab/process/k1882-effective-fisher-rescaled-transport.json',
          'lab/process/k1880-effective-fisher-well-localization.json']


def produce():
    checks = {}
    def ck(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError('FAIL mathematical budget: ' + name)

    k, A, U = F(4), F(5), F(12501, 500)
    delta, h, e = F(1, 10**12), F(1, 10000), F(1, 3000000)
    ep, tau = 13*h/8, 4*e*e/h**2
    E = U-25+25*((1-ep)**-2-1)+30*e+80*tau+40*delta/h**2
    K = U+40*delta/h**2
    S = 5-3*e-8*tau
    D = 1-(1-ep)**2*S*S/K
    B = E/400+D/9+tau/20
    H = E/40+F(20, 9)*D+12*tau
    p0, po = 1-(1+3*e)/4, (1-3*e)/8
    ck('positive_allocation_and_cutoff', 0 < ep < 1 and S > 0 and 0 < D < 1)
    ck('positive_entropy_and_transport', E > 0 and B > 0 and H > 0)
    ck('tail_mass', tau == F(1, 22500))
    ck('Gaussian_normalizer_below_five', F(9, 4)*2*F(22, 7)*U/(k*A) < 25)
    # exp(1)<3: sum n>=2 1/n! <= sum n>=2 1/2^(n-1)=1,
    # strictly because n!>2^(n-1) for n>=3. Thus Cplus<5.
    exp_lower = sum(F(12**n, factorial(n)) for n in range(26))
    ck('positive_exp_series_certifies_log_bound', exp_lower > 5/tau)
    ck('weighted_KL_00255', H < F(51, 20000))
    ck('central_KL_0035', H < p0*F(7, 2000))
    ck('outer_KL_0021', H < po*F(21, 1000))
    weight = e*e*9/3
    ck('even_fixed_weight_entropy_00255', H+weight < F(51, 20000))
    # A rational envelope for (11) avoids an unverified square-root decimal.
    ck('entropy_moment_square_root_0071', 40*B < F(71, 1000)**2)
    entropy_error = H+F(71, 1000)+20*B
    ck('whole_entropy_chain_error_0077', entropy_error < F(77, 1000))
    ck('Laplace_height_constant', F(1, 2)**2 == F(1, 4))
    ck('residual_quadratic_coefficient', F(2)*k*A/2*F(16, 9)/k**2 == F(16, 9)*A/k)
    ck('label_chisquare_coefficient', F(1, 1)/(k*k)/(F(1, 1)/k*(1-1/k)) == F(1, 1)/(k-1))
    ck('entropy_second_moment_coefficient', (2*k*A)/2 == k*A)
    ck('rate_cutoff_mass_exponent', 1-2*F(1, 3) == F(1, 3))

    return {
        'result_id': 'K1884', 'status': 'active_research',
        'classification': 'INTERNAL_STRUCTURAL_ONLY', 'target_claim': 'NONE-NOT-A-KILL',
        'constants': {'height': '1/2', 'local_entropy': '1/2', 'residual_entropy': '16/9',
                      'label_count': 3, 'entropy_log_scale': '1/2',
                      'entropy_chain_sqrt': 2, 'entropy_chain_quadratic': 1},
        'formula': 'E/(2*k*A)+16*A*D/(9*k)+T*log(Cplus/T)',
        'formula_inputs': {'T': 'min(1,tau)', 'Cplus': 'max(exp(1),(3/2)*sqrt(2*pi*U/(k*A)))'},
        'budget': {name: str(v) for name, v in {
            'E': E, 'D': D, 'B': B, 'tau': tau, 'H_rational_upper': H,
            'central_mass_lower': p0, 'outer_mass_lower': po,
            'even_label_divergence_upper': weight, 'exp12_partial_lower': exp_lower,
            'whole_entropy_error_upper': entropy_error}.items()},
        'bounds': {'weighted_KL': '51/20000', 'central_KL': '7/2000',
                   'outer_KL': '21/1000', 'whole_entropy_expansion_error': '77/1000'},
        'scope': {'actual_hard_cells': True, 'all_feasible_valid_U': True,
                  'rare_cell_mass_required': True, 'forward_entropy_only': True,
                  'actual_weight_mixture': True, 'fixed_weights_require_evenness': True,
                  'differential_entropy_expansion': True, 'reverse_KL_finite': False,
                  'sharp_rate': False, 'sextic_gap': False, 'native_GU': False},
        'evidence_kind': {'checks': 'exact rational budgets and coefficient identities; not continuum proof',
                          'continuum': 'explorations/k1884-hard-cell-fisher-entropy-2026-10-21.md'},
        'checks': checks,
        'inputs': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    value = produce()
    if args.write:
        (OUTPUT/REL).write_text(json.dumps(value, indent=2)+'\n')
    elif value != json.loads((OUTPUT/REL).read_text()):
        raise AssertionError('FAIL certificate drift')
    print('PASS K1884', len(value['checks']), 'exact budget/coefficient groups;', len(value['inputs']), 'pins')
