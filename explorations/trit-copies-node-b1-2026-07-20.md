---
artifact_type: exploration
doc_type: results_of_preregistered_node
status: "Execution of pre-registered Node B1. CORRECTED OUTCOME: B1-HOLDS only for equal Cartan weight-space geometry (same dimension/signature and pairwise vector/Krein-space isometries). The three W_m are weights of one nontrivial SU(2)+ spin-1 module, not three invariant family modules; the generation-copy interpretation and 'external S3 is the only distinction' conclusion are retracted."
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (pre-registered Node B1: identical-copies test)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
preregistration: "explorations/prereg-trit-symmetry-and-fork-2026-07-20.md (commit cafcbc7), Node B1; executed as bound, no mid-flight scope change"
probe: tests/channel-swings/trit_copies_node_b1_probe.py
grade: "COMPUTED for the Cartan weight-space facts (float64 with exact structural anchors; 22 checks all pass). REPRESENTATION-TYPING CORRECTION: equal weight spaces and ladder bijections do not make three SU(2)+ submodules or physical family copies. No claim/canon/verdict/posture movement."
related:
  - explorations/prereg-trit-symmetry-and-fork-2026-07-20.md
  - explorations/hardening-h3-triplet-lift-2026-07-19.md
  - explorations/n6-fingerprint-2026-07-20.md
  - explorations/torsion-generation-arena-2026-07-20.md
  - tests/generation-sector/gen_sector_bridge.py
  - tests/generation-sector/ghost_parity_krein.py
  - canon/ghost-parity-krein-synthesis.md
---

# Node B1: the identical-copies test (executed)

> **REPRESENTATION-TYPING CORRECTION (2026-07-20):** The numerical facts
> below remain valid after choosing the $SU(2)_+$ Cartan: the three weight
> spaces have dimension $64$, identical Krein signatures, ladder
> bijections, and pairwise Krein-space isometries. They are **not**, however,
> three $SU(2)_+$-submodules or three equivariant family copies. They are
> the $m=-2,0,+2$ weight spaces of one nontrivial spin-1 representation;
> the ladder is an $SU(2)_+$ action between weights, not an intertwiner
> between invariant modules. At full
> $\operatorname{Spin}(3,1)\times\operatorname{Spin}(6,4)$ symmetry the
> $192$-dimensional carrier is a tangential triplet, whereas three
> conventional family copies carry a trivial three-dimensional multiplicity
> space, so their characters differ. Consequently the B1 receipt proves
> equal **weight-space geometry after a frame/Cartan choice**, not that the
> weights are three physical generations or that only an external $S_3$
> distinguishes them. A successor frozen-fiber audit also finds that the
> first two author source slots have zero full-symmetry intertwiner into this
> triplet; only $\ker\Gamma$ reaches it. The `B1-HOLDS` label below is
> therefore retained only for its predeclared equal-weight-space test, while
> the generation-sector interpretation is retracted.

## 0. What was bound, and what fired

Node B1 (prereg commit cafcbc7) is the LABEL-CAMP half of the copies/simplex fork. Bound
question, unmodifiable by this node: are the three generation-sectors STRUCTURALLY
ISOMORPHIC copies -- identical as modules/representations up to the external S_3 label (the
"three shards / three degenerate copies / three colors" reading physics favors, since
generations are identical except mass)? Or are at least two of the three genuinely
INEQUIVALENT (label camp wrong)? Pre-declared outcomes: B1-HOLDS / B1-FAILS. Planted control:
three deliberately non-isomorphic blocks must FAIL the same tester.

**Outcome fired: B1-HOLDS.** The three generation-sectors are structurally isomorphic copies;
the only distinction among them is the external label. The isomorphisms are exhibited three
independent ways (one from the SU(2)+ symmetry, one from the frozen quaternionic structure,
one constructed as an exact Krein isometry). Probe: 22 checks, all pass, exit 0.

## 1. The object (structural reading, named before testing)

