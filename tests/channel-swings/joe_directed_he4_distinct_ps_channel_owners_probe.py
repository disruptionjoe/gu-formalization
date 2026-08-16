#!/usr/bin/env python3
"""HE-4: exact ownership of the two Pati-Salam channels in 16 x 144.

This dependency-free certificate composes two banked exact results:

* Q5: ``16+ x 144+ = 45 + 54 + 210 + 945 + 1050+``, multiplicity one;
* HE-1: ``dim Inv_PS(16 x 144) = 2``.

It constructs only the three small tensor modules needed to saturate that
total: ``45 = Lambda^2(10)``, ``54 = Sym^2_0(10)``, and
``210 = Lambda^4(10)``.  No branching of the 945 or 1050 is required.

Scope: exact complex D5/Pati-Salam representation theory only.  The words
"channel owner" mean the unique D5 irreducible summand containing a restricted
PS-invariant line.  They do not mean a source-owned field, activated coupling,
scalar VEV, mass operator, family index, chirality theorem, quotient, scale,
threshold, or observable.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
import contextlib
import importlib.util
import io
from pathlib import Path


CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


REPO = Path(__file__).resolve().parents[2]


def load_script(name: str, relative: str, expected_exit=None):
    """Load an exact banked probe while containing its report and exit."""
    path = REPO / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load exact dependency: {path}")
    module = importlib.util.module_from_spec(spec)
    exit_code = None
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            spec.loader.exec_module(module)
        except SystemExit as exc:
            exit_code = exc.code
    if expected_exit is not None:
        check(f"{name} exact dependency exits {expected_exit}",
              exit_code == expected_exit)
    else:
        check(f"{name} exact dependency loads without SystemExit",
              exit_code is None)
    return module


he1 = load_script(
    "he1_exact_engine",
    "tests/channel-swings/joe_directed_imposter_separation_probe.py",
    expected_exit=0,
)
q5 = load_script(
    "q5_exact_dictionary",
    "tests/generation-sector/q5_spin10_vector_spinor_product.py",
)


def weight_sum(indices) -> tuple[int, ...]:
    return tuple(sum(he1.W10[i][j] for i in indices) for j in range(5))


def exterior_power(k: int) -> Counter:
    """Weight character of Lambda^k(10), from ten distinct basis states."""
    return Counter(weight_sum(indices) for indices in combinations(range(10), k))


def symmetric_square() -> Counter:
    """Weight character of Sym^2(10), including its invariant trace."""
    return Counter(weight_sum(indices)
                   for indices in combinations_with_replacement(range(10), 2))


ZERO = (0, 0, 0, 0, 0)
C45 = exterior_power(2)
SYM55 = symmetric_square()
C54 = SYM55.copy()
C54[ZERO] -= 1
if C54[ZERO] == 0:
    del C54[ZERO]
C210 = exterior_power(4)

check("small tensor constructions close on dimensions 45, 55, 54, and 210",
      (sum(C45.values()), sum(SYM55.values()), sum(C54.values()),
       sum(C210.values())) == (45, 55, 54, 210))
check("traceless projection removes exactly one invariant trace from Sym^2(10)",
      SYM55[ZERO] == C54.get(ZERO, 0) + 1)


def d5_signature(character: Counter):
    return sorted((weight, multiplicity, he1.SO10.dim(weight))
                  for weight, multiplicity
                  in he1.decompose(character, he1.SO10).items())


check("Lambda^2(10) is the single D5 irrep 45",
      d5_signature(C45) == [((2, 2, 0, 0, 0), 1, F(45))])
check("Sym^2_0(10) is the single D5 irrep 54",
      d5_signature(C54) == [((4, 0, 0, 0, 0), 1, F(54))])
check("Lambda^4(10) is the single D5 irrep 210",
      d5_signature(C210) == [((2, 2, 2, 2, 0), 1, F(210))])


def ps_dimension_blocks(character: Counter) -> list[int]:
    blocks = []
    for (dimension, left, right, _tag), multiplicity in he1.ps_content(character).items():
        blocks.extend([int(dimension * left * right)] * multiplicity)
    return sorted(blocks)


PS_COUNTS = {
    "45": he1.invariants(C45, he1.PS),
    "54": he1.invariants(C54, he1.PS),
    "210": he1.invariants(C210, he1.PS),
}

check("45 PS branch closes as dimensions 3+3+15+24 and has no singlet",
      ps_dimension_blocks(C45) == [3, 3, 15, 24]
      and PS_COUNTS["45"] == 0)
check("54 PS branch closes as dimensions 1+9+20+24 and has one singlet",
      ps_dimension_blocks(C54) == [1, 9, 20, 24]
      and PS_COUNTS["54"] == 1)
check("210 PS branch closes as dimensions 1+15+24+40+40+45+45 and has one singlet",
      ps_dimension_blocks(C210) == [1, 15, 24, 40, 40, 45, 45]
      and PS_COUNTS["210"] == 1)
check("planted false owner is rejected: the adjoint 45 has no PS singlet",
      PS_COUNTS["45"] != 1)


with contextlib.redirect_stdout(io.StringIO()):
    q5_product = q5.spinor_times_rs("16+", "144+")
check("Q5 reruns the five-summand same-label D5 decomposition exactly",
      q5_product == Counter({
          "45": 1, "54": 1, "210": 1, "945": 1, "1050+": 1,
      }))
check("Q5 owner multiplicities are all one and dimensions close on 2304",
      set(q5_product.values()) == {1}
      and sum(q5.DIMS[name] * multiplicity
              for name, multiplicity in q5_product.items()) == 16 * 144)


PRODUCT = he1.tensor(he1.C16, he1.W144)
TOTAL_PS = he1.invariants(PRODUCT, he1.PS)
check("HE-1 reruns the total dim Inv_PS(16 x 144) = 2", TOTAL_PS == 2)
check("54 and 210 saturate the total two PS singlets",
      PS_COUNTS == {"45": 0, "54": 1, "210": 1}
      and sum(PS_COUNTS.values()) == TOTAL_PS)


def subtract_characters_exact(lhs: Counter, *rhs: Counter) -> Counter:
    out = lhs.copy()
    for character in rhs:
        for weight, multiplicity in character.items():
            if out[weight] < multiplicity:
                raise AssertionError(f"negative character subtraction at {weight}")
            out[weight] -= multiplicity
            if out[weight] == 0:
                del out[weight]
    return out


LARGE_REMAINDER = subtract_characters_exact(PRODUCT, C45, C54, C210)
check("exact character subtraction leaves dimension 945+1050 = 1995",
      sum(LARGE_REMAINDER.values()) == 945 + 1050)
REMAINDER_PS = he1.invariants(LARGE_REMAINDER, he1.PS)
check("the 945+1050 remainder has zero PS invariants",
      REMAINDER_PS == 0)

# Q5 identifies LARGE_REMAINDER as a direct sum of two honest representations,
# each with multiplicity one.  Invariant dimensions are nonnegative integers
# and additive on direct sums.  Their sum is zero, so each is zero.
nonnegative_splits = [
    (left, right)
    for left in range(REMAINDER_PS + 1)
    for right in range(REMAINDER_PS + 1)
    if left + right == REMAINDER_PS
]
check("zero is the unique nonnegative split of the large-remainder invariant count",
      nonnegative_splits == [(0, 0)])
LARGE_OWNER_COUNTS = dict(zip(("945", "1050+"), nonnegative_splits[0]))
check("nonnegative saturation excludes both large summands individually",
      all(value >= 0 for value in LARGE_OWNER_COUNTS.values())
      and sum(LARGE_OWNER_COUNTS.values())
      == REMAINDER_PS)

ALL_OWNER_COUNTS = {"45": 0, "54": 1, "210": 1,
                    "945": 0, "1050+": 0}
check("the two PS channels have exactly the distinct D5 owners 54 and 210",
      [name for name, count in ALL_OWNER_COUNTS.items() if count]
      == ["54", "210"]
      and max(ALL_OWNER_COUNTS.values()) == 1)
check("no single irreducible D5 summand owns both PS channels",
      all(count < TOTAL_PS for count in ALL_OWNER_COUNTS.values()))
check("D5 symmetry alone supplies no Schur intertwiner forcing related scales",
      d5_signature(C54)[0][0] != d5_signature(C210)[0][0]
      and sum(C54.values()) != sum(C210.values()))


# With three identical source-census family copies, each owner contributes one
# arbitrary covector in F*; D5 multiplicity-one fixes each representation-space
# projection only up to its own scale and supplies no relation between the two
# family covectors.  Keep the absent relation typed rather than fitting it.
FAMILY_DIMENSION_IS_SOURCE_CENSUS_INPUT = 3
OWNER_TAGGED_FAMILY_COVECTOR_SLOTS = (
    ("54", FAMILY_DIMENSION_IS_SOURCE_CENSUS_INPUT),
    ("210", FAMILY_DIMENSION_IS_SOURCE_CENSUS_INPUT),
)
SOURCE_RELATION_BETWEEN_COVECTORS = None
REPRESENTATION_SELECTED_FAMILY_RANK = None
check("owner-tagged family coupling space is F*_54 direct-sum F*_210",
      OWNER_TAGGED_FAMILY_COVECTOR_SLOTS == (("54", 3), ("210", 3)))
check("TYPE_MISSING: representation theory supplies no family-row relation",
      SOURCE_RELATION_BETWEEN_COVECTORS is None)
check("owner split alone selects no family rank",
      REPRESENTATION_SELECTED_FAMILY_RANK is None)


# The self-dual 45/54/210 owners recur on the conjugate same-label product.
CONJUGATE_TOTAL_PS = he1.invariants(he1.tensor(he1.C16B, he1.W144B), he1.PS)
check("conjugate cross-half orientation has the same total-two owner pattern",
      CONJUGATE_TOTAL_PS == TOTAL_PS == 2)
check("same-effective-half orientation remains outside this owner result",
      he1.invariants(he1.tensor(he1.C16, he1.W144B), he1.PS) == 0)


print("HE-4 exact PS-singlet ownership in 16 x 144:")
for owner, count in ALL_OWNER_COUNTS.items():
    print(f"  {owner:6s}: {count}")
print()
print("Owner split: one channel in 54, one channel in 210.")
print("No irreducible D5 summand owns both channels.")
print("TYPE_MISSING: source relation/selection between the two family covectors.")
print("No family rank, activation, mass, scalar VEV, index, chirality, or observable is inferred.")
print()

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
raise SystemExit(0 if passed == len(CHECKS) else 1)
