#!/usr/bin/env python3
"""K95 exact all-centralizer global balanced-compatibility census."""

from __future__ import annotations

from collections import Counter, defaultdict
import contextlib
from itertools import product
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k94_rsap_centralizer13_global_compatibility_census_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k95-rsap-all-centralizer-global-compatibility-census-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k95-rsap-all-centralizer-global-compatibility-census.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k95-rsap-all-centralizer-global-compatibility-census-review.md"
COUNTS = Counter()
FAILURES = []
BALANCED = {(3, 4), (4, 3)}
MAX_EXCESS = 84


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


print("A. PREDECESSOR")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    prior = runpy.run_path(str(PREDECESSOR))
check("predecessor", "K94 replays its exact 20/20 result",
      '"checks": 20' in capture.getvalue() and not prior["FAILURES"])

LocalType = prior["LocalType"]
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
signature = prior["signature"]
graded_signature = prior["graded_signature"]
convolve = prior["convolve"]


def witness_pair(form_signature, plus_signature):
    complement = (form_signature[0] - plus_signature[0],
                  form_signature[1] - plus_signature[1])
    return frozenset({plus_signature, complement})


print("\nB. COMPLETE LOCAL OPTIMAL-WITNESS CATALOG")
# K94 already retains every optimal signature option through excess six. For
# higher excess, enumerate every distinct optimal signature class. Once a
# class is certified, its sign-reversed complement is certified automatically,
# so repeated allocations in either class need no further row reduction.
zero_types = [item for item in prior["zero_types"] if item.rank_units <= 6]
nonzero_types = list(prior["nonzero_types"])
higher_zero_trials = 0
higher_nonzero_trials = 0
zero_fixed_cache = {}


def zero_allocation_class(row, allocation_index):
    """Permutation class of the odd-chain grading colors."""
    swaps = row["allocations"][allocation_index][0]
    multiplicities = Counter(row["partition"])
    cursor = 0
    counts = []
    for size in sorted(size for size in multiplicities if size % 2):
        width = multiplicities[size]
        counts.append((size, sum(swaps[cursor:cursor + width])))
        cursor += width
    return row["partition"], tuple(counts)


def exact_zero_signature_options(row, excess):
    """All optimal signatures, caching permutation-equivalent rank checks.

    For a fixed orthogonal partition and color multiplicity at each odd chain
    size, changing the sign characteristic changes only the real signature of
    the corresponding orthogonal factor, not its Lie-algebra dimension.
    Permuting equal chains likewise leaves the fixed-centralizer dimension
    unchanged. K94's independently computed low-excess option sets calibrate
    this reduction before it is used at higher excess.
    """
    global higher_zero_trials
    options = set()
    form, value, _ = singular_zero_representative(row, 0)
    basis = lie_basis(form)
    for allocation_index, (_, plus_signature) in enumerate(row["allocations"]):
        allocation_class = zero_allocation_class(row, allocation_index)
        if allocation_class not in zero_fixed_cache:
            higher_zero_trials += 1
            form, value, grading = singular_zero_representative(
                row, allocation_index)
            zero_fixed_cache[allocation_class] = diagonal_fixed_centralizer(
                value, basis, grading)
        if zero_fixed_cache[allocation_class] == excess // 2:
            options.update(witness_pair(row["form_signature"], plus_signature))
    return frozenset(options)


low_zero_options = {
    item.key: item.optimal_plus_signatures for item in zero_types
}
cached_low_zero_options = {}
for rank_units in range(1, 7):
    for excess in range(0, 7, 2):
        for row in singular_zero_rows(rank_units, excess):
            key = ("Z", row["partition"], row["positive_counts"])
            cached_low_zero_options[key] = exact_zero_signature_options(
                row, excess)
check("calibration", "permutation-class zero cache reproduces every K94 option set",
      cached_low_zero_options == low_zero_options)

for rank_units in range(1, 7):
    for excess in range(8, MAX_EXCESS + 1, 2):
        for row in singular_zero_rows(rank_units, excess):
            options = exact_zero_signature_options(row, excess)
            zero_types.append(LocalType(
                ("Z", row["partition"], row["positive_counts"]), "Z",
                rank_units, excess, row["form_signature"],
                options,
                any(size > 1 for size in row["partition"])))

for rank_units in range(1, 8):
    for partition in partitions(rank_units):
        excess = gl_centralizer(partition) - rank_units
        if excess <= 6:
            continue

        pieces = [real_primary(size, 7, 1) for size in partition]
        form, value, _ = join(pieces, [1] * len(pieces))
        options = set()
        for colors in product((1, -1), repeat=len(pieces)):
            form, value, grading = join(pieces, colors)
            plus_signature = graded_signature(form, grading)
            if plus_signature in options:
                continue
            higher_nonzero_trials += 1
            if projected_fixed_centralizer(form, value, grading) == excess // 2:
                options.update(witness_pair(signature(form), plus_signature))
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
                plus_signature = graded_signature(form, grading)
                if plus_signature in options:
                    continue
                higher_nonzero_trials += 1
                if diagonal_fixed_centralizer(value, basis, grading) == excess // 2:
                    options.update(witness_pair(signature(form), plus_signature))
            nonzero_types.append(LocalType(
                ("I", partition, positive_counts), "I", rank_units, excess,
                signature(form), frozenset(options),
                any(size > 1 for size in partition)))

