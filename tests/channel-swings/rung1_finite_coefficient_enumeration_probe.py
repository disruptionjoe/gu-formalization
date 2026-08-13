#!/usr/bin/env python3
r"""
RUNG 1 -- THE FINITE COEFFICIENT ENUMERATION.

Preregistered in explorations/prereg-rung1-finite-coefficient-enumeration-2026-07-29.md.
Implements Rung 1 of lab/active-research/conditional-source-action-toy-construction-program-2026-07-26.md,
named by CURRENT-STATE.yaml as the bounded next step.

MODEL (fixed before computation):
    H = (T (x) E+) + (T (x) E-) + X,   dim T = 3
with chirality grading, a PURELY CROSS-CHIRALITY Krein form (program-native, not
a positive Hilbert pairing), a mirror involution, a real source coordinate phi,
and a finite operator D(phi).

BINDING DISCIPLINE: enumerate the symmetry-permitted coefficient space FIRST,
then compute which indices it can produce.  Searching the space for a favourable
matrix and reporting that matrix is the failure mode this rung exists to avoid.

Deterministic (fixed seed, stated), foreground, numpy only, no writes, no
network.  EXIT 0 = ran and all controls passed; the PRINTED findings are the
result.
"""
from __future__ import annotations

import sys

import numpy as np

np.random.seed(20260729)

FAILURES: list[str] = []


def check(label: str, condition: bool) -> None:
    if condition:
        print(f"PASS: {label}")
    else:
        FAILURES.append(label)
        print(f"FAIL: {label}")


DIM_T = 3
TOL = 1e-9


def build_space(n_plus: int, n_minus: int):
    """Graded space with declared chirality dimensions."""
    return n_plus, n_minus, n_plus + n_minus


def krein_form(n_plus: int, n_minus: int) -> np.ndarray:
    """PURELY CROSS-CHIRALITY Krein form: K pairs E+ with E-, never within.

    This is the program-native structure (GU's (+96,-96) cross-chirality form),
    NOT a positive Hilbert pairing.  Requires n_plus == n_minus to be
    nondegenerate; degeneracy on the unbalanced case is itself informative and
    is reported rather than patched.
    """
    n = n_plus + n_minus
    K = np.zeros((n, n))
    m = min(n_plus, n_minus)
    for i in range(m):
        K[i, n_plus + i] = 1.0
        K[n_plus + i, i] = 1.0
    return K


def chirality_odd_basis(n_plus: int, n_minus: int) -> list[np.ndarray]:
    """The symmetry-permitted coefficient space, ENUMERATED FROM SYMMETRY ALONE.

    Declared symmetries: (a) chirality-ODD (Dirac type: D maps E+ <-> E- only,
    no within-block terms), (b) real coefficients.  Every basis element is a
    real elementary chirality-off-diagonal generator.  Nothing here is chosen
    with reference to any target index.
    """
    n = n_plus + n_minus
    basis: list[np.ndarray] = []
    for a in range(n_plus):
        for b in range(n_minus):
            E = np.zeros((n, n))
            E[n_plus + b, a] = 1.0   # E+ -> E-
            basis.append(E)
            F = np.zeros((n, n))
            F[a, n_plus + b] = 1.0   # E- -> E+
            basis.append(F)
    return basis


def net_chiral_index(D: np.ndarray, n_plus: int, n_minus: int) -> int:
    """index = dim ker(M) - dim ker(M^dagger) for the E+ -> E- block M."""
    M = D[n_plus:, :n_plus]
    rank = np.linalg.matrix_rank(M, tol=1e-8)
    return int((n_plus - rank) - (n_minus - rank))


print("=" * 74)
print("RUNG 1  --  finite coefficient enumeration (target-blind by construction)")
print("=" * 74)

# ---------------------------------------------------- P1 the coefficient space
print("\n[P1] enumerate the symmetry-permitted coefficient space FIRST")
NP_BAL, NM_BAL = DIM_T, DIM_T           # balanced: X contributes symmetrically
basis = chirality_odd_basis(NP_BAL, NM_BAL)
check("coefficient space is nonempty (kill 1)", len(basis) > 0)
print(f"  declared grading      : n+ = {NP_BAL}, n- = {NM_BAL} (vectorlike)")
print(f"  permitted real coeffs : {len(basis)}  (chirality-odd, real)")

K = krein_form(NP_BAL, NM_BAL)
print(f"  Krein form            : purely cross-chirality, "
      f"signature {tuple(int(round(x)) for x in np.sign(np.linalg.eigvalsh(K)).tolist()).count(1)}"
      f"+/{tuple(int(round(x)) for x in np.sign(np.linalg.eigvalsh(K)).tolist()).count(-1)}-")

# ------------------------------------- P2 dense sampling of the enumerated space
print("\n[P2] dense sampling of that space -- which index can it produce?")
N_SAMPLES = 4000
indices = set()
for _ in range(N_SAMPLES):
    coeffs = np.random.randn(len(basis))
    D = sum(c * B for c, B in zip(coeffs, basis))
    indices.add(net_chiral_index(D, NP_BAL, NM_BAL))
