#!/usr/bin/env python3
"""Exact native principal matter/connection Fourier-support witness.

Uses the owned six-arrow matter symbol and original four-arrow vertex.  The
independent density-dual row is not identified with a physical adjoint.  No
curved plane-wave solution, physical contour, quotient, or GU verdict follows.
Only standard Python and the repository's sparse rational Clifford arithmetic
are used; no background inverse or native receiver construction is executed.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import ast
import base64
import hashlib
import inspect
import json
import sys
import time
import zlib

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
import source_action_deep_geometry as geo
from source_action_deep_algebra import Engine, add, scale
from source_action_physical_probe import mul, gamma, components, contraction
from source_action_slice_completion_probe import (
    column, covector, inverse, norm, sigma, slash, vscale, zero,
)

CERTIFICATE = 'lab/process/source-action-coupled-support-certificates.json'
FILES = (
    'tests/program-focus/source_action_deep_geometry.py',
    'tests/program-focus/source_action_deep_algebra.py',
    'tests/program-focus/source_action_physical_probe.py',
    'tests/program-focus/source_action_slice_completion_probe.py',
    'tests/program-focus/source_action_paired_response_probe.py',
    'tests/program-focus/source_action_current_receiver_probe.py',
    'tests/program-focus/source_action_onshell_dynamics_probe.py',
    'explorations/conditional-build/source-action-physical-dynamics-2026-11-25.md',
    'lab/process/source-action-scalar-normal-operator-certificates.json',
    'lab/process/source-action-kappa1-constraints.json',
    'lab/process/source-action-reduced-evolution.json',
    'lab/process/source-action-receiver-strategy.json',
)


def require(condition, label):
    if not condition:
        raise ValueError(label)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_definition(relative, name, namespace):
    """Execute only the bound definition, never an old probe's top-level job."""
    path = ROOT / relative
    tree = ast.parse(path.read_text())
    nodes = [node for node in tree.body
             if isinstance(node, (ast.FunctionDef, ast.ClassDef))
             and node.name == name]
    require(len(nodes) == 1, 'unique native definition: ' + name)
    code = ast.Module(body=nodes, type_ignores=[])
    exec(compile(code, str(path), 'exec'), namespace)
    return namespace[name], hashlib.sha256(
        ast.get_source_segment(path.read_text(), nodes[0]).encode()).hexdigest()


C, C_SHA = load_definition(
    'tests/program-focus/source_action_paired_response_probe.py', 'C', {'Q': Q})
I = C(0, 1)
VERTEX_NAMESPACE = dict(Q=Q, geo=geo, add=add, scale=scale,
                        mul=mul, gamma=gamma, components=components)
vertex, VERTEX_SHA = load_definition(
    'tests/program-focus/source_action_current_receiver_probe.py',
    'vertex', VERTEX_NAMESPACE.copy())
vertex_onshell, ONSHELL_VERTEX_SHA = load_definition(
    'tests/program-focus/source_action_onshell_dynamics_probe.py',
    'vertex', VERTEX_NAMESPACE.copy())


def cliff_record(value):
    return [[mask, C(z).ser()] for mask, z in sorted(value.items())]


def field_record(value):
    return {'one_form': [cliff_record(v) for v in value[0]],
            'scalar': cliff_record(value[1])}


def covector_record(value):
    return [str(x) for x in value]


def dot(p, q):
    return sum(p[a] * q[a] / geo.d[a] for a in range(14))


def row_contract(q, value):
    """Row (q^j beta, -beta c(q)), with common beta factored on the left."""
    z, nu = value
    return add(*(scale(q[j] / geo.d[j], z[j]) for j in range(14)),
               scale(-1, mul(slash(q), nu)))


def central_form(a, factor=1):
    return {(1 << j, 0): factor * a[j] for j in range(14) if a[j]}


def polarized_formula(p, q, a):
    """Derived central formula; used only to cross-check the original vertex."""
    return add(scale(dot(p, q), slash(a)),
               scale(-dot(q, a), slash(p)),
               scale(-dot(p, a), slash(q)))


def json_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def norm1(value):
    value = C(value)
    return abs(value.a) + abs(value.b)


def native_record(value):
    return [[e, cl, C(z).ser()] for (e, cl), z in sorted(value.items())]


def decode_native(value):
    return {(e, cl): C(*z) for e, cl, z in value}


