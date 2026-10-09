#!/usr/bin/env python3
"""Independent matrix realization of the curved I1B energy coefficients.

No sparse Clifford engine or coefficient bank is imported. Gamma matrices
act on the 128 occupation states of seven fermionic modes. The selected
Shiab contraction is expanded analytically before matrix traces are taken.
This verifies finite action coefficients, not a global evolution theorem.
"""
from functools import lru_cache
from itertools import permutations
import json

import sympy as sp


ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
RADIAL = 10
POSITIVE = tuple(i for i, s in enumerate(ETA) if s == 1)
NEGATIVE = tuple(i for i, s in enumerate(ETA) if s == -1)
MODE = {axis: j for axes in (POSITIVE, NEGATIVE) for j, axis in enumerate(axes)}


def gamma_action(axis, state):
    """(creation+annihilation), or (creation-annihilation), on |state>."""
    mode = MODE[axis]
    sign = (-1) ** ((state & ((1 << mode) - 1)).bit_count())
    if ETA[axis] == -1 and state & (1 << mode):
        sign = -sign
    return state ^ (1 << mode), sign


@lru_cache(maxsize=None)
def trace_word(word):
    diagonal_sum = 0
    for initial in range(128):
        state, coefficient = initial, 1
        for axis in reversed(word):
            state, factor = gamma_action(axis, state)
            coefficient *= factor
        if state == initial:
            diagonal_sum += coefficient
    return sp.Rational(diagonal_sum, 128)


def word(mask):
    return tuple(i for i in range(14) if mask & (1 << i))


@lru_cache(maxsize=None)
def shiab_pair(mu, left, p, q, right):
    """Tr[e^mu left wedge S(e^p wedge e^q right)], expanded from S.

    Phi_1=sum e^a gamma_a, Phi_2=sum_(a<b)e^a e^b gamma_a gamma_b.
    The signature has seven negative directions, hence *vol=-1. The two
    symi channels contribute i^2=-1. Both signs enter the last term below.
    """
    if p == q:
        return sp.S.Zero
    if p > q:
        return -shiab_pair(mu, left, q, p, right)
    first = sp.S.Zero
    if mu == p:
        first += trace_word(left + (q,) + right) - trace_word(left + right + (q,))
    if mu == q:
        first -= trace_word(left + (p,) + right) - trace_word(left + right + (p,))
    second = sum(trace_word(left + term) for term in (
        (mu, p, q) + right,
        (mu,) + right + (p, q),
        (p, q) + right + (mu,),
        right + (p, q, mu),
    ))
    return ETA[p] * ETA[q] * (first - sp.Rational(ETA[mu], 2) * second)


def derivative_entry(axis, u, v):
    mu, left = u
    nu, right = v
    return (shiab_pair(mu, left, axis, nu, right)
            - shiab_pair(nu, right, axis, mu, left)) / 2


def mass_entry(u, v):
    return ETA[u[0]] * trace_word(u[1] + v[1]) if u[0] == v[0] else sp.S.Zero


def cubic_entry(background, u, v):
    value = sp.S.Zero
    for coefficient, b in background:
        for receiver, left, right in permutations((u, v, b)):
            value += coefficient * shiab_pair(receiver[0], receiver[1],
                                              left[0], right[0], left[1] + right[1]) / 3
    return value


def backgrounds():
    return [
        [(sp.S.One, (mu, (mu,))) for mu in range(14) if mu != RADIAL],
        [(sp.S.One, (RADIAL, (RADIAL,)))],
        [(sp.Rational(-1, 8), (mu, (RADIAL, mu))) for mu in range(4)],
        [(sp.S.One, (mu, (RADIAL, mu))) for mu in range(4, 14) if mu != RADIAL],
    ]


def packet_basis(seed, imaginary=True):
    labels = (seed, seed ^ 1, seed ^ (1 << RADIAL), seed ^ 1 ^ (1 << RADIAL))
    residues = (0, 3) if imaginary else (1, 2)
    return [(mu, word(label ^ (1 << mu))) for label in labels for mu in range(14)
            if (label ^ (1 << mu)).bit_count() % 4 in residues]


