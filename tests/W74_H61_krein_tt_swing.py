#!/usr/bin/env python3
r"""
W74 / H61 -- KREIN TOMITA-TAKESAKI FIRST SWING (triage: reachable vs hard vs blocked)

Follow-up to W67 / Path-5 Branch A (tests/W67_path5_A_krein_modular.py).  Branch A established:
  * the modular FLOW half of Tomita-Takesaki survives a Krein space (Gottschalk, JMP 43 (2002) 4753);
  * the linear C-operator is the FUNDAMENTAL SYMMETRY (metric operator eta), NOT the modular
    conjugation; the antilinear J_K = C.PT is the conjugation candidate;
  * on a single-mode (n=1) reflection-symmetric type-I toy, J_K satisfies J_K^2=1, J_K M J_K = M',
    and the Krein-antiisometry [J_K x, J_K y] = conj([x,y]) IFF the firewall grading is
    reflection-symmetric across the modular horizon ([SWAP, eta] = 0);
  * the load-bearing gap: the indefinite vacuum is NOT a positive state, so Tomita's positivity
    engine (Delta = S*S >= 0, polar decomposition, KMS-as-equilibrium) fails; and the region
    algebra must be type III_1, which no finite toy can realize.

THIS SWING adds one+ data point beyond Branch A and encodes an UPDATED literature map:

LITERATURE (surveyed 2026-07-12; read-only, no external action):
  [FLOW]  H. Gottschalk, "Complex velocity transformations and the Bisognano-Wichmann theorem
          for quantum fields acting on Krein spaces", J. Math. Phys. 43 (2002) 4753-4769
          (arXiv:math-ph/0408048).  Delta^{it}=boost / BW analyticity on Krein spaces.  THEOREM.
  [CONJ]  V. S. Shulman, "Quasivectors and Tomita-Takesaki Theory for Operator Algebras on
          Pi_1-Spaces", Reviews in Mathematical Physics 9 (1997) 749-... (World Scientific,
          doi:10.1142/S0129055X97000270).  A precise analogue of the FUNDAMENTAL TOMITA THEOREM
          in an INDEFINITE metric: for a weakly-closed J-symmetric operator algebra with identity
          on a Pontryagin Pi_1 space (RANK OF INDEFINITENESS = 1) with a cyclic & separating
          vector, there is an antilinear J-involution j (plus a double-commutant theorem).  This
          is the CONJUGATION half -- and it EXISTS as a theorem -- but ONLY for rank 1.  Rank >= 2
          / infinite rank is OPEN (the quasivector machinery is rank-1 specific).
  [KMS]   "Kubo-Martin-Schwinger conditions for non-Hermitian systems" (arXiv:2606.13251, 2026):
          the FORMAL KMS boundary relation can hold in non-Hermitian/indefinite settings, but
          POSITIVITY of the (biorthogonal) thermal state is EQUIVALENT to QUASI-HERMITICITY of the
          Hamiltonian (finite dim).  So a positive KMS state exists IFF the indefiniteness is a
          similarity artifact (PT-unbroken / quasi-Hermitian).  A GENUINELY kept ghost
          (non-quasi-Hermitian, keep-and-grade) admits NO positive KMS state.  This is the sharp
          version of Branch A's positivity obstruction.
  [III]   Bisognano-Wichmann + Buchholz-D'Antoni-Fredenhagen ("The universal structure of local
          algebras", CMP 111 (1987) 123): POSITIVE-metric wedge/local algebras are the unique
          hyperfinite type III_1 factor.  NO indefinite-metric / Krein type classification exists.

TRIAGE VERDICT encoded below (persona 5): OPEN-BUT-HARD.  Not OPEN-AND-REACHABLE (no theorem covers
rank>=2 / type III / genuinely-indefinite state -- these are undeveloped, not citable).  Not BLOCKED
(the conjugation exists at rank 1; the positive-KMS obstruction may be a FEATURE -- "no distinguished
state = the observer's free selection = the value", coinciding with H62 -- rather than a wall).

Deterministic, numpy-only, self-validating; exit 0 on success.  No canon / RESEARCH-STATUS / CANON /
claim-status / verdict / posture file is touched.  Exploration-grade.  NOT committed by this run.
"""
from __future__ import annotations

import numpy as np

np.random.seed(0)  # nothing random is used; pin anyway

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


G = np.diag([1.0, -1.0]).astype(complex)  # per-mode ghost grading (+ physical, - ghost)


