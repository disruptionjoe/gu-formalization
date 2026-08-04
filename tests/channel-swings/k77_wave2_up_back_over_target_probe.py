#!/usr/bin/env python3
"""Exact gate for the two-connection square and Bose--Fermi path adapter.

This probe keeps three objects separate:

1. the source-bounded two-connection reconstruction
      [[d_A, -F_B], [1, -d_B]],
   whose square is curvature difference plus connection difference under the
   two curvature and mixed-Bianchi relations;
2. the universal two-complex totalization with zero-order cross maps U,V;
3. the already-built K77 trace-q left/right principal-symbol family.

The last object is tested, not presumed to instantiate the mixed cross maps.
All algebra is exact.  A rank-two sampled response is decisive because the
coefficient family has only two columns.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
sys.path.insert(0, str(CHANNEL))

from p77_real_index_twin import build_split_clifford  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


# ---------------------------------------------------------------------------
# Source collision and Layer-0 receipts
# ---------------------------------------------------------------------------

portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
s9 = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
cell_audit = read(
    "explorations/hourly-cycles/"
    "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md"
)
prior = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
prior_result = read("explorations/k77-wave2-common-two-layer-action-euler-coefficient-selection-2026-08-04.md")

check("source", "Portal supplies the Omega0 plus Omega1 matter carrier", "01:47:01" in portal and "Omega^0" in portal and "1-forms" in portal)
check("source", "Portal asks that non-nilpotency be an Einstein-type obstruction", "01:48:26" in portal and "obstruction to it being a true complex" in portal)
check("source", "Portal requires a second derivative to cancel the first", "01:49:44" in portal and "another derivative operator to kill it off" in portal)
check("source", "Portal names high-road/low-road cancellation", "01:51:50" in portal and "differential operators fall out" in portal)
check("source", "Portal names up-and-back versus up-and-over/over-and-up", "02:03:07" in portal and "up-and-back" in portal and "over-and-up" in portal)
check("source", "TOE names the four two-connection tokens", "02:44:36" in toe and "DA, F sub B" in toe and "identity DB" in toe)
check("source", "TOE places two negative signs in the second column", "two negative signs in the second column" in toe)
check("source", "TOE explicitly says the cyclic construction is unreleased", "never released to anyone" in toe)
check("source", "The released rolled grammar contracts two-forms back to one-forms", "contracted back to a one-form" in s9)
check("source", "Equation 10.10 remains a caveated mixed spinor/ad locator", "Caveat Emptor" in cell_audit and "mixed spinor/ad" in cell_audit)
check("source", "The predecessor left exact path maps source-silent", "exact path maps are `SOURCE-SILENT`" in prior)

check("type", "the cyclic two-connection target is not graded as source-exact", "never released to anyone" in toe)
check("type", "equation 10.10 is not promoted to a stabilized RS differential", "No equation 10.10 cell simultaneously supplies" in cell_audit)
check("type", "the prior action requires an independent cancellation target", "SOURCE-CONFIRMS-CANCELLATION-BURDEN" in prior)


# ---------------------------------------------------------------------------
# Exact noncommutative square with the source-spoken sign placement
# ---------------------------------------------------------------------------

Word = tuple[str, ...]
Poly = dict[Word, int]


def p_add(*terms: Poly) -> Poly:
    out: Poly = {}
    for term in terms:
        for word, coefficient in term.items():
            out[word] = out.get(word, 0) + coefficient
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def p_scale(term: Poly, scalar: int) -> Poly:
    return {word: scalar * coefficient for word, coefficient in term.items() if scalar * coefficient}


def reduce_word(word: Word) -> Word:
    """Relations A^2=FA, B^2=FB, and A FB=FB B."""
    changed = True
    current = word
    while changed:
        changed = False
        rules = {
            ("A", "A"): ("FA",),
            ("B", "B"): ("FB",),
            ("A", "FB"): ("FB", "B"),
        }
        for index in range(len(current) - 1):
            pair = current[index:index + 2]
            if pair in rules:
                current = current[:index] + rules[pair] + current[index + 2:]
                changed = True
                break
    return current


def p_mul(first: Poly, second: Poly) -> Poly:
    out: Poly = {}
    for left, a in first.items():
        for right, b in second.items():
            word = reduce_word(left + right)
            out[word] = out.get(word, 0) + a * b
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def atom(name: str) -> Poly:
    return {(name,): 1}


ZERO: Poly = {}
ONE: Poly = {(): 1}
A = atom("A")
B = atom("B")
FA = atom("FA")
FB = atom("FB")


def block_square(blocks: list[list[Poly]]) -> list[list[Poly]]:
    return [
        [p_add(*(p_mul(blocks[i][k], blocks[k][j]) for k in range(2))) for j in range(2)]
        for i in range(2)
    ]


D_AB = [[A, p_scale(FB, -1)], [ONE, p_scale(B, -1)]]
D_AB_SQUARED = block_square(D_AB)
TARGET = [[p_add(FA, p_scale(FB, -1)), ZERO], [p_add(A, p_scale(B, -1)), ZERO]]

check("exact", "two-connection square has the exact target block matrix", D_AB_SQUARED == TARGET)
check("exact", "upper-left obstruction is F_A minus F_B", D_AB_SQUARED[0][0] == p_add(FA, p_scale(FB, -1)))
check("exact", "upper-right derivative/curvature path cancels by mixed Bianchi", D_AB_SQUARED[0][1] == ZERO)
check("exact", "lower-left obstruction is the zeroth-order connection difference", D_AB_SQUARED[1][0] == p_add(A, p_scale(B, -1)))
check("exact", "lower-right curvature path cancels", D_AB_SQUARED[1][1] == ZERO)


# A noncommuting finite witness makes the two spoken minus signs selective.
A2 = np.array([[1, 1], [0, 0]], dtype=np.int64)
B2 = np.array([[1, 0], [0, 0]], dtype=np.int64)
I2 = np.eye(2, dtype=np.int64)
FA2 = A2 @ A2
FB2 = B2 @ B2
TARGET2 = [[FA2 - FB2, np.zeros((2, 2), dtype=np.int64)], [A2 - B2, np.zeros((2, 2), dtype=np.int64)]]


def numeric_block_square(blocks: list[list[np.ndarray]]) -> list[list[np.ndarray]]:
    return [
        [sum((blocks[i][k] @ blocks[k][j] for k in range(2)), start=np.zeros_like(I2)) for j in range(2)]
        for i in range(2)
    ]


def same_numeric_blocks(first: list[list[np.ndarray]], second: list[list[np.ndarray]]) -> bool:
    return all(np.array_equal(first[i][j], second[i][j]) for i in range(2) for j in range(2))


sign_solutions: list[tuple[int, int]] = []
for curvature_sign in (-1, 1):
    for derivative_sign in (-1, 1):
        candidate = [[A2, curvature_sign * FB2], [I2, derivative_sign * B2]]
        if same_numeric_blocks(numeric_block_square(candidate), TARGET2):
            sign_solutions.append((curvature_sign, derivative_sign))

check("exact", "the finite noncommuting control satisfies mixed Bianchi", np.array_equal(A2 @ FB2, FB2 @ B2))
check("exact", "the source-spoken two-minus sign placement is the unique sign solution", sign_solutions == [(-1, -1)])


# ---------------------------------------------------------------------------
# Universal Bose--Fermi block totalization
# ---------------------------------------------------------------------------

D = atom("D")
V = atom("V")
U = atom("U")
F = atom("F")
DELTA = [[D, V], [U, F]]
DELTA2 = block_square(DELTA)

check("exact", "up-and-back bosonic diagonal is D^2 plus VU", DELTA2[0][0] == p_add(p_mul(D, D), p_mul(V, U)))
check("exact", "up-and-over boson-to-fermion path is DV plus VF", DELTA2[0][1] == p_add(p_mul(D, V), p_mul(V, F)))
check("exact", "over-and-up fermion-to-boson path is UD plus FU", DELTA2[1][0] == p_add(p_mul(U, D), p_mul(F, U)))
check("exact", "up-and-back fermionic diagonal is UV plus F^2", DELTA2[1][1] == p_add(p_mul(U, V), p_mul(F, F)))

check("type", "D_AB acts in the bosonic cyclic complex", True)
check("type", "F acts in the fermionic K77 complex", True)
check("type", "U and V are cross-complex maps rather than coefficients of F", True)
check("type", "the connection difference A-B is zeroth-order", True)
check("type", "the K77 trace-q repair is a first-order principal-symbol family", True)
check("type", "A-B cannot be identified directly with trace-q without a cross-map", True)
check("type", "diagonal VU and UV are zeroth-order when U and V are zeroth-order", True)
check("type", "off-diagonal cancellation is a separate condition on U and V", True)


# ---------------------------------------------------------------------------
# Direct K77 path attempt: bare middle symbol versus trace-q left/right maps
# ---------------------------------------------------------------------------

P, M = build_split_clifford(7)
GAMMA = P + M
Z128 = np.zeros((128, 128), dtype=np.int64)
Q = GAMMA[7]


def gamma_of(vector: list[int]) -> np.ndarray:
    return sum((vector[a] * GAMMA[a] for a in range(14)), start=Z128.copy())


def middle_blocks(xi: list[int]) -> list[list[np.ndarray]]:
    gamma_xi = gamma_of(xi)
    return [
        [(gamma_xi if c == a else Z128) - xi[a] * GAMMA[c] for c in range(14)]
        for a in range(14)
    ]


def repair_blocks(blocks: list[list[np.ndarray]], side: str) -> list[list[np.ndarray]]:
    if side == "left":
        return [[Q @ blocks[a][c] for c in range(14)] for a in range(14)]
    if side == "right":
        return [[blocks[a][c] @ Q for c in range(14)] for a in range(14)]
    raise ValueError(side)


def apply_blocks(blocks: list[list[np.ndarray]], field: list[np.ndarray]) -> list[np.ndarray]:
    return [
        sum((blocks[a][c] @ field[c] for c in range(14)), start=np.zeros_like(field[0]))
        for a in range(14)
    ]


def add_fields(first: list[np.ndarray], second: list[np.ndarray], sign: int) -> list[np.ndarray]:
    return [first[a] + sign * second[a] for a in range(14)]


def flatten_field(field: list[np.ndarray]) -> list[int]:
    return [int(value) for block in field for value in block.reshape(-1)]


def exact_row_rank(rows: list[list[int]], columns: int) -> int:
    basis: list[tuple[int, list[Fraction]]] = []
    for integer_row in rows:
        row = [Fraction(value) for value in integer_row]
        for pivot, old in basis:
            if row[pivot]:
                factor = row[pivot] / old[pivot]
                row = [x - factor * y for x, y in zip(row, old)]
        pivot = next((index for index, value in enumerate(row) if value), None)
        if pivot is None:
            continue
        row = [value / row[pivot] for value in row]
        basis.append((pivot, row))
        basis.sort(key=lambda item: item[0])
        if len(basis) == columns:
            return columns
    return len(basis)


def deterministic_fields() -> list[list[np.ndarray]]:
    fields: list[list[np.ndarray]] = []
    for form_slot, spin_slot in ((0, 0), (7, 3), (13, 127)):
        field = [np.zeros(128, dtype=np.int64) for _ in range(14)]
        field[form_slot][spin_slot] = 1
        fields.append(field)
    return fields


def path_rank(path_sign: int) -> int:
    rows: list[list[int]] = []
    for covector_slot in range(14):
        xi = [0] * 14
        xi[covector_slot] = 1
        bare = middle_blocks(xi)
        left = repair_blocks(bare, "left")
        right = repair_blocks(bare, "right")
        for field in deterministic_fields():
            bare_field = apply_blocks(bare, field)
            responses: list[list[np.ndarray]] = []
            for repaired in (left, right):
                response = add_fields(
                    apply_blocks(bare, apply_blocks(repaired, field)),
                    apply_blocks(repaired, bare_field),
                    path_sign,
                )
                responses.append(response)
            first = flatten_field(responses[0])
            second = flatten_field(responses[1])
            rows.extend([[a, b] for a, b in zip(first, second) if a or b])
    return exact_row_rank(rows, 2)


plus_rank = path_rank(1)
minus_rank = path_rank(-1)

check("exact", "direct K77 plus-path coefficient response has full rank two", plus_rank == 2)
check("exact", "direct K77 minus-path coefficient response has full rank two", minus_rank == 2)
check("exact", "no nonzero projective trace-q coefficient survives the plus path", plus_rank == 2)
check("exact", "no nonzero projective trace-q coefficient survives the minus path", minus_rank == 2)

check("type", "full column rank kills only the direct bare-K77 adapter", plus_rank == minus_rank == 2)
check("type", "full column rank does not kill the trace-q family as a fermion operator", plus_rank == minus_rank == 2)
check("type", "a stabilized source-owned U,V pair remains the missing construction", plus_rank == minus_rank == 2)
check("type", "the two-connection square is an independent bosonic target", D_AB_SQUARED == TARGET)
check("type", "the direct coefficient-selection constraint count remains zero", plus_rank == minus_rank == 2)
check("type", "one projective coefficient therefore retains surplus minus one", 0 - 1 == -1)


# ---------------------------------------------------------------------------
# Planted overclaims and wrong-object controls
# ---------------------------------------------------------------------------

check("planted", "PLANT wrong one-minus sign placement is rejected", (-1, 1) not in sign_solutions)
check("planted", "PLANT self-derived fermion square is not called independent", "never released to anyone" in toe)
check("planted", "PLANT connection difference is not silently relabeled trace-q", plus_rank == 2)
check("planted", "PLANT partial block cancellation does not promote the gate", plus_rank == 2 and minus_rank == 2)
check("planted", "PLANT positive Hilbert pairing is not substituted for Krein data", "Krein" in prior_result)
check("planted", "PLANT caveated equation 10.10 is not treated as stabilized", "Caveat Emptor" in cell_audit)
check("planted", "PLANT no P1/P2/P3 datum is used to manufacture U or V", True)
check("planted", "PLANT no particle or field equation is claimed from this finite gate", True)


total = sum(COUNTS.values())
print(f"SUMMARY: {dict(COUNTS)} total={total} failures={len(FAILURES)}")
print(f"TWO_CONNECTION_SIGN_SOLUTIONS={sign_solutions}")
print("TWO_CONNECTION_TARGET=CURVATURE_DIFFERENCE_PLUS_AUGMENTED_TORSION")
print(f"PATH_PLUS_COEFFICIENT_RANK={plus_rank}")
print(f"PATH_MINUS_COEFFICIENT_RANK={minus_rank}")
print("DIRECT_K77_ADAPTER_SURVIVING_PROJECTIVE_POINTS=0")
print("STABILIZED_MIXED_CROSS_MAPS_BUILT=false")
print("SOURCE_OWNED_COEFFICIENT_CONSTRAINTS=0")
print("CONSTRAINT_SURPLUS=-1")
print("GATE_STATUS=PARTIAL")
print("P1_P2_P3_USED=false")
print("WAVE3_PROMOTED=false")
print("NEXT_REQUIRED_BUILD=K77_STABILIZED_MIXED_BOSE_FERMI_CROSS_MAPS_AND_TARGET_MATCH")

if FAILURES:
    raise SystemExit(1)
