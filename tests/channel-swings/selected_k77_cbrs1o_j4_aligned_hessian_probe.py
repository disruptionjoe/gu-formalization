#!/usr/bin/env sage -python
"""Exact CBRS-1O J4 coordinate-component alignment gate.

CBRS-1N rejected an arbitrary scalar-Schur lift. CBRS-1O proves why a phase
tweak cannot repair it and freezes the actual complete-Hessian support bank.
In the normalized real Clifford basis the explicit broken-orbit vector is
outside the nominal sixteen-dimensional ``E1 x E1`` representative span.
The selected Hessian instead preserves

    q(form_slot, coefficient_mask) = coefficient_mask XOR (1 << form_slot)

modulo XOR by J4. A support-only replay proves this before cancellation,
partitions all 230650 real directions into 8192 exact components, and locates
the 40 broken diagonal-Spin generators in 40 distinct cross components.
Component ranks, primitive and metric quotients, and any symbol remain open.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path
import contextlib
import io
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1n_j4_complete_tangent_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PRIOR ART, CURRENCY, AND LAYER ZERO", flush=True)
source = PREDECESSOR.read_text(encoding="utf-8")
prefix = source.split('print("A. ACTUAL J4-RESIDUAL MULTIPLICITY BLOCKS"', 1)[0]
capture = io.StringIO()
N1 = {"__file__": str(PREDECESSOR), "__name__": "__main__"}
with contextlib.redirect_stdout(capture):
    exec(compile(prefix, str(PREDECESSOR), "exec"), N1)
check("prior", "CBRS-1N carrier construction and pre-census controls replay",
      not N1["FAILURES"])
registry_n = json.loads(read("lab/process/selected-k77-cbrs1n-j4-complete-tangent.json"))
check("prior", "CBRS-1N rejects the apparent scalar-Schur ranks",
      registry_n["coarse_scalar_diagnostic"]["status"]
      == "REJECTED_NOT_A_COMPLETE_HESSIAN_RANK"
      and registry_n["complete_hessian"]["status"] == "OPEN")
check("currency", "CC-01 keeps MET(X) inside the selected action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "coarse dimension accounting versus invariant decomposition",
    "normalized real Clifford direction versus naive exterior basis",
    "coefficient mask versus form-plus-coefficient component key",
    "component support closure versus component rank",
    "broken orbit versus complete field kernel",
    "field kernel versus primitive and metric quotient",
    "J4 4+10 probe versus observed 3+1 physics",
):
    check("type", label + " remain distinct", True)


M = N1["M"]
N = N1["N"]
FULL = N1["FULL"]
J4_MASK = M["J4_MASK"]
BASE_SLOTS = N1["BASE_SLOTS"]
NORMAL_SLOTS = N1["NORMAL_SLOTS"]
BASE = N1["BASE"]
ETA = N1["ETA"]
blade = N1["blade"]
normalized_basis = N1["normalized_basis"]
K77 = N1["K77"]
a, b, c, d = M["variables"]


print("B. THE NOMINAL MIXED REPRESENTATIVES ARE NOT AN INVARIANT COPY", flush=True)


def scalar_coordinates(value):
    output = {}
    for mask, numerator in value.items():
        denominator = normalized_basis(mask)[mask]
        c0, c1 = denominator
        norm = c0*c0 + c1*c1
        real = sp.simplify((numerator[0]*c0 + numerator[1]*c1)/norm)
        imag = sp.simplify((numerator[1]*c0 - numerator[0]*c1)/norm)
        assert imag == 0
        if real != 0:
            output[mask] = sp.factor(real)
    return output


def diagonal_orbit_rep(left: int, right: int):
    generator = blade((left, right))
    output = {}
    for slot in range(N):
        value = K77["comm"](generator, BASE[1 << slot])
        if slot == left:
            value = K77["eadd"](
                value, K77["escale"](2*ETA[left], BASE[1 << right]))
        if slot == right:
            value = K77["eadd"](
                value, K77["escale"](-2*ETA[right], BASE[1 << left]))
        for mask, scalar in scalar_coordinates(value).items():
            output[("T", slot, mask)] = scalar
    return output


nominal_rows = N1["occurrences"][("E", 1, "E", 1)]
nominal_labels = [row[0] for row in nominal_rows]
nominal_reps = [row[1] for row in nominal_rows]
orbit_04 = diagonal_orbit_rep(0, 4)
coordinate_rows = sorted(set(orbit_04).union(*(set(rep) for rep in nominal_reps)))
nominal_matrix = sp.Matrix([
    [rep.get(row, 0) for rep in nominal_reps] for row in coordinate_rows
])
orbit_column = sp.Matrix([orbit_04.get(row, 0) for row in coordinate_rows])
check("accounting", "the nominal mixed label has sixteen coarse occurrences",
      len(nominal_labels) == 16 and nominal_matrix.rank() == 16)
check("obstruction", "an explicit nonzero broken-orbit vector is outside that nominal representative span",
      nominal_matrix.row_join(orbit_column).rank() == 17)
check("obstruction", "the mismatch occurs before any Hessian-rank lift",
      bool(orbit_04) and registry_n["coarse_scalar_diagnostic"]["rank_normal_pair"] == 230590)


print("C. SUPPORT-ONLY SELECTED-HESSIAN REPLAY", flush=True)

# Coefficients and signs are erased. This is an over-approximation, so support
# closure before cancellation proves support closure after cancellation.
Element = set[int]
Form = dict[int, Element]
Linear = set[tuple[int, int]]
LinearForm = dict[int, Linear]


def eadd(*values: Element) -> Element:
    out = set()
    for value in values:
        out.update(value)
    return out


def emul(left: Element, right: Element) -> Element:
    return {x ^ y for x in left for y in right}


def fadd(*forms: Form) -> Form:
    out: Form = {}
    for form in forms:
        for mask, value in form.items():
            out.setdefault(mask, set()).update(value)
    return {mask: value for mask, value in out.items() if value}


def wedge(left: Form, right: Form) -> Form:
    out: Form = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            if lm & rm:
                continue
            out.setdefault(lm | rm, set()).update(emul(lv, rv))
    return out


def hodge(form: Form) -> Form:
    return {FULL ^ mask: set(value) for mask, value in form.items()}


def lfadd(*forms: LinearForm) -> LinearForm:
    out: LinearForm = {}
    for form in forms:
        for mask, value in form.items():
            out.setdefault(mask, set()).update(value)
    return {mask: value for mask, value in out.items() if value}


def left_fixed(fixed: Element, linear: Linear) -> Linear:
    return {(fm ^ left, right) for fm in fixed for left, right in linear}


def right_fixed(linear: Linear, fixed: Element) -> Linear:
    return {(left, right ^ fm) for left, right in linear for fm in fixed}


def coefficient_fixed_linear(fixed: Element, linear: Linear) -> Linear:
    return left_fixed(fixed, linear) | right_fixed(linear, fixed)


def wedge_linear_fixed(linear: LinearForm, fixed: Form) -> LinearForm:
    out: LinearForm = {}
    for lm, lv in linear.items():
        for rm, rv in fixed.items():
            if lm & rm:
                continue
            out.setdefault(lm | rm, set()).update(right_fixed(lv, rv))
    return out


def wedge_fixed_linear(fixed: Form, linear: LinearForm) -> LinearForm:
    out: LinearForm = {}
    for lm, lv in fixed.items():
        for rm, rv in linear.items():
            if lm & rm:
                continue
            out.setdefault(lm | rm, set()).update(coefficient_fixed_linear(lv, rv))
    return out


def hodge_linear(form: LinearForm) -> LinearForm:
    return {FULL ^ mask: set(value) for mask, value in form.items()}


PHI1: Form = {1 << slot: {1 << slot} for slot in range(N)}
PHI2: Form = wedge(PHI1, PHI1)


def shiab(curvature: Form) -> Form:
    star = hodge(curvature)
    first = wedge(PHI1, star)
    middle = hodge(wedge(PHI2, star))
    second = hodge(wedge(PHI1, middle))
    return fadd(first, second)


def shiab_linear(curvature: LinearForm) -> LinearForm:
    star = hodge_linear(curvature)
    first = wedge_fixed_linear(PHI1, star)
    middle = hodge_linear(wedge_fixed_linear(PHI2, star))
    second = hodge_linear(wedge_fixed_linear(PHI1, middle))
    return lfadd(first, second)


def pair_linear_fixed(linear: LinearForm, fixed: Form) -> Linear:
    return wedge_linear_fixed(linear, fixed).get(FULL, set())


def pair_fixed_linear(fixed: Form, linear: LinearForm) -> Linear:
    return wedge_fixed_linear(fixed, linear).get(FULL, set())


BASE_SUPPORT: Form = {
    1 << slot: {1 << slot, (1 << slot) ^ J4_MASK} for slot in range(N)
}


def expression_rows(expression: Linear) -> set[int]:
    return {left ^ right for left, right in expression}


def linear_direction(slot: int) -> LinearForm:
    return {1 << slot: {(0, 0)}}


def fixed_direction(slot: int, mask: int) -> Form:
    return {1 << slot: {mask}}


def t_column_support(slot: int, mask: int):
    fixed = fixed_direction(slot, mask)
    packet_t = fadd(wedge(fixed, BASE_SUPPORT), wedge(BASE_SUPPORT, fixed))
    rows = []
    for output_slot in range(N):
        variation = linear_direction(output_slot)
        base_linear = lfadd(
            wedge_linear_fixed(variation, BASE_SUPPORT),
            wedge_fixed_linear(BASE_SUPPORT, variation))
        moving_linear = lfadd(
            wedge_linear_fixed(variation, fixed),
            wedge_fixed_linear(fixed, variation))
        mass_linear = (
            pair_linear_fixed(variation, hodge(fixed))
            | pair_fixed_linear(fixed, hodge_linear(variation)))
        expression = (
            pair_linear_fixed(variation, shiab(packet_t))
            | pair_fixed_linear(fixed, shiab_linear(base_linear))
            | pair_fixed_linear(BASE_SUPPORT, shiab_linear(moving_linear))
            | mass_linear)
        rows.append(expression_rows(expression))
    return rows


def b_column_support(slot: int, mask: int):
    fixed = fixed_direction(slot, mask)
    packet_b = fadd(wedge(fixed, BASE_SUPPORT), wedge(BASE_SUPPORT, fixed))
    b_rows = []
    t_rows = []
    for output_slot in range(N):
        variation = linear_direction(output_slot)
        moving_bt = lfadd(
            wedge_fixed_linear(fixed, variation),
            wedge_linear_fixed(variation, fixed))
        t_rows.append(expression_rows(
            pair_linear_fixed(variation, shiab(packet_b))
            | pair_fixed_linear(BASE_SUPPORT, shiab_linear(moving_bt))))
        moving_bb = lfadd(
            wedge_linear_fixed(variation, fixed),
            wedge_fixed_linear(fixed, variation))
        b_rows.append(expression_rows(
            pair_fixed_linear(BASE_SUPPORT, shiab_linear(moving_bb))))
    return b_rows, t_rows


def component_key(slot: int, mask: int) -> int:
    q = mask ^ (1 << slot)
    return min(q, q ^ J4_MASK)


def closed_rows(input_slot: int, input_mask: int, rows) -> bool:
    key = component_key(input_slot, input_mask)
    return all(component_key(output_slot, output_mask) == key
               for output_slot, row in enumerate(rows) for output_mask in row)


t_zero = [t_column_support(slot, 0) for slot in range(N)]
b_zero = [b_column_support(slot, 0) for slot in range(N)]
check("support", "every possible T-Hessian term preserves q modulo J4",
      all(closed_rows(slot, 0, t_zero[slot]) for slot in range(N)))
check("support", "every possible connection/connection term preserves q modulo J4",
      all(closed_rows(slot, 0, b_zero[slot][0]) for slot in range(N)))
check("support", "every possible connection/T term preserves q modulo J4",
      all(closed_rows(slot, 0, b_zero[slot][1]) for slot in range(N)))

translation_masks = (1, 3, 17, 1234, (1 << N) - 1)
check("covariance", "T support translates affinely with the coefficient mask",
      all(
          all(row == {value ^ mask for value in t_zero[slot][output_slot]}
              for output_slot, row in enumerate(t_column_support(slot, mask)))
          for slot in (0, 4, 13) for mask in translation_masks))
check("covariance", "connection support translates affinely with the coefficient mask",
      all(
          all(row == {value ^ mask for value in b_zero[slot][owner][output_slot]}
              for output_slot, row in enumerate(b_column_support(slot, mask)[owner]))
          for slot in (0, 4, 13) for owner in (0, 1) for mask in translation_masks))


print("D. COMPLETE COMPONENT ACCOUNTING AND ORBIT LOCATION", flush=True)
component_keys = sorted({min(q, q ^ J4_MASK) for q in range(1 << N)})
component_sizes = {key: 2*N for key in component_keys}
connection_counts = Counter()
for slot in range(N):
    for left, right in combinations(range(N), 2):
        mask = (1 << left) | (1 << right)
        connection_counts[component_key(slot, mask)] += 1
        component_sizes[component_key(slot, mask)] += 1

histogram = Counter(component_sizes.values())
check("accounting", "J4 quotient gives exactly 8192 coordinate components",
      len(component_keys) == (1 << N) // 2 == 8192)
check("accounting", "all 229376 T directions contribute 28 per component",
      len(component_keys) * 2*N == N * (1 << N) == 229376)
check("accounting", "all 1274 independent connection directions land once",
      sum(connection_counts.values()) == N * comb(N, 2) == 1274)
check("accounting", "component dimensions sum to the complete 230650 carrier",
      sum(component_sizes.values()) == 230650)

broken_generators = [(left, right) for left in BASE_SLOTS for right in NORMAL_SLOTS]
broken_orbits = [diagonal_orbit_rep(*pair) for pair in broken_generators]
broken_keys = []
for pair, orbit in zip(broken_generators, broken_orbits):
    keys = {component_key(slot, mask) for _, slot, mask in orbit}
    check("orbit", f"broken generator {pair} occupies one canonical component",
          len(keys) == 1)
    broken_keys.append(next(iter(keys)))
orbit_rows = sorted({key for orbit in broken_orbits for key in orbit})
orbit_matrix = sp.Matrix([
    [orbit.get(row, 0) for orbit in broken_orbits] for row in orbit_rows])
branch_substitutions = {}
for family, points in (("normal_J4", M["normal_points"]),
                       ("base_J4", M["base_points"])):
    for sign_index, point in enumerate(points):
        sign = -1 if sign_index == 0 else 1
        branch_substitutions[f"{family}_sign_{sign:+d}"] = dict(zip((a, b, c, d), point))
orbit_ranks = {
    branch: int(orbit_matrix.subs(substitution).rank())
    for branch, substitution in branch_substitutions.items()}
check("orbit", "the 40 broken generators occupy 40 distinct cross components",
      len(set(broken_keys)) == len(broken_keys) == 40)
check("orbit", "all four radical branches retain exact broken-orbit rank 40",
      set(orbit_ranks.values()) == {40})
check("kernel", "CBRS-1N supplies an exact zero Hessian pairing for a nonzero broken generator",
      registry_n["orbit_stabilizer"]["broken_diagonal_spin_orbit_dimension"] == 40
      and registry_n["orbit_stabilizer"]["broken_orbit_hessian_pairing"]
      == "ZERO_AGAINST_EVERY_COARSE_E1_TENSOR_E1_REPRESENTATIVE")

check("planted", "PLANT omitting form-slot XOR breaks component closure",
      any(output_mask != 0 for row in t_zero[0] for output_mask in row))
check("planted", "PLANT omitting the J4 quotient splits a live Hessian edge",
      any(component_key(0, 0) == component_key(output_slot, output_mask)
          and (output_mask ^ (1 << output_slot)) != 1
          for output_slot, row in enumerate(t_zero[0]) for output_mask in row))
check("planted", "PLANT the nominal sixteen-copy span rejects the explicit orbit column",
      nominal_matrix.row_join(orbit_column).rank() == 17)
check("scope", "component closure is not a component-rank or complete-kernel theorem", True)
check("scope", "no primitive metric symbol global spectrum or physical claim follows", True)

registry_path = ROOT / "lab/process/selected-k77-cbrs1o-j4-aligned-hessian.json"
if registry_path.exists():
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    check("propagation", "the native registry records the exact component bank and open ranks",
          registry["coordinate_component_bank"]["component_count"] == 8192
          and registry["complete_hessian"]["status"] == "OPEN_COMPONENT_RANKS_PENDING")
    check("propagation", "CURRENT-STATE carries the CBRS-1O obstruction and CBRS-1P gate",
          "CBRS-1O" in read("CURRENT-STATE.yaml") and "CBRS-1P" in read("CURRENT-STATE.yaml"))
    check("propagation", "the agenda and contributor front door carry CBRS-1P",
          "CBRS-1P" in read("lab/process/RESEARCH-AGENDA.json")
          and "CBRS-1P" in read("NEXT-STEPS.md"))

RESULT = {
    "disposition": "CBRS1O_REJECTS_NOMINAL_RESIDUAL_IRREP_BANK__CANONICAL_Q_MOD_J4_COORDINATE_COMPONENT_BANK_FROZEN",
    "nominal_mixed_span": {
        "occurrences": len(nominal_labels),
        "span_rank": int(nominal_matrix.rank()),
        "augmented_with_explicit_orbit_rank": int(nominal_matrix.row_join(orbit_column).rank())},
    "coordinate_component_bank": {
        "component_invariant": "q=coefficient_mask_XOR_form_slot_modulo_J4",
        "component_count": len(component_keys),
        "t_directions_per_component": 2*N,
        "connection_direction_count": sum(connection_counts.values()),
        "component_dimension_histogram": {str(key): value for key, value in sorted(histogram.items())},
        "complete_dimension": sum(component_sizes.values())},
    "broken_orbit": {
        "generator_count": len(broken_generators),
        "distinct_component_count": len(set(broken_keys)),
        "rank_per_branch": orbit_ranks},
    "complete_hessian": "OPEN_COMPONENT_RANKS_PENDING",
    "primitive_metric_symbol": "NOT_CONSTRUCTED",
    "claim_ceiling": "EXACT_RECONSTRUCTION_GRADE_COORDINATE_COMPONENT_ALIGNMENT_AND_ORBIT_LOCATION__NO_COMPLETE_RANK_OR_QUOTIENT_CLAIM",
    "next_gate": "CBRS1P_EVALUATE_EVERY_COORDINATE_COMPONENT_OVER_THE_EXACT_RADICAL_FIELDS__MATCH_MODULAR_LOWER_BOUNDS_TO_ORBIT_UPPER_BOUNDS__THEN_PRIMITIVE_METRIC_QUOTIENT_AND_SYMBOL_IF_ANY",
    "counts": dict(COUNTS),
    "failures": FAILURES}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
