"""Independent exact shell, interval-sweep and dual-bound verification.

Does not import the producer. Mathematical mutations are checked only after
a successful clean baseline. Assertion failures are catches; crashes are not.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import copy
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'lab/process/k2006-uniform-two-component-spacing.json'


def qs(xs):
    return [Q(x) for x in xs]


def mean(S, p):
    return sum((s*w for s, w in zip(S, p)), Q(0))


def physical_shells(A, S):
    assert len(set(A)) == len(A), 'nondegenerate physical spectrum'
    for total in {s+b for s in S for b in range(4)}:
        physical = [a for a in A if total-a in (0, 1, 2, 3)]
        occupied = [s for s in S if total-s in (0, 1, 2, 3)]
        assert len(physical) >= 2*len(occupied), 'actual shell rank doubling'
        assert len(occupied) <= 2, 'at most two occupied directions in a four-label shell'


def shell_return(t, S, p):
    Z = sum(t**b for b in range(4))
    retained = []
    for s in S:
        q = Q(0)
        for b in range(4):
            candidates = [w*t**int(s+b-f)/Z for f, w in zip(S, p)
                          if s+b-f in (0, 1, 2, 3)]
            q += max(candidates)/2
        retained.append(q)
    return sum(max(w-q, 0) for w, q in zip(p, retained))


def sweep_offset(A, B, delta):
    """Sweep open forbidden intervals, explicitly retaining touching points."""
    intervals = sorted((Q(a-b)-delta, Q(a-b)+delta) for a in A for b in B)
    x = Q(0)
    for low, high in intervals:
        if low >= x:
            return x
        if high > x:
            x = high
    return x


def geometry_reference():
    # Subsets of the bounded integer interval, not producer gap words.
    shapes = [[0]]
    for n in range(2, 5):
        for tail in combinations(range(1, 10), n-1):
            A = [0]+list(tail)
            if all(b-a <= 3 for a, b in zip(A, A[1:])):
                shapes.append(A)
    assert len(shapes) == 40, 'complete small integer-shape controls'
    count = 0
    for A in shapes:
        for B in shapes:
            centers = set(a-b for a in A for b in B)
            missing = next(i for i in range(max(A)+2) if i not in centers)
            for delta in map(Q, ['1/10', '1/2', '51/100', '3/4', '1']):
                actual = sweep_offset(A, B, delta)
                formula = delta if delta <= Q(1, 2) else missing-1+delta
                assert actual == formula, 'interval-sweep placement identity'
                assert all(abs(a-b-actual) >= delta for a in A for b in B), 'spacing at canonical offset'
                assert max(max(A), actual+max(B)) <= 3*(len(A)+len(B)-2)+delta, 'linear pair span'
                count += 3
    return len(shapes), count


def flattened(components, weights):
    active = [(c, w) for c, w in zip(components, weights) if w > 0]
    low = min(Q(c['offset']) for c, w in active)
    A, masses = [], {}
    for c, w in active:
        off = Q(c['offset'])-low
        A.extend(off+Q(x) for x in c['shape'])
        for s, p in zip(c['support'], c['population']):
            energy = off+Q(s)
            assert energy not in masses, 'independent physical component sites'
            masses[energy] = w*Q(p)
    S = sorted(masses)
    return sorted(A), S, [masses[s] for s in S]


def dual_minimum(e, r, budget):
    # Dual max_{lambda>=0} min_i(r_i+lambda e_i)-lambda budget.
    candidates = {Q(0)}
    for i, j in combinations(range(len(e)), 2):
        if e[i] != e[j]:
            slope = (r[j]-r[i])/(e[i]-e[j])
            if slope >= 0:
                candidates.add(slope)
    return max(min(v+lam*x for v, x in zip(r, e))-lam*budget for lam in candidates)


def check(data, reference):
    n = 0
    assert data['geometry']['shape_count'] == reference[0]
    assert data['geometry']['parameter_controls'] == 8000
    assert data['geometry']['exact_obligations'] == reference[1]
    for row in data['geometry']['rows']:
        A, B, delta, x = row['A'], row['B'], Q(row['delta']), Q(row['offset'])
        assert x == sweep_offset(A, B, delta), 'exact least feasible offset'
        spectrum = sorted([Q(a) for a in A]+[x+b for b in B])
        assert spectrum == qs(row['spectrum']), 'actual canonical spectrum'
        assert len(set(spectrum)) == len(spectrum) and min(b-a for a, b in zip(spectrum, spectrum[1:])) >= delta, 'actual spacing'
        assert row['summed_dimension'] == len(A)+len(B), 'sum physical component dimensions'
        if delta == 1:
            reached = {spectrum[0]}
            while True:
                extra = {b for b in spectrum if any(abs(a-b) in (1, 2, 3) for a in reached)}
                if extra <= reached:
                    break
                reached |= extra
            assert len(reached) == len(spectrum), 'delta1 connected union'
        n += 5

    for row in data['component_reductions']:
        old, new, t = qs(row['old_weights']), qs(row['new_weights']), Q(row['t'])
        assert sum(old) == sum(new) == 1 and min(new) >= 0, 'component probability normalization'
        assert sum(bool(w) for w in new) <= 2, 'at most two retained components'
        e, r = [], []
        for c in row['components']:
            S, p = qs(c['support']), qs(c['population'])
            physical_shells(qs(c['shape']), S)
            assert sum(p) == 1 and min(p) >= 0, 'normalized component preparation'
            e.append(Q(c['offset'])+mean(S, p))
            r.append(shell_return(t, S, p))
        assert mean(e, new) <= mean(e, old), 'original energy budget preserved'
        assert mean(r, new) <= mean(r, old), 'original return dominated'
        assert mean(r, new) == dual_minimum(e, r, mean(e, old)), 'independent optimal component-weight dual'
        sizes = []
        for name, weights in [('before', old), ('after', new)]:
            A, S, p = flattened(row['components'], weights)
            saved = row[name]
            assert A == qs(saved['spectrum']) and S == qs(saved['support']) and p == qs(saved['population']), 'actual retained component construction'
            physical_shells(A, S)
            assert A[0] == 0 and min(b-a for a, b in zip(A, A[1:])) >= Q(row['spacing']), 'retained ground and positive spacing'
            assert mean(S, p) == Q(saved['energy']), 'physical mean energy'
            assert shell_return(t, S, p) == Q(saved['return_value']) == mean(r, weights), 'independent bath-label return and additivity'
            sizes.append(len(A))
        assert sizes[1] <= sizes[0], 'physical dimension decreases'
        n += 15

    for row in data['continuity_repairs']:
        S, T = qs(row['old_support']), qs(row['new_support'])
        p, q, t = qs(row['old_population']), qs(row['repaired_population']), Q(row['t'])
        E, theta = Q(row['budget']), Q(row['repair_mass'])
        assert sum(q) == 1 and min(q) >= 0 and 0 < theta < 1, 'repair probability'
        assert mean(S, p) == mean(T, q) == E, 'repair pays changed spectrum energy'
        assert theta == (mean(T, p)-E)/(mean(T, p)-min(T)), 'energy-repair mass identity'
        assert shell_return(t, S, p) == Q(row['old_return']) and shell_return(t, T, q) == Q(row['new_return']), 'repair return from bath labels'
        norm = sum(abs(a-b) for a, b in zip(p, q))
        assert norm == Q(row['l1_change']) and abs(Q(row['new_return'])-Q(row['old_return'])) <= 4*norm, 'finite exact continuity control'
        n += 5

    for row in data['lighter_component_transfers']:
        w = qs(row['weights'])
        delta, t = Q(row['delta']), Q(row['t'])
        shifted = row['shifted_index']
        A, S, p = qs(row['spectrum']), qs(row['support']), qs(row['population'])
        physical_shells(A, S)
        assert A[0] == 0 and min(b-a for a, b in zip(A, A[1:])) >= delta, 'transfer actual ground and spacing'
        assert len(A) == (5 if w[0] else 0)+(3 if w[1] else 0), 'transfer exact physical dimension charge'
        e0 = w[0]*Q(11, 5)+w[1]
        expected_return = w[0]*shell_return(t, [Q(1), Q(3)], [Q(2, 5), Q(3, 5)])+w[1]/2
        assert mean(S, p) == Q(row['mean']) == e0+delta*min(w), 'lighter shift mean-energy cost'
        assert Q(row['normalized_mean']) == e0 and Q(row['energy_cost']) == delta*min(w) <= delta/2, 'half-spacing energy-transfer bound'
        assert shell_return(t, S, p) == Q(row['actual_return']) == Q(row['normalized_return']) == expected_return, 'transfer preserves exact thermal return'
        assert w[shifted] == min(w), 'shift lighter component'
        n += 6

    c = data['contrary']
    old = shell_return(Q(1, 2), [Q(1), Q(3), Q(10)], [Q(1, 45), Q(1, 5), Q(7, 9)])
    merged = shell_return(Q(1, 2), [Q(1), Q(3)], [Q(4, 5), Q(1, 5)])
    assert old == Q(c['unsafe_endpoint_merge']['old_return']) == Q(22, 45)
    assert merged == Q(c['unsafe_endpoint_merge']['merged_return']) == Q(1, 2) and old < merged, 'unsafe endpoint merge really worsens return'
    s = c['disappearing_singleton']
    assert Q(s['lost_family_later_energy']) > Q(s['budget']) >= Q(s['baseline_energy']), 'family disappears while baseline remains feasible'
    assert Q(s['return_value']) == shell_return(Q(1, 2), [Q(1)], [Q(1)]) == Q(1, 2), 'disappearing singleton has pure baseline value'
    contact = c['endpoint_new_resonance']
    before = shell_return(Q(1, 2), [Q(2), Q(2)+Q(contact['before_delta'])], [Q(1, 2), Q(1, 2)])
    after = shell_return(Q(1, 2), [Q(2), Q(3)], [Q(1, 2), Q(1, 2)])
    physical_shells(list(map(Q, range(6))), [Q(2), Q(3)])
    assert before == Q(contact['before_return']) == Q(1, 2)
    assert after == Q(contact['at_one_return']) < before, 'delta1 newly joined shells improve sharp return'
    assert c['physical_cost']['sum'] == sum(c['physical_cost']['component_sizes']) == 13, 'dimension13 actual cost'
    return n+7


def mutate(data, fault):
    b = copy.deepcopy(data)
    if fault == 'component_mass':
        b['component_reductions'][0]['new_weights'][0] = '2'
    elif fault == 'offset':
        row = next(r for r in b['geometry']['rows'] if r['A'] == list(range(5)) and r['delta'] == '3/4')
        row['offset'] = '3/4'
    elif fault == 'dimension':
        row = b['geometry']['rows'][0]
        row['summed_dimension'] = max(len(row['A']), len(row['B']))
    elif fault == 'unpaid_energy':
        row = b['continuity_repairs'][0]
        row['repaired_population'] = row['old_population']
    elif fault == 'endpoint_return':
        b['contrary']['endpoint_new_resonance']['at_one_return'] = '1/2'
    elif fault == 'shift_heavier':
        row = next(r for r in b['lighter_component_transfers'] if r['weights'] == ['1/5', '4/5'])
        # Construct the actual wrong orientation consistently. This remains a
        # valid thermal protocol but exceeds the claimed delta/2 energy cost.
        delta = Q(row['delta'])
        row['shifted_index'] = 1
        row['spectrum'] = list(map(str, sorted([Q(i) for i in range(5)]+[delta+i for i in range(3)])))
        row['support'] = list(map(str, [Q(1), 1+delta, Q(3)]))
        row['population'] = ['2/25', '4/5', '3/25']
        row['energy_cost'] = str(Q(4, 5)*delta)
        row['mean'] = str(Q(row['normalized_mean'])+Q(4, 5)*delta)
    elif fault == 'free_shift':
        row = next(r for r in b['lighter_component_transfers'] if r['weights'] == ['1/2', '1/2'])
        row['energy_cost'] = '0'
    elif fault == 'component_return':
        b['component_reductions'][0]['after']['return_value'] = '0'
    else:
        raise ValueError(fault)
    return b


if __name__ == '__main__':
    data = json.loads(OUT.read_text())
    reference = geometry_reference()
    count = check(data, reference)
    print('PASS K2006 independent baseline:', reference[1], 'geometry obligations;', count, 'physical/consumer check groups')
    catches = []
    for fault in ['component_mass', 'offset', 'dimension', 'unpaid_energy', 'endpoint_return', 'shift_heavier', 'free_shift', 'component_return']:
        try:
            check(mutate(data, fault), reference)
        except AssertionError as exc:
            catches.append((fault, str(exc)))
            print('DETECTED mathematical fault', fault, ':', str(exc))
        else:
            raise AssertionError('missed mathematical corruption: '+fault)
    for path, digest in data['inputs'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, 'input provenance: '+path
    print('PASS K2006:', len(catches), 'genuine mathematical faults after green baseline;', len(data['inputs']), 'separate provenance hashes')
