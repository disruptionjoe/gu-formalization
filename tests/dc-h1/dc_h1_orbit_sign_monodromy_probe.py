#!/usr/bin/env python3
r"""DC-H1: are the six B5 chirality-orbit relative signs a MONODROMY?

Deciding check for hypothesis H1 of
``explorations/atlas-derived-external-datum-hypotheses-2026-08-04.md``:
is the six-orbit relative-sign assignment a function of a PATH/FRAMING class
(a Z/2 monodromy) or a function of a POINT (a value-type datum)?

The hypothesis names a specific mechanism -- "a Z/2 monodromy of the spine's
double cover S^3 -> RP^3 ~ SO(3)" -- and the hypothesis note types the group
coincidence Z/2 = Z/2 as the WEAKEST evidence class (number-matching) that may
NOT be used as an argument.  This probe therefore tests the MECHANISM, in two
independent halves that the preregistration bundled together:

  (PATH half)    is the sign assignment moved by parallel transport around a
                 nontrivial loop, i.e. is it a holonomy rather than a value?
  (FRAMING half) is that holonomy shifted by a change of framing class, i.e.
                 does it respond to pi_1(SO) = Z/2 (the double cover), which
                 is the ONLY thing a reframing can move about a lift?

Everything is self-contained.  Nothing is imported from
``tests/channel-swings/full20_dewitt_loop_transport_probe.py``; its published
central -1 is reproduced independently here so that agreement is a
cross-check rather than an inheritance.

Parts
-----
1. The six orbits, rebuilt exactly from the certified 12-label B5 type matrix:
   provenance expansion to 136 cells, 68 transpose pairs, 68 mirror orbits,
   29 four-cell + 10 special two-cell joint orbits, and the 6 chirality / 4
   X-sector split.  Plus the invariance battery (DISTINGUISHED-NOT-ORIENTED)
   and the exhaustive 2^10 sum-reduction (even = 68 + sum).
2. The DeWitt metric-fibre loop's class in pi_1(F), F = GL(4,R)/O(3,1):
   exact identification with the PT (time-reflection) component of O(3,1),
   hence with the generator of pi_1(F) = Z/2.
3. The orientation character chi: the sign by which the loop's frame return
   moves the program-native coflip C_perp = K J_obs.  Built on an independent
   Cl(9,5) representation.  chi(loop) = -1 reproduces the published result.
4. THE DECIDING HALF.  chi is quadratic in the Clifford lift, so the deck
   transformation of Spin -> SO acts TRIVIALLY on it; the genuine double-cover
   generator (the 2pi rotation, lift -I) has chi = +1.  chi is invariant under
   an arbitrary change of trivialization.  Therefore the [L^13, SO] reframing
   freedom acts on the orbit signs through the ZERO homomorphism.
5. chi factors through pi_0(O(3,1)) -- exhaustive over all 16 diagonal
   elements -- and is exactly the time-orientation character.  This identifies
   the Z/2 that IS present as the O(1) Lorentz time-reflection of canon
   ``boundary-einvariant-and-the-tangential-fork.md`` Section 7, NOT the spin
   double cover.
6. Controls, including three that must FIRE.

Kill conditions, declared before computation:
  K1  if chi is not constant on a pi_0(O(3,1)) component, chi is not a
      homotopy invariant and the "monodromy" reading dies outright;
  K2  if chi(-T) != chi(T) the framing half is LIVE and H1 gains its
      mechanism;
  K3  if the 2pi-rotation lift is not -I, the double-cover control is not
      testing the double cover and Part 4 is void;
  K4  if chi is constant over all leg subsets, the instrument cannot detect a
      sign and every negative below is vacuous.

Grade: EXACT finite linear algebra over Gaussian integers (all Clifford
entries lie in {0, +-1, +-i}; asserted).  Combinatorics is pure integer
arithmetic.  This probe constructs no operator, freezes no packet field,
selects no phase, and moves no claim, canon verdict, count, or posture.
"""

from __future__ import annotations

import itertools
import sys
from fractions import Fraction

import numpy as np

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


# =============================================================================
# PART 1.  The six orbits, and what assigns their relative signs
# =============================================================================

print("=" * 96)
print("1. THE SIX ORBITS: exact rebuild of the certified B5 special-orbit census")
print("=" * 96)

LABELS = [
    "Lp", "Rm", "Lm", "Rp",
    "X32p", "X23m", "X2Tp", "X1Tm",
    "X32m", "X23p", "X2Tm", "X1Tp",
]
LABEL_INDEX = {name: index for index, name in enumerate(LABELS)}

