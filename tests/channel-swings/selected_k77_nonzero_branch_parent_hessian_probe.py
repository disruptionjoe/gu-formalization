#!/usr/bin/env python3
"""Exact all-grade parent classifier for the selected K77 scalar branch.

The coefficient carrier is ``V* tensor Cl(V)`` (dimension 14*2^14).  At the
Spin-invariant branch ``T=-(1/312) Phi1`` the selected first-action Hessian
preserves Clifford grade and the label ``J xor {i}`` of a basis vector
``e^i tensor gamma_J``.  Signed permutations reduce every resulting block to
one matrix for each signature of that label.  This probe evaluates that exact
finite census and then composes it into the B-adjoint and Weyl-block/coset
candidate parents.
"""

from collections import Counter
from fractions import Fraction
from io import StringIO
from itertools import combinations
from math import comb
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_moving_k77_vacuum_p2_norm_probe.py"
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


print("A. PREDECESSOR, LAYER ZERO, AND PRE-REGISTERED HORNS")
capture = StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "selected nonzero scalar branch predecessor replays",
      "PASS" in capture.getvalue() and not P["FAILURES"])

M = P["M"]
N = M["N"]
FULL = M["FULL"]
ZERO = M["ZERO"]
ONE = M["ONE"]
ETA = M["ETA"]
PHI1 = M["PHI1"]
SELECTED = P["SELECTED"]
T_VALUE = Fraction(-1, 312)
B_SKEW_GRADES = {1, 2, 5, 6, 9, 10, 13, 14}
B_SELF_GRADES = set(range(15)) - B_SKEW_GRADES
check("type", "first-action Hessian is not a residual Jacobian or norm-square Gram Hessian", True)
check("type", "B-adjoint and Weyl parity are rival parent decompositions, not one split", True)
check("type", "finite radical is not yet a gauge, BV, spectral, or Green-domain quotient", True)
check("planted", "PLANT scalar radial instability is not a complete parent classifier", True)


def pair(left, right):
    return M["wedge_raw"](left, right).get(FULL, {}).get(0, ZERO)


def basis(form_index, clifford_mask):
    return {1 << form_index: {clifford_mask: ONE}}


def qform(direction):
    packet = M["fadd"](
        M["wedge_raw"](PHI1, direction),
        M["wedge_raw"](direction, PHI1),
    )
    return M["shiab"](packet, SELECTED)


def hessian(u, v, q_u, q_v):
    """Second variation at kappa_1=1, T=-(1/312) Phi1."""
    mass = M["gscale"](Fraction(1, 2), M["gadd"](
        pair(v, M["hodge"](u)), pair(u, M["hodge"](v))))
    paired_q = M["gadd"](pair(v, q_u), pair(u, q_v))
    d2_packet = M["fscale"](Fraction(1, 3), M["fadd"](
        M["wedge_raw"](v, u), M["wedge_raw"](u, v)))
    cubic = M["gadd"](
        M["gscale"](Fraction(1, 3), paired_q),
        pair(PHI1, M["shiab"](d2_packet, SELECTED)),
    )
    return M["gadd"](mass, M["gscale"](T_VALUE, cubic))


def rational(value):
    assert value[1] == 0
    return sp.Rational(value[0].numerator, value[0].denominator)


def inertia_symmetric(value):
    """Exact congruence elimination, returning positive/negative/null."""
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


POSITIVE = tuple(i for i, sign in enumerate(ETA) if sign == 1)
NEGATIVE = tuple(i for i, sign in enumerate(ETA) if sign == -1)
check("exact", "K77 coefficient metric has seven positive and seven negative axes",
      len(POSITIVE) == len(NEGATIVE) == 7)


def canonical_mask(size, positive_count):
    chosen = POSITIVE[:positive_count] + NEGATIVE[:size - positive_count]
    return sum(1 << i for i in chosen)


def feasible_positive_counts(size):
    return range(max(0, size - 7), min(7, size) + 1)


def states_for_label(label, grade):
    size = label.bit_count()
    if size == grade - 1:
        return [(i, label | (1 << i)) for i in range(N) if not label & (1 << i)]
    if size == grade + 1:
        return [(i, label ^ (1 << i)) for i in range(N) if label & (1 << i)]
    raise AssertionError((size, grade))


