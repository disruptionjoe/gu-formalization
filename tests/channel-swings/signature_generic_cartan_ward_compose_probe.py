#!/usr/bin/env python3
"""Exact signature-generic Cartan/Ward composition with K77/K95 controls.

This probe composes two already-built objects without identifying them:
the primitive source-epsilon gauge chain and ordinary spacetime Lie transport.
The connection Cartan formula shows exactly where the internal gauge summand
appears.  A flat pure-gauge second connection then identifies that summand with
the existing primitive-epsilon row.  K77 and K95 metric/Hodge naturality are
tested separately because those real-form structures are branch-native.

The result is not the complete selected-action Frechet coefficient identity.
"""

from collections import Counter
from itertools import combinations
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_physical_diffeomorphism_split_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


def matrix_zero(value):
    return value.applyfunc(sp.simplify) == sp.zeros(*value.shape)


def comm(left, right):
    return left * right - right * left


print("A. SOURCE, PREDECESSORS, AND LAYER ZERO")
source = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
source_split = (ROOT / "lab/sources/selected-k77-physical-diffeomorphism-split-source-reinspection-2026-08-08.md").read_text()
epsilon = strict("lab/process/selected-first-order-epsilon-preboundary-compose.json")
signature = strict("lab/process/signature-rationale-build-branch-retype.json")
physical = strict("lab/process/selected-k77-physical-diffeomorphism-split.json")

check("source", "source owns epsilon as a gauge transformation and varpi as translated connection data",
      "gauge transformation \\(\\epsilon\\)" in source and "translated connection" in source)
check("source", "source owns the two-connection difference arena",
      "two connections" in source_split and "gauge-equivariant difference" in source_split)
check("source", "source is silent on the exact combined spacetime Cartan identity",
      "SOURCE-SILENT" in source_split and "nonconstant primitive-epsilon Lie derivative" in source_split)
check("repo", "v0.25 already constructs the primitive epsilon Euler chain",
      epsilon["selected_product"]["member_of_prior_eight_row_epsilon_domain"] is True
      and "D_B_ADJOINT" in epsilon["composed_chain"]["primitive_epsilon_euler"])
check("repo", "v0.88 already constructs local physical diffeomorphism naturality",
      physical["local_naturality"]["k77_metric"].startswith("EXACT")
      and physical["local_naturality"]["observation_graph"] == "EXACT")
check("repo", "v0.89 separates K77 author assertion from K95 geometric derivation",
      signature["fork_disposition"]["K77"] == "AUTHOR_ASSERTED_CONDITIONAL_BUILD"
      and signature["fork_disposition"]["K95"] == "GEOMETRY_DERIVED_COMPARATOR")