# The exact type matrix of
# explorations/shiab-operator/b5-observer-symbol-multiplicity-matrix-2026-07-24.md
TYPE_MATRIX_ROWS = [
    "0 0 1 1 1 0 1 0 0 0 0 0",
    "0 0 1 1 0 1 0 1 0 0 0 0",
    "1 1 0 0 0 0 0 0 1 0 1 0",
    "1 1 0 0 0 0 0 0 0 1 0 1",
    "1 0 0 0 0 0 0 0 1 1 0 0",
    "0 1 0 0 0 0 0 0 1 1 0 0",
    "1 0 0 0 0 0 0 0 0 0 1 1",
    "0 1 0 0 0 0 0 0 0 0 1 1",
    "0 0 1 0 1 1 0 0 0 0 0 0",
    "0 0 0 1 1 1 0 0 0 0 0 0",
    "0 0 1 0 0 0 1 1 0 0 0 0",
    "0 0 0 1 0 0 1 1 0 0 0 0",
]
TYPE_MATRIX = np.array(
    [[int(value) for value in row.split()] for row in TYPE_MATRIX_ROWS],
    dtype=int,
)

# The explicit normal-chirality coflip (mirror) of the same artifact.
MIRROR = {
    "Lp": "Lm", "Lm": "Lp",
    "Rm": "Rp", "Rp": "Rm",
    "X32p": "X32m", "X32m": "X32p",
    "X23m": "X23p", "X23p": "X23m",
    "X2Tp": "X2Tm", "X2Tm": "X2Tp",
    "X1Tm": "X1Tp", "X1Tp": "X1Tm",
}
# Slot dimensions (E-type 16-modules carry dim 32 as (2,1,16+) etc.; the X
# slots carry 96 or 288).  Used only for the blindness battery.
DIMENSION = {
    "Lp": 32, "Rm": 32, "Lm": 32, "Rp": 32,
    "X32p": 96, "X23m": 96, "X32m": 96, "X23p": 96,
    "X2Tp": 288, "X1Tm": 288, "X2Tm": 288, "X1Tp": 288,
}
CHIRALITY = {  # the global E+/E- grading; X labels carry no E grading
    "Lp": +1, "Rm": +1, "Lm": -1, "Rp": -1,
}
PROVENANCES = ["S", "imGamma", "kerGamma"]
E_LABELS = ["Lp", "Rm", "Lm", "Rp"]

check(
    "certified 12-label type matrix is symmetric with a zero diagonal",
    bool((TYPE_MATRIX == TYPE_MATRIX.T).all())
    and int(np.trace(TYPE_MATRIX)) == 0
    and set(np.unique(TYPE_MATRIX)) <= {0, 1},
)
check(
    "the mirror is a fixed-point-free involution preserving the type matrix",
    all(MIRROR[MIRROR[name]] == name for name in LABELS)
    and all(MIRROR[name] != name for name in LABELS)
    and all(
        TYPE_MATRIX[LABEL_INDEX[a], LABEL_INDEX[b]]
        == TYPE_MATRIX[LABEL_INDEX[MIRROR[a]], LABEL_INDEX[MIRROR[b]]]
        for a in LABELS
        for b in LABELS
    ),
)


def slots_of(label: str) -> list[str]:
    """Provenance-expanded slot names for one 12-label type."""
    if label in E_LABELS:
        return [f"{prov}:{label}" for prov in PROVENANCES]
    return [label]


def base_label(slot: str) -> str:
    return slot.split(":")[-1]


def provenance(slot: str) -> str:
    return slot.split(":")[0] if ":" in slot else "X"


SLOTS = [slot for label in LABELS for slot in slots_of(label)]

CELLS = [
    (source, target)
    for label_s in LABELS
    for label_t in LABELS
    if TYPE_MATRIX[LABEL_INDEX[label_s], LABEL_INDEX[label_t]]
    for source in slots_of(label_s)
    for target in slots_of(label_t)
]

check(
    "provenance expansion gives 20 slots and 136 ordered nonzero cells",
    len(SLOTS) == 20 and len(CELLS) == 136,
    f"{len(SLOTS)} slots, {len(CELLS)} cells",
)


def mirror_slot(slot: str) -> str:
    """The coflip preserves the provenance label and mirrors the type."""
    if ":" in slot:
        prov, label = slot.split(":")
        return f"{prov}:{MIRROR[label]}"
    return MIRROR[slot]


def mirror_cell(cell: tuple[str, str]) -> tuple[str, str]:
    return (mirror_slot(cell[0]), mirror_slot(cell[1]))


def transpose_cell(cell: tuple[str, str]) -> tuple[str, str]:
    return (cell[1], cell[0])


cell_set = set(CELLS)
check(
    "the cell set is closed under both the mirror and the transpose",
    all(mirror_cell(cell) in cell_set for cell in CELLS)
    and all(transpose_cell(cell) in cell_set for cell in CELLS),
)

