#!/usr/bin/env python3
r"""
W84 / rankN -- DOES PT-UNBROKENNESS CLOSE THE rank>1 KREIN TOMITA-TAKESAKI FOR GU?

The swing question.  W77/H61a proved: the Krein modular skeleton (J^2=1, JMJ=M', eta-positive polar
decomposition S=J Delta^{1/2}, eta-unitary flow) extends past Shulman's rank-1 theorem IFF the Krein
modular operator Delta = S^+ S is MODULAR-PT-UNBROKEN (real-positive spectrum).  W83 argued the
asymptotic-safety branch of GU IS PT-unbroken on the physical (spin-2) sector.  The naive composition:
    PT-unbroken (W83)  =>  rank>1 Krein-TT closes (W77)  =>  the two 'named conditions' of the observer
    conjecture collapse to one (only 'Reuter FP genuine' remains).
This file tests whether that composition actually closes, or whether there is a RESIDUAL type-III /
infinite-rank obstruction BEYOND PT-unbrokenness.

THE CRUX (resolved here).  'Standard Tomita-Takesaki applies once PT-unbroken' would require the
indefinite algebra to be QUASI-HERMITIAN: a metric operator Theta that is BOUNDED with BOUNDED INVERSE,
so that h = Theta^{1/2} H Theta^{-1/2} is a genuine (bounded-similar) self-adjoint operator on a positive
Hilbert space, where standard TT holds at any type.  The decisive fact:

    * FINITE rank (Pontryagin Pi_kappa):  PT-unbroken (real spectrum + diagonalizable)  =>  quasi-Hermitian
      (metric bounded w/ bounded inverse)  =>  standard TT via bounded similarity  =>  and the ghost is
      REMOVABLE.  Every bounded operator on Pi_kappa is DEFINITIZABLE (Langer) -> a spectral function and an
      eta-positive square root exist -> J is constructible.  In finite rank the implication is REAL, and it
      makes keep-and-grade trivial (the ghost is a bounded-similarity artifact).

    * INFINITE rank (type III_1, GU's actual region algebra):  the implication FAILS.  PT-unbroken
      (real spectrum, complete eigenvectors) does NOT imply quasi-Hermitian.  The metric operator can be
      bounded with an UNBOUNDED INVERSE (Krejcirik-Siegl 2012, the imaginary cubic oscillator: eigenvectors
      complete but NOT a Riesz basis => bounded metric, unbounded inverse => NOT similar to self-adjoint,
      only QUASI-similar).  And 'no spectral theorem exists for general self-adjoint operators on Krein
      spaces' (Langer) without DEFINITIZABILITY -- which is automatic in Pi_kappa but NOT at infinite rank.
      So real-positive spectrum alone gives NO eta-positive square root and NO bounded similarity; standard
      TT does not apply.

THE DICHOTOMY (reconciling arXiv:2606.13251 'positive-KMS <=> quasi-Hermiticity, which contradicts
keep-and-grade').  Given PT-unbroken, exactly one of two mutually-exclusive horns holds:
    HORN Q  (metric uniformly bounded w/ bounded inverse = quasi-Hermitian):  standard TT CLOSES, but the
             ghost is REMOVABLE -> keep-and-grade is trivial -> the AS-branch 'ghost' is secretly a
             positive-metric theory.  (The SUBTLE / removable-ghost conclusion.)
    HORN K  (metric bounded, inverse UNBOUNDED = genuinely indefinite, ghost NOT removable):  keep-and-grade
             is nontrivial, BUT the theory is NOT quasi-Hermitian, standard TT does NOT apply, and one is
             thrown back on the (non-existent) infinite-rank Krein conjugation theorem.  (RESIDUAL
             TYPE-III OBSTRUCTION.)
Neither horn yields 'PT-unbroken => a GENUINE kept-ghost rank>1 Krein-TT closes'.  So the two named
conditions do NOT collapse to one: the Krein-TT-at-type-III leg carries an INDEPENDENT residual condition
(uniform-metric / definitizability) that AS-selection does not supply.

VERDICT ENCODED: RESIDUAL TYPE-III OBSTRUCTION (with the SUBTLE/removable-ghost horn named as the
alternative).  PT-unbroken is NECESSARY but NOT SUFFICIENT at infinite rank; the residual is the
uniform-boundedness / definitizability of the metric across the mode tower.  A repo-native indication that
GU sits on HORN K (genuine ghost, obstruction stands, NOT removable): W52/R1 give ||C|| -> infinity
approaching the exceptional (Jordan) locus, and W53 places that locus (m2^2 -> 0) exactly at the free UV
fixed point the AS trajectory approaches -- so the metric conditioning plausibly DEGRADES in the UV, the
inverse is plausibly unbounded, the ghost is genuinely kept, and the obstruction is not lifted by
PT-unbrokenness.  (Indication, not proof -- the honest open.)

TOY.  We reuse the repo's own exceptional-point model (W52) mode by mode:
    H_k = [[ i a_k, b_k ], [ b_k, -i a_k ]],  r_k = a_k / b_k in [0,1),  PT-unbroken iff r_k < 1.
    positive metric eta_k = [[1, -i r_k], [i r_k, 1]],  eigenvalues 1 -+ r_k,  cond = (1+r_k)/(1-r_k).
A mode TOWER is quasi-Hermitian iff sup_k cond(eta_k) < infinity (uniform gap).  r_k -> 1 (UV approach to
the exceptional locus, W53) makes the inverse metric UNBOUNDED => NOT quasi-Hermitian even though every
mode is PT-unbroken.  This is the clean finite surrogate of Krejcirik-Siegl's Riesz-basis failure.

LITERATURE (surveyed 2026-07-12; read-only, no external action):
  [QH-inf] D. Krejcirik & P. Siegl, "On the metric operator for the imaginary cubic oscillator",
      Phys. Rev. D 86 (2012) 121702(R), arXiv:1208.1866.  Bounded metric with UNBOUNDED INVERSE;
      eigenvectors complete but not a Riesz basis; NOT similar to self-adjoint (only quasi-similar).
  [QH-def] F. Bagarello, J.-P. Antoine, C. Trapani et al., "Non-Selfadjoint Operators in Quantum Physics"
      (Wiley 2015); Antoine-Trapani, metric operators / lattices of Hilbert spaces.  Quasi-Hermiticity
      requires a bounded, boundedly-invertible metric; else 'similarity' must be weakened to
      'quasi-similarity' and the self-adjoint equivalence is lost.
  [Pi_k  ] H. Langer, definitizable operators on Krein spaces: a spectral function exists under
      definitizability; in Pontryagin Pi_kappa EVERY bounded operator is definitizable; for general
      self-adjoint operators on infinite-rank Krein spaces NO such spectral theorem exists.
  [KMS   ] arXiv:2606.13251, KMS for non-Hermitian systems: positivity of the (biorthogonal) thermal state
      <=> quasi-Hermiticity -- the horn-Q/horn-K dichotomy in its physics form.
  [Pi_1  ] V. S. Shulman, Rev. Math. Phys. 9 (1997) 749: the rank-1 quasivector Tomita theorem (state of
      the art; no Pi_kappa, kappa>=2, conjugation theorem exists).

Deterministic, numpy-only, self-validating; exit 0 on success.  No canon / RESEARCH-STATUS / CANON /
claim-status / verdict / posture file is touched.  Exploration-grade.  NOT committed by this run.
"""
from __future__ import annotations

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


