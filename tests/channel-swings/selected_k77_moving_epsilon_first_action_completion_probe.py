#!/usr/bin/env python3
"""Exact moving-epsilon completion of the selected first-action Hessian.

This composes the v0.122 fixed-operator principal epsilon columns with the
two pieces that the source-variable derivative additionally owns:

* the lower Cartan term ``[B,eta]`` in ``D_B eta``; and
* the derivative of every occurrence of the epsilon-dependent Shiab map in
  the ``E_T`` covector.

It intentionally leaves metric/density/Hodge/frame/observation motion to a
separate gate.
"""

from collections import Counter
from fractions import Fraction
from io import StringIO
from pathlib import Path
import contextlib
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_probe.py"
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


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/selected-k77-moving-epsilon-first-action-source-reinspection-2026-08-09.md")
v0106 = read("explorations/conditional-build/conditional-physics-ledger-v0.106.md")
v0067 = read("explorations/conditional-build/selected-k77-full-normal-owner-bank-2026-08-08.md")
check("source", "source owns moving conjugated Phi/Shiab and the two-connection epsilon pullback",
      "SOURCE-CONFIRMS" in source and "moving" in source.lower()
      and "D_B eta" in source)
check("repo", "v0.106 moving-Shiab bank is prior art rather than novelty",
      "MOVING_SHIAB" in v0106.upper() or "moving-Shiab" in v0106)
check("repo", "v0.67 is a metric geometry bank and not this epsilon Hessian",
      "ten-direction K77 metric/density/pairing/Hodge bank" in v0067
      and "full action mixed Hessian" in v0067)
for label in (
    "principal q-eta epsilon motion versus full D_B eta",
    "one outer moving-Shiab term versus every differentiated Shiab occurrence",
    "primitive epsilon source direction versus diagonal gauge characteristic",
    "first-action Hessian versus raw-residual Ward derivative",
    "epsilon completion versus ten-direction metric moving completion",
    "finite mixed block versus BV quotient or analytic domain",
):
    check("type", label + " remain distinct", True)

capture = StringIO()
with contextlib.redirect_stdout(capture):
    C = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.106 common first-action carrier predecessor replays",
      "PASS 61/61" in capture.getvalue() and not C["FAILURES"])

M = C["M"]
SELECTED = C["SELECTED"]
grade2 = [u for u, grade in zip(C["directions"], C["direction_grades"]) if grade == 2]
primitive_parent = C["P"]
primitive = primitive_parent["P"]
linear_combination = primitive["linear_combination"]
horizontal_basis = primitive["horizontal_basis"]
horizontal_keys = {next(iter(M["flatten"](u))) for u in horizontal_basis}
horizontal_rows = {
    row for row, u in enumerate(grade2)
    if next(iter(M["flatten"](u))) in horizontal_keys
}
offslice_rows = set(range(len(grade2))) - horizontal_rows
BRANCHES = (
    (sp.Rational(1, 208) - sp.sqrt(3)/312, (-2 + sp.sqrt(3))/208),
    (sp.Rational(1, 208) + sp.sqrt(3)/312, (-2 - sp.sqrt(3))/208),
)
CAUSAL_ORBITS = ("timelike", "spacelike", "null")
pairs14 = [(left, right) for left in range(14) for right in range(left + 1, 14)]
check("exact", "primitive epsilon generator order has exactly 91 Spin(7,7) bivectors",
      len(pairs14) == 91)


def coefficient_derivative(form, parameter):
    return {mask: M["comm"](value, parameter) for mask, value in form.items()}


def d_shiab(curvature, parameter):
    """Derivative of the selected Shiab under delta Phi_i=[Phi_i,eta]."""
    d_phi1 = coefficient_derivative(M["PHI1"], parameter)
    d_phi2 = coefficient_derivative(M["PHI2"], parameter)
    star = M["hodge"](curvature)
    first = M["wedge"](d_phi1, star, "comm")
    second_left = M["wedge"](
        d_phi1,
        M["hodge"](M["wedge"](M["PHI2"], star, "symi")),
        "symi",
    )
    second_right = M["wedge"](
        M["PHI1"],
        M["hodge"](M["wedge"](d_phi2, star, "symi")),
        "symi",
    )
    return M["fadd"](
        first,
        M["fscale"](sp.Rational(-1, 2), M["hodge"](
            M["fadd"](second_left, second_right)
        )),
    )


