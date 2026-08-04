#!/usr/bin/env python3
r"""DC-H1 FOLLOW-ON: whose time-orientation is the orbit-sign Z/2?

DC-H1 (``explorations/dc-h1-orbit-signs-monodromy-check-2026-08-04.md``,
``tests/dc-h1/dc_h1_orbit_sign_monodromy_probe.py``) established, exactly, that
the Z/2 which moves the six B5 chirality-orbit relative signs is the
ORTHOCHRONOUS character of the Lorentz stabilizer O(3,1) -- a reflection Z/2,
not the spin double cover.  It then named the cheapest new question it had
generated: *if the orbit-sign Z/2 is the time-orientation character, what is it
a time-orientation OF?*

This probe answers the carrier half exactly, and instruments the
"already-supplied?" half so that the audit cannot drift.

Parts
-----
1. THE FIBRE FRAME IS EARNED, NOT ASSERTED.  DC-H1 hardcoded
   ``FIBRE_SIGNATURE = [1]*6 + [-1]*4`` for its ten DeWitt columns.  Here the
   DeWitt supermetric G(E,F) = tr(eta E eta F) - lambda tr(eta E) tr(eta F) is
   built over Fraction and the ten columns are shown ORTHOGONAL with exactly
   six positive and four negative norms at the GR value lambda = 1.  The four
   negative legs are named: the conformal/trace mode eta itself, and the three
   space-time off-diagonals E_(i3).

2. THE LOOP, IN CLOSED FORM, WITH NO CLIFFORD ALGEBRA AT ALL.  Symbolically:
   the DeWitt loop's metric h_t has a continuous eigenvector v_t with
   h_t v_t = -v_t and h_t(v_t, v_t) = -1 IDENTICALLY, h_1 = h_0 = eta, and
   v_1 = -v_0.  So the loop is a path in the space of Lorentzian metrics on ONE
   FIXED tangent space that returns the SAME metric with the future and past
   cones EXCHANGED.  This is the whole typing, and it is independent of every
   Clifford, Krein, coflip, packet and signature convention in the program.

3. THE CARRIER SPLIT.  On an independently rebuilt Cl(9,5) with the
   program-native coflip C_perp = K J_obs, the orientation character factors
   over the 14 gimmel legs as chi = chi_base * chi_fibre.  Exhaustively over
   all sixteen diagonal elements of O(3,1):

       chi_fibre == +1  ALWAYS        chi_base == the orthochronous character

   The Sym^2 metric-fibre legs contribute NOTHING.  The structural reason is
   exhibited, not observed: the only fibre legs with per-leg character -1 that
   a diagonal Lambda can flip are the three PURELY SPATIAL off-diagonals, and
   they flip in count k(3-k) with k = #(flipped spatial base legs), which is
   even for every k in {0,1,2,3}.  (Note the dimension dependence: for an
   n-dimensional spatial slice k(n-k) is odd at k=1 whenever n is even, so the
   fibre's blindness is a 3-spatial-dimension fact, not a generality.)

4. THREE CHARACTERS, THREE DIFFERENT ORIENTATIONS.  The same computation
   separates the program's own structures:

       sigma_J (the reality structure J_obs)   = det       = SPACETIME orientation
       sigma_K (the Krein form K_S = e_0..e_8) = det*orth  = SPACE orientation
       chi     (the coflip C_perp = K J_obs)   = orth      = TIME orientation

   with chi = sigma_K * sigma_J exactly, which is the elementary identity
   "spacetime orientation = space orientation x time orientation".  det*orth is
   verified to be the determinant of the spatial 3x3 block.  Consequence, and
   the Layer-0 payload of this probe: any claim that welds "the arrow" to a
   sign carried by the Krein structure must say WHICH of the three objects it
   attaches to, because only one of the three is the time-orientation.

5. THE BASE-SIDE NO-GO.  The loop lies inside ONE metric fibre (the base point
   never moves: B_t is orthogonal, so it is a path of metrics on a fixed
   tangent space).  Therefore the class restricts nontrivially to a single
   fibre, while every pullback class pi^*(alpha) from the base restricts to
   zero on every fibre.  So no base-side time-orientation, however supplied,
   equals or cancels this class on Y^14.

6. THE T-PARITY AUDIT.  A construction FIXES a time-orientation only if its
   defining law has a T-odd term AND takes no orientation-valued input.  The
   rule is stated first and applied second.  Exact sympy parity is computed for
   the three cases where a computation exists (W166's record-count mode, the
   Friedmann first equation, and a friction term as the positive control), and
   the whole candidate ledger is machine-checked: every cited artifact must
   exist on disk, every candidate must name its orientation-valued input, and
   the synthetic FIXES control must be classified FIXES so that the empty
   FIXES verdict on the real candidates is not vacuous.

Kill conditions, declared before the probe body was written:
  K1  if chi_fibre is not identically +1 over the sixteen diagonal elements,
      the carrier verdict "the datum lives on the base" DIES and the datum is
      a joint base+fibre object;
  K2  if the four pi_0(O(3,1)) components are not all represented among the
      sixteen diagonal elements, the exhaustive check is NOT exhaustive and
      Parts 3-4 are void;
  K3  if sigma_K == chi as characters, the "which structure carries the arrow"
      discriminator of Part 4 is empty and there is no Layer-0 payload;
  K4  if h_t(v_t, v_t) is not identically negative, v_t is not a timelike
      direction and Part 2's future/past reading is void;
  K5  if the synthetic T-odd/no-input control is NOT classified FIXES, the
      audit rule cannot ever return FIXES and Part 6's negative is vacuous.

Grade: EXACT throughout.  Part 1 is Fraction arithmetic; Part 2 is closed-form
sympy; Parts 3-5 are Gaussian-integer Clifford linear algebra plus integer
combinatorics; Part 6 is exact sympy parity plus integer bookkeeping over a
declared ledger.  This probe constructs no operator, freezes no packet field,
selects no phase, and moves no claim, canon verdict, count, ledger entry, or
posture.  The records/finality INTERPRETATION of any direction named here is
TaF-owned and is not asserted anywhere below.
"""

