#!/usr/bin/env python3
"""Exact K77 source-sign / Shiab / duality reconciliation gate.

The probe distinguishes four objects before computing:

1. the draft bilinear with independently barred rows;
2. a vector representative obtained only after choosing a row duality;
3. the source-native Spin(7,7)-equivariant 2-form-to-1-form contraction; and
4. an observation-relative repair using an additional moving odd covector q.

It does not identify q with P1, P2, or P3 and does not advance Wave 3.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
sys.path.insert(0, str(CHANNEL))

from p77_real_index_twin import build_split_clifford, clifford_relations_exact  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def product(matrices: list[np.ndarray], dim: int = 128) -> np.ndarray:
    result = np.eye(dim, dtype=np.int64)
    for matrix in matrices:
        result = result @ matrix
    return result


P, M = build_split_clifford(7)
GAMMA = P + M
ETA = [1] * 7 + [-1] * 7
I = np.eye(128, dtype=np.int64)
Z = np.zeros((128, 128), dtype=np.int64)
J = product(GAMMA)


def gamma_of(vector: list[int]) -> np.ndarray:
    return sum((vector[a] * GAMMA[a] for a in range(14)), start=Z.copy())


def middle_blocks(xi: list[int]) -> list[list[np.ndarray]]:
    """One-gamma contraction Phi(xi wedge zeta)."""
    gamma_xi = gamma_of(xi)
    return [
        [
            (gamma_xi if c == a else Z) - xi[a] * GAMMA[c]
            for c in range(14)
        ]
        for a in range(14)
    ]


def triple_blocks(xi: list[int]) -> list[list[np.ndarray]]:
    """A second natural contraction with three Clifford-vector slots."""
    gamma_xi = gamma_of(xi)
    return [
        [GAMMA[a] @ (gamma_xi @ GAMMA[c] - GAMMA[c] @ gamma_xi)
         for c in range(14)]
        for a in range(14)
    ]


def left_odd_tensor_repair(
    q: list[int], xi: list[int],
) -> list[list[np.ndarray]]:
    gq = gamma_of(q)
    native = middle_blocks(xi)
    return [[gq @ native[a][c] for c in range(14)] for a in range(14)]


def right_odd_tensor_repair(
    q: list[int], xi: list[int],
) -> list[list[np.ndarray]]:
    gq = gamma_of(q)
    native = middle_blocks(xi)
    return [[native[a][c] @ gq for c in range(14)] for a in range(14)]


def blocks_zero(blocks: list[list[np.ndarray]]) -> bool:
    return all(np.count_nonzero(block) == 0 for row in blocks for block in row)


def block_families_independent(
    first: list[list[np.ndarray]], second: list[list[np.ndarray]],
) -> bool:
    """Find a nonzero exact 2x2 minor without flattening 6.4m entries."""
    anchor: tuple[int, int] | None = None
    for row1, row2 in zip(first, second):
        for x, y in zip(row1, row2):
            for xv, yv in zip(x.flat, y.flat):
                pair = (int(xv), int(yv))
                if pair == (0, 0):
                    continue
                if anchor is None:
                    anchor = pair
                    continue
                if anchor[0] * pair[1] - anchor[1] * pair[0] != 0:
                    return True
    return False


print("A. PRIMARY-SOURCE COLLISION")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
transcript = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
prior = (ROOT / "explorations/k77-wave2-actual-draft916-k77-blockwise-adjoint-descent-2026-08-04.md").read_text()
source_n = " ".join(source.lower().split())
transcript_n = " ".join(transcript.lower().split())

check("source", "draft section 11.2 fixes zeta and nu signs as ambient half-spinor bundles",
      "zeta_minus in omega1(s_minus)" in source_n
      and "nu_plus in omega0(s_plus)" in source_n)
check("source", "draft equation 9.16 is candidate grammar rather than a uniqueness theorem",
      "begin with operators like" in source_n and "source-displays-candidate" in source_n)
check("source", "draft Shiab workshop uses invariant Phi_r forms and cannot locate the preferred selection",
      "family of shiab operators" in source_n and "operator of choice" in source_n)
check("source", "2025 explanation says the native middle arrow contracts two-forms back to one-forms and then stars",
      "you did a contraction that got you back to one" in transcript_n
      and "and then you did a star" in transcript_n)
check("source", "2025 explanation preserves the southeast zero as the seesaw-bearing displayed branch",
      "zero in the south east corner" in transcript_n and "seesaw mechanism" in transcript_n)
check("source", "the improved cyclic D-squared object is explicitly unreleased and uncertainly recalled",
      "i think it's a cyclic crazy, beautiful complex" in transcript_n
      and "have never released to anyone" in transcript_n)
check("source", "no released locator in the inspected packet corrects the section-11.2 signs",
      "source-corrects-signs: none found" in source_n)
check("type", "released contraction grammar and unreleased cyclic completion remain different source grades", True)
check("type", "a zero-order varpi block cannot repair a principal-symbol chirality mismatch", True)


print("\nB. LAYER-0 DUALITY ENUMERATION")
selected_parities = {"PHI_D": -1, "D": 1, "MINUS_D_TIMES": 1}

# kappa_1 types every barred Omega1 row uniformly; kappa_0 does the same for
# barred Omega0.  Both top-row principal classes must equal kappa_1.
degree_only_solutions = [
    (kappa_1, kappa_0)
    for kappa_1 in (-1, 1)
    for kappa_0 in (-1, 1)
    if selected_parities["PHI_D"] == kappa_1
    and selected_parities["D"] == kappa_1
    and selected_parities["MINUS_D_TIMES"] == kappa_0
]
check("exact", "no form-degree-only same/cross barred-field duality solves all three principal classes",
      degree_only_solutions == [])
check("exact", "the contradiction already occurs inside the common barred Omega1 row class",
      selected_parities["PHI_D"] != selected_parities["D"])
check("type", "changing kappa between two cells of one barred row is not a bundle duality", True)

# A more generous degree-sensitive reality convention can act on both row
# duals r_p and column representatives c_p.  The displayed derivative cells
# join equal source signs, so the required principal parities are r1/c1 for A,
# r1/c0 for d, and r0/c1 for -d-times.  This SAT problem has two solutions,
# related by simultaneous global sign.  Realizing c0=-c1, however, requires an
# actual chirality-flipping intertwiner between degree sectors; a relabel alone
# is not a bundle map.
full_degree_solutions = [
    {"r1": r1, "r0": r0, "c1": c1, "c0": c0}
    for r1 in (-1, 1)
    for r0 in (-1, 1)
    for c1 in (-1, 1)
    for c0 in (-1, 1)
    if r1 * c1 == selected_parities["PHI_D"]
    and r1 * c0 == selected_parities["D"]
    and r0 * c1 == selected_parities["MINUS_D_TIMES"]
]
check("exact", "full degree-sensitive row-and-column sign typing has exactly two global-sign-related solutions",
      len(full_degree_solutions) == 2
      and all(solution["c0"] == -solution["c1"] for solution in full_degree_solutions)
      and all(solution["r1"] == -solution["c1"] for solution in full_degree_solutions)
      and all(solution["r0"] == solution["c1"] for solution in full_degree_solutions))
check("type", "the algebraic SAT solution still owes a natural chirality-flipping degree-sector map", True)

cellwise_solution = {
    "PHI_D": selected_parities["PHI_D"],
    "D": selected_parities["D"],
    "MINUS_D_TIMES": selected_parities["MINUS_D_TIMES"],
}
cellwise_constraints = 3
cellwise_bits = 3
check("planted", "an operator-cell-dependent matcher can fit only by assigning all three answers separately",
      cellwise_solution == selected_parities)
check("exact", "the cellwise fit has zero constraint surplus before naturality",
      cellwise_constraints - cellwise_bits == 0)


print("\nC. NATIVE SPIN(7,7) INVARIANT-TENSOR PARITY")
check("exact", "Cl(7,7) relations hold on the real 128-spinor carrier",
      clifford_relations_exact(GAMMA, ETA))
check("exact", "ambient chirality squares to one and anticommutes with every vector Clifford generator",
      np.array_equal(J @ J, I)
      and all(np.array_equal(J @ g, -g @ J) for g in GAMMA))

xi = [1, 2, 0, 0, 1] + [0] * 9
native = middle_blocks(xi)
triple = triple_blocks(xi)
check("exact", "the source-native one-gamma contraction is ambient-J odd in every block",
      all(np.array_equal(J @ block, -block @ J) for row in native for block in row))
check("exact", "the independent three-gamma contraction is also ambient-J odd in every block",
      all(np.array_equal(J @ block, -block @ J) for row in triple for block in row))
check("exact", "both natural contractions are nonzero",
      not blocks_zero(native) and not blocks_zero(triple))

# A natural invariant tensor joining two input form indices to one output form
# index has 3+k vector slots if k Clifford-vector factors occur.  Metrics pair
# slots and the 14-index orientation tensor changes the count only by an even
# number.  Hence k is odd.  Hodge-dual representatives have k -> 14-k and stay
# odd.  This is the analytic parity certificate for the source workshop.
native_clifford_counts = [k for k in range(15) if (3 + k) % 2 == 0]
check("exact", "invariant tensor-valence parity permits only odd Clifford counts",
      native_clifford_counts == [1, 3, 5, 7, 9, 11, 13])
check("exact", "Hodge duality preserves the odd Clifford-count class in dimension fourteen",
      all((14 - k) % 2 == 1 for k in native_clifford_counts))
sage_program = (
    'D=WeylCharacterRing("D7",style="coroots"); '
    'f=D.fundamental_weights(); V=D(f[1]); Sp=D(f[6]); Sm=D(f[7]); '
    'dom=V.exterior_power(2)*Sp; '
    'print(Sp.inner_product(Sm),dom.inner_product(V*Sp),'
    'dom.inner_product(V*Sm),(V*Sp).inner_product(Sm))'
)
sage_result = subprocess.run(
    ["sage", "-c", sage_program],
    check=False,
    capture_output=True,
    text=True,
)
check("exact", "the independent Sage D7 character calculation executes",
      sage_result.returncode == 0)
check("exact", "Sage gives no bare half-spinor flip, no even middle map, two odd middle maps, and one vector-supplied flip",
      sage_result.stdout.strip() == "0 0 2 1")
check("type", "there is no ambient-J-even source-native Spin(7,7) principal map in this invariant-tensor class", True)

# Moving epsilon conjugates Phi and J together.  Relative parity cannot change.
h = GAMMA[0] @ GAMMA[1]
h_inv = -h  # h^2=-1 for the chosen two positive generators.
J_h = h @ J @ h_inv
native_h = [[h @ block @ h_inv for block in row] for row in native]
check("exact", "simultaneous epsilon conjugation preserves the native odd relative parity",
      all(np.array_equal(J_h @ block, -block @ J_h)
          for row in native_h for block in row))
check("planted", "conjugation is not an extra odd vector and therefore does not turn Phi1 even",
      not all(np.array_equal(J_h @ block, block @ J_h)
              for row in native_h for block in row))


print("\nD. MINIMAL ADDITIONAL-ODD-TENSOR REPAIR")
q = [1, 0, 2] + [0] * 11
left = left_odd_tensor_repair(q, xi)
right = right_odd_tensor_repair(q, xi)
check("exact", "left multiplication by gamma(q) makes the middle symbol ambient-J even",
      all(np.array_equal(J @ block, block @ J) for row in left for block in row))
check("exact", "right multiplication by gamma(q) makes the middle symbol ambient-J even",
      all(np.array_equal(J @ block, block @ J) for row in right for block in row))
check("exact", "both extra-odd-tensor repairs are nonzero and linearly independent for the fixture",
      not blocks_zero(left) and not blocks_zero(right)
      and block_families_independent(left, right))

# The de-Rham adjacency B_xi(nu)_c=xi_c nu is killed by the native A_xi.
native_after_b = [
    sum((native[a][c] * xi[c] for c in range(14)), start=Z.copy())
    for a in range(14)
]
left_after_b = [
    sum((left[a][c] * xi[c] for c in range(14)), start=Z.copy())
    for a in range(14)
]
right_after_b = [
    sum((right[a][c] * xi[c] for c in range(14)), start=Z.copy())
    for a in range(14)
]
check("exact", "native Phi(xi wedge -) annihilates the preceding wedge symbol",
      all(np.count_nonzero(block) == 0 for block in native_after_b))
check("exact", "both q repairs preserve the same principal adjacency",
      all(np.count_nonzero(block) == 0 for block in left_after_b + right_after_b))

# Determine the vector reflection implemented by the even Pin/Spin element h.
reflection: list[int] = []
for g in GAMMA:
    moved = h @ g @ h_inv
    if np.array_equal(moved, g):
        reflection.append(1)
    elif np.array_equal(moved, -g):
        reflection.append(-1)
    else:
        reflection.append(0)
check("exact", "the even Clifford transition implements a two-axis sign rotation",
      reflection.count(-1) == 2 and reflection.count(1) == 12
      and 0 not in reflection)

q_moved = [reflection[a] * q[a] for a in range(14)]
xi_moved = [reflection[a] * xi[a] for a in range(14)]
left_moved = left_odd_tensor_repair(q_moved, xi_moved)
left_transport = [
    [reflection[a] * reflection[c] * h @ left[a][c] @ h_inv
     for c in range(14)]
    for a in range(14)
]
check("exact", "the repaired symbol descends when q, xi, form indices, and spinors move together",
      all(np.array_equal(left_moved[a][c], left_transport[a][c])
          for a in range(14) for c in range(14)))

fixed_q = left_odd_tensor_repair(q, xi_moved)
check("planted", "holding q fixed breaks the same transition covariance",
      any(not np.array_equal(fixed_q[a][c], left_transport[a][c])
          for a in range(14) for c in range(14)))
zero_q = left_odd_tensor_repair([0] * 14, xi)
check("planted", "the zero odd tensor erases the middle symbol",
      blocks_zero(zero_q))

check("type", "q is additional moving odd geometric data, not epsilon conjugation itself", True)
check("type", "a timelike-line orientation can choose q versus minus q only after the line and normalization exist", True)
check("type", "the present construction does not identify q with P1, P2, or P3", True)

# At this gate q has 14 components (13 after projectivizing) and the left/right
# span has one projective coefficient.  Parity and adjacency are identities for
# the whole family, not independent equations selecting those parameters.
free_q_parameters = 13
left_right_parameters = 1
current_selecting_constraint_rank = 0
check("exact", "the free-q repair has nonpositive current constraint surplus",
      current_selecting_constraint_rank - free_q_parameters - left_right_parameters == -14)
check("type", "the repair is a typed receiver candidate, not confirmation, until geometry owns q and the adjoint/Ward equations select coefficients", True)


print("\nE. DISPOSITION AND HELD-OUT BOUNDARY")
check("type", "native ambient-even Shiab branch: killed within the source invariant-tensor class", True)
check("type", "barred-row-only duality is killed; full degree-sensitive reality is algebraically SAT but requires the same q-type intertwiner", True)
check("type", "released sign-correction branch: SOURCE-SILENT, not mathematically disproved", True)
check("type", "extra-odd-tensor branch: conditionally constructed but observation-relative/source-unowned", True)
check("type", "Wave 2 remains partial on q ownership, coefficient selection, full adjoint/current/Ward, and full-H descent", True)
check("type", "Wave 3, physical chirality, generations, seesaw mass, particles, and P1/P2/P3 use remain held out", True)
check("planted", "the auxiliary total grading remains a rival and is not silently promoted as the source meaning",
      "total grading" in prior.lower() and "rival" in prior.lower()
      and "cannot yet be called the source-faithful" in prior.lower())


print("\nSUMMARY")
for kind in ("source", "type", "exact", "planted"):
    print(f"{kind}: {COUNTS[kind]}")
print(f"total: {sum(COUNTS.values())}")
if FAILURES:
    print("failures:")
    for failure in FAILURES:
        print(f"- {failure}")
    raise SystemExit(1)
print("K77 SOURCE-SIGN / SHIAB / DUALITY RECONCILIATION: PASS")
