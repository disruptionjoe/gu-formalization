---
artifact_type: exploration
status: exploration
created: 2026-07-29
lane: "1"
work_item: B5-INDEPENDENT-RECONSTRUCTION
title: "LAYER-0 PASS ON THE TWO 'HIGGS' OBJECTS: verdict HOMONYM AT 14D BOOKKEEPING WITH ONE NAMED, UNADJUDICATED BRIDGE. SA-Y1's Higgs is the Lambda^0 carrier -- dim Hom 1, OPPOSITE chirality, the Dirac-Yukawa mass channel. Weinstein's 'the Higgs is an illusion' object is the IG connection perturbation a in Omega^1(ad) -- which the SAME machine-checked channel table lists as Lambda^1, dim Hom 1, SAME chirality, explicitly 'not a Lorentz scalar'. Different rows of one table with different chirality structure, so Weinstein's mechanism does NOT satisfy SA-Y1 as stated. The bridge that could relate them is specific and computable: does a vertical (fibre-direction) vev of a, under the 14D -> 4D reduction where Lambda^1(V14) -> Lambda^1(V4) (+) ten 4D scalars and the spinors also decompose, convert the 14D same-chirality channel into a 4D opposite-chirality Dirac mass? Unadjudicated. Consequence: T10 is neither dropped nor confirmed; the bridge computation replaces it as the actionable item."
grade: "EXACT as a semantic adjudication against the machine-checked channel table (yukawa_trilinear_channels.py, 20/20). The bridge is NAMED and UNCOMPUTED -- Layer-0 UNCERTAIN is an open sub-task, not a free pass. No physics computed here."
protocol: "Layer-0 semantic-alignment precondition, lab/specifications/six-axis/six-axis-template.md (L1-L7 + Layer-0, ratified 2026-07-10)"
source: "papers/drafts/Transcript into the impossible.md lines 145-149; explorations/yukawa-scoping-2026-07-13.md channel table"
bears_on:
  - explorations/source-action-term-by-term-against-the-spec-2026-07-29.md
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
outcome: "HOMONYM-WITH-NAMED-BRIDGE"
---

# Layer-0 pass on the two "Higgs" objects

Run because Joe recalled a source claim that the Yukawa may not need deriving,
and because the new `AGENTS.md` directive requires Layer-0 *before* revising a
term, not after a result looks surprising.

## What the source actually says

Transcript, lines 145-149:

> **But there's no Higgs. The Higgs is an illusion.** If you look at the Yang
> Mills sector of the standard model versus the Higgs, it's almost exactly the
> same. They both have a Klein Gordon kinetic term. They both have a quartic
> term. You have that `a wedge a` in the perturbative expansion of a curvature
> tensor. So when you take its norm square, you get a quartic.
>
> If you take the norm square, you also get a term that looks like the
> unperturbed curvature, interproducted with `a wedge a`, which is a quadratic.
> **So if your curvature is negative, now you start to get a Mexican hat
> potential. Minimal coupling and Yukawa coupling are the same thing. The only
> thing that's really different is the spin.**

The mechanism is precise and sits entirely inside `T1`. With `A = A_0 + a`:

```text
||F_A||^2  =  ||d_{A_0} a||^2      kinetic
           +  2<F_{A_0}, a ^ a>    quadratic, SIGN SET BY BACKGROUND CURVATURE
           +  ||a ^ a||^2          quartic
```

Negative background curvature flips the quadratic's sign and produces a Mexican
hat with no separate Higgs field and no separate Higgs potential.

## The check

**Shared term: "Higgs."**

| | object denoted | channel-table row |
|---|---|---|
| `SA-Y1` | the `Lambda^0` carrier | dim Hom **1**, **OPPOSITE** chirality (`S+ x S-`) — the Dirac-Yukawa mass channel |
| Weinstein | the IG connection perturbation `a in Omega^1(ad)` | `Lambda^1` (vector, 14): dim Hom **1**, **SAME** chirality, explicitly *"not a Lorentz scalar"* |

Both rows are in the **same machine-checked table**
(`yukawa-scoping-2026-07-13.md`, `yukawa_trilinear_channels.py`, 20/20), which
decomposes `End(S)` exactly as `(+)_k Lambda^k(V_14)` with the checksum
`sum_k C(14,k) = 16384 = 128^2`, zero residuals.

**Verdict: `HOMONYM` at 14D bookkeeping.** They are different rows with
different chirality structure. **Weinstein's mechanism does not satisfy `SA-Y1`
as stated** — a `Lambda^1`, same-chirality channel is not the cross-chirality
Dirac mass channel.

## The bridge, named and unadjudicated

This is not the end of it, because the two objects are stated at different
scopes and one specific reduction could relate them.

Under `14D -> 4D`, `Lambda^1(V_14)` decomposes as `Lambda^1(V_4)` plus **ten 4D
scalars** — the fibre-direction components. A vev of `a` in those vertical
directions is a **4D scalar** even though it is a 14D 1-form. And 4D chirality
is not 14D chirality: the spinors decompose too under the same reduction.

> **The bridge question:** does a vertical vev of `a`, under the `14D -> 4D`
> reduction of both `Lambda^1(V_14)` and the spinor module, convert the 14D
> same-chirality `Lambda^1` channel into a 4D opposite-chirality Dirac mass
> channel?

If **yes**, Weinstein is right, `SA-Y1` is satisfied by `T1` + `T2` already
written, and `T10` should never be written. If **no**, `SA-Y1` stands as a
genuine unmet FORCED row and `T10` is required.

Layer-0 records this as **UNCERTAIN** — an open sub-task, not a free pass.

## Consequences for the term-by-term pass

- **`T10` is neither dropped nor confirmed.** The bridge computation replaces it
  as the actionable item. Writing `T10` now would risk building a term the
  theory calls an illusion; deleting it now would risk discarding a FORCED row
  that still bites.
- **A new demand surfaces.** *"If your curvature is negative"* is a **condition
  on the background**, not a free choice. Something must supply or declare the
  sign of `F_{A_0}`. That is a requirement-row-shaped obligation with no current
  row, and it is unclear whether it is FORCED, DECLARATION, or FIT.
- **`D1` changes character.** If the Higgs is the connection perturbation, then
  "the Yukawa texture" is a statement about how `a`'s vev structure grades the
  fermion blocks — a different computation from the one `SA-Y4` currently
  encodes.

## Why this pass was worth running

Both available shortcuts were wrong. "Joe is right, drop `T10`" would have
discarded a FORCED row on a mechanism that occupies a different channel. "No,
`T10` stands" would have ignored an explicit source claim that the object is an
illusion. The protocol produced a third answer — same role, different channel,
one named reduction that decides it — which neither shortcut would have reached.

Nothing moved: no claim, canon, verdict, count, priority, or posture.