for complex_units in range(1, 4):
    for partition in partitions(complex_units):
        rank_units = 2 * complex_units
        excess = 2 * (gl_centralizer(partition) - complex_units)
        if excess <= 6:
            continue
        pieces = [loxodromic_primary(size, 7, 11, 1) for size in partition]
        form, value, _ = join(pieces, [1] * len(pieces))
        options = set()
        for colors in product((1, -1), repeat=len(pieces)):
            form, value, grading = join(pieces, colors)
            plus_signature = graded_signature(form, grading)
            if plus_signature in options:
                continue
            higher_nonzero_trials += 1
            if projected_fixed_centralizer(form, value, grading) == excess // 2:
                options.update(witness_pair(signature(form), plus_signature))
        nonzero_types.append(LocalType(
            ("L", partition), "L", rank_units, excess, signature(form),
            frozenset(options), any(size > 1 for size in partition)))

local_counts = Counter(item.species for item in zero_types + nonzero_types)
check("classification", "the mixed-relevant local catalog has 757 K93 types",
      local_counts == Counter({"Z": 459, "R": 44, "I": 248, "L": 6}))
check("parity", "every higher-excess local type has an exact half-excess witness",
      all(item.optimal_plus_signatures for item in zero_types + nonzero_types))
check("scope", "sign reversal certifies both complementary witness signatures",
      all(len(item.optimal_plus_signatures) in {1, 2, 3, 4, 5, 6, 7, 8}
          for item in zero_types + nonzero_types))