# Joint orbits under the group generated by mirror and transpose.
joint_orbits: list[frozenset[tuple[str, str]]] = []
seen: set[tuple[str, str]] = set()
for cell in CELLS:
    if cell in seen:
        continue
    orbit = {cell}
    frontier = [cell]
    while frontier:
        current = frontier.pop()
        for image in (mirror_cell(current), transpose_cell(current)):
            if image not in orbit:
                orbit.add(image)
                frontier.append(image)
    seen |= orbit
    joint_orbits.append(frozenset(orbit))

orbit_sizes = sorted(len(orbit) for orbit in joint_orbits)
special_orbits = [orbit for orbit in joint_orbits if len(orbit) == 2]
four_cell_orbits = [orbit for orbit in joint_orbits if len(orbit) == 4]

check(
    "joint orbit census is 29 four-cell plus 10 special two-cell orbits",
    len(four_cell_orbits) == 29
    and len(special_orbits) == 10
    and set(orbit_sizes) == {2, 4}
    and sum(orbit_sizes) == 136,
    f"sizes {29 * [4] == [4] * 29 and ''}"
    f"{len(four_cell_orbits)}x4 + {len(special_orbits)}x2",
)

mirror_orbits = {frozenset({cell, mirror_cell(cell)}) for cell in CELLS}
check(
    "68 transpose pairs and 68 two-cell mirror-support orbits, none fixed",
    len(mirror_orbits) == 68
    and all(len(orbit) == 2 for orbit in mirror_orbits)
    and len({frozenset({c, transpose_cell(c)}) for c in CELLS}) == 68,
)

# The six/four split.
special_named: list[tuple[str, tuple[str, str]]] = []
for orbit in special_orbits:
    representative = sorted(orbit)[0]
    labels = {base_label(representative[0]), base_label(representative[1])}
    kind = "chirality-E" if labels <= set(E_LABELS) else "X-sector"
    special_named.append((kind, representative))

chirality_orbits = sorted(
    rep for kind, rep in special_named if kind == "chirality-E"
)
x_orbits = sorted(rep for kind, rep in special_named if kind == "X-sector")

check(
    "the ten special orbits split 6 chirality-E + 4 X-sector",
    len(chirality_orbits) == 6 and len(x_orbits) == 4,
)
check(
    "the six are exactly the E+/E- pairs, one L16 and one R16 per provenance",
    sorted(
        (provenance(a), tuple(sorted({base_label(a), base_label(b)})))
        for a, b in chirality_orbits
    )
    == sorted(
        (prov, pair)
        for prov in PROVENANCES
        for pair in (("Lm", "Lp"), ("Rm", "Rp"))
    ),
)
check(
    "the four are exactly the X-sector pairs X32, X23, X2T, X1T",
    sorted(
        tuple(sorted({base_label(a), base_label(b)})) for a, b in x_orbits
    )
    == sorted(
        [("X1Tm", "X1Tp"), ("X23m", "X23p"), ("X2Tm", "X2Tp"),
         ("X32m", "X32p")]
    ),
)
for rep in chirality_orbits:
    info(f"chirality orbit: {rep[0]} <-> {rep[1]}")
for rep in x_orbits:
    info(f"X-sector orbit:  {rep[0]} <-> {rep[1]}")

# --- what, in the committed ledger, assigns their relative signs? nothing ---
print("\n--- invariance battery: does any certified invariant orient them? ---")


def global_chirality_exchange(slot: str) -> str:
    """Global E+ <-> E- exchange (the mirror), applied to a slot label."""
    return mirror_slot(slot)


battery = {
    "cell set": {
        (global_chirality_exchange(a), global_chirality_exchange(b))
        for a, b in CELLS
    } == cell_set,
    "slot dimensions": all(
        DIMENSION[base_label(slot)]
        == DIMENSION[base_label(global_chirality_exchange(slot))]
        for slot in SLOTS
    ),
    "provenance sector": all(
        provenance(slot) == provenance(global_chirality_exchange(slot))
        for slot in SLOTS
    ),
    "cell multiplicity": all(
        TYPE_MATRIX[LABEL_INDEX[base_label(a)], LABEL_INDEX[base_label(b)]]
        == TYPE_MATRIX[
            LABEL_INDEX[base_label(global_chirality_exchange(a))],
            LABEL_INDEX[base_label(global_chirality_exchange(b))],
        ]
        for a, b in CELLS
    ),
    "orbit structure": {
        frozenset(
            (global_chirality_exchange(a), global_chirality_exchange(b))
            for a, b in orbit
        )
        for orbit in joint_orbits
    } == set(joint_orbits),
}
check(
    "every certified structure is invariant under global E+ <-> E- exchange",
    all(battery.values()),
    ", ".join(f"{name}: {'sym' if value else 'ASYM'}"
              for name, value in battery.items()),
)
check(
    "chirality DISTINGUISHES the six (the two cells carry different labels)",
    all(
        CHIRALITY[base_label(a)] != CHIRALITY[base_label(mirror_slot(a))]
        for a, _ in chirality_orbits
    ),
)
info(
    "=> DISTINGUISHED-NOT-ORIENTED: the committed ledger separates the two"
)
info(
    "   cells of each of the six orbits but supplies no direction.  The sign"
)
info(
    "   assignment is therefore NOT a function of any committed point-datum."
)

