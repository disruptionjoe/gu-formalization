#!/usr/bin/env sage
"""Independent Sage/FLINT replay of the v0.126 tangent-closure theorem."""

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import importlib.util
import sys


ROOT = Path(__file__).resolve().parents[2]
API_PATH = ROOT / "tests/channel-swings/k77_exact_bank_api.py"
FAILURES = []
COUNTS = {"exact": 0, "planted": 0}


def PF(numerator, denominator=1):
    return Fraction(int(numerator), int(denominator))


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [" + kind + "] " + label)
    if not ok:
        FAILURES.append(label)


spec = importlib.util.spec_from_file_location("k77_exact_bank_api_sage", API_PATH)
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
    return core.shiab(core.fadd(
        core.wedge_raw(core.phi1, direction),
        core.wedge_raw(direction, core.phi1),
    ))


def second_variation_components(u, v, q_u, q_v):
    mass = api.gscale(PF(1, 2), api.gadd(
        pair(v, core.hodge(u)), pair(u, core.hodge(v))))
    paired_q = api.gadd(pair(v, q_u), pair(u, q_v))
    b_part = api.gscale(PF(1, 2), paired_q)
    d2_packet = core.fscale(PF(1, 3), core.fadd(
        core.wedge_raw(v, u), core.wedge_raw(u, v)))
    t_part = api.gadd(
        api.gscale(PF(1, 3), paired_q),
        pair(core.phi1, core.shiab(d2_packet)),
    )
    return mass, b_part, t_part


q_images = [qform(direction) for direction in directions]
pairing_signs = [ZZ(int(pair(value, core.hodge(value))[0])) for value in directions]
check("exact", "independent K pairing has inertia 637 637",
      pairing_signs.count(1) == 637 and pairing_signs.count(-1) == 637)

form_rows = defaultdict(list)
for row, label in enumerate(labels):
    form_rows[int(label["form_mask"])].append(row)

q_target_forms = []
inverse_q_target = defaultdict(set)
for row, value in enumerate(q_images):
    targets = {
        full_mask ^^ form_mask
        for form_mask in value
        if int(form_mask).bit_count() == 13
        and int(full_mask ^^ form_mask).bit_count() == 1
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
            core.escale(PF(-1), core.emul(right_blade, left_blade)),
        )
        if commutator:
            commutator_neighbors[left].add(right)

candidate_rows = []
for column, label in enumerate(labels):
    form_mask = int(label["form_mask"])
    clifford_mask = int(label["clifford_mask"])
    candidates = set(form_rows[form_mask])
    for target_form in q_target_forms[column]:
        candidates.update(form_rows[target_form])
    candidates.update(inverse_q_target[form_mask])
    for other_form, rows in form_rows.items():
        if other_form != form_mask:
            candidates.update(
                row for row in rows
                if int(labels[row]["clifford_mask"]) in commutator_neighbors[clifford_mask]
            )
    candidate_rows.append(candidates)

components = {}
for column, candidates in enumerate(candidate_rows):
    for row in candidates:
        if row < column:
            continue
        value = second_variation_components(
            directions[column], directions[row], q_images[column], q_images[row])
        if any(item != api.ZERO for item in value):
            components[(row, column)] = value
            components[(column, row)] = value

check("exact", "independent grade-two component bank has 5642 directed entries",
      len(components) == 5642)

K.<r> = QuadraticField(3)


def real_component(value):
    if value[1] != PF(0):
        raise AssertionError("nonreal K77 coefficient: %r" % (value,))
    return K(QQ(int(value[0].numerator)) / QQ(int(value[0].denominator)))


def SK(value):
    if isinstance(value, Fraction):
        return K(QQ(int(value.numerator)) / QQ(int(value.denominator)))
    return K(value)


branches = (
    (K(1)/208-r/312, (-K(2)+r)/208),
    (K(1)/208+r/312, (-K(2)-r)/208),
)
horizontal = list(map(int, bank.payload["receivers"]["horizontal_rows"]))
offslice = list(map(int, bank.payload["receivers"]["offslice_rows"]))
off_index = {row: index for index, row in enumerate(offslice)}
row_lookup = {
    (int(label["form_mask"]), int(label["clifford_mask"])): row
    for row, label in enumerate(labels)
}


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


