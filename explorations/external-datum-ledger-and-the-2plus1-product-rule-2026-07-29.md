---
artifact_type: exploration
status: exploration
created: 2026-07-29
lane: "1"
work_item: B5-INDEPENDENT-RECONSTRUCTION
title: "EXTERNAL DATUM LEDGER: the missing pieces reduce from THREE to TWO. Weinstein's '2+1 with an imposter' is an exact consequence of the GAMMA-TRACELESS Rarita-Schwinger product rule over a declared split. With RS(V) = V(x)S(V) - S(V), the two Leibniz terms RS(V)(x)S(W) + S(V)(x)RS(W) subtract TWO copies of S(V)(x)S(W) while RS(V(+)W) subtracts ONE, so they differ by exactly one S(V)(x)S(W) -- the third family. Verified by exact dimension count on every even/even split incl. GU's base+fibre 4+10. The isolating control is decisive: the TRACEFUL rule has only two terms and NO third family, so the third generation comes precisely from gamma-tracelessness. Consequence: the generation count needs NO external Z/3 carrier integer. Ledger: P1 (a Z/2 orientation, serving both the six B5 chirality orbits and the Rung-2 wall) and P2 (the X-sector datum, type unknown) remain; P3 is WITHDRAWN as external."
grade: "EXACT dimension counting on the stated splits, with all controls passing including a planted wrong-subtraction kill and a documented odd/odd scope exception. NOT a representation-theoretic proof: multiplicities work out and the third term is shown not to be of Leibniz form, but internal quantum numbers are NOT checked, the split is NOT shown to be forced, and 2+1 is NOT shown to be phenomenologically three. Those are separate and open."
probe: tests/channel-swings/external_datum_ledger_probe.py
follows:
  - explorations/b5-chirality-orientation-audit-2026-07-29.md
  - explorations/rung1-finite-coefficient-enumeration-2026-07-29.md
  - explorations/prereg-rung2-dynamical-wall-and-selectability-test-2026-07-29.md
source: "papers/drafts/Transcript into the impossible.md (in-repo), Joe-directed 2026-07-29"
construction: "program-native: the gamma-traceless ker-Gamma RS carrier is GU's own commitment, not a standard-field substitution."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
outcome: "P3-IS-NOT-EXTERNAL"
---

# The external datum ledger, and the 2+1 product rule

## Why this exists

Rather than repeatedly concluding "an external datum is needed" and stopping —
which is the orthodox reflex this repo now carries a standing note against — this
run **cuts the missing pieces to fit** and reports their shape and count. We do
not claim to have found them. We claim to have learned what they must look like.

## What Weinstein actually said

From the in-repo transcript:

> which will yield you three families, really **two plus one**. The third family
> is an **imposter for representation theoretic reasons**, but at low energy,
> it'll look the same as the other two.

and the mechanism:

> there's this extra term where it's like, Rarita `V` tensor spinors on `W`,
> spinors on `V` tensor Rarita Schwinger on `W` … plus spinors on `V` tensor
> spinors on `W`. So that's where you get your **third generation of matter**
> from.

## The computation

With the **gamma-traceless** Rarita-Schwinger carrier, `RS(V) = V (x) S(V) - S(V)`:

- `RS(V)(x)S(W) + S(V)(x)RS(W)` subtracts **two** copies of `S(V)(x)S(W)`
- `RS(V (+) W)` subtracts **one**

so the two differ by exactly one `S(V)(x)S(W)`:

```text
RS(V (+) W)  =  RS(V)(x)S(W)  +  S(V)(x)RS(W)  +  S(V)(x)S(W)
                \____________Leibniz___________/    \__extra__/
```

Verified by exact dimension count on every even/even split tested, including
GU's base+fibre split `4 + 10`, where the terms are `384 + 1152 + 128 = 1664`
— and `1664` is exactly `dim ker Gamma`.

## The isolating control, which is the decisive one

The **traceful** vector-spinor `V (x) S(V)` obeys a clean two-term Leibniz rule
with **no extra term at all**. So:

> The third family comes **precisely** from gamma-tracelessness. Remove the
> gamma-trace constraint and the third generation vanishes.

That also explains "imposter" mechanically: terms 1 and 2 are Leibniz partners
of the same kind, while term 3 is a correction of a different kind. It carries
the same internal quantum numbers at low energy while not being a partner —
which is what Weinstein says, and it **predicts the third family behaves
differently at high energy**. That is a discriminator, not a free pass.

## Scope condition found by a control

The first run **failed** its own control on `(3,11)` and `(9,5)`. Both are
**odd (+) odd** splits, where the ungraded spinor exponential property breaks by
exactly a factor of two because of the odd Clifford algebra's central element.
That is a known fact, and the controls forced it to be stated as an explicit
scope condition rather than discovered later as an error. GU's relevant split is
base+fibre `4+10`, which is even/even, so the result applies — but the exception
is carried openly and the odd/odd pairs are excluded by name, not silently.

## The ledger

| piece | type | status |
|---|---|---|
| **P1** | a `Z/2` orientation | **needed** — serves the six B5 chirality orbits **and** the Rung-2 wall orientation; one piece, two slots |
| **P2** | the X-sector datum | **needed** — four B5 orbits, blind to every ledger invariant and not reached by `P1`; type still unknown |
| **P3** | a `Z/3` carrier integer | **WITHDRAWN** — forced by the declared split plus gamma-tracelessness |

**Three pieces became two.** And `P1` does double duty across two slots that
looked unrelated, which is evidence the picture is tighter than a
free-parameter count suggests.

## What this does to the CRT framing

GU's own canon already grades the order-3-class to integer-3 step as *"open and
possibly a category error."* This supports that worry from the other side: if
the count is `2+1` from a product rule, **no `Z/3` torsion class is needed**, and
`Hom(Z/3, Z) = 0` was answering a question the structure does not ask.

That does not overturn the CRT results, which stand on their own arena
arithmetic. It relocates them: they constrain a torsion route the count may
simply not take.

## Honest limits

Dimension counting is not representation theory. This shows the multiplicities
work out exactly and that the third term is not of Leibniz form. It does **not**
show the three factors carry the right internal quantum numbers, does **not**
show the split `V (+) W` is itself forced rather than declared, and does **not**
show that `2+1` is phenomenologically three. Each is separate and open.

## Next

The sharpest remaining question is now **P2**: what class of datum fixes the four
X-sector signs? It is not a ledger invariant and not the chirality `Z/2`. If `P2`
also turns out to be forced by something already declared, the picture closes on
**one** external piece — which would be the strongest coherence result available.
