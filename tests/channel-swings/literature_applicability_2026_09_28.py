#!/usr/bin/env python3
"""Exact literature applicability controls; not a GU theorem or paper reproduction.

Run from any directory. Standard library only; no generated files.
Native K438/K439/K446 are inputs to comparisons, not independently re-proved.
The diagonal model assumes their spectral theorem. Chain maps below are explicit
factorized controls. The last two tests use an ordinary Euclidean metric
boundary comparator, not the GU observation map.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[2]


def native(name):
    return json.loads((ROOT / "lab/process" / name).read_text())


def sign(x, a=F(13823, 575), b=F(-13248, 575)):
    return a*x + b*x**3


def product(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def difference(a, b):
    return [[x-y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def chain(high_defect=False, low_defect=False):
    # C1 = C2 (+) C0; actual sparse injections/projections, not rank flags.
    n2, n0 = 21*512, 70*512
    d2 = {i: i for i in range(n2) if not (high_defect and i % 512 == 0)}
    d1 = {n2+i: i for i in range(n0) if not (low_defect and i % 512 == 256)}
    return (n2, n2+n0, n0), d2, d1


def homology(c):
    dims, d2, d1 = c
    if set(d2.values()) & set(d1):
        raise ValueError("not a chain complex")
    r2, r1 = len(set(d2.values())), len(set(d1.values()))
    return [dims[0]-r2, dims[1]-r1-r2, dims[2]-r1]


# Gaussian rationals as pairs; there is no floating-point arithmetic.
Z, ONE, I = (F(0), F(0)), (F(1), F(0)), (F(0), F(1))


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def scale(a, b):
    return (a*b[0], a*b[1])


def total(xs):
    out = Z
    for x in xs:
        out = add(out, x)
    return out


def boundary_mode(decay=1):
    q = [I, Z, Z, (F(-decay), F(0))]
    xi = [Z, Z, Z, ONE]
    h = [[add(mul(q[a], xi[b]), mul(xi[a], q[b]))
          for b in range(4)] for a in range(4)]
    trace = total(h[a][a] for a in range(4))
    gauge = [add(total(mul(q[a], h[a][b]) for a in range(4)),
                 scale(F(-1, 2), mul(q[b], trace))) for b in range(4)]
    return q, xi, h, gauge


class ApplicabilityControls(unittest.TestCase):
    def test_01_derive_odd_cubic(self):
        # a+b=1; a/24+b/24^3=1, solved without importing coefficients.
        s = F(1, 24)
        b = (1-s)/(s**3-s)
        a = 1-b
        self.assertEqual((a, b), (F(13823, 575), F(-13248, 575)))

    def test_02_quartic_and_projectors(self):
        for x in [F(1), F(-1), F(1, 24), F(-1, 24)]:
            self.assertEqual(576*x**4-577*x**2+1, 0)
            j = sign(x)
            p, m = (1+j)/2, (1-j)/2
            self.assertEqual((j*j, p*p, m*m, p*m, p+m), (1, p, m, 0, 1))
            self.assertEqual(sign(-x), -j)

    def test_03_rank_and_inverse_comparison(self):
        spec = [(F(1), 192), (F(-1), 192), (F(1, 24), 64), (F(-1, 24), 64)]
        self.assertEqual(sum(n for x, n in spec), 512)
        self.assertEqual(sum(n for x, n in spec if sign(x) == 1), 256)
        self.assertEqual(max(abs(1/x) for x, n in spec), 24)
        k438 = native("k438-k77-constraint-compressed-boundary-symbol.json")
        self.assertEqual(k438["cross_characteristic_result"]["characteristic_polynomial_on_im_P"],
                         "(x^2-1)^192 (x^2-1/576)^64")
        k439 = native("k439-k77-compatible-corrected-boundary-split.json")
        self.assertEqual(k439["cross_characteristic_result"]["rank_fingerprint"]["canonical_incoming"], 256)

    def test_04_coefficient_mutation_rejected(self):
        self.assertNotEqual(sign(F(1, 24), a=F(13824, 575)), 1)

    def test_05_coupling_intertwining(self):
        p = [[1, 0], [0, 0]]
        diagonal = [[2, 0], [0, 3]]
        swap = [[0, 1], [1, 0]]
        self.assertEqual(difference(product(p, diagonal), product(diagonal, p)), [[0, 0], [0, 0]])
        defect = difference(product(p, swap), product(swap, p))
        self.assertEqual(defect, [[0, 1], [-1, 0]])
        self.assertEqual(defect[0][0]*defect[1][1]-defect[0][1]*defect[1][0], 1)

    def test_06_decoupled_chain(self):
        self.assertEqual(homology(chain()), [0, 0, 0])

    def test_07_low_defect(self):
        h = homology(chain(low_defect=True))
        self.assertEqual(h, [0, 70, 70])
        self.assertEqual(h, native("k446-k77-compatible-nilpotent-cohomology-obstruction.json")
                         ["low_arrow_defect"]["cohomology_dimensions_H2_H1_H0"])

    def test_08_high_defect(self):
        h = homology(chain(high_defect=True))
        self.assertEqual(h, [21, 21, 0])
        self.assertEqual(h, native("k446-k77-compatible-nilpotent-cohomology-obstruction.json")
                         ["high_arrow_defect"]["cohomology_dimensions_H2_H1_H0"])

    def test_09_both_boundary_squares(self):
        for c in [chain(), chain(low_defect=True), chain(high_defect=True)]:
            dims, d2, d1 = c
            # Every degree uses the same carrier index; first 256 is one half.
            half = lambda index: index % 512 < 256
            self.assertTrue(all(half(src) == half(dst) for src, dst in d2.items()))
            self.assertTrue(all(half(src) == half(dst) for src, dst in d1.items()))
            self.assertEqual(len(set(d2.values()) & set(d1)), 0)

    def test_10_nilpotence_mutation_rejected(self):
        dims, d2, d1 = chain()
        d1[0] = 0
        with self.assertRaises(ValueError):
            homology((dims, d2, d1))

    def test_11_euclidean_boundary_moving_mode(self):
        q, xi, h, gauge = boundary_mode()
        self.assertEqual(total(mul(x, x) for x in q), Z)  # bilinear, not Hermitian
        self.assertTrue(all(h[a][b] == Z for a in range(3) for b in range(3)))
        self.assertEqual(gauge, [Z]*4)
        self.assertNotEqual(xi[3], Z)
        self.assertNotEqual(h[3][3], Z)

    def test_12_wrong_decay_rejected(self):
        q, xi, h, gauge = boundary_mode(decay=2)
        self.assertNotEqual(total(mul(x, x) for x in q), Z)
        self.assertNotEqual(gauge, [Z]*4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
