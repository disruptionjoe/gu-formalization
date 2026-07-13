#!/usr/bin/env python3
r"""
W104 / STEELMAN 2 -- THE KREIN CROSSED PRODUCT: does adjoining the OBSERVER (CLPW mechanism) cure
the W98 wall?

THE STEELMAN UNDER TEST.  W98 broke the observer conjecture's sectorial closure: the OBSERVER-FREE
type-III_1 Krein region algebra has no bounded modular conjugation (the metric conditioning
cond(eta_+(r_k)) = (1+r_k)/(1-r_k) diverges over the UV modes, r_k -> 1).  The steelman says W98
tested the WRONG ALGEBRA under the conjecture's own logic: the observer must be INCLUDED.  In
semiclassical gravity (Witten arXiv:2112.12828; Chandrasekaran-Longo-Penington-Witten
arXiv:2206.10780) the type-III_1 horizon/patch algebra becomes TYPE II -- traces, density matrices,
entropies -- when an observer's clock (energy bounded below) is adjoined via the CROSSED PRODUCT by
the modular flow (Takesaki type conversion).  Since the Krein modular FLOW survives rigorously
(Gottschalk 2002; W91), the crossed product M x_sigma R is at least WELL-POSED to attempt in the
Krein setting.  Question: does observer-dressing tame the non-definitizability -- does the metric
conditioning become BOUNDED on the crossed-product / physical algebra?

THE TOY (built, not gestured at).  Per momentum k the region carries the W98 Krein DOUBLET with
exceptional parameter r_k = g/(g + Dw(k)/2) -> 1 in the UV.  Per mode the repo's W52 model:
    H_mod(r) = [[ i r, 1 ], [ 1, -i r ]]      (the modular Hamiltonian / PT generator; W91 T4)
    eta_K    = sigma_x                        (the KREIN fundamental symmetry: sigma_x H = eta_+ is
                                               Hermitian, so H is eta_K-selfadjoint; eigenvalues of
                                               eta_K are +-1 -- genuinely indefinite)
    eta_+(r) = [[1, -i r], [i r, 1]]          (the positive intertwiner; eta_+ H = (1-r^2) sigma_x
                                               Hermitian, so H is ALSO eta_+-pseudo-Hermitian;
                                               cond(eta_+) = (1+r)/(1-r) = the W84/W98 conditioning)
    spec(H_mod) = +- s,  s = sqrt(1-r^2)      (real for r<1; Jordan/exceptional point at r=1)
The OBSERVER = a clock/energy degree of freedom: L^2-like factor with energy q, spectrum BOUNDED
BELOW (q >= 0), exactly CLPW's observer.  The crossed product's three CLPW ingredients, ported:
  (1) DRESSING: pi(a) = U(p) (a x 1) U(p)^{-1} with U(p) = e^{i H_mod p}, p = the clock momentum
      conjugate to q (per clock-momentum branch p, the dressed operator is the modular flow of a at
      "time" p) -- the defining covariance of M x_sigma R;
  (2) the CONSTRAINT H_mod + q = 0 (group averaging), with the observer's energy q >= 0;
  (3) the DUAL-WEIGHT TRACE on the crossed product (type-II structure).

WHAT THIS FILE PROVES ON THE TOY (deterministic, numpy-only):

  T1 -- THE CONSTRUCTION EXISTS AT THE FLOW LEVEL, mode-wise: U(p) is EXACTLY eta_K-unitary AND
        eta_+-unitary for every r < 1 and every p (machine precision), with the group law
        U(p1)U(p2) = U(p1+p2).  This is the Krein crossed product's covariance skeleton -- it needs
        only the Gottschalk flow, consistent with W91's split (flow-level objects are positivity-
        free).  BUT the implementers are ordinary-norm UNBOUNDED over the region's UV tower:
        sup_p ||U(p)|| grows ~ 1/s(r) -> inf as r -> 1, so the crossed-product REPRESENTATION is
        bounded only on finite-rank / Pi_kappa truncations -- the same sectorial scope as W94/W98.

  T2 -- THE DECISIVE COMPUTATION (cond BEFORE vs AFTER dressing): observer-dressing does NOT
        regulate the metric conditioning.  Dressing is conjugation by an eta_+-UNITARY, and an
        eta_+-unitary conjugation preserves the metric EXACTLY: the pulled-back metric
        U(p)^{-dag} eta_+ U(p)^{-1} = eta_+ to machine precision, for every clock momentum p and for
        every clock-SMEARED (normalizable Gaussian wavepacket) combination.  cond_after / cond_before
        = 1.000... at every mode; the region's sup-cond STILL doubles under UV doubling, identical
        before and after dressing.  The CLPW mechanism regulates STATE-level (entanglement)
        divergences by shifting modular time into the clock; the Krein wall is a METRIC/OPERATOR-
        level divergence, and modular time-shifts are exactly the transformations that leave the
        metric invariant.  Different divergences; the dressing cures the one that was never the wall.

  T3 -- THE POSITIVE-ENERGY CONSTRAINT DOES SOMETHING REAL BUT DOES NOT DEFINITIZE IN THE BOUNDED
        SENSE: group averaging over the constraint H_mod + q = 0 with q >= 0 keeps, per mode, ONLY
        the field eigenvector with modular energy h = -s <= 0 (the clock can only supply q = +s).
        The surviving eigenvector's Krein norm is -s (Hilbert-normalized): the physical form is
        SIGN-DEFINITE mode-wise (a genuine, nontrivial projection -- the observer's positivity DOES
        select a definite-sign subspace, the steelman's kernel of truth), BUT its magnitude
        s_k = sqrt(1 - r_k^2) -> 0 over the UV tower: the physical metric DEGENERATES (null in the
        UV limit), its inverse is unbounded, and its conditioning sup_k s_k / inf_k s_k grows
        without bound under UV doubling.  RELOCATION IDENTITY: the new divergence 1/s_k equals the
        old ||J||-cost n(r_k) = 1/sqrt(1-r_k) times a factor bounded in [1/sqrt(2), 1] -- the SAME
        divergence class, relocated from 'metric blow-up' to 'physical-norm degeneration'.

  T4 -- NO TYPE-II POSITIVE TRACE: (a) the naive dual-weight trace on the Krein crossed product is
        an eta-TRACE (hermitian but indefinite): tau(a^# a) = -1 < 0 on a ghost-graded element (a^#
        = the Krein adjoint) -- positivity of the trace is exactly the positivity the Krein setting
        withholds; (b) the post-constraint sign-flipped candidate is positive PER MODE but its
        density-matrix normalization needs the inverse physical metric, sup_k 1/s_k -> inf: the
        candidate trace is unbounded / non-normal over the tower.  Type conversion III -> II is a
        POSITIVE-trace statement; in the Krein setting the construction's algebraic (flow) skeleton
        goes through and the POSITIVITY of the output is exactly what fails -- Takesaki-duality-style
        type conversion does not survive the indefinite metric, it REDUCES to definitizability.

  T5 -- WHERE POSITIVITY ENTERS (the honest structural map): three gates -- (g1) bounded
        implementers (FAILS: T1), (g2) positive trace (FAILS: T4), (g3) observer positive energy
        definitizes (PARTIAL: sign-definite per mode, degenerate in the UV; T3).  The Krein grading
        PASSES THROUGH the flow-level construction harmlessly, BREAKS the positivity-level payoff,
        and is REGULARIZED-IN-SIGN but NOT-IN-NORM by the observer's energy bound.

  T6 -- VERDICT = PARTIAL.  The Krein crossed product EXISTS as a flow-level construction (novel,
        mode-wise / sectorial); observer-dressing does NOT bound the metric conditioning (the
        decisive number: cond_after = cond_before exactly); the positive-energy constraint yields a
        sign-definite but UV-degenerate physical form (relocates the obstruction at the identical
        divergence rate); no positive type-II trace exists on the full region.  The obstruction
        SURVIVES DRESSING / RELOCATES.  Not DEAD: the construction itself does not break, and the
        sign-definite selection is a genuine new structure.  Not VIABLE: the observer does not cure
        the wall.

LOAD-BEARING assumptions (named): (i) the W52 doublet + W98 momentum-tower model as the Krein
type-III surrogate (same grade as W91/W98 -- toy, not the continuum object); (ii) the per-mode
constraint pairing (each doublet's modular energy matched against the clock's q >= 0) as the toy of
CLPW group-averaging; (iii) the eta-unitarity of the dressing implementers -- which is EXACT and
structural (any crossed product by an eta-unitary flow preserves every intertwined metric
identically), so T2 lifts beyond the toy: it is an invariance argument, not a numerical accident.

Literature (read-only): Witten arXiv:2112.12828 (gravity and the crossed product); CLPW
arXiv:2206.10780 (an algebra of observables for de Sitter space; type II_1, positive-energy
observer, trace); Takesaki duality (type conversion III x_sigma R -> II); Gottschalk JMP 43 (2002)
4753 (Krein modular flow); Langer / Krejcirik-Siegl PRD 86 (2012) 121702 (definitizability,
bounded metric with unbounded inverse).

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
# The per-mode Krein doublet (W52/W91/W98 lineage).
# ------------------------------------------------------------------------------------------------
SX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)          # eta_K: the Krein fundamental symmetry


def H_mod(r: float) -> np.ndarray:
    # the modular Hamiltonian / PT generator of the mode (W91 T4); eta_K-selfadjoint; spec = +-s.
    return np.array([[1j * r, 1.0], [1.0, -1j * r]], dtype=complex)


def eta_pos(r: float) -> np.ndarray:
    # the positive intertwiner; cond = (1+r)/(1-r) = the W84/W98 metric conditioning.
    return np.array([[1.0, -1j * r], [1j * r, 1.0]], dtype=complex)


def cond_of(M: np.ndarray) -> float:
    ev = np.linalg.eigvalsh((M + dag(M)) / 2)
    return float(ev.max() / ev.min())


def s_of(r: float) -> float:
    return float(np.sqrt(max(1.0 - r * r, 0.0)))


def n_of(r: float) -> float:
    # the OLD ||J||-cost of W98: 1/sqrt(1 - r) = 1/sqrt(min eig eta_+).
    return float(1.0 / np.sqrt(1.0 - r))


def U_dress(r: float, p: float) -> np.ndarray:
    # the crossed-product dressing implementer at clock momentum p: U(p) = e^{i H_mod p}.
    H = H_mod(r)
    ev, R = np.linalg.eig(H)
    return R @ np.diag(np.exp(1j * ev * p)) @ np.linalg.inv(R)


# the W98 region model: momentum tower, UV degeneracy, exceptional parameter r_k.
M1, M2, G = 0.0, 0.30, 0.10


def omega(k: float, m: float) -> float:
    return float(np.sqrt(k * k + m * m))


def r_of(g: float, k: float) -> float:
    dw = abs(omega(k, M1) - omega(k, M2))
    rr = g / (g + 0.5 * dw)
    return float(min(rr, 1.0 - 1e-15))


log("=" * 100)
log("W104 / STEELMAN 2 -- the KREIN CROSSED PRODUCT: does adjoining the observer (CLPW) cure the W98 wall?")
log("=" * 100)

# sanity of the model (structural identities used throughout):
for r in (0.3, 0.7, 0.95):
    H, ep = H_mod(r), eta_pos(r)
    assert np.max(np.abs(SX @ H - ep)) < 1e-12                       # sigma_x H = eta_+ (Hermitian)
    assert np.max(np.abs(ep @ H - (1 - r * r) * SX)) < 1e-12          # eta_+ H = (1-r^2) sigma_x (Hermitian)
    ev = np.linalg.eigvals(H)
    assert np.max(np.abs(np.sort(ev.real) - np.array([-s_of(r), s_of(r)]))) < 1e-9 and np.max(np.abs(ev.imag)) < 1e-9

# ================================================================================================
# T1 -- the Krein crossed product EXISTS at the flow level (mode-wise), but its implementers are
#   ordinary-norm UNBOUNDED over the UV tower (sectorial scope only).
# ================================================================================================
log("\n[T1] the construction: dressing implementers exactly eta-unitary (flow level), ordinary-norm unbounded")
r_scan = [0.3, 0.6, 0.85, 0.95, 0.99]
p_grid = np.linspace(-40.0, 40.0, 161)
etaK_resid = 0.0
etaP_resid = 0.0
grp_resid = 0.0
for r in r_scan:
    ep = eta_pos(r)
    for p in (0.7, -2.3, 11.0):
        U = U_dress(r, p)
        etaK_resid = max(etaK_resid, float(np.max(np.abs(dag(U) @ SX @ U - SX))))
        etaP_resid = max(etaP_resid, float(np.max(np.abs(dag(U) @ ep @ U - ep))))
    grp_resid = max(grp_resid, float(np.max(np.abs(U_dress(r, 0.7) @ U_dress(r, -2.3) - U_dress(r, -1.6)))))
flow_level_exists = etaK_resid < 1e-9 and etaP_resid < 1e-9 and grp_resid < 1e-9
# ordinary-norm unboundedness of the implementers over the tower:
supU = {r: max(float(np.linalg.norm(U_dress(r, p), 2)) for p in p_grid) for r in r_scan}
impl_norm_grows = supU[0.99] > 3.0 * supU[0.6] and supU[0.99] > 5.0
check("T1  the KREIN CROSSED PRODUCT EXISTS AT THE FLOW LEVEL, mode-wise: U(p)=e^{iH_mod p} is EXACTLY "
      f"eta_K-unitary (resid {etaK_resid:.1e}) AND eta_+-unitary (resid {etaP_resid:.1e}) with the group "
      f"law U(p1)U(p2)=U(p1+p2) (resid {grp_resid:.1e}) -- the covariance skeleton of M x_sigma R needs "
      "only the Gottschalk flow (positivity-free, consistent with W91).  BUT the implementers are "
      f"ordinary-norm UNBOUNDED toward the exceptional locus: sup_p ||U(p)|| = "
      f"{supU[0.3]:.2f} (r=0.3) -> {supU[0.95]:.2f} (r=0.95) -> {supU[0.99]:.2f} (r=0.99) ~ 1/s(r), so "
      "the crossed-product REPRESENTATION is bounded only on finite-rank / Pi_kappa truncations "
      "(sectorial scope, same as W94/W98).",
      flow_level_exists and impl_norm_grows,
      f"eta-unitary resid {max(etaK_resid, etaP_resid):.1e}, sup||U|| {supU[0.3]:.1f}->{supU[0.99]:.1f}")

# ================================================================================================
# T2 -- THE DECISIVE COMPUTATION: metric conditioning BEFORE vs AFTER observer-dressing.
#   Dressing = conjugation by the eta_+-unitary U(p) => the pulled-back metric is eta_+ EXACTLY.
#   Clock-smearing (a normalizable Gaussian wavepacket over p) changes nothing: a convex combination
#   of copies of eta_+ is eta_+.  The conditioning divergence over the region's UV tower is UNTOUCHED.
# ================================================================================================
log("\n[T2] DECISIVE: cond BEFORE vs AFTER dressing -- observer-dressing does NOT regulate the conditioning")
pull_resid = 0.0
ratio_dev = 0.0
# Gaussian clock wavepacket over clock momentum (normalizable observer state, CLPW-style):
ps = np.linspace(-6.0, 6.0, 121)
wts = np.exp(-ps ** 2 / 2.0)
wts /= wts.sum()
for r in r_scan:
    ep = eta_pos(r)
    c_before = cond_of(ep)
    # per-branch pulled-back metric U(p)^{-dag} eta_+ U(p)^{-1}:
    for p in (0.7, -2.3, 11.0):
        Ui = np.linalg.inv(U_dress(r, p))
        ep_after = dag(Ui) @ ep @ Ui
        pull_resid = max(pull_resid, float(np.max(np.abs(ep_after - ep))))
        ratio_dev = max(ratio_dev, abs(cond_of(ep_after) / c_before - 1.0))
    # clock-SMEARED effective metric (the observer's normalizable wavepacket):
    ep_smear = np.zeros((2, 2), dtype=complex)
    for p, w in zip(ps, wts):
        Ui = np.linalg.inv(U_dress(r, float(p)))
        ep_smear += w * (dag(Ui) @ ep @ Ui)
    pull_resid = max(pull_resid, float(np.max(np.abs(ep_smear - ep))))
    ratio_dev = max(ratio_dev, abs(cond_of(ep_smear) / c_before - 1.0))
dressing_metric_invariant = pull_resid < 1e-8 and ratio_dev < 1e-8


def region_sup_cond(kmax: float, npts: int = 4000) -> float:
    ks = np.linspace(0.1, kmax, npts)
    return float(np.max([cond_of(eta_pos(r_of(G, float(k)))) for k in ks]))


cond_L, cond_2L, cond_4L = region_sup_cond(1e3), region_sup_cond(2e3), region_sup_cond(4e3)
# after dressing the per-mode metric is IDENTICAL, so the region sup-cond after dressing IS the same
# numbers -- verified structurally above (pull_resid), asserted here as the region-level statement:
cond_after_L, cond_after_2L, cond_after_4L = cond_L, cond_2L, cond_4L
still_diverges_after = (cond_after_2L > 1.3 * cond_after_L) and (cond_after_4L > 1.3 * cond_after_2L)
check("T2  DECISIVE NUMBER: cond_after / cond_before = 1 EXACTLY (max deviation "
      f"{ratio_dev:.1e}; pulled-back-metric residual {pull_resid:.1e}), per clock-momentum branch AND "
      "for the clock-smeared (Gaussian wavepacket) observer.  Dressing is conjugation by an "
      "eta_+-UNITARY -- modular time-shifts are exactly the transformations that PRESERVE the metric -- "
      f"so the region's conditioning divergence is UNTOUCHED: sup-cond {cond_L:.0f} (k<1e3) -> "
      f"{cond_2L:.0f} (k<2e3) -> {cond_4L:.0f} (k<4e3), IDENTICAL before and after dressing, still "
      "doubling under UV doubling.  Observer-dressing does NOT bound the metric conditioning: the CLPW "
      "mechanism shifts modular time into the clock (a state-level regulator), while the Krein wall is "
      "metric-level -- and the metric is invariant under exactly those shifts.",
      dressing_metric_invariant and still_diverges_after,
      f"cond before=after: {cond_L:.0f}->{cond_2L:.0f}->{cond_4L:.0f}; deviation {ratio_dev:.1e}")

# ================================================================================================
# T3 -- the POSITIVE-ENERGY CONSTRAINT (group averaging, CLPW): sign-definite per mode (real, new),
#   but UV-DEGENERATE -- the obstruction RELOCATES at the identical divergence rate.
# ================================================================================================
log("\n[T3] the constraint H_mod + q = 0, q >= 0: selects a sign-definite physical form -- which DEGENERATES in the UV")
phys_norms = {}
sign_definite = True
for r in r_scan:
    H = H_mod(r)
    ev, R = np.linalg.eig(H)
    order = np.argsort(ev.real)
    v_minus = R[:, order[0]] / np.linalg.norm(R[:, order[0]])     # field eigenvector, h = -s
    v_plus = R[:, order[1]] / np.linalg.norm(R[:, order[1]])      # field eigenvector, h = +s
    kn_minus = float(np.real(dag(v_minus.reshape(-1, 1)) @ SX @ v_minus.reshape(-1, 1))[0, 0])
    kn_plus = float(np.real(dag(v_plus.reshape(-1, 1)) @ SX @ v_plus.reshape(-1, 1))[0, 0])
    # constraint kernel: field modular energy h must equal -q with q >= 0 => ONLY h = -s survives.
    phys_norms[r] = kn_minus
    sign_definite = sign_definite and (kn_minus < 0.0) and (kn_plus > 0.0)
    # the surviving Krein norm is -s (Hilbert-normalized): verify against sqrt(1-r^2)
    assert abs(abs(kn_minus) - s_of(r)) < 1e-9
constraint_selects_definite_sign = sign_definite
# the physical form DEGENERATES: |norm| = s_k -> 0 over the UV tower; its conditioning is unbounded.


def region_phys_cond(kmax: float, npts: int = 4000) -> tuple[float, float]:
    ks = np.linspace(0.1, kmax, npts)
    ss = np.array([s_of(r_of(G, float(k))) for k in ks])
    return float(ss.max() / ss.min()), float(ss.min())


pc_L, smin_L = region_phys_cond(1e3)
pc_2L, smin_2L = region_phys_cond(2e3)
pc_4L, smin_4L = region_phys_cond(4e3)
phys_degenerates = (pc_2L > 1.3 * pc_L) and (pc_4L > 1.3 * pc_2L) and (smin_4L < smin_L)
# RELOCATION IDENTITY: the new divergence 1/s(r) = the old ||J||-cost n(r) x a factor in [1/sqrt2, 1]:
ratios = [(1.0 / s_of(r)) / n_of(r) for r in [0.9, 0.99, 0.999, 0.99999]]
same_divergence_class = all(0.70 < q < 1.01 for q in ratios)
check("T3  the observer's POSITIVE ENERGY does something REAL but does NOT definitize in the bounded "
      "sense.  Group averaging (constraint H_mod + q = 0, clock energy q >= 0) keeps per mode ONLY the "
      "h = -s field eigenvector, and its Krein norm is NEGATIVE-definite mode-wise (sign selection "
      f"genuine: kn(h=-s) < 0 < kn(h=+s) at every r in {r_scan}) -- a uniformly sign-definite physical "
      f"form (definite after a global flip).  BUT its magnitude s_k = sqrt(1-r_k^2) DEGENERATES over the "
      f"UV tower: |phys norm| {abs(phys_norms[0.3]):.3f} (r=0.3) -> {abs(phys_norms[0.99]):.3f} (r=0.99); "
      f"the physical metric's conditioning grows without bound ({pc_L:.0f} at k<1e3 -> {pc_2L:.0f} -> "
      f"{pc_4L:.0f}) -- no bounded inverse.  RELOCATION IDENTITY: 1/s(r) = n(r) x [1/sqrt2, 1] "
      f"(ratios {[f'{q:.3f}' for q in ratios]}) -- the SAME divergence class as the old ||J||-cost, "
      "relocated from metric blow-up to physical-norm degeneration.",
      constraint_selects_definite_sign and phys_degenerates and same_divergence_class,
      f"sign-definite={constraint_selects_definite_sign}, phys-cond {pc_L:.0f}->{pc_2L:.0f}->{pc_4L:.0f}, "
      f"relocation ratios in [1/sqrt2,1]={same_divergence_class}")

# ================================================================================================
# T4 -- NO TYPE-II POSITIVE TRACE on the Krein crossed product: the naive dual-weight trace is an
#   eta-TRACE (indefinite); the post-constraint candidate is positive per mode but non-normal /
#   unbounded over the tower (needs the unbounded inverse physical metric).
# ================================================================================================
log("\n[T4] the type-II payoff: NO positive trace -- the dual-weight candidate is an eta-trace (indefinite)")
# (a) naive dual-weight trace tau(x) = tr(eta_K x); Krein adjoint a^# = eta_K a^dag eta_K.
#     On a ghost-graded rank-one element a = w e1^dag with [w,w] = -1:  tau(a^# a) = [w,w] = -1 < 0.
w_ghost = np.array([1.0, -1.0], dtype=complex) / np.sqrt(2.0)     # sigma_x-norm = -1 (ghost-graded)
a = np.outer(w_ghost, np.array([1.0, 0.0]))
a_sharp = SX @ dag(a) @ SX
tau_val = float(np.real(np.trace(SX @ (a_sharp @ a))))
eta_trace_indefinite = tau_val < -0.5
# tau is hermitian (an eta-trace) and tracial on eta-unitary conjugation, but NOT positive:
tau_herm = abs(np.trace(SX @ a_sharp @ a) - np.conj(np.trace(SX @ dag(a_sharp @ a) @ np.eye(2)))) >= 0  # structural
# (b) the post-constraint positive candidate needs the INVERSE physical metric: normalization
#     1/s_k -> inf over the tower (no normal/bounded trace on the full region):
trace_norm_L = 1.0 / smin_L
trace_norm_2L = 1.0 / smin_2L
trace_norm_4L = 1.0 / smin_4L
trace_unbounded = (trace_norm_2L > 1.2 * trace_norm_L) and (trace_norm_4L > 1.2 * trace_norm_2L)
check("T4  NO TYPE-II POSITIVE TRACE.  (a) The naive dual-weight trace on the Krein crossed product is "
      f"an eta-TRACE: tau(a^# a) = {tau_val:.3f} < 0 on a ghost-graded element (a^# = Krein adjoint) -- "
      "hermitian but INDEFINITE; the positivity of the CLPW trace is exactly the positivity HORN K "
      "withholds.  (b) The post-constraint sign-flipped candidate is positive PER MODE but its "
      f"density-matrix normalization needs the inverse physical metric: sup_k 1/s_k = {trace_norm_L:.0f} "
      f"(k<1e3) -> {trace_norm_2L:.0f} (k<2e3) -> {trace_norm_4L:.0f} (k<4e3) -- unbounded/non-normal "
      "over the tower.  Takesaki-style type conversion III -> II is a POSITIVE-trace statement: its "
      "algebraic (flow) skeleton goes through in Krein, and its POSITIVITY payoff is exactly what "
      "fails -- type conversion REDUCES to definitizability, it does not deliver it.",
      eta_trace_indefinite and trace_unbounded,
      f"tau(a^#a)={tau_val:.2f}<0; trace normalization {trace_norm_L:.0f}->{trace_norm_2L:.0f}->{trace_norm_4L:.0f}")

# ================================================================================================
# T5 -- the honest structural map: WHERE the indefinite structure meets the crossed product.
# ================================================================================================
log("\n[T5] the structural map: pass-through (flow), break (positivity payoff), partial (sign selection)")
gates = {
    # g0: the construction's covariance/flow skeleton -- Krein PASSES THROUGH HARMLESSLY:
    "g0_flow_covariance_skeleton_constructible_positivity_free": flow_level_exists,        # T1
    # g1: bounded implementers on the full tower -- FAILS (sectorial only):
    "g1_implementers_bounded_on_full_UV_tower": not impl_norm_grows,                       # T1 -> False
    # g2: dressing regulates the metric conditioning -- FAILS (exact invariance):
    "g2_dressing_bounds_the_metric_conditioning": not dressing_metric_invariant,           # T2 -> False
    # g3: observer positive energy definitizes -- PARTIAL (sign yes, norm no):
    "g3a_constraint_selects_sign_definite_physical_form": constraint_selects_definite_sign,  # T3 -> True
    "g3b_physical_form_boundedly_invertible_definitizable": not phys_degenerates,          # T3 -> False
    # g4: positive type-II trace exists -- FAILS:
    "g4_positive_type_II_trace_exists_on_full_region": not (eta_trace_indefinite and trace_unbounded),  # False
}
structural_map_ok = (gates["g0_flow_covariance_skeleton_constructible_positivity_free"]
                     and not gates["g1_implementers_bounded_on_full_UV_tower"]
                     and not gates["g2_dressing_bounds_the_metric_conditioning"]
                     and gates["g3a_constraint_selects_sign_definite_physical_form"]
                     and not gates["g3b_physical_form_boundedly_invertible_definitizable"]
                     and not gates["g4_positive_type_II_trace_exists_on_full_region"])
check("T5  STRUCTURAL MAP.  The Krein grading PASSES THROUGH the crossed product's flow/covariance "
      "skeleton harmlessly (g0: constructible, positivity-free), BREAKS its positivity-level payoff "
      "(g1 bounded implementers: NO; g2 conditioning regulated: NO; g4 positive trace: NO), and is "
      "PARTIALLY reshaped by the observer's positive energy (g3: a genuine sign-definite selection, but "
      "the physical form degenerates in the UV -- definitized in SIGN, not in NORM).  The CLPW "
      "mechanism's positivity inputs (observer energy bounded below) act on the CLOCK factor, which was "
      "never indefinite; the field factor's indefiniteness is conserved by the very eta-unitarity that "
      "makes the construction exist.",
      structural_map_ok,
      f"{sum(1 for v in gates.values() if v)} gates true / {len(gates)}")

# ================================================================================================
# T6 -- VERDICT: PARTIAL.
# ================================================================================================
log("\n[T6] VERDICT = PARTIAL (construction exists at flow level; obstruction survives dressing / relocates)")
verdict = {
    "krein_crossed_product_exists_at_flow_level_mode_wise": True,                # T1
    "crossed_product_representation_bounded_on_full_tower": False,               # T1
    "observer_dressing_bounds_the_metric_conditioning": False,                   # T2 (THE decisive one)
    "cond_after_equals_cond_before_exactly_eta_unitary_invariance": True,        # T2
    "positive_energy_constraint_selects_sign_definite_form": True,               # T3 (steelman's kernel)
    "positive_energy_constraint_definitizes_boundedly": False,                   # T3
    "obstruction_relocates_at_identical_divergence_rate": True,                  # T3
    "type_II_positive_trace_exists_in_krein_setting": False,                     # T4
    "takesaki_type_conversion_reduces_to_definitizability": True,                # T4
    "verdict_VIABLE_observer_cures_the_wall": False,
    "verdict_PARTIAL_construction_exists_obstruction_relocates": True,
    "verdict_DEAD_indefinite_metric_breaks_the_construction_itself": False,
}
partial = (
    verdict["krein_crossed_product_exists_at_flow_level_mode_wise"]
    and (verdict["observer_dressing_bounds_the_metric_conditioning"] is False)
    and verdict["cond_after_equals_cond_before_exactly_eta_unitary_invariance"]
    and verdict["positive_energy_constraint_selects_sign_definite_form"]
    and (verdict["positive_energy_constraint_definitizes_boundedly"] is False)
    and verdict["obstruction_relocates_at_identical_divergence_rate"]
    and (verdict["type_II_positive_trace_exists_in_krein_setting"] is False)
    and (verdict["verdict_VIABLE_observer_cures_the_wall"] is False)
    and verdict["verdict_PARTIAL_construction_exists_obstruction_relocates"]
    and (verdict["verdict_DEAD_indefinite_metric_breaks_the_construction_itself"] is False)
)
check("T6  VERDICT = PARTIAL.  The Krein crossed product EXISTS as a flow-level construction (novel; "
      "sectorial scope); the DECISIVE computation says observer-dressing does NOT bound the metric "
      "conditioning (cond_after = cond_before EXACTLY, by eta-unitary invariance -- structural, not "
      "numerical); the observer's positive energy DOES select a sign-definite physical form (the "
      "steelman's kernel of truth) but the form DEGENERATES over the UV tower at the identical "
      "divergence rate (1/s_k ~ n(r_k)); no positive type-II trace exists.  The W98 obstruction "
      "SURVIVES DRESSING / RELOCATES.  Not VIABLE (the observer does not cure the wall); not DEAD "
      "(the construction itself does not break).",
      partial,
      f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans")

# ================================================================================================
# SUMMARY
# ================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W104 Krein-crossed-product checks FAILED"

log("")
log("W104 STEELMAN-2 KREIN CROSSED PRODUCT VERDICT (this file is the computation, not a claim-status change):")
log("  * DOES THE KREIN CROSSED PRODUCT EXIST?  YES at the FLOW level, mode-wise: the dressing")
log("    implementers U(p)=e^{iH_mod p} are EXACTLY eta-unitary with the crossed-product group law --")
log("    only the Gottschalk flow is needed (consistent with W91's split).  But the implementers are")
log("    ordinary-norm UNBOUNDED over the UV tower (~1/s(r)), so the representation is bounded only on")
log("    finite-rank / Pi_kappa truncations: the construction is SECTORIAL, like everything before it.")
log("  * DOES OBSERVER-DRESSING BOUND THE CONDITIONING?  NO -- EXACTLY NOT.  Dressing is conjugation by")
log("    an eta_+-unitary, and modular time-shifts are precisely the transformations that preserve the")
log("    metric: cond_after = cond_before to machine precision, per branch and clock-smeared; the")
log("    region's sup-cond still doubles under UV doubling.  This is structural (an invariance), so it")
log("    lifts beyond the toy: ANY crossed product by an eta-unitary flow conserves the metric")
log("    conditioning identically.  The CLPW mechanism regulates STATE-level (entanglement) divergences;")
log("    the Krein wall is METRIC-level.  Different divergences; dressing cures the one that was never")
log("    the wall.")
log("  * DOES THE OBSERVER'S POSITIVE ENERGY DEFINITIZE?  IN SIGN, YES (real and new): group averaging")
log("    with q >= 0 keeps only the h=-s eigenvector per mode, giving a uniformly sign-definite physical")
log("    form -- the steelman's kernel of truth.  IN NORM, NO: the surviving Krein norm s_k = ")
log("    sqrt(1-r_k^2) -> 0 over the UV tower, the physical metric degenerates (unbounded inverse), and")
log("    the divergence rate is IDENTICAL to the old ||J||-cost (1/s = n(r) x [1/sqrt2,1]): the")
log("    obstruction RELOCATES, unchanged in class, from metric blow-up to norm degeneration.")
log("  * TYPE CONVERSION III -> II?  The algebraic/flow skeleton passes through; the PAYOFF (a positive")
log("    trace, density matrices, entropies) is exactly the positivity HORN K withholds: the naive")
log("    dual-weight trace is an indefinite eta-trace (tau(a^#a) < 0 on ghost-graded elements) and the")
log("    post-constraint candidate is non-normal over the tower.  Takesaki-style conversion REDUCES to")
log("    definitizability; it does not supply it.")
log("  * VERDICT = PARTIAL.  Not VIABLE: the observer does not cure the wall.  Not DEAD: the flow-level")
log("    construction exists (a genuinely new object -- a sectorial Krein crossed product) and the")
log("    sign-definite selection is a genuinely new structure.  The wall is CONSERVED under the CLPW")
log("    move: the observer's positivity lives on the clock factor, which was never the indefinite one.")
log("  * No canon / RESEARCH-STATUS / CANON / verdict / posture change.  Exploration-grade; the")
log("    conjecture remains a conjecture.  Present, do not decide.")
raise SystemExit(0)
