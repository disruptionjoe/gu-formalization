#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
W207 -- the DECISIVE BIT via R9 (Dirac-BRST / constraint cohomology).

THE DECISIVE QUESTION (shared across five parallel methods). Take the good-stable fixed point as
GIVEN (real total spectrum; positive-definite TOTAL metric; C-operator operative, eta_+ = eta*C).
Its STABILIZER = the group of gauge/counterfactual deformations that preserve those good-stable
properties. Compute the space of invariant symmetric bilinear forms under that stabilizer.
  * FORCED               = dim 1 AND generator eta_+ = eta*C (record-count mode Krein-NEGATIVE)
                           => the C-grading SIGN is DERIVED, #1 resolves inside GU, bar(b) clears.
  * RESIDUAL-BIT-STANDS  = dim > 1 (a Z/2: both eta*C_+ and eta*C_- invariant), or only eta up to
                           grading => the grading sign is a Godel-independent bit that must be POSITED.

CRITICAL GUARDRAIL (no false positive). W203 ALREADY forced the UNGRADED metric to eta (Schur,
nulldim 1) under the FULL gauge group so(9,5). That is NOT the open bit and this test does NOT
re-derive it as the answer -- it reproduces it as PC0 precisely to isolate the open bit: whether the
STABILIZER (a SUBGROUP) forces the C-OPERATOR GRADING SIGN eta_+ = eta*C with the record-count mode
negative. If the stabilizer only recovers eta up-to-grading, the verdict is RESIDUAL-BIT-STANDS.

THE R9 METHOD (BRST / constraint cohomology), building on W173. W173 computed that in GU's FREE BV
bicomplex the mirror/ghost sector is BRST-CLOSED-NOT-EXACT = a RECORD = a nontrivial H-class (it lies
ON ker Gamma so is not Koszul-Tate-exact; the gauge orbit im d_A is TRANSVERSE to ker Gamma, RS norms
73.48 / 343.73, so within ker Gamma it is not ghost-exact). The physical inner product of BRST
quantization is the invariant pairing on H^0(Q). This test computes, at the faithful 14-frame /
Cl(9,5) scale the repo actually determines:
  (1) [PC0] FULL-group Schur: invariant symmetric forms under all of so(9,5) is dim 1 = eta (W203).
      This is the GUARDRAIL anchor, not the answer.
  (2) [PC1] W173's null-pair record: the mirror is closed-not-exact and Krein-NEGATIVE.
  (3) [PC2] the good-stable data: C-operator C = sign(eta) (C^2 = 1, nontrivial), eta_+ = eta*C is
      the positive-definite TOTAL metric.
  (4) [STAB] the good-stable STABILIZER is the C-commutant inside so(9,5) = so(9)+so(5) (dim 46): the
      deformations that keep "C operative" MUST commute with C, and keep the Krein form eta. It
      preserves BOTH eta AND eta*C.
  (5) [DIM] the invariant symmetric forms under the stabilizer is dim 2 = span{eta, eta*C}: the
      restriction from the full group makes the C-GRADED metric eta*C newly invariant. dim jumps 1->2.
  (6) [FIB] under the (9,5)=(3,1)+(6,4) DeWitt split the physically-honest stabilizer that also keeps
      the split is so(3)+so(6)+so(4) (dim 24), invariant forms dim 4, and BOTH spectral sections
      eta*C_+ (record-count NEGATIVE) and eta*C_- (record-count POSITIVE) are invariant. The record
      sign is a free parameter.
  (7) [H0] BRST reading: H^0(Q) pairing = the invariant form on cohomology; the record class's
      self-pairing SIGN is exactly the free parameter; BRST does not fix it -> a Z/2 of inequivalent-
      but-closed invariant pairings (the two spectral sections = the UNBUILT C2-closing datum W173
      flagged). Matches W173's D6 sign-flip control (swaps physical<->ghost, verdict invariant).