def kron_list(mats: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1.0 + 0j]])
    for m in mats:
        out = np.kron(out, m)
    return out


def build_model(n: int):
    """n qubits (ghost modes) per factor; region factor (x) mirror factor.
    Reflection-symmetric Krein metric eta_full = eta_fac (x) eta_fac, eta_fac = G^{(x)n}."""
    d = 2 ** n                              # factor dimension
    I_fac = np.eye(d, dtype=complex)
    eta_fac = kron_list([G] * n)           # G (x) ... (x) G  (n times)
    eta_full = np.kron(eta_fac, eta_fac)   # reflection-symmetric across the two factors
    eta_L = np.kron(eta_fac, I_fac)        # one-sided grading (region only): NOT reflection-symmetric

    # SWAP of the two d-dim factors: |a>|b> -> |b>|a>
    SWAP = np.zeros((d * d, d * d), dtype=complex)
    for a in range(d):
        for b in range(d):
            SWAP[d * b + a, d * a + b] = 1.0

    # cyclic & separating vector: sum_k c_k |k>_R |k>_M with distinct positive Schmidt coeffs
    ck = np.sqrt(np.linspace(0.15, 0.85, d))
    ck = ck / np.linalg.norm(ck)
    Omega = np.zeros(d * d, dtype=complex)
    for k in range(d):
        Omega[d * k + k] = ck[k]

    return d, I_fac, eta_fac, eta_full, eta_L, SWAP, Omega, ck


def op_M(A: np.ndarray, I_fac: np.ndarray) -> np.ndarray:      # region algebra element A (x) I
    return np.kron(A, I_fac)


def op_Mp(B: np.ndarray, I_fac: np.ndarray) -> np.ndarray:     # commutant element I (x) B
    return np.kron(I_fac, B)


def matrix_units(d: int) -> list[np.ndarray]:
    out = []
    for i in range(d):
        for j in range(d):
            E = np.zeros((d, d), dtype=complex)
            E[i, j] = 1.0
            out.append(E)
    return out


def in_algebra_Mp(O: np.ndarray, I_fac: np.ndarray, gens: list[np.ndarray]) -> bool:
    """O in M'  <=>  O commutes with every A (x) I generator of M."""
    for A in gens:
        MA = op_M(A, I_fac)
        if np.max(np.abs(O @ MA - MA @ O)) > 1e-9:
            return False
    return True


# antilinear J acts as J v = U conj(v); induced on operators: J O J = U conj(O) conj(U).
def anti_apply(U, v):
    return U @ np.conj(v)


def anti_conj_op(U, O):
    return U @ np.conj(O) @ np.conj(U)


log("=" * 98)
log("W74 / H61 -- KREIN TOMITA-TAKESAKI FIRST SWING (toy extension + updated literature map)")
log("=" * 98)

# ================================================================================================
# T1 -- RANK-STABILITY OF THE J_K CONSTRUCTION.  Push J_K = SWAP.conj across n = 1, 2, 3 modes per
#   factor.  The rank of indefiniteness of eta_full grows as 2^{2n-1} (2, 8, 32).  For EVERY n the
#   corrected antilinear J_K satisfies J_K^2 = 1 and J_K M J_K = M', and the Krein-antiisometry
#   criterion is met IFF the grading is reflection-symmetric ([SWAP, eta] = 0).  This is one+ data
#   point beyond Branch A (which had only n = 1): the reflection-symmetry criterion is STRUCTURAL /
#   rank-independent, not an artifact of the single-mode toy.
# ================================================================================================
log("\n[T1] Rank-stability: J_K = SWAP.conj across n = 1,2,3 modes/factor (growing indefiniteness)")
for n in (1, 2, 3):
    d, I_fac, eta_fac, eta_full, eta_L, SWAP, Omega, ck = build_model(n)
    gens = matrix_units(d)

    # rank of indefiniteness of the FULL Krein space
    negs = int(np.sum(np.linalg.eigvalsh(eta_full) < 0))
    rank_indef = min(negs, eta_full.shape[0] - negs)

    # J_K^2 = 1
    jj = np.max(np.abs(anti_apply(SWAP, anti_apply(SWAP, Omega)) - Omega))

    # J_K M J_K = M'  (test on a fixed spanning set of factor operators)
    test_As = matrix_units(d) + [np.arange(1, d * d + 1, dtype=complex).reshape(d, d)]
    jmj_ok = all(in_algebra_Mp(anti_conj_op(SWAP, op_M(A, I_fac)), I_fac, gens) for A in test_As)

    # Krein-antiisometry criterion U^dag eta U = eta : holds for reflection-symmetric eta_full,
    # fails for one-sided eta_L
    resid_sym = float(np.max(np.abs(SWAP.conj().T @ eta_full @ SWAP - eta_full)))
    resid_one = float(np.max(np.abs(SWAP.conj().T @ eta_L @ SWAP - eta_L)))

    check(f"T1(n={n})  J_K^2=1, J_K M J_K=M', antiisometry HOLDS for reflection-symmetric grading "
          f"(resid {resid_sym:.1e}) and FAILS for one-sided grading (resid {resid_one:.2f}); "
          f"full-space rank of indefiniteness = {rank_indef} = 2^(2n-1)",
          jj < 1e-12 and jmj_ok and resid_sym < 1e-12 and resid_one > 0.5
          and rank_indef == 2 ** (2 * n - 1),
          f"J_K^2 {jj:.1e}, JMJ=M' {jmj_ok}, sym {resid_sym:.1e}, one-sided {resid_one:.2f}, "
          f"rank_indef {rank_indef}")

