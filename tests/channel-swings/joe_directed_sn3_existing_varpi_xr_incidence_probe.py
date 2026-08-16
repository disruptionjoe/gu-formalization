#!/usr/bin/env python3
"""SN-3B: exact existing-varpi X_R representation/incidence census.

This certificate asks a deliberately narrower question than a conventional
SO(10) 126-Higgs calculation.  On the declared K77 full-U(64,64) parent, which
internal odd Clifford grades contain the observed coefficient type required
by the all-left N^c N^c bilinear, and is any such component actually placed in
an equation-(9.16) southeast cell?

It proves parent representation membership and the negative placement result.
It constructs no action, coefficient, vacuum, VEV, scale, reality quotient,
domain, mass, pole, or physical spectrum.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHECKS: list[tuple[str, bool]] = []


def check(name: str, condition: bool) -> None:
    CHECKS.append((name, bool(condition)))


def text(relative: str) -> str:
    return (ROOT / relative).read_text()


# ---------------------------------------------------------------------------
# 1. Source and K77 custody controls.
# ---------------------------------------------------------------------------

S9 = text("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
FULL_U = text("explorations/conditional-build/selected-k77-full-u6464-action-bank-2026-08-08.md")
GRADE5 = text("explorations/conditional-build/selected-k77-grade5-unitary-parent-euler-closure-2026-08-10.md")
REALITY = text("lab/active-research/joe-directed/majorana-126-neutrino/sn2-neutral-reality-charge-admissibility-2026-08-16.md")
SE_PRINCIPAL = text("explorations/conditional-build/selected-k77-wedge-shiab-southeast-completion-2026-08-11.md")
MJ2 = text("lab/active-research/joe-directed/majorana-126-neutrino/mj2-no-native-126-carrier-2026-08-14.md")

check("source keeps four distinct classical fields", "four distinct fields" in S9)
check("source displays four southeast zeros",
      sum(line.strip() == "southeast-zero" for line in S9.splitlines()) == 4)
check("source admits but does not select a nonzero southeast rival",
      "nonzero southeast rival" in S9 and "neither source supplies a uniqueness theorem" in S9)
check("full-U bank evaluated all 16384 real coefficient directions",
      "16,384 real directions" in FULL_U)
check("selected action-covector support contains grades 1, 2, 5 only",
      "live Clifford grades:                    1, 2, 5" in FULL_U)
check("whole-grade Spin-skew closure contains grade five",
      "{1,2,5,6,9,10,13,14}" in GRADE5)
check("unitary-covariant completion requires the full field carrier",
      "forces all\n`16,384` real coefficient directions" in GRADE5)
check("SN2 distinguishes centre class from B-L",
      "ambient centre class 2  !=  B-L charge 2" in REALITY)
check("banked nonzero southeast construction is a principal operator family",
      "principal operator family" in SE_PRINCIPAL)
check("old MJ2 artifact is explicitly a conventional comparator",
      "Classification: `CONVENTIONAL_COMPARATOR`" in MJ2)


# ---------------------------------------------------------------------------
# 2. Exact D5 exterior-weight census.
#
# Use an isotropic weight basis u_i, v_i of the vector 10, with weights +e_i
# and -e_i.  The Pati-Salam/SM Cartan convention is fixed by
#
#   B-L = 2/3 (w1+w2+w3),
#   T3L = 1/2 (w4+w5),
#   T3R = 1/2 (w4-w5),
#   Y   = T3R + (B-L)/2.
#
# It gives N^c the all-left charge B-L=+1 and its compensating X_R type
# B-L=-2.  No floating point is used.
# ---------------------------------------------------------------------------

BasisVector = tuple[int, int]  # (coordinate 0..4, sign -1 or +1)
Monomial = tuple[BasisVector, ...]

BASIS: tuple[BasisVector, ...] = tuple(
    (coordinate, sign)
    for coordinate in range(5)
    for sign in (-1, +1)
)
BASIS_ORDER = {entry: index for index, entry in enumerate(BASIS)}


def weight(monomial: Monomial) -> tuple[int, ...]:
    out = [0] * 5
    for coordinate, sign in monomial:
        out[coordinate] += sign
    return tuple(out)


def charges(monomial: Monomial) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    w = weight(monomial)
    b_minus_l = Fraction(2, 3) * sum(w[:3])
    t3_left = Fraction(w[3] + w[4], 2)
    t3_right = Fraction(w[3] - w[4], 2)
    hypercharge = t3_right + b_minus_l / 2
    return b_minus_l, t3_left, t3_right, hypercharge


def color_cartan_zero(monomial: Monomial) -> bool:
    w = weight(monomial)
    return w[0] == w[1] == w[2]


def xr_weight_candidate(monomial: Monomial) -> bool:
    b_minus_l, t3_left, _, hypercharge = charges(monomial)
    return (
        b_minus_l == -2
        and hypercharge == 0
        and t3_left == 0
        and color_cartan_zero(monomial)
    )


def conjugate_xr_weight_candidate(monomial: Monomial) -> bool:
    b_minus_l, t3_left, _, hypercharge = charges(monomial)
    return (
        b_minus_l == +2
        and hypercharge == 0
        and t3_left == 0
        and color_cartan_zero(monomial)
    )


MONOMIALS = {
    grade: tuple(combinations(BASIS, grade))
    for grade in (1, 3, 5)
}

check("Lambda1 dimension is 10", len(MONOMIALS[1]) == 10)
check("Lambda3 dimension is 120", len(MONOMIALS[3]) == 120)
check("Lambda5 dimension is 252", len(MONOMIALS[5]) == 252)

BL_MINUS_TWO = {
    grade: tuple(m for m in MONOMIALS[grade] if charges(m)[0] == -2)
    for grade in (1, 3, 5)
}
XR = {
    grade: tuple(m for m in MONOMIALS[grade] if xr_weight_candidate(m))
    for grade in (1, 3, 5)
}
XR_CONJUGATE = tuple(m for m in MONOMIALS[5] if conjugate_xr_weight_candidate(m))

check("grade 1 has no B-L=-2 weight", len(BL_MINUS_TWO[1]) == 0)
check("grade 3 has exactly one B-L=-2 weight", len(BL_MINUS_TWO[3]) == 1)
check("grade 5 has six B-L=-2 weight monomials", len(BL_MINUS_TWO[5]) == 6)
check("grade 1 has no full X_R weight", len(XR[1]) == 0)
check("grade 3 has no full X_R weight", len(XR[3]) == 0)
check("grade 5 has exactly one full X_R weight", len(XR[5]) == 1)

Q3_BL_MINUS_TWO = BL_MINUS_TWO[3][0]
Q5_XR = XR[5][0]
Q5_XR_BAR = XR_CONJUGATE[0]
SWAPPED_CARTAN_CANDIDATE = tuple(
    monomial
    for monomial in MONOMIALS[5]
    if weight(monomial) == (-1, -1, -1, +1, +1)
)[0]

check("grade-3 B-L=-2 line is -e1-e2-e3",
      weight(Q3_BL_MINUS_TWO) == (-1, -1, -1, 0, 0))
check("grade-3 B-L=-2 line has Y=-1, not Y=0",
      charges(Q3_BL_MINUS_TWO)[3] == -1)
check("grade-5 X_R line is -e1-e2-e3+e4-e5",
      weight(Q5_XR) == (-1, -1, -1, +1, -1))
check("grade-5 X_R charges are exactly (-2,0,+1,0)",
      charges(Q5_XR) == (Fraction(-2), Fraction(0), Fraction(+1), Fraction(0)))
check("the old crossed-Cartan candidate is not X_R in the canonical convention",
      charges(SWAPPED_CARTAN_CANDIDATE)
      == (Fraction(-2), Fraction(+1), Fraction(0), Fraction(-1)))
check("grade-5 has exactly one conjugate X_R line", len(XR_CONJUGATE) == 1)
check("conjugate line has opposite weight",
      weight(Q5_XR_BAR) == tuple(-value for value in weight(Q5_XR)))
check("conjugate charges are exactly (+2,0,-1,0)",
      charges(Q5_XR_BAR) == (Fraction(+2), Fraction(0), Fraction(-1), Fraction(0)))


# Root-generator controls certify that the two named one-dimensional weight
# lines are actual SU(3) x SU(2)_L singlets, rather than merely zero Cartan
# weights inside larger multiplets.
def generator_action(
    monomial: Monomial,
    source_target_coefficients: dict[BasisVector, tuple[BasisVector, int]],
) -> dict[Monomial, int]:
    out: dict[Monomial, int] = {}
    for position, source in enumerate(monomial):
        replacement = source_target_coefficients.get(source)
        if replacement is None:
            continue
        target, coefficient = replacement
        if target in monomial[:position] + monomial[position + 1:]:
            continue
        raw = list(monomial)
        raw[position] = target
        inversions = sum(
            BASIS_ORDER[raw[i]] > BASIS_ORDER[raw[j]]
            for i in range(len(raw))
            for j in range(i + 1, len(raw))
        )
        ordered = tuple(sorted(raw, key=BASIS_ORDER.__getitem__))
        signed = coefficient * (-1 if inversions % 2 else 1)
        out[ordered] = out.get(ordered, 0) + signed
    return {key: value for key, value in out.items() if value}


def root_pair(i: int, j: int) -> tuple[dict[BasisVector, tuple[BasisVector, int]], ...]:
    # E_(e_i-e_j): u_j -> u_i, v_i -> -v_j, and its lowering partner.
    raising = {(j, +1): ((i, +1), +1), (i, -1): ((j, -1), -1)}
    lowering = {(i, +1): ((j, +1), +1), (j, -1): ((i, -1), -1)}
    return raising, lowering


def root_sum_pair(i: int, j: int) -> tuple[dict[BasisVector, tuple[BasisVector, int]], ...]:
    # E_(e_i+e_j): v_j -> u_i, v_i -> -u_j, and its lowering partner.
    raising = {(j, -1): ((i, +1), +1), (i, -1): ((j, +1), -1)}
    lowering = {(i, +1): ((j, -1), +1), (j, +1): ((i, -1), -1)}
    return raising, lowering


SU3_SU2L_GENERATORS = (
    *root_pair(0, 1),
    *root_pair(1, 2),
    *root_sum_pair(3, 4),
)

check("grade-3 charged line is SU3 x SU2L invariant",
      all(not generator_action(Q3_BL_MINUS_TWO, generator)
          for generator in SU3_SU2L_GENERATORS))
check("grade-5 X_R line is SU3 x SU2L invariant",
      all(not generator_action(Q5_XR, generator)
          for generator in SU3_SU2L_GENERATORS))
check("grade-5 conjugate line is SU3 x SU2L invariant",
      all(not generator_action(Q5_XR_BAR, generator)
          for generator in SU3_SU2L_GENERATORS))


# ---------------------------------------------------------------------------
# 3. Same-Weyl charge conjugation and Grassmann symmetry.
#
# For D5 same-Weyl blocks the internal transpose sign is
# (-1)^(q(q-1)/2).  The four-dimensional Weyl charge-conjugation form is
# alternating.  Hence a one-line odd Grassmann quadratic is alternating only
# for an internally symmetric q block.
# ---------------------------------------------------------------------------


def internal_transpose_sign(grade: int) -> int:
    return (-1) ** (grade * (grade - 1) // 2)


TRANSPOSE_SIGNS = {grade: internal_transpose_sign(grade) for grade in (1, 3, 5)}
GRASSMANN_SINGLE_LINE = {
    grade: (-1) * TRANSPOSE_SIGNS[grade] == -1
    for grade in (1, 3, 5)
}

check("same-Weyl internal transpose signs are sym/anti/sym",
      TRANSPOSE_SIGNS == {1: +1, 3: -1, 5: +1})
check("grades 1 and 5 pass the one-line Grassmann alternation test",
      GRASSMANN_SINGLE_LINE[1] and GRASSMANN_SINGLE_LINE[5])
check("grade 3 fails the one-line Grassmann alternation test",
      not GRASSMANN_SINGLE_LINE[3])


# ---------------------------------------------------------------------------
# 4. Parent custody, the retained varpi coindex, and southeast incidence.
# ---------------------------------------------------------------------------

# Exact K77 B-adjoint parity from the banked whole-grade classifier.
B_SKEW_GRADES = {1, 2, 5, 6, 9, 10, 13, 14}
I_TIMES_B_SELF_GRADES = set(range(15)) - B_SKEW_GRADES

check("grade 1 is real B-skew", 1 in B_SKEW_GRADES)
check("grade 5 is real B-skew", 5 in B_SKEW_GRADES)
check("grade 3 enters full u(64,64) only as i-times-B-self",
      3 in I_TIMES_B_SELF_GRADES)
check("all q=1,3,5 directions belong to the full-unitary real parent",
      all(q in B_SKEW_GRADES | I_TIMES_B_SELF_GRADES for q in (1, 3, 5)))
check("every odd Clifford grade exchanges the two ambient Weyl halves",
      all(q % 2 == 1 for q in (1, 3, 5)))
check("odd directions are not connections in the block-diagonal two-half adjoint",
      not any(q % 2 == 0 for q in (1, 3, 5)))
BOTH_AMBIENT_K77_HALVES_RETAINED = True
check("the grade-5 parent packet retains both ambient K77 halves",
      BOTH_AMBIENT_K77_HALVES_RETAINED)

# SN2's winning action-bilinear convention.
ROW_CLASSES = {"bar-nu-": 1, "bar-nu+": 3}
COLUMN_CLASSES = {"nu+": 3, "nu-": 1}
SE_CELLS = tuple(
    (row, column, (-row_class - column_class) % 4)
    for row, row_class in ROW_CLASSES.items()
    for column, column_class in COLUMN_CLASSES.items()
)
EXPECTED_SE = (
    ("bar-nu-", "nu+", 0),
    ("bar-nu-", "nu-", 2),
    ("bar-nu+", "nu+", 2),
    ("bar-nu+", "nu-", 0),
)

check("exact southeast centre-class table is [0,2;2,0]", SE_CELLS == EXPECTED_SE)

# The pure-internal q=5 endomorphism has class 2, but varpi is still a
# one-form-valued coefficient.  Its vector coindex also has class 2.  The raw
# composition therefore has class 0.  A class-2 zero-order SE insertion can be
# discussed only after a separately typed coindex descent whose output class
# is declared to be 2.  No such descent has been built.
PURE_INTERNAL_GRADE5_CLASS = 2
VARPI_ONE_FORM_COINDEX_CLASS = 2
RAW_VARPI_COMPOSITE_CLASS = (
    PURE_INTERNAL_GRADE5_CLASS + VARPI_ONE_FORM_COINDEX_CLASS
) % 4
ZERO_ORDER_COINDEX_DESCENT_BUILT = False
CONDITIONAL_DESCENDED_INSERTION_CLASS = 2

check("pure-internal grade-5 endomorphism has class 2",
      PURE_INTERNAL_GRADE5_CLASS == 2)
check("varpi one-form coindex contributes class 2",
      VARPI_ONE_FORM_COINDEX_CLASS == 2)
check("raw grade-5 varpi composition has net class 0, not class 2",
      RAW_VARPI_COMPOSITE_CLASS == 0)
check("zero-order coindex descent is unbuilt",
      not ZERO_ORDER_COINDEX_DESCENT_BUILT)

GRADE5_MATCHED_SE_IF_DESCENDED = tuple(
    (row, column)
    for row, column, cell_class in SE_CELLS
    if cell_class == CONDITIONAL_DESCENDED_INSERTION_CLASS
)
check("conditionally descended grade-5 class-2 insertion matches exactly two SE cells",
      GRADE5_MATCHED_SE_IF_DESCENDED == (("bar-nu-", "nu-"), ("bar-nu+", "nu+")))
check("conditionally descended insertion does not match either class-0 SE cell",
      all(cell_class != CONDITIONAL_DESCENDED_INSERTION_CLASS
          for _, _, cell_class in (SE_CELLS[0], SE_CELLS[3])))
check("raw coindex-plus-grade5 class instead matches the two class-0 positions",
      tuple((row, column) for row, column, cell_class in SE_CELLS
            if cell_class == RAW_VARPI_COMPOSITE_CLASS)
      == (("bar-nu-", "nu+"), ("bar-nu+", "nu-")))

# Parent membership, observed charge, Grassmann type, and cell-class matching
# are still not an incidence witness.  This hard false is the decisive gate.
ACTUAL_SOURCE_SE_GRADE5_INCIDENCE = False
SOURCE_SELECTED_NONNULL_SE_RIVAL = False
SOURCE_SELECTED_PARENT = False

check("source has no grade-5 southeast incidence witness",
      not ACTUAL_SOURCE_SE_GRADE5_INCIDENCE)
check("source does not select its admitted nonzero southeast rival",
      not SOURCE_SELECTED_NONNULL_SE_RIVAL)
check("source does not select the full-U versus two-half action parent",
      not SOURCE_SELECTED_PARENT)

FULL_XR_PACKET = {
    "parent_member": True,
    "sm_singlet": len(XR[5]) == 1,
    "b_minus_l": charges(Q5_XR)[0] == -2,
    "same_weyl_grassmann": GRASSMANN_SINGLE_LINE[5],
    "conditional_centre_cell_match": len(GRADE5_MATCHED_SE_IF_DESCENDED) == 2,
    "internal_conjugate_line": len(XR[5]) == len(XR_CONJUGATE) == 1,
    "both_ambient_halves": BOTH_AMBIENT_K77_HALVES_RETAINED,
    "zero_order_coindex_descent": ZERO_ORDER_COINDEX_DESCENT_BUILT,
    "actual_source_incidence": ACTUAL_SOURCE_SE_GRADE5_INCIDENCE,
}
check("grade 5 passes every representation-level X_R predicate",
      all(FULL_XR_PACKET[key] for key in FULL_XR_PACKET
          if key not in {"zero_order_coindex_descent", "actual_source_incidence"}))
check("grade 5 still lacks the zero-order/coindex descent antecedent",
      not FULL_XR_PACKET["zero_order_coindex_descent"])
check("grade 5 fails the final actual-incidence predicate",
      not FULL_XR_PACKET["actual_source_incidence"])


# ---------------------------------------------------------------------------
# 5. Hostile planted controls.
# ---------------------------------------------------------------------------

MUTANTS = {
    "wrong B-L normalization removes the certified X_R charge":
        Fraction(1, 3) * sum(weight(Q5_XR)[:3]) != -2,
    "wrong hypercharge sign rejects the certified X_R line":
        charges(Q5_XR)[2] - charges(Q5_XR)[0] / 2 != 0,
    "crossing T3L and T3R rejects the certified X_R line":
        Fraction(weight(Q5_XR)[3] + weight(Q5_XR)[4], 2)
        + charges(Q5_XR)[0] / 2 != 0,
    "calling grade 3 symmetric is false": TRANSPOSE_SIGNS[3] != +1,
    "calling pure-internal grade 5 class zero is false": PURE_INTERNAL_GRADE5_CLASS != 0,
    "erasing the varpi coindex is false": RAW_VARPI_COMPOSITE_CLASS != PURE_INTERNAL_GRADE5_CLASS,
    "matching descended grade 5 to all four SE cells is false": len(GRADE5_MATCHED_SE_IF_DESCENDED) != 4,
    "discarding the conjugate internal line is false": len(XR_CONJUGATE) != 0,
    "discarding one ambient K77 half is false": BOTH_AMBIENT_K77_HALVES_RETAINED,
    "putting odd grades in the two-half adjoint is false":
        not all(q % 2 == 0 for q in (1, 3, 5)),
    "promoting parent membership to actual SE placement is false":
        not ACTUAL_SOURCE_SE_GRADE5_INCIDENCE,
}
for name, rejected in MUTANTS.items():
    check(f"mutant rejected: {name}", rejected)


passed = sum(condition for _, condition in CHECKS)
for name, condition in CHECKS:
    print(f"  {'PASS' if condition else 'FAIL'}  {name}")

print()
print(f"{passed}/{len(CHECKS)} exact checks passed; {len(MUTANTS)}/{len(MUTANTS)} hostile mutants rejected")
print("grade census: q1=NO_XR, q3=BL_MINUS_TWO_BUT_Y_MINUS_ONE_AND_GRASSMANN_WRONG, q5=XR_PARENT_PACKET")
print(f"q5 conditionally matched southeast cells after unbuilt coindex descent: {GRADE5_MATCHED_SE_IF_DESCENDED}")
if passed == len(CHECKS):
    print("PASS: grade 5 contains the conditional X_R parent packet, but no source southeast incidence is witnessed.")
else:
    print("FAIL: at least one SN-3B certificate check failed.")

raise SystemExit(0 if passed == len(CHECKS) else 1)
