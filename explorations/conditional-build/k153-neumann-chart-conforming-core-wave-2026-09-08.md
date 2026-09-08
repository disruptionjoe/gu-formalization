---
title: "K153 Neumann-chart conforming-core wave"
status: active_research
doc_type: conditional_native_signed_boundary_neumann_chart_conforming_core_gram_coercivity_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned K139-chart construction for the equal-coupling two-edge signed hard-core control: lambda=256 certifies a strict boundary-map contraction; finite orthonormal free-domain charge cores have explicit conforming U_lambda^-1 images with outward geometric tails, uniformly conditioned Hilbert Grams and exact regular-pullback form matrices; regular lower/action bounds transport to coercivity and shifted form-dual residual bounds, but the operator-specific regular charge-sector action and next-distinct-spectrum floor remain absent, so no native energy interval, threshold/Gram closure, scattering, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k153-neumann-chart-conforming-core-wave.json
probe: tests/channel-swings/k153_neumann_chart_conforming_core_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K153 Neumann-chart conforming-core wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet stays on K139--K152's equal-coupling two-edge native
hard-core signed point control, positive particle/hole polarization,
`m=kappa=|q|=1`, positive self energy `1/4`, diagonal `W=0` and finite circle.
The auxiliary `lambda` is only a K139 boundary-chart coordinate. It does not
change the physical operator, weaken a coupling or select an extension.

```gu-typed-objects
result: the fixed signed boundary map has an explicit strict contraction chart, so finite free-domain charge cores have native conforming inverse-chart images with geometric tail bounds, uniformly positive Hilbert Grams, exact regular-pullback form matrices and certified coercivity/residual transport
carrier: each fixed q=(q1,q2) block of the native C3 hard-core impurity tensor positive particle/hole Fock carrier, with finite orthonormal phi_i in Dom(H0,q) and psi_i=U_lambda^-1 phi_i in the K139 native boundary domain LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive Hilbert pairing for the Gram and K139's regular closed form r_lambda pulled back by U_lambda for the singular form; these are distinct matrices ON=repository_signed_point_control
real_structure: canonical CAR adjoint and momentum conjugation; signed flavor exchange transports the chart only when it intertwines G_lambda, R_lambda, pairing and charge cores
grading: q_i=n_i+N_i+-N_i-, native hard-core constraint n1*n2=0, boundary-word order and finite charge-core index
action_owner: repository-construction -- polarization, extension, auxiliary chart, couplings, regular operator, trial core, state and exterior gap are not selected by Weinstein's source or a GU action
target: native conforming charge cores, exact pullback form serialization, Hilbert-Gram conditioning, coercivity and shifted form-dual residual input for K152 MAP-TYPE=intertwiner
```

## Inline preflight bookend

K152 correctly asks for `psi_i=U_s^-1 phi_i`, but its next-condition wording
treats both the Hilbert Gram and the pulled-back form as if they required
independent infinite-tail summation. K139 owns more structure: the singular
operator is factored through one boundedly invertible boundary chart and a
regular operator. The route-changing question is which tails survive that
identity.

Object retrieval found K139's norm-convergent `G_(N,lambda)`, Neumann inverse,
regular pullback and common domain; K145's exact conserved charges; K151's
canonical finite cores and signed flavor unitary; and K152's conforming form-
dual contract. No later correction supersedes those objects. It found no
numerical contraction choice, explicit representative-charge conforming seed,
regular charge-block action matrix or next-distinct-spectrum floor.

The route census compared direct word-by-word form summation, resolvent
identities, boundary triples, exact pullback forms, Galerkin truncation,
interval Grams, KLMN coercivity, Hilbert-to-form-dual embedding, Schur and
Lehmann--Goerisch routes. Exact pullback plus Neumann tails is selected. It
strictly dominates summing a second form tail that cancels algebraically.

## 1. A numerical strict chart for the fixed native control

K139 defines

```text
G_lambda=-(H0+lambda)^-1 C*,       U_lambda=1-G_lambda. (1)
```

For mass one and the four equal signed edge/polarity coefficients,

```text
||G_lambda|| <= 4 h(lambda),
h(lambda)^2=sum_(k in Z)(sqrt(1+k^2)+lambda)^-2.       (2)
```

For `k>=1`, `sqrt(1+k^2)>=k`; the decreasing-series integral bound gives

```text
h(lambda)^2
 <= 1/(1+lambda)^2
    +2[1/(1+lambda)^2+1/(1+lambda)]
 =3/(1+lambda)^2+2/(1+lambda).                        (3)
```

At the auxiliary coordinate `lambda=256`, exact rational comparison proves

```text
16 h(256)^2 <= 16[3/257^2+2/257] <= (3/8)^2.          (4)
```

Thus

```text
||G_256||<=q=3/8<1,       ||U_256^-1||<=1/(1-q)=8/5. (5)
```

This is a native chart bound for the fixed repository control, not a physical
small-coupling claim. Increasing `lambda` only changes coordinates while the
expanded physical operator is held fixed.

## 2. Explicit conforming charge cores and every inverse tail

Let `phi_1,...,phi_n` be any finite orthonormal family in the free operator
domain of one conserved charge sector. Define

```text
psi_i=U_256^-1 phi_i=sum_(j>=0) G_256^j phi_i.         (6)
```

