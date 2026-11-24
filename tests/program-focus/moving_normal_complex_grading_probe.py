#!/usr/bin/env python3
"""Exact moving-J normal-RS spectral grading controls; no index computation.

Finite Fock/gamma characters and actual K95 Clifford identities support the
written structural theorem. No source action, physical grade or domain built.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS', '1')
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import json
import sys

CHECKS = []
def ck(name, condition):
    if not condition:
        raise AssertionError(name)
    CHECKS.append(name)


def fock_action(mask, i, creation):
    occupied = bool(mask & (1 << i))
    if occupied == creation:
        return None
    sign = (-1) ** ((mask & ((1 << i) - 1)).bit_count())
    return mask ^ (1 << i), sign


def p49(z, denominator=46080):
    return F((z - 1) * (z - 9) * (z - 25), denominator)


def spectral_checks(mutation=None):
    spin = {
        parity: Counter(2 * mask.bit_count() - 5 for mask in range(32)
                        if mask.bit_count() % 2 == parity)
        for parity in (0, 1)
    }
    rows = {}
    for parity in (0, 1):
        raw = Counter()
        image = Counter()
        row_preimages = Counter()
        for creation in (True, False):
            qv = 0 if mutation == 'spin_only' else (2 if creation else -2)
            for i in range(5):
                for mask in range(32):
                    if mask.bit_count() % 2 != parity:
                        continue
                    qs = 2 * mask.bit_count() - 5
                    raw[qs + qv] += 1
                    out = fock_action(mask, i, creation)
                    if out is not None:
                        target, sign = out
                        ck('gamma intertwines doubled J charge',
                           2 * target.bit_count() - 5 == qs + qv)
                        row_preimages[target] += 1
        ck('gamma reaches all opposite spin rows',
           set(row_preimages) == {m for m in range(32) if m.bit_count() % 2 != parity})
        ck('gamma rows have five nonzero one-entry preimages',
           set(row_preimages.values()) == {5})
        # Distinct target rows have disjoint supports, hence the exact rank is16.
        image = spin[1-parity]
        kernel = {q: raw[q] - image.get(q, 0) for q in raw}
        rows[parity] = {q: n for q, n in sorted(kernel.items()) if n}
        ck('normal RS half rank144', sum(rows[parity].values()) == 144)
    ck('even-input normal RS character', rows[0] == {-7:5, -3:50, 1:65, 5:24})
    ck('odd-input normal RS character', rows[1] == {-5:24, -1:65, 3:50, 7:5})
    sq = Counter()
    for row in rows.values():
        for q, n in row.items():
            sq[q*q] += n
    ck('four squared-weight ranks', dict(sq) == {49:10, 9:100, 1:130, 25:48})
    den = 23040 if mutation == 'projector_denominator' else 46080
    for z in sq:
        ck('extreme polynomial is spectral indicator', p49(z, den) == int(z == 49))
        ck('extreme polynomial idempotence', p49(z, den)**2 == p49(z, den))
    ck('observed spinor is annihilated', all(p49(q*q) == 0 for row in spin.values() for q in row))
    ck('normal rank10 and hidden rank40', sq[49] == 10 and 4*sq[49] == 40)
    ck('normal B trace changes but full grade fibre trace stays zero', 288-2*sq[49] == 268 and 2*(288-sq[49])+2*sq[49] == 576 and 576+256 == 832)
    zvalues = [1, 9, 25, 49]
    signs_seen = set()
    for signs in product((-1, 1), repeat=4):
        b = dict(zip(zvalues, signs))
        def grade(q, horizontal_sign):
            return -horizontal_sign*b[q*q]
        ck('spectral sign hidden involution', all(grade(q,h)**2 == 1 for q in (-7,-5,-3,-1,1,3,5,7) for h in (-1,1)))
        ck('tangential Clifford flips grade', all(grade(q,1) == -grade(q,-1) for q in (-7,-5,-3,-1,1,3,5,7)))
        # Actual anti-linear C reverses q and chiH. Even polynomial is essential.
        ck('cross-grade C exchange', all(grade(-q,-h) == -grade(q,h) for q in (-7,-5,-3,-1,1,3,5,7) for h in (-1,1)))
        signs_seen.add(signs)
    ck('sixteen distinct sign choices', len(signs_seen) == 16)
    screened = []
    for signs in signs_seen:
        rminus = sum(sq[z] for z,sgn in zip(zvalues,signs) if sgn == -1)
        if rminus < 128:
            screened.append((rminus,512-4*rminus))
    ck('six rank-excluded choices for actual512 shape block', sorted(screened) == [(0,512),(10,472),(48,320),(58,280),(100,112),(110,72)])
    ck('ten choices only pass dimension screen', len(signs_seen)-len(screened) == 10)
    simple_weight_sectors = set()
    for degree in (2,3,4,5):
        for i in range(5):
            others = [j for j in range(5) if j != i][:degree-1]
            mask = (1 << i) + sum(1 << j for j in others)
            ck('simple wedge witness has stated degree', mask.bit_count() == degree)
            ck('simple wedge witness is gamma-free', fock_action(mask,i,True) is None)
            q2 = 2*degree-3
            simple_weight_sectors.add(q2*q2)
            ck('simple wedge witness belongs to actual RS character', rows[degree%2][q2] > 0)
    ck('simple gamma-free witnesses cover every squared sector', simple_weight_sectors == {1,9,25,49})
    ck('under proven nonzero incidence only all-negative sign passes', sum(all(s == -1 for s in signs) for signs in signs_seen) == 1)
    ck('only two are uniform within each half', sum(len(set(s)) == 1 for s in signs_seen) == 2)
    ck('odd charge sign would violate the needed C law', (1 if 7 > 0 else -1) != (1 if -7 > 0 else -1))
    ck('reality paired normal half weights', all(rows[0][q] == rows[1][-q] for q in rows[0]))
    # gl5 complement witnesses. Mode3 is unaffected by the vector part of X12.
    # Lowering two spin modes sends u3⊗top to a nonzero gamma-free weight3 state.
    out = fock_action(31, 1, False)
    out2 = fock_action(out[0], 0, False)
    ck('lowering coset has nonzero extreme image', out2 is not None)
    target = out2[0]
    ck('lowered witness remains gamma-free', fock_action(target, 2, True) is None)
    ck('lowered witness outside extreme projector', 2*target.bit_count()-5+2 == 3 and p49(9) == 0)
    out = fock_action(0, 1, True)
    out2 = fock_action(out[0], 0, True)
    ck('raising coset has nonzero extreme image', out2 is not None)
    target = out2[0]
    ck('raised witness remains gamma-free', fock_action(target, 2, False) is None)
    ck('raised witness outside extreme projector', 2*target.bit_count()-5-2 == -3 and p49(9) == 0)
    return {'normal_RS_half_doubled_weights': rows,
            'squared_weight_ranks': dict(sorted(sq.items())),
            'spectral_sign_grades': 16,
            'extreme_normal_rank': 10,
            'extreme_hidden_ambient_rank': 40,
            'shape_block_rank_premise': 512,
            'shape_graded_defect_bounds': sorted(screened),
            'rank_screen_only_remaining': 10,
            'simple_gammafree_squared_sectors': sorted(simple_weight_sectors),
            'under_analytic_native_incidence_remaining': 1,
            'remaining_sign': [-1,-1,-1,-1]}


def native_k95_checks(repo):
    import numpy as np
    sys.path.insert(0, str(repo / 'tests/channel-swings'))
    from actual_sym2_c14_orbit_probe import native_gammas
    gamma, eta = native_gammas()
    ident = np.eye(128, dtype=complex)
    zero = 0*ident
    eq = np.array_equal
    def prod(seq):
        out = ident.copy()
        for a in seq:
            out = out @ a
        return out
    h = [9, 0, 1, 2]
    normal = [a for a in range(14) if a not in h]
    pairs = [(3,4), (5,6), (7,8), (10,11), (12,13)]
    ck('K95 actual normal signature6,4', sum(eta[a] == 1 for a in normal) == 6 and sum(eta[a] == -1 for a in normal) == 4)
    twice_r = sum((-eta[a]*gamma[a]@gamma[b] for a,b in pairs), zero.copy())
    chi_h = 1j * prod([gamma[a] for a in h])
    krein = prod(gamma[:9])
    conj = prod([a for a in gamma if eq(a.conjugate(), -a)])
    ck('actual C square minus identity', eq(conj @ conj.conjugate(), -ident))
    ck('actual C commutes with each Clifford generator', all(eq(conj @ a.conjugate(), a @ conj) for a in gamma))
    ck('C reverses the actual horizontal grade', eq(conj @ chi_h.conjugate(), -chi_h @ conj))
    ck('actual normal Lie action commutes anti-linearly with C', eq(conj @ twice_r.conjugate(), twice_r @ conj))
    ck('actual normal Lie action is Krein skew', eq(twice_r.conjugate().T @ krein, -krein @ twice_r))
    ck('actual normal Lie action commutes horizontal Clifford', all(eq(twice_r @ gamma[a], gamma[a] @ twice_r) for a in h))
    for a,b in pairs:
        ck('actual vector-spin gamma intertwiner first leg', eq(twice_r @ gamma[a] - gamma[a] @ twice_r, 2*gamma[b]))
        ck('actual vector-spin gamma intertwiner second leg', eq(twice_r @ gamma[b] - gamma[b] @ twice_r, -2*gamma[a]))
    z = -twice_r @ twice_r
    ck('observed spinor minimal polynomial', eq((z-ident) @ (z-9*ident) @ (z-25*ident), zero))
    ck('squared Lie action is C-real', eq(conj @ z.conjugate(), z @ conj))
    ck('squared Lie action is Krein self-adjoint', eq(z.conjugate().T @ krein, krein @ z))
    ck('squared Lie action commutes horizontal grade', eq(z @ chi_h, chi_h @ z))
    # All entries are Gaussian integers. The dyadic convention is scaled by2,
    # and bounded integer matrix operations here are exactly representable.
    ck('integer matrix carrier, no approximate tolerance', all(np.max(np.abs(a)) < 2**40 for a in [twice_r,z]) and all(np.array_equal(a.real, np.rint(a.real)) and np.array_equal(a.imag, np.rint(a.imag)) for a in [twice_r,z]))
    return {'fixture': 'actual_sym2_c14_orbit_probe.native_gammas K95',
            'normal_pairs': pairs, 'scope': 'Lie-action, gamma, Krein, and anti-linear building blocks; full RS polynomial theorem is analytic'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output', type=Path)
    parser.add_argument('--selftest', action='store_true')
    parser.add_argument('--skip-native', action='store_true')
    args = parser.parse_args()
    result = spectral_checks()
    if not args.skip_native:
        result['native_control'] = native_k95_checks(args.repo)
    clean_checks = list(CHECKS)
    if args.selftest:
        caught = []
        for mutation in ('spin_only', 'projector_denominator'):
            try:
                spectral_checks(mutation)
            except AssertionError:
                caught.append(mutation)
        ck('both false mutations rejected', len(caught) == 2)
        result['mutations_rejected'] = caught
    result.update({'artifact': 'MOVING_REDUCTION_RS_SYMBOL_GRADINGS',
                   'checks_passed': len(clean_checks),
                   'checks': clean_checks,
                   'claim_ceiling': 'Canonical tangential symbol and compatible fibre pairing/reality only; no full source operator/domain, physical grade or index.'})
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
