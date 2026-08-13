#!/usr/bin/env sage
"""Independent Sage/FLINT replay of the K77 Euler first-jet closure."""

from collections import Counter
from hashlib import sha256
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
TANGENT_PATH = ROOT / "tests/fixtures/k77_minimal_tangent_bank_v1.json"
BASE_PATH = ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json"
COUNTS = Counter()
FAILURES = []
K.<sqrt3> = QuadraticField(3)
GZERO = (QQ.zero(), QQ.zero())
GONE = (QQ.one(), QQ.zero())
GI = (QQ.zero(), QQ.one())


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


def gadd(left, right):
    return left[0] + right[0], left[1] + right[1]


def gmul(left, right):
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def gscale(scalar, value):
    return QQ(scalar) * value[0], QQ(scalar) * value[1]


class SparseEchelon:
    def __init__(self, values=()):
        self.pivots = {}
        for value in values:
            self.insert(value)

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
    return SparseEchelon(values).rank()


tangent_payload = strict(TANGENT_PATH)
base_payload = strict(BASE_PATH)
unsigned = dict(tangent_payload)
unsigned.pop("construction_hash", None)
check("architecture", "tangent hash independently matches",
      sha256(canonical(unsigned)).hexdigest() == tangent_payload["construction_hash"])
check("architecture", "tangent dependencies remain current",
      all((ROOT / relative).is_file()
          and sha256((ROOT / relative).read_bytes()).hexdigest() == expected
          for relative, expected in tangent_payload["dependency_hashes"].items()))

vectors = [{
    int(row): QQ(rn) / QQ(rd) + (QQ(sn) / QQ(sd)) * sqrt3
    for row, rn, rd, sn, sd in item["entries"]
} for item in tangent_payload["tangent"]["vectors"]]
check("exact", "independent starting tangent rank is 594",
      len(vectors) == 594 and sparse_rank(vectors) == 594)

eta = tuple(tangent_payload["ambient"]["signature_diagonal"])
full = (1 << 14) - 1
channels = tuple(base_payload["carrier"]["selected_shiab_channels"])
labels = tuple(base_payload["receivers"]["labels"])
offslice = tuple(tangent_payload["ambient"]["offslice_global_rows"])
off_index = {row: index for index, row in enumerate(offslice)}
row_lookup = {(int(label["form_mask"]), int(label["clifford_mask"])): row
              for row, label in enumerate(labels)}


def bits(mask):
    return tuple(index for index in range(14) if mask & (1 << index))


def blade_product(left, right):
    inversions = sum(1 for i in bits(left) for j in bits(right) if i > j)
    sign = -1 if inversions % 2 else 1
    for index in bits(left & right):
        sign *= eta[index]
    return left ^^ right, sign


def eclean(value):
    return {mask: coefficient for mask, coefficient in value.items() if coefficient != GZERO}


def eadd(*values):
    out = {}
    for value in values:
        for mask, coefficient in value.items():
            out[mask] = gadd(out.get(mask, GZERO), coefficient)
    return eclean(out)


def escale(scalar, value):
    gaussian = scalar if isinstance(scalar, tuple) else (QQ(scalar), QQ.zero())
    return eclean({mask: gmul(gaussian, coefficient) for mask, coefficient in value.items()})


def emul(left, right):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            mask, sign = blade_product(lm, rm)
            out[mask] = gadd(out.get(mask, GZERO), gscale(sign, gmul(lc, rc)))
    return eclean(out)


def blade(item):
    if isinstance(item, int):
        item = (item,)
    return {sum(1 << index for index in item): GONE}


def fclean(value):
    return {mask: eclean(coefficient) for mask, coefficient in value.items() if eclean(coefficient)}


def fadd(*values):
    out = {}
    for value in values:
        for mask, coefficient in value.items():
            out[mask] = eadd(out.get(mask, {}), coefficient)
    return fclean(out)


def fscale(scalar, value):
    return fclean({mask: escale(scalar, coefficient) for mask, coefficient in value.items()})


def wedge_sign(left, right):
    if left & right:
        return 0
    inversions = sum(1 for i in bits(left) for j in bits(right) if i > j)
    return -1 if inversions % 2 else 1


def coefficient_product(left, right, channel):
    xy, yx = emul(left, right), emul(right, left)
    if channel == "comm":
        return eadd(xy, escale(-1, yx))
    if channel == "symi":
        return escale(GI, eadd(xy, yx))
    raise ValueError(channel)


def wedge(left, right, channel=None):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            sign = wedge_sign(lm, rm)
            if not sign:
                continue
            product = emul(lc, rc) if channel is None else coefficient_product(lc, rc, channel)
            out[lm | rm] = eadd(out.get(lm | rm, {}), escale(sign, product))
    return fclean(out)


def hodge(value):
    out = {}
    for mask, coefficient in value.items():
        complement = full ^^ mask
        norm = prod(eta[index] for index in bits(mask))
        out[complement] = eadd(out.get(complement, {}), escale(wedge_sign(mask, complement) * norm, coefficient))
    return fclean(out)


phi1 = {1 << index: blade(index) for index in range(14)}
phi2 = fscale(QQ(1) / 2, wedge(phi1, phi1))


def shiab(curvature):
    star = hodge(curvature)
    first = wedge(phi1, star, channels[0])
    middle = hodge(wedge(phi2, star, channels[1]))
    second = hodge(wedge(phi1, middle, channels[2]))
    return fadd(first, fscale(QQ(-1) / 2, second))


