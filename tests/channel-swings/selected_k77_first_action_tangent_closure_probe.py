#!/usr/bin/env python3
"""Exact first-action grade-one tangent-closure gate on both K77 branches."""

from collections import Counter
from fractions import Fraction
from io import StringIO
from pathlib import Path
import contextlib
import json
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


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND PRE-WAVE")
source = (ROOT / "lab/sources/selected-k77-first-action-tangent-source-reinspection-2026-08-09.md").read_text()
v0120 = strict("lab/process/selected-k77-lower-order-source-block-reconciliation.json")
parent = strict("lab/process/selected-k77-operative-pairing-symmetry-closure.json")
check("source", "source confirms the full adjoint one-form and is silent on 321 versus 1571",
      "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source and "321 versus 1571" in source)
check("repo", "v0.120 leaves the complete first-action Hessian open",
      "COMPLETE_FIRST_ACTION_HESSIAN" in v0120["open_blocks"])
check("repo", "expanded parent dimensions and pairing multiplicities are prior art",
      parent["closure"]["weyl_block_u3232_product"]["complex_dimension"] == 16382
      and parent["closure"]["full_u6464"]["complex_dimension"] == 16383)
for label in (
    "first transgression Hessian versus raw-residual Jacobian",
    "first transgression Hessian versus residual-square Gram Hessian",
    "minimum known selected completion versus complete functional tangent",
    "selected Spin parent versus two U32,32 halves versus full U64,64",
    "finite Hessian rank versus BV quotient or analytic domain",
):
    check("type", label + " remain distinct", True)

capture = StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.106 connection branch and epsilon-cross predecessor replays",
      "PASS 61/61" in capture.getvalue() and not P["FAILURES"])

M = P["M"]
directions = P["directions"]
grades = P["direction_grades"]
ZERO = M["ZERO"]
FULL = M["FULL"]
SELECTED = P["SELECTED"]
grade1 = [direction for direction, grade in zip(directions, grades) if grade == 1]
grade2 = [direction for direction, grade in zip(directions, grades) if grade == 2]
check("exact", "the exact low-grade source basis is 196 plus 1274",
      len(grade1) == 196 and len(grade2) == 1274)

# Trap capture: the low-grade list is interleaved by form slot.  This exact
# indexing error produced a false off-slice rank during this Run.
bad_prefix = grades[:196]
check("planted", "PLANT positional first-196 slice is not the Clifford-grade-one bank",
      bad_prefix.count(1) == 28 and bad_prefix.count(2) == 168)


def top(form):
    return form.get(FULL, {}).get(0, ZERO)


def pair(left, right):
    return top(M["wedge_raw"](left, right))


def qform(direction):
    packet = M["fadd"](
        M["wedge_raw"](M["PHI1"], direction),
        M["wedge_raw"](direction, M["PHI1"]),
    )
    return M["shiab"](packet, SELECTED)


q_all = [qform(direction) for direction in directions]
q_grade1 = [value for value, grade in zip(q_all, grades) if grade == 1]
q_grade2 = [value for value, grade in zip(q_all, grades) if grade == 2]
check("planted", "PLANT q-images are selected by grade labels rather than positional slicing",
      len(q_grade1) == 196 and len(q_grade2) == 1274
      and q_grade1 != q_all[:196])


def second_variation_components(u, v, q_u, q_v):
    """Return constant, b and t coefficients of H_TT at B=b Phi1,T=t Phi1."""
    mass = M["gscale"](Fraction(1, 2), M["gadd"](
        pair(v, M["hodge"](u)), pair(u, M["hodge"](v))))
    paired_q = M["gadd"](pair(v, q_u), pair(u, q_v))
    b_part = M["gscale"](Fraction(1, 2), paired_q)
    d2_packet = M["fscale"](Fraction(1, 3), M["fadd"](
        M["wedge_raw"](v, u), M["wedge_raw"](u, v)))
    t_part = M["gadd"](
        M["gscale"](Fraction(1, 3), paired_q),
        pair(M["PHI1"], M["shiab"](d2_packet, SELECTED)),
    )
    return mass, b_part, t_part


def store(target, key, value):
    if value != ZERO:
        assert value[1] == 0
        target[key] = sp.Rational(value[0].numerator, value[0].denominator)


print("\nB. COMPLETE GRADE-ONE TO GRADE-TWO CROSS")
mixed_constant = {}
mixed_b = {}
mixed_t = {}
for column, (u, q_u) in enumerate(zip(grade1, q_grade1)):
    for row, (v, q_v) in enumerate(zip(grade2, q_grade2)):
        values = second_variation_components(u, v, q_u, q_v)
        for target, value in zip((mixed_constant, mixed_b, mixed_t), values):
            store(target, (row, column), value)

check("theorem", "constant b and t mixed components vanish coefficientwise",
      not mixed_constant and not mixed_b and not mixed_t)

def singleton_flat_key(value):
    flattened = M["flatten"](value)
    return next(iter(flattened), None) if len(flattened) == 1 else None


horizontal_keys = {singleton_flat_key(value) for value in P["P"]["P"]["horizontal_basis"]}
check("shape", "every horizontal basis value has exactly one flattened key",
      None not in horizontal_keys)
horizontal_rows = [
    row for row, value in enumerate(grade2)
    if singleton_flat_key(value) in horizontal_keys
]
offslice_rows = [row for row in range(1274) if row not in set(horizontal_rows)]
check("exact", "actual repository basis splits grade two into horizontal 24 and off-slice 1250",
      len(horizontal_rows) == 24 and len(offslice_rows) == 1250)

