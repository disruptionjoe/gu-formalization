---
title: "Pre-registration: the Spin(8)-triality omega-sector conditional — IF the source action yields a twisted-RS complex with a genuine diagonal order-3 symmetry, THEN a nonzero equivariant index in any omega-sector forces chirality"
artifact_type: preregistration
status: preregistration
created: 2026-08-09
lane: "1"
work_item: TRIALITY-OMEGA-CONDITIONAL
kill_conditions_declared_before_computation: true
mode: "CONDITIONAL PRE-REGISTRATION. The antecedent (a built source action) DOES NOT EXIST. Nothing here is
  computed, claimed, or forced. The whole point is that this is written BEFORE the gate opens."
directed_by: "Joe direct chat, 2026-08-09 (take swings 4 and 5)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
follows:
  - canon/anchored-leads-screen-RESULTS.md
  - canon/three-generations-locate-not-force-CRT-RESULTS.md
  - canon/exhaustiveness-by-type-RESULTS.md
  - canon/source-action-family-index-interface-SPEC.md
---

# Pre-registration: the Spin(8)-triality omega-sector conditional

## Why this exists, and why now

`canon/anchored-leads-screen-RESULTS.md` screened six heterodox routes to the generation count. Five died or
gated. One was marked the single standout and explicitly parked:

> Spin(8) triality is the one standout (a real NEW bridge TYPE — symmetry not pairing, type-correct
> equivariant integer that COULD force on the far side of the gate) but it too needs the twisted-RS complex;
> **hold it as the integer TOOL to deploy once the source action exists.**

**A tool held for later is a tool that will be applied after the target is known.** This repository has
caught itself fitting four times — the `24 = chi` import, the reverse-engineered `+8`, the circular rank-4,
the fitted holonomy. A conditional written *after* the source action exists carries far less evidential
weight than the same conditional written now, because the later one cannot be distinguished from a fit.

**So this document states the conditional, its antecedent, its consequent and its kill conditions before the
antecedent exists.** It costs one file and it permanently raises the value of whatever comes out of the gate.

## Why triality is type-correct where every other order-3 object is not

> "Triality is a SYMMETRY (order-3 outer automorphism), not a linking PAIRING, so it is not bound by the
> coprime linking-form / `Hom(Z/3,Z)=0` vanishing that decouples canonical `Z/8 <-> Z/3` maps. And an
> equivariant Lefschetz / representation-valued index is a type-correct INTEGER in `Z[omega]`, not a
> cardinal."

Every other order-3 object in the program dies on the cardinal-vs-torsion type wall (Jones fusion cardinal,
elliptic-genus coefficients, KM parameter count, 't Hooft homogeneity). Triality does not, because it is a
symmetry rather than a pairing and its index is representation-valued.

## The crux — why the standing "stranded" result does NOT kill this

Canon carries a strong negative on triality:

> "The internal-fiber order-3 of **Spin(8) triality**… sits in the `M(64,H)` coefficient/fiber factor…
> internal-fiber endomorphisms have tangent-frame charge exactly 0 … **frame-trivial and cannot feed the
> `-p_1/24` channel.**"

and, upgraded:

> "**a `Z/3` that COMMUTES with the Dirac operator gives a `g`-independent net equivariant index (net count
> = the `g=1` index), so it can only LABEL generations by family charge, never move the total**… SCOPE
> CAVEAT: proven for a `Z/3` placed internally (commuting with `D`); that GU so places the triality outer
> automorphism is reconstruction-tier."

**These kill two specific consequents, and the surviving lead is neither of them.** The stranding forbids
(a) *internal-fiber* realizations (`id_14 (x) M`, frame charge exactly 0), and (b) moving the **NET** count.

The lead that survives is:

- **(i) a DIAGONAL triality** — acting on tangent ⊗ fiber together, not internal-fiber only. Diagonal
  elements carry nonzero frame charge, from the tangent `SO(4)` factor. This evades (a).
- **(ii) the OMEGA-SECTOR decomposition of `ind_g`, not the net.** Chirality protection per `omega`-sector is
  fully compatible with a `g`-independent net. This evades (b).

