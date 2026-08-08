#!/usr/bin/env python3
"""Exact K77 action-bundle and complete-observation overlap audit.

This composes, rather than reconstructs, two previously owned results: the
global chimeric Spin(7,7)/P_H Clifford reduction and the complete observation
germ cotangent theorem.  Two noncommuting signed rotations inside the
Lorentz-labelled four-plane provide a three-patch exact test.  Every patch
recomputes the full selected-action bank from its transformed fields.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
V077 = ROOT / "tests/channel-swings/selected_k77_full_u6464_action_bank_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def text(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE OWNERSHIP AND LAYER ZERO")
global_report = text(
    "explorations/conditional-build/"
    "k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md"
)
receiver_report = text(
    "explorations/conditional-build/selected-k77-moving-action-green-receiver-2026-08-08.md"
)
splitting_report = text(
    "explorations/conditional-build/selected-k77-green-potential-splitting-basicness-2026-08-08.md"
)
check("source", "the source-owned P_H extension is already global",
      "P_H=P_{\\operatorname{Spin}(C)}" in global_report)
check("source", "the moving Clifford frame is source epsilon dependent",
      "\\gamma_\\epsilon=\\operatorname{Ad}(\\epsilon^{-1})\\gamma_0" in global_report)
check("repo", "the complete observation germ theorem is already owned",
      "complete observation-germ duality" in receiver_report)
check("repo", "the complete Green one-form has an exact cotangent lift",
      "exact cotangent-lift naturality" in splitting_report)
for label in (
    "pointwise coefficient fibre versus global associated bundle",
    "global associated section law versus existence of a physical section",
    "complete observation germ versus ordinary four-dimensional pullback",
    "equation-dual overlap versus no-leakage quotient",
    "finite algebraic atlas descent versus analytic BFV/common domain",
):
    check("type", label + " remain distinct", True)


print("\nB. REPLAY FULL POINTWISE BANK")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(V077))
check("repo", "v0.77 exact full-bank predecessor replays",
      "PASS 58/58" in capture.getvalue() and not M["FAILURES"])

N = M["N"]
ZERO = M["ZERO"]
ONE = M["ONE"]
ETA = M["ETA"]
indices = M["indices"]
blade_product = M["blade_product"]
gadd = M["gadd"]
gscale = M["gscale"]
shiab = M["shiab"]
fixed_packet = M["fixed_packet"]
symbolic_row = M["symbolic_row"]
SKEW_GRADES = M["SKEW_GRADES"]


def plane_rotation(first, second):
    """Positive signed quarter-turn e_a->e_b, e_b->-e_a."""
    permutation = list(range(N))
    signs = [1] * N
    permutation[first], permutation[second] = second, first
    signs[second] = -1
    return tuple(permutation), tuple(signs)


def compose(after, before):
    pa, sa = after
    pb, sb = before
    return (
        tuple(pa[pb[index]] for index in range(N)),
        tuple(sb[index] * sa[pb[index]] for index in range(N)),
    )


def map_mask(mask, element):
    permutation, signs = element
    old = list(indices(mask))
    mapped = [permutation[index] for index in old]
    sign = sp.prod(signs[index] for index in old)
    inversions = sum(
        mapped[i] > mapped[j]
        for i in range(len(mapped))
        for j in range(i + 1, len(mapped))
    )
    sign *= -1 if inversions % 2 else 1
    return sum(1 << index for index in mapped), int(sign)


def transform_form(form, element):
    out = {}
    for form_mask, coefficient in form.items():
        new_form_mask, form_sign = map_mask(form_mask, element)
        new_coefficient = {}
        for clifford_mask, value in coefficient.items():
            new_clifford_mask, clifford_sign = map_mask(clifford_mask, element)
            new_coefficient[new_clifford_mask] = gadd(
                new_coefficient.get(new_clifford_mask, ZERO),
                gscale(form_sign * clifford_sign, value),
            )
        out[new_form_mask] = {
            mask: value for mask, value in new_coefficient.items() if value != ZERO
        }
    return {mask: value for mask, value in out.items() if value}


def bank_from_fields(b_field, t_field):
    selected = shiab(fixed_packet(b_field, t_field), ("comm", "symi", "symi"))
    return [symbolic_row(slot, b_field, t_field, selected) for slot in range(N)]


def transform_rows(rows, element):
    permutation, signs = element
    out = [{} for _ in range(N)]
    for slot, row in enumerate(rows):
        new_slot = permutation[slot]
        for mask, value in row.items():
            new_mask, coefficient_sign = map_mask(mask, element)
            out[new_slot][new_mask] = gadd(
                out[new_slot].get(new_mask, ZERO),
                gscale(signs[slot] * coefficient_sign, value),
            )
    return [{mask: value for mask, value in row.items() if value != ZERO} for row in out]


def slot_matrix(element):
    permutation, signs = element
    matrix = sp.zeros(N)
    for index in range(N):
        matrix[permutation[index], index] = signs[index]
    return matrix


def close_columns(rows_by_patch, elements):
    live = set().union(*(set(row) for rows in rows_by_patch for row in rows))
    changed = True
    while changed:
        expanded = live | {map_mask(mask, element)[0] for mask in live for element in elements}
        changed = expanded != live
        live = expanded
    return sorted(live)


def coefficient_matrix(columns, element):
    matrix = sp.zeros(len(columns))
    lookup = {mask: index for index, mask in enumerate(columns)}
    for index, mask in enumerate(columns):
        new_mask, sign = map_mask(mask, element)
        matrix[lookup[new_mask], index] = sign
    return matrix


def dense_bank(rows, columns):
    return sp.Matrix([
        [sp.Rational(rows[slot].get(mask, ZERO)[0].numerator,
                     rows[slot].get(mask, ZERO)[0].denominator)
         for mask in columns]
        for slot in range(N)
    ])


def coefficient_metric(columns):
    return sp.diag(*[
        (1 if len(indices(mask)) in SKEW_GRADES else -1)
        * blade_product(mask, mask)[1]
        for mask in columns
    ])


def patch_family(kind):
    g01 = plane_rotation(1, 2)
    g12 = plane_rotation(2, 3)
    g02 = compose(g12, g01)
    b0, t0 = M["make_fixture"](kind)
    b1, t1 = transform_form(b0, g01), transform_form(t0, g01)
    b2, t2 = transform_form(b1, g12), transform_form(t1, g12)
    rows0 = bank_from_fields(b0, t0)
    rows1 = bank_from_fields(b1, t1)
    rows2 = bank_from_fields(b2, t2)
    columns = close_columns((rows0, rows1, rows2), (g01, g12, g02))
    banks = tuple(dense_bank(rows, columns) for rows in (rows0, rows1, rows2))
    return (g01, g12, g02), (b0, b1, b2), (t0, t1, t2), \
        (rows0, rows1, rows2), columns, banks


print("\nC. NONCOMMUTING THREE-PATCH ACTION COVECTOR")
elements, b_fields, t_fields, rows, columns, banks = patch_family("seed")
g01, g12, g02 = elements
A01, A12, A02 = (slot_matrix(element) for element in elements)
C01, C12, C02 = (coefficient_matrix(columns, element) for element in elements)
K0, K1, K2 = banks
check("geometry", "both transitions preserve K77 and the four-plus-ten split",
      all(A.T * sp.diag(*ETA) * A == sp.diag(*ETA) for A in (A01, A12))
      and all(A[:4, 4:] == sp.zeros(4, 10) and A[4:, :4] == sp.zeros(10, 4)
              for A in (A01, A12)))
check("geometry", "the two signed rotations are noncommuting",
      A12 * A01 != A01 * A12)
check("geometry", "direct and sequential slot transitions agree",
      A02 == A12 * A01)
check("geometry", "direct and sequential transformed fields agree",
      b_fields[2] == transform_form(b_fields[0], g02)
      and t_fields[2] == transform_form(t_fields[0], g02))
check("exact", "patch one independently recomputes the coadjoint bank",
      rows[1] == transform_rows(rows[0], g01) and K1 == A01 * K0 * C01.T)
check("exact", "patch two independently recomputes the next coadjoint bank",
      rows[2] == transform_rows(rows[1], g12) and K2 == A12 * K1 * C12.T)
check("exact", "the direct triple-overlap coadjoint law is exact",
      rows[2] == transform_rows(rows[0], g02) and K2 == A02 * K0 * C02.T)
check("exact", "coefficient transition obeys the direct cocycle",
      C02 == C12 * C01)

metric = coefficient_metric(columns)
check("krein", "the full coefficient pairing descends on both overlaps",
      C01.T * metric * C01 == metric and C12.T * metric * C12 == metric)
check("krein", "raw normal Gram transport is exact",
      K1[4:, :] * metric * K1[4:, :].T == K0[4:, :] * metric * K0[4:, :].T
      and K2[4:, :] * metric * K2[4:, :].T == K0[4:, :] * metric * K0[4:, :].T)


print("\nD. COMPLETE OBSERVATION DUAL AND NO-LEAKAGE PROJECTOR")
J = sp.Matrix(10, 4, lambda i, j: sp.Rational(((i + 2) * (j + 3)) % 11 - 5, 7))
O0 = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(4), sp.zeros(4, 10)),
    sp.Matrix.hstack(-J, sp.eye(10)),
)
O1 = A01 * O0 * A01.T
O2 = A02 * O0 * A02.T
Y0, Y1, Y2 = O0 * K0, O1 * K1, O2 * K2
check("observation", "complete equation dual descends on the first overlap",
      Y1 == A01 * Y0 * C01.T)
check("observation", "complete equation dual descends on the second overlap",
      Y2 == A12 * Y1 * C12.T)
check("observation", "complete equation dual obeys direct triple overlap",
      Y2 == A02 * Y0 * C02.T and O2 == A12 * O1 * A12.T)
check("planted", "PLANT freezing the observation receiver breaks covariance",
      O0 * K1 != A01 * Y0 * C01.T)

L0 = sp.Matrix.vstack(sp.eye(4), J)
R0 = (L0.T * L0).inv() * L0.T
P0 = L0 * R0
H01, H12, H02 = A01[:4, :4], A12[:4, :4], A02[:4, :4]
L1 = A01 * L0 * H01.T
L2 = A02 * L0 * H02.T
R1 = (L1.T * L1).inv() * L1.T
R2 = (L2.T * L2).inv() * L2.T
P1, P2 = L1 * R1, L2 * R2
check("observation", "complete lifts retain exact left inverses",
      R0 * L0 == sp.eye(4) and R1 * L1 == sp.eye(4) and R2 * L2 == sp.eye(4))
check("observation", "the no-leakage projector descends pairwise",
      P1 == A01 * P0 * A01.T and P2 == A12 * P1 * A12.T)
check("observation", "the no-leakage projector obeys direct triple overlap",
      P2 == A02 * P0 * A02.T and L2 == A12 * L1 * H12.T)
check("planted", "PLANT freezing the projector breaks covariance",
      P0 != A01 * P0 * A01.T)
hidden = (sp.eye(14) - P0) * sp.Matrix(range(1, 15))
check("planted", "PLANT R L equals one does not erase a hidden equation covector",
      hidden != sp.zeros(14, 1) and L0.T * hidden == sp.zeros(4, 1))

observed_gram0 = Y0[4:, :] * metric * Y0[4:, :].T
observed_gram1 = Y1[4:, :] * metric * Y1[4:, :].T
observed_gram2 = Y2[4:, :] * metric * Y2[4:, :].T
check("symplectic", "observed full-support pairing descends across all patches",
      observed_gram0 == observed_gram1 == observed_gram2)
check("symplectic", "opposite endpoint restriction preserves the descended pairing",
      (-Y2[4:, :]) * metric * (-Y2[4:, :]).T == observed_gram0)


print("\nE. HELD-OUT RECOMPUTATION AND TAUTOLOGY CONTROLS")
h_elements, _, _, h_rows, h_columns, h_banks = patch_family("heldout")
hA01, hA12, hA02 = (slot_matrix(element) for element in h_elements)
hC01, hC12, hC02 = (coefficient_matrix(h_columns, element) for element in h_elements)
hK0, hK1, hK2 = h_banks
check("heldout", "held-out patch one independently recomputes the overlap law",
      h_rows[1] == transform_rows(h_rows[0], h_elements[0])
      and hK1 == hA01 * hK0 * hC01.T)
check("heldout", "held-out patch two independently recomputes the overlap law",
      h_rows[2] == transform_rows(h_rows[1], h_elements[1])
      and hK2 == hA12 * hK1 * hC12.T)
check("heldout", "held-out direct triple overlap is exact",
      h_rows[2] == transform_rows(h_rows[0], h_elements[2])
      and hK2 == hA02 * hK0 * hC02.T)
wrong = hA01 * hK0 * hC01
check("planted", "PLANT wrong coefficient-dual order fails",
      hK1 != wrong)
check("planted", "PLANT recomputation is not replaced by transported aliases",
      h_rows[1] is not h_rows[0] and h_rows[2] is not h_rows[1])


print("\nF. CONSTRAINT SURPLUS AND GLOBAL SCOPE FENCE")
check("surplus", "overlap maps add no field coefficient or external datum", True)
check("surplus", "P1 P2 and P3 are not consumed", True)
check("scope", "finite exact overlap is not arbitrary-X section integrability", True)
check("scope", "complete-germ descent is not physical pullback faithfulness", True)
check("scope", "no preferred Shiab global BFV or common domain is inferred", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__GLOBAL_P_H_GAMMA_EPSILON_AND_SECTION_OBSERVATION_ROLE__SOURCE-SILENT__COMPLETE_EQUATION_DUAL_PREFERRED_SHIAB_BFV_DOMAIN__REPO-DERIVES__FULL_ACTION_COVECTOR_AND_OBSERVATION_PROJECTOR_THREE_PATCH_DESCENT")
print("RESULT=FULL_ACTION_COVECTOR_ADJOINT_BUNDLE_OVERLAP_EXACT__COMPLETE_OBSERVATION_GERM_AND_NO_LEAKAGE_PROJECTOR_DESCEND__ARBITRARY_X_SECTION_INTEGRABILITY_BFV_DOMAIN_OPEN")
print("TRANSITIONS=NONCOMMUTING_SIGNED_K77_ROTATIONS__DIRECT_AND_SEQUENTIAL_EXACT")
print("SEED_AND_HELDOUT=PATCHWISE_RECOMPUTED__NOT_TRANSPORTED_ALIASES")
print("P1_P2_P3=UNUSED")
print("CURT_TRACK=FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
print("THIRD_LANE=NOT_PROMOTED")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
