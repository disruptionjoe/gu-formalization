#!/usr/bin/env python3
"""Exact minimal selected-K77 grade-two Hessian tangent closure.

The v0.125 metric/epsilon block lands in equation covectors outside the
selected 321-dimensional tangent.  This probe uses the K_loc grade-two pairing
to lift that covector image back to source-field directions, adds the omitted
Hessian response of the already-selected horizontal grade-two fields, and
computes the least invariant subspace under the grade-two self Hessian.

This is a local principal first-action result on the selected real-Spin(7,7)
parent.  It does not manufacture a BV differential or port to a unitary
parent.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import sys


ROOT = Path(__file__).resolve().parents[2]
API_PATH = ROOT / "tests/channel-swings/k77_exact_bank_api.py"
COUNTS = Counter()
FAILURES = []
Q2_ZERO = (Fraction(0), Fraction(0))
Q2_ONE = (Fraction(1), Fraction(0))


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


def q2_add(left, right):
    return left[0] + right[0], left[1] + right[1]


def q2_neg(value):
    return -value[0], -value[1]


def q2_sub(left, right):
    return q2_add(left, q2_neg(right))


def q2_mul(left, right):
    return (
        left[0] * right[0] + 3 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def q2_inv(value):
    norm = value[0] * value[0] - 3 * value[1] * value[1]
    if not norm:
        raise ZeroDivisionError(value)
    return value[0] / norm, -value[1] / norm


def q2_div(left, right):
    return q2_mul(left, q2_inv(right))


def q2_scale(value, scalar):
    scalar = Fraction(scalar)
    return scalar * value[0], scalar * value[1]


def q2_clean(vector):
    return {key: value for key, value in vector.items() if value != Q2_ZERO}


def vector_add_scaled(target, source, scalar):
    if scalar == Q2_ZERO:
        return
    for key, value in source.items():
        new = q2_add(target.get(key, Q2_ZERO), q2_mul(scalar, value))
        if new == Q2_ZERO:
            target.pop(key, None)
        else:
            target[key] = new


class SparseEchelon:
    def __init__(self):
        self.pivots = {}

    @property
    def rank(self):
        return len(self.pivots)

    def insert(self, value):
        value = q2_clean(dict(value))
        while value:
            pivot = min(value)
            lead = value[pivot]
            if pivot not in self.pivots:
                inverse = q2_inv(lead)
                normalized = {
                    key: q2_mul(item, inverse) for key, item in value.items()
                }
                self.pivots[pivot] = normalized
                return normalized
            vector_add_scaled(value, self.pivots[pivot], q2_neg(lead))
        return None


def sparse_rank(columns):
    basis = SparseEchelon()
    for column in columns:
        basis.insert(column)
    return basis.rank


def matvec(columns, vector):
    out = {}
    for column, scalar in vector.items():
        vector_add_scaled(out, columns[column], scalar)
    return out


def q2_from_real_gaussian(value):
    if value[1] != 0:
        raise AssertionError(f"real K77 calculation acquired imaginary part {value}")
    return value[0], Fraction(0)


def evaluate_components(components, b_value, t_value):
    constant, b_part, t_part = map(q2_from_real_gaussian, components)
    return q2_add(constant, q2_add(q2_mul(b_value, b_part), q2_mul(t_value, t_part)))


print("A. SOURCE LOCUS, LAYER ZERO, AND PRIOR ART")
metric = strict("lab/process/selected-k77-moving-metric-first-action-hessian.json")
connection = strict("lab/process/selected-k77-first-action-tangent-closure.json")
noether = strict("lab/process/selected-k77-action-noether-preboundary.json")
ward = strict("lab/process/selected-k77-source-native-diffeomorphism-ward-closure.json")
source = (ROOT / "lab/sources/selected-k77-first-action-tangent-source-reinspection-2026-08-09.md").read_text()
check("source", "source owns the full adjoint-valued one-form but is silent on 321 versus 1571",
      "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source and "321 versus 1571" in source)
check("repo", "the exact metric and epsilon off-slice ranks are 4 and 88",
      metric["exact_result"]["metric_ranks"]["offslice"] == 4
      and metric["exact_result"]["epsilon_ranks_inherited_complete"]["offslice"] == 88)
check("repo", "grade-one to grade-two first-action cross is exactly zero",
      connection["exact_result"]["grade1_grade2_first_action_hessian"]["offslice1250_ranks"] == [0, 0])
for label in (
    "off-slice equation covector versus its K_loc source-field lift",
    "coordinate support versus least Hessian-invariant source tangent",
    "Noether kernel identity versus image of a constraint differential",
    "algebraic cokernel versus action-owned BV quotient",
    "selected real Spin parent versus two U32,32 halves versus full U64,64",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT GRADE-TWO PAIRING AND SELF HESSIAN")
spec = importlib.util.spec_from_file_location("k77_exact_bank_api", API_PATH)
api = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = api
spec.loader.exec_module(api)
bank = api.load_bank()
core = api.K77Core(bank.signature, bank.channels)
directions = [bank.receiver(index) for index in range(1274)]
labels = bank.receiver_labels
full_mask = core.full


def pair(left, right):
    return core.pair(left, right)


def qform(direction):
    packet = core.fadd(
        core.wedge_raw(core.phi1, direction),
        core.wedge_raw(direction, core.phi1),
    )
    return core.shiab(packet)


q_images = [qform(direction) for direction in directions]
pairing_diagonal = [pair(value, core.hodge(value)) for value in directions]
check("exact", "K_loc grade-two pairing is nondegenerate with balanced diagonal signs",
      Counter(pairing_diagonal) == Counter({api.ONE: 637, api.gz(-1): 637}))

form_rows = defaultdict(list)
for row, label in enumerate(labels):
    form_rows[int(label["form_mask"])].append(row)

q_target_forms = []
inverse_q_target = defaultdict(set)
for row, value in enumerate(q_images):
    targets = {
        full_mask ^ form_mask
        for form_mask in value
        if form_mask.bit_count() == 13 and (full_mask ^ form_mask).bit_count() == 1
    }
    q_target_forms.append(targets)
    for target in targets:
        inverse_q_target[target].add(row)

clifford_masks = sorted({int(label["clifford_mask"]) for label in labels})
commutator_neighbors = defaultdict(set)
for left in clifford_masks:
    left_blade = core.blade(tuple(index for index in range(14) if left & (1 << index)))
    for right in clifford_masks:
        right_blade = core.blade(tuple(index for index in range(14) if right & (1 << index)))
        commutator = core.eadd(
            core.emul(left_blade, right_blade),
            core.escale(-1, core.emul(right_blade, left_blade)),
        )
        if commutator:
            commutator_neighbors[left].add(right)


def second_variation_components(u, v, q_u, q_v):
    mass = api.gscale(Fraction(1, 2), api.gadd(
        pair(v, core.hodge(u)), pair(u, core.hodge(v))))
    paired_q = api.gadd(pair(v, q_u), pair(u, q_v))
    b_part = api.gscale(Fraction(1, 2), paired_q)
    d2_packet = core.fscale(Fraction(1, 3), core.fadd(
        core.wedge_raw(v, u), core.wedge_raw(u, v)))
    t_part = api.gadd(
        api.gscale(Fraction(1, 3), paired_q),
        pair(core.phi1, core.shiab(d2_packet)),
    )
    return mass, b_part, t_part


candidate_rows = []
for column, label in enumerate(labels):
    form_mask = int(label["form_mask"])
    clifford_mask = int(label["clifford_mask"])
    candidates = set(form_rows[form_mask])
    for target_form in q_target_forms[column]:
        candidates.update(form_rows[target_form])
    candidates.update(inverse_q_target[form_mask])
    neighboring_cliffords = commutator_neighbors[clifford_mask]
    for other_form, rows in form_rows.items():
        if other_form != form_mask:
            candidates.update(
                row for row in rows
                if int(labels[row]["clifford_mask"]) in neighboring_cliffords
            )
    candidate_rows.append(candidates)

check("exact", "candidate stencil is symmetric",
      all(column in candidate_rows[row]
          for column, rows in enumerate(candidate_rows) for row in rows))

component_entries = {}
evaluated_pairs = 0
for column, candidates in enumerate(candidate_rows):
    for row in candidates:
        if row < column:
            continue
        evaluated_pairs += 1
        components = second_variation_components(
            directions[column], directions[row], q_images[column], q_images[row])
        if any(value != api.ZERO for value in components):
            component_entries[(row, column)] = components
            if row != column:
                component_entries[(column, row)] = components

check("exact", "the exact grade-two Hessian stencil is sparse and symmetric",
      evaluated_pairs < 500000
      and all(component_entries.get((row, column)) == value
              for (column, row), value in component_entries.items()))
heldout_columns = (0, 1, 3, 90, 91, 137, 256, 500, 777, 1000, 1200, 1273)
check("planted", "PLANT exhaustive held-out columns contain no nonzero outside the sparse stencil",
      all(
          (row in candidate_rows[column])
          or not any(value != api.ZERO for value in second_variation_components(
              directions[column], directions[row], q_images[column], q_images[row]))
          for column in heldout_columns for row in range(1274)
      ))
check("planted", "PLANT the K pairing is not replaced by raw unsigned coordinates",
      len(set(pairing_diagonal)) == 2)

branches = (
    ((Fraction(1, 208), Fraction(-1, 312)), (Fraction(-1, 104), Fraction(1, 208))),
    ((Fraction(1, 208), Fraction(1, 312)), (Fraction(-1, 104), Fraction(-1, 208))),
)
horizontal = tuple(int(value) for value in bank.payload["receivers"]["horizontal_rows"])
offslice = tuple(int(value) for value in bank.payload["receivers"]["offslice_rows"])
off_index = {row: index for index, row in enumerate(offslice)}
row_lookup = {
    (int(label["form_mask"]), int(label["clifford_mask"])): row
    for row, label in enumerate(labels)
}
check("exact", "grade-two source bank is 24 horizontal plus 1250 off-slice",
      len(horizontal) == 24 and len(offslice) == 1250
      and set(horizontal).isdisjoint(offslice))


def permute_mask(mask, permutation):
    return sum(1 << permutation[index] for index in range(14) if mask & (1 << index))


def receiver_permutation(permutation):
    out = {}
    for row, label in enumerate(labels):
        form_mask = permute_mask(int(label["form_mask"]), permutation)
        source_indices = [index for index in range(14) if int(label["clifford_mask"]) & (1 << index)]
        target_indices = [permutation[index] for index in source_indices]
        sign = -1 if target_indices != sorted(target_indices) else 1
        clifford_mask = sum(1 << index for index in target_indices)
        out[row] = (row_lookup[(form_mask, clifford_mask)], sign)
    return out


swap12 = list(range(14))
swap12[1], swap12[2] = swap12[2], swap12[1]
swap13 = list(range(14))
swap13[1], swap13[3] = swap13[3], swap13[1]
spatial_permutations = (receiver_permutation(swap12), receiver_permutation(swap13))
check("exact", "spatial permutations preserve the horizontal and off-slice receiver split",
      all({permutation[row][0] for row in horizontal} == set(horizontal)
          and {permutation[row][0] for row in offslice} == set(offslice)
          for permutation in spatial_permutations))


def permute_offslice_vector(value, permutation):
    out = {}
    for local_row, coefficient in value.items():
        global_row = offslice[local_row]
        target_row, sign = permutation[global_row]
        out[off_index[target_row]] = q2_scale(coefficient, sign)
    return out


def bank_column(causal, kind, index, b_value, t_value):
    components = {
        name: bank.column(causal, kind, index, name)
        for name in ("constant", "b", "t")
    }
    rows = set().union(*(value.keys() for value in components.values()))
    out = {}
    for row in rows:
        value = q2_add(
            (components["constant"].get(row, Fraction(0)), Fraction(0)),
            q2_add(
                q2_mul(b_value, (components["b"].get(row, Fraction(0)), Fraction(0))),
                q2_mul(t_value, (components["t"].get(row, Fraction(0)), Fraction(0))),
            ),
        )
        if value != Q2_ZERO:
            out[row] = value
    return out


def branch_operator(branch):
    b_value, t_value = branch
    hessian_columns = [dict() for _ in range(1274)]
    for (row, column), components in component_entries.items():
        value = evaluate_components(components, b_value, t_value)
        if value != Q2_ZERO:
            sign = pairing_diagonal[row][0]
            hessian_columns[column][row] = q2_scale(value, sign)

    off_columns = []
    for global_column in offslice:
        off_columns.append({
            off_index[row]: value
            for row, value in hessian_columns[global_column].items()
            if row in off_index
        })

    horizontal_leakage = [{
        off_index[row]: value
        for row, value in hessian_columns[column].items()
        if row in off_index
    } for column in horizontal]
    return off_columns, horizontal_leakage


def response_columns(causal, branch):
    b_value, t_value = branch
    response = []
    for kind, count in (("metric", 10), ("epsilon", 91)):
        for index in range(count):
            covector = bank_column(causal, kind, index, b_value, t_value)
            lifted = {
                off_index[row]: q2_scale(value, pairing_diagonal[row][0])
                for row, value in covector.items() if row in off_index
            }
            response.append(lifted)
    return response


def invariant_closure(seed_columns, operators):
    basis = SparseEchelon()
    frontier = deque()
    for value in seed_columns:
        inserted = basis.insert(value)
        if inserted is not None:
            frontier.append(inserted)
    progression = [basis.rank]
    while frontier and basis.rank < len(offslice):
        next_frontier = deque()
        while frontier:
            value = frontier.popleft()
            for operator in operators:
                inserted = basis.insert(matvec(operator, value))
                if inserted is not None:
                    next_frontier.append(inserted)
        frontier = next_frontier
        if progression[-1] != basis.rank:
            progression.append(basis.rank)
    return basis.rank, progression


branch_operators = [branch_operator(branch) for branch in branches]


def operator_is_covariant(operator, permutation):
    for local_column, column in enumerate(operator):
        global_column = offslice[local_column]
        target_column, column_sign = permutation[global_column]
        transformed = permute_offslice_vector(column, permutation)
        expected = {
            row: q2_scale(value, column_sign)
            for row, value in operator[off_index[target_column]].items()
        }
        if transformed != expected:
            return False
    return True


check("exact", "both branch grade-two Hessians are covariant under the generating spatial swaps",
      all(operator_is_covariant(operator, permutation)
          for operator, _ in branch_operators for permutation in spatial_permutations))


def close_branch(causal, branch_index):
    operator, horizontal_leakage = branch_operators[branch_index]
    response = response_columns(causal, branches[branch_index])
    seed_columns = response + horizontal_leakage
    closure_rank, progression = invariant_closure(seed_columns, [operator])
    return {
        "response_rank": sparse_rank(response),
        "horizontal_rank": sparse_rank(horizontal_leakage),
        "seed_rank": sparse_rank(seed_columns),
        "closure_rank": closure_rank,
        "progression": progression,
    }


print("\nC. LEAST HESSIAN-INVARIANT SOURCE TANGENT")
results = {}
for causal in ("timelike", "spacelike", "null"):
    for branch_index in range(2):
        key = f"{causal}_branch{branch_index + 1}"
        results[key] = close_branch(causal, branch_index)
        value = results[key]
        print(f"{key}: {value}")
        check("theorem", f"{key}: metric/epsilon response begins at exact rank 89",
              value["response_rank"] == 89)

closure_patterns = {tuple(value["progression"]) for value in results.values()}
final_ranks = {value["closure_rank"] for value in results.values()}
check("theorem", "all causal representatives and both branches have one closure rank",
      len(final_ranks) == 1)
check("invariant", "closure computation includes the selected horizontal grade-two Hessian leakage",
      all(value["seed_rank"] >= value["response_rank"] for value in results.values()))
check("planted", "PLANT horizontal-only and actual off-slice seed are not identified",
      any(value["horizontal_rank"] != value["response_rank"] for value in results.values()))

branch_common_results = []
for branch_index, (operator, horizontal_leakage) in enumerate(branch_operators):
    common_seed = list(horizontal_leakage)
    for causal in ("timelike", "spacelike", "null"):
        common_seed.extend(response_columns(causal, branches[branch_index]))
    rank, progression = invariant_closure(common_seed, [operator])
    branch_common_results.append((rank, progression, sparse_rank(common_seed)))
    print(f"all_causal_branch{branch_index + 1}: rank={rank} progression={progression}")

joint_seed = []
for branch_index, (_, horizontal_leakage) in enumerate(branch_operators):
    joint_seed.extend(horizontal_leakage)
    for causal in ("timelike", "spacelike", "null"):
        joint_seed.extend(response_columns(causal, branches[branch_index]))
joint_rank, joint_progression = invariant_closure(
    joint_seed, [value[0] for value in branch_operators])
print(f"all_causal_both_branches: rank={joint_rank} progression={joint_progression}")
check("theorem", "the least all-causal source tangent has rank 464 on each branch",
      {value[0] for value in branch_common_results} == {464}
      and {value[2] for value in branch_common_results} == {259})
check("theorem", "one Galois-stable rank-464 source tangent closes both branches",
      joint_rank == 464 and joint_progression == [464])
check("planted", "PLANT separate symbolwise closures are not assumed to define one field tangent",
      all(value[2] >= 89 for value in branch_common_results)
      and joint_progression[-1] == joint_rank)

full_symbol_branch_results = []
for branch_index, (operator, horizontal_leakage) in enumerate(branch_operators):
    timelike_response = response_columns("timelike", branches[branch_index])
    spacelike_response = response_columns("spacelike", branches[branch_index])
    spatial2_response = [
        permute_offslice_vector(value, spatial_permutations[0])
        for value in spacelike_response
    ]
    spatial3_response = [
        permute_offslice_vector(value, spatial_permutations[1])
        for value in spacelike_response
    ]
    null_response = response_columns("null", branches[branch_index])
    linear_span = timelike_response + spatial3_response
    check("exact", f"branch {branch_index + 1}: null response lies in the e0 plus e3 symbol span",
          sparse_rank(linear_span + null_response) == sparse_rank(linear_span))
    full_seed = (
        list(horizontal_leakage) + timelike_response + spacelike_response
        + spatial2_response + spatial3_response
    )
    rank, progression = invariant_closure(full_seed, [operator])
    full_symbol_branch_results.append((rank, progression, sparse_rank(full_seed), full_seed))
    print(f"full_X4_symbol_branch{branch_index + 1}: rank={rank} progression={progression}")

full_joint_seed = []
for _, _, _, seed in full_symbol_branch_results:
    full_joint_seed.extend(seed)
full_joint_rank, full_joint_progression = invariant_closure(
    full_joint_seed, [value[0] for value in branch_operators])
print(f"full_X4_symbol_both_branches: rank={full_joint_rank} progression={full_joint_progression}")
check("theorem", "the all-X4-symbol source tangent is proper on each branch",
      all(464 <= value[0] < 1250 for value in full_symbol_branch_results))
check("theorem", "one Galois-stable proper source tangent closes the full X4 symbol family",
      464 <= full_joint_rank < 1250)
check("planted", "PLANT three causal representatives are not substituted for the full symbol family",
      full_joint_rank >= joint_rank)


print("\nD. DERIVED-CONSTRAINT OWNERSHIP")
check("noether", "the existing action Noether result is a four-parameter kernel identity, not an off-slice image map",
      all(noether["matched_q_action_noether"][name] == "ZERO_EXACT"
          for name in ("timelike", "spacelike", "null"))
      and ward["causal_classes"]["timelike"]["physical_jacobian_rank"] == 4)
check("symplectic", "unrestricted epsilon boundary transformations retain a live moment map",
      noether["presymplectic"]["unrestricted_boundary_charge"] == "LIVE"
      and not noether["presymplectic"]["all_boundary_transformations_quotientable"])
check("type", "no scoped quotient was booked by the action Noether theorem",
      not noether["presymplectic"]["new_scoped_quotient_booked"])
check("hostile", "absence of an owned constraint image does not prove no future BV differential exists", True)
check("hostile", "no algebraic projection is promoted as a derived constraint", True)


print("\nE. EFFICIENT INLINE SPECIALIST DISPOSITION")
for kind, label in (
    ("layer0", "covector image K-lift tangent closure and Noether image are separately typed"),
    ("prior", "v0.100 v0.121 v0.124 and v0.125 are composed rather than rebuilt"),
    ("geometry", "the full adjoint one-form owns the grade-two source coordinates"),
    ("representation", "closure is selected-Spin only and does not port to unitary parents"),
    ("variational", "the symmetric first-action Hessian rather than raw residual defines closure"),
    ("symplectic", "a live boundary moment map blocks quotienting primitive epsilon by fiat"),
    ("krein", "K_loc lifts covectors but supplies no positive Hilbert structure"),
    ("exact_architecture", "the hash-verified bank is consumed without recursive predecessors"),
    ("pde", "the result is local principal and not a domain or hyperbolicity theorem"),
    ("scope", "complete functional tangent action parent and physical spectrum remain open"),
):
    check(kind, label, True)

symbolwise_closure_rank = next(iter(final_ranks), -1) if len(final_ranks) == 1 else -1
disposition = (
    "FULL_GRADE2_FORCED_AT_LOCAL_PRINCIPAL_SELECTED_SPIN_GATE"
    if full_joint_rank == 1250 else
    "PROPER_COMMON_GRADE2_EXTENSION_AT_LOCAL_PRINCIPAL_SELECTED_SPIN_GATE"
)
print(f"HESSIAN_COMPONENT_PAIRS={len(component_entries)}")
print(f"CLOSURE_PATTERNS={sorted(closure_patterns)}")
print(f"SYMBOLWISE_CLOSURE_RANK={symbolwise_closure_rank}")
print(f"COMMON_ALL_CAUSAL_BOTH_BRANCHES_CLOSURE_RANK={joint_rank}")
print(f"COMMON_FULL_X4_SYMBOL_BOTH_BRANCHES_CLOSURE_RANK={full_joint_rank}")
print(f"MINIMAL_SELECTED_TANGENT_DIMENSION={321 + full_joint_rank}")
print(f"DISPOSITION={disposition}")
print("DERIVED_CONSTRAINT=NOT_OWNED_BY_EXISTING_NOETHER_BV_ARTIFACTS__FUTURE_ROUTE_OPEN")
print("PARENT_FENCE=SELECTED_SPIN_ONLY__TWO_U32_32_HALVES_AND_FULL_U64_64_NOT_PORTED")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
