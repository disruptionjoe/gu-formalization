"""GU attention priority: Condorcet ranking over the science-advisory council's five archetypes.

PURPOSE. This is the ranking ENGINE for the GU work card (JoeOps WI-068). Joe does not read the card; when
he has attention to give to GU, he wants a prioritized list of what to work on. That list is produced by a
Condorcet vote across the five council archetypes over the current hypothesis/next-move set
(explorations/science-advisory-council-full-picture-2026-07-11.md).

Condorcet is the PRIMARY ranking mode: item X outranks item Y if a MAJORITY of the five archetypes prefer X
to Y. When a strict Condorcet order exists it is used; when there is a cycle (Condorcet paradox) we fall back
to Copeland scores (count of pairwise wins minus losses), which always yields a full order and agrees with the
Condorcet winner when one exists. This makes ties and cycles explicit rather than hidden.

RE-RANKING AFTER A SWING (lightweight, per Joe's spec). After a significant swing toward one hypothesis:
  - if the swing RESOLVED it (cleared/killed): set its ballot rank to 'done' in every archetype (drop it), OR
    remove it from ITEMS; re-run.
  - if the swing STRENGTHENED/WEAKENED it: nudge its position up/down in the 1-2 archetypes whose stated
    values that swing served, and re-run. Do NOT re-elicit all five from scratch -- only move what moved.
The re-rank is just: edit BALLOTS below, run `python attention/gu_priority_condorcet.py`, paste the output
list onto the card. Cheap and reproducible by design.

Run: python attention/gu_priority_condorcet.py
"""
from __future__ import annotations

from itertools import combinations

