---
title: "B5 strict BV action bridge: a nonempty full-nine family and a current-witness route split"
status: active_research
doc_type: exact_action_bv_bridge
created: "2026-08-20"
registry: lab/process/b5-strict-bv-action-bridge.json
probes:
  - tests/channel-swings/b5_strict_bv_action_bridge_probe.py
grade: "AT THE INDEPENDENT B5 FORMAL COMPACT-CORE AND COARSE MULTIPLICITY GRADE, THE STRICT 1->2->2->1 CONTROL HAS AN EXACT QUADRATIC ABELIAN BV/KOSZUL-TATE ACTION. ITS CANONICAL ANTIBRACKET GIVES THE GENUINE MASTER-EQUATION CONDITION K A=0, WHICH IS INDEPENDENT OF HESSIAN SYMMETRY. NORMALIZED Q=1 FIXES THE SELF-DUAL STRICT MIDDLE MAP, AND A TWO-PARAMETER FULL-NINE EULER FAMILY WITH LIVE S->S EXTENDS IT WHILE OBEYING THE SAME STRICT GENERATOR. THE CURRENT STAGE-B HESSIAN WITNESS IS NOT IN THAT FAMILY: IT CLOSES ONLY FOR A GRAPH-MIXING GENERATOR WITH NONZERO S COMPONENT. THE NATIVE FULL-RANK LIFT, MULTIPLICITY GRAM, COFLIP AND DOMAIN REMAIN OPEN."
target_verdict: B5_STRICT_BV_ACTION_FAMILY_EXISTS_CURRENT_H9_REQUIRES_GRAPH_MIXING
target_claim: internal target B5-STRICT-DIFFERENTIAL-ACTION-BRIDGE; verdict exact coarse bridge constructed and current H9 excluded from the strict-generator branch but not from filtered graph actions
canon_verdict_change: none
---

# B5 strict BV action bridge

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds the independent B5 formal compact-core coarse
`S + imGamma + kerGamma` bookkeeping only. It constructs a finite-dimensional
quadratic abelian BV/Koszul--Tate bridge for the strict complex and an exact
full-nine Euler extension. It does not construct the actual
`128 -> 1792 -> 1792 -> 128` maps, the native `Cl(9,5)` multiplicity Gram,
nonlinear/source BV data, a coflip, Green form, domain, quotient, historical
preferred Shiab, particle result or GU verdict.

```gu-typed-objects
result: an exact coarse strict BV action family exists; the current full-nine H9 witness instead requires graph mixing
carrier: strict U0=S, U1=I+R, U2=(I+R)^vee_dens, U3=S^vee_dens plus one gauge-inert S Euler spectator LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: canonical stage evaluation for the strict BV bridge; native S/imGamma multiplicity Gram remains EXTERNAL-VIA-GRAM ON=formal-compact-core
real_structure: rational complex-linear control; native Lorentzian real structure and coflip remain UNTYPED
grading: abelian BV ghost/field/antifield/Noether-dual grading realizing the strict four-stage chain
action_owner: repository-construction quadratic BV/Koszul-Tate action; nonlinear source action remains unowned
target: strict-generator classical master equation, Euler extension and current-H9 compatibility MAP-TYPE=evaluation
```

## Result first

The missing action bridge is nonempty at exact coarse grade. Put

```text
A = (1,1)^T,
K = (6/7) [[1,-1],[-1,1]],
A^T = (1,1).
```

For fields `x in I+R`, ghost `c in S` and antifields `x*`, use the minimal
abelian BV action

```text
S_BV = 1/2 x^T K x + x*^T A c.
```

With the canonical field/antifield antibracket,

```text
(S_BV,S_BV) = 2 x^T K A c.
```

Thus the classical master equation is exactly `K A=0`. This is also the
Noether identity needed for the strict arrows

```text
S --A--> I+R --K--> (I+R)^vee_dens --A^T--> S^vee_dens.
```

