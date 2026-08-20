---
title: "B5 full-20 Gram-adjoint universality result"
status: active_research
doc_type: exact_formal_adjoint_universality_gate
created: "2026-08-20"
registry: lab/process/b5-full20-gram-adjoint-universality.json
probes:
  - tests/channel-swings/verify/rb6_exact_derivative_reverdict.py
  - tests/channel-swings/b5_full20_gram_adjoint_universality_probe.py
grade: "RB6'S FIVE GEOMETRY-OWNED COMMUTATORS ARE STRUCTURALLY ZERO UNDER EXACT GIMMEL DERIVATIVES. FOR THE INDEPENDENT B5 FULL-20 NINE-BLOCK FIRST-ORDER FAMILY, NO FIXED FULL-SUPPORT COEFFICIENT MATRIX HAS ONE FORMAL KREIN-ADJOINT SIGN OVER THE COMPLETE ALLOWED S/IMGAMMA MULTIPLICITY-GRAM FAMILY. THE PUBLISHED ODD CANDIDATE SURVIVES THE CANONICAL DIAGONAL GRAM AND UNIFORM SCALE BUT FAILS AN ALLOWED OFF-DIAGONAL GRAM TWIST. FIELD III IS EXTERNAL-VIA-GRAM; STAGE-B ACTION NORMALIZATION IS NEXT. NO GRAM, ACTION, GREEN DOMAIN, PHYSICAL QUOTIENT OR GU VERDICT IS SELECTED."
target_verdict: B5_FULL_SUPPORT_FORMAL_ADJOINT_SIGN_IS_GRAM_DEPENDENT
canon_verdict_change: none
---

# B5 full-20 Gram-adjoint universality result

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds the repository's independent B5 full-20
`S + imGamma + kerGamma` carrier and its written nine-block formal first-order
family. It tests the complete allowed nondegenerate `S/imGamma` multiplicity
Gram at the coarse three-grade level. It does not recover Weinstein's
historical preferred middle differential and does not select a source action,
pairing, Green form, global domain, quotient, family count, particle, or GU
verdict.

```gu-typed-objects
result: full-support B5 formal-adjoint universality is obstructed by the allowed S/imGamma multiplicity-Gram family
carrier: independent B5 full-20 S+imGamma+kerGamma carrier LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: program-native Cl(9,5) Krein form with free S/imGamma multiplicity Gram ON=independent-B5-full20-carrier
real_structure: B5 antilinear coflip family; not selected by this result
grading: Grassmann-odd first-order formal compact-core grading
action_owner: repository-construction
target: formal Krein-adjoint sign of the fixed full-support nine-block differential MAP-TYPE=evaluation
```

## P-H29 prerequisite: RB6 now exact

The exact gimmel-derivative library rebuilds RB6 without a finite-difference
layer. On the W177 point,

```text
H_Ric = -1/2 I - 3/4 T_tr,
H_R2  =  7/8 I + 9/8 T_tr,
H_RV2 =  3/4 (I + T_tr).
```

All three identities have relative residual below `1e-15`; all five frozen
geometry-owned commutators have norm below `5e-15`. Three deterministic
nearby Lorentzian points retain signature `(6,4)` and the same null. RB6's
source-ownership ceiling is unchanged: the result certifies that no nonzero
geometry-owned Q is present in that grammar; it does not add an action-owned
word. This clears P-H29 for the present interior computation.

## All-Gram equation

At the coarse grades `(S,I,R)=(S,imGamma,kerGamma)`, write the principal
coefficient and pairing as

```text
M = [[a, b,     -13c/14],
     [d, -6e/7,  13f/7 ],
     [g,  h/7,    6q/7 ]],

G = [[alpha, zeta,   0],
     [zeta, beta/14, 0],
     [0,     0,      rho]].
```

For a first-order odd operator, the derivative contributes the common minus
sign; the coefficient matrix must therefore satisfy `M^T G = G M` for the
candidate formal anti-adjoint branch. The three independent equations are

```text
X01 = zeta(a+6e/7) + d beta/14 - alpha b,
X02 = g rho + 13 alpha c/14 - 13 zeta f/7,
X12 = h rho/7 + 13 zeta c/14 - 13 beta f/98.
```

Requiring these identities for all independent allowed
`alpha,beta,zeta,rho` forces

```text
b=d=c=f=g=h=0,  a=-6e/7,
```

with the diagonal `q` block unconstrained by cross-grade equations. The six
forced zeros contradict full nine-block support. Thus a fixed nontrivial
full-support expression cannot be formally anti-adjoint uniformly over the
Gram family.

The opposite formal sign is also exhausted. Requiring the coefficient matrix
to be `G`-skew, `M^T G=-G M`, gives diagonal equations that force
`a=d=b=e=q=0`; its off-diagonal equations then force `c=f=g=h=0`. Only the
zero matrix is uniformly `G`-skew. Therefore neither possible formal-adjoint
sign admits a fixed full-support expression over the complete Gram family.

## Exact plants and packet consequence

The prior odd candidate

```text
(a,b,c,d,e,f,g,h,q)=(1,-1,2,-14,79/40,1,-2,1,1)
```

still satisfies the canonical `G3=diag(1,1/14,13/14)` equation, and uniform
rescaling of `G3` preserves it. The allowed nondegenerate twist
`zeta=1/28` breaks it exactly. This prevents an overstrong claim that the
candidate never has the desired sign: it does, but only after pairing data
are supplied.

The five-field packet stays fail-closed. Field (iii) is now
`EXTERNAL-VIA-GRAM`: its sign is derived once a pairing/action normalization
is owned, but no such owner is selected here. Fields (i), (ii), (iv), and (v)
remain outside this result. The exact next branch is the packet's Stage-B
action-normalization derivation. Coflip and domain-stability work remain
dependent and are not opened by inference.

## Verdict

`B5-FULL-SUPPORT-FORMAL-ADJOINT-SIGN-IS-GRAM-DEPENDENT` at the stated coarse
formal compact-core grade. This is neither a no-go for all B5 actions nor a
GU verdict. A pairing-specific full-support operator remains possible; the
missing scientific owner is the action normalization that fixes the relevant
Gram/coefficient relation.
