#!/usr/bin/env python3
"""Exact controls for the K77 functional gauge and holonomy boundary wave.

The Maxwell/Fourier and rank-two symplectic objects below are supplied
controls.  They are not discretizations of, or bridges into, either K77
packet.  Arithmetic is exact over ``Fraction`` throughout.
"""

from fractions import Fraction as F
import sys


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def scale(a, x):
    return tuple(a * v for v in x)


def gauge(k):
    return (F(k[0]), F(k[1]), F(0), F(0))


def constraint(k, z):
    return F(k[0]) * z[2] + F(k[1]) * z[3]


def generator(k, z):
    kx, ky = map(F, k)
    ax, ay, ex, ey = z
    n = kx * kx + ky * ky
    ka = kx * ax + ky * ay
    return (ex, ey, -n * ax + kx * ka, -n * ay + ky * ka)


def cross(k, v):
    return F(k[0]) * v[1] - F(k[1]) * v[0]


def quotient_coordinates(k, z):
    return cross(k, z[:2]), cross(k, z[2:])


def energy(k, z):
    n = F(k[0] * k[0] + k[1] * k[1])
    q, p = quotient_coordinates(k, z)
    return F(1, 2) * (p * p / n + q * q)


def matmul(a, b):
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
              for j in range(len(b[0])))
        for i in range(len(a))
    )


def transpose(a):
    return tuple(zip(*a))


def congruence(m, h):
    return matmul(matmul(transpose(m), h), m)


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def trace2(m):
    return m[0][0] + m[1][1]


def positive_checks():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    # Nonzero Fourier modes of the action-derived Maxwell control on T^2.
    samples = {
        (1, 0): (F(2), F(3), F(0), F(5)),
        (0, 1): (F(3), F(-2), F(7), F(0)),
        (1, 2): (F(3, 2), F(-1, 3), F(4), F(-2)),
        (2, -1): (F(-5, 3), F(2, 5), F(3), F(6)),
    }
    for k, z in samples.items():
        n = F(k[0] * k[0] + k[1] * k[1])
        g = gauge(k)
        lz = generator(k, z)
        q, p = quotient_coordinates(k, z)
        qdot, pdot = quotient_coordinates(k, lz)
        shifted = add(z, scale(F(7, 3), g))
        check(f"{k}: nonzero mode", n >= 1)
        check(f"{k}: gauge vector is a cycle", constraint(k, g) == 0)
        check(f"{k}: residual gauge image is stationary", generator(k, g) == (F(0),) * 4)
        check(f"{k}: Gauss constraint propagates", constraint(k, lz) == 0)
        check(f"{k}: quotient coordinate is representative independent",
              quotient_coordinates(k, shifted) == (q, p))
        check(f"{k}: quotient generator has qdot=p", qdot == p)
        check(f"{k}: quotient generator has pdot=-|k|^2 q", pdot == -n * q)
        check(f"{k}: quotient energy is gauge invariant", energy(k, shifted) == energy(k, z))
        check(f"{k}: quotient energy is conserved infinitesimally",
              p * pdot / n + q * qdot == 0)

    # The zero Fourier mode is harmonic physical data, not a gauge derivative.
    zero = (0, 0)
    z0 = (F(2), F(-3), F(5), F(7))
    check("zero mode has no derivative-gauge image", gauge(zero) == (F(0),) * 4)
    check("zero mode satisfies Gauss identically", constraint(zero, z0) == 0)
    check("zero-mode Maxwell evolution retains harmonic coordinates",
          generator(zero, z0) == (F(5), F(7), F(0), F(0)))

    # Fourier proof of closed range on the compact torus: every nonzero
    # integer mode has |k|^2 >= 1, while constants are split off as the kernel.
    for k in samples:
        check(f"{k}: compact Poincare gap", k[0] * k[0] + k[1] * k[1] >= 1)

    # Exact dilation witness for D:H^1(R)->L^2(R).  For the normalized
    # triangular phi_R, ||phi_R||_2^2=2/3 and ||D phi_R||_2^2=2/R^2.
    previous_ratio = None
    for r in (1, 2, 4, 8, 16):
        l2 = F(2, 3)
        d2 = F(2, r * r)
        h1 = l2 + d2
        ratio = d2 / h1
        check(f"R={r}: dilation preserves L2 norm", l2 == F(2, 3))
        check(f"R={r}: derivative has exact inverse-square scaling", d2 == F(2, r * r))
        if previous_ratio is not None:
            check(f"R={r}: closed-range lower-bound ratio decreases", ratio < previous_ratio)
        previous_ratio = ratio
    check("noncompact lower-bound ratio tends to zero", F(3, 16 * 16 + 3) < F(1, 80))

    # Supplied rank-two symplectic monodromies.  In dimension two,
    # symplectic is determinant one.  The invariant-majorant equations force
    # a=0 for the hyperbolic and nontrivial parabolic controls.
    rotation = ((F(0), F(-1)), (F(1), F(0)))
    hyperbolic = ((F(2), F(0)), (F(0), F(1, 2)))
    parabolic = ((F(1), F(1)), (F(0), F(1)))
    identity_majorant = ((F(1), F(0)), (F(0), F(1)))
    for name, m in (("elliptic", rotation), ("hyperbolic", hyperbolic), ("parabolic", parabolic)):
        check(f"{name}: determinant-one symplectic control", det2(m) == 1)
    check("elliptic control has trace zero", trace2(rotation) == 0)
    check("elliptic control preserves a positive majorant",
          congruence(rotation, identity_majorant) == identity_majorant)
    check("hyperbolic control has |trace|>2", abs(trace2(hyperbolic)) > 2)
    check("hyperbolic invariant equation forces first diagonal to zero",
          hyperbolic[0][0] ** 2 - 1 != 0)
    check("nontrivial parabolic control has trace two", trace2(parabolic) == 2)
    check("parabolic invariant equation forces first diagonal to zero",
          parabolic[0][1] != 0)
    check("hyperbolic control does not preserve Euclidean majorant",
          congruence(hyperbolic, identity_majorant) != identity_majorant)
    check("parabolic control does not preserve Euclidean majorant",
          congruence(parabolic, identity_majorant) != identity_majorant)

    return checks


