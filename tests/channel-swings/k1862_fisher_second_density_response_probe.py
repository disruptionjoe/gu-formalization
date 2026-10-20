#!/usr/bin/env python3
"""Independent dense Fraction checks; mutations follow the clean baseline."""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
from copy import deepcopy
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]


def add(a, b):
    return [(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0))
            for i in range(max(len(a), len(b)))]


def scale(a, c):
    return [v * c for v in a]


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i + j] += c * d
    return out


def hermite(n):
    # Closed factorial formula, independent of the producer's recurrence.
    out = [F(0)] * (n + 1)
    for j in range(n // 2 + 1):
        out[n - 2 * j] = F((-1) ** j * factorial(n), 2 ** j * factorial(j) * factorial(n - 2 * j))
    return out


def hp(entries):
    result = [F(0)]
    for n, c in entries.items():
        result = add(result, scale(hermite(int(n)), F(c)))
    return result


def derivative(p):
    return [i * p[i] for i in range(1, len(p))] or [F(0)]


def ev(p, x):
    result = F(0)
    for c in reversed(p):
        result = result * x + c
    return result


def gaussian(p):
    return sum((c * F(factorial(n), 2 ** (n // 2) * factorial(n // 2))
                for n, c in enumerate(p) if n % 2 == 0), F(0))


def check(m):
    count = 0
    u, v, density = map(hp, [m['u_hermite'], m['v_hermite'], m['density_second_hermite']])
    constants = {k: F(value) for k, value in m['multipliers'].items()}
    W1 = [F(0), F(0), constants['a1'], F(0), constants['b1']]
    W2 = [F(0), F(0), constants['a2'], F(0), constants['b2']]
    A = lambda p: add(scale(derivative(derivative(p)), -4), [F(0)] + scale(derivative(p), 4))
    first = add(add(A(u), W1), [-constants['E1']])
    second = add(add(add(add(A(v), mul(W1, u)), scale(u, -constants['E1'])), W2), [-constants['E2']])
    density_error = add(add(scale(v, 2), mul(u, u)), scale(density, -1))
    # Degree<=8 and eleven distinct rational roots is an exact polynomial test.
    for label, p in [('first equation', first), ('second equation', second), ('density', density_error)]:
        assert len(p) <= 9, ('declared degree', label)
        for i in range(-5, 6):
            assert ev(p, F(i, 2)) == 0, (label, i, ev(p, F(i, 2)))
            count += 1
    assert gaussian(u) == 0, 'first normalization'
    assert gaussian(add(scale(v, 2), mul(u, u))) == 0, 'second normalization'
    count += 2
    # Independent reconstruction of the dual/virial coefficients.
    assert constants == {'a1': F(-2), 'a2': -F(11, 3), 'b1': F(1, 3),
                         'b2': F(3, 4), 'E1': F(-1), 'E2': -F(19, 12)}, 'multipliers'
    count += 1
    for n in [0, 2, 4, 6, 8]:
        observed = [gaussian([F(0)] * n + [F(1)]),
                    2 * gaussian([F(0)] * n + u), gaussian([F(0)] * n + density)]
        expected = {0: [1, 0, 0], 2: [1, 0, 0], 4: [3, -1, 0],
                    6: [15, -15, F(35, 3)], 8: [105, -210, F(1085, 3)]}[n]
        assert observed == expected, ('moments', n, observed)
        if str(n) in m['moment_response']:
            assert observed == list(map(F, m['moment_response'][str(n)])), ('reported moments', n)
        count += 1
    k = m['constants']
    af, ec, gap, qm, radius = map(F, [k['a_floor'], k['E_ceiling'], k['gap_floor'], k['q_window'], k['tail_q_window']])
    assert 0 < af <= F(1, 2) and ec >= 3, 'inherited operator bounds'
    assert gap > 0 and 36 * af > (ec + gap) ** 2, 'harmonic comparison gap'
    assert 0 < radius <= F(1, 200) and 2 * radius <= qm <= F(1, 100), 'windows'
    count += 3
    finite_gap = F(k['finite_gap_rational'])
    assert finite_gap > 0 and 36 * af > (ec + finite_gap) ** 2, 'finite TV gap'
    assert F(k['tv_excess_factor']) * finite_gap == 1, 'TV reciprocal factor'
    assert F(k['example_excess']) == finite_gap * F(k['example_tv']) ** 2, 'TV example budget'
    affinity = F(7, 11)
    assert (2 - 2 * affinity) * (2 + 2 * affinity) / 4 == 1 - affinity ** 2, 'Cauchy affinity identity'
    count += 4
    # Independently evaluate the actual rational mixture, not producer numerators.
    mass, variance = k['tail_mass_power'], k['tail_variance_power']
    assert mass + 3 * variance == -4, 'sixth moment divergence exponent'
    for divisor in [1, 2, 3, 5, 7, 11, 17, 31, 63, 127]:
        q = radius / divisor
        eps, w = q ** mass, q ** variance
        vv = (1 - eps * w) / (1 - eps)
        k0 = (3 - q - 3 * eps * w * w) / ((1 - eps) * vv * vv)
        q0 = 3 - k0
        assert (1 - eps) * vv + eps * w == 1, 'second moment'
        assert (1 - eps) * vv * vv * k0 + 3 * eps * w * w == 3 - q, 'fourth moment'
        assert 0 < q0 - q < 4 * q ** 4 and q0 < 2 * q, 'q0 interval'
        factor = (1 - eps) / vv
        assert 1 < factor < 1 + 2 * q ** 12, 'dilation interval'
        assert 8 * q ** 5 + 4 * q ** 12 + eps / w < F(k['tail_excess_bound']) * q ** 5, 'excess bound'
        assert 15 * eps * w ** 3 == 15 * q ** -4, 'sixth moment lower bound'
        count += 6
    expected = {'exact_optimizer_weighted_second_response': True,
        'finite_q_excess_to_tv': True,
        'near_optimizer_unweighted_second_response': True,
        'near_optimizer_all_polynomial_response': False,
        'near_optimizer_excess_little_o_q4': True,
        'effective_asymptotic_error': False, 'new_fifth_value_coefficient': False,
        'gu_physics': False, 'novelty': False, 'formal_proof': False}
    assert m['scope'] == expected, 'reporting scope'
    for path, digest in m['dependencies'].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, ('dependency', path)
    return count


if __name__ == '__main__':
    model = json.loads((ROOT / 'lab/process/k1862-fisher-second-density-response.json').read_text())
    print('PASS clean K1862 independent baseline:', check(model), 'exact controls; finite mixture fixtures complement producer interval bounds')
    faults = [('u_hermite', '4', '-1/47'), ('v_hermite', '0', '-1/191'),
        ('v_hermite', '2', '-1/49'), ('v_hermite', '4', '-1/63'),
        ('v_hermite', '6', '1/215'), ('v_hermite', '8', '1/4607'),
        ('density_second_hermite', '6', '7/431'), ('density_second_hermite', '8', '1/1151'),
        ('multipliers', 'a2', '-11/4'), ('multipliers', 'b2', '2/3'),
        ('multipliers', 'E2', '-19/11'), ('constants', 'a_floor', '1/4'),
        ('constants', 'E_ceiling', '4'), ('constants', 'tail_mass_power', 19),
        ('constants', 'tail_variance_power', -7), ('constants', 'tail_excess_bound', '8'),
        ('constants', 'finite_gap_rational', '2'), ('constants', 'tv_excess_factor', '1'),
        ('constants', 'example_excess', '3/2500')]
    for section, key, value in faults:
        bad = deepcopy(model)
        bad[section][key] = value
        try:
            check(bad)
        except AssertionError as error:
            print('DETECTED mathematical-input fault', section, key, str(error))
        else:
            raise AssertionError(('undetected input fault', section, key))
    flags = ['near_optimizer_all_polynomial_response', 'near_optimizer_excess_little_o_q4',
             'effective_asymptotic_error', 'gu_physics', 'finite_q_excess_to_tv']
    for flag in flags:
        bad = deepcopy(model)
        bad['scope'][flag] = not bad['scope'][flag]
        try:
            check(bad)
        except AssertionError as error:
            print('DETECTED reporting fault', flag, str(error))
        else:
            raise AssertionError(('undetected reporting fault', flag))
    print('PASS', len(faults), 'mathematical-input faults and', len(flags), 'reporting faults; no crashes counted as detection')