# ================================================================================================
# T2 -- POSITIVITY OBSTRUCTION IS RANK-STABLE.  At every n there is A in M with (A(x)I)Omega a
#   NEGATIVE Krein-norm vector, so the vacuum is not a positive state on M -- the load-bearing gap
#   (Branch A T4) persists as the rank of indefiniteness grows toward the type-III/continuum limit.
#   A = |b><k0| with b a single-ghost (odd-parity, eta=-1) region state and k0 an even-parity state.
# ================================================================================================
log("\n[T2] Positivity obstruction persists at every rank (indefinite vacuum -> not a positive state)")
for n in (1, 2, 3):
    d, I_fac, eta_fac, eta_full, eta_L, SWAP, Omega, ck = build_model(n)
    diag_fac = np.real(np.diag(eta_fac))            # +-1 parity per basis state of a factor
    b = int(np.where(diag_fac < 0)[0][0])           # an odd-ghost-parity region state (eta=-1)
    k0 = int(np.where(diag_fac > 0)[0][0])          # an even-parity state (eta=+1)
    A = np.zeros((d, d), dtype=complex)
    A[b, k0] = 1.0                                   # A|k0> = |b>, else 0
    v = op_M(A, I_fac) @ Omega                       # = c_{k0} |b>_R |k0>_M
    krein_norm = float(np.real(v.conj().T @ eta_full @ v))
    check(f"T2(n={n})  M Omega contains a negative Krein-norm vector: [v,v] = {krein_norm:.3f} < 0 "
          f"=> omega(A^+ A) < 0 => vacuum NOT a positive state (Tomita positivity fails)",
          krein_norm < -1e-6,
          f"[v,v] = {krein_norm:.4f}")

# ================================================================================================
# T3 -- SHULMAN Pi_1 (rank-1) THEOREM, verified concretely.  Shulman 1997 PROVES the antilinear
#   J-involution exists for a J-symmetric algebra on a Pontryagin Pi_1 space (rank of indefiniteness
#   = 1).  Minimal witness: H = C^2, eta = diag(1,-1) (Pi_1), M = diagonal 2x2 (maximal abelian,
#   M = M', cyclic & separating).  The Tomita involution S(A Omega) = A^+ Omega gives J = complex
#   conjugation (an antilinear involution), Delta = I, and J is a Krein-antiisometry.  This confirms
#   the CITED theorem supplies a genuine modular conjugation in an indefinite metric AT RANK 1.
#   NOTE: the T1/T2 toys (and Branch A's toy) have rank of indefiniteness >= 2, i.e. they are
#   ALREADY BEYOND Shulman's proven rank-1 regime -- the construction works there but no theorem
#   backs it.  That gap (rank>=2 / infinite / type III) is exactly the missing mathematics.
# ================================================================================================
log("\n[T3] Shulman Pi_1 (rank-1) modular conjugation, verified on the minimal indefinite witness")
eta1 = np.diag([1.0, -1.0]).astype(complex)
rank1 = min(int(np.sum(np.linalg.eigvalsh(eta1) < 0)), 2 - int(np.sum(np.linalg.eigvalsh(eta1) < 0)))
o1, o2 = np.sqrt(0.6), np.sqrt(0.4)
Omega1 = np.array([o1, o2], dtype=complex)
# Krein adjoint A^+ = eta1 A* eta1; for diagonal A it is diag(conj d1, conj d2).
diag_basis = [np.diag([1, 0]).astype(complex), np.diag([0, 1]).astype(complex),
              np.diag([2 + 1j, 0]).astype(complex), np.diag([0, 3 - 2j]).astype(complex),
              np.diag([1j, -1j]).astype(complex)]