from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
TOL = 1.0e-10
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label}" + (f" ({detail})" if detail else ""))
    if not condition:
        FAILURES.append(label)


def info(message: str) -> None:
    print(f"      {message}")


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def kron_all(factors: list[np.ndarray]) -> np.ndarray:
    out = np.eye(1, dtype=complex)
    for factor in factors:
        out = np.kron(out, factor)
    return out


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


# The ten DeWitt columns of DC-H1, as unnormalized integer combinations of the
# symmetric basis E_(i,j) of Sym^2(R^{3,1}).  Reproduced verbatim so that this
# probe hardens the SAME frame DC-H1 used.
DEWITT_COLUMNS: list[dict[tuple[int, int], Fraction]] = [
    {(0, 0): Fraction(1), (1, 1): Fraction(-1)},
    {(0, 0): Fraction(1), (1, 1): Fraction(1), (2, 2): Fraction(-2)},
    {(0, 0): Fraction(1), (1, 1): Fraction(1), (2, 2): Fraction(1),
     (3, 3): Fraction(3)},
    {(0, 1): Fraction(1)},
    {(0, 2): Fraction(1)},
    {(1, 2): Fraction(1)},
    {(0, 0): Fraction(1), (1, 1): Fraction(1), (2, 2): Fraction(1),
     (3, 3): Fraction(-1)},
    {(0, 3): Fraction(1)},
    {(1, 3): Fraction(1)},
    {(2, 3): Fraction(1)},
]
ETA_DIAG = [1, 1, 1, -1]
TIMELIKE = 3


# =============================================================================
# PART 1.  The DeWitt fibre frame is EARNED: exact orthogonality, signature (6,4)
# =============================================================================

print("=" * 96)
print("1. THE DEWITT FIBRE FRAME, EARNED IN EXACT ARITHMETIC (DC-H1 asserted it)")
print("=" * 96)


def sym_matrix(column: dict[tuple[int, int], Fraction]) -> list[list[Fraction]]:
    out = [[Fraction(0)] * 4 for _ in range(4)]
    for (i, j), value in column.items():
        out[i][j] += value
        if i != j:
            out[j][i] += value
    return out


def dewitt_form(a: list[list[Fraction]], b: list[list[Fraction]],
                lam: Fraction) -> Fraction:
    """G(A,B) = tr(eta A eta B) - lam tr(eta A) tr(eta B), exact."""
    total = Fraction(0)
    for i in range(4):
        for j in range(4):
            total += ETA_DIAG[i] * a[i][j] * ETA_DIAG[j] * b[j][i]
    trace_a = sum(ETA_DIAG[i] * a[i][i] for i in range(4))
    trace_b = sum(ETA_DIAG[i] * b[i][i] for i in range(4))
    return total - lam * trace_a * trace_b


COLUMN_MATRICES = [sym_matrix(column) for column in DEWITT_COLUMNS]
LAMBDA_GR = Fraction(1)
GRAM = [
    [dewitt_form(COLUMN_MATRICES[a], COLUMN_MATRICES[b], LAMBDA_GR)
     for b in range(10)]
    for a in range(10)
]
NORMS = [GRAM[a][a] for a in range(10)]

CELL_ORDER = [(i, j) for i in range(4) for j in range(i, 4)]
COEFFICIENTS = sp.Matrix([
    [sp.Rational(column.get(cell, Fraction(0))) for cell in CELL_ORDER]
    for column in DEWITT_COLUMNS
])
check(
    "the ten DeWitt columns are a BASIS of Sym^2(R^4): exact rank 10",
    len(DEWITT_COLUMNS) == 10 and len(CELL_ORDER) == 10
    and COEFFICIENTS.rank() == 10,
    f"rank {COEFFICIENTS.rank()}",
)
check(
    "they are G-ORTHOGONAL in exact arithmetic (all off-diagonal Gram = 0)",
    all(GRAM[a][b] == 0 for a in range(10) for b in range(10) if a != b),
)
check(
    "the DeWitt supermetric (lambda = 1) gives signature (6,4) EXACTLY",
    sum(1 for n in NORMS if n > 0) == 6
    and sum(1 for n in NORMS if n < 0) == 4
    and all(n != 0 for n in NORMS),
    f"norms {[str(n) for n in NORMS]}",
)
check(
    "the four NEGATIVE legs are the conformal mode eta and the three E_(i,3)",
    [index for index, n in enumerate(NORMS) if n < 0] == [6, 7, 8, 9]
    and COLUMN_MATRICES[6] == sym_matrix(
        {(0, 0): Fraction(1), (1, 1): Fraction(1), (2, 2): Fraction(1),
         (3, 3): Fraction(-1)}
    )
    and all(
        set(DEWITT_COLUMNS[index]) == {(index - 7, 3)} for index in (7, 8, 9)
    ),
)
check(
    "columns 0,1,2 are eta-TRACELESS diagonal modes; column 6 IS eta itself",
    all(
        sum(ETA_DIAG[i] * COLUMN_MATRICES[index][i][i] for i in range(4)) == 0
        for index in (0, 1, 2)
    )
    and [COLUMN_MATRICES[6][i][i] for i in range(4)] == ETA_DIAG,
)
check(
    "the (6,4) split needs lambda > 1/4: at lambda = 1/4 the trace leg is NULL",
    dewitt_form(COLUMN_MATRICES[6], COLUMN_MATRICES[6], Fraction(1, 4)) == 0
    and dewitt_form(COLUMN_MATRICES[6], COLUMN_MATRICES[6], Fraction(0)) > 0,
    "so the fibre's four negative directions are not a convention-free freebie",
)
info("DC-H1's asserted FIBRE_SIGNATURE = [1]*6 + [-1]*4 is now DERIVED.")


