---
artifact_type: exploration
status: exploration
created: 2026-07-14
hypothesis: H68
title: "W131 -- THE COVARIANT OPERATOR ON Y14 (H68, W125's single blocking object): first swing, build-or-prove-unbuildable. VERDICT: BUILT-WITH-PROPERTIES at the frame/symbol level. The crux [nabla, Pi] = 0 is a THEOREM, not an estimate: Gamma is so(9,5)-equivariant on ALL 91 generators (boosts included, exact zeros), Gamma Gamma^dag = 14 I gives Pi in closed form, so Pi is parallel for EVERY metric-compatible connection on Y14, in particular the gimmel Levi-Civita spin lift. Krein K is parallel too (nabla K = 0, exact), covariant leakage is 0, and SA-C4's curved-Y14 clause CLOSES at symbol level: the pointwise characteristic variety on actual curved Y14 is the gimmel null cone (signature (9,5) verified on the Lorentzian locus), and every covariantization-generated zeroth-order insert (curvature rho(R), II_s, connection-choice differences) is subprincipal BY ALGEBRA MEMBERSHIP; the W125-D failure mode requires a symmetric first-order insert that metric compatibility can never generate. NOT built: the analytic layer (Fredholm/propagator on non-compact Y14) and SA-G9. E1 flag: the one-object pattern PARTIALLY recurs -- the algebraic half of the blocking object is closed, and the residual is a named analytic object (the Y14 propagator), stated plainly below."
grade: "COMPUTED (exact, on the verified Cl(9,5) = M(64,H) rep): Gamma Gamma^dag = 14 I (residual 0.0); both-sided so(9,5) equivariance of Gamma for all 91 generators (max residual 0.0); [rho(J), Pi] = 0 full-matrix on 6 representative generators including boosts (0.0); Krein parallelism rho^dag K + K rho = 0 for all 91 (factor residuals 0.0); covariant leakage ~1e-14. COMPUTED (numeric, the explicit gimmel metric at native n = 4, Lorentzian): signature (9,5) at sample points; parallel-transport holonomy preserves gimmel to 8.6e-10; Gauss identity at n = 4 (residual 4.7e-8) with II_s nonzero (1.63) and symmetric (3e-14); curved-point characteristic variety = gimmel null cone (frame residual 1.8e-15, null smin 8.9e-21); so(9,5) inserts subprincipal (1.6e-6 at L = 1e6) and Pi-commuting (4e-15). ARGUED (standard differential geometry, cited): metric compatibility <=> so(9,5)-valued connection form in orthonormal frames (the parallel-transport check B2 is the machine witness); the Weitzenbock/curvature terms of D^2 are rho(R)-type. Per the E1 rule this wave is a CONSTRUCTION: zero FIT rows move, no gated number unlocks. Status movements: SA-C4's curved-Y14 clause moves from argued-rides-a-citation to machine-checked at symbol level; acceptance leg (a) loses its curved-clause blocker at symbol level; leg (d) and SA-G9 do NOT move."
construction: "program-native throughout (GEOMETER-VS-PHYSICS-OBJECTS.md): the covariant operator is the geometer's object -- the constant equivariant projector Pi transported by the gimmel Levi-Civita spin lift, with the constraint enforced kinematically on curved Y14 exactly as at the flat level. The standard-field objects used where they are the right ones: the Gauss formula and O(9,5) holonomy of Riemannian submanifold geometry (theorems, machine-witnessed), the DeWitt fiber metric signature arithmetic. The physicist's alternative (F-analytic Porrati-Rahman vertex, Schur/E-block route) stays untouched and blocked, exactly as W125 recorded."
depends_on:
  - explorations/W125-source-action-first-build-2026-07-13.md
  - explorations/source-action-requirements-spec-2026-07-13.md
  - explorations/landscape-assessment-post-three-waves-2026-07-14.md
  - explorations/wave34/source-action-landscape-scan-2026-07-11.md
  - canon/w2-y14-spin-structure.md
  - tests/W125_built_candidate_assembly.py
  - tests/W125_sac4_subprincipal_built.py
  - tests/vz_fcvz4_subprincipal.py
  - tests/wave5/H21_theta_equals_II_proof.py
scripts:
  - tests/W131_covariant_operator_y14.py
---

# W131 -- the covariant operator on Y14: built at frame/symbol level

Test: `tests/W131_covariant_operator_y14.py` (12/12, exit 0). Deterministic (fixed seed
20260714); the algebra runs on the repo's verified Cl(9,5) = M(64,H) representation; the
geometry runs on the explicit gimmel metric (base block h, trace-reversed DeWitt fiber block)
at native base dimension n = 4, Lorentzian.

