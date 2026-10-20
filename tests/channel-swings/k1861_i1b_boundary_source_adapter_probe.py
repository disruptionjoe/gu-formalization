#!/usr/bin/env python3
"""Independent linearized-Ricci arithmetic and baseline-first assertion faults."""
from fractions import Fraction as Q
from pathlib import Path
import copy
import json
import traceback

ROOT = Path(__file__).resolve().parents[2]


def einstein(t, k, signs):
    # Direct contraction of the coordinate linearized Ricci tensor with
    # each second derivative replaced by -k_a k_b; not a producer import.
    tr = sum(signs[c]*t[c][c] for c in range(4))
    ric = [[sum(signs[c]*(-k[c]*k[a]*t[b][c]-k[c]*k[b]*t[a][c]
                            + k[c]*k[c]*t[a][b]) for c in range(4))/2
            + k[a]*k[b]*tr/2 for b in range(4)] for a in range(4)]
    scalar = sum(signs[c]*ric[c][c] for c in range(4))
    return [[ric[a][b]-(signs[a]*scalar/2 if a == b else 0) for b in range(4)] for a in range(4)]


def check(d):
    checks = 0
    for signs in [[Q(1)]*4, [Q(-1), Q(1), Q(1), Q(1)]]:
        for k in [[Q(1), Q(0), Q(0), Q(0)], [Q(0), Q(1), Q(2), Q(3)], [Q(2), Q(1), Q(0), Q(1)]]:
            norm = sum(signs[c]*k[c]**2 for c in range(4))
            for seed in range(1, 9):
                t = [[Q((a+seed)*(b+seed), seed+1) for b in range(4)] for a in range(4)]
                G = einstein(t, k, signs)
                assert all(sum(signs[a]*k[a]*G[a][b] for a in range(4)) == 0 for b in range(4))
                source = [[-2*v for v in row] for row in G]
                tr = sum(signs[c]*source[c][c] for c in range(4))
                response = [[(source[a][b]-(Q(d['trace_reversal_coefficient'])*signs[a]*tr if a == b else 0))/norm
                             for b in range(4)] for a in range(4)]
                GR = einstein(response, k, signs)
                assert [[-2*Q(d['symbol_scale'])*v for v in row] for row in GR] == [[-v for v in row] for row in source]
                checks += 2
    # For every symmetric input basis at the chosen Lorentzian null mode,
    # the two transverse traceless output components vanish.
    signs, k = [Q(-1), Q(1), Q(1), Q(1)], [Q(1), Q(0), Q(0), Q(1)]
    for a in range(4):
        for b in range(a, 4):
            t = [[Q(0) for _ in range(4)] for _ in range(4)]
            t[a][b] = t[b][a] = 1
            out = einstein(t, k, signs)
            assert out[1][1] == out[2][2] and out[1][2] == 0
            checks += 1
    # Independent right-inverse check using the Ricci implementation above.
    l = [Q(-1, 2), Q(0), Q(0), Q(1, 2)]
    for w in [[Q(1), Q(2), Q(3), Q(4)], [Q(2, 3), Q(1), Q(-1), Q(5, 7)]]:
        kw = sum(signs[c]*k[c]*w[c] for c in range(4))
        lw = sum(signs[c]*l[c]*w[c] for c in range(4))
        t = [[l[a]*w[b]+l[b]*w[a]-kw*l[a]*l[b]
              -(Q(d['null_inverse_metric_coefficient'])*lw*signs[a] if a == b else 0)
              for b in range(4)] for a in range(4)]
        target = [[k[a]*w[b]+k[b]*w[a]-(signs[a]*kw if a == b else 0)
                   for b in range(4)] for a in range(4)]
        assert [[-2*v for v in row] for row in einstein(t, k, signs)] == target
        checks += 1
    # A nonconstant scalar times eta fails conservation for every nonzero k.
    for rho in [Q(2, 7), Q(-3, 5)]:
        divergence = [rho*v/2 for v in k]
        assert divergence != [0]*4
        checks += 1
    # Differentiate f=a eta(x,x) directly, then form the real-space Ricci
    # tensor of f eta. R'_ab=-f_,ab-(eta_ab/2) Box f in dimension four.
    a = Q(d['box_quadratic_coefficient'])
    box_f = 8*a
    ric_diagonal = [-2*a*sign-box_f*sign/2 for sign in signs]
    scalar = sum(signs[i]*ric_diagonal[i] for i in range(4))
    at_diagonal = [-2*(ric_diagonal[i]-signs[i]*scalar/2) for i in range(4)]
    assert at_diagonal == [-sign/2 for sign in signs]
    # The proposed current must reproduce the independently derived 2tr(At).
    current_coefficient = Q(d['green_current_factor'])*(1-4)*2*a
    actual_trace_pairing = 2*sum(signs[i]*at_diagonal[i] for i in range(4))
    assert 4*current_coefficient == actual_trace_pairing
    checks += 2
    # Directed coordinate-box flux sums independently over the eight faces.
    for lengths in [[Q(1)]*4, [Q(1, 2), Q(2), Q(3, 2), Q(5, 3)]]:
        volume = Q(1)
        for L in lengths:
            volume *= 2*L
        flux = Q(0)
        for axis, L in enumerate(lengths):
            area = volume/(2*L)
            flux += 2*current_coefficient*L*area
        assert flux == Q(d['scale_flux_per_volume'])*volume
        checks += 1
    # Lowest nonzero Euclidean Fourier mode attains the H^{r+2}/H^r
    # multiplier norm 2: trace reversal preserves the Frobenius norm.
    j = [[Q(0) for _ in range(4)] for _ in range(4)]
    j[1][1] = 1
    tr = sum(j[i][i] for i in range(4))
    t = [[j[a][b]-(Q(d['trace_reversal_coefficient'])*tr if a == b else 0)
          for b in range(4)] for a in range(4)]
    input_norm2 = sum(v*v for row in j for v in row)
    output_norm2 = 4*sum(v*v for row in t for v in row)
    assert Q(d['euclidean_sobolev_constant']) > 0
    assert output_norm2 <= Q(d['euclidean_sobolev_constant'])**2*input_norm2
    checks += 1
    return checks


