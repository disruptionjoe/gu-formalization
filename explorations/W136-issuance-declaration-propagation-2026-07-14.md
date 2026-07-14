---
artifact_type: exploration
status: exploration (assume-and-propagate wave; 5-persona inline team; deterministic test)
created: 2026-07-14
wave: W136
hypothesis: "H41 lineage / the 2026-07-14 propose-then-kill wave -- ASSUME the issuance postulate, PROPAGATE it through the source-action requirements spec, record what clicks and what dies"
title: "W136 -- the ISSUANCE-DECLARATION propagation run. DECLARED POSTULATE (never asserted): the observed dark-energy density rho_Lambda,obs ~ (2.3 meV)^4 is a fixed issuance supplied through the source action from outside the geometry, entering via the source/boundary term (a boundary energy flux whose bulk signature is a Lambda-mimic), NOT via the falsified H36 route. VERDICT of the propagation: ONE new exact structural product plus one determined FIT pair plus two kills plus one honest nothing. (1) NEW EXACT NUMBER: the |H|^2 (Willmore) slice decomposition is computed for the first time, h = (h0, h1, h2, h3) = (-1, 4/3, -4/9, 0), so the wave35 family flat constant is a0(alpha,beta) = 2 alpha - beta and BULK-FLATNESS selects the UNIQUE ratio beta/alpha* = 2: under the issuance declaration plus the physical-constant reading plus the sub-mm floor, SA-G5 is pinned to 2 within |x-2| <~ 2e-60 -- the first propagation that DETERMINES a spec FIT row. At the point: the Einstein channel survives attractive (family a1 = 3), the flat tadpole vanishes (flat space becomes a genuine vacuum, discharging the W130 Lambda = -1 tadpole note), the MSS reduction is F(R) = 3R - R^2, and the tree scalaron STAYS tachyonic (family c_R = -4/3 < 0): the issuance selection does NOT cure the tachyon. (2) DETERMINED PAIR: B_i = 0 and f0 = 0 become the natural point (the constant is carried by the boundary supply); exact LCDM in the DE channel, strictly inside every W129 band bound -- the issuance reading converts W129's 'everything allowed is a mimic' from an embarrassment into the prediction. (3) KILLS: the naive do-not-subtract reading of the W126 constant a0 = +2 is DEAD in both measure-fork charts at any allowed mu_DW (Einstein-anchored chart: Lambda_ind/mu^2 = a0/(2 a1) = 3 exactly, Omega-independent, so matching observation forces mu = sqrt(Omega_L) H0 ~ 1.2e-33 eV, ~30 orders below the sub-mm floor, and at the floor the induced Lambda overshoots by ~8e60; mu^4-anchored chart: mu_emb = 1.93/2.94 meV, both below the floor, overshoot 1.9-35x). The two-scale escape (an embedding scale distinct from the operator scale) is named, not taken: it needs an O(1) geometric ratio mu_emb/mu_DW in [0.41, 0.57] (c = 2 chart) and a revision of the H24 one-scale structure. (4) SPURIONS: one dimensionful issuance datum provably cannot feed the dimensionless Yukawa-hierarchy data (SA-Y7b/SA-Y5 untouched); the single order-of-magnitude alignment is the Majorana channel (2.3 meV within ~1 order of the neutrino band; seesaw conversion v^2/rho^{1/4} = 1.3e16 GeV), OOM-tier, comparison-only. (5) CURE SECTOR: honest NO -- the leakage law is dimensionless and Hom-disjoint from the Lambda channel; no cure-sector scale relation unlocks."
grade: "exploration / conditional-theorem register throughout. The issuance is a DECLARED postulate in the spec's DECLARATION sense; nothing here asserts it; every 'X under the issuance' is a statement of the conditional theory, never of GU. COMPUTED (exact sympy): the NEW |H|^2 slice decomposition (replicating the W126 Route-1 machinery verbatim, regression-pinned to the W126 slice coefficients (2, 1/3, 8/9, -4) and the Part-0 curvature pin before extraction); the bulk-flatness point beta/alpha* = 2 and the family coefficients at it; the fork-A ratio identity a0/(2 a1) = 3 (Omega-independent). COMPUTED (floats vs cited anchors): the kill arithmetic (Planck anchor, H52-cited floor envelope recomputed), the pin width, the f0/W129 containment, the spurion OOM ledger. BINDING constraints honored: H36 (rho = c_L mu_DW^4) FALSIFIED and never re-adopted (mu_DW is nowhere re-identified with the DE scale); the B2 rate-identity is FALSE and no rate identity is used; tri-repo gating: 'issuance' is used here as a named local postulate label only -- the issuance CONCEPT is owned by the temporal-issuance repo and NO cross-repo identity claim is made (the R5 issuance-bridge kill stands). NO canon / RESEARCH-STATUS / claim-status / verdict / posture change; no FIT row moves in the spec (the determinations are conditional on the declaration); H41 stays unbuilt; H59 stays OPEN."
construction: "program-native throughout (GEOMETER-VS-PHYSICS-OBJECTS.md): the |H|^2 computation uses the pinned ii-s Convention-B literal-graph construction (the same code path as W126 Route 1); the boundary-term formulation (Persona 1) is a standard-field EFT wrapper explicitly labeled as such; forks carried, not resolved (keep-vs-subtract slice reference: the ENTIRE beta/alpha* = 2 selection lives on the KEEP branch; measure fork: the selection condition is measure-stable because both flat constants live on the dphi = 0 slice where the measures agree pointwise)."
depends_on:
  - explorations/source-action-requirements-spec-2026-07-13.md
  - explorations/W126-beyond4th-vacuum-lift-2026-07-13.md
  - explorations/W130-native-graviton-oneloop-block-2026-07-14.md
  - explorations/W129-oq2-m2-band-sweep-de-exclusion-2026-07-14.md
  - explorations/W125-source-action-first-build-2026-07-13.md
  - explorations/track2-conditional-numbers-2026-07-13.md
  - explorations/wave35/source-action-carve-2026-07-11.md
  - explorations/H64-mass-selection-first-swing-2026-07-11.md
  - canon/shiab-existence-cl95.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W136_issuance_declaration_propagation.py
