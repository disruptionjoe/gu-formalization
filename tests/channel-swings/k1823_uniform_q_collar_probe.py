#!/usr/bin/env python3
"""Independent analytic controls, proof-necessity examples and reporting probes."""
import copy
import json
from fractions import Fraction as F
import k1823_uniform_q_collar as m


class Dual:
    def __init__(self, value, derivative=0):
        self.value, self.derivative = F(value), F(derivative)

    def __add__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.value+other.value, self.derivative+other.derivative)

    __radd__ = __add__

    def __mul__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.value*other.value, self.derivative*other.value+self.value*other.derivative)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.value/other.value,
                    (self.derivative*other.value-self.value*other.derivative)/other.value**2)


def controls():
    count = 0
    # Exact Gaussian input controls test OU differentiation, independently of
    # the finite-mixture moment/collar argument. Non-unit variances here are
    # analytic controls, not members of the admitted unit-variance chart.
    for t in (F(1, 10), F(1, 2), F(3, 4)):
        for variance in (F(1, 2), F(1), F(2)):
            for mean in (F(0), F(2, 3)):
                a = variance-1
                td = Dual(t, 1)
                s = 1+a*td
                j = td*mean**2+td*td*a*a/s
                score_derivative_square = (a*t/(1+a*t))**2
                assert t*j.derivative == j.value+score_derivative_square
                # The posterior variance yields the same relative-score Hessian.
                v = 1-t
                posterior = variance*v/(1+a*t)
                assert -t/v+t*posterior/v**2 == a*t/(1+a*t)
                count += 1
    assert count == 18
    # Exact chart fourth moment after the Gaussian channel: cumulant = -q.
    for c, t in ((F(1, 3), F(1, 10)), (F(7, 5), F(1, 2)), (F(0), F(1, 4))):
        y4 = t*t*(1+c)+6*t*(1-t)+3*(1-t)**2
        assert y4-3 == -t*t*(2-c)
    # Positive local Hessian and local persistence without uniform compactness
    # do NOT ensure global persistence. F(0,x)=x^2 has its unique min at 0.
    for q in (F(1, 10), F(1, 100), F(1, 1000)):
        x = 1/q
        value = x*x*(1-q*x)**2-q*q*x*x
        assert value == -1 and 2*(1-q*q) > 0
    # Compactness does not repair a tied baseline: both +/-1 are nondegenerate
    # minima at q=0, while adding q*x distinguishes their values immediately.
    for q in (F(-1, 100), F(1, 100)):
        assert ((1-1)**2+q) != ((1-1)**2-q)
        assert 12*F(1)**2-4 == 8
    # Recover constants independently, without calling the producer's formulas.
    c = m.constants()
    lower, upper = F(9765624999, 10**13), F(9765625001, 10**13)
    assert (c['q_min'], c['q_max']) == (lower, upper)
    assert c['uniform_rare_gap_floor'] == F(1962, 10**13)
    assert c['common_c_max'] == F(18759765625001, 9384765625000)
    assert upper*961*33**2 < lower*1024*32**2
    assert 2*400000**2 < 36*10**10  # square of rare-loss comparison after scaling
    return count


def main():
    data = json.loads(m.ARTIFACT.read_text())
    m.validate(data)
    count = controls()
    mutations = [
        ('entire-interval uniqueness', lambda x: x['explicit_interval_results'].update(unique_minimizer_on_entire_explicit_interval=True)),
        ('open-chart attainment overclaim', lambda x: x['explicit_interval_results'].update(regular_open_chart_attainment_on_entire_interval=True)),
        ('fabricated quantitative delta', lambda x: x['qualitative_neighborhood_result'].update(delta_value='1/10000000000000')),
        ('missing exterior gap', lambda x: x['qualitative_neighborhood_result'].update(uses_compact_exterior_gap=False)),
        ('noise overclaim', lambda x: x['constants'].update(common_noise_lower='1/32')),
        ('wrong rare margin', lambda x: x['constants'].update(uniform_rare_gap_floor='1/1000000000')),
        ('missing q factor', lambda x: x['identities'].update(q_derivative="dJ/dq=J+E[(r')^2]")),
        ('physical scope', lambda x: x['claim_boundary'].update(source_action_or_physical_state=True)),
        ('new quadrature claim', lambda x: x['verification_boundary'].update(inherited_certificates_recomputed=True)),
        ('missing input', lambda x: x['input_sha256'].pop(m.INPUTS[1])),
    ]
    for label, mutate in mutations:
        bad = copy.deepcopy(data)
        mutate(bad)
        try:
            m.validate(bad)
        except ValueError as exc:
            assert 'artifact differs' in str(exc)
            print('REJECTED:', label)
        else:
            raise AssertionError('accepted '+label)
    print(f'PASS: {count} Gaussian analytic controls, three cumulants, three noncompact and two tied-baseline examples; ten reporting mutations')


if __name__ == '__main__':
    main()