def spin7_response_control(p, q):
    """Recompute one transverse operator on two owned graph responses.

    The root-ball inverse bounds and geometric construction are inherited with
    their byte/function bindings; the small center inverse, source, and current
    arithmetic are recomputed.  This is not a current on an unstable eigenspace.
    """
    def read(name):
        return json.loads((ROOT / 'lab/process' / name).read_text())

    bundle = read('source-action-scalar-normal-operator-certificates.json')
    entry = bundle['records']['scalar-geometry.json']
    require(entry['encoding'] == 'zlib-base64-json', 'geometry record encoding')
    raw = zlib.decompress(base64.b64decode(entry['data'], validate=True))
    require(len(raw) == entry['uncompressed_bytes'] and
            hashlib.sha256(raw).hexdigest() == entry['sha256'], 'geometry raw custody')
    geometry = json.loads(raw)
    require(geometry['complete'] and geometry['time_kernel_dimension'] == 16,
            'owned complete spin7 kernel')
    require(sha(ROOT / 'tests/program-focus/source_action_scalar_normal_operator_probe.py') ==
            bundle['final_probe_sha256'], 'owned scalar producer')
    old = read('source-action-kappa1-constraints.json')
    reduced = read('source-action-reduced-evolution.json')
    strategy = read('source-action-receiver-strategy.json')
    bindings = {}
    for source in (bundle['native_inputs'], geometry['native_inputs'],
                   old['dependencies'], reduced['dependencies'], strategy['sha256']):
        for name, expected in source.items():
            require(sha(ROOT / name) == expected, 'inherited input hash: ' + name)
            bindings[name] = expected
    basis = [decode_native(row) for row in geometry['basis']]
    N = [decode_native(row) for row in geometry['kernel_basis']]
    require(len(basis) == 36 and len(N) == 16, 'owned coordinate dimensions')
    E = Engine(geo)
    gram = [[C(E.pair({key: z.conj() for key, z in u.items()}, v)).ser()
             for v in N] for u in N]
    require(json_digest(gram) == old['exact_probe']['spin7']['kernel_gram_sha256'],
            'actual native N7 basis matches inherited paired inverse')
    for n in N:
        require(not contraction(components(n), range(14)), 'N7 gamma contraction zero')
    A = [[C(*z) for z in row] for row in geometry['matrices']['A']]
    B = [[C(*z) for z in row] for row in geometry['matrices']['B']]
    require(json_digest(geometry['matrices']['A']) ==
            old['exact_probe']['spin7']['time_matrix_sha256'], 'native time matrix custody')

    cp, cq = slash(p), slash(q)
    baxis = caxis = 5
    require(p[caxis] == q[baxis] == 0, 'transverse polarization axes')
    matter = zero()
    matter[0][caxis] = cp
    matter = matter[0], mul(scale(1 / geo.d[caxis], gamma(caxis)), cp)
    require(sigma(p, matter) == zero(), 'transverse column all15 kernel slots')
    for j in range(15):
        require(not mul(cq, sigma(q, column(j))[0][baxis]),
                'transverse row all15 kernel columns')
    maps = []
    for n in N:
        direct = mul(cq, vertex(n, matter)[0][baxis])
        nc = components(n)[baxis]
        cc = scale(1 / geo.d[caxis], gamma(caxis))
        shortcut = mul(cq, mul(add(mul(nc, cc), scale(-1, mul(cc, nc))), cp))
        require(direct == shortcut, 'direct all-four-arrow transverse N7 current')
        maps.append(direct)

    results = []
    for ri, index, mask in ((0, 3, 1902), (1, 12, 1749)):
        candidate = reduced['spin7_inverse_candidates'][ri]
        certificate = old['exact_probe']['spin7']['root_certificates'][ri]
        require(candidate['root'] == certificate['root'] == ri, 'root identity')
        for key in ('radius', 'neumann_bound', 'affine_inverse_coefficient_bound', 'center_defect'):
            require(candidate[key] == certificate[key], 'root inverse bound: ' + key)
        require(json_digest(candidate['inverse']) == certificate['inverse_sha256'] and
                json_digest(candidate['matrix_center']) == certificate['matrix_center_sha256'],
                'paired center inverse matrix custody')
        radius = Q(certificate['radius'])
        eta = Q(certificate['neumann_bound'])
        require(eta == Q(certificate['center_defect']) +
                radius * Q(certificate['affine_inverse_coefficient_bound']) and
                0 <= eta < 1, 'exact inherited Neumann inequality')
        R = [[C(*z) for z in row] for row in candidate['inverse']]
        H = [[C(*z) for z in row] for row in candidate['matrix_center']]
        for i in range(16):
            for j in range(16):
                require(sum((R[i][k] * H[k][j] for k in range(16)), C()) == int(i == j),
                        'exact paired center inverse recomputed')
        vco = [A[i][index] for i in range(36)]
        fco = [sum((B[i][j] * vco[j] for j in range(36)), C()) for i in range(36)]
        v = add(*(scale(z, b) for z, b in zip(vco, basis)))
        force = add(*(scale(z, b) for z, b in zip(fco, basis)))
        source = [C(E.pair({key: z.conj() for key, z in n.items()}, force)) for n in N]
        saved = next(row for row in strategy['exact_probe']['normal_energy']['roots'][ri]['rows']
                     if row['axis'] == 4 and row['range_basis_index'] == index)
        require(json_digest(native_record(v)) == saved['range_sha256'] and
                json_digest(native_record(force)) == saved['force_sha256'], 'same negative-energy native V and force')
        require([[i, z.ser()] for i, z in enumerate(source) if z] == saved['source_coordinates'],
                'same native paired constraint source')
        co = [-sum((x * y for x, y in zip(row, source)), C()) for row in R]
        error = eta / (1 - eta) * max(map(norm1, co))
        energy = sum((z.conj() * w for z, w in zip(source, co)), C())
        energy_error = sum(map(norm1, source)) * error + abs(energy.b)
        require((str(energy.a), str(energy_error), str(energy.a - energy_error),
                 str(energy.a + energy_error)) == tuple(saved[key] for key in
                 ('center', 'error_bound', 'lower', 'upper')), 'owned signed-energy interval reproduced')
        require(energy.a + energy_error < 0, 'strict signed-energy row')
        current = add(*(scale(z, value) for z, value in zip(co, maps)))
        center = C(current.get(mask, 0)).a
        current_error = error * sum(norm1(value.get(mask, 0)) for value in maps)
        require(center + current_error < 0, 'root-robust nonzero transverse current coefficient')
        results.append({
            'root': ri, 'range_basis_index': index, 'b': baxis, 'c': caxis,
            'root_radius': str(radius), 'inherited_neumann_bound': str(eta),
            'range_sha256': saved['range_sha256'], 'force_sha256': saved['force_sha256'],
            'source_coordinates': saved['source_coordinates'],
            'response_coordinates': [z.ser() for z in co],
            'coordinate_infinity_error': str(error),
            'current_operator_center': cliff_record(current),
            'separated_coefficient': {'mask': mask, 'component': 'real', 'center': str(center),
                'error': str(current_error), 'lower': str(center - current_error),
                'upper': str(center + current_error), 'strict_absolute_margin': str(-center - current_error)},
            'inherited_negative_energy': {'lower': saved['lower'], 'upper': saved['upper']},
        })
    return {
        'geometry_raw_sha256': entry['sha256'], 'inherited_bindings': bindings,
        'kernel_gram_sha256_recomputed': json_digest(gram),
        'native_N7_vertex_formula_checks': 16, 'transverse_column_kernel_slots': 15,
        'transverse_row_kernel_columns': 15, 'paired_center_inverse_entries_checked': 512,
        'response': 'n=-M^-1 P K4 V, using the authenticated paired N7 coordinates',
        'polarizations': 'z_5=c(p)chi0, nu=gamma^5 c(p)chi0; eta_5=beta0 c(q), eta_scalar=0',
        'rows': results,
        'scope': 'Current on the same complex-highest principal constrained response; nonzero implies a realified candidate component. This is not physical admission, not a current on the growing eigenspace, not a selected positive matter completion, and not forced energy exchange.',
    }


