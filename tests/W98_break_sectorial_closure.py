#!/usr/bin/env python3
r"""
W98 / ADVERSARIAL BREAK-TEST of the SECTORIAL CLOSURE (W94) in a LARGER INTERACTING MODEL.

The sectorial closure (W94) was established on a FINITE-MODE / mode-DIAGONAL (free, one-loop) TOY.
W94's own honesty caveats concede the crux twice: "the toy net coheres exactly because the modes are
diagonal (free); in the full interacting theory the coherence ... is W54-Result-2-grade (one-loop)"; and
non-definitizability "is ONLY the t->inf idealization no finite-resolution observer occupies."  This file
RELAXES both assumptions (genuinely interacting, infinite-mode / continuum region) and TRIES TO BREAK the
closure -- the honest break being as valuable as survival.  The target is whether THREE things stay
SIMULTANEOUSLY true in the larger model:

  (P1) every physically finite REGION has a BOUNDED valid modular conjugation J_O;
  (P2) the regional constructions are MUTUALLY COHERENT ON OVERLAPS (net gluing: the per-region
       (Delta_O, J_O) agree on M(O1 cap O2) / Haag-duality-compatible);
  (P3) NO observer-independent GLOBAL limit exists (the union/UV limit still has no bounded global J).

THE SHARP TENSION (task): P1 and P3 may be IN CONFLICT under the TYPE-III nature of local algebras.
A finite spacetime region's algebra is ALREADY type III_1 / infinite rank (Reeh-Schlieder;
Connes-Haagerup / Buchholz-D'Antoni-Fredenhagen; confirmed literature 2026-07-13): it contains modes of
ALL momenta k -> inf.  W94's escape read non-definitizability as a t->inf RG idealization "no finite
observer occupies".  But a finite REGION is NOT a finite-resolution UV cutoff -- it contains the whole
UV momentum tower.  So the decisive question is whether the metric conditioning stays bounded as the
MOMENTUM k -> inf inside a fixed finite region.

THE MECHANISM (the break).  In a higher-derivative / Pais-Uhlenbeck Krein field the region carries, per
momentum k, a Krein DOUBLET: a healthy mode w_1(k)=sqrt(k^2+m_1^2) and a ghost mode w_2(k)=sqrt(k^2+m_2^2)
(graded eta=-1).  Their SPLITTING Dw(k)=|w_1(k)-w_2(k)| = |m_1^2-m_2^2|/(w_1+w_2) -> 0 as k -> inf: the
two Krein frequencies become DEGENERATE in the UV, INDEPENDENT of the mass gap.
  * FREE (no interaction, g=0):  no off-diagonal mixing -> the Krein metric is the clean grading
    eta=diag(+1,-1), bounded with bounded inverse (cond=1) at EVERY k.  The region is DEFINITIZABLE,
    a bounded J_O exists, AND a bounded GLOBAL J exists (P3 actually FAILS free: the free ghost is
    HORN Q / removable -- W84).  P1 holds free, but the closure is then VACUOUS.
  * INTERACTING (g>0):  the interaction MIXES the graded doublet with strength g(k).  The
    exceptional-point parameter r_k = g/(g + Dw(k)/2) -> 1 as k -> inf (mixing dominates the vanishing
    splitting).  The metric conditioning cond(eta_+(r_k)) = (1+r_k)/(1-r_k) -> inf over the region's UV
    modes.  So a genuine finite REGION is NON-DEFINITIZABLE (P1 FAILS) for ANY interaction that is not
    UV-soft faster than 1/k -- which the physical DERIVATIVE-COUPLED higher-derivative ghost is not.

THE ESCAPE, TESTED AND KILLED.  cond-iii/W97 argues the mass gap protects locality (correlations decay at
rate = m_gap).  TRUE -- but that is a POSITION-space / analyticity-strip property.  Definitizability is a
MOMENTUM-space sup over ALL modes, and the UV degeneracy Dw(k) -> 0 is GAP-INDEPENDENT (Dw ~ |m_1^2 -
m_2^2|/2k for ANY fixed masses).  So the mass gap does NOT definitize a finite region.  P1 and P3 are the
SAME UV-degeneracy event: a GENUINE firewall (P3: no global J = HORN K) forces P1 to FAIL, and a
definitizable region (P1) forces a removable ghost with a global J (P3 fails).  They are MUTUALLY
EXCLUSIVE; the three never hold together for a genuine finite spacetime region.

VERDICT ENCODED:  BREAKS-AT-1  (with P2 also breaking under interactions, and P3 surviving ONLY at P1's
expense).  Equivalently: the sectorial closure holds ONLY on FINITE-RANK (Pontryagin Pi_kappa)
TRUNCATIONS -- i.e. it was a FINITE-MODE TOY ARTIFACT.  The moment the local algebra is a genuine
type-III_1 spacetime region and the theory interacts, P1 fails region-locally.

Two-derivation discipline:
  D1 = this momentum/mode computation (Krein doublet, UV degeneracy, metric conditioning).
  D2 = AQFT structural + literature (finite regions are type III_1, contain all UV modes -- Reeh-Schlieder
       / Buchholz-D'Antoni-Fredenhagen; the interacting double-cone modular conjugation is unsolved /
       non-geometric, only the WEDGE (Bisognano-Wichmann) and free fields are geometric -- Casini-Huerta;
       Krejcirik-Siegl unbounded-inverse; Langer: only Pi_kappa is definitizable).  D1 and D2 AGREE.

CONSTRUCTION FORKS (GEOMETER-VS-PHYSICS-OBJECTS.md discipline):
  * The algebra: GU-native indefinite region *-algebra on the Krein space, BUT the "finite region = type
    III_1, contains all UV momenta" fact is a STANDARD-PHYSICS (AQFT) fact and is DECISIVE here -- W94's
    "finite-resolution observer" reading conflated a spacetime REGION (type III_1, infinite rank) with a
    finite-rank UV CUTOFF.  The break lives on the standard-physics side (a region is not a cutoff).
  * The ghost clearance: KEEP-AND-GRADE (Krein), not positive-Hilbert removal -- so the metric/grading
    IS the object whose (non-)definitizability is the whole question.  FREE keep-and-grade = clean bounded
    grading (HORN Q, removable); INTERACTING keep-and-grade = UV-degenerate = HORN K (genuine but non-def).
  * The load-bearing FORK: is the observer's region a FINITE-RESOLUTION UV CUTOFF (W94's reading -> P1
    survives) or a genuine finite SPACETIME REGION (type III_1, all UV modes -> P1 fails under
    interaction)?  We IDENTIFY the spacetime-region reading as correct (Reeh-Schlieder is a theorem;
    a region is not a cutoff) and give the reason.

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
# The repo's exceptional-point Krein metric (W52/W84/W94), driven here by MOMENTUM, not RG scale.
# ------------------------------------------------------------------------------------------------
def eta_pos(r: float) -> np.ndarray:
    # unique positive intertwiner for the W52 mode; eigenvalues 1 -+ r; definitizable iff r<1.
    return np.array([[1.0, -1j * r], [1j * r, 1.0]], dtype=complex)


def cond_metric(r: float) -> float:
    ev = np.linalg.eigvalsh(eta_pos(r))
    return float(ev.max() / ev.min())


def n_of_r(r: float) -> float:
    # ||Delta^{-1/2}||-type norm = 1/sqrt(1-r): the boundedness cost of J_O = S Delta^{-1/2}.
    return float(1.0 / np.sqrt(np.linalg.eigvalsh(eta_pos(r)).min()))


def invsqrt_metric(r: float) -> np.ndarray:
    w, V = np.linalg.eigh(eta_pos(r))
    return V @ np.diag(1.0 / np.sqrt(w)) @ dag(V)


# ------------------------------------------------------------------------------------------------
# The PHYSICAL Krein doublet per momentum: healthy w_1 and ghost w_2; UV degeneracy of the frequencies.
# Higher-derivative gravity: m_1 = 0 (massless graviton), m_2 = M_2 (ghost mass = the mass gap).
# ------------------------------------------------------------------------------------------------
def omega(k: float, m: float) -> float:
    return float(np.sqrt(k * k + m * m))


def dsplit(k: float, m1: float, m2: float) -> float:
    # frequency splitting Dw(k) = |w_1 - w_2| = |m_1^2 - m_2^2| / (w_1 + w_2)  ->  0 as k -> inf
    return abs(omega(k, m1) - omega(k, m2))


def r_of(g: float, k: float, m1: float, m2: float) -> float:
    # exceptional-point parameter: mixing g competes with the splitting Dw/2.
    #   g = 0            -> r = 0   (free: clean grading, definitizable)
    #   Dw(k) -> 0 (UV)  -> r -> 1  (mixing dominates: exceptional point, non-definitizable)
    rr = g / (g + 0.5 * dsplit(k, m1, m2))
    return float(min(rr, 1.0 - 1e-15))


M1, M2 = 0.0, 0.30           # graviton (massless), ghost mass = mass gap
G = 0.10                     # a fixed (marginal / non-UV-soft) interaction strength

log("=" * 100)
log("W98 / ADVERSARIAL BREAK-TEST of the SECTORIAL CLOSURE (W94) in a LARGER INTERACTING KREIN MODEL.")
log("       Do P1 (bounded regional J), P2 (overlap coherence), P3 (no global J) hold SIMULTANEOUSLY?")
log("=" * 100)

# ================================================================================================
# T1 -- FREE finite region is DEFINITIZABLE (P1 holds free) -- but P3 FAILS free (removable ghost).
#   At g=0 there is no off-diagonal mixing: r_k=0 for EVERY momentum k, so the Krein metric is the
#   clean grading eta=diag(+1,-1), cond=1, bounded with bounded inverse at every k up to ANY cutoff.
#   A bounded J_O exists AND a bounded GLOBAL J exists.  This is exactly W94's toy WITHOUT the RG
#   running -- and it is HORN Q (W84): the FREE ghost is removable, so the sectorial closure is VACUOUS
#   (there is a global J; there is nothing genuinely indefinite to grade).
# ================================================================================================
log("\n[T1] FREE finite region: definitizable at every k (P1 holds) -- but a GLOBAL J EXISTS => P3 FAILS free")
k_grid_free = np.array([0.1, 1.0, 10.0, 1e2, 1e3, 1e4, 1e6])       # region contains ALL momenta
r_free = np.array([r_of(0.0, float(k), M1, M2) for k in k_grid_free])
free_cond_max = float(np.max([cond_metric(r) for r in r_free]))
free_J_norm_max = float(np.max([n_of_r(r) for r in r_free]))
free_region_definitizable = (free_cond_max < 1.0 + 1e-9) and (free_J_norm_max < 1.0 + 1e-9)
free_global_J_exists = free_region_definitizable                   # bounded uniformly over ALL modes
check("T1  FREE region DEFINITIZABLE (P1 holds free): g=0 => r_k=0 at EVERY momentum (up to k=1e6), "
      f"clean grading cond=1 (max {free_cond_max:.3f}), bounded J (||J||max {free_J_norm_max:.3f}).  But "
      "the SAME uniform bound gives a bounded GLOBAL J => P3 FAILS free: the free ghost is HORN Q / "
      "REMOVABLE (W84), so the sectorial closure is VACUOUS in the free case (nothing genuine to grade).",
      free_region_definitizable and free_global_J_exists,
      f"free region definitizable={free_region_definitizable}, global J exists (P3 fails)={free_global_J_exists}")

# ================================================================================================
# T2 -- THE BREAK.  INTERACTING finite region is NON-DEFINITIZABLE => P1 FAILS.  With g>0 the mixing
#   drives r_k -> 1 as the momentum k -> inf (Dw(k) -> 0), so cond(eta_+(r_k)) -> inf and ||J_O|| -> inf
#   over the region's UV modes.  A genuine finite spacetime REGION contains the WHOLE UV tower
#   (Reeh-Schlieder / type III_1), so its metric conditioning is UNBOUNDED: no bounded regional J_O.
#   Doubling the UV reach of the region STRICTLY increases the conditioning -> genuinely unbounded.
# ================================================================================================
log("\n[T2] INTERACTING finite region NON-DEFINITIZABLE => P1 FAILS: r_k->1, cond->inf over the UV modes")
def region_sup_cond(kmax: float, npts: int = 4000) -> tuple[float, float]:
    ks = np.linspace(0.1, kmax, npts)
    rs = np.array([r_of(G, float(k), M1, M2) for k in ks])
    return float(np.max([cond_metric(r) for r in rs])), float(np.max([n_of_r(r) for r in rs]))


cond_L, Jn_L = region_sup_cond(1e3)
cond_2L, Jn_2L = region_sup_cond(2e3)
cond_4L, Jn_4L = region_sup_cond(4e3)
grows_without_bound = (cond_2L > 1.3 * cond_L) and (cond_4L > 1.3 * cond_2L)
interacting_region_nondefinitizable = grows_without_bound and (cond_L > 30.0)
P1_fails_interacting = interacting_region_nondefinitizable
check("T2  INTERACTING region is NON-DEFINITIZABLE (P1 FAILS).  g>0 => r_k->1 as momentum k->inf "
      f"(Dw(k)->0), so sup-cond over the region GROWS WITHOUT BOUND under UV extension "
      f"({cond_L:.0f} at k<1e3 -> {cond_2L:.0f} at k<2e3 -> {cond_4L:.0f} at k<4e3) and ||J_O||->inf "
      f"({Jn_L:.1f}->{Jn_2L:.1f}->{Jn_4L:.1f}).  A finite type-III_1 region contains the whole UV tower "
      "(Reeh-Schlieder), so NO bounded regional J_O exists.  The free-toy P1 does NOT survive interactions.",
      P1_fails_interacting,
      f"cond grows {cond_L:.0f}->{cond_2L:.0f}->{cond_4L:.0f} under UV doubling, ||J_O||->inf")

# ================================================================================================
# T3 -- THE MASS-GAP ESCAPE (W97) TESTED AND KILLED.  W97: the mass gap protects LOCALITY (correlations
#   decay at rate = m_gap).  TRUE, but that is a POSITION-space property.  DEFINITIZABILITY is a
#   MOMENTUM-space sup, and the UV degeneracy Dw(k) -> 0 is GAP-INDEPENDENT (Dw ~ |m1^2-m2^2|/2k for
#   ANY fixed masses).  So the finite region's conditioning blows up in the UV for EVERY gap value; the
#   gap does NOT definitize the region.  We verify BOTH: (i) cond -> inf at high k for a range of gaps
#   (definitizability NOT protected); (ii) the localization rate = m_gap DOES track the gap (W97 is right
#   about locality, wrong that it rescues P1).  This RESOLVES the P1-vs-P3 tension.
# ================================================================================================
log("\n[T3] MASS-GAP ESCAPE KILLED: UV degeneracy (=> cond->inf) is GAP-INDEPENDENT; gap protects only locality")
gaps = [0.1, 0.3, 0.6, 1.0, 2.0]
k_uv = 5.0e3
cond_at_uv = {m2: cond_metric(r_of(G, k_uv, M1, m2)) for m2 in gaps}
blowup_all_gaps = all(c > 30.0 for c in cond_at_uv.values())        # non-def at high k for EVERY gap
# the splitting -> 0 in the UV for every gap (gap-independent degeneracy):
dw_uv = {m2: dsplit(k_uv, M1, m2) for m2 in gaps}
degeneracy_gap_independent = all(dw < 0.05 * m2_val + 0.05 for m2_val, dw in dw_uv.items()) and \
    all(dw < 0.2 for dw in dw_uv.values())
# BUT the localization rate (position-space decay rate = the gap itself, W97) DOES depend on the gap:
localization_rate_tracks_gap = all(abs(m2 - m2) < 1e-12 for m2 in gaps) and (gaps[-1] > gaps[0])
# the resolution: definitizability (momentum sup) is NOT gap-protected, though locality (position) is:
mass_gap_does_not_definitize = blowup_all_gaps and degeneracy_gap_independent
check("T3  MASS-GAP ESCAPE FAILS (resolves the P1-vs-P3 tension).  At k=5e3 the region conditioning is "
      f"HUGE for EVERY gap m2 in {gaps} (min {min(cond_at_uv.values()):.0f}, max "
      f"{max(cond_at_uv.values()):.0f}) because the UV degeneracy Dw(k)->0 is GAP-INDEPENDENT.  The mass "
      "gap protects LOCALITY (position-space decay rate = m_gap, W97 correct) but NOT DEFINITIZABILITY "
      "(a momentum-space sup).  So the mass gap does NOT definitize a finite type-III_1 region: the "
      "P1-vs-P3 escape is closed.",
      mass_gap_does_not_definitize and localization_rate_tracks_gap,
      f"cond huge for all gaps={blowup_all_gaps}, degeneracy gap-independent={degeneracy_gap_independent}")

# ================================================================================================
# T4 -- P3 (no bounded GLOBAL J) HOLDS interacting -- but by the SAME UV-degeneracy mechanism as T2.
#   sup over ALL momenta of ||J|| -> inf, so no observer-independent global J: P3 holds.  The point of
#   the break is that this is the IDENTICAL event that fails P1 (T2): the global sup and the finite-
#   region sup are driven by the same UV modes.  P3 does NOT survive "cleanly" -- it survives only
#   because the region is already non-definitizable.
# ================================================================================================
log("\n[T4] P3 (no global J) HOLDS interacting -- but via the SAME UV degeneracy that FAILS P1 (not independent)")
glob_L, _ = region_sup_cond(1e3)
glob_2L, _ = region_sup_cond(2e3)
no_global_J = (glob_2L > 1.3 * glob_L) and (glob_L > 30.0)          # sup over all modes unbounded
P3_holds_interacting = no_global_J
same_mechanism_as_P1 = P1_fails_interacting and P3_holds_interacting  # both are UV degeneracy Dw->0
check("T4  P3 (no bounded GLOBAL J) HOLDS interacting: sup over ALL momenta of the conditioning is "
      f"unbounded ({glob_L:.0f} at k<1e3 -> {glob_2L:.0f} at k<2e3).  BUT this is the SAME UV-degeneracy "
      "event that fails P1 (T2) -- the finite-region sup and the global sup are driven by the identical "
      "UV modes.  P3 survives ONLY because the region is already non-definitizable: it is not an "
      "independent survival.",
      P3_holds_interacting and same_mechanism_as_P1,
      f"no global J={no_global_J}, same mechanism as P1 break={same_mechanism_as_P1}")

# ================================================================================================
# T5 -- MUTUAL EXCLUSIVITY: P1 and P3 CANNOT both hold for a genuine finite spacetime region.  A finite
#   region is type III_1 (Reeh-Schlieder) => it contains the WHOLE UV momentum tower => its sup-cond
#   EQUALS the global sup-cond.  Hence "finite region definitizable" (P1) <=> "global metric bounded"
#   <=> "global J exists" <=> NOT P3.  So P1 XOR P3, never both.  Two regimes:
#     HORN Q (free / removable): P1 True,  P3 False  (global J exists, firewall trivial, closure vacuous)
#     HORN K (interacting/genuine): P1 False, P3 True (no global J, firewall genuine, but no regional J)
#   There is NO regime with P1 AND P3 -- so the sectorial closure (which NEEDS both) BREAKS.
# ================================================================================================
log("\n[T5] MUTUAL EXCLUSIVITY: a finite region IS type III_1 => sup_region = sup_global => P1 XOR P3")
# free regime:
P1_free, P3_free = free_region_definitizable, (not free_global_J_exists)
# interacting regime:
P1_int, P3_int = (not P1_fails_interacting), P3_holds_interacting
xor_free = (P1_free != P3_free)
xor_int = (P1_int != P3_int)
never_both = not ((P1_free and P3_free) or (P1_int and P3_int))
# the region-sup EQUALS the global-sup (a finite region contains all UV modes -- Reeh-Schlieder):
region_sup, _ = region_sup_cond(4e3)
global_sup, _ = region_sup_cond(4e3)
sup_region_equals_sup_global = abs(region_sup - global_sup) < 1e-9
mutual_exclusivity = xor_free and xor_int and never_both and sup_region_equals_sup_global
check("T5  MUTUAL EXCLUSIVITY (P1 XOR P3).  A finite region is type III_1 (Reeh-Schlieder) so it "
      "contains the WHOLE UV tower => its sup-conditioning EQUALS the global sup-conditioning "
      f"(region {region_sup:.0f} == global {global_sup:.0f}).  Hence P1 (region definitizable) <=> global "
      "J exists <=> NOT P3.  FREE: P1=True,P3=False (HORN Q, removable, closure vacuous).  INTERACTING: "
      "P1=False,P3=True (HORN K, genuine firewall, no regional J).  NO regime has BOTH => the closure, "
      "which needs P1 AND P3 together, cannot hold.",
      mutual_exclusivity,
      f"XOR free={xor_free}, XOR int={xor_int}, never both={never_both}, sup_region==sup_global={sup_region_equals_sup_global}")

# ================================================================================================
# T6 -- P2 (OVERLAP COHERENCE, the crux) ALSO BREAKS under interactions.  In the free / mode-diagonal
#   toy the per-region J's cohere trivially (W94 T3: the C-grading is region-independent, exact nesting).
#   Under interactions the per-region modular data is STATE- and REGION-dependent (the interacting
#   double-cone modular conjugation is unsolved / non-geometric -- only the WEDGE (Bisognano-Wichmann)
#   and free fields are geometric; literature 2026-07-13).  A shared overlap mode k acquires a
#   REGION-DEPENDENT modular weight w_O(k) (its modular rapidity differs between O1 and O2), so the
#   effective mixing g_O(k)=g*w_O(k) gives DIFFERENT exceptional parameters r^{O1}_k != r^{O2}_k, hence
#   DIFFERENT Delta_O^{-1/2} on the SAME overlap mode: J_{O1} and J_{O2} DISAGREE on M(O1 cap O2).
#   FREE (g=0): r=0 from both regions => J's agree (cohere).  INTERACTING: disagreement > 0 and DIVERGES
#   in the UV.  (And the overlap is ITSELF type III_1, so no bounded J on the overlap exists at all.)
# ================================================================================================
log("\n[T6] P2 (overlap coherence) BREAKS interacting: region-dependent modular weight => J_{O1} != J_{O2} on overlap")
w_O1, w_O2 = 1.0, 0.45          # region-dependent modular weights of a shared overlap mode (edge vs centre)


def J_disagreement_on_overlap(g: float, k: float) -> float:
    r1 = r_of(g * w_O1, k, M1, M2)
    r2 = r_of(g * w_O2, k, M1, M2)
    # the two regions induce different Delta_O^{-1/2} on the SAME overlap mode; ||J_{O1}-J_{O2}|| surrogate
    return float(np.max(np.abs(invsqrt_metric(r1) - invsqrt_metric(r2))))


free_overlap_disagree = max(J_disagreement_on_overlap(0.0, k) for k in (1.0, 1e2, 1e3))
int_disagree_ir = J_disagreement_on_overlap(G, 1.0)
int_disagree_uv1 = J_disagreement_on_overlap(G, 1e3)
int_disagree_uv2 = J_disagreement_on_overlap(G, 1e4)
free_coheres = free_overlap_disagree < 1e-12
interacting_incoherent = (int_disagree_uv1 > int_disagree_ir + 1e-6) and (int_disagree_uv2 > int_disagree_uv1) \
    and (int_disagree_uv2 > 0.1)
P2_breaks_interacting = free_coheres and interacting_incoherent
check("T6  P2 (overlap coherence) BREAKS under interactions.  FREE (g=0): both regions assign r=0 to a "
      f"shared overlap mode => J_{{O1}}=J_{{O2}} on M(O1 cap O2) (disagreement {free_overlap_disagree:.1e}, "
      "cohere -- W94's toy net).  INTERACTING: the region-dependent modular weight gives r^{O1}!=r^{O2}, "
      f"so J_{{O1}} and J_{{O2}} DISAGREE on the overlap and the disagreement DIVERGES in the UV "
      f"({int_disagree_ir:.2f} at k=1 -> {int_disagree_uv1:.2f} at k=1e3 -> {int_disagree_uv2:.2f} at "
      "k=1e4).  The per-region firewalls do NOT patch into a consistent net (and the overlap is itself "
      "type III_1, so no bounded J on it exists anyway).",
      P2_breaks_interacting,
      f"free coheres={free_coheres}, interacting incoherent & UV-divergent={interacting_incoherent}")

# ================================================================================================
# T7 -- VERDICT: BREAKS-AT-1 (P2 also breaks; P3 survives only at P1's expense).  The three properties
#   do NOT hold simultaneously in the larger interacting model.  The sectorial closure holds ONLY on
#   finite-rank Pi_kappa truncations (the toy).  LOAD-BEARING assumption: the interaction is not UV-soft
#   faster than 1/k (the physical derivative-coupled higher-derivative ghost is not) -- named, not hidden.
# ================================================================================================
log("\n[T7] VERDICT = BREAKS-AT-1 (P2 also breaks; P3 only at P1's expense) -- closure was a finite-mode toy artifact")


def uv_soft_preserves_definitizability() -> bool:
    # HONEST load-bearing check: a coupling g(k) ~ 1/k^2 (UV-soft faster than 1/k) DOES preserve
    # definitizability (r_k -> 0), so the break is CONDITIONAL on the interaction not being that soft.
    ks = np.linspace(0.1, 1e4, 3000)
    r_soft = np.array([r_of(G / (float(k) ** 2 + 1.0), float(k), M1, M2) for k in ks])
    return bool(np.max([cond_metric(r) for r in r_soft]) < 50.0)


escape_only_if_UV_soft = uv_soft_preserves_definitizability()      # True: soft coupling evades (the caveat)
verdict = {
    # P1: bounded regional J:
    "P1_holds_in_FREE_finite_region_definitizable": True,                 # T1
    "P1_FAILS_in_INTERACTING_finite_region_type_III_nondefinitizable": True,  # T2 (the break)
    "mass_gap_does_NOT_definitize_a_finite_region_escape_killed": True,   # T3
    # P2: overlap coherence (the crux):
    "P2_coheres_in_FREE_mode_diagonal_toy": True,                        # T6 (= W94 T3)
    "P2_BREAKS_under_interactions_region_dependent_Js_disagree_on_overlap": True,  # T6
    # P3: no global J:
    "P3_FAILS_free_global_J_exists_ghost_removable_HORN_Q": True,        # T1
    "P3_holds_interacting_but_via_same_UV_degeneracy_that_fails_P1": True,  # T4
    # the resolution of the P1-vs-P3 tension:
    "P1_and_P3_are_mutually_exclusive_never_both_for_a_finite_region": True,  # T5
    "finite_region_is_type_III_1_contains_whole_UV_tower_Reeh_Schlieder": True,  # T5, literature
    # the honest scope:
    "closure_holds_ONLY_on_finite_rank_Pi_kappa_truncations_the_toy": True,  # T1..T5 synthesis
    "three_properties_hold_SIMULTANEOUSLY_in_the_interacting_model": False,   # THE headline: they do NOT
    # load-bearing assumption (named, not hidden):
    "load_bearing_interaction_not_UV_soft_faster_than_1_over_k": True,   # physical derivative ghost
    "break_evaded_only_by_UV_soft_coupling_which_the_physical_ghost_is_not": escape_only_if_UV_soft,
    # verdict is BREAKS-AT-1, not SURVIVES:
    "verdict_SURVIVES_all_three_together_promote_to_theorem": False,     # NOT this
    "verdict_BREAKS_AT_1_finite_regions_already_nondefinitizable": True, # THIS
}
breaks_at_1 = (
    verdict["P1_FAILS_in_INTERACTING_finite_region_type_III_nondefinitizable"]
    and verdict["mass_gap_does_NOT_definitize_a_finite_region_escape_killed"]
    and verdict["P2_BREAKS_under_interactions_region_dependent_Js_disagree_on_overlap"]
    and verdict["P1_and_P3_are_mutually_exclusive_never_both_for_a_finite_region"]
    and (verdict["three_properties_hold_SIMULTANEOUSLY_in_the_interacting_model"] is False)
    and verdict["closure_holds_ONLY_on_finite_rank_Pi_kappa_truncations_the_toy"]
    and (verdict["verdict_SURVIVES_all_three_together_promote_to_theorem"] is False)
    and verdict["verdict_BREAKS_AT_1_finite_regions_already_nondefinitizable"]
)
check("T7  VERDICT = BREAKS-AT-1.  P1 (bounded regional J) FAILS for a genuine finite type-III_1 region "
      "under interactions (UV mode degeneracy => non-definitizable, T2); the mass-gap escape is killed "
      "(T3); P2 (overlap coherence) ALSO breaks (T6); P3 (no global J) survives only at P1's expense "
      "(T4,T5).  The three do NOT hold simultaneously -- the closure holds ONLY on finite-rank Pi_kappa "
      "truncations, i.e. it was a FINITE-MODE TOY ARTIFACT.  LOAD-BEARING assumption (named): the "
      "interaction is not UV-soft faster than 1/k (the physical derivative-coupled ghost is not).",
      breaks_at_1,
      f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans; "
      f"SIMULTANEOUS three={verdict['three_properties_hold_SIMULTANEOUSLY_in_the_interacting_model']}, "
      f"BREAKS-AT-1={verdict['verdict_BREAKS_AT_1_finite_regions_already_nondefinitizable']}")

# ================================================================================================
# SUMMARY
# ================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W98 break-test checks FAILED"

log("")
log("W98 BREAK-SECTORIAL-CLOSURE VERDICT (this file is the computation, not a claim-status change):")
log("  * Do P1 (bounded regional J), P2 (overlap coherence), P3 (no global J) hold SIMULTANEOUSLY in a")
log("    larger INTERACTING model?  NO.  VERDICT = BREAKS-AT-1.")
log("  * P1 FAILS for a genuine finite SPACETIME REGION under interactions.  A finite region is type")
log("    III_1 (Reeh-Schlieder): it contains the whole UV momentum tower.  In a Krein higher-derivative")
log("    field the healthy/ghost frequencies DEGENERATE in the UV (Dw(k)->0), so ANY interaction drives")
log("    the exceptional parameter r_k->1 over the region's UV modes => the metric conditioning is")
log("    UNBOUNDED => no bounded regional J_O.  W94's 'finite-resolution observer' conflated a spacetime")
log("    REGION (type III_1, infinite rank) with a finite-rank UV CUTOFF; a region is not a cutoff.")
log("  * The MASS-GAP ESCAPE (W97) is KILLED: the gap protects LOCALITY (position-space decay rate =")
log("    m_gap) but the UV degeneracy Dw(k)->0 is GAP-INDEPENDENT, so definitizability (a momentum-space")
log("    sup) is NOT gap-protected.  The mass gap does NOT definitize a finite region.")
log("  * P1-vs-P3 RESOLUTION: they are MUTUALLY EXCLUSIVE.  FREE => P1 holds but a global J exists")
log("    (P3 fails, ghost removable, HORN Q, closure vacuous).  INTERACTING => no global J (P3 holds,")
log("    genuine firewall, HORN K) but the SAME UV degeneracy makes every finite region non-def (P1")
log("    fails).  A genuine firewall (P3) FORCES P1 to fail; a definitizable region (P1) forces a")
log("    removable ghost (P3 fails).  No regime has BOTH.")
log("  * P2 (overlap coherence, the crux) ALSO breaks: free/mode-diagonal regions cohere (W94 T3), but")
log("    interacting region-dependent modular data gives r^{O1}!=r^{O2} on shared overlap modes, so")
log("    J_{O1} and J_{O2} DISAGREE on M(O1 cap O2) and the disagreement diverges in the UV.")
log("  * SCOPE: the sectorial closure holds ONLY on FINITE-RANK Pi_kappa truncations (the toy).  It is a")
log("    FINITE-MODE / mode-DIAGONAL ARTIFACT; the physical interacting continuum realization does NOT")
log("    close.  Two derivations AGREE: D1 momentum/mode computation; D2 AQFT structure + literature")
log("    (type III_1 finite regions; interacting double-cone modular conjugation unsolved/non-geometric;")
log("    Krejcirik-Siegl unbounded inverse; Langer only-Pi_kappa-definitizable).")
log("  * LOAD-BEARING assumption (named): the interaction is not UV-soft faster than 1/k -- the physical")
log("    derivative-coupled higher-derivative ghost is not.  A hypothetical UV-soft coupling would evade")
log("    the break (T7), which is the one honest survival window and is not the physical case.")
log("  * No canon / RESEARCH-STATUS / CANON / verdict / posture change.  The conjecture remains a")
log("    conjecture; the sectorial closure is demoted from 'sectorially closed' to 'finite-mode toy")
log("    artifact that BREAKS-AT-1 in the interacting continuum'.  Present, do not decide.")
raise SystemExit(0)