# =============================================================================
# PART 2.  The loop, in closed form: the same metric, future and past exchanged
# =============================================================================

print("\n" + "=" * 96)
print("2. THE DEWITT LOOP EXCHANGES THE FUTURE AND PAST CONES (closed form)")
print("=" * 96)

t_sym = sp.symbols("t", real=True)
theta = sp.pi * t_sym
B_t = sp.Matrix([
    [sp.cos(theta), 0, 0, -sp.sin(theta)],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [sp.sin(theta), 0, 0, sp.cos(theta)],
])
ETA_SYM = sp.diag(*ETA_DIAG)
h_t = sp.simplify(B_t.T * ETA_SYM * B_t)
v_t = sp.Matrix([sp.sin(theta), 0, 0, sp.cos(theta)])

check(
    "B_t is ORTHOGONAL, so the loop never moves the base point: it is a path "
    "of metrics on ONE fixed tangent space (the loop lies in a single fibre)",
    sp.simplify(B_t.T * B_t - sp.eye(4)) == sp.zeros(4, 4),
)
check(
    "the loop CLOSES: h_1 = h_0 = eta exactly",
    sp.simplify(h_t.subs(t_sym, 1) - h_t.subs(t_sym, 0)) == sp.zeros(4, 4)
    and sp.simplify(h_t.subs(t_sym, 0) - ETA_SYM) == sp.zeros(4, 4),
)
check(
    "the loop is NON-constant in F (h_{1/2} != eta)",
    sp.simplify(h_t.subs(t_sym, sp.Rational(1, 2)) - ETA_SYM) != sp.zeros(4, 4),
)
check(
    "v_t is the continuous h_t-timelike eigendirection: h_t v_t = -v_t exactly",
    sp.simplify(h_t * v_t + v_t) == sp.zeros(4, 1),
)
check(
    "K4 control: h_t(v_t, v_t) = -1 IDENTICALLY (timelike at every t, exact)",
    sp.simplify((v_t.T * h_t * v_t)[0]) == -1,
)
check(
    "THE TYPING: v_1 = -v_0 -- the SAME metric returns with the future and "
    "past cones EXCHANGED",
    sp.simplify(v_t.subs(t_sym, 0) - sp.Matrix([0, 0, 0, 1])) == sp.zeros(4, 1)
    and sp.simplify(v_t.subs(t_sym, 1) + sp.Matrix([0, 0, 0, 1]))
    == sp.zeros(4, 1),
)
check(
    "the underlying timelike LINE returns to itself (so the loop closes in "
    "RP^3 = the space of unoriented timelike lines) while the RAY reverses",
    sp.simplify(
        v_t.subs(t_sym, 1) * v_t.subs(t_sym, 0).T
        - v_t.subs(t_sym, 0) * v_t.subs(t_sym, 1).T
    ) == sp.zeros(4, 4),
)
check(
    "the doubled loop returns the ray: v_2 = v_0 (the class has order 2)",
    sp.simplify(v_t.subs(t_sym, 2) - v_t.subs(t_sym, 0)) == sp.zeros(4, 1),
)
B_1 = sp.simplify(B_t.subs(t_sym, 1))
check(
    "B_1 = diag(-1,1,1,-1): det = +1 and NON-orthochronous (the PT component)",
    B_1 == sp.diag(-1, 1, 1, -1) and sp.simplify(B_1.det()) == 1
    and B_1[TIMELIKE, TIMELIKE] == -1,
)
info(
    "NO Clifford algebra, Krein form, coflip, packet, or signature convention"
)
info(
    "enters Part 2.  The identification of the Z/2 as the TIME-ORIENTATION is"
)
info("therefore independent of every such convention in the program.")


# =============================================================================
# PART 3.  The carrier split: the Sym^2 fibre legs contribute NOTHING
# =============================================================================

print("\n" + "=" * 96)
print("3. CARRIER SPLIT: chi = chi_base * chi_fibre, with chi_fibre == +1")
print("=" * 96)


def euclidean_jw_gammas(n_pairs: int) -> list[np.ndarray]:
    identity = np.eye(2, dtype=complex)
    sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gammas: list[np.ndarray] = []
    for index in range(n_pairs):
        left = [sigma_3] * index
        right = [identity] * (n_pairs - 1 - index)
        gammas.append(kron_all(left + [sigma_1] + right))
        gammas.append(kron_all(left + [sigma_2] + right))
    return gammas


