#!/usr/bin/env python3
"""Exact full-u(64,64)-comparator selected-action coefficient bank.

The v0.76 bank tested only Cl1+Cl2 coefficient directions.  This probe uses
symbolic Clifford adjoints to evaluate the same selected action on all 16,384
real directions of the K77 u(64,64) comparator.  It keeps the pointwise fibre
calculation distinct from global associated-bundle, physical observation,
preferred-Shiab, BFV and analytic-domain claims.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import contextlib
import io
import math
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
K77 = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
V076 = ROOT / "tests/channel-swings/selected_k77_action_boundary_coefficient_bank_probe.py"
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def text(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def inertia_symmetric(matrix):
    work = sp.Matrix(matrix)
    positive = negative = null = 0
    while work.rows:
        size = work.rows
        diagonal = next((i for i in range(size) if work[i, i] != 0), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(size) if i != diagonal]
            work = work.extract(order, order)
            pivot = sp.simplify(work[0, 0])
            positive += int(bool(pivot > 0))
            negative += int(bool(pivot < 0))
            if size == 1:
                break
            column = work[1:, 0]
            work = sp.simplify(work[1:, 1:] - column * column.T / pivot)
            continue
        off = next(((i, j) for i in range(size) for j in range(i + 1, size)
                    if work[i, j] != 0), None)
        if off is None:
            null += size
            break
        i, j = off
        order = [i, j] + [k for k in range(size) if k not in (i, j)]
        work = work.extract(order, order)
        block = work[:2, :2]
        positive += 1
        negative += 1
        if size == 2:
            break
        coupling = work[:2, 2:]
        work = sp.simplify(work[2:, 2:] - coupling.T * block.inv() * coupling)
    return positive, negative, null


print("A. SOURCE, REAL FORM, AND LAYER ZERO")
source = text("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
algebra_report = text("explorations/resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation-2026-08-04.md")
v076_report = text("explorations/conditional-build/selected-k77-action-boundary-coefficient-bank-2026-08-08.md")
check("source", "the source uses a U(64,64)-type complex presentation",
      "U(64,64)" in source and "REAL-FORM-FORK" in source)
check("source", "the source fixes commutator and i-symmetric algebra products",
      "commutator" in algebra_report and "i`-symmetric" in algebra_report)
check("repo", "the exact K77 algebra is Cl(7,7)=M128(R)",
      "Cl}(7,7)\\cong M_{128}(\\mathbb R)" in algebra_report)
check("repo", "the prior exact audit types the full real u(64,64) comparator",
      "8128=dim so(64,64)" in algebra_report and "16384=dim_R u(64,64)" in algebra_report)
check("repo", "v0.76 explicitly leaves the full coefficient extension open",
      "not the full `U(64,64)`" in v076_report)
for label in (
    "real u(64,64) comparator versus complex matrix algebra",
    "K77 u(64,64) comparator versus K95 right-H Sp(32,32;H) fork",
    "pointwise coefficient fibre versus global associated bundle",
    "full coefficient support versus coefficient-bank rank",
    "complete equation observation fixture versus physical observation section",
    "scalar-Clifford coefficient pairing versus analytic Krein domain",
):
    check("type", label + " remain distinct", True)


print("\nB. PINNED K77 ALGEBRA AND FULL REAL BASIS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(K77))
check("repo", "the exact K77 evaluator replays",
      "TOTAL=50" in capture.getvalue() and "FAILURES=0" in capture.getvalue()
      and not M["FAILURES"])

N = M["N"]
FULL = M["FULL"]
ZERO = M["ZERO"]
ONE = M["ONE"]
I = M["I"]
ETA = M["ETA"]
blade = M["blade"]
blade_product = M["blade_product"]
indices = M["indices"]
gadd = M["gadd"]
gmul = M["gmul"]
gscale = M["gscale"]
fadd = M["fadd"]
fscale = M["fscale"]
wedge_raw = M["wedge_raw"]
shiab = M["shiab"]
hodge = M["hodge"]
wedge_sign = M["wedge_sign"]
PHI1 = M["PHI1"]
PHI2 = M["PHI2"]
SELECTED = ("comm", "symi", "symi")
SKEW_GRADES = {1, 2, 5, 6, 9, 10, 13, 14}
SELF_GRADES = set(range(15)) - SKEW_GRADES

skew_dimension = sum(math.comb(N, grade) for grade in SKEW_GRADES)
self_dimension = sum(math.comb(N, grade) for grade in SELF_GRADES)
check("realform", "real B-skew grades have dimension 8128", skew_dimension == 8128)
check("realform", "i times B-self grades have dimension 8256", self_dimension == 8256)
check("realform", "the real u(64,64) comparator has dimension 16384",
      skew_dimension + self_dimension == 2 ** N == 16384)
check("realform", "low and high vector/two-form copies are both included",
      all(grade in SKEW_GRADES for grade in (1, 2, 13, 14)))


# A linear coefficient expression is a sparse sum c * L * d * R.  Moving all
# fixed factors around the scalar Clifford trace produces the exact functional
# covector without evaluating 229,376 directions one at a time.
def lclean(value):
    return {key: coefficient for key, coefficient in value.items() if coefficient != ZERO}


def ladd(*values):
    out = {}
    for value in values:
        for key, coefficient in value.items():
            out[key] = gadd(out.get(key, ZERO), coefficient)
    return lclean(out)


def lscale(scalar, value):
    factor = scalar if isinstance(scalar, tuple) else (Fraction(scalar), Fraction(0))
    return lclean({key: gmul(factor, coefficient) for key, coefficient in value.items()})


def left_fixed(fixed, linear):
    out = {}
    for fixed_mask, fixed_coefficient in fixed.items():
        for (left, right), coefficient in linear.items():
            new_left, sign = blade_product(fixed_mask, left)
            key = (new_left, right)
            out[key] = gadd(out.get(key, ZERO),
                            gscale(sign, gmul(fixed_coefficient, coefficient)))
    return lclean(out)


def right_fixed(linear, fixed):
    out = {}
    for (left, right), coefficient in linear.items():
        for fixed_mask, fixed_coefficient in fixed.items():
            new_right, sign = blade_product(right, fixed_mask)
            key = (left, new_right)
            out[key] = gadd(out.get(key, ZERO),
                            gscale(sign, gmul(coefficient, fixed_coefficient)))
    return lclean(out)


def coefficient_fixed_linear(fixed, linear, channel=None):
    fixed_linear = left_fixed(fixed, linear)
    linear_fixed = right_fixed(linear, fixed)
    if channel is None:
        return fixed_linear
    if channel == "comm":
        return ladd(fixed_linear, lscale(-1, linear_fixed))
    if channel == "symi":
        return lscale(I, ladd(fixed_linear, linear_fixed))
    raise ValueError(channel)


def coefficient_linear_fixed(linear, fixed):
    return right_fixed(linear, fixed)


def lfclean(form):
    return {mask: lclean(value) for mask, value in form.items() if lclean(value)}


def lfadd(*forms):
    out = {}
    for form in forms:
        for mask, value in form.items():
            out[mask] = ladd(out.get(mask, {}), value)
    return lfclean(out)


def lfscale(scalar, form):
    return lfclean({mask: lscale(scalar, value) for mask, value in form.items()})


def wedge_linear_fixed(linear, fixed):
    out = {}
    for linear_mask, linear_value in linear.items():
        for fixed_mask, fixed_value in fixed.items():
            sign = wedge_sign(linear_mask, fixed_mask)
            if sign:
                mask = linear_mask | fixed_mask
                out[mask] = ladd(out.get(mask, {}),
                                  lscale(sign, coefficient_linear_fixed(linear_value, fixed_value)))
    return lfclean(out)


def wedge_fixed_linear(fixed, linear, channel=None):
    out = {}
    for fixed_mask, fixed_value in fixed.items():
        for linear_mask, linear_value in linear.items():
            sign = wedge_sign(fixed_mask, linear_mask)
            if sign:
                mask = fixed_mask | linear_mask
                out[mask] = ladd(out.get(mask, {}), lscale(
                    sign, coefficient_fixed_linear(fixed_value, linear_value, channel)))
    return lfclean(out)


def hodge_linear(linear):
    out = {}
    for mask, value in linear.items():
        complement = FULL ^ mask
        norm = math.prod(ETA[index] for index in indices(mask))
        out[complement] = ladd(out.get(complement, {}),
                               lscale(wedge_sign(mask, complement) * norm, value))
    return lfclean(out)


def shiab_linear(curvature):
    star = hodge_linear(curvature)
    first = wedge_fixed_linear(PHI1, star, "comm")
    middle = hodge_linear(wedge_fixed_linear(PHI2, star, "symi"))
    second = hodge_linear(wedge_fixed_linear(PHI1, middle, "symi"))
    return lfadd(first, lfscale(Fraction(-1, 2), second))


def pair_fixed_linear(fixed, linear):
    return wedge_fixed_linear(fixed, linear).get(FULL, {})


def pair_linear_fixed(linear, fixed):
    return wedge_linear_fixed(linear, fixed).get(FULL, {})


def make_fixture(kind):
    b_field = {}
    t_field = {}
    for i in range(N):
        if kind == "seed":
            b_pair = tuple(sorted(((i + 1) % N, (i + 2) % N)))
            t_index = (2 * i + 2) % N
            b_scale, t_scale = i % 3 + 1, i % 5 + 1
        else:
            b_pair = tuple(sorted(((2 * i + 1) % N, (2 * i + 4) % N)))
            t_index = (3 * i + 1) % N
            b_scale, t_scale = i % 4 + 1, i % 6 + 1
        b_field[1 << i] = blade(b_pair, (Fraction(b_scale), Fraction(0)))
        t_field[1 << i] = blade(t_index, (Fraction(t_scale), Fraction(0)))
    return b_field, t_field


def fixed_packet(b_field, t_field):
    return fadd(
        wedge_raw(b_field, b_field),
        fscale(Fraction(1, 2), fadd(
            wedge_raw(b_field, t_field), wedge_raw(t_field, b_field))),
        fscale(Fraction(1, 3), wedge_raw(t_field, t_field)),
    )


def symbolic_row(slot, b_field, t_field, selected_packet):
    d_field = {1 << slot: {(0, 0): ONE}}
    d_packet_b = lfadd(
        wedge_linear_fixed(d_field, b_field),
        wedge_fixed_linear(b_field, d_field),
        lfscale(Fraction(1, 2), lfadd(
            wedge_linear_fixed(d_field, t_field),
            wedge_fixed_linear(t_field, d_field))),
    )
    e_b = pair_fixed_linear(t_field, shiab_linear(d_packet_b))
    d_packet_t = lfadd(
        lfscale(Fraction(1, 2), lfadd(
            wedge_fixed_linear(b_field, d_field),
            wedge_linear_fixed(d_field, b_field))),
        lfscale(Fraction(1, 3), lfadd(
            wedge_linear_fixed(d_field, t_field),
            wedge_fixed_linear(t_field, d_field))),
    )
    mass = ladd(pair_linear_fixed(d_field, hodge(t_field)),
                 pair_fixed_linear(t_field, hodge_linear(d_field)))
    e_t = ladd(
        pair_linear_fixed(d_field, selected_packet),
        pair_fixed_linear(t_field, shiab_linear(d_packet_t)),
        lscale(Fraction(1, 2), mass),
    )
    expression = ladd(e_b, lscale(-1, e_t))

    # Sc(L d R)=Sc(R L d). Evaluate the resulting covector on the exact real
    # u(64,64) basis: real B-skew blades and i times B-self blades.
    adjoint = {}
    for (left, right), coefficient in expression.items():
        mask, sign = blade_product(right, left)
        adjoint[mask] = gadd(adjoint.get(mask, ZERO), gscale(sign, coefficient))
    row = {}
    for mask, coefficient in adjoint.items():
        factor = ONE if len(indices(mask)) in SKEW_GRADES else I
        _, square = blade_product(mask, mask)
        value = gscale(square, gmul(coefficient, factor))
        if value != ZERO:
            row[mask] = value
    return row


def full_bank(kind):
    b_field, t_field = make_fixture(kind)
    selected_packet = shiab(fixed_packet(b_field, t_field), SELECTED)
    rows = [symbolic_row(slot, b_field, t_field, selected_packet) for slot in range(N)]
    columns = sorted(set().union(*(set(row) for row in rows)))
    real = sp.Matrix([
        [Q(row.get(mask, ZERO)[0].numerator, row.get(mask, ZERO)[0].denominator)
         for mask in columns]
        for row in rows
    ])
    imaginary = sp.Matrix([
        [Q(row.get(mask, ZERO)[1].numerator, row.get(mask, ZERO)[1].denominator)
         for mask in columns]
        for row in rows
    ])
    return b_field, t_field, rows, columns, real, imaginary


print("\nC. FULL 16,384-DIRECTION ACTION BANK")
B, T, rows, columns, bank, imaginary = full_bank("seed")
grade_counts = {grade: sum(len(indices(mask)) == grade for mask in columns) for grade in range(15)}
row_supports = tuple(len(row) for row in rows)
check("exact", "the symbolic adjoint evaluates all 16,384 real coefficient directions", 2 ** N == 16384)
check("realform", "the selected action covector is real on the full real-form basis",
      imaginary == sp.zeros(14, len(columns)))
check("exact", "the full pointwise bank has rank fourteen", bank.rank() == 14)
check("exact", "the ten full normal rows remain independent", bank[4:, :].rank() == 10)
check("exact", "the seed union has 549 nonzero coefficient coordinates", len(columns) == 549)
check("exact", "only grades 1 2 and 5 are live on the seed fixture",
      {grade for grade, count in grade_counts.items() if count} == {1, 2, 5})
check("exact", "the seed grade-union fingerprint is 14 59 476",
      (grade_counts[1], grade_counts[2], grade_counts[5]) == (14, 59, 476))
check("exact", "the full row-support fingerprint is frozen",
      row_supports == (42, 60, 46, 64, 47, 62, 46, 66, 47, 66, 47, 62, 53, 58))

for grade, expected_columns, expected_entries in ((1, 14, 68), (2, 59, 98), (5, 476, 600)):
    positions = [index for index, mask in enumerate(columns) if len(indices(mask)) == grade]
    grade_bank = bank[:, positions]
    check("grade", f"grade {grade} has the expected union size",
          len(positions) == expected_columns)
    check("grade", f"grade {grade} separately has full/normal rank 14/10",
          grade_bank.rank() == 14 and grade_bank[4:, :].rank() == 10)
    check("grade", f"grade {grade} has the expected nonzero-entry count",
          sum(value != 0 for value in grade_bank) == expected_entries)


print("\nD. DIRECT CONTROLS AND HELD-OUT BACKGROUND")
with contextlib.redirect_stdout(io.StringIO()):
    prior = runpy.run_path(str(V076))
check("repo", "v0.76 replays", not prior["FAILURES"])
low_compare = all(
    rows[slot].get(mask, ZERO) == prior["bank"][slot][index]
    for slot in range(N)
    for index, mask in enumerate(prior["coefficient_masks"])
)
check("exact", "every Cl1+Cl2 entry agrees with v0.76", low_compare)

for slot, chosen in ((4, columns[100]), (8, columns[300]), (13, columns[-1])):
    direct = prior["e_difference"](prior["direction"](
        slot, {chosen: ONE if len(indices(chosen)) in SKEW_GRADES else I}))
    check("exact", f"held-out direct Clifford evaluation agrees at slot {slot}",
          direct == rows[slot].get(chosen, ZERO))

inactive_masks = (
    sum(1 << i for i in (0, 1, 2)),
    sum(1 << i for i in (0, 1, 2, 3)),
    sum(1 << i for i in (0, 1, 2, 3, 4, 5)),
)
for slot, mask in zip((5, 9, 12), inactive_masks):
    factor = ONE if len(indices(mask)) in SKEW_GRADES else I
    direct = prior["e_difference"](prior["direction"](slot, {mask: factor}))
    check("exact", f"held-out inactive grade {len(indices(mask))} evaluates to zero",
          direct == ZERO and mask not in rows[slot])

_, _, heldout_rows, heldout_columns, heldout_bank, heldout_imaginary = full_bank("heldout")
heldout_grades = {len(indices(mask)) for mask in heldout_columns}
check("heldout", "a second background remains real and rank fourteen/ten",
      heldout_imaginary == sp.zeros(14, len(heldout_columns))
      and heldout_bank.rank() == 14 and heldout_bank[4:, :].rank() == 10)
check("heldout", "the second background again has only grades 1 2 and 5 live",
      heldout_grades == {1, 2, 5})
check("heldout", "the second background has a distinct 628-coordinate union",
      len(heldout_columns) == 628 and set(heldout_columns) != set(columns))
check("planted", "PLANT low-grade rank alone misses live grade-five support",
      grade_counts[5] == 476 and bank[:, [i for i, m in enumerate(columns)
                                        if len(indices(m)) in (1, 2)]].rank() == 14)


print("\nE. FULL PAIRING, OBSERVATION, AND ENDPOINT TRANSPORT")
metric = sp.diag(*[
    (1 if len(indices(mask)) in SKEW_GRADES else -1) * blade_product(mask, mask)[1]
    for mask in columns
])
normal = bank[4:, :]
raw_gram = normal * metric * normal.T
J = sp.Matrix(10, 4, lambda i, j: Q(((i + 2) * (j + 3)) % 11 - 5, 7))
observation = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(4), sp.zeros(4, 10)),
    sp.Matrix.hstack(-J, sp.eye(10)),
)
observation_inverse = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(4), sp.zeros(4, 10)),
    sp.Matrix.hstack(J, sp.eye(10)),
)
observed = observation * bank
observed_normal = observed[4:, :]
observed_gram = observed_normal * metric * observed_normal.T
check("krein", "the full raw normal image is nondegenerate with inertia (4,6,0)",
      raw_gram.rank() == 10 and inertia_symmetric(raw_gram) == (4, 6, 0))
check("krein", "the full observed normal image is nondegenerate with inertia (4,6,0)",
      observed_gram.rank() == 10 and inertia_symmetric(observed_gram) == (4, 6, 0))
check("krein", "the exact full raw Gram determinant is frozen",
      raw_gram.det() == Q(720675574777908926000373533816344723456, 129140163))
check("krein", "the exact full observed Gram determinant is frozen",
      observed_gram.det() == Q(675990534521630134428443975864366882756479230976,
                               20100618201669201))
check("observation", "complete observation remains exactly invertible",
      observation_inverse * observation == sp.eye(14)
      and observation_inverse * observed == bank)
check("observation", "complete observation preserves full/normal rank 14/10",
      observed.rank() == 14 and observed_normal.rank() == 10)
check("symplectic", "opposite endpoint restrictions preserve full rank and pairing",
      (-observed_normal).rank() == observed_normal.rank() == 10
      and (-observed_normal) * metric * (-observed_normal).T == observed_gram)
check("planted", "PLANT the low-grade observed inertia is not full-support stable",
      prior["inertia_symmetric"](prior["observed_gram"]) == (5, 5, 0)
      and inertia_symmetric(observed_gram) == (4, 6, 0))


print("\nF. CONSTRAINT AND GLOBAL SCOPE FENCE")
check("surplus", "the grade-five coefficients are action-derived not free parameters", True)
check("surplus", "no field coefficient selector or external datum is added", True)
check("scope", "a pointwise full comparator is not a global adjoint-bundle section", True)
check("scope", "the observation graph is not the physical global section", True)
check("scope", "no preferred Shiab BFV common-domain or vacuum result is inferred", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__U64_64_TYPE_COMPLEX_PRESENTATION_AND_ACTION_PRODUCTS__SOURCE-SILENT__PREFERRED_SHIAB_GLOBAL_BUNDLE_BFV_DOMAIN__REPO-DERIVES__FULL_REAL_U64_64_POINTWISE_ACTION_BANK")
print("RESULT=FULL_U6464_POINTWISE_ACTION_BANK_EXACT__LIVE_GRADES_1_2_5__GRADE5_CORRECTS_LOW_GRADE_SUPPORT_AND_OBSERVED_INERTIA")
print("FULL_REAL_DIMENSION=16384")
print("SEED_UNION=549__GRADE1_14__GRADE2_59__GRADE5_476")
print("HELDOUT_UNION=628__LIVE_GRADES_1_2_5")
print("FULL_RANK=14__NORMAL_RANK=10")
print("RAW_AND_OBSERVED_FULL_INERTIA=4,6,0")
print("BOUNDARY=GLOBAL_ADJOINT_BUNDLE__PHYSICAL_OBSERVATION__PREFERRED_SHIAB__TAU_A0_BFV_COMMON_DOMAIN_OPEN")
print("P1_P2_P3=UNUSED")
print("CURT_TRACK=FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
print("THIRD_LANE=NOT_PROMOTED")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
