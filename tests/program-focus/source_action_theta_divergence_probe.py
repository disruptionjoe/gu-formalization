#!/usr/bin/env python3
"""Exact 1-form coderivative on the published W2 homogeneous 59-family.

Rebuilds the map from native geometry by two different formulas, computes
its kernel, and propagates the existing exact root certificates.  It does
not construct an inverse, search roots, or infer a source/physical verdict.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = 'lab/process/source-action-theta-divergence-certificates.json'
COEFFICIENTS = 'lab/process/source-action-deep-coefficients.json'
PRIOR = 'lab/process/source-action-dynamics-and-continuation.json'
GEOMETRY = 'tests/program-focus/source_action_deep_geometry.py'
ALGEBRA = 'tests/program-focus/source_action_deep_algebra.py'
REFERENCES = (
    'explorations/conditional-build/source-action-external-datum-candidate-2026-11-25.md',
    'explorations/conditional-build/source-action-wave2-construction-2026-11-25.md',
    'explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md',
    'explorations/conditional-build/source-action-dynamics-and-continuation-2026-11-25.md',
    'lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md',
    'lab/sources/source-claim-register.yaml',
)


def require(value, message):
    if not value:
        raise ValueError(message)


def sha_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def sha_file(path):
    return sha_bytes(path.read_bytes())


def canonical_hash(value):
    return sha_bytes(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())


def clean(row):
    return {key: value for key, value in row.items() if value}


def accumulate(target, row, factor=Q(1)):
    for key, value in row.items():
        target[key] = target.get(key, Q(0)) + factor * value


def record(row):
    return {str(key): str(value) for key, value in sorted(row.items()) if value}


def split_one(form):
    result = [{} for unused in range(14)]
    for (ext, cliff), value in form.items():
        require(ext > 0 and ext.bit_count() == 1, 'one-form input')
        result[ext.bit_length()-1][cliff] = value
    return result


def coderivative_covariant(form, geometry):
    """-g^ij nabla_i T_j, including the covector-slot connection."""
    rows = split_one(form)
    result = {}
    for i, metric in enumerate(geometry.d):
        accumulate(result, geometry.cliff_comm(geometry.spin[i], rows[i]), -1/metric)
        for k, value in enumerate(geometry.Lambda[i][i]):
            if value:
                accumulate(result, rows[k], value/metric)
    return clean(result)


def coderivative_weak(form, geometry, engine, omit_divergence=False):
    """Formal density adjoint of 0->1 D_B using native trace weights.

    The commutator block is transposed coefficientwise, with the actual
    indefinite pairing ratio; the derivative contributes -div(e_i)/d_i.
    This does not transpose the invariant exterior-D matrix.
    """
    result = {}
    for (ext, out_cliff), value in form.items():
        i = ext.bit_length()-1
        for beta_cliff, beta_value in geometry.spin[i].items():
            in_cliff = beta_cliff ^ out_cliff
            out1, left = engine.cmul(beta_cliff, in_cliff)
            out2, right = engine.cmul(in_cliff, beta_cliff)
            require(out1 == out2 == out_cliff, 'commutator transpose target')
            coefficient = beta_value * (left-right)
            coefficient *= engine.weight(ext, out_cliff)/engine.weight(0, in_cliff)
            result[in_cliff] = result.get(in_cliff, Q(0)) + coefficient*value
        if not omit_divergence:
            divergence = sum(geometry.Lambda[j][i][j] for j in range(14))
            result[out_cliff] = result.get(out_cliff, Q(0)) - divergence*value/geometry.d[i]
    return clean(result)


def coderivative_observed(form, geometry):
    """Literal flat-section pullback, retaining all ambient endomorphisms.

    The observed form index has four-dimensional LC=0; the retained spinor
    connection is B_h+T_h, not four-dimensional spin LC. Its T_h commutator
    with the same T_h contracts to zero.
    """
    rows = split_one(form)
    result = {}
    for i in range(4):
        accumulate(result, geometry.cliff_comm(geometry.spin[i], rows[i]), -1/geometry.d[i])
    return clean(result)


def rref_and_kernel(columns):
    masks = sorted({mask for column in columns for mask in column})
    matrix = [[column.get(mask, Q(0)) for column in columns] for mask in masks]
    rows = [row[:] for row in matrix]
    pivots = []
    for col in range(len(columns)):
        pivot = next((i for i in range(len(pivots), len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        index = len(pivots)
        rows[index], rows[pivot] = rows[pivot], rows[index]
        factor = rows[index][col]
        rows[index] = [value/factor for value in rows[index]]
        for i, row in enumerate(rows):
            if i != index and row[col]:
                factor = row[col]
                rows[i] = [a-factor*b for a, b in zip(row, rows[index])]
        pivots.append(col)
    require(all(not any(row) for row in rows[len(pivots):]), 'exact row rank')
    free = [j for j in range(len(columns)) if j not in pivots]
    kernel = []
    for col in free:
        vector = {col: Q(1)}
        for i, pivot in enumerate(pivots):
            if rows[i][col]:
                vector[pivot] = -rows[i][col]
        require(all(sum(row[j]*v for j, v in vector.items()) == 0 for row in matrix),
                'kernel vector in original map')
        kernel.append(vector)
    # The distinct free coordinates give independent vectors. RREF proves
    # that they span every solution, not merely a selected zero subspace.
    return masks, matrix, rows[:len(pivots)], pivots, free, kernel


def apply_coordinates(columns, coordinates):
    result = {}
    for key, value in coordinates.items():
        accumulate(result, columns[int(key)], Q(value))
    return clean(result)


def composed_euler_maps(data, columns):
    source = apply_coordinates(columns, data['S'])
    linear = {key: apply_coordinates(columns, value) for key, value in data['K'].items()}
    quadratic = {key: apply_coordinates(columns, value) for key, value in data['N'].items()}
    linear_record = {key: record(value) for key, value in linear.items() if value}
    quadratic_record = {key: record(value) for key, value in quadratic.items() if value}
    def witness(rows):
        for key, row in rows.items():
            if row:
                mask = min(row, key=lambda c: (c.bit_count(), c))
                return {'input': key, 'Clifford_mask': mask, 'value': str(row[mask])}
        return None
    return {
        'D_S': record(source),
        'D_K_nonzero_column_count': len(linear_record),
        'D_K_nonzero_columns_sha256': canonical_hash(linear_record),
        'D_K_witness': witness(linear),
        'D_N_nonzero_pair_count': len(quadratic_record),
        'D_N_nonzero_pairs_sha256': canonical_hash(quadratic_record),
        'D_N_witness': witness(quadratic),
        'gamma4_linear_row': {key: str(row[16]) for key, row in linear.items() if row.get(16)},
        'gamma4_symmetric_quadratic_row': {key: str(row[16]) for key, row in quadratic.items() if row.get(16)},
        'linear_columns_checked': len(linear),
        'symmetric_pairs_checked': len(quadratic),
        'all_three_compositions_zero': not source and not any(linear.values()) and not any(quadratic.values()),
        'meaning': 'Exact composition with inherited complete Euler coefficients, not new full-tensor K/N reconstruction. D(F_kappa(t))=kappa*D(t)+D(S)+D(K)t+D(N)(t,t).',
    }


def branch_coefficients(data, columns, observed_columns):
    def linear(vector):
        answer = {}
        for j, value in vector.items():
            accumulate(answer, {int(k): Q(v) for k, v in data['K'][str(j)].items()}, value)
        return clean(answer)
    def bilinear(left, right):
        answer = {}
        for i, value in left.items():
            for j, other in right.items():
                row = data['N'][f'{min(i,j)},{max(i,j)}']
                accumulate(answer, {int(k): Q(v) for k, v in row.items()}, value*other)
        return clean(answer)
    coefficients = [{int(k): -Q(v) for k, v in data['S'].items()}]
    records = []
    first_nonzero = None
    first_observed = None
    for order in range(1, 5):
        if order > 1:
            answer = {}
            accumulate(answer, linear(coefficients[-1]), Q(-1))
            for i in range(1, order-1):
                accumulate(answer, bilinear(coefficients[i-1], coefficients[order-i-2]), Q(-1))
            coefficients.append(clean(answer))
        coefficient = coefficients[-1]
        divergence = apply_coordinates(columns, coefficient)
        observed = apply_coordinates(observed_columns, coefficient)
        records.append({'order': order, 'T_coordinates': record(coefficient),
                        'ambient_divergence': record(divergence), 'observed_divergence': record(observed)})
        def leading(row):
            mask = min(row, key=lambda c: (c.bit_count(), c))
            return {'order': order, 'Clifford_mask': mask, 'coefficient': str(row[mask])}
        if observed and first_observed is None:
            first_observed = leading(observed)
        if divergence:
            first_nonzero = leading(divergence)
            break
    return {'recurrence': 'T1=-S; Tn=-K*T_(n-1)-sum_(i+j=n-1,i,j>=1) N(Ti,Tj).',
            'maximum_order_budget': 4, 'computed_through_order': len(records),
            'coefficients': records, 'first_nonzero_ambient': first_nonzero,
            'first_nonzero_observed': first_observed,
            'analytic_scope': 'The existing homogeneous small-h theorem proves convergence of this unique branch at fixed geometry and zero matter. A first nonzero finite coefficient proves nonzero receiver for all sufficiently small positive h, with no numerical radius or connection to either kappa1 root inferred.'}


def interval_record(center, error):
    lower, upper = center-error, center+error
    return {'center': str(center), 'error_bound': str(error), 'lower': str(lower), 'upper': str(upper),
            'excludes_zero': lower > 0 or upper < 0,
            'display': {'center': float(center), 'error': float(error)}}


def root_readback(data, columns, masks, matrix, observed_masks, observed_matrix, algebra):
    roots = []
    for root in data['certified_roots']:
        # Recompute the inherited contraction inequalities from the published
        # polynomial, center and approximate inverse. No inverse is built.
        certificate = algebra.certificate_for(data, root)
        keys = ('e', 'a', 'b', 'radius', 'ball_image_bound', 'lipschitz_bound')
        require(certificate['status'] == 'exact_local_root_certified', 'native root existence')
        require(all(certificate[key] == root['certificate'][key] for key in keys), 'native root certificate equality')
        require(Q(certificate['kappa']) == 1, 'held normalization')
        x = list(map(Q, root['coordinates']))
        radius = Q(certificate['radius'])
        receivers = {}
        for mask, row in zip(masks, matrix):
            center = sum(a*b for a, b in zip(row, x))
            error = radius*sum(map(abs, row))
            receivers[str(mask)] = interval_record(center, error)
        nonzero = [mask for mask, value in receivers.items() if value['excludes_zero']]
        observed = {}
        for mask, row in zip(observed_masks, observed_matrix):
            center = sum(a*b for a, b in zip(row, x))
            error = radius*sum(map(abs, row))
            observed[str(mask)] = interval_record(center, error)
        observed_nonzero = [mask for mask, value in observed.items() if value['excludes_zero']]
        def selected(rows, nonzero):
            if not rows:
                return {}
            key = min(nonzero or rows, key=lambda c: (int(c).bit_count(), int(c)))
            return {key: rows[key]}
        roots.append({'id': root['id'], 'root_record_sha256': canonical_hash(root),
                      'native_root_contraction_recomputed': True,
                      'contraction': {key: certificate[key] for key in keys},
                      'receivers': selected(receivers, nonzero),
                      'all_receiver_bounds_sha256': canonical_hash(receivers),
                      'receivers_checked': len(receivers), 'nonzero_receiver_count': len(nonzero),
                      'divergence_certified_nonzero': bool(nonzero),
                      'observed_receivers': selected(observed, observed_nonzero),
                      'all_observed_receiver_bounds_sha256': canonical_hash(observed),
                      'observed_receivers_checked': len(observed),
                      'observed_nonzero_receiver_count': len(observed_nonzero),
                      'observed_divergence_certified_nonzero': bool(observed_nonzero),
                      'all_receivers_exact_center_zero': all(Q(value['center']) == 0 for value in receivers.values())})
    return roots


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def build_certificate(repo, progress=False):
    tick = time.monotonic()
    def announce(stage, **values):
        if progress:
            print(json.dumps({'stage': stage, 'seconds': round(time.monotonic()-tick, 3), **values}), file=sys.stderr, flush=True)
    inputs = {name: sha_file(repo/name) for name in (COEFFICIENTS, PRIOR, GEOMETRY, ALGEBRA, *REFERENCES)}
    data = json.loads((repo/COEFFICIENTS).read_text())
    prior = json.loads((repo/PRIOR).read_text())
    old = prior['verification']
    require(old['coefficient_sha256'] == inputs[COEFFICIENTS], 'published coefficient custody')
    for name in (COEFFICIENTS, GEOMETRY, ALGEBRA):
        require(old['artifact_sha256'][name] == inputs[name], 'published producer custody: '+name)
    require(old['native_probe']['all_passed'] and data['dimension'] == 59
            and data['closed'] and data['coefficients_complete'], 'inherited full-family certificate')
    character = old['native_probe']['results']['reflection']
    require(character['passed'] and character['real_fixed_total'] == 59
            and sum(character['real_fixed_degree_dimensions'].values()) == 59,
            'published independent character upper bound')
    require({str(grade): data['basis_grades'].count(grade) for grade in set(data['basis_grades'])}
            == character['real_fixed_degree_dimensions'], 'grade-by-grade carrier completeness')
    geometry = load_module(repo/GEOMETRY, 'source_action_deep_geometry')
    algebra = load_module(repo/ALGEBRA, 'source_action_theta_owned_algebra')
    engine = algebra.Engine(geometry)
    basis = [{(int(e), int(c)): Q(value) for e, c, value in row} for row in data['basis']]
    require(list(map(Q, data['gram'])) == list(geometry.d), 'native Gram binding')
    require(len(basis) == 59 and len(data['pivots']) == 59, 'whole carrier dimensions')
    pivots = [tuple(pivot) for pivot in data['pivots']]
    require(all(B.get(pivot, Q(0)) == int(i == j)
                for i, pivot in enumerate(pivots) for j, B in enumerate(basis)), 'independent published basis')
    verifier = algebra.Span(engine, max_dimension=59)
    for B in basis:
        verifier.verify_invariant(B)
    flip = sum(1 << i for i in (0, 8, 9, 10))
    require(all(engine.real_skew(B) and all(((e ^ c) & flip).bit_count() % 2 == 0 for e, c in B)
                for B in basis), 'native reality/reflection membership')
    generation = algebra.verify_generation(data)
    controls = {}
    def check(name, value):
        controls[name] = bool(value)
        require(value, name)
    check('native_metric_compatibility', all(geometry.d[k]*geometry.Lambda[i][j][k]
          + geometry.d[j]*geometry.Lambda[i][k][j] == 0
          for i in range(14) for j in range(14) for k in range(14)))
    check('native_spin_Clifford_compatibility', all(
          geometry.cliff_comm(geometry.spin[i], {1 << j: Q(1)})
          == {1 << k: value for k, value in enumerate(geometry.Lambda[i][j]) if value}
          for i in range(14) for j in range(14)))
    check('trace_frame_divergence_minus4', sum(geometry.Lambda[j][4][j] for j in range(14)) == -4)
    check('trace_reference_spin_zero', geometry.spin[4] == {})
    check('all_vertical_reference_spin_zero', all(not row for row in geometry.spin[4:]))
    contracted_form_connection = [sum(geometry.Lambda[i][i][k]/geometry.d[i] for i in range(14))
                                 for k in range(14)]
    check('contracted_form_connection_only_trace', contracted_form_connection
          == [Q(-1, 4) if k == 4 else Q(0) for k in range(14)])
    phi1 = {(1 << i, 1 << i): Q(1) for i in range(14)}
    trace_identity = {(1 << 4, 0): Q(1)}
    check('parallel_Phi1_covariant_zero', coderivative_covariant(phi1, geometry) == {})
    check('parallel_Phi1_weak_zero', coderivative_weak(phi1, geometry, engine) == {})
    check('scalar_trace_minus_one_quarter', coderivative_covariant(trace_identity, geometry) == {0: Q(-1, 4)})
    check('scalar_trace_weak_minus_one_quarter', coderivative_weak(trace_identity, geometry, engine) == {0: Q(-1, 4)})
    check('scalar_trace_observed_zero', coderivative_observed(trace_identity, geometry) == {})
    check('parallel_Phi1_observed_gamma4_over4', coderivative_observed(phi1, geometry) == {1 << 4: Q(1, 4)})
    check('omitted_divergence_mutation_detected', coderivative_weak(trace_identity, geometry, engine, True) == {})
    # i*Id is H-skew although Id is not. The real-coefficient test above
    # extends complex linearly; no imaginary component enters the 59-family.
    def blade_sharp(cliff, gaussian_coefficient):
        degree = cliff.bit_count()
        sign = (-1)**(degree*(degree+1)//2)
        real, imag = gaussian_coefficient
        return sign*real, -sign*imag
    imaginary_unit = (Q(0), Q(1))
    check('i_identity_is_native_u', blade_sharp(0, imaginary_unit)
          == tuple(-value for value in imaginary_unit))
    columns, observed_columns = [], []
    for j, B in enumerate(basis):
        first = coderivative_covariant(B, geometry)
        second = coderivative_weak(B, geometry, engine)
        require(first == second, 'two coderivative methods: '+str(j))
        columns.append(first)
        observed = coderivative_observed(B, geometry)
        difference = dict(observed)
        accumulate(difference, first, Q(-1))
        trace_component = split_one(B)[4]
        require(clean(difference) == {mask: value/4 for mask, value in trace_component.items()},
                'literal observation defect T4/4: '+str(j))
        observed_columns.append(observed)
    masks, matrix, reduced, pivot_columns, free, kernel = rref_and_kernel(columns)
    obs_masks, obs_matrix, obs_reduced, obs_pivots, obs_free, obs_kernel = rref_and_kernel(observed_columns)
    compositions = composed_euler_maps(data, columns)
    announce('map_complete', rank=len(pivot_columns), kernel_dimension=len(free), output_masks=len(masks),
             observed_rank=len(obs_pivots), observed_kernel_dimension=len(obs_free),
             D_S_zero=not compositions['D_S'], D_K_nonzero=compositions['D_K_nonzero_column_count'],
             D_N_nonzero=compositions['D_N_nonzero_pair_count'])
    branch = branch_coefficients(data, columns, observed_columns)
    announce('analytic_branch_coefficients', ambient=branch['first_nonzero_ambient'],
             observed=branch['first_nonzero_observed'], through_order=branch['computed_through_order'])
    # Symmetric contraction kills the shift [T_i,T_j] as a polynomial,
    # independently of diagonalization or the homogeneous family.
    check('symmetric_connection_shift_cancels', all(
          geometry.cliff_comm({1 << i: Q(1)}, {1 << j: Q(1)})
          == {key: -value for key, value in geometry.cliff_comm({1 << j: Q(1)}, {1 << i: Q(1)}).items()}
          for i in range(14) for j in range(14)))
    roots = root_readback(data, columns, masks, matrix, obs_masks, obs_matrix, algebra)
    announce('root_bounds_complete', roots=[{'id': r['id'], 'nonzero': r['divergence_certified_nonzero'],
                                           'observed_nonzero': r['observed_divergence_certified_nonzero'],
                                           'receivers': r['nonzero_receiver_count']} for r in roots])
    return {
        'schema': 'gu-theta-divergence-certificate-v1', 'data_only': True,
        'final_probe_sha256': sha_file(Path(__file__).resolve()),
        'native_inputs_sha256': inputs,
        'formula': {
            'coderivative': 'D_B^dagger T=-sum_i (1/d_i)([beta_i,T_i]-sum_k Lambda[i][i][k]*T_k) for invariant coefficients.',
            'weak_formula': 'Transpose [beta_i,.] with native trace/form weights and add -div(e_i)*T_i/d_i. Derivatives of invariant coefficients vanish; frame divergence does not.',
            'connection_shift': 'D_(B+fT)^dagger T-D_B^dagger T=-f G^ij[T_i,T_j]=0 by symmetry of G^ij and antisymmetry of the bracket, for arbitrary smooth T and real scalar f(x). There is no derivative of f in this connection difference.',
            'scalar_native_control': 'D_B^dagger(i theta4 Id)=-i Id/4. Rational Id computation is complexified; iId is native H-skew.',
            'literal_observation': 'At the flat section with induced4D LC=0 and the full ambient adjoint bundle retained, D_(s*Ahat)^dagger(s*T)=-sum_h<4 [beta_h,T_h]/d_h.',
            'descent_defect': 'For every invariant one-form, D_B^dagger(T)=D_(s*Ahat)^dagger(s*T)-T_4/4. Geometry proves the formula before restriction to the real/reflection59 family. It is not an observed Einstein-stress divergence.',
            'Phi1_control_scope': 'The ambient-conserved but observed-nonconserved Phi1 control is an off-shell field; it is not asserted to be a stationary connection.',
        },
        'carrier': {'dimension': 59, 'field': 'real reflection-fixed connected-Lorentz invariant W2 family',
                    'basis_pivots_independent': True, 'all_six_isotropy_generators_checked': True,
                    'reality_reflection_checked': True, 'generation': generation,
                    'completeness': 'Published independent character dimension59 plus checked membership, pivots and recursive generated-rank witness. No new full-tensor Euler construction.'},
        'controls': controls,
        'divergence_map': {'columns': [record(column) for column in columns],
                           'output_Clifford_masks': masks, 'rank': len(pivot_columns),
                           'kernel_dimension': len(free), 'pivot_columns': pivot_columns,
                           'free_columns': free, 'rref_rows': [[str(v) for v in row] for row in reduced],
                           'kernel_basis': [record(vector) for vector in kernel],
                           'two_independent_formulas_equal_on_all_columns': True},
        'literal_observed_map': {'columns': [record(column) for column in observed_columns],
                                 'output_Clifford_masks': obs_masks, 'rank': len(obs_pivots),
                                 'kernel_dimension': len(obs_free), 'pivot_columns': obs_pivots,
                                 'free_columns': obs_free, 'rref_rows': [[str(v) for v in row] for row in obs_reduced],
                                 'kernel_basis': [record(vector) for vector in obs_kernel],
                                 'all_ambient_endomorphism_components_retained': True,
                                 'trace_defect_checked_on_all_columns': True},
        'Euler_compositions': compositions,
        'small_h_branch': branch,
        'roots': roots,
        'stationarity_scope': prior['results']['coupled_stationarity'],
        'scope': 'Exact actual-candidate ambient coderivative, whole homogeneous59 map and certified stationary-root receiver bounds. No source/canon/GU verdict, observed stress descent, physical domain or full variable-field conservation theorem.',
        'not_run': ['Full native K/N tensor regeneration', 'New inverse or root search', 'Fibre integration or cosmological evolution', 'Lean compilation'],
    }


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
    parser.add_argument('--progress', action='store_true')
    args = parser.parse_args()
    tick = time.monotonic()
    repo = args.repo.resolve()
    path = args.certificate or repo/CERTIFICATE
    actual = build_certificate(repo, args.progress)
    if args.write_certificate:
        write_json(path, actual)
    else:
        require(json.loads(path.read_text()) == actual, 'frozen certificate equality after exact recomputation')
    receipt = {'passed': True, 'mode': 'write-certificate' if args.write_certificate else 'verify',
               'probe_sha256': actual['final_probe_sha256'], 'certificate_sha256': sha_file(path),
               'seconds': time.monotonic()-tick, 'basis_columns_recomputed_twice': 59,
               'rank': actual['divergence_map']['rank'], 'kernel_dimension': actual['divergence_map']['kernel_dimension'],
               'root_contraction_certificates_recomputed': len(actual['roots']),
               'root_divergence_nonzero': [root['divergence_certified_nonzero'] for root in actual['roots']],
               'observed_rank': actual['literal_observed_map']['rank'],
               'observed_kernel_dimension': actual['literal_observed_map']['kernel_dimension'],
               'root_observed_divergence_nonzero': [root['observed_divergence_certified_nonzero'] for root in actual['roots']],
               'D_S_zero': not actual['Euler_compositions']['D_S'],
               'D_K_nonzero_columns': actual['Euler_compositions']['D_K_nonzero_column_count'],
               'D_N_nonzero_pairs': actual['Euler_compositions']['D_N_nonzero_pair_count'],
               'small_h_ambient_leading': actual['small_h_branch']['first_nonzero_ambient'],
               'small_h_observed_leading': actual['small_h_branch']['first_nonzero_observed']}
    if args.output:
        write_json(args.output, receipt)
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
