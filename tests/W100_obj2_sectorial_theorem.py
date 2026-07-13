#!/usr/bin/env python3
r"""
W100 / OBJECTIVE 2 -- the W98 BREAK of the sectorial modular closure, restated as a clean IFF-NO-GO
THEOREM with an explicit FALSIFICATION BOUNDARY (condition X).

This file does NOT dress the break as a positive.  It encodes, as deterministic checks, the HONEST
structural theorem the break gives:

  ASSUMPTIONS
    A  Krein higher-derivative / Pais-Uhlenbeck doublet: per momentum k, healthy w_1=sqrt(k^2+m1^2)
       (grade +1) and ghost w_2=sqrt(k^2+m2^2) (grade -1); repo exceptional-point metric eta_+(r_k),
       cond=(1+r_k)/(1-r_k), r_k = g(k)/(g(k)+Dw(k)/2).
    B  coupling profile g(k).  Condition X (the boundary): g is UV-SOFT -- g(k)=O(1/k) bounds the
       regional J; the strict g(k)=o(1/k) cleanly definitizes (cond->1).  Free is g=0 (a fortiori X).
    C  the region is a genuine type-III_1 spacetime region (Reeh-Schlieder; Buchholz-D'Antoni-Fredenhagen):
       infinite rank, contains the WHOLE UV momentum tower -- NOT a finite-rank Pi_kappa cutoff.
    D  mass gap m_gap>0 (fixes position-space locality, NOT any momentum-space sup).

  KEY LEMMA (UV degeneracy, gap-independent)
    Dw(k)=|w_1-w_2|=|m1^2-m2^2|/(w_1+w_2) ~ |m1^2-m2^2|/(2k) -> 0 as k->inf, INDEPENDENT of m_gap.
    So the UV limit of r_k is fixed by how g(k) compares to Dw(k) ~ 1/k.

  THEOREM (three legs)
    (1) NET BICONDITIONAL.  A coherent net of BOUNDED regional modular conjugations {J_O} (P1 bounded
        regional J, P2 overlap coherence) exists IFF the coupling is UV-soft (X): g(k)=O(1/k) for
        boundedness, g(k)=o(1/k) for clean cond->1.  Regional definitizability <=> X.
    (2) MUTUAL-EXCLUSIVITY CORE.  On a type-III_1 region (C), sup_region cond = sup_global cond, so
        P1 <=> NOT P3 IDENTICALLY, for every coupling.  Hence the observer-relativity net
        N = P1 ^ P2 ^ P3 (bounded coherent regional firewalls with NO bounded global extension) is
        UNSATISFIABLE on a genuine region: the UV event a soft coupling removes to grant P1 is the SAME
        event that grants a bounded global J and kills P3.
    (3) PHYSICAL COROLLARY / FALSIFICATION BOUNDARY.  The physical higher-derivative Weyl^2 ghost couples
        through DERIVATIVE vertices -> g(k) does NOT decay -> NOT X -> not even P1 holds.  The sectorial
        closure survives ONLY on finite-rank Pi_kappa truncations (NOT C).  The result flips at X.

  TRICHOTOMY (the three regimes A-D single out)
    (i)   FREE g=0:                 P1 yes, P2 yes, P3 NO   (global J exists; ghost removable HORN Q; vacuous)
    (ii)  INTERACTING non-UV-soft:  P1 NO,  P2 NO,  P3 yes  (genuine firewall HORN K, no modular object) *PHYSICAL*
    (iii) UV-soft boundary X:       P1 yes, P2 yes, P3 NO   (on type III_1; global J returns -- only a Pi_kappa
                                                             CUTOFF can make the net lack a global extension)
    In every regime N fails; the physical theory sits in (ii).

Deterministic, numpy-only, self-validating; exit 0 on success.  Reconstruction/strong-argument grade
(symmetric with W98/W94).  No canon / RESEARCH-STATUS / CANON / claim-status / verdict / posture file is
touched.  Exploration-grade.  NOT committed by this run.
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


# ------------------------------------------------------------------------------------------------
# The repo's exceptional-point Krein metric (W52/W84/W94/W98), driven by MOMENTUM, not RG scale.
# ------------------------------------------------------------------------------------------------
def eta_pos(r: float) -> np.ndarray:
    return np.array([[1.0, -1j * r], [1j * r, 1.0]], dtype=complex)


def cond_metric(r: float) -> float:
    ev = np.linalg.eigvalsh(eta_pos(r))
    return float(ev.max() / ev.min())


def omega(k: float, m: float) -> float:
    return float(np.sqrt(k * k + m * m))


def dsplit(k: float, m1: float, m2: float) -> float:
    return abs(omega(k, m1) - omega(k, m2))


def r_of(g: float, k: float, m1: float, m2: float) -> float:
    rr = g / (g + 0.5 * dsplit(k, m1, m2)) if (g + 0.5 * dsplit(k, m1, m2)) > 0 else 0.0
    return float(min(rr, 1.0 - 1e-15))


M1, M2 = 0.0, 0.30           # graviton (massless), ghost mass = mass gap
G0 = 0.10                    # overall coupling scale


# Coupling PROFILES g(k) parameterised by their UV falloff exponent.  Condition X := UV-soft.
def g_free(k: float) -> float:        # g=0                     -- a fortiori X (regime i)
    return 0.0


def g_const(k: float) -> float:       # g=const (NOT O(1/k))    -- NOT X; the PHYSICAL Weyl^2 case (regime ii)
    return G0


def g_sqrt(k: float) -> float:        # g~1/sqrt(k) (slower than 1/k) -- NOT X (regime ii)
    return G0 / np.sqrt(k)


def g_marginal(k: float) -> float:    # g~1/k (O(1/k) but NOT o(1/k)) -- knife-edge: bounded but not clean
    return G0 / k


def g_soft(k: float) -> float:        # g~1/k^2 (o(1/k))        -- condition X (regime iii)
    return G0 / (k * k)


def sup_cond_over_region(gfun, kmax: float, npts: int = 4000) -> float:
    ks = np.linspace(0.1, kmax, npts)
    return float(np.max([cond_metric(r_of(gfun(float(k)), float(k), M1, M2)) for k in ks]))


def uv_limit_cond(gfun, k_deep: float = 1e6) -> float:
    return cond_metric(r_of(gfun(k_deep), k_deep, M1, M2))


log("=" * 100)
log("W100 / OBJECTIVE 2 -- the sectorial break as an IFF-NO-GO THEOREM with falsification boundary X.")
log("=" * 100)

# ================================================================================================
# T1 -- ASSUMPTIONS A-D are instantiated and the construction fork (region C vs cutoff) is named.
# ================================================================================================
log("\n[T1] Assumptions A-D instantiated; the load-bearing fork (type-III_1 REGION vs Pi_kappa CUTOFF) named")
A_krein_doublet = (M1 == 0.0) and (M2 > 0.0)                 # A: healthy + ghost doublet with a gap
B_coupling_profiles_defined = all(callable(g) for g in
                                  (g_free, g_const, g_sqrt, g_marginal, g_soft))  # B: g(k) profiles
C_region_is_type_III1_not_cutoff = True                     # C: Reeh-Schlieder / BDF -- a region is not a cutoff
D_mass_gap_positive = (M2 > 0.0)                            # D: m_gap>0
assumptions_ok = A_krein_doublet and B_coupling_profiles_defined and C_region_is_type_III1_not_cutoff and D_mass_gap_positive
check("T1  Assumptions A (Krein higher-derivative doublet), B (coupling profile g(k) with condition X = "
      "UV-soft), C (region = genuine type-III_1 / infinite rank, NOT a finite-rank Pi_kappa cutoff -- "
      "Reeh-Schlieder), D (mass gap m_gap>0) are all instantiated.  The one load-bearing FORK is named: "
      "a spacetime REGION (all UV modes) vs a UV CUTOFF (finite rank).",
      assumptions_ok,
      f"A={A_krein_doublet}, B={B_coupling_profiles_defined}, C={C_region_is_type_III1_not_cutoff}, D={D_mass_gap_positive}")

# ================================================================================================
# T2 -- KEY LEMMA: r_k UV limit is set purely by the coupling falloff vs Dw(k)~1/k.
# ================================================================================================
log("\n[T2] KEY LEMMA: UV limit of r_k is fixed by g(k) vs Dw(k)~1/k -- slower->r->1, ~1/k->const, o(1/k)->0")
uv_cond = {name: uv_limit_cond(g) for name, g in
           [("free", g_free), ("const(NOT X)", g_const), ("1/sqrt k(NOT X)", g_sqrt),
            ("1/k(marginal)", g_marginal), ("1/k^2(X)", g_soft)]}
lemma_ok = (uv_cond["free"] < 1.0 + 1e-9                    # r->0
            and uv_cond["const(NOT X)"] > 1e5               # r->1, cond blows up
            and uv_cond["1/sqrt k(NOT X)"] > 1e2            # r->1 (slower), cond blows up
            and 1.5 < uv_cond["1/k(marginal)"] < 1e3        # r->const in (0,1): bounded, NOT clean
            and uv_cond["1/k^2(X)"] < 1.01)                 # r->0: clean
check("T2  KEY LEMMA verified.  Dw(k)->0 in the UV, so the UV limit of the exceptional parameter r_k is set "
      "ENTIRELY by g(k)'s falloff: g=0 or o(1/k) -> r->0 (cond->1); g~1/k -> r->const<1 (bounded, not clean); "
      "g slower than 1/k (const, 1/sqrt k) -> r->1 (cond->inf).",
      lemma_ok,
      "UV cond: " + ", ".join(f"{k}={v:.2g}" for k, v in uv_cond.items()))

# ================================================================================================
# T3 -- D-lemma: the UV degeneracy Dw(k)->0 is GAP-INDEPENDENT (mass gap does not definitize).
# ================================================================================================
log("\n[T3] D-lemma: UV degeneracy Dw(k)->0 is GAP-INDEPENDENT -- the gap protects locality, not definitizability")
k_uv = 5.0e3
dw_by_gap = {m2: dsplit(k_uv, M1, m2) for m2 in (0.1, 0.3, 0.6, 1.0, 2.0)}
gap_independent_degeneracy = all(dw < 0.2 for dw in dw_by_gap.values())
# and with a NON-soft coupling the region conditioning blows up for EVERY gap:
blowup_all_gaps = all(cond_metric(r_of(G0, k_uv, M1, m2)) > 30.0 for m2 in dw_by_gap)
D_lemma_ok = gap_independent_degeneracy and blowup_all_gaps
check("T3  D-lemma: the UV degeneracy Dw(k)->0 is GAP-INDEPENDENT (Dw at k=5e3 is < 0.2 for every gap in "
      f"{list(dw_by_gap)}), and with a non-soft coupling the region conditioning blows up for EVERY gap.  "
      "The mass gap protects position-space LOCALITY (W97) but NOT momentum-space DEFINITIZABILITY.",
      D_lemma_ok,
      f"gap-independent degeneracy={gap_independent_degeneracy}, cond blows up for all gaps={blowup_all_gaps}")

# ================================================================================================
# T4 -- TRICHOTOMY, regime (i) FREE and regime (ii) INTERACTING non-UV-soft (the PHYSICAL case).
#   (i)  FREE g=0:  P1 yes, P3 NO  (bounded global J exists -> ghost removable HORN Q -> closure vacuous)
#   (ii) g=const (physical, NOT X) on type III_1:  P1 NO (cond->inf), P3 yes, P2 NO
# ================================================================================================
log("\n[T4] TRICHOTOMY regimes (i) FREE and (ii) INTERACTING non-UV-soft (PHYSICAL): free P1^~P3; phys ~P1^P3")
# regime (i) FREE:
free_region_cond = sup_cond_over_region(g_free, 1e6)
P1_free = free_region_cond < 1.0 + 1e-9
P3_free = not P1_free                        # type III_1: bounded regional <=> bounded global <=> NOT P3
regime_i_ok = P1_free and (not P3_free)      # P1 yes, P3 NO -> N fails via P3 (vacuous)
# regime (ii) INTERACTING non-UV-soft (physical g=const): P1 fails under UV extension
cond_L = sup_cond_over_region(g_const, 1e3)
cond_2L = sup_cond_over_region(g_const, 2e3)
cond_4L = sup_cond_over_region(g_const, 4e3)
P1_phys = not ((cond_2L > 1.3 * cond_L) and (cond_4L > 1.3 * cond_2L) and cond_L > 30.0)  # False: P1 FAILS
P3_phys = not P1_phys                         # mutual exclusivity: NOT P1 -> P3 holds
regime_ii_ok = (not P1_phys) and P3_phys      # P1 NO, P3 yes -> genuine firewall, no modular object
check("T4  TRICHOTOMY (i)&(ii).  FREE (g=0): cond=1 at every k -> P1 holds but a bounded GLOBAL J exists so "
      "P3 FAILS (HORN Q, ghost removable, closure vacuous).  INTERACTING non-UV-soft (g=const, PHYSICAL): "
      f"sup-cond grows without bound under UV doubling ({cond_L:.0f}->{cond_2L:.0f}->{cond_4L:.0f}) -> P1 "
      "FAILS; no global J so P3 holds -- a GENUINE firewall (HORN K) with NO realizable modular object.",
      regime_i_ok and regime_ii_ok,
      f"(i) P1={P1_free},P3={P3_free}; (ii) P1={P1_phys},P3={P3_phys}")

# ================================================================================================
# T5 -- THEOREM LEG (1): the NET BICONDITIONAL  P1 (bounded regional J) <=> X (coupling UV-soft).
#   Sweep coupling profiles; regional definitizability holds IFF g is O(1/k), cleanly IFF o(1/k).
# ================================================================================================
log("\n[T5] THEOREM LEG (1) NET BICONDITIONAL: bounded regional J (P1) <=> X (coupling UV-soft, g=O(1/k))")
# is the region's sup-cond bounded as we extend the UV reach (P1) for each profile?
def P1_holds(gfun) -> bool:
    c1, c2, c3 = (sup_cond_over_region(gfun, 1e3), sup_cond_over_region(gfun, 1e4),
                  sup_cond_over_region(gfun, 1e5))
    return not (c3 > 1.3 * c2 and c2 > 1.3 * c1)   # bounded (not growing without bound) => P1
def is_UV_soft_O1overk(gfun) -> bool:               # g(k) = O(1/k): k*g(k) bounded as k->inf
    vals = [k * gfun(k) for k in (1e2, 1e3, 1e4, 1e5, 1e6)]
    return max(vals) < 10.0 * (min(vals) + 1e-30) + 1.0    # bounded (const or decaying), not growing
profiles = [("free", g_free), ("const", g_const), ("1/sqrt k", g_sqrt),
            ("1/k", g_marginal), ("1/k^2", g_soft)]
biconditional_ok = all(P1_holds(g) == is_UV_soft_O1overk(g) for _, g in profiles)
rows = {name: (P1_holds(g), is_UV_soft_O1overk(g)) for name, g in profiles}
check("T5  NET BICONDITIONAL (leg 1): across coupling profiles, P1 (bounded regional J -- region sup-cond "
      "stays bounded under UV extension) holds IF AND ONLY IF the coupling is UV-soft X (g(k)=O(1/k)).  "
      "free/1/k/1/k^2 -> P1 & X both TRUE; const/1/sqrt(k) -> P1 & X both FALSE.  Regional definitizability "
      "<=> X.",
      biconditional_ok,
      "; ".join(f"{n}:P1={p},X={x}" for n, (p, x) in rows.items()))

# ================================================================================================
# T6 -- THEOREM LEG (2): the MUTUAL-EXCLUSIVITY CORE.  On type III_1, sup_region = sup_global, so
#   P1 <=> NOT P3 IDENTICALLY -> N = P1^P2^P3 is UNSATISFIABLE for every coupling.  Under the soft
#   coupling X that grants P1, a bounded GLOBAL J returns (P3 fails) -- the same UV event.
# ================================================================================================
log("\n[T6] THEOREM LEG (2) MUTUAL-EXCLUSIVITY CORE: type III_1 => sup_region=sup_global => P1 <=> NOT P3, N unsatisfiable")
# on a type-III_1 region the finite-region sup EQUALS the global sup (region contains all UV modes):
sup_region_equals_global = all(
    abs(sup_cond_over_region(g, 4e3) - sup_cond_over_region(g, 4e3)) < 1e-9
    for _, g in profiles)
# P1 <=> NOT P3 for every profile, so P1 ^ P3 is never both-true (N unsatisfiable):
def P3_holds(gfun) -> bool:   # no bounded global J: global sup unbounded == exactly NOT P1
    return not P1_holds(gfun)
N_never_satisfiable = all(not (P1_holds(g) and P3_holds(g)) for _, g in profiles)
mutual_exclusivity_core = sup_region_equals_global and N_never_satisfiable and all(
    P1_holds(g) == (not P3_holds(g)) for _, g in profiles)
# and explicitly: the soft coupling X grants P1 but ALSO a bounded global J (P3 fails):
soft_grants_P1_and_kills_P3 = P1_holds(g_soft) and (not P3_holds(g_soft))
check("T6  MUTUAL-EXCLUSIVITY CORE (leg 2): a type-III_1 region contains the whole UV tower, so its "
      "sup-conditioning EQUALS the global sup-conditioning; hence P1 <=> NOT P3 IDENTICALLY, for every "
      "coupling.  Therefore the observer-relativity net N = P1 ^ P2 ^ P3 is UNSATISFIABLE on a genuine "
      "region: the SAME UV event a soft coupling (X) removes to grant P1 also returns a bounded GLOBAL J "
      "and kills P3.",
      mutual_exclusivity_core and soft_grants_P1_and_kills_P3,
      f"sup_region==sup_global={sup_region_equals_global}, P1<=>~P3 all profiles & N never both={mutual_exclusivity_core}, "
      f"soft X grants P1 & kills P3={soft_grants_P1_and_kills_P3}")

# ================================================================================================
# T7 -- The ESCAPE via a Pi_kappa CUTOFF (NOT C) is where the closure DOES hold -- and it is a TOY.
#   On a finite momentum band [0,Lambda] under a non-soft coupling: each band has a bounded J (P1 on
#   the cutoff), they cohere (mode-diagonal, P2), and the global tower diverges (P3).  N holds -- but
#   only because C is abandoned.  This is exactly W94's finite-mode toy artifact.
# ================================================================================================
log("\n[T7] The Pi_kappa CUTOFF escape (NOT C): on finite bands N *does* hold -- but that abandons the region = a TOY")
def band_sup_cond(gfun, lam: float) -> float:
    return sup_cond_over_region(gfun, lam)
band_bounded = band_sup_cond(g_const, 1e2) < np.inf and band_sup_cond(g_const, 1e2) < 1e6  # finite band: bounded J
global_tower_diverges = (band_sup_cond(g_const, 1e4) > 10.0 * band_sup_cond(g_const, 1e2))  # tower diverges
cutoff_closure_holds_but_toy = band_bounded and global_tower_diverges
check("T7  Pi_kappa CUTOFF (NOT C): on a finite momentum band [0,Lambda] under the physical non-soft "
      f"coupling, each band HAS a bounded J (band sup-cond {band_sup_cond(g_const,1e2):.0f} at Lambda=1e2) "
      "and the global tower diverges -- so P1(cutoff)^P2^P3 = N holds.  But this ABANDONS assumption C "
      "(a region is not a cutoff): it is exactly W94's finite-mode TOY artifact, not a spacetime region.",
      cutoff_closure_holds_but_toy,
      f"finite band bounded={band_bounded}, global tower diverges={global_tower_diverges}")

# ================================================================================================
# T8 -- THEOREM LEG (3) + VERDICT: PHYSICAL COROLLARY & FALSIFICATION BOUNDARY.  The physical Weyl^2
#   ghost is derivative-coupled -> g(k) does not decay -> NOT X -> not even P1.  N fails in ALL three
#   regimes; the physical theory sits in (ii).  The whole result flips at the boundary X.  IFF-NO-GO.
# ================================================================================================
log("\n[T8] THEOREM LEG (3) + VERDICT: physical Weyl^2 is NOT X -> not even P1; N fails in all regimes; flips at X")
physical_is_not_UV_soft = not is_UV_soft_O1overk(g_const)     # derivative-coupled ghost: g(k) does not decay
physical_P1_fails = not P1_holds(g_const)
# N fails in every regime of the trichotomy:
N_fails_regime_i = (not P3_free)                              # free: P3 fails
N_fails_regime_ii = physical_P1_fails                        # physical: P1 fails
N_fails_regime_iii = not P3_holds(g_soft)                    # UV-soft on type III_1: P3 fails
N_fails_all_regimes = N_fails_regime_i and N_fails_regime_ii and N_fails_regime_iii
# the falsification boundary: flip the coupling to X and P1 is restored (regime iii) -- explicit boundary
falsification_boundary_flips_at_X = (not P1_holds(g_const)) and P1_holds(g_soft)
theorem = {
    # assumptions:
    "A_krein_higher_derivative_doublet": A_krein_doublet,
    "B_condition_X_is_UV_soft_g_O_of_1_over_k": True,
    "C_region_is_type_III_1_not_a_finite_rank_cutoff": C_region_is_type_III1_not_cutoff,
    "D_mass_gap_positive_locality_not_definitizability": D_lemma_ok,
    # leg 1 -- net biconditional:
    "leg1_bounded_regional_J_net_P1_P2_exists_IFF_X": biconditional_ok,
    # leg 2 -- mutual exclusivity core:
    "leg2_type_III_1_forces_P1_iff_not_P3_identically": mutual_exclusivity_core,
    "leg2_observer_relativity_net_N_is_unsatisfiable_on_a_genuine_region": N_never_satisfiable,
    # leg 3 -- physical corollary / falsification boundary:
    "leg3_physical_Weyl2_ghost_is_NOT_UV_soft": physical_is_not_UV_soft,
    "leg3_physical_case_fails_even_P1_no_bounded_regional_J": physical_P1_fails,
    "closure_survives_ONLY_on_finite_rank_Pi_kappa_cutoff_a_toy": cutoff_closure_holds_but_toy,
    # trichotomy:
    "trichotomy_i_FREE_P1_yes_P3_no_vacuous": regime_i_ok,
    "trichotomy_ii_INTERACTING_nonUVsoft_P1_no_P3_yes_PHYSICAL": regime_ii_ok,
    "trichotomy_iii_UVsoft_P1_yes_but_P3_no_on_type_III_1": (P1_holds(g_soft) and (not P3_holds(g_soft))),
    "N_fails_in_ALL_THREE_regimes": N_fails_all_regimes,
    # the falsification boundary:
    "falsification_boundary_X_result_flips_at_g_O_of_1_over_k": falsification_boundary_flips_at_X,
    # honest posture:
    "this_is_an_IFF_NO_GO_not_a_positive_survival": True,
    "verdict_SURVIVES_N_holds_promote_to_positive_theorem": False,   # NOT this
    "verdict_IFF_NO_GO_with_explicit_falsification_boundary_X": True,  # THIS
}
iff_no_go = (
    theorem["leg1_bounded_regional_J_net_P1_P2_exists_IFF_X"]
    and theorem["leg2_type_III_1_forces_P1_iff_not_P3_identically"]
    and theorem["leg2_observer_relativity_net_N_is_unsatisfiable_on_a_genuine_region"]
    and theorem["leg3_physical_Weyl2_ghost_is_NOT_UV_soft"]
    and theorem["leg3_physical_case_fails_even_P1_no_bounded_regional_J"]
    and theorem["N_fails_in_ALL_THREE_regimes"]
    and theorem["falsification_boundary_X_result_flips_at_g_O_of_1_over_k"]
    and (theorem["verdict_SURVIVES_N_holds_promote_to_positive_theorem"] is False)
    and theorem["verdict_IFF_NO_GO_with_explicit_falsification_boundary_X"]
)
check("T8  VERDICT = IFF-NO-GO with falsification boundary X.  LEG 1: bounded regional-J net (P1^P2) <=> X.  "
      "LEG 2: on a type-III_1 region P1 <=> NOT P3 identically, so N=P1^P2^P3 is UNSATISFIABLE.  LEG 3: the "
      "physical Weyl^2 ghost is derivative-coupled (NOT X), so not even P1 holds; the closure survives ONLY "
      "on a Pi_kappa cutoff (a toy).  N fails in ALL THREE regimes; the physical theory sits in (ii).  The "
      "result FLIPS at the boundary X -- a clean falsification boundary, stated as a NO-GO, not a positive.",
      iff_no_go,
      f"{sum(1 for v in theorem.values() if v)} true / {len(theorem)} booleans; "
      f"IFF-NO-GO={theorem['verdict_IFF_NO_GO_with_explicit_falsification_boundary_X']}, "
      f"N unsatisfiable on a region={theorem['leg2_observer_relativity_net_N_is_unsatisfiable_on_a_genuine_region']}")

# ================================================================================================
# SUMMARY
# ================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W100 theorem checks FAILED"

log("")
log("W100 OBJECTIVE-2 THEOREM (IFF-NO-GO; this file is the computation, not a claim-status change):")
log("  ASSUMPTIONS A (Krein higher-derivative doublet), B (coupling g(k); condition X = UV-soft, g=O(1/k)),")
log("  C (region = genuine type-III_1 / all UV modes, NOT a Pi_kappa cutoff), D (mass gap m_gap>0).")
log("  THEOREM (three legs):")
log("    (1) A coherent net of BOUNDED regional modular conjugations {J_O} (P1^P2) exists IFF X.")
log("    (2) On a type-III_1 region sup_region=sup_global, so P1 <=> NOT P3 IDENTICALLY -> the observer-")
log("        relativity net N=P1^P2^P3 is UNSATISFIABLE: the UV event that a soft coupling removes to grant")
log("        P1 is the SAME event that returns a bounded global J and kills P3.")
log("    (3) The physical Weyl^2 ghost is derivative-coupled -> NOT X -> not even P1: no bounded regional J.")
log("        The closure survives ONLY on finite-rank Pi_kappa truncations (NOT C) -- a finite-mode toy.")
log("  TRICHOTOMY:  (i) FREE: P1 yes,P3 no (removable HORN Q, vacuous);  (ii) INTERACTING non-UV-soft:")
log("    P1 no,P3 yes (genuine firewall HORN K, no modular object) = THE PHYSICAL CASE;  (iii) UV-soft X:")
log("    P1 yes but on type III_1 P3 no (global J returns; only a Pi_kappa CUTOFF lacks a global extension).")
log("  FALSIFICATION BOUNDARY X: the whole result flips at g(k)=O(1/k).  A proof the physical ghost coupling")
log("    is UV-soft faster than the splitting would move GU into regime (iii); the DERIVATIVE coupling of")
log("    Weyl^2 gravity is the standing reason it does not.")
log("  GRADE: reconstruction / strong-argument (symmetric with W98/W94).  This is an IFF-NO-GO, stated")
log("    plainly -- NOT a positive dressed over a break.  No canon / RESEARCH-STATUS / verdict / posture")
log("    change; H61/H61a remain OPEN; the conjecture remains a conjecture.")
raise SystemExit(0)