def compute():
    require(tuple(geo.d) == tuple(map(Q,
        (1, 1, 1, -1, -16, 8, 24, 48, 8, 8, -8, 8, -8, -8))),
        'actual K95 metric')
    p = [Q(0)] * 14
    p[0], p[3], p[4] = Q(5), Q(-3), Q(16)
    q = p.copy()
    q[4] = Q(-16)
    transfer = [a - b for a, b in zip(p, q)]
    require(norm(p) == norm(q) == 0, 'two real null matter covectors')
    require(dot(p, q) == 32, 'null-pair cross norm')
    require(norm(transfer) == -64 and transfer == vscale_covector(32, covector(4)),
            'pure normal timelike transfer')
    spatial = []
    for xi in (p, q):
        kappa = xi.copy()
        kappa[3] = 0
        require(norm(kappa) == 9, 'strict-center margin')
        spatial.append(kappa)

    psi = ([{0: x} if x else {} for x in p], {})
    require(sigma(p, psi) == zero(), 'all 15 column symbol slots vanish')
    row_residuals = [row_contract(q, sigma(q, column(j))) for j in range(15)]
    require(not any(row_residuals), 'all 15 independent-row symbol columns vanish')
    # The primary-minus formal dual on exp(-i q.x) is +i eta sigma(q).
    require(not any(scale(I, value) for value in row_residuals),
            'primary-minus dual phase convention')

    central_symbol_checks = 0
    owned_vertex_checks = 0
    formula_checks = 0
    for axis in range(14):
        a = covector(axis)
        w = central_form(a)
        for j in range(15):
            value = vertex(w, column(j))
            require(value == sigma(a, column(j)),
                    'full four-arrow central vertex equals native symbol')
            require(value == vertex_onshell(w, column(j)),
                    'original and later owned vertices agree')
            central_symbol_checks += 1
            owned_vertex_checks += 1
        direct = row_contract(q, vertex(w, psi))
        require(direct == polarized_formula(p, q, a), 'polarized formula cross-check')
        formula_checks += 1

    time_form = central_form(covector(3))
    true_scalar = vertex(time_form, column(14))
    missing_se = vertex(time_form, column(14), se=Q(0))
    require(true_scalar != missing_se and true_scalar[0] == missing_se[0],
            'southeast mutation detected on scalar input')
    require(true_scalar[1] == scale(Q(-1, 2), slash(covector(3))),
            'actual southeast coefficient is minus one half')

    evolution_square_checks = 0
    for kappa in spatial:
        def evolution(v):
            return vscale(-1, inverse(covector(3), sigma(kappa, v)))
        for j in range(15):
            require(evolution(evolution(column(j))) == vscale(9, column(j)),
                    'strict-center native real time-symbol square')
            evolution_square_checks += 1

    physical_transverse = central_form(covector(1), I)
    bare_current = row_contract(q, vertex(physical_transverse, psi))
    require(bare_current == {1 << 1: 32 * I}, 'transverse native vertex operator')
    beta_factor = {1 << 1: -I}
    scalar_operator = mul(beta_factor, bare_current)
    require(scalar_operator == {0: C(32)}, 'explicit nonzero real action pairing')
    longitudinal = row_contract(q, vertex(central_form(transfer, I), psi))
    require(not longitudinal, 'longitudinal principal Ward cancellation')
    require(mul(beta_factor, longitudinal) == {}, 'paired longitudinal cancellation')
    require(I.conj() == -I, 'central i Id is skew for any nondegenerate Hermitian form')

    se_controls = []
    for se in (Q(0), Q(1)):
        def sigma_se(xi, value):
            native = sigma(xi, value)
            return native[0], add(native[1], scale(se + Q(1, 2), mul(slash(xi), value[1])))
        require(sigma_se(p, psi) == zero(), 'gradient column kernel is SE-independent')
        for j in range(15):
            require(not row_contract(q, sigma_se(q, column(j))),
                    'null dual row kernel is SE-independent')
        require(row_contract(q, vertex(physical_transverse, psi, se=se)) == bare_current,
                'central witness current is SE-independent')
        require(not row_contract(q, vertex(central_form(transfer, I), psi, se=se)),
                'central longitudinal cancellation is SE-independent')
        se_controls.append({'SE': str(se), 'column_kernel_slots': 15,
                            'dual_kernel_columns': 15, 'same_current_and_longitudinal_zero': True})

    spin7 = spin7_response_control(p, q)

    return {
        'schema': 'gu-native-coupled-support-exact-v1',
        'complete': True,
        'producer': {
            'path': 'tests/program-focus/source_action_coupled_support_probe.py',
            'sha256': sha(__file__),
            'dependencies': {path: sha(ROOT / path) for path in FILES},
            'definition_sha256': {
                'original_current_vertex': VERTEX_SHA,
                'onshell_vertex': ONSHELL_VERTEX_SHA,
                'Gaussian_rational_C': C_SHA,
                'native_sigma': hashlib.sha256(inspect.getsource(sigma).encode()).hexdigest(),
            },
            'execution': 'Sparse exact rational Clifford arithmetic and stored 16x16 inverse checks; no receiver setup, root solve, large native assembly, or inverse construction.',
        },
        'conventions': {
            'geometry': 'W2/K95 with the actual rational diagonal metric; no K77 transfer',
            'metric_diagonal': covector_record(geo.d),
            'matter_carrier': '(T*Y plus scalar) tensor S, 15 spinor slots, complex dimension 1920',
            'connection_carrier': 'Full U: the actual central imaginary direction i theta1 Id is retained',
            'row': 'Independent density-dual row; no Hermitian-adjoint contour imposed',
            'formal_dual': '-partial_a(eta A^a) + eta C',
            'phase': 'column exp(i p.x), independent row exp(-i q.x), source exp(i (p-q).x)',
            'physical_action_pairing': 'Re(eta V_a psi), with beta = -i ell gamma1 and ell chi = 1',
            'SE': '-1/2',
        },
        'wave_covectors': {
            'p': covector_record(p), 'q': covector_record(q),
            'p_norm': str(norm(p)), 'q_norm': str(norm(q)), 'p_dot_q': str(dot(p, q)),
            'common_theta3_coefficient': '-3', 'absolute_time_frequency': '3',
            'spatial_norms_strict_center': [str(norm(k)) for k in spatial],
            'transfer': covector_record(transfer), 'transfer_norm': str(norm(transfer)),
            'transfer_spatial_norm': str(norm(transfer)),
            'transfer_is_pure_normal': True,
        },
        'polarizations': {
            'column_before_chi': field_record(psi),
            'independent_row': '(q^j beta, -beta c(q)), q^j = q_j/d_j',
            'beta_left_factor': cliff_record(beta_factor),
            'spinor_realization': 'Any spinor chi and covector ell with ell chi=1; e_j and e_j^T suffice',
            'column_kernel_all15': True, 'dual_kernel_all15': True,
        },
        'exact_current': {
            'transverse_variation': 'i theta1 Id',
            'unpaired_Clifford_operator': cliff_record(bare_current),
            'paired_Clifford_operator': cliff_record(scalar_operator),
            'real_action_amplitude': '32',
            'real_source_phase': '32 cos((p-q).x); both +/- transfer frequencies occur',
            'longitudinal_variation': 'i (p-q) Id',
            'longitudinal_operator': cliff_record(longitudinal),
        },
        'controls': {
            'central_vertex_symbol_all14_by15': central_symbol_checks,
            'original_versus_onshell_vertex_all14_by15': owned_vertex_checks,
            'direct_vertex_versus_polarized_formula_all14': formula_checks,
            'nonnull_time_evolution_square_all15_both_inputs': evolution_square_checks,
            'column_symbol_slots': 15, 'dual_symbol_columns': 15,
            'southeast_mutation_detected': True,
            'southeast_scalar_output': cliff_record(true_scalar[1]),
            'physical_central_skew_direction': True,
            'SE_family_controls': se_controls,
            'SE_family_scope': 'Kernel and central current controls only; strict-center time-evolution square is checked only at the held SE=-1/2.',
        },
        'same_principal_constrained_spin7_response': spin7,
        'scope': {
            'proved': 'Exact native principal on-shell matter polarizations in strict-center support generate a nonzero actual four-arrow polarized connection source at a timelike normal transfer.',
            'central_witness_root_dependence': 'None: the retained principal symbol and algebraic connection vertex are independent of the stationary background roots. The separate constrained spin7 response uses both inherited root boxes.',
            'not_claimed': [
                'These constant polarizations are exact plane-wave solutions of the full variable-coefficient lower-order matter equations.',
                'Physical admission or a chosen adjoint contour for the independent row.',
                'Nonzero projection onto a specified connection growth eigenspace.',
                'A full active central gauge symmetry from the longitudinal principal cancellation.',
                'Global nonlinear solutions, a physical instability, or a GU verdict.',
            ],
        },
    }


