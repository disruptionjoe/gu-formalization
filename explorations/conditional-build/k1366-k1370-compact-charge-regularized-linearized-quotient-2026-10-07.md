---
title: "K1366--K1370 compact-charge regularized linearized quotient"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-07"
updated_at: "2026-10-07"
---

# K1366--K1370 compact-charge regularized linearized quotient

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only because this packet tests the
maximal-compact shielding route left uncertain by SC-META-53. The compact
circle, charge operator, coefficient and regularized action are repository
constructions. They do not identify a source-selected reduction, hypercharge,
observed particles or the source observation map.

Scope: a minimal positive charge regularizer, its closed quadratic form and
self-adjoint free operator, its exact symmetry/normalization cost, and the
vacuum-linearized BRST cohomology of the repository scalar-electrodynamics
control. No global nonlinear Maxwell--matter theorem, closed nonlinear KT/BV-
BFV quotient, quantization or GU physical cohomology is constructed.

```gu-typed-objects
result: positive compact-charge regularizer, closed graph-domain free operator, symmetry and normalization classification, and completed vacuum-linearized BRST cohomology
carrier: L2(T3;H_ps) with X_Q^1=H1(T3;H_ps) intersection L2(T3;D(Q)) and the zero-mean Maxwell sector LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive charge-regularized energy form plus the transverse Maxwell energy ON=repository_owned_graph_energy_space
real_structure: complex Hilbert charge representation with self-adjoint integer Q and real U1 gauge field
grading: spatial Fourier momentum, integer compact charge and linearized BRST ghost degree
action_owner: repository-construction -- the source selects neither Q nor mu nor the observed carrier
target: SC-META-53 conditional analytic control boundary MAP-TYPE=restriction
```

## Preflight bookend

K1364 proves an exact obstruction rather than a vague missing theorem:
K1359's ordinary positive energy admits a zero-gauge sequence with bounded
energy and divergent `Q` norm. Its first admissible repair is therefore a
positive term controlling `Q phi`. This packet asks whether the minimal term

```text
V_Q(phi)=mu ||Q phi||^2,       mu>0,
```

is actually gauge compatible and analytically complete enough to support a
closed linearized quotient. The positive outcome would close one precise
functional layer. The negative outcome would eliminate the simplest coercive
repair. Neither outcome can manufacture the source selector that is still
absent.

The strongest independent challenger remains a typed nonlinear, differential,
integral or distributional map from released source section spaces to the
principal-series carrier. No released kernel or observed-carrier semantics are
available to test, so the exact K1364 demand is presently more decidable.

## K1366 — the minimal positive charge regularizer

Add to K1359's Lorentzian action the potential term

```text
- mu ||Q phi||^2,
```

and hence add `+mu||Q phi||^2` to the classical energy. K1361 gives

```text
Q exp(i alpha Q) phi = exp(i alpha Q) Q phi,
```

for every real local gauge parameter on the graph domain. Unitarity therefore
gives pointwise equality

```text
V_Q(exp(i alpha Q)phi)=V_Q(phi).
```

The term is exactly circle-gauge invariant. On the common core its BRST
variation also vanishes: `s phi=i c Q phi`, and the two conjugate terms cancel
because `Q` is self-adjoint and the infinitesimal circle action is skew.

The form derivative contributes `mu Q^2 phi` to the strong matter equation on
`D(Q^2)`. More importantly, the regularized energy satisfies the sharp bound

```text
||Q phi||_L2^2 <= E_mu/mu.
```

K1364's witness is repaired exactly: its new energy contribution is
`16 mu N`. This controls the internal charge graph term. It does not by itself
turn covariant-gradient control into ordinary spatial `H1` control; that step
still needs an admissible gauge/spatial estimate.

## K1367 — closed form, self-adjoint operator and sharp boundary

On `H=L2(T3;H_ps)`, define

```text
a_mu(phi)=||grad phi||^2+m^2||phi||^2+mu||Q phi||^2,
m>0, mu>0.
```

The spatial Sobolev form and the internal charge graph form are nonnegative,
closed and strongly commuting. Their sum is therefore a densely defined closed
strictly positive form with exact domain

```text
D(a_mu)=H1(T3;H_ps) intersection L2(T3;D(Q))=X_Q^1.
```

The associated self-adjoint operator is

```text
A_mu=-Delta_T3+m^2+mu Q^2,
D(A_mu)=H2(T3;H_ps) intersection L2(T3;D(Q^2)).
```

The domain identity follows from the joint spatial Fourier and circle-charge
decomposition and the equivalence of `(a+b)^2` with `a^2+b^2` for
nonnegative `a,b`. On joint mode `(k,q)`,

```text
A_mu(k,q)=|k|^2+m^2+mu q^2.
```

Hence `A_mu>=m^2 I`, sharply: K1357 supplies a nonzero neutral sector and the
constant spatial mode attains the floor. The wave generator
`[[0,I],[-A_mu,0]]` is skew-adjoint in the graph-energy inner product and
generates a unitary group. Since `mu Q^2` is internal and spacetime zeroth
order, the principal causal cone is unchanged on the smooth graph core.

