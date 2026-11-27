#!/usr/bin/env python3
"""Bounded exact reuse test for two-Q7 principal propagation leakage.

No new inverse, closure, numerical solve or full-R regularity assumption.
Default: cheap certificate/data replay plus only the 36 native highest7 seeds.
--data-only skips native seed reconstruction and is explicitly partial.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
import sys
import time


EXPECTED = {
    'lab/process/source-action-reduced-evolution.json': 'd299647a410d660a2b01f9612e1ab271368f7a4b3244c91655793aa5ed7e1945',
    'lab/process/source-action-kappa1-constraints.json': '5d3401666f8072dd225924e0cc9073c16c7d6c59efd0b4b941e1fcce7ce29233',
    'lab/process/source-action-deep-coefficients.json': 'fb4aacfa69cbc1127b7fddf3b4f66811650c1fd3a889363cc6dfab940439b274',
    'tests/program-focus/source_action_reduced_evolution_probe.py': '2279acba19fe23ba3cbc77106ef8137fb72c4e758bdf45b1ee3ffe259a617426',
    'tests/program-focus/source_action_deep_algebra.py': '4e3800131049e2b397bbce6106bfc5766d2f5fbf996319c50942f3b805d65598',
    'tests/program-focus/source_action_metric_symbol_probe.py': 'eccac86c829c48848a4db9ab49d0313601bc3b19aca9a1fc6635520f489254ef',
    'tests/program-focus/source_action_deep_geometry.py': '7cdfe5f7609300c1ab4fb482f309cfafa52d0aa66cf353ef8b1f9c8be07e52df',
}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


class C:
    """Minimal exact Gaussian rationals, same serialized convention as native C."""
    def __init__(self, a=0, b=0):
        if isinstance(a, C):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = Q(a), Q(b)
    def __add__(x, y):
        y = C(y); return C(x.a+y.a, x.b+y.b)
    __radd__ = __add__
    def __neg__(x): return C(-x.a, -x.b)
    def __sub__(x, y): return x + -C(y)
    def __rsub__(x, y): return C(y) + -x
    def __mul__(x, y):
        y = C(y); return C(x.a*y.a-x.b*y.b, x.a*y.b+x.b*y.a)
    __rmul__ = __mul__
    def __truediv__(x, y):
        y = C(y); den = y.a*y.a+y.b*y.b
        return C((x.a*y.a+x.b*y.b)/den, (x.b*y.a-x.a*y.b)/den)
    def __rtruediv__(x, y): return C(y)/x
    def __bool__(x): return bool(x.a or x.b)
    def __eq__(x, y):
        y = C(y); return x.a == y.a and x.b == y.b
    def conj(x): return C(x.a, -x.b)
    def ser(x): return [str(x.a), str(x.b)]


def cnorm(z):
    z = C(z)
    return abs(z.a)+abs(z.b)


def serial(v):
    return [[e, c, C(z).ser()] for (e, c), z in sorted(v.items()) if z]


def load_bound(repo):
    actual = {name: hashlib.sha256((repo/name).read_bytes()).hexdigest() for name in EXPECTED}
    assert actual == EXPECTED, 'Dependency hash mismatch; review rather than silently rebind.'
    load = lambda name: json.loads((repo/('lab/process/'+name+'.json')).read_text())
    return actual, load('source-action-reduced-evolution'), load('source-action-kappa1-constraints'), load('source-action-deep-coefficients')


def replay_diagonals(evolution, constraints, backgrounds):
    """Replay the old full-source diagonal/error formula, with exact root bindings."""
    source_rows = evolution['exact_probe']['source_receivers']
    sources = {row['basis_index']: row for row in source_rows}
    assert sources[5]['b6'] == [[37, ['3145728', '0']]]
    assert sources[12]['b6'] == [[40, ['9437184', '0']]]
    assert sources[5]['b7_lowered'] == sources[12]['b7_lowered'] == []
    six = constraints['exact_probe']['spin6']
    assert six['spin6']['spin6_time_kernel_multiplicity'] == 128
    assert six['constraint_inverse']['multiplicity_kernel_dimension'] == 128
    assert six['constraint_inverse']['kernel_pairing_rank'] == 128
    assert constraints['exact_probe']['spin7']['time_kernel'] == 16
    results = []
    for ri in (0, 1):
        root = backgrounds['certified_roots'][ri]
        assert root['certificate']['status'] == 'exact_local_root_certified'
        assert root['certificate']['kappa'] == '1'
        candidate = constraints['spin6_inverse_candidates'][ri]
        official = six['constraint_inverse']['root_certificates'][ri]
        assert candidate['root'] == official['root'] == ri and official['all_certified']
        assert len(candidate['blocks']) == len(official['blocks']) == 4
        all_ids = []
        for b, proved in zip(candidate['blocks'], official['blocks']):
            assert b['status'] == proved['status'] == 'exact_rootball_invertibility_certified'
            assert b['dimension'] == proved['dimension'] == len(b['indices'])
            for key in ('component', 'root_radius', 'neumann_bound', 'center_defect',
                        'inverse_norm_bound', 'coefficient_norm_bound'):
                assert b[key] == proved[key], ('certificate field', key)
            assert Q(b['root_radius']) == Q(root['certificate']['radius'])
            assert digest(b['rational_inverse']) == proved['rational_inverse_sha256']
            eta = Q(b['neumann_bound'])
            assert 0 <= eta < 1
            assert eta == Q(b['center_defect']) + Q(b['root_radius'])*Q(b['inverse_norm_bound'])*Q(b['coefficient_norm_bound'])
            all_ids.extend(b['indices'])
        assert sorted(all_ids) == list(range(128))
        diag = []
        old_rows = {x['basis_index']: x for x in evolution['exact_probe']['physical_derivative_energy'][ri]['witnesses']}
        assert evolution['exact_probe']['physical_derivative_energy'][ri]['root'] == ri
        for index in (5, 12):
            bsource = {i: C(*z) for i, z in sources[index]['b6']}
            cs, es = {}, {}
            for block in candidate['blocks']:
                ids = block['indices']
                if not any(i in bsource for i in ids):
                    continue
                inverse = [[C(*z) for z in row] for row in block['rational_inverse']]
                c0 = [-sum((a*bsource.get(j, C()) for a, j in zip(row, ids)), C()) for row in inverse]
                eta = Q(block['neumann_bound'])
                err = eta/(1-eta)*max(map(cnorm, c0))
                cs.update(zip(ids, c0)); es.update((i, err) for i in ids)
            value = sum((z.conj()*cs[i] for i, z in bsource.items()), C())
            error = sum(cnorm(z)*es[i] for i, z in bsource.items())+abs(value.b)
            lower, upper = value.a-error, value.a+error
            old = old_rows[index]
            for key, new in [('center', value.a), ('error_bound', error), ('lower', lower), ('upper', upper)]:
                assert Q(old[key]) == new, ('old energy mismatch', ri, index, key)
            sign = 'positive' if lower > 0 else 'negative' if upper < 0 else 'unresolved'
            assert sign == old['sign'] and sign != 'unresolved'
            diag.append({'basis_index': index, 'center': str(value.a), 'error_bound': str(error),
                         'lower': str(lower), 'upper': str(upper), 'sign': sign})
        positive = next(x for x in diag if x['sign'] == 'positive')
        negative = next(x for x in diag if x['sign'] == 'negative')
        # For H=[[a,z],[conj(z),d]], det(H)=ad-|z|^2 <= ad.
        # a>=positive.lower>0 and d<=negative.upper<0.
        det_upper = Q(positive['lower'])*Q(negative['upper'])
        assert det_upper < 0
        results.append({'root': ri, 'root_id': root['id'], 'root_radius': root['certificate']['radius'],
                        'diagonals': diag, 'determinant_strict_upper_bound': str(det_upper),
                        'cross_entry_assumption': 'None beyond native Hermitian reciprocity.',
                        'highest_Q_multiplicity_quotient_rank': 2})
    return results


def native_parity(repo, evolution):
    """Only highest7 seed reconstruction; no complete N6 basis or new solve."""
    sys.path.insert(0, str(repo/'tests/program-focus'))
    import source_action_deep_geometry as g
    from source_action_deep_algebra import Engine, add, scale
    from source_action_metric_symbol_probe import symbols
    E, I = Engine(g), C(0, 1)
    assert all(c.bit_count()%2 == 1 for e, c in E.phi1)
    assert all(c.bit_count()%2 == 0 for e, c in E.phi2)
    # The structural proof also uses: star changes only e; cmul returns c xor d;
    # adjoints reverse the same odd total factors, with diagonal native weights.
    poly = {0: C(1)}
    for a, b in [(0, 1), (10, 12), (9, 11), (5, 8)]:
        poly = E.cliff_product(poly, {1<<a: C(1), 1<<b: I})
    bs, metadata = [], []
    for mask in range(64):
        zeros = [a for j, a in enumerate([2, 3, 4, 6, 7, 13]) if mask>>j&1]
        if (4+len(zeros))%4 not in (0, 3):
            continue
        cliff = poly
        for a in zeros:
            cliff = E.cliff_product(cliff, {1<<a: C(1)})
        v = {(1<<a, c): f*z for a, f in [(5, C(1)), (8, I)] for c, z in cliff.items()}
        bs.append(scale(1/v[min(v)], v)); metadata.append(zeros)
    assert len(bs) == 36

    def rot(i, j, v):
        H = g.zero(); H[i][j] = Q(1); H[j][i] = Q(-1)
        action = [g.h_action(H, a) for a in range(14)]
        spin = {}
        for a in range(14):
            for b in range(a+1, 14):
                z = action[b].get(a, Q())/(2*g.d[b])
                if z: spin[(1<<a)|(1<<b)] = z
        assert all(c.bit_count()%2 == 0 for c in spin)
        out = {}
        for (e, c), value in v.items():
            ai = e.bit_length()-1
            for b in range(14):
                z = -action[b].get(ai, Q())
                if z: out[1<<b, c] = out.get((1<<b, c), 0)+value*z
            for cc, z in E.cliff_product(spin, {c: Q(1)}, 'comm').items():
                out[e, cc] = out.get((e, cc), 0)+value*z
        return {k: z for k, z in out.items() if z}

    tau = [Q(0)]*14; tau[3] = Q(1)
    xi = [Q(0)]*14; xi[0] = Q(1)
    old_sources = {row['basis_index']: row for row in evolution['exact_probe']['source_receivers']}
    fields, time_fields, checks = [], [], []
    for j in (5, 12):
        assert {c.bit_count() for e, c in bs[j]} == {8}
        V = symbols(E, tau, bs[j])[0]
        AV = symbols(E, tau, V)[0]
        KV = symbols(E, xi, V)[0]
        assert V and AV and KV
        assert all(c.bit_count()%2 == 1 for e, c in V)
        assert all(c.bit_count()%2 == 0 for e, c in AV)
        assert all(c.bit_count()%2 == 0 for e, c in KV)
        assert rot(0, 1, V) == scale(7*I, V)
        assert not add(rot(0, 2, V), scale(I, rot(1, 2, V)))
        vhash = digest(serial(V))
        assert vhash == old_sources[j]['range_sha256']
        fields.append(V); time_fields.append(AV)
        checks.append({'basis_index': j, 'seed_zero_axes': metadata[j], 'seed_degree': 8,
                       'V_terms': len(V), 'AV_terms': len(AV), 'K0V_terms': len(KV),
                       'V_clifford_grades': sorted({c.bit_count() for e, c in V}),
                       'AV_clifford_grades': sorted({c.bit_count() for e, c in AV}),
                       'range_sha256': vhash, 'weight7_and_highest': True})
    # Physical imaginary form is minus this raw pairing; zero is unchanged.
    canonical = [[C(E.pair({k: C(z).conj() for k, z in U.items()}, AV)) for AV in time_fields] for U in fields]
    assert all(not z for row in canonical for z in row)
    native_gram = [[C(E.pair({k: C(z).conj() for k, z in U.items()}, V)) for V in fields] for U in fields]
    assert native_gram == [[C(3145728), C()], [C(), C(-9437184)]]
    return {'seeds': checks, 'canonical_highest_gram': [[z.ser() for z in row] for row in canonical],
            'native_Q_highest_gram': [[z.ser() for z in row] for row in native_gram],
            'all_SO3_descendants_canonical_isotropic': 'Structural Clifford parity proof, not a sampled extrapolation.',
            'Phi_odd_factor_parity': True, 'rotation_even_factor_parity': True}


def run(repo, data_only=False):
    start = time.monotonic()
    bindings, evolution, constraints, backgrounds = load_bound(repo)
    roots = replay_diagonals(evolution, constraints, backgrounds)
    parity = None if data_only else native_parity(repo, evolution)
    return {'scope': 'Two owned Q7 modules at the two held W2/K95 roots; horizontal theta0 principal time-flow quotient only. No full-R inverse, physical state admission or source/GU exclusion.',
            'status': 'partial_data_replay' if data_only else 'exact_reuse_and_native_parity_pass',
            'dependency_bindings': bindings, 'roots': roots, 'native_parity': parity,
            'unknown_auxiliary_kernel': 'Cannot alter these Q-dual rows: the derivative sources lie in complete invertible N6; self-adjointness annihilates every full-M kernel correction.',
            'conclusion_requires_written_theorem': 'No nonzero SO3 submodule contained in these two Q7 copies is closed under the unrestricted local-module degree-two theta0 time symbol.',
            'not_claimed': ['Nonexistence of specially constrained or spatially homogeneous Q solutions',
                            'Instability or ghost propagation', 'W2 or GU inconsistency'],
            'seconds': time.monotonic()-start}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--data-only', action='store_true')
    args = parser.parse_args()
    result = run(args.repo.resolve(), args.data_only)
    payload = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    else:
        print(payload, end='')


if __name__ == '__main__':
    main()
