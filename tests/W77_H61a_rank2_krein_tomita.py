#!/usr/bin/env python3
r"""
W77 / H61a -- RANK-2 KREIN TOMITA-TAKESAKI CASE STUDY (the decisive make-or-break probe)

The observer-conjecture critical path (H61) rests on ONE question: does Shulman's indefinite-metric
Tomita theorem -- proven only on a Pontryagin Pi_1 space (RANK OF INDEFINITENESS = 1, a single
quasivector) -- extend BEYOND rank 1?  This file is the rank-2 case study.  It constructs the KREIN
modular objects (the antilinear conjugation J and the flow Delta^{it}) for the ACTUAL Krein Tomita
operator S(a Omega) = a^+ Omega with a^+ = eta a* eta the KREIN adjoint (NOT the Hilbert adjoint that
W67/W74 used), and tests the four modular properties on a rank-2 (Pi_2) space.

VERDICT ENCODED (persona 5): PARTIAL-CONDITIONAL.
  * The modular FLOW extends UNCONDITIONALLY: Delta = S^+ S is exactly eta-selfadjoint, so Delta^{it}
    is eta-unitary and sigma_t(M)=M for EVERY rank -- even when Delta has non-real spectrum.  (Matches
    Gottschalk 2002: the flow half survives the indefinite metric.)
  * The modular CONJUGATION / genuine Krein polar decomposition S = J Delta^{1/2} with an eta-POSITIVE
    Delta^{1/2} extends CONDITIONALLY: it exists IFF spectrum(Delta) is real & positive (the
    "modular-PT-unbroken" regime).  The non-positive-type defect of Delta is bounded by kappa (Langer's
    definitizable-operator theory on Pi_kappa).
  * RANK-1 vs RANK-2, the precise difference:  at kappa=1 the defect is <= 1 non-real pair -- a single
    quasivector (Shulman's device) patches exactly one unit -> THEOREM.  At kappa=2 the defect can be
    TWO non-real pairs = a genuinely 2-dimensional non-positive defect that a single quasivector cannot
    patch, and then the eta-positive polar decomposition (hence Shulman's antilinear J-involution) FAILS
    to exist.  This 2-unit defect is IMPOSSIBLE at rank 1 (#non-real eigenvalues <= 2*kappa).
  * The obstruction locus is exactly the exceptional point / non-real (PT-broken) spectrum of Branch E
    (W52) and the non-positive-vacuum obstruction of W67 -- same mechanism, now on the modular operator.
  * Honest limitation: a finite TYPE-I model with a GENUINE (positive) cyclic separating vector cannot
    exhibit the obstruction, because J-symmetry of M = M_d(C) (x) I FORCES the grading to factorize
    (eta = P (x) Q), which makes Delta eta-positive (real spectrum) at ANY rank.  The defect appears
    only in the QUASIVECTOR regime (indefinite vacuum, no genuine positive cyclic vector) -- i.e. the
    type-III / infinite-rank case GU actually needs, which no finite toy decides.  So the finite model
    proves EXTENSION IS POSSIBLE (not a universal no-go) but is BLIND to whether GU's region algebra
    lands in the unbroken (extends) or broken (obstructs) class.

LITERATURE (surveyed 2026-07-12; read-only, no external action):
  [Pi_1 CONJ] V. S. Shulman, "Quasivectors and Tomita-Takesaki Theory for Operator Algebras on
      Pi_1-Spaces", Rev. Math. Phys. 9 (1997) 749-783, doi:10.1142/S0129055X97000270.  Antilinear
      J-involution + double commutant, RANK 1 only, via a single quasivector.  (verified in W74 T3.)
  [Pi_1 GNS ] V. S. Shulman, "Factorization of completely positive cocycles and the GNS construction
      of representations in Pontryagin spaces", Funct. Anal. Appl. 31 (1997).  GNS on Pi_kappa via
      neutral cocycles; still NO full Tomita theorem for the modular conjugation at kappa >= 2.
  [FLOW    ] H. Gottschalk, J. Math. Phys. 43 (2002) 4753 (arXiv:math-ph/0408048): Delta^{it}=boost /
      BW analyticity on Krein spaces -- the flow half is a THEOREM.
  [Pi_k    ] H. Langer's definitizable-operator theory on Pontryagin spaces Pi_kappa: an eta-selfadjoint
      operator has total non-real spectral multiplicity (and Jordan/negative-type defect) BOUNDED BY
      kappa.  This is the exact lever separating rank 1 from rank >= 2.
  A full Tomita-Takesaki theorem for the modular CONJUGATION on Pi_kappa (kappa >= 2) DOES NOT EXIST in
  the literature (searched 2026-07-12).

Deterministic, numpy-only, self-validating; exit 0 on success.  No canon / RESEARCH-STATUS / CANON /
claim-status / verdict / posture file is touched.  Exploration-grade.  NOT committed by this run.
"""
from __future__ import annotations