K139's domain theorem makes every `psi_i` native conforming. K145's charge
commutation keeps (6) in the selected sector. In particular,

```text
phi_00=Omega,                 phi_10=d_1^* Omega       (7)
```

give explicit one-vector cores in `q=(0,0)` and `q=(1,0)`. They are symbolic
operator vectors with a certified convergent expansion, not bare cutoff
eigenvectors.

For word order `J`,

```text
||psi_i-sum_(j=0)^J G_256^j phi_i||
 <= q^(J+1)/(1-q)||phi_i||.                            (8)
```

If `||G-G_N||<=delta_N` and both maps have norm at most `q`, the inverse
resolvent identity adds exactly `delta_N/(1-q)^2||phi_i||`. At `J=8`, the
pure word tail is at most `19683/83886080`. Every infinite inverse/cutoff tail
therefore has an outward rational envelope.

## 3. The form tail disappears; the Hilbert Gram does not

Write K139's fixed physical singular operator and regular representative as

```text
H=U_256^* R_256 U_256.                                 (9)
```

For (6), the closed forms obey the exact identity

```text
a(psi_i,psi_j)=r_256(phi_i,phi_j).                    (10)
```

Equation (10) is the central correction. Once the physical operator and its
paired regular representative are fixed, there is no independent infinite
form-matrix tail to serialize. The remaining operator-specific task is to
evaluate and certify the regular matrix/action on the finite free core.

The Hilbert Gram remains nontrivial because `U_256` is not unitary. From
`1-q<=||U x||/||x||<=1+q`, every orthonormal core has

```text
1/(1+q)^2 I <= M <= 1/(1-q)^2 I,
64/121 I <= M <= 64/25 I.                             (11)
```

So the native generalized pencil is uniformly positive definite at every
finite core dimension. Form and Gram are not the same matrix.

## 4. Coercivity and residual transport into K152

If the regular operator has a certified lower bound `R_256>=r0`, then

```text
H+s >= s+r0(1-q)^2,                 r0>=0,
H+s >= s+r0(1+q)^2,                 r0<0.              (12)
```

The sign split in (12) is mandatory because multiplying a norm inequality by
a negative lower bound reverses which chart factor is safe. A positive right
side supplies K152's coercivity floor.

For `phi in Dom(R_256)` and `psi=U_256^-1 phi`,

```text
H psi-rho psi=U_256^* R_256 phi-rho U_256^-1 phi.     (13)
```

This is an ordinary Hilbert vector whenever the regular action is supplied;
no raw point field appears. If its norm is at most `eta` and (12) gives
`H+s>=c>0`, then

```text
||(H+s)^(-1/2)(H-rho)psi||^2 <= eta^2/c.              (14)
```

The compiler also exposes the safe coarse bound
`eta<=(1+q)||R phi||+|rho| ||phi||/(1-q)`. It is an
upper bound, not evidence that K152's projection condition closes.

## 5. Native applicability and charge transport

Equations (4)--(11) now construct native conforming cores and settle their
infinite Gram/form-tail status in both representative charges. K151's signed
flavor unitary transports `q=(1,0)` to `q=(0,1)` only after it intertwines
both `G_256` and `R_256`; verbal equal coupling still does not suffice, and
particle-hole complement remains non-native.

K153 emits no native energy interval. K139 does not serialize the regular
charge-sector matrix/action needed in (10), (12) and (13), and K152's
next-distinct-spectrum floor remains absent. A coarse residual that fails the
projection margin is still an honest bound but not a completed certificate.

## Inline postflight bookend

- **Strongest advance:** native `q=(0,0)` and `q=(1,0)` conforming seed vectors
  now exist explicitly with one numerical strict K139 chart and rational tails.
- **Strongest simplification:** the singular form matrix has no separate tail;
  exact pullback reduces it to the regular finite-core form matrix.
- **Strongest stability result:** every orthonormal core Gram is dimension-
  uniformly positive with spectrum in `[64/121,64/25]`.
- **Strongest contrary route:** direct regular-operator block evaluation is
  still required. The chart theorem cannot manufacture its entries or the
  next-distinct-spectrum floor.
- **Strongest overclaim:** calling `lambda=256` a physical weak-coupling or
  extension selection. Refused: it is an auxiliary coordinate only.
- **Weakest reproducibility seam:** the exact regular representative paired
  with the fixed physical operator must be serialized before (10)--(14) can
  produce a numerical K152 interval.

The five admitted arcs share one pullback identity and exact rational compiler,
so they executed inline. No independent source or specialist context required
a second writer.

## Next condition

Serialize the regular `R_256` form and action on nested finite free-domain
cores generated from `Omega` and `d_1^*Omega` in `q=(0,0)` and `q=(1,0)`.
Use (8) and the cutoff resolvent-identity tail to outer-certify the Hilbert
residual in (13), and prove a next-distinct-spectrum floor by a charge-sector
comparison or equal-rank Lehmann--Goerisch enclosure. Then feed the actual
Gram/form/residual/gap packet to K152 and transport `q=(0,1)` only through the
complete signed flavor intertwiner.

## Reproduction

```bash
python3 tests/channel-swings/k153_neumann_chart_conforming_core_solver.py --demo
python3 tests/channel-swings/k153_neumann_chart_conforming_core_probe.py
python3 tests/channel-swings/k153_neumann_chart_conforming_core_probe.py --selftest
```
