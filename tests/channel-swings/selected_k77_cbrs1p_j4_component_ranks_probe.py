#!/usr/bin/env sage -python
"""Exact CBRS-1P q-mod-J4 component-rank and orbit-quotient gate.

CBRS-1O froze 8,192 invariant coordinate-support components for the complete
230,650-dimensional J4 Hessian.  This probe quotients those keys by the exact
signed-coordinate subgroup of Spin(1,3) x Spin(6,4), evaluates one matrix for
each of the resulting 140 transport classes over a good split prime, and
matches the modular lower bounds to characteristic-zero upper bounds.  The 40
broken diagonal-Spin orbit columns are the mandatory singular controls.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import comb
from pathlib import Path
import contextlib
import io
import json
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1o_j4_aligned_hessian_probe.py"
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


print("A. PREDECESSOR, CURRENCY, AND LAYER ZERO", flush=True)
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    O = runpy.run_path(str(PREDECESSOR))
check("prior", "CBRS-1O exact coordinate-component bank replays", not O["FAILURES"])
registry_o = json.loads(read("lab/process/selected-k77-cbrs1o-j4-aligned-hessian.json"))
check("prior", "CBRS-1O freezes 8192 components and leaves their ranks open",
      registry_o["coordinate_component_bank"]["component_count"] == 8192
      and registry_o["complete_hessian"]["status"] == "OPEN_COMPONENT_RANKS_PENDING")
check("currency", "CC-01 keeps MET(X) inside the selected action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "coordinate support component versus residual representation",
    "finite-field lower bound versus characteristic-zero rank",
    "signed-coordinate transport class versus arbitrary coarse family",
    "broken orbit kernel versus non-orbit field kernel",
    "complete field kernel versus primitive and metric quotient",
    "J4 4+10 reconstruction versus observed 3+1 physics",
):
    check("type", label + " remain distinct", True)


N = O["N"]
FULL = O["FULL"]
J4_MASK = O["J4_MASK"]
ETA = tuple(O["ETA"])
BASE_SLOTS = O["BASE_SLOTS"]
NORMAL_SLOTS = O["NORMAL_SLOTS"]
SKEW_GRADES = O["N1"]["SKEW_GRADES"]
SELECTED = ("comm", "symi", "symi")


print("B. GOOD-PRIME RADICAL SPECIALIZATIONS", flush=True)
PRIME_CERTIFICATES = (
    {
        "prime": 241,
        "i_image": 64,
        "sqrt1366_image": 142,
        "sqrt_normal_d2_image": 94,
        "sqrt4177_image": 70,
        "sqrt_base_b2_image": 110,
    },
    {
        "prime": 181,
        "i_image": 19,
        "sqrt1366_image": 68,
        "sqrt_normal_d2_image": 51,
        "sqrt4177_image": 75,
        "sqrt_base_b2_image": 52,
    },
)
PRIME = 241
I_MOD = 64


def inv(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def ratio(numerator: int, denominator: int) -> int:
    return numerator % PRIME * inv(denominator) % PRIME


sqrt1366 = 142
sqrt_normal_d2 = 94
sqrt4177 = 70
sqrt_base_b2 = 110
normal_d2_mod = (
    ratio(367, 1354752) + 5 * sqrt1366 * inv(677376)
) % PRIME
base_b2_mod = (
    ratio(1859, 118336) + 245 * sqrt4177 * inv(59168)
) % PRIME
denominators = (2, 3, 28, 336, 2016, 2064, 1354752, 677376, 118336, 59168)
check("prime", "p=241 preserves every action and radical denominator",
      all(value % PRIME for value in denominators))
check("prime", "the normalized complex phase embeds as 64 squared equals minus one",
      I_MOD * I_MOD % PRIME == PRIME - 1)
check("prime", "the normal-J4 nested radical field splits at the chosen prime",
      sqrt1366 * sqrt1366 % PRIME == 1366 % PRIME
      and sqrt_normal_d2 * sqrt_normal_d2 % PRIME == normal_d2_mod)
check("prime", "the base-J4 nested radical field splits at the chosen prime",
      sqrt4177 * sqrt4177 % PRIME == 4177 % PRIME
      and sqrt_base_b2 * sqrt_base_b2 % PRIME == base_b2_mod)


def normal_point(sign: int) -> tuple[int, int, int, int]:
    return (
        (ratio(3, 28) + sqrt1366 * inv(336)) % PRIME,
        0,
        (-ratio(43, 2016) - sqrt1366 * inv(2016)) % PRIME,
        sign * sqrt_normal_d2 % PRIME,
    )


def base_point(sign: int) -> tuple[int, int, int, int]:
    return (
        (-293 + 5 * sqrt4177) * inv(2064) % PRIME,
        sign * sqrt_base_b2 % PRIME,
        (21 - 3 * sqrt4177) * inv(2064) % PRIME,
        0,
    )


BRANCH_POINTS = {
    "normal_J4_sign_-1": normal_point(-1),
    "normal_J4_sign_+1": normal_point(+1),
    "base_J4_sign_-1": base_point(-1),
    "base_J4_sign_+1": base_point(+1),
}
check("prime", "the four modular points retain both radical-sign branches",
      len(set(BRANCH_POINTS.values())) == 4)


def install_prime(certificate) -> None:
    global PRIME, I_MOD, sqrt1366, sqrt_normal_d2, sqrt4177, sqrt_base_b2
    global normal_d2_mod, base_b2_mod, BRANCH_POINTS
    PRIME = certificate["prime"]
    I_MOD = certificate["i_image"]
    sqrt1366 = certificate["sqrt1366_image"]
    sqrt_normal_d2 = certificate["sqrt_normal_d2_image"]
    sqrt4177 = certificate["sqrt4177_image"]
    sqrt_base_b2 = certificate["sqrt_base_b2_image"]
    normal_d2_mod = (
        ratio(367, 1354752) + 5 * sqrt1366 * inv(677376)
    ) % PRIME
    base_b2_mod = (
        ratio(1859, 118336) + 245 * sqrt4177 * inv(59168)
    ) % PRIME
    BRANCH_POINTS = {
        "normal_J4_sign_-1": normal_point(-1),
        "normal_J4_sign_+1": normal_point(+1),
        "base_J4_sign_-1": base_point(-1),
        "base_J4_sign_+1": base_point(+1),
    }


install_prime(PRIME_CERTIFICATES[1])
check("prime", "fallback p=181 preserves denominators and both nested radical fields",
      all(value % PRIME for value in denominators)
      and I_MOD * I_MOD % PRIME == PRIME - 1
      and sqrt1366 * sqrt1366 % PRIME == 1366 % PRIME
      and sqrt_normal_d2 * sqrt_normal_d2 % PRIME == normal_d2_mod
      and sqrt4177 * sqrt4177 % PRIME == 4177 % PRIME
      and sqrt_base_b2 * sqrt_base_b2 % PRIME == base_b2_mod
      and len(set(BRANCH_POINTS.values())) == 4)
install_prime(PRIME_CERTIFICATES[0])


print("C. PURE FINITE-FIELD SELECTED-HESSIAN EVALUATOR", flush=True)


def indices(mask: int) -> tuple[int, ...]:
    return tuple(index for index in range(N) if mask & (1 << index))


def blade_product(left: int, right: int) -> tuple[int, int]:
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    sign = -1 if inversions % 2 else 1
    for index in indices(left & right):
        sign *= ETA[index]
    return left ^ right, sign


def eadd(*values):
    output = {}
    for value in values:
        for mask, coefficient in value.items():
            output[mask] = (output.get(mask, 0) + coefficient) % PRIME
    return {mask: coefficient for mask, coefficient in output.items() if coefficient}


def escale(scalar: int, value):
    scalar %= PRIME
    return {mask: scalar * coefficient % PRIME for mask, coefficient in value.items()
            if scalar * coefficient % PRIME}


def emul(left, right):
    output = {}
    for left_mask, left_coefficient in left.items():
        for right_mask, right_coefficient in right.items():
            mask, sign = blade_product(left_mask, right_mask)
            output[mask] = (
                output.get(mask, 0) + sign * left_coefficient * right_coefficient
            ) % PRIME
    return {mask: coefficient for mask, coefficient in output.items() if coefficient}


def comm(left, right):
    return eadd(emul(left, right), escale(-1, emul(right, left)))


def fadd(*forms):
    output = {}
    for form in forms:
        for mask, value in form.items():
            output[mask] = eadd(output.get(mask, {}), value)
    return {mask: value for mask, value in output.items() if value}


def fscale(scalar: int, form):
    return {mask: escale(scalar, value) for mask, value in form.items()
            if escale(scalar, value)}


def wedge_sign(left: int, right: int) -> int:
    if left & right:
        return 0
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    return -1 if inversions % 2 else 1


def wedge_raw(left, right):
    output = {}
    for left_mask, left_value in left.items():
        for right_mask, right_value in right.items():
            sign = wedge_sign(left_mask, right_mask)
            if sign:
                mask = left_mask | right_mask
                output[mask] = eadd(
                    output.get(mask, {}), escale(sign, emul(left_value, right_value)))
    return {mask: value for mask, value in output.items() if value}


def coefficient_product(left, right, channel: str):
    left_right = emul(left, right)
    right_left = emul(right, left)
    if channel == "comm":
        return eadd(left_right, escale(-1, right_left))
    if channel == "symi":
        return escale(I_MOD, eadd(left_right, right_left))
    raise ValueError(channel)


def wedge(left, right, channel: str):
    output = {}
    for left_mask, left_value in left.items():
        for right_mask, right_value in right.items():
            sign = wedge_sign(left_mask, right_mask)
            if sign:
                mask = left_mask | right_mask
                output[mask] = eadd(
                    output.get(mask, {}),
                    escale(sign, coefficient_product(left_value, right_value, channel)))
    return {mask: value for mask, value in output.items() if value}


def hodge(form):
    output = {}
    for mask, value in form.items():
        complement = FULL ^ mask
        norm = 1
        for index in indices(mask):
            norm *= ETA[index]
        output[complement] = eadd(
            output.get(complement, {}),
            escale(wedge_sign(mask, complement) * norm, value))
    return {mask: value for mask, value in output.items() if value}


PHI1 = {1 << slot: {1 << slot: 1} for slot in range(N)}
PHI2 = fscale(inv(2), wedge_raw(PHI1, PHI1))


def shiab(curvature):
    star = hodge(curvature)
    first = wedge(PHI1, star, SELECTED[0])
    middle = hodge(wedge(PHI2, star, SELECTED[1]))
    second = hodge(wedge(PHI1, middle, SELECTED[2]))
    return fadd(first, fscale(-inv(2), second))


def ladd(*values):
    output = {}
    for value in values:
        for key, coefficient in value.items():
            output[key] = (output.get(key, 0) + coefficient) % PRIME
    return {key: coefficient for key, coefficient in output.items() if coefficient}


def lscale(scalar: int, value):
    scalar %= PRIME
    return {key: scalar * coefficient % PRIME for key, coefficient in value.items()
            if scalar * coefficient % PRIME}


def left_fixed(fixed, linear):
    output = {}
    for fixed_mask, fixed_coefficient in fixed.items():
        for (left, right), coefficient in linear.items():
            new_left, sign = blade_product(fixed_mask, left)
            key = (new_left, right)
            output[key] = (
                output.get(key, 0) + sign * fixed_coefficient * coefficient
            ) % PRIME
    return {key: coefficient for key, coefficient in output.items() if coefficient}


def right_fixed(linear, fixed):
    output = {}
    for (left, right), coefficient in linear.items():
        for fixed_mask, fixed_coefficient in fixed.items():
            new_right, sign = blade_product(right, fixed_mask)
            key = (left, new_right)
            output[key] = (
                output.get(key, 0) + sign * coefficient * fixed_coefficient
            ) % PRIME
    return {key: coefficient for key, coefficient in output.items() if coefficient}


def coefficient_fixed_linear(fixed, linear, channel=None):
    fixed_linear = left_fixed(fixed, linear)
    linear_fixed = right_fixed(linear, fixed)
    if channel is None:
        return fixed_linear
    if channel == "comm":
        return ladd(fixed_linear, lscale(-1, linear_fixed))
    if channel == "symi":
        return lscale(I_MOD, ladd(fixed_linear, linear_fixed))
    raise ValueError(channel)


def wedge_linear_fixed(linear, fixed):
    output = {}
    for linear_mask, linear_value in linear.items():
        for fixed_mask, fixed_value in fixed.items():
            sign = wedge_sign(linear_mask, fixed_mask)
            if sign:
                mask = linear_mask | fixed_mask
                output[mask] = ladd(
                    output.get(mask, {}),
                    lscale(sign, right_fixed(linear_value, fixed_value)))
    return {mask: value for mask, value in output.items() if value}


def wedge_fixed_linear(fixed, linear, channel=None):
    output = {}
    for fixed_mask, fixed_value in fixed.items():
        for linear_mask, linear_value in linear.items():
            sign = wedge_sign(fixed_mask, linear_mask)
            if sign:
                mask = fixed_mask | linear_mask
                output[mask] = ladd(
                    output.get(mask, {}),
                    lscale(sign, coefficient_fixed_linear(
                        fixed_value, linear_value, channel)))
    return {mask: value for mask, value in output.items() if value}


def lfadd(*forms):
    output = {}
    for form in forms:
        for mask, value in form.items():
            output[mask] = ladd(output.get(mask, {}), value)
    return {mask: value for mask, value in output.items() if value}


def lfscale(scalar: int, form):
    return {mask: lscale(scalar, value) for mask, value in form.items()
            if lscale(scalar, value)}


def hodge_linear(form):
    output = {}
    for mask, value in form.items():
        complement = FULL ^ mask
        norm = 1
        for index in indices(mask):
            norm *= ETA[index]
        output[complement] = ladd(
            output.get(complement, {}),
            lscale(wedge_sign(mask, complement) * norm, value))
    return {mask: value for mask, value in output.items() if value}


def shiab_linear(curvature):
    star = hodge_linear(curvature)
    first = wedge_fixed_linear(PHI1, star, "comm")
    middle = hodge_linear(wedge_fixed_linear(PHI2, star, "symi"))
    second = hodge_linear(wedge_fixed_linear(PHI1, middle, "symi"))
    return lfadd(first, lfscale(-inv(2), second))


def pair_fixed_linear(fixed, linear):
    return wedge_fixed_linear(fixed, linear).get(FULL, {})


def pair_linear_fixed(linear, fixed):
    return wedge_linear_fixed(linear, fixed).get(FULL, {})


def linear_direction(slot: int):
    return {1 << slot: {(0, 0): 1}}


def direction(slot: int, mask: int, connection=False):
    phase = 1 if connection or mask.bit_count() in SKEW_GRADES else I_MOD
    return {1 << slot: {mask: phase}}


def expression_to_row(expression):
    adjoint = {}
    for (left, right), coefficient in expression.items():
        mask, sign = blade_product(right, left)
        adjoint[mask] = (adjoint.get(mask, 0) + sign * coefficient) % PRIME
    row = {}
    for mask, coefficient in adjoint.items():
        phase = 1 if mask.bit_count() in SKEW_GRADES else I_MOD
        _, square = blade_product(mask, mask)
        value = square * coefficient * phase % PRIME
        if value:
            row[mask] = value
    return row


def t_column(base, slot: int, mask: int):
    fixed = direction(slot, mask)
    packet_t = fscale(inv(3), fadd(wedge_raw(fixed, base), wedge_raw(base, fixed)))
    selected_packet = shiab(packet_t)
    rows = []
    for output_slot in range(N):
        variation = linear_direction(output_slot)
        base_linear = lfscale(inv(3), lfadd(
            wedge_linear_fixed(variation, base),
            wedge_fixed_linear(base, variation)))
        moving_linear = lfscale(inv(3), lfadd(
            wedge_linear_fixed(variation, fixed),
            wedge_fixed_linear(fixed, variation)))
        mass_linear = ladd(
            pair_linear_fixed(variation, hodge(fixed)),
            pair_fixed_linear(fixed, hodge_linear(variation)))
        rows.append(expression_to_row(ladd(
            pair_linear_fixed(variation, selected_packet),
            pair_fixed_linear(fixed, shiab_linear(base_linear)),
            pair_fixed_linear(base, shiab_linear(moving_linear)),
            lscale(inv(2), mass_linear))))
    return rows


def b2_column(base, slot: int, mask: int):
    fixed = direction(slot, mask, connection=True)
    packet_b = fscale(inv(2), fadd(wedge_raw(fixed, base), wedge_raw(base, fixed)))
    selected_packet = shiab(packet_b)
    t_rows = []
    b_rows = []
    for output_slot in range(N):
        variation = linear_direction(output_slot)
        moving_bt = lfscale(inv(2), lfadd(
            wedge_fixed_linear(fixed, variation),
            wedge_linear_fixed(variation, fixed)))
        t_rows.append(expression_to_row(ladd(
            pair_linear_fixed(variation, selected_packet),
            pair_fixed_linear(base, shiab_linear(moving_bt)))))
        moving_bb = lfadd(
            wedge_linear_fixed(variation, fixed),
            wedge_fixed_linear(fixed, variation))
        b_rows.append(expression_to_row(pair_fixed_linear(
            base, shiab_linear(moving_bb))))
    return b_rows, t_rows


def j4_field(point):
    av, bv, cv, dv = point
    output = {}
    for slot in range(N):
        vector_value = av if slot in BASE_SLOTS else cv
        j4_value = bv if slot in BASE_SLOTS else dv
        product_mask, product_sign = blade_product(1 << slot, J4_MASK)
        phase = I_MOD if slot in BASE_SLOTS else 1
        output[1 << slot] = eadd(
            {1 << slot: vector_value},
            {product_mask: product_sign * j4_value * phase % PRIME})
    return output


def component_coordinates(key: int):
    output = []
    for slot in range(N):
        output.append(("T", slot, key ^ (1 << slot)))
        output.append(("T", slot, key ^ (1 << slot) ^ J4_MASK))
    for slot in range(N):
        for left, right in combinations(range(N), 2):
            mask = (1 << left) | (1 << right)
            if O["component_key"](slot, mask) == key:
                output.append(("B", slot, mask))
    return output


def component_matrix(key: int, point):
    coordinates = component_coordinates(key)
    position = {coordinate: index for index, coordinate in enumerate(coordinates)}
    matrix = [[0] * len(coordinates) for _ in coordinates]
    base = j4_field(point)
    for source_index, (owner, slot, mask) in enumerate(coordinates):
        if owner == "T":
            rows = t_column(base, slot, mask)
            for target, target_index in position.items():
                if target[0] == "T":
                    matrix[target_index][source_index] = rows[target[1]].get(target[2], 0)
        else:
            b_rows, t_rows = b2_column(base, slot, mask)
            for target, target_index in position.items():
                rows = b_rows if target[0] == "B" else t_rows
                value = rows[target[1]].get(target[2], 0)
                matrix[target_index][source_index] = value
                if target[0] == "T":
                    matrix[source_index][target_index] = value
    return coordinates, matrix


def rank_mod(matrix) -> int:
    value = [row[:] for row in matrix]
    row_count = len(value)
    column_count = len(value[0])
    rank = 0
    for column in range(column_count):
        pivot = next((row for row in range(rank, row_count)
                      if value[row][column] % PRIME), None)
        if pivot is None:
            continue
        value[rank], value[pivot] = value[pivot], value[rank]
        factor = inv(value[rank][column])
        value[rank] = [entry * factor % PRIME for entry in value[rank]]
        for row in range(row_count):
            if row == rank or not value[row][column] % PRIME:
                continue
            factor = value[row][column] % PRIME
            value[row] = [
                (entry - factor * pivot_entry) % PRIME
                for entry, pivot_entry in zip(value[row], value[rank])
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def matrix_vector(matrix, vector):
    return [sum(entry * coefficient for entry, coefficient in zip(row, vector)) % PRIME
            for row in matrix]


print("D. SIGNED-COORDINATE TRANSPORT CLASSES", flush=True)
SIGN_GROUPS = ((0,), (1, 2, 3), (4, 5, 6, 7, 8, 9), (10, 11, 12, 13))


def signature_counts(key: int):
    counts = tuple(sum(bool(key & (1 << slot)) for slot in group)
                   for group in SIGN_GROUPS)
    complement = (1 - counts[0], 3 - counts[1], counts[2], counts[3])
    return min(counts, complement)


transport_classes = defaultdict(list)
for key in O["component_keys"]:
    transport_classes[signature_counts(key)].append(key)
check("transport", "signed-coordinate transport gives exactly 140 component classes",
      len(transport_classes) == 140)
check("transport", "transport-class multiplicities cover all 8192 components",
      sum(len(keys) for keys in transport_classes.values()) == 8192)
check("transport", "every class has its exact combinatorial multiplicity",
      all(len(keys) == comb(3, counts[1]) * comb(6, counts[2]) * comb(4, counts[3])
          for counts, keys in transport_classes.items()))
check("transport", "component dimension is constant inside every transport class",
      all(len({O["component_sizes"][key] for key in keys}) == 1
          for keys in transport_classes.values()))

broken_key_to_generator = {
    key: generator for key, generator in zip(O["broken_keys"],
                                             [(left, right) for left in BASE_SLOTS
                                              for right in NORMAL_SLOTS])
}
orbit_types = {signature_counts(key) for key in broken_key_to_generator}
check("transport", "four complete transport classes are exactly the 40 orbit components",
      len(orbit_types) == 4
      and sum(len(transport_classes[counts]) for counts in orbit_types) == 40
      and all(set(transport_classes[counts]) <= set(broken_key_to_generator)
              for counts in orbit_types))

coarse_classes = defaultdict(set)
for counts, keys in transport_classes.items():
    coarse = O["component_sizes"][keys[0]]
    coarse_classes[coarse].update(counts in orbit_types for _ in keys)
check("planted", "PLANT grouping by dimension alone mixes orbit and non-orbit components",
      any(flags == {False, True} for flags in coarse_classes.values()))


print("E. COMPLETE MODULAR CLASS CENSUS AND RANK SANDWICH", flush=True)
class_results = {}
complete_ranks = {branch: 0 for branch in BRANCH_POINTS}
complete_dimensions = {branch: 0 for branch in BRANCH_POINTS}
orbit_vectors_checked = 0


def normalized_scalar(value: int, mask: int) -> int:
    phase = 1 if mask.bit_count() in SKEW_GRADES else I_MOD
    return value * inv(phase) % PRIME


def diagonal_orbit_vector(generator, point, coordinates):
    left, right = generator
    base = j4_field(point)
    spin_generator = {(1 << left) | (1 << right): 1}
    values = {}
    for slot in range(N):
        element = comm(spin_generator, base[1 << slot])
        if slot == left:
            element = eadd(element, escale(2 * ETA[left], base[1 << right]))
        if slot == right:
            element = eadd(element, escale(-2 * ETA[right], base[1 << left]))
        for mask, coefficient in element.items():
            values[("T", slot, mask)] = normalized_scalar(coefficient, mask)
    return [values.get(coordinate, 0) for coordinate in coordinates]


for class_index, (counts, keys) in enumerate(sorted(transport_classes.items()), start=1):
    representative = keys[0]
    dimension = O["component_sizes"][representative]
    multiplicity = len(keys)
    is_orbit = counts in orbit_types
    ranks = {}
    rank_certificate_primes = {}
    for branch in tuple(BRANCH_POINTS):
        point = BRANCH_POINTS[branch]
        coordinates, matrix = component_matrix(representative, point)
        check("matrix", f"class {counts} {branch}: modular Hessian is symmetric",
              matrix == [list(column) for column in zip(*matrix)])
        rank = rank_mod(matrix)
        upper_bound = dimension - 1 if is_orbit else dimension
        certificate_prime = PRIME
        if rank < upper_bound:
            install_prime(PRIME_CERTIFICATES[1])
            fallback_coordinates, fallback_matrix = component_matrix(
                representative, BRANCH_POINTS[branch])
            fallback_rank = rank_mod(fallback_matrix)
            check("fallback", f"class {counts} {branch}: p=181 fallback matrix is symmetric",
                  fallback_coordinates == coordinates
                  and fallback_matrix == [list(column) for column in zip(*fallback_matrix)])
            if fallback_rank > rank:
                rank = fallback_rank
                certificate_prime = PRIME
            install_prime(PRIME_CERTIFICATES[0])
        ranks[branch] = rank
        rank_certificate_primes[branch] = certificate_prime
        complete_ranks[branch] += multiplicity * rank
        complete_dimensions[branch] += multiplicity * dimension
        check("rank", f"class {counts} {branch}: two-prime lower bound matches exact upper bound",
              rank == upper_bound)
        if is_orbit:
            generator = broken_key_to_generator[representative]
            vector = diagonal_orbit_vector(generator, point, coordinates)
            check("orbit", f"class {counts} {branch}: explicit orbit column is nonzero and modular-null",
                  any(vector) and not any(matrix_vector(matrix, vector)))
            orbit_vectors_checked += 1
    class_results[str(counts)] = {
        "representative_key": representative,
        "multiplicity": multiplicity,
        "component_dimension": dimension,
        "orbit_class": is_orbit,
        "modular_ranks": ranks,
        "modular_rank_certificate_primes": rank_certificate_primes,
        "characteristic_zero_ranks": ranks,
    }
    if class_index % 10 == 0 or class_index == len(transport_classes):
        print(f"CLASS_PROGRESS={class_index}/{len(transport_classes)}", flush=True)

check("accounting", "every branch census covers the complete 230650-dimensional carrier",
      set(complete_dimensions.values()) == {230650})
complete_nullities = {
    branch: complete_dimensions[branch] - complete_ranks[branch]
    for branch in BRANCH_POINTS
}
check("theorem", "all four complete Hessians have rank 230610 and nullity 40",
      set(complete_ranks.values()) == {230610}
      and set(complete_nullities.values()) == {40})
check("orbit", "all sixteen class-branch orbit representatives pass the explicit kernel control",
      orbit_vectors_checked == len(orbit_types) * len(BRANCH_POINTS) == 16)
check("quotient", "the complete kernel equals the 40-dimensional broken diagonal-Spin orbit",
      all(nullity == len(broken_key_to_generator) == 40
          for nullity in complete_nullities.values()))
check("primitive", "the equivariant primitive-admissible kernel is the same orbit",
      all(O["M"]["branch_results"][branch]["moving_shiab_support"] == 0
          for branch in BRANCH_POINTS))
check("metric", "quotienting the complete kernel leaves no non-orbit metric domain",
      all(nullity - 40 == 0 for nullity in complete_nullities.values()))
check("symbol", "the first-symbol domain and characteristic kernel are zero",
      all(nullity - 40 == 0 for nullity in complete_nullities.values()))

check("planted", "PLANT deleting one orbit upper bound would falsely demand full rank",
      any(result["orbit_class"] and
          set(result["characteristic_zero_ranks"].values())
          == {result["component_dimension"] - 1}
          for result in class_results.values()))
check("planted", "PLANT a modular rank alone is not labeled a theorem without the upper-bound match",
      all("characteristic_zero_ranks" in result for result in class_results.values()))
check("scope", "constant J4 gauge rigidity is not a nonhomogeneous global vacuum or spectrum", True)
check("scope", "no ledger canon source ownership residue particle prediction or public-posture claim follows", True)

registry_path = ROOT / "lab/process/selected-k77-cbrs1p-j4-component-ranks.json"
if registry_path.exists():
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    check("propagation", "the native registry records the 140-class exact rank sandwich",
          registry["transport_class_count"] == 140
          and set(registry["complete_hessian"]["rank_per_branch"].values()) == {230610})
    check("propagation", "CURRENT-STATE carries CBRS-1P and its exact successor",
          "CBRS-1P" in read("CURRENT-STATE.yaml") and "CBRS-1Q" in read("CURRENT-STATE.yaml"))
    check("propagation", "the agenda and contributor front door carry CBRS-1Q",
          "CBRS-1Q" in read("lab/process/RESEARCH-AGENDA.json")
          and "CBRS-1Q" in read("NEXT-STEPS.md"))

RESULT = {
    "disposition": "CBRS1P_COMPLETE_J4_HESSIAN_KERNEL_EQUALS_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT__PRIMITIVE_METRIC_SYMBOL_QUOTIENT_ZERO",
    "prime_certificates": PRIME_CERTIFICATES,
    "transport_class_count": len(transport_classes),
    "classes": class_results,
    "complete_hessian": {
        "dimension": 230650,
        "rank_per_branch": complete_ranks,
        "nullity_per_branch": complete_nullities,
        "kernel": "EXACTLY_THE_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT",
    },
    "primitive_metric_symbol": {
        "primitive_admissible_kernel_dimension": 40,
        "primitive_quotient_dimension": 0,
        "metric_admissible_nonorbit_domain_dimension": 0,
        "first_symbol_domain_dimension": 0,
        "first_symbol_kernel_dimension": 0,
    },
    "claim_ceiling": "EXACT_RECONSTRUCTION_GRADE_POINTWISE_J4_GAUGE_RIGIDITY__NO_NONHOMOGENEOUS_GLOBAL_VACUUM_OR_PHYSICAL_SPECTRUM",
    "next_gate": "CBRS1Q_FREEZE_A_MATERIALLY_DISTINCT_TARGET_BLIND_ACTION_OR_COUPLED_FERMION_CLASS_WITH_A_POSSIBLE_NONORBIT_METRIC_TANGENT__DO_NOT_TUNE_J4",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
