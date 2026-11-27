#!/usr/bin/env python3
"""Exact on-shell printed-endpoint receiver for the held W2 candidate.

Computes the full first analytic coefficient, then a bounded set of scalar
polynomials with all 59 coordinates and uncertainties. No root search,
inverse construction or full quadratic tensor regeneration is performed.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
import argparse
import hashlib
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = 'lab/process/source-action-endpoint-onshell-certificates.json'
COEFFICIENTS = 'lab/process/source-action-deep-coefficients.json'
DYNAMICS = 'lab/process/source-action-dynamics-and-continuation.json'
GEOMETRY = 'tests/program-focus/source_action_deep_geometry.py'
ALGEBRA = 'tests/program-focus/source_action_deep_algebra.py'
THETA_CERT = 'lab/process/source-action-theta-divergence-certificates.json'
THETA_PROBE = 'tests/program-focus/source_action_theta_divergence_probe.py'
THETA_EVIDENCE = 'lab/process/source-action-theta-divergence.json'
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


def file_sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def form_record(form):
    return [[ext, cliff, str(value)] for (ext, cliff), value in sorted(form.items()) if value]


def coordinate_record(row):
    return {str(j): str(value) for j, value in enumerate(row) if value}


def direct_D(form, geometry, algebra):
    """Antisymmetrize the full covariant derivative, not m-bracket code."""
    rows = algebra.Engine.split_one(form)
    out = {}
    for i, j in combinations(range(14), 2):
        result = algebra.add(geometry.cliff_comm(geometry.spin[i], rows.get(j, {})),
                             algebra.scale(-1, geometry.cliff_comm(geometry.spin[j], rows.get(i, {}))))
        for k in range(14):
            difference = geometry.Lambda[i][j][k]-geometry.Lambda[j][i][k]
            if difference:
                result = algebra.add(result, algebra.scale(-difference, rows.get(k, {})))
        for cliff, value in result.items():
            out[((1 << i) | (1 << j), cliff)] = value
    return out


def build_certificate(repo, progress=False):
    started = time.monotonic()
    def announce(stage, **values):
        if progress:
            print(json.dumps({'stage': stage, 'seconds': round(time.monotonic()-started, 3), **values}),
                  file=sys.stderr, flush=True)
    names = (COEFFICIENTS, DYNAMICS, GEOMETRY, ALGEBRA, THETA_CERT, THETA_PROBE, THETA_EVIDENCE, *REFERENCES)
    inputs = {name: file_sha(repo/name) for name in names}
    data = json.loads((repo/COEFFICIENTS).read_text())
    previous = json.loads((repo/DYNAMICS).read_text())
    theta = json.loads((repo/THETA_CERT).read_text())
    theta_evidence = json.loads((repo/THETA_EVIDENCE).read_text())
    require(theta['final_probe_sha256'] == inputs[THETA_PROBE], 'theta producer custody')
    require(theta_evidence['current_sha256'][THETA_CERT] == inputs[THETA_CERT], 'accepted theta certificate custody')
    for name, digest in theta['native_inputs_sha256'].items():
        require(file_sha(repo/name) == digest, 'theta input custody: '+name)
    for name in (COEFFICIENTS, GEOMETRY, ALGEBRA):
        require(previous['verification']['artifact_sha256'][name] == inputs[name], 'native producer custody: '+name)
    require(previous['verification']['coefficient_sha256'] == inputs[COEFFICIENTS]
            and data['closed'] and data['coefficients_complete'] and data['dimension'] == 59,
            'complete inherited Euler family')
    geometry = load_module(repo/GEOMETRY, 'source_action_deep_geometry')
    algebra = load_module(repo/ALGEBRA, 'source_action_endpoint_owned_algebra')
    engine = algebra.Engine(geometry)
    basis = [{(int(e), int(c)): Q(value) for e, c, value in row} for row in data['basis']]
    n = len(basis)
    require(n == 59 and list(map(Q, data['gram'])) == list(geometry.d), 'full native basis and Gram')
    pivots = [tuple(pivot) for pivot in data['pivots']]
    require(all(B.get(pivot, Q(0)) == int(i == j)
                for i, pivot in enumerate(pivots) for j, B in enumerate(basis)), 'basis independence')
    def expand(coordinates):
        return algebra.add(*[algebra.scale(Q(value), basis[int(j)]) for j, value in coordinates.items()])
    def coordinate_linear(coordinates):
        answer = {}
        for j, value in coordinates.items():
            for k, coefficient in data['K'][str(j)].items():
                answer[int(k)] = answer.get(int(k), Q(0)) + Q(value)*Q(coefficient)
        return algebra.clean(answer)
    def coordinate_bilinear(left, right):
        answer = {}
        for i, a in left.items():
            for j, b in right.items():
                for k, coefficient in data['N'][f'{min(int(i),int(j))},{max(int(i),int(j))}'].items():
                    answer[int(k)] = answer.get(int(k), Q(0)) + Q(a)*Q(b)*Q(coefficient)
        return algebra.clean(answer)
    controls = {}
    def check(name, value):
        controls[name] = bool(value)
        require(value, name)
    source_coords = {int(j): Q(value) for j, value in data['S'].items()}
    source = expand(source_coords)
    check('source_matches_owned_native_Ricci_normalization', source == engine.S_known())
    check('source_matches_actual_native_spin_curvature', source == engine.Phi(engine.curvature()))
    check('source_covariant_D_matches_mbracket_D', direct_D(source, geometry, algebra) == engine.D(source))
    source_D = engine.D(source)
    PS = engine.Phi(source_D)
    check('source_direct_nested_Phi_matches_basis_Phi', PS == engine.star_inverse(engine.shiab(source_D)))
    KS_coords = coordinate_linear(source_coords)
    KS = expand(KS_coords)
    check('native_KS_matches_inherited_table', engine.K(source) == KS)
    C1 = algebra.add(KS, algebra.scale(-1, PS))
    branch = [{'order': 1, 'coefficient': form_record(C1)}]
    C2 = None
    if not C1:
        # Use the E-eliminated defect: original kappa*T needs T3 to
        # evaluate its h2 coefficient. No incomplete substitution is used.
        PKS = engine.Phi(engine.D(KS))
        KKS = expand(coordinate_linear(KS_coords))
        NSS = expand(coordinate_bilinear(source_coords, source_coords))
        source_square = engine.wedge(source, source)
        PhiSS = engine.Phi(source_square)
        check('PKS_matches_direct_nested_Phi', PKS == engine.star_inverse(engine.shiab(engine.D(KS))))
        check('native_KKS_matches_inherited_table', KKS == engine.K(KS))
        check('native_NSS_matches_inherited_table', NSS == engine.N_diag(source))
        check('source_square_direct_nested_Phi', PhiSS == engine.star_inverse(engine.shiab(source_square)))
        C2 = algebra.add(PKS, algebra.scale(-1, KKS), PhiSS,
                         algebra.scale(-1, NSS))
        branch.append({'order': 2, 'coefficient': form_record(C2)})
    first_nonzero = C1 if C1 else C2
    if first_nonzero:
        horizontal = {key: value for key, value in first_nonzero.items() if key[0] < (1 << 4)}
        chosen = horizontal or first_nonzero
        witness = min(chosen, key=lambda key: (key[1].bit_count(), key[0], key[1]))
        witnesses = [('first_nonzero_analytic_component', witness)]
    else:
        # Predeclared bounded fallback: source's three coordinate receivers,
        # the single KS coordinate, and the old off-shell Helmholtz receiver.
        # Zero is a valid outcome. This is not a census or an equality proof.
        witnesses = [('source_pivot_'+str(j), pivots[j]) for j in (0, 1, 2)]
        witnesses += [('KS_pivot_4', pivots[4]), ('old_offshell_helmholtz_component', (2, 3))]
    announce('analytic_coefficients', full_C1_support=len(C1),
             full_C2_support=None if C2 is None else len(C2), receiver_count=len(witnesses))
    D_basis = []
    for j, B in enumerate(basis):
        DB = engine.D(B)
        check('D_covariant_column_'+str(j), DB == direct_D(B, geometry, algebra))
        D_basis.append(DB)
    certified_roots = []
    for root in data['certified_roots']:
        certificate = algebra.certificate_for(data, root)
        keys = ('e', 'a', 'b', 'radius', 'ball_image_bound', 'lipschitz_bound')
        require(certificate['status'] == 'exact_local_root_certified' and Q(certificate['kappa']) == 1,
                'native root certificate')
        require(all(certificate[key] == root['certificate'][key] for key in keys), 'native certificate readback')
        certified_roots.append((root, certificate))
    def direct_defect(form):
        return algebra.add(engine.Phi(engine.D(form)), algebra.scale(-1, engine.K(form)),
                           engine.Phi(engine.wedge(form, form)), algebra.scale(-1, engine.N_diag(form)))
    records = []
    for label, witness in witnesses:
        row_started = time.monotonic()
        Z = {witness: Q(1)}
        weight = engine.weight(*witness)
        require(weight != 0, 'nondegenerate native receiver weight')
        H = algebra.scale(1/weight, engine.Phi_adj(Z))
        basis_receiver = [B.get(witness, Q(0)) for B in basis]
        linear = []
        for j, DB in enumerate(D_basis):
            inherited = sum(Q(value)*basis_receiver[int(k)] for k, value in data['K'][str(j)].items())
            linear.append(engine.pair(H, DB)-inherited)
        raw_quadratic = [[Q(0) for j in range(n)] for i in range(n)]
        quadratic = [[Q(0) for j in range(n)] for i in range(n)]
        for i, B in enumerate(basis):
            adjoint_image = engine.left_wedge_adj(B, H, 'comm')
            for j, other in enumerate(basis):
                raw_quadratic[i][j] = engine.pair(other, adjoint_image)/2
                inherited = sum(Q(value)*basis_receiver[int(k)]
                                for k, value in data['N'][f'{min(i,j)},{max(i,j)}'].items())
                quadratic[i][j] = raw_quadratic[i][j]-inherited
        check(label+'_raw_quadratic_symmetric', raw_quadratic == list(map(list, zip(*raw_quadratic))))
        check(label+'_defect_quadratic_symmetric', quadratic == list(map(list, zip(*quadratic))))
        def evaluate(x):
            return sum(a*b for a, b in zip(linear, x)) + sum(
                quadratic[i][j]*x[i]*x[j] for i in range(n) for j in range(n))
        nonzero_pairs = [(i, j) for i in range(n) for j in range(i, n) if raw_quadratic[i][j]]
        selected_pairs = sorted(nonzero_pairs, key=lambda ij: (len(basis[ij[0]])+len(basis[ij[1]]), ij))[:2]
        # A mathematically zero receiver still gets independent direct tests.
        if not selected_pairs:
            selected_pairs = [(0, 1), (0, 2)]
        direct_controls = []
        for i, j in selected_pairs:
            W = engine.wedge(basis[i], basis[j], 'comm')
            direct = engine.Phi(W).get(witness, Q(0))/2
            check(f'{label}_direct_Phi_pair_{i}_{j}', direct == raw_quadratic[i][j])
            check(f'{label}_direct_nested_Phi_pair_{i}_{j}', engine.Phi(W) == engine.star_inverse(engine.shiab(W)))
            check(f'{label}_pointwise_Phi_adjoint_pair_{i}_{j}', engine.pair(H, W)/2 == direct)
            inherited_N = sum(Q(value)*basis_receiver[int(k)] for k, value in data['N'][f'{i},{j}'].items())
            check(f'{label}_native_N_pair_{i}_{j}', engine.N(basis[i], basis[j]).get(witness, Q(0)) == inherited_N)
            x = [Q(0)]*n
            x[i] += Q(2)
            x[j] += Q(-3)
            form = expand({k: value for k, value in enumerate(x) if value})
            check(f'{label}_direct_full_defect_fixture_{i}_{j}', direct_defect(form).get(witness, Q(0)) == evaluate(x))
            direct_controls.append({'basis_indices': [i, j], 'raw_symmetric_coefficient': str(direct),
                                    'direct_defect_fixture': str(evaluate(x))})
        source_vector = [source_coords.get(i, Q(0)) for i in range(n)]
        check(label+'_linear_polynomial_matches_C1', -sum(a*b for a, b in zip(linear, source_vector)) == C1.get(witness, Q(0)))
        if C2 is not None:
            KS_vector = [KS_coords.get(i, Q(0)) for i in range(n)]
            coefficient = sum(a*b for a, b in zip(linear, KS_vector)) + sum(
                quadratic[i][j]*source_vector[i]*source_vector[j] for i in range(n) for j in range(n))
            check(label+'_quadratic_polynomial_matches_C2', coefficient == C2.get(witness, Q(0)))
        roots = []
        for root, certificate in certified_roots:
            x = list(map(Q, root['coordinates']))
            radius = Q(certificate['radius'])
            center = evaluate(x)
            gradient = [linear[i]+2*sum(quadratic[i][j]*x[j] for j in range(n)) for i in range(n)]
            gradient_norm = sum(map(abs, gradient))
            quadratic_norm = sum(abs(value) for row in quadratic for value in row)
            error = radius*gradient_norm+radius*radius*quadratic_norm
            lower, upper = center-error, center+error
            roots.append({'id': root['id'], 'root_record_sha256': canonical_hash(root),
                          'contraction': {key: certificate[key] for key in keys},
                          'center': str(center), 'gradient_one_norm': str(gradient_norm),
                          'quadratic_entry_one_norm': str(quadratic_norm), 'error_bound': str(error),
                          'lower': str(lower), 'upper': str(upper), 'excludes_zero': lower > 0 or upper < 0,
                          'display': {'center': float(center), 'error': float(error)}})
            announce('root_receiver', receiver=label, root=root['id'], center=float(center), error=float(error),
                     excludes_zero=lower > 0 or upper < 0)
        polynomial = {'linear': coordinate_record(linear),
                      'symmetric_quadratic_upper': {f'{i},{j}': str(quadratic[i][j])
                          for i in range(n) for j in range(i,n) if quadratic[i][j]},
                      'convention': 'c.x+sum_i Qii xi^2+2 sum_i<j Qij xi xj; all59 coordinates retained.',
                      'raw_quadratic_upper_sha256': canonical_hash({f'{i},{j}': str(raw_quadratic[i][j])
                          for i in range(n) for j in range(i,n) if raw_quadratic[i][j]})}
        horizontal = witness[0] < 16
        receiver_record = {'id': label, 'exterior_mask': witness[0], 'Clifford_mask': witness[1],
                          'native_coordinate_weight': str(weight), 'dual_form': form_record(H),
                          'horizontal': horizontal, 'branch_coefficients': {str(row['order']):
                              str(dict(((e,c), Q(v)) for e,c,v in row['coefficient']).get(witness, Q(0)))
                              for row in branch},
                          'literal_section_receiver': 'same coefficient with full ambient adjoint fibre' if horizontal else 'killed by flat-section pullback',
                          'optional_4D_index_raise': str(1/geometry.d[witness[0].bit_length()-1]) if horizontal else None,
                          'polynomial': polynomial, 'direct_native_controls': direct_controls, 'roots': roots}
        records.append(receiver_record)
        announce('receiver_complete', receiver=label, receiver_seconds=round(time.monotonic()-row_started, 3),
                 linear_nonzero=sum(bool(v) for v in linear),
                 quadratic_nonzero=len(polynomial['symmetric_quadratic_upper']))
    root_summary = []
    for root, certificate in certified_roots:
        nonzero = [record['id'] for record in records if next(row for row in record['roots'] if row['id'] == root['id'])['excludes_zero']]
        horizontal_nonzero = [record['id'] for record in records if record['horizontal'] and record['id'] in nonzero]
        root_summary.append({'id': root['id'], 'certified_nonzero_receivers': nonzero,
                             'certified_nonzero_horizontal_receivers': horizontal_nonzero,
                             'endpoint_failure_certified': bool(nonzero),
                             'literal_section_failure_certified': bool(horizontal_nonzero)})
    return {'schema': 'gu-endpoint-onshell-certificate-v1', 'data_only': True,
            'final_probe_sha256': file_sha(Path(__file__).resolve()), 'native_inputs_sha256': inputs,
            'formula': {'E': 'kappa T+S+K T+N(T,T)',
                        'R_print': 'kappa T+S+Phi(D_B T)+Phi(T wedge T)',
                        'on_shell_defect': '(Phi D_B-K)T+Phi(T wedge T)-N(T,T)',
                        'receiver_adjoint': 'H=Phi^dagger Z/wZ; raw_Qij=<Bj,Q_Bi^dagger H>/2.',
                        'root_error': 'r||c+2Q x0||1+r^2 sum_ij|Qij|'},
            'carrier': theta['carrier'], 'stationarity_scope': theta['stationarity_scope'],
            'carrier_custody': 'The complete-carrier membership, reality, character dimension and recursive-generation proof are inherited from the authenticated published theta certificate. This execution rechecks basis pivots and Gram; it does not rerun the isotropy census or full K/N construction.',
            'analytic_branch': {'coefficients': branch,
                'computed_via_E_eliminated_defect': True,
                'no_incomplete_original_residual_substitution': True,
                'status': 'nonzero_coefficient' if first_nonzero else 'full_ambient_compatibility_through_h2',
                'scope': 'The full computed coefficients are exact. Zero through h2 does not prove endpoint equality; a nonzero coefficient of the owned convergent branch would exclude it for sufficiently small positive h. No h3 test, numerical radius or path to either kappa1 root.'},
            'observation': 'Compute ambient R_print=*G^-1 Upsilon first, then literal one-form pullback to the flat section. All ambient adjoint components are retained. The degree13 Upsilon is not pulled back.',
            'receiver_selection': 'First nonzero branch component if present; otherwise the predeclared source pivots0/1/2, KS pivot4 and old off-shell horizontal component(2,3). No adaptive receiver census.',
            'receivers': records, 'controls': controls, 'root_summary': root_summary,
            'source_scope': 'Fixed W2/K95 realization and declared source-shaped SC-ACT01/02, WGS01 dictionary. The source does not uniquely select this glyph/product completion or physical observation/domain. No source/GU/canon verdict.',
            'not_run': ['New root search or inverse construction', 'Full native K/N tensor regeneration',
                        'Physical stress or cosmology calculation', 'Unselected h3 or higher analytic test', 'Lean compilation']}


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
    started = time.monotonic()
    repo = args.repo.resolve()
    path = args.certificate or repo/CERTIFICATE
    actual = build_certificate(repo, args.progress)
    if args.write_certificate:
        write_json(path, actual)
    else:
        require(json.loads(path.read_text()) == actual, 'frozen exact native certificate equality')
    receipt = {'passed': True, 'mode': 'write-certificate' if args.write_certificate else 'verify',
               'probe_sha256': actual['final_probe_sha256'], 'certificate_sha256': file_sha(path),
               'seconds': time.monotonic()-started, 'native_D_columns_recomputed_twice': 59,
               'quadratic_receiver_adjoint_images': 59*len(actual['receivers']),
               'root_certificates_recomputed': len(actual['root_summary']),
               'receiver_count': len(actual['receivers']), 'branch_status': actual['analytic_branch']['status'],
               'root_summary': actual['root_summary']}
    if args.output:
        write_json(args.output, receipt)
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