def time_block(basis):
    return sp.Matrix(len(basis), len(basis),
                     lambda i, j: derivative_entry(0, basis[i], basis[j]))


def certify(progress=None):
    checks = []

    def check(label, condition):
        assert condition, label
        checks.append(label)

    for a in range(14):
        for b in range(14):
            for state in range(128):
                s1, c1 = gamma_action(b, state)
                s1, c2 = gamma_action(a, s1)
                s2, c3 = gamma_action(a, state)
                s2, c4 = gamma_action(b, s2)
                assert s1 == s2
                assert c1*c2+c3*c4 == (2*ETA[a] if a == b else 0)
    check("all 128-state gamma matrices satisfy every Clifford relation", True)
    check("normalized matrix trace has the declared scalar normalization",
          trace_word(()) == 1 and all(trace_word((a,)) == 0 for a in range(14)))

    source = packet_basis(1 << RADIAL)
    e0 = time_block(source)
    scalar = source.index((RADIAL, ()))
    s = sp.eye(len(source))[:, scalar]
    kernel = sp.Matrix.hstack(*e0.nullspace())
    check("independent source time form is skew and the scalar is transverse to its kernel",
          e0.T == -e0 and kernel.T*s == sp.zeros(kernel.cols, 1))
    check("independent scalar time symplectic partner has coefficient minus 48",
          (s.T*e0*e0*s)[0] == -48)
    witnesses = []
    for axis, sign in ((4, 1), (1, -1)):
        target = packet_basis((1 << RADIAL) ^ (1 << axis))
        et = time_block(target)
        nt = sp.Matrix.hstack(*et.nullspace())
        cross = sp.Matrix(len(target), len(source),
                          lambda i, j: derivative_entry(axis, target[i], source[j]))
        check(f"axis {axis}: independent primary kernels have zero derivative pairing",
              nt.T*cross*kernel == sp.zeros(nt.cols, kernel.cols))
        force = nt.T*cross*s
        nonzero = [j for j in range(force.rows) if force[j]]
        assert len(nonzero) == 1
        j = nonzero[0]
        n = nt[:, j]
        receiver = (0, tuple(sorted((0, axis, RADIAL))))
        expected = sp.eye(len(target))[:, target.index(receiver)]
        check(f"axis {axis}: complete primary force is two on the explicit gamma receiver",
              force[j] == 2 and n == expected)
        mass_column = sp.Matrix([mass_entry(u, receiver) for u in target])
        check(f"axis {axis}: exact primary Hodge mass column has sign {sign}",
              nt.T*mass_column == sign*sp.eye(nt.cols)[:, j])
        cubic_columns = [nt.T*sp.Matrix([cubic_entry(b, u, receiver) for u in target])
                         for b in backgrounds()]
        check(f"axis {axis}: all four independent primary cubic columns vanish",
              all(c == sp.zeros(nt.cols, 1) for c in cubic_columns))
        kappa = sp.symbols('kappa', real=True, nonzero=True)
        coefficient = -force[j]**2/(2*sign*kappa)
        witnesses.append({"axis": axis, "primary_source": str(force[j]),
                          "receiver": [receiver[0], list(receiver[1])],
                          "mass_sign": sign, "reduced_energy": str(coefficient),
                          "target_dimension": len(target), "kernel_dimension": nt.cols})
        if progress:
            progress(f"Independent matrix witness along axis {axis}: {coefficient}")
    return {"passed": len(checks), "checks": checks, "witnesses": witnesses,
            "implementation": "128 occupation-state Clifford matrices; no sparse engine or coefficient-bank import",
            "scope": "independent finite coefficients for the two imaginary-packet energy witnesses"}


if __name__ == '__main__':
    import sys
    print(json.dumps(certify(lambda message: print(message, file=sys.stderr, flush=True)), indent=2))