# --- the candidate hypotheses / next moves (the council's decision set) ---
# RESOLVED in Wave 1 / Wave 10 (2026-07-11), dropped from the live set:
#   H1 -> gravity CLEARS in the Bach branch (Bach tensor of exact Schwarzschild = 0 all orders; Kerr
#         Ricci-flat), REDUCED to the conformal-invariance datum. tests/wave1/H1_bach_flat_exact_vacua.py.
#   H3 -> DESI verified vs arXiv:2503.14738 (recall was correct; GU ~3-4 sigma on wa, a standing FALSIFIER);
#         the theta INT gravity over-determination WEAKENS under the corrected M^2/r^6 residual (f0 not
#         pinned by gravity). tests/wave1/H3_desi_verified_and_intersection.py.
#   H27 -> the soldering is PROVABLY a genuine postulate: Palatini variation of |theta|^2 does NOT force
#          pi onto the spin-lift; the conditional theorem is the final state within the built structure.
#          tests/wave10/H27_soldering_palatini.py.
ITEMS = {
    # Wave 5: H21 PROVEN (s*(theta)=II_s off-shell, fork does NOT re-open) + H16 CONTESTED-CORNER (antigravity
    # kill retired). BOTH collapse gravity's residual onto ONE object: A = spin-lift(grad^gimmel) = the source
    # action. Gravity is HARD-clear MODULO that object. -> H23 (attempt it) + H24 (the R^Y firm-up).
    # H23 RESOLVED (Wave 8) -> PARTIAL: the spin-lift is canonical AS A MAP + the Krein [P,S]=0 holds (ghost
    # clears structurally); but the SOLDERING (pinning theta to the spin-lift image, codim-8165) is NOT forced
    # -- a single honest postulate. Gauge group sharpened to NON-COMPACT Sp(32,32;H). Gravity = a CONDITIONAL
    # THEOREM (tree-level Stelle-clear, positive decoupled ghost) modulo {the soldering postulate + mu_DW}.
    # H27 RESOLVED (Wave 10) -> the soldering is a genuine postulate, not an unclosed forcing gap; drop it
    # from the live decision set and let attention move to the next unresolved item.
    # --- "PUSH FURTHER" decision set (2026-07-11): each archetype's top-3 next ideas, pooled + deduped.
    # Gravity is a proven conditional theorem; DE is a soft tension; both route to the one unbuilt source
    # action; the fermion/C2 wall (where the count lives) is untouched. ---
    # PARALLEL BATCH (Waves 20-23, 2026-07-11) -- four independent probes fanned out at once:
    # H10 RESOLVED (Wave 22, tests/wave22): PPN GATED-ON-mu_DW, effectively PASSES. GU = R^X+Weyl^2+Lambda has
    #   no R^2 -> pure Einstein-Weyl (massless graviton + one massive spin-2); gamma-1=-(2/3)e^{-m2 r} Yukawa-
    #   suppressed; Cassini needs mu_DW > ~1e-17 eV, natural M_Pl clears it by ~45 orders. A real 4th-order-
    #   gravity falsifier, PASSED. Dropped from the live set (next object mu_DW = existing H24/H25 BAR 2).
    # H26 RESOLVED (Wave 23, tests/wave23): loop ghost unitarity OPEN. The [P,S]=0 COMMUTATION leg is proven
    #   radiatively stable (P is an EXHIBITED group symmetry: Cartan involution = conj by eta in O(9,5); beta_S
    #   in Sp(32,32;H); every so(9,5)-covariant vertex commutes exactly, inherited to all loops). But loop
    #   POSITIVITY (weak ghost symmetry tr(C^dag C)=0, broken by IR regulators) needs an S-matrix -> the source
    #   action (H41). A missing OBJECT, not a missing calc. Routes to H41; dropped from the live set.
    # H28 SUBSUMED by H64 (the mass hierarchy is now the observer's-selection / family-symmetry-breaking question).

    # H29 (Wave 12) NARROWED + H37 (Wave 13) NO-GO -> the count is PROVABLY located-not-forced within the built
    # (9,5) structure (fermion analog of H27). Seven-axis map (L0-L7): L0 baseline + L1-L6 selector-side all
    # LOCKED; L7 = the (9,5)/(7,7) signature was flagged as the sole live escape (= the old H19).
    # H19 RESOLVED (Wave 14, tests/wave14/H19_seven_seven_branch.py, exit 0): adopting (7,7) is LIVE-BUT-NON-
    # DERIVING. It lifts the Kramers 2-primary VETO (odd ranks 1,3,5,7 become admissible) but is STRUCTURALLY
    # INCAPABLE of supplying the count: the signature is a 2-primary datum (Z/8), the 3 lives in the orthogonal
    # Z/3 arena, |Hom(Z/8,Z/3)|=1 (zero map). The triplet carrier is neutral Krein (net index 0) in BOTH sigs.
    # So the count does NOT collapse onto the signature; (7,7) trades a false constraint for MORE freedom and is
    # NOT recommended. H19 drops from the live set. The count's REAL decider is signature-INDEPENDENT -> H38.
    # H38 RESOLVED (Wave 15, tests/wave15/H38_z3_chiral_selector.py, exit 0, 11/11) = NARROWED. A DERIVED Z/3 IS
    # present in the built (9,5) matter sector (the order-3 subgroup of the self-dual SU(2)+ on the 192=3x64
    # triplet; the 3 = dim Lambda^2_+(R^4), forced by the 4-base, not imported, not ambient triality). But
    # ghost parity [P,S]=0 is 2-primary and index-PRESERVING (chiral index fixed=0 for every ghost-parity S) ->
    # it PERMITS the vectorlike 3+3, cannot SELECT a chiral 3. H38=H26 only on the unitarity leg (shared Z2);
    # the count leg W is Z/3, arena-orthogonal (gcd(2,3)=1). The count decider must be 3-primary AND
    # index-CHANGING (non-Krein-unitary) -> that is a SOURCE-ACTION K-class selection, not a ghost-parity
    # condition. H38 drops from the live set; the count's real decider is H39.
    # H39 RESOLVED (Wave 16, tests/wave16/H39_sourceaction_kclass.py, exit 0, 14/14) = NARROWED to a
    # conditional-theorem TWIN of gravity. Carrier B (index -38, rho (0,2,1)) is the UNIQUE index-changing
    # carrier -> any count-selector must be B; but which carrier the source action NAMES is a field-space
    # declaration arithmetic cannot force (gamma-trace-constrained -> B; full field space + BRST -> A), GU
    # commitments B-lean. The count is odd/nonzero with a DERIVED ceiling dim Lambda^2_+=3, realized rank in
    # {1,3}, not pinned (a net index 3 has residue 0 = A's, so no residue certifies 3). NEW (Q3): selecting the
    # count does NOT break gravity's [P,S]=0 -- arena-orthogonal (gcd(2,3)=1) and self-adjoint != index 0
    # (K3 Dirac witness). So gravity's soldering (H27) AND the count's K-class (H39) are COHERENT field-space
    # declarations of the SAME source action. Both reduce to ONE forced build -> H40.
    # H40 RESOLVED (Wave 17, tests/wave17/H40_terminal_sourceaction.py, exit 0, 14/14) = NARROWED, the
    # maximally-hardened terminal state. The Porrati-Rahman causal window IS a genuine structural forcing (the
    # built C2=155.36 leakage is a real VZ acausality on curved Y14, degree-1 -> cure DEMANDED), collapsing the
    # 4-corner residual to the 2 causal cures {A,B} -- one bit removed. But BOTH are causal, so the final
    # constrain(B)-vs-gauge(A) bit stays a B-LEANING LEAN, not forced. Count STAYS {1,3} (order-3 acts on
    # Lambda^2_+ as SO(3): fixed axis + rotated pair; net index 3 = residue 0 = carrier A's, so no order-3 datum
    # certifies 3 -- the "forces 3" temptation checked and REFUSED). Soldering(even) and gamma-trace(odd) are
    # two independent declarations, unifiable under one geometric-posture meta-postulate. The program is ONE
    # forced build from complete, but the build needs an UNBUILT input: the causal-cure term -> H41.
    # H41 REFRAMED (Waves 34-35 landscape assessment): the source action is NO LONGER "blocked/hardest/
    #   unforceable". The consistency-carve (Wave 35) maps its allowed region to a FAMILY of shape-dim 1: the
    #   cure term is FORCED (g=1 full ker-Gamma projection, causality, a Porrati-Rahman-type construction per
    #   Wave 34); the carrier is FORCED to B (count-selection); Krein + soldering are REDUNDANT. The residual
    #   is one gravity-shape ratio beta/alpha (the H45 P2 / H48 fork) + two scales (mu_DW, alpha). GU is NOT
    #   killed (EMPTY falsified) and NOT forced (POINT falsified). The deep residual question -> H54.
    # H54 RESOLVED (guardian wave, Waves 37-41, 5 blind branch-teams) = NO (guardian-forbidden), both exciting
    #   payoffs DEAD. Convergence: GU has supergravity FIELD CONTENT (the RS IS a gravitino, ker-Gamma = the
    #   gauge condition -- Branches 2/4; a graded algebra siso(9,5|N) exists abstractly -- Branch 1) but is NOT
    #   a supergravity: (a) [P,S]=0 is a BOSONIC Krein parity not the SUSY Ward identity -- GU clears its ghost
    #   the anti-SUSY way (Branch 3); (b) the graded symmetry GU's structure actually realizes (super-IG) closes
    #   on Omega^1(ad) = the spin connection, NOT physical P_mu -- so it is graded local-Lorentz, not spacetime
    #   SUSY (Branch 5, decisive); (c) even a local-SUSY guardian would NOT UV-complete GU's finite content (no
    #   Regge tower, Sagnotti-Taronna) -- so it stays a finite-cutoff EFT regardless; (d) super-Higgs RELATES
    #   the scale, does not FIX mu_DW (Branch 2) -- so the falsifiability payoff is dead too. Sole surviving
    #   escape: a derivative-level odd embedding (eps->D_aleph eps) pushing {Q,Q} to P_mu -- LOW value (even if
    #   it gives SUSY, no UV-completion and no mu_DW forcing). REFRAME: GU's UV route is RENORMALIZATION-
    #   theoretic (4th-order Stelle + Krein rescue), not symmetry-theoretic -> the same source action -> H56.
    # H56 RESOLVED (renormalization assessment, Waves 42-43) = RENORMALIZABLE-BUT-POSITIVITY-OPEN, NOT
    #   FORBIDDEN. Power-counting: GU is RENORMALIZABLE, the RS spin-3/2 does NOT spoil it (COMPUTED, survives
    #   the Stelle check: gravity D=4; RS ker-Gamma TT projector momentum-degree 0 -> D=4; the n=2 danger is
    #   exactly the VZ modes ker-Gamma removes). The ONLY obstruction is loop POSITIVITY of the keep-and-grade
    #   Krein rescue -- unified for both sectors, = H26, gated on the source action, AND it is the OPEN FRONTIER
    #   of PT/Krein QFT itself (no keep-and-grade rescue proven at loop level anywhere: Kuntz 2024, Nakayama
    #   2023, Bateman-Turok tree-only) -- so GU's UV-openness is a frontier problem, NOT a GU defect. NO
    #   FORBIDDEN cell. Two live UV routes surfaced -> H57 (asymptotic safety, independent) + H58 (firm
    #   renormalizability); the loop-positivity terminal question stays gated on the source action.
    # H57 RESOLVED (asymptotic-safety FLOW, Waves 44-46, 2026-07-11) = ASYMPTOTICALLY FREE (stronger than safe).
    #   Stage 1 (tests/W45): ported the agravity one-loop betas (f_2 AF, b_2=133/10>0; f_0 conformal mode not AF)
    #   + RS matter shift as a named parameter c_RS_weyl (anchor 17/12, unpinned because ker-Gamma changes the
    #   effective dof). Stage 2 (tests/W46): the Gaussian (0,0) is the UNIQUE UV fixed point (multistart Newton,
    #   25 seeds; NO non-Gaussian FP at one loop / 2 couplings) -> GU realizes asymptotic FREEDOM, not safety;
    #   f_2^2 marginally irrelevant (AF PREDICTS it -- the one predictivity gain over generic higher-derivative
    #   gravity), f_0^2 marginally relevant along a frozen NEGATIVE ratio f_0^2/f_2^2<0 (wrong-sign conformal
    #   direction). UV critical-surface dimension = 3 in the known gravity sector {M_Pl=mu_DW ratio-only keystone,
    #   Lambda, f_0^2} (up to 5 with RS dimensionful at GUESS grade). ROBUST: AF holds for all c_RS_weyl>-13.3
    #   (anchor +1.42 clears by 14.7). Does NOT settle Krein loop-positivity -- the negative fixed-ratio sign is
    #   the SINGLE point where flow and positivity touch, left open. Grade DERIVED-on-PORTED, one-loop/2-4
    #   couplings (an INDICATION, not a proof). Two continuations surfaced -> H59 (loop-positivity at the negative
    #   ratio, the terminal UV North Star, PT/Krein frontier-gated) + H60 (firm the AF: larger/FRG truncation).
    # H58 RESOLVED (renormalizability SWING, Wave 44, tests/W44) = CONFIRMED. Two independent computations give
    #   D<=4 on the ker-Gamma subspace for every L-loop 1PI graph (worst case D=4); the leaked/VZ branch gives
    #   D=4+2*I_B (grows with loops), and ker-Gamma removes exactly those gamma-trace VZ modes (projector COMPUTED
    #   degree-0 and gamma-traceless, residuals ~1e-16, not assumed). Sharpenings: (S1) the RS sector adds its OWN
    #   finite CLOSED counterterm set beyond pure Stelle (extends, not "same as"); (S2) conditional on the exact
    #   background-independent degree-0 projector. GU is renormalizable; positivity stays the sole open leg.
    # H60 RESOLVED (H60 SWING) = CONFIRMED-FIRMER: AF is structural (the one-loop system is homogeneous-quadratic
    #   -> forbids any isolated interacting FP for any ker-Gamma coefficient); c_RS_weyl tightened to [1.02,1.82].
    #   Banked (W47). Dropped from the live set.
    # H59 ADVANCED (path 2, the keep-and-grade loop-positivity BLIND WAVE + wave-2 swings, GU-independent framing)
    #   -> a referee-grade MAP consolidated into papers/candidates/keep-and-grade-loop-cost/: loop unitarity of
    #   4th-order gravity is a POSITIVITY-vs-CAUSALITY trade (4 constructions agree; no construction pays neither);
    #   the grading is RG-stable for AF gravity across the interacting regime (BOUNDARY only at the free UV
    #   endpoint); + a machine-checked NO-LOCAL-POSITIVE-METRIC theorem (kernel exp-localized ~1/m). Not a clean
    #   proof or kill; a structural result. The loop-positivity question is now reframed INTO the observer
    #   conjecture (the Krein grading = the admissibility firewall) -> H61/H63. Dropped as a standalone.
    # --- OBSERVER-CONJECTURE HYPOTHESES (path 5 + the "source action = observer" conjecture, 2026-07-11) ---
    # RETIRED 2026-07-14 full-landscape re-rank (see landscape-assessment-post-three-waves-2026-07-14.md): "H61": "THE KREIN TOMITA-TAKESAKI CAMPAIGN (the observer conjecture's CRITICAL PATH): develop -- or survey the literatur ... [superseded/resolved entry, kept for provenance]
    # RETIRED 2026-07-14 full-landscape re-rank (see landscape-assessment-post-three-waves-2026-07-14.md): "H62": "FIRM THE ARENA/VALUE PARTITION (the CHEAP GATE that governs the whole conjecture): make ARENA (forced dimensionl ... [superseded/resolved entry, kept for provenance]
    # RETIRED 2026-07-14 full-landscape re-rank (see landscape-assessment-post-three-waves-2026-07-14.md): "H63": "ASSEMBLE THE OBSERVER-CONJECTURE PAYOFF THEOREM (the Lawvere no-closure, within reach modulo H61 + the map): pat ... [superseded/resolved entry, kept for provenance]
    # RETIRED 2026-07-14 full-landscape re-rank (see landscape-assessment-post-three-waves-2026-07-14.md): "H64": "THE MASS HIERARCHY AS THE OBSERVER'S SELECTION (the C2 wall = the reframed Yukawa question, subsumes H28): path- ... [superseded/resolved entry, kept for provenance]
    # H55 RESOLVED (Wave 36) = NO-CONSTRAINT. Krein-modified positivity is toothless on the gravity beta/alpha
    #   ratio (the ghost pole makes the spectral measure SIGNED -> forward c2 sign-indefinite; non-compact
    #   Sp(32,32;H) has no positive-definite invariant to restore the bound). The shape residual stays a small
    #   FAMILY (-1/4, 0], decided by SURVIVAL (H49) + structure (theta=II), not analyticity. Positivity dropped
    #   as a shape-collapse lever.
    # --- FULL-LANDSCAPE GENERATIVE RE-RANK after the 2026-07-13 three waves (W119-W126, H46C, H52, Yukawa,
    # spec; consolidated by W127, commit 61937e6). Writeup + full inventory/impact table:
    # explorations/landscape-assessment-post-three-waves-2026-07-14.md. Evidence: (a) native tree-unliftable
    # AF-branch tachyonic scalaron; (b) DE excluded as CMB-calibrated distance model (theta_star, dAIC +35.78);
    # (c) H41 compressed onto the Y14 covariant operator, SA-C4 passing; (d) two-loop graded cleanliness with
    # the even-cut inter-family disagreement (+1 vs 0) and the odd-cut leak as the price; (e) Yukawa no-gos +
    # FN-sterility; (f) mu_DW floor cited (H52). DROPPED this pass:
    #   H52 RESOLVED (wave 32): alpha=1/3 boundary CITED (lambda_max 47.6 um, Lee 2020); H36 window
    #     EXCLUDED-CITED margin 1.9-9.8x; resolved mu_DW floor [3.4,4.7] meV. Banked.
    #   H61 MOOTED (physical leg): the type-III wall (W84) stands AND W122's positive-norm verdict moved the
    #     decisive physical question to the AF-vs-AS branch fork (-> H65). Abstract content lives on in H63.
    #   H62 RESOLVED (W73): arena/value partition FIRMED non-circular (symmetry characterization); folded into
    #     H63 as a lemma.
    #   H30 ABSORBED: the W127 flagship consolidation carries the gravity conditional theorem at referee grade.
    "H63": "ABSTRACT LAWVERE NO-CLOSURE PAYOFF THEOREM in symmetry-breaking language (needs only the fixpoint-free label-involution J^2=1, NOT type-III modular theory -- survives the W84 wall): 'no closure without a residual symmetry-breaking selection = observer vacuum choice'. H62's firmed non-circular arena/value partition is the lemma. The GU-independent credibility result of the observer conjecture. [heterodox/philosopher]",
    "H64": "THE MASS HIERARCHY AS THE OBSERVER'S SELECTION, post-Yukawa-no-gos: the channel table is rigid, non-form carriers forbidden, mod-3 Froggatt-Nielsen provably STERILE (all 27 assignments), hierarchy SILENT -- so any breaking mechanism must be non-FN and non-form-carrier. Sharper question, smaller toolset. [commercial/wild]",
    "A15": "THREAD-A NATIVE CONSTANT-BACKGROUND COEFFICIENT CHAIN (A3-A14): push through the A14 shear gate (pure trace normalization cannot cancel the A13 shear) to supply the SA-G background coefficient rows source-first; the native-computation pattern's standing home in the gravity sector, feeding OQ2-A. [orthodox]",
    "TAFB": "TRI-REPO BOUNDARY-CONTENT LEG: what the boundary must supply, in exact mathematics (GU's leg of the ratified division of labor; TaF owns the capability measure, temporal-issuance the source question). Untouched by the waves; identity claims stay gated. [wild/philosopher]",
    "H65": "COMPUTE THE AS/REUTER-BRANCH SCALARON NATIVELY (the tachyon's last perturbative escape; the referee's strongest vulnerability -- the tachyon chain rests on ported pure-gravity loop blocks with the AS branch UNCOMPUTED; also the sole hinge of W83's conditional observer-leg close): GU's ker-Gamma content in an f(R)+Weyl^2 FRG truncation at the Reuter FP, native heat-kernel blocks, scalaron mass sign out. Either answer is a result: escape closes (global negative at full strength) or GU acquires its one viable branch. [heterodox #1]",
    "H66": "GU-NATIVE GRAVITON ONE-LOOP BLOCK: replace the last big ported ingredient (agravity/pure-gravity one-loop beta blocks under the tachyon chain) with a native computation on GU's own field content and gimmel conventions; discharges the W126 16/3 and c_L background-vs-TT normalization flags. The exact move that produced both blockbuster negatives. [orthodox/heterodox/wild]",
    "H67": "OQ2 M^2-BAND SWEEP OF THE H46C DE EXCLUSION (+ ansatz variants): the exclusion is exploration-grade at M^2=8 only, BAO+theta_star only -- the cheapest computation that can flip or harden a headline claim, retiring the single-pipeline/OQ2-gated vulnerability either way. [orthodox #1, commercial #1]",
    "H68": "BUILD THE Y14 COVARIANT OPERATOR, TIME-BOXED, BUILD-OR-PROVE-UNBUILDABLE (W125's single blocking object: the covariant propagator and vertex on the Met(X4) bundle -- blocks the full source-action build, the H59 loop packet, and SA-G9 alike). Run under the E1 discipline: deliverable is the operator or an unbuildability obstruction, NOT a further reduction (the one-object pattern just recurred here). [wild #1]",
    "H69": "GRADED OPTICAL THEOREM ON THE PHYSICAL SUBSPACE: formulate the optical theorem restricted to the positive (physical) subspace of the graded theory and test whether the odd-ghost-cut leak at s>(2m+M)^2 violates it -- the precise form of the open loop-positivity price (H59's sharpest register), and frontier PT/Krein mathematics independent of GU. [wild/heterodox]",
    "H70": "W124 STAGE C: SPIN-2 TENSOR NUMERATORS for the two-loop overlap/kite cuts (the leak and even-cut verdicts are scalar-core only). Bounded, standard, verdict-bearing. [orthodox]",
    "H71": "THE EVEN-CUT INTER-FAMILY DISAGREEMENT (+1 vs 0) AS A DISCRIMINATOR between the grading and removal families: which family's answer is compatible with fixed-order causality/unitarity trades -- the loop program's first internally generated discriminator candidate (a progressive step, not a consistency pass). [philosopher/commercial]",
    "H72": "RESIDUAL-ARITY AUDIT (the title strain as a research question): is the residual still ONE object? Formalize the residual as (field-space declaration, coefficients, branch choice) and determine whether AF-vs-AS is a derivable consequence of the declared action, a 28th spec row, or an independent second residual. Structural result either way; the honest response to the E1 recurrence at Y14. [philosopher #1]",
    # STANDING RULE (Joe, 2026-07-11): the GU council proposes RESEARCH ADVANCEMENT of this repo only.
    # Do NOT suggest external-review / submission-prep / methodology-paper / "shipping" items (Joe is aware of
    # those; they are not the advancement of the research). H31 (flagship review-ready) and H32 (methodology
    # paper) DROPPED per this rule. H6 (finish the GU-independent family-puzzle THEOREM) is kept as a research
    # result, not a shipping task.
    # H6 RESOLVED (Wave 33, tests/wave33) = DONE. The GU-independent family-puzzle theorem is PROVEN, cited
    #   (Toda/Adams/von Staudt-Clausen), arena-independent, honestly scoped: a selector forcing a 3-primary
    #   count must have nonzero 3-Sylow image; no 2-group or free-Z selector can force it (Hom=0). It constrains
    #   the selector KIND, does NOT derive 3. HONEST CORRECTION: the slogan "forces ODD count" is literally
    #   false (odd = mod-2); the rigorous theorem is MOD-3. Banked as the durable standalone; adds no new front.
    # H34 RESOLVED (Wave 18, tests/wave18/H34_parameter_count.py, exit 0, 13/13) = the honest ledger. Strict
    # count: PREDICTIONS zero; FITS 4 free params (f0, M2, B_i, mu_DW); the asset is the one-residual
    # COMPRESSION (a structural map, not a prediction); DESI is the sole data-touch (+2.55 sigma on wa, soft
    # only because f0 is free); "ACCOMMODATES" is honest, even conservative. Signal: run the CHEAP FALSIFIERS
    # before more synthesis; H41 is demoted in URGENCY (only pays off if forced). The sharpest new move -> H42.
    # H42 RESOLVED (Wave 19, tests/wave19/H42_f0_prereg.py, exit 0, 5/5) = NO-TEST-YET. f0 is NOT source-first
    # derivable now (DERIVABLE-ONLY-AFTER-H41: the amplitude ratio depends on two unbuilt inputs B_i + mu_DW;
    # the geometry fixes only the SHAPE M^2=8H0^2, not the amplitude; the f0=1/8 back-fit was raised and
    # REFUSED). It stays a FIT. But the sharper finding: the source-first (w0,wa) LOCUS misses DESI at EVERY f0
    # (closest 3.47 sigma; joint tension 4.19 sigma at canonical f0) -- freeing the amplitude does NOT rescue
    # the fit; the shape tracks ACROSS the DESI degeneracy. So the DESI tension is deeper than "soft", latent-
    # falsifier-grade, gated only by the reconstruction-grade OQ2 M^2/ansatz -> the sharpened cheap move is the
    # DE SHAPE test, H43. (The amplitude unblock stays H41.)
    # H43 RESOLVED (Wave 20, tests/wave20): DE-shape FALSIFIED -- the first hard negative. GU's source-first
    #   (w0,wa) locus misses DESI's headline CPL contour robustly: NO admissible M^2 (BC_1=8, A_1=7, S^3=3,
    #   threshold=20.25) and NO point in the free (M^2,f0) plane rotates it in (global closest 3.20 sigma); the
    #   1-component ansatz misses too (3.18 sigma). It is a SHAPE/DIRECTION miss, exhausting f0 + OQ2 + ansatz.
    #   HONEST SCOPE: falsifies the (w0,wa) CPL comparison DESI reports, NOT the raw H(z) (GU's non-CPL w(z)
    #   reaches ~1% RMS on distances, near BAO). One untested escape: a self-consistent theta-backreacted
    #   background (currently LCDM) -> H44.
    # H5 RESOLVED (Wave 21, tests/wave21): geometry-vs-information (Bianconi) = DISTINCT PRIMITIVES (rel-entropy
    #   is the 2nd-order Kubo-Mori supermetric; |II|^2 is order-4). KEY CORRECTION: NEITHER frame pins Lambda's
    #   magnitude (Bianconi's Lambda is a subtracted input constant) -- the asserted determinacy asymmetry is
    #   FALSE. Bianconi cleaner on order/ghosts; GU's 4th-order buys the Weyl sector. The real decider is the
    #   SPIN-2/WEYL sector, and the pivotal internal object is the |H|^2-vs-|II|^2 binary -> H45.
    # SECOND PARALLEL BATCH + persona-council coherence assessment (Waves 24-26, 2026-07-11):
    # H44 RESOLVED (Wave 25): DE = FALSIFIED-FULL-STOP at the (w0,wa) CPL level. The self-consistent
    #   theta-backreacted background (backreaction real, +3.6% on H at z~1) shifts the locus AMPLITUDE not its
    #   DIRECTION -- closest 3.22 sigma vs H43's 3.20. Every DE-rescue route (f0, OQ2, components, IC,
    #   background) spent. Scope unchanged: CPL falsified, raw H(z) not independently killed (GU ~1.3% on
    #   distances) -> the one remaining DE object is the raw-likelihood test, H46.
    # H45 RESOLVED (Wave 24): |H|^2-vs-|II|^2 STILL-OPEN, favored |II|^2 (H21 fixed the object theta not the
    #   action NORM P2). GU has the Weyl sector under BOTH branches (Bianconi has none) -> the spin-2/Bach
    #   discriminator is ROBUST to the binary. Lambda +positive under |II|^2. The source action settles P2 +
    #   mu_DW + H26 positivity + the H21 bundle = QUADRUPLY-motivated keystone.
    # H20 RESOLVED (Wave 26): SPLITS-BUT-RELABELS. The Clifford omega-parity DOES split gravity(even, the 91
    #   bivectors) from matter(odd, c(xi)); one first-order D generates both kinetic operators (Weinstein's
    #   first-order-then-square, made precise) -- BUT it removes 0 of 4 unforced choices (relabels them, does
    #   not force them). The elegant-shortcut hope is ELIMINATED.
    # COUNCIL COHERENCE SYNTHESIS (full persona pass + the batch): the coherence gap IS the missing keystone
    #   (the source action); H20 proved there is NO elegant bypass; everything (P2, mu_DW, soldering, K-class,
    #   loop positivity, count) routes to it. THE LOCAL MINIMUM: the program keeps NARROWING onto a keystone
    #   that cannot be FORCED (signature doesn't force it, causality forces only the cure not the carrier, the
    #   even/odd grading is cosmetic). THE ESCAPE: stop narrowing; DECLARE the honest lean and build the
    #   CONDITIONAL theory to get testable predictions -> H47.
    # NORTH-STAR + DE BATCH RESOLVED (Waves 27-29, 2026-07-11):
    # H49 RESOLVED (Wave 28): GU-DISTINGUISHED. box^2 h=-4 Bach re-derived; on the favored |II|^2 branch NO
    #   conformal-gravity refutation transfers (Ostrogradsky tree-cleared; rotation-curve EVADED because the
    #   Einstein term makes the Bach sector short-range <52um; |H|^2 would inherit-and-die). Class Lambda-
    #   magnitude no-go FIRES as a scope-kill of the 'Lambda emerges' headline for GU AND Bianconi (scale-free
    #   action -> O(1) ratios only, can't make 10^-123). Everything empirical gated on ONE number: mu_DW.
    # H48 RESOLVED (Wave 27): forcing RELABELS (color-kinematics is so(9,5)-equivariant -> carrier-blind).
    #   Uniqueness holds (dim 1) but forces the pure-Bach |II_0|^2, NOT GU's Stelle |II|^2. H48xH49 TENSION:
    #   the norm uniqueness forces (pure Bach) is the branch H49 says DIES; the norm GU needs to SURVIVE
    #   (Stelle, with the Einstein term) is the one uniqueness cannot force. GU is a distinct non-conformal
    #   theory; the clean-forcing coherence route is RETIRED.
    # H46 RESOLVED (Wave 29): DE = MARGINAL. Falsified as a (w0,wa) CPL fit (H43/H44 stand, ~3.2 sigma) but
    #   VIABLE as a distance model on the actual DESI DR2 BAO likelihood (competitive-to-better than LCDM once
    #   the amplitude is freed; excluded only at the CPL-tuned+CMB-fixed point). Cornered, NOT dead -- moderates
    #   the 'full stop'.
    # CONVERGENCE: GU SURVIVES (distinguished + DE-viable) as a genuinely distinct theory; the clean-forcing
    #   route is closed; the DE sector is cornered-not-dead; and EVERYTHING (empirical content, the norm/
    #   survival, loop positivity, the count) routes to ONE number, mu_DW -> H50.
    # H50 RESOLVED (Wave 30, tests/wave30): GU's FIRST parameter-linked prediction. The one-scale link HOLDS
    #   (one mu_DW sets both the DeWitt-Lambda rho~c_L mu_DW^4 and m2=sqrt(m2_eff)mu_DW -> the sub-mm number is
    #   a genuine prediction). Under the H36 identification (mu_DW = DE scale ~2.3 meV, a POSTULATE not forced),
    #   GU predicts a sub-mm Stelle-Yukawa deviation lambda=76.7-94.0 um, alpha=1/3 -> EXCLUDED at face value by
    #   Eot-Wash/HUST (Kapner/Lee/Tan), but by an O(1) margin (AT the frontier). SELF-FALSIFIED-AT-FACE-VALUE
    #   conditional-on-H36. The decider is the one uncomputed geometric coefficient c_L -> H51.
    # H51 RESOLVED (Wave 31, tests/wave31): c_L = 3/8 EXACT (from the horizontal sectional; A0=0 exactly so the
    #   DeWitt Lambda is a background/trace vacuum energy not a TT-graviton mass; O(1) background-vs-TT norm
    #   caveat). -> lambda = [60.0, 73.6] um (c_L^{1/4}=0.78 lowered it from H50's 77-94), alpha=1/3. The
    #   alpha=1/3 boundary ~45-52 um (argued not digitized) -> EXCLUDED at both ends, O(1)-robust (LIVE needs
    #   c_L<~0.05, ~5x below computed). GU's first prediction (conditional on H36) is SELF-FALSIFIED at face
    #   value: it falsifies the H36 identification (DeWitt-Lambda = observed DE), NOT GU-gravity (drop H36 ->
    #   mu_DW free -> decoupled, no prediction). Two residual uncertainties -> H52.
    # H53 RESOLVED (Wave 32, tests/wave32) = DECOUPLED. Sector x scale table: 4 needs-free-scale, 3 settled-
    #   FAIL, 3 gated-on-source-action, 1 scale-independent PROPERTY (4th-order/7-DOF) that is NOT an accessible
    #   observable (every GU-vs-GR effect ~(E/m2)^2 -> 0 as mu_DW->M_Pl). Verdict: GU is falsifiable-IN-PRINCIPLE
    #   but decoupled-in-practice -> a consistent geometric FRAMEWORK, not a standing theory; zero standing
    #   predictions (H36 emitted a real self-falsifying number -> not vacuous). GU's FALSIFIABILITY rests on
    #   H41 (the source action forcing mu_DW) -> H41 is the FALSIFIABILITY keystone, quintuply motivated. Verb
    #   stays ACCOMMODATES.
    # RETIRED 2026-07-14 full-landscape re-rank (see landscape-assessment-post-three-waves-2026-07-14.md): "H52": "DIGITIZE THE alpha=1/3 SHORT-RANGE-GRAVITY EXCLUSION CURVE (firm the H36 falsification, cheap): H51 put GU-under ... [superseded/resolved entry, kept for provenance]
    # TWO-TRACK RESTRUCTURE (full-roster persona sweep, 2026-07-11, explorations/two-track-persona-sweep-*/):
    # Joe's frame: keep the NORTH STAR (force-or-falsify GU + the observer-geometry class) as the repo posture;
    # run the conditional-build as ONE branch. ~60 personas across 5 families converged. The load-bearing
    # object is the BACH/WEYL SELF-DUAL-SQUARE GRAVITON SECTOR (it forces, falsifies, decides the class, and
    # needs neither the source action nor the signature settled). RETIRED as North-Star objects: chromatic
    # torsion + the (9,5)/(7,7) signature flip (both proven structurally incapable of the 3-primary count --
    # route ZERO effort there). H47 (declare-and-build) is REFRAMED as the Track-2 branch header below; its
    # count-prediction is DEPRIORITIZED (the count is decoupled/source-action-gated, the worst first deliverable).
    # H47 (Track-2 declare-and-build) FOLDED: its deliverables were executed across the DE waves (H46 viable-as-
    #   distance) and the GU-independent theorem papers (paths 2/3); the conditional-build framing is superseded by
    #   the observer-conjecture direction. Dropped from the live set.
    # H35 (section-functor reframe) SUBSUMED by H48: the Willmore/GJMS uniqueness IS the functorial-identity
    #   forcing, now sharpened to a concrete self-dual-square test. Dropped from the live set.
    # H36 RESOLVED (via Wave 31): the observerse identification (DeWitt-Lambda = the observed dark-energy scale)
    #   was TESTED by H50/H51 and its consequence -- a sub-mm Stelle-Yukawa at lambda=[60,73.6] um -- is
    #   EXCLUDED (O(1)-robust). So the H36 identification is (conditionally, O(1)-robustly) FALSIFIED by
    #   short-range gravity: mu_DW is NOT the DE scale. Dropped from the live set (the observerse/issuance
    #   framing may survive in a different form, but the DeWitt-Lambda=DE-scale identification is ruled out).
}

