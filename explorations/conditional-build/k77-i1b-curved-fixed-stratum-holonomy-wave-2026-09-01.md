---
title: "K77 I1B curved fixed-stratum holonomy wave"
status: active_research
doc_type: reverse_scaffold_i1b_supplied_curved_holonomy_result
date: 2026-09-01
claim_ceiling: exact curved rank-24 quotient connection and hyperbolic rectangular-loop holonomy for one supplied timelike fixed-stratum geometry; no complete I1B Hessian connection, physical quotient, prediction, confirmation, or verdict
manifest: lab/process/k77-i1b-curved-fixed-stratum-holonomy-wave.json
probe: tests/channel-swings/k77_i1b_curved_fixed_stratum_holonomy_probe.py
---

# K77 I1B curved fixed-stratum holonomy wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: supplied curved I1B fixed-stratum quotient connection with computed hyperbolic rectangular-loop holonomy
carrier: native rank-220 I1B timelike fibre modulo its rank-196 radical, yielding a real rank-24 Darboux Green quotient LAYER=conditional CHIRALITY=N/A
pairing: descended nondegenerate alternating Green form ON=timelike_fixed_rank_quotient
real_structure: real I1B fluctuation carrier in one supplied local Darboux trivialization
grading: N/A; no physical gauge or BV quotient is asserted
action_owner: native I1B packet supplies the fibre and Green quotient dimensions; the connection, rectangle and trivialization are supplied conditional geometry, not the complete variable-coefficient I1B Hessian connection
target: fixed-stratum curvature, loop holonomy and invariant-majorant discriminator MAP-TYPE=construction
```

## Construction

Work on one local timelike fixed-rank patch. In a Darboux trivialization of the
native rank-24 quotient `Q`, write its Green form as

```text
J = [[0,I12],[-I12,0]].
```

The hyperbolic generator

```text
H = diag(I12,-I12)
```

lies in `sp(24,R)`. Supply the connection on the unit `x,y` rectangle

```text
nabla = d + log(2) x H dy.
```

Its curvature is nonzero:

```text
F_nabla = log(2) H dx wedge dy.
```

Lift the connection trivially over the native rank-196 radical. The radical is
then parallel, so transport descends representative-independently to `Q` and
preserves the alternating Green form.

Every connection value is a scalar multiple of `H`, so path ordering is
Abelian. Around the positively oriented rectangular boundary,
`integral x dy = 1`, and the parallel-transport convention gives

```text
Hol(gamma) = exp(-log(2) H)
           = diag((1/2)I12,2I12).
```

This is computed from the connection rather than inserted as a monodromy
matrix. It is semisimple symplectic and hyperbolic, with characteristic
polynomial `(lambda-1/2)^12(lambda-2)^12`, minimal polynomial
`(lambda-1/2)(lambda-2)`, determinant one and 24 size-one Jordan blocks.

No positive majorant can be invariant. If `v` is a nonzero half-eigenvector
and `g` were positive with `M^T g M=g`, then

```text
g(v,v) = g(Mv,Mv) = (1/4) g(v,v),
```

a contradiction. The exact probe passes `16/16`; its hostile selftest catches
`12/12` mutations, including nonsymplectic generator, zero curvature, wrong
holonomy, rank drift and ownership promotion.

## What advanced

The predecessor computed identity holonomy on a supplied flat compactification.
This result constructs the first explicitly curved connection and first
nontrivial holonomy in the new fixed-stratum quotient line. It also turns the
earlier supplied-matrix majorant discriminator into an actual
connection-to-curvature-to-loop calculation: this connection's computed
transport lies on the hyperbolic no-majorant side.

## Boundary and next condition

The connection is compatible with the native fixed-stratum Green quotient but
is supplied on that quotient. It is not derived from the complete
variable-coefficient `I1B` coupled Hessian, whose evaluator, radical/gauge
basicness, common closed domain and Green/parametrix equivalence remain absent.
It does not show that the source selects this rectangle, connection or
curvature, and it does not extend through the rank-24/rank-22 null jump.

The next honest reopener is one action-owned complete curved `I1B` connection
or reduction evaluator on a named domain. Its induced quotient connection and
loops must be computed and compared with this exact hyperbolic control. A
different source-owned connection may have compact holonomy and preserve a
majorant; the present construction neither selects nor excludes that route.