Strict positivity does not imply compact resolvent. Every even spherical
harmonic K-type has a circle-neutral, M-fixed vector (take the harmonic
projection of an even polynomial in a coordinate fixed by the selected
circle). These mutually orthogonal K-types make the neutral charge space
infinite dimensional. Constant spatial neutral vectors therefore give
infinite multiplicity at eigenvalue `m^2`.

## K1368 — symmetry and normalization are not selected

The regularizer is invariant precisely under unitaries preserving `D(Q)` and

```text
U* Q^2 U = Q^2.
```

This `Q^2` commutant/normalizer contains the selected circle and may contain a
charge-sign reversal. It is not the full split group. If `Q^2` commuted with
the full irreducible principal-series action, all of its spectral projections
would lie in the representation commutant. Schur irreducibility would force
`Q^2` to be scalar, contradicting K1358's neutral sector and unbounded charges
`plus_or_minus 4n`.

The regularizer also cannot fix charge normalization. For every nonzero real
`c`,

```text
mu Q^2 = (mu/c^2) (cQ)^2.
```

It is additionally blind to `Q -> -Q`. Thus the action term can make a chosen
compact reduction dynamically coercive, but it presupposes the charge ray and
the coefficient product. It selects neither primitive generator, orientation,
normalization nor observed charge labels.

## K1369 — completed vacuum-linearized BRST cohomology

Linearize at `A=0, phi=0` in K1348's zero-mean trivial-holonomy sector. The
BRST differential is

```text
s_lin A=d c,       s_lin c=0,       s_lin phi=0.
```

The matter rule vanishes at the vacuum even though the full nonlinear rule is
`s phi=i c Q phi`. K1342/K1348 supply the closed zero-mean Maxwell gradient
image and positive transverse photon quotient. K1367 supplies the completed
matter energy space

```text
E_matter = X_Q^1 direct_sum L2(T3;H_ps)
```

and its skew-adjoint free generator. Consequently

```text
H_BRST^0(linearized)
  = H_Maxwell_transverse direct_sum E_matter.
```

The quadratic pairing is the positive transverse Maxwell energy plus
`||Pi||^2+a_mu(phi)`. It is positive and nonzero on every nonzero class.
This closes the completed vacuum-linearized layer left at the algebraic core
in K1359.

The nonlinear gap remains exact. Away from the vacuum, the BRST differential
contains `cQphi`, the Gauss constraint is nonlinear and the current contains
`Q D phi`. This packet proves neither closed nonlinear range nor global
coupled evolution.

## K1370 — admission replay

The bridge census now has 45 rows: 30 satisfied, four conditional, seven
excluded and four missing. Three rows are newly satisfied: the positive
gauge-invariant charge regularizer, the closed self-adjoint free graph-domain
operator and the exact `Q^2` symmetry classification. The existing conditional
vacuum-linearized cohomology row is strengthened to the completed charge graph
energy space. One new implication is excluded: the quadratic regularizer does
not by itself select charge sign, normalization or the primitive compact
generator.

The same four source/physical rows remain missing:

- source-owned selection and normalization on the actual observed carrier;
- identification with one source-action-derived interacting constraint complex;
- a closed fully coupled global nonlinear BV-BFV quotient with positive GU
  physical Hilbert cohomology; and
- a source-owned observed-state/export map.

K1145/K1150 remain `0/7`. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53
remains `UNCERTAIN`, and LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`.

## Postflight hostile review

The strongest overclaim is that adding a positive term solves the physical
positivity problem. It does not: `Q` and `mu` are repository choices, the term
breaks full split symmetry to the `Q^2` commutant, and the completed cohomology
is vacuum-linearized. The strongest contrary observation is the normalization
degeneracy `(Q,mu)~(cQ,mu/c^2)`, which prevents the action term from selecting
the data it uses. The weakest analytic seam is the jump from the closed free
form to the nonlinear gauge system; that jump is refused explicitly.

The noncompact-resolvent result is also important. A positive floor and
unitary free evolution do not manufacture finite multiplicity, trace-class
heat kernels or a quantum measure. None is claimed.

## Exact next input

Two independent obligations remain. First, a source/action-owned reduction on
the actual observed carrier must select the compact generator, its orientation
and normalization, and prove that source constraints and observation maps
preserve the graph domain. Second, the regularized nonlinear Maxwell--matter
system needs a global graph-energy estimate, closed nonlinear Gauss/KT range,
proper BV-BFV quotient and positive nonzero physical Hilbert cohomology.

The strongest alternative remains a typed nonlinear or nonlocal source-section
map with declared domain, equivariance reduction, action owner and observed
semantics. Do not call the repository regularizer source-derived, infer compact
resolvent from the positive gap, or transfer vacuum-linearized cohomology to
the nonlinear physical theory.
