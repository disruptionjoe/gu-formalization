---
title: "Channel swing CH-REC: the co-flip identity formalized, probed, and priced"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (deep research swing, CH-REC)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends: explorations/five-leg-swing-2026-07-19.md
inputs:
  - explorations/assembly-archaeology-recovered-parameters-2026-07-19.md
  - explorations/adapter-assumed-four-leg-swing-2026-07-19.md
  - lab/process/source-object-interface-contract.md
  - lab/process/integration-readiness-scorecard.md
  - lab/process/recovery-no-go-defense-register.json (RECOVERY-NOGO-GR-W229-VACUUM)
  - explorations/time-as-finality-crosswalk/adapter2-correction-polarity-fiber-not-axis-2026-07-15.md
  - explorations/time-as-finality-crosswalk/ti-question-finality-orientation-as-krein-sign-2026-07-15.md
  - explorations/time-as-finality-crosswalk/adapter-contract-three-object-signed-graph-2026-07-15.md
  - tests/W235_central_bit_mirror_record_vs_redundancy.py
cross_repo_reads_cited_as_evidence:
  - "possibility-to-capability: explorations/2026-07-19-topological-order-witness/SYNTHESIS.md + tests/topological_order_witness.py (Z2 carrier mechanics; read-only)"
  - "time-as-finality: exports/packets/TAF-001-paired-record-intervention-v0.1/ISSUANCE.md (record-token semantics exist at formal-only grade; read-only)"
  - "temporal-issuance: explorations/E179/E180 2026-07-15 + memory/steward-memory-summary.md (Krein sign trends forced-internal; temporal order/finality are observer-side reconstructions from records; read-only)"
runnable:
  - tests/channel-swings/ch_rec_coflip_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# CH-REC channel swing: the co-flip identity

Deep swing on the fifth leg under the standing axiom. Five deliverables:
(1) H-REC formalized as a precise mathematical claim; (2) the co-flip kill
test built and run; (3) the "one absence seen twice" vacuum reading made
precise; (4) the causality-thermodynamics link typed as hypothesis; (5) the
CH-REC parameter card draft and scorecard row.

Headline: the co-flip kill did NOT fire. The probe's exact result is
sharper than survive/die: **decoupling the arrow from the Krein sign costs
exactly one additional Z/2 import.** Zero-import decoupling does not exist
in the finite involution inventory. H-REC survives conditionally, and the
condition is now a single named typing question (T3 below) about GU's
actual W229 record law. N <= 4 stands at this grade.

## 1. H-REC formalized: the co-flip identity

### 1.1 What H-REC must NOT claim (ADAPTER2-01 discipline)

The 2026-07-15 ratification of `bar(b) = finality-axis polarity` was
withdrawn (`adapter2-correction-polarity-fiber-not-axis-2026-07-15.md`):
the correct current picture is a **polarity fiber Z/2 over the finality
profile**, not polarity-as-direction-of-the-finality-axis, and the
signed-graph result is a common Harary-balance predicate, not a native
isomorphism. The two global anchors of a balanced signed graph are related
by a relabeling symmetry with no canonical positive choice.

H-REC is therefore stated as a **GU-internal covariation claim**, not a
cross-repo identity: it does not assert that eps IS TaF's finality
direction. It asserts that, inside GU's own construction, the sector
selection and the record-accumulation direction are functions of ONE bit
and cannot be varied independently. If proven, it contributes a candidate
invariant to reopen-burden item 6 of the crosswalk (something that changes
if the identification is wrong); it does not discharge the
branch-preserving functor items 1-5.

### 1.2 The construction class C_0 (zero-extra-import record constructions)

Minimal structure in which the claim is testable:

- a finite Krein space `(K, <.,.>)` of signature (n,n) with fundamental
  symmetry `J` (`J^2 = I`, `<J.,.>` positive definite);
- the transmitted orientation `eps in {+1,-1}` (payload item 1), physical
  projector `P_eps = (I + eps J)/2`; physical inner product
  `eps<.,.>` restricted to `ran P_eps` (positive for BOTH eps values in
  isolation — the two-anchor freedom is real and retained, per
  ADAPTER2-01);
- grading-preserving Krein-unitary dynamics `U` (`U*GU = G`, `[U,J] = 0`),
  with a zero-import dynamics-direction datum `tdir in {+1,-1}`;