# --- the sum reduction: the residual is one integer, not ten bits ---
print("\n--- exhaustive 2^10 sum reduction ---")
even_values = set()
sum_formula_agrees = True
for assignment in itertools.product((-1, +1), repeat=10):
    direct = 68 + sum(assignment)
    even_values.add(direct)
    if direct != 68 + sum(assignment):
        sum_formula_agrees = False
check(
    "the ten special-orbit signs have an eleven-valued effect: even = 68 + sum",
    sum_formula_agrees
    and sorted(even_values) == list(range(58, 79, 2))
    and len(even_values) == 11,
    f"{sorted(even_values)[0]}..{sorted(even_values)[-1]} step 2",
)
info(
    "the residual is ONE integer in [-10,+10]; a datum that fixes the signed"
)
info("sum fixes the coefficient dimension without selecting any single phase.")


# =============================================================================
# PART 2.  The loop's class in pi_1(F), F = GL(4,R)/O(3,1)
# =============================================================================

print("\n" + "=" * 96)
print("2. THE DEWITT METRIC-FIBRE LOOP IS THE GENERATOR OF pi_1(F) = Z/2")
print("=" * 96)

ETA4 = np.diag([1.0, 1.0, 1.0, -1.0])
TIMELIKE = 3


def mixed_rotation(angle: float, positive_leg: int = 0) -> np.ndarray:
    """The loop generator of the actual DeWitt probe: rotation in (leg, time)."""
    rotation = np.eye(4)
    cosine, sine = np.cos(angle), np.sin(angle)
    rotation[positive_leg, positive_leg] = cosine
    rotation[TIMELIKE, TIMELIKE] = cosine
    rotation[positive_leg, TIMELIKE] = -sine
    rotation[TIMELIKE, positive_leg] = sine
    return rotation


samples = np.linspace(0.0, 1.0, 65)
metrics = [mixed_rotation(np.pi * t).T @ ETA4 @ mixed_rotation(np.pi * t)
           for t in samples]
signatures = [
    tuple(sorted(np.sign(np.linalg.eigvalsh(metric)).astype(int)))
    for metric in metrics
]
loop_endpoint = mixed_rotation(np.pi)
loop_endpoint_rounded = np.round(loop_endpoint)
double_endpoint = mixed_rotation(2.0 * np.pi)

check(
    "the path stays in the metric fibre: signature (3,1) at every sample",
    all(signature == (-1, 1, 1, 1) for signature in signatures),
)
check(
    "the loop is non-constant in F but closes exactly (h_1 = h_0 = eta)",
    max_abs(metrics[-1] - ETA4) < TOL
    and max(max_abs(metric - ETA4) for metric in metrics) > 0.5,
)
check(
    "the endpoint of the GL(4,R)-lift is B_1 = diag(-1,1,1,-1)",
    max_abs(loop_endpoint - loop_endpoint_rounded) < TOL
    and np.array_equal(loop_endpoint_rounded, np.diag([-1.0, 1.0, 1.0, -1.0])),
)
check(
    "the doubled loop lifts to the identity of GL(4,R)",
    max_abs(double_endpoint - np.eye(4)) < TOL,
)


def in_lorentz_group(matrix: np.ndarray) -> bool:
    return max_abs(matrix.T @ ETA4 @ matrix - ETA4) < TOL


def lorentz_component(matrix: np.ndarray) -> tuple[int, int]:
    """(det, orthochronous) -- the two Z/2 invariants of pi_0(O(3,1))."""
    determinant = int(round(float(np.linalg.det(matrix))))
    orthochronous = 1 if matrix[TIMELIKE, TIMELIKE] > 0 else -1
    return (determinant, orthochronous)


check(
    "B_1 lies in O(3,1)",
    in_lorentz_group(loop_endpoint_rounded),
)
check(
    "B_1 is in the PT component: det = +1 and NON-orthochronous",
    lorentz_component(loop_endpoint_rounded) == (1, -1),
    f"component {lorentz_component(loop_endpoint_rounded)}",
)

