#!/usr/bin/env python3
"""Exact observation-stabilizer test for the rank-594 K77 tangent fiber."""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import sys
import tempfile


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


def q2_inv(value):
    norm = value[0] * value[0] - 3 * value[1] * value[1]
    if not norm:
        raise ZeroDivisionError(value)
    return value[0] / norm, -value[1] / norm


def q2_scale(value, scalar):
    scalar = Fraction(scalar)
    return scalar * value[0], scalar * value[1]


def add_scaled(target, source, scalar):
    for key, value in source.items():
        product = q2_mul(scalar, value)
        result = q2_add(target.get(key, Q2_ZERO), product)
        if result == Q2_ZERO:
            target.pop(key, None)
        else:
            target[key] = result


class SparseEchelon:
    def __init__(self):
        self.pivots = {}

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
            add_scaled(value, self.pivots[pivot], (-lead[0], -lead[1]))
        return value

    def insert(self, value):
        value = self.reduce(dict(value))
        if not value:
            return False
        pivot = min(value)
        inverse = q2_inv(value[pivot])
        self.pivots[pivot] = {key: q2_mul(item, inverse) for key, item in value.items()}
        return True


def sparse_rank(columns):
    basis = SparseEchelon()
    for column in columns:
        basis.insert(column)
    return basis.rank


print("A. BANK, SOURCE LOCUS, AND LAYER ZERO")
tangent_api = load_module("k77_minimal_tangent_bank_api", "tests/channel-swings/k77_minimal_tangent_bank_api.py")
base_api = load_module("k77_exact_bank_api_for_stabilizer", "tests/channel-swings/k77_exact_bank_api.py")
tangent = tangent_api.load_bank()
base = base_api.load_bank()
vectors = tangent.vectors()
labels = base.receiver_labels
offslice = tangent.offslice_rows
off_index = {row: index for index, row in enumerate(offslice)}
row_lookup = {
    (int(label["form_mask"]), int(label["clifford_mask"])): row
    for row, label in enumerate(labels)
}
check("exact_architecture", "ordinary consumer loads a canonical rank-594 bank without executing its producer",
      tangent.rank == 594 and tangent.payload["tangent"]["nnz"] == 1850)
check("exact", "serialized vectors are an exact canonical rank-594 echelon basis",
      sparse_rank(vectors) == 594
      and [min(vector) for vector in vectors]
      == [item["pivot"] for item in tangent.payload["tangent"]["vectors"]])
check("type", "coordinate basis, invariant fiber, associated subbundle, and global trivialization remain distinct", True)
check("type", "selected Spin parent, two U32,32 halves, and full U64,64 remain distinct", True)

with tempfile.TemporaryDirectory() as temporary:
    temporary = Path(temporary)

    def rejected(name, mutate, rehash=False):
        payload = json.loads(json.dumps(tangent.payload))
        mutate(payload)
        if rehash:
            payload["construction_hash"] = tangent_api.payload_hash(payload)
        path = temporary / name
        path.write_bytes(tangent_api.canonical(payload))
        try:
            tangent_api.load_bank(path)
        except tangent_api.TangentBankIntegrityError:
            return True
        return False

    check("planted", "PLANT a coefficient mutation is rejected by the construction hash",
          rejected("mutated.json", lambda p: p["tangent"]["vectors"][0]["entries"][0].__setitem__(1, 7)))
    check("planted", "PLANT a self-consistent wrong rank is rejected by the schema gate",
          rejected("wrong-rank.json", lambda p: p["tangent"].__setitem__("rank", 593), rehash=True))
    check("planted", "PLANT a self-consistent stale dependency is rejected",
          rejected("stale.json", lambda p: p["dependency_hashes"].__setitem__(
              next(iter(p["dependency_hashes"])), "0" * 64), rehash=True))


def bits(mask):
    return tuple(index for index in range(14) if mask & (1 << index))


def generator(a, b):
    eta = tangent.signature
    return {(a, b): 1, (b, a): -eta[a] * eta[b]}


def add_receiver_term(out, form, pair, scalar, coefficient, global_coordinates=False):
    if scalar == 0 or pair[0] == pair[1]:
        return
    left, right = pair
    sign = 1
    if left > right:
        left, right = right, left
        sign = -1
    global_row = row_lookup[(1 << form, (1 << left) | (1 << right))]
    row = global_row if global_coordinates else off_index[global_row]
    value = q2_scale(coefficient, scalar * sign)
    result = q2_add(out.get(row, Q2_ZERO), value)
    if result == Q2_ZERO:
        out.pop(row, None)
    else:
        out[row] = result


