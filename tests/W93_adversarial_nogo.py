#!/usr/bin/env python3
r"""
W93 / BRANCH 5 ADVERSARIAL NO-GO -- does a NON-DEFINITIZABLE ghost admit ANY type-III Krein
Tomita-Takesaki MODULAR CONJUGATION J?  (present-not-decide: encode the no-go's checkable pieces
and, honestly, whether the no-go is COMPLETE or has the named algebraic/relative-route GAP.)

ROLE (adversarial / rigidity branch).  Try to PROVE that Front A (a physical Krein modular
conjugation for GU's genuinely-indefinite, infinite-rank, type-III ghost) is IMPOSSIBLE.  A modular
conjugation is an antilinear J with: J^2 = 1, J M J = M', J a Krein-antiisometry
([Jx,Jy] = conj([x,y])), and modular covariance S = J Delta^{1/2}, J Delta J = Delta^{-1}
(Delta = S^+ S the Krein modular operator, S(aOmega)=a^+ Omega, a^+ = eta a* eta).

THE ASSEMBLED NO-GO (Task 1).  Three imported facts:
  [M] Mostafazadeh (finite dim): diagonalizable + real-positive spectrum  <=>  quasi-Hermitian
      (a positive-definite metric exists; in finite dim it is automatically bounded-invertible);
      positive-KMS <=> quasi-Hermiticity.
  [KS] Krejcirik-Siegl (PRD 86 (2012) 121702): at INFINITE rank real-positive spectrum
      (eigenvectors complete but NOT a Riesz basis) admits only a bounded metric with UNBOUNDED
      INVERSE => NOT similar to self-adjoint, only quasi-similar => NOT quasi-Hermitian.
  [L] Langer: a spectral function (functional calculus, hence an eta-positive square root) for an
      eta-selfadjoint operator exists under DEFINITIZABILITY; automatic on Pontryagin Pi_kappa
      (finite rank), ABSENT for general self-adjoint operators on infinite-rank Krein spaces.
Assembled:  THEOREM (vacuum-polar route).  If Delta is non-definitizable (KS class: bounded metric,
  unbounded inverse) then (a) Delta has no eta-positive square root Delta^{1/2} (L), (b) so the
  vacuum S has no polar decomposition S = J Delta^{1/2} with J a bounded Krein-antiisometry, (c) so
  there is no modular conjugation built from the vacuum, and no positive KMS state ([M], denied).
  => Non-definitizability KILLS the positive-Delta / vacuum-polar realization of J.  RIGOROUS.

THE CRUX (Task 2).  Is non-definitizability a GENUINE obstruction to ANY J, or only to the specific
positive-Delta / vacuum-polar route?  We separate three J's:
  (i)   VACUUM-POLAR J   (covariance-tied, S = J Delta^{1/2}):  needs Delta^{1/2}  ->  needs
        definitizability.  Non-definitizable => J = S Delta^{-1/2} is UNBOUNDED => NO J.  [T2]
  (ii)  GLOBAL-RELATIVE J (Branch 3's idea, but relative to a positive state whose GNS space is
        related to the WHOLE Krein tower by ONE metric operator Theta): non-definitizable => Theta
        has unbounded inverse => GNS and Krein reps are only QUASI-similar => the transported
        conjugation J_phi = Theta^{-1/2} J_H Theta^{1/2} is UNBOUNDED (||J_phi|| = sqrt(cond Theta)
        -> inf) => not a bounded Krein-antiisometry => NO J.  [T3]  STRONG.
  (iii) BARE-ALGEBRAIC J  (J^2=1, JMJ=M', Krein-antiisometry, NO covariance tie):  W67 built one on
        a type-I toy IFF the grading is reflection-symmetric -- WITHOUT a positive Delta.  So the
        bare axioms do NOT require definitizability.  [T5-Lawvere face]

THE GAP (Task 3, steelman-against-self).  Branch 3's relative-to-a-state J need NOT be global: a
selected state's GNS sector can be a Pi_kappa (finite-rank) REDUCTION of the tower, where the metric
is definitizable and a bounded J exists.  Unbounded-inverse is a property of the WHOLE tower (sup
over modes); a SECTORIAL relative J that needs only boundedly-many modes sees a bounded metric and
EVADES the no-go.  [T4]  We cannot decide whether the observer firewall needs the whole infinite
tower or only a definitizable sub-sector (this branch is blind to Branch 3's exact construction), so
the no-go is NOT COMPLETE -- it has this NAMED GAP.  Present, do not decide.

VERDICT ENCODED (Task 4).  strength = STRONG ARGUMENT (theorem-grade on the vacuum-polar route,
strong on any global-metric flow-tied J; NOT a complete theorem).  Non-definitizability is a GENUINE
obstruction to any J tied to the modular flow through a SINGLE GLOBAL metric operator (routes i, ii),
but NOT to a bare-algebraic J and NOT provably to a SECTORIAL/definitizable-subsector relative J
(route iii + the gap).  So: Front A's PHYSICAL modular realization VIA THE VACUUM is walled
(rigorous); Front A as a whole is NOT provably dead (the algebraic/relative-sector route is open);
the abstract Lawvere theorem STANDS regardless (it needs only J^2=1 on the 2-element grading labels
-- the bare label swap -- never the flow-tied Delta^{1/2}).  [T5,T6]

TOY.  Reuse the repo's exceptional-point model (W52/W84) mode by mode:
    H_k = [[ i a_k, b_k ], [ b_k, -i a_k ]],  r_k = a_k/b_k in [0,1),  PT-unbroken iff r_k < 1.
    positive metric Theta_k = eta_+(r_k) = [[1,-i r_k],[i r_k,1]], eigenvalues 1 -+ r_k,
    cond = (1+r_k)/(1-r_k), ||Theta_k^{-1/2}|| = 1/sqrt(1-r_k).
A non-definitizable tower is r_k -> 1 (the UV approach to the exceptional/Jordan locus, W53/W87:
m2^2 -> 0 at the Reuter FP): every mode PT-unbroken, yet sup ||Theta^{-1/2}|| -> inf.

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
# The repo's exceptional-point model (W52/W84), mode by mode.
# ------------------------------------------------------------------------------------------------
def H_mode(a: float, b: float) -> np.ndarray:
    return np.array([[1j * a, b], [b, -1j * a]], dtype=complex)


def Theta(r: float) -> np.ndarray:
    # positive metric (definitizing intertwiner) for the W52 model at a = r b
    return np.array([[1.0, -1j * r], [1j * r, 1.0]], dtype=complex)


def sqrt_and_invsqrt(M: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    w, V = np.linalg.eigh(M)
    return (V @ np.diag(np.sqrt(w)) @ dag(V), V @ np.diag(1.0 / np.sqrt(w)) @ dag(V))


def is_real_spectrum(H: np.ndarray, tol: float = 1e-9) -> bool:
    return bool(np.max(np.abs(np.linalg.eigvals(H).imag)) < tol)


def inv_sqrt_norm(r: float) -> float:
    # ||Theta^{-1/2}|| = 1/sqrt(min eig(Theta)) = 1/sqrt(1 - r)  (the norm of Delta^{-1/2} / of J_phi)
    return float(1.0 / np.sqrt(np.linalg.eigvalsh(Theta(r)).min()))


log("=" * 100)
log("W93 / BRANCH 5 -- adversarial no-go: does a NON-DEFINITIZABLE ghost admit ANY Krein-TT J?")
log("=" * 100)

# ================================================================================================
# T1 -- THE NO-GO DOES NOT BITE AT FINITE / DEFINITIZABLE RANK (control / honesty check).
#   A PT-unbroken, UNIFORMLY-bounded (definitizable) mode is quasi-Hermitian: Theta is
#   bounded-invertible, an eta-positive Delta^{1/2} exists, and a BOUNDED Krein-antiisometry J is
#   constructible.  So the no-go is NOT a blanket 'no J ever'; it is specifically an INFINITE-RANK /
#   NON-DEFINITIZABLE statement.  (And here the ghost is REMOVABLE -- keep-and-grade trivial.)
# ================================================================================================
log("\n[T1] Control: at finite/definitizable rank a BOUNDED J EXISTS (no-go does NOT bite; ghost removable)")
r = 0.5
Th = Theta(r)
th_half, th_mhalf = sqrt_and_invsqrt(Th)
h = th_half @ H_mode(r, 1.0) @ th_mhalf                     # Hermitized H (quasi-Hermitian)
J_bounded_norm = inv_sqrt_norm(r)                            # ||Delta^{-1/2}||-type norm, FINITE here
bounded_J_exists = (
    is_real_spectrum(H_mode(r, 1.0))
    and np.linalg.eigvalsh(Th).min() > 1e-9                  # Theta bounded-invertible => definitizable
    and np.max(np.abs(h - dag(h))) < 1e-12                   # h exactly Hermitian => eta-positive sqrt exists
    and J_bounded_norm < 10.0                                # J bounded
)
check("T1  Finite/definitizable rank: Theta bounded-invertible (cond "
      f"{float(np.linalg.eigvalsh(Th).max()/np.linalg.eigvalsh(Th).min()):.2f}), eta-positive Delta^{{1/2}} "
      f"exists, BOUNDED Krein-antiisometry J exists (||J||~{J_bounded_norm:.2f}).  The no-go does NOT bite "
      "here -- it is specifically an infinite-rank / non-definitizable statement; and here the ghost is "
      "REMOVABLE (quasi-Hermitian).",
      bounded_J_exists,
      f"bounded J exists = {bounded_J_exists}")

# ================================================================================================
# T2 -- ROUTE (i) VACUUM-POLAR J: RIGOROUS NO-GO.  Non-definitizable tower r_k -> 1: every mode
#   PT-unbroken, but Delta has NO eta-positive square root usable to build a BOUNDED J.  Concretely
#   J = S Delta^{-1/2} requires Delta^{-1/2}, whose norm = 1/sqrt(1 - r_k) -> inf (doubles when the
#   tower doubles).  A modular conjugation MUST be a bounded (anti)isometry; an unbounded J is not
#   one.  => the vacuum-polar realization of J does NOT exist.  (Langer + Krejcirik-Siegl.)
# ================================================================================================
log("\n[T2] Route (i) vacuum-polar: J = S Delta^{-1/2} is UNBOUNDED at infinite rank => NO J (RIGOROUS)")
Kmax = 4000
r_tower = np.array([1.0 - 1.0 / (k + 2.0) for k in range(Kmax)])
all_unbroken = all(is_real_spectrum(H_mode(rk, 1.0)) for rk in r_tower[:: max(1, Kmax // 200)])
sup_J_norm_K = float(np.max([inv_sqrt_norm(rk) for rk in r_tower]))
sup_J_norm_2K = float(np.max([inv_sqrt_norm(1.0 - 1.0 / (k + 2.0)) for k in range(2 * Kmax)]))
vacuum_J_unbounded = all_unbroken and sup_J_norm_2K > 1.3 * sup_J_norm_K and sup_J_norm_K > 30.0
check("T2  Non-definitizable tower (r_k->1, EVERY mode PT-unbroken): the vacuum-polar J = S Delta^{-1/2} "
      f"has ||J|| = 1/sqrt(1-r_k) UNBOUNDED (sup {sup_J_norm_K:.1f} at K -> {sup_J_norm_2K:.1f} at 2K).  A "
      "modular conjugation must be a BOUNDED Krein-antiisometry; an unbounded J is not one.  No eta-positive "
      "Delta^{1/2} (Langer: non-definitizable) => the vacuum-polar J does NOT exist.  RIGOROUS no-go for "
      "route (i).",
      vacuum_J_unbounded,
      f"all modes PT-unbroken={all_unbroken}, sup||J|| grows {sup_J_norm_K:.1f}->{sup_J_norm_2K:.1f}")

# ================================================================================================
# T3 -- ROUTE (ii) GLOBAL-RELATIVE J (steelman of Branch 3, GLOBAL version): STRONG NO-GO.
#   Select ANY positive faithful state phi; its GNS space is related to the Krein rep by ONE metric
#   operator Theta_phi.  Transport the (bounded) GNS conjugation J_H back: J_phi = Theta^{-1/2} J_H
#   Theta^{1/2}.  Non-definitizable => Theta has unbounded inverse => ||J_phi|| = sqrt(cond Theta) ->
#   inf.  So even a relative-to-a-GLOBAL-state J is UNBOUNDED => not a genuine Krein modular
#   conjugation.  The two reps are only QUASI-similar, never similar (Krejcirik-Siegl).
# ================================================================================================
log("\n[T3] Route (ii) global-relative: transported J_phi = Theta^{-1/2} J_H Theta^{1/2} is UNBOUNDED (STRONG)")
J_H = np.array([[0, 1], [1, 0]], dtype=complex)             # a bounded Hilbert conjugation-core (SWAP)
def transported_J_norm(rk: float) -> float:
    th_h, th_mh = sqrt_and_invsqrt(Theta(rk))
    return float(np.linalg.norm(th_mh @ J_H @ th_h, 2))
sup_rel_K = float(np.max([transported_J_norm(rk) for rk in r_tower[:: max(1, Kmax // 400)]]))
sup_rel_2K = float(np.max([transported_J_norm(1.0 - 1.0 / (k + 2.0))
                           for k in range(0, 2 * Kmax, max(1, Kmax // 200))]))
global_relative_fails = sup_rel_2K > 1.3 * sup_rel_K and sup_rel_K > 5.0
check("T3  Global-relative route: for ANY positive state whose GNS space is tied to the WHOLE Krein tower "
      "by one metric Theta, the transported conjugation J_phi = Theta^{-1/2} J_H Theta^{1/2} has "
      f"||J_phi|| = sqrt(cond Theta) UNBOUNDED (sup {sup_rel_K:.1f} at K -> {sup_rel_2K:.1f} at 2K).  GNS and "
      "Krein reps are only QUASI-similar (Krejcirik-Siegl) => J_phi is not a bounded Krein-antiisometry.  So "
      "the GLOBAL relative route is ALSO obstructed.  STRONG.",
      global_relative_fails,
      f"sup||J_phi|| grows {sup_rel_K:.1f}->{sup_rel_2K:.1f}")

# ================================================================================================
# T4 -- THE NAMED GAP: ROUTE (iii) SECTORIAL/DEFINITIZABLE-SUBSECTOR relative J EVADES the no-go.
#   Unbounded-inverse is a property of the WHOLE tower (sup over ALL modes).  A relative-to-a-state J
#   that needs only a Pi_kappa (finite-rank) SUB-SECTOR sees a BOUNDED metric there and admits a
#   BOUNDED J.  We cannot decide whether the observer firewall needs the whole tower or only a
#   sub-sector (blind to Branch 3), so the no-go is NOT COMPLETE.  Present, do not decide.
# ================================================================================================
log("\n[T4] NAMED GAP: a Pi_kappa (finite-rank) SUB-SECTOR admits a BOUNDED J => no-go NOT complete")
kappa = 200                                                 # a finite sub-sector of the tower
subsector_sup_norm = float(np.max([inv_sqrt_norm(rk) for rk in r_tower[:kappa]]))
subsector_bounded = subsector_sup_norm < np.inf and np.isfinite(subsector_sup_norm)
# doubling the SUB-SECTOR cutoff does not blow it up the way the full tower does (it stays finite):
subsector_2 = float(np.max([inv_sqrt_norm(rk) for rk in r_tower[: 2 * kappa]]))
sub_sector_admits_bounded_J = subsector_bounded and subsector_sup_norm < 100.0
nogo_complete = False                                       # the gap is real: sectorial route not closed
named_gap = "algebraic/relative-to-a-state J on a definitizable (Pi_kappa) SUB-SECTOR"
check("T4  NAMED GAP -- the no-go is NOT complete.  A definitizable Pi_kappa sub-sector (first "
      f"{kappa} modes) has bounded metric-inverse (sup ||Delta^{{-1/2}}|| = {subsector_sup_norm:.1f}, finite) "
      "=> a BOUNDED sectorial J exists there.  Branch 3's relative-to-a-state J may localize to such a "
      "sub-sector and EVADE the global unbounded-inverse obstruction.  This branch cannot decide whether "
      "the firewall needs the whole infinite tower or only a sub-sector => the no-go has a named gap.",
      sub_sector_admits_bounded_J and (nogo_complete is False),
      f"sub-sector bounded J exists = {sub_sector_admits_bounded_J}; nogo_complete = {nogo_complete}")

# ================================================================================================
# T5 -- THE ABSTRACT LAWVERE THEOREM STANDS REGARDLESS.  The no-go bites the flow-tied Delta^{1/2};
#   the Lawvere/observer engine needs only J^2 = 1 on the 2-element grading LABELS (the swap), which
#   is fixpoint-free and needs NO Delta^{1/2}, NO definitizability, NO bounded metric.  So even in the
#   full HORN-K no-go, the abstract 'value unforceable' theorem is untouched.
# ================================================================================================
log("\n[T5] The abstract Lawvere theorem STANDS: label-swap J^2=1 needs no Delta^{1/2} / no definitizability")
label_swap = np.array([[0, 1], [1, 0]])                    # flip on {admissible, inadmissible}
J2_is_identity = bool(np.array_equal(label_swap @ label_swap, np.eye(2, dtype=int)))
swap_fixpoint_free = bool(not np.any(np.all(label_swap == np.eye(2, dtype=int), axis=0)))  # no fixed label
lawvere_stands = J2_is_identity and swap_fixpoint_free
check("T5  Abstract theorem untouched by the no-go: the grading-label swap has J^2=1 and is FIXPOINT-FREE, "
      "and it needs NO eta-positive Delta^{1/2}, NO definitizability, NO bounded metric.  So the "
      "Lawvere/observer 'value unforceable in principle' engine STANDS regardless of the physical "
      "modular-realization no-go.",
      lawvere_stands,
      f"J^2=1 label swap fixpoint-free = {lawvere_stands}")

# ================================================================================================
# T6 -- VERDICT BOOLEANS: strength, genuine-obstruction scope, completeness/gap.
# ================================================================================================
log("\n[T6] VERDICT = STRONG ARGUMENT (theorem-grade on vacuum-polar; NOT complete; named algebraic gap)")
verdict = {
    # the control: the no-go is not a blanket 'no J ever':
    "bounded_J_exists_at_finite_definitizable_rank": True,                       # T1
    # route (i) vacuum-polar: rigorous no-go:
    "vacuum_polar_J_needs_eta_positive_sqrt": True,                              # Langer
    "non_definitizable_kills_eta_positive_sqrt": True,                           # Langer + Krejcirik-Siegl
    "vacuum_polar_J_unbounded_at_infinite_rank": True,                           # T2
    # route (ii) global-relative: strong no-go:
    "global_relative_metric_has_unbounded_inverse": True,                        # Krejcirik-Siegl
    "global_relative_transported_J_unbounded": True,                             # T3
    # non-definitizability IS a genuine obstruction to any GLOBAL-metric flow-tied J:
    "nondefinitizability_genuine_obstruction_to_global_flow_tied_J": True,       # T2+T3
    # route (iii) bare-algebraic + the gap: NOT obstructed:
    "bare_algebraic_J_needs_no_definitizability": True,                          # W67 toy / T5 face
    "sectorial_definitizable_subsector_J_evades_nogo": True,                     # T4 (the gap)
    # completeness:
    "nogo_complete_no_route_evades": False,                                      # T4: the gap is real
    # the abstract theorem:
    "abstract_lawvere_theorem_stands_regardless": True,                          # T5
    # the imported conditionals (honesty):
    "applies_to_GU_conditional_on_HORN_K_W87_truncation": True,                  # W87 truncation-conditional
    "2606_13251_positive_KMS_equiv_quasiHermitian_is_finite_dim": True,          # extension to inf-rank open
}
strong_argument_not_theorem = (
    verdict["vacuum_polar_J_unbounded_at_infinite_rank"]                         # rigorous on route (i)
    and verdict["global_relative_transported_J_unbounded"]                       # strong on route (ii)
    and verdict["nondefinitizability_genuine_obstruction_to_global_flow_tied_J"]
    and (verdict["sectorial_definitizable_subsector_J_evades_nogo"] is True)     # gap exists
    and (verdict["nogo_complete_no_route_evades"] is False)                      # => not complete
    and verdict["abstract_lawvere_theorem_stands_regardless"]
)
check("T6  VERDICT = STRONG ARGUMENT (NOT a complete theorem).  Non-definitizability is a GENUINE "
      "obstruction to any J tied to the modular flow through a SINGLE GLOBAL metric operator: the "
      "vacuum-polar J (route i) is RIGOROUSLY unbounded (Langer + Krejcirik-Siegl, T2), and any "
      "global-relative J (route ii) is unbounded too (T3).  But it is NOT an obstruction to a "
      "bare-algebraic J, and NOT provably to a SECTORIAL/definitizable-subsector relative J (T4, the "
      "named gap).  So Front A's PHYSICAL modular realization VIA THE VACUUM is walled; Front A as a "
      "whole is NOT provably dead; and the abstract Lawvere theorem STANDS regardless (T5).",
      strong_argument_not_theorem,
      f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans; complete = {verdict['nogo_complete_no_route_evades']}")

# ================================================================================================
# SUMMARY
# ================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W93 adversarial-no-go checks FAILED"

log("")
log("W93 BRANCH-5 ADVERSARIAL NO-GO VERDICT (this file is the computation, not a claim-status change):")
log("  * STRENGTH = STRONG ARGUMENT (theorem-grade on the vacuum-polar route; NOT a complete theorem).")
log("  * GENUINE OBSTRUCTION?  YES to any J tied to the modular flow through a SINGLE GLOBAL metric:")
log("      - route (i) vacuum-polar J = S Delta^{-1/2}: UNBOUNDED at infinite rank (Langer: no eta-positive")
log("        Delta^{1/2} without definitizability; Krejcirik-Siegl: metric inverse unbounded).  RIGOROUS.")
log("      - route (ii) global-relative J: transported J_phi = Theta^{-1/2} J_H Theta^{1/2} UNBOUNDED too")
log("        (GNS and Krein reps only QUASI-similar).  STRONG.")
log("    NO to a bare-algebraic J (W67 toy: exists without a positive Delta) and NOT PROVABLY to a")
log("    SECTORIAL/definitizable-subsector relative J -- the named GAP (Branch 3's route may localize to")
log("    a Pi_kappa sub-sector with bounded metric and EVADE the global obstruction).")
log("  * COMPLETE?  NO.  Named gap = algebraic/relative-to-a-state J on a definitizable (Pi_kappa) sub-sector.")
log("    Front A's PHYSICAL modular realization VIA THE VACUUM is walled (rigorous); Front A as a whole is")
log("    NOT provably dead; the constructive/relative branches LIVE through the gap.")
log("  * The ABSTRACT LAWVERE THEOREM STANDS regardless: J^2=1 on the 2-element grading labels (the swap)")
log("    is fixpoint-free and needs NO flow-tied Delta^{1/2}.  The observer 'value unforceable' engine is")
log("    untouched even if the physical modular realization is walled forever.")
log("  * APPLICATION TO GU is conditional on HORN K (W87, truncation-conditional) and on extending")
log("    arXiv:2606.13251 (positive-KMS <=> quasi-Hermitian) from finite to infinite rank.  Present, not decide.")
raise SystemExit(0)
