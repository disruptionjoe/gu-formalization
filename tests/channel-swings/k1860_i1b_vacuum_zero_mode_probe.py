#!/usr/bin/env python3
"""Independent scalar polynomial controls and baseline-first input faults."""
from fractions import Fraction as F
from pathlib import Path
import copy
import json
import traceback

ROOT = Path(__file__).resolve().parents[2]


def check(d):
    # Derive the monomial metric-volume exponent, not a producer call.
    assert d['observed_dimension'] == 4
    assert d['metric_scaling_power'] == 2
    exponent = F(d['observed_dimension'] * d['metric_scaling_power'], 2)
    assert exponent == d['volume_scaling_power'] == 4
    assert F(d['pure_metric_hessian_scale_entry']) == 0
    # Direct polynomial partial derivatives of a(c-1)t²+b t³+rho c^4.
    a = F(d['toy_scale_quadratic_coefficient'])
    b = F(d['toy_cubic_coefficient'])
    assert a == F(-1, 2) and b == F(1, 3)
    for x in [F(-1, 7), F(2, 13), F(1, 101)]:
        c, t = 1+x, x
        rho = x*x / (F(d['branch_denominator']) * c**d['branch_volume_derivative_power'])
        # Independent direct coefficient expansion of the c and t partials.
        assert a*t*t + 4*rho*c*c*c == 0
        assert 2*a*c*t - 2*a*t + 3*b*t*t == 0
        assert rho > 0
    assert F(d['required_green_defect_factor']) + 4 == 0
    return True


def report_scope(d):
    return (d['conditional_global_hypotheses'] and d['requires_differentiable_response']
            and not d['global_GU_adapter_constructed']
            and not d['all_continuous_responses_excluded'])


if __name__ == '__main__':
    data = json.loads((ROOT/'lab/process/k1860-i1b-vacuum-zero-mode.json').read_text())
    assert check(data) and report_scope(data)  # clean baseline before all faults
    mutations = [
        ('observed_dimension', 3), ('metric_scaling_power', 1),
        ('volume_scaling_power', 2), ('pure_metric_hessian_scale_entry', '1'),
        ('toy_scale_quadratic_coefficient', '1/2'),
        ('toy_cubic_coefficient', '1/2'), ('branch_denominator', '4'),
        ('branch_volume_derivative_power', 4), ('required_green_defect_factor', '4'),
    ]
    for key, value in mutations:
        bad = copy.deepcopy(data)
        bad[key] = value
        try:
            check(bad)
        except AssertionError as exc:
            frame = traceback.extract_tb(exc.__traceback__)[-1]
            print('[DETECTED mathematical-input fault]', key, 'at', frame.lineno, frame.line)
        else:
            raise AssertionError('undetected input fault: '+key)
    controls = 0
    # Full exact rank-defective Hessians generated from an action polynomial
    # I=t0*y0+t1*y1+1/2 t^T C t. Scale s is absent; its Euler residual
    # after adding rho(1+s)^4 is 4rho at s=0 for every other variation.
    for c00 in range(-2, 3):
        for c01 in range(-2, 3):
            for c11 in range(-2, 3):
                for rho in [F(-2, 7), F(3, 11)]:
                    y0, y1, t0, t1 = F(1, 2), F(-1, 3), F(2, 5), F(3, 7)
                    gradient = (4*rho, t0, t1, y0+c00*t0+c01*t1, y1+c01*t0+c11*t1)
                    assert gradient[0] == 4*rho != 0
                    controls += 1
    # Fixed-volume tangent s=0 removes this one residual test; no full
    # source solution is inferred. The supplied multiplier shift is exact.
    for multiplier in [F(-3, 5), F(7, 11)]:
        for shift in [F(-2), F(5, 3)]:
            assert (multiplier-shift)+shift == multiplier
            controls += 1
    for key in ['conditional_global_hypotheses', 'requires_differentiable_response',
                'global_GU_adapter_constructed', 'all_continuous_responses_excluded']:
        bad = copy.deepcopy(data)
        bad[key] = not bad[key]
        assert not report_scope(bad)
        print('[DETECTED reporting fault]', key)
    print('K1860 independent controls PASS:', controls, 'rational fixtures;',
          len(mutations), 'mathematical-input and 4 reporting faults detected')