Run as a 5-persona inline team (one worker, sequential): (1) differential geometer;
(2) representation theorist; (3) higher-spin/causality specialist; (4) computational engineer;
(5) honesty auditor (E1/Lakatos).

**What this wave is.** W125 compressed the whole source-action program onto one blocking
object: "the covariant operator on Y14" (blocking acceptance legs (a)-full and (d)-full,
SA-G9's arena, FC-VZ-1, and the first source-action-derived number). The 2026-07-14 landscape
assessment E1-flagged the compression ("naming is a map, not progress") and dispatched H68:
build it or prove it unbuildable, time-boxed. This is the first swing. The outcome is a
genuine build at the frame/symbol level, and the reason it went through cleanly is a
structural fact nobody had checked: the crux commutator [nabla, Pi] vanishes as a theorem.

---

## 0. The specification (what "the covariant operator on Y14" must be)

Assembled from the spec's consumers (SA-C2, SA-C4, SA-U1, acceptance legs (a) and (d)),
before building. The operator is

```
D  =  Pi (gamma^I nabla_I) Pi  +  m2 Pi
```

acting on sections of ker Gamma inside the Rarita-Schwinger bundle T*Y14 (x) S(9,5) over
Y14 = Met(X4), and it must have:

| # | Property | Consumer | Status this wave |
|---|---|---|---|
| P1 | Bundle exists: spin structure on Y14 with the (9,5) gimmel metric | whole build | INHERITED PRECONDITION: X4 spin (canon W2-01: w2(Y14) = pi* w2(X4)); gimmel signature (9,5) on the Lorentzian locus VERIFIED pointwise (B1) |
| P2 | Connection: nabla = gimmel Levi-Civita spin lift on S, Levi-Civita on T*Y14 (A = spin-lift(grad^gimmel), wave34 ledger item 2) | SA-G1 frame | DECLARED (same postulate as W125; not consumed silently -- see 5.1) |
| P3 | [nabla, Pi] = 0: Pi stays well-defined and idempotent under covariant differentiation | SA-C2 on curved Y14 | **PROVED + machine-checked, exact (A1-A3)** |
| P4 | Covariant leakage 0: Gamma D = 0 on all sections | SA-C2, acceptance (a) | **machine-checked, exact (A5)** |
| P5 | Principal symbol degree-1-exact pointwise; characteristic variety = gimmel null cone; covariantization corrections subprincipal | SA-C4 curved clause | **machine-checked (C1-C3); structure theorem, not estimate** |
| P6 | Krein compatibility: nabla K = 0, D Krein-self-adjoint including connection terms | SA-U1 tree leg | **machine-checked, exact (A4 + C3)** |
| P7 | Flat limit reproduces W125 | positive control | **machine-checked (C1: all anchors reproduced)** |
| P8 | Analytic layer: propagator/Fredholm theory on non-compact Y14; loop arena | SA-U1 loop items, leg (d) | **NOT BUILT (named residual; section 5)** |

## 1. Persona 1 (differential geometer): the geometry supplies the hypotheses

The whole build stands on one classical fact: **a metric-compatible connection has an
so(p,q)-valued connection form in any orthonormal frame.** Everything the covariant operator
adds to the flat symbol model (connection terms, curvature terms, the section insert II_s)
therefore acts on the RS bundle through the so(9,5) representation rho = rho_V (x) 1 + 1 (x)
rho_S. The wave machine-checks that this hypothesis is the ACTUAL Y14 geometry, not a model:

- **Signature (B1).** At Lorentzian sample points the explicit gimmel metric (base block h,
  trace-reversed DeWitt fiber V_h(k,l) = tr(h^-1 k h^-1 l) - (1/2) tr(h^-1 k) tr(h^-1 l))
  has signature exactly (9,5) = base (3,1) + fiber (6,4). This is the load-bearing pointwise
  identification: the eta(9,5) flat model of W125 IS the tangent model of curved Y14.
- **Holonomy (B2).** Parallel transport along a curve in Y14 (RK4 on finite-difference
  Christoffels of the explicit metric) preserves gimmel inner products to 8.6e-10: the
  holonomy sits in O(9,5), the machine witness for "connection form in so(9,5)".
- **The section insert (B3).** The Gauss identity at NATIVE n = 4 (H21 proved it exactly at
  n = 3; here numeric, off-shell data): the tangential part of the ambient derivative along
  a graph section equals the Koszul bracket of the induced metric (residual 4.7e-8), and the
  normal residual II_s = s*(theta) is nonzero (norm 1.63) and symmetric (3e-14). So II_s is
  a real datum, and it enters the section-pulled RS operator as a BLOCK OF THE so(9,5)
  CONNECTION FORM (the tangent-normal mixing block, skew by metric compatibility of both the
  ambient and adapted connections) -- which is exactly what feeds Persona 3.

The induced connection is then P2: Levi-Civita on the T*Y14 factor, spin lift on S. Nothing
else is available without adding non-metric structure, and the build needs nothing else.

## 2. Persona 2 (representation theorist): [nabla, Pi] = 0 is a theorem

The question the task named as the crux -- does the soldering make Gamma parallel -- has a
sharper answer: **Gamma is parallel for EVERY metric-compatible connection; the soldering is
not needed for parallelism** (it only selects WHICH metric connection, P2). The proof, all
steps machine-checked exact (residual 0.0):

1. **Closed-form Pi (A1).** Gamma Gamma^dag = sum_a e_a e_a^dag = 14 I exactly (spacelike
   e_a Hermitian with square +1, timelike anti-Hermitian with square -1: both give
   e_a e_a^dag = I). So Pi = I - Gamma^dag Gamma / 14: the Gram inverse is scalar.
2. **Full equivariance (A2).** With the eta-corrected vector generators M_ij (entries
   M[i,j] = eta_j, M[j,i] = -eta_i; eta M antisymmetric, so genuinely so(9,5)) and the spin
   generators Sigma_ij = (1/4)[e_i, e_j], BOTH intertwining relations hold for ALL 91
   generators, boosts included: Gamma rho(J) = Sigma_J Gamma and rho(J) Gamma^dag =
   Gamma^dag Sigma_J. W125 checked 3 self-dual space-space generators, where the eta factors
   are invisible; the boosts (the II_s-shaped mixing directions) were the genuinely open
   case, and they close exactly.
3. **Corollary.** [rho(J), Pi] = -(1/14)(rho Gamma^dag Gamma - Gamma^dag Gamma rho) =
   -(1/14) Gamma^dag (Sigma_J - Sigma_J) Gamma = 0 for all 91. Direct full-matrix
   confirmation on 6 representatives including 2 boosts: exactly 0.0 (A3). In a local
   orthonormal frame Pi has constant entries and the connection acts by rho(omega) with
   omega valued in so(9,5); hence nabla Pi = [rho(omega), Pi] = 0. **Pi is covariantly
   constant; Pi nabla-slash Pi = nabla-slash restricted to ker Gamma; the projected operator
   acquires NO curvature terms from the projection itself.**
4. **Krein parallelism (A4).** K = eta_V (x) beta_S with beta_S = e_0 ... e_8 satisfies
   rho(J)^dag K + K rho(J) = 0 for all 91 generators, via the exact factor identities
   M^dag eta + eta M = 0 and Sigma^dag beta_S + beta_S Sigma = 0. So nabla K = 0: the Krein
   structure is covariantly constant and the covariant operator (connection terms included)
   is Krein-self-adjoint wherever the flat symbol was. SA-U1's tree identity [P,S] = 0
   survives covariantization; the renormalized question stays open exactly as before.
5. **Covariant constraint closure (A5).** Gamma rho(J) Pi = Sigma_J (Gamma Pi) = 0: the
   leakage of the covariant operator is identically zero. The g = 1 cure is not a flat
   accident; it transports.

Convention note (honesty): the repo's Gamma = hstack(e_a) and the eta-raised gamma-trace
sum_a eta^aa e_a psi_a define unitarily equivalent constraint complexes (conjugation by the
isometry eta_V (x) 1); all norms, leakage values, and symbol spectra are identical. The
eta-corrected M_ij used here is the unique vector action making the repo's Gamma strictly
equivariant, and it is so(9,5) (A2's membership check).

## 3. Persona 3 (higher-spin/causality specialist): SA-C4 on curved Y14

What SA-C4's curved clause needed: that the exact degree-1 symbol property protecting
causality at the flat level survives curvature. W125 argued this by citation (II_s enters
the section-pulled operator at zeroth order); this wave upgrades it to a machine-checked
structure theorem in three steps:

1. **Pointwise curved cone (C2).** At an actual curved-Y14 point (the Block B metric), in a
   gimmel-orthonormal frame, G^{-1}(xi, xi) equals the frame eta-form exactly (residual
   1.8e-15), off-cone covectors of both signs give sigma_min(R) in [0.20, 1.21], and an
   exact gimmel-null covector gives sigma_min = 8.9e-21. **The characteristic variety of the
   covariant operator at each point of Y14 is exactly the gimmel null cone.** The flat model
   is not an analogy; it is the tangent-space restriction.
2. **All covariantization corrections are subprincipal by algebra membership (C3a).** Every
   zeroth-order insert the covariantization can generate -- curvature contractions rho(R)
   from the Weitzenbock/commutator terms, II_s blocks from section pulling, differences of
   metric-compatible connection choices -- is rho(w) for some w in so(9,5). For a generic
   algebra element AND a pure boost/II-type block, machine-checked: commutes with Pi
   (4e-15), zero leakage (3e-14), Krein-compatible (0.0), and strictly subprincipal
   (homogenized symbol returns R(xi) to 1.6e-6 at L = 1e6). This is stronger than W125's
   Block C, which showed arbitrary zeroth-order inserts cannot enter the principal symbol:
   here the inserts ALSO provably stay on the bundle and preserve the Krein structure, so
   the curved operator's lower-order terms cannot break the constraint or the
   pseudo-unitarity either.
3. **The protection boundary, named exactly (C3b).** W125's positive control (the failure
   mode with a finite causal window) used the first-order insert kron(II_sym, c(xi)) with a
   SYMMETRIC vector factor. eta . II_sym is not antisymmetric: that insert is provably
   OUTSIDE so(9,5), and metric-compatible covariantization can never generate it. The exact
   reopening condition for SA-C4 is therefore: a NON-METRIC coupling (non-metricity, or a
   non-minimal vertex differentiating the RS field through a symmetric tensor) producing a
   first-order symmetric insert. The built candidate contains none: T3's vertex is
   zeroth-order in xi (F-coupled, no derivative on Psi) with image inside ker Gamma.

**SA-C4 status for the built candidate: TEST-BUILT-PASSES at principal + subprincipal symbol
order ON CURVED Y14** (pointwise cone + algebra-membership subprincipality + O(9,5) holonomy
witness), upgrading the flat-model-plus-citation status of W125. Honest boundary, unchanged:
this is symbol-level causality, not an all-orders well-posedness theorem (no energy
estimates, no globally hyperbolic foliation of Y14 exhibited); and the 4D section-REDUCED
Schur route (cure A, the unpinned E-block) is untouched, so the repo-level VZ verdict
(CONDITIONALLY_RESOLVED) is NOT upgraded.

## 4. Persona 4 (computational engineer): the test

`tests/W131_covariant_operator_y14.py`, 12/12, exit 0, ~2 min. Design points:

- **Exactness where it matters.** All Block A checks reduce to 14x14 and 128x128 factor
  identities computed blockwise (no p-hackable tolerance tuning): every residual is 0.0 to
  machine representation, not merely below tolerance.
- **Reuse.** The verified rep and anchors come from `gen_sector_bridge` (C2 = 155.3625, rank
  Pi = 1664 reproduced); the Gauss machinery reuses H21's construction (numeric at n = 4,
  where H21's exact-rational proof ran at n = 3); the flat-limit control (C1) reproduces the
  W125 anchor set inside this file, so the curved build degenerates to the 9/9 flat story by
  construction.
- **Positive controls.** C1 (flat anchors), B3's nonzero-II requirement (the geometry is not
  vacuously flat), and C3b (the dangerous insert is detectably outside the algebra -- the
  same discriminator that would fire if a symmetric first-order coupling ever appeared).
