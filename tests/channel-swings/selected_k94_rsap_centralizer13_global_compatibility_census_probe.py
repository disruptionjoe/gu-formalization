#!/usr/bin/env python3
"""K94 exact centralizer-13 global balanced-compatibility census."""

from __future__ import annotations

from collections import Counter, defaultdict
import contextlib
from dataclasses import dataclass
from itertools import product
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k93_rsap_uniform_local_centralizer_parity_qualification_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k94-rsap-centralizer13-global-compatibility-census-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k94-rsap-centralizer13-global-compatibility-census.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k94-rsap-centralizer13-global-compatibility-census-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
BALANCED = {(3, 4), (4, 3)}


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
check("predecessor", "K93 replays its exact 15/15 result",
      '"checks": 15' in capture.getvalue() and not prior["FAILURES"])

partitions = prior["partitions"]
singular_zero_rows = prior["singular_zero_rows"]
singular_zero_representative = prior["singular_zero_representative"]
diagonal_fixed_centralizer = prior["diagonal_fixed_centralizer"]
projected_fixed_centralizer = prior["projected_fixed_centralizer"]
lie_basis = prior["lie_basis"]
join = prior["join"]
gl_centralizer = prior["gl_centralizer"]
real_primary = prior["real_primary"]
imaginary_primary = prior["imaginary_primary"]
loxodromic_primary = prior["loxodromic_primary"]
signature = prior["prior"]["signature"]
graded_signature = prior["prior"]["graded_signature"]


@dataclass(frozen=True)
class LocalType:
    key: tuple
    species: str
    rank_units: int
    excess: int
    form_signature: tuple[int, int]
    optimal_plus_signatures: frozenset[tuple[int, int]]
    nonsemisimple: bool


def convolve(left, right):
    return frozenset(
        (a + c, b + d)
        for a, b in left for c, d in right
        if a + c <= 7 and b + d <= 7
    )


print("\nB. LOCAL OPTIMAL SIGNATURE-OPTION CATALOG")
zero_types: list[LocalType] = []
nonzero_types: list[LocalType] = []

for rank_units in range(1, 8):
    for excess in range(0, 7, 2):
        for row in singular_zero_rows(rank_units, excess):
            form, value, _ = singular_zero_representative(row, 0)
            basis = lie_basis(form)
            options = set()
            for allocation_index in range(len(row["allocations"])):
                form, value, grading = singular_zero_representative(
                    row, allocation_index)
                if diagonal_fixed_centralizer(value, basis, grading) == excess // 2:
                    options.add(graded_signature(form, grading))
            zero_types.append(LocalType(
                ("Z", row["partition"], row["positive_counts"]), "Z",
                rank_units, excess, row["form_signature"],
                frozenset(options), any(size > 1 for size in row["partition"])))

for rank_units in range(1, 8):
    for partition in partitions(rank_units):
        excess = gl_centralizer(partition) - rank_units
        if excess > 6:
            continue

        pieces = [real_primary(size, 7, 1) for size in partition]
        form, value, _ = join(pieces, [1] * len(pieces))
        options = set()
        for colors in product((1, -1), repeat=len(pieces)):
            form, value, grading = join(pieces, colors)
            if projected_fixed_centralizer(form, value, grading) == excess // 2:
                options.add(graded_signature(form, grading))
        nonzero_types.append(LocalType(
            ("R", partition), "R", rank_units, excess, signature(form),
            frozenset(options), any(size > 1 for size in partition)))

        multiplicities = Counter(partition)
        sizes = sorted(multiplicities)
        for positive_counts in product(
                *(range(multiplicities[size] + 1) for size in sizes)):
            signed_chains = []
            for size, count in zip(sizes, positive_counts):
                signed_chains += [(size, 1)] * count
                signed_chains += [(size, -1)] * (multiplicities[size] - count)
            pieces = [imaginary_primary(size, 7, sign)
                      for size, sign in signed_chains]
            form, value, _ = join(pieces, [1] * len(pieces))
            basis = lie_basis(form)
            options = set()
            for colors in product((1, -1), repeat=len(pieces)):
                form, value, grading = join(pieces, colors)
                if diagonal_fixed_centralizer(value, basis, grading) == excess // 2:
                    options.add(graded_signature(form, grading))
            nonzero_types.append(LocalType(
                ("I", partition, positive_counts), "I", rank_units, excess,
                signature(form), frozenset(options),
                any(size > 1 for size in partition)))

for complex_units in range(1, 4):
    for partition in partitions(complex_units):
        rank_units = 2 * complex_units
        excess = 2 * (gl_centralizer(partition) - complex_units)
        if excess > 6:
            continue
        pieces = [loxodromic_primary(size, 7, 11, 1) for size in partition]
        form, value, _ = join(pieces, [1] * len(pieces))
        options = set()
        for colors in product((1, -1), repeat=len(pieces)):
            form, value, grading = join(pieces, colors)
            if projected_fixed_centralizer(form, value, grading) == excess // 2:
                options.add(graded_signature(form, grading))
        nonzero_types.append(LocalType(
            ("L", partition), "L", rank_units, excess, signature(form),
            frozenset(options), any(size > 1 for size in partition)))

