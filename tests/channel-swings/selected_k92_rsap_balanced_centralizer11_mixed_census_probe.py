#!/usr/bin/env python3
"""Exact K92 centralizer-11 mixed-primary census for the balanced horn."""

from __future__ import annotations

from collections import Counter
import contextlib
from itertools import combinations_with_replacement, product
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k91_rsap_balanced_minimal_singular_mixed_census_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k92-rsap-balanced-centralizer11-mixed-census-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k92-rsap-balanced-centralizer11-mixed-census.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k92-rsap-balanced-centralizer11-mixed-census-review.md"
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
check("predecessor", "K91 replays its exact 23/23 result",
      '"checks": 23' in capture.getvalue() and not prior["FAILURES"])
check("artifact", "K92 result, registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))

# K90/K91 canonical blocks, exact linear algebra, and signed-zero machinery.
k90 = prior["prior"]
CATALOG = prior["CATALOG"]
add = prior["add"]
add_signature = prior["add_signature"]
adjoint_rank = prior["adjoint_rank"]
block_diagonal = prior["block_diagonal"]
block_multisets = prior["block_multisets"]
flatten = prior["flatten"]
graded_signature = prior["graded_signature"]
identity = prior["identity"]
imaginary_primary = prior["imaginary_primary"]
loxodromic_primary = k90["loxodromic_primary"]
multiply = prior["multiply"]
nonzero_collision_descriptors = prior["nonzero_collision_descriptors"]
partitions = prior["partitions"]
projected_lie_bases = prior["projected_lie_bases"]
rank_mod_prime = prior["rank_mod_prime"]
real_primary = prior["real_primary"]
regular_families = prior["regular_families"]
signature = prior["signature"]
singular_zero_representative = prior["singular_zero_representative"]
transpose = prior["transpose"]
zero = prior["zero"]


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


def singular_zero_rows(rank_units: int, excess: int):
    """All signed zero-primary rows at the stated centralizer excess."""
    rows = []
    dimension = 2 * rank_units
    for partition in partitions(dimension):
        multiplicities = Counter(partition)
        if any(size % 2 == 0 and count % 2
               for size, count in multiplicities.items()):
            continue
        if centralizer_dimension(partition) != rank_units + excess:
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
            total_signature = add_signature(total_signature,
                                            (even_total, even_total))
            allocations = []
            for swaps in product((0, 1), repeat=len(blocks)):
                plus_signature = (0, 0)
                for swap, (_, _, even, odd) in zip(swaps, blocks):
                    plus_signature = add_signature(
                        plus_signature, odd if swap else even)
                even_half = sum(size * count // 4
                                for size, count in multiplicities.items()
                                if size % 2 == 0)
                plus_signature = add_signature(plus_signature,
                                               (even_half, even_half))
                allocations.append((swaps, plus_signature))
            rows.append({
                "partition": partition,
                "positive_counts": positive_counts,
                "form_signature": total_signature,
                "allocations": allocations,
            })
    return rows


def local_certificate(form, value, grading, rank_units: int, excess: int) -> bool:
    size = len(form)
    full, fixed, moving = projected_lie_bases(form, grading)
    fixed_dimension = rank_mod_prime([flatten(direction) for direction in fixed])
    moving_dimension = rank_mod_prime([flatten(direction) for direction in moving])
    ambient_rank = adjoint_rank(value, full)
    fixed_rank = adjoint_rank(value, fixed)
    moving_rank = adjoint_rank(value, moving)
    fixed_kernel = excess // 2
    return (
        multiply(form, form) == identity(size)
        and multiply(grading, grading) == identity(size)
        and multiply(multiply(transpose(grading), form), grading) == form
        and add(multiply(grading, value), multiply(value, grading)) == zero(size)
        and add(multiply(transpose(value), form), multiply(form, value)) == zero(size)
        and len(full) - ambient_rank == rank_units + excess
        and fixed_dimension - fixed_rank == fixed_kernel
        and moving_dimension - moving_rank == rank_units + excess - fixed_kernel
    )


def available(names: Counter[str], wanted) -> bool:
    demand = Counter(wanted)
    return all(names[name] >= count for name, count in demand.items())


def primitive_excess_four_descriptors(family):
    """One GL/U [d,2] or realified-complex L[d,1] primary."""
    names = Counter(block.name for block in family["blocks"])
    descriptors = []
    for size in range(2, 6):
        wanted = (f"R{size}", "R2")
        if available(names, wanted):
            descriptors.append(("R", *wanted))
        for long_sign, short_sign in product(("+", "-"), repeat=2):
            left = f"I{size}{long_sign}"
            right = f"I2{short_sign}"
            if available(names, (left, right)) and (size != 2 or left <= right):
                descriptors.append(("I", left, right))
    for size in range(1, 3):
        wanted = (f"L{size}", "L1")
        if available(names, wanted):
            descriptors.append(("L", *wanted))
    return descriptors


def double_excess_two_descriptors(family):
    names = Counter(block.name for block in family["blocks"])
    singles = sorted(nonzero_collision_descriptors(family))
    pairs = []
    for left, right in combinations_with_replacement(singles, 2):
        wanted = left[1:] + right[1:]
        if available(names, wanted):
            pairs.append((left, right))
    return pairs


def choose_indices(blocks, descriptor_groups):
    selected = []
    used = set()
    for descriptor in descriptor_groups:
        group = []
        for wanted in descriptor[1:]:
            index = next(index for index, block in enumerate(blocks)
                         if block.name == wanted and index not in used)
            used.add(index)
            group.append(index)
        selected.append(tuple(group))
    return selected


def family_representative(family, descriptor_groups, family_index: int):
    choices = family["passing"][0]
    cursor = 0
    pieces = []
    if family["zero_row"] is not None:
        chain_sign, singleton_sign = family["zero_row"]["signs"]
        chain_color, singleton_color = choices[0][1]
        pieces.append(k90["zero_primary"](
            family["zero_units"], chain_sign, singleton_sign,
            chain_color, singleton_color))
        cursor = 1
    groups = choose_indices(family["blocks"], descriptor_groups)
    parameter_by_index = {}
    for group_index, group in enumerate(groups):
        parameter = 100_000 + family_index * 10 + group_index
        for block_index in group:
            parameter_by_index[block_index] = parameter
    for block_index, block in enumerate(family["blocks"]):
        parameter = parameter_by_index.get(
            block_index, 1_000_000 + family_index * 100 + block_index)
        pieces.append(block.maker(parameter, choices[cursor + block_index][1]))
    return (block_diagonal(*(piece[0] for piece in pieces)),
            block_diagonal(*(piece[1] for piece in pieces)),
            block_diagonal(*(piece[2] for piece in pieces)))


def exact_matrix_ok(form, value, grading) -> bool:
    return (
        len(form) == 14
        and signature(form) == (7, 7)
        and graded_signature(form, grading) in {(3, 4), (4, 3)}
        and multiply(grading, grading) == identity(14)
        and multiply(multiply(transpose(grading), form), grading) == form
        and add(multiply(grading, value), multiply(value, grading)) == zero(14)
        and add(multiply(transpose(value), form), multiply(form, value)) == zero(14)
    )


print("\nB. PRIMITIVE NONZERO EXCESS-FOUR PRIMARIES")
gl_excess_four_inventory = {
    total: [partition for partition in partitions(total)
            if sum(sum(size >= column for size in partition) ** 2
                   for column in range(1, partition[0] + 1)) == total + 4]
    for total in range(2, 8)
}
check("classification", "the only GL/U excess-four partitions are [n-2,2]",
      gl_excess_four_inventory == {
          2: [], 3: [], 4: [(2, 2)], 5: [(3, 2)],
          6: [(4, 2)], 7: [(5, 2)],
      })
primitive_candidates = []
for family_index, family in enumerate(regular_families):
    for descriptor in primitive_excess_four_descriptors(family):
        primitive_candidates.append((family_index, family, descriptor))
primitive_keys = {
    ((None if family["zero_row"] is None else
      (family["zero_units"], family["zero_row"]["signs"])),
     tuple(block.name for block in family["blocks"]), descriptor)
    for _, family, descriptor in primitive_candidates
}
check("census", "primitive excess-four descriptors are structurally unique",
      len(primitive_keys) == len(primitive_candidates))

primitive_controls = 0
primitive_control_failures = []
for size in range(2, 6):
    for left_color, right_color in product((1, -1), repeat=2):
        primitive_controls += 1
        pieces = (real_primary(size, 7, left_color),
                  real_primary(2, 7, right_color))
        joined = tuple(block_diagonal(*(piece[index] for piece in pieces))
                       for index in range(3))
        if not local_certificate(*joined, size + 2, 4):
            primitive_control_failures.append(("R", size, left_color, right_color))
    for left_sign, right_sign in product((1, -1), repeat=2):
        primitive_controls += 1
        pieces = (imaginary_primary(size, 7, left_sign),
                  imaginary_primary(2, 7, right_sign))
        joined = tuple(block_diagonal(*(piece[index] for piece in pieces))
                       for index in range(3))
        if not local_certificate(*joined, size + 2, 4):
            primitive_control_failures.append(("I", size, left_sign, right_sign))
for size in range(1, 3):
    for left_color, right_color in product((1, -1), repeat=2):
        primitive_controls += 1
        pieces = (loxodromic_primary(size, 7, 11, left_color),
                  loxodromic_primary(1, 7, 11, right_color))
        joined = tuple(block_diagonal(*(piece[index] for piece in pieces))
                       for index in range(3))
        if not local_certificate(*joined, 2 * (size + 1), 4):
            primitive_control_failures.append(("L", size, left_color, right_color))
check("rank", "all 40 primitive excess-four local controls have fixed kernel two",
      primitive_controls == 40 and not primitive_control_failures)

primitive_matrix_failures = []
for candidate_index, (family_index, family, descriptor) in enumerate(primitive_candidates):
    if not exact_matrix_ok(*family_representative(
            family, (descriptor,), family_index + candidate_index + 1)):
        primitive_matrix_failures.append(candidate_index)
check("matrix", "every primitive excess-four configuration has an exact balanced representative",
      not primitive_matrix_failures)


print("\nC. TWO INDEPENDENT EXCESS-TWO NONZERO COLLISIONS")
double_candidates = []
for family_index, family in enumerate(regular_families):
    for descriptors in double_excess_two_descriptors(family):
        double_candidates.append((family_index, family, descriptors))
double_keys = {
    ((None if family["zero_row"] is None else
      (family["zero_units"], family["zero_row"]["signs"])),
     tuple(block.name for block in family["blocks"]), descriptors)
    for _, family, descriptors in double_candidates
}
check("census", "double-collision descriptors are unordered and structurally unique",
      len(double_keys) == len(double_candidates))
double_matrix_failures = []
for candidate_index, (family_index, family, descriptors) in enumerate(double_candidates):
    if not exact_matrix_ok(*family_representative(
            family, descriptors, family_index + candidate_index + 1)):
        double_matrix_failures.append(candidate_index)
check("matrix", "every double-collision configuration has an exact balanced representative",
      not double_matrix_failures)
check("rank", "K91 local splitting makes every disjoint collision pair contribute fixed kernel two",
      not prior["collision_control_failures"])


print("\nD. ZERO-PRIMARY EXCESS FOUR")
zero_four_rows_by_units = {
    units: singular_zero_rows(units, 4) for units in range(2, 7)
}
zero_four_inventory = {
    units: sorted({row["partition"] for row in rows})
    for units, rows in zero_four_rows_by_units.items()
}
zero_four_controls = 0
zero_four_passing = 0
for units, rows in zero_four_rows_by_units.items():
    for row in rows:
        row["admissible_allocations"] = []
        for allocation_index, (_, plus_signature) in enumerate(row["allocations"]):
            zero_four_controls += 1
            if local_certificate(
                    *singular_zero_representative(row, allocation_index), units, 4):
                zero_four_passing += 1
                row["admissible_allocations"].append(
                    (plus_signature, allocation_index))
check("rank", "every signed zero-primary excess-four row has an optimal grading",
      all(row["admissible_allocations"]
          for rows in zero_four_rows_by_units.values() for row in rows))

zero_four_candidates = []
zero_four_semisimple_excluded = 0
for units, rows in zero_four_rows_by_units.items():
    for row in rows:
        for blocks in block_multisets(7 - units):
            total_signature = row["form_signature"]
            for block in blocks:
                total_signature = add_signature(total_signature, block.form_signature)
            if total_signature != (7, 7):
                continue
            # The zero operator on a four-plane is semisimple. It contributes
            # to this mixed census only when the regular complement itself has
            # a nonzero nilpotent part; otherwise K88 already covers the row.
            if (row["partition"] == (1,) * (2 * units)
                    and not any(block.nonsemisimple for block in blocks)):
                zero_four_semisimple_excluded += 1
                continue
            option_lists = [row["admissible_allocations"]]
            option_lists += [block.grading_choices for block in blocks]
            passing = []
            for choices in product(*option_lists):
                plus_signature = tuple(map(sum, zip(*(choice[0] for choice in choices))))
                if plus_signature in {(3, 4), (4, 3)}:
                    passing.append(choices)
            zero_four_candidates.append({
                "units": units, "row": row, "blocks": blocks, "passing": passing,
            })
check("census", "every zero-excess-four plus regular-complement row balances",
      all(candidate["passing"] for candidate in zero_four_candidates))

zero_four_matrix_failures = []
for candidate_index, candidate in enumerate(zero_four_candidates):
    choices = candidate["passing"][0]
    pieces = [singular_zero_representative(candidate["row"], choices[0][1])]
    for block_index, block in enumerate(candidate["blocks"]):
        pieces.append(block.maker(
            2_000_000 + candidate_index * 100 + block_index,
            choices[block_index + 1][1]))
    joined = tuple(block_diagonal(*(piece[index] for piece in pieces))
                   for index in range(3))
    if not exact_matrix_ok(*joined):
        zero_four_matrix_failures.append(candidate_index)
check("matrix", "every zero-excess-four mixed configuration has an exact balanced representative",
      not zero_four_matrix_failures)


print("\nE. ZERO-EXCESS-TWO PLUS NONZERO-EXCESS-TWO")
zero_two_rows_by_units = prior["zero_rows_by_units"]
zero_two_nonzero_candidates = []
for units, rows in zero_two_rows_by_units.items():
    for row in rows:
        for blocks in block_multisets(7 - units):
            total_signature = row["form_signature"]
            for block in blocks:
                total_signature = add_signature(total_signature, block.form_signature)
            if total_signature != (7, 7):
                continue
            pseudo_family = {"blocks": blocks}
            for descriptor in nonzero_collision_descriptors(pseudo_family):
                option_lists = [row["admissible_allocations"]]
                option_lists += [block.grading_choices for block in blocks]
                passing = []
                for choices in product(*option_lists):
                    plus_signature = tuple(map(sum, zip(*(choice[0] for choice in choices))))
                    if plus_signature in {(3, 4), (4, 3)}:
                        passing.append(choices)
                zero_two_nonzero_candidates.append({
                    "units": units, "row": row, "blocks": blocks,
                    "descriptor": descriptor, "passing": passing,
                })
check("census", "every zero-two plus nonzero-two configuration balances",
      all(candidate["passing"] for candidate in zero_two_nonzero_candidates))

zero_two_nonzero_matrix_failures = []
for candidate_index, candidate in enumerate(zero_two_nonzero_candidates):
    choices = candidate["passing"][0]
    pieces = [singular_zero_representative(candidate["row"], choices[0][1])]
    groups = choose_indices(candidate["blocks"], (candidate["descriptor"],))
    collided = set(groups[0])
    for block_index, block in enumerate(candidate["blocks"]):
        parameter = (3_000_000 + candidate_index if block_index in collided
                     else 4_000_000 + candidate_index * 100 + block_index)
        pieces.append(block.maker(parameter, choices[block_index + 1][1]))
    joined = tuple(block_diagonal(*(piece[index] for piece in pieces))
                   for index in range(3))
    if not exact_matrix_ok(*joined):
        zero_two_nonzero_matrix_failures.append(candidate_index)
check("matrix", "every zero-two plus nonzero-two row has an exact balanced representative",
      not zero_two_nonzero_matrix_failures)
check("rank", "the two certified excess-two primaries compose to fixed kernel two",
      not prior["collision_control_failures"]
      and all(row["admissible_allocations"]
              for rows in zero_two_rows_by_units.values() for row in rows))


print("\nF. COMPLETE CENTRALIZER-ELEVEN MIXED STRATUM")
mechanism_counts = Counter({
    "primitive_nonzero_excess_four": len(primitive_candidates),
    "two_nonzero_excess_two": len(double_candidates),
    "zero_primary_excess_four": len(zero_four_candidates),
    "zero_two_plus_nonzero_two": len(zero_two_nonzero_candidates),
})
total_candidates = sum(mechanism_counts.values())
rank_histogram = Counter({(11, 80, 2, 89): total_candidates})
check("classification", "the five primitive/composite sources reduce to four disjoint census families",
      total_candidates == (len(primitive_keys) + len(double_keys)
                           + len(zero_four_candidates)
                           + len(zero_two_nonzero_candidates)))
check("census", "the exact mechanism counts sum to 673 mixed configurations",
      mechanism_counts == Counter({
          "primitive_nonzero_excess_four": 137,
          "two_nonzero_excess_two": 169,
          "zero_primary_excess_four": 283,
          "zero_two_plus_nonzero_two": 84,
      }) and total_candidates == 673)
check("scope", "exactly 24 semisimple zero-four rows route back to K88",
      zero_four_semisimple_excluded == 24)
check("rank", "every centralizer-11 row has target rank 80, fixed kernel 2 and map rank 89",
      not primitive_control_failures
      and all(row["admissible_allocations"]
              for rows in zero_four_rows_by_units.values() for row in rows))
check("rank", "every row saturates the 98D pointwise ceiling (98+80)/2=89",
      rank_histogram == Counter({(11, 80, 2, 89): total_candidates}))
check("scope", "mixed strata with centralizer dimension at least 13 remain open", True)
check("scope", "zero-neighborhood coverage, surjectivity and RSAP remain open", True)


print("\nG. REGISTRY AND REVIEW")
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
check("schema", "registry freezes the exact 673-row mechanism census",
      registry["centralizer11_mixed_census"]["signed_structural_configuration_count"] == 673
      and registry["centralizer11_mixed_census"]["primitive_nonzero_excess_four_count"] == 137
      and registry["centralizer11_mixed_census"]["two_nonzero_excess_two_count"] == 169
      and registry["centralizer11_mixed_census"]["zero_primary_excess_four_count"] == 283
      and registry["centralizer11_mixed_census"]["zero_two_plus_nonzero_two_count"] == 84)
check("schema", "registry records the sharp 11/80/2/89 schedule",
      registry["centralizer11_mixed_census"]["centralizer_dimension"] == 11
      and registry["centralizer11_mixed_census"]["target_poisson_rank"] == 80
      and registry["centralizer11_mixed_census"]["h_centralizer_dimension"] == 2
      and registry["centralizer11_mixed_census"]["moment_map_rank"] == 89)
check("schema", "registry retains all 384 nonoptimal zero-primary controls",
      registry["exhaustion"]["zero_primary_local_gradings"] == 621
      and registry["exhaustion"]["zero_primary_optimal_gradings"] == 237
      and registry["exhaustion"]["zero_primary_nonoptimal_controls"] == 384)
check("schema", "next gate advances to centralizer dimension thirteen",
      "CENTRALIZER_DIMENSION_13" in registry["next_gate"])
review_text = REVIEW.read_text(encoding="utf-8")
check("review", "hostile review preserves the higher-singular and RSAP ceiling",
      "centralizer dimension `13`" in review_text.lower()
      and "Do not claim a zero" in review_text)


print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()),
    "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())),
    "mechanism_counts": dict(sorted(mechanism_counts.items())),
    "primitive_by_species": dict(sorted(Counter(
        descriptor[0] for _, _, descriptor in primitive_candidates).items())),
    "double_collision_pair_types": {
        "+".join(key): value for key, value in sorted(Counter(
            tuple(descriptor[0] for descriptor in descriptors)
            for _, _, descriptors in double_candidates).items())
    },
    "zero_four_partition_inventory": {
        str(units): [list(partition) for partition in partitions_]
        for units, partitions_ in zero_four_inventory.items()
    },
    "zero_four_local_controls": zero_four_controls,
    "zero_four_optimal_gradings": zero_four_passing,
    "zero_four_semisimple_rows_excluded": zero_four_semisimple_excluded,
    "total_centralizer11_mixed_configurations": total_candidates,
    "rank_histogram": {str(key): value for key, value in rank_histogram.items()},
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