- **Numerics honesty.** Blocks B use finite differences (steps 1e-4/1e-5) and RK4; their
  residuals (1e-8 to 1e-10) are consistent with the discretization order, and no exact claim
  rides on them -- they are witnesses for cited theorems, with the exact content carried by
  Block A.

## 5. Persona 5 (honesty auditor, E1/Lakatos): ledger, verdict, and the pattern

### 5.1 Consumption ledger

Nothing new is silently consumed. P2 (the connection = gimmel Levi-Civita spin lift) is the
SAME datum as W125's SA-G1/wave34-item-2 postulate, restated not re-decided; carrier B and
the A/B bit are untouched (the equivariance results hold on the full 1792-dim space, so as
in W125 the transport closes on both carriers and decides nothing); no FIT row moves; the
spurion/Yukawa sectors are untouched. Preconditions INHERITED and named, not discharged:
X4 spin (W2-01: for non-spin X4 the bundle S does not exist without extra structure, and
Spin^h does not rescue the index -- the build is conditional on X4 spin exactly as the
generation count is); gimmel nondegeneracy holds on the Lorentzian locus pointwise (B1), its
global degeneration boundary (where the fiber metric or h degenerates) is not characterized.

### 5.2 What moved and what did not

| Item | Before (W125) | After (W131) |
|---|---|---|
| [nabla, Pi] on curved Y14 | open (the named crux) | **= 0, theorem, exact (all 91 generators)** |
| SA-C4 curved clause | argued via citation (flat model + zeroth-order rider) | **machine-checked at symbol level on curved Y14** |
| Acceptance leg (a) | PARTIAL (curved clause open) | PARTIAL, sharper: symbol-level curved clause CLOSED; all-orders analytic clause remains |
| SA-U1 tree leg | flat symbol only | **covariant: nabla K = 0, Krein survives connection terms** |
| Leg (d) loop items | blocked on "the covariant operator" | still blocked, now on the ANALYTIC layer only (propagator on non-compact Y14) |
| SA-G9 | unmet | unmet (even-sector; this odd-sector wave does not touch it) |
| Gated numbers | none | none (the construction adds structure, not scales; E1: this wave is a construction) |

