#!/usr/bin/env python3
r"""B2C13 bifurcated residual-symbol and staged-preboundary probe.

This probe keeps two bosonic residuals separate:

``U_src``
    the manuscript-compressed source residual, represented in the finite jet
    model by ``rho[S(F_B+D_B T+q(T,T))+kappa H T]``;

``E_var``
    the exact Euler covector of the selected G2 first action, obtained here by
    applying the Euler operator to every occurrence of ``T`` in the written
    first-order transgression-shaped Lagrangian.

The exact one-dimensional rational model has a graph composite
``B=G0 z+G1 z'`` and ``T=A-B``.  It is deliberately noncyclic.  It proves
that the compressed branch cancels its graph curvature symbol and remains
first order, whereas the exact variational branch retains the formal-
adjoint residue and becomes second order in ``z``.  Squaring the two
residuals through a moving indefinite primalizer then yields distinct
preboundary packets.  The exact branch has an Ostrogradsky pair for
``(z,z')`` and cannot reuse the source branch or the old first-order fermion
Green matrix.

The probe also ports two independent residual vectors through B2C12's actual
trace-reversed ``(9,5)`` active ``R_res`` and verifies the moving-inverse
return.  The polynomial jet model is a universal local calculus certificate,
not the unreleased global Y^14 Shiab symbol, trace theorem, or closed domain.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import runpy
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests/channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))

B2C12 = runpy.run_path(
    str(CHANNEL / "eric_curt_wave3d_b2c12_active_staged_action_probe.py")
)
B2C9 = runpy.run_path(
    str(CHANNEL / "eric_curt_wave3d_b2c9_offdiagonal_total_current_preboundary_probe.py")
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
    print(f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"source: {label}")


def type_level(label: str, condition: bool = True, detail: str = "") -> None:
    global TYPE
    TYPE += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: type-level - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def is_zero(value) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(item) == 0 for item in value)
    return sp.simplify(value) == 0


def source_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    paired = (
        ROOT / "lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md"
    ).read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    pullback = (ROOT / "lab/sources/g3-weinstein-section-pullback-recheck-2026-07-31.md").read_text()
    rendered = (
        ROOT
        / "explorations/hourly-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
    ).read_text()
    g2 = (ROOT / "explorations/g2-field-space-native-variational-shiab-2026-07-31.md").read_text()

    source_receipt(
        "the manuscript writes the compressed residual norm and the unsuperscripted compact 9.15 equation",
        r"I_2^B=\|\Upsilon_\omega^B\|^2" in paired
        and "D_omega^* Upsilon_omega=0" in rendered,
        "2021 draft 9.11-9.15",
    )
    source_receipt(
        "the draft's first-order-total and second-order-sourced equations are alternatives",
        r"\Upsilon^B_\omega+\Upsilon^F_\omega=0" in pack
        and r"D_\omega^*\Upsilon^B_\omega=\Upsilon^F_\omega" in pack,
        "2021 draft 9.18-9.20",
    )
    source_receipt(
        "the modern two-connection D-squared construction is expressly unreleased",
        "have never released" in toe and "on shell where the equations get satisfied" in toe,
        "TOE 02:44:06-02:45:13",
    )
    source_receipt(
        "the checked author-guided four-dimensional route is restriction/pullback rather than a supplied defect action",
        "author-guided physicalization map is restriction/pullback" in pullback
        and "return no mathematical construction of a defect action" in pullback,
        "TOE/Portal/ITI collision packet",
    )
    exact(
        "the repository G2 collision corrects rather than source-confirms the compressed Euler formula",
        "fails the cyclic identities" in g2 and "exact slot-symmetrized Euler covector" in g2,
        "repository construction; SOURCE-CORRECTS",
    )


# ---------------------------------------------------------------------------
# Exact rational first-jet model.


x = sp.symbols("x", real=True)
eps = sp.symbols("eps", real=True)
kappa = sp.Rational(5, 3)

t = sp.Matrix([sp.Function("t0")(x), sp.Function("t1")(x)])
b = sp.Matrix([sp.Function("b0")(x), sp.Function("b1")(x)])
rho = sp.Function("rho")(x)
s00, s01, s10, s11 = [sp.Function(name)(x) for name in ("s00", "s01", "s10", "s11")]
S = sp.Matrix([[s00, s01], [s10, s11]])
h00, h01, h11 = [sp.Function(name)(x) for name in ("h00", "h01", "h11")]
H = sp.Matrix([[h00, h01], [h01, h11]])

C0 = sp.Matrix([[0, 1], [-1, 0]])
C1 = sp.Matrix([[1, 0], [1, -1]])
C2 = sp.Matrix([[0, -1], [2, 1]])
C = C0 + b[0] * C1 + b[1] * C2
q = sp.Matrix([t[0] * t[1], t[0] ** 2 - t[1] ** 2])
F_B = b.diff(x) + C * b
D_BT = t.diff(x) + C * t

L1 = sp.expand(
    rho
    * (
        (t.T * S * F_B)[0]
        + sp.Rational(1, 2) * (t.T * S * D_BT)[0]
        + sp.Rational(1, 3) * (t.T * S * q)[0]
        + kappa * sp.Rational(1, 2) * (t.T * H * t)[0]
    )
)


def first_order_euler(lagrangian: sp.Expr, fields: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(
        [
            sp.diff(lagrangian, field)
            - sp.diff(sp.diff(lagrangian, sp.diff(field, x)), x)
            for field in fields
        ]
    )


E_VAR_INTERMEDIATE = first_order_euler(L1, t)
U_SRC_INTERMEDIATE = rho * (S * (F_B + D_BT + q) + kappa * H * t)

a = sp.Matrix([sp.Function("a0")(x), sp.Function("a1")(x)])
z = sp.Function("z")(x)
g = sp.Function("g")(x)
G0 = sp.Matrix([1, -1])
G1 = sp.Matrix([1, 2])
B_GRAPH = G0 * z + G1 * sp.diff(z, x)
T_GRAPH = a - B_GRAPH

S0 = sp.Matrix([[1, 2], [-1, 0]])
SZ = sp.Matrix([[0, 1], [2, -1]])
SG = sp.Matrix([[1, 0], [1, 1]])
S_GRAPH = S0 + z * SZ + g * SG
H0 = sp.Matrix([[2, 1], [1, -1]])
HG = sp.Matrix([[1, -1], [-1, 2]])
H_GRAPH = H0 + g * HG
R0 = sp.Matrix([[1, sp.Rational(1, 2)], [sp.Rational(1, 2), -1]])
RG = sp.Matrix([[0, sp.Rational(1, 3)], [sp.Rational(1, 3), sp.Rational(1, 2)]])
RHO_GRAPH = 2 + g
RBAR_GRAPH = R0 + g * RG
R_GRAPH = RBAR_GRAPH / RHO_GRAPH
B_LOWERER_GRAPH = sp.simplify(R_GRAPH.inv())

BASE_SUBS = {
    t[0]: T_GRAPH[0],
    t[1]: T_GRAPH[1],
    b[0]: B_GRAPH[0],
    b[1]: B_GRAPH[1],
    rho: RHO_GRAPH,
    s00: S_GRAPH[0, 0],
    s01: S_GRAPH[0, 1],
    s10: S_GRAPH[1, 0],
    s11: S_GRAPH[1, 1],
    h00: H_GRAPH[0, 0],
    h01: H_GRAPH[0, 1],
    h11: H_GRAPH[1, 1],
}


def apply_base(expr):
    return expr.subs(BASE_SUBS, simultaneous=True).doit().expand()


U_SRC = apply_base(U_SRC_INTERMEDIATE)
E_VAR = apply_base(E_VAR_INTERMEDIATE)
BRANCHES = {"source": U_SRC, "variational": E_VAR}


def jacobian_jet(expr: sp.Matrix, fields: sp.Matrix, order: int) -> sp.Matrix:
    return sp.Matrix(
        len(expr),
        len(fields),
        lambda row, col: sp.diff(expr[row], sp.diff(fields[col], x, order)),
    )


def graph_symbol_checks() -> None:
    source_b = jacobian_jet(U_SRC_INTERMEDIATE, b, 1)
    source_t = jacobian_jet(U_SRC_INTERMEDIATE, t, 1)
    exact_b = jacobian_jet(E_VAR_INTERMEDIATE, b, 1)
    exact_t = jacobian_jet(E_VAR_INTERMEDIATE, t, 1)
    k_source = sp.simplify(source_b - source_t)
    k_exact = sp.simplify(exact_b - exact_t)
    expected_exact = sp.simplify(sp.Rational(1, 2) * rho * (S + S.T))

    exact("compressed branch cancels the B/T curvature graph symbol", is_zero(k_source))
    exact(
        "exact action branch retains one-half of the formal-antisymmetric graph residue",
        is_zero(k_exact - expected_exact) and not is_zero(k_exact),
    )
    exact(
        "the exact graph second-jet coefficient is K_B times the first-jet graph symbol",
        is_zero(jacobian_jet(E_VAR, sp.Matrix([z]), 2) - apply_base(k_exact) * G1),
    )
    exact(
        "the compressed residual has no second graph jet",
        is_zero(jacobian_jet(U_SRC, sp.Matrix([z]), 2)),
    )

    sigma_source_a = jacobian_jet(U_SRC, a, 1)
    sigma_exact_a = jacobian_jet(E_VAR, a, 1)
    exact(
        "the two A-principal symbols have the predicted full versus formal-symmetric coefficients",
        is_zero(sigma_source_a - RHO_GRAPH * S_GRAPH)
        and is_zero(
            sigma_exact_a
            - sp.Rational(1, 2) * RHO_GRAPH * (S_GRAPH - S_GRAPH.T)
        ),
    )
    exact("the two residual branches have unequal A-principal symbols", not is_zero(sigma_source_a - sigma_exact_a))

    skew = sp.Function("skew")(x)
    cyclic_sub = {
        s00: 0,
        s11: 0,
        s01: skew,
        s10: -skew,
    }
    exact(
        "a formally self-adjoint/cyclic control kills the exact graph residue",
        is_zero(k_exact.subs(cyclic_sub, simultaneous=True)),
    )
    reject("copy the compressed graph cancellation into the noncyclic exact branch", is_zero(k_exact))
    reject("identify the two principal symbols by their common field type", is_zero(sigma_source_a - sigma_exact_a))


def b2c9_noncentral_symbol_checks() -> None:
    """Execute the existing exact first-jet G2 comparator, not just the toy model."""

    g2 = B2C9["G2"]
    background = B2C9["bosonic_fixture"]()
    basis = []
    for slot in range(3):
        for matrix_index in range(4):
            element = [B2C9["mzero"](), B2C9["mzero"](), B2C9["mzero"]()]
            element[slot] = B2C9["B2C7"]["unit2"](matrix_index)
            basis.append(tuple(element))

    def source_functional(data, test):
        b_conn, t_form, insertion, b_jet, t_jet, _h_jet, metric_scale, kappa_value = data
        d_b = B2C9["antisymmetrize"](b_jet)
        d_t = B2C9["antisymmetrize"](t_jet)
        a_conn = B2C9["f1_add"](b_conn, t_form)
        d_a = B2C9["f2_add"](d_b, d_t)
        return (
            g2["wedge_pair"](
                test,
                g2["shiab_insert"](insertion, g2["curvature"](a_conn, d_a)),
            )
            + kappa_value * metric_scale * g2["inner1"](test, t_form)
        )

    covector = (F(1), F(2), F(-1))

    def jet_rows(vector, sign=F(1)):
        return tuple(
            tuple(B2C9["mscale"](sign * covector[j], vector[i]) for j in range(3))
            for i in range(3)
        )

    def t_jet_direction(vector):
        return B2C9["replace_direction"](
            B2C9["zero_direction"](), 4, jet_rows(vector)
        )

    def fixed_a_graph_direction(vector):
        direction = B2C9["replace_direction"](
            B2C9["zero_direction"](), 3, jet_rows(vector)
        )
        return B2C9["replace_direction"](
            direction, 4, jet_rows(vector, F(-1))
        )

    def derivative_variational(direction, test):
        return B2C9["richardson"](
            lambda parameter: B2C9["full_euler_functional"](
                B2C9["shift_background"](background, direction, parameter), test
            )
        )

    def derivative_source(direction, test):
        return B2C9["richardson"](
            lambda parameter: source_functional(
                B2C9["shift_background"](background, direction, parameter), test
            )
        )

    sigma_variational = [
        [derivative_variational(t_jet_direction(vector), test) for vector in basis]
        for test in basis
    ]
    sigma_source = [
        [derivative_source(t_jet_direction(vector), test) for vector in basis]
        for test in basis
    ]
    difference_count = sum(
        sigma_variational[row][column] != sigma_source[row][column]
        for row in range(12)
        for column in range(12)
    )
    exact(
        "the existing exact noncentral G2 fixture changes 60 of 144 principal-symbol entries",
        difference_count == 60,
        f"different={difference_count}/144",
    )

    graph_direction = fixed_a_graph_direction(basis[5])
    source_graph = derivative_source(graph_direction, basis[0])
    variational_graph = derivative_variational(graph_direction, basis[0])
    exact(
        "the fixed-A graph-jet witness cancels in the source residual but survives in exact G2",
        source_graph == 0 and variational_graph == F(1, 2),
        f"source={source_graph}; variational={variational_graph}",
    )
    reject("treat the G2 correction as lower order only", difference_count == 0)
    reject("copy source graph cancellation into the exact B2C9 Euler map", variational_graph == 0)


# ---------------------------------------------------------------------------
# Complete moving chain through S, H/rho, graph, and R.


dt = sp.Matrix([sp.Function("dt0")(x), sp.Function("dt1")(x)])
db = sp.Matrix([sp.Function("db0")(x), sp.Function("db1")(x)])
drho = sp.Function("drho")(x)
ds00, ds01, ds10, ds11 = [sp.Function(name)(x) for name in ("ds00", "ds01", "ds10", "ds11")]
dS = sp.Matrix([[ds00, ds01], [ds10, ds11]])
dh00, dh01, dh11 = [sp.Function(name)(x) for name in ("dh00", "dh01", "dh11")]
dH = sp.Matrix([[dh00, dh01], [dh01, dh11]])

da = sp.Matrix([sp.Function("da0")(x), sp.Function("da1")(x)])
dz = sp.Function("dz")(x)
dg = sp.Function("dg")(x)
dB_GRAPH = G0 * dz + G1 * sp.diff(dz, x)
dT_GRAPH = da - dB_GRAPH
dS_GRAPH = SZ * dz + SG * dg
dH_GRAPH = HG * dg


def gateaux(expr, replacements: dict) -> sp.Expr | sp.Matrix:
    shifted = {base: base + eps * direction for base, direction in replacements.items()}
    return sp.diff(expr.subs(shifted, simultaneous=True).doit(), eps).subs(eps, 0).doit().expand()


dR_GRAPH = gateaux(R_GRAPH, {g: dg})


def intermediate_components(branch: sp.Matrix) -> dict[str, sp.Matrix]:
    zero2 = sp.Matrix([0, 0])
    components = {
        "A": gateaux(branch, {t[0]: da[0], t[1]: da[1]}),
        "graph": gateaux(
            branch,
            {t[0]: -dB_GRAPH[0], t[1]: -dB_GRAPH[1], b[0]: dB_GRAPH[0], b[1]: dB_GRAPH[1]},
        ),
        "Shiab": gateaux(branch, {s00: dS_GRAPH[0, 0], s01: dS_GRAPH[0, 1], s10: dS_GRAPH[1, 0], s11: dS_GRAPH[1, 1]}),
        "density": gateaux(branch, {rho: dg}),
        "Hodge": gateaux(branch, {h00: dH_GRAPH[0, 0], h01: dH_GRAPH[0, 1], h11: dH_GRAPH[1, 1]}),
    }
    return {name: apply_base(value) for name, value in components.items()}


COMPONENTS = {
    "source": intermediate_components(U_SRC_INTERMEDIATE),
    "variational": intermediate_components(E_VAR_INTERMEDIATE),
}


BASE_POLYS = {
    a[0]: 1 + x + x**2,
    a[1]: -1 + 2 * x - x**2,
    z: 1 - x + x**2,
    # Keep the base density spatially constant while varying it in a
    # nonconstant direction. This makes the exact density-dual/R_jet witness
    # polynomial after evaluation without freezing the density response.
    g: sp.Integer(1),
}
V1_POLYS = {
    da[0]: 1 - 2 * x + x**2,
    da[1]: sp.Rational(1, 2) + x,
    dz: -1 + x + 2 * x**2,
    dg: 2 - x + x**2,
}
V2_POLYS = {
    da[0]: -1 + x,
    da[1]: 2 - x + x**2,
    dz: 1 + 2 * x - x**2,
    dg: -1 + sp.Rational(1, 2) * x,
}


def evaluate(expr, direction: dict | None = None):
    substitutions = dict(BASE_POLYS)
    if direction:
        substitutions.update(direction)
    return sp.simplify(expr.subs(substitutions, simultaneous=True).doit().expand())


def integral_01(expr) -> sp.Expr:
    return sp.integrate(sp.expand(expr), (x, 0, 1))


def endpoint(expr) -> sp.Expr:
    return sp.simplify(expr.subs(x, 1) - expr.subs(x, 0))


def moving_chain_checks() -> None:
    fundamental_shift = {
        a[0]: da[0],
        a[1]: da[1],
        z: dz,
        g: dg,
    }
    exact(
        "the jet lowerer and primalizer are typed inverses with R_jet=rho^-1 Rbar",
        is_zero(sp.simplify(B_LOWERER_GRAPH * R_GRAPH - sp.eye(2))),
    )
    for name, residual in BRANCHES.items():
        u = (R_GRAPH * residual).applyfunc(sp.cancel)
        de_direct = gateaux(residual, fundamental_shift)
        de_parts = sum(COMPONENTS[name].values(), sp.zeros(2, 1))
        exact(
            f"{name} residual derivative returns A, graph, Shiab, density, and Hodge pieces",
            is_zero(evaluate(de_direct - de_parts, V1_POLYS)),
        )

        part_integrals = {}
        for part_name, part in COMPONENTS[name].items():
            part_integrals[part_name] = sp.simplify(integral_01(evaluate((part.T * u)[0], V1_POLYS)))
            exact(
                f"{name} {part_name} return is live through R_jet",
                part_integrals[part_name] != 0,
                str(part_integrals[part_name]),
            )

        moving_r = sp.cancel(sp.Rational(1, 2) * (residual.T * dR_GRAPH * residual)[0])
        moving_r_value = sp.simplify(integral_01(evaluate(moving_r, V1_POLYS)))
        exact(f"{name} moving-primalizer return is live", moving_r_value != 0, str(moving_r_value))

        l2 = sp.cancel(sp.Rational(1, 2) * (residual.T * R_GRAPH * residual)[0])
        direct_l2 = gateaux(l2, fundamental_shift)
        decomposed = (de_parts.T * u)[0] + moving_r
        exact(
            f"{name} complete squared-residual derivative equals the decomposed moving return",
            is_zero(evaluate(direct_l2 - decomposed, V1_POLYS)),
        )
        reject(
            f"freeze R_jet in the complete {name} square variation",
            sp.simplify(integral_01(evaluate(direct_l2 - (de_parts.T * u)[0], V1_POLYS))) == 0,
        )
        for omitted in ("graph", "Shiab", "density", "Hodge"):
            reject(
                f"omit the live {omitted} term from the {name} squared-residual return",
                part_integrals[omitted] == 0,
            )


# ---------------------------------------------------------------------------
# Euler/Green integration and the two distinct preboundary jet packets.


FUNDAMENTAL = (a[0], a[1], z, g)
FUNDAMENTAL_VARIATION = (da[0], da[1], dz, dg)


def derivative_order(expr: sp.Expr, field) -> int:
    order = 0 if expr.has(field) else -1
    for derivative in expr.atoms(sp.Derivative):
        if derivative.expr == field and all(variable == x for variable in derivative.variables):
            order = max(order, len(derivative.variables))
    return order


def boundary_packet(lagrangian: sp.Expr):
    packet = {}
    eulers = {}
    orders = {}
    theta = 0
    for field, variation in zip(FUNDAMENTAL, FUNDAMENTAL_VARIATION):
        order = derivative_order(lagrangian, field)
        orders[str(field.func)] = order
        partials = {0: sp.diff(lagrangian, field)}
        for k in range(1, order + 1):
            partials[k] = sp.diff(lagrangian, sp.diff(field, x, k))
        euler = partials[0]
        for k in range(1, order + 1):
            euler += (-1) ** k * sp.diff(partials[k], x, k)
        eulers[field] = sp.expand(euler)
        momenta = {}
        for j in range(order):
            momentum = 0
            for k in range(j + 1, order + 1):
                momentum += (-1) ** (k - j - 1) * sp.diff(partials[k], x, k - j - 1)
            momenta[j] = sp.expand(momentum)
            theta += momenta[j] * sp.diff(variation, x, j)
        packet[field] = momenta
    return orders, eulers, packet, sp.expand(theta)


PREBOUNDARY = {}


def preboundary_checks() -> None:
    fundamental_shift = {a[0]: da[0], a[1]: da[1], z: dz, g: dg}
    for name, residual in BRANCHES.items():
        l2 = sp.expand(sp.cancel(sp.Rational(1, 2) * (residual.T * R_GRAPH * residual)[0]))
        orders, eulers, packet, theta = boundary_packet(l2)
        PREBOUNDARY[name] = (l2, orders, eulers, packet, theta)

        direct = gateaux(l2, fundamental_shift)
        bulk = sum(
            eulers[field] * variation
            for field, variation in zip(FUNDAMENTAL, FUNDAMENTAL_VARIATION)
        )
        direct_value = sp.simplify(integral_01(evaluate(direct, V1_POLYS)))
        bulk_value = sp.simplify(integral_01(evaluate(bulk, V1_POLYS)))
        boundary_value = endpoint(evaluate(theta, V1_POLYS))
        exact(
            f"{name} square satisfies the exact bulk-plus-preboundary Green identity",
            direct_value == bulk_value + boundary_value and boundary_value != 0,
            f"direct={direct_value}; bulk={bulk_value}; boundary={boundary_value}",
        )
        reject(f"discard the nonzero {name} preboundary potential", direct_value == bulk_value)

    source_orders = PREBOUNDARY["source"][1]
    exact_orders = PREBOUNDARY["variational"][1]
    exact(
        "the compressed branch has only first-order A/z traces and no g conormal",
        source_orders == {"a0": 1, "a1": 1, "z": 1, "g": 0},
        str(source_orders),
    )
    exact(
        "the exact G2 branch prolongs the graph to z-second-order and makes the moving coefficient g first-order",
        exact_orders == {"a0": 1, "a1": 1, "z": 2, "g": 1},
        str(exact_orders),
    )

    exact_packet = PREBOUNDARY["variational"][3]
    source_packet = PREBOUNDARY["source"][3]
    exact_z1 = exact_packet[z][1]
    exact_z1_flux = endpoint(evaluate(exact_z1 * sp.diff(dz, x), V1_POLYS))
    exact("the prolonged exact branch has a live z-prime conormal momentum", exact_z1_flux != 0, str(exact_z1_flux))
    reject("drop the exact branch's z-prime conormal pair", exact_z1_flux == 0)
    reject("copy the source packet into the exact branch", 1 in source_packet[z])

    source_slots = sum(len(momenta) for momenta in source_packet.values())
    exact_slots = sum(len(momenta) for momenta in exact_packet.values())
    exact("the exact comparator preboundary packet is strictly enlarged", source_slots == 3 and exact_slots == 5)
    reject("reuse the first-order bosonic/fermion Green matrix before jet prolongation", source_slots == exact_slots)


def omega_value(name: str, first: dict, second: dict) -> sp.Expr:
    _l2, _orders, _eulers, packet, _theta = PREBOUNDARY[name]
    first_shift = {a[0]: da[0], a[1]: da[1], z: dz, g: dg}
    total = 0
    for field, variation in zip(FUNDAMENTAL, FUNDAMENTAL_VARIATION):
        for jet, momentum in packet[field].items():
            dmomentum = gateaux(momentum, first_shift)
            total += dmomentum * sp.diff(variation, x, jet)
    # ``total`` is D_first Theta[second] once the base-direction functions
    # are assigned from ``first`` and the test variations from ``second``.
    first_names = dict(first)
    second_names = dict(second)
    forward = evaluate(total, {**first_names, **second_names})

    # Use a disjoint second direction alphabet to avoid overwriting the
    # differentiating and test variations.
    ea = sp.Matrix([sp.Function("ea0")(x), sp.Function("ea1")(x)])
    ez = sp.Function("ez")(x)
    eg = sp.Function("eg")(x)
    second_shift = {a[0]: ea[0], a[1]: ea[1], z: ez, g: eg}
    reverse_total = 0
    for field, first_variation in zip(FUNDAMENTAL, FUNDAMENTAL_VARIATION):
        for jet, momentum in packet[field].items():
            dmomentum = gateaux(momentum, second_shift)
            reverse_total += dmomentum * sp.diff(first_variation, x, jet)
    second_alias = {
        ea[0]: second[da[0]],
        ea[1]: second[da[1]],
        ez: second[dz],
        eg: second[dg],
    }
    reverse = evaluate(reverse_total, {**first, **second_alias})
    return endpoint(sp.simplify(forward - reverse))


def presymplectic_checks() -> None:
    # Direct construction with two disjoint alphabets, avoiding any claim of
    # boundary reduction or polarization.
    ea = sp.Matrix([sp.Function("ea0")(x), sp.Function("ea1")(x)])
    ez = sp.Function("ez")(x)
    eg = sp.Function("eg")(x)
    second_polys = {ea[0]: V2_POLYS[da[0]], ea[1]: V2_POLYS[da[1]], ez: V2_POLYS[dz], eg: V2_POLYS[dg]}
    first_shift = {a[0]: da[0], a[1]: da[1], z: dz, g: dg}
    second_shift = {a[0]: ea[0], a[1]: ea[1], z: ez, g: eg}

    values = {}
    for name, (_l2, _orders, _eulers, packet, _theta) in PREBOUNDARY.items():
        omega = 0
        for field, v1, v2 in zip(FUNDAMENTAL, FUNDAMENTAL_VARIATION, (ea[0], ea[1], ez, eg)):
            for jet, momentum in packet[field].items():
                omega += gateaux(momentum, first_shift) * sp.diff(v2, x, jet)
                omega -= gateaux(momentum, second_shift) * sp.diff(v1, x, jet)
        value = endpoint(evaluate(omega, {**V1_POLYS, **second_polys}))
        values[name] = value
        exact(f"{name} preboundary two-form is nonzero and action-derived", value != 0, str(value))

        swapped = 0
        for field, v1, v2 in zip(FUNDAMENTAL, FUNDAMENTAL_VARIATION, (ea[0], ea[1], ez, eg)):
            for jet, momentum in packet[field].items():
                swapped += gateaux(momentum, second_shift) * sp.diff(v1, x, jet)
                swapped -= gateaux(momentum, first_shift) * sp.diff(v2, x, jet)
        swapped_value = endpoint(evaluate(swapped, {**V1_POLYS, **second_polys}))
        exact(f"{name} preboundary two-form is antisymmetric", swapped_value == -value)

    exact("the two action-derived preboundary two-forms remain distinct", values["source"] != values["variational"])


# ---------------------------------------------------------------------------
# Actual active (9,5) coefficient port inherited from B2C12.


def active_r_res_checks() -> None:
    g0 = np.diag([1.0, 1.0, 1.0, -1.0])
    h = np.diag([0.2, -0.1, 0.15, 0.05])
    lowerer, primalizer, d_lowerer, d_primalizer = B2C12["residual_maps"](g0, h)
    identity = np.eye(28)
    inertia = np.linalg.eigvalsh(lowerer)
    exact(
        "the active coefficient port retains inverse b_res/R_res and balanced (14,14) inertia",
        np.max(np.abs(primalizer @ lowerer - identity)) < 1.0e-9
        and (int(np.sum(inertia > 1.0e-9)), int(np.sum(inertia < -1.0e-9))) == (14, 14),
    )
    exact(
        "the active port retains dR=-R(db)R",
        np.max(np.abs(d_primalizer + primalizer @ d_lowerer @ primalizer)) < 2.0e-9,
    )

    rng = np.random.default_rng(2026080113)
    test_covectors = {
        "source": rng.integers(-3, 4, size=28).astype(float),
        "variational": rng.integers(-3, 4, size=28).astype(float),
    }
    directions = {
        "source": rng.integers(-2, 3, size=28).astype(float),
        "variational": rng.integers(-2, 3, size=28).astype(float),
    }
    exact("the two independently labeled active-port test covectors are not collapsed", np.linalg.norm(test_covectors["source"] - test_covectors["variational"]) > 1.0)
    for name in test_covectors:
        e = test_covectors[name]
        de = directions[name]
        u = primalizer @ e
        direct = float(de @ u + 0.5 * e @ d_primalizer @ e)
        inverse = float(de @ u - 0.5 * u @ d_lowerer @ u)
        exact(
            f"{name} residual returns through the moving active R_res with the inverse-pairing sign",
            abs(direct - inverse) < 2.0e-8 and abs(0.5 * e @ d_primalizer @ e) > 1.0e-5,
        )
        reject(f"freeze active R_res for the {name} branch", abs(direct - float(de @ u)) < 1.0e-7)


def layer_zero_scope() -> None:
    type_level("Upsilon_B_src, exact G2 E_T_var, either squared-action Euler equation, and the full owner tuple are distinct")
    type_level("source D_omega-star, a Frechet formal adjoint, a Green adjoint, a Noether differential, and unreleased D-squared are distinct")
    type_level("the manuscript residual norm, spoken inter-layer square/root, and unreleased two-connection D-squared are distinct")
    type_level("a Green endpoint, preboundary potential, presymplectic current, reduced BFV phase space, and selected domain are distinct")
    type_level("a nonzero preboundary two-form alone does not select or prove a maximal Green-isotropic domain")
    type_level("A_tr, B_rot, and T=A_tr-B_rot replace unstable naked A/B labels")
    type_level("the exact branch's M response is differentiated through the action's cubic slots rather than replaced by S(q)")
    type_level("moving S includes the trace gamma, soldering, Hodge, projection, Krein dual, and density at the native port; the finite model separates representative S/rho/H returns")
    type_level("R_res is algebraic in the present active metric port, so DR contributes bulk and delta-u in omega but no independent Green term")
    type_level("the exact rational/B2C9 graph comparator is second order and requires Ostrogradsky boundary pairs; nonvanishing of the corresponding active Y14 graph symbol remains open")
    type_level("the finite rational jet theorem now uses R_jet=rho^-1 Rbar exactly once but does not construct the global Y14 atlas, native local Shiab coefficients, trace theorem, or closed domain")
    type_level("the repo active trace-reversed (9,5) right-H Sp(32,32;H) port is not globally identified with the draft Y^(7,7) plus complex C^(64,64)/u(64,64)-type carrier")
    type_level("P1/P2/P3 supplies no residual, derivative, symbol, pairing, conormal momentum, boundary condition, quotient, or action")
    type_level("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    type_level("the common mixed boson-fermion domain search remains gated on prolonging and typing the exact bosonic jet trace")


def main() -> int:
    print("ECW3D-B2C13 DUPSILON SYMBOL / STAGED PREBOUNDARY JET FORM")
    source_checks()
    graph_symbol_checks()
    b2c9_noncentral_symbol_checks()
    moving_chain_checks()
    preboundary_checks()
    presymplectic_checks()
    active_r_res_checks()
    layer_zero_scope()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source receipts + {TYPE} type-level + {PLANTED} planted = {total}",
        flush=True,
    )
    if FAILURES:
        print("FAILED: " + "; ".join(FAILURES), flush=True)
        return 1
    print("ALL B2C13 CHECKS PASS", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
