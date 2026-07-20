---
title: "N2 at truncated-real grade: a faithful Y14-end model (DeWitt-induced (9,5), induced 6-leg holonomy, degeneration rays, collar) -- the two-section structure survives to the boundary-at-infinity on the spacelike-gapped sector and the F2 kill fires NOWHERE; the F5 decisive form does NOT fire (signed C2 response nonzero at infinity on every surviving ray); the end is provably NOT uniformly invertible (cone-crossing + K-null sectors) -- the N2 obstruction precisely named"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (five-path fan-out: N2 real grade)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/sig-b5-f2-f5-shadow-2026-07-20.md
  - explorations/master-identity-mechanism-2026-07-20.md
inputs:
  - explorations/sig-b5-f2-f5-shadow-2026-07-20.md
  - explorations/master-identity-mechanism-2026-07-20.md
  - explorations/sig-b5-habitat-verification-2026-07-20.md
  - explorations/blockbuster-p5-instance-dossier-2026-07-19.md
  - explorations/hardening-h3-triplet-lift-2026-07-19.md
  - tests/channel-swings/f2_shadow_two_section_probe.py
  - tests/channel-swings/f5_shadow_c2_flip_probe.py
  - tests/generation-sector/gen_sector_bridge.py
  - tests/oq_rk1_cl95_explicit_rep.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
runnable:
  - tests/channel-swings/n2_end_family_probe.py
  - tests/channel-swings/n2_end_f5_signed_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# N2 at the best honestly-reachable grade: the end family, built

The F2/F5 shadow swing left the P5 candidate's stakes at exactly the
N-rungs, with N2 -- the actual Y14-end boundary Dirac family and its
spectral-section classification -- carrying both live falsifiers: F2 in
its real form (does the two-section structure exist for the actual end
family, beyond the toy?) and F5 in its decisive form (in a faithful
end-model, does the C2 global residual respond to the sector flip?). The
dossier files N2 as needs-new-mathematics. This swing pushes the
construction as far as honest mathematics allows short of that theorem:
it builds a FAITHFUL end-model -- the real fiber degeneration structure,
the real induced holonomy, the real constraint objects -- and runs both
falsifiers in it, to and including the boundary-at-infinity.

Receipts, both deterministic, numpy only, seeded 20260720, both exit 0:

- `tests/channel-swings/n2_end_family_probe.py` (F2-real)
  -- HEADLINE `14 [E] + 4 [F] = 18 (setup [T] = 3 excluded) ALL PASS`.
- `tests/channel-swings/n2_end_f5_signed_probe.py` (F5-decisive)
  -- HEADLINE `7 [E] + 3 [F] = 10 (setup [T] = 2 excluded) ALL PASS`.

## Headline results

**F2-real (truncated-real grade): the two-section structure EXISTS on the
spacelike-gapped sector of the faithful end, uniformly to the
boundary-at-infinity, and the kill fires NOWHERE.** Admissible
Krein-compatible cuts exist at every sampled collar radius and for the
limit family itself (Gram margin >= 0.43, never degenerating on the
surviving sector); the seam is the deck exchange machine-exactly at every
depth (worst defect 1e-15); neither cut descends anywhere (descent gap
>= 11); the K-sign classification is Z/2, nontrivial, uniformly. Where
the structure fails -- and it does fail, on real parts of the end -- it
fails by EXITING THE EXISTENCE DOMAIN (Krein collision at finite collar
radius on cone-crossing rays; exact K-nullity of the spectral halves in
the timelike regime, a little theorem machine-checked), never by the F2
kill shape (classifying invariant trivial, one section up to
equivalence). Triviality occurs nowhere in the faithful model.

