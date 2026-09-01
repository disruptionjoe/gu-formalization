---
title: "K81 null zero-crossing matching wave"
status: active_research
doc_type: reverse_scaffold_null_zero_crossing_matching_result
date: 2026-09-01
claim_ceiling: exact C2 zero-crossing, shear-divisibility and nondegenerate mass-control classification for one real signature-(1,1) affine first-jet class; no source-owned full carrier, physical matching law, gauge quotient, analytic domain, prediction, confirmation or GU verdict
manifest: lab/process/k81-null-zero-crossing-matching-wave.json
probe: tests/channel-swings/k81_null_zero_crossing_matching_probe.py
---

# K81 null zero-crossing matching wave

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
result: C2 classification of a null-line direction switch through an isolated zero, the exact regular shear-divisibility law, and the surviving signature-(1,1) mass-control collapse
carrier: real two-component affine first-jet control with H=diag(1,-1) LAYER=conditional CHIRALITY=N/A
pairing: constant nondegenerate symmetric form H on the repository-owned control ON=signature_11_null_zero_crossing
real_structure: ordinary real conjugation; the two punctured null lines are span(1,1) and span(1,-1)
grading: same-line and switched-line zero horns; no gauge, BRST, BV or physical grading
action_owner: repository owns the frozen quadratic control only; no filed source action owns this bridge or its interface data
target: whether a C2 zero permits a regular projective null-direction switch with an invertible shear matching law or escapes the mass control MAP-TYPE=classification
```

## A `C2` switch must be flat through second order

Use `H=diag(1,-1)`. Its two real null lines are

```text
N_+ = span(1,1),             N_- = span(1,-1).                 (1)
```

Let `n(q)` be `C2`, null, nonzero for `q != 0` sufficiently close to zero,
and suppose the projective null line on the two punctured sides differs. After
relabeling,

```text
n(q)=r_+(q)(1,1), q>0;       n(q)=r_-(q)(1,-1), q<0.          (2)
```

Continuity first gives `n(0)=0`. The common derivative `n'(0)` belongs to
both lines in (1), hence vanishes because their intersection is zero. The same
argument applied to the common second derivative gives

```text
n(0)=n'(0)=n''(0)=0.                                      (3)
```

This order is sharp. The explicit field

```text
n(q)=q^3(1,1), q>=0;        n(q)=q^3(1,-1), q<0              (4)
```

is null and `C2`, genuinely switches projective line, and is not `C3`: its
one-sided third derivatives are `6(1,1)` and `6(1,-1)`. Thus a zero can hide a
direction switch from every second-order local test, but only by annihilating
the complete two-jet at the interface.

## The regular shear coordinate has an exact divisibility law

On a same-line horn write `n=r n_sigma` and absorb the scale into the shear:

```text
tilde_w^rho = r w^rho.                                      (5)
```

At a simple zero, `r(0)=0`, `r'(0)!=0`, a continuous regular shear `w` exists
exactly when `tilde_w/r` has a continuous extension. For `C1` data,
`tilde_w(0)=0` supplies that extension and

```text
w(0)=tilde_w'(0)/r'(0).                                    (6)
```

For `C2` data the first matching jet is

```text
w'(0) = [tilde_w''(0)r'(0)-tilde_w'(0)r''(0)]
        / [2 r'(0)^2].                                      (7)
```

If `tilde_w(0)` is nonzero, the scaled coordinate `w` has a pole. The product
`n w=n_sigma tilde_w` may still be regular, but the purported regular shear
coordinate is not. This distinguishes a regular bridge chart from a regular
product written in a singular chart.

For the switched-line field (4), bounded one-sided shear amplitudes are
multiplied by an order-three zero. Their product has zero value, first jet and
second jet at the interface regardless of the two one-sided amplitude traces.
Consequently `C2` bridge regularity derives no invertible transport or matching
relation between them. Any such relation is extra boundary, action, gauge or
domain data; the zero itself does not own it.

## The nondegenerate mass control still collapses

Freeze the affine first-jet map

```text
T=b(q)+n(q) w^rho(q) v_rho                                (8)
```

and the nondegenerate potential `(m^2/2)<T,T>_H`, `m!=0`.
Velocity independence requires `<n,b>_H=0` on each punctured side. In real
signature `(1,1)`, `n^perp=span(n)`, so `b` lies on `N_+` for `q>0` and on
`N_-` for `q<0`. Continuity forces `b(0)=0` when the lines differ. On each
side, `T` and the relevant first derivatives remain on one fixed null line;
the controlled kinetic density therefore vanishes there and by continuity at
the crossing.

The cubic switch closes the projective-zero horn but does not escape the
two-dimensional mass-control conclusion. It instead makes the failure of
invertible matching explicit.

## Hostile review, scope and next condition

The strongest overclaim would call (3) a theorem in higher signature. It is
not: higher-dimensional null cones have continuous projective directions, as
the preceding signature-`(2,1)` rotating control proves. The strongest
contrary construction is the same-line zero, where both side jets lie in one
line and (3) is not forced. The weakest propagation seam is the word
"matching": bridge regularity only shows that amplitudes are invisible through
the two-jet; it does not select a boundary relation.

The exact probe passes its algebraic, jet, divisibility and mass controls and
contains planted hostile mutations. This packet is a repository-owned local
classification, not a full-carrier GU bridge. The next decisive object is the
independently source/action-owned principal symbol, gauge complex and analytic
domain. A singular, auxiliary, nonlocal, on-shell or gauge-reduced alternative
is also admissible only when its own constraint and interface law are frozen.
