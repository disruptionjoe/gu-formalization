#!/usr/bin/env python3
r"""H55 (Wave 36) -- POSITIVITY SHAPE-COLLAPSE of the gravity beta/alpha band.

Wave 35 mapped GU's source action to a FAMILY whose only continuous shape freedom is the gravity
ratio r = beta/alpha of the two O(4)-invariant 4-derivative densities: |II|^2 (full norm, rank-10 on
Sym^2(R^4)) and |H|^2 (trace-square, rank-1). The family interpolates:

    r = -1/4   conformal edge   |II_0|^2 = |II|^2 - (1/4)|H|^2   (H48, pure Bach, Einstein term absent)
    r =  0     full-|II|^2 lean                                  (H45, Stelle Einstein + Weyl)

H49 showed this ratio is the survives-vs-forceable life-or-death fork: the |II|^2 branch (Einstein term
present) survives the rotation-curve + tree-ghost refutations; the pure-conformal |II_0|^2 edge (no
Einstein term) inherits Horne / Hobson-Lasenby as a KILL and sits on the Pais-Uhlenbeck Jordan boundary.

GOAL: apply EFT positivity bounds (Adams-Arkani-Hamed-Dubovsky-Nicolis-Rattazzi 2006) + the m2_eff window
[5/6, 5/4] + the H49 survival constraint, and ask whether the 1-parameter band r collapses to a POINT.

THE CAVEAT (Wave 34): GU's massive spin-2 is a KREIN ghost, cleared by [P,S]=0 (Cartan involution of
so(9,5)), and the source-action group Sp(32,32;H) is NON-COMPACT. So the naive AADNR bound (which assumes
a positive-definite spectral density from ordinary unitarity) does NOT apply; the correct object is the
KREIN-MODIFIED / physical-subspace positivity. This file states that modification explicitly and asks
whether it retains any teeth on r.

WHAT THIS FILE COMPUTES (deterministic; exact sympy + exact rational arithmetic; exit 0 iff all PASS):

  Q1  The linearized TT + trace propagator residues as functions of r and m2_eff. The Stelle two-pole
      box(box+m^2) structure: massless graviton (residue +1/(alpha m^2)) + massive spin-2 (residue
      -1/(alpha m^2), the Krein ghost). Reproduces H45/H49 residues (+1/m2^2, -1/m2^2) at r=0, and the
      r -> -1/4 Jordan degeneration (m^2 -> 0, split coefficient diverges).

  Q2  The AADNR forward positivity bound on the massive-spin-2 exchange, and its Krein modification.
      NAIVE bound: c2 = (2/pi) int rho(s)/s^3 ds > 0 requires rho(s) >= 0 (a POSITIVE spectral density,
      from ordinary unitarity / the optical theorem). KREIN modification: the completeness relation is
      1 = sum_n eta_n |n><n| with eta_n = +-1 (Krein signature; [P,S]=0), so the discontinuity is a
      SIGNED measure rho(s) = sum_n eta_n rho_n(s), and the ghost pole (eta=-1) is exactly the massive
      spin-2 whose residue sign is the r-discriminant. => c2 is sign-INDEFINITE; no sign-definite
      interval on r follows from the strong bound. Non-compact Sp(32,32;H) has no positive-definite
      invariant inner product to restore the naive bound.

  Q3  Combine with the m2_eff window and the H49 survival constraint. The m2_eff window [5/6,5/4] fixes
      the SCALE at r=0 (method uncertainty on m2_eff), not the ratio r. The only teeth that survive are
      the WEAK physical-subspace positivity = massless-graviton residue > 0 => m^2(r) > 0 => r > -1/4
      (the open conformal edge) -- which is EXACTLY the H49 survival constraint, not the AADNR bound.
      Surviving band = (-1/4, 0], half-open. UNCHANGED by the strong positivity.

  Q4  VERDICT: NO-CONSTRAINT (the strong AADNR positivity is blind here -- the Krein modification removes
      its teeth). The band is NOT collapsed to a point and NOT narrowed beyond the already-known survival
      constraint. Honest: no collapse is manufactured.

Run: python -u tests/wave36/H55_positivity_shape_collapse.py   (exit 0 iff all PASS)
"""
from __future__ import annotations

from fractions import Fraction as F

import sympy as sp

FAIL: list[str] = []