def off_permutation_matrix(permutation):
    entries = {}
    for source_local, source_global in enumerate(offslice):
        target_global, sign = permutation[source_global]
        entries[(off_index[target_global], source_local)] = K(sign)
    return matrix(K, 1250, 1250, entries, sparse=True)


spatial_matrices = tuple(off_permutation_matrix(value) for value in spatial_permutations)


def evaluated_bank_column(causal, kind, index, b_value, t_value):
    pieces = {
        name: bank.column(causal, kind, index, name)
        for name in ("constant", "b", "t")
    }
    rows = set().union(*[set(value) for value in pieces.values()])
    return {
        row: SK(pieces["constant"].get(row, PF(0)))
             + b_value * SK(pieces["b"].get(row, PF(0)))
             + t_value * SK(pieces["t"].get(row, PF(0)))
        for row in rows
        if SK(pieces["constant"].get(row, PF(0)))
           + b_value * SK(pieces["b"].get(row, PF(0)))
           + t_value * SK(pieces["t"].get(row, PF(0))) != 0
    }


def columns_matrix(columns, row_count):
    entries = {}
    for column, value in enumerate(columns):
        for row, coefficient in value.items():
            if coefficient != 0:
                entries[(row, column)] = coefficient
    return matrix(K, row_count, len(columns), entries, sparse=True)


def branch_operator(branch):
    b_value, t_value = branch
    h_entries = {}
    for (row, column), value in components.items():
        coefficient = (
            real_component(value[0])
            + b_value * real_component(value[1])
            + t_value * real_component(value[2])
        )
        if coefficient != 0:
            h_entries[(row, column)] = pairing_signs[row] * coefficient

    aoo_entries = {
        (off_index[row], off_index[column]): coefficient
        for (row, column), coefficient in h_entries.items()
        if row in off_index and column in off_index
    }
    aoo = matrix(K, 1250, 1250, aoo_entries, sparse=True)

    horizontal_columns = [{
        off_index[row]: coefficient
        for (row, column), coefficient in h_entries.items()
        if column == source_column and row in off_index
    } for source_column in horizontal]
    return aoo, columns_matrix(horizontal_columns, 1250)


def response_matrix(causal, branch):
    b_value, t_value = branch
    response = []
    for kind, count in (("metric", 10), ("epsilon", 91)):
        for index in range(count):
            covector = evaluated_bank_column(causal, kind, index, b_value, t_value)
            response.append({
                off_index[row]: pairing_signs[row] * coefficient
                for row, coefficient in covector.items() if row in off_index
            })
    return columns_matrix(response, 1250)


def invariant_closure(seed, operators):
    progression = [seed.rank()]
    basis = seed.column_space().basis_matrix().transpose()
    while basis.ncols() < 1250:
        enlarged = basis
        for operator in operators:
            enlarged = enlarged.augment(operator * basis)
        new_rank = enlarged.rank()
        if new_rank == basis.ncols():
            break
        progression.append(new_rank)
        basis = enlarged.column_space().basis_matrix().transpose()
    return basis.ncols(), progression


branch_operators = [branch_operator(branch) for branch in branches]
check("exact", "independent branch operators commute with both spatial permutation generators",
      all(permutation * operator == operator * permutation
          for operator, _ in branch_operators for permutation in spatial_matrices))


def closure_result(causal, branch_index):
    aoo, horizontal_matrix = branch_operators[branch_index]
    response = response_matrix(causal, branches[branch_index])
    seed = response.augment(horizontal_matrix)
    rank, progression = invariant_closure(seed, [aoo])
    return response.rank(), horizontal_matrix.rank(), seed.rank(), rank, progression


results = {}
for causal in ("timelike", "spacelike", "null"):
    for branch_index in range(2):
        key = causal + "_branch" + str(branch_index + 1)
        results[key] = closure_result(causal, branch_index)
        print(key, results[key])

check("exact", "all independent response ranks are 89",
      {value[0] for value in results.values()} == {89})
check("exact", "all independent horizontal leakage ranks are 4",
      {value[1] for value in results.values()} == {4})