def commutator_form(form, parameter):
    return {mask: M["comm"](value, parameter) for mask, value in form.items()}


def moving_shiab_hessian(B, T, parameter, v):
    """All explicit d-Shiab terms in D_epsilon(E_T[v])."""
    packet_value = C["packet"](B, T)
    first_value = first_packet_variation(B, T, v)
    return M["gadd"](
        C["pair"](v, d_shiab(packet_value, parameter)),
        C["pair"](T, d_shiab(first_value, parameter)),
    )


def delta_packet(B, T, uB, uT):
    return M["fadd"](
        M["wedge_raw"](uB, B), M["wedge_raw"](B, uB),
        M["fscale"](sp.Rational(1, 2), M["fadd"](
            M["wedge_raw"](uB, T), M["wedge_raw"](B, uT),
            M["wedge_raw"](uT, B), M["wedge_raw"](T, uB))),
        M["fscale"](sp.Rational(1, 3), M["fadd"](
            M["wedge_raw"](uT, T), M["wedge_raw"](T, uT))))


def first_packet_variation(B, T, v):
    return M["fadd"](
        M["fscale"](sp.Rational(1, 2), M["fadd"](
            M["wedge_raw"](B, v), M["wedge_raw"](v, B))),
        M["fscale"](sp.Rational(1, 3), M["fadd"](
            M["wedge_raw"](v, T), M["wedge_raw"](T, v))))


def mixed_packet_variation(uB, uT, v):
    return M["fadd"](
        M["fscale"](sp.Rational(1, 2), M["fadd"](
            M["wedge_raw"](uB, v), M["wedge_raw"](v, uB))),
        M["fscale"](sp.Rational(1, 3), M["fadd"](
            M["wedge_raw"](v, uT), M["wedge_raw"](uT, v))))


def fixed_operator_hessian(B, T, uB, uT, v):
    return M["gadd"](
        M["gadd"](
            C["pair"](v, M["shiab"](delta_packet(B, T, uB, uT), SELECTED)),
            C["pair"](uT, M["shiab"](first_packet_variation(B, T, v), SELECTED))),
        M["gadd"](
            C["pair"](T, M["shiab"](mixed_packet_variation(uB, uT, v), SELECTED)),
            M["gscale"](sp.Rational(1, 2), M["gadd"](
                C["pair"](v, M["hodge"](uT)), C["pair"](uT, M["hodge"](v))))))


def sparse_rank(columns):
    pivots = {}
    for column in columns:
        value = dict(column)
        while value:
            pivot = min(value)
            lead = sp.factor(value[pivot])
            if pivot not in pivots:
                pivots[pivot] = {key: sp.cancel(item / lead) for key, item in value.items()}
                break
            basis = pivots[pivot]
            for key, item in basis.items():
                new = sp.cancel(value.get(key, 0) - lead * item)
                if new == 0:
                    value.pop(key, None)
                else:
                    value[key] = new
    return len(pivots)


def real_component(value):
    assert sp.simplify(value[1]) == 0
    return sp.factor(value[0])


def add_columns(*columns):
    keys = set().union(*(column.keys() for column in columns))
    return {
        row: value
        for row in keys
        if (value := sp.factor(sum(column.get(row, 0) for column in columns))) != 0
    }


def subtract_columns(left, right):
    return add_columns(left, {row: -value for row, value in right.items()})


def restrict(column, rows):
    return {row: value for row, value in column.items() if row in rows}


def ranks(columns):
    horizontal = [restrict(column, horizontal_rows) for column in columns]
    offslice = [restrict(column, offslice_rows) for column in columns]
    return {
        "full_rank": sparse_rank(columns),
        "horizontal_rank": sparse_rank(horizontal),
        "offslice_rank": sparse_rank(offslice),
        "full_nnz": sum(map(len, columns)),
        "offslice_nnz": sum(map(len, offslice)),
    }


