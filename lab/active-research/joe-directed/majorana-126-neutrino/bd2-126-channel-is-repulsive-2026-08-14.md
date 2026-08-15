---
artifact_type: exploration
status: exploration
doc_type: condensate-channel-force-gate
created: 2026-08-14
work_item: BD-2
channel: majorana_126_neutrino_mechanism
title: "BD-2: the 126 channel is REPULSIVE. Delta C2 = (+54, +6, -10) on (10, 120, 126) exactly, so the most attractive channel is the Dirac 10 and the 126 cannot condense at any coupling. The ghost-like p sector contributes EXACTLY ZERO to the 126, so its disposal cannot flip the verdict. Also corrects MJ-4's scope: the source places the spin-zero component in the adjoint-valued ONE-FORM, whose content 10 (x) 45 DOES meet 16 (x) 16 -- via the Dirac 10, which cannot make nu_R Majorana."
grade: "EXACT integer/rational computation of the channel force at one-gauge-boson-exchange (MAC) grade, 29/29. Cross-checked against two independent prior computations: hand Casimir arithmetic and MJ-3's Fierz row. NOT: a critical-coupling calculation, a non-perturbative statement, a source action, or any claim-status movement."
disposition: 126_CHANNEL_REPULSIVE_AT_ONE_BOSON_EXCHANGE__DIRAC_10_IS_THE_MOST_ATTRACTIVE_CHANNEL__P_SECTOR_CONTRIBUTES_ZERO__CONDENSATE_ESCAPE_CLOSED_AT_MAC_GRADE__MJ4_SCOPE_CORRECTED_TO_EPS_ONLY
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/majorana-126-neutrino/mj1-exact-126-majorana-block-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj3-4-source-vev-channel-and-twenty-lens-hypothesis-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md
  - lab/active-research/joe-directed/baryon-number-and-proton-decay/
  - explorations/weinstein-primary-source-reinspection-overlooked-answers-2026-07-30.md
scripts:
  - tests/channel-swings/joe_directed_condensate_mac_probe.py
---

# BD-2 — the 126 channel is repulsive

## The question

MJ-2, MJ-4 and MJ-5 closed the *explicit* route to a `nu_R` Majorana mass: no
carrier field, and `B-L` symmetry-forbidden. One escape survived — a
**condensate**, `<nu nu>` in the 126 channel, which needs no `B-L`-charged
elementary field because it would break `B-L` *spontaneously*. MJ-3 banked
`F[45][126] = -5/32`, showing gauge exchange **reaches** the channel.

Reaching a channel is not condensing in it. The decidable question is the
**sign of the channel force**, and it is exactly decidable: a **repulsive
channel never condenses at any coupling**. So no critical-coupling estimate and
no SG4 declaration is needed — which is why this gate is exact where I
previously expected it could not be.

## Result

With `Delta C2(R) = 2 C2(16) - C2(R)` (attractive iff positive):

| channel | `Delta C2` | verdict |
|---|---:|---|
| **10** (Dirac) | **+54** | **most attractive** |
| 120 | +6 | attractive |
| **126** (Majorana) | **-10** | **REPULSIVE** |

> **The 126 channel is repulsive, and the most attractive channel is the Dirac
> 10.** GU's own gauge dynamics prefers Dirac mass and disfavours the Majorana
> channel.

**Triple cross-check.** These are `8x` the hand Casimir values
`(27/4, 3/4, -5/4)` computed independently from `C2(Lambda^k) = k(N-k)/2`, and
their signs match MJ-3's independently computed Fierz row
`F[45][.] = [27/16, 3/16, -5/32]`. The 10 and 120 share one proportionality
constant with that row and the **126 differs from it by exactly the factor 2
expected from the self-dual projection `Lambda^5 = 126 + 126bar`** — three
independent routes agreeing, including on the anomalous-looking factor.

