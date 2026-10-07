---
title: "K1336--K1340 principal-series Lorentzian free-field control"
status: active_research
doc_type: conditional_research_result
created: "2026-10-07"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1336--K1340 principal-series Lorentzian free-field control

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only for the SC-META-53 carrier-level
positivity question and `INTERNAL_STRUCTURAL_ONLY` for the free
Klein--Gordon, Green and tensor-equivariance control.

Scope: a repository-owned free field on the ultrastatic globally hyperbolic
spacetime `R x T3`, with K1335's spherical minimal-principal-series Hilbert
space `H_ps=L2(K/M)` as an internal fibre. This is not the GU action, does not
derive the split charge, and has no nontrivial gauge or interacting BV-BFV
complex.

```gu-typed-objects
result: Hilbert-valued Klein--Gordon domain, positive energy generator, causal Green operators, Cauchy form, internal principal-series equivariance and physical-admission replay
carrier: H1(T3;H_ps) direct_sum L2(T3;H_ps), H_ps=L2(K/M) LAYER=toy CHIRALITY=N/A
pairing: positive Klein--Gordon energy pairing ON=free_Cauchy_data
real_structure: real spacetime field with complex unitary principal-series internal fibre and conjugate-compatible evolution
grading: trivial constraint grading; degree-zero cohomology only
action_owner: repository-construction -- free quadratic control after an imported regular charge
target: whether the completed principal-series Hilbert carrier alone obstructs local causal positive free dynamics MAP-TYPE=not-a-map
```

## Preflight bookend

K1331--K1335 close the full normalized-intertwiner obligation. A fourth
adjacent singular-charge or nonspherical representation packet would not test
the physical bottleneck. The route therefore switches to the cheapest
carrier-level falsifier: tensor the exact positive internal Hilbert space with
a standard local Lorentzian field operator and ask whether common domain,
positive energy, causal Green and internal equivariance coexist.

The first kill is failure of positivity or skew-adjointness on one spatial
Fourier mode. The second is a nonzero commutator between the spacetime
operator and the internal `Spin_0(7,7)` action. A positive result excludes only
the narrow statement that the completed mathematical Hilbert carrier itself
prevents free causal positive dynamics. It cannot supply GU action ownership,
interaction, constraints, observed-state meaning or physical cohomology.

## K1336: common local domain and positive spatial operator

Take

```text
X=R_t x T3_x,
H_ps=L2(K/M),
H=L2(T3;H_ps),
A_m=(-Delta_T3+m^2) tensor I_Hps,  m>0.
```

The positive quadratic form of `A_m` has domain `H1(T3;H_ps)` and the
self-adjoint operator has domain `H2(T3;H_ps)`. Finite spatial Fourier sums
with K-finite internal values form a common core. On mode `k in Z3`,

```text
A_m(k)=omega_k^2=|k|^2+m^2 >= m^2.
```

Thus `P=partial_t^2+A_m` is a local Hilbert-valued Klein--Gordon operator with
an explicit common domain, zero kernel for `m>0`, and a strict free gap.

## K1337: positive energy and unitary evolution

On the energy space

```text
E=D(A_m^(1/2)) direct_sum H
```

use

```text
||(phi,pi)||_E^2=||A_m^(1/2)phi||^2+||pi||^2,
G(phi,pi)=(pi,-A_m phi).
```

The generator domain is `D(A_m) direct_sum D(A_m^(1/2))`. Modewise,

```text
G_k=[[0,1],[-omega_k^2,0]],
H_k=diag(omega_k^2,1),
G_k^* H_k+H_k G_k=0.
```

The spectral theorem therefore gives a skew-adjoint generator and a strongly
continuous unitary group. Its modal propagator is

```text
[[cos(omega t), sin(omega t)/omega],
 [-omega sin(omega t), cos(omega t)]].
```

This is positive conserved free energy, not a bounded interacting GU
Hamiltonian.

## K1338: causal Green system and Cauchy boundary form

`R x T3` is globally hyperbolic and `P` is normally hyperbolic. Its Green
operators are the direct tensor lifts `E_plus/minus_scalar tensor I_Hps`, so
the scalar support theorem supplies unique advanced and retarded operators on
compactly supported smooth `H_ps`-valued sources, with support in the
appropriate causal future or past. Modewise the retarded kernel is

```text
theta(t) sin(omega_k t)/omega_k,
```

whose value is zero and derivative jump is one at the source time. The Cauchy
form

```text
Omega_Sigma((phi,pi),(psi,rho))=<phi,rho>-<pi,psi>
```

is preserved by the flow and is independent of the Cauchy slice for
homogeneous solutions. This is a free boundary symplectic control, not the
source-owned GU BFV reduction.

## K1339: internal symmetry and chamber blindness

Let `pi_lambda(g)` be K1335's unitary principal-series action. On spacetime
fields,

```text
U(g)=I_spacetime tensor pi_lambda(g),
P=P_spacetime tensor I_Hps.
```

Consequently `P`, the first-order evolution and both Green operators commute
with the internal action. The normalized Weyl operator
`I_spacetime tensor R_w(lambda)` intertwines the same free dynamics between
charge fibres. K1335's coherent chamber diagonal therefore remains a free
`G`-invariant field subspace. The construction is deliberately chamber-blind:
it derives neither the charge nor a physical chamber.

## K1340: the carrier-only obstruction is excluded only at free level

The fourteen-row free-control census has nine satisfied rows, one conditional
row and four missing rows. The common domain, positive gap, unitary evolution,
causal Green system, conserved Cauchy form, internal equivariance and nonzero
free solution space are explicit. Positive degree-zero cohomology is only the
trivial-constraint complex and therefore remains conditional rather than GU
physical cohomology.

The four missing rows are load-bearing: source-owned charge/chamber data, an
action-derived interacting constraint/KT/BV-BFV complex, positive nonzero
cohomology of that nontrivial physical quotient, and a source-owned observed
state/export map. K1145/K1150 therefore remain `0/7` for native candidates.

## Postflight hostile review

The strongest overclaim is that a positive free tensor model solves
SC-META-53. It does not: the source's indefinite interacting and observed
physical problem is not this quadratic control. The strongest mistyping is to
call the trivial constraint complex a GU BV complex. Its degree-zero
cohomology is merely the free solution space. The strongest contrary
construction would add a nontrivial action-owned gauge constraint whose
quotient destroys positivity, closed range or domain invariance; no such
constraint was tested here.

The weakest seam is the passage from finite modal controls to the full
operator. It is protected by the positive self-adjoint spectral theorem and
the direct tensor lift of the scalar normally-hyperbolic Green operators on
the declared ultrastatic background, not inferred from finite matrices. The finite producers test the
exact identities and hostile probes prevent domain, support, interaction,
source and observation overclaims.

SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains `UNCERTAIN`, and
LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`. No source, ledger, canon, paper,
prediction, confirmation or public status moves.

## Exact next input

Preserve the free compatibility result. The next progress-bearing input must
replace the scalar free operator with a source-action-owned nontrivial
constraint/KT/BV-BFV complex on the same kind of common Lorentzian domain,
prove its interacting evolution and boundary law, and show that its physical
cohomology is positive, nonzero and connected to an observed-state map. A
free mass, trivial complex or internal unitary symmetry cannot substitute.