**F5-decisive (truncated-real grade): does NOT fire on the surviving
sector.** The signed C2 accounting responds to the sector flip at every
collar radius and its response ratio |k|/C2^2 converges to a NONZERO
boundary value (0.5975 at the base -> 0.5021 at infinity on the primary
ray; 0.5000 on a control ray), zero-sum exact and holonomy-tied at every
depth, with trichotomy, frame-artifact, and SRC-REJ-1 controls all run at
depth. The magnitude channel is theorem-vacuous at every collar radius --
the DERIVED master identity holds for every real xi, and the end-dressed
symbol is real at every s -- so magnitude invariance on the end is a
regression, never evidence. Outside the spacelike sector the accounting
is UNDEFINED (no admissible cut exists there): the verdict is
sector-relative by structure, not by choice.

**The N2 obstruction, precisely named (this is the swing's third
result).** The faithful end family is NOT uniformly invertible: over the
degeneration rays of the fiber, the boundary symbol family changes Krein
type -- spacelike-gapped (real gap, two-section structure), cone-crossing
(the symbol hits the Krein null cone at finite collar radius: 64-dim even
kernel, spectrum leaves the real axis), and timelike (imaginary spectrum,
K-null halves, no K-definite cut can exist). Seeded sweep over 200
diagonal rays: 132 gapped / 53 crossing / 0 timelike / 15 undecided at
the sampled depth, and the surviving sector is open (20/20 perturbed
conformal rays stay gapped). Every off-the-shelf spectral-section theorem
(Melrose-Piazza shape) requires an invertible -- or at least
gap-uniform -- boundary family; the faithful GU end REFUSES that
hypothesis. What a proof of N2 therefore requires is a new object: a
SECTOR-RELATIVE spectral-section theory -- existence and classification
of Krein-compatible sections relative to the spacelike sub-end, with
controlled behavior at the cone-crossing walls -- over a non-compact
fiber with non-compact structure group, for Krein-indefinite quaternionic
families. That is the exact mathematical shape of the missing theorem;
naming it (with the failure exhibited, not conjectured) is N2 progress of
the honest kind.

## The construction (what "faithful" means here, object by object)

1. **The fiber and its end.** F = Lorentzian forms g on R^4 (dim 10 = 3
   compact RP^3 directions + 7 non-compact shape directions). The collar
   variable s is the radial coordinate of the end; a degeneration ray
   a(s) = exp(2 alpha s) (diagonal, the Weyl slice of the shape space)
   picks the boundary point; s -> infinity is the boundary-at-infinity.
   The loop is the RP^3 generator at every collar radius: the pi-rotation
   congruence g_t = R_t^-T g_s R_t^-1 in a (space, time) plane -- the
   4-dim ORIGINAL of the habitat probe's loop.
2. **The induced (9,5) geometry.** A fiber point g induces on the 14-dim
   chimeric space V = R^4 + S^2(R^4) the form: horizontal block g
   (signature (3,1)); vertical block the DeWitt form G_lam(h,k) =
   tr(g^-1 h g^-1 k) - lam tr(g^-1 h) tr(g^-1 k). For every lam > 1/4
   the vertical signature is (6,4) and the total is the program's frozen
   (9,5); lam = 1/2 is used and the lam-dependence is controlled in-probe
   (lam = 0.3 and 1.0 change nothing headline; lam < 1/4 breaks the
   signature to (10,4) -- the frozen signature PINS the coefficient
   family). Closed-form G-orthonormal frames on the Weyl slice, with a
   deterministic gauge inside degenerate eigenvalue clusters.
3. **The family.** D(t,s) = c(xi(t,s)) with xi(t,s) the components of ONE
   fixed covector in the transported frame rho(R_t) F_s, on the verified
   Cl(9,5) = M(64,H) rep. At (t,s) = (0,0) this reproduces the repo
   symbol XI exactly, hence the anchors bare = 58.7215, C2 = 155.3625:
   the end-model at s = 0 IS the shadow probes' model; everything before
   this swing is its s = 0 slice.