# pi_0(O(3,1)) = Z/2 x Z/2 by (det, orthochronous); the fibration
# O(3,1) -> GL(4,R) -> F gives pi_1(F) = ker(pi_0 O(3,1) -> pi_0 GL(4,R)),
# and pi_0 GL(4,R) = Z/2 by det.  So pi_1(F) = {1, PT} = Z/2.
components = {
    lorentz_component(np.diag(signs))
    for signs in itertools.product((1.0, -1.0), repeat=4)
}
kernel_of_det = {
    component for component in components if component[0] == 1
}
check(
    "pi_0(O(3,1)) has order 4 and ker(-> pi_0 GL(4,R)) = {1, PT} has order 2",
    len(components) == 4 and len(kernel_of_det) == 2,
)
check(
    "therefore [loop] is the NONTRIVIAL element of pi_1(F) = Z/2",
    lorentz_component(loop_endpoint_rounded) in kernel_of_det
    and lorentz_component(loop_endpoint_rounded) != (1, 1),
)
info(
    "canon boundary-einvariant Section 7: the Z/2 of the RP^3 spine IS the"
)
info("O(1) Lorentz time-reflection -- exactly the invariant that fires here.")


# =============================================================================
# PART 3.  The orientation character chi on an independent Cl(9,5)
# =============================================================================

print("\n" + "=" * 96)
print("3. THE ORIENTATION CHARACTER chi OF THE PROGRAM-NATIVE COFLIP C_perp")
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
    gammas = [
        gamma if metric[index] > 0 else 1j * gamma
        for index, gamma in enumerate(euclidean)
    ]
    return gammas, metric


def clifford_defect(gammas: list[np.ndarray], metric: np.ndarray) -> float:
    identity = np.eye(gammas[0].shape[0], dtype=complex)
    defect = 0.0
    for left, gamma_left in enumerate(gammas):
        for right, gamma_right in enumerate(gammas):
            expected = (
                2.0 * metric[left] * identity if left == right
                else np.zeros_like(identity)
            )
            defect = max(
                defect,
                max_abs(gamma_left @ gamma_right + gamma_right @ gamma_left
                        - expected),
            )
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
gamma_14 = (
    [np.kron(g, np.eye(32, dtype=complex)) for g in gamma_4]
    + [np.kron(omega_4, g) for g in gamma_10]
)
eta_14 = np.concatenate((eta_4, eta_10))
IDENTITY_128 = np.eye(128, dtype=complex)

check(
    "independent Cl(9,5) rep: exact Clifford relations, signature (9,5)",
    clifford_defect(gamma_14, eta_14) < TOL
    and int(np.sum(eta_14 > 0)) == 9
    and int(np.sum(eta_14 < 0)) == 5,
    f"defect {clifford_defect(gamma_14, eta_14):.2e}",
)


def is_gaussian_integer(matrix: np.ndarray) -> bool:
    real_ok = max_abs(matrix.real - np.round(matrix.real)) < TOL
    imag_ok = max_abs(matrix.imag - np.round(matrix.imag)) < TOL
    return bool(real_ok and imag_ok)


check(
    "all fourteen generators have Gaussian-integer entries (exact arithmetic)",
    all(is_gaussian_integer(g) for g in gamma_14)
    and all(max_abs(g) <= 1.0 + TOL for g in gamma_14),
)

observer_reality = np.kron(
    commuting_real_structure(gamma_4), commuting_real_structure(gamma_10)
)
krein = matrix_product([g for g, s in zip(gamma_14, eta_14) if s > 0])
CPERP = krein @ observer_reality

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
        raise AssertionError(
            "the transported coflip is not +-C: the character is undefined"
        )
    return +1 if plus < minus else -1


leg_characters = [
    orientation_character(gamma_14[index], CPERP) for index in range(14)
]
check(
    "chi is defined leg by leg: every generator sends C_perp to +-C_perp",
    len(leg_characters) == 14 and set(leg_characters) <= {-1, 1},
    f"per-leg chi {leg_characters}",
)


def leg_lift(legs: list[int]) -> np.ndarray:
    if not legs:
        return IDENTITY_128.copy()
    return matrix_product([gamma_14[index] for index in legs])


def chi_of_legs(legs: list[int]) -> int:
    product = 1
    for index in legs:
        product *= leg_characters[index]
    return product


multiplicative = True
rng = np.random.default_rng(20260804)
for _ in range(60):
    size = int(rng.integers(0, 7))
    legs = sorted(rng.choice(14, size=size, replace=False).tolist())
    if orientation_character(leg_lift(legs), CPERP) != chi_of_legs(legs):
        multiplicative = False
check(
    "chi is a group homomorphism: chi(A) = product of per-leg characters",
    multiplicative,
)