The arrows have ranks `(1,1,1)` and the coarse complex is exact. Its folded
operator has all eight eligible blocks nonzero, structural `SS=0`, normalized
W131 `q=1`, and is self-adjoint for the declared canonical stage evaluation.
This supplies a real action owner and a real master-equation condition rather
than renaming `H^T=H`.

## Where the separate `a D_S` term goes

Embed the strict generator in the folded Euler carrier as

```text
A_strict = (0,1,1)^T
```

and add one gauge-inert `S` Euler spectator. The complete symmetric
strict-compatible Hessian family is

```text
             [[ a,    t,   -t ],
H(a,t) =      [ t,   6/7, -6/7],
              [-t,  -6/7,  6/7]].
```

For every `a,t`, `H(a,t) A_strict=0`; for generic nonzero `a,t` it has full
nine-entry support, live `SS=a`, and rank two. Hence the separate `a D_S`
term can live in a quadratic Euler action without entering the strict
differential and without violating the coarse classical master equation.

This is a construction, but not a normalization theorem. The CME leaves both
`a` and `t` free. In particular `a=0` and `a!=0` members obey the same master
equation. The native multiplicity Gram is not the canonical cotangent pairing
used here and remains unselected.

## The current `H9` witness chooses the other route

The current Stage-B witness is

```text
H_current = (13/735)(u u^T + v v^T),
u=(1,2,3), v=(4,5,6).
```

It is symmetric, rank two, and full-nine, but

```text
H_current (0,1,1)^T != 0.
```

Therefore it fails the strict-generator CME. Its exact kernel is instead

```text
r_graph = (1,-2,1)^T,
```

which has a live `S` component. At this grade the current witness can be
action-owned only by the alternative graph-mixing generator, not by the
strict stage-preserving generator. This is a route discriminator, not a
no-go for filtered field/antifield actions.

## Preflight and route selection

The work searched the existing B5 five-field packet, four-stage support,
Euler separation, Stage-B normalization, full-nine Gram and minimal
source-action toy by mechanism and exact numbers before execution. No prior
artifact contained this strict-compatible `H(a,t)` family or tested
`H_current` against `A_strict`.

The route council compared homological, variational/BV, Hodge/Krein,
representation-support, exact-computation, source-custody and hostile-scope
routes. Canonical abelian BV was selected because it exposes the polynomial
CME directly. A broad coefficient search was rejected as dominated: symmetry
and `H A=0` solve the family structurally. The fallback is the graph-mixing
route, triggered exactly by `H_current A_strict != 0` and witnessed by
`H_current r_graph=0`. Computation is a final exact certificate, not a scout.

## Postflight and hostile checks

The exact probe passes `29/29` with `fractions.Fraction`. Planted controls
show that a symmetric Hessian can fail the CME and break nilpotence. A second
family member proves the bridge is not a fitted point; an `a=0` member proves
the CME does not normalize the Dirac coefficient. The current witness is
replayed exactly and its strict failure and graph-kernel closure are both
certified.

The strongest overclaim is that an exact coarse BV action supplies the native
full-rank action. It does not. The strongest contrary route survives: a
filtered graph embedding may own the current `H9`. The weakest propagation
seam is the pairing homonym; `SELF` here means only canonical coarse stage
evaluation, not the native multiplicity Gram.

## Packet consequence and exact next owner

`B5-STRICT-DIFFERENTIAL-ACTION-BRIDGE` is constructed at coarse grade, but the
five-field packet remains fail-closed. Its strict field (iii) now has the
conditional value `SELF-CANONICAL-COARSE`; the native full-20 formal-adjoint
field remains open, while the current Euler family's field (iii) remains
`EXTERNAL-VIA-GRAM`.

The smallest next gate is `B5-NATIVE-BV-HESSIAN-LIFT`: lift `A`, `K`, `A^T`
and the relations defining `H(a,t)` to the actual 20-slot
`128/1792/1792/128` carrier with representation-natural blocks and a declared
native Krein pairing, or prove the lift empty. Only that lift can decide
whether the strict action branch reaches the native coefficient family and
whether coflip/domain work has an assembled operator to consume.
