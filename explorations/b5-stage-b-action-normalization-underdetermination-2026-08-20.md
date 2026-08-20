---
title: "B5 Stage-B action-normalization owner result"
status: active_research
doc_type: exact_action_normalization_gate
created: "2026-08-20"
registry: lab/process/b5-stage-b-action-normalization.json
probes:
  - tests/channel-swings/b5_stage_b_action_normalization_probe.py
grade: "AT THE INDEPENDENT B5 COARSE FORMAL COMPACT-CORE GRADE, THE CURRENTLY SERIALIZED QUADRATIC-ACTION, FORMAL-ADJOINT, NORMALIZED-W131, PRINCIPAL-KERNEL AND LINEAR BV/NOETHER EQUATIONS DO NOT SELECT THE S/IMGAMMA MULTIPLICITY GRAM OR ONE NINE-BLOCK COEFFICIENT PACKET. TWO INEQUIVALENT ALLOWED GRAMS ADMIT EXACT FULL-SUPPORT Q=1 RANK-TWO PACKETS WITH THE SAME SYMMETRIC ACTION HESSIAN AND THE SAME ALL-GRADE KERNEL. THE ACTION-SYMMETRY AND ADJOINT EQUATIONS ARE IDENTICAL, AND LINEAR BV/NOETHER CLOSURE DUPLICATES THE KERNEL EQUATION. FIELD III REMAINS EXTERNAL-VIA-GRAM. THE NEXT MISSING OWNER IS AN ACTION-OWNED FOUR-STAGE DIFFERENTIAL/ROLL PACKET OR ANOTHER INDEPENDENT RELATION; NO FUTURE NORMALIZATION, GLOBAL DOMAIN, QUOTIENT OR GU VERDICT IS EXCLUDED."
target_verdict: B5_CURRENT_STAGE_B_EQUATIONS_UNDERDETERMINE_GRAM_AND_COEFFICIENTS
canon_verdict_change: none
---

# B5 Stage-B action-normalization owner result

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds only the repository's independent B5 full-20
`S + imGamma + kerGamma` coarse first-order family, its currently serialized
relative quadratic action, and its formal compact-core principal equations.
It does not recover Weinstein's historical preferred middle differential and
does not select a source action, pairing, four-stage complex, nonlinear BV
completion, Green domain, quotient, particle result, or GU verdict.

```gu-typed-objects
result: the currently serialized B5 Stage-B quadratic action equations underdetermine the S/imGamma multiplicity Gram and nine-block coefficients
carrier: independent B5 full-20 S+imGamma+kerGamma carrier LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: program-native Cl(9,5) Krein form with free S/imGamma multiplicity Gram ON=independent-B5-full20-carrier
real_structure: B5 antilinear coflip family; not selected by this result
grading: Grassmann-odd first-order formal compact-core grading
action_owner: repository-construction; four-stage rolled action differential remains UNTYPED
target: normalization power of the currently serialized quadratic-action and linear BV equations MAP-TYPE=evaluation
```

## Owner census before algebra

The 2026-07-29 first write owns a coefficient-parametric carrier endomorphism
`M`, a real quadratic ansatz, and its polarized density-dual Hessian. It
explicitly does not own the `0 -> 1 -> 13 -> 14` differential, its Hodge/Krein
roll maps, a master equation, nilpotency, or B5 cohomology. The 2026-07-30
polarization result owns formal adjoint closure, a broad singular principal
locus, and one exact auxiliary `S + imGamma` identity; it explicitly does not
own physical-`R` Noether closure or nonlinear BV closure.

Therefore the equations presently available to Stage-B are:

1. a nondegenerate allowed multiplicity Gram `G`;
2. the quadratic Hessian `H = G M`;
3. formal self-adjointness `M^T G = G M`, equivalently `H^T = H`;
4. the inherited W131 principal normalization `q=1`; and
5. a coarse principal/linear-Noether kernel `M r=0`, equivalently `H r=0`.

Calling items 2 and 3 two independent action constraints would double-count
one equation. Likewise, because `G` is invertible, the present linear
BV/Noether equation and the coarse kernel equation are the same equation.
The desired four-stage acyclicity and nonlinear master equation are missing
owners, not additional constraints that can be silently imposed.

## Exact inequivalent action packets

Take the two allowed nondegenerate Grams

```text
G0 = diag(1, 1/14, 13/14),
G1 = [[1, 1/28, 0], [1/28, 1/14, 0], [0, 0, 13/14]].
```

They are not common rescalings. Let

```text
u=(1,2,3),  v=(4,5,6),  r=(1,-2,1),
H=(13/735)(u u^T + v v^T).
```

Then `H` is symmetric, has exact rank two, and annihilates the all-grade
vector `r`. Its `(R,R)` entry is `39/49`, so for both Grams
`M_i=G_i^-1 H` has `M_RR=6/7`, exactly the nine-block normalization `q=1`.
Both `M_i` have every entry nonzero and satisfy

```text
M_i^T G_i = G_i M_i,
G_i M_i = H,
M_i r = H r = 0.
```

The corresponding coefficient packets are

```text
G0: (a,b,c,d,e,f,g,h,q)
  = (221/735, 286/735, -18/35, 572/105, -377/45,
     24/5, 18/35, 24/5, 1),

G1: (a,b,c,d,e,f,g,h,q)
  = (208/1925, 52/385, -48/275, 31148/5775, -4108/495,
     1308/275, 18/35, 24/5, 1).
```

The packets are inequivalent, not rescalings. Thus even after fixing full
nine-block support, `q=1`, a rank-two coarse singularity, an all-grade kernel,
quadratic-action symmetry, formal adjointness and linear BV/Noether closure,
the current equations admit more than one Gram/coefficient pair.

The freedom is structural, not an accident of the two witnesses. For a fixed
allowed `G`, a symmetric `H` has six entries. `q=1` fixes one entry and
`det(H)=0` supplies one equation, leaving a generic four-dimensional algebraic
locus before imposing the open full-support condition. Fixing the displayed
kernel still leaves a positive-dimensional symmetric-H family.

## Controls and packet consequence

The exact probe passes `26/26`. A one-sided coefficient mutation breaks
`M^T G=G M`; a normalized Hessian mutation breaks both the planted kernel and
singularity; a zero gauge vector is rejected. The prior all-Gram conclusion
is compatible: a *fixed* `M` is not universal, while Stage-B can pair each
allowed `G` with a different `M`. That covariance is precisely why the current
action ansatz does not normalize the pairing.

The five-field packet remains fail-closed and field (iii) remains
`EXTERNAL-VIA-GRAM`. This result does not show that every future action
completion is underdetermined. It shows that the action data currently in the
repository provide no independent selector beyond the equations already
counted.

## Verdict and exact next owner

`B5-CURRENT-STAGE-B-EQUATIONS-UNDERDETERMINE-GRAM-AND-COEFFICIENTS` at coarse
formal compact-core grade.

Before another normalization attempt, serialize an
`ACTION-OWNED-FOUR-STAGE-DIFFERENTIAL` packet: the explicit Hodge/Krein roll
maps and the actual `0 -> 1 -> 13 -> 14` differential whose rolled Hessian
lands in the nine-block family. It must expose an independently checkable
nilpotence/acyclicity or nonlinear BV relation rather than restating Hessian
symmetry or the same kernel equation. If no such owner exists, the Gram stays
a typed external datum; no convenient Gram may be promoted by fit.