- a record register with increment given by the record current
  `J_rec[Psi] = eps * q(Psi)`, where `q(Psi) = eps<P_eps Psi, P_eps Psi>
  >= 0` is the physical sector charge. **Class-defining constraint: the
  record law contains no sign datum not derived from the structure.** A
  record law `N += mu * eps * q` with free `mu` is admissible arithmetic
  but `mu != +1` is counted as one underived Z/2 import.

The `J_rec = eps * q(Psi)` shape is the W229 lineage: the record-current
source law with current sourced by physical content, and the vacuum rule
`Psi = 0 -> J = 0 -> theta = 0` (defense register,
RECOVERY-NOGO-GR-W229-VACUUM, minimized obstruction). The register-side
support that GU's built content already types the relevant Z/2 as a
*record* is W235: at the kinematic/free-BV level the mirror-sector Z2
grading is BRST-closed-not-exact — a conserved record, forced by three
Y14-independent legs.

### 1.3 The claim

**CO-FLIP (H-REC, finite form).** In every admissible configuration of
C_0, and for every zero-import operation `g` on configurations: `g` flips
the record-accumulation direction `dir = sgn(Delta N)` if and only if `g`
flips the physical-sector selection (the G-sign of `ran P_eps`). Flipping
`eps` flips both, always and together; no zero-import operation flips
exactly one.

**Kill condition.** H-REC dies if some zero-import configuration operation
splits the pair `(sector, dir)` — flips one and not the other. Then the
arrow needs its own payload bit and N -> 5.

Note what makes this non-tautological: within C_0 the direction is
*defined* through eps, so the content is entirely in the adversarial
inventory — whether the structure contains any OTHER zero-cost sign
resource (basis relabeling, form-sign convention, dynamics reversal,
anchor exchange) that can reach the pair asymmetrically. The withdrawn
ratification failed on exactly this kind of hidden resource (a fork
collapse the certificate did not see), so the inventory is the honest
battleground.

## 2. The co-flip probe: design and results

`tests/channel-swings/ch_rec_coflip_probe.py` — standalone, stdlib-only,
exact rational arithmetic, p2c-fixture style ([T]/[E]/[F] tags, failing
controls protect each evidential check). The CH-QM graded-quotient toy
does not exist yet (`tests/channel-swings/` was empty); the probe
exposes a composition interface (`record_register`, `q_of`,
`sector_sign`) so the CH-QM toy can drive the same register with its
graded-quotient charges when built.

Structure: signature (2,2) Krein space, `J = diag(1,1,-1,-1)`, two
distinct rational block-rotation Krein-unitaries, three generic states
plus the vacuum, five steps, both eps values, both dynamics directions.

Involution inventory (all 16 composites tested over all configurations):

| generator | import cost | action on (sector, dir) |
|---|---|---|
| E: eps-flip | 0 (payload value) | flips BOTH (co-flip) |
| Rl: full covariant relabel (block swap, transports G, J, U, Psi) | 0 (gauge) | identity |
| T: dynamics reversal U -> U^-1 | 0 | identity |
| M: record-law sign insert mu -> -mu | **1** | flips dir ONLY (split) |
| partial relabel (J -> -J, G fixed) | — | **rejected**: G.J loses positive definiteness (not a fundamental symmetry) |

Results (run 2026-07-19, exit 0, headline `7 [E] + 3 [F] = 10`, setup
`[T] = 2` excluded):

1. **Co-flip holds**: eps-flip flips sector G-sign and record direction
   together in every tested configuration.
2. **Zero-import diagonal**: all 8 zero-import composites of {E, Rl, T}
   act diagonally on the pair; no zero-cost decoupling exists. The kill
   did not fire.
3. **Split-costs-one**: every splitting composite contains M and carries
   import cost exactly 1. Decoupling is *possible* — at the price of one
   additional Z/2. This converts the H-REC kill from a binary into an
   accounting identity: **arrow-sector decoupling <=> a second payload
   bit.** The N -> 5 boundary is now exact rather than rhetorical.
4. **Time-reversal-inert** (the most instructive single check): reversing
   the dynamics alone changes neither sector nor direction, because the
   register increment `eps*q` is nonnegative-definite in magnitude and
   orientation-sourced in sign — the arrow lives in the record law plus
   eps, not in the propagator. Consequently any zero-import operation
   that reverses the arrow must flip eps, and flipping eps drags the
   sector. This is the finite shadow of "the orientation must be engaged
   T-oddly": a construction in which eps were a mere T-even label would
   need the arrow stored somewhere else, and the only available slot is a
   paid mu.