---

# W136 -- the issuance-declaration propagation run (assume-and-propagate)

**Posture.** This wave GUESSES in a disciplined way, per the wave brief: it ASSUMES a named
postulate and PROPAGATES it through the source-action requirements spec, machine-checking
every step, and then hands the result to the kill list. The postulate is DECLARED in the
spec's DECLARATION sense and is never asserted. Everything below of the form "X" is to be
read "X under the issuance declaration"; any quotation without that clause is a
misquotation.

**THE ISSUANCE DECLARATION (stated, never asserted).** The observed dark-energy density,
rho_Lambda,obs ~ (2.3 meV)^4 (the Planck-anchored value the repo's DE machinery carries,
H50/track2; recomputed to 2.24 meV from the primary anchors, within 3%), is a fixed
issuance supplied through the source action from OUTSIDE the geometry: the source action's
coupling supplies a boundary energy flux whose bulk signature is a Lambda-mimic. It does
NOT enter via the falsified H36 route rho = c_L mu_DW^4 (BINDING: H36 is dead, killed by
sub-mm gravity, H50/H51/H52; the floor envelope mu_DW in [3.4, 4.7] meV is honored
throughout and recomputed in the test).

**Terminology gate (tri-repo).** "Issuance" is used here as the LABEL of this local
postulate only. The issuance concept as such is owned by the temporal-issuance repo; the
one previously built bridge attempt in this repo (R5, the chiral-block-tie selector) was
KILLED, and no cross-repo identity claim is made or implied here. The B2 rate identity is
FALSE (binding); no rate statement is used anywhere below.