4. **The faithful holonomy (the fidelity upgrade over the toy).** The
   rotation acts on BOTH factors of V, so the seam flips SIX legs
   {0,3,4,9,11,12} -- 2 horizontal plus 4 INDUCED vertical space-time
   modes -- and the deck is U_h = g0 g3 g4 g9 g11 g12 (U_h^2 = +I).
   Exactly 3 of the 6 flipped legs are K_S factors, so U_h K_S U_h^-1 =
   -K_S: the twist SURVIVES the faithful holonomy. This was a genuine
   exposure -- an even count would have killed the carrier. The toy's
   2-leg holonomy FAILS the faithful seam (defect 8.0): the induced
   vertical flips are load-bearing, and the faithful same-sign-plane seam
   (also 6 legs, but FOUR K_S factors -- even) is untwisted, so the
   trichotomy survives faithfully with the corrected mechanism. This
   parallels the habitat swing's dossier-1.2 repair: the toy's conclusion
   stands, its holonomy was a truncation of the real one.
5. **The C2 accounting on the end.** X(s) = Gamma (I x c(xi(0,s))) Pi_RS
   with the real 1792-dim constraint structure, computed by the DERIVED
   closed form X_a = e_a c + (6/7) c e_a (verified against the full build
   at 3.4e-16). Sector datum = the canonical Krein cut of the boundary
   family at that radius; the two dressings are the genuine holonomy pair
   (deck identity consumed at every s).

Truncations, named: symbol grade (no Dirac OPERATOR on the end, no L^2
spaces, no APS problem -- the N2 theorem); the Weyl slice of rays
(null-shear degenerations not sampled); one loop class (pi_1 = Z/2, the
generator suffices); finite collar sampling with the limit family
computed in closed form (convergence rate e^{-3s}, measured 20.1/unit-s
against e^3 = 20.1).

## What the end adds beyond the toy (the honest ledger)

1. The gap is CONTINGENT on the end: the toy family was gapped by the
   frozen symbol's content; the faithful end makes gap survival a
   ray-by-ray question, and the answer is a genuine trichotomy of end
   sectors with the crossing walls at finite collar radius. The
   two-section structure is a property of the SPACELIKE SUB-END, not of
   "the end" simpliciter -- new structure invisible at toy grade.
2. The holonomy is richer and the twist still survives: 6 legs, odd
   K_S-count, forced correction of the toy seam.
3. The K-nullity little theorem: for q < 0, K_S D Hermitian + imaginary
   spectrum forces x^H K_S x = 0 on the halves -- in the timelike regime
   the two-section question is not merely hard, it is structurally empty
   (no K-definite cut exists at all). Kill-shape honesty: this is
   existence-domain failure, not classification triviality.
4. The F5 response survives the limit and its mechanism decomposes: at
   the boundary the signed response is scalar-cut dominated (the derived
   closed form splits k = (26/7)|xi|^2 tr(K_S Q) - (2/7) tr(K_S Q B); the
   bivector share drains as the vertical mixed legs decay, ratio 0.5975
   -> 0.5021, and survives nonzero only on rays whose limit keeps mixed
   content), while the response itself survives on EVERY sampled
   surviving ray -- including a control ray with ||B_inf|| ~ 0, where the
   K-definiteness of the cut alone carries it (ratio 0.5000).
5. The standard-fork record extends to the end: the positive-Hilbert cut
   descends (sees no datum) at every collar radius including the limit
   family -- the known false-kill fork stays false uniformly on the end.

## Council pass (inline, five lenses)

- **Spectral geometer:** the right Melrose-Piazza-shaped statement to aim
  for is now visible and is NOT the textbook one. MP existence of
  spectral sections needs the boundary family invertible (or with
  uniform spectral gap) over a compact base; here the base of the family
  is the non-compact fiber itself and invertibility fails on an exhibited
  open set of rays. The theorem N2 needs is sector-relative: sections
  over the spacelike sub-end with prescribed wall behavior. The collar
  computations (deck exchange at every s, margin uniformity, the limit
  family carrying the full structure) are exactly the finite content such
  a theorem would have to reproduce; nothing computed contradicts its
  existence, and the failure modes are located where its hypotheses must
  sit. What is NOT reached: any operator-grade statement -- no
  self-adjointness theory, no Fredholmness, no K-group. Grade honestly:
  truncated-real, existence side; theorem side untouched.
