---
artifact_type: exploration
status: exploration (W139 / full-roster steelman sweep, MATHEMATICS family = slice B geometric/structural; 14 personas inline, one worker, no sub-agents; assumption-first hypothesis generation, kill rigorously afterwards)
created: 2026-07-14
wave: W139
hypothesis: "Joe's framing, steelmanned per persona: IF the dark-energy/cosmological constant is a SET ISSUANCE RATE, that issuance gets DISTRIBUTED THROUGH THE OBSERVERS in the system; find the distribution FUNCTION F solid enough to serve as an ASSUMPTION LEG so the source action, the spec FITs, and the observer-slice structure can be backed into."
title: "W139 -- MATHEMATICS-family steelman sweep of the issuance-distribution framing: 28 candidate distribution functions (two per persona), each with its assumption leg and its test, scored against the W138 kill battery. Six killed at generation; top survivors are the stationary-varifold ensemble law (GMT), the spectral-action heat-kernel distribution (NCG), the C-compression share law (rep theory / NCG), the EL-residual gradient-flow schedule (geometric analysis), and the parallel-tractor uniqueness law (conformal geometry)."
grade: "exploration / hypothesis-generation, conditional register throughout. NOTHING here is asserted; every story is of the form 'under the issuance declaration (W136 sense) plus this story's own named assumption leg'. No new computation was required for scoring (all gate checks reduce to citations of computed bounds in W136/W137/W138/W129/W130); no test file is shipped. Tri-repo gating enforced: capability MEASURE belongs to TaF; whether the distribution is genuine issuance vs disclosure belongs to temporal-issuance; everything below is GU-side mathematics only, and 'issuance' is used solely as the W136 local postulate label. No canon / RESEARCH-STATUS / claim-status / verdict / posture change."
depends_on:
  - explorations/two-track-persona-sweep-2026-07-11/B-geometric-structural.md
  - explorations/two-track-persona-sweep-2026-07-11/SYNTHESIS.md
  - explorations/W136-issuance-declaration-propagation-2026-07-14.md
  - explorations/W137-observer-slice-structure-2026-07-14.md
  - explorations/W138-issuance-kill-battery-2026-07-14.md
  - explorations/W129-oq2-m2-band-sweep-de-exclusion-2026-07-14.md
  - explorations/W130-native-graviton-oneloop-block-2026-07-14.md
  - explorations/source-action-requirements-spec-2026-07-13.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
---

# W139 -- MATHEMATICS family: steelman sweep of the issuance-distribution framing

## 0. The framing being steelmanned, and the misreading being avoided

**Joe's framing (verbatim intent, this wave):** IF the dark-energy/cosmological constant is a
SET ISSUANCE RATE, then that issuance gets DISTRIBUTED THROUGH THE OBSERVERS in the system in
some way. The goal is the FUNCTION describing that rate/distribution -- a function solid enough
to serve as an ASSUMPTION LEG so the rest of the story (the source action, the spec's FITs, the
observer-slice structure) can be backed into. Posture is explicitly assumption-first: generate
strong candidate stories now, kill rigorously afterwards.

**The misreading NOT tested here:** this is NOT the claim that record creation consumes positive
issuance. That naive positive-ledger reading was already falsified pointwise in W137 (the
deformation-cost form is SIGNED and indefinite, exact witnesses +32/-32 w^2 inside the traceless
sector). Every story below either builds on the SIGNED ledger or routes around the ledger
entirely. No story below asserts a positive per-record cost.

**The structural insight the whole family exploits:** under the W136 issuance declaration the
TOTAL schedule is already pinned -- f0 = 0 is the natural point, exact LCDM, w = -1, schedule
drift bounded < 0.3 per e-fold (W129 band = W138 G2). So the SET RATE is not where the freedom
lives. The freedom, and therefore the candidate assumption leg, lives in the PARTITION: how the
fixed total is distributed over the observer-slice structure (sections sigma: X4 -> Y14, the
theorem-grade W137 skeleton). Every distribution function F below is a partition law on section
space or on fluctuation-mode space, with the total held at the declared constant. That design
choice is what lets most stories clear G2 by construction.

**Binding evidence pack honored throughout:**

- W136 (cc227b0): bulk-flatness uniquely selects beta/alpha* = 2 (SA-G5 pinned, KEEP branch);
  f0 = 0 exact-LCDM natural; a0-as-physical-Lambda DEAD in both measure forks; only the
  two-scale escape band mu_emb/mu_DW in [0.41, 0.57] or [0.63, 0.85] survives there; Majorana
  OOM click 1.3e16 GeV; Yukawa dimensional no-go; cure sector Hom-disjoint (1792/1664/128).
- W137 (9cb9f4c): slice = section is theorem-grade; conjecture C1 (record space =
  section-compressed C-operator positive subspace, conditional on W132); the signed
  deformation-cost ledger (D1: linear term -8u; D2: indefinite; D3: exact points).
- W138 (ec00fbd) kill battery, binding on every story: G1 conservation (ledger named; background
  Q^nu = q(t) u^nu; local enhancement < ~1e19; H10/H52 mediator floors), G2 mimic (drift < 0.3
  per e-fold; must NOT claim the DESI wiggle), G3 H36 non-reimport (no rho = c_L mu_DW^4,
  exclusion >= 4.775x), G4 B2 non-reimport (no structural constant read as a rate;
  filtration/schedule readings explicitly alive), G5 de Sitter relabeling (E_Lambda =
  T_dS S_dS / 1.46; a normalization derived from that identity alone fails NOVELTY), G6
  Landauer (informative).
- Prior hard kills stand: W122/W126 tachyon chain; H46C/W129 DE exclusion (a Lambda-mimic is
  REQUIRED and, under W136, natural).

**Construction-fork discipline (GEOMETER-VS-PHYSICS-OBJECTS.md):** each story names whether it
lives program-native (the pinned Convention-B section machinery, the W130/W131 operators) or
standard-field (EFT wrapper, GR conservation). Default is program-native, because the
observer-slice skeleton (W137 Section 1.1) only exists there.