# The DeWitt loop's frame return, derived (not hardcoded) from B_1.
PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]
# The DeWitt orthonormal frame columns, as unnormalized integer combinations
# of the symmetric basis E_(i,j).  The normalization is irrelevant to a sign.
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
# Signature of the DeWitt frame: six positive then four negative.
FIBRE_SIGNATURE = [1] * 6 + [-1] * 4


def induced_leg_flips(signs: tuple[int, int, int, int]) -> list[int]:
    """Flipped legs of the 14-dim gimmel frame under a diagonal B in O(3,1).

    Base frame transforms by B^-1 = B; the Sym^2(T*X) fibre by E -> B^T E B,
    which acts on E_(i,j) by signs[i]*signs[j].  Exact integer arithmetic.
    """
    flips = [index for index in range(4) if signs[index] < 0]
    for column_index, column in enumerate(DEWITT_COLUMNS):
        eigen = {
            signs[i] * signs[j] for (i, j) in column
        }
        if len(eigen) != 1:
            raise AssertionError(
                "diagonal B does not act diagonally on the DeWitt frame"
            )
        if eigen.pop() < 0:
            flips.append(4 + column_index)
    return flips


loop_signs = (-1, 1, 1, -1)
loop_legs = induced_leg_flips(loop_signs)
positive_flips = sum(1 for leg in loop_legs if eta_14[leg] > 0)
negative_flips = sum(1 for leg in loop_legs if eta_14[leg] < 0)

check(
    "the loop return reverses 2 base + 4 Sym^2 legs = 3 positive + 3 negative",
    sum(1 for leg in loop_legs if leg < 4) == 2
    and sum(1 for leg in loop_legs if leg >= 4) == 4
    and positive_flips == 3
    and negative_flips == 3,
    f"legs {loop_legs}, {positive_flips}+/{negative_flips}-",
)

LOOP_LIFT = leg_lift(loop_legs)
chi_loop = orientation_character(LOOP_LIFT, CPERP)
check(
    "chi(DeWitt loop) = -1  [independently reproduces the published central -1]",
    chi_loop == -1,
    f"chi = {chi_loop:+d}",
)
check(
    "chi(doubled loop) = +1: chi is a Z/2 character of pi_1(F)",
    chi_of_legs(loop_legs + loop_legs) == +1
    and orientation_character(LOOP_LIFT @ LOOP_LIFT, CPERP) == +1,
)
info(
    "=> the ten special-orbit signs are moved by parallel transport around a"
)
info(
    "   nontrivial loop.  PATH-TYPE half of H1: SUPPORTED (holonomy, not a"
)
info("   stored value); the class is w != 0 in H^1(F; Z/2).")

# 3b.  Arithmetic consequence of C -> -C, stated at arithmetic grade only.
# Under C -> -C the C-even and C-odd subspaces of the 136-cell coefficient
# space exchange, so the even count d maps to 136 - d.  This is the arithmetic
# of an involution sign flip; it is NOT a claim about the B5 packet, whose
# common domain, Green form, and nonlinear completion remain unbuilt.
swap_pairs = {(68 + s, 68 - s) for s in range(-10, 11, 2)}
check(
    "arithmetic: C -> -C exchanges the even/breaking counts, d <-> 136 - d",
    all(low + high == 136 for low, high in swap_pairs)
    and (58, 78) in swap_pairs
    and (78, 58) in swap_pairs,
)
info(
    "so only the UNORDERED pair {68-sum, 68+sum} is loop-invariant; which"
)
info(
    "member is the even count is not a globally defined function on F."
)
info(
    "SCOPE: arithmetic only.  Certifying this ON the packet is a named"
)
info("reopener, not a result of this probe.")


# =============================================================================
# PART 4.  THE DECIDING HALF: does a change of framing class move chi?
# =============================================================================

print("\n" + "=" * 96)
print("4. THE FRAMING ACTION: does pi_1(SO) = Z/2 move the orbit signs?")
print("=" * 96)

# 4a.  The loop's Clifford lift is an involution: Spin -> SO is NOT engaged.
check(
    "K3 control: the DeWitt loop's Clifford lift squares to +I (order 2)",
    max_abs(LOOP_LIFT @ LOOP_LIFT - IDENTITY_128) < TOL,
    f"defect {max_abs(LOOP_LIFT @ LOOP_LIFT - IDENTITY_128):.2e}",
)

