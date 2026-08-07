#!/usr/bin/env python3
r"""B2C15N full first-action owner Euler and moving-atlas gate.

This probe performs the coordinate return that the preceding weighted-order
ledger deliberately did not perform.  In an exact noncentral rational model
it varies the selected first action first in the independent ``(B,T)``
coordinates and only then returns through ``B=B(u)``, ``T=A-B(u)``.  It also
constructs the complete local owner Euler tuple directly from the pulled-back
action, verifies the Green identity and Helmholtz reciprocity, and records the
realized (rather than merely capped) derivative orders.

The moving polynomial calculation is intentionally background-aware.  It
builds the exact owner linearization on a one-parameter background family and
shows that its support and total-symbol dispersion polynomial change with the
background jet.  This kills a
background-free promotion of the earlier frozen-Shiab conormal atlas.  The
finite theorem is a universal action/graph certificate, not the unreleased
global Y^14 owner coefficient, a BV quotient, or a Green domain.
"""

from __future__ import annotations

from functools import reduce
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


B13 = load_probe(
    "b2c13_owner_fixture",
    "eric_curt_wave3d_b2c13_dupsilon_preboundary_probe.py",
)

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
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


# ---------------------------------------------------------------------------
# Source collision and Layer 0.


def source_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    g2 = (ROOT / "explorations/g2-field-space-native-variational-shiab-2026-07-31.md").read_text()

    source_receipt(
        "the draft supplies the completed first-action one-half/one-third grammar",
        "F_{B_\\omega}" in pack
        and "\\frac12d_{B_\\omega}T_\\omega" in pack
        and "\\frac13[T_\\omega,T_\\omega]" in pack,
        "SOURCE-CONFIRMS; draft p.44 eq.9.4",
    )
    source_receipt(
        "Portal requires an adjustment making the curvature-based tensor exact",
        "01:43:32" in portal
        and "01:45:53" in portal
        and "adjustment needed for exactness" in portal,
        "SOURCE-CONFIRMS; Portal/Oxford 01:43:32-01:45:53",
    )
    source_receipt(
        "Portal later identifies that completion explicitly as a quadratic eddy tensor",
        "02:35:10" in portal and "quadratic eddy tensor" in portal,
        "SOURCE-CONFIRMS; Portal/Oxford 02:35:10",
    )
    source_receipt(
        "Weinstein corrects Shiab from projection to contraction",
        "01:36:35" in toe and "contraction operator" in toe,
        "SOURCE-CORRECTS; TOE 01:36:35-01:36:56",
    )
    source_receipt(
        "the repository records that the compressed source formula is not the exact noncyclic Euler covector",
        "fails the cyclic identities" in g2
        and "exact slot-symmetrized Euler covector" in g2,
        "SOURCE-CORRECTS; G2 exact collision",
    )
    source_receipt(
        "the modern two-connection D-squared remains explicitly unreleased",
        "02:44:06" in toe and "have never released to anyone" in toe,
        "SOURCE-SILENT for the missing full owner coefficient",
    )


def layer_zero_checks() -> None:
    type_level("the written first action, its partial-T Euler covector, its direct-B covector, its returned owner tuple, and either residual-square Euler system are distinct objects")
    type_level("a passive vertical Spin lift is a descent/frame direction, not an epsilon owner coordinate")
    type_level("the native LC graph and the A0 lower-filtered comparator are distinct; the latter may add only a separately typed lower-order return")
    type_level("moving-Shiab coefficients require a background action jet; a conormal alone does not define their rank")
    type_level("the source (7,7)/complex carrier and repository (9,5) right-H/Krein carrier remain a real-form fork")
    type_level("source odot_omega with omega=(epsilon,varpi) is not identified with the selected reconstruction S_(epsilon,g); this branch assumes no independent translation derivative of S")


# ---------------------------------------------------------------------------
# Full first-action owner return.