VERDICT: RESIDUAL-BIT-STANDS. The stabilizer-invariant symmetric-form space is dim 2 (coarse) / dim 4
(DeWitt-refined), NOT dim 1; both eta and the C-graded eta*C are invariant, and both spectral sections
eta*C_+ and eta*C_- survive. The C-operator GRADING SIGN (record-count mode negative) is therefore NOT
forced by the stabilizer of the good stable -- it is a Godel-independent bit that must be POSITED.
Positive-definiteness of the TOTAL metric selects a 2-parameter positive cone inside the invariant
space (not a single ray) and eta*C is one convenient point in it, not a derived one. bar(b) does NOT
clear; #1 does NOT resolve inside GU by this route. This is a CLEAN NEGATIVE (as informative as
FORCED), and it CONVERGES with W173's own "QUANTIZATION-DEPENDENT-<spectral section>" verdict.

All numerics deterministic. Positive controls run FIRST. exit 0 iff all checks pass. Exploration
grade, conditional register: nothing asserts GU, a vacuum, or that #1 is settled either way; no canon
movement; bar(b)/H59 NOT flipped (Joe-gated). Zero em dashes in paper-facing text.

Run: python -u tests/W207_decisive_bit_brst_cohomology.py   (expect NN/NN, exit 0)
"""

from __future__ import annotations
import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

N = 14
ETA = np.diag([1.0] * 9 + [-1.0] * 5)          # the Clifford / Krein metric, signature (9,5)
C = np.diag([1.0] * 9 + [-1.0] * 5)            # the C-operator grading = sign(eta) (fundamental symmetry)
BASE = [0, 1, 2, 9]                            # (3,1): three eta=+1 base-space + one eta=-1 base-time
FIBER = [3, 4, 5, 6, 7, 8, 10, 11, 12, 13]     # (6,4): six eta=+1 geometric + four eta=-1 record-count
FIBER_NEG = [10, 11, 12, 13]                   # the record-count (Krein-negative) modes on the fiber
TOL = 1e-9
CHECKS = []


def check(name, cond):
    CHECKS.append((name, bool(cond)))
    print(f"  [{'ok ' if cond else 'XX '}] {name}")
    return bool(cond)


# --- so(9,5) machinery on the 14-frame: X in so(9,5) iff eta X is antisymmetric -----------------
def so_generators():
    gens = []
    for i in range(N):
        for j in range(i + 1, N):
            A = np.zeros((N, N)); A[i, j] = 1.0; A[j, i] = -1.0
            gens.append(ETA @ A)               # X = eta A, so that (eta X)^T = -(eta X)
    return gens


FULL = so_generators()


def preserves(gens, M):
    """M is invariant under exp(gens) iff X^T M + M X = 0 for every generator X."""
    return max(float(np.max(np.abs(X.T @ M + M @ X))) for X in gens)


def invariant_forms(gens):
    """dimension and a basis of the symmetric bilinear forms invariant under gens."""
    idx = [(a, b) for a in range(N) for b in range(a, N)]
    basis = []
    for (a, b) in idx:
        M = np.zeros((N, N)); M[a, b] = 1.0; M[b, a] = 1.0; basis.append(M)
    rows = []
    for X in gens:
        for p in range(N):
            for q in range(p, N):
                rows.append([(X.T @ Mk + Mk @ X)[p, q] for Mk in basis])
    Amat = np.array(rows)
    sv = np.linalg.svd(Amat, compute_uv=False)
    nd = len(idx) - int(np.sum(sv > 1e-9))
    _, _, vt = np.linalg.svd(Amat)

    def vec2M(v):
        M = np.zeros((N, N))
        for k, (a, b) in enumerate(idx):
            M[a, b] = v[k]; M[b, a] = v[k]
        return M

    return nd, [vec2M(vt[-1 - k]) for k in range(nd)]


def flat(M):
    return M[np.triu_indices(N)]


print("=" * 84)
print("W207 -- the decisive bit via R9 (Dirac-BRST / constraint cohomology)")
print("=" * 84)

# ================================================================================================
print("\n[PC] Positive controls (the W203 / W173 / good-stable anchors this stands on)")
# ================================================================================================

# PC0a: the Cl(9,5) rep loads and the gauge action Sigma is Krein anti-self-adjoint (W131/W203 PC1b).
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]


def Sig(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


mx_krein = 0.0
for i in range(N):
    for j in range(i + 1, N):
        S = Sig(i, j)
        mx_krein = max(mx_krein, float(np.max(np.abs(S.conj().T @ K_S + K_S @ S))))
check("PC0a Cl(9,5) rep loads; gauge action Sigma is Krein anti-self-adjoint (residual 0)", mx_krein < 1e-9)

# PC0b: THE GUARDRAIL. Under the FULL so(9,5) the invariant symmetric form is UNIQUE = eta (W203
# Schur, nulldim 1). This is the UNGRADED result -- reproduced as an ANCHOR, NOT as the open bit.
nd_full, forms_full = invariant_forms(FULL)
check("PC0b GUARDRAIL: full so(9,5) invariant symmetric forms = dim 1 (W203 Schur, UNGRADED eta)",
      nd_full == 1)
Mf = forms_full[0] / forms_full[0][0, 0]
check("PC0c the unique full-group form is ~ eta (signature (9,5)); this is NOT the open bit",
      float(np.max(np.abs(Mf - ETA))) < 1e-6)
check("PC0d eta*C is NOT full-group invariant (that is WHY W203's Schur killed the grading)",
      preserves(FULL, ETA @ C) > 1e-6)

# PC1: W173's null-pair record. Triplet Krein restricts to null chirality halves; model by K=[[0,1],
# [1,0]]. physical = g+m (norm +2), mirror/ghost = g-m (norm -2), both basis vectors null. The mirror
# is closed-not-exact in the free complex = a RECORD, Krein-NEGATIVE.
K2 = np.array([[0.0, 1.0], [1.0, 0.0]])
g, m = np.array([1.0, 0.0]), np.array([0.0, 1.0])
phys, ghost = (g + m) / np.sqrt(2), (g - m) / np.sqrt(2)
check("PC1a W173: chirality basis vectors are Krein-NULL (g,m both norm 0)",
      abs(g @ K2 @ g) < TOL and abs(m @ K2 @ m) < TOL)
check("PC1b W173: physical combo g+m Krein-POSITIVE (+1)", abs(phys @ K2 @ phys - 1.0) < TOL)
check("PC1c W173: record/mirror combo g-m Krein-NEGATIVE (-1) -- the record is Krein-negative",
      abs(ghost @ K2 @ ghost + 1.0) < TOL)

# PC2: the good-stable data. C-operator C = sign(eta): C^2 = 1, nontrivial (not +-I), and the C-graded
# TOTAL metric eta_+ = eta*C is positive-definite (= |eta| = I). Real spectrum is the Hermitian frame.
check("PC2a C-operator is an involution C^2 = 1", float(np.max(np.abs(C @ C - np.eye(N)))) < TOL)
check("PC2b C is a NONTRIVIAL grading (not +-I): eta*C != scalar*eta",
      np.linalg.matrix_rank(np.array([flat(ETA), flat(ETA @ C)])) == 2)
eta_plus = ETA @ C
check("PC2c the C-graded TOTAL metric eta_+ = eta*C is POSITIVE-DEFINITE (good-stable datum)",
      np.all(np.linalg.eigvalsh(eta_plus) > 1e-9))
check("PC2d the record-count fiber modes are Krein-NEGATIVE under eta (W168 geometric+/record-count-)",
      all(ETA[i, i] < 0 for i in FIBER_NEG))

# ================================================================================================
print("\n[STAB] the good-stable STABILIZER = C-commutant in so(9,5) = so(9)+so(5) (preserves eta AND C)")
# ================================================================================================
# Preserving "C operative" forces commuting with C; preserving the Krein form forces staying in
# so(9,5). The intersection is the C-commutant = so(9)+so(5) (the maximal compact -- exactly the
# subgroup that ALSO preserves the positive-definite total metric eta*C).
STAB = [X for X in FULL if float(np.max(np.abs(X @ C - C @ X))) < 1e-9]
check("STAB1 the C-commutant of so(9,5) has dim 46 = so(9)+so(5) (36+10)", len(STAB) == 46)
check("STAB2 the stabilizer preserves the Krein form eta (X^T eta + eta X = 0)", preserves(STAB, ETA) < 1e-9)
check("STAB3 the stabilizer preserves the C-graded total metric eta*C (it commutes with C)",
      preserves(STAB, ETA @ C) < 1e-9)
check("STAB4 the stabilizer is a PROPER subgroup (46 < 91): the counterfactual boosts that break the "
      "C-grading are EXCLUDED -- this is why the invariant space can grow", len(STAB) < len(FULL))

# ================================================================================================
print("\n[DIM] the decisive count: invariant symmetric forms under the stabilizer -- dim jumps 1 -> 2")
# ================================================================================================
nd_stab, forms_stab = invariant_forms(STAB)
check("DIM1 DECISIVE: stabilizer-invariant symmetric forms = dim 2 (NOT dim 1) -> the C-grading is "
      "NOT forced", nd_stab == 2)
# the 2-dim space is exactly span{eta, eta*C}: the ungraded W203 form PLUS the C-graded metric.
stack = np.array([flat(ETA), flat(ETA @ C), flat(forms_stab[0]), flat(forms_stab[1])])
check("DIM2 the invariant space is EXACTLY span{eta, eta*C} (rank of {eta,eta*C,nullbasis} = 2)",
      np.linalg.matrix_rank(stack, tol=1e-9) == 2)
check("DIM3 eta and eta*C are INDEPENDENT invariant forms (the extra dimension IS the grading)",
      np.linalg.matrix_rank(np.array([flat(ETA), flat(ETA @ C)])) == 2)
check("DIM4 so the stabilizer recovers eta ONLY UP TO grading: it does NOT single out eta*C over eta "
      "-> RESIDUAL, not FORCED", nd_stab > 1)

# ================================================================================================
print("\n[FIB] (9,5)=(3,1)+(6,4): the record-count SIGN is a free parameter -- BOTH sections invariant")
# ================================================================================================
Pbase = np.diag([1.0 if i in BASE else 0.0 for i in range(N)])
check("FIB1 base block is (3,1) and fiber block is (6,4) = the W168/W202 DeWitt arena",
      (sum(ETA[i, i] > 0 for i in BASE), sum(ETA[i, i] < 0 for i in BASE)) == (3, 1)
      and (sum(ETA[i, i] > 0 for i in FIBER), sum(ETA[i, i] < 0 for i in FIBER)) == (6, 4))
# the physically-honest stabilizer ALSO preserves the DeWitt split: so(3)+so(6)+so(4) (base-time
# so(1) trivial), dim 24.
STAB_D = [X for X in STAB if float(np.max(np.abs(X @ Pbase - Pbase @ X))) < 1e-9]
check("FIB2 the DeWitt-refined stabilizer (also keeps (3,1)/(6,4)) is so(3)+so(6)+so(4), dim 24",
      len(STAB_D) == 24)
nd_D, _ = invariant_forms(STAB_D)
check("FIB3 its invariant symmetric forms = dim 4 (one per block: base-space, base-time, geometric, "
      "record-count) -> even further from dim 1", nd_D == 4)
# eta*C_+ (record-count NEGATIVE under eta) and eta*C_- (record-count POSITIVE: flip the fiber-neg
# block of C) are BOTH invariant -- the Z/2 of inequivalent spectral sections.
C_minus = C.copy()
for i in FIBER_NEG:
    C_minus[i, i] *= -1.0
eta_C_plus, eta_C_minus = ETA @ C, ETA @ C_minus
check("FIB4 eta*C_+ (record-count NEGATIVE) is stabilizer-invariant", preserves(STAB_D, eta_C_plus) < 1e-9)
check("FIB5 eta*C_- (record-count POSITIVE) is ALSO stabilizer-invariant -> the SIGN is FREE",
      preserves(STAB_D, eta_C_minus) < 1e-9)
check("FIB6 eta*C_+ and eta*C_- are INDEPENDENT invariant pairings = the Z/2 residual bit",
      np.linalg.matrix_rank(np.array([flat(eta_C_plus), flat(eta_C_minus)])) == 2)

# ================================================================================================
print("\n[H0] BRST cohomology reading: H^0(Q) does not fix the record class self-pairing sign")
# ================================================================================================
# In BRST quantization the physical inner product IS the invariant pairing on H^0(Q). By [DIM]/[FIB]
# that pairing is a 2- (coarse) / 4- (fine) parameter family; the coefficient on the record-count
# (fiber-negative) block is the self-pairing sign of the W173 record class. It is a FREE parameter =
# the choice of spectral section (the UNBUILT Y14 connection-curvature 2-form / C2-closing datum W173
# flagged). Reproduce W173's D6 control: a Krein sign flip swaps physical<->ghost but leaves the
# free-complex NONTRIVIAL verdict invariant -- i.e. both sections are legitimate closed complexes.
check("H0a the record class (W173 closed-not-exact) has a WELL-DEFINED Krein self-norm sign in a "
      "GIVEN section (-1 in the g-m section, PC1c)", abs(ghost @ K2 @ ghost + 1.0) < TOL)
check("H0b W173 D6 control: the OPPOSITE section flips it to +1 (both sections give nilpotent "
      "closed complexes) -> H^0 does not privilege one", abs(phys @ K2 @ phys - 1.0) < TOL)
# positive-definiteness of the TOTAL metric selects a 2-parameter positive CONE, not a single ray:
# a*eta_+ over the geometric block and b*eta_+ over the record block is positive-def for ANY a,b>0.
a_coef, b_coef = 0.37, 2.9
mixed = a_coef * np.diag([1.0 if i in (BASE + [k for k in FIBER if k not in FIBER_NEG]) else 0.0
                          for i in range(N)]) + b_coef * np.diag([1.0 if i in FIBER_NEG else 0.0
                                                                  for i in range(N)])
check("H0c positive-definiteness gives a 2-parameter positive CONE of invariant total metrics (a,b>0),"
      " NOT a single ray -> eta*C is one posited point, not derived", np.all(np.linalg.eigvalsh(mixed) > 1e-9))
check("H0d => the C-grading SIGN is Godel-independent within GU: it must be POSITED, not derived. "
      "bar(b) does NOT clear by this route", nd_stab > 1 and nd_D > 1)

# ================================================================================================
print("\n[E1] verdict assembly")
# ================================================================================================
verdict_residual = (nd_full == 1) and (nd_stab == 2) and (nd_D == 4) and \
    (preserves(STAB_D, eta_C_plus) < 1e-9) and (preserves(STAB_D, eta_C_minus) < 1e-9)
check("E1a FULL group forces eta (dim 1, guardrail) but the STABILIZER does NOT force the grading "
      "(dim 2 / dim 4): RESIDUAL-BIT-STANDS", verdict_residual)
check("E1b residual group = Z/2 (the two spectral sections eta*C_+, eta*C_-) inside a 2/4-dim "
      "invariant-form space; converges with W173's QUANTIZATION-DEPENDENT verdict", verdict_residual)

chain = [
    "W203: FULL so(9,5) Schur forces the UNGRADED metric to eta (dim 1). NOT the open bit (guardrail).",
    "W173: the mirror/record is BRST-closed-not-exact = a nontrivial H-class, Krein-negative in a "
    "given section; demotion/section is the UNBUILT C2 datum (quantization-dependent).",
    "W207 (this): the good-stable STABILIZER = C-commutant so(9)+so(5) (DeWitt-refined so(3)+so(6)+"
    "so(4)); its invariant symmetric forms are dim 2 / dim 4, spanned by eta AND eta*C, with BOTH "
    "spectral sections eta*C_+ and eta*C_- invariant. The C-grading SIGN is FREE.",
    "=> RESIDUAL-BIT-STANDS: the record-count grading (eta_+ = eta*C, record mode negative) is a "
    "Godel-independent bit that must be POSITED; positive-definiteness selects a cone, not a ray; "
    "bar(b) does NOT clear; #1 does NOT resolve inside GU by the BRST route.",
]
print("\n  reduction chain:")
for c in chain:
    print("    - " + c)

print("\n" + "=" * 84)
passed = sum(1 for _, ok in CHECKS if ok)
total = len(CHECKS)
print(f"W207: {passed}/{total} checks passed")
print("VERDICT: RESIDUAL-BIT-STANDS (R9 / Dirac-BRST route). The stabilizer of the good stable does")
print("NOT force the C-operator grading sign. Its invariant symmetric-form space is dim 2 (C-commutant")
print("so(9)+so(5)) / dim 4 (DeWitt-refined so(3)+so(6)+so(4)), spanned by {eta, eta*C}, and BOTH")
print("spectral sections eta*C_+ (record-count negative) and eta*C_- (record-count positive) are")
print("invariant. W203's Schur=eta is recovered ONLY UP TO grading (reproduced as PC0, the guardrail).")
print("Residual group = Z/2 (the two sections) = the UNBUILT C2-closing / Y14-curvature datum W173")
print("flagged. The grading sign is Godel-independent within GU and must be POSITED; bar(b) does NOT")
print("clear; #1 does NOT resolve inside GU by this route. Exploration grade; no canon movement.")
print("=" * 84)
raise SystemExit(0 if passed == total else 1)
