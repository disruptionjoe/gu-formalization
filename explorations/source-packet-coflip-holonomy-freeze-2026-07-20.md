---
title: "Frozen evidence packet: the co-flip as derived holonomy of the Z/2-twisted Krein bundle over the metric fiber — commit-pinned receipts, typed grades, consumer gap analysis, adoption ladder"
status: frozen_evidence_packet
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (cross-repo evidence-packet freeze)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/sig-b5-habitat-verification-2026-07-20.md
  - explorations/blockbuster-p5-instance-dossier-2026-07-19.md
inputs:
  - lab/process/source-object-interface-contract.md
  - explorations/sig-b5-habitat-verification-2026-07-20.md
  - explorations/blockbuster-p5-instance-dossier-2026-07-19.md
  - tests/channel-swings/sig_b5_habitat_probe.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
runnable:
  - tests/channel-swings/sig_b5_habitat_probe.py
frozen_at_commit: 32e3603f12aae3fc76298534c47a204b5584b171
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
packet_semantics: >
  FROZEN EVIDENCE PACKET, GU-owned. This file freezes what gu-formalization
  has machine-verified about the co-flip/holonomy result as of commit
  32e3603, typed by grade, so that consuming repos (possibility-to-
  capability primarily; time-as-finality and temporal-issuance for
  awareness) can adjudicate it against their own gates. It is NOT a
  source-owned packet under the interface contract: provenance independent
  of the GU consequences is the consumer's to establish, and this packet
  says so in Section 6. Nothing here asserts the source object exists.
---

# Frozen evidence packet: co-flip = holonomy of the Z/2 Krein twist

## 1. Identity

- Packet name: `GU-COFLIP-HOLONOMY-FREEZE-2026-07-20`.
- Owner: gu-formalization (this repo). Ownership does NOT transfer with
  citation; the packet is GU-adjacent evidence until a consumer gives its
  contents independent source-side identity (Section 6).
- Object frozen: the machine-verified statement that, on the actual
  verified Cl(9,5) = M(64,H) representation and the program-native metric
  fiber F = GL(4,R)/O(3,1),
  1. pi_1(F) = Z/2 at matrix grade (double-cover monodromy -1, squared
     loop closed; the covering-space step typed IMPORTED-standard);
  2. the Krein form K_S = e_0...e_8 is a section of a genuinely
     Z/2-twisted bundle over the generator loop (all 45 mixed (+,-)
     planes transport K_S -> -K_S; all 46 same-sign controls -> +K_S;
     doubled loop untwisted; lift-independent via det(h_9));
  3. the co-flip (Krein sector and record direction flip TOGETHER,
     register history invariant) is DERIVED as the holonomy of that
     twist — one composed machine-checked chain: transported form
     exchanges the two Krein anchors exactly (P_+(-K_S) = P_-(K_S)),
     charge and record current flip sign, and a direction flip inserted
     ALONE (a mu) still splits the register (the paid/unpaid accounting
     survives composition).
- What the co-flip previously was: a posited/accounted identity (CH-REC
  finite-class accounting; hardened to theorem + sorry-free Lean
  certificate for the FINITE CO-FLIP CLASS in commit 91e3fae). What it is
  now: additionally derived as loop holonomy of a concrete geometric
  twist on the verified rep. The geometric derivation is the new fact.

## 2. Provenance chain (commit-pinned)

| commit | date | role in this packet |
|---|---|---|
| `995857d` | 2026-07-19 | interface contract frozen (`lab/process/source-object-interface-contract.md`, packet-field spec used here) |
| `b90fb75` | 2026-07-19 | P5 instance dossier created (`explorations/blockbuster-p5-instance-dossier-2026-07-19.md`) — the candidate's source text; pre-declared falsifiers F1-F8 |
| `91e3fae` | 2026-07-20 00:19 -0500 | hardening wave: co-flip theorem, sorry-free axiom-free Lean certificate (`Lean/GUFormalization/CoflipCore.lean`), one-bit dossier v2 |
| `b7275dd` | 2026-07-20 00:47 -0500 | lane-state refresh after the hardening wave |
| `32e3603` | 2026-07-20 05:59 -0500 | habitat verification: pi_1(F) = Z/2 and the K_S twist machine-verified; co-flip derived as holonomy; dossier 1.2 mechanism repaired. **Freeze commit (HEAD at freeze).** |

Frozen file identities at `32e3603` (git blob SHAs):

