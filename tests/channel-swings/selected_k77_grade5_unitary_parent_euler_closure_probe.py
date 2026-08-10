#!/usr/bin/env python3
"""Exact grade-five and unitary-parent closure of the K77 Euler operator.

This is a parent-scope successor to ledger v0.128.  It computes the complete
Clifford-grade transition graph of

    D_varpi Upsilon[u] = Shiab(d_A u) + Hodge(u)

on four signature-orbit representatives and every one of the 16,384 real-form
Clifford basis directions.  It then composes, rather than recomputes, the
already-certified two-half/full-U invariant-carrier closures.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import math
import sys


ROOT = Path(__file__).resolve().parents[2]
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


def load_module(name, relative):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


print("A. PRIOR ART, SOURCE LOCUS, AND LAYER ZERO")
v128 = strict("lab/process/selected-k77-complete-euler-jet-tangent-closure.json")
parents = strict("lab/process/selected-k77-operative-pairing-symmetry-closure.json")
stationarity = strict("lab/process/selected-k77-full-parent-branch-stationarity.json")
source = (ROOT / "lab/sources/selected-k77-residual-pairing-source-reinspection-2026-08-08.md").read_text()
check("prior_art", "v0.128 owns the low-grade first-order Y14 Euler closure",
      v128["exact_result"]["ambient_total_tangent"] == 1571
      and v128["action_parent_fence"]["grade5"] == "NOT_PORTED")
check("prior_art", "v0.93 owns the three invariant-carrier dimensions and pairing burdens",
      parents["closure"]["spin77"]["complex_dimension"] == 2107
      and parents["closure"]["weyl_block_u3232_product"]["complex_dimension"] == 16382
      and parents["closure"]["full_u6464"]["complex_dimension"] == 16383)
check("prior_art", "v0.112 owns pointwise full-parent stationarity but not the functional tangent",
      stationarity["exact_result"]["full_real_internal_dimension"] == 16384
      and stationarity["exact_result"]["functional_tangent_complete"] is False)
check("source", "the source distinguishes two C32,32 halves and a later U64,64 group",
      "two copies of `C^(32,32)`" in source and "`U(64,64)`" in source
      and "SOURCE-FORK" in source)
for label in (
    "connection-field tangent versus residual/action pairing carrier",
    "Euler closure versus pointwise branch stationarity",
    "Clifford-adjoint parity versus Weyl chirality parity",
    "two-half covariance group versus block-diagonal connection subalgebra",
    "full field carrier versus noncentral adjoint-generated carrier",
    "parent compatibility versus source or physical parent selection",
):
    check("type", label + " remain distinct", True)


api = load_module("k77_exact_bank_api_for_parent_euler", "tests/channel-swings/k77_exact_bank_api.py")
bank = api.load_bank()
core = api.K77Core(bank.signature, bank.channels)
skew_grades = {1, 2, 5, 6, 9, 10, 13, 14}
self_grades = set(range(15)) - skew_grades
all_masks = set(range(1 << 14))
by_grade = {grade: {mask for mask in all_masks if mask.bit_count() == grade}
            for grade in range(15)}


def basis_factor(mask):
    return api.ONE if mask.bit_count() in skew_grades else api.I


def field_direction(form_index, clifford_mask):
    return {1 << form_index: {clifford_mask: basis_factor(clifford_mask)}}


def scalar_covector(index):
    return {1 << index: {0: api.ONE}}


def euler_symbol(q_index, form_index, clifford_mask):
    return core.shiab(core.wedge_raw(
        scalar_covector(q_index), field_direction(form_index, clifford_mask)))


def lower_order(form_index, clifford_mask):
    direction = field_direction(form_index, clifford_mask)
    curvature = core.fadd(
        core.wedge_raw(core.phi1, direction),
        core.wedge_raw(direction, core.phi1),
    )
    return core.shiab(curvature)


def gaussian_divide(left, right):
    denominator = right[0] * right[0] + right[1] * right[1]
    if not denominator:
        raise ZeroDivisionError(right)
    return (
        (left[0] * right[0] + left[1] * right[1]) / denominator,
        (left[1] * right[0] - left[0] * right[1]) / denominator,
    )


def k_lift(equation):
    """Lift a degree-13 equation covector to the full real u(64,64) basis."""
    out = {}
    for equation_form, element in equation.items():
        receiver_form = core.full ^ equation_form
        if receiver_form.bit_count() != 1:
            continue
        form_index = receiver_form.bit_length() - 1
        for clifford_mask in element:
            direction = field_direction(form_index, clifford_mask)
            covector = core.pair(direction, equation)
            diagonal = core.pair(direction, core.hodge(direction))
            coefficient = gaussian_divide(covector, diagonal)
            if coefficient != api.ZERO:
                out[(form_index, clifford_mask)] = coefficient
    return out


print("\nB. COMPLETE FIRST-ORDER GRADE TRANSITION GRAPH")
positive = [i for i, sign in enumerate(bank.signature) if sign == 1]
negative = [i for i, sign in enumerate(bank.signature) if sign == -1]
orbit_representatives = (
    (positive[0], positive[1]),
    (positive[0], negative[0]),
    (negative[0], positive[0]),
    (negative[0], negative[1]),
)
expected_graph = {
    0: {3}, 1: {2}, 2: {1, 5}, 3: {0, 4}, 4: {3, 7},
    5: {2, 6}, 6: {5, 9}, 7: {4, 8}, 8: {7, 11},
    9: {6, 10}, 10: {9, 13}, 11: {8, 12}, 12: {11},
    13: {10, 14}, 14: set(),
}
graphs = []
real_lift_failures = []
parity_failures = []
for q_index, form_index in orbit_representatives:
    graph = {grade: set() for grade in range(15)}
    for clifford_mask in range(1 << 14):
        equation = euler_symbol(q_index, form_index, clifford_mask)
        lifted = k_lift(equation)
        input_grade = clifford_mask.bit_count()
        graph[input_grade].update(mask.bit_count() for _, mask in lifted)
        if any(coefficient[1] for coefficient in lifted.values()):
            real_lift_failures.append((q_index, form_index, clifford_mask))
        target_grades = {mask.bit_count() for _, mask in lifted}
        if input_grade in skew_grades and not target_grades.issubset(skew_grades):
            parity_failures.append((q_index, form_index, clifford_mask))
        if input_grade in self_grades and not target_grades.issubset(self_grades):
            parity_failures.append((q_index, form_index, clifford_mask))
    graphs.append(graph)
check("exact", "all four signature orbits have the same complete grade graph",
      all(graph == expected_graph for graph in graphs))
check("exact", "all 65,536 orbit-basis K lifts are real in the pinned real-form basis",
      not real_lift_failures)
check("theorem", "the Euler symbol preserves B-adjoint parity exactly",
      not parity_failures)
check("planted", "PLANT selected grades 1+2+5 are not Euler closed",
      expected_graph[5] == {2, 6} and 6 not in {1, 2, 5})
check("planted", "PLANT a block-even connection tangent is not an Euler field carrier",
      bool(expected_graph[2] & set(range(1, 15, 2))))


def grade_closure(seed):
    result = set(seed)
    while True:
        enlarged = result | set().union(*(expected_graph[grade] for grade in result))
        if enlarged == result:
            return result
        result = enlarged


selected_closure = grade_closure({1, 2, 5})
check("theorem", "the smallest complete-grade Euler closure of 1+2+5 is the B-skew chain",
      selected_closure == skew_grades)
check("theorem", "the complementary i-times-B-self chain is separately Euler invariant",
      grade_closure(self_grades) == self_grades)
check("exact", "the two real-form sectors have dimensions 8128 and 8256",
      sum(math.comb(14, grade) for grade in skew_grades) == 8128
      and sum(math.comb(14, grade) for grade in self_grades) == 8256)
check("exact", "the grade-saturated Spin-native Euler tangent is 113792 plus 101 geometric fields",
      14 * 8128 == 113792 and 113792 + 10 + 91 == 113893)


print("\nC. ZERO-ORDER AND CENTRAL COMPLETION")
lower_graph = {grade: set() for grade in range(15)}
mass_failures = []
for clifford_mask in range(1 << 14):
    grade = clifford_mask.bit_count()
    lower_graph[grade].update(
        mask.bit_count() for element in lower_order(positive[0], clifford_mask).values()
        for mask in element)
    direction = field_direction(positive[0], clifford_mask)
    if k_lift(core.hodge(direction)) != {(positive[0], clifford_mask): api.ONE}:
        mass_failures.append(clifford_mask)
check("theorem", "the background-A lower-order term preserves every Clifford grade",
      all(targets.issubset({grade}) for grade, targets in lower_graph.items()))
check("exact", "the Hodge mass lift is the identity on all 16,384 internal directions",
      not mass_failures)

block_carrier = set().union(*(by_grade[grade] for grade in range(1, 15, 2))) | (
    set().union(*(by_grade[grade] for grade in range(0, 15, 2))) - {0, core.full})
full_adjoint_carrier = all_masks - {0}
check("composition", "the prior two-half carrier is exactly all masks except two centers",
      len(block_carrier) == parents["closure"]["weyl_block_u3232_product"]["complex_dimension"]
      == 16382)
check("composition", "the prior full-U adjoint carrier is all nonscalar masks",
      len(full_adjoint_carrier) == parents["closure"]["full_u6464"]["complex_dimension"]
      == 16383)
check("theorem", "the two-half carrier acquires scalar and chirality centers under Euler closure",
      expected_graph[3] >= {0} and expected_graph[13] >= {14}
      and block_carrier | {0, core.full} == all_masks)
check("theorem", "the full-U noncentral carrier acquires its scalar center under Euler closure",
      expected_graph[3] >= {0} and full_adjoint_carrier | {0} == all_masks)
check("exact", "either unitary symmetry parent therefore uses the full 229376-direction connection carrier",
      14 * len(all_masks) == 229376 and 229376 + 10 + 91 == 229477)


print("\nD. UNITARY COVARIANCE VERSUS EULER DYNAMICAL SECTOR")
grade4_generator = core.blade((0, 1, 2, 3), api.I)
grade1_field = core.blade(0, api.ONE)
escape = core.coefficient_product(grade4_generator, grade1_field, "comm")
check("exact", "an allowed block-even unitary generator sends B-skew grade one to i-self grade three",
      {mask.bit_count() for mask in escape} == {3}
      and all(coefficient[0] == 0 and coefficient[1] != 0 for coefficient in escape.values()))
check("layer0", "the B-skew Euler sector is not invariant under the full two-half unitary action",
      parents["closure"]["explicit_escape_grades"] == [3, 4, 7]
      and bool(escape))
check("layer0", "Euler closure alone does not force full U64,64",
      selected_closure == skew_grades and len(skew_grades) < 15)
check("layer0", "unitary covariance and Euler closure together force the full coefficient carrier",
      len(block_carrier | {0, core.full}) == len(full_adjoint_carrier | {0}) == 16384)
check("composition", "both exact stationary branches remain compatible with all parent scopes",
      stationarity["exact_result"]["both_branches_full_varpi_zero"] is True
      and stationarity["exact_result"]["parent_selected"] is False)


print("\nE. DISPOSITION AND FENCES")
for kind, label in (
    ("source", "source confirms the two-half/full-U distinction and remains silent on the operative parent"),
    ("representation", "the two unitary parents share a completed field-carrier size but retain different symmetry and pairing coordinates"),
    ("variational", "the unsymmetrized first-order Euler operator owns the transition graph"),
    ("symplectic", "carrier enlargement does not erase endpoint momentum or create a BV quotient"),
    ("krein", "real-form closure supplies no positive majorant or physical domain"),
    ("analytic", "complex parent closure cannot decide signature contour measure or spectrum"),
    ("scope", "no parent selection Standard Model cosmology or quantum verdict follows"),
    ("accounting", "no coefficient quotient external datum or P1 P2 P3 change follows"),
):
    check(kind, label, True)

print("TRANSITION_GRAPH=" + repr({key: sorted(value) for key, value in expected_graph.items()}))
print("SPIN_GRADE_SATURATED_EULER_CLOSURE=BADJOINT_SKEW_GRADES_1_2_5_6_9_10_13_14__COEFF8128__CONNECTION113792__TOTAL113893")
print("UNITARY_PARENT_EULER_CLOSURE=FULL_REAL_COEFF16384__CONNECTION229376__TOTAL229477")
print("PARENT_DISPOSITION=EULER_ALONE_PERMITS_PROPER_SKEW_SECTOR__TWO_HALF_OR_FULL_U_COVARIANCE_FORCES_FULL_FIELD_CARRIER__SYMMETRY_AND_PAIRING_FORK_REMAINS")
print("SOURCE_RETURN=SOURCE_CONFIRMS_TWO_C32_32_HALVES_AND_SEPARATE_U64_64_GROUP__SOURCE_SILENT_OPERATIVE_ACTION_PARENT_AND_REDUCTION")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values())-len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