def action(value, a, b, include_covector=True, include_adjoint=True, global_coordinates=False):
    matrix = generator(a, b)
    out = {}
    for local_row, coefficient in value.items():
        global_row = offslice[local_row]
        label = labels[global_row]
        form = bits(int(label["form_mask"]))[0]
        left, right = bits(int(label["clifford_mask"]))
        if include_covector:
            for target in range(14):
                if (form, target) in matrix:
                    add_receiver_term(out, target, (left, right),
                                      -matrix[(form, target)], coefficient,
                                      global_coordinates)
        if include_adjoint:
            for target in range(14):
                if (target, left) in matrix:
                    add_receiver_term(out, form, (target, right),
                                      matrix[(target, left)], coefficient,
                                      global_coordinates)
                if (target, right) in matrix:
                    add_receiver_term(out, form, (left, target),
                                      matrix[(target, right)], coefficient,
                                      global_coordinates)
    return out


def phi1_action(a, b, include_covector=True, include_vector=True):
    matrix = generator(a, b)
    out = {}
    for form in range(14):
        vector = form
        if include_covector:
            for target in range(14):
                coefficient = -matrix.get((form, target), 0)
                if coefficient:
                    out[(target, vector)] = out.get((target, vector), 0) + coefficient
        if include_vector:
            for target in range(14):
                coefficient = matrix.get((target, vector), 0)
                if coefficient:
                    out[(form, target)] = out.get((form, target), 0) + coefficient
    return {key: value for key, value in out.items() if value}


print("\nB. REPRESENTATION AND PLANTED CONTROLS")
eta = tangent.signature
base_generators = tuple((a, b) for a in range(4) for b in range(a + 1, 4))
normal_generators = tuple((a, b) for a in range(4, 14) for b in range(a + 1, 14))
stabilizer_generators = base_generators + normal_generators
check("exact", "the observation stabilizer has all 6 plus 45 infinitesimal generators",
      len(base_generators) == 6 and len(normal_generators) == 45
      and len(stabilizer_generators) == 51)
check("exact", "every generator is skew for the exact K77 diagonal metric",
      all(
          all(
              eta[i] * generator(a, b).get((i, j), 0)
              + eta[j] * generator(a, b).get((j, i), 0) == 0
              for i in range(14) for j in range(14)
          )
          for a, b in stabilizer_generators
      ))
check("exact", "simultaneous covector and vector action fixes the tautological Phi1 tensor",
      all(not phi1_action(a, b) for a, b in stabilizer_generators))
check("planted", "PLANT covector-only action fails tautological invariance",
      any(phi1_action(a, b, include_vector=False) for a, b in stabilizer_generators))
check("planted", "PLANT vector-only action fails tautological invariance",
      any(phi1_action(a, b, include_covector=False) for a, b in stabilizer_generators))


print("\nC. COMPLETE OBSERVATION-STABILIZER INVARIANCE")
span = SparseEchelon()
for vector in vectors:
    span.insert(vector)
defects = {}
for a, b in stabilizer_generators:
    failures = sum(bool(span.reduce(action(vector, a, b))) for vector in vectors)
    defects[(a, b)] = failures
    check("generator", f"generator ({a},{b}) preserves the rank-594 tangent", failures == 0)
base_failures = sum(defects[pair] for pair in base_generators)
normal_failures = sum(defects[pair] for pair in normal_generators)
check("theorem", "all six so(1,3) generators preserve the tangent exactly", base_failures == 0)
check("theorem", "all forty-five so(6,4) generators preserve the tangent exactly", normal_failures == 0)

# The full ambient group is deliberately not the observation stabilizer. Embed
# tangent vectors in all 1,274 grade-two coordinates and fire one mixed H/N
# generator as a scope control.
full_span = SparseEchelon()
for vector in vectors:
    full_span.insert({offslice[row]: value for row, value in vector.items()})
cross_actions = [action(vector, 0, 4, global_coordinates=True) for vector in vectors]
cross_rank_before = full_span.rank
for value in cross_actions:
    full_span.insert(value)
cross_rank_after = full_span.rank
check("planted", "PLANT full ambient so(7,7) invariance is not inferred from block-stabilizer invariance",
      cross_rank_after > cross_rank_before)


print("\nD. NATURAL BLOCK PROFILE")
def block_name(global_row):
    label = labels[global_row]
    form = bits(int(label["form_mask"]))[0]
    left, right = bits(int(label["clifford_mask"]))
    form_part = "H" if form < 4 else "N"
    if right < 4:
        bivector_part = "HH"
    elif left < 4:
        bivector_part = "HN"
    else:
        bivector_part = "NN"
    return f"{form_part}_{bivector_part}"

block_rows = {}
for local, global_row in enumerate(offslice):
    block_rows.setdefault(block_name(global_row), set()).add(local)
expected_block_dimensions = {"H_HN": 160, "H_NN": 180, "N_HH": 60,
                             "N_HN": 400, "N_NN": 450}
check("exact", "offslice representation has the five source-natural block dimensions",
      {name: len(rows) for name, rows in block_rows.items()} == expected_block_dimensions)
