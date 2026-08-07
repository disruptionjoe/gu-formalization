#!/usr/bin/env python3
r"""B2C15O source-coordinate return and selected local-fixture stabilizer gate.

The previous owner theorem used independent total-connection coordinates
``(A, epsilon_red, g)``.  Weinstein's displayed first action instead uses
``(epsilon, varpi, g)`` with

    A_tot = Gamma(g) + varpi,
    B     = Gamma(g) + q_g(epsilon),
    T     = varpi - q_g(epsilon).

This probe first performs that coordinate change exactly in B2C15N's
noncentral rational fixture on the literal epsilon-family Shiab branch.  It
then constructs one trace-reversed-carrier-compatible algebraic fixture with
a realizable four-dimensional metric two-jet and an explicit affine
connection germ.  It computes selected diagonal-Spin coefficient-tuple
stabilizers exactly and checks the right-H, Krein, and C-plus word identities
without using floating point.

The fixture is not yet proved to lie in the image of the GU Zorro/DeWitt
total-space metric construction.  It is not a full action jet, global
section, stationary vacuum, BV quotient, or physical background.  The finite
graph coordinate is not identified with the manuscript's H-valued epsilon;
that Layer-0 bridge remains open.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))


def load_probe(name: str, filename: str):
    spec = spec_from_file_location(name, CHANNEL / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


B15N = load_probe(
    "b2c15n_owner_fixture",
    "eric_curt_wave3d_b2c15n_full_owner_euler_moving_atlas_probe.py",
)
B13 = B15N.B13
B15M = load_probe(
    "b2c15m_native_fixture",
    "eric_curt_wave3d_b2c15m_moving_shiab_exact_g2_weighted_euler_probe.py",
)
B15R = B15M.B15R
B15 = B15R.B15
B14 = B15.B14


FAILURES: list[str] = []
EXACT = 0
SOURCE = 0
TYPE = 0
PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def source_receipt(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE
    SOURCE += 1
    suffix = f" ({detail})" if detail else ""
    print(
        f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}",
        flush=True,
    )
    if not condition:
        FAILURES.append(f"source: {label}")


def type_level(label: str, condition: bool = True, detail: str = "") -> None:
    global TYPE
    TYPE += 1
    suffix = f" ({detail})" if detail else ""
    print(
        f"{'PASS' if condition else 'FAIL'}: type-level - {label}{suffix}",
        flush=True,
    )
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(
        f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}",
        flush=True,
    )
    if false_claim:
        FAILURES.append(f"planted: {label}")


def is_zero(value) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(item) == 0 for item in value)
    return sp.simplify(value) == 0


# ---------------------------------------------------------------------------
# Primary-source collision and Layer 0.


def source_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    transcription = (
        ROOT
        / "explorations/hourly-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
    ).read_text()
    portal = (
        ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md"
    ).read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()

    source_receipt(
        "the displayed action owns source coordinates omega=(epsilon,varpi) and a varpi-direction variation",
        "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in pack
        and "I^B_1(\\epsilon,\\varpi+s\\alpha)" in pack,
        "SOURCE-CONFIRMS; draft pp.43-44 eqs.9.1-9.5",
    )
    source_receipt(
        "the source summary makes varpi relative to nabla-g and T the difference from the gauge-rotated connection",
        "varpi=nabla^varpi-nabla^g" in transcription
        and "T_omega=nabla^varpi-nabla^{g*epsilon}" in transcription,
        "SOURCE-CONFIRMS; draft pp.56-57 eqs.12.4-12.7",
    )
    source_receipt(
        "literal equations 9.2-9.3 display an epsilon-family contraction; equality with equation 9.4's odot_omega remains unverified",
        "circledot_e" in transcription
        and "displayed Shiab operator family" in transcription,
        "SOURCE-IMPLIES-FOR-LITERAL-EQ9.2-9.3-EPSILON-FAMILY; EQ9.4 IDENTIFICATION UNVERIFIED",
    )
    source_receipt(
        "the Zorro chain runs from the X metric through Levi-Civita to the Y metric and spin connection",
        "02:23:30" in portal and "02:23:52" in portal,
        "SOURCE-CONFIRMS; Portal/Oxford 02:23:30-02:23:52",
    )
    source_receipt(
        "the modern interview places gauge-rotated Levi-Civita in the contorsion slot",
        "02:19:17" in toe and "02:20:33" in toe,
        "SOURCE-CONFIRMS; TOE 02:19:17-02:20:33",
    )


def layer_zero_checks() -> None:
    type_level("source varpi, total A=Gamma+varpi, reference B=Gamma+q, and distortion T=varpi-q are four different objects")
    type_level("holding source varpi fixed while varying g is not holding total A fixed")
    type_level("the manuscript H-valued epsilon and the repository quotient reduction owner epsilon_red are homonyms until a tangent map is built")
    type_level("a selected algebraic coefficient fixture, a Zorro/DeWitt total-space jet, a global action background, and a stationary physical vacuum are different grades")
    type_level("selected diagonal-Spin tuple stabilizer, full ambient/action-jet stabilizer, conormal-family stabilizer, and global gauge automorphisms are different objects")
    type_level("the source (7,7) complex presentation and active trace-reversed (9,5) right-H/Krein carrier remain a real-form fork")


# ---------------------------------------------------------------------------
# Exact source-coordinate return in the noncentral owner fixture.


x = B13.x
varpi = sp.Matrix([sp.Function("varpi0")(x), sp.Function("varpi1")(x)])
dvarpi = sp.Matrix([sp.Function("dvarpi0")(x), sp.Function("dvarpi1")(x)])

# The B2C15N graph splits uniquely in its declared fixture into the pure
# metric-origin part Gamma and the remaining q graph.  This is a finite
# coordinate-chain certificate, not the native epsilon map.
GAMMA = B15N.GRAPH_H0 * B13.g + B15N.GRAPH_H1 * sp.diff(B13.g, x)
Q_GRAPH = sp.expand(B15N.GRAPH_B - GAMMA)
SOURCE_SUBS = {
    B13.a[index]: varpi[index] + GAMMA[index] for index in range(2)
}


def source_pull(expr):
    return expr.subs(SOURCE_SUBS, simultaneous=True).doit().expand()


L_SOURCE = source_pull(B15N.L_OWNER)
SOURCE_OWNERS = (varpi[0], varpi[1], B13.z, B13.g)
SOURCE_VARIATIONS = (dvarpi[0], dvarpi[1], B13.dz, B13.dg)


def derivative_order(expr: sp.Expr, field) -> int:
    order = 0 if expr.has(field) else -1
    for derivative in expr.atoms(sp.Derivative):
        if derivative.expr == field and all(variable == x for variable in derivative.variables):
            order = max(order, len(derivative.variables))
    return order


def euler_boundary(lagrangian: sp.Expr):
    eulers = {}
    packet = {}
    theta = sp.Integer(0)
    orders = {}
    for field, variation in zip(SOURCE_OWNERS, SOURCE_VARIATIONS):
        order = derivative_order(lagrangian, field)
        orders[str(field.func)] = order
        partials = {0: sp.diff(lagrangian, field)}
        for degree in range(1, order + 1):
            partials[degree] = sp.diff(lagrangian, sp.diff(field, x, degree))
        euler = partials[0]
        for degree in range(1, order + 1):
            euler += (-1) ** degree * sp.diff(partials[degree], x, degree)
        eulers[field] = sp.expand(euler)
        packet[field] = {}
        for jet in range(order):
            momentum = sp.Integer(0)
            for degree in range(jet + 1, order + 1):
                momentum += (-1) ** (degree - jet - 1) * sp.diff(
                    partials[degree], x, degree - jet - 1
                )
            packet[field][jet] = sp.expand(momentum)
            theta += packet[field][jet] * sp.diff(variation, x, jet)
    return orders, eulers, packet, sp.expand(theta)


SOURCE_ORDERS, SOURCE_EULERS, SOURCE_PACKET, SOURCE_THETA = euler_boundary(L_SOURCE)
SOURCE_E_T = source_pull(B15N.E_T)
FIXED_A_Z = source_pull(B15N.OWNER_EULERS[B13.z])
FIXED_A_G = source_pull(B15N.OWNER_EULERS[B13.g])
GAMMA_ADJOINT_E_T = sp.expand(
    (B15N.GRAPH_H0.T * SOURCE_E_T)[0]
    - sp.diff((B15N.GRAPH_H1.T * SOURCE_E_T)[0], x)
)
DGAMMA_VARIATION = sp.expand(
    B15N.GRAPH_H0 * B13.dg + B15N.GRAPH_H1 * sp.diff(B13.dg, x)
)
FIXED_A_THETA_IN_SOURCE = sp.expand(
    source_pull(B15N.OWNER_THETA)
    .subs(
        {
            B13.da[index]: dvarpi[index] + DGAMMA_VARIATION[index]
            for index in range(2)
        },
        simultaneous=True,
    )
    .doit()
)
GAMMA_GREEN_COMPANION = sp.expand(
    (B15N.GRAPH_H1.T * SOURCE_E_T)[0] * B13.dg
)


def source_coordinate_checks() -> None:
    exact(
        "on the literal epsilon-family branch the source varpi Euler covector is exactly E_T",
        all(
            is_zero(SOURCE_EULERS[varpi[index]] - SOURCE_E_T[index])
            for index in range(2)
        ),
    )
    exact(
        "the finite q-owner return agrees in fixed-A and fixed-varpi coordinates because Gamma is q-independent",
        is_zero(SOURCE_EULERS[B13.z] - FIXED_A_Z),
    )
    exact(
        "the source fixed-varpi metric return equals the fixed-A return plus (D_g Gamma)^! E_T",
        is_zero(SOURCE_EULERS[B13.g] - FIXED_A_G - GAMMA_ADJOINT_E_T),
    )
    exact(
        "the source-coordinate metric correction is live on the noncentral fixture",
        not is_zero(GAMMA_ADJOINT_E_T),
    )
    exact(
        "the metric correction carries its isolated exact Green companion",
        is_zero(
            SOURCE_THETA
            - FIXED_A_THETA_IN_SOURCE
            - GAMMA_GREEN_COMPANION
        )
        and not is_zero(GAMMA_GREEN_COMPANION),
    )
    reject(
        "reuse the B2C15N fixed-A metric Euler equation as the source fixed-varpi equation",
        is_zero(GAMMA_ADJOINT_E_T),
    )
    reject(
        "add a second varpi owner rather than pricing a rival D_varpi-odot response inside the existing varpi equation",
        len(SOURCE_OWNERS) != 4,
    )

    realized = tuple(
        tuple(derivative_order(SOURCE_EULERS[out], incoming) for incoming in SOURCE_OWNERS)
        for out in SOURCE_OWNERS
    )
    grouped = (
        (
            max(realized[i][j] for i in (0, 1) for j in (0, 1)),
            max(realized[i][2] for i in (0, 1)),
            max(realized[i][3] for i in (0, 1)),
        ),
        (
            max(realized[2][j] for j in (0, 1)),
            realized[2][2],
            realized[2][3],
        ),
        (
            max(realized[3][j] for j in (0, 1)),
            realized[3][2],
            realized[3][3],
        ),
    )
    exact(
        "the source-coordinate realized order table is recomputed rather than imported from fixed-A coordinates",
        grouped == ((1, 2, 2), (2, 2, 3), (2, 3, 2))
        and not is_zero(SOURCE_EULERS[B13.g] - FIXED_A_G),
        f"full={realized}; grouped={grouped}",
    )

    background = dict(B13.BASE_POLYS)
    gamma_background = sp.Matrix(
        [item.subs(background, simultaneous=True).doit().expand() for item in GAMMA]
    )
    for index in range(2):
        background[varpi[index]] = sp.expand(
            background[B13.a[index]] - gamma_background[index]
        )
    variations = {
        dvarpi[0]: B13.V1_POLYS[B13.da[0]],
        dvarpi[1]: B13.V1_POLYS[B13.da[1]],
        B13.dz: B13.V1_POLYS[B13.dz],
        B13.dg: B13.V1_POLYS[B13.dg],
    }
    substitutions = {**background, **variations}
    direct = B13.gateaux(
        L_SOURCE,
        {
            varpi[0]: dvarpi[0],
            varpi[1]: dvarpi[1],
            B13.z: B13.dz,
            B13.g: B13.dg,
        },
    )
    bulk = sum(
        SOURCE_EULERS[field] * variation
        for field, variation in zip(SOURCE_OWNERS, SOURCE_VARIATIONS)
    )
    evaluate = lambda expr: expr.subs(substitutions, simultaneous=True).doit().expand()
    direct_value = sp.integrate(evaluate(direct), (x, 0, 1))
    bulk_value = sp.integrate(evaluate(bulk), (x, 0, 1))
    theta_value = evaluate(SOURCE_THETA)
    boundary_value = theta_value.subs(x, 1) - theta_value.subs(x, 0)
    exact(
        "the source-coordinate owner tuple satisfies its exact bulk-plus-preboundary identity",
        is_zero(direct_value - bulk_value - boundary_value) and boundary_value != 0,
        f"direct={direct_value}; bulk={bulk_value}; boundary={boundary_value}",
    )

    factor = x**3 * (1 - x) ** 3
    first_values = (1 + x, 2 - x, 1 + 2 * x, -1 + x)
    second_values = (2 - x, 1 + x**2, -2 + x, 1 + 3 * x)
    first = {
        field: factor * value for field, value in zip(SOURCE_OWNERS, first_values)
    }
    second = {
        field: factor * value for field, value in zip(SOURCE_OWNERS, second_values)
    }
    d_first = sp.Matrix(
        [B13.gateaux(SOURCE_EULERS[field], first) for field in SOURCE_OWNERS]
    ).subs(background, simultaneous=True).doit().expand()
    d_second = sp.Matrix(
        [B13.gateaux(SOURCE_EULERS[field], second) for field in SOURCE_OWNERS]
    ).subs(background, simultaneous=True).doit().expand()
    v_first = sp.Matrix(list(first.values()))
    v_second = sp.Matrix(list(second.values()))
    forward = sp.integrate((v_second.T * d_first)[0], (x, 0, 1))
    reverse = sp.integrate((v_first.T * d_second)[0], (x, 0, 1))
    exact(
        "the corrected fixed-varpi owner linearization obeys exact integrated Helmholtz reciprocity",
        is_zero(forward - reverse) and forward != 0,
        f"paired_value={forward}",
    )
    fixed_a_reused = sp.Matrix(
        [SOURCE_E_T[0], SOURCE_E_T[1], FIXED_A_Z, FIXED_A_G]
    )
    wrong_first = fixed_a_reused.applyfunc(
        lambda equation: B13.gateaux(equation, first)
    ).subs(background, simultaneous=True).doit().expand()
    wrong_second = fixed_a_reused.applyfunc(
        lambda equation: B13.gateaux(equation, second)
    ).subs(background, simultaneous=True).doit().expand()
    wrong_defect = sp.simplify(
        sp.integrate((v_second.T * wrong_first - v_first.T * wrong_second)[0], (x, 0, 1))
    )
    exact(
        "reusing the fixed-A metric equation in source coordinates has the preregistered nonzero Helmholtz defect",
        wrong_defect == sp.Rational(79042325, 279351072),
        f"defect={wrong_defect}",
    )
    reject(
        "accept the fixed-A metric equation as the source fixed-varpi equation despite its Helmholtz defect",
        wrong_defect == 0,
    )


# ---------------------------------------------------------------------------
# Exact native (9,5) word involutions.


N = B14.N
ETA = B14.ETA
TRACE_INDEX = B14.TRACE_INDEX
SPLIT_ORDER = (0, 1, 2, 9, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13)
ORIGINAL_TO_SPLIT = {original: split for split, original in enumerate(SPLIT_ORDER)}


def mask_from_original(indices) -> int:
    return sum(1 << ORIGINAL_TO_SPLIT[index] for index in indices)


BETA_MASK = mask_from_original(range(9))
RIGHT_H_MASK = mask_from_original((1, 3, 5, 7, 10, 12))
C_PLUS_MASK = mask_from_original(tuple(index for index in range(14) if index % 2 == 0))


def blade_transform(mask: int, kind: str) -> tuple[int, F]:
    selected = B14.bits(mask)
    degree = len(selected)
    reverse = F(-1 if (degree * (degree - 1) // 2) % 2 else 1)
    if kind == "conjugate":
        sign = F(1)
        for split in selected:
            original = SPLIT_ORDER[split]
            sign *= -1 if original % 2 else 1
            sign *= -1 if original >= 9 else 1
        return mask, sign
    if kind == "transpose":
        sign = reverse
        for split in selected:
            sign *= -1 if SPLIT_ORDER[split] % 2 else 1
        return mask, sign
    if kind == "dagger":
        sign = reverse
        for split in selected:
            sign *= ETA[split]
        return mask, sign
    raise ValueError(kind)


def cliff_transform(value, kind: str):
    result = {}
    for mask, coefficient in value.items():
        out_mask, sign = blade_transform(mask, kind)
        result[out_mask] = result.get(out_mask, F(0)) + coefficient * sign
    return B14.clean_cliff(result)


def cliff_sub(left, right):
    return B14.cliff_add(left, B14.cliff_scale(right, F(-1)))


def word_compatible(value) -> bool:
    return word_compatible_variant(value)


def word_compatible_variant(
    value,
    *,
    beta_mask: int = BETA_MASK,
    right_h_mask: int = RIGHT_H_MASK,
    c_plus_mask: int = C_PLUS_MASK,
    corrupt_transform: str | None = None,
) -> bool:
    beta = {beta_mask: F(1)}
    right_h = {right_h_mask: F(1)}
    c_plus = {c_plus_mask: F(1)}
    conjugate = value if corrupt_transform == "conjugate" else cliff_transform(value, "conjugate")
    dagger = value if corrupt_transform == "dagger" else cliff_transform(value, "dagger")
    transpose = value if corrupt_transform == "transpose" else cliff_transform(value, "transpose")
    right_defect = cliff_sub(
        B14.cliff_mul(value, right_h),
        B14.cliff_mul(right_h, conjugate),
    )
    krein_defect = B14.cliff_add(
        B14.cliff_mul(beta, value),
        B14.cliff_mul(dagger, beta),
    )
    charge_defect = B14.cliff_add(
        B14.cliff_mul(transpose, c_plus),
        B14.cliff_mul(c_plus, value),
    )
    return not right_defect and not krein_defect and not charge_defect


def form_compatible(value) -> bool:
    return all(word_compatible(coefficient) for coefficient in value.values())


# ---------------------------------------------------------------------------
# A trace-reversed-compatible algebraic fixture and exact stabilizer kernels.


BASE = tuple(range(4))
FIBRE = tuple(range(4, 14))


def so_generator(left: int, right: int) -> sp.Matrix:
    value = sp.zeros(N)
    value[left, right] = 1
    value[right, left] = -ETA[left] * ETA[right]
    return value


SO_BASIS = tuple(
    (left, right, so_generator(left, right))
    for left, right in combinations(range(N), 2)
)


def spin_word(left: int, right: int):
    return {((1 << left) | (1 << right)): F(ETA[right], 2)}


def canonical_key(indices):
    if len(set(indices)) != len(indices):
        return None, F(0)
    inversions = sum(indices[i] > indices[j] for i in range(len(indices)) for j in range(i + 1, len(indices)))
    return tuple(sorted(indices)), F(-1 if inversions % 2 else 1)


def infinitesimal_form_action(value, left: int, right: int, matrix: sp.Matrix):
    generator = spin_word(left, right)
    # Active spin action is [K, value].  B14.form_commutator uses the passive
    # [value,K] convention needed in its moving-frame identities, so reverse
    # the order here before combining it with the covector pullback action.
    result = B14.clean_form(
        {
            key: B14.cliff_comm(generator, coefficient)
            for key, coefficient in value.items()
        }
    )
    external = {}
    for key, coefficient in value.items():
        for slot, old in enumerate(key):
            for new in range(N):
                scalar = -F(matrix[old, new])
                if not scalar:
                    continue
                candidate = list(key)
                candidate[slot] = new
                out_key, sign = canonical_key(candidate)
                if out_key is None:
                    continue
                external[out_key] = B14.cliff_add(
                    external.get(out_key, {}),
                    B14.cliff_scale(coefficient, scalar * sign),
                )
    return B14.add_forms(result, external)


def constant_curvature_form():
    # In an orthonormal normal frame the constant-curvature LC two-form is the
    # metric identification Lambda2(base*) -> spin(base).  In the orthonormal
    # coframe convention used by the Clifford action its spin lift is
    # (1/2) gamma_left gamma_right.  The metric signs enter through the
    # curvature endomorphism and spin generator and cancel in this component.
    return {
        (left, right): B14.cliff_scale(spin_word(left, right), F(ETA[right]))
        for left, right in combinations(BASE, 2)
    }


F_B0 = constant_curvature_form()


def riemann0(a: int, b: int, c: int, d: int) -> F:
    metric = lambda left, right: F(ETA[left]) if left == right else F(0)
    return metric(a, c) * metric(b, d) - metric(a, d) * metric(b, c)


def active_native_blades(grade: int):
    return tuple(
        mask
        for mask in B15.GRADE_MASKS[grade]
        if word_compatible({mask: F(1)})
    )


GRADE3_ACTIVE = active_native_blades(3)
NONCOMMUTING_PAIRS = tuple(
    (left, right)
    for left, right in combinations(GRADE3_ACTIVE, 2)
    if B14.cliff_comm({left: F(1)}, {right: F(1)})
)
if len(NONCOMMUTING_PAIRS) < 2:
    raise RuntimeError("native grade-three noncommuting plant family unexpectedly empty")


def distortion_from_pair(pair):
    return B14.one_form(
        {
            0: {pair[0]: F(1)},
            1: {pair[1]: F(1)},
        }
    )


T0 = distortion_from_pair(NONCOMMUTING_PAIRS[0])
T1_HELDOUT = distortion_from_pair(NONCOMMUTING_PAIRS[1])
Q_T0 = B14.q_sym(T0, T0)


def affine_connection_germ(curvature):
    """Return the origin value and first derivative of B for radial gauge."""
    value = {index: {} for index in range(N)}
    derivative = {}
    for (left, right), coefficient in curvature.items():
        derivative[(left, right)] = B14.cliff_add(
            derivative.get((left, right), {}),
            B14.cliff_scale(coefficient, F(1, 2)),
        )
        derivative[(right, left)] = B14.cliff_add(
            derivative.get((right, left), {}),
            B14.cliff_scale(coefficient, F(-1, 2)),
        )
    return value, derivative


def curvature_at_origin(value, derivative):
    result = {}
    for left, right in combinations(range(N), 2):
        coefficient = B14.cliff_add(
            derivative.get((left, right), {}),
            B14.cliff_scale(derivative.get((right, left), {}), F(-1)),
            B14.cliff_comm(value.get(left, {}), value.get(right, {})),
        )
        if coefficient:
            result[(left, right)] = coefficient
    return B14.clean_form(result)


def covariant_distortion_at_origin(connection_value, distortion, derivative=None):
    derivative = derivative or {}
    result = {}
    for left, right in combinations(range(N), 2):
        coefficient = B14.cliff_add(
            derivative.get((left, right), {}),
            B14.cliff_scale(derivative.get((right, left), {}), F(-1)),
            B14.cliff_comm(connection_value.get(left, {}), distortion.get((right,), {})),
            B14.cliff_scale(
                B14.cliff_comm(connection_value.get(right, {}), distortion.get((left,), {})),
                F(-1),
            ),
        )
        if coefficient:
            result[(left, right)] = coefficient
    return B14.clean_form(result)


B_VALUE0, DB_VALUE0 = affine_connection_germ(F_B0)
F_B_FROM_GERM = curvature_at_origin(B_VALUE0, DB_VALUE0)
DB_T0 = covariant_distortion_at_origin(B_VALUE0, T0)
F_A0 = B14.add_forms(F_B_FROM_GERM, DB_T0, Q_T0)
NONZERO_DT_PLANT = {(0, 1): {1: F(1)}}
DB_T_PLANT = covariant_distortion_at_origin(B_VALUE0, T0, NONZERO_DT_PLANT)
F_A_INDEPENDENT_PLANT = F_B0
S_FB0 = B14.trace_line_source(F_B0)
S_QT0 = B14.trace_line_source(Q_T0)


OBSERVATION_PROJECTOR = sp.diag(*(1 if index in BASE else 0 for index in range(N)))
TRACE_VECTOR = sp.Matrix([1 if index == TRACE_INDEX else 0 for index in range(N)])
XI = sp.Matrix([1 if index == 0 else 0 for index in range(N)])


def flatten_matrix(value: sp.Matrix):
    return tuple(F(item) for item in value)


def flatten_form(value):
    return tuple(
        coefficient
        for key in sorted(value)
        for mask, coefficient in sorted(value[key].items())
        for _tag in ((key, mask),)
    )


def form_coordinate_dict(value):
    return {
        (key, mask): coefficient
        for key, cliff in value.items()
        for mask, coefficient in cliff.items()
    }


def stabilizer_dimension(
    include_projector: bool,
    include_trace: bool,
    forms=(),
    include_xi: bool = False,
    action_fn=infinitesimal_form_action,
):
    columns = []
    all_form_keys = set()
    actions_by_generator = []
    for left, right, matrix in SO_BASIS:
        actions = tuple(
            action_fn(value, left, right, matrix) for value in forms
        )
        actions_by_generator.append((matrix, actions))
        for action in actions:
            all_form_keys.update(form_coordinate_dict(action))
    ordered_form_keys = tuple(sorted(all_form_keys))
    for matrix, actions in actions_by_generator:
        column = []
        if include_projector:
            column.extend(flatten_matrix(matrix * OBSERVATION_PROJECTOR - OBSERVATION_PROJECTOR * matrix))
        if include_trace:
            column.extend(flatten_matrix(matrix * TRACE_VECTOR))
        if include_xi:
            column.extend(flatten_matrix(matrix * XI))
        for action in actions:
            coordinates = form_coordinate_dict(action)
            column.extend(coordinates.get(key, F(0)) for key in ordered_form_keys)
        columns.append(column)
    matrix = sp.Matrix.hstack(*(sp.Matrix(column) for column in columns))
    orbit_rank = matrix.rank()
    return len(SO_BASIS) - orbit_rank, orbit_rank


def grade_support(value):
    return tuple(sorted({mask.bit_count() for cliff in value.values() for mask in cliff}))


def infinitesimal_internal_only(value, left: int, right: int, _matrix: sp.Matrix):
    generator = spin_word(left, right)
    return B14.clean_form(
        {
            key: B14.cliff_comm(generator, coefficient)
            for key, coefficient in value.items()
        }
    )


def native_matrix_max_defect(values) -> float:
    original_gammas, _ = B14.sym2.native_gammas()
    gammas = [original_gammas[index] for index in SPLIT_ORDER]
    beta = B14.matrix_product(original_gammas[:9])
    right_h = B14.matrix_product(
        [original_gammas[index] for index in (1, 3, 5, 7, 10, 12)]
    )
    c_plus = B14.matrix_product(
        [original_gammas[index] for index in range(14) if index % 2 == 0]
    )
    maximum = 0.0
    for value in values:
        for coefficient in value.values():
            matrix = B14.cliff_matrix(coefficient, gammas)
            maximum = max(
                maximum,
                B14.max_abs(matrix @ right_h - right_h @ matrix.conj()),
                B14.max_abs(beta @ matrix + matrix.conj().T @ beta),
                B14.max_abs(matrix.T @ c_plus + c_plus @ matrix),
            )
    return maximum


def native_background_checks() -> None:
    exact(
        "the selected carrier metric is the trace-reversed (9,5) split with Lorentzian base and (6,4) fibre",
        tuple(ETA[index] for index in BASE) == (1, 1, 1, -1)
        and sum(ETA[index] > 0 for index in FIBRE) == 6
        and sum(ETA[index] < 0 for index in FIBRE) == 4
        and ETA[TRACE_INDEX] == -1,
    )
    reject(
        "replace the trace-reversed fibre by raw Frobenius signature (7,3)",
        sum(ETA[index] > 0 for index in FIBRE) == 7,
    )
    exact(
        "the hostile raw-Frobenius recomputation gives total inertia (10,4), not the active trace-reversed (9,5)",
        (3 + 7, 1 + 3) == (10, 4) and (10, 4) != (9, 5),
    )
    exact(
        "the constant-curvature base seed is an algebraic Riemann tensor and hence a realizable four-dimensional normal-coordinate metric two-jet",
        all(
            riemann0(a, b, c, d) == -riemann0(b, a, c, d)
            and riemann0(a, b, c, d) == -riemann0(a, b, d, c)
            and riemann0(a, b, c, d) == riemann0(c, d, a, b)
            and riemann0(a, b, c, d)
            + riemann0(a, c, d, b)
            + riemann0(a, d, b, c)
            == 0
            for a in BASE
            for b in BASE
            for c in BASE
            for d in BASE
        ),
    )
    exact(
        "the unit-curvature Riemann convention spin-lifts to one-half gamma_left gamma_right",
        all(
            F_B0[(left, right)]
            == {((1 << left) | (1 << right)): F(1, 2)}
            for left, right in combinations(BASE, 2)
        ),
    )
    exact(
        "the base constant-curvature two-jet is invariant under every base Lorentz generator",
        all(
            not infinitesimal_form_action(F_B0, left, right, matrix)
            for left, right, matrix in SO_BASIS
            if left in BASE and right in BASE
        ),
    )
    exact(
        "the preregistered lexicographic distortion uses two compatible noncommuting native grade-three generators",
        form_compatible(T0)
        and B14.cliff_comm(T0[(0,)], T0[(1,)])
        and Q_T0,
        f"pair={NONCOMMUTING_PAIRS[0]}",
    )
    exact(
        "the explicit affine B germ and constant T germ derive F_B, D_B T=0, and F_A=F_B+q(T,T) at the origin",
        F_B_FROM_GERM == F_B0
        and not DB_T0
        and F_A0 == B14.add_forms(F_B0, Q_T0),
    )
    reject(
        "retain the shortened F_A identity after planting a nonzero D_B T term",
        not DB_T_PLANT,
    )
    reject(
        "assign F_A independently as F_B while the distortion bracket is live",
        F_A_INDEPENDENT_PLANT == F_A0,
    )
    exact(
        "the selected fixture has the exact reported Clifford-grade supports",
        grade_support(F_B0) == (2,)
        and grade_support(Q_T0) == (2,)
        and grade_support(F_A0) == (2,)
        and grade_support(S_FB0) == (2,)
        and grade_support(S_QT0) == (6,),
        f"supports F_B={grade_support(F_B0)}; qTT={grade_support(Q_T0)}; S(F_B)={grade_support(S_FB0)}; S(qTT)={grade_support(S_QT0)}",
    )
    exact(
        "every selected fixture and contraction coefficient satisfies exact right-H, Krein-skew, and C-plus word identities",
        all(form_compatible(value) for value in (F_B0, T0, Q_T0, F_A0, S_FB0, S_QT0)),
    )
    exact(
        "the independent native 128-by-128 comparator has zero right-H, Krein, and C-plus defect on every selected coefficient",
        native_matrix_max_defect((F_B0, T0, Q_T0, F_A0, S_FB0, S_QT0)) < 1.0e-10,
    )
    representative = T0[(0,)]
    hilbert_plant = T0[(1,)]
    reject(
        "replace the Krein adjoint by the positive-Hilbert adjoint on the selected grade-three word",
        not B14.cliff_add(hilbert_plant, cliff_transform(hilbert_plant, "dagger")),
    )
    selected_words = tuple(
        coefficient
        for value in (F_B0, T0, Q_T0, F_A0, S_FB0, S_QT0)
        for coefficient in value.values()
    )
    for transform_kind in ("conjugate", "dagger", "transpose"):
        reject(
            f"omit the {transform_kind} word sign in the exact reality involution",
            all(
                word_compatible_variant(word, corrupt_transform=transform_kind)
                for word in selected_words
            ),
        )
    reject(
        "replace the Krein beta word by a one-generator-corrupted word",
        all(
            word_compatible_variant(word, beta_mask=BETA_MASK ^ 1)
            for word in selected_words
        ),
    )
    reject(
        "replace the right-H word by a one-generator-corrupted word",
        all(
            word_compatible_variant(word, right_h_mask=RIGHT_H_MASK ^ 1)
            for word in selected_words
        ),
    )
    reject(
        "replace the C-plus word by a one-generator-corrupted word",
        all(
            word_compatible_variant(word, c_plus_mask=C_PLUS_MASK ^ 1)
            for word in selected_words
        ),
    )
    reject(
        "admit a forbidden grade-one Clifford word into the selected real coefficient class",
        word_compatible({1: F(1)}),
    )
    # A pure imaginary phase breaks the real C-plus/Krein class in the
    # independent complex matrix realization even when the unphased word is valid.
    original_gammas, _ = B14.sym2.native_gammas()
    split_gammas = [original_gammas[index] for index in SPLIT_ORDER]
    representative_matrix = 1j * B14.cliff_matrix(representative, split_gammas)
    beta_matrix = B14.matrix_product(original_gammas[:9])
    reject(
        "admit an unpriced imaginary phase as if it preserved the selected Krein-real class",
        B14.max_abs(
            beta_matrix @ representative_matrix
            + representative_matrix.conj().T @ beta_matrix
        )
        < 1.0e-10,
    )

    split_dim, _ = stabilizer_dimension(True, False)
    trace_dim, _ = stabilizer_dimension(True, True)
    curvature_dim, _ = stabilizer_dimension(True, True, (F_B0,))
    tuple_dim, _ = stabilizer_dimension(True, True, (F_B0, T0, F_A0, S_FB0, S_QT0))
    conormal_dim, _ = stabilizer_dimension(
        True, True, (F_B0, T0, F_A0, S_FB0, S_QT0), True
    )
    heldout_dim, _ = stabilizer_dimension(
        True, True, (F_B0, T1_HELDOUT, B14.add_forms(F_B0, B14.q_sym(T1_HELDOUT, T1_HELDOUT)))
    )
    exact(
        "the observation split and trace line have the expected exact Lie stabilizer dimensions",
        split_dim == 51 and trace_dim == 42,
        f"split={split_dim}; trace={trace_dim}",
    )
    exact(
        "the constant-curvature jet preserves the geometric 42-dimensional stabilizer before distortion is added",
        curvature_dim == 42,
        f"curvature_stabilizer={curvature_dim}",
    )
    internal_only_dim, _ = stabilizer_dimension(
        True,
        True,
        (F_B0, T0, F_A0, S_FB0, S_QT0),
        action_fn=infinitesimal_internal_only,
    )
    exact(
        "the selected diagonal-Spin coefficient tuple and its one non-null xi=e0 intersection have the exact preregistered kernel dimensions",
        tuple_dim == 36 and conormal_dim == 36 and heldout_dim == 28,
        f"tuple={tuple_dim}; tuple_and_xi_e0={conormal_dim}; heldout_tuple={heldout_dim}",
    )
    reject("use the trace-line isotropy dimension as the selected tuple isotropy dimension", tuple_dim == 42)
    reject(
        "omit the external covector pullback term from the diagonal-Spin stabilizer action",
        internal_only_dim == tuple_dim,
    )
    reject("force two algebraic candidate tuples with different isotropy dimensions into one isotropy stratum", heldout_dim == tuple_dim)
    reject("promote the local Lie stabilizer to a disconnected global stabilizer group", False)


def scope_checks() -> None:
    type_level("the constructed object is a trace-reversed-carrier-compatible algebraic fixture with a realizable four-dimensional metric two-jet and explicit affine B/T germs; membership in the GU Zorro/DeWitt total-space jet image remains open")
    type_level("the finite source-coordinate graph q is a chain-rule surrogate only; it does not identify source epsilon with epsilon_red")
    type_level("D_varpi Shiab=0 holds on the literal equations-9.2-to-9.3 epsilon-family branch; equality with equation 9.4's odot_omega and rival selection remain open")
    type_level("the exact native word table is stronger than the retained 128x128 floating comparator but does not supply the missing (7,7)-to-(9,5) source port")
    type_level("the source-coordinate correction changes the metric equation even though the realized order table happens to survive on this fixture; neither fact may be imported without recomputation")
    type_level("a local ten-owner metric response is not a global Y-to-X metric Euler pushforward")
    type_level("no BV quotient, Green domain, hyperbolicity, positive symmetrizer, vacuum, Standard Model, generation, cosmological, dark-matter, or PP3 claim follows")
    type_level("P1/P2/P3 remain unchanged and supply no coordinate map, background jet, stabilizer, coefficient, or domain")
    type_level("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    reject("use one selected-fixture support calculation as a complete native support theorem", grade_support(S_QT0) != (6,))
    reject("call the selected algebraic fixture a stationary physical vacuum", bool(DB_T0))
    reject("silently identify the source (7,7) and active (9,5) real forms", tuple(ETA) == (1,) * 7 + (-1,) * 7)


def main() -> None:
    print("=" * 96)
    print("B2C15O SOURCE-COORDINATE RETURN / SELECTED (9,5) COEFFICIENT-FIXTURE STABILIZER GATE")
    print("=" * 96)
    source_checks()
    layer_zero_checks()
    source_coordinate_checks()
    native_background_checks()
    scope_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source receipts + "
        f"{TYPE} type-level + {PLANTED} planted = {total}",
        flush=True,
    )
    if FAILURES:
        print("FAILURES:", flush=True)
        for failure in FAILURES:
            print(f"  - {failure}", flush=True)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
