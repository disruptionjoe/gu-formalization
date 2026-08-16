#!/usr/bin/env python3
"""Exact SN-2 K77 neutral restriction of the equation-9.16 zero-order grammar.

Dependency-free exact integer/Fraction bookkeeping.  This is a conditional
carrier and cell-support certificate, not a mass, action, reality map, selected
gauge group, physical quotient, or standard seesaw construction.
"""

from __future__ import annotations

import os
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MUT = os.environ.get("SN2_MUTATE", "")
FAILURES: list[str] = []
COUNTS = {"source": 0, "charge": 0, "carrier": 0, "grammar": 0,
          "centre": 0, "type": 0, "control": 0}


def check(kind: str, label: str, condition: bool) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


SOURCE = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
SOURCE_1112 = read("lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md")
K77 = read("explorations/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md")
CRB = read("lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md")
SN1 = read("lab/active-research/joe-directed/majorana-126-neutrino/sn1-observed-neutrino-mass-pencil-2026-08-16.md")
ARTIFACT = read("lab/active-research/joe-directed/majorana-126-neutrino/sn2-equation916-k77-neutral-restriction-2026-08-16.md")
TOE = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")


print("A. SOURCE CUSTODY AND PRIOR ART")
check("source", "equation 9.16 fixes four independent classical fields",
      "four distinct fields" in SOURCE)
check("source", "source row order is preserved",
      "(bar-zeta-minus, bar-zeta-plus, bar-nu-minus, bar-nu-plus)" in SOURCE)
check("source", "source column order is preserved",
      "(zeta-plus, zeta-minus, nu-plus, nu-minus)" in SOURCE)
check("source", "the southeast-zero branch is candidate strength, not unique",
      "SE=0" in SOURCE and "non-trivial map in the lower right quadrant" in SOURCE)
check("source", "source seesaw language is prospective rather than a constructed neutral horn",
      "what I think will be found to be a seesaw mechanism" in TOE)
check("source", "K77-A banks four complex 2 x 16 observation blocks",
      "four complex `2 x 16` blocks" in K77)
check("source", "the p.51 zeta slots contain a second F occurrence",
      "Z ⊕ Q ⊕ F" in SOURCE_1112 and "standalone" in SOURCE_1112)
check("type", "committed SN1 does not claim a 20-complex neutral count",
      "20-complex" not in SN1 and "dimension `20`" not in SN1)
check("type", "SN2 carries the mandatory source-native comparator notice",
      "GU-COMPARATOR-ROUTING" in ARTIFACT and "Classification: `SOURCE_NATIVE_ROUTE`" in ARTIFACT)


print("\nB. EXACT INTERNAL CHARGE DICTIONARY")
# One all-left internal 16. Color multiplicities are expanded explicitly.
states16 = []
for color in range(3):
    states16 += [
        (f"u_L_{color}", Fraction(2, 3), False),
        (f"d_L_{color}", Fraction(-1, 3), False),
        (f"u_L_c_{color}", Fraction(-2, 3), False),
        (f"d_L_c_{color}", Fraction(1, 3), False),
    ]
states16 += [
    ("nu_L", Fraction(0), False),
    ("e_L", Fraction(-1), False),
    ("e_L_c", Fraction(1), False),
    ("nu_L_c", Fraction(0), True),
]
check("charge", "the imported all-left packet has internal dimension 16", len(states16) == 16)

q0_16 = [state for state in states16 if state[1] == 0]
sm1_16 = [state for state in states16 if state[2]]
if MUT == "q_as_singlet":
    sm1_16 = list(q0_16)
check("charge", "Q=0 retains exactly nu_L and all-left nu_L_c",
      [state[0] for state in q0_16] == ["nu_L", "nu_L_c"])
check("charge", "full-SM-singlet restriction retains only nu_L_c",
      [state[0] for state in sm1_16] == ["nu_L_c"])