### 5.3 The E1 flag: does the one-object pattern recur?

Plainly: **partially yes, and here is the exact shape.** W125 compressed everything onto
"the covariant operator on Y14". This wave splits that object into an algebraic half and an
analytic half, closes the algebraic half completely (the operator exists, with P3-P7
machine-checked), and leaves the analytic half as a genuinely new named object: **the
propagator/Fredholm theory of D on the non-compact, infinite-in-practice Y14 = Met(X4)**
(needed by leg (d)'s counterterm/loop-rule/IR items and by any source-action-derived
number). That is a reduction-with-a-remainder, not a pure hand-off: the remainder is
strictly smaller (the loop items were blocked on operator + arena; now only the arena), it
is a different KIND of object (analysis, not algebra -- no amount of further rep theory
closes it), and the reduction produced falsifiable structure on the way (any symmetric
first-order insert now provably reopens SA-C4; any non-(9,5) signature point of Met(X4)
would break B1). But the pattern watcher should log: this is the second consecutive wave
whose deliverable includes "the remaining object is X". If W-next reduces the propagator to
yet another object rather than building or obstructing it, the E1 rule says treat the chain
as degenerating and demote the build path in the rankings.

### 5.4 Verdict (the sentence)

**BUILT-WITH-PROPERTIES at the frame/symbol level: the covariant operator
D = Pi (gamma . nabla) Pi + m2 Pi on ker Gamma over Y14 exists, with [nabla, Pi] = 0 proved
exactly (the crux dissolves: Gamma is parallel for every metric-compatible connection),
covariant leakage 0, nabla K = 0, pointwise curved characteristic variety = the gimmel null
cone, and all covariantization-generated corrections subprincipal by so(9,5) membership --
closing SA-C4's curved clause at symbol level; NOT built are the analytic layer (the Y14
propagator, now the sole blocker of leg (d)) and SA-G9, and no gated number unlocks, so
under the E1 rule this is a construction whose one status movement is SA-C4-curved:
argued -> machine-checked.** No unbuildability obstruction was found; none was needed.

## Honest limits

- Frame/symbol level: "the operator exists with these properties" means the local
  differential-geometric object is exhibited and its algebraic properties are exact; no
  global analysis on Y14 (completeness, self-adjoint extensions, propagator, spectral
  theory) is claimed. Those form the named analytic residual.
- The geometry checks (B1-B3) are numeric witnesses at sample points for cited theorems
  (Gauss formula, metric-compatibility <=> orthonormal-frame skewness), not new theorems;
  the exact content of the wave is Block A.
- Conditional on X4 spin (W2-01) exactly as the generation-count machinery is; for non-spin
  X4 the bundle itself needs a structure GU has not supplied.
- The 4D section-reduced VZ story (cure A / Schur / E-block) and the repo VZ verdict are
  untouched. m2 remains the FIT sqrt(m2_eff) mu_DW; nothing here narrows any FIT.
- Time-box honesty: this was the pre-declared first swing. The analytic layer was not
  attempted, by design; a sharp partial beats a mush.

*Filed 2026-07-14. Wave W131 (H68), five personas inline in one session. Reproducible:
`python -u tests/W131_covariant_operator_y14.py` (12/12, exit 0). Exploration-grade; no
canon movement; the spec document receives an append-only status note for the SA-C4 row's
curved clause only.*