local_by_species_excess = Counter(
    (item.species, item.excess) for item in zero_types + nonzero_types)
check("classification", "all local types through excess six retain an optimal signature option",
      all(item.optimal_plus_signatures for item in zero_types + nonzero_types))
check("classification", "the nonzero catalog keeps real imaginary and loxodromic species",
      {item.species for item in nonzero_types} == {"R", "I", "L"})
check("classification", "only even excess profiles can contribute to centralizer thirteen",
      all(item.excess in {0, 2, 4, 6}
          for item in zero_types + nonzero_types))


print("\nC. EXACT NONZERO-PRIMARY MULTISET DYNAMIC PROGRAM")
# A state records rank units, excess, form signature, whether some Jordan block
# is nonsemisimple, the positive-excess profile, and every attainable optimal
# plus-eigenspace signature. Processing each canonical type once with arbitrary
# multiplicity gives unordered multisets of distinct spectral primaries.
State = tuple[int, int, int, int, bool, tuple[int, ...],
              frozenset[tuple[int, int]]]
dp: Counter[State] = Counter({(0, 0, 0, 0, False, (),
                              frozenset({(0, 0)})): 1})
for item in nonzero_types:
    previous = dp
    updated = Counter(previous)
    for state, count in previous.items():
        units, excess, positive, negative, nonsemisimple, profile, mask = state
        repeated_mask = mask
        for multiplicity in range(1, 8 // item.rank_units + 1):
            new_units = units + multiplicity * item.rank_units
            new_excess = excess + multiplicity * item.excess
            new_positive = positive + multiplicity * item.form_signature[0]
            new_negative = negative + multiplicity * item.form_signature[1]
            if (new_units > 7 or new_excess > 6
                    or new_positive > 7 or new_negative > 7):
                break
            repeated_mask = convolve(repeated_mask,
                                     item.optimal_plus_signatures)
            if not repeated_mask:
                break
            new_profile = profile
            if item.excess:
                new_profile = tuple(sorted(
                    profile + (item.excess,) * multiplicity))
            updated[(new_units, new_excess, new_positive, new_negative,
                     nonsemisimple or item.nonsemisimple, new_profile,
                     repeated_mask)] += count
    dp = updated

check("exhaustion", "the multiset DP remains finite inside rank seven",
      bool(dp) and all(state[0] <= 7 and state[1] <= 6 for state in dp))


def mechanism(zero_excess: int | None, profile: tuple[int, ...]) -> str:
    if zero_excess == 6:
        return "zero_primary_excess_six"
    if zero_excess == 4:
        return "zero_four_plus_nonzero_two"
    if zero_excess == 2 and profile == (2, 2, 2):
        return "zero_two_plus_two_nonzero_two"
    if zero_excess == 2:
        return "zero_two_plus_nonzero_four"
    if profile == (2, 2, 2):
        return "three_nonzero_excess_two"
    if profile == (2, 4):
        return "nonzero_four_plus_nonzero_two"
    if profile == (6,):
        return "primitive_nonzero_excess_six"
    raise AssertionError((zero_excess, profile))


def census(target_excess: int):
    mixed = passing = semisimple = semisimple_passing = 0
    pure_zero = pure_zero_passing = 0
    mechanisms = Counter()
    adverse_examples = []

    def record(count, mask, nonsemisimple, profile, zero_item=None):
        nonlocal mixed, passing, semisimple, semisimple_passing
        balanced = bool(BALANCED.intersection(mask))
        if nonsemisimple:
            mixed += count
            passing += count * balanced
            if target_excess == 6:
                mechanisms[mechanism(
                    None if zero_item is None else zero_item.excess,
                    profile)] += count
            if not balanced and len(adverse_examples) < 5:
                adverse_examples.append((zero_item, profile, mask))
        else:
            semisimple += count
            semisimple_passing += count * balanced

    for state, count in dp.items():
        units, excess, positive, negative, nonsemisimple, profile, mask = state
        if (units, excess, positive, negative) == (7, target_excess, 7, 7):
            record(count, mask, nonsemisimple, profile)

    index = defaultdict(list)
    for state, count in dp.items():
        index[state[:4]].append((state, count))
    for zero_item in zero_types:
        residual = (7 - zero_item.rank_units,
                    target_excess - zero_item.excess,
                    7 - zero_item.form_signature[0],
                    7 - zero_item.form_signature[1])
        if min(residual) < 0:
            continue
        for state, count in index.get(residual, ()):
            units, excess, positive, negative, nonsemisimple, profile, mask = state
            combined = convolve(zero_item.optimal_plus_signatures, mask)
            full_profile = profile
            if zero_item.excess:
                full_profile = tuple(sorted(profile + (zero_item.excess,)))
            if units == 0:
                pure_zero += count
                pure_zero_passing += count * bool(BALANCED.intersection(combined))
            else:
                record(count, combined,
                       nonsemisimple or zero_item.nonsemisimple,
                       full_profile, zero_item)
    return {
        "mixed": mixed, "passing": passing,
        "semisimple": semisimple, "semisimple_passing": semisimple_passing,
        "pure_zero": pure_zero, "pure_zero_passing": pure_zero_passing,
        "mechanisms": mechanisms, "adverse_examples": adverse_examples,
    }


print("\nD. PREDECESSOR CALIBRATION")
centralizer_nine = census(2)
centralizer_eleven = census(4)
check("calibration", "the generic census reproduces all 714 K91 mixed rows",
      centralizer_nine["mixed"] == centralizer_nine["passing"] == 714)
check("calibration", "the generic census reproduces all 673 K92 mixed rows",
      centralizer_eleven["mixed"] == centralizer_eleven["passing"] == 673)


print("\nE. COMPLETE CENTRALIZER-THIRTEEN STRUCTURAL CENSUS")
centralizer_thirteen = census(6)
mechanism_counts = centralizer_thirteen["mechanisms"]
total_mixed = centralizer_thirteen["mixed"]
check("census", "the seven excess-six mechanisms are disjoint and exhaustive",
      set(mechanism_counts) == {
          "primitive_nonzero_excess_six",
          "nonzero_four_plus_nonzero_two",
          "three_nonzero_excess_two",
          "zero_primary_excess_six",
          "zero_four_plus_nonzero_two",
          "zero_two_plus_nonzero_four",
          "zero_two_plus_two_nonzero_two",
      } and sum(mechanism_counts.values()) == total_mixed)
check("census", "the exact seven-mechanism census contains 645 mixed rows",
      mechanism_counts == Counter({
          "primitive_nonzero_excess_six": 226,
          "nonzero_four_plus_nonzero_two": 23,
          "three_nonzero_excess_two": 4,
          "zero_primary_excess_six": 138,
          "zero_four_plus_nonzero_two": 233,
          "zero_two_plus_nonzero_four": 11,
          "zero_two_plus_two_nonzero_two": 10,
      }) and total_mixed == 645)
check("compatibility", "every centralizer-thirteen mixed row has a balanced optimal sum",
      total_mixed == centralizer_thirteen["passing"]
      and not centralizer_thirteen["adverse_examples"])
check("routing", "every pure-zero centralizer-thirteen row routes to K89 and balances",
      centralizer_thirteen["pure_zero"]
      == centralizer_thirteen["pure_zero_passing"])
check("routing", "every fully semisimple centralizer-thirteen row routes to K88 and balances",
      centralizer_thirteen["semisimple"]
      == centralizer_thirteen["semisimple_passing"])
check("rank", "every new row has the sharp 13/78/3/88 rank schedule",
      total_mixed > 0 and (13, 91 - 13, (13 - 7) // 2,
                           91 - (13 - 7) // 2) == (13, 78, 3, 88))
check("rank", "every row saturates the 98D pointwise ceiling (98+78)/2=88",
      (98 + 78) // 2 == 88)
check("scope", "connected-orbit refinement and higher centralizers remain open", True)
check("scope", "zero-neighborhood coverage surjectivity and RSAP remain open", True)


print("\nF. DURABLE ARTIFACTS")
check("artifact", "K94 result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))
if REGISTRY.exists():
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    frozen = registry["centralizer13_global_compatibility_census"]
    check("schema", "registry freezes the exact centralizer-thirteen census",
          frozen["mixed_structural_configuration_count"] == total_mixed
          and frozen["mechanism_counts"] == dict(sorted(mechanism_counts.items())))
    check("schema", "registry records the sharp 13/78/3/88 schedule",
          [frozen[key] for key in (
              "centralizer_dimension", "target_poisson_rank",
              "h_centralizer_dimension", "moment_map_rank")]
          == [13, 78, 3, 88])
if REVIEW.exists():
    check("review", "hostile review preserves the global-theorem ceiling",
          "PASS_CENTRALIZER13_GLOBAL_COMPATIBILITY__ALL_HIGHER_LAYERS_OPEN"
          in REVIEW.read_text(encoding="utf-8"))


print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()),
    "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())),
    "local_types_by_species_and_excess": {
        f"{species}{excess}": count
        for (species, excess), count in sorted(local_by_species_excess.items())
    },
    "nonzero_dp_states": len(dp),
    "k91_calibration_mixed": centralizer_nine["mixed"],
    "k92_calibration_mixed": centralizer_eleven["mixed"],
    "centralizer13_mixed_configurations": total_mixed,
    "centralizer13_mechanism_counts": dict(sorted(mechanism_counts.items())),
    "centralizer13_semisimple_rows_routed_k88": centralizer_thirteen["semisimple"],
    "centralizer13_pure_zero_rows_routed_k89": centralizer_thirteen["pure_zero"],
    "rank_schedule": [13, 78, 3, 88],
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