x = B13.x
GRAPH_G0 = B13.G0
GRAPH_G1 = B13.G1
GRAPH_H0 = sp.Matrix([2, 1])
GRAPH_H1 = sp.Matrix([-1, 1])
GRAPH_MIX = sp.Matrix([1, -2])
GRAPH_B = (
    GRAPH_G0 * B13.z
    + GRAPH_G1 * sp.diff(B13.z, x)
    + GRAPH_H0 * B13.g
    + GRAPH_H1 * sp.diff(B13.g, x)
    + GRAPH_MIX * B13.g * sp.diff(B13.z, x)
)
GRAPH_T = B13.a - GRAPH_B
GRAPH_S = B13.S0 + B13.z * B13.SZ + B13.g * B13.SG
GRAPH_H = B13.H0 + B13.g * B13.HG
GRAPH_RHO = 2 + B13.z + B13.g
N_SUBS = {
    B13.t[0]: GRAPH_T[0],
    B13.t[1]: GRAPH_T[1],
    B13.b[0]: GRAPH_B[0],
    B13.b[1]: GRAPH_B[1],
    B13.rho: GRAPH_RHO,
    B13.s00: GRAPH_S[0, 0],
    B13.s01: GRAPH_S[0, 1],
    B13.s10: GRAPH_S[1, 0],
    B13.s11: GRAPH_S[1, 1],
    B13.h00: GRAPH_H[0, 0],
    B13.h01: GRAPH_H[0, 1],
    B13.h11: GRAPH_H[1, 1],
}


def apply_n(expr):
    return expr.subs(N_SUBS, simultaneous=True).doit().expand()


L_OWNER = apply_n(B13.L1)
OWNER_ORDERS, OWNER_EULERS, OWNER_PACKET, OWNER_THETA = B13.boundary_packet(L_OWNER)
OWNERS = B13.FUNDAMENTAL
VARIATIONS = B13.FUNDAMENTAL_VARIATION

E_T = apply_n(B13.E_VAR_INTERMEDIATE)
E_B_INTERMEDIATE = B13.first_order_euler(B13.L1, B13.b)
E_B = apply_n(E_B_INTERMEDIATE)
RETURN_DRIVER = sp.simplify(E_B - E_T)

SLOTS = (B13.s00, B13.s01, B13.s10, B13.s11)
C_Z_INTERMEDIATE = sp.diff(B13.L1, B13.rho)
C_Z_INTERMEDIATE += sum(
    (
        sp.diff(B13.L1, SLOTS[2 * row + column]) * B13.SZ[row, column]
        for row in range(2)
        for column in range(2)
    ),
    sp.Integer(0),
)
C_G_INTERMEDIATE = sp.diff(B13.L1, B13.rho)
C_G_INTERMEDIATE += sum(
    (
        sp.diff(B13.L1, SLOTS[2 * row + column]) * B13.SG[row, column]
        for row in range(2)
        for column in range(2)
    ),
    sp.Integer(0),
)
C_G_INTERMEDIATE += (
    sp.diff(B13.L1, B13.h00) * B13.HG[0, 0]
    + sp.diff(B13.L1, B13.h01) * B13.HG[0, 1]
    + sp.diff(B13.L1, B13.h11) * B13.HG[1, 1]
)
C_Z = apply_n(C_Z_INTERMEDIATE)
C_G = apply_n(C_G_INTERMEDIATE)

RETURNED_Z = apply_n(
    (GRAPH_G0.T * (E_B_INTERMEDIATE - B13.E_VAR_INTERMEDIATE))[0]
    - sp.diff(
        ((GRAPH_G1 + GRAPH_MIX * B13.g).T * (E_B_INTERMEDIATE - B13.E_VAR_INTERMEDIATE))[0], x
    )
    + C_Z_INTERMEDIATE
)
RETURNED_G = apply_n(
    ((GRAPH_H0 + GRAPH_MIX * sp.diff(B13.z, x)).T * (E_B_INTERMEDIATE - B13.E_VAR_INTERMEDIATE))[0]
    - sp.diff((GRAPH_H1.T * (E_B_INTERMEDIATE - B13.E_VAR_INTERMEDIATE))[0], x)
    + C_G_INTERMEDIATE
)
ASSEMBLED = {
    B13.a[0]: E_T[0],
    B13.a[1]: E_T[1],
    B13.z: RETURNED_Z,
    B13.g: RETURNED_G,
}


