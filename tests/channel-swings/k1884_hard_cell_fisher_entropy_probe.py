#!/usr/bin/env python3
"""Independent arithmetic and transfer controls; finite controls are not continuum proof."""
from copy import deepcopy
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path

ROOT = Path(os.environ.get('GU_ROOT', Path(__file__).resolve().parents[2]))
OUTPUT = Path(os.environ.get('GU_OUTPUT_ROOT', ROOT))
CERT = 'lab/process/k1884-hard-cell-fisher-entropy.json'


def check(v):
    counts = {'exact_arithmetic': 0, 'numerical_transfer_controls': 0, 'reporting_and_pins': 0}
    def ck(name, condition, kind='exact_arithmetic'):
        if not condition:
            raise AssertionError('FAIL '+name)
        counts[kind] += 1

    constants = v['constants']
    height, local, tail = (F(constants[n]) for n in ['height', 'local_entropy', 'residual_entropy'])
    # Exact Laplace p_a(x)=a exp(-a|x|)/2 has I=a² and height a/2.
    for a in [F(1, 7), F(1), F(3), F(19, 2)]:
        ck('Laplace Fisher-to-height inequality', a/2 <= height*a)
    # Shifted Gaussian has KL=b*mu²/2 and relative Fisher=b²*mu².
    for b in [F(1, 3), F(2), F(20), F(40)]:
        for mu in [F(-3), F(1, 7), F(2)]:
            ck('shifted Gaussian entropy normalization', b*mu*mu/2 <= local*b*mu*mu)
    # The actual extreme precision bmax=2kA applied to residual moment bound.
    for k in [F(7, 2), F(4), F(8), F(21, 2)]:
        for d in [F(1, 10000), F(1, 4), F(1)]:
            actual = k*(k+1)*F(16, 9)*d/k**2
            claimed = tail*(k+1)*d/k
            ck('residual quadratic entropy transfer', actual <= claimed)
    # Discrete mixture convexity and the entropy-of-label normalization.
    def kl(p, q):
        return sum(x*math.log(x/y) for x, y in zip(p, q) if x)
    for t in [0.01, 0.1, 0.4, 0.9]:
        first, residual, target = [0.2, 0.8], [0.9, 0.1], [0.5, 0.5]
        mixture = [(1-t)*x+t*y for x, y in zip(first, residual)]
        ck('finite mixture convexity', kl(mixture, target) <= (1-t)*kl(first, target)+t*kl(residual, target)+1e-14,
           'numerical_transfer_controls')
        uniform_tail = sum((t/3)*math.log(1/(t/3)) for _ in range(3))
        claimed = t*math.log(constants['label_count']/t)
        ck('uniform three-label entropy cost', uniform_tail <= claimed+1e-14, 'numerical_transfer_controls')
    # Exact moment-coupling envelope; centered Gaussian dilation from
    # standard deviation 1/sqrt(b) to 1/sqrt(b)+q gives equality.
    for b in [F(1), F(4), F(16)]:
        root_b = F(math.isqrt(b.numerator), math.isqrt(b.denominator))
        for q in [F(1, 100), F(1, 3), F(2)]:
            actual_difference = 2*q/root_b+q*q
            ck('coupled second moments', actual_difference == q*(2/root_b+q))
            ck('entropy quadratic coefficient', b*q*q/2 <= constants['entropy_chain_quadratic']*b*q*q/2)
    for delta in [0.01, 0.25, 4.0]:
        h_before = math.log(2*math.pi*math.e)/2
        h_after = math.log(2*math.pi*math.e*delta)/2
        claimed_change = float(F(constants['entropy_log_scale']))*math.log(delta)
        ck('Gaussian entropy change of scale', abs(h_after-h_before-claimed_change) < 1e-14,
           'numerical_transfer_controls')
    for k in [F(7, 2), F(4), F(8)]:
        q = F(1, 7)
        actual_linear_squared = 2*k*(k+1)*q*q
        envelope_squared = constants['entropy_chain_sqrt']*k*(k+1)*q*q
        ck('entropy aggregate maximum precision', actual_linear_squared <= envelope_squared)

    # Reconstruct the example independently from upstream certified fractions.
    upstream = json.loads((ROOT/'lab/process/k1882-effective-fisher-rescaled-transport.json').read_text())
    ub = {n: F(s) for n, s in upstream['budget'].items()}
    expected = ub['E']/40+F(20, 9)*ub['D']+12*ub['tau']
    vb = {n: F(s) for n, s in v['budget'].items()}
    for n in ['E', 'D', 'B', 'tau', 'central_mass_lower', 'outer_mass_lower']:
        ck('upstream budget '+n, vb[n] == ub[n])
    ck('rational entropy sum', vb['H_rational_upper'] == expected)
    ck('weighted finite entropy bound', expected < F(v['bounds']['weighted_KL']))
    ck('central finite entropy bound', expected < ub['central_mass_lower']*F(v['bounds']['central_KL']))
    ck('outer finite entropy bound', expected < ub['outer_mass_lower']*F(v['bounds']['outer_KL']))
    # Reconstruct exp lower sum by recurrence, independent of producer factorials.
    term = total = F(1)
    for i in range(1, 26):
        term *= F(12, i)
        total += term
    ck('exp recurrence', total == vb['exp12_partial_lower'])
    ck('log twelve certificate', total > 5/ub['tau'])
    ck('normalizer upper', F(9, 4)*F(44, 7)*F(12501, 500)/20 < 25)
    ck('even-label correction', vb['even_label_divergence_upper'] == F(1, 3000000)**2*3)
    ck('even-mixture finite bound', expected+vb['even_label_divergence_upper'] < F(v['bounds']['weighted_KL']))
    ck('entropy sqrt envelope', 40*ub['B'] < F(71, 1000)**2)
    ck('entropy expansion envelope', vb['whole_entropy_error_upper'] == expected+F(71, 1000)+20*ub['B'])
    ck('entropy expansion finite bound', vb['whole_entropy_error_upper'] < F(v['bounds']['whole_entropy_expansion_error']))

    # Explicit shrinking spike shows TV/W2 control cannot replace bounded height.
    previous = 0.0
    for t in [0.2, 0.1, 0.05, 0.02]:
        binary = -t*math.log(t)-(1-t)*math.log1p(-t)
        lower = 1/t-t/2-binary
        ck('spike entropy diverges while transport vanishes', lower > previous and t < 1,
           'numerical_transfer_controls')
        previous = lower
    for p in [F(1, 10), F(1, 2), F(9, 10)]:
        ck('conditional mass denominator', F(1, 10)/p*p == F(1, 10))

    ck('result identity', v['result_id'] == 'K1884', 'reporting_and_pins')
    ck('classification', v['classification'] == 'INTERNAL_STRUCTURAL_ONLY', 'reporting_and_pins')
    for n in ['actual_hard_cells', 'all_feasible_valid_U', 'rare_cell_mass_required',
              'forward_entropy_only', 'actual_weight_mixture', 'fixed_weights_require_evenness',
              'differential_entropy_expansion']:
        ck('scope '+n, v['scope'][n] is True, 'reporting_and_pins')
    for n in ['reverse_KL_finite', 'sharp_rate', 'sextic_gap', 'native_GU']:
        ck('ceiling '+n, v['scope'][n] is False, 'reporting_and_pins')
    for p, digest in v['inputs'].items():
        ck('input pin '+p, hashlib.sha256((ROOT/p).read_bytes()).hexdigest() == digest, 'reporting_and_pins')
    return counts


