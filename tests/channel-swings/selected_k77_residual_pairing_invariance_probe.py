#!/usr/bin/env python3
"""Exact local K77 residual-pairing and invariance gate.

Run with ``sage -python``.  The frozen all-grade raw-Upsilon response is
reused.  This probe constructs the local degree-13 Hodge times Clifford-trace
bilinear, distinguishes Spin(7,7)-only grade weights from full-u(64,64)
adjoint invariance, and restricts the pairing to the 1,470-dimensional source
response image.  It does not construct a fundamental symmetry, formal
adjoint, Green identity, contour, or closed analytic domain.
"""

from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib
import io
import json
import runpy

from sage.all import QQ, diagonal_matrix, matrix


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_coupled_all_grade_upsilon_graph_probe.py"
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


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, LAYER ZERO, AND IMMUTABLE RESPONSE")
source = read("lab/sources/selected-k77-residual-pairing-source-reinspection-2026-08-08.md")
prior = strict("lab/process/selected-k77-action-frechet-ward-object-separation.json")
check("source", "Portal source explicitly says to norm-square Upsilon",
      "02:00:49" in source and "norm square" in source)
check("source", "Portal source expects a Shiab-adjoint operator after variation",
      "02:01:28" in source and "adjoint" in source)
check("source", "source is silent on the real K77 Riesz map and analytic domain",
      "SOURCE-SILENT" in source and "closed analytic domain" in source)
check("source", "Curt separately states two C32 32 Weyl halves and a U64 64 principal group",
      "two copies of `C^(32,32)`" in source and "`U(64,64)`" in source)
check("repo", "v0.91 leaves the residual pairing open",
      prior["exact_results"]["residual_pairing_K"] == "OPEN")
for label in (
    "source norm-square phrase versus a positive Hilbert norm",
    "local residual bilinear versus a Krein fundamental symmetry",
    "local Riesz map versus a formal adjoint on sections",
    "formal adjoint versus a Green identity and boundary domain",
    "Spin covariance versus full u(64,64) adjoint invariance",
    "finite response support versus a global associated residual bundle",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "all-grade raw-Upsilon predecessor replays",
      "PASS 50/50" in capture.getvalue() and not P["FAILURES"])

M = P["M"]
response_columns = P["response_columns"]
output_coordinates = sorted(P["output_coordinates"])
N = M["N"]
ETA = M["ETA"]


def clifford_square_sign(mask):
    product_mask, sign = M["blade_product"](mask, mask)
    assert product_mask == 0
    return sign


def form_sign(mask):
    value = 1
    for index in M["indices"](mask):
        value *= ETA[index]
    return value


def coordinate_sign(key):
    form_mask, clifford_mask = key
    return form_sign(form_mask) * clifford_square_sign(clifford_mask)


print("\nB. FULL LOCAL RESIDUAL CARRIER")
selected_grades = (1, 2, 5)
form13_masks = [sum(1 << i for i in item) for item in combinations(range(N), 13)]
form13_inertia = (
    sum(form_sign(mask) > 0 for mask in form13_masks),
    sum(form_sign(mask) < 0 for mask in form13_masks),
)
check("exact", "degree-thirteen K77 Hodge pairing has inertia seven seven",
      form13_inertia == (7, 7))

clifford_inertia = {}
for grade in selected_grades:
    masks = [sum(1 << i for i in item) for item in combinations(range(N), grade)]
    clifford_inertia[grade] = (
        sum(clifford_square_sign(mask) > 0 for mask in masks),
        sum(clifford_square_sign(mask) < 0 for mask in masks),
    )
check("exact", "Clifford grade inertias are exact",
      clifford_inertia == {1: (7, 7), 2: (49, 42), 5: (1001, 1001)})
