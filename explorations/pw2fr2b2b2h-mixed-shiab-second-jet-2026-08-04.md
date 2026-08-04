---
title: "PW2F-R2B2B2H exact mixed trace/Phi/Hodge/Shiab operator jet"
status: active_research
doc_type: exploration
created: "2026-08-04"
run_id: RUN-20260804-052005-gu-formalization-pw2fr2b2b2h-mixed-shiab-second-jet
---

# PW2F-R2B2B2H exact mixed Shiab operator jet

## Earned result

The conditional active nonlinear-Zorro branch now has an exact sparse
`(1,r,s,rs)` operator jet for the normalized trace, moving Clifford `Phi1` and
`Phi2`, full density/inverse-metric Hodge map, raw reduction, and projected
Shiab response.

On one independent off-diagonal metric-owner/conormal pair:

- all 196 Clifford-generator pairs satisfy the moving metric relation through
  mixed order;
- `Phi1` and `Phi2` recover the accepted base objects and `Phi2` stays free of
  scalar contamination;
- both first Hodge slots reproduce the accepted `dstar` constructor, and the
  full Hodge jet squares to the exact signature sign `-1` through `rs`;
- the base and both first Shiab slots reproduce the accepted fixed and moving
  constructors coefficientwise;
- the mixed Shiab slot is live in 515 sparse coordinates;
- swapping the two owner/conormal directions exchanges the first slots and
  preserves the mixed slot; and
- all four slots are linear in curvature.

The frozen-trace and omitted distinct-slot Hodge-cross plants both change the
mixed response. The new slot is therefore not a disguised first-order replay
or an arbitrary symmetric completion.

Earned verdict:

```text
CONDITIONAL_ACTIVE_MIXED_TRACE_PHI_HODGE_SHIAB_OPERATOR_JET_CLOSED
```

## Construction

Let `G=(G0,Gr,Gs,Grs)` be the exact nonlinear Zorro metric jet and
`Q=G^{-1} eta`. For an exterior-form jet, the Hodge construction applies the
full exterior power of `Q`, including the distinct-slot mixed action

```text
rho(A) rho(B) - rho(B A),
```

then applies the base `(9,5)` Hodge star and the exact density jet once. The
moving Clifford generators come from the same symmetric coframe
`E=sqrt(1+eta(G-eta))`; `Phi2` is one half of the exterior square of `Phi1`.
The geometric trace `t(g)=g/2` is the transported trace from R2B2B2G, not a
frozen blade. Shiab is finally assembled as the projected trace insertion into
the complete raw reduction.

This is the geometer's active trace-reversed `(9,5)` construction because the
campaign's accepted nonlinear Zorro/DeWitt branch lives there. The source
`(7,7)` action pairing remains an unported typed fork, not an alternative value
silently substituted into this calculation.

## Source and Layer 0

The pinned manuscript source confirms the `I1` transgression grammar and its
`1/2,1/3` coefficients. It is silent on this active mixed operator jet.
Repository derivation supplies the metric/coframe, Clifford, Hodge, trace, and
projection composition.

The following remain distinct:

- geometric trace, Clifford generators, `Phi`, Hodge, and Shiab;
- operator jet, raw action density, Euler coefficient bank, Green concomitant,
  and Helmholtz quotient;
- source `I1`, repository `A4`, and manuscript residual-square `I2B`; and
- active `(9,5)` reconstruction and the unported source `(7,7)` action.

## Hostile boundary

This swing closes only the mixed operator dependency on the exercised
conditional active pair. It does **not** assemble the 35-monomial `I1 A4`
bank. More importantly, the distinct off-shell `I2B` action still lacks its
complete second residual-primalizer/pairing jet. Without that object there is
no distinct `I2B C4` bank, no two-bank multi-index Green/Helmholtz reduction,
no live-C3 return, and no coefficientwise `kappa1` classification.

The result does not extend to vertical/mixed conormals, partial-`Z1`, section
tangents, an analytic domain, quotient, observation map, characteristic, or
physics.

## Campaign fences and next gate

P1/P2/P3 remain unchanged and unused. Curt remains
`FORMALLY_SEPARATE_INSIDE_ERIC_LANE`. `TG-1 AND TG-2 AND TG-3` remains
`NOT_PROMOTED`.

Resume at
`PW2F-R2B2B2H2-COMPLETE-I2B-SECOND-PRIMALIZER-PAIRING-THEN-C4-BANKS`.
Construct the full off-shell residual/primalizer/pairing second jet before
assembling separate `I1` and `I2B` quartic banks or running Green/Helmholtz and
projective classification.
