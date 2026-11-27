#!/usr/bin/env python3
"""Exact four-witness Riemann-silence theorem on the fixed K77 carrier.

Requires SymPy 1.14.0. Loads only definitions from the authenticated B3 probe;
never executes its source checks, census, Sage, FLINT or main body. Rebuilds
four native kernel witnesses and checks them by independent rational word
algebra. This does not construct a source action or a physical domain.
"""
from __future__ import annotations

import argparse
import ast
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path
import sys
import time
import types

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
B3 = 'tests/channel-swings/resolver_wave_k77b3_full_domain_cyclic_kernel_obstruction_probe.py'
B2 = 'lab/process/resolver-wave-k77b2-shiab-family-curvature-selector-transgression.json'
B3_CERT = 'lab/process/resolver-wave-k77b3-full-domain-cyclic-kernel-obstruction.json'
B2_REPORT = 'explorations/resolver-wave-k77b2-shiab-family-curvature-selector-transgression-2026-08-04.md'
B3_REPORT = 'explorations/resolver-wave-k77b3-full-domain-cyclic-kernel-obstruction-2026-08-04.md'
CERT = 'lab/process/source-action-riemann-silence-certificates.json'


def require(value, message):
    if not value:
        raise AssertionError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def load_b3_definitions(path):
    """Execute the declaration prefix, excluding optional unused imports."""
    tree = ast.parse(path.read_text(), filename=str(path))
    nodes = []
    stop = None
    for node in tree.body:
        if (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name) and node.value.func.id == 'print'):
            stop = ast.literal_eval(node.value.args[0])
            break
        if isinstance(node, ast.ImportFrom) and node.module == 'flint':
            continue
        if isinstance(node, ast.Import) and any(alias.name == 'subprocess' for alias in node.names):
            continue
        require(isinstance(node, (ast.Import, ast.ImportFrom, ast.Assign, ast.AnnAssign,
                                  ast.FunctionDef, ast.For, ast.Expr)), 'unexpected B3 prefix statement')
        nodes.append(node)
    require(stop == 'A. PRIMARY SOURCE COLLISION AND LAYER 0', 'B3 definition boundary')
    module = types.ModuleType('gu_riemann_silence_owned_b3_definitions')
    module.__file__ = str(path)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), 'exec'), module.__dict__)
    require('subprocess' not in module.__dict__ and 'sage' not in module.__dict__, 'no old census imported')
    require(module.sp.__version__ == '1.14.0', 'pinned exact symbolic dependency')
    return module


def sparse_record(form):
    return [[ext, cliff, str(value)] for ext, row in sorted(form.items())
            for cliff, value in sorted(row.items()) if value]


def rational_form(form):
    return {(ext, cliff): Q(str(value)) for ext, row in form.items() for cliff, value in row.items() if value}


def independent_word_product(left, right, eta, exterior=False):
    """List insertion and adjacent equal-letter cancellation, not bit inversions."""
    word = list(left)
    sign = 1
    for letter in right:
        at = len(word)
        while at and word[at-1] > letter:
            at -= 1
            sign = -sign
        if at and word[at-1] == letter:
            if exterior:
                return (), 0
            del word[at-1]
            sign *= eta[letter]
        else:
            word.insert(at, letter)
    return tuple(word), sign


def word(mask, n):
    return tuple(i for i in range(n) if mask & (1 << i))


def mask(indices):
    return sum(1 << i for i in indices)


def independent_wedge(left, right, eta):
    n = len(eta)
    out = {}
    for (e, c), x in left.items():
        for (f, d), y in right.items():
            ef, s = independent_word_product(word(e, n), word(f, n), eta, True)
            if not s:
                continue
            cd, t = independent_word_product(word(c, n), word(d, n), eta)
            key = (mask(ef), mask(cd))
            out[key] = out.get(key, Q(0)) + s*t*x*y
    return {key: value for key, value in out.items() if value}


def independent_add(*forms):
    out = {}
    for form in forms:
        for key, value in form.items():
            out[key] = out.get(key, Q(0)) + value
    return {key: value for key, value in out.items() if value}