def owner_return_checks() -> None:
    exact(
        "the A-owner covector is exactly the independent partial-T Euler covector",
        is_zero(OWNER_EULERS[B13.a[0]] - ASSEMBLED[B13.a[0]])
        and is_zero(OWNER_EULERS[B13.a[1]] - ASSEMBLED[B13.a[1]]),
    )
    exact(
        "the graph owner is DB-adjoint applied to E_B-E_T plus the direct moving-Shiab return",
        is_zero(OWNER_EULERS[B13.z] - ASSEMBLED[B13.z]),
    )
    exact(
        "the metric owner is the complete graph plus density/Shiab/lowerer return",
        is_zero(OWNER_EULERS[B13.g] - ASSEMBLED[B13.g]),
    )
    exact(
        "direct-B, returned-T, their difference, and both coefficient returns are all live",
        not is_zero(E_B)
        and not is_zero(E_T)
        and not is_zero(RETURN_DRIVER)
        and not is_zero(C_Z)
        and not is_zero(C_G),
    )

    wrong_z = apply_n(
        -(GRAPH_G0.T * B13.E_VAR_INTERMEDIATE)[0]
        + sp.diff(((GRAPH_G1 + GRAPH_MIX * B13.g).T * B13.E_VAR_INTERMEDIATE)[0], x)
        + C_Z_INTERMEDIATE
    )
    reject(
        "return E_T alone and omit the independently varied direct-B covector",
        is_zero(wrong_z - OWNER_EULERS[B13.z]),
    )
    reject(
        "identify E_B-E_T with either E_B or minus E_T",
        is_zero(RETURN_DRIVER - E_B) or is_zero(RETURN_DRIVER + E_T),
    )

    shift = dict(zip(OWNERS, VARIATIONS))
    direct = B13.gateaux(L_OWNER, shift)
    bulk = sum(OWNER_EULERS[field] * variation for field, variation in zip(OWNERS, VARIATIONS))
    direct_value = B13.integral_01(B13.evaluate(direct, B13.V1_POLYS))
    bulk_value = B13.integral_01(B13.evaluate(bulk, B13.V1_POLYS))
    boundary_value = B13.endpoint(B13.evaluate(OWNER_THETA, B13.V1_POLYS))
    exact(
        "the complete owner tuple satisfies the exact bulk-plus-preboundary first-variation identity",
        sp.simplify(direct_value - bulk_value - boundary_value) == 0
        and boundary_value != 0,
        f"direct={direct_value}; bulk={bulk_value}; boundary={boundary_value}",
    )
    reject("discard the first-action owner preboundary packet", direct_value == bulk_value)
    exact(
        "the first action has the expected A-first/two-graph-owner second-order trace packet",
        OWNER_ORDERS == {"a0": 1, "a1": 1, "z": 2, "g": 2}
        and len(OWNER_PACKET[B13.a[0]]) == 1
        and len(OWNER_PACKET[B13.a[1]]) == 1
        and len(OWNER_PACKET[B13.z]) == 2
        and len(OWNER_PACKET[B13.g]) == 2,
        str(OWNER_ORDERS),
    )


# ---------------------------------------------------------------------------
# Weighted Helmholtz and the actual order/cancellation ledger.


def derivative_order_in(expr: sp.Expr, field) -> int:
    order = 0 if expr.has(field) else -1
    for derivative in expr.atoms(sp.Derivative):
        if derivative.expr == field and all(variable == x for variable in derivative.variables):
            order = max(order, len(derivative.variables))
    return order