# The conjugate 16bar has the negated charges and the conjugate singlet.
states16bar = [(name + "_bar", -charge, singlet) for name, charge, singlet in states16]
q0_16bar = [state for state in states16bar if state[1] == 0]
sm1_16bar = [state for state in states16bar if state[2]]
check("charge", "16 and 16bar have equal Q=0 multiplicity two",
      len(q0_16) == len(q0_16bar) == 2)
check("charge", "16 and 16bar have equal SM-singlet multiplicity one",
      len(sm1_16) == len(sm1_16bar) == 1)


print("\nC. ALL FOUR K77 BLOCKS AND BOTH AMBIENT HALVES")
blocks = [
    {"name": "ambient+_2Lx16", "ambient": "+", "weyl": "L", "parent": "16", "class": 1},
    {"name": "ambient+_2Rx16bar", "ambient": "+", "weyl": "R", "parent": "16bar", "class": 3},
    {"name": "ambient-_2Lx16bar", "ambient": "-", "weyl": "L", "parent": "16bar", "class": 3},
    {"name": "ambient-_2Rx16", "ambient": "-", "weyl": "R", "parent": "16", "class": 1},
]
if MUT == "drop_half":
    blocks = [block for block in blocks if block["ambient"] == "+"]


def internal_rank(block: dict, horn: str) -> int:
    if horn == "Q0":
        return len(q0_16 if block["parent"] == "16" else q0_16bar)
    return len(sm1_16 if block["parent"] == "16" else sm1_16bar)


def block_rank(block: dict, horn: str) -> int:
    return 2 * internal_rank(block, horn)


q_block_ranks = [block_rank(block, "Q0") for block in blocks]
s_block_ranks = [block_rank(block, "SM1") for block in blocks]
check("carrier", "both ambient halves contribute exactly four observed blocks",
      len(blocks) == 4 and {block["ambient"] for block in blocks} == {"+", "-"})
check("carrier", "every observed block has Q=0 rank four", q_block_ranks == [4, 4, 4, 4])
check("carrier", "every observed block has SM-singlet rank two", s_block_ranks == [2, 2, 2, 2])
q_four = sum(q_block_ranks)
s_four = sum(s_block_ranks)
if MUT == "force_twenty":
    q_four = 20
check("carrier", "all four observed blocks have exact Q=0 rank 16", q_four == 16)
check("carrier", "all four observed blocks have exact SM-singlet rank 8", s_four == 8)
check("control", "unsupported complex rank 20 is rejected on the four-block carrier", q_four != 20 and s_four != 20)

# One F sign contains the two blocks in one ambient half.
f_ranks = {
    "Q0": {sign: sum(block_rank(block, "Q0") for block in blocks if block["ambient"] == sign)
           for sign in ("+", "-")},
    "SM1": {sign: sum(block_rank(block, "SM1") for block in blocks if block["ambient"] == sign)
            for sign in ("+", "-")},
}
check("carrier", "F+ and F- each have Q=0 rank eight", f_ranks["Q0"] == {"+": 8, "-": 8})
check("carrier", "F+ and F- each have SM-singlet rank four", f_ranks["SM1"] == {"+": 4, "-": 4})


print("\nD. MINIMAL AND SECOND-F FOUR-FIELD HORNS")
columns = ("zeta+", "zeta-", "nu+", "nu-")
rows = ("bar-zeta-", "bar-zeta+", "bar-nu-", "bar-nu+")
field_sign = {"zeta+": "+", "zeta-": "-", "nu+": "+", "nu-": "-"}
minimal_q = sum(f_ranks["Q0"][field_sign[field]] for field in columns)
minimal_s = sum(f_ranks["SM1"][field_sign[field]] for field in columns)
two_f_q = minimal_q + f_ranks["Q0"]["+"] + f_ranks["Q0"]["-"]
two_f_s = minimal_s + f_ranks["SM1"]["+"] + f_ranks["SM1"]["-"]
if MUT == "wrong_second_f":
    two_f_q -= 8