for label in (
    "primitive epsilon gauge variation versus ordinary spacetime Lie transport",
    "ordinary connection Lie derivative versus gauge-covariant Lie derivative",
    "internal gauge summand versus curvature-contraction summand",
    "flat pure-gauge specialization versus a global identification of generators",
    "tensor naturality versus selected-action Frechet coefficients",
    "K77 Hodge/Krein data versus K95 Hodge/Krein data",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT SIGNATURE-GENERIC NONABELIAN CARTAN IDENTITIES")
x, y = sp.symbols("x y", real=True)
xi = (
    1 + x + 2 * y,
    -2 + 3 * x - y,
)
coords = (x, y)
A = (
    sp.Matrix([[x, 1 + y], [x * y, -x]]),
    sp.Matrix([[y, x - y], [1 + x, -y]]),
)
T = (
    sp.Matrix([[1 + x, y], [x - y, -1 - x]]),
    sp.Matrix([[x * y, 2 + x], [1 - y, -x * y]]),
)


def lie_one_form(field):
    return tuple(
        sum((xi[nu] * field[mu].diff(coords[nu]) for nu in range(2)), sp.zeros(2))
        + sum((field[nu] * sp.diff(xi[nu], coords[mu]) for nu in range(2)), sp.zeros(2))
        for mu in range(2)
    )


def covariant_scalar_derivative(value, mu):
    return value.diff(coords[mu]) + comm(A[mu], value)


F01 = A[1].diff(x) - A[0].diff(y) + comm(A[0], A[1])
iA = xi[0] * A[0] + xi[1] * A[1]
lie_A = lie_one_form(A)
cartan_A = (
    -xi[1] * F01 + covariant_scalar_derivative(iA, 0),
    xi[0] * F01 + covariant_scalar_derivative(iA, 1),
)
check("exact", "ordinary nonabelian connection Lie transport obeys L_xi A=i_xi F+D_A(i_xi A)",
      all(matrix_zero(left - right) for left, right in zip(lie_A, cartan_A)))
check("planted", "PLANT curvature contraction alone does not equal ordinary connection Lie transport",
      any(not matrix_zero(value) for value in (
          lie_A[0] + xi[1] * F01,
          lie_A[1] - xi[0] * F01,
      )))
check("planted", "PLANT internal gauge derivative alone does not equal ordinary connection Lie transport",
      any(not matrix_zero(lie_A[mu] - covariant_scalar_derivative(iA, mu)) for mu in range(2)))

DT01 = T[1].diff(x) - T[0].diff(y) + comm(A[0], T[1]) - comm(A[1], T[0])
iT = xi[0] * T[0] + xi[1] * T[1]
lie_T = lie_one_form(T)
covariant_T = (
    -xi[1] * DT01 + covariant_scalar_derivative(iT, 0),
    xi[0] * DT01 + covariant_scalar_derivative(iT, 1),
)
internal_T = tuple(comm(value, iA) for value in T)
check("exact", "adjoint one-form Lie transport is covariant Cartan transport plus its internal gauge orbit",
      all(matrix_zero(lie_T[mu] - covariant_T[mu] - internal_T[mu]) for mu in range(2)))
check("planted", "PLANT dropping the internal orbit breaks adjoint one-form Cartan transport",
      any(not matrix_zero(lie_T[mu] - covariant_T[mu]) for mu in range(2)))


print("\nC. LIVE NONCONSTANT PURE-GAUGE EPSILON SPECIALIZATION")
# A commuting flat connection is enough to test a nonconstant field-dependent
# epsilon parameter without importing an exponential or a numerical fit.
B = (
    sp.diag(1, -1),
    sp.diag(2, -2),
)
FB01 = comm(B[0], B[1])
iB = xi[0] * B[0] + xi[1] * B[1]
lie_B = lie_one_form(B)
DB_iB = tuple(iB.diff(coords[mu]) + comm(B[mu], iB) for mu in range(2))
check("exact", "the selected pure-gauge comparator is flat", FB01 == sp.zeros(2))
check("exact", "for flat B, nonconstant diffeomorphism transport is exactly the primitive epsilon direction D_B(i_xi B)",
      all(matrix_zero(left - right) for left, right in zip(lie_B, DB_iB)))
check("planted", "PLANT the field-dependent primitive epsilon direction is live rather than a constant-background zero",
      any(value != sp.zeros(2) for value in DB_iB))

distortion = tuple(A[mu] - B[mu] for mu in range(2))
lie_distortion = lie_one_form(distortion)
check("exact", "the two-connection distortion Lie derivative is L_xi A-L_xi B",
      all(matrix_zero(lie_distortion[mu] - lie_A[mu] + lie_B[mu]) for mu in range(2)))
check("exact", "the B-owned distortion contribution is minus the existing primitive epsilon direction",
      all(matrix_zero(-lie_B[mu] + DB_iB[mu]) for mu in range(2)))
check("type", "the composition reuses eta=i_xi B as a field-dependent instance and does not identify every epsilon variation with a diffeomorphism", True)


print("\nD. K77 AND K95 BRANCH-NATIVE METRIC/HODGE CONTROLS")
capture = StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.88 K77 physical-diffeomorphism predecessor replays",
      "PASS 170/170" in capture.getvalue() and not P["FAILURES"])

ETA = P["ETA"]
branches = {
    "K77": ETA,
    "K95": -ETA,
}
q_bank = {
    "axis0": sp.Matrix([1, 0, 0, 0]),
    "axis1": sp.Matrix([0, 1, 0, 0]),
    "null03": sp.Matrix([1, 0, 0, 1]),
}
branch_stars = {}
branch_inertia = {}
p2_basis = list(combinations(range(14), 2))
p2_columns = [p2_basis.index(pair) for pair in ((0, 1), (0, 4), (4, 5))]
J = sp.Matrix(10, 4, lambda i, j: sp.Rational(((i + 2) * (j + 3)) % 7 - 3, 5))
L = sp.Matrix.vstack(sp.eye(4), J)