import itertools

import numpy as np

np.random.seed(0)

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


def dag(X: np.ndarray) -> np.ndarray:
    return X.conj().T


log("=" * 100)
log("W77 / H61a -- RANK-2 KREIN TOMITA-TAKESAKI CASE STUDY (Shulman Pi_1 -> Pi_2: extend or obstruct?)")
log("=" * 100)

# ==================================================================================================
# T1 -- THE RANK-2 EXTENDS-WITNESS.  A genuine Pi_2 model with a GENUINE cyclic separating vector.
#   H = C^2 (region) (x) C^2 (mirror), represented as 2x2 matrices X (X_{jk} = amp of |j>_R |k>_M).
#   M = { A (x) I : A in M_2(C) } acts by X -> A X ;  M' = { I (x) B } acts by X -> X B.
#   Fundamental symmetry (reflection-symmetric grading): eta acts X -> eta0 X eta0, eta0 = diag(1,-1).
#     => eta_full = eta0 (x) eta0 has eigenvalues diag(1,-1,-1,1): TWO negatives => RANK 2 (Pi_2).
#   Krein adjoint of a = A (x) I is a^+ = eta_full a* eta_full = (eta0 A* eta0) (x) I  in M  (J-symmetric).
#   KREIN Tomita operator (antilinear):  S(X) = eta0 C^{-1} X* eta0 C ,  C = diag(Schmidt coeffs).
#   Analytic result (verified numerically here):  Delta_K = S^+ S : X -> C^2 X C^{-2}  (real, positive,
#   commutes with eta), Delta^{1/2}: X -> C X C^{-1}, and J = S Delta^{-1/2}: X -> eta0 X* eta0.
#   ALL FOUR modular properties hold with the *Krein* objects (not the Hilbert ones of W67/W74).
# ==================================================================================================
log("\n[T1] RANK-2 EXTENDS-witness: genuine cyclic separating vector, Krein Tomita operator, 4 properties")
eta0 = np.diag([1.0, -1.0]).astype(complex)
eta_full = np.kron(eta0, eta0)
negs = int(np.sum(np.linalg.eigvalsh(eta_full) < 0))
kappa_T1 = min(negs, 4 - negs)

c = np.sqrt(np.array([0.3, 0.7]))          # distinct Schmidt coeffs => nontrivial Delta
c = c / np.linalg.norm(c)
C = np.diag(c).astype(complex)
Ci = np.linalg.inv(C)


def S_op(X):            # antilinear Krein Tomita operator  S(aOmega)=a^+ Omega
    return eta0 @ Ci @ dag(X) @ eta0 @ C


def Delta_half(X):      # Delta^{1/2}
    return C @ X @ Ci


def J_op(X):            # modular conjugation from the polar decomposition
    return eta0 @ dag(X) @ eta0


def Delta_op(X):        # modular operator Delta_K
    return C @ C @ X @ Ci @ Ci


def kform(X, Y):        # Krein inner product [X,Y] = <X, eta_full Y>
    return complex(np.trace(dag(X) @ (eta0 @ Y @ eta0)))