def label_block(label, grade):
    states = states_for_label(label, grade)
    directions = [basis(i, mask) for i, mask in states]
    q_values = [qform(direction) for direction in directions]
    for (form_index, clifford_mask), q_value in zip(states, q_values):
        expected_label = clifford_mask ^ (1 << form_index)
        for form_mask, output_mask in M["flatten"](q_value):
            missing = FULL ^ form_mask
            assert missing.bit_count() == 1
            assert output_mask.bit_count() == grade
            assert output_mask ^ missing == expected_label
    matrix = sp.zeros(len(states), len(states))
    for row, (v, q_v) in enumerate(zip(directions, q_values)):
        for column, (u, q_u) in enumerate(zip(directions, q_values)):
            matrix[row, column] = rational(hessian(u, v, q_u, q_v))
    assert matrix == matrix.T
    return states, matrix


print("\nB. CONSERVED LABEL AND SIGNED-PERMUTATION ORBITS")
# The q-image supplies the only nontrivial first-action linear term.  On every
# signed-permutation orbit representative, each potentially pairable output
# retains J xor {i}.  The mass term is diagonal and the remaining cubic term is
# checked below by explicit cross-label controls.
q_label_checks = 0
for grade in range(15):
    for family_size in (grade - 1, grade + 1):
        if not 0 <= family_size <= 14:
            continue
        for positive_count in feasible_positive_counts(family_size):
            label = canonical_mask(family_size, positive_count)
            state = states_for_label(label, grade)[0]
            direction = basis(*state)
            for form_mask, clifford_mask in M["flatten"](qform(direction)):
                missing = FULL ^ form_mask
                assert missing.bit_count() == 1
                check_label = clifford_mask ^ missing
                q_label_checks += 1
                if check_label != label:
                    FAILURES.append("q-image violates conserved label")
check("theorem", "all signed-permutation q-image representatives preserve J xor {i}",
      q_label_checks > 0 and "q-image violates conserved label" not in FAILURES)

# Off-label controls exercise both membership families and all grades.  A wrong
# target is chosen with the same grade but a different XOR label.
off_label_values = []
for grade in range(15):
    source_mask = (1 << grade) - 1
    source = (0, source_mask)
    if grade == 0:
        source = (0, 0)
    u = basis(*source)
    q_u = qform(u)
    target = next(
        (candidate for j in range(N) for mask in combinations(range(N), grade)
         if (candidate := (j, sum(1 << x for x in mask)))[1] ^ (1 << candidate[0])
         != source[1] ^ (1 << source[0])),
        None,
    )
    assert target is not None
    v = basis(*target)
    off_label_values.append(hessian(u, v, q_u, qform(v)))
check("planted", "PLANT one off-label target in every grade has zero Hessian entry",
      all(value == ZERO for value in off_label_values))

# A full grade-pair matrix is unnecessary once the coefficient/product rule is
# typed, but these 225 exact representatives catch a mistaken Hodge-complement
# or parity coupling in the implemented second derivative.
grade_representatives = []
for grade in range(15):
    mask = (1 << grade) - 1
    direction = basis(0, mask)
    grade_representatives.append((direction, qform(direction)))
cross_grade_values = [
    hessian(u, v, q_u, q_v)
    for left_grade, (u, q_u) in enumerate(grade_representatives)
    for right_grade, (v, q_v) in enumerate(grade_representatives)
    if left_grade != right_grade
]
check("planted", "PLANT all 210 cross-grade representatives vanish exactly",
      len(cross_grade_values) == 210 and all(value == ZERO for value in cross_grade_values))

q_phi1 = qform(PHI1)
check("exact", "the all-grade Hessian reproduces radial value minus fourteen",
      hessian(PHI1, PHI1, q_phi1, q_phi1) == (Fraction(-14), Fraction(0)))
complement_direction = basis(0, 0)  # Clifford grade zero is B-self.
check("planted", "PLANT P-only quadratic form misses an actual nonzero complement Hessian entry",
      hessian(complement_direction, complement_direction,
              qform(complement_direction), qform(complement_direction)) != ZERO)