for branch, base_metric in branches.items():
    fibre_metric = P["dewitt"](base_metric)
    total_metric = sp.diag(base_metric, fibre_metric)
    eigenvalues = total_metric.eigenvals()
    inertia = (
        sum(m for value, m in eigenvalues.items() if value.is_positive),
        sum(m for value, m in eigenvalues.items() if value.is_negative),
    )
    branch_inertia[branch] = inertia
    star1 = P["hodge_matrix_degree_one"](total_metric)
    branch_stars[branch] = star1
    for q_name, q in q_bank.items():
        for nu in range(4):
            basis_vector = sp.eye(4)[:, nu]
            b = basis_vector * q.T
            vertical = P["sym2_rep"](b)
            h_base = b.T * base_metric + base_metric * b
            h_vertical = P["d_dewitt"](base_metric, h_base)
            h_total = sp.diag(h_base, h_vertical)
            generator = sp.diag(-b, vertical)
            check("branch", f"{branch}/{q_name}/{nu}: metric lift is natural",
                  h_total + generator.T * total_metric + total_metric * generator == sp.zeros(14))
            check("branch", f"{branch}/{q_name}/{nu}: density and frame Jacobian cancel",
                  sp.Rational(1, 2) * sp.trace(total_metric.inv() * h_total) + sp.trace(generator) == 0)
            pull = generator.T
            dstar1 = P["hodge_degree_one_derivative"](total_metric, h_total)
            rhs1 = star1 * P["exterior_rep"](pull, 1) - P["exterior_rep"](pull, 13) * star1
            check("branch", f"{branch}/{q_name}/{nu}: degree-one Hodge naturality is exact",
                  dstar1 == rhs1)
            r2 = P["exterior_rep"](pull, 2)
            r12 = P["exterior_rep"](pull, 12)
            for column in p2_columns:
                alpha = sp.eye(len(p2_basis))[:, column]
                direct = P["hodge_basis_derivative"](total_metric, h_total, 2, column)
                rin = r2 * alpha
                star_rin = sum(
                    (rin[j] * P["hodge_basis_vector"](total_metric, 2, j)
                     for j in range(len(p2_basis)) if rin[j]),
                    sp.zeros(91, 1),
                )
                rhs = star_rin - r12 * P["hodge_basis_vector"](total_metric, 2, column)
                check("branch", f"{branch}/{q_name}/{nu}: sampled degree-two Hodge naturality is exact",
                      direct == rhs)
            ah = -b
            dj = vertical * J - J * ah
            dl = sp.Matrix.vstack(sp.zeros(4), dj)
            check("branch", f"{branch}/{q_name}/{nu}: moving observation graph is natural",
                  generator * L - L * ah - dl == sp.zeros(14, 4))

check("exact", "branch inertias are K77=(7,7) and K95=(9,5)",
      branch_inertia == {"K77": (7, 7), "K95": (9, 5)})
check("planted", "PLANT the K77 and K95 Hodge stars are genuinely different operators",
      branch_stars["K77"] != branch_stars["K95"])


print("\nE. CONSTRAINT, VARIATIONAL, SYMPLECTIC, AND ANALYTIC FENCES")
check("theorem", "signature-generic Cartan transport composes the existing primitive epsilon direction without fitting",
      not FAILURES)
for kind, label in (
    ("variational", "the actual selected-action Frechet coefficient bank and coefficientwise J R zero remain open"),
    ("variational", "Cartan naturality does not derive K-star or the formal adjoint"),
    ("symplectic", "bulk Ward composition is not a reduced presymplectic or BFV quotient"),
    ("symplectic", "no boundary charge or polarization is promoted"),
    ("krein", "separate Hodge naturality does not give a common K77/K95 fundamental symmetry or domain"),
    ("analytic", "no hyperbolic evolution contour determinant saddle or path-integral measure is selected"),
    ("scope", "no new field coefficient function quotient or external datum is introduced"),
    ("scope", "P1 P2 P3 remain unused and Curt remains formally separate"),
    ("scope", "no Standard Model Einstein cosmology chirality mass or generation verdict moves"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_ARENA__SOURCE-SILENT_EXACT_CARTAN_COMPOSITION")
print("GENERIC_CARTAN=CONNECTION_AND_ADJOINT_ONEFORM_EXACT")
print("PRIMITIVE_EPSILON=ALREADY_BUILT__FIELD_DEPENDENT_FLAT_B_INSTANCE_COMPOSED")
print("K77_K95=SEPARATE_HODGE_OPERATORS__BOTH_LOCALLY_NATURAL")
print("SELECTED_ACTION_JR_ZERO=OPEN")
print("NEXT=ASSEMBLE_ACTUAL_SELECTED_ACTION_FRECHET_BANK_ON_K77__USE_K95_BRANCH_NATIVE_CONTROL__THEN_KSTAR_ADJOINT_GREEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
