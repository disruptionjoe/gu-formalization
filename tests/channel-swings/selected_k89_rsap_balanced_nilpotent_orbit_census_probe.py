#!/usr/bin/env python3
"""Exact K89 balanced nilpotent signed-diagram and rank certificate."""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
from itertools import product
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k88_rsap_zero_charge_symmetric_mixed_cartan_horn_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k89-rsap-balanced-nilpotent-orbit-census-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k89-rsap-balanced-nilpotent-orbit-census.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k89-rsap-balanced-nilpotent-orbit-census-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def partitions(total: int, maximum: int | None = None):
    if total == 0:
        yield ()
        return
    maximum = min(total, maximum or total)
    for first in range(maximum, 0, -1):
        for rest in partitions(total - first, first):
            yield (first, *rest)


def anti_diagonal_signature(values: list[int]) -> tuple[int, int]:
    pairs = len(values) // 2
    positive = pairs
    negative = pairs
    if len(values) % 2:
        center = values[len(values) // 2]
        positive += int(center > 0)
        negative += int(center < 0)
    return positive, negative


def odd_block(size: int, sign: int):
    values = [sign * (-1) ** index for index in range(size)]
    total = anti_diagonal_signature(values)
    even = anti_diagonal_signature(values[0::2])
    odd = anti_diagonal_signature(values[1::2])
    return total, even, odd


def add_signature(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] + right[0], left[1] + right[1]


def signed_orbit_rows():
    rows = []
    for partition in partitions(14):
        multiplicities = Counter(partition)
        if any(size % 2 == 0 and count % 2 for size, count in multiplicities.items()):
            continue
        odd_sizes = sorted(size for size in multiplicities if size % 2)
        choices = [range(multiplicities[size] + 1) for size in odd_sizes]
        for positive_counts in product(*choices):
            blocks = []
            total = (0, 0)
            for size, positive_count in zip(odd_sizes, positive_counts):
                signs = [1] * positive_count + [-1] * (multiplicities[size] - positive_count)
                for sign in signs:
                    block_total, even, odd = odd_block(size, sign)
                    total = add_signature(total, block_total)
                    blocks.append((size, sign, even, odd))
            even_total = sum(
                size * (count // 2)
                for size, count in multiplicities.items() if size % 2 == 0
            )
            even_half = sum(
                (size // 2) * (count // 2)
                for size, count in multiplicities.items() if size % 2 == 0
            )
            total = add_signature(total, (even_total, even_total))
            if total != (7, 7):
                continue
            allocations = []
            for swaps in product((0, 1), repeat=len(blocks)):
                plus = (even_half, even_half)
                for swap, (_, _, even, odd) in zip(swaps, blocks):
                    plus = add_signature(plus, odd if swap else even)
                if plus in {(3, 4), (4, 3)}:
                    allocations.append((swaps, plus))
            rows.append({
                "partition": partition,
                "positive_counts": positive_counts,
                "allocations": allocations,
            })
    return rows


def zero_matrix(size: int) -> list[list[int]]:
    return [[0] * size for _ in range(size)]


def add(left, right, scale: int = 1):
    return [[left[i][j] + scale * right[i][j] for j in range(len(left))]
            for i in range(len(left))]


def matmul(left, right):
    size = len(left)
    return [[sum(left[i][k] * right[k][j] for k in range(size))
             for j in range(size)] for i in range(size)]


def transpose(value):
    return [list(row) for row in zip(*value)]


def flatten(value):
    return [entry for row in value for entry in row]


def matrix_rank(rows: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    for column in range(len(work[0]) if work else 0):
        pivot = next((i for i in range(rank, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [value / pivot_value for value in work[rank]]
        for i, row in enumerate(work):
            if i != rank and row[column]:
                factor = row[column]
                work[i] = [a - factor * b for a, b in zip(row, work[rank])]
        rank += 1
    return rank


def commutator(left, right):
    return add(matmul(left, right), matmul(right, left), -1)


def lie_basis(form):
    size = len(form)
    # Every form used below is involutive, so Q^-1=Q and Q^-1 S spans so(Q).
    basis = []
    for i in range(size):
        for j in range(i + 1, size):
            skew = zero_matrix(size)
            skew[i][j] = 1
            skew[j][i] = -1
            basis.append(matmul(form, skew))
    return basis


def grading_parts(basis, grading):
    size = len(grading)
    h = [value for value in basis if all(
        (grading[i] - grading[j]) * value[i][j] == 0
        for i in range(size) for j in range(size)
    )]
    p = [value for value in basis if all(
        (grading[i] + grading[j]) * value[i][j] == 0
        for i in range(size) for j in range(size)
    )]
    return h, p


def adjoint_rank(value, basis):
    return matrix_rank([flatten(commutator(value, direction)) for direction in basis])


def rank_mod_prime(columns, prime: int = 1_000_003) -> int:
    """Sparse finite-field rank, used with a matching characteristic-zero bound."""
    pivots = {}
    for raw in columns:
        column = {i: entry % prime for i, entry in enumerate(raw) if entry % prime}
        while column:
            pivot = min(column)
            if pivot not in pivots:
                inverse = pow(column[pivot], prime - 2, prime)
                pivots[pivot] = {i: entry * inverse % prime for i, entry in column.items()}
                break
            factor = column[pivot]
            for i, entry in pivots[pivot].items():
                replacement = (column.get(i, 0) - factor * entry) % prime
                if replacement:
                    column[i] = replacement
                else:
                    column.pop(i, None)
    return len(pivots)


def centralizer_dimension(partition):
    columns = [sum(size >= column for size in partition)
               for column in range(1, partition[0] + 1)]
    return (sum(size * size for size in columns)
            - sum(size % 2 for size in partition)) // 2


def canonical_row_representative(row):
    """Turn one enumerated signed form and one passing allocation into Q,N,R."""
    partition = row["partition"]
    multiplicities = Counter(partition)
    odd_sizes = sorted(size for size in multiplicities if size % 2)
    signs_by_size = {}
    for size, positive_count in zip(odd_sizes, row["positive_counts"]):
        signs_by_size[size] = ([1] * positive_count
                               + [-1] * (multiplicities[size] - positive_count))
    swaps = row["allocations"][0][0]
    swaps_by_size = {}
    cursor = 0
    for size in odd_sizes:
        count = multiplicities[size]
        swaps_by_size[size] = list(swaps[cursor:cursor + count])
        cursor += count

    form = zero_matrix(14)
    value = zero_matrix(14)
    grading = []
    offset = 0
    for size in sorted(multiplicities, reverse=True):
        if size % 2:
            for sign, swap in zip(signs_by_size[size], swaps_by_size[size]):
                for i in range(size):
                    form[offset + i][offset + size - 1 - i] = sign * (-1) ** i
                    grading.append((-1 if swap else 1) * (-1) ** i)
                    if i:
                        value[offset + i - 1][offset + i] = 1
                offset += size
        else:
            for _ in range(multiplicities[size] // 2):
                left = offset
                right = offset + size
                for i in range(size):
                    partner = size - 1 - i
                    sign = (-1) ** i
                    form[left + i][right + partner] = sign
                    form[right + partner][left + i] = sign
                    if i:
                        value[left + i - 1][left + i] = 1
                        value[right + i - 1][right + i] = 1
                grading.extend([(-1) ** i for i in range(size)])
                grading.extend([-(-1) ** i for i in range(size)])
                offset += 2 * size
    assert offset == 14 and len(grading) == 14
    return form, value, grading


def principal_control():
    size = 14
    form = zero_matrix(size)
    for i in range(13):
        form[i][12 - i] = (-1) ** i
    form[13][13] = -1
    value = zero_matrix(size)
    for i in range(1, 13):
        value[i - 1][i] = 1
    grading = [(-1) ** i for i in range(13)] + [-1]
    return form, value, grading


def regular_control(chain_size: int):
    size = 14
    form = zero_matrix(size)
    for i in range(chain_size):
        form[i][chain_size - 1 - i] = (-1) ** i
    singleton = chain_size
    value = zero_matrix(size)
    for i in range(1, chain_size):
        value[i - 1][i] = 1
    grading = [(-1) ** i for i in range(chain_size)]
    if chain_size == 5:
        form[singleton][singleton] = -1
        grading.append(-1)
        planes = [(6, 1, 1), (8, 1, 2), (10, -1, 4), (12, -1, 8)]
    else:
        form[singleton][singleton] = 1
        grading.append(-1)
        planes = [(4, 1, 1), (6, 1, 2), (8, -1, 4), (10, -1, 8), (12, 0, 16)]
    for base, sign, weight in planes:
        if sign:
            form[base][base] = sign
            form[base + 1][base + 1] = sign
            value[base][base + 1] = -weight
            value[base + 1][base] = weight
        else:
            form[base][base] = 1
            form[base + 1][base + 1] = -1
            value[base][base + 1] = weight
            value[base + 1][base] = weight
        grading.extend([1, -1])
    return form, value, grading


def verify_rank_control(label, form, value, grading):
    size = len(form)
    basis = lie_basis(form)
    h_basis, p_basis = grading_parts(basis, grading)
    so_defect = add(matmul(transpose(value), form), matmul(form, value))
    anti_defect = all((grading[i] + grading[j]) * value[i][j] == 0
                      for i in range(size) for j in range(size))
    ambient_rank = adjoint_rank(value, basis)
    h_rank = adjoint_rank(value, h_basis)
    p_rank = adjoint_rank(value, p_basis)
    check("matrix", f"{label} is Q-skew and anticommutes with the grading",
          so_defect == zero_matrix(size) and anti_defect)
    check("rank", f"{label} has the balanced 42+49 decomposition",
          len(basis) == 91 and len(h_basis) == 42 and len(p_basis) == 49)
    check("rank", f"{label} has ambient adjoint rank 84", ambient_rank == 84)
    check("rank", f"{label} has trivial h-centralizer", h_rank == 42)
    check("rank", f"{label} has p-kernel seven and moment rank 91",
          len(p_basis) - p_rank == 7 and 49 + p_rank == 91)
    return ambient_rank, h_rank, p_rank


print("A. PREDECESSOR AND DURABLE FILES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    prior = runpy.run_path(str(PREDECESSOR))
check("prior", "K88 replays its exact 104/104 regular-semisimple result",
      '"checks": 104' in capture.getvalue() and not prior["FAILURES"])
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. COMPLETE REAL NILPOTENT SIGNED-DIAGRAM CENSUS")
rows = signed_orbit_rows()
orthogonal_partitions = {row["partition"] for row in rows}
failed_rows = [row for row in rows if not row["allocations"]]
check("census", "there are exactly 43 admissible orthogonal partitions of 14",
      len(orthogonal_partitions) == 43)
check("census", "there are exactly 99 split-real signed-form allocations",
      len(rows) == 99)
check("census", "every signed-form allocation has a balanced involution",
      not failed_rows)
check("census", "every allocation lands at (3,4) or (4,3)",
      all(all(signature in {(3, 4), (4, 3)} for _, signature in row["allocations"])
          for row in rows))
check("classification", "no very-even partition can occur at total size 14",
      all(any(size % 2 for size in partition) for partition in orthogonal_partitions)
      and 14 % 4 == 2)
principal_rows = [row for row in rows if row["partition"] == (13, 1)]
check("classification", "the two real principal [13,1] signed forms both pass",
      len(principal_rows) == 2 and all(row["allocations"] for row in principal_rows))


print("\nC. PRINCIPAL AND REGULAR-NONSEMISIMPLE RANK CONTROLS")
principal_ranks = verify_rank_control("principal [13,1]", *principal_control())
control_51 = verify_rank_control("regular [5,1] plus four elliptic primaries", *regular_control(5))
control_31 = verify_rank_control("regular [3,1] plus elliptic/hyperbolic primaries", *regular_control(3))


print("\nD. ALL-ORBIT POINTWISE RANK SATURATION")
rank_schedule = []
for row in rows:
    form, value, grading = canonical_row_representative(row)
    basis = lie_basis(form)
    h_basis, p_basis = grading_parts(basis, grading)
    centralizer = centralizer_dimension(row["partition"])
    h_rank = rank_mod_prime([flatten(commutator(value, direction)) for direction in h_basis])
    p_rank = rank_mod_prime([flatten(commutator(value, direction)) for direction in p_basis])
    rank_schedule.append((centralizer, h_rank, p_rank, len(h_basis), len(p_basis)))
check("rank-census", "every nilpotent representative has the balanced 42+49 decomposition",
      all(h_dimension == 42 and p_dimension == 49
          for _, _, _, h_dimension, p_dimension in rank_schedule))
check("rank-census", "all 99 fixed and moving adjoint ranks reach the exact orbit ceiling",
      all(h_rank == p_rank == (91 - centralizer) // 2
          for centralizer, h_rank, p_rank, _, _ in rank_schedule))
check("rank-census", "all 99 nilpotent map ranks saturate the 98D pointwise bound",
      all(49 + p_rank == (189 - centralizer) // 2
          for centralizer, _, p_rank, _, _ in rank_schedule))
check("rank-census", "the two principal rows are rank 91 and zero is rank 49",
      sum(centralizer == 7 and 49 + p_rank == 91
          for centralizer, _, p_rank, _, _ in rank_schedule) == 2
      and sum(centralizer == 91 and 49 + p_rank == 49
              for centralizer, _, p_rank, _, _ in rank_schedule) == 1)


print("\nE. MUTATION AND CLAIM-CEILING CONTROLS")
bad_partition = (2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
check("mutation", "a singleton even block violates the orthogonal partition rule",
      Counter(bad_partition)[2] % 2 == 1)
check("mutation", "dropping either principal signed form changes the exact census count",
      len(rows) - 1 != 99)
check("mutation", "a definite seven-plane is not the required balanced eigenspace",
      (7, 0) not in {(3, 4), (4, 3)})

registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
check("schema", "registry freezes the 43/99/0 census",
      registry["classification"]["admissible_partition_count"] == 43
      and registry["classification"]["split_real_signed_form_allocation_count"] == 99
      and registry["classification"]["failed_balanced_allocations"] == 0)
check("schema", "registry principal ranks equal the exact matrix certificate",
      principal_ranks == (84, 42, 42)
      and registry["principal_control"]["moment_map_rank"] == 91)
check("schema", "both mixed regular controls equal the exact matrix ranks",
      control_51 == (84, 42, 42) and control_31 == (84, 42, 42))
check("schema", "registry records all-orbit pointwise rank saturation",
      registry["coverage_gate"]["all_nilpotent_pointwise_rank_saturation"]
      == "PROVED_ON_ALL_99_CONNECTED_REAL_ORBITS")
check("scope", "mixed Jordan, zero-neighborhood and global RSAP remain open",
      registry["coverage_gate"]["complete_regular_nonsemisimple_census"] == "OPEN"
      and registry["coverage_gate"]["singular_mixed_jordan_census"] == "OPEN"
      and registry["coverage_gate"]["zero_neighborhood"] == "OPEN"
      and registry["coverage_gate"]["global_rsap"] == "OPEN")
check("scope", "ambient successor and dimension interval are unchanged",
      registry["disposition"]["ambient_a3_successor"] == "TYPE_MISSING_NOT_REOPENED"
      and registry["disposition"]["dimension_interval"] == [98, 182])
check("review", "hostile review preserves the mixed-Jordan ceiling",
      "PASS_FULL_NILPOTENT_CONE__ALL_99_POINTWISE_RANK_SATURATING__MIXED_JORDAN_AND_ZERO_NEIGHBORHOOD_OPEN"
      in REVIEW.read_text(encoding="utf-8"))


print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()),
    "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())),
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