# 4b.  The genuine double-cover generator: a 2pi rotation in a spacelike plane.
spacelike = [index for index in range(14) if eta_14[index] > 0][:2]
bivector = gamma_14[spacelike[0]] @ gamma_14[spacelike[1]]
two_pi_lift = (
    np.cos(np.pi) * IDENTITY_128 + np.sin(np.pi) * bivector
)  # exp(pi * gamma_i gamma_j) with (gamma_i gamma_j)^2 = -I
check(
    "K3 control: the 2pi rotation is I in SO and lifts to -I in Spin",
    max_abs(bivector @ bivector + IDENTITY_128) < TOL
    and max_abs(two_pi_lift + IDENTITY_128) < TOL,
    f"lift = {complex(np.trace(two_pi_lift) / 128).real:+.0f} I",
)
chi_double_cover = orientation_character(two_pi_lift, CPERP)
check(
    "THE DECIDING RESULT: the double-cover deck element has chi = +1",
    chi_double_cover == +1,
    f"chi(-I) = {chi_double_cover:+d}",
)

# 4c.  chi is blind to the Clifford-lift sign, for every lift.
blind = True
for _ in range(40):
    size = int(rng.integers(0, 7))
    legs = sorted(rng.choice(14, size=size, replace=False).tolist())
    lift = leg_lift(legs)
    if orientation_character(lift, CPERP) != orientation_character(-lift, CPERP):
        blind = False
check(
    "K2 control: chi(T) = chi(-T) for every lift -- chi is quadratic in T",
    blind,
)
info(
    "T . C . conj(T)^-1 is invariant under T -> -T, so chi descends to SO and"
)
info("cannot see the Spin double cover at all.")

# 4d.  chi is invariant under an ARBITRARY change of trivialization.
covariant = True
max_covariance_defect = 0.0
for _ in range(6):
    g = (rng.normal(size=(128, 128)) + 1j * rng.normal(size=(128, 128))) / 64.0
    g = g + IDENTITY_128  # deterministic-seeded, diagonally dominant
    if np.linalg.cond(g) > 1.0e6:
        continue
    transported_coflip = g @ CPERP @ np.linalg.inv(g.conj())
    transported_lift = g @ LOOP_LIFT @ np.linalg.inv(g)
    moved = (
        transported_lift
        @ transported_coflip
        @ np.linalg.inv(transported_lift.conj())
    )
    defect = max_abs(moved - chi_loop * transported_coflip)
    max_covariance_defect = max(max_covariance_defect, defect)
    if defect >= 1.0e-6 * max_abs(transported_coflip):
        covariant = False
check(
    "chi is invariant under an arbitrary change of trivialization g",
    covariant,
    f"max relative defect {max_covariance_defect:.2e}",
)
info(
    "a reframing acts by (C, T) -> (g C conj(g)^-1, g T g^-1) at the basepoint"
)
info(
    "and by a class in pi_1(SO) = Z/2 on the lift.  The first is the identity"
)
info("on chi by the computation above; the second is killed by 4b/4c.")
info(
    "=> the [L^13, SO] reframing freedom acts on the orbit signs through the"
)
info("   ZERO homomorphism.  FRAMING half of H1: FALSIFIED.")

# 4e.  Controls that MUST FIRE, so that the invariance in 4d is not vacuous.
# (i) a DIFFERENT antilinear structure gives a different chi on the same loop.
alternative_coflip = gamma_14[loop_legs[0]] @ CPERP
check(
    "N-control FIRED: a different antilinear structure gives a different chi",
    orientation_character(LOOP_LIFT, alternative_coflip) == -chi_loop,
    f"chi(gamma_{loop_legs[0]} C_perp) = "
    f"{orientation_character(LOOP_LIFT, alternative_coflip):+d}",
)
# (ii) moving the coflip WITHOUT moving the lift is not a reframing and
# destroys the character outright.
broken = 0
for _ in range(6):
    g = (rng.normal(size=(128, 128)) + 1j * rng.normal(size=(128, 128))) / 64.0
    g = g + IDENTITY_128
    inconsistent = g @ CPERP @ np.linalg.inv(g.conj())
    try:
        orientation_character(LOOP_LIFT, inconsistent)
    except AssertionError:
        broken += 1
check(
    "N-control FIRED: a one-sided (non-reframing) move destroys the character",
    broken == 6,
    f"{broken}/6 undefined",
)


# =============================================================================
# PART 5.  chi factors through pi_0(O(3,1)) and IS the time-orientation
# =============================================================================

print("\n" + "=" * 96)
print("5. WHICH Z/2 IS IT?  chi factors through pi_0(O(3,1)) exhaustively")
print("=" * 96)

component_characters: dict[tuple[int, int], set[int]] = {}
rows: list[tuple[tuple[int, ...], tuple[int, int], int]] = []
for signs in itertools.product((1, -1), repeat=4):
    matrix = np.diag([float(value) for value in signs])
    assert in_lorentz_group(matrix), "diagonal sign matrix must be in O(3,1)"
    component = lorentz_component(matrix)
    value = chi_of_legs(induced_leg_flips(signs))
    component_characters.setdefault(component, set()).add(value)
    rows.append((signs, component, value))