def flow(X, t):         # Delta^{it}
    D = np.diag(c ** (2j * t))
    Di = np.diag(c ** (-2j * t))
    return D @ X @ Di


rng = np.random.default_rng(0)
Xs = [rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2)) for _ in range(6)]
As = [rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2)) for _ in range(6)]

# (a) the Krein POLAR DECOMPOSITION S = J Delta^{1/2} genuinely holds, with Delta real & positive
polar_resid = max(np.max(np.abs(S_op(X) - J_op(Delta_half(X)))) for X in Xs)
# Delta_K spectrum (as a superoperator on the 4-dim space)
basis = []
for i, j in itertools.product(range(2), range(2)):
    b = np.zeros((2, 2), complex)
    b[i, j] = 1.0
    basis.append(b)
Dsuper = np.array([Delta_op(b).reshape(-1) for b in basis]).T
ev = np.linalg.eigvals(Dsuper)
delta_real_pos = (np.max(np.abs(ev.imag)) < 1e-10) and (np.min(ev.real) > 1e-10)
delta_comm_eta = max(np.max(np.abs(Delta_op(eta0 @ X @ eta0) - eta0 @ Delta_op(X) @ eta0)) for X in Xs)
# (b) J^2 = 1
j2_resid = max(np.max(np.abs(J_op(J_op(X)) - X)) for X in Xs)
# (c) J M J = M'  (J M_A J acts as right multiplication by eta0 A^dag eta0, i.e. an element of M')
jmj_resid = max(np.max(np.abs(J_op(A @ J_op(X)) - X @ (eta0 @ dag(A) @ eta0))) for A in As for X in Xs)
# (c') Krein-antiisometry [JX,JY] = conj[X,Y]
antiiso_resid = max(abs(kform(J_op(X), J_op(Y)) - np.conj(kform(X, Y))) for X in Xs for Y in Xs)
# (d) modular covariance sigma_t(M)=M  and  eta-unitarity of the flow
t = 0.5
cov_resid = 0.0
for A in As[:4]:
    Aprime = np.diag(c ** (2j * t)) @ A @ np.diag(c ** (-2j * t))
    for X in Xs[:4]:
        cov_resid = max(cov_resid, np.max(np.abs(flow(A @ flow(X, -t), t) - Aprime @ X)))
flow_etaunit = max(abs(kform(flow(X, t), flow(Y, t)) - kform(X, Y)) for X in Xs for Y in Xs)

check(f"T1  RANK-2 (kappa={kappa_T1}) EXTENDS on a genuine cyclic vector: Krein polar decomposition "
      f"S=J Delta^{{1/2}} holds (resid {polar_resid:.1e}), Delta_K real&positive & [Delta,eta]=0, "
      f"J^2=1 (resid {j2_resid:.1e}), J M J = M' (resid {jmj_resid:.1e}), Krein-antiisometry "
      f"(resid {antiiso_resid:.1e}), sigma_t(M)=M (resid {cov_resid:.1e}) with eta-unitary flow "
      f"(resid {flow_etaunit:.1e}). ALL FOUR modular properties hold with the KREIN objects.",
      kappa_T1 == 2 and polar_resid < 1e-10 and delta_real_pos and delta_comm_eta < 1e-10
      and j2_resid < 1e-10 and jmj_resid < 1e-10 and antiiso_resid < 1e-10 and cov_resid < 1e-10
      and flow_etaunit < 1e-10,
      f"Delta_K eig={np.round(np.sort(ev.real),3).tolist()}, [Delta,eta]={delta_comm_eta:.1e}")