# --- five council ballots: strict preference order, best first ---
# "PUSH FURTHER" vote (2026-07-11): each archetype ranks the pooled 14 ideas; their own top-3 lead, the rest
# ranked by their values. Expect the fermion/C2 wall (H29) and the cheap falsification bars (H10/H26) to lead.
# RE-RANK after the ASYMPTOTIC-SAFETY FLOW (Waves 44-46) resolved H57+H58. GU is RENORMALIZABLE (H58 CONFIRMED)
# and ASYMPTOTICALLY FREE in the higher-derivative couplings (H57: Gaussian UV FP, f_2 predicted, ~3-param
# gravitational critical surface incl. mu_DW; robust; positivity NOT settled -- the negative fixed-ratio is the
# one point flow and positivity touch). Post-flow council reflection drafted two continuations: H59 (settle
# loop-positivity at that negative ratio -- the terminal UV NORTH STAR, but the PT/Krein frontier, possibly not
# GU-decidable alone) and H60 (firm the AF: larger/FRG truncation, could find a non-Gaussian FP; feeds H59).
# The council's honest read: H59 is the North Star but frontier-GATED (the whole field can't yet crack keep-and-
# grade loop positivity); H60 is the actionable de-risking move that also sharpens exactly where H59 bites, so
# most archetypes rank H60 #1 with H59 the standing North Star behind it; the wild/philosopher archetypes lead
# with H59. H30 (document the now-strong UV picture at referee grade) rises to a genuine bank-the-result option.
# MODE: H60 minimal = SWING (add RS couplings to the one-loop system) escalating to FLOW (full FRG); H59 =
# frontier research, not a clean swing/flow, gated on the source action.
# RE-RANK after the OBSERVER-CONJECTURE arc (paths 2-5 + the "source action = observer" conjecture, 2026-07-11).
# Generative re-rank: the council's 3-question reflection produced FOUR new hypotheses (H61 Krein-TT critical
# path; H62 firm the arena/value partition = the cheap gate; H63 the Lawvere payoff theorem modulo H61; H64 the
# mass hierarchy as observer-selection). RESOLVED/dropped: H57/H58/H60 (renormalizable + asymptotically free,
# banked), H59 (advanced to the keep-and-grade paper), H28 (subsumed by H64), H47 (folded). The council's read:
# H62 is the cheap GATE that governs whether the expensive Krein-TT campaign (H61) and the payoff theorem (H63)
# are even worth mounting (a theorem true-by-definition is not the headline) -> H62 leads for orthodox/philosopher,
# with heterodox leading H63 (the prize), wild leading H61 (the real math), commercial leading H64 (data contact).
# FULL-LANDSCAPE RE-RANK ballots (2026-07-14, post-three-waves; see landscape-assessment writeup for the five
# reflections these ballots encode). Twelve items: survivors H63/H64/A15/TAFB + drafted H65-H72. Expected and
# realized: H65 is the Condorcet winner (the native AS/Reuter-branch scalaron -- the tachyon's last perturbative
# escape and the referee's strongest vulnerability, one computation); H67 (OQ2 band sweep, cheap and decisive)
# and H66 (native graviton loop block) follow. Low-tier survivors below the ballot cutoff (family-puzzle
# follow-ons, causal-set axis, anomaly global leg, shiab selector, gauge-vacuum selection) are carried in the
# writeup, not voted -- each is dormant or collapses into H68.
BALLOTS = {
    "orthodox":            ["H67", "H70", "H66", "H65", "H69", "A15", "H68", "H71", "H72", "H63", "H64", "TAFB"],
    "heterodox_rigorous":  ["H65", "H66", "H68", "H67", "H69", "H70", "H71", "H72", "A15", "H63", "H64", "TAFB"],
    "commercial":          ["H67", "H65", "H64", "H71", "H66", "H70", "H68", "A15", "H72", "H69", "TAFB", "H63"],
    "philosopher":         ["H72", "H71", "H65", "H67", "H63", "H69", "H66", "H68", "H64", "A15", "TAFB", "H70"],
    "wild_frontier":       ["H68", "H66", "H69", "H65", "H63", "H71", "H70", "H72", "A15", "H64", "TAFB", "H67"],
}