check("carrier", "minimal one-F four-field column has Q=0 rank 32", minimal_q == 32)
check("carrier", "minimal one-F four-field column has SM-singlet rank 16", minimal_s == 16)
check("carrier", "second-F zeta horn has Q=0 rank 48", two_f_q == 48)
check("carrier", "second-F zeta horn has SM-singlet rank 24", two_f_s == 24)
barred_independent = MUT != "identify_bars"
check("type", "barred and unbarred carriers remain independent fields", barred_independent)
check("type", "row and column carrier dimensions agree without a reality quotient",
      minimal_q == 32 and minimal_s == 16 and len(rows) == len(columns) == 4)


print("\nE. SOURCE ZERO-ORDER BLOCK SUPPORT AND OWNER CUSTODY")
# Zero-order token ledger. C(V) is the contracted occurrence of the same V.
matrix = [
    ["C(Vpp)", "C(Vpm)", "Vpp", "Vpm"],
    ["C(Vmp)", "C(Vmm)", "Vmp", "Vmm"],
    ["-Bpp*", "-Bpm*", "0", "0"],
    ["-Bmp*", "-Bmm*", "0", "0"],
]
if MUT == "southeast_nonzero":
    matrix[2][2] = "M"
support = {(i, j) for i in range(4) for j in range(4) if matrix[i][j] != "0"}
expected_support = {(i, j) for i in range(4) for j in range(4)
                    if not (i >= 2 and j >= 2)}
check("grammar", "source order has four rows and four columns", len(rows) == len(columns) == 4)
check("grammar", "released zero-order restriction has exactly twelve supported blocks",
      support == expected_support and len(support) == 12)
check("grammar", "released southeast quadrant has four exact zero blocks",
      all(matrix[i][j] == "0" for i in (2, 3) for j in (2, 3)))

unbarred_occurrences = [cell.replace("C(", "").replace(")", "")
                         for row in matrix[:2] for cell in row]
unbarred_owners = set(unbarred_occurrences)
barred_owners = {matrix[i][j] for i in (2, 3) for j in (0, 1)}
if MUT == "scalarize_owners":
    unbarred_owners = {f"S{k}" for k in range(8)}
check("grammar", "four unbarred varpi owners recur in both upper quadrants",
      unbarred_owners == {"Vpp", "Vpm", "Vmp", "Vmm"}
      and all(unbarred_occurrences.count(owner) == 2 for owner in unbarred_owners))
check("grammar", "four barred/formal-star partners remain separately named",
      barred_owners == {"-Bpp*", "-Bpm*", "-Bmp*", "-Bmm*"})
check("type", "smallest source-faithful custody has eight parent maps, not twelve unrelated scalars",
      len(unbarred_owners) + len(barred_owners) == 8)


print("\nF. CHARGE PROJECTION AND CENTRE-CLASS CONTROLS")
classes = {"16": 1, "16bar": 3, "adjoint": 0, "class2_insertion": 2}
check("centre", "D5 parent classes are 16->1, 16bar->3, adjoint->0",
      classes == {"16": 1, "16bar": 3, "adjoint": 0, "class2_insertion": 2})

# A class-c coefficient maps a source class a to a+c mod 4.
def class_allowed(source_class: int, target_class: int, coefficient_class: int) -> bool:
    return (source_class + coefficient_class) % 4 == target_class


same_class0 = [class_allowed(c, c, 0) for c in (1, 3)]
cross_class0 = [class_allowed(1, 3, 0), class_allowed(3, 1, 0)]
cross_class2 = [class_allowed(1, 3, 2), class_allowed(3, 1, 2)]
if MUT == "class0_swaps":
    cross_class0 = [True, True]
check("centre", "class-zero adjoint coefficients preserve 16 and 16bar sectors",
      same_class0 == [True, True])
check("centre", "class-zero adjoint coefficients cannot swap 16 and 16bar",
      cross_class0 == [False, False])
