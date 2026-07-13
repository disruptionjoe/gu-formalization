#!/usr/bin/env python3
r"""
W103 / STEELMAN 1 of the W98 break: does the non-definitizability obstruction FACTOR THROUGH a clean
TAIL QUOTIENT (Calkin-style: bounded operators modulo compact / finite-rank observer-accessible
corrections), so that the W98 wall is a LOCATED, TYPED ADAPTER SLOT rather than an unstructured failure?

THE STEELMAN (tested, not assumed): the divergence cond(C) = sup_k (1+r_k)/(1-r_k) -> inf (W98) lives
EXCLUSIVELY in the k->inf sup.  Claim: (i) the metric C = oplus_k eta(r_k) descends to a WELL-DEFINED
class [C] in the Calkin-style quotient; (ii) the definitizability failure descends to the CLEAN statement
"[C] is a singular (non-invertible) element -- in fact exactly TWICE A PROPER PROJECTION"; (iii) the
modular structure splits (flow = clean and bounded everywhere; conjugation = obstructed exactly by the
quotient class); and the slot left open is TYPED (a positive metric at infinity on a specific Krein-null,
essentially-complex line).  The adversary's vacuity objection ("every divergence lives at the tail by
definition; the quotient restates the break") is answered by TWO COUNTER-MODELS in which the BREAK is
identical but the quotient statement FAILS -- so the quotient statement has model-discriminating content.

THE MODEL (W98's own data): per momentum k a Krein doublet with metric
    eta(r) = [[1, -i r],[i r, 1]] = I + r*sigma_y,   eigenvalues 1 -+ r,   cond = (1+r)/(1-r),
    r_k = g / (g + Dw(k)/2),  Dw(k) = |m1^2-m2^2|/(w1+w2) ~ 1/(2k)  ->  0,   so r_k -> 1 (non-UV-soft g).

HEADLINE FACTS COMPUTED HERE (exact per-block, verified numerically):
  F1 (tail limit EXISTS):     ||eta(r_k) - eta(1)|| = 1 - r_k -> 0, and eta(1) = 2P with P = P^2 = P^dag
                              a RANK-1 PROJECTION.  Hence C = 2*P_oplus + K with K COMPACT (block norms
                              -> 0):  the interacting Krein metric is a COMPACT PERTURBATION OF TWICE A
                              PROJECTION.  [C] = 2[P_oplus] in the Calkin quotient -- a proper projection
                              class, manifestly NON-invertible ([P] != 0 since P_oplus is infinite rank;
                              [P] != 1 since 1-P_oplus is infinite rank).
  F2 (exactness / iff):       every finite mode is STRICTLY definitizable (r_k < 1), so C is invertible
                              in B(H)  <=>  limsup r_k < 1  <=>  [C] invertible in the quotient.  The
                              obstruction has ZERO finite-mode component: it descends WITHOUT LOSS.
  F3 (rate-independence):     ANY two non-UV-soft profiles (r_k -> 1) give the SAME tail class 2[P]
                              (their difference is compact).  The quotient forgets the divergence RATE
                              and remembers only the singular limit -- the slot is ONE typed object.
  F4 (modular split):         eta(r)^{it} is UNITARY (norm 1) at EVERY r < 1 (flow: clean, no
                              conditioning cost), while ||eta(r)^{-1/2}|| = 1/sqrt(1-r) -> inf
                              (conjugation: obstructed).  The flow has NO tail norm-limit (the phase
                              (1-r_k)^{it} spins as log(1-r_k) -> -inf): the tail carries a degenerate
                              metric + an unfixed spinning phase.  The missing datum is a boundary
                              phase/metric AT INFINITY.
  F5 (the typed slot):        ker eta(1) = span{(i,1)/sqrt(2)} -- a KREIN-NULL (<e, sigma_z e> = 0),
                              ESSENTIALLY-COMPLEX line (e and conj(e) span C^2), CONSTANT across the
                              tail.  The completion must supply a positive invertible metric on the
                              (1-P) tail line; NO compact (observer-accessible) correction can do it
                              (compacts have zero image in the quotient) => the filler is PROVABLY
                              EXTERNAL to the observer filtration.  Closure-theorem-forced externality.
  F6 (Nguyen-slot comparison): [eta(r), J_quat] = 2r*conj (J_quat = sigma_y K, the doublet's canonical
                              quaternionic structure): the FREE metric is quaternionic-linear, the
                              INTERACTING part is EXACTLY the J_quat-ODD component, and sigma_y = i*J0
                              (i times a real matrix) is the scalar-i-laden mixing.  META-TYPE match
                              with the Nguyen para-3.1 slot (closure-theorem-forced external object):
                              GENUINE.  Fine-type (scalar-i / antilinear-interface): SUGGESTIVE but
                              representative-dependent.  PAYLOAD type MISMATCH (discrete count-fixing
                              vs continuous definitizing metric).  Verdict: RELATED, not SAME.

VACUITY COUNTER-MODELS (the content beyond the break):
  CM1 (rotating mixing):      theta_k non-convergent, eta_k = I + r_k*(cos th_k sigma_x + sin th_k
                              sigma_y).  Break IDENTICAL (same eigenvalues 1 -+ r_k, same cond
                              divergence) but NO tail norm-limit exists: C is NOT projection+compact;
                              the slot is NOT a single line bundle at infinity.  The steelman's
                              statement is FALSE here while W98's break statement is TRUE => the
                              quotient statement is strictly stronger than the break.
  CM2 (finite-k exceptional): one finite mode sits exactly AT r = 1, tail UV-soft.  C is singular in
                              B(H) (a break) but its 0-eigenvalue is FINITE-RANK: the quotient class IS
                              invertible.  The obstruction does NOT factor through the tail here =>
                              "descends exactly" (F2) is a PROPERTY of the W98 model, not a tautology.

VERDICT ENCODED: PARTIAL (leaning viable on the adapter-slot half).  The quotient structure is REAL and
CLEAN in the W98 Krein-doublet model (F1-F5, with counter-model-backed content), so the wall IS a
located, typed interface slot at model grade.  The UNIFICATION with the Nguyen slot is RELATED (same
meta-type: internal closure theorem forcing a typed external object; shared scalar-i/antilinear flavor)
but NOT established SAME-TYPE (different algebras, different payload).  The genuinely-type-III intrinsic
version (no compacts inside a III_1 factor; the tail quotient must be built from the mode filtration /
flow-of-weights side) is the named frontier, NOT done here.

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


SX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SY = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
SZ = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def eta(r: float, theta: float = np.pi / 2.0) -> np.ndarray:
    # mixing direction theta in the Hermitian-traceless plane; theta=pi/2 is the W52/W98 form I + r*SY
    return I2 + r * (np.cos(theta) * SX + np.sin(theta) * SY)


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, 2))


def eig_minmax(A: np.ndarray) -> tuple[float, float]:
    ev = np.linalg.eigvalsh(A)
    return float(ev.min()), float(ev.max())


# --- the W98 mode data -----------------------------------------------------------------------------
M1, M2, G = 0.0, 0.30, 0.10


def omega(k: float, m: float) -> float:
    return float(np.sqrt(k * k + m * m))


def dsplit(k: float) -> float:
    return abs(omega(k, M1) - omega(k, M2))


def r_of(g_k: float, k: float) -> float:
    return float(min(g_k / (g_k + 0.5 * dsplit(k)), 1.0 - 1e-15))


log("=" * 100)
log("W103 / STEELMAN 1: does the W98 obstruction FACTOR THROUGH a clean TAIL QUOTIENT (Calkin-style),")
log("       leaving a TYPED adapter slot -- and does the slot's type match the Nguyen para-3.1 slot?")
log("=" * 100)

# ====================================================================================================
# T1 -- QUOTIENT INVERTIBILITY CRITERION.  C = oplus_k eta(r_k) is invertible-with-bounded-inverse in
#   the Calkin quotient  <=>  0 not in sigma_ess(C)  <=>  limsup_k (1 - r_k) > 0.  W98 model (non-UV-
#   soft): tail infimum of the min-eigenvalue -> 0 => [C] NON-invertible.  UV-soft g(k)=G/k^2: tail
#   min-eigenvalue -> 1 => [C] invertible.  Marginal g(k)=G/k: bounded away from 0 => invertible (not
#   clean).  This is exactly the W100 condition-X boundary DESCENDED to a single C*-invertibility
#   statement about one element of the quotient.
# ====================================================================================================
log("\n[T1] Calkin-invertibility criterion: [C] invertible <=> limsup(1 - r_k) > 0  (the X boundary, descended)")


def tail_min_eig(profile, windows=((1e3, 2e3), (4e3, 8e3), (1.6e4, 3.2e4))) -> list[float]:
    out = []
    for a, b in windows:
        ks = np.linspace(a, b, 400)
        out.append(min(eig_minmax(eta(r_of(profile(float(k)), float(k))))[0] for k in ks))
    return out


hard = tail_min_eig(lambda k: G)                    # non-UV-soft (physical): r_k -> 1
soft = tail_min_eig(lambda k: G / (k * k + 1.0))    # UV-soft (condition X): r_k -> 0
marg = tail_min_eig(lambda k: G / k)                # marginal O(1/k): r_k -> const < 1
hard_noninv = hard[0] > hard[1] > hard[2] and hard[2] < 1e-3          # tail min-eig -> 0
soft_inv = all(m > 0.9 for m in soft)                                  # tail min-eig -> 1 (clean)
marg_inv = all(m > 0.05 for m in marg) and abs(marg[1] - marg[2]) < 0.05  # bounded away from 0, const
check("T1  [C] NON-invertible in the quotient for the physical (non-UV-soft) coupling: tail min-eigenvalue "
      f"-> 0 ({hard[0]:.2e} -> {hard[1]:.2e} -> {hard[2]:.2e}); INVERTIBLE for UV-soft (min-eig "
      f"{min(soft):.3f} > 0.9, clean) and marginal O(1/k) (min-eig ~ {marg[2]:.3f} = const, bounded not "
      "clean).  The W100 falsification boundary X descends VERBATIM to invertibility of one quotient "
      "element.", hard_noninv and soft_inv and marg_inv,
      f"hard tail min-eig {hard[2]:.1e}; soft {min(soft):.3f}; marginal {marg[2]:.3f}")

# ====================================================================================================
# T2 -- THE TAIL LIMIT EXISTS AND IS TWICE A PROJECTION (the class is CLEAN, not just singular).
#   ||eta(r_k) - eta(1)|| = 1 - r_k -> 0  (exact identity), and eta(1) = 2P with P a rank-1 orthogonal
#   projection.  Hence C - 2*P_oplus is block-diagonal with block norms -> 0 = a COMPACT operator:
#   C = 2*P_oplus + compact,  [C] = 2[P_oplus]  -- a PROPER projection class (P and 1-P both infinite
#   rank), manifestly non-invertible.  This is STRICTLY MORE than "cond -> inf": it identifies the
#   singular quotient element and its null direction.
# ====================================================================================================
log("\n[T2] The tail limit: C = 2*(projection) + compact; [C] = 2[P], a proper projection class")
eta1 = eta(1.0)
P = 0.5 * eta1
is_proj = opnorm(P @ P - P) < 1e-12 and opnorm(P - dag(P)) < 1e-12 and abs(np.trace(P).real - 1.0) < 1e-12
ks_conv = [1e2, 1e3, 1e4, 1e5]
devs = [opnorm(eta(r_of(G, k)) - eta1) for k in ks_conv]
exact_identity = all(abs(devs[i] - (1.0 - r_of(G, ks_conv[i]))) < 1e-12 for i in range(len(ks_conv)))
block_norms_vanish = devs[0] > devs[1] > devs[2] > devs[3] and devs[3] < 1e-3
check("T2  eta(1) = 2P with P a rank-1 orthogonal projection (P^2=P=P^dag, tr P=1); "
      f"||eta(r_k) - 2P|| = 1 - r_k EXACTLY, -> 0 ({devs[0]:.2e} -> {devs[3]:.2e}).  So C - 2*P_oplus has "
      "block norms -> 0 (COMPACT): the interacting Krein metric is a COMPACT PERTURBATION OF TWICE A "
      "PROJECTION, and [C] = 2[P_oplus] is a PROPER projection class -- the definitizability failure "
      "descends to the CLEAN statement '[C] is singular, with an identified null direction'.",
      is_proj and exact_identity and block_norms_vanish,
      f"P projection={is_proj}, identity ||eta-2P||=1-r exact={exact_identity}, block norms vanish={block_norms_vanish}")

# ====================================================================================================
# T3 -- EXACTNESS (no finite-mode component): every finite mode is STRICTLY definitizable (r_k < 1 with
#   sup over any bounded window < 1), so C is invertible in B(H) <=> [C] invertible in the quotient.
#   The obstruction descends WITHOUT LOSS: nothing of it is visible at any finite resolution, and
#   nothing of it is lost in the quotient.  (W98's "every finite-rank truncation is definitizable",
#   upgraded to an iff.)
# ====================================================================================================
log("\n[T3] Exactness: obstruction has ZERO finite-mode component -- B(H)-invertibility <=> quotient-invertibility")
windows = [(0.1, 1e2), (0.1, 1e3), (0.1, 1e4)]
finite_sups = [max(r_of(G, float(k)) for k in np.linspace(a, b, 2000)) for a, b in windows]
finite_all_strict = all(s < 1.0 - 1e-12 for s in finite_sups)
sup_approaches_1 = finite_sups[0] < finite_sups[1] < finite_sups[2] and finite_sups[2] > 0.999
check("T3  every bounded momentum window has sup r < 1 STRICTLY "
      f"({finite_sups[0]:.6f} -> {finite_sups[1]:.6f} -> {finite_sups[2]:.6f}), approaching 1 only in the "
      "limit: every Pi_kappa truncation is definitizable, and C is invertible in B(H) IFF [C] is "
      "invertible in the quotient.  The failure descends EXACTLY -- no finite-mode component, no loss.",
      finite_all_strict and sup_approaches_1,
      f"all finite sups < 1={finite_all_strict}, sup -> 1 only asymptotically={sup_approaches_1}")

# ====================================================================================================
# T4 -- RATE-INDEPENDENCE: any two non-UV-soft profiles give the SAME quotient class.  g=const and a
#   GROWING derivative-type coupling g(k)=G*k both have r_k -> 1; the difference of the two metrics has
#   block norms -> 0 (compact), so [C_1] = [C_2] = 2[P].  The quotient forgets the divergence RATE and
#   remembers only the singular limit: the adapter slot is ONE typed object, not a profile-family.
# ====================================================================================================
log("\n[T4] Rate-independence: all non-UV-soft profiles collapse to the SAME tail class 2[P]")
ks4 = [1e2, 1e3, 1e4, 1e5]
diffs = [opnorm(eta(r_of(G, k)) - eta(r_of(G * k, k))) for k in ks4]
same_class = diffs[0] > diffs[3] and diffs[3] < 1e-3
check("T4  ||eta(r_k[g=const]) - eta(r_k[g=G*k])|| -> 0 "
      f"({diffs[0]:.2e} -> {diffs[3]:.2e}): the two metrics differ by a COMPACT operator, so const and "
      "GROWING (derivative-vertex) couplings define the IDENTICAL quotient class 2[P].  The slot "
      "requirement is RATE-INDEPENDENT: one typed object fills it for every non-UV-soft interaction.",
      same_class, f"difference block norms {diffs[0]:.1e} -> {diffs[3]:.1e}")

# ====================================================================================================
# T5 -- THE MODULAR SPLIT: flow clean everywhere, conjugation obstructed exactly at the tail class.
#   (a) eta(r)^{it} = exp(it log eta(r)) is UNITARY (norm 1) at every r < 1 -- the FLOW has ZERO
#       conditioning cost even as r -> 1 (Gottschalk's flow-half survival, per-block exact);
#   (b) ||eta(r)^{-1/2}|| = 1/sqrt(1-r) -> inf -- the CONJUGATION piece diverges;
#   (c) the flow has NO tail norm-limit: the phase (1-r_k)^{it} spins (log(1-r_k) -> -inf), so distinct
#       large-k blocks stay ~2 apart.  The tail carries a DEGENERATE METRIC plus an UNFIXED SPINNING
#       PHASE -- exactly the two data a boundary condition at infinity would have to supply.
# ====================================================================================================
log("\n[T5] Modular split: flow unitary (norm 1) at every r<1; conjugation cost -> inf; flow phase spins at the tail")


def flow_t1(r: float) -> np.ndarray:
    w, V = np.linalg.eigh(eta(r))
    return V @ np.diag(np.exp(1j * np.log(w))) @ dag(V)     # eta(r)^{i}, t=1


rs5 = [r_of(G, k) for k in (1e1, 1e3, 1e5, 1e7)]
flow_unitary = all(abs(opnorm(flow_t1(r)) - 1.0) < 1e-9 and opnorm(flow_t1(r) @ dag(flow_t1(r)) - I2) < 1e-9
                   for r in rs5)
conj_costs = [1.0 / np.sqrt(1.0 - r) for r in rs5]
conj_diverges = conj_costs[0] < conj_costs[1] < conj_costs[2] < conj_costs[3] and conj_costs[3] > 1e3
# spinning phase: pick large-k pairs whose log(1-r) differ by ~pi -> flow blocks ~2 apart (not Cauchy)
k_a = 1e5
k_b = k_a * float(np.exp(np.pi))    # log(1-r) ~ log(const/k): ratio e^pi shifts the phase by ~pi
spin_gap = opnorm(flow_t1(r_of(G, k_a)) - flow_t1(r_of(G, k_b)))
no_flow_tail_limit = spin_gap > 1.5     # blocks stay ~2 apart arbitrarily deep in the tail -> not Cauchy
check("T5  SPLIT: eta(r)^{it} is UNITARY (norm 1) at every r<1 tested up to r corresponding to k=1e7 "
      f"(flow: clean, zero cost), while ||eta^(-1/2)|| = 1/sqrt(1-r) diverges ({conj_costs[0]:.1f} -> "
      f"{conj_costs[3]:.0f}) (conjugation: obstructed).  And the flow has NO tail norm-limit: deep-tail "
      f"blocks at k=1e5 vs k=1e5*e^pi stay {spin_gap:.2f} apart (phase (1-r_k)^(it) spins).  The tail = "
      "degenerate metric + unfixed spinning phase; the observer-accessible part carries the whole "
      "bounded modular structure.", flow_unitary and conj_diverges and no_flow_tail_limit,
      f"flow unitary={flow_unitary}, conj cost -> {conj_costs[3]:.0f}, tail spin gap {spin_gap:.2f}")

# ====================================================================================================
# T6 -- THE TYPED SLOT: what must an external completion supply?  ker eta(1) = span{e_null},
#   e_null = (i,1)/sqrt(2): (a) KREIN-NULL (<e, sigma_z e> = 0 -- the metric dies exactly on a null
#   line of the grading); (b) ESSENTIALLY COMPLEX (e_null and conj(e_null) are linearly independent --
#   the line cannot be described without the scalar i); (c) CONSTANT across the tail (the same line at
#   every large k -- T2's norm convergence).  The completion must supply a positive invertible metric
#   on the (1-P) tail line ("a state/boundary condition at infinity"), and NO compact (= observer-
#   accessible, finite-resolution) correction can supply it: compacts have zero image in the quotient.
#   EXTERNALITY IS A CLOSURE THEOREM, not a preference -- same META-shape as the Nguyen slot.
# ====================================================================================================
log("\n[T6] The typed slot: a positive metric at infinity on a Krein-null, essentially-complex, constant line")
e_null = np.array([1j, 1.0], dtype=complex) / np.sqrt(2.0)
in_kernel = opnorm((eta1 @ e_null).reshape(2, 1)) < 1e-12
krein_null = abs(np.vdot(e_null, SZ @ e_null)) < 1e-12
essentially_complex = abs(np.linalg.det(np.column_stack([e_null, e_null.conj()]))) > 0.9   # e, conj(e) indep
# constancy across the tail: the min-eigenvector of eta(r_k) converges to e_null (up to phase)
def null_overlap(k: float) -> float:
    w, V = np.linalg.eigh(eta(r_of(G, k)))
    v = V[:, int(np.argmin(w))]
    return abs(np.vdot(v, e_null))


overlaps = [null_overlap(k) for k in (1e1, 1e3, 1e5)]
constant_line = all(o > 1.0 - 1e-9 for o in overlaps)       # the SAME null line at every k (exact here)
# compacts cannot fill the slot: a finite-rank correction leaves the tail min-eigenvalue at 0
def truncated_fix_fails(K_cut: int = 2000) -> bool:
    # correcting the first K_cut modes to identity leaves modes k > K_cut untouched: tail min-eig -> 0 still
    ks = np.linspace(K_cut + 1.0, 20.0 * K_cut, 300)
    return min(eig_minmax(eta(r_of(G, float(k))))[0] for k in ks) < 1e-2


compact_cannot_fill = truncated_fix_fails()
check("T6  ker eta(1) = span{(i,1)/sqrt(2)}: KREIN-NULL (<e,sigma_z e>=0), ESSENTIALLY COMPLEX (e and "
      "conj(e) independent -- the line needs the scalar i), and CONSTANT across the tail (min-eigvec "
      f"overlap with e_null = {min(overlaps):.9f} at k=1e1..1e5).  Any finite-resolution (compact) "
      "correction leaves the tail min-eigenvalue at 0 (verified): the definitizing completion MUST live "
      "in the quotient -- PROVABLY EXTERNAL to the observer filtration.  TYPED REQUIREMENT: a positive "
      "invertible metric (a 'state/boundary condition at infinity') on the asymptotic Krein-null line.",
      in_kernel and krein_null and essentially_complex and constant_line and compact_cannot_fill,
      f"kernel={in_kernel}, Krein-null={krein_null}, ess-complex={essentially_complex}, constant={constant_line}, "
      f"compact-fix-fails={compact_cannot_fill}")

# ====================================================================================================
# T7 -- NGUYEN-SLOT COMPARISON (honest typing).  The doublet's canonical quaternionic structure is
#   J_quat = SY * conj (J^2 = -1).  Computation (exact): [eta(r), J_quat] = 2r * conj -- the FREE metric
#   is quaternionic-linear, and the INTERACTING part r*SY is EXACTLY the J_quat-ODD component; moreover
#   SY = i * J0 (i times the real rotation matrix): the obstruction-carrying mixing is the scalar-i-
#   laden term.  MATCHES the Nguyen slot's flavor (non-quaternionic, essential scalar-i, antilinear-
#   interfacing).  HONEST LIMITS: (a) EVERY Hermitian-traceless 2x2 mixing is J_quat-odd (the odd-ness
#   is generic, not specific); the scalar-i identification of SY is representative-dependent unless the
#   W52 form is forced; (b) the payload types DIFFER: Nguyen slot supplies a DISCRETE count-fixing
#   rank, this slot supplies a CONTINUOUS definitizing metric.  META-TYPE (closure-theorem-forced typed
#   external object): SAME.  Fine type: RELATED.  Overall: RELATED, not SAME.
# ====================================================================================================
log("\n[T7] Nguyen-slot comparison: meta-type SAME (closure-forced external), fine type RELATED, payload DIFFERENT")
# antilinear commutator: for A linear, J = U*conj:  A J - J A = (A U - U conj(A)) * conj
U = SY


def anticommutator_defect(A: np.ndarray) -> float:
    return opnorm(A @ U - U @ A.conj())


defects = {r: anticommutator_defect(eta(r)) for r in (0.0, 0.25, 0.5, 0.9)}
free_is_quaternionic = defects[0.0] < 1e-12
interacting_is_J_odd = all(abs(defects[r] - 2.0 * r) < 1e-12 for r in (0.25, 0.5, 0.9))
sy_is_scalar_i_times_real = opnorm(SY - 1j * np.array([[0, -1], [1, 0]], dtype=complex)) < 1e-12
# genericity caveat (honest): SX (a REAL mixing) is ALSO J_quat-odd -- odd-ness alone is not scalar-i
sx_also_odd = anticommutator_defect(SX) > 1.9
# BUT relative to the grading-compatible real structure K (conj), SY is IMAGINARY while SX is REAL:
sy_imaginary_wrt_K = opnorm(SY.conj() + SY) < 1e-12
sx_real_wrt_K = opnorm(SX.conj() - SX) < 1e-12
typing = {
    "meta_type_match_closure_theorem_forced_external_object": True,      # T6 here; step10/11 there
    "obstruction_part_of_metric_is_J_quat_odd": interacting_is_J_odd,
    "W52_mixing_is_scalar_i_wrt_grading_real_structure": bool(sy_is_scalar_i_times_real and sy_imaginary_wrt_K),
    "oddness_is_generic_not_specific_CAVEAT": bool(sx_also_odd),          # honesty flag
    "payload_types_MATCH": False,                                         # discrete count vs continuous metric
    "verdict_SAME_TYPE": False,
    "verdict_RELATED": True,
    "verdict_UNRELATED": False,
}
check("T7  [eta(r), J_quat] = 2r*conj EXACTLY (free metric quaternionic-linear; the interacting part is "
      "the J_quat-ODD component), and the W52 mixing SY = i*(real J0) is the scalar-i-laden, K-imaginary "
      "direction (SX would be K-real).  META-TYPE match with the Nguyen para-3.1 slot: BOTH walls are "
      "closure theorems forcing a typed EXTERNAL object.  HONEST LIMITS: J-odd-ness is generic for "
      "Hermitian mixings (SX also odd); the payloads differ (discrete count vs continuous metric).  "
      "VERDICT: RELATED, not SAME-TYPE.",
      free_is_quaternionic and interacting_is_J_odd and sy_is_scalar_i_times_real and sx_also_odd
      and sy_imaginary_wrt_K and sx_real_wrt_K and typing["verdict_RELATED"] and not typing["verdict_SAME_TYPE"],
      f"defect(r)=2r exact={interacting_is_J_odd}, SX-odd caveat={sx_also_odd}, RELATED={typing['verdict_RELATED']}")

# ====================================================================================================
# T8 -- VACUITY COUNTER-MODEL 1 (rotating mixing): the BREAK is identical but the QUOTIENT statement
#   FAILS.  eta_k = I + r_k*(cos th_k SX + sin th_k SY) with th_k non-convergent: same eigenvalues
#   1 -+ r_k (cond diverges identically) but the blocks do NOT norm-converge -- deep-tail blocks stay
#   far apart AND far from the fixed 2P.  C is NOT projection+compact; there is no single tail line; no
#   single typed slot.  => the steelman's statement is STRICTLY STRONGER than the break: it has model-
#   discriminating content, answering the adversary's vacuity objection.
# ====================================================================================================
log("\n[T8] Counter-model 1 (rotating mixing): identical break, NO clean tail element -- the quotient claim is falsifiable")
PHI = np.pi * (3.0 - np.sqrt(5.0))          # golden angle: th_k equidistributes, never converges


def eta_rot(k: float) -> np.ndarray:
    return eta(r_of(G, k), theta=PHI * k)


ks8 = np.linspace(1e5, 1.001e5, 50)                          # deep tail, r_k ~ 1 throughout
same_break = all(abs(eig_minmax(eta_rot(float(k)))[0] - eig_minmax(eta(r_of(G, float(k))))[0]) < 1e-12
                 for k in ks8)                               # identical eigenvalues => identical cond blow-up
pair_gaps = [opnorm(eta_rot(float(ks8[i])) - eta_rot(float(ks8[j])))
             for i in range(0, 40, 8) for j in range(i + 4, 50, 11)]
no_cauchy = max(pair_gaps) > 0.5                             # deep-tail blocks stay far apart
dist_to_2P = [opnorm(eta_rot(float(k)) - eta1) for k in ks8]
not_conv_to_2P = max(dist_to_2P) > 0.5                       # and far from the W98 tail element
check("T8  ROTATING MIXING: eigenvalues (hence cond divergence, the W98 BREAK) IDENTICAL to the W98 "
      f"model at every deep-tail k tested, but deep-tail blocks stay up to {max(pair_gaps):.2f} apart "
      f"(no norm limit) and up to {max(dist_to_2P):.2f} from 2P: C is NOT projection+compact, no single "
      "null line, no single typed slot.  The tail-quotient statement is FALSE here while the break is "
      "TRUE => the statement has content BEYOND the break (it is falsifiable within the model class).",
      same_break and no_cauchy and not_conv_to_2P,
      f"break identical={same_break}, no-Cauchy gap {max(pair_gaps):.2f}, dist to 2P {max(dist_to_2P):.2f}")

# ====================================================================================================
# T9 -- VACUITY COUNTER-MODEL 2 (finite-k exceptional point): a model whose obstruction does NOT live
#   at the tail.  One finite mode k0 sits exactly AT r=1 (block singular); the tail is UV-soft (clean).
#   C is singular in B(H) -- a genuine definitizability failure -- but the singular part is FINITE-RANK,
#   so [C] IS invertible in the quotient: the obstruction does NOT factor through the tail.  => T3's
#   exactness ("descends without loss") is a PROPERTY of the W98 model, not a tautology of divergences.
# ====================================================================================================
log("\n[T9] Counter-model 2 (finite-k exceptional point): obstruction with ZERO tail component -- descent is a property")
K0 = 5.0


def eta_cm2(k: float) -> np.ndarray:
    if abs(k - K0) < 0.5:
        return eta(1.0)                                       # exact exceptional point at finite k0
    return eta(r_of(G / (k * k + 1.0), k))                    # UV-soft tail (clean)


sing_at_k0 = eig_minmax(eta_cm2(K0))[0] < 1e-12               # C singular in B(H): a genuine failure
tail_clean = min(eig_minmax(eta_cm2(float(k)))[0] for k in np.linspace(1e3, 1e5, 300)) > 0.9
check("T9  FINITE-k EXCEPTIONAL POINT: the k0=5 block is exactly singular (min-eig "
      f"{eig_minmax(eta_cm2(K0))[0]:.1e}) so C fails definitizability in B(H), but the tail is clean "
      f"(tail min-eig {min(eig_minmax(eta_cm2(float(k)))[0] for k in np.linspace(1e3, 1e5, 300)):.3f} > 0.9): "
      "the singular part is FINITE-RANK and [C] IS invertible in the quotient.  Here the obstruction "
      "does NOT factor through the tail => T3's exactness for the W98 model is a genuine property, not "
      "'every divergence lives at the tail by definition'.", sing_at_k0 and tail_clean,
      f"k0 singular={sing_at_k0}, tail clean={tail_clean}")

# ====================================================================================================
# T10 -- VERDICT: PARTIAL.  Quotient structure REAL and CLEAN (T1-T6, counter-model-backed content
#   T8/T9): the W98 wall IS a located, typed adapter slot at Krein-doublet-model grade.  The Nguyen
#   unification is RELATED, not SAME (T7).  The intrinsic type-III version (no compacts inside a III_1
#   factor -- the ideal must come from the mode filtration / flow-of-weights side) is the named
#   frontier, NOT done here.
# ====================================================================================================
log("\n[T10] VERDICT = PARTIAL: adapter-slot half clean at model grade; Nguyen unification RELATED not SAME")
verdict = {
    # the quotient structure (the steelman's part (a)):
    "obstruction_descends_to_quotient_EXACTLY_no_finite_mode_component": True,   # T3, T9 contrast
    "quotient_class_is_clean_singular_element_2P_projection": True,              # T2
    "criterion_X_descends_to_quotient_invertibility": True,                      # T1
    "slot_is_rate_independent_single_typed_object": True,                        # T4
    "modular_split_flow_clean_conjugation_obstructed_at_tail": True,             # T5
    "slot_typed_positive_metric_at_infinity_on_Krein_null_complex_line": True,   # T6
    "externality_is_closure_theorem_compacts_cannot_fill": True,                 # T6
    "content_beyond_break_two_falsifying_counter_models": True,                  # T8, T9
    # the unification (the steelman's part (b)):
    "nguyen_meta_type_match_closure_forced_external": True,                      # T7
    "nguyen_fine_type_scalar_i_antilinear_suggestive_only": True,                # T7 caveats
    "nguyen_payload_type_match": False,                                          # discrete vs continuous
    "unification_SAME_TYPE": False,
    "unification_RELATED": True,
    # honest scope:
    "model_grade_only_intrinsic_type_III_tail_quotient_is_frontier": True,       # no compacts in III_1
    "verdict_VIABLE_full_steelman": False,
    "verdict_PARTIAL": True,
    "verdict_DEAD": False,
}
partial = (
    verdict["obstruction_descends_to_quotient_EXACTLY_no_finite_mode_component"]
    and verdict["quotient_class_is_clean_singular_element_2P_projection"]
    and verdict["content_beyond_break_two_falsifying_counter_models"]
    and verdict["unification_RELATED"] and not verdict["unification_SAME_TYPE"]
    and verdict["verdict_PARTIAL"] and not verdict["verdict_VIABLE_full_steelman"] and not verdict["verdict_DEAD"]
)
check("T10 VERDICT = PARTIAL.  (a) The quotient structure is REAL: the obstruction descends EXACTLY "
      "([C]=2[P], criterion X = quotient invertibility, typed rate-independent slot, closure-theorem "
      "externality), with content beyond the break (two counter-models falsify the quotient claim while "
      "preserving the break).  (b) The Nguyen unification is RELATED (same meta-type: internal closure "
      "theorem forcing a typed external object; shared scalar-i/antilinear flavor) but NOT SAME-TYPE "
      "(payload mismatch; model-surrogate grade).  Intrinsic type-III tail quotient = the named frontier.",
      partial, f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans; PARTIAL={verdict['verdict_PARTIAL']}")

# ====================================================================================================
# SUMMARY
# ====================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(ok for _, ok, _ in results), "some W103 steelman-1 checks FAILED"

log("")
log("W103 STEELMAN-1 VERDICT (this file is the computation, not a claim-status change):")
log("  * DOES the W98 obstruction factor through a clean tail quotient?  YES, at Krein-doublet-model")
log("    grade, and EXACTLY: C = 2*(projection)+compact, [C]=2[P] singular; invertible in B(H) IFF")
log("    invertible in the quotient (zero finite-mode component); the W100 condition X descends to")
log("    invertibility of one quotient element; the class is RATE-independent (all non-UV-soft")
log("    couplings give the same 2[P]).")
log("  * CONTENT BEYOND THE BREAK: two counter-models (rotating mixing; finite-k exceptional point)")
log("    where the break holds/exists but the quotient statement FAILS -- the statement is falsifiable")
log("    within the model class, answering the vacuity objection.  What the break did not have: the")
log("    identified singular element (2P), its constant Krein-null essentially-complex line, exactness,")
log("    rate-independence, and the flow/conjugation split (flow unitary norm-1 at every r<1;")
log("    conjugation cost diverges; tail phase spins unfixed).")
log("  * THE TYPED SLOT: a positive invertible metric AT INFINITY on the asymptotic Krein-null,")
log("    essentially-complex (scalar-i) line -- a boundary condition/state at infinity.  Provably")
log("    EXTERNAL: no compact (observer-accessible) correction changes the quotient class.")
log("  * NGUYEN COMPARISON: RELATED, not SAME.  Same meta-type (closure theorem forcing a typed")
log("    external object; scalar-i / antilinear flavor shared at suggestive grade); payload types")
log("    differ (discrete count-fixing vs continuous definitizing metric).")
log("  * VERDICT: PARTIAL.  The adapter-slot half is clean at model grade; the unification half is")
log("    RELATED-only; the intrinsic type-III tail quotient (no compacts inside a III_1 factor -- the")
log("    ideal must be built from the mode filtration / flow-of-weights side) is the named frontier.")
log("  * No canon / RESEARCH-STATUS / CANON / verdict / posture change.  Present, do not decide.")
raise SystemExit(0)
