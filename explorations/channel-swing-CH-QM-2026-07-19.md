---
title: "Channel swing CH-QM: the graded-quotient toy runs, and the J_quat verdict on the orientation"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (channel deep-research swings)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends: explorations/five-leg-swing-2026-07-19.md
inputs:
  - explorations/adapter-assumed-four-leg-swing-2026-07-19.md
  - explorations/assembly-archaeology-recovered-parameters-2026-07-19.md
  - explorations/construction-space-qm-checklist-p4-2026-07-19.md
  - lab/process/source-object-interface-contract.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/no-go-quaternionic-parity-generation-sector.md
  - docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md
tests: tests/channel-swings/ch_qm_graded_quotient_toy.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Channel swing CH-QM

Two deliverables, both machine-checked
(`tests/channel-swings/ch_qm_graded_quotient_toy.py`, exit 0):

1. **H-QM's first falsification test is BUILT and RUN, and the hypothesis
   survives it.** The finite graded-quotient toy produces a positive-definite
   physical sector with state-preserving dynamics for the right orientation;
   the wrong orientation visibly fails, and it fails the way the archaeology
   predicted — **cohomologically** (Noether non-closure), not as a removable
   subspace.
2. **The decisive joint CH-QM/CH-SM probe is ANSWERED for the (9,5) H-class:
   the transmitted Z/2 orientation CANNOT be non-quaternionic.** An
   anticommuting orientation is impossible (theorem, machine-corroborated at
   bit-exact residual), and the canonical ghost-parity orientation commutes
   with `J_quat`. **One payload bit does NOT discharge Krein sign +
   quaternionic parity.** The archaeology's question 6 resolves to its second
   branch: generations force a fifth payload item (or the rank-pin / (7,7)
   reframes below).

All of this is conditional work under the standing axiom. No claim status,
canon verdict, or public posture moves.

## 1. The finite graded-quotient toy (H-QM first test): results

Design (mirrors the p2c fixture style conceptually, implemented standalone):
a 9-dim Krein module — one transverse mode, one hyperbolic gauge block
`(g,s)`, three generation/mirror hyperbolic pairs `(u_i, v_i)` — carrying a
pseudo-Hermitian dynamics `H` with the true orientation `sigma* = +1` baked
into the ACTION side; the received bit `sigma` arrives from a p2c-style Z/2
register (loop of 6 edges, vertex-flip gauge, holonomy-stored). The
transmitted object is the **action-level Noether identity**
(`delta_2(psi) = K(n_sigma*, H psi)`), per spec B.2 — not the bare
differential. The received bit defines `d_{RS,-1} = ( . )·n_sigma` with
`n_sigma = (g + i·sigma·s)/sqrt(2)` (both candidate gauge directions are
K-null; the bit chooses which root of -1 — resonant with the quaternionic
story). A causality-style coupling `c` leaks the pair sector into the
`sigma*` null direction; the quotient absorbs it exactly when the bit is
right (the finite analog of "the ghost is causality-required").

| check | right orientation | wrong orientation |
|---|---|---|
| Noether closure `delta_2 . d_{RS,-1}` | `0` exactly (complex closes) | `= gamma = 0.7` — **NON-CLOSURE, the primary failure, cohomological** |
| quotient `ker delta_2 / im d` | well-formed; physical Gram = identity (positive-definite) — Q1, Q6 | ill-formed: `dist(im d, ker delta_2) = 1` |
| dynamics on physical sector | descended `H` exactly Hermitian; norm preserved — Q5 | (see repair branches) |
| toy Born rule | probabilities positive, sum-1 drift `0` — Q3 | — |
| observables | K-Hermitian parity-even ops restrict Hermitian — Q2 | — |
| repair 1: brute grading | — | 3 surviving NEGATIVE-NORM physical states (Q6 fails visibly) |
| repair 2: delete negatives | — | unremovable null "zombie" `n_+` stays in the constraint surface (`im d = n_-` cannot quotient it), Hilbert norm grows exactly `e^{gamma t}` (2.014 → 4.055 checked), and it is REGENERATED from the kept graded ghosts through the coupling (`feed = c = 0.35`) — deletion is not dynamics-invariant; the Velo-Zwanziger analog (Q5/Q3 fail) |
| repair 3: retune `delta_2` | — | restores closure numerically, but requires rewriting the TRANSMITTED identity; blocked structurally because the bit is loop-coherent — no local target-side operation can retune it |
| local inertness (Q4 support) | every proper-subset marginal of the register is identical across the two holonomy sectors; only the full loop reads the bit | same register |

