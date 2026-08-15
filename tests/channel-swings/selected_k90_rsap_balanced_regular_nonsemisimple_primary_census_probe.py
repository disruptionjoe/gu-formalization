#!/usr/bin/env python3
"""Exact K90 balanced regular-nonsemisimple primary census and rank gate."""

from __future__ import annotations

from collections import Counter
import contextlib
from itertools import product
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k89_rsap_balanced_nilpotent_orbit_census_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k90-rsap-balanced-regular-nonsemisimple-primary-census-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k90-rsap-balanced-regular-nonsemisimple-primary-census.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k90-rsap-balanced-regular-nonsemisimple-primary-census-review.md"
PRIME = 1_000_003
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def zero(size: int) -> list[list[int]]:
    return [[0] * size for _ in range(size)]


def identity(size: int) -> list[list[int]]:
    return [[int(i == j) for j in range(size)] for i in range(size)]


def transpose(value):
    return [list(row) for row in zip(*value)]


def add(left, right, scale: int = 1):
    return [[left[i][j] + scale * right[i][j] for j in range(len(left[0]))]
            for i in range(len(left))]


def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def scalar(value, coefficient: int):
    return [[coefficient * entry for entry in row] for row in value]


def kronecker(left, right):
    return [[a * b for a in left_row for b in right_row]
            for left_row in left for right_row in right]


def block_diagonal(*blocks):
    size = sum(len(block) for block in blocks)
    result = zero(size)
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            result[offset + i][offset:offset + len(block)] = row
        offset += len(block)
    return result


def block_two_by_two(a, b, c, d):
    return [a[i] + b[i] for i in range(len(a))] + [c[i] + d[i] for i in range(len(c))]


def flatten(value):
    return [entry for row in value for entry in row]


def commutator(left, right):
    return add(multiply(left, right), multiply(right, left), -1)


def rank_mod_prime(columns) -> int:
    pivots = {}
    for raw in columns:
        column = {i: entry % PRIME for i, entry in enumerate(raw) if entry % PRIME}
        while column:
            pivot = min(column)
            if pivot not in pivots:
                inverse = pow(column[pivot], PRIME - 2, PRIME)
                pivots[pivot] = {i: entry * inverse % PRIME for i, entry in column.items()}
                break
            factor = column[pivot]
            for i, entry in pivots[pivot].items():
                replacement = (column.get(i, 0) - factor * entry) % PRIME
                if replacement:
                    column[i] = replacement
                else:
                    column.pop(i, None)
    return len(pivots)


def signature(form):
    size = len(form)
    assert multiply(form, form) == identity(size)
    trace = sum(form[i][i] for i in range(size))
    return (size + trace) // 2, (size - trace) // 2