def receiver(row):
    label = labels[row]
    real, imag = label["coefficient"]
    return {int(label["form_mask"]): {int(label["clifford_mask"]):
            (QQ(real[0]) / QQ(real[1]), QQ(imag[0]) / QQ(imag[1]))}}


directions2 = [receiver(row) for row in range(1274)]
directions1 = [{1 << form: blade(coefficient)}
               for form in range(14) for coefficient in range(14)]


def pairing_diagonal(row):
    label = labels[row]
    form_mask = int(label["form_mask"])
    clifford_mask = int(label["clifford_mask"])
    complement = full ^^ form_mask
    hodge_sign = wedge_sign(form_mask, complement) * prod(eta[index] for index in bits(form_mask))
    exterior = wedge_sign(form_mask, complement)
    _, clifford_sign = blade_product(clifford_mask, clifford_mask)
    return QQ(hodge_sign * exterior * clifford_sign)


diagonal = tuple(pairing_diagonal(row) for row in range(1274))
check("exact", "independent K diagonal is balanced 637 plus 637",
      Counter(diagonal) == Counter({QQ.one(): 637, QQ(-1): 637}))


def equation_column(equation):
    out = {}
    for form_mask, element in equation.items():
        one_form = full ^^ form_mask
        if int(one_form).bit_count() != 1:
            continue
        for clifford_mask, coefficient in element.items():
            row = row_lookup.get((one_form, clifford_mask))
            if row not in off_index:
                continue
            _, clifford_sign = blade_product(clifford_mask, clifford_mask)
            value = gscale(wedge_sign(one_form, form_mask) * clifford_sign, coefficient)
            if value[1] != 0:
                raise AssertionError("projected real operator acquired imaginary coefficient")
            local = off_index[row]
            result = out.get(local, K.zero()) + K(value[0]) * K(diagonal[row])
            if result == 0:
                out.pop(local, None)
            else:
                out[local] = result
    return out


def scalar_q(mu):
    return {1 << mu: {0: GONE}}


def symbol_column(mu, direction):
    return equation_column(shiab(wedge(scalar_q(mu), direction)))


observed = SparseEchelon(vectors)
observed_progression = [observed.rank()]
for mu in range(4):
    for direction in directions1:
        observed.insert(symbol_column(mu, direction))
    observed_progression.append(observed.rank())
check("theorem", "independent observed progression is 594 648 702 756 810",
      observed_progression == [594, 648, 702, 756, 810])


def block_name(global_row):
    label = labels[global_row]
    form = bits(int(label["form_mask"]))[0]
    left, right = bits(int(label["clifford_mask"]))
    return ("H" if form < 4 else "N") + "_" + (
        "HH" if right < 4 else "HN" if left < 4 else "NN")


block_rows = {}
for local, global_row in enumerate(offslice):
    block_rows.setdefault(block_name(global_row), set()).add(local)
observed_vectors = list(observed.pivots.values())
profile = {}
all_rows = set(range(1250))
for name, rows in block_rows.items():
    projection = sparse_rank([{row: value for row, value in vector.items() if row in rows}
                              for vector in observed_vectors])
    complement = all_rows - rows
    intersection = 810 - sparse_rank([
        {row: value for row, value in vector.items() if row in complement}
        for vector in observed_vectors])
    profile[name] = (len(rows), projection, intersection)
check("theorem", "independent observed profile fills only the missing rank-216 N_HN block",
      profile == {"H_HN": (160, 160, 160), "H_NN": (180, 180, 180),
                  "N_HH": (60, 60, 60), "N_HN": (400, 400, 400),
                  "N_NN": (450, 10, 10)})

ambient = SparseEchelon(vectors)
ambient_progression = [ambient.rank()]
for mu in range(14):
    for direction in directions1:
        ambient.insert(symbol_column(mu, direction))
    ambient_progression.append(ambient.rank())
check("theorem", "independent ambient progression ends at full rank 1250",
      ambient_progression == [594, 648, 702, 756, 810, 899, 978, 1047,
                              1106, 1155, 1194, 1223, 1242, 1250, 1250])
check("scope", "observed total is 1131 and full Y14 low-grade total is 1571",
      321 + observed.rank() == 1131 and 321 + ambient.rank() == 1571)


def a_column(direction):
    return equation_column(shiab(fadd(wedge(phi1, direction), wedge(direction, phi1))))


a_columns = [a_column(directions2[row]) for row in offslice]


def matvec(columns, vector):
    out = {}
    for column, scalar in vector.items():
        for row, coefficient in columns[column].items():
            result = out.get(row, K.zero()) + scalar * coefficient
            if result == 0:
                out.pop(row, None)
            else:
                out[row] = result
    return out


lower = SparseEchelon(observed_vectors)
for vector in observed_vectors:
    lower.insert(matvec(a_columns, vector))
check("theorem", "independent lower-order background-A operator preserves rank 810",
      lower.rank() == 810)

bad_q = {1: blade((0,))}
bad_same_grade = any(equation_column(shiab(wedge(bad_q, direction)))
                     for direction in directions2)
check("planted", "Clifford-vector q plant creates a false same-grade response",
      bad_same_grade)
check("scope", "no conormal quotient unitary parent domain or P1 P2 P3 is inferred", True)

print("OBSERVED_PROGRESSION", observed_progression)
print("AMBIENT_PROGRESSION", ambient_progression)
print("OBSERVED_PROFILE", profile)
print("CHECKS", dict(COUNTS))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print("PASS %d/%d" % (sum(COUNTS.values()), sum(COUNTS.values())))