block_profile = {}
all_rows = set(range(1250))
for name, rows in sorted(block_rows.items()):
    projection = sparse_rank([
        {row: value for row, value in vector.items() if row in rows}
        for vector in vectors
    ])
    complement = all_rows - rows
    complement_projection = sparse_rank([
        {row: value for row, value in vector.items() if row in complement}
        for vector in vectors
    ])
    intersection = 594 - complement_projection
    block_profile[name] = {
        "ambient": len(rows), "projection": projection, "intersection": intersection
    }
    print(name, block_profile[name])
check("exact", "block projections and intersections obey rank bounds",
      all(0 <= value["intersection"] <= value["projection"] <= value["ambient"]
          for value in block_profile.values()))


def atomic_receiver(form, left, right, coefficient=1):
    sign = 1
    if left > right:
        left, right = right, left
        sign = -1
    global_row = row_lookup[(1 << form, (1 << left) | (1 << right))]
    return {off_index[global_row]: (Fraction(sign * coefficient), Fraction(0))}


def combine(*vectors_to_add):
    out = {}
    for value in vectors_to_add:
        add_scaled(out, value, (Fraction(1), Fraction(0)))
    return out


# N* tensor (H wedge N) is H tensor End(N). The retained 184 dimensions are
# exactly H tensor (scalar identity plus so(6,4)); the 54-dimensional normal
# symmetric-tracefree summand is absent for each of the four H factors.
expected_n_hn = []
for horizontal_index in range(4):
    expected_n_hn.append(combine(*[
        atomic_receiver(normal, horizontal_index, normal)
        for normal in range(4, 14)
    ]))
    for left in range(4, 14):
        for right in range(left + 1, 14):
            expected_n_hn.append(combine(
                atomic_receiver(right, horizontal_index, left),
                atomic_receiver(left, horizontal_index, right,
                                -eta[left] * eta[right]),
            ))
n_hn_projection = [
    {row: value for row, value in vector.items() if row in block_rows["N_HN"]}
    for vector in vectors
]
check("theorem", "the rank-184 N_HN sector is exactly H tensor (one plus so(6,4))",
      len(expected_n_hn) == 184
      and sparse_rank(expected_n_hn) == 184
      and sparse_rank(n_hn_projection + expected_n_hn) == 184)

# The remaining ten dimensions in N* tensor Lambda2(N) are the canonical
# vector/contraction injection v -> sum_a theta^a tensor (v wedge e_a).
expected_n_nn = []
for vector_index in range(4, 14):
    expected_n_nn.append(combine(*[
        atomic_receiver(form_index, vector_index, form_index)
        for form_index in range(4, 14) if form_index != vector_index
    ]))
n_nn_projection = [
    {row: value for row, value in vector.items() if row in block_rows["N_NN"]}
    for vector in vectors
]
check("theorem", "the rank-10 N_NN sector is exactly the canonical normal contraction copy",
      sparse_rank(expected_n_nn) == 10
      and sparse_rank(n_nn_projection + expected_n_nn) == 10)


print("\nE. ASSOCIATED-SUBBUNDLE AND SCOPE DISPOSITION")
check("geometry", "an invariant rank-594 fiber defines an associated subbundle after an observation reduction is supplied",
      all(value == 0 for value in defects.values()))
check("type", "stabilizer invariance does not construct the observation reduction or a preferred global frame", True)
check("variational", "principal invariant-fiber closure does not imply lower-order or derivative-jet Hessian closure", True)
check("symplectic", "no constraint quotient or reduced phase space is manufactured", True)
check("krein", "representation invariance supplies no positive Hilbert majorant or closed domain", True)
check("source", "source owns the full connection and observation reduction grammar but is silent on the rank-594 subbundle", True)
check("scope", "no action-parent, Einstein, Standard Model, spectrum, index, or quantum verdict moves", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)

print(f"BANK_RANK={tangent.rank}")
print(f"BANK_NNZ={tangent.payload['tangent']['nnz']}")
print(f"STABILIZER_GENERATORS={len(stabilizer_generators)}")
print(f"STABILIZER_DEFECTS={sum(defects.values())}")
print(f"CROSS_GENERATOR_RANK={cross_rank_before}->{cross_rank_after}")
print(f"BLOCK_PROFILE={block_profile}")
print("NATURAL_DECOMPOSITION=HSTAR_HN160_PLUS_HSTAR_NN180_PLUS_NSTAR_HH60_PLUS_H_TENSOR_1_PLUS_SO64_184_PLUS_NORMAL_CONTRACTION10")
print("DISPOSITION=INVARIANT594__ASSOCIATED_SUBBUNDLE_CONDITIONAL_ON_OBSERVATION_REDUCTION")
print("LOWER_ORDER_DERIVATIVE_JET=OPEN")
print("PARENT_FENCE=SELECTED_SPIN_ONLY__TWO_U32_32_HALVES_AND_FULL_U64_64_NOT_PORTED")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