**Roster covered (the sweep's slice B, the geometric/structural-mathematics family, all 14):**
(1) differential geometer, (2) geometric analyst, (3) higher-spin/RS specialist,
(4) representation theorist, (5) index theorist, (6) spin-geometry/Clifford specialist,
(7) symplectic/Poisson geometer, (8) category theorist, (9) homotopy theorist,
(10) twistor/conformal specialist, (11) K-theory/NCG specialist, (12) gauge-theory/moduli
geometer, (13) wild frontier mathematician, (14) GMT/calculus-of-variations specialist.
Run inline, sequentially, one context.

Notation used below: sigma is a section, W(sigma; x) the pointwise family cost density
alpha |II|^2 + beta |H|^2 at the W136-selected ratio beta/alpha = 2 (family constant = 0,
family a1 = 3, tadpole vanishes), q_tot the declared total issuance per unit time (constant,
w = -1), F the candidate distribution function (per-observer or per-mode share of q_tot).

---

## 1. Differential geometer (Cartan connections, soldering, torsion)

### Story 1A -- induced-volume distribution

- **(i) F.** The issuance is distributed per unit INDUCED volume of the observer's slice:
  F(sigma; x) = q_tot * sqrt(det sigma*gimmel) / integral_X4 sqrt(det sigma*gimmel). The
  distribution is a function of nothing but the section's induced metric gbar = sigma*(gimmel);
  at the constant section it is exactly uniform, and deformations redistribute at second order
  in the jet (the volume element is stationary at first order for traceless deformations).
- **(ii) Assumption leg.** Pins SA-G6 (the overall normalization alpha): under this F, alpha is
  the conversion factor between the boundary supply and per-unit-induced-volume density, so the
  spec's free normalization becomes the ratio q_tot / vol_gbar -- one named number instead of a
  band. Secondary: it gives W136's "GU-native home of the flux" row (declared, not derived) a
  candidate derivation: the flux couples to the induced volume form, i.e. the pure-trace channel,
  reproducing T^iss = -rho g automatically (G1a form).
- **(iii) Test.** Jet-level exact computation with the existing W126/W137 sympy machinery:
  expand sqrt(det gbar) on the conformal family and the traceless directions to second order and
  check (a) first-order stationarity (uniformity of F at the vacuum), (b) that the second-order
  redistribution is proportional to the W137 signed cost in the trace channel only. Enhancement
  over uniform is O(metric potential) ~ 1e-6 in the solar system, clearing G1b by ~25 orders.

### Story 1B -- torsion-current distribution

- **(i) F.** In the Cartan-connection reading (one connection on Y14 soldering base and fiber),
  the issuance current is carried by the torsion channel: F(sigma; x) = q_tot *
  |Theta(sigma)|^2 / integral |Theta|^2, where Theta is the torsion of the unique Cartan
  connection whose soldering datum is sigma. Observers on torsion-free slices receive the
  uniform share; torsion concentrates issuance.
- **(ii) Assumption leg.** Pins the source-action TERM that carries S_iss: the torsion-square
  invariant, which is the one quadratic invariant of the Cartan datum absent from the
  alpha |II|^2 + beta |H|^2 family. If the leg holds, SA-G9 (matter coupling) inherits a
  derivation route: matter couples to issuance only through torsion sources (spin density),
  which are negligible for unpolarized matter, explaining the G1d clearance structurally.
- **(iii) Test.** Hom-disjointness check in the W136 F1-F3 style: compute whether the torsion
  channel of the pinned construction has nonzero overlap with the pure-trace Lambda channel.
  If the Hom space is zero the story dies exactly the way the cure sector did (no operator for
  the datum to feed); if nonzero, the overlap coefficient is the story's first number.

## 2. Geometric analyst (Willmore / second fundamental form)

### Story 2A -- Willmore-share distribution (boundary-balanced)

- **(i) F.** The issuance share of an observer is its family Willmore energy:
  F(sigma) = q_tot * integral_X4 W(sigma; x) dvol / (ensemble total), with W the family density
  at beta/alpha = 2, where the family constant vanishes identically so NO background subtraction
  is needed -- F is a bona fide function on section space with F(constant section) = 0 and the
  supply entering entirely through the boundary term of the first variation.
- **(ii) Assumption leg.** Pins W137's conjecture C2 (boundary-balanced record cost) as the
  distribution law itself: the assumption leg is "the integrated first variation of the family
  functional along any admissible deformation family equals the boundary influx F", which backs
  into the source action's boundary term (the W136 wrapper's declared row) as the UNIQUE
  functional whose variation balances the signed bulk bookkeeping. The signed ledger stops being
  an embarrassment: deformations that release density (the -32 directions) are net EXPORTERS to
  the boundary, deformations that pay (+32) are importers; the distribution is the flux map.
- **(iii) Test.** The named C2 computation nobody has run: the integration-by-parts of the first
  variation on Y14 sections. Compact-support control (boundary term must vanish, so the bulk
  bookkeeping must integrate to zero against compact deformation families) is the kill; the
  W103 tail-quotient slot is the retreat landing if the balance is forced asymptotic. Existing
  jet machinery suffices for the compact-support half.

### Story 2B -- EL-residual (gradient-flow) schedule

- **(i) F.** The issuance rate drawn by an observer is the squared Euler-Lagrange residual of
  its slice: F(sigma) = q_tot * ||EL(sigma)||^2_{L2(gbar)} / ensemble normalization, where EL is
  the first-variation operator of the family functional at beta/alpha = 2. At the selected ratio
  flat space is a genuine vacuum (W136: tadpole vanishes), so F = 0 at equilibrium and grows
  quadratically in the deformation amplitude: only off-shell (record-creating, in the framing's
  vocabulary) slices draw issuance.
- **(ii) Assumption leg.** Pins SA-G4 (f0) as DERIVED rather than declared: f0 = 0 exactly at
  the vacuum, with the leading correction quadratic in cosmological perturbation amplitude
  (~1e-10 for sigma-Phi ~ 1e-5), i.e. the mimic bound is a CONSEQUENCE of the distribution law,
  not an input. This converts W136's "determined pair" from a naturalness argument into a
  theorem-shaped statement of the conditional theory: the schedule drift is bounded by the
  square of the largest admissible deformation.
- **(iii) Test.** Exact second-order expansion of ||EL||^2 using the W130 Stage-A quadratic form
  (the fluctuation operator IS the linearized EL), evaluated at the family point once the family
  c_W is computed (the settling computation W136 already names). Then the G2 number: predicted
  drift ~ (1e-5)^2 = 1e-10 per e-fold, five orders inside the 0.3 bound, and manifestly NOT the
  DESI wiggle (which needs 0.744).

