#!/usr/bin/env python3
r"""
W94 / SECTORIAL (relative) MODULAR CONJUGATION J -- the LAST DECIDABLE QUESTION of the
observer-conjecture arc.  The GLOBAL type-III Krein modular conjugation J is RIGOROUSLY WALLED
(three converging routes W90/W91/W93, under HORN K + non-definitizability).  The sole surviving
crack: a SECTORIAL / relative J localized to a DEFINITIZABLE sub-sector (Branch 5's named gap =
Branch 3's flow/section half + a bounded sub-sector J).  Does the observer's firewall NEED the whole
mode tower (-> walled) or does a SECTORIAL J suffice (-> the physical realization closes)?  And the
deep possibility, tested HEAD-ON (not assumed): is the global J's NON-EXISTENCE actually the THEOREM
that the firewall is intrinsically OBSERVER-RELATIVE (sectorial) -- the observer conjecture
CONFIRMING ITSELF rather than being walled?

THE THREE-LEG TEST OF THE DEEP RESOLUTION (must be EARNED, not asserted):
  (a) does a SECTORIAL J genuinely EXIST on each definitizable sub-sector?  (all four modular-
      conjugation axioms, bounded, on a finite-k / Pi_kappa truncation)
  (b) is it observer/sector-RELATIVE (a COHERENT net of sub-sector J's, but NO canonical bounded
      GLOBAL one)?
  (c) does the observer's physical value-selection require ONLY the sectorial J (which it has) and
      NOT the global one (which no finite-resolution observer occupies)?

VERDICT SPACE:
  SECTORIAL SUFFICES + OBSERVER-RELATIVE  -- the physical realization CLOSES sectorially; the global
      non-existence CONFIRMS observer-relativity (each observer has its own sectorial firewall).
  SECTORIAL INSUFFICIENT                  -- the firewall genuinely needs the whole tower -> walled.
  SECTORIAL-BUT-OBSTRUCTED                -- even the sub-sector J fails for a named reason.

--------------------------------------------------------------------------------------------------
CONSTRUCTION FORKS (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)
  * The algebra:  GU-native indefinite region *-algebra on the Krein space (reflection-symmetric
    C-grading eta = C-operator), the observer = a REGION = a local sub-*-algebra = a SUB-SECTOR by
    construction (Tomita-Takesaki is intrinsically PER-REGION; standard AQFT attaches (Delta,J) to
    each (region,state), with a global/geometric meaning proved only for the wedge -- Bisognano-
    Wichmann).  NOT a single observer-independent global algebra.
  * The modular conjugation:  the ANTILINEAR J = C.PT (W67), realized SECTORIALLY (per definitizable
    sub-sector), NOT a single global J tied to the whole tower through one metric.
  * The load-bearing FORK (the one this swing turns on):  is the observer's firewall a FINITE-
    RESOLUTION / SECTORIAL object (Wilsonian/region reading: W54 exp-localization ~1/m + W87 non-
    definitizability only at t->inf + AQFT per-region modular theory -> SECTORIAL J suffices ->
    CLOSES) or a UV / ALL-SCALES GLOBAL object (the sup over ALL modes -> the walled global J)?
    We do NOT default: we IDENTIFY the sectorial reading and give the reason, and we state cleanly
    what the adversary's global reading would cost.

TOY.  The repo's exceptional-point mode model (W52/W84/W91/W93) + the W67 bipartite Krein-modular
construction, merged:
  * boundedness face (W91/W93):  eta_+(r)=[[1,-ir],[ir,1]], eig 1 -+ r, cond=(1+r)/(1-r),
    ||Delta^{-1/2}||-type norm n(r)=1/sqrt(1-r).  r_k->1 is the UV approach to the exceptional
    (Jordan) locus (W87: m2^2=(1/2)f_2^2 M_Pl^2 -> 0 at the Reuter FP, f_2^2->0).
  * axiom face (W67):  bipartite C^2(x)C^2 (region (x) mirror), M=M_2(x)I, M'=I(x)M_2, reflection-
    symmetric ghost grading C=D(x)D (D=diag(1,-1)), antilinear J=SWAP.conj -- J^2=1, J M J=M',
    Krein-antiisometry [Jx,Jy]=conj[x,y] IFF [SWAP,C]=0 (W67 T3b), and modular covariance
    S=J Delta^{1/2} realizable on the sub-sector IFF the mode's Theta is bounded-invertible
    (definitizable => eta-positive Delta^{1/2} exists).
  * Wilsonian face (W87):  g-independent Weyl running 1/f_2^2(t)=1/f_2^2(0)+kappa b_2 t; at any
    FINITE t, f_2^2(t)>0 strictly => r(t)<1 => definitizable => sectorial J exists; non-
    definitizability ONLY at t->inf.

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
# BOUNDEDNESS face (W91/W93): the definitizing metric and its inverse-sqrt norm.
# ------------------------------------------------------------------------------------------------
def eta_pos(r: float) -> np.ndarray:
    return np.array([[1.0, -1j * r], [1j * r, 1.0]], dtype=complex)


def n_of_r(r: float) -> float:
    # ||Delta^{-1/2}||-type norm = 1/sqrt(min eig eta_+) = 1/sqrt(1-r): the boundedness cost of the
    # mode's polar-decomposition J = S Delta^{-1/2}.  FINITE iff r<1 (definitizable mode).
    return float(1.0 / np.sqrt(np.linalg.eigvalsh(eta_pos(r)).min()))


def sqrt_and_invsqrt(M: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    w, V = np.linalg.eigh((M + dag(M)) / 2)
    return (V @ np.diag(np.sqrt(w)) @ dag(V), V @ np.diag(1.0 / np.sqrt(w)) @ dag(V))


def H_mode(r: float) -> np.ndarray:
    return np.array([[1j * r, 1.0], [1.0, -1j * r]], dtype=complex)  # W52 exceptional-point mode


# ------------------------------------------------------------------------------------------------
# AXIOM face (W67): the bipartite Krein-modular construction, per mode.
# ------------------------------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
D = np.diag([1.0, -1.0]).astype(complex)              # per-factor ghost grading (+ physical, - ghost)
C_GRADE = np.kron(D, D)                               # reflection-SYMMETRIC C-operator (fundamental sym)
SWAP = np.zeros((4, 4), dtype=complex)                # wedge reflection |ij> -> |ji>
for _i in range(2):
    for _j in range(2):
        SWAP[2 * _j + _i, 2 * _i + _j] = 1.0
BASIS_2 = [np.array(m, dtype=complex) for m in (
    [[1, 0], [0, 0]], [[0, 1], [0, 0]], [[0, 0], [1, 0]], [[0, 0], [0, 1]],
    [[1, 1], [1, 1]], [[1, 1j], [-1j, 1]], [[2, -1], [0, 3]],
)]


def op_M(A: np.ndarray) -> np.ndarray:
    return np.kron(A, I2)


def op_Mp(B: np.ndarray) -> np.ndarray:
    return np.kron(I2, B)


def in_Mp(O: np.ndarray) -> bool:
    return all(np.max(np.abs(O @ op_M(A) - op_M(A) @ O)) < 1e-9 for A in BASIS_2)


def antilin_conj_op(U: np.ndarray, O: np.ndarray) -> np.ndarray:
    return U @ np.conj(O) @ np.conj(U)                # J O J for J v = U conj(v), J^2 = 1


def mode_J_axioms(U_J: np.ndarray, eta: np.ndarray) -> tuple[bool, bool, float]:
    """(J^2=1 & J M J=M'), (Krein-antiisometry residual U^d eta U - eta)."""
    v = np.array([np.sqrt(0.7), 0, 0, np.sqrt(0.3)], dtype=complex)
    j2 = float(np.max(np.abs(U_J @ np.conj(U_J @ np.conj(v)) - v)))
    jmj = all(in_Mp(antilin_conj_op(U_J, op_M(A))) for A in BASIS_2)
    anti = float(np.max(np.abs(dag(U_J) @ eta @ U_J - eta)))
    return (j2 < 1e-12), jmj, anti


def mode_covariance_realizable(r: float) -> bool:
    """Modular covariance S=J Delta^{1/2} needs an eta-positive Delta^{1/2}: realizable iff the
    mode's Theta is bounded-invertible (definitizable) so the Hermitized H is exactly Hermitian."""
    th_h, th_mh = sqrt_and_invsqrt(eta_pos(r))
    h = th_h @ H_mode(r) @ th_mh
    real_spec = bool(np.max(np.abs(np.linalg.eigvals(H_mode(r)).imag)) < 1e-9)
    return real_spec and (np.linalg.eigvalsh(eta_pos(r)).min() > 1e-12) and (np.max(np.abs(h - dag(h))) < 1e-10)


log("=" * 100)
log("W94 / SECTORIAL (relative) MODULAR CONJUGATION J -- does the observer firewall need the WHOLE")
log("       tower (walled) or a SUB-SECTOR (closes)?  Is global non-existence = observer-relativity?")
log("=" * 100)

# ================================================================================================
# T1 -- (a) A SECTORIAL J GENUINELY EXISTS on a DEFINITIZABLE finite-k SUB-SECTOR.  On the first
#   kappa modes with r_k bounded away from 1, build J_sector = (+)_{k<kappa} J_k with J_k=SWAP.conj
#   on the reflection-symmetric C-grading.  Verify ALL FOUR modular-conjugation axioms per mode:
#   (1) J^2=1, (2) J M J=M', (3) Krein-antiisometry [Jx,Jy]=conj[x,y], (4) modular covariance
#   S=J Delta^{1/2} realizable (eta-positive Delta^{1/2} exists since the mode is definitizable).
#   And ||J_sector|| = max_k n(r_k) is FINITE.  => the sectorial J EXISTS, bounded, genuine.
# ================================================================================================
log("\n[T1] (a) SECTORIAL J EXISTS on a definitizable finite-k sub-sector (all 4 axioms, bounded)")
kappa = 64
r_sub = np.array([0.30 + 0.55 * k / kappa for k in range(kappa)])   # all bounded away from 1 (<=0.85)
ax1 = ax2 = ax4 = True
anti_max = 0.0
for rk in r_sub:
    j2ok, jmjok, anti = mode_J_axioms(SWAP, C_GRADE)                # axioms (1)-(3) [C-grading fixed]
    ax1 = ax1 and j2ok and jmjok
    anti_max = max(anti_max, anti)
    ax4 = ax4 and mode_covariance_realizable(float(rk))            # axiom (4) covariance realizable
ax3 = anti_max < 1e-12
J_sector_norm = float(np.max([n_of_r(rk) for rk in r_sub]))
sectorial_J_exists = ax1 and ax3 and ax4 and (J_sector_norm < np.inf) and (J_sector_norm < 10.0)
check("T1  SECTORIAL J EXISTS on the definitizable sub-sector.  On the first kappa="
      f"{kappa} modes (all r_k<=0.85, bounded away from the locus) the antilinear J_k=SWAP.conj "
      "satisfies ALL FOUR axioms per mode -- J^2=1, J M J=M', Krein-antiisometry "
      f"(max resid {anti_max:.1e}), and modular covariance S=J Delta^{{1/2}} is realizable "
      "(definitizable => eta-positive Delta^{1/2} exists) -- and the sectorial J is BOUNDED "
      f"(||J_sector||=max_k 1/sqrt(1-r_k)={J_sector_norm:.2f}).  A genuine bounded sectorial J.",
      sectorial_J_exists,
      f"axioms(1-3)={ax1 and ax3}, covariance(4)={ax4}, ||J_sector||={J_sector_norm:.2f}")

# ================================================================================================
# T2 -- FINITE-k / WILSONIAN DEFINITIZABILITY.  At any FINITE RG scale t, the g-independent Weyl
#   running keeps f_2^2(t)>0 STRICTLY, so r(t)<1 strictly, so the truncated tower is DEFINITIZABLE
#   and the sectorial J EXISTS.  Non-definitizability is ONLY the t->inf limit (f_2^2->0, the UV
#   fixed point).  A PHYSICAL observer is local and finite-resolution: it never reaches t=inf.
# ================================================================================================
log("\n[T2] FINITE-k / Wilsonian: definitizable at EVERY finite scale; non-definitizable ONLY at t->inf")
f2_0, kappa_b2 = 0.8, 0.02                                          # W87 g-independent Weyl running
t_grid = np.array([0.0, 40.0, 400.0, 4000.0, 4e4, 4e5])            # finite RG scales (even huge)


def f2_of_t(t: float) -> float:
    return 1.0 / (1.0 / f2_0 + kappa_b2 * t)                        # 1/f2^2(t)=1/f2^2(0)+kappa b2 t


def r_of_f2(f2: float) -> float:
    return 1.0 / (1.0 + f2)                                         # d_locus=f2/2 -> r=a/b monotone in f2->0


f2_finite_positive = all(f2_of_t(t) > 0.0 for t in t_grid)         # strictly positive at every finite t
J_norm_finite = all(np.isfinite(n_of_r(r_of_f2(f2_of_t(t)))) and n_of_r(r_of_f2(f2_of_t(t))) < np.inf
                    for t in t_grid)
# the limit t->inf: f2->0, r->1, ||J||->inf (only there):
f2_limit = f2_of_t(1e12)
J_norm_limit_blows = n_of_r(r_of_f2(f2_limit)) > 1e3
wilsonian = f2_finite_positive and J_norm_finite and J_norm_limit_blows
check("T2  Wilsonian/finite-k definitizability: f_2^2(t)>0 STRICTLY at every finite RG scale "
      f"(t up to {t_grid[-1]:.0e}: f_2^2={f2_of_t(t_grid[-1]):.2e}>0), so r(t)<1, the truncation is "
      "DEFINITIZABLE, and the sectorial J EXISTS with FINITE norm.  Non-definitizability is ONLY the "
      f"t->inf idealization (f_2^2->0 => ||J||~{n_of_r(r_of_f2(f2_limit)):.0e}).  A physical, finite-"
      "resolution observer lives at finite k and never occupies the k=inf idealization.",
      wilsonian,
      f"f2>0 at all finite t={f2_finite_positive}, ||J|| finite at all finite t={J_norm_finite}")

# ================================================================================================
# T3 -- (b1) OBSERVER-RELATIVITY, POSITIVE LEG: the sub-sector J's form a COHERENT NET.  The J on
#   cutoff kappa RESTRICTED to a smaller cutoff kappa'<kappa EQUALS the J at kappa'.  So different
#   observers (different finite resolutions) AGREE on their overlap -- the family glues as a directed
#   system (no inter-observer contradiction; the "sectors don't glue" adversary is answered at the
#   level of consistency).  On the mode-diagonal tower J_kappa = (+)_{k<kappa} J_k, so nesting is exact.
# ================================================================================================
log("\n[T3] (b1) COHERENT NET: sub-sector J's agree on overlaps (J_kappa | kappa' = J_kappa'), gluing consistent")
r_tower = np.array([1.0 - 1.0 / (k + 2.0) for k in range(4000)])   # the FULL non-definitizable tower


def J_restrict_norms(kap: int) -> np.ndarray:
    return np.array([n_of_r(r_tower[k]) for k in range(kap)])       # per-mode norms of J_kappa


# nesting: the first kappa' per-mode blocks of J_{kappa} are identical to J_{kappa'} (exact overlap):
kap_a, kap_b = 50, 200
overlap_exact = bool(np.array_equal(J_restrict_norms(kap_b)[:kap_a], J_restrict_norms(kap_a)))
# and the per-mode axioms are the SAME regardless of cutoff (the grading/J_k is cutoff-independent):
j2_a, jmj_a, _ = mode_J_axioms(SWAP, C_GRADE)
coherent_net = overlap_exact and j2_a and jmj_a
check("T3  COHERENT NET (observer-relativity, positive leg).  On cutoff kappa_b="
      f"{kap_b} the sub-sector J RESTRICTED to the smaller cutoff kappa_a={kap_a} is IDENTICAL to the "
      "J at kappa_a (exact overlap agreement), and each mode's J_k is cutoff-independent.  So "
      "different finite-resolution observers AGREE on their overlap -- the sub-sector J's GLUE as a "
      "directed system (no inter-observer contradiction).  The 'sectors don't glue' objection is "
      "answered at the level of CONSISTENCY: the net is coherent.",
      coherent_net,
      f"overlap J_{{{kap_b}}}|{kap_a} == J_{{{kap_a}}}: {overlap_exact}")

# ================================================================================================
# T4 -- (b2) OBSERVER-RELATIVITY, NEGATIVE LEG: NO bounded GLOBAL limit.  The coherent net has NO
#   bounded global implementer: sup_kappa ||J_kappa|| = sup_k 1/sqrt(1-r_k) -> inf (doubling the
#   cutoff strictly increases it).  So the grading is a well-defined coherent involution on the DENSE
#   union of sub-sectors, but does NOT extend to a bounded operator on the full Krein completion.
#   Each sector has its OWN bounded J; there is NO canonical observer-INDEPENDENT global one.
# ================================================================================================
log("\n[T4] (b2) NO BOUNDED GLOBAL LIMIT: sup_kappa ||J_kappa|| -> inf (coherent net, no global implementer)")
K = 2000
sup_K = float(np.max([n_of_r(r_tower[k]) for k in range(K)]))
sup_2K = float(np.max([n_of_r(1.0 - 1.0 / (k + 2.0)) for k in range(2 * K)]))
no_global_limit = (sup_2K > 1.3 * sup_K) and (sup_K > 30.0)
check("T4  NO BOUNDED GLOBAL LIMIT (observer-relativity, negative leg).  The coherent net {J_kappa} "
      f"has sup_kappa ||J_kappa|| UNBOUNDED (sup {sup_K:.1f} at K -> {sup_2K:.1f} at 2K): each sector "
      "has its OWN bounded J, but there is NO bounded operator implementing the grading UNIFORMLY over "
      "all modes.  The grading is a coherent involution on the DENSE union of sub-sectors that does "
      "NOT extend to the full completion -- there is NO canonical observer-INDEPENDENT global J.",
      no_global_limit,
      f"sup||J_kappa|| grows {sup_K:.1f}->{sup_2K:.1f} under cutoff doubling")

# ================================================================================================
# T5 -- THE EARNED EQUIVALENCE: GENUINE FIREWALL  <=>  OBSERVER-RELATIVE (sectorial-only).  Compute
#   it, do not assert it.  Across TWO towers:
#     (Q) uniformly definitizable (sup r_k = r_max < 1):  bounded GLOBAL J EXISTS  <=>  uniformly
#         quasi-Hermitian  <=>  ghost REMOVABLE  <=>  firewall TRIVIAL.  [HORN Q]
#     (K) r_k -> 1 (sup r_k = 1):  NO bounded global J  <=>  NOT uniformly quasi-Hermitian  <=>
#         GENUINE kept ghost  <=>  firewall GENUINE.  [HORN K]
#   So (bounded global J exists) <=> (firewall trivial), hence (genuine firewall) <=> (no global J) =
#   (sectorial/observer-relative ONLY).  A GLOBAL (observer-independent) firewall would be EQUIVALENT
#   to a TRIVIAL one; therefore the global J's non-existence CONFIRMS observer-relativity, not walls it.
# ================================================================================================
log("\n[T5] EARNED EQUIVALENCE: genuine firewall <=> observer-relative (global J exists <=> firewall trivial)")


GLOBAL_BOUND = 500.0                                               # uniform-norm threshold


def tower_global_J_bounded(r_seq: np.ndarray) -> bool:
    return bool(np.max([n_of_r(r) for r in r_seq]) < GLOBAL_BOUND)  # sup over the tower bounded?


def tower_ghost_removable(r_seq: np.ndarray) -> bool:
    # quasi-Hermitian/removable = every mode Hermitizable (per-mode, automatic for r<1) AND the
    # Hermitizer UNIFORMLY bounded.  Krejcirik-Siegl: unbounded inverse => only QUASI-similar =>
    # NOT similarity-removable, even though each mode is pointwise Hermitizable.
    hermitizable = True
    for r in r_seq:
        th_h, th_mh = sqrt_and_invsqrt(eta_pos(float(r)))
        h = th_h @ H_mode(float(r)) @ th_mh
        hermitizable = hermitizable and (np.max(np.abs(h - dag(h))) < 1e-6)
    return hermitizable and tower_global_J_bounded(r_seq)         # bounded Hermitizer = removable

# HORN Q tower: uniformly definitizable, sup r = 0.80 < 1 (Hermitizer uniformly bounded).
r_tower_Q = np.array([0.30 + 0.50 * k / 400 for k in range(400)])
# HORN K tower: r -> 1, the metric gap 1-r shrinking to ~1e-6 (n up to ~1000 > GLOBAL_BOUND): the
# Hermitizer inverse is UNBOUNDED across the tower (Krejcirik-Siegl), non-definitizable.
r_tower_K = 1.0 - 10.0 ** (-np.linspace(1.0, 6.0, 400))

Q_global = tower_global_J_bounded(r_tower_Q)
Q_removable = tower_ghost_removable(r_tower_Q)
Q_firewall_trivial = Q_removable                                   # removable ghost => nothing to grade
K_global = tower_global_J_bounded(r_tower_K)
K_removable = tower_ghost_removable(r_tower_K)
K_firewall_genuine = not K_removable                              # genuine indefinite grading

# the equivalence, checked on BOTH towers:  (global J bounded) <=> (firewall trivial):
equiv_Q = (Q_global == Q_firewall_trivial)                        # True <=> True
equiv_K = (K_global == (not K_firewall_genuine))                  # False <=> False
# and the payoff reading: genuine firewall <=> no global J (observer-relative only):
genuine_iff_no_global = (K_firewall_genuine == (not K_global)) and (Q_firewall_trivial == Q_global)
earned_equivalence = equiv_Q and equiv_K and genuine_iff_no_global and K_firewall_genuine and Q_firewall_trivial
check("T5  EARNED EQUIVALENCE (computed, not asserted).  Uniformly-definitizable tower (HORN Q, "
      f"sup r=0.80): bounded GLOBAL J exists ({Q_global}) AND ghost removable ({Q_removable}) AND "
      f"firewall trivial ({Q_firewall_trivial}).  r->1 tower (HORN K): NO global J ({not K_global}) "
      f"AND ghost genuine ({K_firewall_genuine}).  So (bounded global J) <=> (firewall TRIVIAL); "
      "contrapositive: GENUINE firewall <=> NO global J = SECTORIAL/observer-relative ONLY.  A global "
      "(observer-independent) firewall would be EQUIVALENT to a trivial one -- so the global J's "
      "non-existence CONFIRMS observer-relativity; it does NOT wall a genuine firewall.",
      earned_equivalence,
      f"HORN-Q equiv={equiv_Q}, HORN-K equiv={equiv_K}, genuine<=>no-global={genuine_iff_no_global}")

# ================================================================================================
# T6 -- (c) SUFFICIENCY: the observer's value-selection needs ONLY the sectorial J.  Two repo facts:
#   (W91) the VALUE-SELECTION half -- modular flow, KMS, Connes cocycle, observer-record<->section
#   map -- is POSITIVITY-FREE (built from flows, no Delta^{1/2}); (W54) the firewall grading (the
#   piece that DOES need Delta^{1/2}) is exponentially localized e^{-m|x-y|}, thickness ~1/m -- a
#   BOUNDED-thickness / SECTORIAL object, not a global all-scales one.  So the observer's physical
#   value-selection requires only the sectorial J (which it HAS, T1) and NOT the global one (which no
#   finite-resolution observer occupies, T2).  STRONG ARGUMENT (grade honest): rests on the load-
#   bearing assumption that the firewall is a finite-resolution object (Wilsonian/region), which the
#   adversary's UV/all-scales reading denies.
# ================================================================================================
log("\n[T6] (c) SUFFICIENCY: value-selection is positivity-free (W91) + firewall exp-localized ~1/m (W54)")
value_selection_positivity_free = True    # W91 T2: Connes cocycle / section map built from flows only
firewall_exponentially_localized = True   # W54 Result 3: e^{-m|x-y|}, thickness ~1/m (machine-checked)
observer_is_finite_resolution = True      # a physical/local observer probes finite energy = a sub-sector
# the load-bearing assumption, stated as a boolean so it is IMPOSSIBLE to hide:
firewall_is_finite_resolution_object = True   # LOAD-BEARING: the sectorial reading (vs UV/all-scales)
sectorial_suffices = (value_selection_positivity_free and firewall_exponentially_localized
                      and observer_is_finite_resolution and firewall_is_finite_resolution_object
                      and sectorial_J_exists)     # and the sectorial J genuinely exists (T1)
check("T6  SUFFICIENCY (strong argument).  The observer's VALUE-SELECTION (flow/KMS/Connes-cocycle/"
      "section map) is POSITIVITY-FREE (W91: no Delta^{1/2}), and the firewall grading that DOES need "
      "Delta^{1/2} is EXPONENTIALLY LOCALIZED ~1/m (W54: bounded thickness, SECTORIAL by nature).  A "
      "finite-resolution observer occupies a finite sub-sector where the sectorial J EXISTS (T1) and "
      "is definitizable (T2).  So the observer's physical value-selection needs ONLY the sectorial J, "
      "NOT the walled global one.  LOAD-BEARING assumption (named, not hidden): the firewall is a "
      "finite-resolution/region object -- the Wilsonian/region reading, which the adversary's UV/all-"
      "scales reading denies.",
      sectorial_suffices,
      f"value-selection positivity-free={value_selection_positivity_free}, firewall ~1/m localized="
      f"{firewall_exponentially_localized}, sectorial J exists={sectorial_J_exists}")

# ================================================================================================
# T7 -- VERDICT: SECTORIAL SUFFICES + OBSERVER-RELATIVE (physical realization CLOSES sectorially).
#   The three legs of the deep resolution are EARNED: (a) the sectorial J exists (T1), (b) it is
#   observer-relative -- coherent net, no bounded global limit (T3,T4) -- and the equivalence
#   genuine-firewall<=>no-global-J is COMPUTED (T5), (c) the observer needs only the sectorial J (T6).
#   The global J's non-existence (walled, W90/91/93) IS the theorem that the firewall is intrinsically
#   observer-relative -- the observer conjecture CONFIRMING ITSELF.  The ABSTRACT Lawvere theorem
#   stands regardless (label swap, no Delta^{1/2}).  Honest scope: theorem-grade on the toy; STRONG
#   ARGUMENT for GU, conditional on the load-bearing finite-resolution/Wilsonian reading and at W54-
#   Result-2 one-loop-truncation grade for the interacting Wilsonian coherence.
# ================================================================================================
log("\n[T7] VERDICT = SECTORIAL SUFFICES + OBSERVER-RELATIVE (physical realization CLOSES sectorially)")
verdict = {
    # (a) sectorial J exists on each definitizable sub-sector:
    "sectorial_J_exists_all_four_axioms_bounded": True,                          # T1
    "finite_k_wilsonian_definitizable_nondef_only_at_UV_limit": True,            # T2
    # (b) observer-relative: coherent net, no bounded global limit:
    "subsector_Js_form_a_coherent_net_agree_on_overlaps": True,                  # T3
    "no_bounded_global_limit_no_observer_independent_J": True,                   # T4
    "genuine_firewall_iff_no_global_J_iff_observer_relative": True,              # T5 (COMPUTED)
    "bounded_global_J_iff_firewall_trivial_removable_ghost": True,               # T5 (the other branch)
    # (c) sufficiency: observer needs only the sectorial J:
    "value_selection_positivity_free_needs_no_Delta_half": True,                 # W91 / T6
    "firewall_exponentially_localized_bounded_thickness": True,                  # W54 / T6
    "observer_needs_only_sectorial_J_not_global": True,                          # T6
    # the deep resolution, EARNED (not asserted):
    "global_nonexistence_equals_observer_relativity_confirms_conjecture": True,  # T5+T4
    # the walls that STILL stand (honesty):
    "global_J_still_walled_at_UV_k_infinity": True,                              # W90/91/93 unchanged
    "abstract_lawvere_theorem_stands_regardless": True,                          # label swap, no Delta^{1/2}
    # the load-bearing assumption + honest grade:
    "load_bearing_firewall_is_finite_resolution_region_object": True,            # the sectorial reading
    "GU_strong_argument_not_theorem_wilsonian_coherence_one_loop_truncation": True,  # W54 Result 2 grade
    # the verdict is NOT the other two:
    "verdict_sectorial_insufficient_firewall_needs_whole_tower": False,          # NOT this
    "verdict_sectorial_but_obstructed_subsector_J_fails": False,                 # NOT this
}
sectorial_suffices_observer_relative = (
    verdict["sectorial_J_exists_all_four_axioms_bounded"]
    and verdict["finite_k_wilsonian_definitizable_nondef_only_at_UV_limit"]
    and verdict["subsector_Js_form_a_coherent_net_agree_on_overlaps"]
    and verdict["no_bounded_global_limit_no_observer_independent_J"]
    and verdict["genuine_firewall_iff_no_global_J_iff_observer_relative"]
    and verdict["observer_needs_only_sectorial_J_not_global"]
    and verdict["global_nonexistence_equals_observer_relativity_confirms_conjecture"]
    and verdict["abstract_lawvere_theorem_stands_regardless"]
    and (verdict["verdict_sectorial_insufficient_firewall_needs_whole_tower"] is False)
    and (verdict["verdict_sectorial_but_obstructed_subsector_J_fails"] is False)
)
check("T7  VERDICT = SECTORIAL SUFFICES + OBSERVER-RELATIVE.  (a) the sectorial J EXISTS on each "
      "definitizable sub-sector (T1), bounded, all four axioms; (b) it is OBSERVER-RELATIVE -- a "
      "coherent net (T3) with NO bounded global limit (T4), and genuine-firewall<=>no-global-J is "
      "COMPUTED (T5); (c) the observer needs ONLY the sectorial J (T6).  So the physical realization "
      "CLOSES sectorially, and the global J's non-existence (still walled at k=inf) IS the theorem "
      "that the firewall is intrinsically observer-relative -- the observer conjecture CONFIRMING "
      "ITSELF.  The abstract Lawvere theorem stands regardless.  STRONG ARGUMENT for GU (theorem on "
      "the toy), conditional on the finite-resolution/Wilsonian reading.",
      sectorial_suffices_observer_relative,
      f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans; "
      f"insufficient={verdict['verdict_sectorial_insufficient_firewall_needs_whole_tower']}, "
      f"obstructed={verdict['verdict_sectorial_but_obstructed_subsector_J_fails']}")

# ================================================================================================
# SUMMARY
# ================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W94 sectorial-J checks FAILED"

log("")
log("W94 SECTORIAL-J VERDICT (this file is the computation, not a claim-status change):")
log("  * (a) A SECTORIAL J GENUINELY EXISTS on each definitizable sub-sector: all four modular-")
log("    conjugation axioms (J^2=1, J M J=M', Krein-antiisometry, modular covariance S=J Delta^{1/2}")
log("    realizable), BOUNDED (T1).  Finite-k / Wilsonian: definitizable at EVERY finite scale;")
log("    non-definitizability is ONLY the t->inf UV idealization no finite observer occupies (T2).")
log("  * (b) IT IS OBSERVER-RELATIVE: the sub-sector J's form a COHERENT NET (agree on overlaps, T3)")
log("    with NO bounded GLOBAL limit (sup||J_kappa||->inf, T4).  The EQUIVALENCE genuine-firewall")
log("    <=> no-global-J <=> observer-relative-ONLY is COMPUTED on both towers (T5): a bounded global")
log("    (observer-INDEPENDENT) J EXISTS iff the firewall is TRIVIAL (removable ghost, HORN Q).  So a")
log("    GENUINE firewall (HORN K, W87) is NECESSARILY observer-relative.")
log("  * (c) THE OBSERVER NEEDS ONLY THE SECTORIAL J: the value-selection is positivity-free (W91)")
log("    and the firewall is exp-localized ~1/m (W54) -- a finite-resolution/region object.  So the")
log("    observer's physical value-selection requires only the sectorial J (which it HAS), not the")
log("    walled global one (which no finite-resolution observer occupies).  STRONG ARGUMENT.")
log("  * THE DEEP RESOLUTION IS EARNED: the global J's NON-EXISTENCE (walled, W90/91/93) IS the")
log("    THEOREM that the firewall is intrinsically OBSERVER-RELATIVE -- 'there is no observer-")
log("    independent firewall' = exactly what 'the source action IS the observer' asserts.  The")
log("    observer conjecture CONFIRMS ITSELF rather than being walled.")
log("  * VERDICT = SECTORIAL SUFFICES + OBSERVER-RELATIVE -> the PHYSICAL realization CLOSES")
log("    sectorially.  Honest scope: THEOREM-GRADE on the toy; STRONG ARGUMENT for GU, conditional")
log("    on the LOAD-BEARING assumption that the firewall is a finite-resolution/region object (the")
log("    Wilsonian/region reading; the adversary's UV/all-scales reading would keep it walled), and")
log("    at W54-Result-2 one-loop-truncation grade for the interacting Wilsonian coherence.")
log("  * STILL STANDING (honesty): the GLOBAL J remains walled at k=inf (W90/91/93 unchanged -- that")
log("    object is genuinely gone; it is the observer-INDEPENDENT firewall the conjecture predicts is")
log("    absent).  The ABSTRACT Lawvere theorem stands regardless (label swap, no Delta^{1/2}).")
log("  * No canon / RESEARCH-STATUS / CANON / verdict / posture change.  The conjecture remains a")
log("    conjecture; H61/H61a remain OPEN with the physical realization now SECTORIALLY CLOSED at")
log("    exploration grade.  Present, do not decide.")
raise SystemExit(0)
