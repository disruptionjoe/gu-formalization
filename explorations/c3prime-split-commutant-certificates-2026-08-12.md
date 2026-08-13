---
title: "C3-prime construction result (draft): the exact spin(1,3) x spin(6,4) commutant on the certified Cl(7,7) bank, the native split-layer complex structures, and the Krein C^(32,32) on the total spinor module"
status: draft
doc_type: construction_result
created: 2026-08-12
brief_version: "1.2"
brief_lineage: >-
  Launched under orchestrator brief v1.1; v1.2 ratified mid-run by
  coordinator relay (rule 14: minimum-five specialist-lens preflight, inline;
  correction dropping the launch brief's step-4 per-half-Hermitian
  specification as a mis-specification; C3a/C3b/C3c successor structure;
  independent-replication framing against the hourly gate result).
run_context: "GU Formalization, Nguyen-pincer successor check C3-prime per the 'Integration correction -- the split layer' section appended to the C1/C2 certificates; executed independently in a read-only checkout"
target: "AC-G1a arena, split layer (REAL-CLIFFORD-FORM only; no ambient-signature claim; SIGNATURE-AMBIENT untouched)"
head_pin: >-
  Spec section ('Integration correction -- the split layer',
  explorations/nguyen-c1c2-real-form-certificates-2026-08-12.md) pinned at
  c789e75b; tree read at HEAD 0e299cf5 (hourly commits 29286b1f
  preregistration and 0e299cf5 split-layer gate landed mid-run); repo treated
  READ-ONLY throughout (verified: clean tree after run, no bytecode written).