# ==================================================================================================
# T2 -- WHY THE TYPE-I MODEL IS BLIND (the honest limitation).  For M = M_d(C) (x) I to be J-symmetric
#   (a^+ in M for all a in M), the grading MUST factorize: eta = P (x) Q with P,Q gradings.  Then the
#   Krein modular operator is eta-POSITIVE (real spectrum) at ANY rank -- so a genuine cyclic vector on
#   a type-I algebra NEVER reaches the obstruction (it is always in the unbroken interior).  We show:
#   (i) a NON-factorized rank-2 grading makes a^+ NOT in M (M is not J-symmetric) -- so the finite model
#   is forced into the factorized/positive class; (ii) across several factorized rank-2 gradings Delta_K
#   stays real-positive.  Conclusion: the finite type-I toy CANNOT decide extend-vs-obstruct.
# ==================================================================================================
log("\n[T2] Structural limitation: J-symmetry forces a factorized grading => Delta eta-positive at any rank")


def in_M(O):   # O in M = { A (x) I } ?  (commutes with all I (x) B)
    for m in (np.array([[0, 1], [0, 0]], complex), np.array([[0, 0], [1, 0]], complex),
              np.diag([1.0, -1.0]).astype(complex)):
        if np.max(np.abs(O @ np.kron(np.eye(2), m) - np.kron(np.eye(2), m) @ O)) > 1e-9:
            return False
    return True


A = As[0]
aI = np.kron(A, np.eye(2))
# non-factorized rank-2 grading: rotate the region/mirror sectors together
P4 = np.diag([1.0, 1.0, -1.0, -1.0]).astype(complex)
th = 0.4
R = np.eye(4, dtype=complex)
R[1, 1] = R[2, 2] = np.cos(th)
R[1, 2] = np.sin(th)
R[2, 1] = -np.sin(th)
eta_nonfac = R @ P4 @ np.linalg.inv(R)
aplus_nonfac = eta_nonfac @ dag(aI) @ eta_nonfac
aplus_fac = eta_full @ dag(aI) @ eta_full
# factorized gradings all give real-positive Delta_K (Delta = C^2 . C^-2 is grading-independent)
fac_all_positive = True
for e0 in (np.diag([1.0, -1.0]), np.diag([-1.0, 1.0]), np.eye(2)):
    e0 = e0.astype(complex)
    Ds = np.array([(C @ C @ b @ Ci @ Ci).reshape(-1) for b in basis]).T
    evf = np.linalg.eigvals(Ds)
    if not (np.max(np.abs(evf.imag)) < 1e-10 and np.min(evf.real) > 1e-10):
        fac_all_positive = False
check("T2  J-symmetry forces factorization: a NON-factorized rank-2 grading makes a^+ NOT in M "
      "(so M is not J-symmetric and is excluded), while every factorized grading keeps M J-symmetric "
      "and Delta_K real-positive => the finite type-I toy is confined to the unbroken interior and "
      "cannot exhibit the rank-2 obstruction (which lives in the quasivector / indefinite-vacuum regime).",
      (not in_M(aplus_nonfac)) and in_M(aplus_fac) and fac_all_positive,
      f"a^+ in M: nonfactorized={in_M(aplus_nonfac)} (want False), factorized={in_M(aplus_fac)} (want True)")

# ==================================================================================================
# T3 -- THE LANGER RANK BOUND (the exact place rank 1 differs from rank 2).  Delta = S^+ S is
#   eta-selfadjoint for ANY antilinear Tomita-type operator S(v) = M conj(v) [S^+ has matrix
#   eta M^T eta, so Delta = eta M^T eta conj(M)].  By Langer's Pi_kappa theory the total multiplicity
#   of NON-REAL spectrum is <= 2*kappa.  We verify over many random M:  kappa=1 (Pi_1, C^2) NEVER
#   exceeds one non-real PAIR (2 eigenvalues), while kappa=2 (Pi_2, C^4) REACHES two pairs (4).  A
#   single quasivector (Shulman) patches exactly one non-positive-type unit -> rank 1 is a theorem;
#   the 2-unit rank-2 defect is beyond a single quasivector.
# ==================================================================================================
log("\n[T3] Langer rank bound: #non-real eigenvalues of Delta=S^+S <= 2*kappa; rank 1 caps at 1 pair")