def main():
    value = json.loads((OUTPUT/CERT).read_text())
    counts = check(value)  # Baseline must pass before any mutation is credited.
    mathematical = [('height', '1/4'), ('local_entropy', '1/4'),
                    ('residual_entropy', '8/9'), ('label_count', 2),
                    ('entropy_chain_quadratic', 0), ('entropy_log_scale', '1'),
                    ('entropy_chain_sqrt', 1)]
    caught = 0
    for key, replacement in mathematical:
        mutant = deepcopy(value)
        mutant['constants'][key] = replacement
        try:
            check(mutant)
        except AssertionError as exc:
            if not str(exc).startswith('FAIL '):
                raise
            print('CAUGHT mathematical coefficient', key, str(exc))
            caught += 1
        else:
            raise AssertionError('FAIL undetected mathematical coefficient '+key)
    report_mutants = []
    for key in ['reverse_KL_finite', 'native_GU', 'fixed_weights_require_evenness']:
        mutant = deepcopy(value)
        mutant['scope'][key] = not mutant['scope'][key]
        report_mutants.append((key, mutant))
    mutant = deepcopy(value)
    first = next(iter(mutant['inputs']))
    mutant['inputs'][first] = '0'*64
    report_mutants.append(('input pin', mutant))
    mutant = deepcopy(value)
    mutant['budget']['H_rational_upper'] = '1/1000000'
    report_mutants.append(('serialized arithmetic', mutant))
    for key, mutant in report_mutants:
        try:
            check(mutant)
        except AssertionError as exc:
            if not str(exc).startswith('FAIL '):
                raise
            print('CAUGHT reporting/pin/arithmetic', key, str(exc))
        else:
            raise AssertionError('FAIL undetected reporting/pin/arithmetic '+key)
    print('PASS K1884 probe', counts, ';', caught, 'mathematical coefficient faults;',
          len(report_mutants), 'report/pin/serialized faults')


if __name__ == '__main__':
    main()