Five personas inline, one context, no sub-agents. Deterministic test:
`tests/W136_issuance_declaration_propagation.py` (31 checks, exit 0; the symbolic part
replicates the W126 Route-1 machinery verbatim and regression-pins it to the W126 slice
coefficients before extracting anything new).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Why / status |
|---|---|---|
| II / H of the section | ii-s Convention-B literal graph, vertical representative + normal lift (the W126 Route-1 code path, replicated verbatim) | The repo's pinned construction; the |H|^2 slice decomposition is NEW but computed inside the pinned convention, controls first. |
| Keep-vs-subtract slice reference | KEEP branch | The beta/alpha* = 2 selection EXISTS ONLY on the keep branch: on the subtract branch the flat constant is identically zero for every (alpha, beta) and the issuance is a pure boundary datum with no SA-G5 leverage. FORK-DEPENDENT, flagged, not resolved. |
| Measure | slice-stable | Both flat constants (a0 = 2, h0 = -1) live on the dphi = 0 slice where the two measures agree pointwise (W126), so the selection CONDITION is measure-fork-stable; quadratic-operator magnitudes differ by sector exactly as W130 quantified. |
| Boundary-term wrapper | standard-field EFT (labeled) | Persona 1's covariant bookkeeping is the standard boundary-source formulation; the GU-native home of the flux (which boundary of Y14 or of X4, and which source-action term carries it) is DECLARED, not derived. |
| The two-scale escape (fork B) | named, not taken | A second dimensionful scale mu_emb distinct from mu_DW contradicts the H24 ratio-only one-scale structure unless a new mechanism supplies the O(1) ratio; carried as a named target with its band computed. |

## 1. Persona 1 -- EFT theorist: the boundary-flux formulation and its bookkeeping

**The wrapper.** Declare a source term whose variation contributes a pure-trace,
covariantly constant stress piece: S_iss supplies T^iss_{mu nu} = -rho_iss g_{mu nu} in
the bulk equations, rho_iss fixed by the declaration to rho_Lambda,obs. Bianchi/conservation
bookkeeping is then automatic EXACTLY when rho_iss is constant: nabla^mu G_{mu nu} = 0
forces nabla_nu rho_iss = 0 for a pure-trace source. So the conservation-clean case is
w = -1 exactly, and any TIME VARIATION of the issuance re-enters as a dynamical DE
component -- which is exactly the object W129 bounds. The W129 band-wide mimic bound
|w0 + 1| < 0.1 therefore caps the issuance variation at |d ln rho_iss / d ln a| < 0.3
today (test D3). A boundary flux that is not constant is not killed; it is bounded, by
data already in the repo.

**Where it must NOT enter.** The declaration explicitly does not route through
rho = c_L mu_DW^4: the bulk DeWitt constant is a property of the geometry, the issuance is
a property of the source. That distinction is what the whole propagation below turns on:
if the geometry's own constant is kept physical it must be confronted separately (Persona
2), and the honest finding is that the issuance reading FORCES a position on it.

## 2. Persona 2 -- differential geometer: thread B1, the W126 constant, worked exactly

**The question as posed.** W126 computed the |II|^2 flat constant EXACTLY: a0 = +2,
sitting next to the Einstein coefficient a1 = +1/3, currently subtracted as background
convention. The issuance reading proposes: do NOT subtract it -- it is the physical Lambda
supplied at the boundary. What scale does that imply?

**Fork A (Einstein-anchored chart, the W126/W130 exact chain).** Both the constant and
the Einstein term ride the SAME overall normalization Omega, which therefore CANCELS out
of the physical cosmological constant:

```
Lambda_ind / mu^2 = a0 / (2 a1) = 3     (EXACT, Omega-independent; test C1)
```

Matching the observed Lambda then forces mu = sqrt(Lambda_obs/3) = sqrt(Omega_L) H0
~ 1.2e-33 eV: the HUBBLE scale, not the meV scale (test C2; the identity
mu = sqrt(Omega_L) H0 is exact given rho_crit = 3 H0^2 M_Pl^2). That mu sits ~30 orders
below the sub-mm floor; conversely, at the floor mu = 3.4 meV the induced Lambda
OVERSHOOTS the observed one by 8.4e60 (test C3). **The do-not-subtract reading is DEAD in
this chart** -- it reproduces the cosmological-constant problem with an exact repo
coefficient (3), which is itself a clean statement the repo did not previously carry.