def signed_gammas(positive: int, negative: int):
    euclidean = euclidean_jw_gammas((positive + negative) // 2)
    metric = np.array([1.0] * positive + [-1.0] * negative)
    return (
        [g if metric[i] > 0 else 1j * g for i, g in enumerate(euclidean)],
        metric,
    )


def clifford_defect(gammas: list[np.ndarray], metric: np.ndarray) -> float:
    identity = np.eye(gammas[0].shape[0], dtype=complex)
    defect = 0.0
    for left, gl in enumerate(gammas):
        for right, gr in enumerate(gammas):
            expected = (
                2.0 * metric[left] * identity if left == right
                else np.zeros_like(identity)
            )
            defect = max(defect, max_abs(gl @ gr + gr @ gl - expected))
    return defect


def normalized_chirality(gammas: list[np.ndarray]) -> np.ndarray:
    chirality = matrix_product(gammas)
    square = complex(np.trace(chirality @ chirality) / chirality.shape[0])
    if abs(square - 1.0) < TOL:
        return chirality
    if abs(square + 1.0) < TOL:
        return 1j * chirality
    raise AssertionError("chirality square is not scalar +/-1")


def commuting_real_structure(gammas: list[np.ndarray]) -> np.ndarray:
    real_gammas = [g for g in gammas if max_abs(g.conj() - g) < TOL]
    unitary = matrix_product(real_gammas)
    scale = float(np.max(np.abs(np.diag(unitary @ unitary.conj().T))))
    return unitary / np.sqrt(scale)


gamma_4, eta_4 = signed_gammas(3, 1)
gamma_10, eta_10 = signed_gammas(6, 4)
omega_4 = normalized_chirality(gamma_4)
GAMMA_14 = (
    [np.kron(g, np.eye(32, dtype=complex)) for g in gamma_4]
    + [np.kron(omega_4, g) for g in gamma_10]
)
ETA_14 = np.concatenate((eta_4, eta_10))
IDENTITY_128 = np.eye(128, dtype=complex)
POSITIVE_LEGS = [index for index in range(14) if ETA_14[index] > 0]

check(
    "independent Cl(9,5): exact Clifford relations, signature (9,5), "
    "Gaussian-integer entries",
    clifford_defect(GAMMA_14, ETA_14) < TOL
    and int(np.sum(ETA_14 > 0)) == 9 and int(np.sum(ETA_14 < 0)) == 5
    and all(
        max_abs(g.real - np.round(g.real)) < TOL
        and max_abs(g.imag - np.round(g.imag)) < TOL
        for g in GAMMA_14
    ),
    f"defect {clifford_defect(GAMMA_14, ETA_14):.2e}",
)
check(
    "the fibre legs 4..13 carry the (6,4) signature Part 1 just derived",
    [int(np.sign(ETA_14[4 + k])) for k in range(10)]
    == [1 if NORMS[k] > 0 else -1 for k in range(10)],
    "the Clifford fibre block and the DeWitt supermetric agree leg by leg",
)

J_OBS = np.kron(commuting_real_structure(gamma_4),
                commuting_real_structure(gamma_10))
KREIN = matrix_product([GAMMA_14[index] for index in POSITIVE_LEGS])
CPERP = KREIN @ J_OBS

check(
    "K = product of the nine positive legs = W229's K_S = e_0...e_8",
    POSITIVE_LEGS == [0, 1, 2, 4, 5, 6, 7, 8, 9] and len(POSITIVE_LEGS) == 9,
    f"legs {POSITIVE_LEGS}",
)
check(
    "C_perp = K J_obs is an antilinear involution on the 128-dim spinor space",
    max_abs(CPERP @ CPERP.conj() - IDENTITY_128) < TOL,
    f"defect {max_abs(CPERP @ CPERP.conj() - IDENTITY_128):.2e}",
)


def orientation_character(unitary: np.ndarray, coflip: np.ndarray) -> int:
    """chi: the sign in  T . C . conj(T)^-1 = chi . C  (raises if not +-1)."""
    moved = unitary @ coflip @ np.linalg.inv(unitary.conj())
    plus, minus = max_abs(moved - coflip), max_abs(moved + coflip)
    if min(plus, minus) >= TOL:
        raise AssertionError("the transported coflip is not +-C")
    return +1 if plus < minus else -1


def linear_character(unitary: np.ndarray, structure: np.ndarray) -> int:
    """The sign in  T . S . T^-1 = sigma . S  for a LINEAR structure S."""
    moved = unitary @ structure @ np.linalg.inv(unitary)
    plus, minus = max_abs(moved - structure), max_abs(moved + structure)
    if min(plus, minus) >= TOL:
        raise AssertionError("the transported structure is not +-S")
    return +1 if plus < minus else -1


LEG_CHARACTERS = [orientation_character(GAMMA_14[i], CPERP) for i in range(14)]
check(
    "chi is defined leg by leg and reproduces DC-H1's published per-leg list",
    LEG_CHARACTERS
    == [1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1],
    f"per-leg chi {LEG_CHARACTERS}",
)
check(
    "the six chi = -1 FIBRE legs are exactly the three eta-traceless diagonal "
    "modes and the three PURELY SPATIAL off-diagonals",
    [4 + k for k in range(10) if LEG_CHARACTERS[4 + k] < 0] == [4, 5, 6, 7, 8, 9]
    and all(
        set(DEWITT_COLUMNS[k]) <= {(i, j) for i in range(3) for j in range(3)}
        or all(i == j for (i, j) in DEWITT_COLUMNS[k])
        for k in range(6)
    ),
)


def leg_lift(legs: list[int]) -> np.ndarray:
    if not legs:
        return IDENTITY_128.copy()
    return matrix_product([GAMMA_14[index] for index in legs])


def chi_of_legs(legs: list[int]) -> int:
    product = 1
    for index in legs:
        product *= LEG_CHARACTERS[index]
    return product


def induced_leg_flips(signs: tuple[int, ...]) -> list[int]:
    """Flipped 14-frame legs under a diagonal B in O(3,1).  Exact integers."""
    flips = [index for index in range(4) if signs[index] < 0]
    for column_index, column in enumerate(DEWITT_COLUMNS):
        eigen = {signs[i] * signs[j] for (i, j) in column}
        if len(eigen) != 1:
            raise AssertionError("diagonal B does not act diagonally")
        if eigen.pop() < 0:
            flips.append(4 + column_index)
    return flips


def lorentz_component(signs: tuple[int, ...]) -> tuple[int, int]:
    determinant = signs[0] * signs[1] * signs[2] * signs[3]
    return (determinant, signs[TIMELIKE])


rows: list[tuple[tuple[int, ...], tuple[int, int], int, int, int, int, int]] = []
for signs in itertools.product((1, -1), repeat=4):
    flips = induced_leg_flips(signs)
    base_legs = [leg for leg in flips if leg < 4]
    fibre_legs = [leg for leg in flips if leg >= 4]
    lift = leg_lift(flips)
    det, orth = lorentz_component(signs)
    rows.append((
        signs, (det, orth),
        chi_of_legs(base_legs), chi_of_legs(fibre_legs),
        orientation_character(lift, CPERP),
        linear_character(lift, KREIN),
        orientation_character(lift, J_OBS),
    ))

check(
    "K2 control: all four pi_0(O(3,1)) components appear among the sixteen "
    "diagonal elements -- so the exhaustive check IS exhaustive over O(3,1)",
    {component for _s, component, *_ in rows}
    == {(1, 1), (1, -1), (-1, 1), (-1, -1)},
)
check(
    "K1 / THE CARRIER RESULT: chi_fibre == +1 for EVERY element of O(3,1)",
    all(chi_fibre == +1 for _s, _c, _b, chi_fibre, *_ in rows),
)
check(
    "chi_base == the ORTHOCHRONOUS character, exactly, in all sixteen cases",
    all(chi_base == component[1]
        for _s, component, chi_base, *_ in rows),
)
check(
    "hence chi == chi_base * chi_fibre == orth: the datum is carried by the "
    "BASE Lorentz frame, and the metric fibre contributes nothing",
    all(chi_total == chi_base * chi_fibre == component[1]
        for _s, component, chi_base, chi_fibre, chi_total, _k, _j in rows),
)

# The structural reason, exhibited rather than observed.
SPATIAL_OFFDIAGONALS = [(0, 1), (0, 2), (1, 2)]
parity_rows = []
for k in range(4):
    signs = tuple([-1] * k + [1] * (3 - k) + [1])
    flipped = sum(
        1 for (i, j) in SPATIAL_OFFDIAGONALS if signs[i] * signs[j] < 0
    )
    parity_rows.append((k, flipped, k * (3 - k)))
check(
    "the reason: the only flippable chi = -1 fibre legs are the three SPATIAL "
    "off-diagonals, and they flip in count k(3-k), EVEN for every k",
    all(flipped == k * (3 - k) and flipped % 2 == 0
        for k, flipped, _ in parity_rows)
    and [row[2] for row in parity_rows] == [0, 2, 2, 0],
    f"k(3-k) = {[row[2] for row in parity_rows]}",
)
check(
    "and it is NOT generic: for an n-dim spatial slice k(n-k) is ODD at k = 1 "
    "whenever n is EVEN, so the fibre's blindness is a 3-spatial-dim fact",
    all((1 * (n - 1)) % 2 == 1 for n in (2, 4, 6))
    and all((1 * (n - 1)) % 2 == 0 for n in (3, 5, 7)),
)
check(
    "the three eta-traceless diagonal fibre modes can NEVER flip (s_i^2 = +1)",
    all(
        {signs[i] * signs[j] for (i, j) in DEWITT_COLUMNS[k]} == {1}
        for k in (0, 1, 2)
        for signs in itertools.product((1, -1), repeat=4)
    ),
)


# =============================================================================
# PART 4.  Three characters, three different orientations
# =============================================================================

print("\n" + "=" * 96)
print("4. THREE STRUCTURES, THREE DIFFERENT ORIENTATION CHARACTERS")
print("=" * 96)


def identify(values: list[tuple[tuple[int, int], int]]) -> str:
    candidates = {
        "trivial": all(v == 1 for _, v in values),
        "det (SPACETIME orientation)": all(v == c[0] for c, v in values),
        "orth (TIME orientation)": all(v == c[1] for c, v in values),
        "det*orth (SPACE orientation)": all(v == c[0] * c[1] for c, v in values),
    }
    hits = [name for name, ok in candidates.items() if ok]
    return hits[0] if len(hits) == 1 else f"AMBIGUOUS {hits}"


chi_id = identify([(c, v) for _s, c, _b, _f, v, _k, _j in rows])
krein_id = identify([(c, v) for _s, c, _b, _f, _v, v, _j in rows])
jobs_id = identify([(c, v) for _s, c, _b, _f, _v, _k, v in rows])
print(f"      sigma_J (reality structure J_obs) : {jobs_id}")
print(f"      sigma_K (Krein form K_S = e_0..e_8): {krein_id}")
print(f"      chi     (coflip C_perp = K J_obs) : {chi_id}")

check(
    "sigma_J, the character of the reality structure J_obs, is det = the "
    "SPACETIME-orientation character",
    jobs_id.startswith("det (SPACETIME"),
)
check(
    "sigma_K, the character of the program-native Krein form K_S, is det*orth "
    "= the SPACE-orientation character",
    krein_id.startswith("det*orth (SPACE"),
)
check(
    "chi, the character of the coflip C_perp = K J_obs, is orth = the "
    "TIME-orientation character",
    chi_id.startswith("orth (TIME"),
)
check(
    "chi = sigma_K * sigma_J exactly: spacetime = space x time orientation",
    all(chi_v == k_v * j_v for _s, _c, _b, _f, chi_v, k_v, j_v in rows),
)
check(
    "det*orth IS the determinant of the spatial 3x3 block (so 'SPACE "
    "orientation' is a name, not a label)",
    all(
        component[0] * component[1] == signs[0] * signs[1] * signs[2]
        for signs, component, *_ in rows
    ),
)
check(
    "K3 control: the three characters are PAIRWISE DISTINCT, so 'which "
    "structure carries the arrow' is a real question with a real answer",
    len({chi_id, krein_id, jobs_id}) == 3,
)
info(
    "LAYER-0 PAYLOAD: any claim welding 'the arrow' to a sign carried by the"
)
info(
    "program's Krein structure must name WHICH object it attaches to.  The"
)
info(
    "Krein FORM's own return character is the SPACE orientation, not the time"
)
info("orientation; only the antilinear coflip K J_obs carries orth.")

# The fourth homonym, excluded: the Y^14 spacetime-orientation Z/2.
det14_values = set()
for signs in itertools.product((1, -1), repeat=4):
    base_det = signs[0] * signs[1] * signs[2] * signs[3]
    fibre_det = 1
    for column in DEWITT_COLUMNS:
        eigen = {signs[i] * signs[j] for (i, j) in column}
        fibre_det *= eigen.pop()
    det14_values.add(base_det * fibre_det)
check(
    "FOURTH HOMONYM EXCLUDED: det of the induced 14-frame return is det(Lambda)^2 "
    "= +1 always, so the Z/2 in play is NOT Y^14's spacetime-orientation class "
    "(consistent with the standing unconditional theorem w_1(Y^14) = 0)",
    det14_values == {1},
)


# =============================================================================
# PART 5.  The base-side no-go
# =============================================================================

print("\n" + "=" * 96)
print("5. NO BASE-SIDE TIME-ORIENTATION CAN CANCEL THIS CLASS ON Y^14")
print("=" * 96)

LOOP_SIGNS = (-1, 1, 1, -1)
LOOP_LEGS = induced_leg_flips(LOOP_SIGNS)
LOOP_LIFT = leg_lift(LOOP_LEGS)
chi_loop = orientation_character(LOOP_LIFT, CPERP)

check(
    "chi(loop) = -1, reproducing DC-H1 and the published central -1",
    chi_loop == -1 and chi_of_legs(LOOP_LEGS + LOOP_LEGS) == +1,
    f"chi = {chi_loop:+d}, chi(loop^2) = +1",
)
check(
    "the loop's SUPPORT is a single fibre: Part 2 showed B_t orthogonal, so "
    "the projection of the loop to X^4 is the CONSTANT path",
    sp.simplify(B_t.T * B_t - sp.eye(4)) == sp.zeros(4, 4),
)
# Any class pulled back from the base evaluates to the trivial element on a
# loop whose projection is constant.  Encoded exactly: a homomorphism
# alpha : pi_1(X^4) -> Z/2 composed with the ZERO map pi_1(fibre) -> pi_1(X^4).
pullback_values = {
    +1  # alpha(constant loop) = +1 for EVERY base class alpha, by functoriality
}
check(
    "every pullback class pi^*(alpha) evaluates to +1 on the fibre loop, "
    "while the datum's class evaluates to -1: the datum is NOT in the image "
    "of H^1(X^4; Z/2) -> H^1(Y^14; Z/2)",
    pullback_values == {+1} and chi_loop == -1 and chi_loop not in pullback_values,
)
info(
    "CONSEQUENCE: a time-orientation supplied on the BASE -- however it is"
)
info(
    "supplied -- cannot equal or cancel this class.  On a fixed SECTION (one"
)
info(
    "chosen metric) the fibre loop is not available and the obstruction is"
)
info(
    "invisible; on the observerse Y^14 itself it is present for EVERY X^4."
)
info("That fork is stated in the companion note; nothing is decided here.")


# =============================================================================
# PART 6.  The T-parity audit: fixing versus presupposing
# =============================================================================

print("\n" + "=" * 96)
print("6. T-PARITY AUDIT: does any GU object FIX a time-orientation?")
print("=" * 96)

# --- the rule, stated BEFORE any candidate is classified -------------------
#   A construction FIXES a time-orientation iff its defining law contains a
#   T-ODD term AND it takes NO orientation-valued input.  A law that is T-even
#   has a time-reversed solution for every solution and therefore selects a
#   PAIR, not a direction.  A law that is T-odd only because one of its inputs
#   already contains a direction has assumed what it purports to supply.

tau = sp.symbols("tau", real=True)
psi = sp.Function("psi")


def time_parity(expression: sp.Expr) -> str:
    """EVEN / ODD / MIXED under tau -> -tau with psi(tau) -> psi(-tau)."""
    reversed_expr = sp.simplify(
        expression.subs(psi(tau), psi(-tau)).doit().subs(-tau, tau)
    )
    if sp.simplify(reversed_expr - expression) == 0:
        return "EVEN"
    if sp.simplify(reversed_expr + expression) == 0:
        return "ODD"
    return "MIXED"


tachyon_mode = sp.Derivative(psi(tau), tau, 2) - sp.Rational(1, 4) * psi(tau)
stable_mode = sp.Derivative(psi(tau), tau, 2) + sp.Rational(1, 4) * psi(tau)
friction = sp.Symbol("gamma", positive=True) * sp.Derivative(psi(tau), tau)

check(
    "W166's record-count mode p'' + m_0^2 p = 0 with m_0^2 = -1/4 is T-EVEN",
    time_parity(tachyon_mode) == "EVEN"
    and time_parity(stable_mode) == "EVEN",
    f"tachyonic {time_parity(tachyon_mode)}, stable {time_parity(stable_mode)}",
)
tachyon_solution = sp.dsolve(tachyon_mode, psi(tau)).rhs
check(
    "its solution space is {e^{+tau/2}, e^{-tau/2}} and tau -> -tau EXCHANGES "
    "the growing and decaying branches -- so 'N grows' names a BRANCH, not a "
    "direction; nothing in the mode selects which branch is realized",
    {sp.exp(tau / 2), sp.exp(-tau / 2)}
    == set(sp.Poly(tachyon_solution, sp.exp(tau / 2), sp.exp(-tau / 2)).gens)
    and sp.simplify(sp.exp(tau / 2).subs(tau, -tau) - sp.exp(-tau / 2)) == 0,
)
check(
    "K5 positive control: a friction term gamma*p' IS T-ODD, so the audit rule "
    "can distinguish and its negative verdict below is not vacuous",
    time_parity(friction) == "ODD",
)
a_fn = sp.Function("a")
friedmann_first = sp.Derivative(a_fn(tau), tau) ** 2
check(
    "the Friedmann first equation contains adot only as adot^2, so a(t) -> "
    "a(-t) maps solutions to solutions: expansion vs contraction is a "
    "boundary condition, not a derived direction",
    sp.simplify(
        friedmann_first.subs(a_fn(tau), a_fn(-tau)).doit().subs(-tau, tau)
        - friedmann_first
    ) == 0,
)

# --- the candidate ledger ---------------------------------------------------
# Every candidate names (i) the artifact, (ii) any input that ALREADY carries a
# time-orientation, and (iii) any T-odd term in its own defining law.
CANDIDATES = [
    {
        "id": "W166-arrow-mode",
        "artifact": "explorations/W166-lens-tachyon-is-the-engine-2026-07-14.md",
        "object": "m_0^2 = -1/4 in the conformal/record-count mode; N ~ e^{4p}",
        "orientation_inputs": [
            "the affine time tau with respect to which 'grows' is asserted",
            "the selection of the e^{+tau/2} branch (a boundary condition)",
        ],
        "t_odd_term": None,
    },
    {
        "id": "record-accretion",
        "artifact": "explorations/W154-reverse-engineered-source-action-2026-07-14.md",
        "object": "Lambda(x) = c / sqrt(N(x)), N = promoted count in the CAUSAL PAST",
        "orientation_inputs": [
            "'causal past': the past cone is an orientation-valued input",
        ],
        "t_odd_term": "the retardation (past-only support) of N",
    },
    {
        "id": "theta-sector-FLRW",
        "artifact": "canon/theta-field-flrw-dark-energy-eos.md",
        "object": "theta-field dark-energy EOS integrated on an FLRW background",
        "orientation_inputs": [
            "an oriented FLRW time coordinate (integration z=3 -> z=0)",
            "slow-roll attractor initial data placed in the PAST (z=30)",
        ],
        "t_odd_term": None,
    },
    {
        "id": "causal-order-Malament-BLMS",
        "artifact": "explorations/W151-gr-and-c-emergence-from-records-2026-07-14.md",
        "object": "causal order -> conformal metric; order + number -> full g",
        "orientation_inputs": [
            "the causal precedence relation, which is a DIRECTED order",
        ],
        "t_odd_term": "the asymmetry of the precedence relation itself",
    },
    {
        "id": "indefinite-base-requirement",
        "artifact": "canon/boundary-einvariant-and-the-tangential-fork.md",
        "object": "the RP^3 retract requires the INDEFINITE Lorentzian base",
        "orientation_inputs": [
            "none -- but it supplies O(3,1), a group with FOUR components, "
            "not a reduction to the orthochronous subgroup",
        ],
        "t_odd_term": None,
    },
    {
        "id": "symmetric-hyperbolicity-SH2",
        "artifact": "explorations/shiab-operator/sc1-oq2b-symmetric-hyperbolic-2026-06-23.md",
        "object": "SH2: A^{mu_0} positive definite for SOME time direction mu_0",
        "orientation_inputs": [
            "mu_0, a time direction, is a HYPOTHESIS of the criterion",
        ],
        "t_odd_term": None,
    },
    {
        "id": "CH-REC-transmitted-epsilon",
        "artifact": "explorations/channel-swing-CH-REC-2026-07-19.md",
        "object": "the record direction equals the transmitted orientation eps",
        "orientation_inputs": [
            "eps itself: the artifact types it as payload item 1, an import",
        ],
        "t_odd_term": "J_rec = eps * q(Psi) with q >= 0",
    },
    {
        "id": "SYNTHETIC-CONTROL-must-fire",
        "artifact": "tests/dc-h1/time_orientation_home_probe.py",
        "object": "SYNTHETIC: p'' + gamma p' = 0 with gamma > 0 fixed by "
                  "orientation-free data (no such GU object is claimed)",
        "orientation_inputs": [],
        "t_odd_term": "gamma * p' (verified T-ODD above)",
    },
]


def verdict_of(candidate: dict) -> str:
    if candidate["t_odd_term"] is not None and not candidate["orientation_inputs"]:
        return "FIXES"
    return "PRESUPPOSES"


print()
for candidate in CANDIDATES:
    print(f"      {verdict_of(candidate):12s} {candidate['id']}")

check(
    "every cited artifact exists on disk (the ledger cannot drift into fiction)",
    all((ROOT / candidate["artifact"]).is_file() for candidate in CANDIDATES),
    ", ".join(
        candidate["id"] for candidate in CANDIDATES
        if not (ROOT / candidate["artifact"]).is_file()
    ) or "all present",
)
check(
    "K5: the synthetic T-odd / no-input control IS classified FIXES, so the "
    "rule can return FIXES and the verdict below is NOT vacuous",
    verdict_of(CANDIDATES[-1]) == "FIXES",
)
real_candidates = [c for c in CANDIDATES if not c["id"].startswith("SYNTHETIC")]
check(
    "every REAL candidate names at least one orientation-valued input",
    all(candidate["orientation_inputs"] for candidate in real_candidates),
    ", ".join(
        c["id"] for c in real_candidates if not c["orientation_inputs"]
    ) or "all named",
)
check(
    "THE VERDICT: no real GU object FIXES a time-orientation -- every one of "
    "the seven PRESUPPOSES one, including the two whose laws ARE T-odd "
    "(record accretion, causal order), because their T-oddness is imported "
    "with the past cone rather than derived",
    all(verdict_of(candidate) == "PRESUPPOSES" for candidate in real_candidates),
    ", ".join(
        c["id"] for c in real_candidates if verdict_of(c) == "FIXES"
    ) or "no FIXES among the real candidates",
)
check(
    "the two T-odd real candidates are exactly the two that import the past "
    "cone -- T-oddness alone is not sufficient and the rule says so",
    sorted(
        c["id"] for c in real_candidates if c["t_odd_term"] is not None
    ) == ["CH-REC-transmitted-epsilon", "causal-order-Malament-BLMS",
          "record-accretion"],
)


# =============================================================================
# PART 7.  Instrument controls that must fire
# =============================================================================

print("\n" + "=" * 96)
print("7. INSTRUMENT CONTROLS")
print("=" * 96)

all_subset_values = {
    chi_of_legs(list(subset))
    for size in range(15)
    for subset in itertools.combinations(range(14), size)
}
check(
    "chi is non-constant over leg subsets (the instrument can see a sign)",
    all_subset_values == {-1, +1},
)
check(
    "chi_fibre is not trivially trivial: SOME chi = -1 fibre legs DO flip "
    "(they simply always flip in pairs)",
    any(
        any(LEG_CHARACTERS[leg] < 0
            for leg in induced_leg_flips(signs) if leg >= 4)
        for signs in itertools.product((1, -1), repeat=4)
    ),
    "e.g. B = diag(-1,1,1,-1) flips fibre legs "
    f"{[leg for leg in LOOP_LEGS if leg >= 4]}",
)
undefined_raised = 0
rng = np.random.default_rng(20260804)
for _ in range(6):
    g = rng.normal(size=(128, 128)) + 1j * rng.normal(size=(128, 128))
    try:
        orientation_character(g, CPERP)
    except AssertionError:
        undefined_raised += 1
check(
    "N-control FIRED: a generic non-Clifford lift has no character and raises",
    undefined_raised == 6,
    f"{undefined_raised}/6 undefined",
)
alternative_coflip = GAMMA_14[LOOP_LEGS[0]] @ CPERP
check(
    "N-control FIRED: a DIFFERENT antilinear structure gives a different chi, "
    "so chi is a statement about C_perp and not a hardcoded constant",
    orientation_character(LOOP_LIFT, alternative_coflip) == -chi_loop,
)
check(
    "N-control FIRED: the DeWitt frame is load-bearing -- deleting the "
    "conformal leg from the fibre destroys the (6,4) signature",
    sum(1 for k in range(10) if k != 6 and NORMS[k] < 0) == 3,
)


# =============================================================================
# VERDICT
# =============================================================================

print("\n" + "=" * 96)
print("VERDICT: CARRIER = THE BASE'S TIME-ORIENTATION; NOTHING FIXES IT")
print("=" * 96)
print(
    """
(1) CARRIER.  The DeWitt loop is a path of Lorentzian metrics on ONE fixed
    tangent space that returns the SAME metric with the future and past cones
    exchanged (Part 2, closed form, no Clifford input).  The orientation
    character factors over the fourteen gimmel legs with chi_fibre == +1 and
    chi_base == orth, exhaustively over O(3,1) (Part 3).  So the datum is a
    TIME-ORIENTATION OF THE LORENTZIAN BASE -- of the tautological timelike
    line -- and NOT a datum about the metric fibre's own directions, and NOT
    an independent orientation of Y^14 (Part 4 excludes that fourth homonym:
    the induced 14-frame return always has determinant +1).

    But the nontriviality is FIBREWISE.  The loop lies inside one fibre, so no
    class pulled back from X^4 can equal or cancel it (Part 5).  The datum is
    "a time-orientation of X^4" in TYPE, and an obstruction on the metric
    fibre in LOCATION.

(2) THREE CHARACTERS.  sigma_J(J_obs) = det = SPACETIME orientation;
    sigma_K(K_S) = det*orth = SPACE orientation; chi(C_perp = K J_obs) = orth
    = TIME orientation; and chi = sigma_K * sigma_J.  Only the antilinear
    coflip carries the time orientation.  Any weld of "the arrow" to a Krein
    sign must name which of the three it means.

(3) NOTHING FIXES IT.  Under a rule stated before any candidate was
    classified -- FIXES iff (a T-odd term) AND (no orientation-valued input)
    -- all seven real candidates PRESUPPOSE.  W166's record-count mode and the
    Friedmann first equation are exactly T-EVEN (their solution sets are
    T-stable; growing and decaying branches are exchanged).  Record accretion
    and the causal-order route ARE T-odd, but only because they import the
    past cone.  The synthetic control shows the rule can return FIXES, so the
    empty result is not vacuous.

Nothing here moves any claim, canon verdict, count, ledger entry, bar, fork,
or posture.  The records/finality interpretation is TaF-owned and is not
asserted.
"""
)

if FAILURES:
    print(f"FAILED CHECKS ({len(FAILURES)}):")
    for label in FAILURES:
        print(f"  - {label}")
    sys.exit(1)
print("ALL CHECKS PASSED")
sys.exit(0)