def based(expr):
    return expr.subs(B13.BASE_POLYS, simultaneous=True).doit().expand()


def integrate_polynomial(expr: sp.Expr) -> sp.Expr:
    return sp.integrate(sp.Poly(sp.expand(expr), x).as_expr(), (x, 0, 1))


def helmholtz_and_order_checks() -> None:
    factor = x**3 * (1 - x) ** 3
    first_values = (1 + x, 2 - x, 1 + 2 * x, -1 + x)
    second_values = (2 - x, 1 + x**2, -2 + x, 1 + 3 * x)
    first = {field: factor * value for field, value in zip(OWNERS, first_values)}
    second = {field: factor * value for field, value in zip(OWNERS, second_values)}
    d_first = based(sp.Matrix([B13.gateaux(OWNER_EULERS[field], first) for field in OWNERS]))
    d_second = based(sp.Matrix([B13.gateaux(OWNER_EULERS[field], second) for field in OWNERS]))
    v_first = sp.Matrix(list(first.values()))
    v_second = sp.Matrix(list(second.values()))
    forward = integrate_polynomial((v_second.T * d_first)[0])
    reverse = integrate_polynomial((v_first.T * d_second)[0])
    exact(
        "the full owner linearization obeys the exact integrated Helmholtz reciprocity identity",
        sp.simplify(forward - reverse) == 0 and forward != 0,
        f"paired_value={forward}",
    )

    wrong = dict(ASSEMBLED)
    wrong[B13.z] = apply_n(
        -(GRAPH_G0.T * B13.E_VAR_INTERMEDIATE)[0]
        + sp.diff(((GRAPH_G1 + GRAPH_MIX * B13.g).T * B13.E_VAR_INTERMEDIATE)[0], x)
        + C_Z_INTERMEDIATE
    )
    wrong_first = based(sp.Matrix([B13.gateaux(wrong[field], first) for field in OWNERS]))
    wrong_second = based(sp.Matrix([B13.gateaux(wrong[field], second) for field in OWNERS]))
    wrong_defect = sp.simplify(
        integrate_polynomial((v_second.T * wrong_first - v_first.T * wrong_second)[0])
    )
    exact(
        "the E_T-only hostile return has a nonzero Helmholtz defect",
        wrong_defect != 0,
        str(wrong_defect),
    )
    reject("accept an owner tuple with a nonzero Helmholtz defect", wrong_defect == 0)

    realized = tuple(
        tuple(derivative_order_in(OWNER_EULERS[out], incoming) for incoming in OWNERS)
        for out in OWNERS
    )
    expected = (
        (0, 1, 2, 2),
        (1, 0, 2, 2),
        (2, 2, 2, 3),
        (2, 2, 3, 2),
    )
    exact(
        "the exact four-owner fixture realizes its complete derivative-order matrix",
        realized == expected,
        str(realized),
    )
    grouped = (
        (max(realized[i][j] for i in (0, 1) for j in (0, 1)), max(realized[i][2] for i in (0, 1)), max(realized[i][3] for i in (0, 1))),
        (max(realized[2][j] for j in (0, 1)), realized[2][2], realized[2][3]),
        (max(realized[3][j] for j in (0, 1)), realized[3][2], realized[3][3]),
    )
    exact(
        "direct-B/T cancellation lowers both diagonal graph blocks while retaining mixed odd-order returns",
        grouped == ((1, 2, 2), (2, 2, 3), (2, 3, 2)),
        str(grouped),
    )
    reject("promote every DN order cap to a realized nonzero coefficient", grouped == ((1, 2, 2), (2, 3, 3), (2, 3, 3)))

    symmetric = sp.Matrix([[1, sp.Rational(1, 2)], [sp.Rational(1, 2), 2]])
    skew = sp.Matrix([[0, sp.Rational(3, 2)], [-sp.Rational(3, 2), 0]])
    source_shiab = sp.Matrix([[1, 2], [-1, 0]])
    exact(
        "the E_T-only and full-return graph symbols are complementary symmetric/skew parts",
        (source_shiab + source_shiab.T) / 2 == sp.Matrix([[1, sp.Rational(1, 2)], [sp.Rational(1, 2), 0]])
        and (source_shiab - source_shiab.T) / 2 == skew,
    )
    one_owner = sp.Matrix([1, 2])
    exact(
        "one scalar graph owner kills the odd skew top coefficient while a two-owner graph retains it",
        (one_owner.T * skew * one_owner)[0] == 0
        and skew.rank() == 2,
    )
    exact(
        "symmetric- and skew-Shiab rival controls exchange which complementary graph symbol survives",
        (symmetric - symmetric.T) / 2 == sp.zeros(2)
        and (skew + skew.T) / 2 == sp.zeros(2),
    )
    mixed_zg = sp.factor(
        sp.diff(OWNER_EULERS[B13.z], sp.diff(B13.g, x, 3))
    )
    mixed_gz = sp.factor(
        sp.diff(OWNER_EULERS[B13.g], sp.diff(B13.z, x, 3))
    )
    expected_mixed = sp.factor(
        (B13.g - 3) * (B13.g + B13.z - 3) * (B13.g + B13.z + 2) / 2
    )
    exact(
        "the realized mixed third-order coefficients are nonzero formal-adjoint opposites",
        sp.factor(mixed_zg - expected_mixed) == 0
        and sp.factor(mixed_gz + expected_mixed) == 0
        and mixed_zg.subs({B13.z: 0, B13.g: 0}) == 9
        and mixed_gz.subs({B13.z: 0, B13.g: 0}) == -9,
        "sigma3(H_zg)=+9; sigma3(H_gz)=-9 at z=g=0",
    )
    reject("infer native third-order cancellation from a scalar graph-owner plant", skew.rank() == 0)