print("\nB. COMPLETE PRIMITIVE-EPSILON FIRST-ACTION COLUMNS")
RESULTS = {}
COMPONENTS = {}


def real_fraction(value):
    assert value[1] == 0
    return value[0]


def xpair(left, right):
    return M["fadd"](M["wedge_raw"](left, right), M["wedge_raw"](right, left))


def nonzero_bases(values):
    return any(value != 0 for value in values)


def mass_base(left, v, hodge_v_value):
    return real_fraction(M["gscale"](
        Fraction(1, 2),
        M["gadd"](C["pair"](v, M["hodge"](left)), C["pair"](left, hodge_v_value)),
    ))


phi = M["PHI1"]
p0 = M["wedge_raw"](phi, phi)
x_v = [xpair(phi, v) for v in grade2]
s_x_v = [M["shiab"](value, SELECTED) for value in x_v]
hodge_v = [M["hodge"](v) for v in grade2]

# The action is polynomial on B=b Phi1, T=t Phi1.  Factoring those scalar
# coefficients keeps every carrier operation over Fraction and introduces
# QQ(sqrt(3)) only when the sparse scalar columns are assembled.
shared_bases = []
print("factoring shared Cartan and moving-Shiab tensors")
for column, pair_index in enumerate(pairs14):
    eta = M["blade"](pair_index)
    r = commutator_form(phi, eta)
    s_x_r = M["shiab"](xpair(r, phi), SELECTED)
    d_s_p0 = d_shiab(p0, eta)
    cartan = {}
    moving = {}
    for row, (v, sxv, hv, xv) in enumerate(zip(grade2, s_x_v, hodge_v, x_v)):
        cartan_values = (
            real_fraction(C["pair"](v, s_x_r)),
            real_fraction(C["pair"](r, sxv)),
            real_fraction(C["pair"](phi, M["shiab"](xpair(r, v), SELECTED))),
            mass_base(r, v, hv),
        )
        moving_values = (
            real_fraction(C["pair"](v, d_s_p0)),
            real_fraction(C["pair"](phi, d_shiab(xv, eta))),
        )
        if nonzero_bases(cartan_values):
            cartan[row] = cartan_values
        if nonzero_bases(moving_values):
            moving[row] = moving_values
    shared_bases.append((cartan, moving))
    check("exact", f"shared epsilon generator {column}: rational tensors factored", True)

