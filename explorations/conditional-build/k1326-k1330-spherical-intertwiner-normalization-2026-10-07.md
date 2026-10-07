---
title: "K1326--K1330 spherical intertwiner normalization boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-07"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1326--K1330 spherical intertwiner normalization boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only for the SC-META-53 positivity
question and `INTERNAL_STRUCTURAL_ONLY` for the spherical coefficient,
meromorphic divisor, inversion-set factorization and Coxeter normalization.

Scope: normalized standard intertwiners restricted to the one-dimensional
spherical vectors of K1312's split-D7 minimal principal series at a supplied
regular imaginary charge. This packet does not construct the operators on all
K-types or a GU physical state space.

```gu-typed-objects
result: rank-one spherical coefficient, meromorphic divisor, D7 inversion-set factorization, spherical-line Coxeter normalization and admission replay
carrier: one-dimensional spherical lines inside the 322560 chamber-indexed compact-picture principal-series controls LAYER=toy CHIRALITY=N/A
pairing: inherited positive compact-picture Hilbert pairing restricted to the spherical vector ON=spherical_line
real_structure: regular imaginary split spectral parameter with complex conjugation z maps to minus z
grading: ungraded Weyl-orbit line bundle with D7 Coxeter transport
action_owner: repository-construction -- scalar analytic control after K1321--K1325
target: whether meromorphic scalar normalization removes Coxeter defects before the full operator problem MAP-TYPE=not-a-map
```

## Preflight bookend

K1321--K1325 close sign-valued normalization but leave arbitrary analytic
scalar defects open. The full Knapp--Stein operator family is not serialized:
there is no common operator domain, K-type spectrum or reducibility analysis.
The cheapest honest discriminator is therefore the spherical line. Its
rank-one integral can be evaluated exactly and then composed by D7 inversion
sets. The claim ceiling is scalar analytic normalization on regular imaginary
charge; nonspherical and physical conclusions remain separate.

The standard theorem context is Knapp and Stein,
[*Intertwining Operators for Semisimple Groups II*](https://doi.org/10.1007/BF01389898),
Inventiones Mathematicae 60 (1980), 9--84. The coefficient below is rederived
directly from the Euler beta integral rather than imported as an unchecked
normalizing convention.

## K1326: exact rank-one spherical coefficient

Every split-D7 root has multiplicity one and no double root. For one simple
root, write the rank-one spectral coordinate as

```text
z=<lambda,alpha_coroot>.
```

On the spherical vector in the noncompact rank-one picture, the raw standard
intertwining integral at the identity is

```text
m(z)=integral_R (1+x^2)^(-(z+1)/2) dx.
```

It converges absolutely for `Re(z)>0`. Substituting `u=x^2` gives the Euler
beta integral

```text
m(z)=B(1/2,z/2)
    =sqrt(pi) Gamma(z/2)/Gamma((z+1)/2).
```

Thus `J_alpha(z)v_z=m(z)v_s_alpha_z` on the spherical vector. Wherever `m(z)`
is finite and nonzero, the scalar-normalized map sends `v_z` exactly to
`v_s_alpha_z`. This evaluates one matrix coefficient; it is not the full
operator.

## K1327: meromorphic divisor and regular imaginary locus

Gamma has simple poles at the nonpositive integers and no zeros. The numerator
and denominator pole lattices are disjoint, so

```text
poles of m: z=0,-2,-4,...
zeros of m: z=-1,-3,-5,... .
```

For `z=i t` with real nonzero `t`, `m(i t)` is finite and nonzero. Complex
conjugation gives `m(-i t)=conjugate(m(i t))`; hence its phase has unit modulus
and the inverse phase at `-t`. A regular split charge has nonzero pairing with
all 42 D7 roots, so every scalar factor encountered along every reduced word
lies on this punctured unitary locus. The singular walls remain excluded, and
the scalar divisor is not an operator reducibility classification.

## K1328: D7 products depend only on inversion sets

For a reduced word `w=s_i1...s_ik`, define

```text
beta_j=s_i1...s_i(j-1)(alpha_ij),
M_w(lambda)=product_j m(<lambda,beta_j_coroot>).
```

The root sequence enumerates the inversion set of `w` once. Therefore the
scalar product is independent of the reduced expression. In D7 the only local
relations are:

- nonadjacent commutation, where both words see `{alpha_i,alpha_j}`; and
- adjacent braid, where both words see
  `{alpha_i,alpha_i+alpha_j,alpha_j}`.

The exact root certificate checks all six adjacent and fifteen nonadjacent
simple-root pairs, the 42 positive roots and longest length 42. This is a
scalar Gindikin--Karpelevich-type factorization, not an operator composition
theorem.

## K1329: the spherical lines are exactly Coxeter-flat

Normalize each simple spherical transport by its nonzero scalar coefficient:

```text
R_i(lambda)=m(<lambda,alpha_i_coroot>)^(-1) J_i(lambda),
R_i(lambda)v_lambda=v_s_i_lambda.
```

The normalized maps satisfy involution, nonadjacent commutation and adjacent
braid relations exactly on the spherical vectors. More generally,
`R_w(lambda)v_lambda=v_w_lambda` is independent of the reduced expression.
K1325's sign repair is therefore a special case of the wider fact that every
nonzero meromorphic scalar defect is removed on this line. A K-type-dependent
operator defect could still survive away from the spherical vector.

## K1330: one analytic row advances; full and physical admission do not

The integrated census now has twenty rows: nine satisfied, three excluded, two
conditional and six missing. The new satisfied row is analytic spherical-line
normalization. Full Coxeter-flat `G` intertwining remains conditional because
operator kernels, a common dense invariant domain, all K-type eigenvalues and
operator pole/reducibility behavior are absent. Source charge/chamber
ownership, interacting constraints, local BV-BFV domain, causal Green or
boundary data, positive nonzero physical cohomology and observed export remain
missing.

## Postflight hostile review

The strongest overclaim is to replace the full principal-series operator by
its spherical eigenvalue. The strongest contrary possibility is a
K-type-dependent zero, pole or relator defect invisible on the spherical line.
The weakest reproducibility seam is the D7 root ordering; the exact certificate
checks all 21 simple-root pairs and pins every composed input. Hostile probes
reverse the divisor, root counts, normalization and all operator/physical
ceilings.

K1145/K1150 remain `0/7`; SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53
remains `UNCERTAIN`, and LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`. No source,
ledger, canon, paper, prediction, confirmation or public status moves.

## Exact next input

For mathematical chamber descent, construct the full normalized simple
intertwiners on a common dense compact-picture domain, compute their action on
every relevant K-type, classify operator zeros, poles, kernels and reducibility,
and prove the operator-valued Coxeter relations. For physical admission,
independently supply a released source action, boundary or Green law deriving
the charge/chamber data together with the interacting local BV-BFV domain,
causal evolution, conserved positive physical cohomology and observed state
map.