Reading, in the archaeology's terms: B.2 (Noether-forced differential) and
B.4 (cohomological realization; clean decoupling acausal) both have faithful
finite realizations, and the wrong-orientation failure mode presents exactly
as spec'd — non-closure first, negative-norm survivors and zombie
regeneration as downstream symptoms of the one cohomological failure. The
"if both orientations work, the hypothesis is empty" kill was armed and did
NOT fire: **H-QM survives its first test.** The toy does not yet contain the
non-equivariant compensator `sigma_c` (its gauge block is abelian) — that is
a named gap, not a silent one.

## 2. The decisive probe: the J_quat verdict (joint CH-QM / CH-SM)

Question (archaeology item 6): is the transmitted Z/2 orientation itself
non-quaternionic — can ONE payload bit discharge Krein sign + quaternionic
parity, keeping N <= 4?

**Verdict: NO, in the (9,5) H-class. The orientation is quaternionic
(J_quat-commuting) by type.** Three-part argument, each part machine-checked:

**(i) An ANTIcommUting orientation is impossible — theorem.** The Krein Gram
of the matter module is `B = eta_V (x) beta_S` with
`beta_S = e_0 e_1 ... e_8` (the 9 spacelike gammas; verified Hermitian with
NO i-factor, `beta_S^2 = I`). Every generator `e_a` commutes with
`J_quat = (id (x) C)·conj`, `C = e_1 e_3 e_5 e_7 e_10 e_12` (the canon C07
per-generator-exact certificate; re-verified here at residual 0.0e+00), and a
real-coefficient product of J-commuting operators is J-commuting — so
`[beta_S, J_quat] = 0` (verified bit-exact). Therefore J_quat **preserves the
Krein sign**: `K(Jx, Jx) = K(x, x)` (verified, max residual 7e-15). But an
orientation anticommuting with J_quat (`J_K J = -J J_K`) would force
`J(H_+) ⊂ H_-`, i.e. J_quat would map K-positive vectors to the K-negative
physical complement — contradicting sign preservation. So no fundamental
symmetry (no Krein-sign choice) can anticommute with J_quat in (9,5). The
single-pair control (C0) shows what the discharging world would look like —
there the quaternionic structure ANTIcommutes with the Gram and flips the
Krein sign — and C2 shows Cl(9,5) is not that world.

**(ii) The canonical orientation COMMUTES with J_quat, and Kramers persists
inside the physical sector.** The synthesis's V2 result identifies the ghost
parity with K itself on the triplet; since the Gram commutes with J_quat, so
does the ghost parity, and the canonical orientation projectors
`(1 ± beta_S)/2` are J_quat-commuting (verified bit-exact). Both canonical
halves are J_quat-INVARIANT; each inherits a quaternionic structure
(`J^2 = -1` on the sector, verified in the Kramers-doubled pair model); and
every J-commutant Hermitian carrier ON the physical sector has a doubly
degenerate spectrum and EVEN signature (verified; a rank-1 odd carrier has
J-defect 1.41 — it is an import). **Adjoining the orientation bit to the
GU-native algebra does not leave the J_quat-commutant. The quaternionic-parity
no-go survives orientation transmission intact.**

**(iii) A J-breaking orientation exists parametrically but is not
Z/2-typed.** Non-canonical maximal K-positive subspaces that fail
J-invariance exist (the contraction-graph family), and prior canon already
recorded that admissible C-operators are non-unique at spectral degeneracies.
But such a choice is a CONTINUUM datum, not one bit; it is not what the
payload type declares (one global Z/2, loop-coherent), and it is exactly what
"a fifth payload item of larger type" means. Within the declared payload
type, non-quaternionicity is unreachable.

**Consequences.**

- The strongest version of the one-hole picture — one bit carrying Krein
  sign + parity + arrow — is **dead in (9,5)**. This is a
  construction-class kill (H-class signature + Z/2-typed payload), not a
  global GU verdict; the defense attorney gets three named reframes:
  1. **Rank pin** (half-index reading): the fifth item is a single a-priori
     integer, the cheapest possible additional import. N = 5 with item 5 of
     type `integer`, or folded into CH-SM's finite datum.
  2. **(7,7) signature fork**: verified here (C3): the analogous conjugation
     in Cl(7,7) has `J'^2 = +1` — real class, the Kramers wall dissolves.
     The hyperbolic (+96,-96) pairing already survives in (7,7)
     (`tests/generation-sector/ghost_parity_krein.py`), so the Krein/ghost
     story is intact there WITHOUT the parity wall. This is the live
     signature contingency already flagged in canon, now load-bearing: if
     generations must come through the orientation, the construction is
     pushed toward the real class.
  3. **Genuinely larger-typed fifth item** (a non-quaternionic structure):
     allowed, but it is a new import with its own provenance burden.
