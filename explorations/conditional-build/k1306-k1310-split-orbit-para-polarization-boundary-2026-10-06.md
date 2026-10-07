---
title: "K1306--K1310 split-orbit para-polarization boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1306--K1310 split-orbit para-polarization boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only for the SC-META-53 positivity
question and `INTERNAL_STRUCTURAL_ONLY` for the homogeneous-space theorems.

Scope: the regular split coadjoint orbit
`O_mu=Spin_0(7,7)/G_mu` supplied by K1301--K1305, where the stabilizer has
identity component the split Cartan `A`, its convention-signed KKS form, and
invariant tensor fields defined from the real `D7` root decomposition. Any
finite centralizer components preserve the root lines used below. The charge
`mu`, positive-root system, functional domain, physical pairing and observed
state map are not source-derived.

```gu-typed-objects
result: invariant complex obstruction, integrable para-complex structure, neutral para-Kahler metric and real-polarization classification
carrier: regular split orbit Spin_0(7,7)/G_mu LAYER=toy CHIRALITY=N/A
pairing: convention-signed KKS symplectic form and induced neutral g_K=omega(.,K.) ON=orbit_tangent
real_structure: real split D7 root spaces with one-dimensional real g_alpha
grading: positive/negative root para-complex eigenspace grading, 42 plus and 42 minus
action_owner: repository-construction after an imported regular charge and positive-root choice
target: invariant real Lagrangian polarization geometry MAP-TYPE=not-a-map
```

## K1306: full split invariance forbids an almost-complex structure

At the identity coset the tangent representation is
`m=direct_sum_{alpha in Delta} g_alpha`. Each real root space is
one-dimensional, and the split Cartan `A` acts on it through the distinct real
character `exp(alpha(H))`. Every `A`-equivariant endomorphism therefore
preserves each `g_alpha` and is multiplication by a real scalar there. No real
scalar squares to `-1`. Hence `G/G_mu` has no `G`-invariant almost-complex
structure and in particular no invariant KKS-compatible complex
polarization. This is stronger and more precise than inferring the failure of
a complex structure from K1304's positive-metric obstruction alone.

## K1307: every positive-root system gives an integrable para-complex structure

Choose a positive system `Delta_plus` and set

```text
n_plus  = direct_sum_{alpha in Delta_plus} g_alpha,
n_minus = direct_sum_{alpha in Delta_plus} g_-alpha,
K|n_plus=+1,  K|n_minus=-1.
```

The two eigenspaces both have dimension 42. The definition commutes with the
split-Cartan isotropy and therefore extends to a `G`-invariant tensor on the
orbit. Positive roots are closed under addition whenever the sum is a root,
and the same holds for negative roots, so both eigendistributions are
involutive. Equivalently the Nijenhuis tensor vanishes. Thus `K` is an
integrable para-complex structure. It depends on the positive-root choice and
is not an ordinary complex structure.

## K1308: KKS compatibility is neutral, with signature (42,42)

The KKS form pairs `g_alpha` only with `g_-alpha`. Define
`g_K(X,Y)=omega(X,KY)`. On each root plane
`span(E_alpha,E_-alpha)` its matrix is, up to the global KKS sign,

```text
[[0,-c_alpha],[-c_alpha,0]],
```

where regularity of `mu` gives `c_alpha != 0`. Every such block has one
positive and one negative eigenvalue. Therefore `g_K` is invariant,
nondegenerate and symmetric with exact signature `(42,42)`, and satisfies
`g_K(KX,KY)=-g_K(X,Y)`. Together with closed `omega` and integrable `K`, this
is a para-Kahler structure. It is not a positive state metric.

## K1309: the invariant real polarizations form one 322560-point Weyl orbit

Each eigendistribution is 42-dimensional and KKS-Lagrangian. Conversely, an
invariant KKS-compatible para-complex sign assignment must choose exactly one
of `alpha,-alpha` for its plus distribution. Integrability requires both sign
sets to be closed under root addition, exactly the definition of a positive
root system. Positive systems are Weyl chambers. For `D7`,

```text
|W(D7)|=2^(7-1) 7! = 322560.
```

Thus there are exactly 322560 invariant integrable real polarizations, and the
Weyl group acts transitively on them. No chamber is Weyl-fixed or canonical.
This is an exact finite classification, not a positive complex polarization,
half-form measure, unitary representation or physical state construction.

## K1310: para-polarization refines geometry, not physical positivity

Five geometric rows are now satisfied: KKS orbit geometry, invariant complex
test, invariant integrable para-complex structure, neutral para-Kahler metric
and invariant real Lagrangian polarization. Two naive routes are excluded: a
`G`-invariant positive Kahler metric and a canonical Weyl-fixed polarization.
Finite compatibility with K1303 is conditional because no polarized BFV
cohomology or measure was constructed. Six physical rows remain missing:
source ownership of the charge and chamber, positive physical pairing,
functional local BV-BFV domain, causal Green/boundary law, positive nonzero
physical cohomology and observed export.

The result closes K1304's broad "noninvariant polarization" wording in an
unexpected direction: invariant real polarizations do exist, but only as a
large Weyl-torsor of neutral para-Kahler choices. They neither select `mu` nor
resolve SC-META-53. K1145/K1150 remain `0/7`; SC-ACT-01/02/06 remain
`ASSERTS`, SC-META-53 remains `UNCERTAIN`, and LT-SM8/LT-GR6b/RA-F1/AC-F1
remain `NEEDS`.

## Verification and exact next input

Five producers and five independent hostile probes certify the split-isotropy
endomorphism obstruction, integrability, KKS block signature, Weyl-chamber
count and admission census. The next exact input is a released source action,
boundary or Green law deriving the regular charge and selecting or replacing
the chamber choice, plus a conserved positive physical pairing, common local
BV-BFV domain, causal realization and observed state map.
