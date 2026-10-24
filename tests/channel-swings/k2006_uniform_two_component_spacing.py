"""Exact controls for the all-d two-component spacing theorem.

The universal statements are proved in the accompanying exploration. This
small producer tests actual spectra and populations; it does not enumerate
the optimum in every dimension. Only standard-library rational arithmetic.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "lab/process/k2006-uniform-two-component-spacing.json"


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def valid(shape, support):
    return all(sum(z-a in (0, 1, 2, 3) for a in shape) >=
               2*sum(z-s in (0, 1, 2, 3) for s in support)
               for z in {s+b for s in support for b in range(4)})


def rate(t, support, p):
    """Incoming excess formula; valid supports have no triple shared shell."""
    inc = [Q(0)] * len(p)
    Z = sum(t**b for b in range(4))
    for i, j in combinations(range(len(p)), 2):
        if support[i] > support[j]:
            i, j = j, i
        g = support[j] - support[i]
        if g in (1, 2, 3):
            L = sum(t**b for b in range(4-int(g))) / Z
            excess = L*(t**int(g)*p[i]-p[j])
            inc[i] += max(-excess, 0)
            inc[j] += max(excess, 0)
    return sum(max(a-b, 0) for a, b in zip(p, inc))/2


def offset(A, B, delta):
    if delta <= Q(1, 2):
        return delta
    centers = {a-b for a in A for b in B}
    n = 0
    while n+1 in centers:
        n += 1
    return n+delta


def interval_oracle(A, B, delta):
    candidates = {Q(0)} | {Q(a-b)+delta for a in A for b in B}
    return min(x for x in candidates if x >= 0 and
               all(abs(Q(a-b)-x) >= delta for a in A for b in B))


def weight_optimum(energies, returns, weights):
    """Enumerate the vertices of the one-moment component-weight polytope."""
    E = dot(energies, weights)
    candidates = []
    for i, e in enumerate(energies):
        if e <= E:
            candidates.append(tuple(Q(i == j) for j in range(len(weights))))
    for i, j in combinations(range(len(weights)), 2):
        if energies[i] == energies[j]:
            continue
        x = (E-energies[j])/(energies[i]-energies[j])
        if 0 <= x <= 1:
            p = [Q(0)] * len(weights)
            p[i], p[j] = x, 1-x
            candidates.append(tuple(p))
    return min(candidates, key=lambda p: (dot(returns, p), dot(energies, p), p))


def physical(components, weights):
    kept = [(c, w) for c, w in zip(components, weights) if w]
    base = min(c['offset'] for c, w in kept)
    spectrum = sorted(c['offset']+a-base for c, w in kept for a in c['shape'])
    population = sorted((c['offset']+s-base, w*p)
                        for c, w in kept for s, p in zip(c['support'], c['population']))
    return spectrum, [s for s, p in population], [p for s, p in population]


def component_examples():
    rows = []
    for name, sizes, pairs in [
            ('d13_5_5_3', [5, 5, 3], [(Q(2, 5), Q(3, 5)), (Q(7, 10), Q(3, 10)), (Q(1),)]),
            ('d15_5_5_5', [5, 5, 5], [(Q(1, 3), Q(2, 3)), (Q(3, 5), Q(2, 5)), (Q(4, 5), Q(1, 5))]),
            ('d15_equal_means', [5, 5, 5], [(Q(1, 2), Q(1, 2)), (Q(3, 5), Q(2, 5)), (Q(7, 10), Q(3, 10))])]:
        components = [dict(shape=list(range(size)), support=[1, 3] if size == 5 else [1],
                           population=list(p), offset=Q(j, 5))
                      for j, (size, p) in enumerate(zip(sizes, pairs))]
        weights = [Q(1, 4), Q(1, 3), Q(5, 12)]
        energies = [c['offset']+dot(c['support'], c['population']) for c in components]
        for t in [Q(1, 3), Q(1, 2), Q(3, 4)]:
            returns = [rate(t, c['support'], c['population']) for c in components]
            new = weight_optimum(energies, returns, weights)
            A, S, p = physical(components, weights)
            B, T, q = physical(components, new)
            assert len(A) == sum(sizes) and valid(A, S) and valid(B, T)
            assert len(set(B)) == len(B) and min(b-a for a, b in zip(B, B[1:])) >= Q(1, 5)
            assert sum(new) == 1 and min(new) >= 0 and sum(bool(w) for w in new) <= 2
            assert dot(energies, new) <= dot(energies, weights)
            assert dot(returns, new) <= dot(returns, weights)
            assert rate(t, S, p) == dot(returns, weights)
            assert rate(t, T, q) == dot(returns, new)
            rows.append(dict(name=name, t=t, spacing=Q(1, 5), components=components,
                             old_weights=weights, new_weights=new,
                             before=dict(spectrum=A, support=S, population=p, energy=dot(S, p), return_value=rate(t, S, p)),
                             after=dict(spectrum=B, support=T, population=q, energy=dot(T, q), return_value=rate(t, T, q))))
    return rows


def geometry_controls():
    shapes = [[0]]
    for n in range(2, 5):
        for gaps in product((1, 2, 3), repeat=n-1):
            A = [0]
            for g in gaps:
                A.append(A[-1]+g)
            shapes.append(A)
    deltas = [Q(1, 10), Q(1, 2), Q(51, 100), Q(3, 4), Q(1)]
    checks = 0
    for A, B in product(shapes, repeat=2):
        for delta in deltas:
            x = offset(A, B, delta)
            assert x == interval_oracle(A, B, delta)
            assert x <= max(A)+delta
            assert max(max(A), x+max(B)) <= 3*(len(A)+len(B)-2)+delta
            checks += 3
    pairs = [(list(range(5)), list(range(3))), (list(range(3)), list(range(5))),
             ([0, 1, 4, 5, 6, 7, 8], [0, 1, 4]), ([0, 1, 4], [0, 1, 4, 5, 6, 7, 8]),
             ([0, 2], [0, 2]), ([0, 3, 6, 9], [0, 3, 6])]
    rows = []
    for A, B in pairs:
        for delta in deltas:
            x = offset(A, B, delta)
            rows.append(dict(A=A, B=B, delta=delta, offset=x,
                             spectrum=sorted([Q(a) for a in A]+[x+b for b in B]),
                             summed_dimension=len(A)+len(B)))
    return dict(shape_count=len(shapes), ordered_pairs=len(shapes)**2,
                parameter_controls=len(shapes)**2*len(deltas), exact_obligations=checks,
                rows=rows, evidence_kind='finite exact geometry controls; universal proof in exploration')


def repair_controls():
    delta = Q(1, 4)
    S = [Q(1), Q(3), 1+delta]
    p = [Q(1, 4), Q(1, 2), Q(1, 4)]
    E = dot(S, p)
    rows = []
    for h in [Q(1, 100), Q(1, 1000), Q(1, 10000)]:
        T = [Q(1), Q(3), 1+delta+h]
        ep = dot(T, p)
        theta = (ep-E)/(ep-1)
        q = [(1-theta)*v + (theta if j == 0 else 0) for j, v in enumerate(p)]
        assert 0 < theta < 1 and sum(q) == 1 and dot(T, q) == E
        norm = sum(abs(x-y) for x, y in zip(p, q))
        for t in [Q(1, 3), Q(1, 2), Q(3, 4)]:
            old = rate(t, S, p)
            new = rate(t, T, q)
            assert abs(new-old) <= 4*norm
            rows.append(dict(delta=delta, increment=h, t=t, old_support=S,
                             new_support=T, old_population=p, repaired_population=q,
                             budget=E, repair_mass=theta, old_return=old, new_return=new,
                             l1_change=norm))
    return rows


def contrary_controls():
    # Both are real protocol returns, not flags saying a theorem was checked.
    old = rate(Q(1, 2), [Q(1), Q(3), Q(10)], [Q(1, 45), Q(1, 5), Q(7, 9)])
    merged = rate(Q(1, 2), [Q(1), Q(3)], [Q(4, 5), Q(1, 5)])
    assert old == Q(22, 45) and merged == Q(1, 2) and merged > old
    # A valid pure family can disappear at a parameter threshold. Its value
    # is 1/2, and the actual pure ground-normalized baseline remains feasible.
    d0, h = Q(1, 4), Q(1, 100)
    E = 1+d0
    assert 1+d0+h > E and rate(Q(1, 2), [1+d0], [Q(1)]) == Q(1, 2)
    assert valid([0, 1, 2], [1]) and Q(1) < E
    # Resonance at delta1 changes the sharp return, although old blocks remain valid.
    # A={0,2,4}, B={0,2,4} have least x=delta even at delta1.
    before = rate(Q(1, 2), [Q(2), Q(2)+Q(99, 100)], [Q(1, 2), Q(1, 2)])
    boundary = rate(Q(1, 2), [Q(2), Q(3)], [Q(1, 2), Q(1, 2)])
    assert before == Q(1, 2) and boundary < before
    assert valid([0, 2, 4, 1, 3, 5], [2, 3])
    return dict(unsafe_endpoint_merge=dict(old_return=old, merged_return=merged),
                disappearing_singleton=dict(delta=d0, later_delta=d0+h, budget=E,
                                            lost_family_later_energy=1+d0+h, baseline_energy=Q(1), return_value=Q(1, 2)),
                endpoint_new_resonance=dict(A=[0, 2, 4], B=[0, 2, 4],
                                            before_delta=Q(99, 100), before_return=before,
                                            at_one_return=boundary),
                physical_cost=dict(component_sizes=[5, 5, 3], sum=13))


def lighter_shift_controls():
    rows = []
    # Normalize both shapes to zero as in the infimum-transfer proof. These
    # tagged inputs are not misreported as degenerate physical protocols.
    A, B = list(range(5)), list(range(3))
    for w in [Q(0), Q(1, 5), Q(1, 2), Q(4, 5), Q(1)]:
        for delta in [Q(1, 10), Q(1, 2)]:
            for t in [Q(1, 3), Q(1, 2), Q(3, 4)]:
                normalized = [dict(shape=A, support=[1, 3], population=[Q(2, 5), Q(3, 5)], offset=Q(0)),
                              dict(shape=B, support=[1], population=[Q(1)], offset=Q(0))]
                weights = [w, 1-w]
                shifted = 0 if w <= 1-w else 1
                if 0 < w < 1:
                    normalized[shifted]['offset'] = delta
                spectrum, S, p = physical(normalized, weights)
                e0 = w*Q(11, 5)+(1-w)
                r0 = w*rate(t, [1, 3], [Q(2, 5), Q(3, 5)])+(1-w)/2
                cost = delta*min(w, 1-w)
                assert valid(spectrum, S) and len(spectrum) <= 8
                assert min(b-a for a, b in zip(spectrum, spectrum[1:])) >= delta
                assert dot(S, p) == e0+cost and cost <= delta/2
                assert rate(t, S, p) == r0
                rows.append(dict(t=t, delta=delta, weights=weights, shifted_index=shifted,
                                 spectrum=spectrum, support=S, population=p,
                                 normalized_mean=e0, mean=dot(S, p), energy_cost=cost,
                                 normalized_return=r0, actual_return=rate(t, S, p)))
    return rows


def encode(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


def calculate():
    refs = ['explorations/conditional-build/k1972-thermal-two-component-reduction-2026-10-22.md',
            'explorations/conditional-build/k1978-thermal-spectral-spacing-2026-10-23.md',
            'explorations/conditional-build/k1981-wide-spacing-thermal-frontier-2026-10-23.md',
            'explorations/conditional-build/k1987-thermal-spacing-parametric-frontier-2026-10-23.md',
            'explorations/conditional-build/k1996-positive-spacing-finite-program-2026-10-23.md',
            'explorations/conditional-build/k1998-uniform-small-spacing-transfer-2026-10-23.md']
    return encode(dict(result_id='K2006', status='active_research', classification='INTERNAL_STRUCTURAL_ONLY',
                       target_claim='NONE-NOT-A-KILL',
                       claim_ceiling='conditional internal mathematics; no GU, source, ledger, canon, novelty or external-certification credit',
                       proof_artifact='explorations/conditional-build/k2006-uniform-two-component-spacing-2026-10-24.md',
                       geometry=geometry_controls(), component_reductions=component_examples(),
                       continuity_repairs=repair_controls(), contrary=contrary_controls(),
                       lighter_component_transfers=lighter_shift_controls(),
                       inputs={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},
                       scope='K1972 two-component result transferred to positive spacing; universal canonical pair placement, linear representative box, jump-location theorem and energy-transfer cost at most delta/2. No all-d evaluated frontier or all-d wide rigidity.'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = calculate()
    if args.write:
        OUT.write_text(json.dumps(data, indent=2)+'\n')
    else:
        assert data == json.loads(OUT.read_text()), 'complete certificate replay'
    print('PASS K2006 producer:', data['geometry']['exact_obligations'],
          'exact geometry obligations;', len(data['component_reductions']),
          'physical reduction examples;', len(data['continuity_repairs']), 'exact energy repairs')
    print('PASS K2006 lighter-component transfers:', len(data['lighter_component_transfers']))
