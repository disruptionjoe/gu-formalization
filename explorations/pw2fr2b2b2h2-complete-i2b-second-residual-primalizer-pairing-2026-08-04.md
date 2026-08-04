---
title: "PW2F-R2B2B2H2 conditional I2B residual/primalizer/pairing second jet"
status: reconstruction
doc_type: exploration
updated_at: "2026-08-04"
run_id: RUN-20260804-062944-gu-formalization-pw2fr2b2b2h2-i2b-second-primalizer
---

# PW2F-R2B2B2H2 conditional I2B residual/primalizer/pairing second jet

## Question

R2B2B2H closed the exact mixed normalized-trace/Phi/Hodge/Shiab operator jet.
The distinct off-shell residual-square action still needed its moving residual,
Hodge primalizer, and pairing through `(1,r,s,rs)` before any `I2B C4` bank
could be admitted.

This swing asks one narrower exact question on the same conditional active
off-diagonal nonlinear-Zorro pair:

> Does the fixed-background active residual square have a dependency-complete
> second residual/primalizer/pairing jet, and does its mixed coefficient equal
> the complete five-family off-shell Hessian product rule?

The source `I1`, the separately custodied manuscript `I2B` glyph, and this
repository active `(9,5)` residual-square port remain distinct. The source is
silent on the active jet and does not identify it with the unported `(7,7)`
pairing.

## Construction

Use the R2B2B2H metric, normalized trace, and mixed Shiab operator on owner 3
with conormal `(-1,2,0,1)` and owner 7 with conormal `(1,0,-2,2)`. Apply it to
the accepted active spin-curvature background to obtain

```text
E = (E0, Er, Es, Ers).
```

Independently construct the moving symmetric residual pairing

```text
P_g(left,right)
  = 1/2 [ top((*_g left) wedge right) + top((*_g right) wedge left) ].
```

The base slot is checked against the earlier 115,584-dimensional full-carrier
coordinate primalizer. Both first slots are checked against the accepted
`dstar` constructor. Hodge square is checked through mixed order on the actual
13-form residual.

For

```text
I2B(g) = 1/2 P_g(E(g),E(g)),
```

the mixed coefficient must be exactly

```text
P0(Er,Es)
+ P0(E0,Ers)
+ Pr(E0,Es)
+ Ps(E0,Er)
+ 1/2 Prs(E0,E0).
```

This is the complete five-family off-shell product rule at the scoped jet. It
does not interpolate a quartic bank.

## Exact result

The new base residual recovers all 13 accepted sparse residual coordinates.
The full-carrier norm and moving pairing jet are

```text
P_g(E0,E0) = (981/64, 0, 4293/128, 0).
```

The exact intrinsic mixed pairing slot is therefore zero on this pair, not
nonzero. This is non-vacuous: the second first-order slot is live. The Hodge
primalizer squares to `+1` on the residual 13-form through mixed order.

The mixed action is

```text
D_rs I2B = -103/256.
```

Its five families are

```text
normal J R J                 = -409/1024
residual R D2E               =    3/1024
J DR E (r-pairing, s-J)      =    0
J DR E (s-pairing, r-J)      =   -3/512
1/2 residual D2R residual    =    0
sum                          = -103/256.
```

Thus three families are live and the two zeros are exact scoped values. The
direct sparse action jet equals the independently assembled five-family sum.
The exact nonlinear metric and trace jets exchange their first slots and
preserve mixed data under the owner/conormal swap.

Frozen-primalizer, omitted-mixed-residual, planted-nonzero-`D2R`, positive-
Hilbert, and complete-bank promotion controls are all rejected.

Earned result:

```text
CONDITIONAL_ACTIVE_FIXED_BACKGROUND_I2B_SECOND_RESIDUAL_PRIMALIZER_PAIRING_JET_CLOSED
```

## Hostile boundary

The initial preregistered expectation that the intrinsic mixed pairing slot
must be live was overbroad. Exact computation gives zero while retaining a
live first slot and a live mixed action through the other three families. The
acceptance rule was repaired to require an exact non-vacuous five-family jet,
not a predetermined nonzero value for every family.

This result closes the fixed-background residual/operator second-jet
dependency on the exercised pair. It does **not** construct the global
source-epsilon curvature graph. Consequently it does **not** assemble either
35-monomial `I1 A4` or `I2B C4` bank, perform full four-dimensional
multi-index Green/Helmholtz reduction, select `kappa1`, close the live C3
return, or establish a domain, quotient, observation, characteristic, or
physics result.

## Campaign fences and next gate

P1/P2/P3 remain unchanged and unused. Curt remains
`FORMALLY_SEPARATE_INSIDE_ERIC_LANE`. `TG-1 AND TG-2 AND TG-3` remains
`NOT_PROMOTED`.

Resume at
`PW2F-R2B2B2H3-COMPLETE-SOURCE-EPSILON-CURVATURE-GRAPH-THEN-SEPARATE-C4-BANKS`.
Complete the global/source-epsilon curvature graph on the admitted active
port before assembling the separate `I1` and `I2B` quartic banks or running
the multi-index Green/Helmholtz and projective classifier.
