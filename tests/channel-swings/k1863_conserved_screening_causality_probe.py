#!/usr/bin/env python3
"""Independent rational jets/tensors and baseline-first assertion fault controls."""
from fractions import Fraction as F
from pathlib import Path
import copy
import itertools
import json
import traceback

ROOT = Path(__file__).resolve().parents[2]


def deriv(poly, axis):
    out = {}
    for power, coeff in poly.items():
        if power[axis]:
            new = list(power)
            new[axis] -= 1
            new = tuple(new)
            out[new] = out.get(new, F(0)) + power[axis] * coeff
    return {p: c for p, c in out.items() if c}


def combine(*terms):
    out = {}
    for factor, poly in terms:
        for p, c in poly.items():
            out[p] = out.get(p, F(0)) + factor * c
    return {p: c for p, c in out.items() if c}


def controls(d):
    # Finite polynomial jets test local derivative algebra, not compact support.
    chi = {(2, 2, 0, 0): F(3, 5), (3, 1, 1, 0): F(-2, 7), (4, 0, 1, 1): F(5, 3), (2, 0, 0, 3): F(11, 13)}
    S = [[F(2), F(-1, 3), F(1, 7)], [F(-1, 3), F(-3), F(2, 5)], [F(1, 7), F(2, 5), F(4)]]
    T = [[{} for _ in range(4)] for _ in range(4)]
    T[0][0] = combine(*[(S[i][j], deriv(deriv(chi, i+1), j+1)) for i in range(3) for j in range(3)])
    for i in range(3):
        T[0][i+1] = T[i+1][0] = combine(*[(F(d['stress_cross_factor'])*S[i][j], deriv(deriv(chi, 0), j+1)) for j in range(3)])
        for j in range(3):
            T[i+1][j+1] = combine((F(d['stress_spatial_factor'])*S[i][j], deriv(deriv(chi, 0), 0)))
    for nu in range(4):
        assert not combine((-1, deriv(T[0][nu], 0)), *[(1, deriv(T[i][nu], i)) for i in range(1, 4)])
    count = 4
    # Differentiate the retarded homogeneous metric twice via independent ODE data.
    for aa, bb, cc, dd in itertools.product([-1, 0, 2], repeat=4):
        A = [[F(aa), F(dd, 3), F(1, 7)], [F(dd, 3), F(bb), F(-2, 5)], [F(1, 7), F(-2, 5), F(cc)]]
        tr = sum(A[i][i] for i in range(3)); k = F(7, 11)
        hb2 = [[-F(d['wave_factor'])*k*A[i][j] for j in range(3)] for i in range(3)]
        hbtr = sum(hb2[i][i] for i in range(3))
        h2 = [[hb2[i][j] - (F(d['trace_reverse_factor'])*hbtr if i == j else 0) for j in range(3)] for i in range(3)]
        E = [[-h2[i][j]/2 for j in range(3)] for i in range(3)]
        Ric00 = sum(E[i][i] for i in range(3)); scalar = -2*Ric00
        assert scalar == F(d['scalar_factor'])*k*tr
        for i in range(3):
            for j in range(3):
                delta = int(i == j)
                assert E[i][j] == k*(A[i][j]-F(d['tidal_trace_factor'])*delta*tr)
                assert -E[i][j]-delta*scalar/2 == -k*A[i][j]
                assert F(d['inverse_factor'])*(E[i][j]-delta*Ric00)/k == A[i][j]
                Weyl = E[i][j]/2-delta*Ric00/2-delta*scalar/6
                assert Weyl == F(d['weyl_factor'])*k*(A[i][j]-delta*tr/3)
        count += 1
    # Independent timelike Fourier-symbol projector with six spatial input slots.
    for p0, p1 in [(F(3), F(1)), (F(5), F(2)), (F(7, 2), F(-1, 3))]:
        p = [p0, p1, F(0), F(0)]; eta = [-1, 1, 1, 1]
        p2 = -p0*p0+p1*p1
        Pi = [[F(eta[i] if i == j else 0)-F(d['transverse_factor'])*p[i]*p[j]/p2 for j in range(4)] for i in range(4)]
        assert all(sum(eta[i]*p[i]*Pi[i][j] for i in range(4)) == 0 for j in range(4))
        assert sum(eta[i]*Pi[i][i] for i in range(4)) == 3
        def project(B):
            trb = sum(eta[i]*B[i][i] for i in range(4))
            return [[B[i][j]-F(d['trace_projector_factor'])*Pi[i][j]*trb for j in range(4)] for i in range(4)]
        B = [[F(0) for _ in range(4)] for _ in range(4)]
        for i in range(3):
            for j in range(3): B[i+1][j+1] = S[i][j]
            B[0][i+1] = B[i+1][0] = (p1/p0)*S[0][i]
        B[0][0] = (p1/p0)**2*S[0][0]
        C = project(B)
        assert sum(eta[i]*C[i][i] for i in range(4)) == 0
        assert all(sum(eta[i]*p[i]*C[i][j] for i in range(4)) == 0 for j in range(4))
        assert project(C) == C
        assert project(Pi) == [[F(0)]*4 for _ in range(4)]
        count += 1
    return count


def reporting(d):
    return d['signed_source_class'] and d['zero_killing_charges'] and not any(d[key] for key in ['GU_adapter', 'positive_matter_realization', 'constant_vacuum_in_retarded_domain', 'nonlinear_integrability', 'retarded_projector_action_derived'])


if __name__ == '__main__':
    data = json.loads((ROOT / 'lab/process/k1863-conserved-screening-causality.json').read_text())
    n = controls(data)
    faults = [('stress_cross_factor', '-1'), ('stress_spatial_factor', '2'), ('wave_factor', '1'), ('trace_reverse_factor', '1/3'), ('tidal_trace_factor', '1/3'), ('inverse_factor', '2'), ('scalar_factor', '-1'), ('weyl_factor', '1'), ('transverse_factor', '-1'), ('trace_projector_factor', '1/4')]
    for key, value in faults:
        mutant = copy.deepcopy(data); mutant[key] = value
        try:
            controls(mutant)
        except AssertionError as exc:
            frame = traceback.extract_tb(exc.__traceback__)[-1]
            print('[DETECTED mathematical input fault]', key, 'line', frame.lineno, frame.line)
        else:
            raise AssertionError('Undetected mathematical input fault: '+key)
    assert reporting(data)
    flags = ['signed_source_class', 'zero_killing_charges', 'GU_adapter', 'positive_matter_realization', 'constant_vacuum_in_retarded_domain', 'nonlinear_integrability', 'retarded_projector_action_derived']
    for key in flags:
        mutant = copy.deepcopy(data); mutant[key] = not mutant[key]
        assert not reporting(mutant)
    print('K1863 independent controls PASS:', n, 'groups;', len(faults), 'mathematical input faults and', len(flags), 'separate reporting faults detected')