**Fork B (mu^4-anchored chart, M_Pl external; the H50 chain, c_L = 3/8, and this chain's
flat 2 -- the 16/3 flag pair).** Here rho_ind = c mu^4 and the reading demands
mu_emb = (rho_obs/c)^{1/4} = 1.93 meV (c = 2) or 2.94 meV (c = 3/8; this is EXACTLY the
falsified H36 point, reproduced as a control, test C4). Both sit BELOW the floor: the
one-scale reading overshoots by a factor 1.9 (softest corner) to 35 (largest corner)
(test C5). **DEAD as a one-scale statement.**

**The surviving branch of the question "is rho_obs a statement about the section's
embedding scale?"** Only as a TWO-SCALE reading: an embedding scale mu_emb for the section
distinct from the operator scale mu_DW that the sub-mm channel binds (the floor binds
m2 = sqrt(m2_eff) mu_DW; it does not directly touch mu_emb). The required ratio is O(1),
not hierarchical: mu_emb/mu_DW in [0.41, 0.57] (c = 2 chart) or [0.63, 0.85] (c = 3/8
chart) (test C6). This is a NAMED computable target: the repo's H24 structure says the
gimmel geometry fixes ratios only, with ONE free scale, so the two-scale reading requires
either a computed geometric ratio landing in that band or a new declaration row (an
honest, counted cost). It is H36-adjacent but NOT H36: mu_DW is nowhere re-identified with
the DE scale.

**The propagation's own resolution: bulk-flatness.** The issuance reading does not need
the do-not-subtract branch; it prefers its negation with a mechanism. If the observed
Lambda is boundary-supplied, the BULK constant must not add a second, larger Lambda -- and
the wave35 shape family alpha |II|^2 + beta |H|^2 has exactly one ratio at which the bulk
constant vanishes IDENTICALLY. Computing the missing number (NEW, test B3): the |H|^2
slice decomposition in the pinned convention is

```
|H|^2  =  h0 + h1 R + h2 R^2 + h3 Ric^2   with   (h0, h1, h2, h3) = (-1, 4/3, -4/9, 0)
```

(controls first: the machinery reproduces the W126 |II|^2 row (2, 1/3, 8/9, -4) and the
Part-0 curvature pin exactly before this is extracted). Consistency notes: the Einstein
channels satisfy a1 = h1 - 1 exactly, the Gauss-relation sign in the R channel; the
constant channel does NOT satisfy the naive trace identity (2 != -1), a computed property
of the literal-graph algebraic-slice term, consistent with the construction not being a
literal isometric immersion; h0 = -1 < 0 is the DeWitt-negative pure-trace fiber
direction. The family flat constant is therefore

```
a0(alpha, beta) = 2 alpha - beta   ==>   bulk-flatness at the UNIQUE ratio  beta/alpha* = 2
```

(test B5). At that point, all exact (tests B7-B10):

- the Einstein channel SURVIVES and stays attractive: family a1 = 1/3 + 2(4/3) = 3;
- the flat tadpole VANISHES: flat space becomes a genuine stationary point of the induced
  functional (the W130 note "flat space is not a stationary point, Lambda = -1" is
  discharged at this ratio);
- the MSS reduction is F(R) = 3R - R^2 (zero constant term);
- the scalar channel is c_R = (a2 + 2 h2) + (a3 + 2 h3)/3 = -4/3 < 0: the tree scalaron
  STAYS TACHYONIC at the issuance-selected point (f_0^2 = 1/(6 c_R) = -1/8). The
  selection does not cure the tachyon; recorded at full strength.

**The pin width (the sharpest form of the click).** Combining the declaration, the
physical-constant reading, and the sub-mm floor pins the SA-G5 ratio to 2 within
|x - 2| <~ 2.1e-60 in the fork-A chart (test C7): the observed Lambda is a 1e-60
perturbation of the bulk-flat point. Under the issuance declaration, SA-G5 -- a FIT row
the spec bounds only to a band -- becomes DETERMINED.

**What is NOT computed here (named).** The Weyl channel of |H|^2 (the family c_W at
beta/alpha = 2) needs the W130 plane-wave evaluator run on |H|^2 in the TT sector; until
then the sub-mm phenomenology numbers (m2_eff, the floor itself) are quoted at the repo's
existing construction and FLAGGED for recomputation at the selected ratio. This is the
settling computation this thread hands to a successor wave.