target_claim: NONE-NOT-A-KILL
run_id: RUN-PLACEHOLDER
hostile_review: "PLACEHOLDER -- owed by the absorbing/executing run per repository convention; the three-charge self-review below does not substitute for it"
probe: "c3prime_probe.py (same directory; python3 stdlib only; deterministic, no randomness; exact integer/Gaussian-rational arithmetic; 23/23 checks PASS, exit 0, ~1.9 s; imports the certified gamma bank and solver from tests/channel-swings/nguyen_c1c2_real_form_probe.py with sys.dont_write_bytecode set)"
relates_to:
  - explorations/nguyen-c1c2-real-form-certificates-2026-08-12.md (the C1/C2 certificates this check extends; the appended correction section is the spec)
  - tests/channel-swings/nguyen_c1c2_real_form_probe.py (certified construction REUSED: gamma ladder, eta, solver -- anti-redo)
  - explorations/conditional-build/selected-k77-split-layer-commutant-action-parent-gate-2026-08-12.md (hourly gate, RUN-20260812-020740: the independent same-question result this run replicates)
  - tests/channel-swings/selected_k77_split_layer_commutant_action_parent_probe.py (the hourly gate's driver; shared audited primitives, different driver code)
  - explorations/nguyen-forest-verdict-preregistration-2026-08-12.md (blind preregistration filed while C3-prime was executing)
  - explorations/nguyen-pincer-real-form-design-packet-2026-08-11.md (outcome row O4; the three honest real-form targets)
  - lab/sources/source-claim-register.yaml (SC-GRP-01, SC-GRP-02, SC-GRP-03, SC-FER-05, SC-CHI-03 -- polarity ASSERTS in every case cited here)
  - lab/process/layer0-fork-registry.yaml (REAL-CLIFFORD-FORM settled; SIGNATURE-AMBIENT distinct and OPEN -- untouched)
  - GEOMETER-VS-PHYSICS-OBJECTS.md and lab/process/NAMES.md (Layer-0 discipline applied; the Krein rows)
binding: >-
  Binds nothing. This draft carries no disposition, no verdict, no registry or
  ledger edit, and no posture change; the executing wave owns every
  disposition. The computation results below are certified facts of exact
  arithmetic and are stated plainly as such.
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
row_change: none
registry_change: none
---

# C3-prime (draft): the split-layer commutant certificate

## 1. What was computed, and on what

Check C3-prime from the correction section: the exact commutant of the
`spin(1,3) x spin(6,4)` generators inside `M(128,R)` on the CERTIFIED
Cl(7,7) gamma bank -- reusing (not rebuilding) the C1/C2 probe's
Jordan-Wigner signed-permutation ladder, its `eta = diag(+1 x7, -1 x7)`
convention, and its exact sign-consistent-orbit complete-nullspace solver.
All results are exact integer arithmetic (Gaussian rationals -- pairs of
`Fraction` -- appear only in the Hermitian LDL* congruence, still exact).
No floats anywhere. The probe is deterministic with no random seed.

**Block assignment (stated, with rationale).** The certified eta ordering is
plus-first (`gamma_0..gamma_6` square `+1`, `gamma_7..gamma_13` square
`-1`), so the eq (12.19) split `TX^{1,3} (+) N^{6,4}` (SC-CHI-03, ASSERTS,
context s11:249-250) selects a NON-CONTIGUOUS base block: the `(1,3)`
factor needs one square-`+1` and three square-`-1` generators. Assignment
used: `BASE = (0, 7, 8, 9)`, `NORMAL = (1,2,3,4,5,6,10,11,12,13)` --
signature multisets `(1,3)` and `(6,4)`, disjoint and exhaustive, verified
exactly. Any other admissible assignment differs by an orthogonal
relabeling inside the plus and minus sets, implemented by Pin(7,7)
conjugation, so the commutant dimension and type are assignment-independent
[that one step SCOPED, standard]; control ALT-ASSIGNMENT verifies it
computationally with the disjointly chosen `BASE = (3, 9, 11, 13)`.
Generators: the 6 base bivectors plus the 45 normal bivectors, 51 total, no
mixed products.

Reproduce: `python3 c3prime_probe.py` (prints PASS/FAIL per check; exit
code = failure count; full transcript in `run_output.txt`).

## 2. Exact certificate table (all CONFIRMED by computation unless graded)

| # | object | certified result | grade |
|---|---|---|---|
| 1 | construction ground | imported certified bank re-verified: 105 anticommutators + 14 squares exact, eta `(7,7)` | CONFIRMED |
| 2 | split commutant (the C3-prime question) | `dim_R End_{spin(1,3)+spin(6,4)}(R^128) = 4` by complete nullspace over all 51 generators; the refutation branch (dim 1, which would have restored the ambient-only typing at full strength) did NOT occur | CONFIRMED |
| 3 | commutant basis and relations | commutant `= span{1, J4, J10, omega}` (all four verified in the computed span; dim 4 forces equality), with `J4 = gamma_0 gamma_7 gamma_8 gamma_9` (base-block volume), `J10` = normal-block volume, `omega` = the ambient volume; `J4^2 = J10^2 = -I`, `omega^2 = +I`, `J4 J10 = J10 J4 = +omega`, all pairs commute | CONFIRMED |
| 4 | algebra type | commutative, so center = whole algebra; relations give `C (x)_R C = C (+) C`, central idempotents `(1 +- omega)/2` = the chirality projections; complete square-root-of-minus-one census by exact case arithmetic on `X = a + bJ4 + cJ10 + d omega`: `X^2 = (a^2-b^2-c^2+d^2) + 2(ab-cd)J4 + 2(ac-bd)J10 + 2(ad+bc)omega = -1` forces `a = d = 0`, `bc = 0`, `b^2+c^2 = 1`, hence EXACTLY FOUR equivariant complex structures `{+-J4, +-J10}` | CONFIRMED (case arithmetic exact) |
| 5 | equivariance | `[J4, sigma] = [J10, sigma] = 0` for all 51 generators, exactly | CONFIRMED |
| 6 | B re-certification | eps = -1 invariant bilinear: dim 1, symmetric, `B^2 = I`, `tr B = 0` => signature `(64,64)` (C1 row 4 reproduced) | CONFIRMED |
| 7 | B-compatibility classes | `chi(1) = +1`, `chi(omega) = -1`, `chi(J4) = +1`, `chi(J10) = -1` (`chi`: B-symmetric/B-skew as in C1 row 7); B-skew slice of the commutant `= span{omega, J10}`; solving `(u omega + v J10)^2 = -I` with `omega J10 = -J4` forces `uv = 0`, `u = 0`, `v = +-1`: the B-COMPATIBLE complex structures (`J^2 = -I` and `J^T B J = B`, verified directly for `J10`) are EXACTLY `+-J10` -- the "factor of i" that is both equivariant and Krein-compatible is the normal-block `(6,4)` volume element, unique up to sign | CONFIRMED |
| 8 | chirality behavior | `[J10, omega] = [J4, omega] = 0`; `J10` PRESERVES each ambient half (does not swap); restrictions are exact signed perms with `(J10|S+)^2 = (J10|S-)^2 = -I` => each real-64 half carries a native complex-32 structure; `J10|S+ = -J4|S+` and `J10|S- = +J4|S-` (forced by `J4 J10 = omega`), so the two units agree per half up to orientation | CONFIRMED |
| 9 | per-half split commutants | `dim End_split(S+) = dim End_split(S-) = 2 = span{1, J|half}`, complex type C on each half; the certified ambient-Spin values were 1/1 (REAL type). The layer contrast is exact: REAL halves ambient-equivariantly, COMPLEX halves split-equivariantly | CONFIRMED |
| 10 | split-invariant bilinears | `dim Hom_split(S x S, R) = 4` (= commutant composed with B); blocks `pp/mm/pm/mp = 0/0/2/2`: even at the split layer NO same-half invariant real bilinear exists; the cross-pairing doubles from the ambient Spin-level 1/1 | CONFIRMED |
| 11 | Hermitian form, total module | `h(x,y) = B(x,y) + i B(x, J10 y)` on `(S, J10) = C^64`: Gram over the J-pair coordinate basis is exactly Hermitian; exact Gaussian-rational LDL* signature `(32,32)`, 0 zero pivots (nondegenerate) => ONE Krein space `C^(32,32)` on the TOTAL spinor module | CONFIRMED |
| 12 | Krein presentation of the halves | `h(S+,S+) = 0` and `h(S-,S-) = 0` identically (both the `B` and the `B(., J.)` blocks vanish); real cross-block det = 1 != 0 (C1 row 6 reproduced) => the two ambient halves are MAXIMAL h-NEUTRAL (isotropic) complex-32 subspaces of the `C^(32,32)`, nondegenerately cross-paired (if `x` in `S+` pairs to zero with `S-`, isotropy makes it h-null, and nondegeneracy kills it -- exact) | CONFIRMED |
| 13 | C3b-partial: conjugate branching | `J|half` is a real operator, square `-I`, `tr(J|S+) = tr(J|S-) = 0` => each complexified half `S+- (x) C = E_{+i} (+) E_{-i}`, a complex-conjugate pair with `dim_C = 32` each (`tr P_{+-i} = (64 -+ i tr J)/2 = 32` exactly); `[J|half, sigma] = 0` for all 51 restricted generators => both eigenspaces are complex-32 SUBREPRESENTATIONS exchanged by conjugation | CONFIRMED |
| 14 | C3b remainder | identifying those conjugate 32s with eq (11.6)'s `(2-+ x 16+) (+) (2+- x 16-)` labels (SC-FER-05, ASSERTS), and deriving the Hermitian `(32,32)` ON the conjugate-pair object (the complexified half), is NOT done here | OWED (= C3b proper): needs the complex branching of `E_{+-i}` under the two factors and an invariant sesquilinear pairing on the complexified half -- one further bounded exact run |

## 3. C3a replication compare (independent driver, same question)

The hourly gate (`selected-k77-split-layer-commutant-action-parent-gate-2026-08-12.md`,
RUN-20260812-020740, filed at 0e299cf5 mid-run) reports:
`End = span{1, J4, J10, omega} = C (+) C`, `J4^2 = J10^2 = -1`,
`J4 J10 = omega`, `omega^2 = +1`, reducing to C on each ambient half (real-64
half = complex-32). This run reproduces DIMENSION, GENERATORS, RELATIONS,
and the per-half reduction EXACTLY -- agreement, no escalation.

Scope of independence, stated plainly: both drivers sit on the same audited
signed-permutation primitives and complete-nullspace solver (the brief's
anti-redo clause mandates reusing the certified construction), and both
declare the same source-owned block indices. The replication is at the
driver level (independent code path, independently chosen controls), not at
the arithmetic-core level. Complementary controls unique to this run:
wrong-split TYPE discrimination (R^4 vs C+C), broken-generator collapse to
dim 3, alternate block assignment, and the exact Hermitian LDL* signature
`(32,32)` with the maximal-neutral-halves presentation (rows 11-12), which
the gate did not compute. Controls unique to the gate: mixed-bivector
adjunction collapse 4 -> 2; the 40 mixed bivectors preserving `omega` while
anticommuting with `J4`; odd directions exchanging the halves.

## 4. Controls table (all planted controls ran; all behaved)

| control | requirement | result |
|---|---|---|
| full Clifford set (14 gammas) | dim 1 (re-certify C2 row 11) | dim 1, basis Identity |
| full ambient Spin set (91 degree-2 words) | certified C2 row 12 value | dim 2 `= span{1, omega}`, `omega^2 = +1` => still no J there. NOTE: the launch brief's control (a) says the 91-product set "must return commutant dim 1"; that expectation conflates C2's 14-gamma row (dim 1) with its 91-word row (dim 2, filed 2026-08-12). Certified numbers preserved; both rows re-certified. The control's PURPOSE (restriction enlarges the commutant) holds exactly: 1 -> 2 -> 4 |
| wrong-split `(2,2) x (5,5)` (brief control (b)) | comparison point | dim 4 -- SAME dimension -- `span{1, u, v, omega}` with block volumes `u^2 = v^2 = +I`, commutative: Klein-four group algebra `= R^4`, NO complex structure (identity coefficient of any square is a sum of four real squares, never -1). Dimension alone does NOT discriminate; the C-vs-R^4 TYPE does, and it tracks the source's `(1,3)+(6,4)` split exactly: blocks with `p-q = -2` and `+2` (complex classes `+-2 mod 8`) vs the control's `p-q = 0` blocks (real-split class) |
| broken generator (one sign flipped in generator 0; brief control (c)) | answer must change | commutant dim 3 != 4 (exact; planted negative detected) |
| alternate `(1,3)` assignment `BASE = (3,9,11,13)` (adversarial-lens addition) | assignment-independence | dim 4; base volume squares `-I` |
| refutation branch (brief clause (d)) | if dim 1: correction refuted, prior typing restored | did NOT occur: dim 4. The native-J claim of the correction section STANDS as computed |

## 5. Five-lens specialist preflight (v1.2 rule 14; run INLINE, retrospectively against the finished computation, before the typing section was written)

| lens | basis | confidence | contribution |
|---|---|---|---|
| representation theory (real forms / commutants) | DIRECT (computed) + SCOPED (classification cross-check) | high | the computed `C (+) C` matches `Cl^0(1,3) (x) Cl^0(6,4) = M(2,C) (x) M(16,C) = M(32,C) (+) M(32,C)` acting with one simple summand per chirality half; classification (`Cl^0(1,3) = M(2,C)`, `Cl^0(6,4) = M(16,C)`) is cited SCOPED, the commutant itself is computed, not inferred |
| Krein / indefinite operator theory | DIRECT (computed) + PRINCIPLE | high | forced the row-7/11/12 distinction: `J4` is B-symmetric (gives a complex-BILINEAR extension, not Hermitian); only `+-J10` is Krein-compatible; `(S, J10, h)` is a Krein `C^(32,32)` whose two ambient halves are maximal NEUTRAL subspaces -- the split-spinor Krein `(+64,-64)` row of GEOMETER-VS-PHYSICS-OBJECTS realized complexly. CHANGED A TYPING SENTENCE: the halves' role is stated as "maximal neutral, cross-paired," not "degenerate restriction" |
| source criticism (which layer the source builds on) | DIRECT (register quotes) | moderate | the unitary-bundle constructions (Portal 01:21, TOE 02:41; `P_H` with `H = U(64,64)`, SC-GRP-02, ASSERTS) are spoken/printed at the complex-parent layer; eq (12.19)'s split (SC-CHI-03, ASSERTS) and eq (11.6)'s labels (SC-FER-05, ASSERTS) live at the split layer; the source nowhere states which layer the operative ACTION connection preserves -- that is exactly C3c, and it stays SOURCE-SILENT |
| Layer-0 semantics (ambient vs split equivariance; the fence objects) | DIRECT (docs + computed) | high | "no equivariant complex structure" is a LAYER-INDEXED sentence: true at ambient Spin(7,7) (dim-2 commutant, no J), false at the split layer (dim-4, four Js). The fence's `C^(32,32)` is kept distinct from the real-64 half (complex-32) and from the complexified half (complex-64, conjugate 32+32): three objects, no silent identification -- the NAMES.md discipline applied to "half" |
| adversarial refutation (what would make the native-J reading wrong anyway) | DIRECT (controls) + PRINCIPLE | moderate-high | (i) a large commutant does not select the action's J: `D_varpi J = 0` is unverified and source-silent (C3c) -- the reading would be wrong AS AN ACTION CLAIM if the operative connection preserves only `omega` (block level) or neither; (ii) four Js exist and only `+-J10` is B-compatible -- a construction using the `J4`-type unit changes the Hermitian story; (iii) assignment-dependence was a live worry: killed by the ALT-ASSIGNMENT control; (iv) dimension-4 alone could be over-read: killed by the wrong-split control (R^4 there). ADDED the four-J caveat sentence and the ALT control to the artifact |

Lens-driven changes, named per rule 14: the Krein lens rewrote the
halves-restriction sentence (neutral-subspace presentation instead of
failure language -- convergent with the v1.2 step-4 correction); the
adversarial lens added the ALT-ASSIGNMENT control and the four-J /
`+-J10`-uniqueness caveat to rows 4 and 7 and to the typing below. No lens
contradicted a computed number.

## 6. Typing: what C3-prime decides, and what it leaves open

Successor structure per v1.2: **C3a replicated / C3b owed / C3c open.**

DECIDED BY THE CERTIFIED NUMBERS (no kill language; no register row is
contradicted; target_claim: NONE-NOT-A-KILL).

- The correction section's native-J claim is CONFIRMED as computed: the
  split commutant is strictly larger than R (dim 4), contains equivariant
  complex structures (exactly `{+-J4, +-J10}`), and the restriction from
  ambient Spin(7,7) to `Spin(1,3) x Spin(6,4)` is precisely what admits
  them (1 -> 2 -> 4). The "factors of i" of the source's p.42 eq (8.6)
  step (SC-GRP-01, ASSERTS; fn-3 caveat) have a NATIVE SUPPLIER at the
  split layer: the block volume elements of the eq (12.19) decomposition
  (SC-CHI-03, ASSERTS), with the Krein-compatible unit unique up to sign
  (`+-J10`, the `(6,4)` normal-block volume). The C1/C2 sentence "an
  addition, not native" remains true AMBIENT-equivariantly and false at
  the split layer -- both now certified at their own layers, matching the
  hourly gate's scope sentence.
- The two-halves fence is recovered IN CORRECTED FORM: one Krein
  `C^(32,32)` on the total `(S, J10) = C^64` with Hermitian signature
  exactly `(32,32)`, whose two ambient chiral halves are maximal neutral
  complex-32 subspaces, nondegenerately cross-paired -- NOT two per-half
  `(32,32)` Hermitian forms on the real halves (impossible: same-half
  invariant bilinears have dimension 0 even split-equivariantly, row 10).
  The fence's per-half `C^(32,32)` object lives on the COMPLEXIFIED
  halves, where C3b-partial certifies the equivariant conjugate 32+32
  branching; the eq (11.6) label identification (SC-FER-05, ASSERTS) and
  the Hermitian `(32,32)` on that conjugate-pair object are OWED (C3b).
  The three-objects fence (two-halves block product / full `U(64,64)` /
  Spin-carrier reading; design packet Lens 4) is NOT collapsed by this
  result: all three parents remain distinct and live.
- O4 REFINES exactly as the correction section proposed, and now has its
  computational floor: the question is no longer "does the action import
  the complexification?" but "WHICH LAYER owns the action" -- and, in the
  gate's covariant-constancy form (C3c): does the operative connection
  satisfy `D_varpi omega = 0` (block level), the stronger
  `D_varpi J10 = 0` (split-native complex level), or neither, or act
  through the full parent before observation. That is an ACTION question;
  no commutant computation can answer it.

LEFT OPEN / SOURCE-SILENT (named).

- Which layer the operative action parent gauges: SOURCE-SILENT (the
  2026-08-09 reinspection stands; the packet's O4 wake condition -- a
  source display fixing the parent -- is unchanged). These are
  algebra-level certificates; whether the source's unitary-bundle
  construction (Portal 01:21, TOE 02:41; SC-GRP-02, ASSERTS) uses the
  split-native `+-J10` is not decided here. C3c.
- C3b proper (label identification + Hermitian form on the conjugate-pair
  object), as scoped in row 14.
- SIGNATURE-AMBIENT: untouched. The anomaly legs (packet C3/C4/C5):
  untouched.

FRAME-SENSITIVE findings (compression would re-import a default frame;
IDs inline).

1. "A native J exists" is LAYER-INDEXED. Compressed without "at the
   split layer, under `Spin(1,3) x Spin(6,4)` equivariance," it
   re-imports either the ambient frame (falsely killing the C1/C2
   no-J certificate) or the complex-parent frame (falsely making
   `U(64,64)` native). [SC-GRP-01 ASSERTS; SC-CHI-03 ASSERTS]
2. "The fence is recovered" is PRESENTATION-INDEXED. The certified
   object is ONE `C^(32,32)` with neutral cross-paired halves;
   compressing to "two `C^(32,32)` halves recovered" re-imports the
   block-product default frame onto the real module, where same-half
   invariant pairings are dimension-0. [SC-GRP-01 ASSERTS; SC-FER-05
   ASSERTS; SC-CHI-03 ASSERTS]
3. "The split supplies the i" is SIGNATURE-INDEXED. The wrong-split
   control has the same commutant DIMENSION with no complex structure
   at all (R^4); compressing to "splitting enlarges the commutant,
   hence i" re-imports a generic-split frame -- the complex type tracks
   the source's specific `(1,3)+(6,4)` signatures (blocks `p-q = -2, +2`).
   [SC-CHI-03 ASSERTS; SC-GRP-03 ASSERTS; SC-FER-05 ASSERTS]
4. "C3-prime confirms the correction" is CLAIM-INDEXED. What is
   confirmed is the commutant/J/Krein layer; the action-ownership
   reading (the refined O4/C3c) is NOT confirmed and stays
   SOURCE-SILENT; compression to "the source operates at the split
   layer" would re-import an action claim the source has not printed.
   [SC-GRP-01 ASSERTS; SC-GRP-02 ASSERTS]

## 7. Novelty scoping (anti-redo; run before any "new" wording)

Greps at the read tree: `Spin(1,3) x Spin(6,4)` commutant work exists in
exactly one prior computational surface -- the hourly gate probe/doc pair
filed mid-run (0e299cf5), treated here as the replication target, not
prior art silently absorbed (Section 3 states the shared-core caveat).
What is new ABOUT this artifact relative to the gate: the exact Hermitian
LDL* signature `(32,32)` on `(S, J10)` with the maximal-neutral-halves
Krein presentation (gate row 5 stops at "no same-half real bilinear");
the complete four-element square-root-of-minus-one census with the
`+-J10`-uniqueness of the B-compatible unit; the wrong-split TYPE
discriminator (R^4 vs C+C) and the alternate-assignment control; the
C3b-partial equivariant conjugate-branching certificate with exact
projector traces. The C1/C2 probe itself computed no split-restricted
commutant (its rows stop at the 14-gamma, 91-word, and per-half
ambient objects). No novelty claim beyond these deltas is made.

## 8. Three-charge self-review (per house convention; hostile review proper still owed)

Charge 1 -- where the summary outruns the artifact.
- "The commutant is C (+) C": the algebra identification rests on the
  certified relations plus the standard identification
  `R[u,v]/(u^2=v^2=-1, uv=vu) = C (x) C = C (+) C`; the relations are
  computed, the last equality is textbook. SURVIVES (as scoped).
- "Pin(7,7) conjugation makes the certificate assignment-independent":
  the general statement is SCOPED (standard); the computation certifies
  it for TWO assignments only. The ALT control makes the summary sentence
  honest. SURVIVES (as scoped, with the control named).
- "Each complexified half branches into conjugate 32+32
  subrepresentations": certified at the J-eigenspace level; NOT yet
  matched to eq (11.6)'s labels (SC-FER-05, ASSERTS). The draft says so
  (row 14). SURVIVES (as scoped).
- No other summary sentence exceeds a certificate. No further items.

Charge 2 -- where rigor defends a superseded or mistyped object.
- The launch brief's step-4 per-half-Hermitian specification was
  mis-typed (it restricts a form to subspaces that C1 row 6 had already
  certified isotropic); v1.2 dropped it mid-run, and this run's own
  Krein lens had independently reached the same conclusion. The
  computation reports the isotropy as a POSITIVE Krein presentation,
  not a failure. DISSOLVED (correction applied, disclosed here).
- The launch brief's control-(a) "91 products -> expect dim 1" conflates
  C2's two rows; the certified value 2 was preserved and both rows
  re-certified. DISSOLVED (disclosed in the controls table).
- (2,2)x(5,5) and the broken generator appear strictly as planted
  controls, never as live rivals. DISSOLVED.
- No other items.

Charge 3 -- what else must change if the result stands (wave-owned; this
draft binds nothing).
- The C1/C2 draft's Charge-1 item "u(64,64) requires structure the
  algebra does not supply -- NEEDS-RECHECK at C4" can now be recorded as
  layer-scoped by these numbers (supplied natively at the split layer,
  not ambient); the correction section already says this, and the wave
  may fold the certificate reference in. NEEDS-RECHECK (wave edit).
- AC-G1a's narrowing can note that the parent-candidate question now has
  an exact split-layer floor (this certificate + the gate); distance
  only, per the gate's own boundary sentence. NEEDS-RECHECK.
- C3b (owed) and C3c (the covariant-constancy gate on `omega` and `J10`)
  become the next decisive steps; the gate names the same successor.
  SURVIVES as the open hinge.
- No other items.