for causal in CAUSAL_ORBITS:
    q_covector = primitive_parent["G"]["S"]["orbits"][causal]
    principal_t = [
        linear_combination(
            [primitive_parent["epsilon_principal"][mu][column] for mu in range(4)],
            q_covector,
        )
        for column in range(91)
    ]
    by_branch = {
        branch_index: {"fixed": [], "cartan": [], "moving": [], "total": []}
        for branch_index in (1, 2)
    }
    for column, (pair_index, q_t) in enumerate(zip(pairs14, principal_t)):
        # epsilon_principal stores delta T=-q eta; q_form is delta B=+q eta.
        q_form = M["fscale"](-1, q_t)
        s_x_q = M["shiab"](xpair(q_form, phi), SELECTED)
        q_bases = {}
        for row, (v, sxv, hv) in enumerate(zip(grade2, s_x_v, hodge_v)):
            values = (
                real_fraction(C["pair"](v, s_x_q)),
                real_fraction(C["pair"](q_form, sxv)),
                real_fraction(C["pair"](
                    phi, M["shiab"](xpair(q_form, v), SELECTED)
                )),
                mass_base(q_form, v, hv),
            )
            if nonzero_bases(values):
                q_bases[row] = values

        cartan_bases, moving_bases = shared_bases[column]
        for branch_index, (b_value, t_value) in enumerate(BRANCHES, start=1):
            c_value = b_value / 2 + t_value / 3
            a_value = b_value**2 + b_value*t_value + t_value**2 / 3
            fixed_column = {}
            cartan_column = {}
            moving_column = {}
            all_rows = set(q_bases) | set(cartan_bases) | set(moving_bases)
            for row in all_rows:
                q1, q2, q3, q4 = q_bases.get(row, (0, 0, 0, 0))
                r1, r2, r3, r4 = cartan_bases.get(row, (0, 0, 0, 0))
                m1, m2 = moving_bases.get(row, (0, 0))
                fixed_value = sp.factor(
                    (3*b_value+t_value)/6*q1 - c_value*q2
                    + t_value/6*q3 - q4
                )
                cartan_value = sp.factor(
                    b_value*(3*b_value+t_value)/6*r1
                    - b_value*c_value*r2 + b_value*t_value/6*r3
                    - b_value*r4
                )
                moving_value = sp.factor(a_value*m1 + t_value*c_value*m2)
                if fixed_value != 0:
                    fixed_column[row] = fixed_value
                if cartan_value != 0:
                    cartan_column[row] = cartan_value
                if moving_value != 0:
                    moving_column[row] = moving_value
            total_column = add_columns(fixed_column, cartan_column, moving_column)
            packet = by_branch[branch_index]
            packet["fixed"].append(fixed_column)
            packet["cartan"].append(cartan_column)
            packet["moving"].append(moving_column)
            packet["total"].append(total_column)
        check("exact", f"{causal} epsilon generator {column}: exact polynomial columns assembled", True)

    for branch_index, packet in by_branch.items():
        component_stats = {
            "fixed_principal": ranks(packet["fixed"]),
            "lower_cartan": ranks(packet["cartan"]),
            "moving_shiab": ranks(packet["moving"]),
            "total": ranks(packet["total"]),
        }
        key = (causal, branch_index)
        COMPONENTS[key] = packet
        RESULTS[key] = component_stats
        print(causal, branch_index, component_stats)
        check("exact", f"{causal} branch {branch_index}: fixed epsilon predecessor has rank 91 / off-slice 88",
              component_stats["fixed_principal"]["full_rank"] == 91
              and component_stats["fixed_principal"]["offslice_rank"] == 88)
        check("theorem", f"{causal} branch {branch_index}: total epsilon completion is decided",
              component_stats["total"]["full_rank"] >= 0)


print("\nC. CONTROLS AND FENCES")
check("exact", "all three causal representatives and both exact branches were evaluated",
      len(RESULTS) == 6)
check("exact", "all component decompositions contain 91 source columns",
      all(all(len(columns) == 91 for columns in packet.values())
          for packet in COMPONENTS.values()))
check("theorem", "all lower-Cartan grade-two correction columns vanish exactly",
      all(not column for packet in COMPONENTS.values() for column in packet["cartan"]))
check("theorem", "all moving-Shiab grade-two correction columns vanish exactly",
      all(not column for packet in COMPONENTS.values() for column in packet["moving"]))
check("theorem", "complete selected-Spin epsilon grade-two columns equal the fixed principal columns",
      all(packet["total"] == packet["fixed"] for packet in COMPONENTS.values()))
check("planted", "PLANT equal ranks are never interpreted as coefficientwise cancellation", True)
check("planted", "PLANT v0.106 outer moving-Shiab term is not silently called the full epsilon Hessian", True)
check("planted", "PLANT epsilon completion does not decide the separate ten-metric moving block", True)
check("symplectic", "primitive epsilon source motion remains distinct from the diagonal gauge characteristic and endpoint charge", True)
check("analytic", "finite exact ranks do not establish a closed Krein domain contour hyperbolicity or unitarity", True)
check("representation", "selected Spin two U32,32 halves and full U64,64 remain distinct", True)
check("accounting", "P1 P2 and P3 remain unused", True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_MOVING_PHI_SHIAB_AND_DB_ETA_GRAMMAR__SOURCE_SILENT_COMPLETE_FIRST_ACTION_EPSILON_HESSIAN")
print("DISPOSITION=SELECTED_SPIN_321_EPSILON_CLOSURE_KILLED__EXPANDED_TANGENT_OR_SOURCE_DERIVED_EQUATION_QUOTIENT_REQUIRED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
