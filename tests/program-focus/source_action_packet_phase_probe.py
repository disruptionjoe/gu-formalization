#!/usr/bin/env python3
"""Light exact proof-input controls for the matched packet/source phase audit.

No native graph, inverse, current, packet or PDE calculation is regenerated.
The selected-jet raw records are authenticated; their small exact Gram bound
is recomputed. Analytic packet estimates and source uniformity are written
proof obligations, not consequences of the finite controls in this file.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import ast
import base64
import hashlib
import importlib.util
import json
import re
import sys
import time
import zlib

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
BUNDLE = 'lab/process/source-action-packet-phase-certificates.json'
SELECTED = 'lab/process/source-action-selected-jet-certificates.json'
FINITE = 'lab/process/source-action-finite-loss-certificates.json'
RECORDS = {'selected-prepare.json', 'selected-outputs.json',
           'selected-spectral.json', 'selected-spectral-certificate.json',
           'selected-dense-producer.txt', 'selected-spectral-producer.txt'}
CLAIMS = {'SC-ACT-01': 'ASSERTS', 'SC-ACT-02': 'ASSERTS',
          'SC-OP-04': 'ASSERTS', 'SC-OP-05': 'UNCERTAIN',
          'SC-GEO-51': 'ASSERTS', 'SC-META-52': 'UNCERTAIN',
          'SC-META-53': 'UNCERTAIN'}


def require(ok, label):
    if not ok:
        raise ValueError(label)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def path_in(repo, name):
    path = (repo / name).resolve()
    require(not Path(name).is_absolute() and path.is_relative_to(repo),
            'repository-relative input: ' + name)
    return path


def check_files(repo, expected, files):
    for name, digest in expected.items():
        require(re.fullmatch('[0-9a-f]{64}', digest) is not None, 'SHA format')
        actual = file_sha(path_in(repo, name))
        require(actual == digest, 'changed input: ' + name)
        files[name] = actual


def load(repo, name, files):
    raw = path_in(repo, name).read_bytes()
    files[name] = sha(raw)
    return json.loads(raw)


def record_bytes(record):
    require(record['encoding'] in ('zlib-base64-json', 'zlib-base64-utf8'),
            'data-only record encoding')
    raw = zlib.decompress(base64.b64decode(record['data'], validate=True))
    require(len(raw) == record['uncompressed_bytes'] and sha(raw) == record['sha256'],
            'raw record byte count and SHA')
    return raw


def definition(source, name):
    nodes = [n for n in ast.parse(source).body
             if isinstance(n, ast.FunctionDef) and n.name == name]
    require(len(nodes) == 1, 'unique function: ' + name)
    return ast.get_source_segment(source, nodes[0])


def prior(repo, stem, files):
    result = load(repo, 'lab/process/source-action-' + stem + '.json', files)
    check_files(repo, result['current_sha256'], files)
    return result


def selected_inputs(repo, files):
    result = prior(repo, 'selected-jet', files)
    bundle = load(repo, SELECTED, files)
    producer = 'tests/program-focus/source_action_selected_jet_probe.py'
    require(bundle['schema'] == 'gu-selected-jet-certificate-v1'
            and bundle['data_only'], 'selected bundle type')
    require(bundle['final_probe_sha256'] == files[producer], 'selected final producer')
    check_files(repo, bundle['native_inputs'], files)
    require(set(bundle['records']) == RECORDS, 'six selected raw records')
    raw = {name: record_bytes(row) for name, row in bundle['records'].items()}
    data = {name: json.loads(value) for name, value in raw.items() if name.endswith('.json')}
    prepare, outputs = data['selected-prepare.json'], data['selected-outputs.json']
    spectral, proof = data['selected-spectral.json'], data['selected-spectral-certificate.json']
    dense = raw['selected-dense-producer.txt'].decode()
    spec = raw['selected-spectral-producer.txt'].decode()
    live = path_in(repo, producer).read_text()
    common = ('binding', 'records', 'field_errors', 'scale_errors', 'error_record',
              'read_errors', 'matrix_record', 'read_matrix', 'solve_low',
              'stage_prepare', 'hs_inner', 'output_stats', 'stage_outputs')
    for name in common:
        require(definition(dense, name) == definition(live, name), 'dense procedure: ' + name)
    for name in ('modular_rank', 'integer_operator', 'real_trace', 'integer_hs', 'stage_spectral'):
        require(definition(spec, name) == definition(live, name), 'spectral procedure: ' + name)
    require(prepare['execution_probe_sha256'] == outputs['execution_probe_sha256'] == sha(raw['selected-dense-producer.txt']),
            'original dense producer binding')
    require(spectral['execution_probe_sha256'] == sha(raw['selected-spectral-producer.txt']),
            'original spectral producer binding')
    require(prepare['bindings'] == spectral['bindings'] == outputs['bindings']['inputs'] == bundle['native_inputs'],
            'current native selected inputs')
    require(outputs['bindings']['prepare_sha256'] == bundle['records']['selected-prepare.json']['sha256'],
            'output-to-graph record binding')
    require(prepare['complete'] and len(prepare['roots']) == 2
            and [r['root'] for r in prepare['roots']] == [0, 1]
            and all(len(r['columns']) == 20 for r in prepare['roots']), 'forty inherited graph columns')
    require(not outputs['complete'] and len(outputs['columns']) == 2,
            'dense affine output remains PARTIAL2/40')
    require(spectral['complete'] and spectral['native_complex_basis_dimension'] == 36
            and spectral['realification_dimension'] == spectral['realified_u8_rank']['rank'] == 72
            and spectral['realified_u8_rank']['denominators_all_invertible']
            and spectral['direct_five_slot_formula_checks'] == 720, 'inherited spectral dimensions')
    require(all(row['Casimir_identity'] and row['Kap_zero'] for row in prepare['direct_controls']),
            'inherited matched derivative controls')
    # Only this live, hash-bound, scalar arithmetic function is executed.
    # Archived producer text is inert custody data, never executed.
    function = definition(live, 'spectral_certificate')
    namespace = {'Q': Q, 'require': require}
    exec(compile(function, str(path_in(repo, producer)) + ':spectral_certificate', 'exec'), namespace)
    exact = namespace['spectral_certificate'](spectral)
    require(all(proof[key] == value for key, value in exact.items()), 'exact sparse spectral Gram readback')
    require(proof['spectral_sha256'] == bundle['records']['selected-spectral.json']['sha256'],
            'spectral certificate record binding')
    require(exact['component_sizes'] == {'1': 64, '2': 112}
            and Q(exact['Hermitian_HS_squared_lower_coefficient_h']) == Q(212992, 15)
            and Q(exact['raw_HS_squared_upper_coefficient_U']) == 62813896704,
            'owned exact spectral bounds')
    replay = result['verification']['replay']
    require(replay['passed'] and replay['probe_sha256'] == bundle['final_probe_sha256']
            and replay['bundle_sha256'] == files[SELECTED]
            and replay['graph_columns_reconstructed'] == 40, 'published selected replay custody')
    for owner in ('scalar', 'onshell'):
        meta = prepare['owned'][owner]
        check_files(repo, {meta['bundle']: meta['bundle_sha256']}, files)
    return {'bundle_sha256': files[SELECTED], 'producer_sha256': bundle['final_probe_sha256'],
            'raw_records': {name: {key: row[key] for key in ('encoding', 'sha256', 'uncompressed_bytes')}
                            for name, row in bundle['records'].items()},
            'unchanged_production_functions_checked': 18,
            'inherited_graph_columns_authenticated': 40, 'graph_columns_reconstructed_now': 0,
            'dense_status': 'PARTIAL2/40', 'native_spectral_outputs_recomputed_now': 0,
            'exact_spectral_Gram_bound_recomputed': True,
            'spectral_certificate_function_sha256': sha(function.encode()),
            'positive_components': exact['component_sizes'],
            'robust_Gram_lower': exact['robust_Gram_minimum_eigenvalue_lower'],
            'Hermitian_lower_h': exact['Hermitian_HS_squared_lower_coefficient_h'],
            'raw_upper_U': exact['raw_HS_squared_upper_coefficient_U'],
            'matched_graph_formula': prepare['formula'],
            'root_record_bindings': [{k: r[k] for k in ('root', 'radius', 'owned_root_sha256')}
                                     for r in prepare['roots']],
            'phase_geometry_origin': prepare['owned']['scalar'],
            'intrinsic_dynamics_origin': prepare['owned']['onshell'],
            'visibility_scope': 'The normalized whole-band theorem is for sufficiently small members of the existing fixed-seed CK tube family. Its analytic uniformity and current interpretation are inherited written proofs, not recomputed here.'}


def geometry_controls(repo, files, selected):
    meta = selected['phase_geometry_origin']
    bundle = load(repo, meta['bundle'], files)
    require(files[meta['bundle']] == meta['bundle_sha256'], 'geometry bundle origin')
    producer = 'tests/program-focus/source_action_scalar_normal_operator_probe.py'
    require(bundle['final_probe_sha256'] == files[producer], 'geometry producer')
    for name, digest in meta['records'].items():
        require(bundle['records'][name]['sha256'] == digest, 'owned geometry record: ' + name)
    record = bundle['records']['scalar-geometry.json']
    data = json.loads(record_bytes(record))
    check_files(repo, data['native_inputs'], files)
    require(data['complete'] and data['dimension'] == 36
            and data['time_range_dimension'] == 20 and data['time_kernel_dimension'] == 16,
            'inherited scalar carrier')
    path = path_in(repo, 'tests/program-focus/source_action_deep_geometry.py')
    spec = importlib.util.spec_from_file_location('packet_phase_native_geometry', path)
    geo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(geo)
    native, traces, h_traces = [], [], []
    adaptations = []
    for S in geo.A:
        H = geo.zero()
        for i in range(3):
            H[i][3] = H[3][i] = -S[3][i]
        X = [[a + b for a, b in zip(row, hrow)] for row, hrow in zip(S, H)]
        native.append(X); adaptations.append(H)
        traces.append(geo.trace(X)); h_traces.append(geo.trace(H))
    stored = [[[Q(z) for z in row] for row in X] for X in data['adapted_generators']]
    require(native == stored, 'adapted generators equal authenticated native construction')
    require(traces == [Q(4)] + [Q(0)] * 9 and not any(h_traces), 'exact scalar trace character')
    require(not any(z for row in adaptations[8 - 4] for z in row), 'H8 is zero')
    require(all(geo.trace(geo.comm(X, Y)) == 0 for X in native for Y in native),
            'all adapted commutator traces vanish')
    return {'native_geometry_sha256': files['tests/program-focus/source_action_deep_geometry.py'],
            'geometry_record_sha256': record['sha256'], 'adapted_generators_compared': 10,
            'adapted_generator_traces_axes4_to13': list(map(str, traces)),
            'isotropy_correction_traces_axes4_to13': list(map(str, h_traces)),
            'H8_exact_zero': True, 'commutator_trace_controls': 100,
            'native_signature_diagonal': list(map(str, geo.d)),
            'inherited_section_convention': data['section'],
            'written_phase_identity': 'For g=g_p exp(sum z^a(A_a+H_a)), det(exp Z)=exp(tr Z) gives r-r(p)=(1/4)tr Z=z4, with r=-(1/8)log|det y|. Thus the packet linear phase is the same global scalar r; partial8 r=0 and its coordinate Hessian vanishes.',
            'verification_scope': 'Rational generators, traces and H8 are recomputed. The determinant/exponential and coordinate arguments are written identities; no numerical matrix exponential or PDE estimate is checked.'}


def inherited_packet_inputs(repo, files, selected):
    result = prior(repo, 'finite-loss', files)
    finite = load(repo, FINITE, files)
    producer = 'tests/program-focus/source_action_finite_loss_probe.py'
    require(finite['schema'] == 'gu-finite-loss-proof-inputs-v1' and finite['data_only']
            and finite['final_probe_sha256'] == files[producer], 'finite-loss certificate custody')
    verification = result['verification']['proof_input_verification']
    require(verification['passed'] and verification['certificate_sha256'] == files[FINITE]
            and verification['probe_sha256'] == files[producer], 'published finite-loss verification')
    intrinsic = finite['intrinsic_certificate_readback']
    require(intrinsic['bundle_sha256'] == selected['intrinsic_dynamics_origin']['bundle_sha256'],
            'same actual intrinsic dynamics')
    roots = intrinsic['roots']
    require([r['root'] for r in roots] == [0, 1], 'both held root records')
    checked = []
    for old, graph in zip(roots, selected['root_record_bindings']):
        lower, upper = Q(old['exact_real_lower']), Q(old['exact_real_upper'])
        require(old['root_record_sha256'] == graph['owned_root_sha256']
                and Q(old['radius']) == Q(graph['radius']), 'graph and dynamics root identity')
        require(lower > Q(19, 80) and upper >= lower
                and Q(old['strict_margin_over_19_over_80']) == lower - Q(19, 80),
                'inherited exact intrinsic moment threshold')
        require(old['whole_family_trace_zero_proof_authenticated_not_reproved'], 'trace-zero proof custody')
        checked.append({'root': old['root'], 'root_record_sha256': old['root_record_sha256'],
                        'strict_lower_above_19_over_80': True,
                        'exact_lower_sha256': sha(old['exact_real_lower'].encode()),
                        'moment_matrices_recomputed_now': False})
    auxiliary = finite['full_auxiliary_readback']
    name = 'lab/process/source-action-full-auxiliary-certificates.json'
    check_files(repo, {name: auxiliary['manifest_sha256'],
                      'tests/program-focus/source_action_full_auxiliary_probe.py': auxiliary['producer_sha256']}, files)
    require(auxiliary['full_M_dimension'] == 49154, 'inherited complete M dimension')
    return {'finite_loss_certificate_sha256': files[FINITE], 'producer_sha256': files[producer],
            'intrinsic_scalar_threshold_readback': checked,
            'full_auxiliary_manifest_sha256': auxiliary['manifest_sha256'],
            'full_M_dimension_inherited': 49154, 'full_M_matrices_recomputed_now': 0,
            'inherited_norm_transfer_assumptions': finite['norm_transfer_assumptions'],
            'packet_normalization': 'k=h^-2; tau=kt; y=(x-p)/h; spatial dimension d=13. The graph is the same fixed properly supported classical reconstruction used by the finite-loss proof.',
            'two_distinct_scopes': {
                'local_output': 'A known growing spin7 eigen-initial packet with chi=1 near y=0 and w_j(0)=0 for j>=1. The normal-jet statement is at initialization and, by continuity, short fixed rescaled time.',
                'weak_source_barrier': 'Any owned finite-order logarithmic-window packet, including the maximal-full-spectral-abscissa packet. Its leading eigenvector is not identified with the spin7 output witness.'},
            'verification_scope': 'Immutable prior proof-input/report hashes and scalar moment inequalities authenticated. No full-M defect, graph reconstruction, native spectral calculation or analytic packet remainder is repeated.'}


def source_inputs(repo, files):
    name = 'lab/sources/source-claim-register.yaml'
    raw = path_in(repo, name).read_bytes(); files[name] = sha(raw)
    text = raw.decode(); rows = []
    for claim, expected in CLAIMS.items():
        blocks = re.findall(r'^- id: ' + re.escape(claim) + r'\n.*?(?=^- id: |\Z)', text, re.M | re.S)
        require(len(blocks) == 1, 'unique source record: ' + claim)
        polarity = re.findall(r'^  polarity: (\S+)\s*$', blocks[0], re.M)
        require(polarity == [expected], 'source polarity: ' + claim)
        rows.append({'id': claim, 'polarity': expected, 'source_record_sha256': sha(blocks[0].encode())})
    return {'records': rows,
            'source_necessity': 'Absent for this completion. Action/field grammar and full-U source assertions do not select W2/K95, canonical-injection CK seeds, a fixed band/dispersion/tube, graph core, physical quotient or this current-visibility criterion.'}


def ceil_fraction(value):
    return -((-value.numerator) // value.denominator)


def exponent_controls():
    # Coordinates (m,L,g,A,d,constant), g=c*rho. This exact subtraction
    # is the universal identity used with q>=X, not a sample-based proof.
    gap = (Q(1), Q(-1), Q(-2), Q(-1), Q(1, 2), Q(-2))
    substituted = (Q(1), Q(-1), Q(-2), Q(-1), Q(1, 2), Q(0))
    require(gap[:-1] == substituted[:-1] and gap[-1] + 2 == substituted[-1],
            'substitution m=q+2')
    X_coefficients = (Q(0), Q(1), Q(2), Q(1), Q(-1, 2), Q(2))
    q_plus_two = (Q(1), Q(0), Q(0), Q(0), Q(0), Q(2))
    require(substituted == tuple(a-b for a, b in zip(q_plus_two, X_coefficients)),
            'gap=q-X+2 coefficient identity')
    fixtures = []
    for L in map(Q, ('0', '1/2', '3', '100')):
        for g in map(Q, ('1/40', '3/2', '17')):
            for A in map(Q, ('0', '5/3')):
                d = Q(13); X = L + 2*g + A + 2 - d/2
                q = max(0, ceil_fraction(X)); m = q + 2
                slack = m + d/2 - 2 - 2*g - A - L
                require(Q(q) >= X and slack == q-X+2 and slack >= 2,
                        'arbitrary-decay exponent fixture')
                fixtures.append({'L': str(L), 'c_rho': str(g), 'amplitude_loss_A': str(A),
                                 'q': q, 'integrations_m': m, 'power_above_L': str(slack)})
    return {'quantifiers': 'Every finite L>=0, g=c*rho>=0, fixed total polynomial amplitude loss A>=0, and d=13.',
            'schedule': 'X=L+2g+A+2-d/2; q=max(0,ceil X); m=q+2.',
            'exact_identity': 'm+d/2-2-2g-A-L=q-X+2>=2.',
            'fixed_log_powers': 'The h^2 slack absorbs every fixed power of log(1/h); this asymptotic fact is a written proof, not sampled numerically.',
            'coefficient_identity_checked': True, 'rational_fixtures': fixtures,
            'scope': 'Finite fixtures control arithmetic only. The universal conclusion uses ceil X>=X and the displayed exact identity, not an extrapolation from samples.'}


def poly_derivative(poly):
    return {j-1: j*a for j, a in poly.items() if j and a}


def poly_value(poly, y):
    return sum(a * y**j for j, a in poly.items())


def oscillatory_controls():
    rows = []
    for m in (1, 2, 4, 8):
        # f=(1-y^2)^m; compact extension has finite endpoint smoothness.
        f = {0: Q(1)}
        for unused in range(m):
            new = {}
            for j, a in f.items():
                new[j] = new.get(j, 0) + a
                new[j+2] = new.get(j+2, 0) - a
            f = {j: a for j, a in new.items() if a}
        derivatives = [f]
        while derivatives[-1]:
            derivatives.append(poly_derivative(derivatives[-1]))
        require(all(poly_value(derivatives[j], side) == 0 for j in range(m) for side in (-1, 1)),
                'finite endpoint derivatives vanish')
        require(all(poly_value(derivatives[m], side) != 0 for side in (-1, 1)),
                'first nonzero endpoint derivative')
        # With formal t=(i*omega)^-1, F=sum(-1)^j t^(j+1) f^(j).
        # Verify (1/t)F+dF/dy=f coefficientwise: d(exp(i*omega*y)F)/dy=exp(...)f.
        identity = {}
        for j, poly in enumerate(derivatives[:-1]):
            for degree, a in poly.items():
                key = (j, degree)
                identity[key] = identity.get(key, 0) + (-1)**j*a
            for degree, a in poly_derivative(poly).items():
                key = (j+1, degree)
                identity[key] = identity.get(key, 0) + (-1)**j*a
        identity = {key: a for key, a in identity.items() if a}
        require(identity == {(0, j): a for j, a in f.items()}, 'exact oscillatory antiderivative cancellation')
        integral = sum(Q(2)*a/(j+1) for j, a in f.items() if not j % 2)
        require(integral > 0, 'nonoscillatory amplitude integral')
        rows.append({'endpoint_vanishing_order': m, 'degree': 2*m,
                     'oscillatory_endpoint_first_possible_power_of_h': m+1,
                     'exact_nonoscillatory_integral': str(integral),
                     'opposite_phase_product_integral': str(integral),
                     'coefficientwise_antiderivative_identity': True})
    return {'controls': rows,
            'identity': 'For formal t=(i omega)^-1, (1/t+partial_y) sum_j (-1)^j t^(j+1) f^(j)=f.',
            'opposite_phase_control': 'Multiplying by exp(-i omega y) cancels the packet phase and leaves the nonzero amplitude integral. Such a source has unbounded derivative seminorms as omega grows and is outside the fixed uniformly smooth CK source class.',
            'scope': 'Finite exact integration-by-parts bookkeeping, not a physical countermodel or proof of a C-infinity/PDE estimate. The polynomial controls have only the displayed finite endpoint vanishing.'}


def certificate(repo):
    files = {}
    selected = selected_inputs(repo, files)
    geometry = geometry_controls(repo, files, selected)
    inherited = inherited_packet_inputs(repo, files, selected)
    sources = source_inputs(repo, files)
    return {'schema': 'gu-packet-phase-proof-inputs-v1', 'data_only': True,
            'final_probe_sha256': file_sha(Path(__file__).resolve()),
            'files_sha256': dict(sorted(files.items())),
            'selected_jet_readback': selected, 'native_phase_controls': geometry,
            'inherited_packet_inputs': inherited, 'source_polarity': sources,
            'arbitrary_power_arithmetic': exponent_controls(),
            'oscillatory_bookkeeping': oscillatory_controls(),
            'analytic_assumptions_not_probe_certified': {
                'local_output': 'Complexify the selected real-linear candidate current before using a complex packet. At least one real quadrature is detected. With the plateau and initial-zero hierarchy, partial8(Q_lambda packet)(p) has leading h^(-d/2-2) O8(lambda;v); graph-frequency terms hit zero local envelope derivatives.',
                'uniform_current': 'Fix the bounded matter band, bounded measurable dispersion and one admissible sufficiently small positive-volume CK tube independently of h. On a compact patch, all spacetime derivatives of normalized column/dual kernels are uniformly bounded over the compact parameter closure. Independent L2 amplitudes give uniform C^m current bounds for each m; no derivative of the measurable dispersion is taken.',
                'weak_pairing': 'The actual four-arrow connection vertex is algebraic in the connection insertion. Integration by parts against the nonstationary scalar phase, with compact envelope and controlled microlocal remainders, gives h^(m+d/2-2) exp(rho*tau) times a fixed log polynomial. On tau<=c log k this yields arbitrary weak decay. The same result follows by moving the fixed properly supported classical graph reconstruction to the smooth source by its formal transpose.',
                'graph_and_packet_estimates': 'Classical-symbol remainders, pseudolocal tails, finite-order packet hierarchy, and the fixed-time continuity of the local output require the written analytic proof. They are not established by finite JSON or polynomial tests.'},
            'not_claimed': ['Full coherent-packet output is recomputed', 'Every original tube with defect below one half is current-faithful',
                            'The full-rho packet eigenvector is necessarily spin7', 'Exact zero force at finite frequency',
                            'A retarded response bound at fixed positive physical time', 'Source bounds uniform over expanding bands or singular normalizers',
                            'Nonlinear closure, physical admission, or GU falsification'],
            'scope': 'Light native phase/input authentication and exact scalar bookkeeping. Initial spin7 packet-jet visibility and the uniform weak-source barrier for any owned logarithmic packet are distinct written statements. No native large operator, graph reconstruction, current census, inverse or PDE simulation is run.'}


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.new')
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=ROOT)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write-certificate', action='store_true')
    group.add_argument('--verify', action='store_true')
    parser.add_argument('--certificate', type=Path)
    parser.add_argument('--output', type=Path, help='Optional small verification receipt.')
    args = parser.parse_args(); tick = time.monotonic()
    repo = args.repo.resolve(); path = args.certificate or repo / BUNDLE
    actual = certificate(repo)
    if args.write_certificate:
        write(path, actual)
    else:
        require(json.loads(path.read_text()) == actual, 'frozen proof-input certificate equality')
    receipt = {'passed': True, 'mode': 'verify' if args.verify else 'write-certificate',
               'probe_sha256': actual['final_probe_sha256'], 'certificate_sha256': file_sha(path),
               'selected_raw_records_authenticated': 6, 'selected_spectral_Gram_blocks_checked': 176,
               'native_adapted_generators_checked': 10, 'H8_zero': True,
               'graph_columns_reconstructed': 0, 'native_spectral_outputs_recomputed': 0,
               'PDE_or_uniform_source_estimates_verified': False,
               'seconds': time.monotonic() - tick}
    if args.output:
        write(args.output, receipt)
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