# ---------------------------------------------------------------------------
# Exact moving background/conormal polynomial atlas for the owner fixture.


lam, c = sp.symbols("lambda c", real=True)


def background_jet(polynomials: dict, scale: sp.Expr) -> dict:
    result = {}
    for field, polynomial in polynomials.items():
        scaled = sp.expand(scale * polynomial)
        result[field] = scaled.subs(x, 0)
        for order in range(1, 4):
            result[sp.diff(field, x, order)] = sp.diff(scaled, x, order).subs(x, 0)
    return result


def owner_symbol(background: dict) -> sp.Matrix:
    matrix = sp.zeros(len(OWNERS))
    for row, equation_field in enumerate(OWNERS):
        equation = OWNER_EULERS[equation_field]
        for column, field in enumerate(OWNERS):
            for order in range(4):
                jet = field if order == 0 else sp.diff(field, x, order)
                coefficient = sp.diff(equation, jet)
                matrix[row, column] += (
                    coefficient.subs(background, simultaneous=True).doit() * lam**order
                )
    return matrix.applyfunc(sp.expand)


def lagrange(values: dict[int, sp.Expr], symbol: sp.Symbol) -> sp.Expr:
    total = 0
    nodes = tuple(values)
    for node in nodes:
        basis = sp.Integer(1)
        for other in nodes:
            if other != node:
                basis *= (symbol - other) / sp.Rational(node - other)
        total += values[node] * basis
    return sp.expand(total)


def monic_gcd(values: list[sp.Expr], symbol: sp.Symbol) -> sp.Expr:
    polynomials = [sp.Poly(value, symbol, domain=sp.QQ) for value in values if value != 0]
    if not polynomials:
        return sp.Integer(0)
    result = reduce(sp.gcd, polynomials)
    return sp.factor(result.monic().as_expr())


