#!/usr/bin/env python3
"""Exact local tensor identities; causal support is proved in the companion note."""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]


def verify(d):
    x = s.symbols('t x y z', real=True)
    t = x[0]
    chi = s.Function('chi')(*x)
    a = s.Function('a')(t)
    k = s.symbols('k', nonzero=True)
    ss = s.symbols('s11 s22 s33 s12 s13 s23')
    S = s.Matrix([[ss[0], ss[3], ss[4]], [ss[3], ss[1], ss[5]], [ss[4], ss[5], ss[2]]])
    eta = s.diag(-1, 1, 1, 1)
    rat = lambda key: s.Rational(d[key])
    T = s.zeros(4)
    T[0, 0] = sum(S[i, j] * s.diff(chi, x[i+1], x[j+1]) for i in range(3) for j in range(3))
    for i in range(3):
        T[0, i+1] = T[i+1, 0] = rat('stress_cross_factor') * sum(S[i, j] * s.diff(chi, t, x[j+1]) for j in range(3))
        for j in range(3):
            T[i+1, j+1] = rat('stress_spatial_factor') * S[i, j] * s.diff(chi, t, 2)
    for nu in range(4):
        assert s.simplify(sum(eta[mu, mu] * s.diff(T[mu, nu], x[mu]) for mu in range(4))) == 0
    groups = 1
    hb = s.zeros(4)
    for i in range(3):
        for j in range(3):
            hb[i+1, j+1] = -rat('wave_factor') * k * S[i, j] * a
    h = hb - rat('trace_reverse_factor') * eta * s.trace(eta * hb)
    R = {}
    for aa in range(4):
        for bb in range(4):
            for cc in range(4):
                for dd in range(4):
                    R[aa, bb, cc, dd] = (s.diff(h[aa, dd], x[bb], x[cc]) + s.diff(h[bb, cc], x[aa], x[dd]) - s.diff(h[aa, cc], x[bb], x[dd]) - s.diff(h[bb, dd], x[aa], x[cc])) / 2
    Ric = s.Matrix(4, 4, lambda i, j: s.simplify(sum(eta[m, m] * R[m, i, m, j] for m in range(4))))
    scalar = s.simplify(s.trace(eta * Ric))
    Ein = Ric - eta * scalar / 2
    target = s.zeros(4)
    for i in range(3):
        for j in range(3):
            target[i+1, j+1] = -k * S[i, j] * s.diff(a, t, 2)
    assert (Ein - target).applyfunc(s.simplify) == s.zeros(4)
    groups += 1
    A = S * s.diff(a, t, 2)
    E = s.Matrix(3, 3, lambda i, j: R[0, i+1, 0, j+1])
    assert (E - k * (A - rat('tidal_trace_factor') * s.eye(3) * s.trace(A))).applyfunc(s.simplify) == s.zeros(3)
    assert (rat('inverse_factor') * (E - s.eye(3) * s.trace(E)) / k - A).applyfunc(s.simplify) == s.zeros(3)
    assert s.simplify(scalar - rat('scalar_factor') * k * s.trace(A)) == 0
    groups += 3
    W = s.Matrix(3, 3, lambda i, j: s.simplify(E[i, j] + Ric[i+1, j+1]/2 - s.KroneckerDelta(i, j)*Ric[0, 0]/2 - s.KroneckerDelta(i, j)*scalar/6))
    assert (W - rat('weyl_factor') * k * (A - s.eye(3)*s.trace(A)/3)).applyfunc(s.simplify) == s.zeros(3)
    assert s.simplify(s.trace(W)) == 0
    groups += 2
    # Arbitrary nonnull symbol; do not use symbol inversion to define the null domain.
    p = s.Matrix([2, 1, 0, 0])
    p2 = (p.T * eta * p)[0]
    Pi = eta - rat('transverse_factor') * p * p.T / p2
    assert p.T * eta * Pi == s.zeros(1, 4)
    assert s.trace(eta * Pi) == 3
    def project(B):
        return B - rat('trace_projector_factor') * Pi * s.trace(eta * B)
    conserved = s.zeros(4)
    for i in range(3):
        for j in range(3):
            conserved[i+1, j+1] = S[i, j]
        conserved[0, i+1] = conserved[i+1, 0] = S[0, i] / 2
    conserved[0, 0] = S[0, 0] / 4
    assert p.T * eta * conserved == s.zeros(1, 4)
    result = project(conserved)
    assert p.T * eta * result == s.zeros(1, 4)
    assert s.simplify(s.trace(eta * result)) == 0
    assert (project(result) - result).applyfunc(s.simplify) == s.zeros(4)
    assert project(Pi).applyfunc(s.simplify) == s.zeros(4)
    image = s.Matrix([result[i, j] for i in range(4) for j in range(i, 4)]).jacobian(ss)
    assert image.rank() == d['conserved_projector_rank'] == 5
    groups += 7
    for dep in d['dependencies']:
        assert hashlib.sha256((ROOT / dep['path']).read_bytes()).hexdigest() == dep['sha256']
    assert d['signed_source_class'] and d['zero_killing_charges']
    assert not any(d[key] for key in ['GU_adapter', 'positive_matter_realization', 'constant_vacuum_in_retarded_domain', 'nonlinear_integrability', 'retarded_projector_action_derived'])
    return groups


if __name__ == '__main__':
    data = json.loads((ROOT / 'lab/process/k1863-conserved-screening-causality.json').read_text())
    print('K1863 exact tensor identity groups PASS:', verify(data))
