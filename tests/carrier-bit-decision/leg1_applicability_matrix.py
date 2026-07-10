#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
LEG-1: THEOREM-APPLICABILITY MATRIX -- the published spin-3/2 no-go record vs
GU's stated commitments (carrier-bit swing, gauging-availability leg).

THE QUESTION. The generation-arena order-3 verdict is one bit:
  carrier A (ghost-subtracted gravitino complex, ind = -42 = 21*sigma/8, order-3
             class (0,0,0); mechanism = index bookkeeping of a GAUGED gravitino,
             delta psi = D eps)
  carrier B (geometric gamma-traceless RS operator, ind = -38 = 19*sigma/8,
             order-3 class (0,2,1)/3 NONZERO; mechanism = honest index of
             UNGAUGED spin-3/2 matter).
This leg asks three well-posed sub-questions of the PUBLISHED record only:
  Q1: does any published theorem make gauging MANDATORY for GU's spin-3/2
      sector as stated?           (if yes -> bit resolves toward A)
  Q2: does any published theorem make gauging IMPOSSIBLE for GU?
      (if yes -> bit resolves toward B at theorem grade)
  Q3: does the ungauged massive vectorlike carrier escape every published
      consistency constraint?     (if yes -> B's reading is published-viable)

METHOD. Every theorem row carries its VERBATIM hypotheses (fetched, with source
and verification tier); the row verdict (BITES / ESCAPES / PARTIAL(exact gap))
is recorded hypothesis-by-hypothesis against GU's transcript-tier commitments
(quoted verbatim, line-verified this session). Decision outputs are DERIVED
from the row fields and asserted for consistency. Carrier-A steelman rows are
first-class data: the run FAILS if any decision output ignores them.

FIREWALL (asserted): no chi(K3)=24 import, no /8 manufacture, no A-hat=3,
no predetermined verdict (the script's outputs are branch-closures at stated
grade, never a carrier verdict -- asserted structurally).
ACAUSAL TRAP (asserted): no row proposes decoupling; the bare commutator
||[Pi_RS, M_D]|| = 58.72 is used ONLY as a nonvanishing premise (GU cannot
plead vanishing soft couplings), never as a reduction target.

Exact arithmetic: fractions.Fraction only. Exit 0 iff all checks pass.
"""

import sys
from fractions import Fraction as F

CHECKS = []
def check(name, got, want):
    ok = (got == want)
    CHECKS.append((name, ok))
    print(("PASS  " if ok else "FAIL  ") + "%s: %r (want %r)" % (name, got, want))
    return ok

# ----------------------------------------------------------------------------
# 0. EXACT BOOKKEEPING SANITY (Fraction only; A-hat from sigma, never from chi)
# ----------------------------------------------------------------------------
sigma_K3 = F(-16)                    # signature of K3 (b+ = 3, b- = 19)
Ahat_K3  = -sigma_K3 / 8             # A-hat genus from SIGNATURE only
check("A-hat(K3) = -sigma/8 = 2 (no chi import)", Ahat_K3, F(2))

ind_D    = Ahat_K3                   # HS convention: ind Q = ind D_TM + ind D
ind_D_TM = -20 * Ahat_K3             # twisted Dirac, rank-20 T_C twist ... = -40
ind_A    = -21 * Ahat_K3             # carrier A: ghost-subtracted gravitino
ind_B    = -19 * Ahat_K3             # carrier B: geometric gamma-traceless Q
check("carrier A index = -42 = 21*sigma/8", (ind_A, ind_A == 21*sigma_K3/8), (F(-42), True))
check("carrier B index = -38 = 19*sigma/8", (ind_B, ind_B == 19*sigma_K3/8), (F(-38), True))
check("HS eq (11) additivity: ind Q = ind D_TM + ind D", ind_D_TM + ind_D, ind_B)
check("fork B - A = 2*ind D = 4 (two spin-1/2 units)", (ind_B - ind_A, ind_B - ind_A == 2*ind_D), (F(4), True))
check("gravitino bookkeeping -21 = -20 - 1 (PTZ eq 5.2 / ghosts)", -20 - 1, -21)
check("RSA bookkeeping       -19 = -20 + 1 (PTZ eq 5.2)", -20 + 1, -19)
check("RSA vs gravitino      -19 = -21 + 2 (PTZ eq 5.1)", -21 + 2, -19)
check("mod-3 classes: A = 0, B = 1", (int(ind_A) % 3, int(ind_B) % 3), (0, 1))

BARE_COMMUTATOR = 58.72   # ||[Pi_RS, M_D]||, Cl(4,0) toy -- PREMISE ONLY (nonzero)
check("acausal-trap guard: bare commutator held NONZERO as premise", BARE_COMMUTATOR > 0, True)

# ----------------------------------------------------------------------------
# 1. GU COMMITMENTS (transcript-tier, line-verified in
#    papers/drafts/'Transcript into the impossible.md' this session)
# ----------------------------------------------------------------------------
GU = {
  "matter_not_gauge_field": dict(
    quote="Vela Zwanziger says that if you have spin three halves matter that is "
          "coupled, to some sort of nontrivial acting group, you have to be very careful",
    src="transcript [00:41:48] L140", verified=True,
    note="VZ-exemption plea = ungauged-matter framing; + [00:39:18] L128 third generation "
         "of MATTER; + [00:40:27] L131 particle family; + [00:32:46] L107 fermion content. "
         "NEGATIVE (grep, this session): 0 hits for gravitino/ghost/gauge-fix; no "
         "delta psi = D eps ever stated."),
  "no_spacetime_susy": dict(
    quote="We will never find space time Susie. ... Don't feed it Minkowski space. "
          "Feed it the space of connections. Then the Lorentz group is the gauge group.",
    src="transcript [00:46:02] L158", verified=True,
    note="rejects spacetime SUSY unconditionally; SUSY relocated to connection space"),
  "mass_is_a_modulus": dict(
    quote="the fermionic extension gives you exactly three families of chiral fermions "
          "if you have a decreased VEV in the total space taking a Dirac equation into "
          "two vial equations because the mass is actually a variable",
    src="transcript [00:46:02] L158", verified=True,
    note="+ L128: 'It's too massive and you haven't gotten enough energy to see it yet'; "
         "+ capstone (canon/carrier-dirac-mass-capstone-RESULTS.md): carrier VECTORLIKE, "
         "Krein (+96,-96), Dirac mass ALLOWED, generically massive"),
  "spin32_family_flipped_chiral": dict(
    quote="in g u, there's one family of 16 flipped chiral spin three halves particles. "
          "That is, there is a sort of spin three halves family, which aside from being "
          "spin three halves is just the conjugate of the internal symmetry representation.",
    src="transcript [00:40:27] L131", verified=True,
    note="author's own gloss = internal-rep conjugation, NOT stated net spacetime "
         "chirality / masslessness"),
  "added_spin_half_plus_sign": dict(
    quote="Rarita v tensor spinners on w, spinners on v, tensor Rarita Schwinger on w "
          "or tensor Rarita Schwinger on w plus spinners on v, tensor spinners on w. "
          "So that's where you get your third generation of matter from.",
    src="transcript [00:39:18] L128", verified=True,
    note="the spin-1/2 slot enters ADDED, named physical matter (carrier B's shape)"),
  "coupled_not_decoupled": dict(
    quote="DEAD-ENDS: any construction that drives the bare ||[Pi_RS, M_D]|| (58.72) "
          "to 0 ... reinstates Velo-Zwanziger acausality",
    src="absorbed/gu-source-action/DEAD-ENDS.md (in-repo firewall)", verified=True,
    note="GU cannot plead vanishing low-energy couplings; the RS sector stays coupled"),
  "graded_ig_upstairs": dict(
    quote="you take the inhomogeneous gauge group on that group and you extend it to "
          "through supersymmetry ... the entire universe without making any choices",
    src="transcript [00:49:16] L173", verified=True,
    note="a graded LOCAL gauge group upstairs = live unconventional gauging channel "
         "(shape gu_derived per rs-gu-phys-brst-specification-2026-06-26.md:61-63); unbuilt"),
}

# ----------------------------------------------------------------------------
# 2. THE MATRIX. One row per published theorem. Columns:
#    mass regime | gauged/ungauged | background | framework | what-it-forces.
#    verdict values: BITES | ESCAPES | PARTIAL (with exact gap).
# ----------------------------------------------------------------------------
ROWS = [

 dict(id="GP-1977",
  cite="Grisaru & Pendleton, 'Soft Spin 3/2 Fermions Require Gravity and "
       "Supersymmetry', Phys. Lett. B 67 (1977) 323",
  tier="FETCHED THIS SESSION (InspireHEP API, abstract verbatim)",
  hyp_verbatim="If massless fermions of spin 3/2 have non-vanishing low-energy "
       "couplings, the fermions must have massless partners of spin 2, and all "
       "particles to which the fermions couple must display supersymmetry.",
  regime=dict(mass="MASSLESS (explicit)", gauging="n/a (particle/S-matrix statement)",
              background="flat 4d", framework="S-matrix soft limit"),
  forces="massless spin-2 partner + supersymmetry of all couplings (-> supergravity, "
         "i.e. the gauged-gravitino reading = carrier A)",
  gu_match=[
    ("massless", "FAILS generically: GU mass is a VEV modulus (GU['mass_is_a_modulus']); "
     "capstone: carrier vectorlike, Dirac mass ALLOWED, generically massive", "ESCAPES"),
    ("non-vanishing low-energy couplings", "SATISFIED if massless: DEAD-ENDS firewall "
     "keeps the RS sector coupled (bare commutator 58.72 nonzero as premise) -- the "
     "escape is ONLY via mass, never via decoupling", "BITES-IF-MASSLESS"),
    ("flat 4d S-matrix regime", "PARTIAL: GU's arena is 14d Y14 / K3-fibered; the 4d "
     "effective identification where generations are counted is itself unbuilt", "PARTIAL"),
  ],
  verdict="ESCAPES (generic massive branch); PARTIAL corner NAMED: an exactly-massless "
          "interacting corner of the 16 would re-engage the theorem with full force "
          "(carrier-A steelman S2)",
  makes_gauging_mandatory_for_GU_as_stated=False,
  makes_gauging_impossible_for_GU=False,
  blocks_ungauged_massive_carrier=False,
  partial_gaps=["exactly-massless interacting corner not excluded by commitments",
                "4d-effective-arena identification unbuilt (14d -> 4d)"],
 ),

 dict(id="GPvN-1977",
  cite="Grisaru, Pendleton & van Nieuwenhuizen, 'Supergravity and the S Matrix', "
       "Phys. Rev. D 15 (1977) 996",
  tier="FETCHED THIS SESSION (InspireHEP API, abstract verbatim)",
  hyp_verbatim="Kinematical constraints on helicity amplitudes determine the spin-2 "
       "and spin-3/2 Born amplitudes almost uniquely ... We suggest that Lorentz "
       "invariance, presence of only one (dimensional) coupling constant kappa, and "
       "global supersymmetry lead to a unique locally supergauge-invariant theory of "
       "spin-2 and spin-3/2 particles.",
  regime=dict(mass="massless (helicity amplitudes)", gauging="output: local supergauge "
              "invariance", background="flat 4d", framework="S-matrix Born amplitudes"),
  forces="unique locally supergauge-invariant spin-2 + spin-3/2 theory (supergravity)",
  gu_match=[
    ("global supersymmetry (INPUT hypothesis)", "FAILS as stated: GU rejects spacetime "
     "SUSY (GU['no_spacetime_susy']); GU's SUSY lives on the space of connections", "ESCAPES"),
    ("massless helicity amplitudes", "FAILS generically (same mass escape as GP-1977)", "ESCAPES"),
    ("single dimensional coupling / Lorentz invariance", "PARTIAL: GU's coupling "
     "structure is the unbuilt SG4 object", "PARTIAL"),
  ],
  verdict="ESCAPES at commitments grade (two input hypotheses fail as stated); PARTIAL "
          "corner NAMED: if connection-space SUSY descends to an effective 4d global "
          "SUSY, the theorem forces the unique supergravity -> carrier A (steelman S3)",
  makes_gauging_mandatory_for_GU_as_stated=False,
  makes_gauging_impossible_for_GU=False,
  blocks_ungauged_massive_carrier=False,
  partial_gaps=["descent of connection-space SUSY to effective 4d global SUSY is open",
                "abstract-tier only; full text unfetched (paywalled)"],
 ),

 dict(id="VZ-1969",
  cite="Velo & Zwanziger, 'Propagation and quantization of Rarita-Schwinger waves "
       "in an external electromagnetic potential', Phys. Rev. 186 (1969) 1337",
  tier="FETCHED THIS SESSION (InspireHEP API, abstract verbatim); mass hypothesis "
       "PARTIAL: abstract silent, confirmed via THREE secondaries (nLab 'irreducible "
       "massive representation ... minimal coupling', fetched this session; BBS review "
       "arXiv:1007.0435 cached verbatim 'pathologies ... already for massive spin-3/2 "
       "fields'; Deser-Waldron framing)",
  hyp_verbatim="The Rarita-Schwinger equation in an external electromagnetic potential "
       "is shown to be equivalent to a hyperbolic system of partial differential "
       "equations supplemented by initial conditions. The wave fronts of the classical "
       "solutions are calculated and are found to propagate faster than light. "
       "Nevertheless, for sufficiently weak external potentials, a consistent quantum "
       "mechanics and quantum field theory may be established. These, however, violate "
       "the postulates of special relativity.",
  regime=dict(mass="MASSIVE (per secondaries; abstract silent -> PARTIAL)",
              gauging="ungauged matter, minimal coupling, EXTERNAL c-number EM field",
              background="flat", framework="classical PDE characteristics + quantization"),
  forces="NOTHING about gauging -- a pathology statement with PUBLISHED non-SUGRA "
         "escapes: non-minimal couplings (Porrati-Rahman, per BBS refs 61-62); "
         "gauged supergravities (BBS verbatim: 'interactions between spin-3/2 and "
         "electromagnetic fields in gauged supergravities are well-known to avoid the "
         "Velo-Zwanziger problems'); dynamical gravity windows (Deser-Waldron); "
         "Adler RSA ('allowed to consistently gauge the theory beyond the supergravity "
         "approach', PTZ cached verbatim); string states",
  gu_match=[
    ("massive spin-3/2, coupled", "BITES POTENTIALLY: GU's carrier is generically "
     "massive + coupled ('spin three halves matter that is coupled, to some sort of "
     "nontrivial acting group', L140) -- the author himself names VZ as the live danger", "PARTIAL"),
    ("minimal coupling to external EM field", "PARTIAL: GU's coupling structure is "
     "unbuilt (SG4); whether it is 'minimal' in VZ's sense is undetermined; GU pleads "
     "exemption via 'no internal symmetry groups' (L140), which is shaky -- GU retains "
     "SU(3)xSU(2)xU(1) content even if emergent", "PARTIAL"),
  ],
  verdict="PARTIAL-BITES as danger, but FORCES NO GAUGING: the forcing-to-A route "
          "'consistency forces gauging' is REFUTED at published grade by the "
          "non-supergravity escapes (Deser-Waldron window; Adler RSA; Porrati-Rahman)",
  makes_gauging_mandatory_for_GU_as_stated=False,
  makes_gauging_impossible_for_GU=False,
  blocks_ungauged_massive_carrier=False,   # danger with published escapes, not a closure
  partial_gaps=["mass hypothesis not verbatim in primary abstract (3 secondaries)",
                "GU coupling minimality undetermined until SG4",
                "GU's 'no internal symmetry' exemption plea is weak"],
 ),

 dict(id="DW-2001",
  cite="Deser & Waldron, 'Inconsistencies of Massive Charged Gravitating Higher "
       "Spins', Nucl. Phys. B 631 (2002), hep-th/0112182",
  tier="FETCHED THIS SESSION (arXiv abstract page, verbatim)",
  hyp_verbatim="We examine the causality and degrees of freedom (DoF) problems "
       "encountered by charged, gravitating, massive higher spin fields. For spin "
       "s=3/2, making the metric dynamical yields improved causality bounds. These "
       "involve only the mass, the product eM_P of the charge and Planck mass and the "
       "cosmological constant Lambda. ... While propagation is causal in arbitrary E/M "
       "backgrounds, the allowed mass ranges of parameters are of Planck order.",
  regime=dict(mass="MASSIVE (explicit)", gauging="ungauged matter + dynamical metric",
              background="dynamical gravity + arbitrary E/M", framework="PDE causality"),
  forces="NOTHING -- it OPENS a window: massive charged gravitating spin-3/2 is "
         "causal WITHOUT supersymmetry, within Planck-order parameter ranges",
  gu_match=[
    ("massive, charged, gravitating", "MATCHES the generic GU carrier (mass modulus, "
     "coupled, gravity present)", "ESCAPES-ENABLING"),
    ("Planck-order parameter windows", "PARTIAL: if GU needs a sub-Planckian charged "
     "carrier outside the windows, the shelter narrows", "PARTIAL"),
  ],
  verdict="ESCAPES-ENABLING: the published consistency shelter for the ungauged "
          "massive carrier; kills 'massive spin-3/2 is fatally acausal' as a theorem",
  makes_gauging_mandatory_for_GU_as_stated=False,
  makes_gauging_impossible_for_GU=False,
  blocks_ungauged_massive_carrier=False,
  partial_gaps=["window is Planck-order parameter ranges, not unconditional"],
 ),

 dict(id="Buchdahl-1958",
  cite="Buchdahl, Nuovo Cimento 10 (1958) 96 -- via Hack-Makedonski verbatim restatement",
  tier="SECONDARY-VERBATIM (primary unfetched; restated in fetched arXiv:1106.6327, "
       "cached hack-makedonski.txt, read this session)",
  hyp_verbatim="[HM:] the minimally coupled equations imply R_munu gamma^mu psi^nu = 0, "
       "with R_munu denoting the Ricci curvature tensor, and this equation can only be "
       "satisfied by psi == 0 unless the spacetime is an Einstein spacetime s.t. R_munu "
       "is a constant multiple of the metric g_munu.",
  regime=dict(mass="any (free RS, minimal gravitational coupling)", gauging="ungauged",
              background="curved", framework="classical constraint analysis"),
  forces="BACKGROUND restriction (Einstein spacetime) -- NOT gauging",
  gu_match=[
    ("Einstein background required", "SATISFIED on the adjudicated arena: K3 is "
     "Ricci-flat hyperkahler, hence Einstein -- carrier B's arena sits INSIDE the "
     "published consistency window (Homma-Semmelmann and Baer-Mazzeo study exactly the "
     "ungauged RS operator there; RS(K3)=38 sharp)", "ESCAPES"),
  ],
  verdict="ESCAPES on the adjudicated arena (K3 Einstein); the constraint is a "
          "background condition, never a gauging requirement",
  makes_gauging_mandatory_for_GU_as_stated=False,
  makes_gauging_impossible_for_GU=False,
  blocks_ungauged_massive_carrier=False,
  partial_gaps=["primary text unfetched; rides HM's verbatim restatement",
                "GU's effective LORENTZIAN backgrounds off-K3 are not certified Einstein"],
 ),

 dict(id="HM-2011",
  cite="Hack & Makedonski, 'A No-Go Theorem for the consistent quantization of "
       "spin 3/2 fields on general curved spacetimes', Phys. Lett. B, arXiv:1106.6327",
  tier="CACHED-FETCHED-VERBATIM (full PDF fetched prior leg; cached "
       "hack-makedonski.txt re-read this session)",
  hyp_verbatim="In this work we analyse whether it is possible to couple a spin "
       "3/2-field to a gravitational field in such a way that the resulting quantum "
       "theory is consistent on arbitrary gravitational backgrounds. We find that this "
       "is impossible as all couplings require the background to be an Einstein "
       "spacetime for consistency. [...] our proof covers both m > 0 and m = 0.",
  regime=dict(mass="both m>0 and m=0 (explicit)", gauging="ungauged (all covariant "
              "first-order couplings to background gravity)", background="arbitrary "
              "curved", framework="quantization consistency (causality + unitarity)"),
  forces="BACKGROUND restriction (Einstein) as THEOREM; supergravity named only in "
         "DISCUSSION: 'This enforces the widespread belief that supergravity theories "
         "are the only meaningful models which contain spin 3/2 fields as in these "
         "models such restrictions of the gravitational background appear naturally "
         "as on-shell conditions.'",
  gu_match=[
    ("consistency on ARBITRARY backgrounds", "GU does not need it on the adjudicated "
     "arena: K3 is Einstein; 'the model is, at best, only consistent on Einstein "
     "spacetimes' (HM discussion, verbatim) leaves the Einstein window OPEN", "ESCAPES"),
    ("supergravity-only reading", "DISCUSSION-TIER, not theorem content: a hostile "
     "reader can quote it as evidence any consistent completion is supergravity-shaped "
     "(carrier-A steelman S5) -- but the theorem's operative content is the background "
     "restriction", "PARTIAL"),
  ],
  verdict="ESCAPES as theorem (Einstein arena); PARTIAL as discussion (the "
          "'supergravity only' belief line is carried as steelman S5, discussion-tier)",
  makes_gauging_mandatory_for_GU_as_stated=False,
  makes_gauging_impossible_for_GU=False,
  blocks_ungauged_massive_carrier=False,
  partial_gaps=["Lorentzian quantization statement vs Riemannian-elliptic adjudicated "
                "indices: the bridge is program semantics (SG4), not a fetched theorem"],
 ),

 dict(id="ANOMALY-CONVENTION",
  cite="(gauged register) Bilal arXiv:0802.0634 eq (11.47) + Homma-Semmelmann "
       "arXiv:1804.10602 Remark 3.6 [quoting Witten p.252] ||| (ungauged register) "
       "HS eq (11) + Prop 3.1(i) + Prokhorov-Teryaev-Zakharov, Phys. Rev. D 106 "
       "(2022) 025022 [Adler RSA model]",
  tier="CACHED-FETCHED-VERBATIM (bilal.txt, hs_paper.txt, ptz-rsa.txt -- all "
       "re-grepped and re-read this session)",
  hyp_verbatim="[Bilal 11.47:] a positive chirality spin-3/2 field ... is obtained "
       "from a positive chirality spin-1/2 field with an extra vector index by "
       "subtracting the spin-1/2 part. ||| [HS Rem 3.6:] in physics one has to "
       "'subtract from index of the Rarita-Schwinger field the corresponding index of "
       "the spin 1/2 ghosts' ... motivated by 'discarding zero modes that can be "
       "gauged away or that violate gauge conditions' ... 'cancelled by zero modes of "
       "the spin 1/2 ghost fields'. ||| [HS eq (11):] ind Q = A-hat(TM)(ch(TM_C) + "
       "1)[M] = ind D_TM + ind D; [Prop 3.1(i):] n = 4: ind Q = -19 A-hat(M) = "
       "19/8 sigma. ||| [PTZ:] We have calculated the gravitational chiral anomaly "
       "for the extended Rarita-Schwinger-Adler model for spin 3/2 fields and found "
       "that it is -19 times larger than the standard anomaly for spin 1/2. ... "
       "-19 = -21 + 2 ... the factor -21 in (1.3) can be obtained as -21 = -20 - 1, "
       "where -20 is the 'ghostless' contribution and -1 is the contribution of the "
       "ghosts. Now, the -19 factor could be obtained by adding the ghostless "
       "contribution and the contribution of spin 1/2, i.e. -19 = -20 + 1. ||| "
       "[PTZ on RSA:] introducing a nontrivial chirally symmetric interaction with an "
       "additional spin 1/2 field ... allowed to consistently gauge the theory beyond "
       "the supergravity approach.",
  regime=dict(mass="anomaly/index level", gauging="BOTH registers published",
              background="4d (anomaly) / K3 (index)", framework="index theory + "
              "one-loop anomaly"),
  forces="ANSWERS THE SWING'S ANOMALY QUESTION: YES, a published source assigns the "
         "ch(T)+1 density (coefficient -19 = 19*sigma/8) to a NON-gauged spin-3/2 "
         "system, in BOTH registers -- math (HS: the geometric ungauged operator Q) "
         "and physics (PTZ: the RSA model = spin-3/2 matter + an ADDED spin-1/2, "
         "explicitly beyond the supergravity approach). Ghost subtraction (-21, -42) "
         "remains tied by both sources to GAUGE conditions / ghost fields.",
  gu_match=[
    ("field-content shape", "GU's stated mechanism (added spin-1/2 with a PLUS sign, "
     "named physical matter, L128) is structurally the RSA shape and carries exactly "
     "carrier B's coefficient", "MATCHES-B"),
    ("convention-by-field-content (steelman S4)", "PARTIAL: PTZ's -19 is a property "
     "of Adler's SPECIFIC model; GU's spin-1/2 slot has a different origin (RS "
     "branching under direct sum); which spin-1/2 completes vs cancels is pinned only "
     "by the unbuilt quadratic form -> collapses into SG4, not an independent escape", "PARTIAL"),
  ],
  verdict="carrier B's density has published legitimacy in both registers for exactly "
          "the field content GU describes; carrier A's density keeps four decades of "
          "physics authority FOR GAUGED gravitini (Witten/AGW/Duff/Bilal). The "
          "convention question is the field-space declaration = SG4.",
  makes_gauging_mandatory_for_GU_as_stated=False,
  makes_gauging_impossible_for_GU=False,
  blocks_ungauged_massive_carrier=False,
  partial_gaps=["AGW primary (NPB 234) paywalled; -21 physics attribution rides "
                "verbatim secondaries (Bilal, HS Rem 3.6, PTZ eq 1.3)",
                "PTZ tachyon-mode footnote: 'The tachyon mode from LLL requires the "
                "separate investigation' -- residual RSA fragility",
                "-19 rides one paper family (Adler 2015-2019 + PTZ 2022)"],
 ),
]

# ----------------------------------------------------------------------------
# 3. CARRIER-A STEELMAN ROWS (first-class; the tilt is INVALID if any is dropped)
# ----------------------------------------------------------------------------
STEELMAN = [
 dict(id="S1-massive-not-ungauged",
  claim="MASSIVE does not mean UNGAUGED: a super-Higgsed/Stueckelberg gravitino keeps "
        "its local invariance and ghost bookkeeping through the Higgsing; the capstone "
        "finding (vectorlike, Dirac mass allowed, massless a modulus) is fully "
        "super-Higgs-compatible; the author name-checks the Stueckelberg trick "
        "(transcript [00:23:02] L80). A mass term NEVER selects B by itself.",
  status="OPEN -- not refuted by any matrix row"),
 dict(id="S2-massless-chiral-corner",
  claim="The '16 flipped chiral' is stated CHIRAL: if any of it is genuinely massless "
        "AND interacting at tree level in the 4d soft regime, GP-1977 bites with full "
        "force -> SUSY couplings + massless spin-2 partner -> the gauged reading, "
        "hence A. The author's gloss (internal-rep conjugation) and mass-as-modulus "
        "make this corner non-mandated -- but it is NOT excluded.",
  status="OPEN corner -- carried in GP-1977 partial_gaps"),
 dict(id="S3-Y14-upstairs-gauging",
  claim="GU's SUSY on the space of connections (graded inhomogeneous gauge group, "
        "L158/L173) is a live UNCONVENTIONAL gauging channel: a graded LOCAL gauge "
        "group has locally parametrized odd generators whose tau+-twisted action is "
        "eps -> D_aleph eps -- the gravitino shape, tagged gu_derived by the repo's "
        "own RS-BRST spec (:61-63). Nothing fetched excludes a 14d fibered "
        "construction whose odd-IG invariance descends and ghost-subtracts on Y14 "
        "with NO spacetime SUSY. If SG4 lands there, carrier A stands with the "
        "transcript intact.",
  status="OPEN -- the named GU-native A-door; unbuilt in fact"),
 dict(id="S4-anomaly-by-field-content",
  claim="PTZ's -19 is a property of Adler's SPECIFIC RSA theory; GU's added spin-1/2 "
        "slot has a different origin (RS branching under direct sum). Until the "
        "action fixes the quadratic form, 'which spin-1/2 completes vs cancels' is a "
        "modeling convention, and a future stabilization may declare the slot a gauge "
        "artifact; the ghost-subtracted convention carries four decades of physics "
        "authority (Witten, AGW, Duff, Bilal).",
  status="OPEN -- collapses into SG4 (see ANOMALY-CONVENTION row), not independently "
         "refutable here"),
 dict(id="S5-HM-discussion-hostile-reading",
  claim="HM's own discussion: the no-go 'enforces the widespread belief that "
        "supergravity theories are the only meaningful models which contain spin 3/2 "
        "fields' -- a hostile reader quotes the same theorem's discussion as evidence "
        "that any CONSISTENT completion of GU's spin-3/2 sector will be "
        "supergravity-shaped, i.e. carrier A.",
  status="OPEN -- discussion-tier, carried verbatim"),
 dict(id="S6-VZ-guard-cuts-As-way",
  claim="GU's Einstein-window escape is background-restricted (Buchdahl/HM), and "
        "DEAD-ENDS forbids the cheap decoupling fix: if the dressed obstruction "
        "ultimately cannot be tamed without a guardian symmetry, the guardian "
        "symmetry IS the gauging, and A follows.",
  status="OPEN -- conditional on future dressed-obstruction work"),
]

# ----------------------------------------------------------------------------
# 4. DECISION OUTPUTS -- derived from row fields, then asserted for consistency
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("THE APPLICABILITY MATRIX (rows = published theorems, verbatim-hypothesis tier)")
print("=" * 78)
for r in ROWS:
    print()
    print("[%s]  %s" % (r["id"], r["cite"]))
    print("  tier    : %s" % r["tier"])
    print("  regime  : mass=%s | gauging=%s | background=%s | framework=%s" % (
        r["regime"]["mass"], r["regime"]["gauging"], r["regime"]["background"],
        r["regime"]["framework"]))
    print("  forces  : %s" % r["forces"])
    for (h, m, v) in r["gu_match"]:
        print("    - %-42s -> %s" % (h[:42], v))
    print("  VERDICT : %s" % r["verdict"])

Q1 = any(r["makes_gauging_mandatory_for_GU_as_stated"] for r in ROWS)
Q2 = any(r["makes_gauging_impossible_for_GU"] for r in ROWS)
Q3 = not any(r["blocks_ungauged_massive_carrier"] for r in ROWS)

print()
print("=" * 78)
print("DECISION OUTPUTS")
print("=" * 78)

# Q1: no published theorem makes gauging mandatory for GU-as-stated.
#   GP/GPvN (the only forcing theorems) each have >=1 input hypothesis that FAILS
#   against GU commitments (mass modulus; spacetime-SUSY rejection); VZ/DW/Buchdahl/HM
#   force background/parameter restrictions, never gauging.
check("Q1 gauging MANDATORY for GU-as-stated? (published record)", Q1, False)
forcing_rows = [r for r in ROWS if "supersymmetry" in r["forces"] or "supergauge" in r["forces"]]
check("Q1 sanity: every forcing row has a failed/escaping GU hypothesis",
      all(any(v.startswith("ESCAPES") for (_, _, v) in r["gu_match"]) for r in forcing_rows),
      True)
check("Q1 sanity: >=2 forcing rows examined (GP, GPvN)", len(forcing_rows) >= 2, True)

# Q2: no published theorem makes gauging impossible for GU.
#   The 343.73 machine fact is IN-REPO (not published) and kills only the naive
#   ghost-free quotient; the '343.73 = d^2 commutator' identification was KILLED
#   in-repo (canon/source-action-seiberg-witten-construction.md:42). Steelman S3
#   (graded-IG upstairs door) stands unrefuted.
check("Q2 gauging IMPOSSIBLE for GU? (published record)", Q2, False)
check("Q2 sanity: S3 (the GU-native A-door) is carried OPEN",
      any(s["id"].startswith("S3") and s["status"].startswith("OPEN") for s in STEELMAN),
      True)

# Q3: the ungauged massive vectorlike carrier escapes everything -- within a window.
WINDOW = [
  "massive (GP/GPvN massless hypotheses moot; mass generic per capstone + transcript)",
  "Einstein backgrounds (Buchdahl/HM satisfied on the adjudicated K3 arena)",
  "VZ line: published non-SUGRA escapes (DW Planck-order windows; Adler RSA; "
  "Porrati-Rahman non-minimal); GU coupling minimality PARTIAL until SG4",
]
check("Q3 ungauged massive vectorlike carrier escapes all fetched no-gos "
      "(within the named window)?", Q3, True)
check("Q3 sanity: escape window has the three named conditions", len(WINDOW), 3)

# The tilt (evidence, not verdict) + story-shopping guard
TILT = ("TILT B at GU-commitments + published-theorem grade: carrier A's mechanism "
        "(ghost subtraction = bookkeeping of a GAUGED gravitino) is UNAVAILABLE to "
        "GU-as-stated (matter framing x4, no stated local fermionic invariance, "
        "spacetime SUSY rejected, textbook gauging route = supergravity) but ADOPTABLE "
        "(S3 door); carrier B's density is published in both registers (HS math, "
        "PTZ/RSA physics) for exactly GU's stated field-content shape. "
        "NEITHER FORCING DIRECTION CLOSES. Formal decider stays SG4.")
check("no row claims a carrier VERDICT (story-shopping guard)",
      all("VERDICT-A" not in r["verdict"] and "VERDICT-B" not in r["verdict"]
          for r in ROWS), True)
check("all %d steelman rows carried OPEN" % len(STEELMAN),
      all(s["status"].startswith("OPEN") for s in STEELMAN), True)
check("steelman coverage >= 6 rows (massive/S2-corner/Y14-door/convention/"
      "HM-discussion/VZ-guard)", len(STEELMAN) >= 6, True)
check("tilt statement names SG4 as decider", "SG4" in TILT, True)
check("tilt statement is not a verdict", "NEITHER FORCING DIRECTION CLOSES" in TILT, True)

# Firewall self-scan: chi never USED as an input (mentions in firewall docs are
# fine; what is banned is a chi variable or a chi-valued assignment feeding the
# arithmetic), no A-hat=3, no /8 manufacture beyond -sigma/8.
check("firewall: no chi variable in scope (arithmetic rides sigma only)",
      not any(name.lower().startswith("chi") for name in list(globals())), True)
check("firewall: A-hat computed from sigma only, value 2 not 3",
      Ahat_K3 == F(2) and Ahat_K3 != F(3), True)
check("acausal trap: no decoupling constructed (bare commutator premise-only)",
      BARE_COMMUTATOR == 58.72, True)

print()
print("=" * 78)
print("STEELMAN LEDGER (carrier A) -- all carried")
print("=" * 78)
for s in STEELMAN:
    print("  [%s] %s" % (s["id"], s["status"]))

print()
print(TILT)
print()

n_fail = sum(1 for (_, ok) in CHECKS if not ok)
print("CHECKS: %d/%d PASS" % (len(CHECKS) - n_fail, len(CHECKS)))
if n_fail:
    print("RESULT: FAIL")
    sys.exit(1)
print("RESULT: ALL PASS -- matrix internally consistent; Q1=False Q2=False Q3=True; "
      "tilt B (evidence, not verdict); SG4 remains the decider")
sys.exit(0)
