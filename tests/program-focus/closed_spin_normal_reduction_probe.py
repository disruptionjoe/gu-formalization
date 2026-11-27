#!/usr/bin/env python3
"""Exact arithmetic controls, not a proof of Furuta/Wu or manifold existence."""
from fractions import Fraction as F
import json
from math import gcd
import time


def dot(q, x, y):
    return sum(x[i] * q[i][j] * y[j] for i in range(len(q)) for j in range(len(q)))


def det(a):
    a = [[F(x) for x in row] for row in a]
    out = F(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            out *= -1
        p = a[i][i]
        out *= p
        for j in range(i + 1, len(a)):
            factor = a[j][i] / p
            for k in range(i + 1, len(a)):
                a[j][k] -= factor * a[i][k]
    return out


def blockdiag(*blocks):
    n = sum(len(q) for q in blocks)
    out = [[0] * n for _ in range(n)]
    offset = 0
    for q in blocks:
        for i, row in enumerate(q):
            for j, v in enumerate(row):
                out[offset+i][offset+j] = v
        offset += len(q)
    return out


def main():
    start = time.monotonic()
    checks = {}
    def check(name, truth):
        assert name not in checks
        checks[name] = bool(truth)
        assert truth, name
    h = [[0, 1], [1, 0]]
    check('hyperbolic_unimodular', det(h) == -1)
    certificates = []
    for k in [-17, -3, -1, 0, 1, 4, 19]:
        a = [1, 6*k]
        c = [2*x for x in a]
        check(f'witness_{k}', dot(h, c, c) == 48*k)
        check(f'even_lift_{k}', all(x % 2 == 0 for x in c))
        check(f'orientation_reversal_{k}', dot([[-x for x in row] for row in h], c, c) == 3*(-16*k))
        if k:
            check(f'planted_half_coefficient_rejected_{k}', dot(h, [2, 6*k], [2, 6*k]) != 48*k)
        certificates.append({'signature':16*k, 'a':a, 'c':c, 'square':dot(h, c, c)})
    # Primitive isotropic e, any paired f0, evenness enables null correction.
    for m in [-11, -1, 0, 2, 13]:
        q = [[0, 1], [1, 2*m]]
        e, f = [1, 0], [-m, 1]
        check(f'null_adjustment_{m}', dot(q, e, e) == dot(q, f, f) == 0 and dot(q, e, f) == 1)
        check(f'unimodular_adjustment_{m}', det(q) == -1)
        for k in [-2, 3]:
            a = [e[i]+6*k*f[i] for i in range(2)]
            check(f'nonstandard_basis_{m}_{k}', 4*dot(q, a, a) == 48*k)
    # The normalization test must reject a non-unimodular rescaling.
    check('planted_rescaled_pair_rejected', 4*dot([[0, 2], [2, 0]], [1, 6], [1, 6]) != 48)
    # Known closed Lorentz spin example: K3 # 12(S1 x S3).
    e8 = [[2*int(i == j) for j in range(8)] for i in range(8)]
    for i, j in [(i, i+1) for i in range(6)] + [(2, 7)]:
        e8[i][j] = e8[j][i] = -1
    check('e8_unimodular', det(e8) == 1)
    check('e8_positive', all(det([row[:i] for row in e8[:i]]) > 0 for i in range(1, 9)))
    minus_e8 = [[-v for v in row] for row in e8]
    q = blockdiag(minus_e8, minus_e8, h, h, h)
    c = [0]*22
    c[16], c[17] = 2, -12
    check('k3_lorentz_euler', 2-2*12+22 == 0)
    check('k3_closed_square', dot(q, c, c) == -48)
    check('k3_c1_zero_not_repair', dot(q, [0]*22, [0]*22) != -48)
    check('k3_orientation_reverse', dot([[-v for v in row] for row in q], c, c) == 48)
    # Test the 10/8 *stabilization* algebra; it is not a numerical proof of Furuta.
    for rank in [8, 16, 32, 48]:
        check(f'definite_stabilization_contradiction_{rank}', 4*(rank+2) < 5*rank+8)
    check('zero_rank_exception_survives', 4*2 == 5*0+8)
    # A/2A arithmetic for torsion; no assumption that H2 is torsion free.
    for modulus in [2, 4, 5, 6, 8, 12]:
        doubles = {(2*x) % modulus for x in range(modulus)}
        check(f'torsion_quotient_order_{modulus}', modulus // len(doubles) == gcd(modulus, 2))
    check('nonzero_even_torsion_not_trivial', 2 != 0 and 2 in {(2*x) % 4 for x in range(4)})
    check('rank_zero_lorentz_control', 2-2*1+0 == 0 and 0 == 3*0)
    check('torus_zero_signature_control', 2-2*4+6 == 0 and 0 == 3*0)
    # Outside-class controls prevent spin-only or Lorentz-only promotion.
    check('s4_spin_only_fails_wu', 0 != 2*2+3*0)
    odd_squares = {x*x % 8 for x in range(1, 16, 2)}
    check('odd_square_residue_calibration', odd_squares == {1})
    check('nonspin_chi_zero_no_complex', 3*2 % 8 not in {(x+y) % 8 for x in odd_squares for y in odd_squares})
    check('nonspin_lorentz_euler', 3+3-2-2*2 == 0)
    result = {'status':'PASS', 'grouped_checks':len(checks), 'checks':checks,
              'hyperbolic_witness_certificates':certificates,
              'scope':'Exact bilinear, parity and characteristic-number controls only. Smoothness, spin, Lorentz existence, Furuta/Rokhlin/Wu and lattice classification remain written theorem inputs. No finite sample certifies their universal quantifiers.',
              'runtime_seconds':time.monotonic()-start}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
