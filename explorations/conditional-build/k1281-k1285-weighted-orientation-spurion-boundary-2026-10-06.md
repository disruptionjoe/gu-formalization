---
title: "K1281--K1285 weighted orientation-spurion boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1281--K1285 weighted orientation-spurion boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact classifies
> internally generated homogeneous functions of the connected split-`D7`
> invariant ring. It does not exclude nonhomogeneous action terms, singular or
> parity-nonstable branches, source-owned boundary/Green data, or an external
> orientation spurion. Read `lab/methods/source-native-comparator-routing.md`
> before reuse.

Classification: `SOURCE_NATIVE_ROUTE` for composition with the K1273/K1280
owner question and `INTERNAL_STRUCTURAL_ONLY` for the invariant-ring and
covering-space theorems.

```gu-typed-objects
result: weighted parity semigroup, internal weight-21 coefficient obstruction, regular analytic/rational extension, orbit-cover section boundary and integrated admission
carrier: frozen regular split-D7 Cartan quotient with invariant generators of weights 2,4,6,8,10,12,7 LAYER=source-print CHIRALITY=N/A
pairing: weighted scalar invariant multiplication and sign-cover projection ON=cartan_invariants
real_structure: real invariant coordinates with outer deck reflection p to minus p
grading: p has weight 7; the K1273 coefficient has weight 21; the scale-covariant selector has weight 28
action_owner: repository-construction -- no released source coefficient or physical orientation is supplied
target: K1273 scale-covariant odd response and K1280 source/functional admission MAP-TYPE=evaluation
```

## K1281: weighted parity is fixed by total weight

Write a monomial in

```text
R[e2,e4,e6,e8,e10,e12,p7]
```

as `e2^a2 ... e12^a12 p^j`. Its weighted degree is an even integer plus
`7j`, so

```text
W = j (mod 2).
```

Every homogeneous even-weight polynomial is therefore even in `p`, and every
homogeneous odd-weight polynomial is odd in `p`. In particular weight 28 is
outer-even and weight 21 is outer-odd. This is stronger than K1276's
low-ordinary-degree floor but narrower in another direction: it assumes one
weighted-homogeneous piece.

## K1282: the internal coefficient restores the symmetry

K1273 requires a coefficient `epsilon` of invariant weight 21 so that
`epsilon p` has weight 28. Exact enumeration gives fifteen weight-21 monomial
exponent classes. Their `p` exponents are only one or three; all are odd.
Hence every internally generated polynomial coefficient obeys

```text
epsilon(-p) = -epsilon(p),
epsilon(-p)(-p) = epsilon(p)p.
```

It cannot act as the fixed scalar tilt of K1271--K1273. The apparent
orientation is absorbed back into an even weight-28 term. A fixed scalar or an
independently transforming spurion would evade the theorem precisely because
it is extra data rather than a function of the same invariant point.

## K1283: regular analytic and rational repairs do not help

A convergent weighted-homogeneous analytic germ has only finitely many
monomials at a fixed positive weight, so K1281 applies termwise. For a regular
homogeneous rational function `F=N_A/D_B` on a parity-stable domain,

```text
F(-p) = (-1)^(A-B) F(p).
```

Thus every regular rational coefficient of weight 21 is also odd and its
product with `p` is even. Denominators vanishing on the reflection locus,
branch cuts, parity-nonstable domains and nonhomogeneous effective laws fall
outside this regular theorem and remain possible only with explicit ownership.

## K1284: selecting a sheet is exactly an orientation choice

The outer quotient is locally `q=p^2`. Over connected `q>0`, every continuous
section is `p=sigma sqrt(q)` for one constant sign `sigma`. Such a section
exists only after choosing one sheet. It extends continuously to `q=0` by
`p=0`, but it is not `C1` in the quotient coordinate there. No deck-equivariant
section exists over `q>0`, because equivariance under a trivial quotient action
would require `p=-p`. The mathematical existence of two sections therefore
does not make either one canonical or source-owned.

## K1285: admission boundary

The integrated certificate contains eleven satisfied, six excluded, four
conditional and six missing rows. Internally generated homogeneous polynomial,
convergent analytic and regular rational weight-21 coefficients are closed as
fixed odd-tilt owners in this scope. External spurions, explicitly
nonhomogeneous action terms, boundary/Green response, singular owned branches
and physical one-component restrictions remain open.

K1145 and K1150 remain `0/7`. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53
remains `UNCERTAIN`, LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`, and no source,
ledger, canon, paper, public posture, prediction, confirmation or protected
verdict moves.

## Verification and next exact input

The five producers pass `65/65` declared controls and the five probes reject
`40/40` hostile mutations. The next exact input is a source-owned datum that
is not merely a homogeneous function of the same connected invariant point:
an external orientation spurion, an explicitly nonhomogeneous action term, a
boundary/Green law, or an owned singular/component restriction. It must also
supply the six shape responses and the complete K1145/K1150 functional packet.