- **H-REC is untouched.** The arrow/Krein identification needs the bit to
  carry orientation, not to break J_quat. The bit still plausibly carries
  Krein sign + arrow; what it provably does not carry (in (9,5)) is
  generations.
- **CH-SM's card must not point at CH-QM's bit for generations.** The
  scorecard's CH-SM row and the interface contract's open question are
  answered on the pessimistic branch: the subgroup-chain datum plus the
  orientation bit are jointly insufficient; the generation mechanism is a
  separate payload decision.

## 3. CH-QM parameter card (draft for freeze)

**Sector construction parameters (GU-internal, conditional on the payload):**

| # | parameter | value/type | receipt |
|---|---|---|---|
| S1 | matter module | Krein space `(V (x) S, K = eta_V (x) beta_S)`, signature (+896, -896); triplet sector 192-dim = 96 hyperbolic (generation, mirror) pairs | ghost-parity synthesis, machine-checked |
| S2 | grading operator | ghost parity `P`; on the triplet `P = K` (V2); J_quat-commuting (this swing) | canon V2 + C2 check |
| S3 | physical-sector rule | graded quotient: `ker delta_2 / im d_{RS,-1}`, then P-grading by the received orientation; cohomological realization mandatory (both BV legs); clean decoupling forbidden (VZ) | spec B.4; toy repair-2 branch |
| S4 | dynamics condition | `[P, S] = 0` (Turok-Bateman); C-operator derivedness fails at spectral degeneracies (R1) — the orientation is the datum that resolves the non-uniqueness | synthesis update 2026-07-06/07 |
| S5 | certificate battery | Q1-Q6 (P4 checklist), each with a toy-grade machine template now existing | P4 + this toy |

**Adapter parameters (what CH-QM requires the boundary to transmit):**

| # | item | type / range | binding constraints |
|---|---|---|---|
| A1 | global orientation `sigma` | one Z/2, topologically stored (loop-coherent, locally unreadable); range: binary | non-retuning is STRUCTURAL (storage), not procedural — toy Part A; Q4 partially discharged by the storage mechanism itself |
| A2 | the action-level identity | the source action / Noether identity pair `(S_src, delta_2)` whose gauge invariance FORCES `delta_2 . d_{RS,-1} = 0`, with `d_{RS,-1}` determined by `sigma` | **transmits the identity, not the bare differential** (spec B.2); toy realizes this form exactly |
| A3 | compensator hook | non-equivariant ghost `sigma_c` OUTSIDE the Spin(9,5) family | equivariant payloads dead on arrival (B.3 / GHOST-01); NOT yet in the toy — named gap |
| A4 | type annotation (new, this swing) | `sigma` is J_quat-COMMUTING by type | the QM leg neither needs nor can use a non-quaternionic bit; the generation demand must NOT be double-counted onto A1 — it belongs to CH-SM's card as a separate item (rank pin / larger-typed structure / signature fork) |

**Weld-consistency checks the card imposes:** same Z/2 as CH-GR's
cancellation sign and CH-REC's arrow (if H-REC holds); no leg may demand a
J-anticommuting bit (impossible, part (i)); the compensator must reproduce
the C2 scale law `C2(2xi)/C2(xi) = 2` (archaeology item 8).

## 4. Proposed scorecard row (CH-QM) — proposal only, row not edited here

- **Q1: PARTIAL -> YES at finite-fixture strength.** The conditional
  construction now EXISTS and runs: right orientation yields all six
  certificates in toy form; wrong orientation fails cohomologically, exactly
  as the recovered spec predicts. Remaining gap to full YES: lift from the
  9-dim toy to the 192-dim triplet with a candidate `d_{RS,-1}` on the real
  module, and add the non-equivariant compensator.
- **Q2: YES (unchanged), now exercised.** The P4 certificates stopped being
  a list and became a runnable battery.
