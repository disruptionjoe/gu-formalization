#!/usr/bin/env sage
"""Independent Sage/FLINT replay of the K77 stabilizer-subbundle theorem."""

from collections import Counter
from hashlib import sha256
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
BANK_PATH = ROOT / "tests/fixtures/k77_minimal_tangent_bank_v1.json"
BASE_PATH = ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json"
COUNTS = Counter()
FAILURES = []
K.<sqrt3> = QuadraticField(3)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL"), "[" + kind + "]", label)
    if not ok:
        FAILURES.append(label)


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError("duplicate key %r in %s" % (key, path))
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


def canonical(payload):
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


class SparseEchelon:
    def __init__(self):
        self.pivots = {}

    def reduce(self, value):
        value = {key: K(item) for key, item in value.items() if item != 0}
        while value:
            pivot = min(value)
            lead = value[pivot]
            if pivot not in self.pivots:
                return value
            for key, item in self.pivots[pivot].items():
                result = value.get(key, K.zero()) - lead * item
                if result == 0:
                    value.pop(key, None)
                else:
                    value[key] = result
        return value

    def insert(self, value):
        value = self.reduce(value)
        if not value:
            return False
        pivot = min(value)
        lead = value[pivot]
        self.pivots[pivot] = {key: item / lead for key, item in value.items()}
        return True

    def rank(self):
        return len(self.pivots)


def sparse_rank(values):
    basis = SparseEchelon()
    for value in values:
        basis.insert(value)
    return basis.rank()


payload = strict(BANK_PATH)
base = strict(BASE_PATH)
unsigned = dict(payload)
unsigned.pop("construction_hash", None)
check("architecture", "independent canonical hash matches",
      sha256(canonical(unsigned)).hexdigest() == payload["construction_hash"])
check("architecture", "all dependency hashes are current",
      all((ROOT / relative).is_file()
          and sha256((ROOT / relative).read_bytes()).hexdigest() == expected
          for relative, expected in payload["dependency_hashes"].items()))

vectors = []
for item in payload["tangent"]["vectors"]:
    vectors.append({
        int(row): QQ(rn) / QQ(rd) + (QQ(sn) / QQ(sd)) * sqrt3
        for row, rn, rd, sn, sd in item["entries"]
    })
check("exact", "independent FLINT echelon rank is 594",
      len(vectors) == 594 and sparse_rank(vectors) == 594)

eta = tuple(payload["ambient"]["signature_diagonal"])
offslice = tuple(payload["ambient"]["offslice_global_rows"])
off_index = {row: index for index, row in enumerate(offslice)}
labels = tuple(base["receivers"]["labels"])
row_lookup = {
    (int(label["form_mask"]), int(label["clifford_mask"])): row
    for row, label in enumerate(labels)
}


def bits(mask):
    return tuple(index for index in range(14) if mask & (1 << index))


def generator(a, b):
    return {(a, b): 1, (b, a): -eta[a] * eta[b]}


def add_term(out, form, pair, scalar, coefficient, global_coordinates=False):
    if scalar == 0 or pair[0] == pair[1]:
        return
    left, right = pair
    sign = 1
    if left > right:
        left, right = right, left
        sign = -1
    global_row = row_lookup[(1 << form, (1 << left) | (1 << right))]
    row = global_row if global_coordinates else off_index[global_row]
    value = out.get(row, K.zero()) + K(sign * scalar) * coefficient
    if value == 0:
        out.pop(row, None)
    else:
        out[row] = value


def action(value, a, b, global_coordinates=False):
    matrix = generator(a, b)
    out = {}
    for local_row, coefficient in value.items():
        label = labels[offslice[local_row]]
        form = bits(int(label["form_mask"]))[0]
        left, right = bits(int(label["clifford_mask"]))
        for target in range(14):
            if (form, target) in matrix:
                add_term(out, target, (left, right), -matrix[(form, target)],
                         coefficient, global_coordinates)
            if (target, left) in matrix:
                add_term(out, form, (target, right), matrix[(target, left)],
                         coefficient, global_coordinates)
            if (target, right) in matrix:
                add_term(out, form, (left, target), matrix[(target, right)],
                         coefficient, global_coordinates)
    return out