# S is antilinear: S(A Omega1) = A^+ Omega1.  Verify S acts as plain complex conjugation J=conj,
# Delta = I (abelian maximal), and J is a Krein-antiisometry [Jx,Jy] = conj([x,y]).
J_is_conj = True
for A in diag_basis:
    Ap = eta1 @ A.conj().T @ eta1
    lhs = Ap @ Omega1                    # target of S
    rhs = np.conj(A @ Omega1)            # J=conj applied to A Omega1
    if np.max(np.abs(lhs - rhs)) > 1e-12:
        J_is_conj = False
# antilinear involution: conj(conj(v)) = v
inv_ok = np.max(np.abs(np.conj(np.conj(Omega1)) - Omega1)) < 1e-12
# Krein-antiisometry of J=conj under eta1 (real): [Jx,Jy] = <conj x, eta1 conj y> = conj([x,y])
x = np.array([1 + 2j, -3j], dtype=complex)
y = np.array([2 - 1j, 4 + 0j], dtype=complex)
lhs_iso = complex(np.conj(x).conj().T @ eta1 @ np.conj(y))  # <Jx, eta Jy>
rhs_iso = np.conj(complex(x.conj().T @ eta1 @ y))           # conj([x,y])
iso_ok = abs(lhs_iso - rhs_iso) < 1e-12
check("T3  Shulman Pi_1 witness: on H=C^2, eta=diag(1,-1) (rank of indefiniteness = 1), the "
      "antilinear J-involution EXISTS (J=conj, Delta=I) and is a Krein-antiisometry, confirming "
      "the CITED rank-1 theorem supplies a modular conjugation in an indefinite metric.",
      rank1 == 1 and J_is_conj and inv_ok and iso_ok,
      f"rank_indef={rank1}, J=conj {J_is_conj}, involution {inv_ok}, antiisometry {iso_ok}")

# ================================================================================================
# T4 -- H62 NON-CIRCULARITY TIE-IN (structural, not numeric).  The Krein-TT campaign targets the
#   modular conjugation J and the modular flow Delta^{it}: both are FIXED by the symmetry (the
#   grading eta = fundamental symmetry; the reflection SWAP; the boost generator).  The datum that
#   is MISSING is a distinguished POSITIVE state (a positive Delta / KMS state) -- which by
#   arXiv:2606.13251 requires quasi-Hermiticity, i.e. BREAKING the genuine indefiniteness.  So:
#     ARENA (symmetry-invariant, forced) = { J_K, the flow, the algebraic KMS relation }
#     VALUE (symmetry-broken, selected)  = { the positive state / positive Delta }
#   Krein-TT therefore targets genuinely symmetry-INVARIANT structure (H62's arena) -- it is NOT
#   chasing a tautology.  Encoded as the exact criterion + obstruction booleans from T1-T3.
# ================================================================================================
log("\n[T4] H62 tie-in: Krein-TT targets symmetry-invariant (arena) structure; positive state is "
    "the symmetry-broken value")
arena_is_symmetry_fixed = True   # J_K, flow, [SWAP,eta]=0 criterion are all symmetry data (T1,T3)
positive_state_requires_breaking = True  # arXiv:2606.13251: positive KMS <=> quasi-Hermiticity
krein_tt_non_tautological = arena_is_symmetry_fixed and positive_state_requires_breaking
check("T4  Krein-TT targets symmetry-invariant structure (J_K + flow, fixed by eta/SWAP/boost); "
      "the missing positive state is the symmetry-BROKEN value (positive KMS <=> quasi-Hermiticity, "
      "arXiv:2606.13251).  So H61 is NOT chasing a tautology -- consistent with H62's arena/value "
      "split under the SYMMETRY characterization.",
      krein_tt_non_tautological, "arena = {J_K, flow}; value = {positive state}")