## 3. Higher-spin / Rarita-Schwinger specialist (Velo-Zwanziger)

### Story 3A -- causally graded zero-mean distribution

- **(i) F.** Take W137's computed causal grading at face value as the distribution law: the
  issuance flow through a deformation mode is the SIGNED cost, F(mode) = q_tot * c(mode)/Z with
  c the exact W137 coefficients (+32 time-space mixing, -32 spatial traceless, -64 MSS, -16/+16
  timelike/spacelike gradient), and the SET total is the second moment (the variance) of the
  signed flow over the O(3,1)-invariant ensemble of 1-jets and 2-jets, not its mean.
- **(ii) Assumption leg.** Pins the interpretation slot W137 left open: what survives of
  "consumption" is a zero-mean signed exchange whose VARIANCE is the declared constant. That
  backs into the a0 = 2 issuance constant as the second moment of the deformation ensemble --
  a new FIT-shaped relation: a0 = Var_ensemble[c] under the invariant measure, which is a pure
  number the construction either satisfies or does not.
- **(iii) Test.** Compute the mean and variance of the exact signed-cost coefficients over the
  O(3,1)-invariant measure on the deformation sectors (finite-dimensional integrals over the
  computed axes; existing exact coefficients). Mean = 0 is the story's first prediction (the
  causal grading balances exactly); the variance-to-a0 ratio is its first number. If the mean is
  nonzero the zero-mean reading dies immediately.

### Story 3B -- characteristic-cone (hyperbolicity-gated) distribution

- **(i) F.** Issuance is distributed ONLY over deformation directions that preserve
  hyperbolicity of the section's induced quadratic operator (the VZ-causal cone): F(mode) =
  q_tot * chi_cone(mode) * gamma(mode) / Z, where chi_cone is the indicator of the causal cone
  of the W131 characteristic variety and gamma(mode) is the W130 sector coefficient. Acausal
  directions receive zero.
- **(ii) Assumption leg.** Pins WHICH sector of the W130 3:2:1 split carries the supply: if the
  paying (+) directions of the W137 ledger coincide with the causal cone, the distribution is
  supported on the TT channel (gamma_TT = 3) and the assumption leg reads "the issuance is a TT-
  sector flux", giving SA-G7's 3:2:1 normalization item its first physical job.
- **(iii) Test.** Overlap computation between the W137 sign decomposition and the W131 null-cone
  symbol: check whether the +32 (paying) direction s_01 lies inside, and the -32 (releasing)
  spatial-traceless direction outside, the causal cone of the characteristic variety. Both
  objects exist in the test suite; the check is a finite symbol evaluation.

## 4. Representation theorist (noncompact real forms)

### Story 4A -- irrep-multiplicity partition (the 3:2:1 law)

- **(i) F.** The fixed issuance decomposes over the section-fluctuation representation channels
  with weights proportional to the computed sector coefficients: F(TT) : F(phi) : F(slice) =
  gamma_TT : gamma_phi : gamma_slice = 3 : 2 : 1, i.e. shares (1/2, 1/3, 1/6) of q_tot. The
  distribution is a function of the channel's representation label only, section-independent.
- **(ii) Assumption leg.** Pins W137's conjecture C3 in the AMBIENT direction: the assumption
  leg is "the issuance partition is a constant of the construction (collective), not of the
  slice", which is exactly C3's section-independence horn. If adopted, SA-G7's 3:2:1
  normalization item is promoted from an unexplained computed ratio to the partition law of the
  declared supply -- the first FIT-adjacent object the issuance framing would explain rather
  than consume.
- **(iii) Test.** C3's own named decision computation: rerun the W130 Stage-A quadratic-form
  extraction around one non-flat background jet. Ratio fixed = this story's leg confirmed at
  first nontrivial order (and the per-slice rival loses its best candidate); ratio moves = this
  story dies and story 4B's per-observer version takes over. Either outcome is informative;
  machinery named and scoped in W137 Section 5.

### Story 4B -- C-compression share law

- **(i) F.** The issuance share of an observer at slice sigma is the relative size of its
  admissible record space inside the collective positive subspace: F(sigma) = q_tot *
  tau(P_sigma H_C+) / tau(H_C+), where H_C+ is the C-operator's maximal positive subspace
  (W132), P_sigma the sigma-localized compression (W137 C1), and tau a fixed trace weight
  (finite rank where available, Dixmier-regularized otherwise, see story 11B). The collective
  object C sets every observer's share; the distribution IS the compression.
- **(ii) Assumption leg.** Pins C1 clause 2 (one section-independent C determines every
  R(sigma)) and adds the partition-of-unity form: over an admissible cover {sigma_i}, the
  compressions must satisfy sum_i tau(P_i H_C+) = tau(H_C+) up to overlap corrections -- a
  precise new compatibility condition that backs into the collective/single matching as a
  measure-theoretic statement. It also gives the framing's "distributed through the observers"
  its sharpest GU-side referent: distribution = compression of the one collective positive
  subspace.
- **(iii) Test.** Exactly W137's K2 (the cheapest named discriminator, tractable with existing
  W54 machinery): compute the compressed metric P_sigma eta_+ P_sigma on a half-space region in
  the W54 free model, check positivity and bounded invertibility, and compute the trace weight.
  Degeneration at the boundary kills the strict-local reading; a finite well-defined share is
  the story's first number.

## 5. Index theorist (Atiyah-Singer, APS)

### Story 5A -- index-density distribution

- **(i) F.** The issuance is distributed per unit local index density of the twisted
  Rarita-Schwinger operator along the slice: F(sigma; x) = q_tot * |ind_loc(x)| / integral,
  where ind_loc is the Atiyah-Singer integrand (Ahat-form times the twist character) of the
  W125/W131 covariant operator restricted along sigma. Records, in this reading, are index
  quanta; the per-generation share is q_tot / |index|.
- **(ii) Assumption leg.** Pins the boundary datum fork e = 1/12 vs 3/8 (the tangential-vs-gauge
  fork the double-major sweep carries): the two forks give different boundary contributions to
  the index density, so requiring the distribution to integrate to the declared total selects at
  most one. The leg is "the issuance normalization is the index normalization", backing into the
  fork as a determined datum rather than a declared one.