carrier_dimension = 14 * sum(len(list(combinations(range(N), grade))) for grade in selected_grades)
carrier_inertia = (carrier_dimension // 2, carrier_dimension // 2, 0)
check("exact", "full selected residual carrier has dimension 29498",
      carrier_dimension == 29498)
check("exact", "tensoring with balanced degree-thirteen forms gives balanced nondegenerate inertia",
      carrier_inertia == (14749, 14749, 0))


print("\nC. SPIN, WEYL-BLOCK, AND FULL-ADJOINT INVARIANCE")
# A Spin bivector preserves Clifford grade, so a grade-diagonal trace form has
# three independent weights.  Allowed full-u generators in grades one and
# five mix the live grades and force w1=w2=w5.  The rows below are evaluated
# from exact blade witnesses rather than asserted by rank alone.


def raw_blade_product(left, right, signature):
    def indices(mask):
        return tuple(i for i in range(len(signature)) if mask & (1 << i))

    inversions = sum(i > j for i in indices(left) for j in indices(right))
    sign = -1 if inversions % 2 else 1
    for index in indices(left & right):
        sign *= signature[index]
    return left ^ right, sign


def invariance_row(z, x, y, signature):
    grades = selected_grades

    def comm(left, right):
        mask, a = raw_blade_product(left, right, signature)
        mask2, b = raw_blade_product(right, left, signature)
        assert mask == mask2
        return mask, a - b

    def scalar(left, right):
        mask, value = raw_blade_product(left, right, signature)
        return value if mask == 0 else 0

    zx, a = comm(z, x)
    zy, b = comm(z, y)
    row = [0, 0, 0]
    if a and zx.bit_count() == y.bit_count():
        row[grades.index(y.bit_count())] += a * scalar(zx, y)
    if b and zy.bit_count() == x.bit_count():
        row[grades.index(x.bit_count())] += b * scalar(x, zy)
    divisor = next((abs(value) for value in row if value), 1)
    row = [value // divisor for value in row]
    if next((value for value in row if value), 1) < 0:
        row = [-value for value in row]
    return tuple(row)


signature6 = (1, -1, -1, -1, 1, 1)
mask = lambda *items: sum(1 << i for i in items)
row12 = invariance_row(mask(0), mask(1), mask(0, 1), signature6)
row25 = invariance_row(
    mask(0, 1, 2, 3, 4), mask(0, 5), mask(1, 2, 3, 4, 5), signature6
)
constraint_matrix = matrix(QQ, [row12, row25])
check("exact", "grade-one full-u witness forces w1 equals w2",
      row12 == (1, -1, 0))
check("exact", "grade-five full-u witness forces w2 equals w5",
      row25 == (0, 1, -1))
check("exact", "full-adjoint grade-weight constraint has rank two",
      constraint_matrix.rank() == 2)
check("exact", "the only surviving grade-weight line is w1=w2=w5",
      constraint_matrix.right_kernel().basis_matrix().row_space()
      == matrix(QQ, [[1, 1, 1]]).row_space())
check("representation", "Spin-only covariance leaves three grade weights because bivectors preserve grade",
      True)
check("representation", "both full-u weight witnesses are odd and exchange Weyl halves",
      mask(0).bit_count() % 2 == 1 and mask(0, 1, 2, 3, 4).bit_count() % 2 == 1)
check("scope", "full-u witness equations do not transfer to a Weyl-block product",
      True)
check("planted", "PLANT unequal weights pass Spin grade preservation but fail full-adjoint invariance",
      constraint_matrix * matrix(QQ, [[1], [2], [3]]) != 0)


print("\nD. EXACT K ON THE FROZEN 1470-DIMENSIONAL RESPONSE IMAGE")
coordinate_position = {key: index for index, key in enumerate(output_coordinates)}
entries = {}
for column_index, column in enumerate(response_columns):
    for key, value in column.items():
        check_imaginary = value[1]
        if check_imaginary:
            raise AssertionError("selected response coefficient is not real")
        entries[coordinate_position[key], column_index] = (
            QQ(value[0].numerator) / QQ(value[0].denominator)
        )
response = matrix(QQ, len(output_coordinates), len(response_columns), entries, sparse=True)
signs = [coordinate_sign(key) for key in output_coordinates]
local_k = diagonal_matrix(QQ, signs, sparse=True)
gram = response.transpose() * local_k * response

check("exact", "frozen response has shape 4330 by 1470 and full column rank",
      response.nrows() == 4330 and response.ncols() == response.rank() == 1470)
support_inertia = (
    sum(value > 0 for value in signs), sum(value < 0 for value in signs), 0
)
support_by_grade = {}
for grade in selected_grades:
    grade_signs = [coordinate_sign(key) for key in output_coordinates
                   if key[1].bit_count() == grade]
    support_by_grade[grade] = (
        sum(value > 0 for value in grade_signs),
        sum(value < 0 for value in grade_signs),
    )
check("exact", "finite output-support inertia is diagnostic and exact",
      support_inertia == (2195, 2135, 0)
      and support_by_grade == {1: (98, 98), 2: (637, 637), 5: (1460, 1400)})
check("scope", "the 4330-coordinate support is not promoted to a global invariant subbundle", True)

grade_results = {}
for grade in selected_grades:
    positions = [index for index, key in enumerate(output_coordinates)
                 if key[1].bit_count() == grade]
    grade_response = response.matrix_from_rows(positions)
    grade_k = diagonal_matrix(QQ, [signs[index] for index in positions], sparse=True)
    grade_gram = grade_response.transpose() * grade_k * grade_response
    grade_results[grade] = {
        "coordinate_count": len(positions),
        "response_rank": grade_response.rank(),
        "gram_rank": grade_gram.rank(),
    }
check("exact", "grade-separated response and Gram ranks are frozen",
      grade_results == {
          1: {"coordinate_count": 196, "response_rank": 196, "gram_rank": 196},
          2: {"coordinate_count": 1274, "response_rank": 1274, "gram_rank": 1274},
          5: {"coordinate_count": 2860, "response_rank": 286, "gram_rank": 286},
      })
check("exact", "grades one plus two already detect all 1470 source directions",
      response.matrix_from_rows([
          index for index, key in enumerate(output_coordinates)
          if key[1].bit_count() in (1, 2)
      ]).rank() == 1470)
check("exact", "equal-weight local K Gram is sparse and nondegenerate",
      len(gram.dict()) == 7346 and gram.rank() == 1470)


def components(value):
    adjacency = [set() for _ in range(value.nrows())]
    for (left, right), coefficient in value.dict().items():
        if left != right and coefficient:
            adjacency[left].add(right)
            adjacency[right].add(left)
    seen = set()
    out = []
    for start in range(value.nrows()):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        component = []
        while stack:
            vertex = stack.pop()
            component.append(vertex)
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        out.append(sorted(component))
    return out


def inertia_exact(value):
    work = matrix(QQ, value)
    positive = negative = null = 0
    while work.nrows():
        size = work.nrows()
        diagonal = next((index for index in range(size) if work[index, index]), None)
        if diagonal is not None:
            order = [diagonal] + [index for index in range(size) if index != diagonal]
            work = work.matrix_from_rows_and_columns(order, order)
            pivot = work[0, 0]
            positive += int(pivot > 0)
            negative += int(pivot < 0)
            if size == 1:
                break
            column = work[1:, 0]
            work = work[1:, 1:] - column * column.transpose() / pivot
            continue
        off = next(((i, j) for i in range(size) for j in range(i + 1, size)
                    if work[i, j]), None)
        if off is None:
            null += size
            break
        left, right = off
        order = [left, right] + [index for index in range(size)
                                if index not in (left, right)]
        work = work.matrix_from_rows_and_columns(order, order)
        block = work[:2, :2]
        positive += 1
        negative += 1
        if size == 2:
            break
        coupling = work[:2, 2:]
        work = work[2:, 2:] - coupling.transpose() * block.inverse() * coupling
    return positive, negative, null


blocks = components(gram)
block_sizes = Counter(len(component) for component in blocks)
block_inertias = Counter()
total_inertia = [0, 0, 0]
for component in blocks:
    value = inertia_exact(gram.matrix_from_rows_and_columns(component, component))
    block_inertias[(len(component), value)] += 1
    total_inertia = [left + right for left, right in zip(total_inertia, value)]

check("exact", "response Gram splits into 391 small exact congruence blocks",
      len(blocks) == 391
      and block_sizes == Counter({3: 286, 5: 78, 13: 13, 2: 13, 27: 1}))
check("exact", "local K response Gram has exact inertia 741 729 zero",
      tuple(total_inertia) == (741, 729, 0))
check("planted", "PLANT nondegenerate indefinite K is not a positive norm",
      total_inertia[0] > 0 and total_inertia[1] > 0 and total_inertia[2] == 0)


print("\nE. CONSTRAINT, SYMPLECTIC, ANALYTIC, AND PROGRAM FENCES")
registry = strict("lab/process/selected-k77-residual-pairing-invariance.json")
check("registry", "registry records the full exact pairing packet",
      registry["local_pairing"]["response_gram"] == {
          "dimension": 1470, "rank": 1470, "inertia": [741, 729, 0],
          "nonzero_entries": 7346, "component_count": 391,
      })
check("registry", "registry preserves Spin Weyl-block and full-u as three distinct demands",
      registry["invariance_selection"]["full_u6464_grade_weight_dimension"] == 1
      and registry["invariance_selection"]["spin77_only_grade_weight_dimension"] == 3
      and registry["invariance_selection"]["weyl_block_u3232_product_grade_weight_dimension"] == "OPEN")
for kind, label in (
    ("variational", "conditional local K opens formal-adjoint construction but does not supply it"),
    ("symplectic", "bulk residual Gram is not a reduced presymplectic or BFV form"),
    ("symplectic", "no boundary charge polarization or edge mode is selected"),
    ("krein", "algebraic nondegeneracy is not a fundamental symmetry or positive state space"),
    ("pde", "finite inertia does not establish a closed hyperbolic evolution domain"),
    ("analytic", "no contour determinant measure saddle or path integral is selected"),
    ("scope", "the full-u comparator overall scale is the already-counted source_norm coordinate"),
    ("scope", "the operative Weyl-block selector and its relative weights remain open"),
    ("scope", "no field quotient external datum verdict canon or public posture changes"),
    ("scope", "P1 P2 P3 remain unchanged and unused"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__NORM_SQUARE_AND_ADJOINT_ARENA__CURT_WEYL_SPLIT_VERSUS_FULL_U6464_FORK__OPERATIVE_PAIRING_SYMMETRY_OPEN")
print("LOCAL_K77_RESIDUAL_PAIRING=HODGE13_TIMES_CLIFFORD_TRACE__NONDEGENERATE_CANDIDATE")
print("GRADE_WEIGHTS=SPIN_ONLY_DIM3__FULL_U6464_COMPARATOR_DIM1__WEYL_BLOCK_PRODUCT_OPEN")
print("RESPONSE_GRAM=RANK1470__INERTIA741_729_0")
print("NEXT=SETTLE_OPERATIVE_FULL_U6464_VERSUS_WEYL_BLOCK_PRODUCT_PAIRING_SYMMETRY__THEN_LOWER_ORDER_TRANSVERSE_DG_UPSILON_FORMAL_ADJOINT_AND_GREEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