check("exact", "horizontal leakage adds no initial seed rank",
      {value[2] for value in results.values()} == {89})
check("exact", "least invariant closure has rank 174 in all six cases",
      {value[3] for value in results.values()} == {174})
check("exact", "timelike and spacelike stabilize in one image step",
      {tuple(value[4]) for key, value in results.items() if not key.startswith("null")} == {(89, 174)})
check("exact", "null stabilizes through the exact intermediate rank 164",
      {tuple(value[4]) for key, value in results.items() if key.startswith("null")} == {(89, 164, 174)})
check("planted", "PLANT closure is proper and not the raw 1250-coordinate support",
      all(value[3] < 1250 for value in results.values()))
check("planted", "PLANT response rank and invariant closure rank are not identified",
      all(value[0] != value[3] for value in results.values()))

branch_common = []
for branch_index, (operator, horizontal_matrix) in enumerate(branch_operators):
    seed = horizontal_matrix
    for causal in ("timelike", "spacelike", "null"):
        seed = seed.augment(response_matrix(causal, branches[branch_index]))
    rank, progression = invariant_closure(seed, [operator])
    branch_common.append((seed.rank(), rank, progression))
    print("all_causal_branch%s" % (branch_index + 1), branch_common[-1])

joint_seed = matrix(K, 1250, 0, sparse=True)
for branch_index, (_, horizontal_matrix) in enumerate(branch_operators):
    joint_seed = joint_seed.augment(horizontal_matrix)
    for causal in ("timelike", "spacelike", "null"):
        joint_seed = joint_seed.augment(response_matrix(causal, branches[branch_index]))
joint_rank, joint_progression = invariant_closure(
    joint_seed, [value[0] for value in branch_operators])
print("all_causal_both_branches", (joint_seed.rank(), joint_rank, joint_progression))
check("exact", "each all-causal branch seed has rank 259 and closes at 464",
      {(value[0], value[1], tuple(value[2])) for value in branch_common} == {(259, 464, (259, 464))})
check("exact", "the joint Galois-stable tangent has rank 464 and is already invariant",
      joint_seed.rank() == 464 and joint_rank == 464 and joint_progression == [464])
check("planted", "PLANT symbolwise rank 174 is not promoted as a common field tangent",
      joint_rank != 174)

full_branch = []
for branch_index, (operator, horizontal_matrix) in enumerate(branch_operators):
    timelike = response_matrix("timelike", branches[branch_index])
    spacelike = response_matrix("spacelike", branches[branch_index])
    spatial2 = spatial_matrices[0] * spacelike
    spatial3 = spatial_matrices[1] * spacelike
    null = response_matrix("null", branches[branch_index])
    check("exact", "branch %s null image lies in e0 plus e3 span" % (branch_index + 1),
          timelike.augment(spatial3).augment(null).rank()
          == timelike.augment(spatial3).rank())
    seed = horizontal_matrix.augment(timelike).augment(spacelike).augment(spatial2).augment(spatial3)
    rank, progression = invariant_closure(seed, [operator])
    full_branch.append((seed.rank(), rank, progression, seed))
    print("full_X4_symbol_branch%s" % (branch_index + 1), full_branch[-1][:3])

full_joint_seed = full_branch[0][3].augment(full_branch[1][3])
full_joint_rank, full_joint_progression = invariant_closure(
    full_joint_seed, [value[0] for value in branch_operators])
print("full_X4_symbol_both_branches", (full_joint_seed.rank(), full_joint_rank, full_joint_progression))
check("exact", "each full-X4 branch seed has rank 344 and closes at 594",
      {(value[0], value[1], tuple(value[2])) for value in full_branch} == {(344, 594, (344, 594))})
check("exact", "the joint full-X4 Galois-stable tangent has rank 594 and is invariant",
      full_joint_seed.rank() == 594 and full_joint_rank == 594
      and full_joint_progression == [594])
check("planted", "PLANT the three-representative rank 464 is not the full symbol tangent",
      full_joint_rank != 464)

print("CHECKS exact=%s planted=%s" % (COUNTS["exact"], COUNTS["planted"]))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS %s/%s" % (sum(COUNTS.values()), sum(COUNTS.values())))