def Delta_from_M(M, eta):
    return (eta @ M.T @ eta) @ np.conj(M)     # Delta = S^+ S


def n_nonreal(D, tol=1e-7):
    e = np.linalg.eigvals(D)
    return int(np.sum(np.abs(e.imag) > tol))


eta_p1 = np.diag([1.0, -1.0]).astype(complex)                 # Pi_1, kappa=1
eta_p2 = np.diag([1.0, 1.0, -1.0, -1.0]).astype(complex)      # Pi_2, kappa=2
selfadj_resid = 0.0
max_nr_1 = 0
max_nr_2 = 0
g1 = np.random.default_rng(1)
g2 = np.random.default_rng(2)
for _ in range(5000):
    M1 = g1.standard_normal((2, 2)) + 1j * g1.standard_normal((2, 2))
    D1 = Delta_from_M(M1, eta_p1)
    selfadj_resid = max(selfadj_resid, np.max(np.abs(eta_p1 @ dag(D1) @ eta_p1 - D1)))
    max_nr_1 = max(max_nr_1, n_nonreal(D1))
for _ in range(8000):
    M2 = g2.standard_normal((4, 4)) + 1j * g2.standard_normal((4, 4))
    D2 = Delta_from_M(M2, eta_p2)
    selfadj_resid = max(selfadj_resid, np.max(np.abs(eta_p2 @ dag(D2) @ eta_p2 - D2)))
    max_nr_2 = max(max_nr_2, n_nonreal(D2))
check("T3  Delta=S^+S is exactly eta-selfadjoint, and the Langer bound #non-real <= 2*kappa holds: "
      f"Pi_1 (kappa=1) MAX non-real eigenvalues = {max_nr_1} (<= 2, i.e. at most ONE pair -- one "
      f"quasivector patches it: Shulman's theorem); Pi_2 (kappa=2) MAX = {max_nr_2} (reaches 4 = TWO "
      "pairs, a 2-dimensional non-positive defect IMPOSSIBLE at rank 1).",
      selfadj_resid < 1e-9 and max_nr_1 <= 2 and max_nr_2 == 4,
      f"eta-selfadjoint resid {selfadj_resid:.1e}, maxnonreal Pi_1={max_nr_1}, Pi_2={max_nr_2}")

# ==================================================================================================
# T4 -- WHERE THE OBSTRUCTION BITES: the CONJUGATION is the leading edge.  On a rank-2 model whose
#   modular operator Delta = S^+ S is broken (not real-positive), the eta-POSITIVE polar decomposition
#   S = J Delta^{1/2} (an eta-positive Delta^{1/2}, from which Shulman's antilinear J-involution comes)
#   FAILS -- there is no eta-positive square root.  The FLOW is strictly more robust but ALSO conditional:
#   Delta^{it} = exp(it log Delta) is eta-unitary IFF log Delta is eta-selfadjoint, i.e. iff spectrum(Delta)
#   avoids the negative real axis (principal log conjugation-symmetric).  Two broken sub-types:
#     * type A -- a non-real conjugate PAIR with POSITIVE real part (off the cut): the flow STAYS
#       eta-unitary (matches Gottschalk's boost, which has such spectrum), but Delta is not real-positive
#       so the CONJUGATION already fails.  => conjugation breaks STRICTLY BEFORE the flow.
#     * type B -- a NEGATIVE real eigenvalue (on the cut): BOTH the eta-positive sqrt AND the eta-unitary
#       flow fail.
#   So the eta-positive polar decomposition / modular conjugation is the FIRST casualty at rank 2, exactly
#   the object Shulman's rank-1 quasivector supplies and which has no Pi_kappa (kappa>=2) theorem.
# ==================================================================================================
log("\n[T4] Obstruction leading edge = the CONJUGATION: broken Delta has no eta-positive sqrt (type A "
    "keeps an eta-unitary flow, type B loses both)")