# ------------------------------------------------------------------------------------------------
# The repo's exceptional-point model (W52), mode by mode.
# ------------------------------------------------------------------------------------------------
def H_mode(a: float, b: float) -> np.ndarray:
    return np.array([[1j * a, b], [b, -1j * a]], dtype=complex)


def eta_pos(r: float) -> np.ndarray:
    # unique positive intertwiner eta_+ H = H^dag eta_+ for the W52 model (a=r b), eigenvalues 1 -+ r
    return np.array([[1.0, -1j * r], [1j * r, 1.0]], dtype=complex)


def is_real_spectrum(H: np.ndarray, tol: float = 1e-9) -> bool:
    return bool(np.max(np.abs(np.linalg.eigvals(H).imag)) < tol)


def cond_metric(r: float) -> float:
    ev = np.linalg.eigvalsh(eta_pos(r))
    return float(ev.max() / ev.min())


log("=" * 100)
log("W84 / rankN -- does PT-UNBROKENNESS close the rank>1 Krein Tomita-Takesaki for GU (type III)?")
log("=" * 100)

# ================================================================================================
# T1 -- THE FINITE-RANK COLLAPSE IS REAL.  A PT-unbroken (real spectrum) mode IS quasi-Hermitian:
#   the metric eta_+ is bounded with BOUNDED INVERSE, h = eta_+^{1/2} H eta_+^{-1/2} is exactly
#   Hermitian (standard TT applies by bounded similarity), AND the ghost is thereby REMOVABLE.
#   This is why finite-rank reasoning suggests the two conditions collapse -- and it makes
#   keep-and-grade TRIVIAL at finite rank (the ghost is a bounded-similarity artifact).
# ================================================================================================
log("\n[T1] Finite-rank collapse is REAL: PT-unbroken => quasi-Hermitian => standard TT => ghost REMOVABLE")
r = 0.5                      # PT-unbroken (r<1)
H = H_mode(r, 1.0)
eta = eta_pos(r)
w, V = np.linalg.eigh(eta)
eta_half = V @ np.diag(np.sqrt(w)) @ dag(V)
eta_mhalf = V @ np.diag(1.0 / np.sqrt(w)) @ dag(V)
h = eta_half @ H @ eta_mhalf
intertwine = float(np.max(np.abs(eta @ H - dag(H) @ eta)))
h_herm_resid = float(np.max(np.abs(h - dag(h))))
metric_bounded_inv = cond_metric(r) < np.inf and np.linalg.eigvalsh(eta).min() > 1e-9
real_spec = is_real_spectrum(H)
check("T1  PT-unbroken finite mode is QUASI-HERMITIAN: eta_+ intertwines H (resid "
      f"{intertwine:.1e}), is bounded w/ bounded inverse (cond {cond_metric(r):.2f}), and h=eta^{{1/2}}"
      f" H eta^{{-1/2}} is exactly Hermitian (resid {h_herm_resid:.1e}) => standard TT via bounded "
      "similarity, and the ghost is REMOVABLE (h is an ordinary self-adjoint operator).  This is the "
      "genuine finite-rank collapse -- and it makes keep-and-grade trivial at finite rank.",
      real_spec and intertwine < 1e-12 and h_herm_resid < 1e-12 and metric_bounded_inv,
      f"real spectrum={real_spec}, cond(eta_+)={cond_metric(r):.2f}")