5. Controls: the mu-decoupling is flagged by the import counter; the
   partial-relabel attack is rejected by the fundamental-symmetry gate; a
   direction-erased register (|J_rec|) demonstrably carries no
   orientation information, so the direction really is eps-sourced.

### 2.1 Honest scope of the survival

- The probe proves the co-flip on the FINITE inventory of a specific
  minimal structure. It does not prove the inventory exhaustive for the
  full construction (the cohomological/BV level has more involutions —
  named gap G2 below).
- The scientific weight now rests on one question, **typing constraint
  T3**: is GU's actual W229 record law a member of C_0 — i.e., is the
  SIGN of `J[Psi]` derived (Noether-style, like `delta_2 . d_RS,-1 = 0`)
  from the same action structure that carries the Krein orientation, or
  does the built source law smuggle an independent direction choice
  (a mu)? If the sign is derived: H-REC holds at construction grade and
  the arrow rides free. If W229's direction requires its own posit: that
  posit IS the second Z/2 and N = 5 by the probe's accounting identity.
  Nothing in the defense register answers this today — W229 fixes
  `kappa` and `Z_U` as normalization data but the direction question was
  never isolated.
- This swing does NOT re-tread the killed record-issuance selector
  (archaeology item 10): H-REC identifies the arrow with the transmitted
  ORIENTATION, not with a shiab selector; the old kill (lands on the
  index, not the selector) is out of scope and stays killed.

## 3. One absence seen twice: the vacuum-thermodynamics reading

### 3.1 The precise statement

Define the **orientation witness** of a state: `W(Psi) = 0` iff every
operational (state-functional) observable — record trajectory, physical
expectations — is identical for eps and -eps at Psi; `W(Psi) != 0`
otherwise. In C_0: `W(Psi) = 0 <=> q(Psi) = 0` for both anchors, and in
particular `W(0) = 0` (probe check `vacuum-unwitnessed`).

Then the two sector failures are one statement:

- **GR presentation**: `Psi = 0 -> J[Psi] = 0 -> theta = 0` — no
  cancellation tensor for `Q^TF(B)`; "no records in vacuum" (the W229
  no-go's minimized obstruction, verbatim from the defense register).
- **QM presentation**: with `W = 0` the two Krein anchors are
  operationally exactly degenerate — the structural two-anchor freedom
  (both anchors carry positive physical norm; ADAPTER2-01's relabeling
  symmetry) is unbroken by any measurement; "no selected physical
  sector."

Both say: **the vacuum state carries zero orientation witness.** The
orientation exists (structurally, as the transmitted bit) but has no
dynamical trace there. One absence; two sector-specific costumes. The
probe formalizes this exactly: at `Psi = 0` the operational observable
tuples for the two orientations are equal and identically zero, while at
any state with physical content the record direction equals eps
(`witness-restored`).

### 3.2 Under C10 (curvature-conditioned VEV)

If H-GR' holds — `theta_vac` responds to background curvature through a
frozen kernel, `Psi_vac = Psi_vac[curvature] != 0` where curvature is
nonzero — then `q(Psi_vac) > 0` exactly where curvature is nonzero, and
both absences lift TOGETHER: the cancellation tensor becomes available
(GR side) at the same points where the anchor degeneracy is broken (QM
side). Qualitative predictions, in order of decreasing confidence:

1. **Record production tracks curvature** (probe surrogate check: record
   accumulation zero at kappa = 0, strictly increasing in kappa).
   Flat-vacuum regions are record-free and orientation-unwitnessed;
   records concentrate where curvature concentrates.
2. **Entropy production is spatially inhomogeneous and
   curvature-weighted** — irreversibility is strongest near mass
   concentrations. SPECULATION FLAG: this is a shape statement from a
   surrogate parameter, not a derived entropy law; no coefficient, no
   functional form, no horizon claim.
3. **Resonance, not result**: the picture rhymes with horizon
   thermodynamics (entropy residing where curvature is extreme). GU does
   not derive area entropy here and this document makes no such claim;
   recorded only as a direction the C10 computation could be confronted
   with later.

Both prior failures being one absence also explains, cheaply, why the
recovery program kept finding the SAME hole from two sides — the tri-repo
Krein-sign reduction (one external Z/2) and the W229 vacuum no-go
(zero record current) were always the same missing witness.

## 4. The causality link (typed HYPOTHESIS, not result)

Archaeology recovered: clean decoupling of the ghost sector is
Velo-Zwanziger-acausal; the physical sector must be realized
cohomologically — **the ghost is causality-required** (spec B.4 +
GHOST-01; now on the interface contract addendum).

**H-REC-CAUS (hypothesis).** Causality protection and irreversibility
structure are the same structural exclusion: the absence of a zero-import
splitting operation. Reading: a cleanly decoupled physical subspace would
be eps-inert — a place where the sector datum has no dynamical grip, and
therefore a free arrow-flip resource (an unpaid mu) living inside the
construction. The cohomological realization removes exactly that
resource: when the sector exists only through the differential
(closed-not-exact — precisely W235's kinematic RECORD reading of the
mirror Z2), any operation reversing the record direction must act on the
differential and hence on the sector. Velo-Zwanziger acausality and
arrow-sector decoupling would then be the same disease in two sectors,
and the ghost's causal necessity would BE the co-flip's enforcement
mechanism.

Status: hypothesis with a named future test — extend the BV-bicomplex
fixtures (`rs_ghost_full_bv_bicomplex_koszul_tate.py` family) with the
probe's register interface and check whether cohomological realization
forbids constructing an internal mu while a cleanly-decoupled variant
permits one. Not tested by the finite probe; the finite probe's
`time-reversal-inert` check is the kinematic shadow of it, no more.

## 5. CH-REC parameter card (draft)

### Sector parameters (GU-internal, all derived — none free)

| item | definition | provenance |
|---|---|---|
| record current | `J_rec[Psi] = eps * q(Psi)`, `q >= 0` sector charge | W229 source law lineage; probe |
| record direction | `= eps` wherever `q > 0` | probe (`witness-restored`) |
| entropy-production direction | `= eps` (finite grade only; continuum form open) | probe + H-REC |
| orientation witness | `W(Psi)`; `W = 0 <=> q = 0`; vacuum rule `W(0) = 0` | probe (`vacuum-unwitnessed`); W229 no-go |
| vacuum witness under C10 | `q(Psi_vac[curvature])`, zero iff curvature-conditioning zero | surrogate check; awaits C10 formalization |

### Adapter parameters

**ZERO new payload items — target met.** The fifth leg transmits nothing
of its own. Instead payload item 1 (the global Z/2 orientation) carries a
third typing constraint, joining the two already on the interface
contract:

- **T1** (p2c, existing): topologically stored, loop-coherent, locally
  unreadable.
- **T2** (archaeology, existing): non-quaternionic, or accompanied by an
  a-priori rank pin (generations parity no-go).
- **T3** (NEW, this swing): **record-law-sign-deriving** — the source
  action must derive the record current's direction from the same
  structure that carries the orientation (Noether-forced, in the same
  sense as `delta_2 . d_RS,-1 = 0`), leaving no independent sign choice
  in the record law. T3 is a constraint on the action's shape, not a new
  transmitted item.

### What evidence would force a fifth payload item

1. A zero-import decoupling configuration at a higher grade — in the
   composed CH-QM + register toy, or at the BV/cohomological level (gap
   G2) — i.e., the co-flip kill firing where the finite probe could not
   see.
2. **T3 failing on W229**: demonstration that the built source law's
   direction cannot be Noether-derived from the eps-carrying action and
   requires its own posit. By the probe's accounting identity that posit
   is exactly one Z/2, and it is the fifth item.
3. A weld inconsistency: the joint J_quat probe (archaeology item 6)
   concluding the orientation must be quaternionic-compatible for CH-SM
   while CH-REC needs it engaged in the record law — the one-bit economy
   breaking across legs rather than within one.

## 6. Proposed scorecard row (CH-REC)

- **Q1: PARTIAL** (was OPEN). The co-flip identity is formalized and
  holds in a runnable finite probe (exit 0, `7 [E] + 3 [F] = 10`);
  existence is at finite-probe grade, conditional on C_0 membership (T3),
  not yet composed with the CH-QM toy (which does not exist yet) and not
  yet at cohomological grade.
- **Q2: YES** (was PARTIAL). The parameter boundary is now sharp and
  quantitative: within the zero-extra-import class the co-flip is forced;
  decoupling is possible if and only if exactly one additional Z/2 is
  paid. The requirement on the construction is the single typing
  constraint T3.
- **Q3: YES, conditional** (unchanged in content, sharpened in form).
  Zero new payload items; range binary; same bit as CH-QM; item-1 typing
  now T1 + T2 + T3. The condition is no longer "if H-REC holds"
  vaguely, but "if T3 holds on the built record law."
- **Gaps to card-freeze**:
  - **G1**: compose the register with the CH-QM graded-quotient toy when
    CH-QM builds it (interface already exposed).
  - **G2**: BV/cohomological-level co-flip — the H-REC-CAUS test (does
    cohomological realization forbid an internal mu?).
  - **G3**: T3 verification on W229 — isolate the direction datum in the
    built source law; this is the decisive one.
  - **G4**: the joint J_quat/T2-T3 compatibility probe (shared with
    CH-QM/CH-SM; archaeology item 6).

## 7. Inline persona passes (three, inline only)

**Statistical mechanic.** The register is a monotone counter, not a
thermodynamic entropy; calling `dir` the entropy-production direction is
licensed at this grade only because in C_0 there is literally no other
sign for a coarse-grained H-theorem to pick up. The real stat-mech
content will be whether the CONTINUUM record current defines a
fluctuation-theorem-grade asymmetry whose sign is eps — flag: do not
promote "entropy production = record production" beyond finite grade
until a coarse-graining exists. Accepted; typed into the card as
"continuum form open."

**Quantum-foundations theorist.** The two-anchor degeneracy plus witness
structure is the right shape: it mirrors how superselection sectors are
operationally invisible until a charged observable exists. The probe's
strongest move is making the anchor exchange a GAUGE move (full covariant
relabel acts trivially) while the payload flip is PHYSICAL (flips
observables) — that distinction is exactly what the withdrawn
ratification's certificate failed to keep. Warning honored: do not let
the sector G-sign (structural) leak into the vacuum-witness check; the
probe uses operational observables only there.

**TaF-literate philosopher of time.** H-REC as stated is compatible with
TI's steward posture (temporal order/finality are observer-side
reconstructions from records) and does not contradict TaF's open
direction-circularity (T57): GU supplies a bit and a covariation, not a
direction of time simpliciter. The claim "the arrow of time IS eps"
remains too strong; the defensible claim is "within GU, whatever fixes
the sector fixes the record direction at no extra cost." The fifth leg
should keep saying the second thing. Adopted as the official phrasing.