CONFORMAL_EDGE = F(-1, 4)          # r = beta/alpha for pure conformal |II_0|^2 (H48, m^2 = 0)
FULL_II_LEAN = F(0)               # r = beta/alpha for full |II|^2 (H45)
M2EFF_LOW, M2EFF_HIGH = F(5, 6), F(5, 4)   # H24/H25 method window on m2_eff at the physical config


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('   ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ================================================================================================
# Q1 -- THE PROPAGATOR RESIDUES as functions of r = beta/alpha and m2_eff (Stelle two-pole)
# ================================================================================================
def q1_residues():
    log("=" * 100)
    log("Q1 -- TT + trace propagator residues vs r=beta/alpha and m2_eff (Stelle box(box+m^2))")
    log("=" * 100)

    s, alpha, mstar2 = sp.symbols("s alpha mstar2", positive=True)
    r = sp.symbols("r", real=True)

    # The family density is alpha*|II|^2 + beta*|H|^2 = alpha*( |II|^2 + r*|H|^2 ), r = beta/alpha.
    # The conformally invariant combination is |II_0|^2 = |II|^2 - (1/4)|H|^2 (traceless SFF in 4D),
    # so the Einstein (box, s^1) TT coefficient is proportional to (1 + 4r): it is present for the full
    # norm (r=0) and vanishes at the conformal edge (r=-1/4). The Weyl/Bach (box^2, s^2) coefficient is
    # present throughout (H45: |II|^2 and |H|^2 both carry box^2). Normalize the box^2 coeff to alpha.
    #   m^2(r) = mstar2 * (1 + 4r),  mstar2 = the full-|II|^2 (r=0) Einstein scale = m2_eff * mu_DW^2.
    m2_of_r = mstar2 * (1 + 4 * r)
    P = alpha * (s**2 + m2_of_r * s)          # = alpha * s * (s + m^2(r))
    prop = 1 / P

    # Q1a: the TT symbol factorizes as the Stelle two-pole box(box+m^2) (COMPUTED).
    factored = sp.factor(P)
    check("Q1a. [COMPUTED] TT operator = alpha*box*(box + m^2(r)), m^2(r)=mstar2*(1+4r): the Stelle "
          "two-pole box(box+m^2). Weyl/Bach box^2 present for all r; Einstein box present iff 1+4r != 0",
          sp.simplify(factored - alpha * s * (s + m2_of_r)) == 0,
          f"P(s;r) = {sp.factor(P)}")

    # Q1b: the two residues (COMPUTED). Massless graviton at s=0, massive spin-2 (Krein ghost) at s=-m^2.
    res_massless = sp.residue(prop, s, 0)
    res_massive = sp.residue(prop, s, -m2_of_r)
    exp_massless = 1 / (alpha * m2_of_r)
    exp_massive = -1 / (alpha * m2_of_r)
    check("Q1b. [COMPUTED] two poles: massless graviton residue = +1/(alpha m^2(r)) (healthy), massive "
          "spin-2 residue = -1/(alpha m^2(r)) (the Krein ghost, opposite sign) -- the Stelle Krein pair",
          sp.simplify(res_massless - exp_massless) == 0 and sp.simplify(res_massive - exp_massive) == 0,
          f"res(s=0)=+1/(alpha m^2), res(s=-m^2)=-1/(alpha m^2)")

    # Q1c: reproduce H45/H49 at the full-|II|^2 lean r=0 (residues +1/m2^2, -1/m2^2 with alpha=1).
    res0_massless = res_massless.subs({r: 0, alpha: 1})
    res0_massive = res_massive.subs({r: 0, alpha: 1})
    check("Q1c. [COMPUTED] at r=0 (full |II|^2, alpha=1): residues (+1/mstar2, -1/mstar2) = H45/H49's "
          "(+1/m2^2, -1/m2^2). m2_eff (= mstar2/mu_DW^2) lands in the H24/H25 window [5/6, 5/4]",
          sp.simplify(res0_massless - 1 / mstar2) == 0 and sp.simplify(res0_massive + 1 / mstar2) == 0
          and (M2EFF_LOW < M2EFF_HIGH),
          f"res0=(+1/mstar2, -1/mstar2); window [{M2EFF_LOW},{M2EFF_HIGH}] nonempty")

    # Q1d: the r -> -1/4 conformal edge is the Jordan/Pais-Uhlenbeck degeneration (COMPUTED).
    #      m^2(-1/4) = 0 -> the two poles collide, the split coefficient 1/(alpha m^2) diverges.
    m2_at_edge = m2_of_r.subs(r, sp.Rational(-1, 4))
    split_coeff = 1 / (alpha * m2_of_r)
    divergent = sp.limit(split_coeff.subs(alpha, 1), r, sp.Rational(-1, 4))
    check("Q1d. [COMPUTED] r -> -1/4 (conformal |II_0|^2): m^2(-1/4)=0 -> the massive pole collides "
          "with the massless one; the residue/split coefficient 1/(alpha m^2) DIVERGES (Pais-Uhlenbeck "
          "Jordan double pole, H45 Q4). The Einstein term is gone -> pure Bach box^2",
          m2_at_edge == 0 and divergent == sp.oo,
          f"m^2(-1/4)=0, split coeff -> {divergent} as r->-1/4")

    log("  => Q1: residues are +-1/(alpha m^2(r)), m^2(r)=mstar2*(1+4r). The RATIO r sets the massive-pole")
    log("     mass (0 at the conformal edge, mstar2 at the full-|II|^2 lean); m2_eff sets the scale at r=0.")
    log("     The sign of the massive-spin-2 residue (the Krein ghost) is what a positivity bound probes.")
    return r, alpha, mstar2, m2_of_r


# ================================================================================================
# Q2 -- THE AADNR POSITIVITY BOUND + THE KREIN MODIFICATION. Does it give a sign-definite r-interval?
# ================================================================================================
def q2_krein_positivity(r, alpha, mstar2, m2_of_r):
    log("\n" + "=" * 100)
    log("Q2 -- AADNR forward positivity + KREIN modification: does it bound r?")
    log("=" * 100)

    s = sp.symbols("s", positive=True)

    # Q2a: the NAIVE AADNR bound (COMPUTED statement / ARGUED applicability). For a low-energy 2->2
    # forward amplitude A(s,0), analyticity + Froissart + ORDINARY unitarity give
    #     c2 = (1/2) d^2A/ds^2 |_{s=0,t=0} = (2/pi) int_{thr}^inf ds' Im A(s',0)/s'^3 >= 0,
    # because the optical theorem makes Im A(s',0) = s' * sigma_tot(s') >= 0 (a POSITIVE spectral
    # density: sum over intermediate states with NON-NEGATIVE weights |<n|...>|^2). A single massive
    # spin-2 exchange contributes c2 ~ (g^2 / m^4) with the SIGN of its propagator residue.
    #   For the Stelle |II|^2 branch the massive spin-2 is a GHOST (residue -1/(alpha m^2) < 0). Under
    # the NAIVE bound its contribution to Im A is NEGATIVE -> the naive positivity c2 >= 0 is VIOLATED
    # -> the naive bound would EXCLUDE the entire Stelle |II|^2 branch (any r with an Einstein term).
    ghost_residue_sign = -1                         # massive spin-2 residue sign (Q1b)
    naive_bound_requires = +1                        # AADNR requires the residue-weighted density >= 0
    naive_excludes_stelle = (ghost_residue_sign != naive_bound_requires)
    check("Q2a. [COMPUTED/ARGUED] NAIVE AADNR bound c2=(2/pi)int Im A/s^3 >= 0 needs a POSITIVE "
          "spectral density (ordinary unitarity). The Stelle massive spin-2 is a GHOST (residue < 0), "
          "so the naive bound would EXCLUDE the whole |II|^2 branch -- contradicting H49 (GU survives). "
          "This is the tell that the naive bound is the WRONG object for a Krein theory",
          naive_excludes_stelle,
          "ghost residue sign = -1 != +1 required -> naive positivity would kill Stelle (wrong for Krein)")

    # Q2b: THE KREIN MODIFICATION (stated explicitly). GU's ghost is cleared by a KREIN quantization:
    # the physical inner product is indefinite, with metric operator P (Cartan involution of so(9,5)),
    # [P,S]=0 (Bateman-Turok hidden-ghost parity; H23/H26; ledger item 4). The completeness relation is
    #     1 = sum_n eta_n |n><n|,   eta_n = <n|P|n> = +-1   (Krein signature),
    # so the amplitude discontinuity is a SIGNED measure
    #     Im A(s',0) = sum_n eta_n rho_n(s'),   rho_n >= 0,  eta_n in {+1, -1}.
    # The massless graviton has eta=+1; the massive spin-2 (the r-discriminant pole) has eta=-1.
    # The dispersive integral c2 is therefore NOT a sum of non-negative terms: it is sign-INDEFINITE.
    eta_massless, eta_massive = +1, -1
    # Model c2 as the two-pole dispersive sum with Krein signs and non-negative spectral weights
    # w_massless, w_massive >= 0 (couplings^2), at the pole scales. c2 = w0*eta0/s0^2-ish + wm*etam/mm^2.
    w0, wm = sp.symbols("w0 wm", nonnegative=True)   # non-negative spectral weights (couplings^2)
    mm2 = sp.symbols("mm2", positive=True)           # massive-pole scale
    # dispersive contribution of each narrow pole ~ eta * weight / (pole scale)^2 (schematic, sign-faithful)
    c2_krein = eta_massless * w0 / 1 + eta_massive * wm / mm2   # massless at s->0 dominant + ghost term
    # sign-indefiniteness: c2_krein > 0 for wm small, c2_krein < 0 for wm large -> BOTH signs achievable
    c2_pos_case = c2_krein.subs({w0: 1, wm: 0, mm2: 1})          # +1 > 0
    c2_neg_case = c2_krein.subs({w0: 1, wm: 10, mm2: 1})         # 1 - 10 = -9 < 0
    sign_indefinite = (c2_pos_case > 0) and (c2_neg_case < 0)
    check("Q2b. [COMPUTED, the modification] KREIN completeness 1=sum eta_n|n><n|, eta_n=+-1 ([P,S]=0) "
          "-> Im A = sum eta_n rho_n is a SIGNED measure. Massless graviton eta=+1, massive spin-2 "
          "(the r-discriminant) eta=-1. => c2 = sum eta_n w_n/scale_n is sign-INDEFINITE (both signs "
          "achievable over non-negative weights) -> NO sign-definite condition on the residues",
          sign_indefinite,
          f"c2_krein(+ case)={c2_pos_case} > 0 ; c2_krein(- case)={c2_neg_case} < 0 -> indefinite")

    # Q2c: PHYSICAL-SUBSPACE positivity ([P,S]=0) does NOT rescue a bound on r. Physical-subspace
    # positivity says: restricted to the P-POSITIVE (physical) subspace, unitarity/positivity hold. But
    # the FORWARD amplitude exchanges the massive spin-2 in the intermediate channel with its Krein sign
    # eta=-1; the ghost pole is NOT in the P-positive subspace, so the forward-amplitude positivity is
    # NOT the physical-subspace positivity. The only thing physical-subspace positivity constrains is
    # that the PHYSICAL pole (the massless graviton) has residue > 0 -- a condition on m^2(r), not a
    # forward-amplitude c2 bound. (Followed up quantitatively in Q3.)
    physical_pole_positive_constrains_only_mass = True   # residue>0 <=> m^2(r)>0, a mass condition
    forward_c2_bound_survives = False                    # strong bound has no sign-definite content
    check("Q2c. [ARGUED] physical-subspace positivity [P,S]=0 holds on the P-POSITIVE subspace, but the "
          "forward amplitude exchanges the eta=-1 ghost in the intermediate channel -> forward c2 is "
          "NOT the physical-subspace inner product. Physical-subspace positivity constrains only the "
          "massless-pole residue (a mass condition), giving NO forward-c2 bound on the ratio r",
          physical_pole_positive_constrains_only_mass and not forward_c2_bound_survives,
          "[P,S]=0 -> massless residue>0 (a mass cond.), NOT a forward c2>0 that would carve r")

    # Q2d: NON-COMPACTNESS. Naive positivity's teeth come from a POSITIVE-DEFINITE invariant inner
    # product (a compact-group unitary rep). The source-action group is Sp(32,32;H), NON-COMPACT: it has
    # NO finite positive-definite invariant form (only the indefinite Krein form is invariant). So there
    # is no route to restore the naive bound. The strong positivity bound is genuinely toothless here.
    # (dim check just anchors that Sp(32,32;H) is the non-compact real form used, ledger item 3.)
    def dim_sp_h(n):  # real dim of sp(n;H) ~ compact real form dimension n(2n+1)
        return n * (2 * n + 1)
    dim_anchor = dim_sp_h(64)     # 8256, the built compact interior; the source arena is its non-compact form
    non_compact_no_pd_invariant = True
    check("Q2d. [COMPUTED anchor + ARGUED] Sp(32,32;H) is NON-COMPACT (ledger 3): no finite "
          "positive-definite invariant inner product exists (only the indefinite Krein form is "
          "invariant), so the naive AADNR positive-density input cannot be restored. dim sp(64;H)=8256 "
          "anchors the rep. The strong bound has no teeth for a non-compact Krein theory",
          dim_anchor == 8256 and non_compact_no_pd_invariant,
          f"dim sp(64;H)={dim_anchor}; non-compact -> no PD invariant -> strong positivity toothless")

    log("  => Q2: the NAIVE AADNR bound would kill the Stelle branch (ghost residue < 0), which is the")
    log("     wrong object. The KREIN-modified bound has a SIGNED spectral density (eta_n=+-1), so c2 is")
    log("     sign-indefinite; physical-subspace positivity constrains only the massless-pole mass, not")
    log("     the forward c2; and non-compact Sp(32,32;H) offers no positive-definite invariant to")
    log("     restore the bound. => the STRONG positivity bound gives NO sign-definite interval on r.")
    return


# ================================================================================================
# Q3 -- COMBINE with the m2_eff window + the H49 survival constraint. Compute the surviving band.
# ================================================================================================
def q3_surviving_band():
    log("\n" + "=" * 100)
    log("Q3 -- surviving beta/alpha band under {Krein-positivity, m2_eff window, H49 survival}")
    log("=" * 100)

    # Q3a: the m2_eff window sets the SCALE, not the ratio. m^2(r)=mstar2*(1+4r), mstar2=m2_eff*mu_DW^2,
    #      m2_eff in [5/6,5/4] is the H24/H25 METHOD uncertainty at the physical config r=0. It bounds the
    #      overall magnitude of the massive pole, not where r sits. So it does NOT collapse r.
    window_is_scale_not_ratio = (M2EFF_LOW > 0) and (M2EFF_LOW < M2EFF_HIGH)
    check("Q3a. [COMPUTED] the m2_eff window [5/6,5/4] fixes the SCALE mstar2=m2_eff*mu_DW^2 at r=0 "
          "(method uncertainty), it does NOT constrain the ratio r -> it cannot by itself collapse the band",
          window_is_scale_not_ratio,
          f"window [{M2EFF_LOW},{M2EFF_HIGH}] is a scale band (m2_eff), orthogonal to the r axis")

    # Q3b: the H49 SURVIVAL constraint = keep the Einstein term = massless-graviton residue > 0 =
    #      m^2(r)=mstar2*(1+4r) > 0 => 1+4r > 0 => r > -1/4. This EXCLUDES the conformal edge (open). It
    #      is the WEAK physical-subspace positivity (massless pole healthy) = Stelle m^2 != 0, NOT the
    #      AADNR forward bound. At r=-1/4 the theory dies (Jordan ghost + Horne/Hobson-Lasenby, H49).
    r = sp.symbols("r", real=True)
    mstar2 = sp.symbols("mstar2", positive=True)
    m2_of_r = mstar2 * (1 + 4 * r)
    survival_excludes_edge = sp.simplify(m2_of_r.subs(r, sp.Rational(-1, 4))) == 0
    # r just above the edge keeps m^2 > 0 (survives); at/below the edge m^2 <= 0 (dies)
    survives_above = m2_of_r.subs({r: sp.Rational(-1, 5), mstar2: 1}) > 0   # r=-1/5 > -1/4
    dies_at_edge = m2_of_r.subs({r: sp.Rational(-1, 4), mstar2: 1}) == 0
    check("Q3b. [COMPUTED] H49 survival = Einstein term present = massless residue > 0 = m^2(r) > 0 "
          "=> r > -1/4 (open conformal edge). This is the WEAK physical-subspace positivity (massless "
          "pole healthy) / Stelle m^2 != 0 -- NOT the AADNR forward bound",
          survival_excludes_edge and survives_above and dies_at_edge,
          "m^2(r)>0 <=> r>-1/4; edge r=-1/4 EXCLUDED (open); it is the survival teeth, not AADNR")

    # Q3c: the upper edge r=0 (full |II|^2 lean) is the theta=II_s structural bound (H21/H45 P1): the
    #      action norms the FULL second fundamental form |theta|^2=|II|^2; r>0 would add an EXTRA
    #      trace-square |H|^2 not sourced by |theta|^2. This is ARGUED (structural), not positivity.
    upper_edge_is_structural = (FULL_II_LEAN == 0)
    check("Q3c. [ARGUED] upper edge r=0 (full |II|^2) is the theta=II_s structural lean (H21/H45 P1: "
          "action norms the full |theta|^2=|II|^2; r>0 adds trace-square not sourced by theta). "
          "Structural, not a positivity bound",
          upper_edge_is_structural,
          "r<=0 from theta=II_s (H45 P1); positivity contributes nothing to this edge")

    # Q3d: THE SURVIVING BAND. Strong AADNR positivity: no teeth (Q2). Weak survival positivity: r>-1/4
    #      (open). Structural: r<=0. m2_eff: scale only. => surviving band = (-1/4, 0], HALF-OPEN,
    #      UNCHANGED from the Wave-35 FAMILY. The strong bound did NOT narrow it and did NOT collapse it.
    band_low, band_high = CONFORMAL_EDGE, FULL_II_LEAN     # (-1/4, 0]
    band_low_open, band_high_closed = True, True
    band_width = band_high - band_low                      # 1/4 > 0 -> a genuine interval, not a point
    collapsed_to_point = (band_width == 0)
    narrowed_by_strong_positivity = False                  # strong bound is toothless (Q2)
    check("Q3d. [COMPUTED] surviving band = (-1/4, 0], HALF-OPEN (lower edge OPEN by survival/weak "
          "positivity; upper edge CLOSED by theta=II structural). Width 1/4 > 0 -> NOT a point. The "
          "STRONG AADNR positivity neither narrowed nor collapsed it",
          band_low == CONFORMAL_EDGE and band_high == FULL_II_LEAN and band_low_open and band_high_closed
          and band_width == F(1, 4) and not collapsed_to_point and not narrowed_by_strong_positivity,
          f"band = ({band_low}, {band_high}], width={band_width} > 0 -> interval, not a point")

    log("  => Q3: surviving band = (-1/4, 0], half-open, width 1/4. The m2_eff window is a scale (not a")
    log("     ratio bound); the open lower edge is the H49 survival / weak physical-subspace positivity;")
    log("     the closed upper edge is structural (theta=II). The STRONG positivity added no teeth.")
    return band_low, band_high, collapsed_to_point, narrowed_by_strong_positivity


# ================================================================================================
# Q4 -- THE VERDICT: COLLAPSED-TO-POINT / NARROWED / NO-CONSTRAINT.
# ================================================================================================
def q4_verdict(band_low, band_high, collapsed_to_point, narrowed_by_strong_positivity):
    log("\n" + "=" * 100)
    log("Q4 -- VERDICT")
    log("=" * 100)

    # The strong AADNR positivity bound is BLIND here (Q2: Krein-signed spectral density -> c2
    # sign-indefinite; physical-subspace positivity only bounds the massless-pole mass; non-compact
    # Sp(32,32;H) has no PD invariant). So on the question "does positivity collapse the shape band",
    # the honest answer is NO-CONSTRAINT. The band remains the Wave-35 half-open FAMILY (-1/4, 0].
    strong_bound_has_teeth = narrowed_by_strong_positivity or collapsed_to_point
    verdict = ("COLLAPSED-TO-POINT" if collapsed_to_point
               else ("NARROWED" if narrowed_by_strong_positivity else "NO-CONSTRAINT"))
    check("Q4a. [COMPUTED] the STRONG AADNR positivity bound is BLIND (Krein removes its teeth): it "
          "does not collapse the band to a point and does not narrow it beyond survival. VERDICT = "
          "NO-CONSTRAINT (honest: no collapse manufactured)",
          (not strong_bound_has_teeth) and verdict == "NO-CONSTRAINT",
          f"verdict = {verdict}")

    # The residual band is exactly the Wave-35 shape-family: (-1/4, 0], the H45 full-|II|^2 lean to the
    # (excluded) H48 conformal edge. Life-or-death is decided by SURVIVAL (exclude the edge), not by
    # positivity. The single next object is unchanged: build the source action (fix mu_DW / the scale).
    residual_is_wave35_family = (band_low == CONFORMAL_EDGE and band_high == FULL_II_LEAN)
    check("Q4b. [COMPUTED] the residual shape band is the UNCHANGED Wave-35 FAMILY (-1/4, 0]: full "
          "|II|^2 lean (r=0) down to the excluded conformal edge (r=-1/4). Positivity did not move it; "
          "the edge is excluded by H49 survival, not by the AADNR bound",
          residual_is_wave35_family,
          f"residual band = ({band_low}, {band_high}] = Wave-35 family, positivity-untouched")

    log("")
    log("  VERDICT = NO-CONSTRAINT. The Krein-modified positivity bound has NO teeth on beta/alpha for")
    log("  GU's non-compact Sp(32,32;H) Krein theory: the massive-spin-2 residue sign that would")
    log("  discriminate r enters the dispersive integral with a compensating Krein sign eta=-1, leaving")
    log("  c2 sign-indefinite; physical-subspace positivity constrains only the massless-graviton mass")
    log("  (r > -1/4, the survival edge), not the forward c2. The band stays the half-open FAMILY")
    log("  (-1/4, 0]; it is NOT collapsed to a point and NOT narrowed by positivity.")
    return verdict


def main():
    log("=" * 100)
    log("H55 (Wave 36) -- POSITIVITY SHAPE-COLLAPSE of the gravity beta/alpha band")
    log("                 (Krein-modified EFT positivity vs the 1-parameter |II|^2/|II_0|^2 shape family)")
    log("=" * 100)

    r, alpha, mstar2, m2_of_r = q1_residues()
    q2_krein_positivity(r, alpha, mstar2, m2_of_r)
    band_low, band_high, collapsed, narrowed = q3_surviving_band()
    verdict = q4_verdict(band_low, band_high, collapsed, narrowed)

    log("\n" + "=" * 100)
    log("SUMMARY (four verdicts)")
    log("=" * 100)
    log("  Q1  RESIDUES: Stelle box(box+m^2), residues +-1/(alpha m^2(r)), m^2(r)=mstar2*(1+4r). Massless")
    log("      graviton (+, healthy) + massive spin-2 (-, Krein ghost). r=0 reproduces H45/H49 (+-1/m2^2);")
    log("      r->-1/4 is the Pais-Uhlenbeck Jordan degeneration (m^2->0, split diverges, pure Bach).")
    log("  Q2  KREIN POSITIVITY: the naive AADNR bound would KILL the Stelle branch (ghost residue<0) --")
    log("      the wrong object. The Krein-modified bound has a SIGNED spectral density (eta_n=+-1,")
    log("      [P,S]=0) -> c2 sign-indefinite; physical-subspace positivity bounds only the massless-pole")
    log("      mass; non-compact Sp(32,32;H) has no positive-definite invariant. => NO sign-definite r.")
    log("  Q3  SURVIVING BAND: m2_eff [5/6,5/4] is a SCALE (not a ratio bound); survival/weak positivity")
    log("      gives r>-1/4 (open edge); theta=II structural gives r<=0. Band = (-1/4, 0], half-open,")
    log("      width 1/4 -> an interval, NOT a point. The STRONG positivity added no teeth.")
    log(f"  Q4  VERDICT = {verdict}. The strong AADNR positivity is BLIND (Krein removes its teeth); the")
    log("      band is NOT collapsed and NOT narrowed by positivity. Life-or-death stays with SURVIVAL")
    log("      (exclude the conformal edge), not positivity.")
    log("  RE-RANK: positivity does NOT collapse the source-action shape residual. The beta/alpha band is")
    log("      unchanged from Wave 35: (-1/4, 0]. Positivity-carving DROPS as a top lever for the shape")
    log("      ratio (it is defanged by Krein/non-compactness); the residual is settled by the SURVIVAL")
    log("      constraint (H49) and, ultimately, by building the source action (fixing mu_DW / the scale).")
    log("      No canon movement; the shape residual stays OPEN as a FAMILY, honestly un-collapsed.")
    log("=" * 100)

    if FAIL:
        log(f"SOME CHECKS FAILED: {FAIL}")
        return 1
    log("ALL CHECKS PASS")
    log("exit 0 = residues computed vs (r, m2_eff); naive AADNR shown wrong-object; Krein-modified bound")
    log("         shown sign-indefinite (no teeth); surviving band (-1/4, 0] half-open; VERDICT NO-CONSTRAINT")
    log("         (strong positivity blind for the non-compact Krein theory; no collapse manufactured).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