- **(iii) Test.** Heavy but scoped: the oc2-y14-weighted-fredholm parametrix machinery is the
  named path. Cheaper first cut: compute the index-density integrand's constant-section value in
  the pinned construction and check whether it is nonzero at all (a zero integrand kills the
  story before any APS work).

### Story 5B -- eta-invariant / asymptotic-boundary distribution

- **(i) F.** The issuance enters ONLY through the boundary at infinity, distributed as an
  eta-density on the asymptotic boundary: F(boundary mode) = q_tot * eta-density / eta-total,
  with the bulk receiving zero direct supply (the bulk Lambda-mimic is the integration-constant
  shadow of the boundary flux, unimodular-ledger style).
- **(ii) Assumption leg.** Pins C2's retreat position AND gives the W103 tail-quotient slot (the
  one typed interface the wall analysis left standing: a positive invertible metric at infinity
  on the asymptotic Krein-null line) its first candidate occupant: the leg is "the issuance flux
  lives on the W103 slot", which simultaneously names the G1a ledger sector (boundary reservoir)
  and explains why compact-support deformations show only signed, zero-net bookkeeping (W137's
  compact-support kill becomes this story's PREDICTION).
- **(iii) Test.** Two halves with existing machinery: (a) verify the compact-support half (the
  bulk first variation integrates to zero against compact families) with the W126/W137 jets --
  if it does NOT, the boundary-only reading is false and the story dies; (b) check that the W103
  slot's positive invertible tail metric admits a nonzero constant flux (a finite one-dimensional
  integral on the asymptotic line model).

## 6. Spin-geometry / Clifford specialist (Cl(9,5), omega-parity)

### Story 6A -- parity-forced metric-only distribution

- **(i) F.** The issuance distributes over the omega-parity grading with ALL weight on the even
  (gravity) sector and ZERO on the odd (matter/RS) sector: F(even) = q_tot, F(odd) = 0. Not a
  choice: the W136 cure-sector computation already shows the Hom spaces are disjoint (1792 =
  14 x 128 RS carrier vs the gravity-sector Lambda channel), so a pure-trace dimensionful datum
  HAS no odd-sector operator to feed. The distribution function is the parity projector.
- **(ii) Assumption leg.** Pins SA-G9 (matter coupling) NEGATIVELY and structurally: matter
  coupling of the issuance = 0 identically, by Clifford parity plus Hom-disjointness. This is
  the story that explains why W138's G1 margin is 1.2e19: the issuance is metric-only because
  the algebra forbids the matter channel, so G1d (sub-mm matter-coupling floor) is cleared
  identically, not accidentally. The spec's matter-coupling FIT becomes a derived zero.
- **(iii) Test.** Extend the W136 F1-F3 Hom-disjointness computation from the cure operator to
  ALL odd-sector operators at the relevant order: verify every odd (matter-side) channel has
  zero overlap with the pure-trace source. Finite representation-theoretic computation on the
  existing 1792/1664/128 decomposition.

### Story 6B -- DeWitt-negative trace-line flux

- **(i) F.** The issuance enters through exactly ONE fiber direction: the DeWitt-negative
  pure-trace line (the direction whose family constant is h0 = -1 < 0 in the new W136 |H|^2
  decomposition). F is the delta-distribution on that line in fiber-mode space: F(mode) =
  q_tot * delta(mode = conformal trace). All other 13 fiber directions receive zero direct
  supply and feel the issuance only through the metric.
- **(ii) Assumption leg.** Pins the W136 fork-table row "the GU-native home of the flux
  (declared, not derived)": the leg is "the flux home is the DeWitt-negative trace line",
  which is the unique fiber direction that (a) carries negative signature (so influx there is
  the signed ledger's natural inlet), and (b) produces a pure-trace stress T = -rho g on
  restriction, i.e. the G1a form is a consequence, not an input.
- **(iii) Test.** Jet-level check with existing code: inject a constant source on the trace line
  in the pinned construction and verify the induced stress is exactly pure-trace (no traceless
  contamination at second order). The W126/W136 slice-decomposition machinery evaluates this
  directly.

## 7. Symplectic / Poisson geometer (moment maps)

### Story 7A -- moment-map level distribution

- **(i) F.** The issuance is distributed over observers by the moment-map norm of their slice:
  F(sigma) = q_tot * |mu(sigma)|^2 / ensemble total, where mu is the moment map of the IG
  action on section space and |mu|^2 = |theta|^2 is the Kempf-Ness energy (the repo's S =
  |theta|^2 reading). Equi-issuance surfaces are moment-map level sets; the vacuum level set
  mu = 0 receives zero.
- **(ii) Assumption leg.** Pins SA-G3 (B_i) as derived: B_i = 0 is the mu = 0 level set, so
  W136's "the theta amplitude has no job" becomes "the theta amplitude's job is the
  distribution, not the background" -- the background stays exactly LCDM (consistent with the
  determined pair) while theta measures each observer's issuance draw. The spec FIT B_i moves
  from determined-by-naturalness to determined-by-the-distribution-law.
- **(iii) Test.** Consistency check against G2 with existing bounds: the level-set drift maps to
  schedule drift through the continuity equation; verify with the W129 band that any admissible
  theta amplitude (f0 bounds 0.027/0.039/0.208) keeps the distribution's back-reaction on the
  total inside 0.3 per e-fold. Symbolic plus cited numbers; no new likelihood run.

### Story 7B -- coadjoint-orbit quantized shares

- **(i) F.** Issuance quantized in units of symplectic volumes of IG coadjoint orbits; F(record
  class) = q_tot * vol(orbit)/sum. Record classes = orbits (Kirillov correspondence).
- **(ii) Assumption leg.** Would pin a discreteness structure on the record space (an orbit
  basis for C1).
- **(iii) Test.** None available: IG = G semidirect Omega^1(ad) is infinite-dimensional and no
  repo machinery regularizes its orbit volumes. KILLED AT GENERATION (untestable with existing
  machinery; see Section 15).

## 8. Category theorist (bicategorical / fibrational)

### Story 8A -- sheaf-descent partition (class-level distribution)

- **(i) F.** The distribution is a Cech 0-cochain on an admissible cover of section space,
  valued in the W107 interface classes, whose coboundary vanishes: F assigns each observer its
  share as the evaluation of ONE fixed global class against the observer's interface class,
  F(sigma) = q_tot * <kappa_global, [sigma]> / normalization. Distribution exists at CLASS
  level; no operator-level current exists.