def independent_hodge(form, eta):
    n = len(eta)
    out = {}
    for (e, c), value in form.items():
        selected = word(e, n)
        complementary = tuple(i for i in range(n) if i not in selected)
        _, sign = independent_word_product(selected, complementary, eta, True)
        for i in selected:
            sign *= eta[i]
        out[(mask(complementary), c)] = sign*value
    return out


def independent_pair_top(left, right, eta):
    return 128*independent_wedge(left, right, eta).get(((1 << len(eta))-1, 0), Q(0))


def independent_curvature(form, eta):
    """Recover all covariant R slots from sparse grade-two two-forms."""
    n = len(eta)
    result = {}
    for (e, c), value in form.items():
        ij, ab = word(e, n), word(c, n)
        require(len(ij) == len(ab) == 2, 'independent curvature type')
        i, j = ij
        a, b = ab
        raised = value*eta[a]*eta[b]
        for ii, jj, s in ((i, j, 1), (j, i, -1)):
            for aa, bb, t in ((a, b, 1), (b, a, -1)):
                result[(ii, jj, aa, bb)] = s*t*raised
    return result


def independent_outputs(curvature, eta):
    n = len(eta)
    ric = [[sum(eta[i]*curvature.get((i, j, i, l), Q(0)) for i in range(n))
            for l in range(n)] for j in range(n)]
    scalar = sum(eta[i]*ric[i][i] for i in range(n))
    scalar_metric = [[scalar*eta[i] if i == j else Q(0) for j in range(n)] for i in range(n)]
    outputs = []
    for high in (False, True):
        for tensor in (ric, scalar_metric):
            form = {}
            for i in range(n):
                for j in range(n):
                    if tensor[i][j]:
                        cliff, sign = ((j,), 1)
                        if high:
                            cliff, sign = independent_word_product((j,), tuple(range(n)), eta)
                        form[(1 << i, mask(cliff))] = eta[j]*sign*tensor[i][j]
            outputs.append(independent_hodge(form, eta))
    return ric, scalar, outputs


