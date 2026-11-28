#!/usr/bin/env python3
"""Exact actual-P nonlinear transfer controls; no dense inversion or PDE solve.

The universal identities and analytic/domain scope are reviewed written proofs.
Contributor sketches were integrated and executed only by root.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb, prod
from types import SimpleNamespace
import argparse
import hashlib
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def read_field(rows):
    return {(int(e), int(c)): F(v) for e, c, v in rows if F(v)}


def field_record(field):
    return [[e, c, str(v)] for (e, c), v in sorted(field.items()) if v]


def context(repo):
    repo = Path(repo).resolve()
    sys.path.insert(0, str(repo / "tests/program-focus"))
    ar = 'tests/program-focus/source_action_deep_algebra.py'
    gr = 'tests/program-focus/source_action_deep_geometry.py'
    br = 'lab/process/printed-endpoint-analytic-branch-certificates.json'
    pr = 'tests/program-focus/printed_endpoint_analytic_branch_probe.py'
    dr = 'lab/process/source-action-deep-coefficients.json'
    cert = json.loads((repo / br).read_text())
    assert cert['probe_sha256'] == digest(repo / pr)
    for rel, value in cert['native_inputs_sha256'].items():
        assert digest(repo / rel) == value, ('input custody', rel)
    a = load_module(repo / ar, '_gu_nlj_algebra')
    g = load_module(repo / gr, '_gu_nlj_geometry')
    data = json.loads((repo / dr).read_text())
    e = a.Engine(g)
    ts = [read_field(r['ambient_form']) for r in cert['printed_coefficients']]
    assert len(ts) == 4
    basis = [read_field(r) for r in data['basis'][:6]]
    pivots = [tuple(p) for p in data['pivots'][:6]]
    assert [sorted({c.bit_count() for _, c in b}) for b in basis] == [[1]]*3+[[2]]*3
    assert all(b.get(p, F()) == int(i == j)
               for i, p in enumerate(pivots) for j, b in enumerate(basis))
    return SimpleNamespace(repo=repo, a=a, g=g, e=e, ts=ts,
        basis=basis, pivots=pivots,
        bindings={p: digest(repo / p) for p in [ar, gr, br, pr, dr]})


def symbol(ctx, xi, field):
    x = {(1 << i, 0): F(v) for i, v in xi.items() if v}
    return ctx.e.Phi(ctx.e.wedge(x, field))


def jacobian(ctx, T, u):
    # Exactly 2Q(T,u), including the full symmetric raw wedge.
    return ctx.e.Phi(ctx.a.add(ctx.e.wedge(T, u), ctx.e.wedge(u, T)))


def quadratic(ctx, T, u):
    return ctx.a.scale(F(1, 2), jacobian(ctx, T, u))


def linear(ctx, T):
    return ctx.e.Phi(ctx.e.D(T))


def reduce_six(ctx, field):
    rem = dict(field)
    coordinates = []
    for pivot, basis in zip(ctx.pivots, ctx.basis):
        value = rem.get(pivot, F())
        coordinates.append(value)
        if value:
            rem = ctx.a.add(rem, ctx.a.scale(-value, basis))
    assert ctx.a.add(rem, *(ctx.a.scale(c, b)
        for c, b in zip(coordinates, ctx.basis))) == field
    return coordinates, rem


def diagonal_grade_one(field):
    assert all(e == c and e.bit_count() == 1 for e, c in field)
    return [field.get((1 << i, 1 << i), F()) for i in range(14)]


def controls(ctx):
    a, e = ctx.a, ctx.e
    checks = []
    def ck(name, value):
        assert value, name
        checks.append(name)
    tau = {3: F(1)}
    omega = (1 << 14)-1
    wt = diagonal_grade_one(ctx.ts[0])
    w3 = diagonal_grade_one(ctx.ts[2])
    ck('t1_diagonal', wt == [F(21, 4)]*5+[F(15, 4)]*9)
    ck('t1_trace', sum(wt) == 60)
    for order in (2, 4):
        ck('owned_even_grade:'+str(order),
           all(c.bit_count() % 2 == 0 for _, c in ctx.ts[order-1]))
    constants = [4*x for x in [1, 12, 22, 30, 36, 40, 42]+list(range(-1, -13, -1))]
    K = prod(constants)
    ck('leading_scalarizer_constant_positive', K > 0)
    long_first = sum(comb(13, p) for p in range(1, 12, 2))
    long_second = sum(comb(13, p) for p in range(1, 14, 2))
    ck('range_dimension', (long_first, long_second, long_first+long_second+13)
       == (4095, 4096, 8204))
    samples = []
    for order, weights in [(1, wt), (3, w3)]:
        T = ctx.ts[order-1]
        for j in (0, 4, 5, 10):
            u = {(1 << j, omega): F(1)}
            actual = jacobian(ctx, T, u)
            expected = a.scale(-4*(sum(weights)-weights[j]), u)
            ck(f'volume_diagonal:{order}:{j}', actual == expected)
            samples.append({'order': order, 'volume_leg': j, 'image': field_record(actual)})
        for j in (0, 5):
            u = {(1 << 3, 1 << j): F(1)}
            expected = a.scale(-4*(sum(weights)-weights[3]-weights[j]), u)
            ck(f'longitudinal_grade1:{order}:{j}', jacobian(ctx, T, u) == expected)
    for order in (2, 4):
        for j in (0, 3, 5):
            ck(f'even_T_volume_zero:{order}:{j}',
               not jacobian(ctx, ctx.ts[order-1], {(1 << j, omega): F(1)}))
    # All14 volume-valued one-forms are zero-Jordan images, including the
    # one longitudinal volume column. The thirteen count is transverse only.
    transverse_top = omega ^ (1 << 3)
    for j in range(14):
        w = {(1 << j, omega): F(1)}
        ck('volume_in_kernel:'+str(j), not symbol(ctx, tau, w))
        if j != 3:
            z = {(1 << j, transverse_top): F(-1, 2)}
        else:
            # Compute Gamma E(omega_W), then normalize its single output.
            z = {}
            for b in range(14):
                if b == 3:
                    continue
                cm, cv = e.cmul(1 << b, transverse_top)
                gm, gv = e.cmul(1 << 3, cm)
                z[(1 << b, gm)] = cv*gv
            pz = symbol(ctx, tau, z)
            ck('long_volume_preimage_has_only_owned_receiver', set(pz) == {(1 << 3, omega)})
            z = a.scale(1/pz[(1 << 3, omega)], z)
        ck('volume_is_zero_Jordan_image:'+str(j), symbol(ctx, tau, z) == w)
    # Genuine full-translation first-correction cokernel example, unrelated
    # to an assertion that the actual branch has this grade5 coefficient.
    tmask = sum(1 << i for i in (0, 3, 11, 12, 13))
    T = {(1 << 1, tmask): F(1)}
    w = {(1 << 0, omega): F(1)}
    receiver_mask = sum(1 << i for i in (0, 1, 2, 4, 5, 6, 7, 8, 9, 10))
    target = (1 << 1, receiver_mask)
    expected = {target: F(2048)}
    actual = jacobian(ctx, T, w)
    ck('full_translation_cokernel_output', actual == expected)
    ck('comm_wedge_normalization',
       actual == e.Phi(e.wedge(T, w, 'comm')))
    ck('counterexample_real_form', e.real_skew(T) and e.real_skew(w) and e.real_skew(actual))
    z = {(1 << 0, transverse_top): F(-1, 2)}
    ck('counterexample_input_is_zero_Jordan_image', symbol(ctx, tau, z) == w)
    # Exhaustive source columns able to hit this ONE receiver under actual
    # Phi(tau wedge .). Clifford products toggle fixed masks: at most13
    # candidates. All other columns cannot reach the receiver by XOR support.
    candidates = {(1 << 1, receiver_mask ^ (1 << 3))}
    zm = receiver_mask ^ (1 << 1)
    for b in range(14):
        if b != 3:
            candidates.add((1 << b, zm ^ (1 << 3) ^ (1 << b)))
    for key in sorted(candidates):
        ck('cokernel_candidate_column:'+str(key),
           not symbol(ctx, tau, {key: F(1)}).get(target, F()))
    # Generic double-sandwich can also be nonzero; actual low-jet result is
    # different. On this output P^2=0, so B39 acts as K*q^19*P exactly.
    pa = symbol(ctx, tau, actual)
    ck('generic_output_zero_generalized', not symbol(ctx, tau, pa))
    ck('generic_double_sandwich_nonzero', bool(pa))
    return {'status': 'PASS', 'checks': checks, 'range_dimension': 8204,
        'longitudinal_dimensions': [long_first, long_second],
        'volume_dimension_total': 14, 'volume_transverse_added': 13,
        'B39_constant_product_c': str(K), 'actual_branch_samples': samples,
        'generic_counterexample': {'T': field_record(T), 'w': field_record(w),
            'V_T_w': field_record(actual), 'P_V_T_w': field_record(pa),
            'cokernel_receiver': list(target), 'candidate_columns': len(candidates),
            'scope': 'Arbitrary full translation. Not an actual analytic-branch coefficient.'},
        'scope': 'Finite native controls; all-xi and image-class coverage use the accompanying written proof.'}


def closure(ctx):
    rows = []
    for i, b in enumerate(ctx.basis):
        out = linear(ctx, b)
        cs, rem = reduce_six(ctx, out)
        rows.append({'map': 'P', 'indices': [i], 'coordinates': list(map(str, cs)),
                     'remainder': field_record(rem)})
    for i in range(6):
        for j in range(i, 6):
            out = quadratic(ctx, ctx.basis[i], ctx.basis[j])
            cs, rem = reduce_six(ctx, out)
            rows.append({'map': 'Q', 'indices': [i, j], 'coordinates': list(map(str, cs)),
                         'remainder': field_record(rem)})
    s_cs, s_rem = reduce_six(ctx, ctx.a.scale(-1, ctx.ts[0]))
    passed = not s_rem and all(not row['remainder'] for row in rows)
    return {'closed': passed, 'maps': rows, 'map_count': len(rows),
        'basis': [field_record(b) for b in ctx.basis],
        'basis_source_indices': list(range(6)), 'S_coordinates': list(map(str, s_cs)),
        'S_remainder': field_record(s_rem),
        'scope': 'If closed, the finite six-space IFT branch agrees with the full216 branch by uniqueness. If not, this is only failure of this sufficient subspace.'}


def next_coefficient(ctx):
    t1, t2, t3, t4 = ctx.ts
    u5 = ctx.a.scale(-1, ctx.a.add(linear(ctx, t4),
        ctx.a.scale(2, quadratic(ctx, t1, t3)), quadratic(ctx, t2, t2)))
    cs, rem = reduce_six(ctx, u5)
    return {'order': 5, 'field': field_record(u5),
        'grades': sorted({c.bit_count() for _, c in u5}),
        'six_coordinates': list(map(str, cs)), 'six_remainder': field_record(rem),
        'scope': 'Actual next printed coefficient, not Euler K/N recurrence.'}


from fractions import Fraction as Q
from hashlib import sha256
import json

from source_action_deep_algebra import Engine, add, scale


def null_hook_checks(e: Engine):
    """Return exact controls and native Phi(D) lower columns.

    A zero native defect is an admissible outcome. This helper certifies the
    frozen sector and records, rather than assumes, its constant-component
    first-jet defect in the supplied native frame.
    """
    checks = []

    def ck(name, value):
        assert value, name
        checks.append(name)

    expected_d = tuple(map(Q, [1, 1, 1, -1, -16, 8, 24, 48,
                              8, 8, -8, 8, -8, -8]))
    ck("native-K95-orthogonal-basis", e.dim == 14 and e.d == expected_d)

    def cov_inner(v, w):
        return sum((v.get(i, Q()) * w.get(i, Q()) / e.d[i]
                    for i in range(e.dim)), Q())

    def raised_cliff(v):
        return {1 << i: z / e.d[i] for i, z in v.items() if z}

    def scalar_one(v):
        return {(1 << i, 0): z for i, z in v.items() if z}

    def tensor(v, coefficient):
        return {(1 << i, c): x * y for i, x in v.items()
                for c, y in coefficient.items() if x * y}

    def left_cliff(coefficient, field):
        return e.wedge({(0, c): z for c, z in coefficient.items()}, field)

    def pair_add(*values):
        return (add(*(v[0] for v in values)), add(*(v[1] for v in values)))

    def pair_scale(z, value):
        return (scale(z, value[0]), scale(z, value[1]))

    def pair_conjugate(value):
        return (value[0], scale(-1, value[1]))

    def pair_linear(operator, value):
        return (operator(value[0]), operator(value[1]))

    def pair_wedge(x, y):
        return (add(e.wedge(x[0], y[0]), scale(-1, e.wedge(x[1], y[1]))),
                add(e.wedge(x[0], y[1]), e.wedge(x[1], y[0])))

    def pair_zero(value):
        return not value[0] and not value[1]

    def sharp_real(field):
        return {(leg, c): ((-1) ** (c.bit_count() * (c.bit_count() + 1) // 2)) * z
                for (leg, c), z in field.items() if z}

    def sharp_pair(value):
        # Krein sharp is anti-linear, and reverses Clifford products.
        return (sharp_real(value[0]), scale(-1, sharp_real(value[1])))

    def sparse(field):
        return [[leg, c, str(z)] for (leg, c), z in sorted(field.items()) if z]

    def field_record(field):
        entries = sparse(field)
        order = sorted(field, key=lambda k: (k[1].bit_count(), k[0], k[1]))
        first = order[0] if order else None
        return {
            "nonzero": bool(entries),
            "components": len(entries),
            "sha256": sha256(json.dumps(entries, separators=(",", ":")).encode()).hexdigest(),
            "simplest_receiver": None if first is None else {
                "form_mask": first[0], "clifford_mask": first[1],
                "coefficient": str(field[first]),
            },
            "sparse_entries": entries,
        }

    tau = {3: Q(1)}
    eta = {4: Q(4)}
    a = {5: Q(1), 10: Q(1)}
    ct, cn, ca = map(raised_cliff, (tau, eta, a))
    ck("tau-negative-unit", cov_inner(tau, tau) == -1)
    ck("eta-negative-unit", cov_inner(eta, eta) == -1)
    ck("a-real-nonzero-null", bool(a) and cov_inner(a, a) == 0)
    ck("three-covectors-orthogonal", all(cov_inner(v, w) == 0
       for v, w in ((tau, eta), (tau, a), (eta, a))))
    ck("raised-tau-sign", ct == {1 << 3: Q(-1)})
    ck("raised-normal-scale", cn == {1 << 4: Q(-1, 4)})
    ck("raised-null-scale", ca == {1 << 5: Q(1, 8), 1 << 10: Q(-1, 8)})
    ck("Clifford-tau-square", e.cliff_product(ct, ct) == {0: Q(-1)})
    ck("Clifford-eta-square", e.cliff_product(cn, cn) == {0: Q(-1)})
    ck("Clifford-null-square", not e.cliff_product(ca, ca))
    ck("Clifford-orthogonality", not e.cliff_product(ct, ca, "anti")
       and not e.cliff_product(cn, ca, "anti"))

    kap, lam, freq = Q(2), Q(3, 4), Q(5, 4)
    qq = lam * lam * cov_inner(tau, tau) - freq * freq * cov_inner(eta, eta)
    ck("rational-hook-mass-shell", qq == 1 and 4 * qq == kap * kap)
    beta = tensor(a, ca)
    tbeta, nbeta = left_cliff(ct, beta), left_cliff(cn, beta)
    gamma_beta = (scale(lam, tbeta), scale(freq, nbeta))
    beta_pair = (beta, {})
    zeta_one = (scale(lam, scalar_one(tau)), scale(freq, scalar_one(eta)))
    Pz = lambda field: pair_linear(e.Phi, pair_wedge(zeta_one, field))

    ck("native-hook-forward", Pz(beta_pair) == pair_scale(-2, gamma_beta))
    ck("native-hook-back", Pz(gamma_beta) == pair_scale(-2 * qq, beta_pair))
    mode = pair_add(pair_scale(kap, beta_pair), pair_scale(2, gamma_beta))
    ck("nonzero-mode", bool(mode[0]) and bool(mode[1]))
    ck("actual-frozen-massive-kernel", pair_zero(pair_add(pair_scale(kap, mode), Pz(mode))))
    ck("primary-minus-conjugate-sharp", sharp_pair(mode) == pair_scale(-1, pair_conjugate(mode)))
    ck("native-real-quadratures-skew", e.real_skew(mode[0]) and e.real_skew(mode[1])
       and sharp_real(mode[0]) == scale(-1, mode[0])
       and sharp_real(mode[1]) == scale(-1, mode[1]))
    ck("only-vector-bivector-quadratures", all(c.bit_count() in (1, 2)
       for field in mode for leg, c in field))

    # Re(exp(i n y) mode) = A cos(n y) + B sin(n y), with B=-Im(mode).
    cosine, sine = mode[0], scale(-1, mode[1])
    Pt = lambda field: e.Phi(e.wedge(scalar_one(tau), field))
    Pn = lambda field: e.Phi(e.wedge(scalar_one(eta), field))
    ck("real-cosine-equation", not add(scale(kap, cosine), scale(lam, Pt(cosine)), scale(freq, Pn(sine))))
    ck("real-sine-equation", not add(scale(kap, sine), scale(lam, Pt(sine)), scale(-freq, Pn(cosine))))
    for label, field in (("cosine", cosine), ("sine", sine)):
        rows = e.split_one(field)
        ck(label + "-common-real-a", set(rows) == {5, 10} and rows[5] == rows[10])
    for label, x, y in (("cos-cos", cosine, cosine), ("cos-sin", cosine, sine),
                        ("sin-cos", sine, cosine), ("sin-sin", sine, sine)):
        w = e.wedge(x, y)
        ck("common-leg-wedge-zero:" + label, not w)
        ck("printed-quadratic-zero:" + label, not e.Phi(w))
    ck("complex-self-wedge-zero", pair_zero(pair_wedge(mode, mode)))
    ck("complex-conjugate-cross-zero", pair_zero(pair_wedge(mode, pair_conjugate(mode))))

    # Meaningful planted controls: wrong mass, missing raising, and two form legs.
    wrong_mass = kap + 1
    wrong_mode = pair_add(pair_scale(wrong_mass, beta_pair), pair_scale(2, gamma_beta))
    wrong_residual = pair_add(pair_scale(wrong_mass, wrong_mode), Pz(wrong_mode))
    ck("wrong-mass-is-detected", wrong_residual == pair_scale(wrong_mass * wrong_mass - 4 * qq, beta_pair)
       and not pair_zero(wrong_residual))
    unraised_normal = {1 << 4: Q(4)}
    bad_gamma_beta = (gamma_beta[0], scale(freq, left_cliff(unraised_normal, beta)))
    bad_mode = pair_add(pair_scale(kap, beta_pair), pair_scale(2, bad_gamma_beta))
    ck("unraised-normal-is-detected", not pair_zero(pair_add(pair_scale(kap, bad_mode), Pz(bad_mode))))
    two_leg = {(1 << 5, 1 << 5): Q(1), (1 << 3, 1 << 3): Q(1)}
    ck("two-leg-wedge-can-be-nonzero", bool(e.wedge(two_leg, two_leg)))

    # Native connection terms: retain exact full output, including all form legs.
    # No assertion that a defect must be nonzero: cancellation is a valid result.
    lower = lambda field: e.Phi(e.D(field))
    r1, rt, rn = lower(beta), lower(tbeta), lower(nbeta)
    real_defect = add(scale(kap, r1), scale(2 * lam, rt))
    imag_defect = scale(2 * freq, rn)
    ck("native-lower-real-linearity", lower(mode[0]) == real_defect)
    ck("native-lower-imag-linearity", lower(mode[1]) == imag_defect)
    ck("native-lower-quadratures-real", e.real_skew(real_defect) and e.real_skew(imag_defect))

    return {
        "status": "PASS",
        "checks": len(checks),
        "check_names": checks,
        "parameters": {"kappa": str(kap), "lambda": str(lam), "frequency": str(freq), "q_zeta": str(qq)},
        "covectors": {"tau": [[i, str(z)] for i, z in tau.items()],
                      "eta": [[i, str(z)] for i, z in eta.items()],
                      "a": [[i, str(z)] for i, z in a.items()]},
        "mode_quadratures": {"real": field_record(mode[0]), "imaginary": field_record(mode[1])},
        "native_lower_columns": {"beta": field_record(r1), "c_tau_beta": field_record(rt),
                                 "c_eta_beta": field_record(rn)},
        "native_mode_defect": {"real": field_record(real_defect), "imaginary": field_record(imag_defect),
                               "nonzero": bool(real_defect or imag_defect)},
        "scope": [
            "Exact zero-source frozen massive printed equation and its Phi(T wedge T) term, in the native primary-minus grade1/2 sector.",
            "Native lower columns are the exact constant-component first-jet Phi(D_B) remainder in the supplied geometry frame; no corrected amplitude is solved.",
            "Actual source S and background cross term 2Q(T0,t) are not discarded or evaluated here; no curved nonlinear solution is asserted.",
            "Fixed-a modes do not automatically furnish nonzero L2(R13) packets; no physical domain, quantum or full-GU conclusion.",
        ],
    }


ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'lab/process/printed-nonlinear-transfer-certificates.json'

def stable_support_controls():
    import sympy as sp
    from printed_equation_jets_symbol_probe import engine
    e=engine([-1,1,1,1]+[1]*6+[-1]*4)
    checks=[]
    def ck(n,v):
        assert v,n
        checks.append(n)
    def mode(xi,label):
        z={a:sp.I*v for a,v in xi.items()}; q=sum(v*v/e.d[a]for a,v in z.items())
        gamma={(0,1<<a):v/e.d[a]for a,v in z.items()}
        long={(1<<a,1<<b):v*w/e.d[b]/q for a,v in z.items()for b,w in z.items()}
        O=add(e.phi1,scale(-1,long)); V=e.wedge(gamma,O);u=add(scale(12,O),scale(2,V))
        P=e.Phi(e.wedge({(1<<a,0):v for a,v in z.items()},u))
        ck(label+':real_oscillatory_mass_shell',q==-3)
        ck(label+':actual_system_mode',not add(scale(12,u),P))
        ck(label+':realification_grades',all(c.bit_count()in[1,2]for leg,c in u))
        return u
    xp={0:F(2),1:F(4),10:F(3)};xm={0:F(-2),1:F(-4),10:F(3)}
    up=mode(xp,'plus');um=mode(xm,'minus')
    cross=e.Phi(e.wedge(up,um,'comm'))
    ck('mixed_coefficient_is_polarized_Q',cross==e.Phi(add(e.wedge(up,um),e.wedge(um,up))))
    ck('outside_support_nonzero_receiver',cross[(1,1)]==-22080 and len(cross)==29)
    ck('both_spatial_inputs_stable',4**2-3**2-12**2/48==4)
    ck('sum_spatial_frequency_unstable',0**2-6**2-12**2/48==-39)
    ck('sum_full_frequency_pure_normal',{a:xp.get(a,0)+xm.get(a,0)for a in set(xp)|set(xm)}=={0:0,1:0,10:6})
    # Realification gives frequencies +/-xp,+/-xm. Only xp+xm and its
    # ordered partner contribute to the selected pure normal sum.
    keys=[(2,4,3),(-2,-4,3),(-2,-4,-3),(2,4,-3)]
    hits=[(i,j)for i,x in enumerate(keys)for j,y in enumerate(keys)if tuple(a+b for a,b in zip(x,y))==(0,0,6)]
    ck('realification_no_other_sum_pairs',hits==[(0,1),(1,0)])
    # Rank-one common real leg is a nontrivial zero-interaction countercase,
    # already checked in null_hook; do not infer all sectors fail closure.
    return {'checks':checks,'kappa':12,'xi_plus':{str(a):str(v)for a,v in xp.items()},'xi_minus':{str(a):str(v)for a,v in xm.items()},'cross_coefficient':field_record(cross),'receiver':{'form_mask':1,'clifford_mask':1,'value':'-22080'},'scope':'Frozen zero-source actual printed Q; strict all-field stable spatial Fourier cutoff admitting both exact linear modes fails second-order perturbative closure. Not a source-required state rule, growing response, physical quotient or variable-coefficient result.'}

def build():
    ctx=context(ROOT)
    support=stable_support_controls()
    null=null_hook_checks(ctx.e)
    ctl=controls(ctx)
    cl=closure(ctx)
    nxt=next_coefficient(ctx)
    checks=[]
    def ck(n,v):
        assert v,n
        checks.append(n)
    ck('six_space_not_closed',not cl['closed'])
    failures=[x for x in cl['maps']if x['remainder']]
    ck('exact_six_space_failure',[(x['map'],x['indices'])for x in failures]==[('Q',[4,4])])
    ck('actual_fifth_coefficient_exits',nxt['grades']==[1,5] and len(nxt['field'])==264 and len(nxt['six_remainder'])==250)
    t5=read_field(nxt['field']); w={(1,16383):F(1)}; target=(1,6133)
    ck('actual_receiver_parity',6133 .bit_count()==10 and 6133&1 and not 6133&8)
    low=[]
    for order,T in enumerate(ctx.ts+[t5],1):
        v=jacobian(ctx,T,w); val=v.get(target,F())
        ck('actual_receiver_order:'+str(order),val==(F(1296)if order==5 else F()))
        low.append(str(val))
    # Exhaust all columns capable of reaching this receiver by Clifford XOR.
    candidates={(1,6133^8)}
    for b in range(14):
        if b!=3:candidates.add((1<<b,6133^1^8^(1<<b)))
    for key in sorted(candidates):
        ck('actual_cokernel_receiver_column:'+str(key),not symbol(ctx,{3:F(1)},{key:F(1)}).get(target,F()))
    # Authenticate its zero-Jordan input using the explicit volume preimage.
    pre={(1,16383^8):F(-1,2)}
    ck('actual_receiver_zero_Jordan_input',symbol(ctx,{3:F(1)},pre)==w and not symbol(ctx,{3:F(1)},w))
    ck('actual_fifth_real',ctx.e.real_skew(t5))
    nr=null['native_lower_columns']; rn=read_field(nr['c_eta_beta']['sparse_entries'])
    rho=(32,32)
    ck('literal_mode_native_receiver',rn[rho]==F(-1,4))
    # u/n at phase i has real value -2 c(eta) beta, independent of frequency.
    beta={(1<<a,1<<b):F(1,8)*(1 if b==5 else -1)for a in[5,10]for b in[5,10]}
    U=ctx.e.wedge({(0,16):F(-1,4)},beta)
    S=ctx.a.scale(-1,ctx.ts[0]); cross=jacobian(ctx,S,U)
    ck('leading_background_cross',cross==ctx.a.scale(21,U))
    ck('leading_cross_receiver_zero',not cross.get(rho,F()))
    ck('phase_rotated_native_receiver',-2*rn[rho]==F(1,2))
    deps=dict(ctx.bindings)
    for p in ['explorations/conditional-build/printed-equation-jets-and-symbol-2026-11-27.md','explorations/conditional-build/printed-differential-solvability-2026-11-27.md','tests/program-focus/printed_differential_solvability_probe.py','tests/program-focus/printed_equation_jets_symbol_probe.py']:
        deps[p]=digest(ROOT/p)
    return {'schema':'gu-printed-nonlinear-transfer-v1','status':'PASS','probe_sha256':digest(Path(__file__)),'dependencies':deps,'null_hook':null,'jacobian_controls':ctl,'six_space_test':cl,'fifth_coefficient':nxt,'actual_branch_receiver':{'input':field_record(w),'receiver':list(target),'orders_1_to_5':low,'possible_source_columns':len(candidates),'series':'1296*h^5+O(h^6)','scope':'Obstructs first same-leading-scalarizer correction, not nonlinear solutions'},'literal_curved_mode_receiver':{'receiver':list(rho),'native_phase_rotated':'1/2','background_cross_leading':0,'series':'1/2+O(h^2)','scope':'Unchanged frozen-frame first jet about actual small-h branch only'},'stable_support':support,'extra_check_names':checks,'check_count':len(checks)+null['checks']+len(ctl['checks'])+cl['map_count']+len(support['checks']),'scope':'Exact finite native algebra and data. All-xi range and analytic h-series consequences are written proofs. No source-GU, physical ghost, nonlinear curved existence/instability or fullspace L2 nonlinear theorem.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write-certificate',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t=time.monotonic();d=build()
    if a.write_certificate:CERT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(CERT.read_text())==d,'certificate differs'
    print(json.dumps({'status':'PASS','checks':d['check_count'],'six_closed':d['six_space_test']['closed'],'actual_receiver':d['actual_branch_receiver']['orders_1_to_5'],'seconds':time.monotonic()-t}))