- **(ii) Assumption leg.** Pins the collective/single matching at the level W137's three-row
  ladder proved is the right one: the leg is "the issuance descends at class level and provably
  NOT at operator level" (W94/W98 non-gluing), which retroactively explains a W138 fact: G1's
  background current is exactly q(t) u^nu with no measurable local operator structure because
  no operator-level current EXISTS -- only the class-level partition does. A distribution that
  is principled about being invisible to local operator probes.
- **(iii) Test.** On the W107 model (where class descent is computed with non-triviality
  controls): check whether a constant global class admits a nonzero partition consistent on
  overlaps (a finite cocycle computation in the existing model). Failure (only the zero
  partition is consistent) kills the story.

### Story 8B -- adjoint-counit normalization

- **(i) F.** F is the counit of the section-functor adjunction evaluated on the collective
  constant; forced up to unique iso if the adjoint exists.
- **(ii) Assumption leg.** Would pin uniqueness of F itself (the distribution is not chosen but
  forced).
- **(iii) Test.** No computable formulation exists this wave; the adjunction is not constructed.
  KILLED AT GENERATION (no test; pure shape).

## 9. Homotopy theorist (bordism, tmf)

### Story 9A -- Gauss-Bonnet boundary (topological-ledger) distribution

- **(i) F.** The issuance enters through the Chern-Gauss-Bonnet BOUNDARY integral of the slice:
  the bulk GB term is null in the W130 basis map (computed), so a GB-sector supply term changes
  no bulk equation of motion; the physical Lambda-mimic is the integration constant of the
  resulting unimodular-style ledger. F(sigma) = q_tot * (GB boundary density of sigma) / total.
- **(ii) Assumption leg.** Pins W138's G1a ledger sector by name: the Bianchi ledger is "the GB
  boundary term plus the unimodular integration constant", a concrete answer to the gate's first
  structural demand. Secondary: because the GB channel is quotiented out of all structural
  equations, G4 is cleared by construction (nothing structural is being read as a rate; the
  supply lives entirely in the quotiented sector).
- **(iii) Test.** Verify GB-nullity extends from the W130 basis map to the family at
  beta/alpha = 2 (the existing plane-wave evaluator, run on the family combination); then check
  the boundary density is nonzero on at least one admissible non-compact deformation (else the
  supply has no inlet and the story dies the C2 compact-support death).

### Story 9B -- tmf q-expansion weights

- **(i) F.** F(n-th record class) = q_tot * a_n / sum a_n with a_n the tmf q-expansion
  coefficients of the relevant class.
- **(ii) Assumption leg.** Would pin an odd-primary grading of record classes.
- **(iii) Test.** None: the mod-3 arena on the actual data is empty (Omega^Spin_5(BG_SM) tensor
  Z_(3) = 0, cited) and no geometry-dependent tmf class has been computed on Y14. KILLED AT
  GENERATION (arena empty plus no computable coefficient).

## 10. Twistor / conformal specialist (tractor calculus, GJMS)

### Story 10A -- conformal-weight -4 distribution

- **(i) F.** The distribution is the unique Weyl-covariant density of conformal weight -4:
  F(x) = q_tot * Omega(x)^{-4} / integral, where Omega is the conformal factor relating the
  observer's induced metric to the reference. The issuance couples at the weight of a
  density-valued cosmological term (rho has weight -4), so the distribution function is FORCED
  by conformal covariance once the coupling weight is declared.
- **(ii) Assumption leg.** Pins the FUNCTIONAL FORM of the source-action boundary term: S_iss
  must be Weyl-covariant of weight -4 (a new FIT-shaped constraint on the W136 wrapper), and
  conservation (nabla rho = 0 for pure trace, the G1a consistency condition) follows identically
  from the weight rather than being imposed. Local enhancement over uniform is O(4 Phi) ~ 1e-5
  in the solar system (metric potential, not matter density), clearing G1b by ~24 orders.
- **(iii) Test.** Jet-level symbolic check: verify that a weight -4 pure-trace source is the
  unique weight at which the Bianchi bookkeeping closes without a compensator field on the
  conformal family (existing machinery; a one-parameter scan over the weight).

### Story 10B -- parallel-tractor uniqueness law

- **(i) F.** F is the top slot of a PARALLEL standard tractor on the slice's conformal class:
  uniform in the tractor gauge, non-uniform in any physical gauge by exactly the Schouten
  corrections, F(x) = q_tot * (parallel-tractor top slot)(x). Distribution = the unique parallel
  section, when it exists.
- **(ii) Assumption leg.** The classical fact does the forcing: a parallel standard tractor
  exists iff the conformal class contains an Einstein metric. So the leg "the issuance
  distribution is parallel-tractor" BACKS INTO the Einstein condition on the observer's slice --
  i.e. it derives, rather than assumes, the survival of the attractive Einstein channel (W136:
  family a1 = 3 at the selected ratio) and predicts flat space is the equilibrium distribution
  carrier (consistent with the vanishing tadpole at beta/alpha = 2). Uniqueness of F is a
  theorem, which is the sharpest assumption-leg shape available in the whole sweep: the
  distribution is not modeled, it is the unique parallel object.
- **(iii) Test.** Verify on the conformal family that the parallel-tractor existence condition
  at the bulk-flat point coincides with the vanishing-tadpole condition (both should single out
  the Einstein/flat locus): a finite tractor-connection computation on the existing jets. If
  the two loci differ, the story is falsified at generation order.

## 11. K-theory / NCG specialist (spectral triples)

### Story 11A -- spectral-action heat-kernel distribution

- **(i) F.** The issuance is the cosmological term of the spectral action and its distribution
  over observers is the LOCALIZED heat trace: F(sigma; x) = q_tot * tr K_{D_sigma}(x, x; t*) /
  integral, where D_sigma is the W131 covariant operator restricted along sigma and K its heat
  kernel at the fixed cutoff scale t*. Uniform at the constant section (translation invariance);
  redistributed by the Seeley-DeWitt densities a_2(x), a_4(x) of the slice under deformation.