The three generation-sectors are the three SU(2)+ generation weight-spaces `W_{-2}, W_0,
W_{+2}` inside the verified 192-dim self-dual triplet (the H1/ghost-parity triplet, built
verbatim from `gen_sector_bridge` + the ghost-parity recipe: the Casimir-8 spin-1 eigenspace
of `ker(Gamma)`). These ARE "the three generations" of the spin-1 flavor multiplet; the weight
value is the S_3/Weyl label. Each sector is 64-dim (`{-2,0,+2} x 64`, N6's "3 pair-slots").

This is the correct home for the identical-copies question. The alternative "cube-root
sectors" reading (eigenspaces of the commutant order-3 element) is DEGENERATE and cannot be
what "three copies" means: the C-linear order-3 element `wI` puts the WHOLE triplet in one
eigenspace `(0,192,0)`, and N6's generic commutant element gives `(0,192,192)` -- either way
one or two sectors are EMPTY (the division-algebra freeness of N6). Empty sectors are not
three equal copies. The weight-space reading is the one where copies can live, so it is the
one B1 tests. (Cross-checked in the probe, [E].)

## 2. The invariants: the sectors are genuine Krein modules, and identical

`iJ3` is K-SELF-ADJOINT: `(iJ3)^# = K^{-1}(iJ3)^dag K = iJ3` (defect 2.0e-13). so(9,5)
generators are K-anti-self-adjoint (`beta sigma + sigma^dag beta = 0`), so `J3^# = -J3` and the
factor `i` flips the sign back. Consequence: the three weight-spaces, being eigenspaces of
`iJ3` at distinct real eigenvalues `{-2,0,+2}`, are mutually K-ORTHOGONAL (cross-blocks
`||K|| < 1.6e-14`). K therefore block-diagonalizes over the three sectors and is nondegenerate
on each -- each sector is a bona-fide Krein module with a well-defined signature.

The COMPLETE Krein-module invariant set is `(dimension, Krein signature)`: the H-module type
is dimension-forced because `H (x)_R C = M_2(C)`, so every complex H-module is a sum of copies
of the standard 2-dim rep and carries no invariant beyond `dim/2`. Computed:

| sector | dim | Krein signature | H-dim |
|---|---|---|---|
| `W_{-2}` | 64 | `(+32, -32, 0)` | 32 |
| `W_0`   | 64 | `(+32, -32, 0)` | 32 |
| `W_{+2}` | 64 | `(+32, -32, 0)` | 32 |

All three invariant triples COINCIDE. By the classification of finite-dimensional modules over
a division algebra carrying a nondegenerate invariant Krein form (isomorphism class = dimension
+ signature), the three sectors are pairwise Krein-ISOMORPHIC. Each is neutral (+32,-32); the
triplet's total `(+96,-96)` splits evenly `32+32+32` across the three -- the symmetric outcome.

## 3. The isomorphisms, exhibited (three independent constructions)

The invariant match already forces isomorphism; B1 additionally EXHIBITS the maps, so the
claim rests on constructed objects, not only on an invariant count.

- **ISO-1, the SU(2)+ ladder (symmetry-native, C-linear).** `L = J_1 + iJ_2` is built from the
  frozen gammas, preserves the triplet (leak 2.0e-13), and shifts weight by a fixed step. Its
  blocks `W_{+2} -> W_0` and `W_0 -> W_{-2}` are rank 64 (bijections) with no weight leak
  (5.7e-14). It intertwines the C-linear commutant (scalars, trivially) and is an SU(2)+
  intertwiner: an explicit MODULE isomorphism carrying each sector onto the next. (The ladder's
  explicit `i` makes the antilinear `J_quat` swap raising<->lowering rather than commute -- so
  it is a C-linear, not H-linear, iso; ISO-2 supplies the quaternionic one.)

- **ISO-2, the frozen `J_quat` (quaternionic, antilinear).** `J_quat = C.conj` maps the
  `m`-eigenspace of `iJ3` to the `-m`-eigenspace (antilinear: `J i = -i J`), giving a canonical
  FROZEN antilinear bijection `W_{+2} -> W_{-2}` (rank 64, no leak into `W_0`, 1.6e-14). It is a
  Krein isometry: `<J_quat x, J_quat y>_K = conj(<x,y>_K)` (defect 2.6e-13). So the outer pair
  are isomorphic even as quaternionic Krein modules, from frozen structure alone.

- **ISO-3, constructed exact Krein isometries.** For each pair, signature-adapted
  Krein-orthonormalizers `O_i` (`O_i^dag K_i O_i = eta`, the sorted `diag(+1..,-1..)`) give
  `T_{ij} = O_j O_i^{-1}`, invertible, with `T^# K_j T = K_i` EXACTLY (residuals ~3e-14) for all
  three pairs. This is a hands-on isometry realizing the interchange, valid precisely because
  the signatures match.

**Net:** the three sectors are interchangeable up to relabeling; the only thing distinguishing
`W_{-2}, W_0, W_{+2}` is which external S_3/weight tag they wear.

## 4. Control (demonstrated two-sided power)

The SAME `iso_tester` (dimension gate, signature gate, then constructed Krein isometry) was run
on planted blocks:

- **positive control**: two INDEPENDENT random `(+32,-32)` 64-blocks -> ISOMORPHIC, exact
  Krein isometry built (residual 3.0e-14). The tester CAN return iso; the verdict is not baked in.
- **negative (a)**: dim 64 vs dim 63 -> NOT isomorphic (dimension gate).
- **negative (b)**: `(+32,-32)` vs `(+40,-24)`, same dim -> NOT isomorphic (signature gate).
- **negative (c)**: neutral `(+32,-32)` vs definite `(+64,0)` -> NOT isomorphic.
- **control trio** `{(+32,-32),(+40,-24),(+64,0)}`: 0/3 pairs isomorphic -- the exact opposite
  of the real sectors' 3/3. The test discriminates.

## 5. Five-lens council (inline, short)

**Representation theorist.** The invariant set is complete: over `H` (division algebra, `H (x) C
= M_2(C)`) a complex module is `dim/2` copies of one irrep, so nothing beyond dimension +
Krein signature can distinguish two such modules; equal triples => isomorphic, and the ladder
exhibits the intertwiner. The 32+32+32 split of `(+96,-96)` is the equal, symmetric partition.
Passed.

**Krein operator theorist.** Block-diagonality is earned, not assumed: `iJ3` is K-self-adjoint
(computed 2.0e-13), so the weight-spaces are genuinely K-orthogonal and each carries a bona-fide
nondegenerate signature; the constructed `T^# K_j T = K_i` isometries are exact to 3e-14.
`J_quat`'s antilinear Krein-isometry (outer pair) is the strongest single object. Passed.

**Physicist.** This is the physics-favored answer: generations identical except a label matches
"three identical Krein copies + external S_3 tag." The equal `(+32,-32)` per sector means each
generation carries the same 32-physical/32-mirror hyperbolic content -- no sector is privileged
by the kinematic structure. Mass-splitting, if any, must come from OUTSIDE this frozen structure
(consistent with the program's standing "external datum" shape). Passed.

**Skeptical auditor.** Guarded against three cheats: (i) baked-in verdict -- refuted by the
positive control passing and the negative trio failing under the identical tester; (ii) wrong
object -- the degenerate cube-root reading is explicitly shown `(0,192,0)`/`(0,192,192)` and set
aside with reason; (iii) invariant-only hand-wave -- three explicit isomorphisms are constructed
and checked, not merely counted. One honest scope note recorded below. Passed.

**Fork adjudicator.** B1-HOLDS fires the copies leg. It does NOT by itself decide the fork: the
pre-declared outcomes need B2 (does the trit couple to the grade-2/two-form sector?). If B2
FAILS -> F-COPIES (three identical copies + external label). If B2 also HOLDS -> F-BOTH (copies
that assemble into a simplex). B1 alone rules OUT F-NEITHER on the label side and rules out
F-SIMPLEX-with-B1-failing. Recorded, not overreached. Passed.

## 6. Scope and boundary

Exploration-grade execution of a pre-registered node. The isomorphisms are of the frozen
KINEMATIC Krein structure (the 192-dim self-dual triplet with its `K = eta_V (x) beta_S`); no
dynamics, no mass operator, no Y14 geometry enters -- so "identical copies" is a statement about
the kinematic module structure, exactly the level at which "generations identical except mass"
should read. The verdict is (9,5)-signature conditional like the rest of the frozen spine. The
structural reading (weight-spaces = generation-sectors) is named and defended against the
degenerate cube-root alternative; a referee preferring a different sector definition would file
a NEW node. No claim, canon, verdict, or public posture moves; no external actions; no edits to
existing files; only this document and the probe were written.

## 7. Receipts

- `tests/channel-swings/trit_copies_node_b1_probe.py`: 22 checks = 7 [T] + 10 [E] + 5 [F], ALL
  PASS, exit 0, 21 s, deterministic (seed 20260720), float64 with exact structural anchors
  (`Gamma Gamma^dag = 14 I`, `C Cbar = -I`, all-14 J-commutation at literal 0.0). HEADLINE names
  B1-HOLDS.
- Frozen inputs read in full: the prereg (Node B1), the H3 triplet-lift doc, the N6 fingerprint
  doc, the torsion-arena doc, `gen_sector_bridge.py`, `ghost_parity_krein.py`.
- Pre-registration honored: the bound question was not modified; the control ran (two-sided
  power demonstrated); the outcome is one of the two pre-declared branches; the object choice is
  named and its alternative addressed.