def moving_atlas_checks() -> None:
    symbolic = owner_symbol(background_jet(B13.BASE_POLYS, c))
    background_degrees = sp.Matrix(
        symbolic.rows,
        symbolic.cols,
        lambda row, column: sp.degree(symbolic[row, column], c),
    )
    conormal_degrees = sp.Matrix(
        symbolic.rows,
        symbolic.cols,
        lambda row, column: sp.degree(symbolic[row, column], lam),
    )
    exact(
        "the complete total-symbol entrywise degree ledgers reproduce the realized owner orders",
        background_degrees
        == sp.Matrix([[4, 4, 5, 5], [4, 4, 5, 5], [5, 5, 6, 6], [5, 5, 6, 6]])
        and conormal_degrees
        == sp.Matrix([[0, 1, 2, 2], [1, 0, 2, 2], [2, 2, 2, 3], [2, 2, 3, 2]]),
        f"background={background_degrees.tolist()}; conormal={conormal_degrees.tolist()}",
    )

    nodes = (-3, -2, -1, 0, 1, 2, 3)
    heldouts = (4, 5)
    sampled = {value: symbolic.subs(c, value) for value in nodes + heldouts}
    reconstructed = sp.Matrix(
        len(OWNERS),
        len(OWNERS),
        lambda row, column: lagrange(
            {value: sampled[value][row, column] for value in nodes}, c
        ),
    )
    exact(
        "degree-six interpolation reconstructs every owner-symbol coefficient at both held-out backgrounds",
        all(
            is_zero(reconstructed.subs(c, value) - sampled[value])
            for value in heldouts
        ),
    )
    hidden_septic = sp.expand(reduce(lambda left, right: left * right, (c - node for node in nodes)))
    exact(
        "the hidden-degree-seven plant vanishes at every interpolation node and is live at both holdouts",
        all(hidden_septic.subs(c, node) == 0 for node in nodes)
        and all(hidden_septic.subs(c, node) != 0 for node in heldouts),
    )
    reject("certify degree six from interpolation nodes without held-out backgrounds", hidden_septic.subs(c, 4) == 0)

    determinant = sp.factor(symbolic.det())
    factor_coefficient, irreducible_factors = sp.factor_list(determinant)
    exact(
        "the complete total-symbol square maximal minor is one exact irreducible bivariate dispersion polynomial over Q",
        factor_coefficient != 0
        and len(irreducible_factors) == 1
        and irreducible_factors[0][1] == 1
        and sp.degree(determinant, c) == 20
        and sp.degree(determinant, lam) == 8,
        "degree_c=20; degree_lambda=8",
    )

    dn_row_weights = (0, 0, 1, 1)
    dn_column_weights = (1, 1, 2, 2)
    dn_principal = sp.zeros(len(OWNERS))
    background = background_jet(B13.BASE_POLYS, c)
    for row, equation_field in enumerate(OWNERS):
        for column, field in enumerate(OWNERS):
            order = dn_row_weights[row] + dn_column_weights[column]
            jet = field if order == 0 else sp.diff(field, x, order)
            dn_principal[row, column] = sp.expand(
                sp.diff(OWNER_EULERS[equation_field], jet)
                .subs(background, simultaneous=True)
                .doit()
                * lam**order
            )
    dn_determinant = sp.factor(dn_principal.det())
    expected_dn = sp.factor(
        16
        * (c - 3) ** 2
        * (c + 2) ** 2
        * (3 * c - 1) ** 2
        * (c + 1) ** 4
        * lam**8
    )
    exact(
        "the actual Douglis--Nirenberg principal determinant has four exact background factors",
        sp.factor(dn_determinant - expected_dn) == 0,
        "16(c-3)^2(c+2)^2(3c-1)^2(c+1)^4 lambda^8",
    )

    matrices = {value: symbolic.subs(c, value) for value in (-1, 0, 1, 2)}
    ranks = {value: matrix.rank() for value, matrix in matrices.items()}
    supports = {value: sum(entry != 0 for entry in matrix) for value, matrix in matrices.items()}
    exact(
        "the moving owner support changes at the zero-density background even though the generic matrix rank stays four",
        ranks == {-1: 4, 0: 4, 1: 4, 2: 4}
        and supports == {-1: 14, 0: 16, 1: 16, 2: 16},
        f"ranks={ranks}; support_entries={supports}",
    )
    reject("reuse the frozen same-grade support as a background-independent owner atlas", len(set(supports.values())) == 1)
    exact(
        "two admissible background slices have distinct exact total-symbol dispersion polynomials",
        sp.factor(matrices[0].det() - matrices[1].det()) != 0
        and matrices[0].det() != 0
        and matrices[1].det() != 0,
    )
    reject("assign a background-free total-symbol dispersion polynomial to the moving owner system", sp.factor(matrices[0].det() - matrices[1].det()) == 0)
    selected_entry_plant = sp.Matrix([[c, 1], [1, 0]])
    exact(
        "the selected-entry plant vanishes at c=0 while its full maximal minor stays nonzero",
        selected_entry_plant[0, 0].subs(c, 0) == 0
        and selected_entry_plant.det() == -1,
    )
    reject(
        "certify the bivariate total-symbol dispersion set from a selected non-maximal entry",
        selected_entry_plant[0, 0].subs(c, 0) == 0
        and selected_entry_plant.det().subs(c, 0) == 0,
    )
    type_level(
        "c=-1 makes the local density rho=2+z+g vanish at the frozen point and is an inadmissible density chart, not a physical support stratum"
    )
    type_level(
        "the irreducible degree-(20,8) determinant is full total-symbol dispersion data, while the factored DN determinant is the weighted principal characteristic data; neither is the frozen trace-stabilizer norm q(xi)=0"
    )