- **(ii) Assumption leg.** Pins the family c_W: if the issuance term is the a_0 coefficient of
  the spectral action, then the SAME cutoff function's higher moments determine a_2 and a_4, so
  the declaration plus this F forces the Weyl-channel coefficient of the family at
  beta/alpha = 2 -- exactly the named settling computation W136 hands to a successor wave
  (SA-G8's m2_eff recomputation gate). One assumption leg, one currently-open FIT determined.
- **(iii) Test.** The W130 second-order Gilkey route is already validated as an engine
  (Christensen-Duff trio derived, the /180 shift rule derived): run it on the family combination
  at beta/alpha = 2 and read a_4; compare the extracted c_W against the spectral-action
  prediction from the a_0 normalization. Strongest existing-machinery test in this family.

### Story 11B -- Dixmier-trace equidistribution

- **(i) F.** F(sigma) = q_tot * Tr_omega(P_sigma |D|^{-14}) / Tr_omega(|D|^{-14}): the
  observer's share is the noncommutative volume of its compression, with Tr_omega the Dixmier
  trace (dimension 14 for Y14). This is story 4B's share law with the trace weight made
  well-defined in infinite rank: the noncommutative integral is exactly the tool that turns
  "rank of the compression" into a finite measure.
- **(ii) Assumption leg.** Pins C1's share function against its most obvious degeneracy
  objection (infinite-dimensional compressions have no rank): the leg is "shares are
  noncommutative volumes", which makes the 4B partition-of-unity a statement about the Dixmier
  trace's additivity on the cover -- a checkable measure-theoretic identity rather than a hope.
- **(iii) Test.** In the W54 free model: compute the compressed heat operator's trace on a
  half-space (the Dixmier trace is the t -> 0 coefficient), adjacent to the K2 test and using
  the same machinery; verify additivity over two complementary half-spaces against the global
  trace.

## 12. Gauge-theory / moduli geometer (Donaldson, Uhlenbeck)

### Story 12A -- moduli-volume distribution

- **(i) F.** F = q_tot * (Uhlenbeck volume density on the vacuum moduli space) / Vol(M).
- **(ii) Assumption leg.** Would pin finiteness of Vol(M) (coercivity of the source functional).
- **(iii) Test.** No compactness or volume machinery exists for the IG moduli problem in the
  repo. KILLED AT GENERATION (untestable; the moduli space's non-emptiness is itself open).

### Story 12B -- orbit-volume (measure-fork-selecting) distribution

- **(i) F.** The issuance share of a slice is weighted by the volume of its IG gauge orbit:
  F(sigma) = q_tot * vol(IG . sigma) / total, i.e. more symmetric observers (larger stabilizer,
  smaller orbit) receive proportionally less; generic slices receive the uniform share. In the
  quadratic neighborhood of the constant section this weight is computable from the
  Faddeev-Popov determinant of the W130 fluctuation operator.
- **(ii) Assumption leg.** Pins the repo's MEASURE FORK: the two measures agree on the dphi = 0
  slice and differ off it (W126/W136); the orbit-volume weighting is a selection principle --
  the issuance-natural measure is the one for which the distribution is gauge-orbit-uniform
  (Faddeev-Popov). A standing two-branch convention becomes a determined row under the leg.
- **(iii) Test.** Compute the Faddeev-Popov weight at second order in the deformation on the two
  measure-fork branches with the W130 sector data (the per-sector magnitudes are exactly what
  W130 quantified as measure-dependent); check which branch makes the weighted distribution
  uniform. Finite computation on existing coefficients.

## 13. Wild frontier mathematician

### Story 13A -- filtration-schedule distribution (the G4-legal rate)

- **(i) F.** The distribution is a FILTRATION, not a rate: F assigns to each observer the
  filtration degree function tau -> dim-profile of (F_tau compressed to R(sigma)), where {F_tau}
  is the increasing filtration of the collective positive subspace H_C+ and R(sigma) the
  observer's compression (C1). The issuance "flow" is the derivative of the compressed profile
  along tau -- exactly the schedule/filtration reading W138's G4 explicitly leaves alive (the
  killed thing was structural constants read as rates; filtrations are the allowed object).
- **(ii) Assumption leg.** Pins the one-way bridge object the tri-repo structure needs but does
  not have: a GU-side filtration whose compressions are per-observer. If the leg holds, the
  temporal-issuance repo's D-FORK receives its GU-side shadow through the gate (stress-test
  input, never support), and C1 acquires a graded refinement (records arrive filtered, not all
  at once). GU-side, the pinned object is the grading of H_C+ -- a new named structure the
  W132 C-operator analysis did not need but is consistent with.
- **(iii) Test.** In the W132 order-by-order QM model (branch B, the only place C is explicitly
  constructed): exhibit the perturbative filtration by order, compress to a subsystem, and check
  the profile is well-defined and monotone. Existing toy machinery; a negative (compression
  destroys the filtration) kills the leg cleanly.

### Story 13B -- horizon-area distribution with an |II|^2 correction

- **(i) F.** F(sigma) = q_tot * [A(sigma)/A_H] * [1 + c * integral |II_sigma|^2] / Z, where
  A(sigma) is the apparent-horizon area of the observer's causal patch and the |II|^2 correction
  is the NEW degree of freedom that separates the story from the Gibbons-Hawking identity.
- **(ii) Assumption leg.** Would pin c as a boundary coefficient of C2 (the correction is the
  non-relabeled content; the area prefactor alone is G5-dead by construction and is included
  only as the zeroth term).
- **(iii) Test.** Compute whether the correction survives G5: subtract the pure-area part and
  check the residual normalization does not reduce to T_dS S_dS / 1.46; then the G2 drift of the
  correction term. Honest flag: if c is fitted rather than derived, the story is one free
  parameter away from unfalsifiable; scored low unless c comes out of the C2 boundary
  computation.

## 14. GMT / calculus-of-variations specialist

### Story 14A -- stationary-varifold ensemble law

- **(i) F.** The observer ensemble is a varifold V on Y14 (sections with multiplicity, the
  measure-theoretic completion of "the collection of all observers"); the issuance is
  distributed per unit varifold mass: F = q_tot * d||V|| / ||V||(Y14). The distribution function
  is the ensemble measure itself, and the DEFINING equation is stationarity: the first variation
  of the family functional against V vanishes, delta_V(alpha |II|^2 + beta |H|^2)|_{beta/alpha=2}
  = 0, even though no INDIVIDUAL section is cost-critical (W137 D1: linear term -8u).