def vscale_covector(factor, xi):
    return [factor * x for x in xi]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write-certificate', action='store_true')
    mode.add_argument('--verify', action='store_true')
    parser.add_argument('--certificate', type=Path, default=ROOT / CERTIFICATE)
    parser.add_argument('--output', type=Path, help='Optional receipt path; no cache is required.')
    args = parser.parse_args()
    started = time.monotonic()
    result = compute()
    if args.write_certificate:
        args.certificate.parent.mkdir(parents=True, exist_ok=True)
        args.certificate.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    else:
        require(json.loads(args.certificate.read_text()) == result,
                'certificate differs from exact recomputation or current input bindings')
    receipt = {
        'passed': True, 'mode': 'verify' if args.verify else 'write-certificate',
        'producer_sha256': sha(__file__), 'certificate_sha256': sha(args.certificate),
        'seconds': time.monotonic() - started, 'controls': result['controls'],
        'real_action_amplitude': result['exact_current']['real_action_amplitude'],
        'spin7_current_separation': [
            {'root': row['root'], 'range_basis_index': row['range_basis_index'],
             'center_approximation': float(Q(row['separated_coefficient']['center'])),
             'error_upper_approximation': float(Q(row['separated_coefficient']['error']))}
            for row in result['same_principal_constrained_spin7_response']['rows']],
        'scope': 'All recorded native sparse identities and bindings recomputed; no full curved matter or physical-contour claim.',
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(json.dumps(receipt, sort_keys=True))


if __name__ == '__main__':
    main()