## 3. Persona 3 -- rep theorist: SHIAB-05 and the spurion rows

Do the Majorana channel (SA-Y8) and the Yukawa hierarchy (SA-Y5/SA-Y7b) admit ONE
issuance normalization that also feeds the Lambda-mimic?

**The dimensional no-go (exact bookkeeping, test E3).** The issuance is ONE dimensionful
datum ([rho] = mass^4). The Yukawa-hierarchy rows need DIMENSIONLESS data: the spurion's
relative split, sign, and mixing angle (SA-Y7b), and the FN small parameter eps (SA-Y5).
A single dimensionful number supplies zero dimensionless numbers without a second scale.
**The issuance cannot feed the charged-fermion hierarchy; those rows are UNTOUCHED.** This
is a clean negative: the "same external supply channel" reading fails for the hierarchy on
dimensional grounds alone, before any dynamics.

**The Majorana channel (SA-Y8) is the one dimensionally reachable spurion, and it carries
the wave's one suggestive alignment (OOM tier, comparison-only, tests E1-E2):**

- rho_obs^{1/4} = 2.3 meV sits within ~one order of the neutrino mass band
  (sqrt(dm2_sol) = 8.6 meV, x3.7; sqrt(dm2_atm) = 50 meV, x22) -- the ONLY Standard-Model
  mass scale within reach of the issuance datum;
- the seesaw conversion v^2 / rho_obs^{1/4} = 1.32e16 GeV lands within a factor ~2 of the
  canonical 2e16 GeV heavy-Majorana scale.

Stated honestly: this is the well-known dark-energy/neutrino-mass numerical coincidence,
recorded as an order-of-magnitude ledger entry, NOT a derivation, NOT a relation the test
could falsify at O(1) precision, and NOT a GU-specific signature. The verdict on the
brief's question is: no INCOMPATIBILITY (no kill), no consistent SINGLE normalization
either -- the two spurion demands (dimensionless hierarchy data, dimensionful Majorana
scale) are of different kinds, and only the second is even in the issuance's reach.

## 4. Persona 4 -- the C2/cure sector: is the issuance the missing scale input?

W125 proved the causal cure pins only dimensionless numbers (g = 1, t* = -1/6, both exact)
and unlocked zero gated numbers, with the missing ingredient identified as a dimensionful
datum. The issuance ADDS a dimensionful boundary datum. Does that unlock a first
source-action-derived relation in the cure sector?

**Honest answer: NO (tests F1-F3).** Two independent reasons, both machine-checked at
their arithmetic level:

1. The leakage law leakage(g) = (1 - g) C2 contains no dimensionful scale; it is invariant
   under any rescaling of the issuance datum. The cure point cannot feel rho_iss.
