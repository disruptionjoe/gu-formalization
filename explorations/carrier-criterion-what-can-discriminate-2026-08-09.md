---
title: "What can and cannot discriminate the generation carrier: the Spin(10) Casimir provably cannot, any internal-Clifford criterion provably cannot, and the only surviving discriminators are BASE-side — so 'generation carrier' is currently a base-rotation label"
artifact_type: exploration_result
created: 2026-08-09
status: CASIMIR_CRITERION_HAS_NO_SELECTIVE_POWER__INTERNAL_CLIFFORD_CRITERIA_PROVABLY_CANNOT_DISCRIMINATE__ONLY_BASE_SIDE_LABELS_SURVIVE__NEXT_TEST_IS_SCRAMBLING_THE_KREIN_AND_MASS_RESULTS
grade: "ANALYSIS of computed results from the 2026-08-09 fast sweep (6 agents, hostile-verified). No new
  computation run for this note. The named next test is specified but NOT executed."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# What can discriminate the carrier

## The problem

"The 192 is the pure `Spin(10)` generation spinor" is the sector's foundational identification. The sweep
showed the criterion used to establish it **has no selective power**: the `so(10)` Casimir is exactly a
scalar (`-90/8 = -11.25`) on the whole 128, has spread `0.00e+00` across the entire 512-dim
`(base-4) (x) 128` block, and **a random 192-dim subspace passes the identical test**.

So the carrier is currently **asserted**, not identified. What would identify it?

## Criteria that DO discriminate — all base-side

| criterion | separates | value |
|---|---|---|
| internal-vector weight | the two 192s **from** the 640s | `5e-30` vs `0.929` |
| joint `(Cas_+, Cas_-)` | the two 192s **from each other** | `(8,3)` vs `(3,8)` |
| `su(2)_+` Casimir | the 192 within `ker(Gamma)` | `8` (vs `0`, `3`) |

Every one of these is a property of the **base `so(4)`** action or of how the state sits relative to the
base/internal split. **None is an internal-Clifford statement.**

## Criteria that PROVABLY CANNOT discriminate

**Any criterion built from the internal Clifford structure.** The sweep destroyed all ten internal gammas —
internal anticommutator residual `16.35`, so the internal Clifford algebra is genuinely gone — and the
sector was unchanged: `ker` still 1664, split still `640/832/192`, `su(2)_+` closure still exact at
`7.43e-16`, the 192 still at `Cas = 8`.

**A quantity that survives the destruction of the algebra it is supposedly about cannot be a statement about
that algebra.** So no internal-`so(10)` invariant can single out the carrier. That is not a gap in the
search; it is a closed class.

Reinforcing: the whole split is reproduced **to the digit by `so(4)` branching arithmetic with zero Dirac
input** — `14 = 4+10`, `128 = 4_so(4) (x) 32_int`, tensor, remove one equivariant copy of the 128 ->
`64 triplets + 416 doublets + 640 singlets`.

## The consequence, stated plainly

**"Generation carrier" is at present a BASE-ROTATION label.** The 192 is distinguished by how it transforms
under `su(2)_+` and by having no internal-vector support — both facts about the `4 + 10` split, neither a
fact about generations. The `Spin(10)` content it carries is inherited block-wide and is shared with a random
subspace of the block, and with its own ASD mirror.

This does **not** show the carrier is the wrong object. It shows the reason for choosing it has not yet been
given.

## The next test — specified, not run

**Scramble-test the results that were NOT tested.** The sweep tested the Casimir identification and the
sector decomposition. It explicitly did **not** test:

- the Krein signature `(+96,-96,0)` and the totally-isotropic chirality halves;
- `{K, chir} = 0`;
- the carrier Dirac-mass results (vectorlike, `{+64, 0, -64}`, massive-decouples-to-zero).

**Run the internal-gamma scramble against those.** Two outcomes, both decisive:

- **They also survive** -> the entire generation sector is base-side, and every "generation" statement in the
  program is a statement about `so(4)` representation theory with the internal structure playing no role.
  That would be the largest single deflation the program has had.
- **They do NOT survive** -> those results have genuine internal Dirac content, and **the first
  discriminating criterion for the carrier has been found** — it is whichever of them breaks.

Either way it costs one script on an existing substrate, and it is the highest-leverage cheap test now
outstanding. Note the asymmetry: a null here is bad news for the program but good news for clarity, and a
break is the thing the sector actually needs.

## Honest scope

The `Spin(10)` identification is **true** — the 192 *is* a `16 + 16bar`. The finding is that this is true of
everything in the block, so it does not select. Nothing here touches the Krein, chirality, or mass results,
which remain untested under scramble and are exactly what the next test targets.
