---
artifact_type: exploration
status: exploration
doc_type: source-mechanism-obstruction-gate
created: 2026-08-14
work_item: SRC-3
channel: majorana_126_neutrino_mechanism
title: "SRC-3: the source's Mexican-hat potential is UNBOUNDED BELOW, from two independent causes. The quartic ||a^a||^2 is built from the unique Ad-invariant pairing (Killing, CC-1), which PV-2 showed is indefinite on so(6,4), and independently from the internal DeWitt metric of signature (6,4) which is intrinsic to Y14 = Met(X4). An explicit k-valued ray gives K = -4 < 0. Restricting to k does NOT restore boundedness, because the internal-metric source survives."
grade: "EXACT integer arithmetic, 16/16, with PV-2's Killing signature re-verified as a live control. CONDITIONAL on the load-bearing assumption that the norm-square uses the Ad-invariant pairing on ad and the DeWitt metric on internal form indices; SG4 leaves the actual quadratic form undeclared. NOT a falsification of GU, and not a claim about GU's full action."
disposition: POTENTIAL_UNBOUNDED_BELOW_ON_AN_EXPLICIT_RAY__TWO_INDEPENDENT_INDEFINITENESS_SOURCES__NO_AD_INVARIANT_REPAIR_EXISTS__INTERNAL_METRIC_SOURCE_IS_GEOMETRIC_AND_NOT_A_CHOICE__CONDITIONAL_ON_THE_UNDECLARED_NORM
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/majorana-126-neutrino/src2-mexican-hat-is-automatic-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/src1-source-steelman-of-the-vev-2026-08-14.md
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md
  - lab/active-research/joe-directed/cosmological-constant-sign/
  - canon/shiab-existence-cl95.md
scripts:
  - tests/channel-swings/joe_directed_potential_boundedness_probe.py
---

# SRC-3 — the potential is unbounded below

## The question

SRC-2 showed Eric's Mexican hat is automatic: the cross-term mass form is
exactly traceless, so a tachyonic direction exists for any nonzero background
curvature. A Mexican hat is only a Mexican hat if the quartic stabilises it.
Along a ray `a = t v`,

```text
V(t v) = t^2 Q(v) + t^4 K(v),    K(v) = || v ^ v ||^2,
```

so the mechanism survives iff `K(v) > 0` wherever `Q(v) < 0`.

## Result

> **`K` is not positive. An explicit `k`-valued ray gives `K = -4 < 0`, so
> `V(t v) -> -infinity` regardless of `Q`. The potential is unbounded below.**

The construction is elementary and exact: take `X` and `Y` in the `so(6)` block
(both in `k`), place them on two spacelike internal directions. Then
`(v^v) = [X,Y]`, which lands back in `k` because `[k,k]` is contained in `k`,
and the Killing form is **negative** there. So the quartic is negative.

**There are two independent sources, and this matters for repair.**

1. **The ad pairing.** CC-1 established that `so(6,4)` admits an Ad-invariant
   bilinear form space of dimension exactly **one** — the Killing form. PV-2
   established that form is negative on all 21 directions of `k` and positive on
   all 24 of `p`. So the unique *gauge-invariant* choice is indefinite, and
   **no Ad-invariant repair exists**. Any positive-definite alternative breaks
   Ad-invariance, which is not a small price in a gauge theory.
2. **The internal metric.** The internal 10 is `Sym^2(T*X4)` with DeWitt
   signature `(6,4)` — derived in `canon/shiab-existence-cl95.md` from the
   trace-reversed Frobenius metric, and therefore **intrinsic to GU's own
   construction of `Y14 = Met(X4)`, not a choice of pairing.** Putting one leg
   on a timelike internal direction flips the sign of the very same bracket:
   the probe exhibits `-4` and `+4` from one bracket, differing only in which
   internal direction the second leg occupies.

**Restricting to `k` does not fix it.** On branch B — the algebra available if
the wrong-sign `p` sector is disposed of, which is PV-2's open quantization
question — `-B` is positive definite on `k` and brackets of `k` elements stay in
`k`, so the ad-side is repaired. **But the internal-metric source survives**, and
the quartic goes negative again with one timelike internal leg. Ghost disposal
is not sufficient.

**Flat directions exist too.** 630 abelian generator pairs give `K = 0`
identically. On any such direction with `Q < 0` the potential runs away already
at quadratic order, with no quartic to stabilise it.

## What this does and does not say

**Conditional, and the condition is named.** This assumes the norm-square uses
the Ad-invariant pairing on `ad` and the DeWitt metric on internal form indices.
Eric says "when you take its norm square", so a norm-square is invoked, but
**SG4 leaves the actual quadratic form undeclared**, and GU's action is the
Shiab / Einstein-replacement construction rather than textbook Yang-Mills. If
SG4 declares a different pairing, source 1 is escapable — at the cost of
Ad-invariance. Source 2 is harder, because the `(6,4)` signature is geometric.

**This is not a falsification of GU.** It is a constraint on what SG4 can
declare, and it is the sharpest one this session has produced, because it bites
on the source's *own* stated mechanism rather than on an imported one.

**Not claimed:** anything about GU's full action, about whether a stabilising
higher-order term exists, about the physical state space, or about the
disposition of the `p` sector, which remains `W173`/`W132` property.

## Standing of the source mechanism after SRC-1..SRC-3

- **SRC-1**: the mechanism is *no Higgs* — curvature-induced Mexican hat in the
  ad-valued one-form, with minimal coupling doubling as Yukawa coupling.
- **SRC-2**: the Mexican hat is **automatic**, needing no sign condition at all,
  which is stronger than the source claims. But it is unselective and leaves the
  symmetric point unstable everywhere.
- **SRC-3**: the resulting potential is **unbounded below** on an explicit ray,
  with no Ad-invariant repair, and one of the two causes is geometric.

Composed: the source mechanism generates symmetry breaking too easily and
cannot obviously be stabilised. That is a materially different — and more
interesting — difficulty than the one the MJ/PV/BD/SG4 arc found, and it is
aimed at the claim the source actually makes.

## Next gate

SRC-4: does GU's *actual* action rescue this? The natural candidates are the
eddy / Chern-Simons quadratic completion the source insists on (the primary
reinspection records that "the bare Shiab-curvature is not exact without the
eddy completion"), and any higher-order term that could bound the runaway.
That gate needs the action itself, which is SG4/Lane 1 property and not this
channel's — so this is the point at which the channel's own resources run out.

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface moves.