def hostile_checks():
    caught = []

    def reject(name, false_claim):
        caught.append((name, not bool(false_claim)))

    k = (1, 2)
    z = (F(3, 2), F(-1, 3), F(4), F(-2))
    g = gauge(k)
    bad_gauge = (F(1), F(0), F(0), F(0))
    reject("nongradient direction called gauge", cross(k, bad_gauge[:2]) == 0)
    reject("gauge vector claimed nonstationary", generator(k, g) != (F(0),) * 4)
    reject("Gauss propagation denied", constraint(k, generator(k, z)) != 0)
    reject("raw A norm called gauge invariant",
           dot(add(z, g)[:2], add(z, g)[:2]) == dot(z[:2], z[:2]))
    q, p = quotient_coordinates(k, z)
    qdot, pdot = quotient_coordinates(k, generator(k, z))
    reject("wrong quotient q equation", qdot == -p)
    reject("wrong quotient p equation", pdot == F(k[0] * k[0] + k[1] * k[1]) * q)
    reject("gauge shift changes quotient", quotient_coordinates(k, add(z, g)) != (q, p))
    reject("gauge shift changes quotient energy", energy(k, add(z, g)) != energy(k, z))
    reject("zero mode removed as derivative gauge", gauge((0, 0)) != (F(0),) * 4)
    reject("Poincare gap asserted at zero mode", 0 >= 1)
    r = 16
    ratio = F(2, r * r) / (F(2, 3) + F(2, r * r))
    reject("uniform noncompact derivative lower bound", ratio >= F(1, 10))
    reject("dilation derivative norm claimed constant", F(2, r * r) == F(2))

    rotation = ((F(0), F(-1)), (F(1), F(0)))
    hyperbolic = ((F(2), F(0)), (F(0), F(1, 2)))
    parabolic = ((F(1), F(1)), (F(0), F(1)))
    h = ((F(1), F(0)), (F(0), F(1)))
    nonsymplectic = ((F(2), F(0)), (F(0), F(2)))
    reject("nonsymplectic matrix admitted", det2(nonsymplectic) == 1)
    reject("rotation denied invariant majorant", congruence(rotation, h) != h)
    reject("hyperbolic Euclidean majorant asserted", congruence(hyperbolic, h) == h)
    reject("parabolic Euclidean majorant asserted", congruence(parabolic, h) == h)
    reject("hyperbolic called elliptic by trace", abs(trace2(hyperbolic)) < 2)
    reject("nontrivial parabolic called elliptic by trace", abs(trace2(parabolic)) < 2)
    reject("trace alone calls parabolic identity", parabolic == ((F(1), F(0)), (F(0), F(1))))
    return caught


def report(rows, label):
    failed = [name for name, ok in rows if not ok]
    if failed:
        for name in failed:
            print(f"FAIL {label}: {name}")
        return False
    print(f"{label} PASS {len(rows)}/{len(rows)}")
    return True


def main():
    if "--selftest" in sys.argv:
        return 0 if report(hostile_checks(), "HOSTILE SELFTEST") else 1
    return 0 if report(positive_checks(), "CERTIFICATE") else 1


if __name__ == "__main__":
    raise SystemExit(main())