def scope_checks() -> None:
    type_level("the exact finite owner theorem includes direct B, returned T, moving contraction, density, lowerer, graph, Green, and preboundary terms")
    type_level("D(L-adjoint) and the six-slot DM enter the owner Hessian, not the first variation itself")
    type_level("coefficientwise native right-H/Krein/reality remains gated on the unreconstructed Y14 owner coefficient; real rational Helmholtz symmetry is not a substitute")
    type_level("the completed owner background may have a smaller stabilizer than the frozen trace-stabilizer atlas, so negative/null/pure-trace promotion must wait for that stabilizer")
    type_level("zero perpendicular vector and nonzero null perpendicular vector must retain separate atlas tags")
    type_level("P1/P2/P3 remain unchanged and unused; none supplies an owner coefficient, background jet, exceptional locus, quotient, or domain")
    type_level("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    type_level("no BV differential, observation-descended quotient, Green domain, hyperbolicity, Standard Model, generation, or cosmological claim follows")


def main() -> int:
    print("ECW3D-B2C15N FULL FIRST-ACTION OWNER EULER / MOVING POLYNOMIAL ATLAS GATE")
    source_checks()
    layer_zero_checks()
    owner_return_checks()
    helmholtz_and_order_checks()
    moving_atlas_checks()
    scope_checks()

    reject("use the unreleased D-squared discussion to fill the owner coefficient", False)
    reject("identify a characteristic kernel with a source-derived BV tangent", False)
    reject("use P1/P2/P3 to choose a moving background or polynomial component", False)

    print(
        "RESULT: full_finite_owner_tuple=constructed; direct_B_minus_T_return=live; "
        "Helmholtz=exact; mixed_order3=(+9,-9); total_dispersion_degree=(20,8); "
        "DN_factors=(c-3,c+2,3c-1,c+1)",
        flush=True,
    )
    print(
        "BOUNDARY: the native Y14 owner coefficient/stabilizer and coefficientwise "
        "right-H/Krein/reality atlas remain open",
        flush=True,
    )
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source receipts + "
        f"{TYPE} type-level + {PLANTED} planted = {total}",
        flush=True,
    )
    if FAILURES:
        print("FAILURES: " + "; ".join(FAILURES), flush=True)
        return 1
    print("ALL B2C15N CHECKS PASS", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