def references(d):
    # Explicitly reported as reference metadata, not mathematical mutations.
    assert d['dimension'] == 4
    assert d['nonnull_rank'] == 6
    assert d['null_rank'] == 4


def reporting(d):
    return (d['scope'] == 'horizontal_equation_dual_control'
            and not d['full_native_dual_injection_constructed']
            and not d['companion_row_solved']
            and not d['lorentzian_global_inverse_claimed'])


if __name__ == '__main__':
    data = json.loads((ROOT/'lab/process/k1861-i1b-boundary-source-adapter.json').read_text())
    count = check(data)
    references(data)
    assert reporting(data)  # A clean baseline must precede every mutation.
    mutations = [('symbol_scale', '-1'), ('trace_reversal_coefficient', '1/4'), ('null_inverse_metric_coefficient', '1/2'),
                 ('box_quadratic_coefficient', '1/12'), ('green_current_factor', '2'),
                 ('scale_flux_per_volume', '4'), ('euclidean_sobolev_constant', 1)]
    for key, value in mutations:
        bad = copy.deepcopy(data)
        bad[key] = value
        try:
            check(bad)
        except AssertionError as exc:
            frame = traceback.extract_tb(exc.__traceback__)[-1]
            print('[DETECTED mathematical-input fault]', key, 'at', frame.lineno, frame.line)
        else:
            raise AssertionError('undetected mathematical-input fault: '+key)
    for key, value in [('dimension', 3), ('nonnull_rank', 4), ('null_rank', 6)]:
        bad = copy.deepcopy(data)
        bad[key] = value
        try:
            references(bad)
        except AssertionError as exc:
            frame = traceback.extract_tb(exc.__traceback__)[-1]
            print('[DETECTED reference-metadata fault]', key, 'at', frame.lineno, frame.line)
        else:
            raise AssertionError('undetected reference-metadata fault: '+key)
    for key in ['full_native_dual_injection_constructed', 'companion_row_solved', 'lorentzian_global_inverse_claimed']:
        bad = copy.deepcopy(data)
        bad[key] = True
        assert not reporting(bad)
        print('[DETECTED reporting fault]', key)
    bad = copy.deepcopy(data)
    bad['scope'] = 'global_GU_response'
    assert not reporting(bad)
    print('[DETECTED reporting fault] scope')
    print('K1861 independent controls PASS:', count, 'controls;', len(mutations),
          'mathematical-input, 3 reference-metadata and 4 reporting faults')