- **(ii) Assumption leg.** The sharpest leg in the sweep after 10B: "the collective is
  stationary where the individual is not." It backs into TWO things at once: (a) beta/alpha = 2
  -- at the W136-selected ratio the flat tadpole vanishes, so the constant-section Dirac
  varifold IS stationary, i.e. the story's defining equation SELECTS the same ratio bulk-flatness
  selected, an independent convergence on the pinned SA-G5 value; (b) the ensemble measure d||V||
  becomes the determined object: stability (second variation, the W130 quadratic form) decides
  which deformation sectors the equilibrium measure can spread into, so the family c_W (the
  named open coefficient) becomes the stability discriminant of the observer ensemble. One leg,
  one pinned FIT re-derived, one open FIT given a job.
- **(iii) Test.** Two steps, both scoped: (a) verify that stationarity of the constant-section
  varifold under the family functional holds exactly at beta/alpha = 2 and fails at every other
  ratio (this is a one-line consequence of the computed a0(alpha, beta) = 2 alpha - beta, W136
  test B5, so step (a) is already effectively computed); (b) the stability half is the SAME
  named settling computation as stories 2B and 11A: the family c_W via the W130 evaluator on
  |H|^2 in the TT sector. Three independent personas' tests converge on one existing-machinery
  computation.

### Story 14B -- Gibbs-measure (canonical-ensemble) distribution

- **(i) F.** F(sigma) = q_tot * exp(-W_family(sigma)/kappa) / Z: the observer ensemble is the
  canonical ensemble of the family functional at beta/alpha = 2, and the SET issuance rate is
  the ensemble temperature kappa (a schedule parameter, G4-legal). The distribution is the
  Gibbs density on section space.
- **(ii) Assumption leg.** Pins the direct-method foundation this persona has demanded all
  along: the leg is "Z exists" (integrability of exp(-W_family) on the admissible class), which
  backs into concrete positivity requirements on the family functional -- specifically, the
  W137 releasing directions (-32 w^2 spatial traceless, -64 u^2 MSS) make the quadratic level
  unbounded below, so Z exists only if higher-order terms restore coercivity. The leg therefore
  converts the signed ledger into a sharp, decidable requirement on the quartic jet.
- **(iii) Test.** Concrete and cheap with the all-orders exact W126-family machinery: expand
  W_family to QUARTIC order along the exact releasing directions (the spatial-traceless w axis
  and the MSS u axis; the MSS interpolant W(u) = 2 - 8u - 64u^2 is already exact and its family
  version is a finite recomputation) and check the quartic sign. Positive quartic on both axes =
  coercivity plausible, story alive; negative or zero = the Gibbs ensemble diverges along an
  exact axis and the story is dead by computation.

---

## 15. KILLED AT GENERATION (with one-line reasons)

| story | persona | one-line kill |
|---|---|---|
| 3A-prime (RS-carrier partition, the draft predecessor of 3A) | higher-spin | issuance cannot reach the RS sector at all: Hom-disjointness is already computed (W136 F1-F3, 1792/1664/128); a partition over channels the datum cannot feed is empty |
| 7B (coadjoint-orbit quantized shares) | symplectic | untestable: IG is infinite-dimensional, no orbit-volume regularization exists anywhere in the repo; zero machinery, zero number |
| 8B (adjoint-counit normalization) | category theorist | the adjunction is not constructed; "forced up to unique iso" with no exhibited functor is shape, not a function |
| 9B (tmf q-expansion weights) | homotopy theorist | the mod-3 arena on the actual data is empty (cited) and no tmf class has been computed on Y14; the distribution has no computable value |
| 12A (moduli-volume distribution) | gauge-theory geometer | the vacuum moduli space's non-emptiness and compactness are themselves open; a distribution over an unconstructed measure space pins nothing |
| 13B (horizon-area with |II|^2 correction) | wild frontier | G5 exposure at the core: the zeroth term IS the Gibbons-Hawking identity, and the correction coefficient c has no derivation this wave, leaving one fitted parameter between the story and a pure relabeling; killed unless C2's boundary computation later supplies c |

(13B is killed conservatively at generation on the novelty gate; it is the only kill above that a
successor computation could reverse, and the reversal condition is named.)

## 16. Scoring pass -- every surviving story against the W138 battery and the evidence pack

Gate key: G1 conservation (a: ledger named / b: enhancement < 1e19 / c,d: mediator floors),
G2 mimic (< 0.3 per e-fold, no DESI claim), G3 H36 non-reimport, G4 B2 non-reimport, G5 dS
relabeling (novelty), G6 Landauer (informative). "auto" = cleared by the shared design (total
schedule = W136 constant; distribution is a partition at fixed total). All verdicts conditional.

