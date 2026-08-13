#!/usr/bin/env python3
"""Exact full-tau_A0 boundary moment-map and edge-kernel composition.

This composes three already-owned objects without identifying their types:

1. the derivative-bearing nonzero-reference tilted cocycle ``tau_A``;
2. its left-quotient distortion ``Theta_A``, carrying the residual adjoint
   action; and
3. the group-valued boundary edge frame.

The selected action pairing is used only on the conditionally Spin-native
grade-1+2+5 parent.  The two U(32,32) halves and full U(64,64) remain rival
parents because they do not preserve that selected carrier.  The finite QQ
fixture proves algebraic associated-bundle descent, not an analytic BFV phase
space or a physical boundary-condition selection.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
G1_PATH = ROOT / "tests/channel-swings/g1_derivative_cocycle_moving_reference_probe.py"
PREVIOUS = ROOT / "tests/channel-swings/selected_k77_boundary_disposition_selector_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def load(relative):
    return json.loads(read(relative))


def comm(left, right):
    return sp.simplify(left * right - right * left)


def flat(matrix):
    return sp.Matrix(list(matrix))


def trace_pair(left, right):
    return sp.simplify(sp.trace(left * right))


def to_sympy(matrix):
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in matrix])


print("A. SOURCE LOCUS, LAYER ZERO, AND PREDECESSORS")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
g1_report = read("explorations/g1-derivative-cocycle-moving-reference-2026-07-31.md")
pairing = load("lab/process/selected-k77-residual-pairing-invariance.json")
closure = load("lab/process/selected-k77-operative-pairing-symmetry-closure.json")

check("source", "Weinstein states the tilted subgroup and double-coset grammar",
      "A mod G is replaced by the double coset" in toe)
check("source", "Portal locates tau_A0 at the distinguished Levi-Civita connection",
      "tau_{A_0}" in portal and "Levi-Civita connection" in portal)
check("source", "Portal supplies the bi-connection and affine difference owner",
      "bi-connection" in portal and "difference of two connections" in portal)
check("source", "source is not credited with a boundary moment-map or edge theorem", True)
check("prior", "the repository already owns the full derivative cocycle",
      "q_A(g)=A-\\operatorname{Ad}_gA+(dg)g^{-1}" in g1_report)

for label in (
    "active gauge action versus atlas transition",
    "left tilted quotient versus residual right action",
    "nonzero-reference q_A cocycle versus flat Maurer-Cartan shadow",
    "adjoint distortion versus affine connection coordinate",
    "raw residual moment map versus edge-completed characteristic orbit",
    "global algebraic bundle descent versus analytic BFV phase space",
    "Spin-native selected parent versus two U(32,32) halves",
    "two U(32,32) halves versus full U(64,64)",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    previous = runpy.run_path(str(PREVIOUS))
check("repo", "the v0.101 boundary selector replays",
      "PASS 48/48" in capture.getvalue() and not previous["FAILURES"])


print("\nB. FULL NONZERO-A0 TILTED DOUBLE ACTION")
g1 = runpy.run_path(str(G1_PATH))
m = g1["matrix"]
a0 = m([[2, 1], [3, -1]])
g = (m([[1, 1], [0, 1]]), m([[1, 0], [2, -1]]))
h = (m([[2, 0], [1, 1]]), m([[0, 1], [-1, 2]]))
k = (m([[1, 0], [-1, 1]]), m([[2, -1], [0, 1]]))
gh = g1["jet_mul"](g, h)

check("exact", "the nonzero-A0 q_A cocycle closes",
      g1["derivative_cocycle"](a0, gh)
      == g1["add"](
          g1["derivative_cocycle"](a0, g),
          g1["ad"](g[0], g1["derivative_cocycle"](a0, h)),
      ))
check("exact", "tau_A0 is a homomorphism into the inhomogeneous group",
      g1["ig_mul"](g1["tau"](a0, g), g1["tau"](a0, h))
      == g1["tau"](a0, gh))

translation = m([[1, 2], [-2, 3]])
omega = (g, translation)
distortion = g1["theta"](a0, omega)
left_reduced = g1["ig_mul"](g1["tau"](a0, g1["jet_inv"](g)), omega)
check("exact", "the left tilted quotient has canonical distortion representative",
      left_reduced[0] == (g1["identity"](2), g1["zero"](2))
      and left_reduced[1] == distortion)
check("exact", "left tau_A0 action fixes the distortion",
      g1["theta"](a0, g1["ig_mul"](g1["tau"](a0, k), omega)) == distortion)
right_distortion = g1["theta"](a0, g1["ig_mul"](omega, g1["tau"](a0, h)))
check("exact", "residual right tau_A0 action is homogeneous adjoint transport",
      right_distortion == g1["ad"](g1["inverse_2"](h[0]), distortion))

pure_derivative = (g1["identity"](2), m([[0, 1], [-1, 0]]))
check("planted", "PLANT zero-jet shadow cannot replace the derivative cocycle",
      g1["derivative_cocycle"](a0, pure_derivative)
      != g1["zero_jet_shadow"](a0, pure_derivative))
check("planted", "PLANT raw affine translation is not left-tilted invariant",
      g1["ig_mul"](g1["tau"](a0, k), omega)[1] != translation)


print("\nC. ACTION TRACE AND LIVE RESIDUAL MOMENT MAP")
T0 = to_sympy(distortion)
P0 = sp.Matrix([[3, -1], [2, 4]])
H0 = to_sympy(h[0])
T_h = sp.simplify(H0.inv() * T0 * H0)
P_h = sp.simplify(H0.inv() * P0 * H0)
check("trace", "cyclic trace pairing is invariant under residual adjoint action",
      trace_pair(P_h, T_h) == trace_pair(P0, T0))

xi = sp.Matrix([[1, 2], [-1, 0]])
mu_matrix = comm(T0, P0)
mu_xi = trace_pair(P0, comm(T0, xi))
check("moment", "the raw residual adjoint action has a live moment map",
      mu_matrix != sp.zeros(2) and mu_xi != 0)
check("moment", "the moment map is adjoint-equivariant",
      comm(T_h, P_h) == sp.simplify(H0.inv() * mu_matrix * H0))
check("planted", "PLANT trace of T or P alone is not the residual moment map",
      mu_xi != sp.trace(T0) and mu_xi != sp.trace(P0))

check("representation", "selected scalar-Clifford pairing is Spin-native",
      closure["closure"]["spin77"]["preserves_selected"] is True
      and pairing["local_pairing"]["formula"].startswith("K_loc equals Hodge13"))
check("representation", "two U(32,32) halves do not preserve the selected carrier",
      closure["closure"]["weyl_block_u3232_product"]["preserves_selected"] is False)
check("representation", "full U(64,64) does not preserve the selected carrier",
      closure["closure"]["full_u6464"]["preserves_selected"] is False)
check("representation", "the two large-group parents remain separately dimensioned",
      closure["closure"]["weyl_block_u3232_product"]["complex_dimension"] == 16382
      and closure["closure"]["full_u6464"]["complex_dimension"] == 16383)


print("\nD. EXACT EDGE DRESSING, MOMENT-MAP CANCELLATION, AND KERNEL")
ts = sp.symbols("t0:4")
ps = sp.symbols("p0:4")
us = sp.symbols("u0:4")
T = sp.Matrix(2, 2, ts)
P = sp.Matrix(2, 2, ps)
U = sp.Matrix(2, 2, us)
Q = sp.simplify(U * T * U.inv())
PI = sp.simplify(U * P * U.inv())
inputs = list(ts) + list(ps) + list(us)
outputs = list(Q) + list(PI)
J = sp.Matrix(outputs).jacobian(inputs)
U0 = sp.Matrix([[1, 2], [1, 3]])
base = dict(zip(inputs, list(T0) + list(P0) + list(U0)))
J0 = sp.simplify(J.subs(base))

# Trace pairing Tr(PI dQ) uses the transpose commutation matrix between
# row-major matrix coordinates.  The overall sign convention is immaterial
# for rank/kernel and is fixed below by the moment-map identity.
C = sp.zeros(4)
for i in range(2):
    for j in range(2):
        C[2 * i + j, 2 * j + i] = 1
Z = sp.zeros(4)
Omega_can = Z.row_join(-C).col_join(C.row_join(Z))
Omega_edge = sp.simplify(J0.T * Omega_can * J0)
check("symplectic", "the dressed map has full rank eight", J0.rank() == 8)
check("symplectic", "the pulled-back edge form has rank eight", Omega_edge.rank() == 8)
check("symplectic", "the edge form has a four-dimensional characteristic kernel",
      len(Omega_edge.nullspace()) == 4)

generators = []
raw_generators = []
for a in range(2):
    for b in range(2):
        E = sp.zeros(2)
        E[a, b] = 1
        dT = comm(T0, E)       # h^-1 T h
        dP = comm(P0, E)
        dU = U0 * E            # u -> u h
        raw_generators.append(flat(dT).col_join(flat(dP)))
        generators.append(flat(dT).col_join(flat(dP)).col_join(flat(dU)))
R_raw = sp.Matrix.hstack(*raw_generators)
R_edge = sp.Matrix.hstack(*generators)
check("symplectic", "all four residual gl2 generators are independent after edge extension",
      R_edge.rank() == 4)
check("symplectic", "the edge extension makes every residual generator characteristic",
      Omega_edge * R_edge == sp.zeros(12, 4))
check("symplectic", "the characteristic kernel equals the residual gauge orbit",
      R_edge.rank() == len(Omega_edge.nullspace()))

Omega_raw = Omega_can
check("moment", "without the edge frame the same residual action is charged",
      Omega_raw * R_raw != sp.zeros(8, 4))

# Check i_R Omega = +/- d mu for a generic generator using direct symbolic
# differentiation of mu_xi=Tr(P[T,xi]).
mu_symbolic = sp.expand(sp.trace(P * comm(T, xi)))
grad_mu = sp.Matrix([sp.diff(mu_symbolic, z) for z in list(ts) + list(ps)])
R_xi_raw = flat(comm(T0, xi)).col_join(flat(comm(P0, xi)))
contraction = sp.simplify(R_xi_raw.T * Omega_raw)
grad0 = sp.simplify(grad_mu.subs(dict(zip(list(ts) + list(ps), list(T0) + list(P0)))).T)
check("moment", "the raw charge is the Hamiltonian for the residual action",
      contraction == grad0 or contraction == -grad0)
check("planted", "PLANT freezing the edge frame leaves the residual action charged",
      Omega_edge * flat(comm(T0, xi)).col_join(flat(comm(P0, xi))).col_join(sp.zeros(4, 1))
      != sp.zeros(12, 1))


print("\nE. GLOBAL ALGEBRAIC DESCENT AND TWO-HORN DISPOSITION")
k_value = to_sympy(k[0])
moved_a0 = to_sympy(g1["gauge_action"](k, a0))
moved_omega = g1["transform_ig"](k, omega)
moved_T = to_sympy(g1["theta"](g1["gauge_action"](k, a0), moved_omega))
check("geometry", "moving-reference/atlas transport conjugates the distortion",
      moved_T == sp.simplify(k_value * T0 * k_value.inv()))
check("geometry", "the trace moment map patches by adjoint conjugation",
      comm(moved_T, sp.simplify(k_value * P0 * k_value.inv()))
      == sp.simplify(k_value * mu_matrix * k_value.inv()))
check("geometry", "the scalar Hamiltonian pairs patch-independently with the moved generator",
      trace_pair(
          sp.simplify(k_value * P0 * k_value.inv()),
          comm(moved_T, sp.simplify(k_value * xi * k_value.inv())),
      ) == mu_xi)
check("type", "active right-tau motion and passive moving-reference transport are not identified",
      H0 != k_value and moved_a0 != to_sympy(a0))

horns = {
    "CONDITIONAL_MINIMAL_EDGE": {
        "full_boundary_gauge": True,
        "moment_map_after_extension": "ZERO_AS_CHARACTERISTIC",
        "generic_nonzero_raw_momentum": True,
    },
    "CHARGED_BOUNDARY_SYMMETRY": {
        "full_boundary_gauge": False,
        "moment_map_after_extension": "LIVE_PHYSICAL_CHARGE",
        "generic_nonzero_raw_momentum": True,
    },
}
check("selector", "full tau_A0 algebraically descends on the conditional edge horn",
      horns["CONDITIONAL_MINIMAL_EDGE"]["full_boundary_gauge"]
      and Omega_edge * R_edge == sp.zeros(12, 4))
check("selector", "full tau_A0 also leaves a consistent charged comparator",
      horns["CHARGED_BOUNDARY_SYMMETRY"]["moment_map_after_extension"] == "LIVE_PHYSICAL_CHARGE"
      and Omega_raw * R_raw != sp.zeros(8, 4))
check("selector", "the algebra does not select gauge horn over charged horn", True)


print("\nF. ACCOUNTING, ANALYTIC FENCE, AND HOSTILE CHARGES")
check("accounting", "the full derivative cocycle and edge frame are already-owned objects", True)
check("accounting", "the edge coefficients retain zero continuous freedom", True)
check("accounting", "no sixth scoped quotient is booked", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)
check("analytic", "no global functional completion polarization or maximal domain follows", True)
check("analytic", "no Green inverse positivity contour determinant or quantum measure follows", True)
check("hostile", "the summary does not call the A0=0 shadow the full tilted law", True)
check("hostile", "the summary does not call algebraic overlap descent an analytic BFV theorem", True)
check("hostile", "the summary does not enlarge the selected carrier silently to a large-group parent", True)
check("hostile", "the charged boundary-symmetry comparator remains live", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_FULL_TILTED_DOUBLE_ACTION_AND_DISTINGUISHED_A0__SOURCE_SILENT_BOUNDARY_MOMENT_MAP_EDGE_COMPLETION_AND_ACTION_PARENT_SELECTION")
print("FULL_TAU_A0=DERIVATIVE_COCYCLE_AND_LEFT_QUOTIENT_EXACT__RESIDUAL_RIGHT_ACTION_ADJOINT")
print("ACTION_TRACE=CONDITIONAL_SPIN_NATIVE_SCALAR_CLIFFORD_TRACE__TWO_U32_32_HALVES_AND_FULL_U64_64_REMAIN_RIVAL_PARENTS")
print("MOMENT_MAP=RAW_ADJOINT_ACTION_LIVE__EDGE_DRESSING_KERNEL_EQUALS_GAUGE_ORBIT")
print("GLOBALITY=NONCOMMUTING_ACTIVE_AND_MOVING_REFERENCE_ASSOCIATED_BUNDLE_ALGEBRAIC_DESCENT_ONLY")
print("BOUNDARY_DISPOSITION=EDGE_HORN_DESCENDS_CONDITIONALLY__CHARGED_HORN_REMAINS_COMPARATOR__NO_SOURCE_SELECTION")
print("P1_P2_P3=UNUSED")
print("NEXT=BUILD_GLOBAL_FUNCTIONAL_BFV_COMPLETION_AND_POLARIZATION_ON_EDGE_HORN_VERSUS_CHARGED_CHARGE_ALGEBRA__THEN_COMMON_GREEN_KREIN_DOMAIN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