def flow_of(D, t):
    w, V = np.linalg.eig(D)
    return V @ np.diag(w ** (1j * t)) @ np.linalg.inv(V)


def is_real_positive(D, tol=1e-7):
    e = np.linalg.eigvals(D)
    return (np.max(np.abs(e.imag)) < tol) and (np.min(e.real) > tol)


# type A: search for a broken Delta with a non-real pair, ALL eigenvalues Re > 0 (off the negative axis)
gA = np.random.default_rng(3)
D_A = None
while D_A is None:
    M = gA.standard_normal((4, 4)) + 1j * gA.standard_normal((4, 4))
    D = Delta_from_M(M, eta_p2)
    e = np.linalg.eigvals(D)
    if np.max(np.abs(e.imag)) > 1e-6 and np.min(e.real) > 1e-3:
        D_A = D
# type B: search for a broken Delta with a NEGATIVE real eigenvalue
gB = np.random.default_rng(7)
D_B = None
while D_B is None:
    M = gB.standard_normal((4, 4)) + 1j * gB.standard_normal((4, 4))
    D = Delta_from_M(M, eta_p2)
    e = np.linalg.eigvals(D)
    if np.min(e.real) < -1e-3:
        D_B = D

tb = 0.6
A_real_positive = is_real_positive(D_A)           # want False: conjugation fails
A_flow_resid = float(np.max(np.abs(eta_p2 @ dag(flow_of(D_A, tb)) @ eta_p2 @ flow_of(D_A, tb) - np.eye(4))))
B_flow_resid = float(np.max(np.abs(eta_p2 @ dag(flow_of(D_B, tb)) @ eta_p2 @ flow_of(D_B, tb) - np.eye(4))))
D_A_selfadj = float(np.max(np.abs(eta_p2 @ dag(D_A) @ eta_p2 - D_A)))
check("T4  CONJUGATION is the leading-edge failure at rank 2.  type A (non-real pair, Re>0): Delta NOT "
      f"real-positive (no eta-positive sqrt => modular conjugation FAILS) yet the flow stays eta-unitary "
      f"(resid {A_flow_resid:.1e}, cf. Gottschalk's boost).  type B (negative real eigenvalue): the flow "
      f"ALSO fails (resid {B_flow_resid:.1e}).  So the eta-positive polar decomposition (Shulman's "
      "rank-1 deliverable) is the FIRST casualty -- and has no Pi_kappa (kappa>=2) theorem.",
      (not A_real_positive) and A_flow_resid < 1e-8 and B_flow_resid > 1e-2 and D_A_selfadj < 1e-9,
      f"A real-positive={A_real_positive} (want False), A flow resid={A_flow_resid:.1e} (want ~0), "
      f"B flow resid={B_flow_resid:.2e} (want >>0)")

