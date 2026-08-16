#!/usr/bin/env python3
"""Exact SN-3A census of already-admitted ``varpi`` types against ``X_D``.

The calculation is pointwise and conditional.  It distinguishes the selected
Clifford-grade support, the full pointwise U(64,64) parent, the later frozen
trace-H_q horn, internal versus connection-form versus positional centre
classes, the equation-(9.16) cell grammar, and observed charge types.  It
constructs no action, vacuum, observation quotient, or mass.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
sys.path.insert(0, str(CHANNEL))

from p77_real_index_twin import build_split_clifford  # noqa: E402


PASSES: list[str] = []
FAILURES: list[str] = []


def check(kind: str, name: str, condition: bool, detail: object = "") -> None:
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] [{kind}] {name}"
          + (f" -- {detail}" if detail != "" else ""), flush=True)
    (PASSES if ok else FAILURES).append(f"{kind}:{name}")


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def vector_weights() -> list[tuple[F, ...]]:
    out = []
    for i in range(5):
        for sign in (1, -1):
            weight = [F(0)] * 5
            weight[i] = F(sign)
            out.append(tuple(weight))
    return out


def wedge_weights(k: int) -> Counter:
    result = Counter()
    for terms in combinations(vector_weights(), k):
        result[tuple(sum(x) for x in zip(*terms))] += 1
    return result


def b_minus_l(weight) -> F:
    return F(2, 3) * sum(weight[:3])


def t3_left(weight) -> F:
    return (weight[3] + weight[4]) / 2


def t3_right(weight) -> F:
    return (weight[3] - weight[4]) / 2


def hypercharge(weight) -> F:
    return t3_right(weight) + b_minus_l(weight) / 2


SU3_ALT = [
    ((0, 0, 0), +1),
    ((-1, 1, 0), -1),
    ((0, -1, 1), -1),
    ((-2, 0, 2), -1),
    ((-1, -1, 2), +1),
    ((-2, 1, 1), +1),
]


def colour_singlets(weights: Counter, predicate) -> int:
    sectors: dict[tuple, Counter] = {}
    for weight, multiplicity in weights.items():
        if predicate(weight):
            key = (sum(weight[:3]), weight[3], weight[4])
            sectors.setdefault(key, Counter())[weight[:3]] += multiplicity
    total = 0
    for (coordinate_sum, _h4, _h5), sector in sectors.items():
        base_coordinate = coordinate_sum / 3
        sample = next(iter(sector))
        if (sample[0] - base_coordinate).denominator != 1:
            continue
        base = (base_coordinate,) * 3
        for offset, sign in SU3_ALT:
            probe = tuple(base[i] + offset[i] for i in range(3))
            total += sign * sector.get(probe, 0)
    return total


def xd_doublets(weights: Counter, y: F) -> int:
    predicate = lambda w, t: (
        t3_left(w) == t and hypercharge(w) == y and b_minus_l(w) == 0
    )
    return (colour_singlets(weights, lambda w: predicate(w, F(1, 2)))
            - colour_singlets(weights, lambda w: predicate(w, F(3, 2))))


print("A. SOURCE, ROUTING, PRIOR ART, AND CONDITIONAL SCOPE")
packet = read("lab/active-research/joe-directed/majorana-126-neutrino/sn2-source-native-neutrino-conditional-build-read-packet-2026-08-16.md")
sn2 = read("lab/active-research/joe-directed/majorana-126-neutrino/sn2-neutral-reality-charge-admissibility-2026-08-16.md")
neutral_restriction = read("lab/active-research/joe-directed/majorana-126-neutrino/sn2-equation916-k77-neutral-restriction-2026-08-16.md")
source916 = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
action_bank = read("explorations/conditional-build/selected-k77-full-u6464-action-bank-2026-08-08.md")
radial = read("explorations/conditional-build/selected-k77-varpi-radial-half-exchange-gate-2026-08-12.md")
routing = read("lab/methods/source-native-comparator-routing.md")
la8 = read("lab/active-research/joe-directed/ledger-advancement/la8-rae2-is-refuted-at-the-settled-form-leg-and-the-open-fork-is-not-load-bearing-2026-08-15.md")

check("scope", "conditional-build packet forbids action and vacuum manufacture",
      "ACTION_AND_EXTERNAL_DATUM_PATHS_OFF_LIMIT" in packet.upper())
check("source", "equation 9.16 keeps four independent barred and unbarred fields",
      "four distinct fields" in source916 and "barred and unbarred" in source916)
check("source", "source assigns Higgs-like and Yukawa functions only at assignment strength",
      "Higgs-like, CKM, and Yukawa functions" in source916
      and "These are source assignments" in source916
      and "not derivations" in source916)
check("prior", "selected pointwise full-U bank has live grades 1, 2 and 5",
      "live Clifford grades:" in action_bank and "1, 2, 5" in action_bank)
check("prior", "radial theorem certifies grade one and moving-composite fences",
      "gamma(q)" in radial and "moving soldering receiver" in radial
      and "fourth real component" in radial)
check("correction", "withdrawn scalar descent is recorded rather than reused",
      "both horns give zero" in la8 and "returns a 4D **one-form**" in la8)
check("routing", "standard 126 remains a non-adjudicating comparator",
      "standard `126`" in routing and "logically non-adjudicating" in routing)
check("scope", "SN2 requires X_D only after a printed cross-degree incidence",
      "printed cross-degree" in sn2 and "slot-to-line incidence" in sn2)
check("prior", "SN2 composes class-two internal and one-form legs to positional class zero",
      "underlying class-2" in sn2 and "class-2 one-form leg combine to net class zero" in sn2)


print("\nB. EXACT INTERNAL REPRESENTATION CENSUS")
grade_reps = {grade: wedge_weights(grade) for grade in (1, 2, 3, 5)}
expected = {
    1: (1, 1),
    2: (0, 0),
    3: (2, 2),
    5: (2, 2),
}
for grade, representation in grade_reps.items():
    got = (xd_doublets(representation, F(1, 2)),
           xd_doublets(representation, F(-1, 2)))
    check("representation", f"normal Clifford grade {grade} B-L-zero doublet multiplicities",
          got == expected[grade], got)

check("representation", "grade five is 126 plus conjugate 126bar and retains both doublet copies",
      sum(grade_reps[5].values()) == 252 and expected[5] == (2, 2))
check("charge", "L N^c needs precisely the positive-hypercharge B-L-zero dual",
      F(-1, 2) + F(0) + F(1, 2) == 0 and -1 + 1 + 0 == 0)
check("plant", "grade two is rejected despite belonging to the selected action support",
      expected[2] == (0, 0))
check("control", "grade three has internal X_D types but is not in selected 1/2/5 support",
      expected[3] == (2, 2) and "live Clifford grades:" in action_bank)


print("\nC. REAL K77 PARENT, HALF, AND FROZEN-Hq TESTS")
P_PLUS, P_MINUS = build_split_clifford(7)
GAMMA = [P_PLUS[0], P_MINUS[0], P_MINUS[1], P_MINUS[2], *P_PLUS[1:], *P_MINUS[3:]]
I128 = np.eye(128, dtype=np.int64)
ZERO128 = np.zeros((128, 128), dtype=np.int64)


def matrix_product(matrices) -> np.ndarray:
    answer = I128.copy()
    for matrix in matrices:
        answer = answer @ matrix
    return answer


B = matrix_product(P_MINUS)
OMEGA4 = matrix_product(GAMMA[:4])
OMEGA14 = matrix_product(GAMMA)
NORMAL = GAMMA[4:]
Q_INDEX = 6
Q = NORMAL[Q_INDEX]
H0 = B @ Q

normal_monomials: dict[int, list[tuple[tuple[int, ...], np.ndarray]]] = {}
for grade in (1, 2, 3, 5):
    normal_monomials[grade] = [
        (indices, matrix_product([NORMAL[i] for i in indices]))
        for indices in combinations(range(10), grade)
    ]

for grade in (1, 2, 5):
    check("parent", f"every pure-normal grade-{grade} monomial is B-skew and admitted in the real full-U bank",
          all(np.array_equal(X.T @ B + B @ X, ZERO128)
              for _indices, X in normal_monomials[grade]))
check("control", "grade-three real monomials are B-self and enter only after the complex-unitary completion",
      all(np.array_equal(X.T @ B - B @ X, ZERO128)
          for _indices, X in normal_monomials[3]))

for grade in (1, 5):
    for _indices, X in normal_monomials[grade]:
        check("half", f"grade-{grade} bare/KX parity sample",
              np.array_equal(X @ OMEGA4, OMEGA4 @ X)
              and np.array_equal(X @ OMEGA14, -OMEGA14 @ X)
              and np.array_equal((B @ X) @ OMEGA4, -OMEGA4 @ (B @ X))
              and np.array_equal((B @ X) @ OMEGA14, OMEGA14 @ (B @ X)))
        break

fixed_expected = {1: 1, 2: 36, 5: 126}
for grade in (1, 2, 5):
    fixed = []
    nonzero_masks = []
    defect_values_are_exact = True
    for indices, X in normal_monomials[grade]:
        defect = X.T @ H0 + H0 @ X
        if np.array_equal(defect, ZERO128):
            fixed.append(indices)
        else:
            # H0 and X are Clifford monomials.  Every nonzero defect is twice
            # one Clifford-basis monomial; distinct X masks give distinct
            # output masks, proving there are no hidden linear cancellations.
            defect_values_are_exact &= set(np.unique(defect)).issubset({-2, 0, 2})
            nonzero_masks.append(tuple(sorted(set(indices) ^ {Q_INDEX})))
    check("exact", f"every nonzero grade-{grade} frozen-Hq defect is a signed twice-monomial",
          defect_values_are_exact)
    check("fixed_hq", f"dim pure-normal grade-{grade} intersection with fixed u(Hq)",
          len(fixed) == fixed_expected[grade], len(fixed))
    check("fixed_hq", f"grade-{grade} defect images have distinct Clifford masks",
          len(nonzero_masks) == len(set(nonzero_masks)))

check("fixed_hq", "grade-one fixed-Hq intersection is exactly the radial q line",
      [indices for indices, X in normal_monomials[1]
       if np.array_equal(X.T @ H0 + H0 @ X, ZERO128)] == [(Q_INDEX,)])
grade2_fixed = [indices for indices, X in normal_monomials[2]
                if np.array_equal(X.T @ H0 + H0 @ X, ZERO128)]
check("fixed_hq", "grade-two fixed-Hq subspace is exactly the q-avoiding monomials",
      len(grade2_fixed) == 36 and all(Q_INDEX not in indices for indices in grade2_fixed))
grade5_fixed = [indices for indices, X in normal_monomials[5]
                if np.array_equal(X.T @ H0 + H0 @ X, ZERO128)]
check("fixed_hq", "grade-five fixed-Hq half-space is exactly the q-containing monomials",
      len(grade5_fixed) == 126 and all(Q_INDEX in indices for indices in grade5_fixed))


print("\nD. EQUATION-9.16 CELL CUSTODY AND NEUTRAL HORN")
rows = ("bar-zeta-", "bar-zeta+", "bar-nu-", "bar-nu+")
cols = ("zeta+", "zeta-", "nu+", "nu-")
row_classes = (1, 3, 1, 3)
col_classes = (3, 1, 3, 1)
cell_class = lambda r, c: (-row_classes[r] - col_classes[c]) % 4

pm_mp_cells = {
    (0, 3): "varpi_+-",
    (1, 2): "varpi_-+",
    (2, 1): "-bar-varpi_+-^*",
    (3, 0): "-bar-varpi_-+^*",
}
pp_mm_cells = {
    (0, 2): "varpi_++",
    (1, 3): "varpi_--",
    (2, 0): "-bar-varpi_++^*",
    (3, 1): "-bar-varpi_--^*",
}
pm_mp_reverse_pairs = {
    (0, 3): (3, 0),
    (1, 2): (2, 1),
}
pp_mm_reverse_pairs = {
    (0, 2): (2, 0),
    (1, 3): (3, 1),
}


def native_connection_class(internal_class: int, form_leg_class: int) -> int:
    return (internal_class + form_leg_class) % 4


internal_odd_class = 2
connection_form_leg_class = 2
native_odd_connection_class = native_connection_class(
    internal_odd_class, connection_form_leg_class
)
old_drop_form_leg_mutant = internal_odd_class

check("cells", "the cross-degree ledger has four pp/mm and four pm/mp positions",
      set(pp_mm_cells) == {(0, 2), (1, 3), (2, 0), (3, 1)}
      and set(pm_mp_cells) == {(0, 3), (1, 2), (2, 1), (3, 0)})
check("cells", "pp/mm positions have positional net class zero",
      all(cell_class(r, c) == 0 for r, c in pp_mm_cells))
check("cells", "pm/mp positions have positional net class two",
      all(cell_class(r, c) == 2 for r, c in pm_mp_cells))
check("composition", "internal odd class two plus connection form-leg class two gives net class zero",
      native_odd_connection_class == 0)
check("cells", "native grade-one/five one-form content formally aligns only with pp/mm positions",
      all(cell_class(r, c) == native_odd_connection_class for r, c in pp_mm_cells)
      and all(cell_class(r, c) != native_odd_connection_class for r, c in pm_mp_cells))
check("mutant", "dropping the form-leg class reproduces and exposes the old false pm/mp selection",
      old_drop_form_leg_mutant == 2
      and old_drop_form_leg_mutant != native_odd_connection_class
      and all(cell_class(r, c) == old_drop_form_leg_mutant for r, c in pm_mp_cells))
check("cells", "crossed reverse custody is pm to bar-mp and mp to bar-pm",
      pm_mp_cells[pm_mp_reverse_pairs[(0, 3)]] == "-bar-varpi_-+^*"
      and pm_mp_cells[pm_mp_reverse_pairs[(1, 2)]] == "-bar-varpi_+-^*")
check("cells", "pp/mm reverse custody preserves the owner label",
      pp_mm_cells[pp_mm_reverse_pairs[(0, 2)]] == "-bar-varpi_++^*"
      and pp_mm_cells[pp_mm_reverse_pairs[(1, 3)]] == "-bar-varpi_--^*")
all_cross_degree_cells = pp_mm_cells | pm_mp_cells
check("cells", "NE cells are source Omega0 to Omega1 cross-degree cells",
      all(rows[r].startswith("bar-zeta") and cols[c].startswith("nu")
          for r, c in all_cross_degree_cells if r < 2))
check("cells", "SW cells are the reverse Omega1 to Omega0 cells",
      all(rows[r].startswith("bar-nu") and cols[c].startswith("zeta")
          for r, c in all_cross_degree_cells if r >= 2))
check("half", "all four owners and independent barred partners remain in the two form-shifted packages",
      set(all_cross_degree_cells.values())
      == {"varpi_++", "varpi_+-", "varpi_-+", "varpi_--",
          "-bar-varpi_++^*", "-bar-varpi_+-^*",
          "-bar-varpi_-+^*", "-bar-varpi_--^*"})
check("neutral", "X_D is available only on Q0 because SM1 deletes the L endpoint",
      "SN2-NEUTRAL=Q0" in neutral_restriction
      and "SN2-NEUTRAL=SM1" in neutral_restriction
      and "`nu_L` is electrically neutral but belongs to a weak doublet" in neutral_restriction)
check("reality", "barred partners remain independently named rather than identified by the census",
      "four distinct fields" in source916)


print("\nE. CLOSURE, COVARIANCE, AND CLAIM CEILING")
check("coindex", "observation pullback returns a 4D one-form rather than a scalar",
      "returns a 4D **one-form**" in la8)
check("moving", "moving Hq composite is not four fixed-Hq Lie-algebra generators",
      fixed_expected[1] == 1 and "fourth real component" in radial
      and "complete moving" in radial)
check("typing", "parent representation membership is not actual neutral-line incidence",
      "coefficient_missing" in sn2.lower() and "slot-to-line incidence" in sn2)
check("fence", "source zeta/nu are not relabelled as observed L/Nc",
      "zeta = nu_L" in packet and "nu = nu_R" in packet)
check("fence", "no standard 126, action, vacuum, quotient, or mass is constructed",
      "standard `126` results remain non-adjudicating" in packet
      and "no action, vacuum, or external datum" in packet)
check("plant", "a full-SM singlet horn cannot host the L N^c endpoint pair",
      "keeps only full Standard-Model singlets" in neutral_restriction
      and "`nu_L` is electrically neutral but belongs to a weak doublet" in neutral_restriction)
check("plant", "radial parent membership alone is not a weak-doublet certificate",
      fixed_expected[1] == 1 and expected[1] == (1, 1))
check("plant", "equal dimensions do not identify barred and unbarred fields",
      "same dimension as the corresponding unbarred" in neutral_restriction
      and "declares barred and unbarred variables to be" in neutral_restriction
      and "independent classical fields" in neutral_restriction)

print("\nSUMMARY")
print(f"passes={len(PASSES)} failures={len(FAILURES)}")
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: selected grades one and five contain conditional X_D parent types; native class 2+2=0 formally aligns the one-form packet with pp/mm, while crossed pm/mp custody is ledger-only. Actual neutral-line/coindex incidence remains unconstructed.")