def row_rank(matrix):
    rows = [list(map(Q, row)) for row in matrix]
    rank = 0
    for col in range(len(rows[0]) if rows else 0):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        factor = rows[rank][col]
        rows[rank] = [v/factor for v in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                factor = rows[i][col]
                rows[i] = [a-factor*b for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank, rows


def build_certificate(repo):
    paths = (B3, B2, B3_CERT, B2_REPORT, B3_REPORT)
    inputs = {name: digest(repo/name) for name in paths}
    b = load_b3_definitions(repo/B3)
    eta, n = tuple(b.ETA), b.N
    checks = {}
    def check(name, value):
        checks[name] = bool(value)
        require(value, name)
    check('native_signature_7_7', n == 14 and eta.count(1) == eta.count(-1) == 7)
    check('native_volume_square_positive', b.emul(b.VOLUME, b.VOLUME) == {0: 1})
    check('native_trace_identity_and_volume', b.scalar_trace({0: 1}) == 128 and b.scalar_trace(b.VOLUME) == 0)
    # Generator multiplication and volume multiplication exercise both signs
    # against an algorithm that reduces actual words by insertion/cancellation.
    for i, j in product(range(n), repeat=2):
        letters, sign = independent_word_product((i,), (j,), eta)
        check(f'independent_generator_product_{i}_{j}', b.emul(b.blade(i), b.blade(j)) == {mask(letters): sign})
    for i in range(n):
        letters, sign = independent_word_product((i,), tuple(range(n)), eta)
        check(f'independent_gamma_volume_{i}', b.emul(b.blade(i), b.VOLUME) == {mask(letters): sign})
        vi = b.emul(b.blade(i), b.VOLUME)
        check(f'native_high_square_{i}', b.emul(vi, vi) == {0: -eta[i]})
    families = []
    for label, active, pivot in (('low', tuple(range(12)), 12), ('high', tuple(range(13)), None)):
        c = {1 << i: b.emul(b.blade(i), b.blade(pivot)) if pivot is not None else b.blade(i)
             for i in active}
        curvature = b.wedge(c, c)
        ci = rational_form(c)
        fi = independent_wedge(ci, ci, eta)
        check(label+'_native_c_B_skew', b.form_b_skew(c))
        check(label+'_independent_curvature', rational_form(curvature) == fi)
        check(label+'_native_constant_curvature_scale2', b.matches_active_constant_curvature(curvature, set(active), 2))
        R = independent_curvature(fi, eta)
        def r(i, j, a, d):
            return R.get((i, j, a, d), Q(0))
        check(label+'_independent_pair_exchange_and_first_Bianchi', all(
            r(i,j,a,d) == r(a,d,i,j) and r(i,j,a,d)+r(j,a,i,d)+r(a,i,j,d) == 0
            for i,j,a,d in product(range(n), repeat=4)))
        ric, scalar, independent_basis = independent_outputs(R, eta)
        cross = b.cross_ricci(curvature)
        check(label+'_independent_Ricci', cross == ric)
        check(label+'_independent_scalar', b.scalar_from_cross(cross) == scalar == 2*len(active)*(len(active)-1))
        native_basis = []
        for sector in ('LOW', 'HIGH'):
            contractions = b.contraction_basis(curvature, sector)
            check(label+'_'+sector+'_symmetric_Ricci', contractions[0] == contractions[1])
            native_basis.extend((contractions[0], contractions[2]))
        for j in range(4):
            check(label+'_independent_output_'+str(j), rational_form(native_basis[j]) == independent_basis[j])
        rows = []
        for position, ell in (('outside', 13), ('inside', 0)):
            v = {1 << ell: b.blade(ell) if label == 'low' else b.emul(b.blade(ell), b.VOLUME)}
            vi = rational_form(v)
            kernel = b.quadratic_pair(v, c)
            check(label+'_'+position+'_B_skew', b.form_b_skew(v))
            check(label+'_'+position+'_native_Q_zero', not kernel)
            check(label+'_'+position+'_independent_Q_zero', not independent_add(
                independent_wedge(vi, ci, eta), independent_wedge(ci, vi, eta)))
            check(label+'_'+position+'_variation_square_zero', not b.wedge(v, v))
            responses = [Q(str(b.pair_top(v, out))) for out in native_basis]
            independent_responses = [independent_pair_top(vi, out, eta) for out in independent_basis]
            check(label+'_'+position+'_all_four_independent_pairings', responses == independent_responses)
            direct = []
            # These are exact evaluations of a cubic polynomial. Q=0 and v^2=0
            # first prove the curvature is unchanged along the whole line.
            for j, sector in enumerate(('LOW', 'LOW', 'HIGH', 'HIGH')):
                values = []
                for t in (-1, 1):
                    field = b.fadd(c, b.fscale(t, v))
                    field_F = b.wedge(field, field)
                    check(f'{label}_{position}_curvature_constant_{j}_{t}', field_F == curvature)
                    candidate = b.contraction_basis(field_F, sector)[0 if j % 2 == 0 else 2]
                    values.append(Q(str(b.pair_top(field, candidate)))/3)
                direct.append((values[1]-values[0])/2)
            check(label+'_'+position+'_actual_cubic_derivative', direct == [x/3 for x in responses])
            normalization = 128 if label == 'low' else -128
            normalized = [x/normalization for x in responses]
            rows.append({'id': label+'_'+position, 'variation': sparse_record(v),
                         'native_Q_zero': True, 'native_pairings': list(map(str, responses)),
                         'normalization_divisor': str(normalization),
                         'normalized_coefficients': list(map(str, normalized)),
                         'direct_cubic_derivative': list(map(str, direct)),
                         'unit_endpoint': list(map(str, responses)),
                         'derivative_minus_unit_endpoint': [str(x-y) for x,y in zip(direct,responses)]})
        families.append({'id': label, 'active_axes': list(active), 'pivot': pivot,
                         'field': sparse_record(c), 'curvature_sparse_sha256': canonical_hash(sparse_record(curvature)),
                         'curvature_nonzero_form_slots': len(curvature), 'curvature_scale': '2',
                         'scalar_curvature': str(scalar), 'raised_Ricci_on_active_plane': str(2*(len(active)-1)),
                         'rows': rows})
    rows = [row for family in families for row in family['rows']]
    matrix = [list(map(Q, row['normalized_coefficients'])) for row in rows]
    rank, rref = row_rank(matrix)
    check('complete_four_coordinate_rank4', rank == 4)
    check('independent_SymPy_rank4', b.sp.Matrix(matrix).rank() == rank)
    check('old_outside_witnesses_only_rank2', row_rank([matrix[0], matrix[2]])[0] == 2)
    check('old_outside_not_full_four_coordinate_theorem', row_rank([matrix[0], matrix[2]])[0] != rank)
    check('new_inside_rows_add_two_dimensions', rank-2 == 2)
    check('native_high_trace_sign_is_negative', Q(rows[2]['native_pairings'][3]) < 0 and Q(rows[3]['native_pairings'][2]) < 0)
    check('planted_positive_high_trace_sign_rejected', Q(rows[2]['native_pairings'][3]) != 128*312)
    low_c = {1 << i: b.emul(b.blade(i), b.blade(12)) for i in range(12)}
    check('planted_nonmatching_form_index_is_not_kernel', bool(b.quadratic_pair({1 << 13: b.blade(0)}, low_c)))
    check('planted_low_pivot_coefficient_is_not_kernel', bool(b.quadratic_pair({1: b.blade(12)}, low_c)))
    check('no_Einstein_ratio_used', matrix[0][0] == matrix[2][2] == 0 and matrix[1][0] != 0 and matrix[3][2] != 0)
    return {'schema': 'gu-riemann-silence-certificate-v1', 'data_only': True,
            'producer_sha256': digest(Path(__file__).resolve()), 'native_inputs_sha256': inputs,
            'dependency': {'sympy': '1.14.0', 'native_loader': 'AST declaration prefix before first printed main-stage marker; FLINT/subprocess imports excluded; no main/census execution'},
            'carrier': {'signature': [7,7], 'dimension': 14, 'real_structure': 'real B-skew Cl(7,7) coefficients',
                        'pairing': 'native top-form trace; trace(1)=128; orientation0..13; no positive metric substitution',
                        'inherited_Riemann_Hom_dimension': 4,
                        'inherited_scope': 'B2 complete equivariant Riemann restriction, with low/high Ricci and scalar coordinates; no new character census'},
            'coordinate_order': ['low_Ricci','low_scalar_metric','high_Ricci','high_scalar_metric'],
            'families': families, 'normalized_matrix': [[str(x) for x in row] for row in matrix],
            'rank': rank, 'rref': [[str(x) for x in row] for row in rref],
            'old_outside_rank': 2, 'checks': checks, 'check_count': len(checks),
            'theorem': 'For fixed real linear equivariant S on the full translation tangent, if S(T wedge T) is the unit-weight Euler derivative of (1/3)<T,S(T wedge T)>, then S restricted to algebraic Riemann curvature is zero.',
            'scope': 'All four Riemann coordinates vanish; off-Riemann values of S need not vanish. No Einstein ratio or reconstructed Bianchi criterion is assumed. Fixed metric/epsilon, zero-order linear S and full translation tangent are retained hypotheses.',
            'not_run': ['Old Sage/FLINT/Hom census', 'Full tensor reconstruction', 'New action or physical-domain construction', 'Source necessity or GU verdict', 'Lean compilation'],
            'timing_policy': 'Wall time belongs only in the ephemeral run receipt; this certificate is deterministic.'}


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix+'.new')
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True)+'\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=ROOT)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write-certificate', action='store_true')
    mode.add_argument('--verify', action='store_true')
    parser.add_argument('--certificate', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    repo = args.repo.resolve()
    path = args.certificate or repo/CERT
    actual = build_certificate(repo)
    if args.write_certificate:
        write_json(path, actual)
    else:
        require(json.loads(path.read_text()) == actual, 'exact frozen certificate reconstruction')
    receipt = {'passed': True, 'mode': 'write-certificate' if args.write_certificate else 'verify',
               'probe_sha256': actual['producer_sha256'], 'certificate_sha256': digest(path),
               'certificate_bytes': path.stat().st_size, 'checks': actual['check_count'],
               'rank': actual['rank'], 'normalized_matrix': actual['normalized_matrix'],
               'seconds': time.monotonic()-started}
    if args.output:
        write_json(args.output, receipt)
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