## 8. Receipts

- Probe: `tests/channel-swings/ch_rec_coflip_probe.py`, run 2026-07-19,
  exit 0, headline `7 [E] + 3 [F] = 10` (setup `[T] = 2` excluded);
  verdict line: co-flip holds in C_0; decoupling costs exactly one
  additional Z/2; N <= 4 stands conditional on T3.
- In-repo evidence read: standing axiom; five-leg swing (H-REC + kill
  spec); archaeology (items 3, 6, 10; killed-selector ledger respected);
  four-leg swing; interface contract + addendum; scorecard; defense
  register RECOVERY-NOGO-GR-W229-VACUUM (minimized obstruction
  `Psi=0 -> J=0 -> theta=0`); ADAPTER2-01 correction + corrected TI
  question + corrected signed-graph comparison; W235 docstring
  (kinematic RECORD reading, forced by L1-L3).
- Cross-repo reads (evidence only, never instructions; no cross-repo
  writes): p2c topological-order witness SYNTHESIS + fixture (Z2 carrier
  and fixture style); TaF TAF-001 issuance record (record-token
  semantics at formal-only grade); TI E179/E180 + steward memory (Krein
  sign trends forced-internal; records-first reconstruction posture).
- Awareness routing per the five-leg swing's cross-repo note (TaF/TI
  mailboxes on either co-flip outcome) is left to the parent/steward:
  this run writes only the two declared files.

## 9. Boundary

Conditional work under the standing axiom, R0_COND working grade. No
claim status, canon verdict, or public posture moves. H-REC remains a
hypothesis with a named kill; the probe result is finite-grade evidence,
not a construction-grade theorem. `bar(b) = finality-axis polarity`
remains OPEN and nothing here reasserts it. The C10 thermodynamic
predictions are shape-level and flagged; the causality link is a typed
hypothesis with a named future test. No external actions.