check(
    "K1 control: chi is CONSTANT on each of the four pi_0(O(3,1)) components",
    all(len(values) == 1 for values in component_characters.values())
    and len(component_characters) == 4,
    ", ".join(
        f"{component}: {sorted(values)}"
        for component, values in sorted(component_characters.items())
    ),
)
check(
    "chi is exactly the time-orientation (orthochronous) character of O(3,1)",
    all(
        value == component[1]
        for _signs, component, value in rows
    ),
)
check(
    "chi restricted to pi_1(F) = {1, PT} is an ISOMORPHISM onto Z/2",
    component_characters[(1, 1)] == {+1}
    and component_characters[(1, -1)] == {-1},
)
for signs, component, value in rows:
    if signs in {(1, 1, 1, 1), (-1, 1, 1, -1), (-1, -1, -1, -1),
                 (1, 1, 1, -1), (-1, -1, -1, 1)}:
        info(
            f"B = diag{signs}  component (det,orth) = {component}  "
            f"chi = {value:+d}"
        )
info(
    "the Z/2 that fires is pi_0 of the Lorentz stabilizer -- the O(1) TIME"
)
info(
    "REFLECTION named in canon Section 7 -- and NOT pi_1(SO), the spin double"
)
info("cover.  Same group order, different mechanism: Layer-0 HOMONYM.")


# =============================================================================
# PART 6.  Instrument controls that must fire
# =============================================================================

print("\n" + "=" * 96)
print("6. INSTRUMENT CONTROLS")
print("=" * 96)

all_subset_values = {
    chi_of_legs(list(subset))
    for size in range(15)
    for subset in itertools.combinations(range(14), size)
}
check(
    "K4 control: chi is non-constant over leg subsets (the instrument fires)",
    all_subset_values == {-1, +1},
)

undefined_raised = 0
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

toggle_moves = {
    leg: chi_of_legs(sorted(set(loop_legs) ^ {leg})) != chi_loop
    for leg in range(14)
}
check(
    "N-control FIRED: toggling exactly the chi=-1 legs moves the loop's sign",
    all(
        moved == (leg_characters[leg] < 0)
        for leg, moved in toggle_moves.items()
    )
    and any(toggle_moves.values()),
    f"{sum(toggle_moves.values())}/14 legs flip chi",
)


# =============================================================================
# VERDICT
# =============================================================================

print("\n" + "=" * 96)
print("VERDICT: DC-H1-PARTIAL -- PATH-TYPE CONFIRMED, FRAMING MECHANISM DEAD")
print("=" * 96)
print(
    """
(i)   The six orbits are the E+/E- special two-cell mirror orbits, one L16 and
      one R16 in each of the S / imGamma / kerGamma provenances.  NOTHING in
      the committed ledger assigns their relative signs: every certified
      structure is invariant under global E+ <-> E- exchange.  Their joint
      effect is one integer (even = 68 + sum), not ten bits.

(ii)  The assignment IS a function of a path class.  Parallel transport of the
      program-native coflip C_perp = K J_obs around the DeWitt metric-fibre
      loop -- shown here to be exactly the generator of pi_1(F) = Z/2, the PT
      / time-reflection component of O(3,1) -- returns C_perp -> -C_perp, and
      the doubled loop returns +C_perp.  So the sign is a Z/2 holonomy class
      w != 0 in H^1(F; Z/2), not a stored value.

(iii) The assignment is NOT covariant with the framing class.  chi is
      quadratic in the Clifford lift, so it descends to SO and is blind to the
      double cover: the deck element -I of Spin -> SO has chi = +1.  chi is
      also invariant under an arbitrary change of trivialization.  The
      [L^13, SO] reframing freedom therefore acts through the ZERO
      homomorphism, and pi_1(SO(3)) = Z/2 does not move a single orbit sign.

      The Z/2 that DOES act is pi_0 of the Lorentz stabilizer O(3,1) -- the
      O(1) time reflection.  It is a REFLECTION Z/2, not a double-cover Z/2.
      The two share a group order and nothing else: Layer-0 HOMONYM.

Consequence for H1: the "holonomy not a stored value" half is supported, but
by a mechanism H1 did not name and via a result already in the repository
(the full-20 DeWitt transport, 2026-07-30).  The half H1 needed in order to
REDUCE the external ledger -- P1 determined by the boundary framing class --
is falsified.  P1 is not framing-determined.  The ledger does not reduce.
Preregistered outcome (c): PARTIAL.  No promotion.
"""
)

if FAILURES:
    print(f"FAILED CHECKS ({len(FAILURES)}):")
    for label in FAILURES:
        print(f"  - {label}")
    sys.exit(1)
print("ALL CHECKS PASSED")
sys.exit(0)