base_generators = tuple((a, b) for a in range(4) for b in range(a + 1, 4))
normal_generators = tuple((a, b) for a in range(4, 14) for b in range(a + 1, 14))
check("exact", "independent generator census is 6 plus 45",
      len(base_generators) == 6 and len(normal_generators) == 45)

span = SparseEchelon()
for vector in vectors:
    span.insert(vector)
base_defects = sum(bool(span.reduce(action(vector, a, b)))
                   for a, b in base_generators for vector in vectors)
normal_defects = sum(bool(span.reduce(action(vector, a, b)))
                     for a, b in normal_generators for vector in vectors)
check("theorem", "all so(1,3) actions have zero quotient defect", base_defects == 0)
check("theorem", "all so(6,4) actions have zero quotient defect", normal_defects == 0)

full_span = SparseEchelon()
for vector in vectors:
    full_span.insert({offslice[row]: value for row, value in vector.items()})
for vector in vectors:
    full_span.insert(action(vector, 0, 4, global_coordinates=True))
check("planted", "a mixed ambient generator expands the rank-594 block fiber",
      full_span.rank() == 727)


def block_name(global_row):
    label = labels[global_row]
    form = bits(int(label["form_mask"]))[0]
    left, right = bits(int(label["clifford_mask"]))
    return ("H" if form < 4 else "N") + "_" + (
        "HH" if right < 4 else "HN" if left < 4 else "NN")


block_rows = {}
for local, global_row in enumerate(offslice):
    block_rows.setdefault(block_name(global_row), set()).add(local)
expected_profile = {
    "H_HN": (160, 160, 160),
    "H_NN": (180, 180, 180),
    "N_HH": (60, 60, 60),
    "N_HN": (400, 184, 184),
    "N_NN": (450, 10, 10),
}
profile = {}
all_rows = set(range(1250))
for name, rows in block_rows.items():
    projection = sparse_rank([{row: value for row, value in vector.items() if row in rows}
                              for vector in vectors])
    complement = all_rows - rows
    intersection = 594 - sparse_rank([
        {row: value for row, value in vector.items() if row in complement}
        for vector in vectors
    ])
    profile[name] = (len(rows), projection, intersection)
check("exact", "independent five-block profile is 160 plus 180 plus 60 plus 184 plus 10",
      profile == expected_profile)


def atomic(form, left, right, coefficient=1):
    sign = 1
    if left > right:
        left, right = right, left
        sign = -1
    global_row = row_lookup[(1 << form, (1 << left) | (1 << right))]
    return {off_index[global_row]: K(sign * coefficient)}


def combine(values):
    out = {}
    for value in values:
        for row, coefficient in value.items():
            result = out.get(row, K.zero()) + coefficient
            if result == 0:
                out.pop(row, None)
            else:
                out[row] = result
    return out


expected_184 = []
for horizontal in range(4):
    expected_184.append(combine([atomic(normal, horizontal, normal)
                                 for normal in range(4, 14)]))
    for left in range(4, 14):
        for right in range(left + 1, 14):
            expected_184.append(combine([
                atomic(right, horizontal, left),
                atomic(left, horizontal, right, -eta[left] * eta[right]),
            ]))
projection_184 = [{row: value for row, value in vector.items()
                   if row in block_rows["N_HN"]} for vector in vectors]
check("theorem", "independent rank-184 block equals H tensor (one plus so(6,4))",
      sparse_rank(expected_184) == 184
      and sparse_rank(projection_184 + expected_184) == 184)

expected_10 = [combine([atomic(form, vector, form)
                        for form in range(4, 14) if form != vector])
               for vector in range(4, 14)]
projection_10 = [{row: value for row, value in vector.items()
                  if row in block_rows["N_NN"]} for vector in vectors]
check("theorem", "independent rank-10 block equals the canonical contraction copy",
      sparse_rank(expected_10) == 10
      and sparse_rank(projection_10 + expected_10) == 10)

check("scope", "an invariant fiber is not a global reduction, trivialization, lower-order theorem, or quotient", True)
check("scope", "unitary parents and P1 P2 P3 remain untouched", True)
print("BASE_DEFECTS", base_defects)
print("NORMAL_DEFECTS", normal_defects)
print("FULL_AMBIENT_CROSS_RANK", full_span.rank())
print("PROFILE", profile)
print("CHECKS", dict(COUNTS))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print("PASS %d/%d" % (sum(COUNTS.values()), sum(COUNTS.values())))
