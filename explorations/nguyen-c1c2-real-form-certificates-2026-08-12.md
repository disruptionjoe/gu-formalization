---
title: "C1/C2 construction result (draft): exact Cl(7,7) gamma ladder, the unique invariant bilinears, and the commutant non-transfer certificate"
status: draft
doc_type: construction_result
created: 2026-08-12
brief_version: "1.0"
run_context: "Nguyen-pincer real-form design packet, first decisive steps C1 and C2, implemented independently per orchestrator brief v1.0"
target: "AC-G1a arena (REAL-CLIFFORD-FORM only; no ambient-signature claim)"
head_pin: "c4f05a13e31a44c069db0119aa489920791dcff0 (2026-08-11 20:11:50 -0500); all repo citations opened at this tree; repo treated READ-ONLY"
target_claim: NONE-NOT-A-KILL
hostile_review: "PLACEHOLDER -- owed by the absorbing/executing run per repository convention; the three-charge self-review in the final section does not substitute for it"
probe: "nguyen_c1c2_probe.py (same directory; python3 stdlib only; deterministic; exact integer arithmetic; 42/42 checks PASS, exit 0, ~2.6 s)"
relates_to:
  - explorations/nguyen-pincer-real-form-design-packet-2026-08-11.md (checks C1, C2; Lens 2 expectations; outcome table)
  - lab/sources/source-claim-register.yaml (SC-GRP-01: the p.22 eq (3.19) ladder, restated p.42 eqs (8.3)-(8.6); fn-3 check-me caveat)
  - explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md (p.42 rows: (8.5) degree lists, (8.6) "factors of i required inside the complexification")
  - lab/process/layer0-fork-registry.yaml (REAL-CLIFFORD-FORM settled Cl(7,7)=M128(R); SIGNATURE-AMBIENT distinct and OPEN -- untouched here)
  - tests/observable-algebra/dq2_trichotomy_77_rerun.py (prior COMPLEX commutant leg, float tolerances -- see novelty scoping)
  - tests/chase/MOVE-4/move4_spinor_square_forms.py and tests/big-swing/R4_spin95_hom_vanishing.py (the (9,5) bilinear harness; the (7,7) analog was unrun per the packet; this build is independent, not a port)
  - tests/channel-swings/selected_k77_full_u6464_action_bank_probe.py (8128/16384 previously typed as dimensions only)
binding: >-
  Binds nothing. This draft carries no disposition, no verdict, no registry or
  ledger edit, and no posture change; the executing wave owns every
  disposition. The computation results below are certified facts of exact
  integer arithmetic and are stated plainly as such.
canon_verdict_change: none
row_change: none
registry_change: none
---

# C1/C2 (draft): the Cl(7,7) ladder certificate and the commutant non-transfer certificate

## 1. What was computed

Independent construction (not a rerun or port of any repo harness). The 14
gamma matrices of Cl(7,7) were built on R^128 as a Jordan-Wigner Kronecker
ladder over the four integer 2x2 letters [[1,0],[0,1]], [[0,1],[1,0]],
[[0,1],[-1,0]], [[1,0],[0,-1]]: gamma_k^+ = Z^(k-1) X I^(7-k) and
gamma_k^- = Z^(k-1) Yp I^(7-k), k = 1..7, ordered 7 plus then 7 minus.

Convention: eta = diag(+1 x7, -1 x7). Why: packet check C1 names exactly this
eta, and the source arena is Y^(7,7) with a (7,7) metric (draft-2021 eq (8.3);
register row SC-GRP-01). The mostly-plus-first ordering is the packet's stated
convention; no ambient-signature (SIGNATURE-AMBIENT) claim is made or implied.

Every gamma, and every one of the 16384 Clifford words, is a signed
permutation matrix; all products, transposes, traces, determinants and linear
solves are exact integer arithmetic (no floats anywhere in the probe). The
commutant and invariant-bilinear equations were solved as COMPLETE nullspaces
of the full linear systems on matrix-entry positions by sign-consistent orbit
counting (union-find with a Z/2 sign weight): dimension = number of
sign-consistent orbits; solutions reconstructed by sign propagation. This is
an exact total solve, not a basis ansatz. The encoding is grounded against
dense integer matmul (exhaustive at the 2x2 letter level; all 64 Cl(4,4)
pairs at n=16; independent dense Kronecker rebuild of gammas 1, 8, 14 at
n=128).