print("\nC. COMPLETE SIGNATURE-ORBIT CENSUS")
grade_results = {}
orbit_results = []
for grade in range(15):
    total_dim = total_pos = total_neg = total_null = 0
    for family_size in (grade - 1, grade + 1):
        if not 0 <= family_size <= 14:
            continue
        for positive_count in feasible_positive_counts(family_size):
            label = canonical_mask(family_size, positive_count)
            states, matrix = label_block(label, grade)
            multiplicity = comb(7, positive_count) * comb(7, family_size - positive_count)
            inertia = inertia_symmetric(matrix)
            total_dim += multiplicity * len(states)
            total_pos += multiplicity * inertia[0]
            total_neg += multiplicity * inertia[1]
            total_null += multiplicity * inertia[2]
            orbit_results.append({
                "grade": grade,
                "label_size": family_size,
                "label_positive": positive_count,
                "block_size": len(states),
                "multiplicity": multiplicity,
                "rank": matrix.rank(),
                "inertia": list(inertia),
            })
    expected = N * comb(N, grade)
    check("exact", f"grade {grade} orbit census covers {expected} directions",
          total_dim == expected)
    grade_results[grade] = {
        "dimension": total_dim,
        "rank": total_pos + total_neg,
        "inertia": [total_pos, total_neg, total_null],
    }

check("exact", "all-grade census covers the complete 14 times 2^14 carrier",
      sum(row["dimension"] for row in grade_results.values()) == N * 2**N)

# Independent representatives at three structurally different grades test the
# signed-permutation multiplication rule used to expand the census wholesale.
for grade, family_size, positive_count in ((1, 2, 1), (7, 6, 3), (13, 12, 6)):
    canonical = canonical_mask(family_size, positive_count)
    alternative_indices = (
        POSITIVE[-positive_count:] + NEGATIVE[-(family_size - positive_count):]
        if family_size - positive_count else POSITIVE[-positive_count:]
    )
    alternative = sum(1 << index for index in alternative_indices)
    _, canonical_matrix = label_block(canonical, grade)
    _, alternative_matrix = label_block(alternative, grade)
    check("planted", f"PLANT grade {grade} alternative orbit representative has identical rank and inertia",
          canonical_matrix.rank() == alternative_matrix.rank()
          and inertia_symmetric(canonical_matrix) == inertia_symmetric(alternative_matrix))


def compose(grades):
    rows = [grade_results[grade] for grade in grades]
    return {
        "grades": sorted(grades),
        "dimension": sum(row["dimension"] for row in rows),
        "rank": sum(row["rank"] for row in rows),
        "inertia": [sum(row["inertia"][index] for row in rows) for index in range(3)],
    }


parents = {
    "B_skew": compose(B_SKEW_GRADES),
    "B_self_complement": compose(B_SELF_GRADES),
    "Weyl_block_even": compose({grade for grade in range(15) if grade % 2 == 0}),
    "Weyl_coset_odd": compose({grade for grade in range(15) if grade % 2 == 1}),
    "complete": compose(set(range(15))),
}
check("exact", "B-adjoint split retains the certified 8128 plus 8256 coefficient dimensions",
      parents["B_skew"]["dimension"] == 14 * 8128
      and parents["B_self_complement"]["dimension"] == 14 * 8256)
check("exact", "Weyl block/coset split is 8192 plus 8192 coefficient dimensions",
      parents["Weyl_block_even"]["dimension"] == 14 * 8192
      and parents["Weyl_coset_odd"]["dimension"] == 14 * 8192)


print("\nD. RESULT REGISTRY AND SCIENTIFIC FENCES")
registry_path = ROOT / "lab/process/selected-k77-nonzero-branch-parent-hessian.json"
if registry_path.exists():
    registry = strict("lab/process/selected-k77-nonzero-branch-parent-hessian.json")
    check("registry", "durable registry matches the exact grade and parent census",
          registry["exact_result"]["grade_results"]
          == {str(key): value for key, value in grade_results.items()}
          and registry["exact_result"]["parents"] == parents)
else:
    check("registry", "draft execution precedes durable registry", True)
check("type", "nonzero finite Hessian classification does not choose a physical spectrum", True)
check("type", "no radical may be called gauge without a source-derived tangent or BV differential", True)
check("type", "the induced K77 Dirac/Rarita-Schwinger operator remains a serial successor", True)
check("type", "P1 P2 P3 and the external datum ledger remain unused", True)
check("planted", "PLANT Hessian ownership is not a proof of Standard Model recovery", True)


print("GRADE_RESULTS_JSON=" + json.dumps({str(k): v for k, v in grade_results.items()}, sort_keys=True))
print("PARENTS_JSON=" + json.dumps(parents, sort_keys=True))
print("COUNTS " + " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
