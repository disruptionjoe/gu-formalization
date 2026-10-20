#!/usr/bin/env python3
"""Sparse exact arithmetic; the written proof owns the analytic estimates."""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]


def add(*ps):
    out = defaultdict(F)
    for p in ps:
        for n, c in p.items():
            out[n] += c
    return {n: c for n, c in out.items() if c}


def scale(p, c):
    return {n: c * v for n, v in p.items() if c * v}


def shift(p, n):
    return {n + k: v for k, v in p.items()}


def mul(p, q):
    out = defaultdict(F)
    for n, c in p.items():
        for j, d in q.items():
            out[n + j] += c * d
    return {n: c for n, c in out.items() if c}


def derivative(p):
    return {n - 1: n * c for n, c in p.items() if n}


def hermite(n):
    a, b = {0: F(1)}, {1: F(1)}
    if n == 0:
        return a
    for k in range(1, n):
        a, b = b, add(shift(b, 1), scale(a, -k))
    return b


def hp(entries):
    return add(*(scale(hermite(int(n)), F(c)) for n, c in entries.items()))


def moment(n):
    if n % 2:
        return F(0)
    result = F(1)
    for j in range(1, n, 2):
        result *= j
    return result


def expectation(p):
    return sum((c * moment(n) for n, c in p.items()), F(0))


def interval(p, radius):
    """Coefficient enclosure on [0,radius], exact and conservative."""
    lo = hi = p.get(0, F(0))
    for n, c in p.items():
        if n:
            if c < 0:
                lo += c * radius ** n
            else:
                hi += c * radius ** n
    return lo, hi


def check(m):
    checks = 0

    def zero(name, p):
        nonlocal checks
        assert not p, (name, p)
        checks += 1

    def equal(name, a, b):
        nonlocal checks
        assert a == b, (name, a, b)
        checks += 1

    u, v = hp(m['u_hermite']), hp(m['v_hermite'])
    d2 = hp(m['density_second_hermite'])
    z = {0: F(1)}
    c = {k: F(value) for k, value in m['multipliers'].items()}
    A = lambda p: add(scale(derivative(derivative(p)), -4),
                      scale(shift(derivative(p), 1), 4))
    W1 = {2: c['a1'], 4: c['b1']}
    W2 = {2: c['a2'], 4: c['b2']}
    zero('first oscillator residual', add(A(u), W1, {0: -c['E1']}))
    zero('second oscillator residual', add(A(v), mul(W1, u),
         scale(u, -c['E1']), W2, {0: -c['E2']}))
    zero('density second polynomial', add(scale(v, 2), mul(u, u), scale(d2, -1)))
    equal('normalization first', expectation(u), 0)
    equal('normalization second', expectation(add(scale(v, 2), mul(u, u))), 0)
    # Virial coefficients reconstructed from the value and subgradient expansion.
    equal('b1 secant', c['b1'], F(1, 3))
    equal('b2 secant', c['b2'], F(3, 4))
    equal('a1 virial', c['a1'], -6 * c['b1'])
    equal('a2 virial', c['a2'], F(1, 6) + 2 * c['b1'] - 6 * c['b2'])
    equal('E1 virial', c['E1'], -3 * c['b1'])
    equal('E2 virial', c['E2'], F(1, 3) + c['b1'] - 3 * c['b2'])
    for n, values in m['moment_response'].items():
        n = int(n)
        equal('moment response ' + str(n),
              [moment(n), 2 * expectation(shift(u, n)), expectation(shift(d2, n))],
              list(map(F, values)))
    for n, first in [(0, 0), (2, 0), (4, -1)]:
        equal('prescribed moment first ' + str(n), 2 * expectation(shift(u, n)), first)
        equal('prescribed moment second ' + str(n), expectation(shift(d2, n)), 0)
    # Derive the weighted energy cross-term coefficient at several degrees.
    for degree in range(1, 6):
        weight = {degree: F(1)}
        zero('weight derivative ' + str(degree),
             add(mul(derivative(weight), derivative(weight)),
                 {2 * degree - 2: F(-degree * degree)}))
    k = m['constants']
    qm, af, ec, gap = map(F, [k['q_window'], k['a_floor'], k['E_ceiling'], k['gap_floor']])
    assert 0 < qm <= F(1, 100), 'optimizer window'
    assert 0 < af <= F(1, 2) and ec >= 3, 'inherited operator bounds'
    assert gap > 0 and 36 * af > (ec + gap) ** 2, 'full-line spectral gap'
    checks += 3
    finite_gap = F(k['finite_gap_rational'])
    assert finite_gap > 0 and 36 * af > (ec + finite_gap) ** 2, 'finite TV gap'
    checks += 1
    equal('TV reciprocal factor', F(k['tv_excess_factor']) * finite_gap, 1)
    equal('TV precision budget', F(k['example_excess']),
          finite_gap * F(k['example_tv']) ** 2)
    zero('affinity Cauchy product', add(mul({0: F(1), 1: F(-1)},
         {0: F(1), 1: F(1)}), {0: F(-1), 2: F(1)}))
    radius = F(k['tail_q_window'])
    assert 0 < radius <= F(1, 200) and 2 * radius <= qm, 'tail window'
    mass, variance = k['tail_mass_power'], k['tail_variance_power']
    equal('tail fourth exponent', mass + 2 * variance, 4)
    equal('tail second exponent', mass + variance, 12)
    equal('tail sixth exponent', mass + 3 * variance, -4)
    # Work with rational numerators, not a sampled small-q approximation.
    U, V = {0: F(1), mass: F(-1)}, {0: F(1), mass + variance: F(-1)}
    K = {0: F(3), 1: F(-1), mass + 2 * variance: F(-3)}
    V2, U2 = mul(V, V), mul(U, U)
    zero('mixture second moment', add(V, {mass + variance: F(1)}, {0: F(-1)}))
    zero('mixture fourth moment', add(K, {mass + 2 * variance: F(3)}, {0: F(-3), 1: F(1)}))
    numerator = add(mul({0: F(3), 1: F(-1)}, V2), scale(mul(K, U), -1))
    normalized = shift(numerator, -4)
    assert min(normalized) >= 0, 'q0 difference order'
    assert interval(normalized, radius)[0] > 0, 'q0 larger than q'
    assert interval(add(scale(V2, 4), scale(normalized, -1)), radius)[0] > 0, 'q0 difference upper'
    assert 4 * radius ** 3 < 1, 'q0 below 2q'
    factor_num = add(U2, scale(V, -1))
    factor_div = shift(factor_num, -12)
    assert interval(factor_div, radius)[0] > 0, 'scaling factor above1'
    assert interval(add(scale(V, 2), scale(factor_div, -1)), radius)[0] > 0, 'scaling factor upper'
    bound = F(k['tail_excess_bound'])
    assert 8 + 4 * radius ** 7 + radius ** 23 < bound, 'tail excess bound'
    checks += 8
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
    return checks


if __name__ == '__main__':
    model = json.loads((ROOT / 'lab/process/k1862-fisher-second-density-response.json').read_text())
    print('PASS K1862:', check(model), 'exact polynomial, interval and operator-bound groups; dependency and scope checks separate')
