---
title: "Selected-K77 SR-1C mixed-order operator admission"
status: active_research
doc_type: construction_result
created: "2026-08-14"
registry: lab/process/selected-k77-sr1c-mixed-order-operator-admission.json
probe: tests/channel-swings/selected_k77_sr1c_mixed_order_operator_admission_probe.py
grade: "EXACT MIXED-ORDER INTERFACE CORRECTION AND TOP-ORDER CONTROL; O_SR1C COEFFICIENTS STILL TYPE-MISSING"
canon_verdict_change: none
---

# Selected-K77 SR-1C mixed-order operator admission

## Result first

The advertised uniform “field two-jet” successor to the `O_SR1C` type gate is
not an admissible primitive-source interface. GU already owns the reduced
first-action density weights

```text
(g,varpi,epsilon) = (2,1,1).
```

Consequently, before exact top-coefficient cancellations are computed, the
safe primitive jet ceilings split into two stages:

```text
primitive epsilon / j1(E_B-E_T):  (g,varpi,epsilon) <= (3,2,2)
complete fixed-varpi metric row:   (g,varpi,epsilon) <= (4,3,3).
```

This corrects the VRS-5 execution interface. It does not construct the missing
196-row branch coefficient bank. `O_SR1C` remains `TYPE-MISSING` at coefficient
grade, both algebraic branches remain `NOT-YET-FALSIFIED`, `SR-1` remains
`BACKGROUND-MISSING`, and `SR-2` remains blocked.

## Why connection two-jets are not primitive field two-jets

The source coordinates are `(g,varpi,epsilon)`, with dependent
`B_Z=B_Z(g,epsilon)` and `T=varpi-B_Z`. In the already-owned covariantly
reduced action grammar, the density contains second metric derivatives but
only first derivatives of `varpi` and `epsilon`. One derivative of the
connection momentum can therefore reach `g^3`; the complete metric Euler
variation can reach `g^4` and cross-orders three in the other primitive
fields. Calling a second connection jet a “field two-jet” erases this
distinction.

The bounds are safe ceilings, not assertions that every top coefficient is
nonzero. Covariance, Bianchi identities or exact integration by parts may
lower them. That lowering must be proved on the selected action and exact
two-root witness; it cannot be assumed at admission.

## Exact order fence

A one-dimensional source-shaped control isolates the issue without pretending
to be the selected K77 coefficient bank. Take

```text
B=g',  T=varpi-B,  L=(1/2)(D T)^2.
```

Then the connection momentum and its first two formal-adjoint returns are

```text
p       = varpi' - g'',
-D p    = -varpi'' + g''',
-D^2 p  = -varpi''' + g''''.
```

Two extensions with the same metric two-jet can therefore give different
primitive rows, and two extensions with the same metric three-jet can give
different metric rows. Wrong adjoint signs fire independently. These are
planted order controls: they prove that absent top slots cannot be zero-filled,
not that the selected K77 top coefficients survive.

For a held-out exact branch check, the element `1+t` in
`QQ[t]/(28392t^2+91t-351)` has conjugate norm `13975/14196`, so it is nonzero
on both real embeddings. The interface and tests therefore retain both roots
without selecting a floating representative.

## Corrected operator contract

`O_SR1C` must now serialize two nested outputs on the same exact witness:

1. a common-196-row evaluator for `j^1(E_B-E_T)` accepting the safe
   `(3,2,2)` primitive jet envelope; and
2. the full fixed-`varpi` metric/graph return accepting the safe `(4,3,3)`
   envelope, including dependent `B_Z`, Shiab, Hodge, frame, density and
   lowerer terms.

The implementation must compute the branch-specific top coefficients first.
Only coefficients proved zero may be removed. The subsequent compatible-jet
solve uses the surviving exact orders; it is no longer predeclared as a
uniform two-jet solve.

## Scope and next gate

This is an interface correction and exact determinacy result. It adds no
coefficient, selector, field, quotient, datum, source claim, ledger move,
canon verdict or public-posture change. It constructs no background, total
complex, physical cohomology, positive pairing, superposition law or Born
rule.

Next:

```text
compute the branch-specific top coefficients of O_SR1C over the mixed
primitive jet envelopes; serialize and held-out validate the common-basis
bank; then solve only the exact orders that survive those cancellations.
```