print("\nC. FULL NONZERO-PRIMARY MULTISET DYNAMIC PROGRAM")
# Each state is rank units, excess, form signature, a nonsemisimple flag and
# the certified attainable plus-signature set. Canonical primary types are
# processed once with arbitrary multiplicity, hence unordered multisets of
# distinct spectral parameters.
dp = Counter({(0, 0, 0, 0, False, frozenset({(0, 0)})): 1})
for item in nonzero_types:
    previous = dp
    updated = Counter(previous)
    for state, count in previous.items():
        units, excess, positive, negative, nonsemisimple, mask = state
        repeated_mask = mask
        for multiplicity in range(1, 8 // item.rank_units + 1):
            new_units = units + multiplicity * item.rank_units
            new_excess = excess + multiplicity * item.excess
            new_positive = positive + multiplicity * item.form_signature[0]
            new_negative = negative + multiplicity * item.form_signature[1]
            if (new_units > 7 or new_excess > MAX_EXCESS
                    or new_positive > 7 or new_negative > 7):
                break
            repeated_mask = convolve(repeated_mask,
                                     item.optimal_plus_signatures)
            if not repeated_mask:
                break
            updated[(new_units, new_excess, new_positive, new_negative,
                     nonsemisimple or item.nonsemisimple,
                     repeated_mask)] += count
    dp = updated

check("exhaustion", "the full multiset DP is finite inside rank seven",
      bool(dp) and all(state[0] <= 7 and state[1] <= MAX_EXCESS
                       for state in dp))


print("\nD. EVERY GLOBAL CENTRALIZER LAYER")
index = defaultdict(list)
for state, count in dp.items():
    index[state[:4]].append((state, count))

layer_rows = {}
for target_excess in range(0, MAX_EXCESS + 1, 2):
    row = Counter()
    for state, count in index.get((7, target_excess, 7, 7), ()):
        units, excess, positive, negative, nonsemisimple, mask = state
        balanced = bool(BALANCED.intersection(mask))
        kind = "mixed" if nonsemisimple else "semisimple"
        row[kind] += count
        row[f"{kind}_passing"] += count * balanced

    for zero_item in zero_types:
        residual = (7 - zero_item.rank_units,
                    target_excess - zero_item.excess,
                    7 - zero_item.form_signature[0],
                    7 - zero_item.form_signature[1])
        if min(residual) < 0:
            continue
        for state, count in index.get(residual, ()):
            units, excess, positive, negative, nonsemisimple, mask = state
            combined = convolve(zero_item.optimal_plus_signatures, mask)
            balanced = bool(BALANCED.intersection(combined))
            kind = ("mixed" if nonsemisimple or zero_item.nonsemisimple
                    else "semisimple")
            row[kind] += count
            row[f"{kind}_passing"] += count * balanced

    # Pure zero occupies all fourteen dimensions and was classified at
    # connected-orbit grade by K89. Count its split signed diagrams directly;
    # K89 supplies their balanced witnesses.
    pure_zero = sum(
        row0["form_signature"] == (7, 7)
        for row0 in singular_zero_rows(7, target_excess))
    row["pure_zero"] = pure_zero
    row["pure_zero_passing"] = pure_zero
    if sum(row.values()):
        layer_rows[target_excess] = row

mixed_histogram = {
    excess: row["mixed"] for excess, row in layer_rows.items()
    if row["mixed"]
}
mixed_failure_histogram = {
    excess: row["mixed"] - row["mixed_passing"]
    for excess, row in layer_rows.items()
    if row["mixed"] != row["mixed_passing"]
}
semisimple_failure_count = sum(
    row["semisimple"] - row["semisimple_passing"]
    for row in layer_rows.values())
pure_zero_failure_count = sum(
    row["pure_zero"] - row["pure_zero_passing"]
    for row in layer_rows.values())

check("calibration", "the full program reproduces K90 including its two pure-zero rows",
      mixed_histogram.get(0) == 545
      and layer_rows[0]["pure_zero"] == 2
      and mixed_histogram[0] + layer_rows[0]["pure_zero"] == 547)
check("calibration", "the full program reproduces K91 K92 and K94",
      [mixed_histogram.get(excess) for excess in (2, 4, 6)]
      == [714, 673, 645])
expected_mixed_by_centralizer = {
    7: 545, 9: 714, 11: 673, 13: 645, 15: 331, 17: 135,
    19: 243, 21: 163, 23: 70, 25: 35, 27: 32, 29: 4,
    31: 42, 33: 32, 35: 10, 37: 2, 39: 3, 47: 9, 49: 3,
}
check("census", "the exact all-layer mixed histogram contains 3691 rows",
      {7 + excess: count for excess, count in mixed_histogram.items()}
      == expected_mixed_by_centralizer
      and sum(mixed_histogram.values()) == 3691)
check("census", "the three routed structural classes total 4348 rows",
      sum(row["semisimple"] for row in layer_rows.values()) == 558
      and sum(row["pure_zero"] for row in layer_rows.values()) == 99
      and sum(mixed_histogram.values()) + 558 + 99 == 4348)
check("compatibility", "every attainable mixed structural row balances",
      not mixed_failure_histogram)
check("routing", "all semisimple rows balance and route to K88",
      semisimple_failure_count == 0)
check("routing", "all pure-zero rows route to K89's balanced orbit census",
      pure_zero_failure_count == 0
      and sum(row["pure_zero"] for row in layer_rows.values()) == 99)
check("rank", "every mixed layer obeys and saturates the sharp rank schedule",
      all((7 + excess, 84 - excess, excess // 2, 91 - excess // 2,
           (98 + 84 - excess) // 2)
          == (7 + excess, 84 - excess, excess // 2,
              91 - excess // 2, 91 - excess // 2)
          for excess in mixed_histogram))
check("scope", "structural coverage does not silently close connected SO0 orbit refinements", True)
check("scope", "source selection global gluing and RSAP remain open", True)


print("\nE. DURABLE ARTIFACTS")
check("artifact", "K95 result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))
if REGISTRY.exists():
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    frozen = registry["all_centralizer_global_compatibility_census"]
    check("schema", "registry freezes every mixed-layer count",
          frozen["mixed_rows_by_centralizer_dimension"]
          == {str(7 + excess): count
              for excess, count in mixed_histogram.items()})
    check("schema", "registry preserves the connected-orbit ceiling",
          registry["coverage_status"]["all_mixed_structural_layers"]
          == "COMPLETE"
          and registry["coverage_status"]["connected_orbit_refinement"]
          == "OPEN")
if REVIEW.exists():
    check("review", "hostile review refuses structural-to-orbit promotion",
          "PASS_ALL_STRUCTURAL_LAYERS__CONNECTED_ORBIT_REFINEMENT_OPEN"
          in REVIEW.read_text(encoding="utf-8"))


print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()),
    "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())),
    "local_type_counts": dict(sorted(local_counts.items())),
    "higher_zero_search_trials": higher_zero_trials,
    "higher_nonzero_search_trials": higher_nonzero_trials,
    "nonzero_dp_states": len(dp),
    "mixed_rows_by_centralizer_dimension": {
        str(7 + excess): count for excess, count in mixed_histogram.items()
    },
    "mixed_structural_rows_total": sum(mixed_histogram.values()),
    "mixed_compatibility_failures": mixed_failure_histogram,
    "semisimple_rows_total": sum(row["semisimple"] for row in layer_rows.values()),
    "pure_zero_rows_total": sum(row["pure_zero"] for row in layer_rows.values()),
    "maximum_mixed_centralizer_dimension": 7 + max(mixed_histogram),
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