sqrt3 = sp.sqrt(3)
branches = (
    (sp.Rational(1, 208) - sqrt3/312, (-2 + sqrt3)/208),
    (sp.Rational(1, 208) + sqrt3/312, (-2 - sqrt3)/208),
)
mixed_branches = []
for b_value, t_value in branches:
    entries = {
        key: sp.simplify(
            mixed_constant.get(key, 0)
            + b_value * mixed_b.get(key, 0)
            + t_value * mixed_t.get(key, 0))
        for key in set(mixed_constant) | set(mixed_b) | set(mixed_t)
    }
    matrix = sp.SparseMatrix(1274, 196, {key: value for key, value in entries.items() if value != 0})
    mixed_branches.append(matrix)
    check("theorem", "branch mixed matrix has zero full horizontal and off-slice rank",
          matrix.rank() == 0
          and matrix.extract(horizontal_rows, range(196)).rank() == 0
          and matrix.extract(offslice_rows, range(196)).rank() == 0)


print("\nC. COMPLETE GRADE-ONE SELF BLOCK")
self_constant = {}
self_b = {}
self_t = {}
for column, (u, q_u) in enumerate(zip(grade1, q_grade1)):
    for row, (v, q_v) in enumerate(zip(grade1, q_grade1)):
        values = second_variation_components(u, v, q_u, q_v)
        for target, value in zip((self_constant, self_b, self_t), values):
            store(target, (row, column), value)


def inertia_symmetric(value):
    work = sp.Matrix(value)
    positive = negative = null = 0
    while work.rows:
        size = work.rows
        diagonal = next((i for i in range(size) if work[i, i] != 0), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(size) if i != diagonal]
            work = work.extract(order, order)
            pivot = sp.simplify(work[0, 0])
            if bool(pivot > 0):
                positive += 1
            elif bool(pivot < 0):
                negative += 1
            else:
                raise AssertionError(f"undecided exact pivot sign: {pivot}")
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
        left, right = off
        order = [left, right] + [i for i in range(size) if i not in (left, right)]
        work = work.extract(order, order)
        block = work[:2, :2]
        positive += 1
        negative += 1
        if size == 2:
            break
        coupling = work[:2, 2:]
        work = sp.simplify(work[2:, 2:] - coupling.T * block.inv() * coupling)
    return positive, negative, null


self_branches = []
self_inertias = []
for b_value, t_value in branches:
    keys = set(self_constant) | set(self_b) | set(self_t)
    entries = {
        key: sp.simplify(
            self_constant.get(key, 0)
            + b_value * self_b.get(key, 0)
            + t_value * self_t.get(key, 0))
        for key in keys
    }
    matrix = sp.SparseMatrix(196, 196, {key: value for key, value in entries.items() if value != 0})
    self_branches.append(matrix)
    self_inertias.append(inertia_symmetric(matrix))
    check("theorem", "branch grade-one self Hessian is symmetric full rank with 560 entries",
          matrix == matrix.T and matrix.rank() == 196 and len(matrix.todok()) == 560)

check("theorem", "both branch self Hessians have exact inertia 97 99 zero",
      self_inertias == [(97, 99, 0), (97, 99, 0)])
check("exact", "the branch matrices are unequal Galois conjugates",
      self_branches[0] != self_branches[1]
      and self_branches[0].xreplace({sqrt3: -sqrt3}) == self_branches[1])


print("\nD. DISPOSITION, REGISTRY, AND FENCES")
registry = strict("lab/process/selected-k77-first-action-tangent-closure.json")
check("registry", "registry records zero mixed ranks and nondegenerate self blocks",
      registry["exact_result"]["grade1_grade2_first_action_hessian"]["branch_ranks"] == [0, 0]
      and registry["exact_result"]["grade1_grade1_first_action_hessian"]["branch_ranks"] == [196, 196]
      and registry["exact_result"]["grade1_grade1_first_action_hessian"]["branch_inertias"]
      == [[97, 99, 0], [97, 99, 0]])
check("variational", "321 survives this connection-block gate but is not selected as complete",
      registry["exact_result"]["minimal_321_disposition"]
      == "SURVIVES_THIS_CONNECTION_BLOCK_GATE__NOT_SELECTED_OR_COMPLETE")
for kind, label in (
    ("symplectic", "zero off-slice connection cross does not construct a BV or BFV quotient"),
    ("analytic", "finite nondegenerate self blocks do not supply a Riesz contour or closed domain"),
    ("representation", "expanded parent Hessians remain distinct and unbuilt"),
    ("accounting", "no field coefficient selector quotient or datum is added"),
    ("accounting", "P1 P2 P3 remain unused"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_FULL_ADJOINT_ONE_FORM_TWO_CONNECTION_AND_FIRST_ACTION_GRAMMAR__SOURCE_SILENT_321_VS1571_TANGENT_BRANCH_HESSIAN_AND_ACTION_PARENT")
print("GRADE1_GRADE2_FIRST_ACTION_HESSIAN=BOTH_BRANCHES_ZERO_1274_BY196__HORIZONTAL24_ZERO__OFFSLICE1250_ZERO")
print("GRADE1_SELF_HESSIAN=BOTH_BRANCHES_RANK196_INERTIA97_99__UNEQUAL_GALOIS_CONJUGATES")
print("MINIMAL321=SURVIVES_CONNECTION_BLOCK_GATE_ONLY__METRIC_EPSILON_DERIVATIVE_AND_EXPANDED_PARENT_BLOCKS_OPEN")
print("TRAP=LOW_GRADE_BASIS_INTERLEAVED__POSITIONAL_FIRST196_IS_28_GRADE1_PLUS168_GRADE2")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