| story | G1 | G2 | G3 | G4 | G5 | notes |
|---|---|---|---|---|---|---|
| 1A volume | pass (ledger = boundary supply; enhancement ~1e-6) | auto | pass (no mu_DW) | pass (partition, not rate) | pass (normalization = vol ratio, not T_dS S_dS) | modest leg (SA-G6 conversion only) |
| 1B torsion | pass (metric-sector; spin-density coupling negligible) | auto | pass | pass | pass | leg is real but Hom-disjointness risk is high (may die exactly like the cure sector) |
| 2A Willmore-share | pass (boundary ledger named) | auto | pass | pass | pass | leg = C2 itself; compact-support kill is live and cheap |
| 2B EL-residual | pass | PASS WITH A NUMBER (predicted drift ~1e-10, 9 orders inside; not the DESI signal) | pass | pass (schedule reading, G4's allowed class) | pass | derives f0 = 0 rather than assuming it; test gated on family c_W |
| 3A causal zero-mean | pass | auto | pass | pass | pass | leg (a0 = ensemble variance) is sharp; mean-zero check is immediate and could kill it next wave |
| 3B cone-gated | pass | auto | pass | pass | pass | leg pins the TT channel; overlap test is a finite symbol evaluation |
| 4A 3:2:1 partition | pass | auto | pass | pass | pass | leg = C3's ambient horn; test is C3's own named computation |
| 4B C-compression share | pass (no local current claimed) | auto | pass | pass | pass | conditional on W132/C1 existence (K1); K2 test cheapest in the roster |
| 5A index-density | pass | auto | pass | pass | pass | leg (e-fork determined) is good but the test is the heaviest in the family |
| 5B eta/boundary | pass (ledger = W103 slot, named) | auto | pass | pass | pass | predicts the compact-support result; W103 slot occupancy is novel |
| 6A parity-forced | pass (explains the G1 margin structurally) | auto | pass | pass | pass | leg is a derived ZERO (SA-G9 = 0); explanatory rather than generative |
| 6B trace-line flux | pass (G1a form derived) | auto | pass | pass | pass | pins the declared flux-home row; cheap jet test |
| 7A moment-map | pass | pass (W129 containment cited) | pass | pass | pass | leg re-jobs B_i; weaker than 2B (does not derive the mimic, only respects it) |
| 8A sheaf-descent | pass (explains absence of a local current) | auto | pass | pass | pass | leg is interpretive of proven structure; test on the W107 model is real but the leg pins no FIT row |
| 9A GB-boundary ledger | pass (G1a answered by name) | auto | pass | pass (supply lives in the quotiented sector) | pass | clean ledger story; leg pins G1a's demand, not a spec FIT |
| 10A weight -4 | pass (enhancement ~1e-5) | auto | pass | pass | pass | leg constrains S_iss functional form; uniqueness scan is cheap |
| 10B parallel tractor | pass | auto | pass | pass | PASS AND NOVEL (normalization from parallelism, not horizon thermodynamics) | uniqueness is a theorem; backs into the Einstein channel; test = locus comparison |
| 11A heat-kernel | pass | auto | pass | pass | pass | leg DETERMINES the open family c_W; test engine already validated (W130 Gilkey) |
| 11B Dixmier share | pass | auto | pass | pass | pass | makes 4B well-defined at infinite rank; test adjacent to K2 |
| 12B orbit-volume | pass | auto | pass | pass | pass | leg resolves the measure fork; computable from W130 sector data |
| 13A filtration | pass | auto | pass | PASS BY DESIGN (the explicitly-allowed G4 class) | pass | leg is the tri-repo bridge object; test in the W132 toy model |
| 14A stationary varifold | pass | auto | pass | pass | PASS AND NOVEL | independently re-selects beta/alpha = 2; gives family c_W the stability job; test converges with 2B/11A |
| 14B Gibbs ensemble | pass | auto | pass | pass (temperature = schedule parameter) | pass | decidable by one quartic-jet computation; could die cleanly |

No surviving story claims the DESI wiggle (all totals are exact-LCDM mimics per W136's
determined pair, which is exactly what H46C/W129 requires). No story identifies any scale with
mu_DW (the two-scale escape band was deliberately not used by any story; it remains a separate
named target). No story reads f0, c_L, or alpha_W as a rate.

## 17. Ranking of survivors

Criteria per the brief: (a) sharpness of the assumption leg (does it pin a NAMED FIT/object),
(b) testability with existing machinery, (c) novelty vs the de Sitter relabeling line.

**Tier 1 (top five):**

1. **14A stationary-varifold ensemble (GMT).** Leg pins TWO named objects: independently
   re-derives the pinned SA-G5 = 2 (convergent with W136's bulk-flatness, from a different
   principle: collective stationarity where the individual fails) and assigns the open family
   c_W its job (stability discriminant of the observer ensemble). Test: step (a) already
   effectively computed (W136 B5); step (b) is the named W130-evaluator run. Fully novel vs G5.
2. **11A spectral-action heat-kernel (NCG).** Leg DETERMINES the family c_W, the one FIT-gating
   coefficient W136 explicitly hands to a successor (SA-G8 flag). Test engine (second-order
   Gilkey route) validated in W130. The only story whose leg closes a currently-open named
   computation rather than adding a parallel one.
3. **4B + 11B C-compression share law (rep theory / NCG, one story in two registers).** Leg pins
   C1 clause 2 with a new partition-of-unity condition and makes the share well-defined at
   infinite rank (Dixmier). Test is K2, already named by W137 as the cheapest discriminator in
   the thread. Honest conditionality: dies with C1's K1 if no interacting C exists.
4. **2B EL-residual schedule (geometric analysis).** Leg turns f0 = 0 from natural into derived
   and emits an actual G2 number (drift ~1e-10, nine orders inside the bound, manifestly not
   the DESI signal). Test shares the same family-c_W computation as 14A/11A.
5. **10B parallel-tractor law (conformal geometry).** The only story where UNIQUENESS of F is a
   classical theorem (parallel standard tractor); the leg backs into the Einstein-channel
   survival and the flat equilibrium. Test (locus comparison on existing jets) is cheap. Maximal
   novelty vs G5 (normalization from parallelism, zero horizon-thermodynamics content).

**Tier 2 (alive, run after tier 1):** 4A (C3's ambient horn; its test is the C3 decision
computation and is worth running regardless), 14B (one quartic-jet computation decides it),
6B (cheap jet test; pins the declared flux-home row), 5B (W103 slot occupancy; predicts the
compact-support result), 3A (immediate mean-zero check), 12B (measure-fork selector), 2A
(= the C2 computation), 13A (tri-repo bridge, toy-model test).

**Tier 3 (alive, low priority):** 1A, 1B (high Hom-disjointness risk), 3B, 6A (explanatory
zero), 7A, 8A, 9A, 10A, 5A (heaviest test).

**Convergence note (the sweep's one emergent structural fact):** three independent personas'
top tests (2B, 11A, 14A) reduce to the SAME existing-machinery computation: the family Weyl
channel c_W at beta/alpha = 2 via the W130 plane-wave/Gilkey evaluators -- which is also
W136's own named settling computation for SA-G8. Under this family's reading, that single
computation is now quadruple-loaded: it recomputes the sub-mm floor consistency (W136), fixes
the spectral-action leg (11A), closes the EL-residual schedule number (2B), and decides the
stability of the observer-ensemble equilibrium (14A). It is the clear next computation for the
issuance thread from the mathematics family's side.

## 18. What this does NOT do

No canon / RESEARCH-STATUS / claim-status / verdict / posture change. Nothing above asserts the
issuance declaration or any story's assumption leg; every statement is conditional twice over
(on the W136 declaration AND on the story's own leg). No new computation was run (scoring
reduced to citations of computed bounds); no test file ships with this wave. Capability MEASURE
remains TaF's; issuance-vs-disclosure typing remains temporal-issuance's; the one-way gate is
respected (story 13A supplies a stress-test input through it, never support). The two-scale
escape band, H41, H59, the AF-vs-AS fork, and the tachyon chain are all untouched. W135's
taxonomy had not landed at the time of writing and is not cited.