- `explorations/sig-b5-habitat-verification-2026-07-20.md` — `e3cdc90`
- `tests/channel-swings/sig_b5_habitat_probe.py` — `caacdcf`
- `explorations/blockbuster-p5-instance-dossier-2026-07-19.md` — `b096925`
- `lab/process/source-object-interface-contract.md` — `1b5f61e`

Runnable receipt: `tests/channel-swings/sig_b5_habitat_probe.py`
(deterministic, numpy only, no network). Exit code 0. Headline
`15 [E] + 2 [F] = 17` (setup `[T] = 3` excluded), ALL PASS.
Re-executed at freeze time 2026-07-20 (this packet's assembly): exit 0,
identical headline. Upstream object receipts:
`tests/oq_rk1_cl95_explicit_rep.py` (the verified Cl(9,5) rep),
`tests/channel-swings/pt3_w229_membership_probe.py` (K_S, J^a, register
conventions — identical conventions consumed unmodified).

## 3. Typed claims, by grade

**Machine-PROVEN at matrix grade** (probe-checked on the verified finite
rep; exit 0; each row names its probe part):

| claim | receipt |
|---|---|
| F = GL(4,R)/O(3,1) deformation-retracts onto the RP^3 model {I - 2P}; signature constant along the path (sampled) | Part A |
| generator loop has double-cover monodromy -1; squared loop lifts closed — the order-2 class; pi_1(F) = Z/2 with the covering-space step typed IMPORTED-standard | Part A |
| the congruence loop g_t = A_t^T eta A_t (pi-rotation in a mixed plane; Sylvester keeps (9,5)) is a genuine closed loop in F projecting onto the generator | Part B |
| transported K_S = -K_S on ALL 45 mixed planes; +K_S on all 36 (+,+) and 10 (-,-) control planes; doubled loop -> +K_S; det(h_9) lemma makes the -1 lift-independent. The twist is real and fires exactly on the genuine F-loops | Part B |
| holonomy exchanges the two Krein anchors exactly; Krein charge and record current flip sign; (sector, direction) co-flip with register history invariant — anchor exchange IS the holonomy, one composed chain | Part C |
| control: direction flip inserted alone (mu) splits the register — the unpaid Z/2 stays detectable at the holonomy composition point | Part C |
| repair: the dossier-1.2 "timelike leg e_0 in K_S" mechanism is dead (timelike legs are e_9..e_13, not K_S factors); the sign comes from the SPACELIKE partner leg. Same conclusion, corrected mechanism | Part C |

**Proven elsewhere, consumed here as typed input:** the finite co-flip
class theorem and its sorry-free, new-axiom-free Lean certificate
(`Lean/GUFormalization/CoflipCore.lean`, commit 91e3fae) — the abstract
accounting identity the holonomy derivation now grounds geometrically.
Kramers blindness of every J_quat-commuting GU-native probe
(NATIVE-PROVEN, canon no-go; untouched and untested by this probe).

**Conditional (bounding everything above):** all results sit under the
boundary-adapter standing axiom at R0_COND working grade, and "matrix
grade" means the verified FINITE rep — not the actual infinite-
dimensional boundary geometry. The identification of the congruence loop
with the loop the families pushforward actually sees is exact at this
grade and unexamined at N2 grade (dossier falsifier F1's residual).

**Externally posited (unchanged by this packet):** the VALUE of the bit
— which of the two sectors obtains. Kramers blindness stands: no
GU-native operator reads it. The value remains the one external Z/2
posit, typed p2c-owned per the tri-repo signed-graph result (the
forgotten orientation). The habitat being proven makes the blindness
derivation load-bear MORE, not less.

## 4. Branch assumptions and normalizations

- Signature convention (9,5): eta = diag(+1 x9, -1 x5); the five
  timelike legs are e_9..e_13; K_S = e_0...e_8 has NO timelike factor
  (probe-pinned, [T] row). Consumers importing the twist computation
  must import this convention or re-derive under their own.
- The loop is a CONGRUENCE path (moves the metric), not an isometry or
  gauge transformation — that is why the holonomy is physical. Program-
  native constructions throughout per `GEOMETER-VS-PHYSICS-OBJECTS.md`;
  no standard-physics substitute used silently.
- Register/record conventions are those of the pt3 W229 membership
  probe, unmodified.
- Sector count is TWO (one loop class, flat Z/2) — not the toric code's
  four; no D = 2 arithmetic transfers.

## 5. Loss ledger, import counts, explicit nonclaims

Loss ledger (what the finite rep loses against the actual object): the
non-compact fiber directions are not modeled (the RP^3 class is carried
at 4x4/14-dim matrix grade); no boundary Dirac FAMILY is constructed;
"deformation retraction" and "continuous frame" are sampled/discretized
statements at machine tolerance (1e-9..1e-12), not symbolic proofs;
the covering-space step pi_1(RP^3) = Z/2 is IMPORTED-standard.

Import count: this packet adds NO new payload import. N-accounting is
unchanged from round 11 (core 3, ceiling 4, both named +1 triggers
intact). The bit is counted once; holonomy/anchor-exchange/tau/eps are
one datum in several costumes (machine-checked edge, not an analogy).

Explicit NONCLAIMS — none of the following exists or moved:

- No B.5(i)-(iii) theorem-grade objects: no families pushforward over
  the non-compact fiber (N1), no boundary Dirac family for the actual
  Y14 end and no spectral section for it or its classification (N2 —
  dossier falsifier F2, the sharpest kill, is OPEN and is this
  candidate's live stake), no BV-to-boundary-Dirac weld (N3).
- No absolute scale: nothing computes 2.24 meV; the scale element
  remains an ASSUMED empirical import with a candidate slot only.
- No generation integer: Door B remains a pure DEMAND.
- No F5 relevance result: whether C2's global residual actually depends
  on the sector flip is untested (needs an end-model; M2/N2 grade).
- No claim-status, canon, verdict, scorecard, or public-posture
  movement; no anyon/TEE physics; C2 is not an index.

## 6. Gap analysis against each consumer's gate (honest)

### possibility-to-capability (primary consumer, designated home of the value)

P2C's gate language (read-only: `LANE-STATE.yaml` Lane 1;
`steward/research-portfolio.json#P2C-CROSS-REPO-ADJUDICATION`):
"Wait for source-grounded specimen; do not build GU ETA/Z2 habitat from
mailbox text alone"; prior GU note recorded as "not importable source
truth"; next swing wants "a source-grounded exact-Hamiltonian
topological specimen or a finer physical P2C-W1 transition model";
witness success condition wants matched before/after descriptions, a
fixed intervention menu and budget, a native response, and a
discriminator from the strongest completion rival.

What this packet DOES satisfy:

- It is no longer mailbox text alone: a frozen, commit-pinned,
  independently re-runnable source text with typed grades and
  pre-declared falsifiers (the "frozen source input" p2c's steering said
  to wait for, on the GU side of the interface).
- It supplies the specimen's SPECIFICATION and verification target: the
  two-sector flat-Z/2 carrier shape, the Kramers-blind reader class, the
  loop-only access mechanics, the exact controls a faithful finite model
  must reproduce (45/46 trichotomy, doubled-loop closure,
  lift-independence).

What it does NOT satisfy — p2c's side to establish:

- **Independent provenance.** The interface contract's identity clauses
  (`provenance_independent_of_gu_result`,
  `source_owned_not_gu_constructed_from_consequence`) are structurally
  unsatisfiable by any GU-authored file, this one included. Anything
  built from this packet must acquire source-side identity and
  provenance in p2c's own vocabulary before it can return as an
  instance (the W3 rung below exists for exactly this).
- **No Hamiltonian.** The result is kinematic; p2c's stated preference
  for an exact-Hamiltonian specimen is not met and is not claimed met.
- **No transition/witness frame.** No before/after task pair, no
  intervention menu or budget, no native response, no completion-rival
  discriminator in p2c's sense — W1/W2 would build these p2c-side.

Net: this packet is a qualified CANDIDATE INPUT for p2c's
source-grounded-specimen gate — the strongest frozen input GU can emit
— not a passer of that gate. It is GU-adjacent evidence with a proposed
adoption ladder, and it says so.

### time-as-finality

TaF's disposition of the prior co-flip note (their archive,
2026-07-19): "source-adjacent watch evidence only"; Lane 1 "parked until
a provenance-valid physical source packet, frozen witness, source-owned
native record-issuance rule, or sharper counterexample changes the T587
contract."

- Closed by this packet: the evidence-grade gap inside the co-flip
  result itself — the identity is now geometrically DERIVED (holonomy of
  a proven twist), theorem-backed and Lean-certified in its finite
  class, not an accounting observation.
- NOT closed: every one of their named gates. The packet remains
  GU-owned (not a source-owned packet or TaF-ownable witness); it is not
  a physical source packet; it contains no record-issuance rule. The
  freeze plus a P2C adjudication (P2C being the value's designated home)
  is the path by which a qualifying source-owned packet could later
  exist. TaF's park stands on its own terms.

### temporal-issuance

TI's gate (their `agent-governance/NEXT-TRIGGER-PLAN.md`, active
trigger): six post-tournament survivor criteria, scored honestly:

1. source-owned transition law — NOT met (kinematic result; no
   transition law, no issuance event);
2. internal anti-after-naming — shape present only (falsifiers F1/F3
   were pre-declared in the dossier before the probe ran), but there is
   no issuance event for after-naming to threaten; not met as TI means it;
3. W4 perturbation nonfactorization — not tested;
4. native carrier or algebra growth — NOT met (fixed kinematic carrier;
   nothing grows);
5. matched intervention/resource budget — absent;
6. observable difference from the strongest fixed rival — the 45/46
   trichotomy is a discriminator SHAPE, not a physical observable
   difference in TI's sense.

Additionally TI's do-not-repeat list bars "emergent effective-gauge or
topological-sector" candidates "unless their missing source-law objects
appear" — the missing source-law object has NOT appeared. Verdict this
packet asserts about itself: still NOT a qualifying candidate for TI's
gate; grade upgrade (toy -> matrix-grade-proven habitat) only.

## 7. Adoption ladder (carried from P5 Element 5; a work program p2c may adopt)

Provenance firewall, restated: these are constructions p2c COULD build;
anything built from them must acquire source-side provenance independent
of the GU consequences before returning as an instance. GU's regression
SRC-REJ-1 stands against every rung (symbol-level C2 reduction =
auto-reject).

- **W1 (one week):** two-sector flat-Z/2 variant of p2c's witness
  fixture — one noncontractible loop class, holonomy +-1, same four
  discriminator legs and whole-family absorber. Sector-count honest (2,
  not 4).
- **W2 (one week):** Kramers control — J-doubled (quaternionic) probes
  provably cannot read the sector (mod-2 readout forced even); a single
  non-quaternionic loop probe can. Operationalizes the reader demand.
- **W3 (one week):** provenance/typing freeze of W1/W2 in p2c's own
  vocabulary (identity, assumptions, non-retuning) — the rung that makes
  the artifacts source-owned from birth.
- **M1-M4 (one month):** finite Dirac-family spectral-flow toy
  (holonomy -1 iff odd flow; J-doubled family even); spectral-section
  choice toy with the cut scale as the only dimensionful dial;
  image-through-gu regression against SRC-REJ-1; literature freeze
  (APS, Melrose-Piazza, mod-2 spectral flow, quaternionic families).
- **N1-N4 (needs new mathematics, named not scheduled):** families
  pushforward over the non-compact fiber; the actual boundary Dirac
  family and section classification (F2 lives here); the
  BV-to-boundary-Dirac map; the Door B property and the scale
  derivation.

## 8. Falsifiers and rollback

This packet is INVALIDATED (not merely incomplete) if any of the
following occurs; on any of them the packet is superseded by a v2 that
names the kill — never edited in place, never silently withdrawn:

- P1. An error is found in `sig_b5_habitat_probe.py` (logic, numerics,
  or convention pin) that changes any [E]/[F] outcome. The probe is the
  packet's load-bearing receipt.
- P2. F1-residual fires at N2 grade: the configuration space the
  families pushforward actually sees kills the RP^3 class (the
  congruence loop fails to represent the relevant loop).
- P3. F2 fires: the section-classifying invariant for the actual
  (quaternionic, Krein-indefinite) boundary family is trivial — the
  two-section READING of the twist loses its object (the matrix-grade
  twist itself stands, but the packet's stored-bit interpretation dies).
- P4. F4 fires: a J_quat-commuting GU-native reader of the sector is
  exhibited — the externally-valued typing is falsified (double-edged:
  good for GU-native economy, fatal for this packet as typed).
- P5. F5 fires: C2's global residual is sector-flip-invariant in a
  faithful end-model — the datum is not the thing C2 needs.
- Rollback: consumers citing this packet must cite
  `GU-COFLIP-HOLONOMY-FREEZE-2026-07-20` + commit `32e3603`; a
  superseding v2 releases them from nothing automatically — each
  consumer re-adjudicates. GU will notify each mailbox previously
  notified if any P-falsifier fires.

## 9. Boundary

Freeze artifact under the standing axiom, R0_COND working grade. No
claim status, canon verdict, scorecard, register, or public posture
moves; no cross-owner writes (consumer surfaces read read-only:
p2c LANE-STATE.yaml + research-portfolio.json, TaF and TI mailbox
archive notes, TI NEXT-TRIGGER-PLAN.md); no external actions; no Lean
run required (the Lean certificate is cited at its landing commit).
Cross-repo routing happens by mailbox proposal notes only, per this
repo's AGENTS.md; the receiving stewards adjudicate.