- **Index theorist:** the classification claimed is the finite-margin
  continuous Z/2 invariant, uniform over the surviving sector including
  the limit -- the KO-shadow, not a KO computation; the covering and
  separates-components steps stay IMPORTED-standard. The important
  index-theoretic negative stands sharpened: the kill shape F2 names (a
  VANISHING classifying group) is now known to be the wrong failure mode
  for this family everywhere it can be tested -- the real dichotomy is
  existence-domain vs. two-sections, not one-section vs. two-sections.
  Any future N2 theorem should be stated against that dichotomy.
- **Krein-space analyst:** two exact structural facts do real work: (i)
  K_S D Hermitian for the whole family (the Krein-native presentation),
  which yields the K-nullity theorem in the timelike regime by a
  two-line argument -- definitizability fails there in the strongest
  possible way; (ii) on the spacelike sector the Gram margin is bounded
  below along the collar and AT the limit, which is precisely the
  uniform definitizability a sector-relative theory would posit. The
  collision walls are where positivity fails by rank, not by leakage --
  the 64-dim even kernel is the Kramers signature of the quaternionic
  structure, consistent throughout.
- **Numerical analyst (truncation faithfulness):** what the finite model
  provably preserves: the rep is exact (Clifford residuals ~ 1e-15); the
  frames are exact closed forms on the Weyl slice (orthonormality 2e-16)
  with a deterministic degenerate-cluster gauge (the one place numerics
  could have injected a spurious discontinuity -- located and fixed, and
  the t-continuity of the cut verified by 8x refinement scaling at the
  worst step, 1.77 -> 0.22); the collar scaling law is machine-exact so
  the limit family is closed-form, not extrapolated; X via the derived
  block form matches the full 1792-dim build at 3.4e-16. What it cannot
  see: operator/domain effects (deliberately out of scope), null-shear
  rays, and s-continuity of the cut gauge across rays (all statements
  are per-s or closed-form; nothing consumed s-continuity).
- **Adversarial referee ("toy dressed as real?"):** charges considered.
  (1) "The DeWitt lam is a fit." Answer: the frozen (9,5) signature pins
  lam > 1/4; two other values re-run headline-identical; the excluded
  regime breaks the signature and is shown to. (2) "The Weyl slice is
  cherry-picked." Answer: generic diagonalizable rays reduce to it by
  fiber symmetry; the non-sampled null-shear rays are named as a
  truncation; and the sweep's 200 rays plus openness test make the
  surviving sector a stable open set, not a curated example. (3) "The
  limit family is an artifact of normalization." Answer: the scaling law
  is exact, the limit direction is closed-form, and the limit family
  satisfies the same seam, cut, deck, and classification identities as
  every finite-s slice -- at machine precision, not asymptotically. (4)
  "F5's surviving response just reads the cut, not the sector." Answer:
  partially conceded and typed: at infinity the response is scalar-cut
  dominated, and the zero-sum theorem makes ALL of it relational; but
  the sign is the sector (deck transport = sign flip at every radius,
  trichotomy and covariant-dressing controls at depth), which is exactly
  the storable-but-locally-unreadable typing -- the response never
  becomes an absolute readout, and SRC-REJ-1 holds on the whole collar.
  (5) "Symbol grade proves nothing about operators." Answer: correct,
  and stated everywhere; the claim is existence-side narrowing plus
  obstruction-naming, not the theorem.

## Grade statements (per result)

- Two-section existence + deck exchange + Z/2 classification on the
  spacelike sector, to and including the boundary-at-infinity:
  **truncated-real, NATIVE-PROVEN (matrix grade)** -- real fiber
  degeneration, real induced holonomy, real constraint anchors; symbol
  grade; Weyl slice; the two standard steps IMPORTED-standard.
- The end-sector trichotomy (gapped / crossing / K-null) and the failure
  of uniform invertibility: **truncated-real, NATIVE-PROVEN (matrix
  grade)**, with the K-nullity lemma **NATIVE-DERIVED (paper grade,
  two-line proof machine-checked)**.