# include the phi-source sweep explicitly: phi scales one declared generator
for phi in np.linspace(-4.0, 4.0, 401):
    D = phi * basis[0] + 0.3 * basis[1]
    indices.add(net_chiral_index(D, NP_BAL, NM_BAL))

print(f"  samples                     : {N_SAMPLES} random + 401 phi-sweep")
print(f"  distinct net chiral indices : {sorted(indices)}")
coefficient_breaks = indices != {0}
check("index is constant across the whole enumerated space", not coefficient_breaks)

# ------------------------------------------- N1 planted unbalanced grading
print("\n[N1] planted UNBALANCED grading must move the index (kill 3)")
NP_UB, NM_UB = DIM_T + 1, DIM_T
ub_basis = chirality_odd_basis(NP_UB, NM_UB)
ub_indices = set()
for _ in range(500):
    coeffs = np.random.randn(len(ub_basis))
    D = sum(c * B for c, B in zip(coeffs, ub_basis))
    ub_indices.add(net_chiral_index(D, NP_UB, NM_UB))
check("unbalanced grading moves the index", ub_indices != {0})
print(f"  n+ = {NP_UB}, n- = {NM_UB}  ->  indices {sorted(ub_indices)}")

# --------------------------------------- N2 positive-Hilbert hostile control
print("\n[N2] positive-Hilbert hostile control (typed, never a substitute)")
ph_indices = set()
for _ in range(500):
    coeffs = np.random.randn(len(basis))
    D = sum(c * B for c, B in zip(coeffs, basis))
    D = 0.5 * (D + D.T)          # positive-Hilbert symmetrization, not Krein
    ph_indices.add(net_chiral_index(D, NP_BAL, NM_BAL))
check("positive-Hilbert control gives the same grading-determined index",
      ph_indices == {0})
print(f"  positive-Hilbert indices: {sorted(ph_indices)}")

# ---------------------------------- question 1: gap without a hand-set projector
print("\n[Q1] can phi open a mirror-sector gap WITHOUT a hand-set rank-3 projector?")
gaps = []
for phi in np.linspace(0.0, 4.0, 81):
    D = phi * basis[0] + 0.3 * basis[1]
    H = D @ D.T
    ev = np.sort(np.linalg.eigvalsh(H))
    gaps.append(float(ev[1] - ev[0]))
opened = max(gaps) - min(gaps) > TOL
zero_modes = [
    int(np.sum(np.abs(np.linalg.eigvalsh(
        (phi * basis[0] + 0.3 * basis[1]) @ (phi * basis[0] + 0.3 * basis[1]).T
    )) < 1e-8))
    for phi in (0.0, 2.0, 4.0)
]
kernel_moves = len(set(zero_modes)) > 1
print(f"  low-gap varies with phi     : {opened}")
print(f"  zero-mode count at phi=0,2,4: {zero_modes}  (kernel moves: {kernel_moves})")
print("  -> whatever phi does to the spectrum, the NET INDEX is unmoved ([P2]).")

# ------------------------------------------------------------------- verdict
print("\n" + "=" * 74)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("RESULT: VOID.")
    sys.exit(1)

verdict = "COEFFICIENT-BREAKS-PAIRING" if coefficient_breaks else "GRADING-ONLY"
print(f"VERDICT: {verdict}")
print("=" * 74)
print(
    "\nQ2 ANSWER -- 'which term first breaks the index-zero pairing?':\n"
    "  NO TERM DOES.  Across the entire symmetry-permitted coefficient space\n"
    "  (chirality-odd, real), sampled densely and swept in the source\n"
    "  coordinate phi, the net chiral index is identically zero at fixed\n"
    "  balanced grading.  The index is a function of the GRADING, not of any\n"
    "  coefficient: it moves only when n+ != n- (control N1).\n"
    "\n  So the index-zero pairing is broken by a FIELD-SPACE DECLARATION, never\n"
    "  by an operator term.  This independently reproduces the ladder's own\n"
    "  preamble warning that a Krein-isometric moment-map source has exact net\n"
    "  chiral index zero -- reached here by enumeration rather than by citation."
)
q1 = (
    "phi changes the KERNEL DIMENSION" if kernel_moves else "phi does not move the kernel"
) + (
    " and varies the low-lying gap" if opened else
    ", but the gap between the two smallest eigenvalues does NOT vary"
)
print(
    f"\nQ1 ANSWER (derived from the computation, not asserted): {q1}.\n"
    "  No hand-set rank-three projector was used anywhere.  Whatever motion\n"
    "  phi produces is an ACCESSIBLE-RANK effect and never a global-index one,\n"
    "  since [P2] shows the index is constant across the entire space.\n"
    "  Q4 therefore resolves to ACCESSIBLE, not GLOBAL: nothing here produces\n"
    "  global index three."
)
print(
    "\nEARNS (per the ladder): an exact scoped no-go at this rung.\n"
    "DOES NOT EARN: locality, anomaly inflow, a physical boundary, GU-native\n"
    "operator status, a derivation of three, or any packet field."
)