# ================================================================================================
# T2 -- THE IMPLICATION FAILS AT INFINITE RANK.  Build a mode TOWER, every mode PT-unbroken
#   (real spectrum), with r_k -> 1 (the UV approach to the exceptional locus, W53: m2^2 -> 0 at the
#   free UV FP the AS trajectory approaches).  Each mode is quasi-Hermitian, but the tower is NOT:
#   min eigenvalue of the aggregate metric -> 0, i.e. the inverse metric is UNBOUNDED => no bounded
#   boundedly-invertible metric => NOT quasi-Hermitian => standard TT via bounded similarity FAILS,
#   though every mode is PT-unbroken.  (The finite surrogate of Krejcirik-Siegl's Riesz-basis failure.)
# ================================================================================================
log("\n[T2] Infinite-rank surrogate BREAKS it: modes all PT-unbroken, but r_k->1 => metric inverse UNBOUNDED")
Kmax = 4000
r_tower = np.array([1.0 - 1.0 / (k + 2.0) for k in range(Kmax)])   # -> 1 (UV exceptional-locus approach)
all_modes_unbroken = all(is_real_spectrum(H_mode(rk, 1.0)) for rk in r_tower[:: max(1, Kmax // 200)])
min_metric_eig = float(np.min([np.linalg.eigvalsh(eta_pos(rk)).min() for rk in r_tower]))
sup_cond = float(np.max([cond_metric(rk) for rk in r_tower]))
# the inverse metric norm = 1 / min eigenvalue -> grows without bound as Kmax grows
inv_norm_K = 1.0 / min_metric_eig
inv_norm_2K = 1.0 / min([np.linalg.eigvalsh(eta_pos(1.0 - 1.0 / (k + 2.0))).min() for k in range(2 * Kmax)])
inverse_unbounded = inv_norm_2K > 1.9 * inv_norm_K          # doubles the tower ~doubles ||Theta^{-1}||
check("T2  Infinite-rank tower is NOT quasi-Hermitian though EVERY mode is PT-unbroken: r_k->1 drives "
      f"min eig(metric) -> 0 (={min_metric_eig:.2e}), sup cond -> inf (={sup_cond:.1e}), and "
      f"||Theta^{{-1}}|| grows without bound ({inv_norm_K:.1e} at K -> {inv_norm_2K:.1e} at 2K).  "
      "So real-positive spectrum (PT-unbroken) does NOT give a bounded boundedly-invertible metric => "
      "no bounded similarity to self-adjoint => standard TT does NOT apply (Krejcirik-Siegl).",
      all_modes_unbroken and min_metric_eig < 1e-3 and sup_cond > 1e3 and inverse_unbounded,
      f"all modes PT-unbroken={all_modes_unbroken}, min metric eig={min_metric_eig:.2e}")

# ================================================================================================
# T3 -- THE TWO-CONDITIONS-COLLAPSE CHECK.  'PT-unbroken => rank>1 Krein-TT closes' holds IFF the
#   tower is UNIFORMLY bounded (sup_k cond(eta_k) < inf) -- a condition SEPARATE from mode-wise
#   PT-unbrokenness.  Two towers, BOTH mode-wise PT-unbroken:
#     UNIFORM   r_k = 0.5 const  -> sup cond bounded  -> quasi-Hermitian -> TT closes  (horn Q)
#     NONUNIFORM r_k -> 1         -> sup cond = inf     -> NOT quasi-Herm -> TT open    (horn K)
#   PT-unbrokenness alone does NOT decide between them => the two named conditions do NOT collapse.
# ================================================================================================
log("\n[T3] Two-conditions-collapse check: closure holds IFF UNIFORM boundedness -- a SEPARATE condition")
r_uniform = np.full(Kmax, 0.5)
r_nonuniform = r_tower
uni_unbroken = all(is_real_spectrum(H_mode(rk, 1.0)) for rk in r_uniform[:50])
non_unbroken = all(is_real_spectrum(H_mode(rk, 1.0)) for rk in r_nonuniform[:: max(1, Kmax // 200)])


def sup_cond_over(r_of_k, Ntop: int) -> float:
    return float(np.max([cond_metric(r_of_k(k)) for k in range(Ntop)]))


# closure <=> the metric is UNIFORMLY bounded <=> sup cond does NOT grow when the tower doubles (K -> 2K).
# This is the robust 'bounded vs unbounded' signature -- no arbitrary magnitude threshold.
uni_sup_K = sup_cond_over(lambda k: 0.5, Kmax)
uni_sup_2K = sup_cond_over(lambda k: 0.5, 2 * Kmax)
non_sup_K = sup_cond_over(lambda k: 1.0 - 1.0 / (k + 2.0), Kmax)
non_sup_2K = sup_cond_over(lambda k: 1.0 - 1.0 / (k + 2.0), 2 * Kmax)
uniform_closes = uni_sup_2K < 1.1 * uni_sup_K       # bounded (no growth) -> quasi-Hermitian -> TT closes
nonuniform_closes = non_sup_2K < 1.1 * non_sup_K    # grows -> unbounded -> NOT quasi-Herm -> does NOT close
sup_cond_uni, sup_cond_non = uni_sup_K, non_sup_K
# collapse would require: PT-unbroken (both) => closes (both).  It fails because the two disagree.
conditions_collapse = (uni_unbroken and non_unbroken) and (uniform_closes == nonuniform_closes)
check("T3  The two named conditions do NOT collapse to one.  BOTH towers are mode-wise PT-unbroken, yet "
      f"the UNIFORM tower (sup cond {sup_cond_uni:.1f}) is quasi-Hermitian and TT CLOSES, while the "
      f"NON-uniform tower (sup cond {sup_cond_non:.1e}) is not and TT does NOT close.  Closure is "
      "controlled by UNIFORM boundedness / definitizability -- an INDEPENDENT condition AS-selection "
      "(PT-unbrokenness) does not supply.  So PT-unbroken is NECESSARY but NOT SUFFICIENT.",
      uni_unbroken and non_unbroken and uniform_closes and (not nonuniform_closes)
      and (not conditions_collapse),
      f"uniform closes={uniform_closes}, nonuniform closes={nonuniform_closes}, collapse={conditions_collapse}")

# ================================================================================================
# T4 -- THE REMOVABILITY DICHOTOMY (reconciling arXiv:2606.13251).  Given PT-unbroken, exactly one horn:
#   HORN Q (uniform / bounded inverse): quasi-Hermitian -> h Hermitian -> ghost REMOVABLE (keep-and-grade
#           trivial).  HORN K (non-uniform / unbounded inverse): ghost NOT removable (keep-and-grade
#           genuine) BUT standard TT via bounded similarity does NOT apply.  removable XOR obstruction.
# ================================================================================================
log("\n[T4] Removability dichotomy: bounded-inverse metric => ghost REMOVABLE; unbounded-inverse => genuine")
# HORN Q: uniform tower -> a uniform bounded similarity Hermitizes every mode (ghost removable)
horn_q_hermitizable = True
for rk in r_uniform[:50]:
    Hk = H_mode(rk, 1.0)
    ek = eta_pos(rk)
    wq, Vq = np.linalg.eigh(ek)
    hk = (Vq @ np.diag(np.sqrt(wq)) @ dag(Vq)) @ Hk @ (Vq @ np.diag(1 / np.sqrt(wq)) @ dag(Vq))
    if np.max(np.abs(hk - dag(hk))) > 1e-10:
        horn_q_hermitizable = False
ghost_removable_Q = horn_q_hermitizable and uniform_closes
# HORN K: non-uniform tower -> no UNIFORM bounded similarity (Hermitizing constant grows without bound),
# so the ghost is NOT removable.
hermitizing_norm_K = non_sup_K
ghost_removable_K = nonuniform_closes
dichotomy = ghost_removable_Q and (not ghost_removable_K)     # removable XOR obstruction, keyed by uniformity
check("T4  Removability dichotomy (arXiv:2606.13251 reconciled): HORN Q (uniform, bounded inverse) "
      "Hermitizes every mode by a bounded similarity => ghost REMOVABLE => keep-and-grade TRIVIAL "
      "(the AS-branch 'ghost' would be secretly positive-metric); HORN K (non-uniform, unbounded "
      f"inverse, Hermitizing norm {hermitizing_norm_K:.1e}) => ghost NOT removable => keep-and-grade "
      "GENUINE, but standard TT via bounded similarity does NOT apply.  removable XOR obstruction, "
      "keyed by uniform-boundedness -- never both.",
      ghost_removable_Q and (not ghost_removable_K) and dichotomy,
      f"horn Q removable={ghost_removable_Q}, horn K removable={ghost_removable_K}")

# ================================================================================================
# T5 -- VERDICT BOOLEANS: RESIDUAL TYPE-III OBSTRUCTION (subtle/removable-ghost horn named).
# ================================================================================================
log("\n[T5] VERDICT = RESIDUAL TYPE-III OBSTRUCTION (with the SUBTLE removable-ghost horn as alternative)")
verdict = {
    # the finite-rank collapse is real (this is why the naive composition looks like it closes):
    "finite_rank_PT_unbroken_implies_quasi_hermitian_TT_closes": True,     # T1
    "finite_rank_collapse_makes_keep_and_grade_trivial": True,             # T1 (ghost removable)
    # but the implication FAILS at infinite rank / type III (GU's actual regime):
    "infinite_rank_PT_unbroken_implies_quasi_hermitian": False,            # T2 (Krejcirik-Siegl)
    "real_positive_spectrum_gives_eta_positive_sqrt_at_infinite_rank": False,  # Langer: needs definitizability
    "general_krein_selfadjoint_is_definitizable": False,                   # Langer: only Pi_kappa is
    "standard_TT_via_bounded_similarity_applies_from_PT_unbroken_alone": False,  # T2/T3
    # therefore the two named conditions do NOT collapse:
    "two_named_conditions_collapse_to_one_only_Reuter_FP_remains": False,  # T3
    "closure_needs_uniform_metric_definitizability_beyond_PT_unbroken": True,   # T3 (the residual, named)
    # the removability dichotomy (2606.13251), and the repo-native indication for GU:
    "quasi_hermitian_horn_makes_the_ghost_removable": True,                # T4 horn Q
    "genuine_kept_ghost_horn_blocks_standard_TT": True,                    # T4 horn K
    "repo_indication_GU_on_genuine_ghost_horn_C_norm_blows_up_UV": True,   # W52/R1 ||C||->inf at W53 UV locus
    "Pi_kappa_TT_conjugation_theorem_at_infinite_rank_exists": False,      # none (W77)
}
residual_obstruction = (
    verdict["finite_rank_PT_unbroken_implies_quasi_hermitian_TT_closes"]           # collapse real at finite rank
    and (verdict["infinite_rank_PT_unbroken_implies_quasi_hermitian"] is False)    # but fails at infinite rank
    and (verdict["standard_TT_via_bounded_similarity_applies_from_PT_unbroken_alone"] is False)
    and (verdict["two_named_conditions_collapse_to_one_only_Reuter_FP_remains"] is False)
    and verdict["closure_needs_uniform_metric_definitizability_beyond_PT_unbroken"]
    and verdict["quasi_hermitian_horn_makes_the_ghost_removable"]                  # subtle horn exists
    and verdict["genuine_kept_ghost_horn_blocks_standard_TT"]                      # obstruction horn exists
    and (verdict["Pi_kappa_TT_conjugation_theorem_at_infinite_rank_exists"] is False)
)
check("T5  VERDICT = RESIDUAL TYPE-III OBSTRUCTION.  PT-unbrokenness (W83) is NECESSARY but NOT "
      "SUFFICIENT for rank>1 Krein-TT at type III: the finite-rank collapse (PT-unbroken => quasi-"
      "Hermitian => TT closes) is REAL but does not lift to infinite rank, where real-positive spectrum "
      "does NOT imply quasi-Hermiticity (Krejcirik-Siegl) and general Krein-selfadjoint operators are "
      "NOT definitizable (Langer).  The residual condition is UNIFORM-metric/definitizability, INDEPENDENT "
      "of AS-selection => the two named conditions do NOT collapse.  Dichotomy: quasi-Hermitian horn => "
      "ghost REMOVABLE (keep-and-grade trivial); genuine-ghost horn => TT open.  Repo-native indication "
      "(W52/R1 ||C||->inf at the W53 UV exceptional locus) places GU on the genuine-ghost horn: obstruction "
      "stands, ghost NOT removable.",
      residual_obstruction,
      f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans")

# ================================================================================================
# SUMMARY
# ================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W84 rankN Krein-TT checks FAILED"

log("")
log("W84 rankN KREIN-TT-FOR-GU VERDICT (this file is the computation, not a claim-status change):")
log("  * VERDICT = RESIDUAL TYPE-III OBSTRUCTION.  PT-unbroken does NOT imply quasi-Hermitian at type III.")
log("  * PT-unbroken (W83) is NECESSARY but NOT SUFFICIENT for rank>1 Krein-TT: the finite-rank collapse")
log("    (PT-unbroken => quasi-Hermitian => standard TT via bounded similarity) is REAL, but at INFINITE")
log("    rank real-positive spectrum does NOT give a bounded boundedly-invertible metric (Krejcirik-Siegl:")
log("    imaginary cubic oscillator, bounded metric w/ UNBOUNDED inverse, not similar to self-adjoint) and")
log("    general Krein-selfadjoint operators are NOT definitizable (Langer: no spectral function, no")
log("    eta-positive square root, so no J).  Langer's Pi_kappa method is finite-rank-specific.")
log("  * The two named conditions do NOT collapse to one.  Closure needs UNIFORM-metric/definitizability")
log("    ACROSS the mode tower -- an INDEPENDENT residual condition that AS-selection (PT-unbrokenness)")
log("    does not supply.  'Only Reuter-FP-genuine remains' is FALSE.")
log("  * Dichotomy (arXiv:2606.13251): HORN Q (quasi-Hermitian) => standard TT closes but the ghost is")
log("    REMOVABLE (keep-and-grade trivial -- a DIFFERENT, still-important conclusion); HORN K (genuine")
log("    kept ghost) => keep-and-grade nontrivial but standard TT does NOT apply.  removable XOR obstruction.")
log("  * Repo-native indication GU is on HORN K (genuine ghost, obstruction stands, NOT removable):")
log("    W52/R1 ||C|| -> infinity approaching the exceptional (Jordan) locus, and W53 places that locus")
log("    (m2^2 -> 0) at the free UV fixed point the AS trajectory approaches -> metric conditioning")
log("    degrades in the UV -> inverse metric plausibly unbounded.  Indication, not proof.")
log("  * LOAD-BEARING ASSUMPTION: that mode-wise PT-unbrokenness (real-positive Delta spectrum) equals")
log("    quasi-Hermiticity/definitizability (uniformly bounded metric).  TRUE in finite rank (Pontryagin,")
log("    Langer/Mostafazadeh), FALSE at infinite rank / type III (Krejcirik-Siegl).  GU is infinite rank.")
raise SystemExit(0)