2. Sector disjointness (the spec's Check 1): the cure acts on the RS carrier
   (1792 = 14 x 128, ker Gamma = 1664), the Lambda/boundary channel lives in the gravity
   sector; the Hom spaces are disjoint, so the issuance datum has no cure-sector operator
   to renormalize.

The dimensionful datum the issuance supplies lands in the Lambda channel (Section 2), and
THERE it does unlock a relation (the beta/alpha* = 2 selection) -- so W125's "the missing
scale input" diagnosis is answered in the gravity sector, not the cure sector. The only
bridge into the RS sector would be mu_DW itself, and identifying the issuance scale with
mu_DW is the falsified H36 (refused, binding).

## 5. Persona 5 -- adversarial skeptic: the kill list, and the steelman

**The steelman NOTHING-CLICKS was run first**, and it loses on one count and wins on
three:

- It LOSES on SA-G5/G3/G4: the bulk-flatness selection is a genuine new determination
  (a unique ratio, from a newly computed exact number, with a 1e-60 pin width), and
  f0 = 0 is a genuine natural point the declaration supplies where the built structure
  had only a fit. Neither was available before the declaration; W129 alone bounds f0, it
  does not prefer zero.
- It WINS on the cure sector (nothing clicks, F1-F3), on the Yukawa hierarchy (dimensional
  no-go, E3), and on the VALUE of Lambda: the issuance postulate does NOT make rho_obs
  predictable -- the boundary datum is free, so the declaration buys structure (which
  ratio, which amplitudes vanish), never the number (2.3 meV stays an input). Anyone
  quoting this wave as "GU explains dark energy" is misquoting it twice over.

**The kill list (every clicked relation, with its falsifier and its standing-data
check):**

| # | Relation (under the declaration) | Falsifier | Standing-data check |
|---|---|---|---|
| K1 | Do-not-subtract, fork A (Einstein-anchored): Lambda_ind = 3 mu^2 | already falsified | DEAD NOW: needs mu = 0.83 H0, ~30 orders below the sub-mm floor [3.4, 4.7] meV; overshoot at floor 8.4e60 (tests C1-C3) |
| K2 | Do-not-subtract, fork B (mu^4-anchored, one scale) | already falsified | DEAD NOW: mu_emb = 1.93/2.94 meV both below the floor; overshoot 1.9-35x (tests C4-C5) |
| K3 | Two-scale escape (mu_emb != mu_DW) | a computed geometric ratio outside [0.41, 0.57] (c = 2) / [0.63, 0.85] (c = 3/8); or no mechanism exhibited (H24 one-scale then rules, ratio = 1, already outside both bands) | OPEN, named target; carries the cost of a new declaration row (test C6) |
| K4 | beta/alpha* = 2 (the bulk-flatness selection) | (a) the wave35 m2_eff-to-band map, once derived, excluding 2; (b) the family c_W at the point flipping the TT/Stelle structure or breaking the sub-mm floor consistency (settling computation named in Sec 2); (c) the subtract branch of the slice-reference fork being the correct convention (then no selection exists); (d) falsification of the declaration itself | not currently falsified; the point avoids the two named wave35 exclusions (conformal edge -1/4, pure-|H|^2 corner) (tests B5-B6); rotation-curve kill does not apply (alpha != 0) |
| K5 | B_i = 0, f0 = 0: EXACT LCDM in the DE channel | any confirmed non-mimic DE signal, |w0 + 1| > 0.1 at signal level (e.g. DESI CPL confirmed jointly by BAO + SNe + CMB) | CONSISTENT NOW: W129 band-wide, everything allowed is a mimic and f0 = 0 is inside every bound (0.027/0.039/0.208); the DESI CPL preference is exactly what the theta sector cannot carry, and under the declaration GU no longer needs it to (test D1) |
| K6 | Issuance constancy (conservation) | measured |d ln rho_DE / d ln a| > 0.3 today | CONSISTENT: bounded by the same W129 mimic band (test D3) |
| K7 | PPN / LIGO | tensor dispersion, extra polarizations, non-luminal speed | UNCHANGED: the declaration keeps mu_DW free above the floor; exact GR at LIGO stands exactly as in track2 row 7; nothing in the propagation touches the massless TT pole |
| K8 | Majorana OOM alignment | neutrino spectrum pinned quasi-degenerate at >~ 100 meV (stretch factor > 40); or SA-Y8 landing at an unrelated scale | OOM-tier only; current band factors 3.7-22 (test E1) |

## 6. The propagation table (the brief's return format)

Spec row by spec row; verdicts are all conditional on the declaration.

| Spec row | Relation under the issuance declaration | Verdict | Machine check |
|---|---|---|---|
| SA-G3 (B_i) | the theta amplitude has no job; B_i = 0 is the natural point | DETERMINED (conditional) | D1, D2 (exit 0) |
| SA-G4 (f0) | f0 = 0 exactly; exact LCDM; strictly inside every W129 bound | DETERMINED (conditional) | D1, D2 |
| SA-G5 (beta/alpha) | bulk-flatness selects beta/alpha* = 2, unique, pin width ~2e-60; KEEP-branch only | DETERMINED-CONDITIONAL | B3-B10, C7 |
| SA-G6 (alpha) | positivity unchanged; the overall normalization now anchors the Einstein term only (constant gone at the selected ratio) | RELATED | B7, B10 |
| SA-G2 (mu_DW) | NOT re-identified (H36 binding); fork-B escape names the ratio band [0.41, 0.57] | RELATED (escape branch only), otherwise UNTOUCHED | C4-C6 |
| SA-G7 (c_L) | the background-density job (c_L mu_DW^4 as a physical density) is MOOTED at the selected ratio (bulk constant = 0); the 3:2:1 normalization item (W130) untouched | RELATED / MOOTED | B10 |
| SA-G8 (m2_eff) | numerically untouched; FLAGGED for recomputation at beta/alpha = 2 (family c_W unbuilt) | UNTOUCHED-FLAGGED | -- (named remainder) |
| SA-G9 (matter coupling) | untouched | UNTOUCHED | -- |
| SA-Y3 (vev), SA-Y4 (couplings) | untouched | UNTOUCHED | E3 |
| SA-Y5 (hierarchy mechanism) | dimensional no-go: the issuance cannot supply eps | UNTOUCHED (no-go recorded) | E3 |
| SA-Y7b (spurion values) | dimensional no-go (dimensionless data) | UNTOUCHED | E3 |
| SA-Y8 (Majorana spurion, DECLARATION row) | the one dimensionally reachable channel; OOM alignment (x3.7-22 to the neutrino band; seesaw 1.3e16 GeV) | RELATED (OOM tier only) | E1, E2 |
| SA-C2 (cure) | leakage law dimensionless; Hom-disjoint; NO unlock | UNTOUCHED (honest NO) | F1-F3 |
| SA-U1..U5, SA-C1/C3/C4, SA-G1 | untouched | UNTOUCHED | -- |

Tally: 3 DETERMINED (conditional), 4 RELATED, the rest UNTOUCHED, 2 of the untouched
carrying recorded no-gos. Before this wave the declaration's expected yield (per the
skeptic's prior) was zero determinations beyond what W129 allows; the computed yield is
the SA-G5 selection plus the (B_i, f0) pair, at the price of one new named target (K3)
and one fork dependence (keep-branch).

## 7. What would settle the remainder

1. **The family Weyl channel** c_W(beta/alpha = 2): run the W130 plane-wave evaluator on
   |H|^2 in the TT sector. Settles K4(b), updates the native tree point
   (f_2^2, f_0^2) = (-1/4, -3/8) to the selected ratio (the f_0^2 leg is already computed
   here: -1/8, still negative), and feeds the m2_eff recomputation the floor numbers need.
2. **The wave35 band map**: derive the m2_eff-to-beta/alpha band and check whether 2 is
   inside. Settles K4(a).
3. **The keep-vs-subtract fork**: any argument pinning the slice-reference convention
   decides whether the selection exists at all (K4(c)).
4. **The two-scale target** (K3): either exhibit a geometric mechanism giving
   mu_emb/mu_DW in the computed band, or let the H24 one-scale structure kill fork B's
   escape permanently.

## Honest limits

- Everything is conditional on a DECLARED postulate; no verdict, canon item, count, or
  posture moves. The spec's FIT rows do not move: "DETERMINED (conditional)" is a property
  of the conditional theory, recorded here, not a spec-status change.
- The issuance VALUE (2.3 meV) is an input everywhere; the declaration never predicts it.
- The beta/alpha* = 2 selection stands on the keep branch of the slice-reference fork and
  on the no-fine-tuning reading (no boundary-vs-bulk cancellation); both named.
- The |H|^2 decomposition is one route (the W126 Route-1 machinery); W126's Route-2
  full-ambient cross-check was not replicated for |H|^2 (the |II|^2 regression controls
  are the pin). A Route-2 |H|^2 cross-check is cheap insurance for a successor wave.
- The spurion alignment is OOM-tier and literature-known; it is a ledger entry, not
  evidence.
- The sub-mm floor, W129 bounds, Planck anchors are cited/recomputed, not re-derived.

*Filed 2026-07-14. Five personas run inline in one session (EFT theorist, differential
geometer, rep theorist, numerical engineer, adversarial skeptic). Reproducible:
`python -u tests/W136_issuance_declaration_propagation.py` (31/31, exit 0). Exploration
grade; no canon movement; H41 stays unbuilt; H59 stays OPEN.*