def prefers(ballot, x, y):
    return ballot.index(x) < ballot.index(y)


def pairwise_margin(items):
    """margin[(x,y)] = (# archetypes preferring x to y) - (# preferring y to x)."""
    margin = {}
    for x, y in combinations(items, 2):
        sx = sum(1 for b in BALLOTS.values() if prefers(b, x, y))
        sy = len(BALLOTS) - sx
        margin[(x, y)] = sx - sy
        margin[(y, x)] = sy - sx
    return margin


def copeland(items, margin):
    """Copeland score: pairwise wins minus losses. Full order; agrees with Condorcet winner if one exists."""
    score = {i: 0 for i in items}
    for x, y in combinations(items, 2):
        m = margin[(x, y)]
        if m > 0:
            score[x] += 1; score[y] -= 1
        elif m < 0:
            score[y] += 1; score[x] -= 1
    return score


def condorcet_winner(items, margin):
    for x in items:
        if all(margin[(x, y)] > 0 for y in items if y != x):
            return x
    return None


def main():
    items = list(ITEMS)
    margin = pairwise_margin(items)
    cw = condorcet_winner(items, margin)
    score = copeland(items, margin)
    # rank by Copeland, break ties by average ballot position (lower = better)
    def avg_pos(i):
        return sum(b.index(i) for b in BALLOTS.values()) / len(BALLOTS)
    order = sorted(items, key=lambda i: (-score[i], avg_pos(i)))

    print("=" * 78)
    print("GU ATTENTION PRIORITY  --  Condorcet over the 5-archetype council")
    print("=" * 78)
    print(f"Condorcet winner: {cw if cw else 'NONE (cycle) -> Copeland order below is authoritative'}\n")
    print("Prioritized list (what to hand Joe when he has GU attention):\n")
    for rank, i in enumerate(order, 1):
        print(f"  {rank}. [{i}]  Copeland {score[i]:+d}  (avg ballot pos {avg_pos(i):.1f})")
        print(f"       {ITEMS[i]}")
    print("\n" + "-" * 78)
    print("Per-archetype #1 picks:")
    for a, b in BALLOTS.items():
        print(f"  {a:20s} -> {b[0]}")
    # a couple of decisive pairwise checks for transparency
    print("\nKey pairwise margins (positive = row beats col across the 5 archetypes):")
    top = order[:4]
    hdr = "        " + "".join(f"{j:>6}" for j in top)
    print(hdr)
    for x in top:
        row = "".join(f"{margin[(x, y)]:+6d}" if x != y else "     ." for y in top)
        print(f"  {x:>5} {row}")
    return order


if __name__ == "__main__":
    main()