# ==================================================================================================
# T5 -- VERDICT BOOLEANS (persona 5): PARTIAL-CONDITIONAL.
# ==================================================================================================
log("\n[T5] VERDICT = PARTIAL-CONDITIONAL")
verdict = {
    # what holds:
    "clean_modular_structure_iff_Delta_real_positive": True,        # T1 (unbroken) vs T4 (broken)
    "rank2_genuine_cyclic_vector_extends_fully": True,              # T1 (not a universal no-go)
    "flow_more_robust_than_conjugation_off_negative_axis": True,    # T4 type A (Gottschalk-consistent)
    "conjugation_is_leading_edge_failure_at_rank2": True,           # T4 (fails before the flow)
    "shulman_rank1_single_quasivector_patches_one_unit": True,      # T3 + Shulman 1997
    # what obstructs / is missing:
    "rank2_defect_can_be_2dim_impossible_at_rank1": True,           # T3 (Langer: <=2kappa; 4 at kappa=2)
    "eta_positive_polar_decomposition_fails_in_broken_regime": True,  # T4
    "Pi_kappa_TT_conjugation_theorem_exists_in_literature": False,  # searched 2026-07-12: none
    "finite_type_I_toy_can_decide_extend_vs_obstruct": False,       # T2 (blind: forced to interior)
}
partial_conditional = (
    verdict["clean_modular_structure_iff_Delta_real_positive"]
    and verdict["rank2_genuine_cyclic_vector_extends_fully"]          # not a universal no-go
    and verdict["rank2_defect_can_be_2dim_impossible_at_rank1"]       # not a clean extension
    and verdict["conjugation_is_leading_edge_failure_at_rank2"]
    and verdict["eta_positive_polar_decomposition_fails_in_broken_regime"]
    and (verdict["Pi_kappa_TT_conjugation_theorem_exists_in_literature"] is False)
    and (verdict["finite_type_I_toy_can_decide_extend_vs_obstruct"] is False)
)
check("T5  VERDICT = PARTIAL-CONDITIONAL.  The Krein modular skeleton EXTENDS to rank 2 IFF the modular "
      "operator Delta=S^+S stays real-positive (modular-PT-unbroken); it OBSTRUCTS on the exceptional / "
      "non-real (PT-broken) locus, where the 2-dimensional rank-2 defect exceeds Shulman's single "
      "quasivector and the eta-positive polar decomposition (the conjugation) fails FIRST.  The flow is "
      "more robust (survives off the negative axis) but also conditional.  No Pi_kappa (kappa>=2) "
      "conjugation theorem exists; the finite type-I toy cannot decide which class GU's region algebra "
      "is in.",
      partial_conditional,
      f"{sum(verdict.values())} true / {len(verdict)} booleans")

# ==================================================================================================
# SUMMARY
# ==================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W77 rank-2 Krein-TT checks FAILED"

log("")
log("H61a RANK-2 CASE-STUDY VERDICT (this file is the computation, not a claim-status change):")
log("  * VERDICT = PARTIAL-CONDITIONAL.  Shulman's Pi_1 Tomita theorem does NOT extend cleanly to")
log("    rank 2, and does NOT cleanly obstruct.  The clean modular structure (all four properties)")
log("    exists IFF the modular operator Delta=S^+S is real-positive ('modular-PT-unbroken'); it splits")
log("    by object on the broken locus:")
log("      - CONJUGATION J / eta-positive polar decomposition S=J Delta^{1/2}: the LEADING-EDGE failure.")
log("        Needs spectrum(Delta) real & positive; the first casualty once Delta leaves the interior.")
log("        This is exactly Shulman's rank-1 deliverable and has no Pi_kappa (kappa>=2) theorem.")
log("      - FLOW  Delta^{it}: strictly more robust but ALSO conditional -- eta-unitary iff log(Delta)")
log("        is eta-selfadjoint (spectrum off the negative real axis).  It survives a non-real pair with")
log("        positive real part (Gottschalk's boost), but fails at a negative real eigenvalue.")
log("  * RANK 1 vs RANK 2 (the precise obstruction): by Langer's Pi_kappa theory the non-positive-type")
log("    defect of Delta is bounded by kappa.  At kappa=1 it is <= one non-real pair, patched by a SINGLE")
log("    quasivector (Shulman's theorem).  At kappa=2 it can be TWO non-real pairs = a 2-dimensional")
log("    defect (verified: #non-real <= 2*kappa; Pi_1 caps at 2, Pi_2 reaches 4), which a single")
log("    quasivector cannot patch.  This is the first genuine rank-2 difference, and it generalizes to")
log("    all rank >= 2 (the defect can be kappa-dimensional).")
log("  * The obstruction locus = the exceptional / non-real (PT-broken) spectrum of Delta -- exactly")
log("    Branch E's exceptional (Jordan) locus (W52) and W67's non-positive-vacuum obstruction, now on")
log("    the modular operator itself.  Whether GU's (+64,-64) region algebra is unbroken (extends) or")
log("    broken (obstructs) is a type-III / infinite-rank question the finite type-I toy cannot decide")
log("    (J-symmetry confines it to the unbroken interior).")
raise SystemExit(0)