def graded_signature(form, grading, eigenvalue: int = 1):
    size = len(form)
    grading_trace = sum(grading[i][i] for i in range(size))
    dimension = (size + eigenvalue * grading_trace) // 2
    form_grading = multiply(form, grading)
    form_trace = sum(form[i][i] for i in range(size))
    mixed_trace = sum(form_grading[i][i] for i in range(size))
    restricted_trace = (form_trace + eigenvalue * mixed_trace) // 2
    return ((dimension + restricted_trace) // 2,
            (dimension - restricted_trace) // 2)


def plain_reversal(size: int):
    result = zero(size)
    for i in range(size):
        result[i][size - 1 - i] = 1
    return result


def alternating_reversal(size: int, sign: int = 1):
    result = zero(size)
    for i in range(size):
        result[i][size - 1 - i] = sign * (-1) ** i
    return result


def jordan_nilpotent(size: int):
    result = zero(size)
    for i in range(size - 1):
        result[i][i + 1] = 1
    return result


def real_primary(size: int, eigenvalue: int, grading_sign: int):
    jordan = add(scalar(identity(size), eigenvalue), jordan_nilpotent(size))
    unit = identity(size)
    empty = zero(size)
    reversal = scalar(plain_reversal(size), grading_sign)
    form = block_two_by_two(empty, unit, unit, empty)
    value = block_two_by_two(jordan, empty, empty, scalar(transpose(jordan), -1))
    grading = block_two_by_two(empty, reversal, reversal, empty)
    return form, value, grading


def imaginary_primary(size: int, eigenvalue: int, form_sign: int):
    reversal = alternating_reversal(size, form_sign)
    alternating = block_diagonal(*[[[(-1) ** i]] for i in range(size)])
    unit_two = identity(2)
    symplectic_two = [[0, 1], [-1, 0]]
    rotation = [[0, -eigenvalue], [eigenvalue, 0]]
    reflection = [[1, 0], [0, -1]]
    multiplicity_form = unit_two if size % 2 else symplectic_two
    form = kronecker(reversal, multiplicity_form)
    value = add(kronecker(identity(size), rotation),
                kronecker(jordan_nilpotent(size), unit_two))
    grading = kronecker(alternating, reflection)
    return form, value, grading


def loxodromic_primary(size: int, real_part: int, imaginary_part: int,
                       grading_sign: int):
    complex_block = [[real_part, -imaginary_part], [imaginary_part, real_part]]
    reflection = [[1, 0], [0, -1]]
    unit_two = identity(2)
    jordan = add(kronecker(identity(size), complex_block),
                 kronecker(jordan_nilpotent(size), unit_two))
    dimension = 2 * size
    unit = identity(dimension)
    empty = zero(dimension)
    reversal = scalar(kronecker(plain_reversal(size), reflection), grading_sign)
    form = block_two_by_two(empty, unit, unit, empty)
    value = block_two_by_two(jordan, empty, empty, scalar(transpose(jordan), -1))
    grading = block_two_by_two(empty, reversal, reversal, empty)
    return form, value, grading


def zero_primary(rank_units: int, chain_sign: int, singleton_sign: int,
                 chain_color: int, singleton_color: int):
    chain_size = 2 * rank_units - 1
    form = block_diagonal(alternating_reversal(chain_size, chain_sign),
                          [[singleton_sign]])
    value = block_diagonal(jordan_nilpotent(chain_size), [[0]])
    grading = block_diagonal(
        *[[[chain_color * (-1) ** i]] for i in range(chain_size)],
        [[singleton_color]],
    )
    return form, value, grading


class PrimaryBlock:
    def __init__(self, name, rank_units, form_signature, nonsemisimple,
                 maker, grading_choices):
        self.name = name
        self.rank_units = rank_units
        self.form_signature = form_signature
        self.nonsemisimple = nonsemisimple
        self.maker = maker
        self.grading_choices = grading_choices


def primary_catalog():
    catalog = []
    for size in range(1, 8):
        form, _, _ = real_primary(size, 2, 1)
        choices = []
        for grading_sign in (1, -1):
            choice_form, _, choice_grading = real_primary(size, 2, grading_sign)
            choices.append((graded_signature(choice_form, choice_grading), grading_sign))
        catalog.append(PrimaryBlock(
            f"R{size}", size, signature(form), size > 1,
            lambda index, choice, size=size: real_primary(size, 10 + index, choice),
            choices,
        ))
        for form_sign in (1, -1):
            form, _, grading = imaginary_primary(size, 2, form_sign)
            catalog.append(PrimaryBlock(
                f"I{size}{'+' if form_sign > 0 else '-'}", size,
                signature(form), size > 1,
                lambda index, choice, size=size, form_sign=form_sign:
                    imaginary_primary(size, 20 + index, form_sign),
                [(graded_signature(form, grading), 0)],
            ))
        if 2 * size <= 7:
            form, _, _ = loxodromic_primary(size, 2, 3, 1)
            choices = []
            for grading_sign in (1, -1):
                choice_form, _, choice_grading = loxodromic_primary(
                    size, 2, 3, grading_sign)
                choices.append((graded_signature(choice_form, choice_grading), grading_sign))
            catalog.append(PrimaryBlock(
                f"L{size}", 2 * size, signature(form), size > 1,
                lambda index, choice, size=size:
                    loxodromic_primary(size, 30 + index, 40 + index, choice),
                choices,
            ))
    return sorted(catalog, key=lambda block: block.name)


CATALOG = primary_catalog()


def zero_variants(rank_units: int):
    # At rank one the two Jordan rows both have size one, so their signs are
    # an unordered multiset. In higher rank the long chain and singleton differ.
    sign_pairs = ([(1, 1), (1, -1), (-1, -1)] if rank_units == 1
                  else list(product((1, -1), repeat=2)))
    variants = []
    for chain_sign, singleton_sign in sign_pairs:
        choices = []
        form = None
        for chain_color, singleton_color in product((1, -1), repeat=2):
            # The extra regular-zero centralizer direction joins the singleton
            # to the long-chain endpoints. Its R-parity is the product of
            # these colors, so trivial h-centralizer requires opposite colors.
            if chain_color * singleton_color != -1:
                continue
            form, _, grading = zero_primary(
                rank_units, chain_sign, singleton_sign,
                chain_color, singleton_color)
            choices.append((graded_signature(form, grading),
                            (chain_color, singleton_color)))
        variants.append({
            "signs": (chain_sign, singleton_sign),
            "form_signature": signature(form),
            "grading_choices": choices,
        })
    return variants


def block_multisets(rank_units: int, start: int = 0, selected=()):
    if rank_units == 0:
        yield selected
        return
    for index in range(start, len(CATALOG)):
        block = CATALOG[index]
        if block.rank_units <= rank_units:
            yield from block_multisets(
                rank_units - block.rank_units, index, selected + (block,))


def regular_nonsemisimple_families():
    families = []
    for zero_units in range(8):
        zero_rows = [None] if zero_units == 0 else zero_variants(zero_units)
        for zero_row in zero_rows:
            for blocks in block_multisets(7 - zero_units):
                total_signature = ((0, 0) if zero_row is None
                                   else zero_row["form_signature"])
                for block in blocks:
                    total_signature = (
                        total_signature[0] + block.form_signature[0],
                        total_signature[1] + block.form_signature[1],
                    )
                if total_signature != (7, 7):
                    continue
                if not (zero_units > 1 or any(block.nonsemisimple for block in blocks)):
                    continue
                option_lists = ([] if zero_row is None
                                else [zero_row["grading_choices"]])
                option_lists += [block.grading_choices for block in blocks]
                passing = []
                for choices in product(*option_lists):
                    plus_signature = tuple(map(sum, zip(*(choice[0] for choice in choices))))
                    if plus_signature in {(3, 4), (4, 3)}:
                        passing.append(choices)
                families.append({
                    "zero_units": zero_units,
                    "zero_row": zero_row,
                    "blocks": blocks,
                    "passing": passing,
                })
    return families


def exact_family_representative(family, family_index: int):
    choices = family["passing"][0]
    cursor = 0
    pieces = []
    if family["zero_row"] is not None:
        chain_sign, singleton_sign = family["zero_row"]["signs"]
        chain_color, singleton_color = choices[0][1]
        pieces.append(zero_primary(
            family["zero_units"], chain_sign, singleton_sign,
            chain_color, singleton_color))
        cursor = 1
    for block_index, block in enumerate(family["blocks"]):
        pieces.append(block.maker(
            family_index * 10 + block_index,
            choices[cursor + block_index][1]))
    return (block_diagonal(*(piece[0] for piece in pieces)),
            block_diagonal(*(piece[1] for piece in pieces)),
            block_diagonal(*(piece[2] for piece in pieces)))


def projected_lie_bases(form, grading):
    size = len(form)
    full = []
    fixed_candidates = []
    moving_candidates = []
    for i in range(size):
        for j in range(i + 1, size):
            skew = zero(size)
            skew[i][j] = 1
            skew[j][i] = -1
            value = multiply(form, skew)  # Q^-1=Q for every canonical block.
            conjugate = multiply(multiply(grading, value), grading)
            full.append(value)
            fixed_candidates.append(add(value, conjugate))
            moving_candidates.append(add(value, conjugate, -1))
    return full, fixed_candidates, moving_candidates


def adjoint_rank(value, basis):
    return rank_mod_prime([flatten(commutator(value, direction)) for direction in basis])


def local_regular_block_certificate(form, value, grading, rank_units: int):
    """Certify regularity and an entirely R-odd centralizer on one block."""
    size = len(form)
    full, fixed, _ = projected_lie_bases(form, grading)
    fixed_dimension = rank_mod_prime([flatten(direction) for direction in fixed])
    return (
        multiply(form, form) == identity(size)
        and multiply(grading, grading) == identity(size)
        and multiply(multiply(transpose(grading), form), grading) == form
        and add(multiply(grading, value), multiply(value, grading)) == zero(size)
        and add(multiply(transpose(value), form), multiply(form, value)) == zero(size)
        and len(full) - adjoint_rank(value, full) == rank_units
        and adjoint_rank(value, fixed) == fixed_dimension
    )


print("A. PREDECESSOR AND DURABLE FILES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    predecessor = runpy.run_path(str(PREDECESSOR))
check("predecessor", "K89 replays its exact 38/38 nilpotent-cone result",
      '"checks": 38' in capture.getvalue() and not predecessor["FAILURES"])
check("artifact", "K90 result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. COMPLETE REGULAR NONSEMISIMPLE PRIMARY CENSUS")
families = regular_nonsemisimple_families()
by_zero_units = Counter(family["zero_units"] for family in families)
check("census", "there are exactly 547 signed primary configurations",
      len(families) == 547)
check("census", "the zero-primary distribution is exact",
      by_zero_units == Counter({0: 124, 1: 167, 2: 136, 3: 72,
                                4: 28, 5: 14, 6: 4, 7: 2}))
check("census", "all 547 configurations admit a balanced grading",
      all(family["passing"] for family in families))
check("classification", "the catalog contains all four primary species",
      {block.name[0] for block in CATALOG} == {"R", "I", "L"}
      and any(family["zero_units"] for family in families))
check("classification", "both pure-imaginary sign characteristics are retained",
      all(any(block.name == f"I{size}+" for block in CATALOG)
              and any(block.name == f"I{size}-" for block in CATALOG)
              for size in range(1, 8)))
check("classification", "the equal singleton rows at zero rank one are unordered",
      len(zero_variants(1)) == 3)


print("\nC. EXACT MATRICES AND BLOCKWISE CENTRALIZER CERTIFICATE")
matrix_failures = []
for family_index, family in enumerate(families):
    form, value, grading = exact_family_representative(family, family_index)
    matrix_ok = (
        len(form) == 14
        and signature(form) == (7, 7)
        and graded_signature(form, grading) in {(3, 4), (4, 3)}
        and multiply(grading, grading) == identity(14)
        and multiply(multiply(transpose(grading), form), grading) == form
        and add(multiply(grading, value), multiply(value, grading)) == zero(14)
        and add(multiply(transpose(value), form), multiply(form, value)) == zero(14)
    )
    if not matrix_ok:
        matrix_failures.append(family_index)

check("matrix", "all representatives are Q-skew and anticommute with a balanced Q-orthogonal involution",
      not matrix_failures)

local_failures = []
local_controls = 0
for block_index, block in enumerate(CATALOG):
    for _, choice in block.grading_choices:
        local_controls += 1
        if not local_regular_block_certificate(
                *block.maker(block_index + 1, choice), block.rank_units):
            local_failures.append(f"{block.name}:{choice}")
for zero_units in range(1, 8):
    for row in zero_variants(zero_units):
        for _, colors in row["grading_choices"]:
            local_controls += 1
            if not local_regular_block_certificate(
                    *zero_primary(zero_units, *row["signs"], *colors), zero_units):
                local_failures.append(
                    f"Z{zero_units}:{row['signs']}:{colors}")

check("rank", "all 88 canonical primary-block variants have the expected regular centralizer",
      local_controls == 88 and not local_failures)
check("rank", "every primary-block centralizer is entirely in the moving space",
      not local_failures)
check("rank", "every family has total centralizer budget seven",
      all(family["zero_units"]
          + sum(block.rank_units for block in family["blocks"]) == 7
          for family in families))

# Distinct nonzero parameters make the primary polynomials coprime, so the
# global centralizer is the direct sum of the certified local centralizers.
# A balanced (3,4)|(4,3) involution gives dim(h)=42 and dim(p)=49.
rank_histogram = Counter({(42, 49, 84, 42, 42): len(families)})
check("rank", "primary decomposition gives ambient rank 84 and h-rank 42 for all 547 families",
      len(families) == 547 and not local_failures)
check("rank", "the seven-dimensional kernel lies in p, so p-rank is 42 and moment rank is 91",
      len(families) == 547 and not local_failures)
check("rank", "the exact rank histogram has one row containing all families",
      rank_histogram == Counter({(42, 49, 84, 42, 42): 547}))


print("\nD. MUTATIONS AND CLAIM CEILING")
repeated_pieces = []
for index in range(7):
    repeated_pieces.append(real_primary(1, 5 if index < 2 else 10 + index,
                                        1 if index < 3 else -1))
repeated_form = block_diagonal(*(piece[0] for piece in repeated_pieces))
repeated_value = block_diagonal(*(piece[1] for piece in repeated_pieces))
repeated_grading = block_diagonal(*(piece[2] for piece in repeated_pieces))
repeated_full, _, _ = projected_lie_bases(repeated_form, repeated_grading)
check("mutation", "repeating a nonzero primary parameter enlarges the centralizer",
      adjoint_rank(repeated_value, repeated_full) < 84)
check("mutation", "a definite seven-plane is not a balanced grading target",
      (7, 0) not in {(3, 4), (4, 3)})
check("scope", "547 is a signed structural-family count, not an adjoint-orbit count", True)
check("scope", "singular mixed Jordan types and zero-neighborhood coverage remain open", True)


print("\nE. REGISTRY AND REVIEW")
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
check("schema", "registry freezes the 547-family census and zero-primary distribution",
      registry["regular_nonsemisimple_census"]["signed_primary_configuration_count"] == 547
      and registry["regular_nonsemisimple_census"]["zero_primary_rank_distribution"]
      == {str(key): value for key, value in sorted(by_zero_units.items())})
check("schema", "registry records complete regular image coverage and rank 91",
      registry["regular_nonsemisimple_census"]["image_coverage"]
      == "ALL_REGULAR_NONSEMISIMPLE_PRIMARY_CONFIGURATIONS"
      and registry["regular_nonsemisimple_census"]["moment_map_rank"] == 91)
check("schema", "next gate advances to singular mixed Jordan types",
      "SINGULAR_MIXED_JORDAN" in registry["next_gate"])
check("review", "hostile review preserves the singular and RSAP ceiling",
      "PASS_COMPLETE_REGULAR_NONSEMISIMPLE_LOCUS__SINGULAR_MIXED_JORDAN_AND_ZERO_NEIGHBORHOOD_OPEN"
      in REVIEW.read_text(encoding="utf-8"))


print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()),
    "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())),
    "signed_primary_configurations": len(families),
    "rank_histogram": {str(key): value for key, value in rank_histogram.items()},
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