- **Q3: YES (unchanged), SHARPENED.** Range binary, habitat demonstrated
  (p2c), storage-level non-retuning realized in-toy — but the payload is
  now TYPED: J_quat-commuting. What the bit discharges: Krein sign (+ arrow,
  conjecturally). What it provably does not discharge: generations.
- **Gaps:** (1) triplet-scale lift; (2) Noether-forced `d_{RS,-1}` on the
  real module (the toy realizes the FORM, not the object); (3) compensator
  `sigma_c` absent from the toy; (4) CH-REC co-flip analysis pending (their
  agent, their call).

## 5. Sharpened kill tests

- **K1 (armed and survived):** "both orientations work -> H-QM is empty."
  RUN this swing: wrong orientation fails at non-closure `gamma != 0`. The
  hypothesis is falsifiable and survived its first exposure.
- **K2 (armed and FIRED, scoped):** "one bit discharges Krein sign + parity."
  KILLED in the (9,5) H-class with Z/2-typed payload (Section 2). Scope
  fence: reframes are rank-pin, (7,7) fork, larger-typed item — this is a
  lane-local kill with a defense attorney, not a global verdict.
- **K3 (new, cheap):** equivariant-payload tripwire — any candidate packet
  whose compensator transforms Spin(9,5)-equivariantly is rejected without
  further computation (GHOST-01). Machine test: transformation check on
  `sigma_c`.
- **K4 (new, cheap):** removable-subspace tripwire — any candidate that
  presents its physical sector as a cleanly decoupled H-invariant subspace
  (zero leakage into the graded ghosts) fails B.4/VZ. Toy number: the
  causality coupling `c` must be nonzero and absorbed by the quotient, not
  by deletion.
- **K5 (owned by CH-REC):** co-flip decoupling counterexample -> N -> 5 for
  the arrow. Hook data emitted (Section 6); conclusion not drawn here.
- **K6 (new, signature fork):** if generation recovery forces the (7,7)
  class, the whole Krein/ghost battery must be re-run there. Standing
  results: the hyperbolic pairing survives (7,7); the parity wall does not
  (this swing, C3). A construction that silently changes signature class
  mid-weld is a mutual-inconsistency ending per P0.

## 6. CH-REC coordination (hook, not conclusion)

The toy carries a record register: a sigma-independent weak drive from the
transverse mode into pair 1, with per-orientation raw traces of graded
physical vs ghost occupation and a time-integrated register value. Output for
the current parameters: register integral `-0.0439` for `sigma = +1`,
`+0.0439` for `sigma = -1` — sign-antisymmetric under the orientation flip
in this fixture. Whether that constitutes the H-REC co-flip identity (sector
selection and record direction flip TOGETHER, ALWAYS — including whether the
antisymmetry is structural or fixture-tuned) is CH-REC's analysis to run and
own; the register and traces are left in the script
(`part_D`, `RESULTS["D_ch_rec_hook"]`) as the shared fixture.

## 7. Adapter demand ledger entries (for routing to the interface contract / p2c)

Per standing-axiom rule 4, typed demands recorded this swing (routing to the
contract's ledger is the parent's move; no cross-owner write made here):

- `D-QM-1` — one global Z/2 orientation; holonomy-class storage; **type
  annotation NEW: J_quat-commuting**; non-retuning structural.
- `D-QM-2` — the action-level Noether identity (`S_src` forcing
  `delta_2 . d_{RS,-1} = 0`); the differential is a CONSEQUENCE, never bare
  data.
- `D-QM-3` — non-equivariant compensator `sigma_c` (outside Spin(9,5));
  equivariant candidates auto-rejected.
- `D-QM-NEG` — the QM leg does NOT demand non-quaternionic structure; the
  generation demand must be counted once, on CH-SM's card, as rank-pin OR
  non-quaternionic fifth item OR the (7,7) fork. Double-counting it onto the
  orientation bit is now provably wrong in (9,5).

## Boundary

Everything here is conditional construction under the standing axiom
(`R0_COND`/`R1_COND` working grades). The toy is a finite fixture, not a
field theory; the J_quat verdict is exact for the (9,5) representation-level
structure and machine-corroborated, but its consequence for generations is a
statement about the declared payload TYPE and construction class, not a
global GU verdict. The (7,7) contingency remains exactly as fenced in canon.
No claim status, canon verdict, or public posture moves; no external action;
CH-REC's and CH-SM's conclusions belong to their own swings.
