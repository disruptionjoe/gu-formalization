---
title: "K1301--K1305 nonzero-charge shifting and BFV boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1301--K1305 nonzero-charge shifting and BFV boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` for the SC-ACT-06 source-epsilon
preboundary question and `INTERNAL_STRUCTURAL_ONLY` for the shifting, finite
BFV and homogeneous-space theorems.

Scope: the action-owned finite source-epsilon cotangent parent
`T*Spin_0(7,7)`, one supplied regular split coadjoint charge, its auxiliary
negative orbit and the resulting finite Hamiltonian reduction. This is not a
local field-space BV-BFV complex, a released boundary action, a Lorentzian
Green system, a positive physical Hilbert space or an observed state map.

```gu-typed-objects
result: regular nonzero-charge shifting parent, smooth orbit reduction, proper finite BFV complex and invariant positive-metric obstruction
carrier: T*Spin_0(7,7) times the repository auxiliary coadjoint orbit O_-mu LAYER=source-print+toy BRIDGE=shifting_trick CHIRALITY=N/A
pairing: canonical cotangent symplectic form plus the convention-signed Kirillov-Kostant-Souriau form ON=finite_shifted_parent
real_structure: real split group Spin_0(7,7), real regular split charge and real coadjoint orbit
grading: classical BFV ghost number with 91 degree-one ghosts and 91 conjugate antighosts
action_owner: source-action owns the cotangent preboundary parent; repository-construction supplies the shift orbit, charge value and BFV completion
target: diagonal zero reduction identified with the supplied regular coadjoint orbit MAP-TYPE=quotient
```

## K1301: the nonzero charge has a regular shifted presentation

Let `G=Spin_0(7,7)`, so `dim G=91`, and use the source-epsilon cotangent
moment map already authenticated in K941,

```text
J_L(g,p)=Ad_g^* p.
```

For one supplied regular split charge `mu`, let `O_-mu` be the coadjoint orbit
through `-mu`. Its stabilizer is the seven-dimensional split Cartan, so
`dim O_mu=91-7=84`. On

```text
M_shift=T*G x O_-mu
```

take the diagonal left action and moment map

```text
C(g,p,nu)=Ad_g^* p+nu.
```

The cotangent-fiber derivative is always the isomorphism `Ad_g^*`. Therefore
`dC` has rank 91 everywhere, zero is a regular value and the 91 constraints
are irreducible. The diagonal action is free because its action on the `G`
coordinate is free. Hence the 266-dimensional shifted parent has a smooth
175-dimensional zero surface and an 84-dimensional reduced space.

This is the finite shifting trick. Its scientific boundary is as important as
its existence: defining `O_-mu` already supplies the complete charge orbit.
The construction changes the presentation of nonzero reduction; it does not
derive `mu`, its seven invariant values or a source boundary law.

## K1302: the reduction is exactly the supplied coadjoint orbit

The constraint equation is

```text
nu=-Ad_g^* p,
```

with `nu in O_-mu`, equivalently `p in O_mu`. The map

```text
[g,p,nu] -> p
```

is well defined because left multiplication changes `g` and `nu` but leaves
the left-trivialized `p` fixed. Every orbit class has the unique representative
`(e,p,-p)`, so the reduced space is smoothly diffeomorphic to `O_mu`.

With the declared canonical cotangent convention and the KKS form on
`O_-mu`, the gauge slice pulls the reduced symplectic form back to minus the
KKS form on `O_mu`. The sign is conventional; nondegeneracy and the
84-dimensional orbit identification are not. All seven primitive invariant
values are constant on this orbit because they were already fixed by the
choice of `mu`.

## K1303: a proper finite nonzero-charge BFV complex exists

Choose a basis of the Lie algebra and write

```text
C_a=J_a+nu_a,
{C_a,C_b}=f_ab^c C_c.
```

Regularity and freeness give 91 independent first-class constraints with no
first-stage reducibility. The minimal BFV charge is

```text
Omega=c^a C_a-(1/2) f_ab^c c^a c^b b_c.
```

The Jacobi identity and moment-map bracket close `{Omega,Omega}=0`. Locally,
the `C_a` form a regular sequence, so the Koszul--Tate part is proper. Degree
zero after constraint and gauge reduction is

```text
C-infinity(O_mu),
```

not the constants obtained in K944's zero-charge reduction.

This closes one finite presentation gap: a supplied regular nonzero charge is
compatible with a proper finite BFV model. It does not close the selection
gap. The auxiliary orbit carries exactly the `mu` that the seven-lock contract
asked a boundary law to derive. Nor does finite properness construct a local
functional complex, common operator domain, Green law or physical cohomology.

## K1304: the regular split orbit has no invariant positive metric

At a regular split charge, the tangent representation of the stabilizing
split Cartan `A` is the sum of the 84 real root spaces. For
`v_alpha in g_alpha`,

```text
Ad_exp(H) v_alpha=exp(alpha(H)) v_alpha.
```

Suppose a positive-definite tangent inner product were `A`-invariant. Then

```text
||v_alpha||^2
 = ||Ad_exp(H) v_alpha||^2
 = exp(2 alpha(H)) ||v_alpha||^2
```

for every `H`. A nonzero split root admits `alpha(H) != 0`, contradicting
positivity. Thus `G/A` admits no `G`-invariant Riemannian metric and the KKS
form cannot combine with a `G`-invariant compatible complex structure to
produce a positive Kähler metric.

The KKS form remains a perfectly nondegenerate symplectic form. The theorem
does not exclude noninvariant polarizations, unitary representation methods,
boundary-selected metrics or a separately owned positive physical Hilbert
space. It proves only that positivity does not arrive canonically from the
regular split orbit while retaining full `G` invariance.

## K1305: properness moves; ownership and positivity do not

The shifted presentation has three exact satisfied rows: the action-owned
cotangent parent, smooth regular nonzero reduction and the invariant
positivity test. It has two satisfied formal rows: a proper finite nonzero BFV
complex and the orbit-valued degree-zero observable algebra. It excludes one
naive route, a `G`-invariant positive orbit metric. Six decisive rows remain
missing: a source-owned shift or seven-lock law, derived charge values, a
functional local BV-BFV domain, a causal Green or boundary law, positive
nonzero physical cohomology, and an observed state/effect map.

The conclusion is therefore asymmetric. K944's zero-charge model was not the
only proper finite BFV horn: shifting proves conditional nonzero properness.
But the shifting trick cannot select the charge because its auxiliary orbit is
defined by that charge, and split symmetry cannot supply the missing positive
metric invariantly. K1300's native K1145/K1150 candidate pass counts remain
`0/7`.

SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`;
LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`. No source, physics-ledger, canon,
paper, public-posture, prediction, confirmation or protected verdict moves.

## Verification and exact next input

The five producers and their independent hostile probes certify dimensions,
regularity, quotient identification, BFV properness, observable algebra and
the split-isotropy positivity obstruction. The next exact input is a released
source action, boundary or Green law deriving the regular charge or equivalent
seven invariant values, together with a noninvariant-but-owned positive
physical pairing, common local BV-BFV domain, causal realization and observed
state map.