- F2 verdict: the kill does NOT fire at truncated-real grade; N2 theorem
  grade remains open with the obstruction named (sector-relative
  spectral-section theory over a non-compact fiber, non-compact structure
  group, Krein-indefinite quaternionic family, symbol changing Krein type
  across the end).
- F5 decisive form: does NOT fire at truncated-real grade on the
  surviving sector (nonzero signed response at infinity on every sampled
  surviving ray; magnitude channel theorem-vacuous everywhere; accounting
  undefined outside the sector). Operator-grade F5 = the same N2 gap.
- The faithful-holonomy correction (6-leg seam, twist survival, toy seam
  failure): **NATIVE-PROVEN (matrix grade)**; the toy probes' conclusions
  survive re-derivation under the corrected deck.

## Falsifier ledger (dossier Section 6, updated at this grade)

- F1 habitat / F3 twist: did not fire (habitat swing); the twist now
  additionally survives the FAITHFUL induced holonomy (this swing).
- F2 existence: did NOT fire at toy grade (shadow swing) and does NOT
  fire at truncated-real grade (this swing): two-section structure on the
  spacelike sub-end, uniform to the boundary; failure elsewhere is
  existence-domain, never triviality. Theorem grade: open, obstruction
  named.
- F4 blindness (double edge): untouched here; the signed channel remains
  relational-only at every depth (consistent, not decisive).
- F5 relevance: decisive form run in the faithful end-model: NOT FIRED on
  the surviving sector; magnitude form theorem-vacuous at every collar
  radius; sector-relative domain honesty recorded. Operator grade: open
  (= N2).
- F6-F8: untouched; SRC-REJ-1 re-verified as a guard along the whole
  collar.

## Receipts

- Probes (deterministic, numpy only, seeded 20260720, both exit 0):
  `tests/channel-swings/n2_end_family_probe.py` (14 E + 4 F + 3 T),
  `tests/channel-swings/n2_end_f5_signed_probe.py` (7 E + 3 F + 2 T).
- Objects: verified Cl(9,5) = M(64,H) rep via
  `tests/generation-sector/gen_sector_bridge.py` /
  `tests/oq_rk1_cl95_explicit_rep.py`; anchors 58.7215 / 155.3625
  reproduced in-probe on the full 1792-dim build; K_S conventions
  identical to the habitat/shadow probes; base-point slice identities
  with the shadow probes verified in-probe (r = 129.2640, k = 14421.0,
  ratio 0.5975).
- Theorem consumed: the master identity / closed form of A, DERIVED for
  all real xi (`explorations/master-identity-mechanism-2026-07-20.md`,
  `tests/channel-swings/master_identity_mechanism_probe.py`) -- cited,
  regression-checked on the collar, not re-derived.
- Construction discipline: `GEOMETER-VS-PHYSICS-OBJECTS.md` -- every
  load-bearing object's construction named above; both cut forks computed
  on the end (standard fork recorded blind at every depth); killed list
  honored (C2 a norm with its closed-form law regression-checked, never
  an index; no eta-based count; no positive-Hilbert default; no
  equivariant compensator).

## Boundary

Exploration tier under the standing axiom, R0_COND working grade
(except the K-nullity lemma and the consumed master identity, which are
unconditional algebra). The results are truncated-real: real fiber
degeneration, real induced holonomy, real constraint structure, symbol
grade -- NOT the N2 theorem; no operator on the end, no families
pushforward (N1), no BV weld (N3), no K-theory. Nothing here moves claim
status, canon verdicts, scorecard rows, N-accounting, or public posture;
the bit's VALUE remains externally posited (p2c-owned); the scale element
and Door B are untouched; no cross-owner writes; no external actions.
Next rungs in order of exposure: (i) state the sector-relative
spectral-section conjecture precisely (the wall behavior is the only
undetermined clause -- the finite content on both sides of the wall is
now computed); (ii) the M2 lambda_0 scale-dial leg on the collar (the cut
scale is now a genuine dial of a genuine family); (iii) N1/N3 as named,
with the operator-grade F2/F5 waiting on the named new mathematics.
