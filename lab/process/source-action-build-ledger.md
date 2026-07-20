---
title: "Source-Action Build Ledger"
status: living_surface
doc_type: channel_build_ledger
created: 2026-07-19
updated: 2026-07-19
owner_channel: CH-SRC
contract: "research-portfolio.json channel_structure.ch_src_contract"
axiom: lab/process/boundary-adapter-standing-axiom.md
update_rule: "CH-SRC is the lagging integrator: each CH-SRC run re-reads every explorations/channel-swing-CH-*-<date>.md and the interface contract, moves PENDING rows to FROZEN/CONSUMED as sibling channels land, re-runs tests/channel-swings/ch_src_minimal_action_toy.py against the updated constraint set, and records any new conflict as a first-class computed result under the P0 pre-registered endings. This file is the only surface CH-SRC runs are expected to mutate."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Source-Action Build Ledger

The standing integration surface for the one missing object: the RS/IG
source action `S_IG` (spec sheet: B.1-B.6 in
`docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md`). Every demand a
channel freezes lands here as a build constraint; the minimal toy
(`tests/channel-swings/ch_src_minimal_action_toy.py`, exit 0, 2026-07-19) is
the current best skeleton and is graded against this table.

Build state, one line: **skeleton EXISTS at toy grade (B.1-B.4 exhibited);
no computed conflict between any two frozen constraints; the un-suppliable
remainder is exactly the B.5 global data, as the spec predicted.**

## 1. Constraint table

Statuses: FROZEN (value/type fixed by a channel swing, with receipt),
CONSUMED (integrated into the build and exercised by the toy), PENDING
(awaiting a sibling channel or an external instance). Toy column: how the
current skeleton stands against the row.

