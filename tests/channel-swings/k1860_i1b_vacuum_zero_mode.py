#!/usr/bin/env python3
"""Exact algebra controls, not certification of an unconstructed global domain."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]


def verify(d):
    count = 0
    n = d['observed_dimension']
    metric_power = d['metric_scaling_power']
    volume_power = d['volume_scaling_power']
    assert n == 4 and metric_power == 2
    assert Q(n * metric_power, 2) == volume_power == 4
    # Diagonal metric determinant, including a Lorentzian negative entry.
    for c in [Q(1, 2), Q(2, 3), Q(1), Q(3, 2)]:
        diag = [-c**metric_power] + [c**metric_power] * (n - 1)
        determinant = Q(1)
        for entry in diag:
            determinant *= entry
        assert -determinant == c ** (2 * volume_power)
        count += 1
    # A metric scale column lies in ker A. C is arbitrary symmetric,
    # including invertible, singular and indefinite fixtures.
    for a in [Q(-2), Q(1, 3), Q(5)]:
        for C in [((0, 0), (0, 0)), ((1, 0), (0, 1)), ((1, 2), (2, -1))]:
            A = ((0, a, 1), (0, 2, -a))
            H = [[Q(0) for _ in range(5)] for _ in range(5)]
            H[0][0] = Q(d['pure_metric_hessian_scale_entry'])
            for i in range(2):
                for j in range(3):
                    H[3+i][j] = H[j][3+i] = Q(A[i][j])
                for j in range(2):
                    H[3+i][3+j] = Q(C[i][j])
            v = [Q(1), Q(0), Q(0), Q(0), Q(0)]
            assert all(sum(H[i][j]*v[j] for j in range(5)) == 0 for i in range(5))
            for w in [[Q(j-2) for j in range(5)], [Q(1, j+1) for j in range(5)]]:
                Hw = [sum(H[i][j]*w[j] for j in range(5)) for i in range(5)]
                assert sum(v[i]*Hw[i] for i in range(5)) == 0
                for volume in [Q(1, 7), Q(3)]:
                    residual = Hw[:]
                    residual[0] += volume_power*volume
                    assert sum(v[i]*residual[i] for i in range(5)) == 4*volume > 0
                    count += 1
    # Exact nonlinear singular branch with V=c^4. No float differentiation.
    for x in [Q(-1, 8), Q(-1, 20), Q(1, 30), Q(1, 10)]:
        c = 1+x
        t = x
        rho = x*x/(Q(d['branch_denominator']) * c**d['branch_volume_derivative_power'])
        e_t = 2*Q(d['toy_scale_quadratic_coefficient'])*(c-1)*t + 3*Q(d['toy_cubic_coefficient'])*t*t
        e_c = Q(d['toy_scale_quadratic_coefficient'])*t*t + volume_power*rho*c**(volume_power-1)
        assert e_t == 0 and e_c == 0 and rho > 0
        assert rho/(x*x) == 1/(8*c**3)
        count += 2
    # Actual bulk Green defect sign for the +rho V convention.
    for volume in [Q(2, 5), Q(3)]:
        flux = Q(d['required_green_defect_factor'])*volume
        assert flux + 4*volume == 0
        count += 1
    for dep in d['dependencies']:
        assert hashlib.sha256((ROOT/dep['path']).read_bytes()).hexdigest() == dep['sha256']
    assert d['conditional_global_hypotheses'] and d['requires_differentiable_response']
    assert not d['global_GU_adapter_constructed'] and not d['all_continuous_responses_excluded']
    return count


if __name__ == '__main__':
    data = json.loads((ROOT/'lab/process/k1860-i1b-vacuum-zero-mode.json').read_text())
    print('K1860 exact algebra controls PASS:', verify(data), 'controls; global hypotheses remain conditional')