**The p-sector escape closes too, and more cleanly than expected.** PV-2 showed
the Killing form is negative on `k` and positive on `p`, so wrong-sign `p`
exchange could in principle flip a repulsive channel. It cannot: **the `p`
sector contributes exactly zero** to the 126 channel, and the whole repulsion
`-10` is carried by the physical `k` sector. So the verdict survives *any*
disposition of the ghost-like `p` summand, which is the open quantization
question PV-2 deliberately left to `W173`/`W132`. That independence is worth
more than the sign itself.

## Source-fidelity correction to MJ-4's scope

Reading the primary-source record rather than the derived layer changed
something, and MJ-4 must be narrowed accordingly.

`explorations/weinstein-primary-source-reinspection-overlooked-answers-2026-07-30.md`
records that the draft **"places a true-spin-zero component inside the
adjoint-valued one-form/gauge potential and links its VEV simultaneously to
fermion mass and the cosmological sector."**

That is `$` (`Omega^1 (x) ad`), **not** `eps` (`Omega^0 (x) ad`). The two have
different Lorentz-scalar internal content: `eps` gives `Lambda^2(10) = 45`,
while `$` gives `10 (x) 45 = 10 + 120 + 320`. MJ-4 showed the whole even tower
`{1,45,210}` is absent from `16 (x) 16` — correct, and it kills the direct
reading **for `eps`**. But the 10 and the 120 **do** meet `16 (x) 16`.

> **MJ-4's kill is correctly scoped to `eps` and does NOT kill the source's
> three-way link under the adjoint-valued one-form reading.**

This does not rescue the Majorana route; it sharpens the Dirac one. The channel
`$` feeds is the **Dirac 10**, whose `(nu_R, nu_R)` entry MJ-4 showed vanishes
identically over every direction. So the source's own mass channel gives Dirac
mass and **cannot** make `nu_R` Majorana — and BD-2 now adds that the same
channel is the most attractive one dynamically.

Note that a related fork was dispositioned differently, and correctly, for a
different question: the CC-1 analysis found the `eps`-versus-`$` fork
*indifferent* because both land in the same internal carrier `ad` for a
Killing-form argument on the adjoint. That is right there and wrong here — the
Lorentz-scalar *content* differs even though the carrier does not.

## Claim ceiling

**One-gauge-boson-exchange (MAC) grade.** The channel force is computed exactly
at that grade; the group theory is exact and the sign is not an estimate. But
MAC is a standard *approximate* dynamical criterion. Multi-boson exchange or
genuinely non-perturbative dynamics are not covered, and this artifact does not
claim condensation is impossible in principle — it claims the channel is
repulsive under the exchange GU actually has.

**Not claimed:** any critical coupling; any statement about the 10 channel
actually condensing (attractive is necessary, not sufficient); any value for a
mass; any movement of SG4, which remains the open decider on field space.

## Standing after BD-2

- **H-CONDENSATE: closed at MAC grade.** The last escape from the explicit-route
  closure is repulsive, and the escape's own escape (the `p` sector) contributes
  zero.
- **H-DIRAC: strengthened twice over.** It is symmetry-protected (MJ-5),
  dynamically preferred (BD-2: the 10 is the most attractive channel), and
  matches the source's own mass channel under the corrected `$` reading.
- **The baryogenesis obstruction becomes permanent for GU-as-declared**, since
  BD-1's escape was the same condensate.

Falsifier unchanged and still live: observation of neutrinoless double beta
decay would falsify the whole composed picture.

## Next gate

The composed negative now rests on one unexamined joint: everything above is
`GU-as-declared`, and canon makes SG4 the open decider. The honest next gate is
not another channel but **SG4 itself** — what minimal field-space declaration
would simultaneously supply a `B-L`-charged SM singlet, give the nine surviving
gauge bosons mass, and restore baryogenesis? BD-1 already showed one object
(the 126) does all three. That is a constraint on SG4 worth stating precisely.

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface moves.