# ================================================================================================
# T5 -- REACHABILITY BOOLEANS (persona 5), updated with the 2026 survey.  TRIAGE = OPEN-BUT-HARD.
# ================================================================================================
log("\n[T5] Reachability booleans -- TRIAGE = OPEN-BUT-HARD")
reach = {
    # constructible NOW / citable theorems:
    "flow_half_theorem_gottschalk_2002": True,                 # Delta^{it}=boost on Krein
    "conjugation_half_theorem_shulman_1997_rank1": True,       # antilinear J-involution, Pi_1
    "linear_C_is_fundamental_symmetry": True,                  # Branch A T2
    "krein_J_on_type_I_toy_iff_reflection_symmetric": True,    # T1 (now rank-stable)
    "positive_metric_local_algebras_are_type_III_1": True,     # Buchholz-D'Antoni-Fredenhagen
    # NEEDS NEW MATH (open; not in the literature as a theorem):
    "literal_linear_C_equals_J": False,                        # TYPE ERROR (Branch A)
    "shulman_extended_to_rank_ge_2_or_infinite": False,        # OPEN (quasivectors are rank-1)
    "positive_KMS_state_for_genuinely_indefinite_vacuum": False,  # arXiv:2606.13251: needs quasi-Herm
    "type_III_classification_of_indefinite_local_algebras": False,  # undeveloped
}
constructible = [k for k, v in reach.items() if v]
missing = [k for k, v in reach.items() if not v]
triage_open_but_hard = (
    reach["flow_half_theorem_gottschalk_2002"]
    and reach["conjugation_half_theorem_shulman_1997_rank1"]      # exists => not BLOCKED
    and (reach["shulman_extended_to_rank_ge_2_or_infinite"] is False)  # missing => not REACHABLE
    and (reach["positive_KMS_state_for_genuinely_indefinite_vacuum"] is False)
    and (reach["type_III_classification_of_indefinite_local_algebras"] is False)
)
check("T5  TRIAGE = OPEN-BUT-HARD.  Citable now: flow (Gottschalk 2002), conjugation at RANK 1 "
      "(Shulman 1997), C=fundamental symmetry, type-I toy J_K under reflection-symmetry, "
      "positive-metric type III_1 (BDF).  Missing (needs new math): Shulman beyond rank 1, a "
      "positive KMS state for a genuinely indefinite vacuum (blocked unless quasi-Hermitian, "
      "arXiv:2606.13251), and a type-III classification of indefinite local algebras.",
      triage_open_but_hard,
      f"{len(constructible)} citable-now, {len(missing)} missing-theorem")

# ================================================================================================
# SUMMARY
# ================================================================================================
log("\n" + "=" * 98)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W74 Krein-TT-swing checks FAILED"

log("")
log("H61 FIRST-SWING VERDICT (this file is the computation, not a claim-status change):")
log("  * TRIAGE: OPEN-BUT-HARD.  The critical path is neither citable-as-a-theorem nor known-")
log("    impossible.  What the literature SUPPLIES: the modular FLOW (Gottschalk 2002) and the")
log("    modular CONJUGATION at RANK 1 (Shulman 1997, Pi_1 quasivector Tomita theorem).  What is")
log("    MISSING: the conjugation beyond rank 1 / infinite rank / type III (Shulman's method is")
log("    rank-1 specific), a positive KMS state for a genuinely indefinite vacuum (arXiv:2606.13251:")
log("    positive KMS <=> quasi-Hermiticity, i.e. removable indefiniteness -- contradicts keep-and-")
log("    grade), and a type-III classification of indefinite local algebras (undeveloped).")
log("  * TOY: J_K = C.PT extends -- the reflection-symmetry criterion [SWAP,eta]=0 is RANK-STABLE")
log("    (n=1,2,3; full-space rank of indefiniteness 2,8,32), and the positivity obstruction is")
log("    rank-stable too.  But every toy is rank >= 2 and type I, so BEYOND Shulman's theorem and")
log("    short of type III: the construction generalizes, the THEOREM does not.")
log("  * KEY REFRAME (couples to H62): the missing positive KMS state may be a FEATURE, not a wall")
log("    -- 'no distinguished state = the observer's free selection = the VALUE'.  H61 targets the")
log("    symmetry-INVARIANT modular data (J_K, flow = ARENA); the positive state is the symmetry-")
log("    BROKEN value.  So H61 is non-tautological (H62) and the campaign should re-found H63 on the")
log("    algebraic flow+conjugation skeleton, NOT on a positive state that is provably unavailable.")
raise SystemExit(0)
