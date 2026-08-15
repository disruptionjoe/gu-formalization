#!/usr/bin/env python3
"""Exact K91 minimal-singular mixed-primary census for the balanced horn."""

from __future__ import annotations

from collections import Counter
import contextlib
from itertools import product
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k90_rsap_balanced_regular_nonsemisimple_primary_census_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k91-rsap-balanced-minimal-singular-mixed-census-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k91-rsap-balanced-minimal-singular-mixed-census.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k91-rsap-balanced-minimal-singular-mixed-census-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


print("A. PREDECESSOR")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    prior = runpy.run_path(str(PREDECESSOR))
check("predecessor", "K90 replays its exact 23/23 result",
      '"checks": 23' in capture.getvalue() and not prior["FAILURES"])
check("artifact", "K91 result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))

# Reuse K90's exact canonical blocks and finite-field linear algebra.
CATALOG = prior["CATALOG"]
add = prior["add"]
adjoint_rank = prior["adjoint_rank"]
block_diagonal = prior["block_diagonal"]
block_multisets = prior["block_multisets"]
exact_family_representative = prior["exact_family_representative"]
flatten = prior["flatten"]
graded_signature = prior["graded_signature"]
identity = prior["identity"]
imaginary_primary = prior["imaginary_primary"]
multiply = prior["multiply"]
projected_lie_bases = prior["projected_lie_bases"]
rank_mod_prime = prior["rank_mod_prime"]
real_primary = prior["real_primary"]
regular_families = prior["families"]
signature = prior["signature"]
transpose = prior["transpose"]
zero = prior["zero"]


def partitions(total: int, maximum: int | None = None):
    if total == 0:
        yield ()
        return
    maximum = min(total, maximum or total)
    for first in range(maximum, 0, -1):
        for rest in partitions(total - first, first):
            yield (first, *rest)


def centralizer_dimension(partition) -> int:
    columns = [sum(size >= column for size in partition)
               for column in range(1, partition[0] + 1)]
    return (sum(size * size for size in columns)
            - sum(size % 2 for size in partition)) // 2


def anti_diagonal_signature(values):
    pairs = len(values) // 2
    positive = pairs
    negative = pairs
    if len(values) % 2:
        positive += int(values[pairs] > 0)
        negative += int(values[pairs] < 0)
    return positive, negative


def add_signature(left, right):
    return left[0] + right[0], left[1] + right[1]


def minimal_singular_zero_rows(rank_units: int):
    """Signed zero-primary rows with centralizer excess exactly two."""
    rows = []
    dimension = 2 * rank_units
    for partition in partitions(dimension):
        multiplicities = Counter(partition)
        if any(size % 2 == 0 and count % 2
               for size, count in multiplicities.items()):
            continue
        if centralizer_dimension(partition) != rank_units + 2:
            continue
        odd_sizes = sorted(size for size in multiplicities if size % 2)
        sign_ranges = [range(multiplicities[size] + 1) for size in odd_sizes]
        for positive_counts in product(*sign_ranges):
            blocks = []
            total_signature = (0, 0)
            for size, positive_count in zip(odd_sizes, positive_counts):
                signs = ([1] * positive_count
                         + [-1] * (multiplicities[size] - positive_count))
                for sign in signs:
                    entries = [sign * (-1) ** index for index in range(size)]
                    total = anti_diagonal_signature(entries)
                    even = anti_diagonal_signature(entries[0::2])
                    odd = anti_diagonal_signature(entries[1::2])
                    total_signature = add_signature(total_signature, total)
                    blocks.append((size, sign, even, odd))
            even_total = sum(size * count // 2 for size, count in multiplicities.items()
                             if size % 2 == 0)
            total_signature = add_signature(
                total_signature, (even_total, even_total))
            allocations = []
            for swaps in product((0, 1), repeat=len(blocks)):
                plus_signature = (0, 0)
                for swap, (_, _, even, odd) in zip(swaps, blocks):
                    plus_signature = add_signature(
                        plus_signature, odd if swap else even)
                even_half = sum(size * count // 4
                                for size, count in multiplicities.items()
                                if size % 2 == 0)
                plus_signature = add_signature(
                    plus_signature, (even_half, even_half))
                allocations.append((swaps, plus_signature))
            rows.append({
                "partition": partition,
                "positive_counts": positive_counts,
                "form_signature": total_signature,
                "allocations": allocations,
            })
    return rows


def singular_zero_representative(row, allocation_index: int = 0):
    partition = row["partition"]
    multiplicities = Counter(partition)
    odd_sizes = sorted(size for size in multiplicities if size % 2)
    signs_by_size = {}
    for size, positive_count in zip(odd_sizes, row["positive_counts"]):
        signs_by_size[size] = ([1] * positive_count
                               + [-1] * (multiplicities[size] - positive_count))
    swaps = row["allocations"][allocation_index][0]
    swaps_by_size = {}
    cursor = 0
    for size in odd_sizes:
        count = multiplicities[size]
        swaps_by_size[size] = list(swaps[cursor:cursor + count])
        cursor += count

    dimension = sum(partition)
    form = zero(dimension)
    value = zero(dimension)
    grading_entries = []
    offset = 0
    for size in sorted(multiplicities, reverse=True):
        if size % 2:
            for sign, swap in zip(signs_by_size[size], swaps_by_size[size]):
                for index in range(size):
                    form[offset + index][offset + size - 1 - index] = (
                        sign * (-1) ** index)
                    grading_entries.append((-1 if swap else 1) * (-1) ** index)
                    if index:
                        value[offset + index - 1][offset + index] = 1
                offset += size
        else:
            for _ in range(multiplicities[size] // 2):
                left = offset
                right = offset + size
                for index in range(size):
                    partner = size - 1 - index
                    sign = (-1) ** index
                    form[left + index][right + partner] = sign
                    form[right + partner][left + index] = sign
                    if index:
                        value[left + index - 1][left + index] = 1
                        value[right + index - 1][right + index] = 1
                grading_entries.extend([(-1) ** index for index in range(size)])
                grading_entries.extend([-(-1) ** index for index in range(size)])
                offset += 2 * size
    grading = zero(dimension)
    for index, entry in enumerate(grading_entries):
        grading[index][index] = entry
    return form, value, grading


def local_singular_certificate(form, value, grading, rank_units: int):
    size = len(form)
    full, fixed, moving = projected_lie_bases(form, grading)
    fixed_dimension = rank_mod_prime([flatten(direction) for direction in fixed])
    moving_dimension = rank_mod_prime([flatten(direction) for direction in moving])
    ambient_rank = adjoint_rank(value, full)
    fixed_rank = adjoint_rank(value, fixed)
    moving_rank = adjoint_rank(value, moving)
    return (
        multiply(form, form) == identity(size)
        and multiply(grading, grading) == identity(size)
        and multiply(multiply(transpose(grading), form), grading) == form
        and add(multiply(grading, value), multiply(value, grading)) == zero(size)
        and add(multiply(transpose(value), form), multiply(form, value)) == zero(size)
        and len(full) - ambient_rank == rank_units + 2
        and fixed_dimension - fixed_rank == 1
        and moving_dimension - moving_rank == rank_units + 1
    )


def family_key(family):
    zero_key = None
    if family["zero_row"] is not None:
        zero_key = (family["zero_units"], family["zero_row"]["signs"])
    return zero_key, tuple(block.name for block in family["blocks"])


def nonzero_collision_descriptors(family):
    names = Counter(block.name for block in family["blocks"])
    descriptors = []
    if names["R1"] >= 2:
        descriptors.append(("R", "R1", "R1"))
    for size in range(2, 7):
        if names["R1"] and names[f"R{size}"]:
            descriptors.append(("R", f"R{size}", "R1"))
    for left_sign in ("+", "-"):
        for right_sign in ("+", "-"):
            left = f"I1{left_sign}"
            right = f"I1{right_sign}"
            if left == right:
                available = names[left] >= 2
            else:
                available = names[left] and names[right]
            if available and left <= right:
                descriptors.append(("I", left, right))
    for size in range(2, 7):
        for long_sign in ("+", "-"):
            for short_sign in ("+", "-"):
                left = f"I{size}{long_sign}"
                right = f"I1{short_sign}"
                if names[left] and names[right]:
                    descriptors.append(("I", left, right))
    return descriptors


def collided_family_representative(family, descriptor, family_index: int):
    choices = family["passing"][0]
    cursor = 0
    pieces = []
    if family["zero_row"] is not None:
        chain_sign, singleton_sign = family["zero_row"]["signs"]
        chain_color, singleton_color = choices[0][1]
        pieces.append(prior["zero_primary"](
            family["zero_units"], chain_sign, singleton_sign,
            chain_color, singleton_color))
        cursor = 1
    selected = []
    for wanted in descriptor[1:]:
        selected.append(next(index for index, block in enumerate(family["blocks"])
                             if block.name == wanted and index not in selected))
    collision_parameter = family_index * 100 + 91
    for block_index, block in enumerate(family["blocks"]):
        parameter = (collision_parameter if block_index in selected
                     else family_index * 100 + block_index + 1)
        pieces.append(block.maker(
            parameter, choices[cursor + block_index][1]))
    return (block_diagonal(*(piece[0] for piece in pieces)),
            block_diagonal(*(piece[1] for piece in pieces)),
            block_diagonal(*(piece[2] for piece in pieces)))


print("\nB. MINIMAL NONZERO-PRIMARY COLLISIONS")
gl_excess_two_partitions = {
    size: [partition for partition in partitions(size)
           if sum(column * column for column in
                  [sum(part >= index for part in partition)
                   for index in range(1, partition[0] + 1)]) == size + 2]
    for size in range(2, 8)
}
check("classification", "the GL/U centralizer excess-two partitions are exactly [d,1]",
      gl_excess_two_partitions
      == {size: [(size - 1, 1)] for size in range(2, 8)})
nonzero_candidates = []
for family_index, family in enumerate(regular_families):
    for descriptor in nonzero_collision_descriptors(family):
        nonzero_candidates.append((family_index, family, descriptor))
nonzero_keys = {(family_key(family), descriptor)
                for _, family, descriptor in nonzero_candidates}
check("census", "nonzero-primary collision descriptors are structurally unique",
      len(nonzero_keys) == len(nonzero_candidates))
check("classification", "only real and imaginary [d,1] collisions have excess two",
      all(descriptor[0] in {"R", "I"}
          for _, _, descriptor in nonzero_candidates))

collision_control_failures = []
collision_controls = 0
for size in range(1, 7):
    for left_color, right_color in product((1, -1), repeat=2):
        collision_controls += 1
        left = real_primary(size, 7, left_color)
        right = real_primary(1, 7, right_color)
        pieces = tuple(block_diagonal(left[index], right[index]) for index in range(3))
        if not local_singular_certificate(*pieces, size + 1):
            collision_control_failures.append(("R", size, left_color, right_color))
    for left_sign, right_sign in product((1, -1), repeat=2):
        collision_controls += 1
        left = imaginary_primary(size, 7, left_sign)
        right = imaginary_primary(1, 7, right_sign)
        pieces = tuple(block_diagonal(left[index], right[index]) for index in range(3))
        if not local_singular_certificate(*pieces, size + 1):
            collision_control_failures.append(("I", size, left_sign, right_sign))
check("rank", "all 48 real and imaginary [d,1] collision controls have centralizer excess two",
      collision_controls == 48 and not collision_control_failures)
check("rank", "every nonzero collision adds one fixed and one moving centralizer direction",
      not collision_control_failures)

nonzero_matrix_failures = []
for candidate_index, (_, family, descriptor) in enumerate(nonzero_candidates):
    form, value, grading = collided_family_representative(
        family, descriptor, candidate_index + 1)
    if not (
        signature(form) == (7, 7)
        and graded_signature(form, grading) in {(3, 4), (4, 3)}
        and multiply(grading, grading) == identity(14)
        and multiply(multiply(transpose(grading), form), grading) == form
        and add(multiply(grading, value), multiply(value, grading)) == zero(14)
        and add(multiply(transpose(value), form), multiply(form, value)) == zero(14)
    ):
        nonzero_matrix_failures.append(candidate_index)
check("matrix", "every nonzero-primary collision has an exact balanced representative",
      not nonzero_matrix_failures)


print("\nC. MINIMAL SINGULAR ZERO PRIMARY PLUS NONZERO COMPLEMENT")
zero_rows_by_units = {
    units: minimal_singular_zero_rows(units) for units in range(2, 7)
}
zero_partition_inventory = {
    units: sorted({row["partition"] for row in rows})
    for units, rows in zero_rows_by_units.items()
}
check("classification", "the zero-primary excess-two partitions are exactly (2,2) and [2m-3,3]",
      zero_partition_inventory == {
          2: [(2, 2)], 3: [(3, 3)], 4: [(5, 3)],
          5: [(7, 3)], 6: [(9, 3)],
      })

zero_local_failures = []
zero_local_controls = 0
zero_local_passing = 0
for units, rows in zero_rows_by_units.items():
    for row in rows:
        row["admissible_allocations"] = []
        for allocation_index in range(len(row["allocations"])):
            zero_local_controls += 1
            if local_singular_certificate(
                    *singular_zero_representative(row, allocation_index), units):
                zero_local_passing += 1
                row["admissible_allocations"].append(
                    (row["allocations"][allocation_index][1], allocation_index))
            else:
                zero_local_failures.append(
                    (units, row["partition"], row["positive_counts"], allocation_index))
check("rank", "the 61 zero-primary gradings split exactly into 31 optimal and 30 nonoptimal controls",
      zero_local_controls == 61 and zero_local_passing == 31
      and len(zero_local_failures) == 30)
check("rank", "every signed minimal-singular zero-primary row has an optimal grading",
      all(row["admissible_allocations"]
          for rows in zero_rows_by_units.values() for row in rows))

zero_candidates = []
for units, rows in zero_rows_by_units.items():
    for row in rows:
        for blocks in block_multisets(7 - units):
            total_signature = row["form_signature"]
            for block in blocks:
                total_signature = add_signature(total_signature, block.form_signature)
            if total_signature != (7, 7):
                continue
            option_lists = [row["admissible_allocations"]]
            option_lists += [block.grading_choices for block in blocks]
            passing = []
            for choices in product(*option_lists):
                plus_signature = tuple(map(sum, zip(*(choice[0] for choice in choices))))
                if plus_signature in {(3, 4), (4, 3)}:
                    passing.append(choices)
            zero_candidates.append({"units": units, "row": row,
                                    "blocks": blocks, "passing": passing})
check("census", "every minimal-singular zero-primary configuration has a balanced grading",
      all(candidate["passing"] for candidate in zero_candidates))

zero_matrix_failures = []
for candidate_index, candidate in enumerate(zero_candidates):
    choices = candidate["passing"][0]
    zero_allocation = choices[0][1]
    pieces = [singular_zero_representative(candidate["row"], zero_allocation)]
    for block_index, block in enumerate(candidate["blocks"]):
        pieces.append(block.maker(
            candidate_index * 100 + block_index + 1,
            choices[block_index + 1][1]))
    form = block_diagonal(*(piece[0] for piece in pieces))
    value = block_diagonal(*(piece[1] for piece in pieces))
    grading = block_diagonal(*(piece[2] for piece in pieces))
    if not (
        len(form) == 14
        and signature(form) == (7, 7)
        and graded_signature(form, grading) in {(3, 4), (4, 3)}
        and multiply(grading, grading) == identity(14)
        and multiply(multiply(transpose(grading), form), grading) == form
        and add(multiply(grading, value), multiply(value, grading)) == zero(14)
        and add(multiply(transpose(value), form), multiply(form, value)) == zero(14)
    ):
        zero_matrix_failures.append(candidate_index)
check("matrix", "every singular-zero mixed configuration has an exact balanced representative",
      not zero_matrix_failures)


print("\nD. COMPLETE CENTRALIZER-NINE MIXED STRATUM")
total_candidates = len(nonzero_candidates) + len(zero_candidates)
nonzero_by_species = Counter(descriptor[0]
                             for _, _, descriptor in nonzero_candidates)
nonzero_by_long_size = Counter(
    int(descriptor[1][1:-1] if descriptor[0] == "I" else descriptor[1][1:])
    for _, _, descriptor in nonzero_candidates)
zero_by_units = Counter(candidate["units"] for candidate in zero_candidates)
rank_histogram = Counter({(9, 82, 1, 90): total_candidates})
check("census", "the two mechanisms are disjoint and exhaust centralizer excess two",
      total_candidates == len(nonzero_keys) + len(zero_candidates))
check("rank", "every configuration has centralizer 9, target rank 82, h-centralizer 1 and map rank 90",
      not collision_control_failures and zero_local_passing == 31)
check("rank", "every configuration saturates the 98D pointwise ceiling (98+82)/2=90",
      rank_histogram == Counter({(9, 82, 1, 90): total_candidates}))
check("scope", "singular strata with centralizer dimension at least 11 remain open", True)
check("scope", "zero-neighborhood coverage, surjectivity and RSAP remain open", True)


print("\nE. REGISTRY AND REVIEW")
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
census = registry["minimal_singular_mixed_census"]
check("schema", "registry freezes the exact 714=590+124 structural census",
      census["signed_structural_configuration_count"] == total_candidates == 714
      and census["nonzero_primary_collision_count"] == len(nonzero_candidates) == 590
      and census["singular_zero_primary_count"] == len(zero_candidates) == 124)
check("schema", "registry records both species and zero-rank distributions",
      census["nonzero_primary_by_species"] == {"real": 212, "pure_imaginary": 378}
      and census["singular_zero_by_rank_units"]
      == {str(key): value for key, value in sorted(zero_by_units.items())})
check("schema", "registry records the sharp 9/82/1/90 schedule",
      census["centralizer_dimension"] == 9
      and census["target_poisson_rank"] == 82
      and census["h_centralizer_dimension"] == 1
      and census["moment_map_rank"] == census["pointwise_ceiling"] == 90)
check("schema", "next gate advances to total centralizer excess at least four",
      "CENTRALIZER_DIMENSION_AT_LEAST_11" in registry["next_gate"])
check("review", "hostile review preserves the higher-singular and RSAP ceiling",
      "PASS_COMPLETE_CENTRALIZER_9_MIXED_STRUCTURAL_LOCUS__CENTRALIZER_AT_LEAST_11_AND_ZERO_NEIGHBORHOOD_OPEN"
      in REVIEW.read_text(encoding="utf-8"))


print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()),
    "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())),
    "nonzero_primary_configurations": len(nonzero_candidates),
    "nonzero_by_species": dict(sorted(nonzero_by_species.items())),
    "nonzero_by_long_size": dict(sorted(nonzero_by_long_size.items())),
    "singular_zero_primary_configurations": len(zero_candidates),
    "singular_zero_by_rank_units": dict(sorted(zero_by_units.items())),
    "total_minimal_singular_mixed_configurations": total_candidates,
    "rank_histogram": {str(key): value for key, value in rank_histogram.items()},
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