Reproduce: `python3 nguyen_c1c2_probe.py` (same directory as this draft;
prints PASS/FAIL per check; exit code = failure count; deterministic, fixed
seed 20260812 used only for sampled-law and planted-negative checks).

## 2. Exact certificate table (all CONFIRMED by computation unless graded)

| # | object | certified result | grade |
|---|---|---|---|
| 1 | Clifford relations | gamma_i gamma_j + gamma_j gamma_i = 2 eta_ij I exactly, all 105 pairs + 14 squares, eta = diag(+7,-7) | CONFIRMED |
| 2 | algebra completeness | 16384 words, all signed perms (w^T w = I), tr(w) = 0 for every w != 1, product law w_a^T w_b = +-w_(a xor b), Gram = 128*I; checksum 2097152 = 128*16384 (the MOVE-4-pattern checksum) | CONFIRMED |
| 3 | volume element | omega = gamma_1...gamma_14: omega^2 = +I, tr(omega) = 0, anticommutes with all 14 gammas; chirality split 64+64 | CONFIRMED |
| 4 | invariant bilinear, eps = -1 | B gamma_i = -gamma_i^T B: solution space dim = 1 (exists, UNIQUE up to scale); B^T = +B (SYMMETRIC); B^2 = I, tr B = 0, invertible => signature exactly (64,64) | CONFIRMED |
| 5 | companion, eps = +1 | solution space dim = 1; B_+^T = -B_+ (antisymmetric), B_+^2 = -I: a symplectic form (the sp(128,R)-type companion) | CONFIRMED |
| 6 | chirality blocks (both forms) | B(S+,S+) = 0 and B(S-,S-) = 0; cross 64x64 block has det = 1 != 0: omega-eigenspaces are B-ISOTROPIC with nondegenerate CROSS-PAIRING (not B-orthogonal) | CONFIRMED |
| 7 | grading split w.r.t. symmetric B | B-skew part of End(S): total 8128 = dim so(64,64), per degree {1:14, 2:91, 5:2002, 6:3003, 9:2002, 10:1001, 13:14, 14:1}; B-symmetric part: total 8256 = 128*129/2, per degree {0:1, 3:364, 4:1001, 7:3432, 8:3003, 11:364, 12:91} | CONFIRMED |
| 8 | degree-2 restriction | all 91 degree-2 words B-skew, 0 B-symmetric: spin(7,7) sits inside so(B) | CONFIRMED |
| 9 | eq (8.5) comparison | skew degrees = {2,6,10,14} + {1,5,9,13} with the dims above: the source's eq (8.5) so(64,64) display is reproduced EXACTLY; the eq (8.6) complement degrees {0,3,4,7,8,11,12} are exactly the B-symmetric degrees (dims above, total 8256 = 16384 - 8128) | CONFIRMED (degree lists); the "factors of i" clothing of the complement is the source's complexification step, not computed here |
| 10 | TRIPWIRE | NOT tripped: an invariant symmetric B of signature (64,64) exists and reproduces eq (8.5); no over-determined escalation; SC-GRP-01 fn-3's "should be checked" caveat is discharged at the algebra level for the (8.5) row and the (8.6) degree lists | CONFIRMED |
| 11 | full commutant (C2) | {X : [X, gamma_i] = 0, i = 1..14} on M(128,R): dim_R = 1, basis = Identity => commutant R, algebra = M(128,R); no invariant complex or quaternionic structure | CONFIRMED |
| 12 | even (Spin) commutant | commutant of all 91 degree-2 words: dim_R = 2 = span{1, omega}; since omega^2 = +I, J = a + b*omega with J^2 = -I needs a^2 + b^2 = -1: impossible over R => no Spin(7,7)-equivariant complex structure on S | CONFIRMED |
| 13 | half commutants | restrictions of all 91 generators to the omega eigenbases are exact signed perms; End_Spin(S+) and End_Spin(S-) both dim_R = 1 (REAL type on each half; consistent with Cl^0(7,7) = M(64,R) + M(64,R), the iso itself graded SCOPED from classification) | CONFIRMED (dims); SCOPED (iso) |
| 14 | Spin-invariant bilinears | dim Hom_Spin(S x S, R) = 2 = span{B, B_+} (packet C1's "expect 1" is the per-epsilon Clifford-intertwiner count: 1 per epsilon sector, certified); blocks: Hom_Spin(S+ x S+) = 0, (S- x S-) = 0, (S+ x S-) = 1, (S- x S+) = 1 -- the (7,7) analog of SHIAB-05 at Spin level: no same-chirality invariant scalar, Dirac-type cross pairing only (a C4 ingredient, computed early) | CONFIRMED |

## 3. Controls table (all planted controls ran; all behaved)

| control | requirement | result |
|---|---|---|
| Cl(9,5) on R^256 (wrong-metric set, brief control (a)) | commutant dim_R 4 = type H | built via Cl(4,0) base + 5 Cl(1,1) doublings; Clifford relations exact for eta (9,5); commutant dim_R = 4, contains J with J^2 = -c I (c > 0), noncommutative: quaternionic type certified. Side-by-side with row 11: the Sp(1)/right-H structure EXISTS on the retired (9,5) horn and has NO counterpart on the settled horn -- the exact non-transfer certificate. (9,5) appears here as CONTROL only. |
| Cl(4,0) on R^8 | commutant 4 (M(2,H)) | dim = 4 |
| Cl(1,1) on R^2 (packet C2 control) | commutant 1 (M(2,R)) | dim = 1 |
| Cl(0,2) on R^4 (packet C2 control) | commutant 4 (H) | dim = 4; solver proven able to answer both real and quaternionic ways |
| Cl(8,0) on R^16 (packet C1 control) | symmetric positive-definite B, so(16) skew part | commutant 1; eps = +1 invariant B unique = +Identity: positive definite (16,0); B-skew part 120 = dim so(16) (textbook) |
| Cl(4,4) on R^16 (packet C1 control) | split symmetric [was SCOPED] | eps = -1 invariant B unique, symmetric, B^2 = I, tr = 0: split (8,8); skew part 120 = dim so(8,8). Packet's SCOPED expectation confirmed |
| sign-perturbed gamma set (packet C1 control) | must FAIL Clifford check | one sign flipped in gamma_5: Clifford verification fails (planted negative detected) |
| antisymmetrized candidate (packet C1 control) | must be rejected by the typer | the eps = +1 antisymmetric companion's grading (skew 8256, degrees {2,3,6,7,10,11,14} = sp(128,R)) is REJECTED by the eq (8.5) matcher |
| broken B, sign-flipped on one slot (brief control (b)) | must FAIL invariance | 28 invariance violations, exact count > 0 |
| seeded random dense bilinear (brief control (c)) | must FAIL invariance | 196722 violations (eps = -1), 196666 (eps = +1) |
| inconsistent system (gamma_1 with both epsilons) | solver must find NOTHING | complete solution space dim = 0 |
| random extra signed-perm generator adjoined | solver must find NOTHING | complete solution space dim = 0 |
| twisted-epsilon sector (eps_1 = +1, rest -1) | typed correctly in-session | consistent twisted intertwiner sector, dim = 1, solution = +-gamma_2..gamma_7 exactly as predicted. NOTE: first planted as "must be 0" -- that expectation was mathematically wrong and the exact solver caught it; retyped as a positive sector-discrimination control. Recorded for honesty. |

## 4. Novelty scoping (anti-redo; run before any "new" wording)

`lab/sources/media-index.md`: zero hits for gamma/bilinear/commutant/Cl(7,7)
terms (grep at HEAD). `novelty-check.py` run for "Cl(7,7) gamma",
"signature (64,64)", "commutant dim", "8128", "8256": prior hits exist and
were read. What is new ABOUT this artifact relative to them:
`tests/observable-algebra/dq2_trichotomy_77_rerun.py` computed the COMPLEX
commutant (C.I on C^128) with float tolerances (taus 1e-4..1e-8, seeded);
this probe certifies the REAL commutant on R^128 by exact integer complete
nullspace. The MOVE-4/R4 exact bilinear harness is (9,5)-instanced; the
packet itself records the (7,7) analog as unrun, and this build is an
independent signed-perm orbit solver, not a port. 8128/8256/16384 appear
in-repo as typed dimensions (u6464 probe); new here is the matrix-level
certificate that a UNIQUE invariant symmetric B realizes the 8128/8256 split
with the eq (8.5)/(8.6) degree lists, plus the signature, isotropy,
commutant, and half-block facts. Commits between the packet pin (bdd2c93)
and this HEAD (c4f05a1) touch K77 jet/gate probes and the claim register,
not this computation.

## 5. What this decides, and what it leaves open (w.r.t. the packet's outcome table)

The typing step (no computation beyond the certificates above; no
disposition -- the wave owns those):

DECIDED BY THE CERTIFIED NUMBERS.
- The native invariance object of the settled horn is the symmetric split
  form: on M(128,R) the invariant B is unique per epsilon sector, and the
  epsilon = -1 form is symmetric of signature exactly (64,64), with all 91
  degree-2 words inside so(B). Infinitesimally, spin(7,7) sits inside
  so(64,64) exactly as the source's eq (8.5) prints it (SC-GRP-01); the
  group-level ladder rung Spin(7,7) -> SO(64,64) follows by exponentiating
  the certified infinitesimal inclusion [that one step SCOPED, standard].
- The complexification step is non-native, exactly: the full commutant is
  R.1 and the even commutant is span{1, omega} with omega^2 = +I, so no
  equivariant J with J^2 = -I exists on S (nor on either half: End dim 1
  each). Passing from so(64,64) to u(64,64) therefore requires structure
  the real algebra provably does not supply -- which is what the source's
  own p.42 eq (8.6) says ("factors of i required inside the
  complexification", register row SC-GRP-01, transcription rows 104-107).
  This CONFIRMS the packet's P1' premise: the step Nguyen flagged as
  unannotated is source-printed, and on this horn it is an addition, not a
  native structure.
- The quaternionic defusal does not transfer, exactly: commutant R on
  (7,7) vs commutant H on (9,5), certified side by side in one run. The
  (9,5)-horn Sp(1)/right-H mechanism has no counterpart object on the
  settled horn.
- Packet outcome row O5 (transfer surprise) is NOT triggered: B is
  symmetric, the commutant is R, eq (8.5) is reproduced, the tripwire did
  not trip. Nothing downstream is blocked on O5.
- No register row is contradicted; this artifact asserts no kill
  (target_claim: NONE-NOT-A-KILL). The computation CONFIRMS SC-GRP-01's
  displayed decomposition and discharges its fn-3 check-me caveat at the
  algebra level.

LEFT OPEN (named, per the fence's three senses of "open").
- Which group the settled-horn theory actually gauges: the operative action
  parent remains SOURCE-SILENT; these certificates type the algebra's
  native invariance object, not the theory's gauge choice. O4 remains the
  live typing branch, now narrowed: any parent candidate must either live
  in the certified real frame (SO(64,64)-type) or carry the posited i
  explicitly.
- The local anomaly leg (packet C3): untouched here; requires the typed
  content through the validated exact lattice.
- The global leg's hinge (packet C4): the Spin-level block table
  0/0/1/1 (no same-chirality scalar; unique cross pairing) is computed
  above, but INVARIANCE OF THE PAIRING UNDER THE TYPED PARENT acting on
  the full content (gauge factor, both ambient halves) is not decided
  here.
- The 2-primary global receptacle (packet C5): untouched.

WHAT WOULD DECIDE THE REMAINDER. C3's typed-content lattice run; C4's
parent-level invariance verdict on the certified cross pairing; C5's
receptacle scoping; or a source display fixing the operative parent (the
O4 wake condition).

## 6. Three-charge self-review (per AGENTS.md; hostile review proper still owed)

Charge 1 -- where the summary outruns the artifact.
- "Spin(7,7) -> SO(64,64) realized": the certified fact is infinitesimal
  (91 degree-2 words in so(B)); the group statement adds exponentiation.
  Kept SCOPED in the text above. SURVIVES (as scoped).
- "u(64,64) requires structure the algebra does not supply": certified as
  no-equivariant-complex-structure in the full and even commutants and on
  both halves. A U(64,64) action UNRELATED to this equivariance frame is
  not excluded by these numbers; the parent-level question is C4/O4.
  NEEDS-RECHECK at C4. The draft states the scoped form.
- "Cl^0(7,7) = M(64,R) + M(64,R)": dims certified; the isomorphism itself
  is classification, graded SCOPED. SURVIVES (as scoped).
- No other summary sentence exceeds a certificate. No further items.

Charge 2 -- where rigor defends a superseded or mistyped object.
- The whole computation lives on the settled REAL-CLIFFORD-FORM arena;
  SIGNATURE-AMBIENT is untouched and no ambient-signature sentence
  appears. DISSOLVED.
- (9,5) appears strictly as a planted control on the retired horn, never
  as a live rival. DISSOLVED.
- One in-session mistyping occurred and is disclosed: the mixed-epsilon
  control was first planted with a wrong expected answer (0); the exact
  solver returned the true twisted-sector solution (+-gamma_2..gamma_7)
  and the control was retyped. DISSOLVED (corrected in-session, recorded
  in the controls table).
- No other items.

Charge 3 -- what else must change if the result stands (wave-owned).
- AC-G1a's "replacement group open" clause can be narrowed (not resolved):
  the native invariance object is now certified; openness reduces to the
  parent CHOICE among the three candidates. NEEDS-RECHECK by the wave.
- The packet's SCOPED verify-manifest rows (B symmetric (64,64); D7-type
  isotropy; commutant = R; Cl(4,4) split control) are now computation-
  confirmed; the executing wave may upgrade those grades. NEEDS-RECHECK.
- SC-GRP-01's adherence note could record the fn-3 caveat as discharged at
  algebra level. NEEDS-RECHECK (register edit is not this draft's to
  make).
- The SHIAB-05 (7,7) analog now exists at Spin level and feeds C4; the C4
  parent-level invariance question becomes the next decisive step.
  SURVIVES as the open hinge.
- No other items.

## Integration correction — the split layer (Joe direct chat, 2026-08-12)

The certificates above stand unchanged. Their TYPING is corrected in
scope (relay-rule compliance: SC-GEO rows for eq (12.19); SC-FER rows
for eq (11.6); SC-GRP rows and the standing two-halves fence):

- C2's "no equivariant complex structure" is equivariance with respect
  to the FULL ambient Spin(7,7), where the Weyl halves are real-64
  (certified). The source's Standard-Model and generations explanation
  does not operate at that layer: it operates after eq (12.19)'s split
  `TX^{1,3} (+) N^{6,4}`, under `Spin(1,3) x Spin(6,4)` — whose even
  algebras are COMPLEX-type, so the Weyl 2's and 16's of eq (11.6)
  carry native complex structures. Restricting from the ambient group
  to the split ENLARGES the commutant: the "factors of i" are native at
  the split layer, supplied by the embedding's decomposition, not
  imported by hand. "An addition, not native" is therefore true only
  ambient-equivariantly and must not be quoted without that scope.
- The two-halves structure completes the typing: `U(64,64)`'s Hermitian
  `(64,64)` is the two chiral halves' `(32,32) + (32,32)` — the standing
  fence's `C^{32,32}` halves and `U(32,32) x U(32,32)` block subgroup
  are the group-side shadow of the split-native complex layer.
- O4 accordingly refines: not "does the action import the
  complexification?" but "WHICH LAYER owns the action — ambient-real or
  split-complex — and is the split-native J the one the source's
  unitary-bundle construction (Portal 01:21, TOE 02:41) uses?"
- **New check C3-prime (bounded, exact, same solver):** compute the
  exact commutant of `Spin(1,3) x Spin(6,4)` generators inside
  `M(128,R)` on the certified gamma bank; expect a commutant strictly
  larger than R containing an equivariant `J` (`J^2 = -I`); verify the
  induced complex-32 structure per chiral half and the Hermitian
  `(32,32)` forms recovering the two-halves fence exactly. A commutant
  of dimension 1 would refute this correction's native-J claim and
  restore the filed typing at full strength — planted both ways.

Relay-rule note: this is the second same-day frame-regression instance
caught by Joe — the first lost the source-native count typing, this one
lost the source-operative LAYER. Both are now worked examples in the
machinery's record.
