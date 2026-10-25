---
title: "K2030: Changing the positive metric does not rescue the fixed raw coefficients"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: complete constant positive-core metric boundary for the fixed common H and contraction; no GU-wide or variable-background exclusion
scripts:
  - tests/channel-swings/k2030_positive_metric_rescue.py
  - tests/channel-swings/k2030_positive_metric_rescue_probe.py
---

# K2030: Changing the positive metric does not rescue the fixed raw coefficients

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: complete upper-preserving image, all positive principal metrics and mixed Fourier instability
carrier: fixed raw1920 construction and its128 core LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed full indefinite H and arbitrary positive Hermitian core P ON=declared_full_and_core_carriers
real_structure: real raw generators and their explicitly complexified Hermitian coefficient branch
grading: Clifford central decomposition, not observed physical chirality
action_owner: repository-construction -- frozen raw contraction and invariant injection
target: conservative core dynamics for every real spatial momentum MAP-TYPE=intertwiner
```

## 1. Question and result

[K2028](k2028-all-grade-raw-common-form-2026-10-24.md) imposed the inherited
positive core form P=8I. Its coefficient census already stores **14** imaginary
upper-preserving directions before the energy condition, although only13
survive that condition. Could a different positive metric rescue the extra
one, or a mixture with the real survivor?

No, for this fixed constant-coefficient construction. The entire upper action is

    s M + i(t N + a0 I + a1 C1 + a2 C2 + a3 C3),       (1)

with real parameters. Nine further imaginary coefficient directions act
trivially on the core. Direct reconstruction of all14 imaginary directions
and the existing real survivor gives

    M^2 = alpha I, alpha=4193408/1087849 > 0,
    N^2 = -I/2,    MN+NM=0,
    {M,Cj}={N,Cj}=0,    {Ci,Cj}=2 delta_ij I.          (2)

For any nonzero (s,t), there are64 growing and64 decaying Fourier modes at
one real momentum. No positive conserved norm can remove those eigenvalues.
Thus allowing **every constant positive Hermitian principal metric**, including
complex non-scalar forms, leaves exactly the same13-dimensional coefficient
space and scalar/vector image as K2028. This is a substantive extension of the
fixed-P result, not a new all-grade census or a source-physics verdict.

## 2. Reconstruction and completeness boundary

The all-grade coefficient-space completeness is reused from K2028's pinned
real and imaginary kernels and its separate raw-action rank certificate.
Here every stored imaginary upper kernel vector is substituted into the
original coefficients

    Omega_k=(3I+volume) eta_k gamma_k Y_k/4.

The producer evaluates D_k(Omega_k J), sums the raw returns, and checks all14
upper blocks and the forced negative H-adjoint lower block. The separate
checker reverses the contraction order using the explicit upper formula and
checks all210 returns again. All14 directions have full lower invariance with
southeast zero. Their image has dimension5, with basis I,C1,C2,C3,N; its kernel
has dimension9. The report contains the coefficients, images and coordinates.
No extra direction was guessed from a small coefficient sample.

The real upper direction M is the exact K2028 survivor. Its full lower return
requires K2028's southeast repair when s is nonzero. Allowing that repair
cannot help the positive-core obstruction below, which already holds on the
upper equation. Forbidding the repair only narrows the available class.

## 3. Mixed directions have an open band of unstable momenta

Use the core equation

    partial_t phi + sum Cj partial_j phi
       + [sM+i(tN+a0I+sum aj Cj)] phi = 0.

For real Fourier momentum xi, remove the scalar phase a0 and put k=xi+a.
The remaining evolution generator is the negative of

    G(k)=sM+i(tN+sum kj Cj).

Equation(2) gives the exact matrix identity

    G(k)^2=[alpha s^2+t^2/2-|k|^2] I,   tr G(k)=0.     (3)

At k=0 and (s,t)!=0 the bracket is strictly positive. The roots are distinct,
so G is diagonalizable with eigenvalues plus/minus sqrt(alpha s^2+t^2/2).
Trace zero fixes both multiplicities at64. More strongly, the same real growth
occurs on the open ball |k|^2<alpha s^2+t^2/2. This is not merely a single
non-normalizable plane wave: Fourier packets supported in a compact sub-ball
and in a growing spectral bundle give exponentially growing L2 solutions.
The spectral projectors (I plus/minus G/sqrt(discriminant))/2 are bounded
there. A compactly supported smooth Fourier section gives an actual packet.

If a positive Hermitian form P made this generator skew-adjoint, an eigenvector
with nonzero real growth rate lambda would satisfy

    0 = v^dagger(PG+G^dagger P)v
      = 2 Re(lambda) v^dagger P v,

a contradiction. This argument permits a momentum-dependent positive metric
at the unstable momenta as well; it does not assume P=8I or commutation with M.
No nonzero invariant subspace or quotient of the k=0 diagonalizable matrix
can carry a positive conserved norm, since all its eigenvalues have nonzero
real parts. This statement is at that momentum, not a claim about every
frequency-selective restriction.

A time-dependent norm uniformly equivalent to the fixed L2 norm for all time
cannot conserve these growing packets either. An unrestricted time-dependent
metric can hide growth: for the constant ODE dot u=-G u,
P(t)=exp(t G^dagger) P(0) exp(tG) gives an exactly conserved quadratic form.
Its exponential loss of uniform bounds is the missing hypothesis. We do not
exclude that coordinate construction or arbitrary variable backgrounds.

## 4. All principal metrics and the surviving directions

With s=t=0, every positive Hermitian P commuting with C1,C2,C3 conserves the
constant-coefficient equation. Conversely, a common constant energy for every
spatial momentum must commute with each Cj, because they are real symmetric.
The principal-metric freedom is large; its failure to repair (1) is not an
absence of alternatives.

Let V=C1 C2 C3. Exact identities give V^2=-I, V^T=-V, and [V,Cj]=0.
Over the complex numbers K=iV is a Hermitian involution. Its plus/minus
projectors have rank64. Within each central sector, C3 has two rank32
eigenspaces and C1 is an invertible isometry exchanging them. C2 is fixed by
C1,C3 and the central sign. Thus the commutant is

    M32(C) direct-sum M32(C).

Every principal-compatible positive Hermitian form is an arbitrary positive
32-by32 Hermitian matrix on each multiplicity space, tensored with the
2-dimensional Clifford representation. This cone has **2048 real dimensions**.
For real symmetric forms, complex conjugation exchanges the two central
sectors and ties the two blocks, leaving **1024 real dimensions**. These are
parameter counts of metrics, not physical modes or generations.

An explicit non-scalar example is P=I+(i/2)V, with eigenvalues1/2 and3/2.
All scalar/vector imaginary coefficients conserve it; none of the extra
mass-like directions does. The report checks the central and joint C3
projectors directly. The commutant classification follows from the displayed
2-by2 block representation, not from numerical rank fitting.

For smooth prescribed surviving scalar/vector potentials, the local current
and gauge-curvature identities are those of K2028. The general bounded-
coefficient common-domain/causal construction already appears in
[K1961](k1961-curved-core-connections-2026-10-22.md), with its declared
hypotheses. It is reused, not counted as a new global-domain result here.
Neither a new metric nor the existing propagator selects a source field,
physical quotient, interacting action or global source bundle.

## 5. Review, controls and next discriminant

Strongest hidden assumption: assuming failure at P=8I excludes every P.
The full14-direction reconstruction and mixed polynomial(3) supply the missing
argument. Strongest contrary route: combining the two rejected directions;
the positive sum alpha s^2+t^2/2 rules out that repair. A genuinely unbounded
moving metric is retained as a counterexample to an overly broad no-metric
claim. Weakest transfer seam: raw image completeness; its full-space rank
certificate is inherited by hash, while every surviving raw action is replayed.

The producer's14 full raw reconstructions, matrix identities and five Fourier
controls are exact. The separate contraction, central/multiplicity projectors,
four mixed Fourier controls and four actual coefficient faults are independent
implementations by the same author. Provenance hashes are separate checks.
The universal PDE and metric conclusions are the arguments above, not a pass
count. No external specialist or proof-assistant certification is claimed.

SC-OP-04 ASSERTS the candidate four-field grammar; SC-OP-05 is UNCERTAIN about
the unselected southeast rival. SC-META-53 remains UNCERTAIN on physical
positivity and SC-META-56 DISAVOWS an odd-action prerequisite. These polarities,
LT-SM8/LT-GR6b, source register and canon do not change. A different full form,
raw contraction, principal carrier or actual physical constraint remains a
new branch. Reweighting the same constant positive core metric is now exhausted.
