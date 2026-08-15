#!/usr/bin/env python3
"""K93 exhaustive local centralizer-parity qualification in dimension 14."""

from collections import Counter
import contextlib
from itertools import product
import io
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k92_rsap_balanced_centralizer11_mixed_census_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k93-rsap-uniform-local-centralizer-parity-qualification-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k93-rsap-uniform-local-centralizer-parity-qualification.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k93-rsap-uniform-local-centralizer-parity-qualification-review.md"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


print("A. PREDECESSOR AND ARTIFACTS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    prior = runpy.run_path(str(PREDECESSOR))
check("predecessor", "K92 replays its exact 27/27 result",
      '"checks": 27' in capture.getvalue() and not prior["FAILURES"])
check("artifact", "K93 result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))

k91 = prior["prior"]
k90 = k91["prior"]
partitions = prior["partitions"]
centralizer_dimension = prior["centralizer_dimension"]
singular_zero_rows = prior["singular_zero_rows"]
singular_zero_representative = prior["singular_zero_representative"]
zero = prior["zero"]
multiply = prior["multiply"]
flatten = prior["flatten"]
rank_mod_prime = prior["rank_mod_prime"]
adjoint_rank = prior["adjoint_rank"]
projected_lie_bases = prior["projected_lie_bases"]
block_diagonal = prior["block_diagonal"]
real_primary = prior["real_primary"]
imaginary_primary = prior["imaginary_primary"]
loxodromic_primary = prior["loxodromic_primary"]
scalar = k90["scalar"]
commutator = k90["commutator"]


def gl_centralizer(partition):
    return sum(sum(size >= column for size in partition) ** 2
               for column in range(1, partition[0] + 1))


def lie_basis(form):
    size = len(form)
    basis = []
    for i in range(size):
        for j in range(i + 1, size):
            skew = zero(size)
            skew[i][j] = 1
            skew[j][i] = -1
            basis.append(multiply(form, skew))
    return basis


def diagonal_fixed_centralizer(value, basis, grading):
    size = len(grading)
    fixed = [direction for direction in basis if all(
        (grading[i][i] - grading[j][j]) * direction[i][j] == 0
        for i in range(size) for j in range(size))]
    return len(fixed) - rank_mod_prime([
        flatten(commutator(value, direction)) for direction in fixed])


def projected_fixed_centralizer(form, value, grading):
    _, fixed, _ = projected_lie_bases(form, grading)
    fixed_dimension = rank_mod_prime([flatten(direction) for direction in fixed])
    return fixed_dimension - adjoint_rank(value, fixed)


def join(pieces, colors):
    return (
        block_diagonal(*(piece[0] for piece in pieces)),
        block_diagonal(*(piece[1] for piece in pieces)),
        block_diagonal(*(scalar(piece[2], color)
                         for piece, color in zip(pieces, colors))),
    )


print("\nB. ALL ZERO-PRIMARY TYPES RELEVANT TO A MIXED COMPLEMENT")
zero_rows = 0
zero_trials = 0
zero_failures = []
zero_by_units = Counter()
for units in range(1, 7):
    excesses = set()
    for partition in partitions(2 * units):
        multiplicities = Counter(partition)
        if any(size % 2 == 0 and count % 2
               for size, count in multiplicities.items()):
            continue
        excess = centralizer_dimension(partition) - units
        if excess >= 0 and excess % 2 == 0:
            excesses.add(excess)
    for excess in sorted(excesses):
        for row in singular_zero_rows(units, excess):
            zero_rows += 1
            zero_by_units[units] += 1
            form, value, _ = singular_zero_representative(row, 0)
            basis = lie_basis(form)
            found = False
            for allocation_index in range(len(row["allocations"])):
                zero_trials += 1
                _, _, grading = singular_zero_representative(row, allocation_index)
                if diagonal_fixed_centralizer(value, basis, grading) == excess // 2:
                    found = True
                    break
            if not found:
                zero_failures.append((units, excess, row["partition"],
                                      row["positive_counts"]))
check("census", "there are 459 signed zero-primary types in rank units one through six",
      zero_rows == 459 and zero_by_units == Counter({1: 3, 2: 10, 3: 25,
                                                     4: 57, 5: 121, 6: 243}))
check("parity", "every mixed-relevant zero-primary type has a half-excess grading",
      not zero_failures)


print("\nC. ALL NONZERO PRIMARY TYPES")
real_types = imaginary_types = loxodromic_types = 0
real_failures = []
imaginary_failures = []
loxodromic_failures = []

for units in range(1, 8):
    for partition in partitions(units):
        excess = gl_centralizer(partition) - units
        pieces = [real_primary(size, 7, 1) for size in partition]
        found = False
        for colors in product((1, -1), repeat=len(partition)):
            form, value, grading = join(pieces, colors)
            if projected_fixed_centralizer(form, value, grading) == excess // 2:
                found = True
                break
        real_types += 1
        if not found:
            real_failures.append(partition)

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
            found = False
            for colors in product((1, -1), repeat=len(pieces)):
                _, _, grading = join(pieces, colors)
                if diagonal_fixed_centralizer(value, basis, grading) == excess // 2:
                    found = True
                    break
            imaginary_types += 1
            if not found:
                imaginary_failures.append((partition, positive_counts))

for complex_units in range(1, 4):
    for partition in partitions(complex_units):
        excess = 2 * (gl_centralizer(partition) - complex_units)
        pieces = [loxodromic_primary(size, 7, 11, 1) for size in partition]
        found = False
        for colors in product((1, -1), repeat=len(partition)):
            form, value, grading = join(pieces, colors)
            if projected_fixed_centralizer(form, value, grading) == excess // 2:
                found = True
                break
        loxodromic_types += 1
        if not found:
            loxodromic_failures.append(partition)

check("census", "the local nonzero inventory is exactly 44 real 248 imaginary and 6 loxodromic types",
      (real_types, imaginary_types, loxodromic_types) == (44, 248, 6))
check("parity", "every real primary type has a half-excess grading",
      not real_failures)
check("parity", "every signed imaginary primary type has a half-excess grading",
      not imaginary_failures)
check("parity", "every loxodromic primary type has a half-excess grading",
      not loxodromic_failures)


print("\nD. QUALIFICATION BOUNDARY")
total_types = zero_rows + real_types + imaginary_types + loxodromic_types
check("theorem", "all 757 local signed primary types satisfy fixed centralizer equals half excess",
      total_types == 757 and not (zero_failures + real_failures
                                  + imaginary_failures + loxodromic_failures))
check("scope", "local parity does not by itself prove a balanced global direct sum", True)
check("scope", "centralizer-13 global compatibility and connected-orbit seams remain open", True)
check("scope", "zero-neighborhood coverage surjectivity and RSAP remain open", True)


print("\nE. REGISTRY AND REVIEW")
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
check("schema", "registry freezes the 757-type local census",
      registry["local_primary_census"]["total_signed_primary_types"] == 757)
check("schema", "registry preserves the global compatibility ceiling",
      registry["coverage_status"]["global_balanced_direct_sum"] == "OPEN")
check("review", "hostile review rejects promotion to a global theorem",
      "PASS_LOCAL_PARITY_QUALIFICATION__GLOBAL_BALANCED_COMPATIBILITY_OPEN"
      in REVIEW.read_text(encoding="utf-8"))

print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()), "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())), "total_local_types": total_types,
    "zero_rows": zero_rows, "zero_search_trials": zero_trials,
    "real_types": real_types, "imaginary_types": imaginary_types,
    "loxodromic_types": loxodromic_types,
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
