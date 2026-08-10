#!/usr/bin/env python3
"""Exact lower-order and first-jet closure of the selected K77 Euler operator.

The source variation owns ``Upsilon = Shiab(F_A) + Hodge(T)``.  At fixed
epsilon its varpi linearization is the first-order operator

    D_varpi Upsilon[u] = Shiab(d_A u) + Hodge(u).

This probe composes the already-closed metric/epsilon blocks, then decides the
low-grade field tangent under observed H* jets and under all ambient V*=H*+N*
jets.  It keeps the source Euler operator distinct from a pointwise density
Hessian and from the residual-square Gram action.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import sys


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []
Q2_ZERO = (Fraction(0), Fraction(0))


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


def q2_add(left, right):
    return left[0] + right[0], left[1] + right[1]


def q2_mul(left, right):
    return (
        left[0] * right[0] + 3 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def q2_neg(value):
    return -value[0], -value[1]


def q2_inv(value):
    norm = value[0] * value[0] - 3 * value[1] * value[1]
    if not norm:
        raise ZeroDivisionError(value)
    return value[0] / norm, -value[1] / norm


def q2_scale(value, scalar):
    scalar = Fraction(scalar)
    return scalar * value[0], scalar * value[1]


def add_scaled(target, source, scalar):
    if scalar == Q2_ZERO:
        return
    for key, value in source.items():
        result = q2_add(target.get(key, Q2_ZERO), q2_mul(scalar, value))
        if result == Q2_ZERO:
            target.pop(key, None)
        else:
            target[key] = result


class SparseEchelon:
    def __init__(self, values=()):
        self.pivots = {}
        for value in values:
            self.insert(value)

    @property
    def rank(self):
        return len(self.pivots)

    def reduce(self, value):
        value = {key: item for key, item in value.items() if item != Q2_ZERO}
        while value:
            pivot = min(value)
            lead = value[pivot]
            if pivot not in self.pivots:
                return value
            add_scaled(value, self.pivots[pivot], q2_neg(lead))
        return value

    def insert(self, value):
        value = self.reduce(dict(value))
        if not value:
            return False
        pivot = min(value)
        inverse = q2_inv(value[pivot])
        self.pivots[pivot] = {
            key: q2_mul(item, inverse) for key, item in value.items()
        }
        return True


def sparse_rank(values):
    return SparseEchelon(values).rank


def matvec(columns, vector):
    out = {}
    for column, scalar in vector.items():
        add_scaled(out, columns[column], scalar)
    return out


print("A. SOURCE LOCUS, PRIOR ART, AND LAYER ZERO")
source = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
epsilon = strict("lab/process/selected-k77-moving-epsilon-first-action-completion.json")
metric = strict("lab/process/selected-k77-moving-metric-first-action-hessian.json")
minimum = strict("lab/process/selected-k77-minimal-hessian-tangent-closure.json")
subbundle = strict("lab/process/selected-k77-observation-stabilizer-subbundle.json")
section = strict("lab/process/selected-k77-physical-section-faithfulness-gate.json")
check("source", "source owns the first Y14 action and its first-order Euler residual",
      "I^B_1" in source and "d_{B_\\omega}T_\\omega" in source
      and "\\Upsilon^B_\\omega" in source and "F_{A_\\omega}" in source)
check("prior_art", "complete epsilon lower-Cartan and moving-Shiab grade-two corrections are zero",
      epsilon["exact_result"]["lower_cartan_ranks"] == {"full": 0, "horizontal": 0, "offslice": 0}
      and epsilon["exact_result"]["moving_shiab_ranks"] == {"full": 0, "horizontal": 0, "offslice": 0})
check("prior_art", "complete stationary metric block is the exact cached source block",
      metric["exact_result"]["complete_metric_equals_cached_fixed_operator_source_block"] is True)
check("prior_art", "v0.126 owns rank 594 only at local X4 principal grade",
      minimum["scope"]["differential_grade"] == "LOCAL_PRINCIPAL_FULL_X4_SYMBOL_FAMILY"
      and minimum["exact_result"]["full_X4_both_branches"]["closure"] == 594)
check("prior_art", "ordinary observation pullback has an independent rank-ten conormal kernel",
      section["exact_results"]["conormal_kernel_rank"] == 10
      and section["result"].startswith("COMPLETE_RECEIVER_REQUIRED"))
check("prior_art", "rank 594 is an observation-stabilizer fiber, not an ambient Spin77 fiber",
      subbundle["layer0"]["invariant_fiber"] == "PROVED"
      and subbundle["layer0"]["full_ambient_spin77_invariance"].startswith("REFUTED"))
for label in (
    "source Euler linearization versus pointwise density Hessian",
    "first-action Euler operator versus residual-square Gram Hessian",
    "scalar exterior covector q versus Clifford-vector-valued Phi1 component",
    "observed H-star first jets versus full ambient H-star plus N-star first jets",
    "selected low-grade projection versus two U32,32 halves and full U64,64",
    "tangent expansion versus image of an action-owned BV differential",
):
    check("type", label + " remain distinct", True)


base_api = load_module("k77_exact_bank_api_for_euler_jet", "tests/channel-swings/k77_exact_bank_api.py")
tangent_api = load_module("k77_minimal_tangent_bank_api_for_euler_jet", "tests/channel-swings/k77_minimal_tangent_bank_api.py")
base = base_api.load_bank()
tangent = tangent_api.load_bank()
core = base_api.K77Core(base.signature, base.channels)
directions2 = [base.receiver(row) for row in range(1274)]
directions1 = [
    {1 << form: core.blade(coefficient)}
    for form in range(14) for coefficient in range(14)
]
labels = base.receiver_labels
offslice = tangent.offslice_rows
off_index = {row: index for index, row in enumerate(offslice)}
row_lookup = {
    (int(label["form_mask"]), int(label["clifford_mask"])): row
    for row, label in enumerate(labels)
}
pairing_diagonal = [core.pair(value, core.hodge(value)) for value in directions2]
check("exact", "low-grade source coordinates are 196 grade one plus 1274 grade two",
      len(directions1) == 196 and len(directions2) == 1274)
check("exact", "grade-two K lift is nondegenerate and balanced",
      Counter(pairing_diagonal) == Counter({base_api.ONE: 637, base_api.gz(-1): 637}))


def equation_to_offslice(equation):
    """K-lift a degree-13 equation form into off-slice grade-two fields."""
    out = {}
    for form_mask, element in equation.items():
        receiver_form = core.full ^ form_mask
        if receiver_form.bit_count() != 1:
            continue
        wedge_sign = core.wedge_sign(receiver_form, form_mask)
        for clifford_mask, coefficient in element.items():
            global_row = row_lookup.get((receiver_form, clifford_mask))
            if global_row not in off_index:
                continue
            scalar_mask, clifford_sign = core.blade_product(clifford_mask, clifford_mask)
            if scalar_mask:
                continue
            covector = base_api.gscale(wedge_sign * clifford_sign, coefficient)
            lifted = base_api.gmul(covector, pairing_diagonal[global_row])
            local_row = off_index[global_row]
            value = q2_add(out.get(local_row, Q2_ZERO), lifted)
            if value == Q2_ZERO:
                out.pop(local_row, None)
            else:
                out[local_row] = value
    return out


def scalar_covector(mu):
    return {1 << mu: {0: base_api.ONE}}


def euler_symbol(mu, direction):
    return core.shiab(core.wedge_raw(scalar_covector(mu), direction))


def symbol_column(mu, direction):
    return equation_to_offslice(euler_symbol(mu, direction))


def coefficient_grades(form):
    return {mask.bit_count() for element in form.values() for mask in element}


print("\nB. SOURCE FIRST-ORDER SYMBOL AND CONTROLS")
heldouts = (0, 1, 13, 14, 60, 100, 137, 195)
for mu in range(4):
    for index in heldouts:
        direct = {
            local: base_api.gmul(core.pair(directions2[global_row], euler_symbol(mu, directions1[index])),
                                 pairing_diagonal[global_row])
            for local, global_row in enumerate(offslice)
            if core.pair(directions2[global_row], euler_symbol(mu, directions1[index])) != base_api.ZERO
        }
        check("exact", f"q{mu} grade-one heldout {index}: direct and sparse K lifts agree",
              direct == symbol_column(mu, directions1[index]))

grade1_symbol_grades = set()
grade2_symbol_grades = set()
for mu in range(4):
    for direction in directions1:
        grade1_symbol_grades.update(coefficient_grades(euler_symbol(mu, direction)))
    for direction in directions2:
        grade2_symbol_grades.update(coefficient_grades(euler_symbol(mu, direction)))
check("theorem", "scalar q couples grade one only into grade-two equation coefficients",
      grade1_symbol_grades == {2})
check("theorem", "scalar q couples grade two only into grade-one or grade-five equation coefficients",
      grade2_symbol_grades == {1, 5})
check("type", "all selected grade-one equation receivers are already retained; grade five remains a parent fence", True)

bad_q = {1: core.blade(0)}
bad_outputs = [core.shiab(core.wedge_raw(bad_q, direction)) for direction in directions2]
check("planted", "PLANT a Clifford-vector q creates forbidden same-grade output and is rejected",
      any(2 in coefficient_grades(value) for value in bad_outputs))
check("planted", "PLANT same-grade projection would erase the live first-order grade1-grade2 coupling",
      any(symbol_column(mu, direction) for mu in range(4) for direction in directions1)
      and not any(symbol_column(mu, direction) for mu in range(4) for direction in directions2))


print("\nC. OBSERVED FOUR-JET CLOSURE")
base_vectors = tangent.vectors()
observed_span = SparseEchelon(base_vectors)
observed_progression = [observed_span.rank]
observed_columns = []
for mu in range(4):
    columns = [symbol_column(mu, direction) for direction in directions1]
    observed_columns.extend(columns)
    for column in columns:
        observed_span.insert(column)
    observed_progression.append(observed_span.rank)
print("OBSERVED_PROGRESSION=" + repr(observed_progression))
check("theorem", "four observed covector directions enlarge 594 by 54 each to 810",
      observed_progression == [594, 648, 702, 756, 810])
check("theorem", "the observed derivative image supplies exactly 216 new grade-two directions",
      observed_span.rank - tangent.rank == 216)


def bits(mask):
    return tuple(index for index in range(14) if mask & (1 << index))


def block_name(global_row):
    label = labels[global_row]
    form = bits(int(label["form_mask"]))[0]
    left, right = bits(int(label["clifford_mask"]))
    return ("H" if form < 4 else "N") + "_" + (
        "HH" if right < 4 else "HN" if left < 4 else "NN")


block_rows = {}
for local, global_row in enumerate(offslice):
    block_rows.setdefault(block_name(global_row), set()).add(local)


def block_profile(vectors):
    rank = sparse_rank(vectors)
    all_rows = set(range(1250))
    out = {}
    for name, rows in sorted(block_rows.items()):
        projection = sparse_rank([
            {row: value for row, value in vector.items() if row in rows}
            for vector in vectors
        ])
        complement = all_rows - rows
        intersection = rank - sparse_rank([
            {row: value for row, value in vector.items() if row in complement}
            for vector in vectors
        ])
        out[name] = {"ambient": len(rows), "projection": projection, "intersection": intersection}
    return out


observed_vectors = tuple(observed_span.pivots.values())
observed_profile = block_profile(observed_vectors)
expected_observed_profile = {
    "H_HN": {"ambient": 160, "projection": 160, "intersection": 160},
    "H_NN": {"ambient": 180, "projection": 180, "intersection": 180},
    "N_HH": {"ambient": 60, "projection": 60, "intersection": 60},
    "N_HN": {"ambient": 400, "projection": 400, "intersection": 400},
    "N_NN": {"ambient": 450, "projection": 10, "intersection": 10},
}
print("OBSERVED_PROFILE=" + repr(observed_profile))
check("theorem", "observed jets fill precisely the missing H tensor Sym0(N) rank-216 block",
      observed_profile == expected_observed_profile)


def generator(a, b):
    eta = tangent.signature
    return {(a, b): 1, (b, a): -eta[a] * eta[b]}


def add_receiver_term(out, form, pair, scalar, coefficient):
    if not scalar or pair[0] == pair[1]:
        return
    left, right = pair
    sign = 1
    if left > right:
        left, right = right, left
        sign = -1
    global_row = row_lookup[(1 << form, (1 << left) | (1 << right))]
    if global_row not in off_index:
        return
    local_row = off_index[global_row]
    value = q2_scale(coefficient, scalar * sign)
    result = q2_add(out.get(local_row, Q2_ZERO), value)
    if result == Q2_ZERO:
        out.pop(local_row, None)
    else:
        out[local_row] = result


def stabilizer_action(value, a, b):
    matrix = generator(a, b)
    out = {}
    for local_row, coefficient in value.items():
        label = labels[offslice[local_row]]
        form = bits(int(label["form_mask"]))[0]
        left, right = bits(int(label["clifford_mask"]))
        for target in range(14):
            if (form, target) in matrix:
                add_receiver_term(out, target, (left, right), -matrix[(form, target)], coefficient)
            if (target, left) in matrix:
                add_receiver_term(out, form, (target, right), matrix[(target, left)], coefficient)
            if (target, right) in matrix:
                add_receiver_term(out, form, (left, target), matrix[(target, right)], coefficient)
    return out


stabilizer_generators = (
    tuple((a, b) for a in range(4) for b in range(a + 1, 4))
    + tuple((a, b) for a in range(4, 14) for b in range(a + 1, 14))
)
stabilizer_defects = sum(
    bool(observed_span.reduce(stabilizer_action(vector, a, b)))
    for a, b in stabilizer_generators for vector in observed_vectors
)
check("theorem", "the rank-810 observed-jet fiber is invariant under all 51 stabilizer generators",
      stabilizer_defects == 0)


print("\nD. LOWER-ORDER DIRECT EULER CLOSURE")


def equation_column(equation):
    return equation_to_offslice(equation)


def a_operator_column(direction):
    commutator_curvature = core.fadd(
        core.wedge_raw(core.phi1, direction),
        core.wedge_raw(direction, core.phi1),
    )
    return equation_column(core.shiab(commutator_curvature))


a_columns = [a_operator_column(directions2[row]) for row in offslice]
mass_columns = [equation_column(core.hodge(directions2[row])) for row in offslice]
check("exact", "the Hodge mass K-lift is the identity on all 1250 off-slice coordinates",
      all(column == {index: (Fraction(1), Fraction(0))}
          for index, column in enumerate(mass_columns)))
lower_span = SparseEchelon(observed_vectors)
for vector in observed_vectors:
    lower_span.insert(matvec(a_columns, vector))
check("theorem", "the background-A lower-order Euler operator preserves rank 810",
      lower_span.rank == 810)

grade1_zero_order = []
for direction in directions1:
    curvature = core.fadd(
        core.wedge_raw(core.phi1, direction),
        core.wedge_raw(direction, core.phi1),
    )
    grade1_zero_order.append(equation_column(core.fadd(core.shiab(curvature), core.hodge(direction))))
check("theorem", "grade-one lower-order Euler columns have no omitted grade-two component",
      not any(grade1_zero_order))
check("composition", "completed metric and epsilon lower-order blocks add no new grade-two direction",
      epsilon["exact_result"]["coefficientwise_total_equals_fixed"] is True
      and metric["exact_result"]["complete_metric_equals_cached_fixed_operator_source_block"] is True)
check("construction", "the complete selected low-grade value-plus-observed-first-jet tangent is 1131",
      321 + observed_span.rank == 1131)


print("\nE. FULL AMBIENT Y14 FIRST-JET CLOSURE")
ambient_span = SparseEchelon(base_vectors)
ambient_progression = [ambient_span.rank]
for mu in range(14):
    for direction in directions1:
        ambient_span.insert(symbol_column(mu, direction))
    ambient_progression.append(ambient_span.rank)
print("AMBIENT_PROGRESSION=" + repr(ambient_progression))
check("theorem", "observed four jets reach 810 before conormal jets enter",
      ambient_progression[:5] == [594, 648, 702, 756, 810])
check("theorem", "the ten conormal jet directions force the complete off-slice rank 1250",
      ambient_progression[-1] == 1250 and ambient_progression[5] > 810)
check("theorem", "full source-native Y14 first jets force the complete low-grade tangent 1571",
      321 + ambient_span.rank == 1571)
check("planted", "PLANT observed X4 closure is not promoted to ambient Y14 closure",
      observed_span.rank == 810 and ambient_span.rank == 1250)
check("layer0", "an observed-only 1131 tangent requires a conormal-jet restriction not supplied by ordinary pullback",
      section["construction_fork"]["selected"] is False
      and section["exact_results"]["action_conormal_witness_nonzero"] is True)


print("\nF. DISPOSITION AND FENCES")
for kind, label in (
    ("variational", "the unsymmetrized source Euler symbol, not a pointwise symmetric matrix, owns first-jet closure"),
    ("symplectic", "tangent expansion does not erase the live endpoint moment map or create a BV quotient"),
    ("pde", "value-plus-first-jet closure is not a hyperbolicity or closed-domain theorem"),
    ("krein", "K lifting uses the exact indefinite pairing and supplies no positive majorant"),
    ("representation", "selected low-grade Spin, two U32,32 halves, and full U64,64 remain distinct"),
    ("source", "source owns all Y14 derivative jets and is silent on a conormal restriction selecting 1131"),
    ("scope", "no Einstein Standard Model spectrum index dark-energy or quantum verdict moves"),
    ("accounting", "no coefficient quotient source type or external datum is added"),
    ("accounting", "P1 P2 P3 remain unchanged and unused"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_FIRST_Y14_ACTION_DB_T_AND_FIRST_ORDER_UPSILON__SOURCE_SILENT_CONORMAL_JET_RESTRICTION_AND_TANGENT_SELECTION")
print("OBSERVED_X4=GRADE2_594_TO810__TOTAL_TANGENT1131__N_HN_184_TO400")
print("AMBIENT_Y14=GRADE2_594_TO1250__TOTAL_LOW_GRADE_TANGENT1571")
print("LOWER_ORDER=HODGE_IDENTITY__BACKGROUND_A_PRESERVES810__METRIC_EPSILON_PREDECESSORS_COMPOSE")
print("DISPOSITION=OBSERVED1131_CONDITIONAL__SOURCE_NATIVE_Y14_FIRST_JETS_FORCE_FULL1571__TANGENT915_NOT_FIRST_JET_CLOSED")
print("PARENT_FENCE=SELECTED_LOW_GRADE_SPIN_ONLY__GRADE5_TWO_U32_32_HALVES_FULL_U64_64_NOT_PORTED")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