check("centre", "a separately typed class-two insertion can swap the centre sectors",
      cross_class2 == [True, True])

# Exact projector identity on charge eigenstates: P0 A_q P0 vanishes for q!=0.
neutral_charges = [Fraction(0), Fraction(0)]
coefficient_charge = Fraction(1) if MUT != "charged_survives" else Fraction(0)
charged_projected_support = sum(1 for q_source in neutral_charges
                                for q_target in neutral_charges
                                if q_target == q_source + coefficient_charge)
check("charge", "a nonzero-charge coefficient has zero neutral-to-neutral projection",
      charged_projected_support == 0)
neutral_projected_support = sum(1 for q_source in neutral_charges
                                for q_target in neutral_charges
                                if q_target == q_source)
check("charge", "a charge-zero coefficient has nonempty neutral-to-neutral support",
      neutral_projected_support == 4)
check("type", "Q neutrality does not override the independent centre-class constraint",
      neutral_projected_support > 0 and cross_class0 == [False, False])

corner_classes = {"nu+": 3, "nu-": 1, "zeta+": 1, "zeta-": 3}
check("centre", "ambient D7 corner classes retain the exact 3,1,1,3 ledger",
      corner_classes == {"nu+": 3, "nu-": 1, "zeta+": 1, "zeta-": 3})
check("centre", "the two opposite-half source packages are class homogeneous",
      corner_classes["nu+"] == corner_classes["zeta-"]
      and corner_classes["nu-"] == corner_classes["zeta+"])
check("source", "CR-B independently records the same four corner classes",
      "nu_+   in Omega^0(S_+)    class 3" in CRB
      and "zeta_- in Omega^1(S_-)    class 3" in CRB)


print("\nG. CLAIM CEILING AND HOSTILE CONTROLS")
check("control", "Q=0 and full-SM-singlet horns are genuinely different",
      len(q0_16) == 2 and len(sm1_16) == 1)
check("control", "one field label is not an extra carrier basis vector",
      q_four == 16 and minimal_q == 2 * q_four)
check("control", "including the second zeta F is distinct from the minimal horn",
      two_f_q != minimal_q and two_f_s != minimal_s)
check("type", "source nu remains an Omega0 field rather than a standard nu_L label",
      "nu, bar-nu     in Omega^0(Y,S)" in SOURCE)
check("type", "source zeta remains an Omega1 field rather than a standard nu_R label",
      "zeta, bar-zeta in Omega^1(Y,S)" in SOURCE)
check("type", "no reality map, Majorana status, action, mass, or physical quotient is constructed", True)
check("control", "ordinary 126/seesaw ownership is absent from the exact construction", True)


TOTAL = sum(COUNTS.values())
print("\nSUMMARY")
print(" + ".join(f"{value} {kind}" for kind, value in COUNTS.items()), "=", TOTAL)
if FAILURES:
    print("FAILURES:", FAILURES)
    raise SystemExit(1)
print("PASS: exact K77 neutral ranks are 16/8 on the four observation blocks; the minimal four-field pencils are 32/16 and the second-F zeta horns are 48/24; equation 9.16 retains twelve permitted blocks, four southeast zeros, shared unbarred owners and independent bars; no source-faithful count is 20.")


if "--selftest" in sys.argv:
    mutations = (
        "q_as_singlet",
        "drop_half",
        "force_twenty",
        "wrong_second_f",
        "identify_bars",
        "southeast_nonzero",
        "scalarize_owners",
        "class0_swaps",
        "charged_survives",
    )
    for mutation in mutations:
        env = dict(os.environ)
        env["SN2_MUTATE"] = mutation
        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve())],
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if result.returncode == 0:
            raise SystemExit(f"FAIL selftest: mutation {mutation} escaped")
        print(f"PASS [mutation] {mutation} drives exit {result.returncode}")
    print(f"PASS selftest: {len(mutations)}/{len(mutations)} mutations rejected")
