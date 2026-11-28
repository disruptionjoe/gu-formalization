#!/usr/bin/env python3
"""Exact native local-current controls.

Standard-library/Fractions only. This script imports sparse Cl14 operations
from the declared repository dependency, never its run() function. Finite
controls support written universal proofs; no physical current is selected.
"""
import argparse
import hashlib
import importlib.util
import json
import time
from fractions import Fraction as F
from pathlib import Path


def product(a, b):
    cols = list(zip(*b))
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in cols] for row in a]


def transpose(a):
    return [list(col) for col in zip(*a)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def subtract(a, b):
    return [[x-y for x, y in zip(row, other)]
            for row, other in zip(a, b)]


def scalar_matrix(a, s):
    return [[s*x for x in row] for row in a]


def coefficient(k, p, sigma, c):
    m = [[F(0) for _ in range(15)] for _ in range(15)]
    for a in range(14):
        for b in range(14):
            if len({a, b, k}) == 3:
                m[a][b] = F(1)
    m[k][14] = F(1)
    m[14][k] = F(sigma)/p
    m[14][14] = c/p
    return m


def time_inverse(p, sigma, c):
    inv = [[F(0) for _ in range(15)] for _ in range(15)]
    inv[0][14] = p/F(sigma)
    inv[0][0] = -c/F(sigma)
    for i in range(1, 14):
        for j in range(1, 14):
            inv[i][j] = F(1, 12)-F(i == j)
    inv[14][0] = F(1)
    return inv


def normalizer(k, ratio):
    if k == 0:
        return eye(15)
    ell = [F(0)] + [F(-1)]*13 + [F(1)]
    ell[k] = F(0)
    n = eye(15)
    n[0] = [ratio*x for x in ell]
    n[0][k] += 1
    n[k] = [-F(11, 12)*x for x in ell]
    n[k][0] += 1
    for i in range(1, 14):
        if i != k:
            n[i] = [x+F(1, 12)*y for x, y in zip(n[i], ell)]
    n[14] = [F(0)] + [F(1)]*13 + [F(0)]
    n[14][k] = F(0)
    return n


def run(root):
    dep_path = root/'tests/program-focus/local_complement_probe.py'
    spec = importlib.util.spec_from_file_location('owned_local_complement', dep_path)
    dependency = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dependency)
    add, scale, mul = dependency.add, dependency.scale, dependency.mul
    checks, cases = {}, []
    normalized_blocks = 0

    def ok(name, condition):
        if name in checks:
            raise AssertionError('duplicate check name: '+name)
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    I = {0: F(1)}
    omega = {(1 << 14)-1: F(1)}
    gamma = [{1 << i: F(1)} for i in range(14)]
    ports = [
        ('K77', -1, [1, -1, -1, -1]+[1]*6+[-1]*4),
        ('K95', 1, [-1, 1, 1, 1]+[1]*6+[-1]*4),
    ]
    weights = [(F(1), F(1)), (F(2), F(3)),
               (F(1), F(-2)), (F(3, 2), F(5, 4))]
    for port, sigma, eta in ports:
        mm = lambda a, b: mul(a, b, eta)
        ok(port+' native Clifford signs', all(
            mm(gamma[i], gamma[i]) == scale(I, eta[i]) for i in range(14)))
        ok(port+' volume square', mm(omega, omega) == I)
        extra_time = next(k for k in range(4, 14) if eta[k] == eta[0])
        ordinary_space = 1
        ok(port+' same-sign normal exists', eta[extra_time] == eta[0])
        ok(port+' observed spatial sign opposite', eta[ordinary_space] == -eta[0])
        for case_index, (wp, wm) in enumerate(weights):
            prefix = f'{port}/weight{case_index}'
            p = wp*wm
            W = add(scale(I, (wp+wm)/2), scale(omega, (wp-wm)/2))
            Ws = add(scale(I, (wp+wm)/2), scale(omega, (wm-wp)/2))
            ok(prefix+' chiral inverse', mm(W, Ws) == scale(I, p))
            # Completed triple channel: c/sigma=-11/12 in each port.
            c = -F(11, 12)*sigma
            SE = scale(W, c/p)
            R = [scale(gamma[a], eta[a]) for a in range(14)]+[Ws]
            Ri = gamma+[scale(W, 1/p)]
            ok(prefix+' slotwise transport inverse', all(
                mm(R[a], Ri[a]) == I and mm(Ri[a], R[a]) == I
                for a in range(15)))

            def raw(k, a, b):
                if a < 14 and b < 14 and len({a, b, k}) == 3:
                    return scale(mm(mm(mm(gamma[a], gamma[k]), gamma[b]), W), eta[a])
                if a == k and b == 14:
                    return I
                if a == 14 and b == k:
                    return scale(I, sigma*eta[k])
                if a == 14 and b == 14:
                    return mm(gamma[k], SE)
                return {}

            m0 = coefficient(0, p, sigma, c)
            inv = time_inverse(p, sigma, c)
            ok(prefix+' full15 time inverse', product(m0, inv) == eye(15)
               and product(inv, m0) == eye(15))
            for k in range(14):
                mk = coefficient(k, p, sigma, c)
                Gk = mm(gamma[k], Ws)
                match = True
                for a in range(15):
                    for b in range(15):
                        match &= mm(mm(Ri[a], raw(k, a, b)), R[b]) == scale(Gk, mk[a][b])
                        normalized_blocks += 1
                ok(prefix+f' raw all-slot normalization/{k}', match)
                nk = normalizer(k, c/F(sigma))
                ok(prefix+f' M0N=Mk/{k}', product(m0, nk) == mk)
                ok(prefix+f' completed N square/{k}', product(nk, nk) == eye(15))
                # G0^-1 Gk cancels the reciprocal chiral weights exactly.
                G0inv = mm(scale(W, 1/p), scale(gamma[0], eta[0]))
                alpha = mm(scale(gamma[0], eta[0]), gamma[k])
                ok(prefix+f' normalized Clifford factor/{k}', mm(G0inv, Gk) == alpha)
                expected = F(1) if k == 0 else F(-eta[0]*eta[k])
                ok(prefix+f' alpha square/{k}', mm(alpha, alpha) == scale(I, expected))

            # A native visible rankS RS block, not an arbitrary Dirac copy.
            V = [{} for _ in range(15)]
            V[1] = I
            V[2] = scale(mm(gamma[2], gamma[1]), -eta[2])
            trace = {}
            for a in range(14):
                trace = add(trace, mm(gamma[a], V[a]))
            ok(prefix+' RS gamma trace zero', trace == {})
            ok(prefix+' RS observation injective first slot', V[1] == I)
            ok(prefix+' RS tau eta contractions zero', V[0] == {} and V[extra_time] == {} and V[14] == {})
            for k in (0, extra_time):
                image = []
                for a in range(15):
                    val = {}
                    for b in (1, 2):
                        val = add(val, mm(raw(k, a, b), V[b]))
                    image.append(val)
                Tk = mm(gamma[k], W)
                ok(prefix+f' native RS closure/{k}', image == [mm(v, Tk) for v in V])
            cases.append({'port': port, 'weight_plus': str(wp), 'weight_minus': str(wm),
                          'completed_c': str(c), 'extra_time_slot': extra_time,
                          'all_derivative_slots': 14})

        # Uncompleted members: exact defect instead of a diagonalization claim.
        for ratio in (F(0), F(1), -F(11, 12)):
            p = F(6)
            c = sigma*ratio
            m0 = coefficient(0, p, sigma, c)
            for k in range(1, 14):
                nk = normalizer(k, ratio)
                defect = subtract(product(nk, nk), eye(15))
                ell = [F(0)]+[F(-1)]*13+[F(1)]
                ell[k] = F(0)
                predicted = [[F(0) for _ in range(15)] for _ in range(15)]
                predicted[0] = [-(ratio+F(11, 12))*x for x in ell]
                predicted[k] = [(ratio+F(11, 12))*x for x in ell]
                label = f'{port}/ratio{ratio}/direction{k}'
                ok(label+' coefficient identity', product(m0, nk) == coefficient(k, p, sigma, c))
                ok(label+' exact Jordan defect', defect == predicted)
                ok(label+' square-zero defect', product(defect, defect) == scalar_matrix(eye(15), 0))
                ok(label+' defect nonzero iff incomplete', any(any(row) for row in defect) == (ratio != -F(11, 12)))

    # Affine r=sigma/p identity at r=0,1. The zero case is intentionally
    # singular; it verifies the polynomial identity, never time inversion.
    for ratio in (F(0), -F(11, 12)):
        for affine_r in (F(0), F(1)):
            def affine_coefficient(k):
                m = coefficient(k, F(1), 1, ratio)
                m[14] = [affine_r*x for x in m[14]]
                return m
            m0 = affine_coefficient(0)
            for k in range(14):
                ok(f'affine r{affine_r} ratio{ratio} direction{k}',
                   product(m0, normalizer(k, ratio)) == affine_coefficient(k))
            if affine_r == 0:
                ok(f'affine zero singular row ratio{ratio}', not any(m0[14]))

    # Current core: real matrices are a subcase of the Hermitian identities.
    J = [[F(0), F(1)], [F(-1), F(0)]]
    I2 = eye(2)
    ok('extra-time anti-involution', product(J, J) == scalar_matrix(I2, -1))
    ok('positive identity fails extra-time symmetrization', product(I2, J) != product(transpose(J), I2))
    for a, b in ((F(0), F(0)), (F(1), F(0)), (F(0), F(2)), (F(3, 2), F(-2, 3))):
        H = [[a, b], [b, -a]]
        label = f'current a{a} b{b}'
        ok(label+' indefinite symmetrizer control', product(H, J) == product(transpose(J), H))
        ok(label+' anti-isometry identity', product(product(transpose(J), H), J) == scalar_matrix(H, -1))
        ok(label+' determinant nonpositive', H[0][0]*H[1][1]-H[0][1]*H[1][0] == -a*a-b*b)
    D = [[F(1), F(0)], [F(0), F(-1)]]
    ok('ordinary one-time Dirac positive control', product(I2, D) == product(transpose(D), I2) and product(D, D) == I2)
    for k, ell in ((F(5), F(3)), (F(2), F(-1)), (F(3), F(5)), (F(1), F(1))):
        A = [[k, ell], [-ell, -k]]
        H = [[F(1), ell/k], [ell/k, F(1)]]
        label = f'nonlocal cone k{k} ell{ell}'
        ok(label+' dispersion', product(A, A) == scalar_matrix(I2, k*k-ell*ell))
        ok(label+' frequency-dependent symmetrizer', product(H, A) == product(transpose(A), H))
        determinant = F(1)-(ell/k)**2
        ok(label+' positive exactly inside cone', (determinant > 0) == (abs(ell) < abs(k)))
        if abs(k) == abs(ell):
            ok(label+' threshold singularity', determinant == 0 and product(A, A) == scalar_matrix(I2, 0) and A != scalar_matrix(I2, 0))

    dependencies = [
        'tests/program-focus/local_complement_probe.py',
        'explorations/conditional-build/source-natural-symbol-class-2026-11-24.md',
        'explorations/conditional-build/bet-2plus1-chiral-weight-transport-2026-11-25.md',
        'lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md',
        'explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md',
        'explorations/conditional-build/source-action-wave2-construction-2026-11-25.md',
        'explorations/conditional-build/bet-mass-gap-reference-holonomy-2026-11-27.md',
        'explorations/conditional-build/k2203-observed-lower-pairing-compatibility-2026-10-28.md',
    ]
    return {'status': 'PASS', 'grouped_checks': len(checks), 'checks': checks,
            'full_Cl14_normalized_blocks': normalized_blocks, 'cases': cases,
            'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependency_sha256': {p: hashlib.sha256((root/p).read_bytes()).hexdigest() for p in dependencies},
            'scope': 'Exact finite native controls. Written/reviewed proofs own universal parameter coverage, local-current jet necessity, positive-semidefinite quotient reasoning and source/domain scope. No physical current or norm is selected.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo-root', type=Path,
                        default=Path(__file__).resolve().parents[2])
    parser.add_argument('--verify', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    result = run(args.repo_root.resolve())
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    if args.verify:
        expected = json.loads((args.repo_root/'lab/process/local-current-certificates.json').read_text())
        assert result == expected, 'certificate mismatch'
    print(json.dumps({**{k: v for k, v in result.items()
                      if k not in ('checks', 'dependency_sha256', 'cases')},
                      'runtime_seconds': time.perf_counter()-started}, indent=2))