| ID | origin | constraint (type) | status | toy status (2026-07-19) |
|---|---|---|---|---|
| B.1 | spec 2026-06-27 | `(S,S) = 0`, classical master equation | FROZEN | EXHIBITED (two tiers; operator-exact + 20-config antibracket; controls hold) |
| B.2 | spec + CH-QM D-QM-2 | gauge invariance FORCES `delta_2 . d_RS,-1 = 0` via Noether; the differential is a consequence, never bare data | FROZEN | EXHIBITED (`B_W A_W = 0` == invariance of S; together-failure under perturbation; raw-generator control) |
| B.3 | spec + GHOST-01 + CH-QM D-QM-3 | non-equivariant compensator `sigma_c` outside the spin-symmetry family; equivariant payloads dead on arrival | FROZEN | PARTIAL-STRONG (present, adjoint defect 0.80; necessary at (S,S) level; equivariant-impossibility inherited from real-rep SHIAB-04/GHOST-01 — mini-rep is rigidity-inert, see Section 3) |
| B.4 | spec + VZ causality finding | physical sector cohomological (closed-not-exact, both BV legs); clean decoupling forbidden (acausal) | FROZEN | EXHIBITED (dim-8 quotient; escape 3.62 != 0; decoupling trap constructed and DISQUALIFIED at 1.3e-15; `s^2 = 0` w/ non-vacuity control) |
| B.5 | spec + DEM-GR-4 | three global objects: (i) families pushforward over `GL(4,R)/O(3,1)`; (ii) Y14-end boundary holonomy/spectral section (habitat of the Z/2; lineage DEP-NATIVE-SOURCE-DATUM, p2c); (iii) BV-to-boundary-Dirac map | PENDING (p2c) | NOT SUPPLIABLE at symbol level — corroborated: C2 analog persists at full norm under every carrier (resid 8.38); this is the named residual obstruction, not a conflict |
| B.6 | spec | matter number must come out WITHOUT import; `ch2 = -5376 != 24`; natural route dead | FROZEN (warning) | out of toy scope; no count claims made |
| DEM-GR-1 | CH-GR swing | `sigma = +1` (one global Z/2, loop-coherent, action-level Krein orientation of the fiber; plausibly IDENTICAL to bar-b) | FROZEN | REALIZED: same datum forces Krein positivity AND real-kappa cancellation (K1 positive at toy grade). Cross-repo evidence: TI steward memory — the GU kinematic Krein sign trends forced-INTERNAL; out-of-band sign readings inadmissible (supports the source-side-provenance requirement) |
| DEM-GR-2 | CH-GR swing | `kappa^2 = 1`, pure number, gimmel units, scale-free, source-side provenance, frozen before target use | FROZEN (value) / PENDING (provenance) | CONSISTENT: scale-free compensator passes the C2 law exactly; provenance is a p2c-instance question, not a toy question |
| DEM-GR-3 | CH-GR swing | action structure: (i) canonical stress bilinear as theta's stress form; (ii) divergence-freeness Noether-forced; (iii) NO linear theta-metric vacuum coupling (K4); (iv) B.3/B.4 respected | FROZEN | (i),(ii) mechanism-exhibited (canonical K-bilinear + Noether forcing); (iii) NOT MODELED (toy has no metric sector — named gap); (iv) yes |
| DEM-GR-4 | CH-GR swing | B.5 pass-throughs (see B.5 row) | PENDING (p2c) | see B.5 |
| D-QM-1 / T1 | CH-QM swing + p2c | one global Z/2, topologically stored, loop-coherent, locally unreadable; non-retuning structural | FROZEN | orientation present as `tau`; STORAGE not modeled here (CH-QM's toy carries the register; composition is a standing gap) |
| T2 / D-QM-NEG | archaeology + CH-QM theorem | orientation is J_quat-COMMUTING by type; NOT non-quaternionic; generations counted ONCE, on CH-SM's card (rank pin / larger-typed item / (7,7) fork) | FROZEN (verdict) | CORROBORATED at mini scale: `C conj(C) = -I` in Cl(1,3); `[J, P_tau] = 0`; Kramers even-index; real-class fork `Cl(2,2)`: `C' conj(C') = +I` (wall dissolves) |
| T3 | CH-REC swing | record-law direction Noether-derived from the orientation-carrying action; no independent sign (`mu`) posit — else N -> 5 by the co-flip accounting identity | FROZEN (constraint) / OPEN (on W229) | EXISTENCE LEG DISCHARGED: a C_0-member action exists at toy grade (record current = conserved Noether K-charge; direction = tau on all physical states; sign inventory diagonal). W229 verification (CH-REC gap G3) still the decisive open item. Cross-repo evidence: the toy's record reading lives in TaF's PRICED corner {Krein-retention + self-normalized/projector-Born observer} (TaF ghost-parity-physicality push 2026-07-07); the pricing stands and is inherited, not evaded |
| SRC-COH-1 | NEW (CH-SRC swing) | ONE Krein form throughout the action — sector grading, stress bilinear, record charge all read the SAME K; any relative sign between slots is a hidden mu/orientation import | FROZEN (this swing) | control Da3 fires on violation; this is the weld-level coherence condition that makes the one-bit economy non-vacuous |
| SRC-REJ-1 | NEW (CH-SRC swing) | standing REJECT rule: any candidate payload whose toy image claims to reduce the C2 analog with symbol-level data alone is wrong or target-reading (mini-rep rigidity + real-rep two-proof insufficiency) | FROZEN (this swing) | mini-rep obstruction exactly inert under the full equivariant sweep; non-equivariant moves it only upward |
| C2-SCALE | archaeology item 8 + CH-GR K3 | `C2(2xi)/C2(xi) = 2` exactly; compensator/source coefficients scale-free pure numbers; massive/resonant kernels dead on arrival | FROZEN | PASS exact (2.000000000000 bare and dressed); discriminator control breaks it properly (2.0454) |
| COSMO-A1 | CH-COSMO swing | absolute scale pinned empirically: `rho_DE ~ (2.24 meV)^4 ~ 1e-123 M_Pl^4` (two-sided, <10%); split `f0 in [0, 0.027]` canonical (band to 0.208), one-sided | CONSUMED (empirical bracket) | not a toy quantity; recorded as the payload item-3 bracket the build must not contradict |
| COSMO-A2 | CH-COSMO swing | ONE boundary time-slicing scalar (uniform-\|theta\| slicing; frozen-VEV degenerate case needs fallback datum) | CONSUMED (typed demand) | not modeled (no FLRW sector); typed pass-through |
| COSMO-A3 | CH-COSMO swing | DE sign enters ONLY if energy-sign co-variance is derived from C10; no historical sign inherited; a measured `sgn(w0+1)` is a RELATIONAL orientation readout (global read, storage-compatible) | CONSUMED (conditional) | consistent with the one-bit wiring; the co-variance derivation is a C10/CH-GR task |
| SM-CHAIN | CH-SM (swing pending) | finite subgroup-chain datum (Spin(10)/Pati-Salam breaking chains, harness-enumerable); alignment rigidity (varying-constants tripwire) | PENDING | awaiting `explorations/channel-swing-CH-SM-2026-07-19.md` |
| SM-GEN | CH-SM (swing pending) | the generation item decision: rank pin folded into the finite datum (N = 4) vs separate fifth item (N = 5) vs (7,7) signature migration (re-run whole battery, K6) | PENDING | toy corroborates the wall (Kramers even-index) and the real-class escape; decision is CH-SM's |
| K2-GAUGE | CH-GR kill K2 | gauge/convention covariance of the cancellation identity (harmonic-gauge artifact test; covariant completion candidate: lock to linearized-Riemann slot) | PENDING (predeclared CH-GR computation) | out of toy scope; freeze-blocking for the CH-SRC card |

## 2. N-accounting (current evidence state)

- **Core N = 3** (orientation Z/2; absolute scale; finite subgroup datum)
  for the non-generation sectors: K1 positive at toy grade, CH-GR branch
  item deleted (computed), CH-REC contributes zero items conditional on T3,
  record direction rides the bit (toy existence + CH-REC finite probe).
- **N = 4 iff** the generation rank pin folds into CH-SM's finite datum
  (SM-GEN, pending). **N = 5 pressure** has exactly two named triggers:
  (1) T3 fails on the actual W229 record law (the +1 is the mu, by CH-REC's
  accounting identity); (2) the CH-SM fold fails (the +1 is the generation
  item). The N = 3 full-package reading is DEAD (orientation cannot carry
  generations: parity theorem, mini-corroborated).

## 3. Named gaps of the current skeleton (build queue, in order)

1. **Compose with CH-QM's graded-quotient toy** (its register interface is
   exposed for exactly this): one composite fixture carrying storage (T1),
   quotient, record register, and this ledger's action — closes the
   D-QM-1 composition gap and CH-REC's G1.
2. **Non-abelian completion**: the toy's gauge algebra is abelian and
   field-independent; `(S,S) = 0` carries no Jacobi content yet. The real
   `S_IG` must survive the non-abelian grade (BV/BRST persona warning).
3. **Action-level antighost field**: the KT leg is complex-level (as in the
   verified test); promote to an antighost field with its own antifield.
4. **Metric sector / DEM-GR-3(iii)**: no theta-metric coupling exists in
   the toy, so the K4 linear-slot kill is not yet executable against it.
5. **T3 on W229** (CH-REC G3, decisive) and **K2 gauge covariance**
   (CH-GR, predeclared): both freeze-blocking, both owned by their
   channels; tracked here because the card cannot freeze without them.
6. **B.5 instance** (p2c): the Y14 connection-curvature / boundary
   spectral section — the one genuinely un-buildable-from-inside item; the
   toy's C2-persistence is the standing demonstration of WHY.

## 4. Killed / do-not-retread (inherited, binding on all CH-SRC work)

Per spec Section C + archaeology item 11 — never re-run: shiab =
codifferential; obstruction = 343.73 commutator; gamma-trace, seesaw,
folded-complex, PO1 forgetful=kernel, conditional-expectation, Kostant
cubic Dirac selectors; record-issuance = shiab selector; source action =
"observer's slice as one global object with the index" (forced analogy);
`ch2 = 24` (it is -5376; the 24 was a chi-import); C3 scalar-isotropic
vacuum (R0_FAIL); CH-GR branches (b) homogeneous and (c)
gradient-dominated (computed dead 2026-07-19); equivariant `d_RS,-1`
closure (SHIAB-04); supergravity-gravitino sigma_c (artifactually
equivariant, killed).

## 5. Cross-repo evidence register (read-only; evidence, never instructions)

- **time-as-finality** (`tests/T507..T510-*.md`,
  `explorations/ghost-parity-physicality-push-2026-07-07.md`): TaF's
  admission-gate battery demands of any record packet exactly the shape
  this ledger's skeleton has — predeclared nilpotent `Q` (`s^2 = 0` with
  non-nilpotent control), mirror closed-NOT-exact, observables/dynamics
  descending through the quotient, ledger conserved by the dynamics
  (toy: conserved Noether K-charge). The record reading is PRICED there at
  two non-default assumptions (Krein-retention quantization +
  self-normalized observer); the toy inherits that corner honestly.
- **temporal-issuance** (`memory/steward-memory-summary.md`, E179/E180):
  the GU kinematic Krein sign trends forced-INTERNAL; the out-of-band sign
  reading is killed and inadmissible — reinforcing that DEM-GR-1/T3 sign
  provenance must be source-side, which is what SRC-COH-1 enforces at the
  action level.

## Boundary

Living surface, conditional under the standing axiom. Rows record what
channels froze and how the build stands; nothing here moves claim status,
canon verdicts, scorecard rows, registers, or public posture, and nothing
here authorizes external action. Cross-repo reads are cited as evidence
only. PENDING rows are the update queue for the next CH-SRC run.