**Those are exactly the two scope holes the exhaustiveness caveat leaves open, and they are the only two.**
Any future version of this conditional that drifts into an internal-fiber realization, or that claims to
move the net count, is **dead on arrival** and this document says so in advance.

## The conditional, stated

### Antecedent — property `P` the source action must supply

The source action `S_IG` yields a Fredholm/elliptic twisted Rarita-Schwinger complex on `Y14` such that:

- **P1** — `H^i` (ker/coker of `D_RS = E + E^dag`) exist and are computable.
- **P2** — an order-3 `g` realizing triality is a **genuine symmetry of that complex** (`[g, D_RS] = 0`),
  **not imposed by hand**. Imposition by hand is the probe's stated failure mode and is disqualifying.
- **P3** — `g` is **NOT** a pure internal-fiber endomorphism: its net self-dual **tangent-frame charge is
  nonzero** (evading `Tr(L^dag) Tr(Z) = 0`), so it feeds the gravitational `-p_1/24` channel.
- **P4** — any carrier Dirac mass admitted by `S_IG` is `g`-equivariant.

Interface obligations for the same object are already specified in
`canon/source-action-family-index-interface-SPEC.md` (vertical bundle + clutching over `GL(4,R)/O(3,1)`;
a-priori `Y14` boundary connection; family symbol; `ch2`/eta correction; `H`-line normalization), with the
hard bar **`N != 0 mod 3`**.

### Consequent — the integer `N`

```
N = ind_g = tr(g|ker) - tr(g|coker)   in  Z[omega],   decomposed into omega-sectors.
```

- **CONFIRM** — `N` is **nonzero in some `omega`-sector** ⇒ representation-valued chirality protection ⇒
  a `g`-equivariant mass provably cannot lift the `omega`, `omega^2` modes ⇒ **forced chirality**.
- **REFUTE** — `N` **vanishes in every sector** ⇒ triality is a type-correct integer **LABEL only**, and
  this route joins the other five as closed.

**The forcing mechanism is deformation-invariance, not a bound.** In a regular-rep toy configuration the
equivariant index is `-1`, stable across `m = 0 -> 100`. That toy value is **not** a prediction for the real
object and must never be cited as one — the only number currently in the repository for this lead.

## Declared kill conditions (before computation)

This conditional is **dead**, not merely weakened, if any of the following holds:

1. `P2` fails — no order-3 `g` commutes with the actual twisted-RS complex, so triality must be imposed by
   hand as an extra discrete family symmetry. (Standing negative: triality is **not** an inner automorphism
   of `Spin(9,5)`; `dim so(8) = 28 >> 6`; no `Spin(8)` commutes with `Spin(10)`.)
2. `P3` fails — every realization admitted by the built action is internal-fiber, frame charge 0. The
   stranding result then applies unchanged and this route is closed by existing canon.
3. `N` vanishes in **every** `omega`-sector on the real complex.
4. The `omega`-sector decomposition turns out not to be defined on the actual complex — e.g. the index is
   not representation-valued because the relevant spaces are not `g`-modules.
5. Any version of this argument is found to require the net count to move. That is forbidden by
   `canon/exhaustiveness-by-type-RESULTS.md` and is not a repairable defect.

## What this document does NOT claim

- **No claim that the antecedent will be satisfied.** The source action does not exist, and every prior
  attempt to build it performed none of the jobs it was built for.
- **No claim about the generation count.** The standing verdict is *located, not forced*, and it **tilts
  toward one**. Nothing here moves it.
- **No prediction of a value.** `N` is unspecified. The toy `-1` is a toy.
- **No claim of novelty for triality itself** — the lead is canon's, screened and graded GATED/maybe-build.
  What is new here is only that the conditional is written down **before** the gate opens.

## Success criterion for this pre-registration itself

Independent of whether the source action is ever built: this file succeeds if, on the day the antecedent is
tested, the test is run against **these** stated `P1`-`P4` and **these** kill conditions, and the outcome is
recorded against them without renegotiation. If the criteria are edited after the antecedent exists, this
document has failed and the resulting claim should be treated as a fit.
