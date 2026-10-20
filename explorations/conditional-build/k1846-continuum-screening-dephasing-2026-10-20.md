---
title: "K1846: conservative continuum screening and late-time dephasing"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional scalar response only; no source GU action or cosmological screening verdict
---

# Conservative positive energy can coexist with late-time screened readout

A continuum of positive-mass, positive-energy fields can have a causal local
cross-readout whose response to a homogeneous switched constant tends to zero,
without damping. An explicit mass band gives a uniform O(1/t) bound. The
unseen field energy persists: this is dephasing of the measured response, not
energy loss. A conjugate readout can do the same when a direct source contact
is included. Finite positive-frequency spectra cannot give nontrivial ordinary
late-time screening in this frozen conservative linear setting.

This extends K1844's static examples; it does not contradict their persistent
finite-mode oscillations. The continuum, couplings and readouts are imported
conditional data. SC-COS-50/51/54 and SC-ACT-01/02 remain ASSERTS;
SC-META-53 remains UNCERTAIN. LT-GR2c/2d/6b and LT-SM8 do not move.
No GU connection-to-scalar bridge, amplitude selection, exact global projector,
interacting positivity, novelty or external acceptance is claimed.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.


Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: causal continuum step-response decay, finite-spectrum obstruction and source-contact repair
carrier: real Hilbert-valued scalar fields with mass label omega in [1,2] on flat spacetime or spatial torus LAYER=toy CHIRALITY=N/A
pairing: positive L2([1,2],domega) kinetic form ON=real_scalar_fields
real_structure: real field, source and readout
grading: none; spectral parameter is not exterior or particle grading
action_owner: repository-construction -- local direct-integral Klein-Gordon action
target: homogeneous step response of a specified bounded local readout MAP-TYPE=evaluation
```

## 1. One action, one causal domain

Let H=L2([1,2],domega), A multiplication by omega², c(omega)=1 and

```
d(omega)=omega²(omega-3/2).
S = integral_spacetime { 1/2 ||dot(phi)||² - 1/2 sum_j ||partial_j phi||²
                        - 1/2 <phi,A phi> + J<c,phi> }.
```

A is bounded, self-adjoint and 1<=A<=4. Compact variations give
`(Box+A)phi=c J`. Use zero past Cauchy data and the standard energy domain
`H1(space;H) x L2(space;H)`; on R^n take compact-space/time source data.
The scalar fields have no gauge equivalence. The readout O=<d,phi> is bounded
in H and local in spacetime. Its continuum in internal mass is not a spatial
average. Each retarded massive wave has light-cone support; finite uniform
energy bounds on the compact mass band justify integrating the solutions.
Consequently O also has causal support. This is a well-defined positive-energy
linear field theory with infinitely many internal modes, not a finite local
field replacement. Homogeneous steps are taken on the spatial torus, per unit
spatial volume; the sharp time step is an energy-solution limit of smooth
switching. These conventions do not claim a finite-energy homogeneous source
on infinite-volume space.

At J=0, E=1/2(||dot(phi)||²+||grad(phi)||²+<phi,A phi>) is conserved and
nonnegative. The step source does work; after switching, energy relative to
its displaced equilibrium is conserved. Conservation does not imply that every
bounded linear readout retains a nonzero oscillation.

## 2. Exact cross-readout response and its bound

At Laplace frequency s>0 and spatial wave number xi, set z=s²+|xi|². Then

```
R(z)=integral_1^2 omega²(omega-3/2)/(z+omega²) domega,
R(0)=integral_1^2 (omega-3/2) domega=0,
lim_(z->infinity) z R(z)=integral_1^2 omega²(omega-3/2) domega=1/4.
```

The response is thus nontrivial. For a homogeneous source J0 H(t),

```
phi(t,omega)=J0(1-cos(omega t))/omega²,
O(t)/J0 = -integral_1^2 (omega-3/2)cos(omega t) domega
        = -(sin(2t)+sin(t))/(2t) - (cos(2t)-cos(t))/t².       (1)
```

The apparent singularity at zero is removable. In particular
`O/J0=t²/8+O(t4)` and, for t>0,

```
|O(t)|/|J0| <= 1/t+2/t² -> 0.                              (2)
```

A sign-changing cross spectral weight supplies cancellation while all field
energies are positive. The full two-channel resolvent Gram matrix remains
positive semidefinite: `<v,(z+A)^-1 v>>=0` for v in span(c,d). It is the
cross-entry, not the physical norm, that has signs. K1844's contact-free
conjugate positivity theorem still applies and its static integral here is1/2.

The oscillatory fluctuation `psi=phi-J0/omega²` has constant energy density

```
1/2 integral_1^2 (dot(psi)²+omega² psi²) domega = J0²/4.     (3)
```

Thus decay in(2) is not strong energy convergence or dissipation. Nor is it
instantaneous immunity to a time-dependent source: the nonzero short-time
coefficient in(1) is a direct counterexample.

## 3. Spectral boundary: what decay actually requires

For a real finite signed cross measure nu on a mass band [a,b], a>0,
step response is `J0 integral (1-cos(omega t))/omega² dnu`.
If `dnu/omega²=w(omega)domega` with w in L1, the Riemann--Lebesgue lemma
makes its oscillatory part tend to zero; ordinary late screening is exactly
`integral w=0`. For absolutely continuous w on [a,b] with w' in L1,
integration by parts bounds the remainder by
`(|w(a)|+|w(b)|+||w'||_1)/t`.
These are sufficient regularity hypotheses; absence of atoms alone is not a
claimed sufficient condition for Fourier decay. Singular continuous measures
need a separate Fourier-decay hypothesis.

For finitely many distinct positive frequencies, put
`a_j=nu({omega_j})/omega_j²`. Then `O/J0=S-sum a_j cos(omega_j t)` with
S=sum a_j. If O tends to zero, its Cesaro average gives S=0 and its Cesaro
mean square gives `sum a_j²/2=0`; all grouped a_j vanish. Repeated frequencies
must first be combined: cancellation inside a degenerate eigenspace makes the
observable response identically zero and is not a nontrivial decay example.
The proof uses exact integral averages of cosines, not rational independence.
It excludes finite conservative massive realizations of this response,
including finite approximations of the continuum in(1), at arbitrarily long
times. A finite approximation can match a bounded time interval; the limits
of mode count and t->infinity cannot be interchanged without proof.

## 4. Released repair: conjugate contact response also decays

Keep the same H, A, c, but add the local source term `-J²/4` to S. The field
equation and J=0 energy do not change. Now the source-conjugate readout is

```
O_c=<c,phi>-J/2,
R_c(z)=integral_1^2 1/(z+omega²) domega-1/2,
O_c(t)/J0=-integral_1^2 cos(omega t)/omega² domega.            (4)
```

It tends to zero and integration by parts gives `|O_c/J0|<=2/t` for t>0:
the endpoint sum is5/4 and the derivative L1 norm is3/4. Its value at0+
is-1/2, from the direct contact; it is causal, not delayed or time-independent
immunity. This executes the same-source loophole with actual late relaxation.
The negative external-source contact is not a negative field energy. Making J
dynamical would change the positivity problem and is not authorized by this
argument. Finite contact realizations still leave their cosine amplitudes;
a contact can cancel S but cannot remove nonzero-frequency atoms.

## 5. Robustness and consuming scope

Static cancellation is a codimension-one condition on the readout. For
`d -> d+epsilon c`, the static/late residual is exactly epsilon/2. More
generally it is `<delta d,A^-1 c>` and is bounded by
`||delta d|| ||A^-1 c||`, where `||A^-1 c||²=7/24` here. Neither positivity
nor causality protects that tuning. A source mechanism would still need to
select the spectral measure and readout/contact, protect the cancellation,
and type the measured cosmological object. Infinite extra fields do not provide
that identification. The result refutes only an extension of the finite-mode
nonrelaxation argument to all conservative positive systems.

The next consequential conditional question is protected response under
interactions or a derived constraint, not another discretized mass band.
For source GU work the actual intervention, physical readout/contact and common
domain remain the prerequisite; no declaration of a missing input closes the
program. Scalar density stability is separately addressed by K1847.

## Validation and hostile review

Run `sage -python tests/channel-swings/k1846_continuum_screening_dephasing.py`
and `python3 tests/channel-swings/k1846_continuum_screening_dephasing_probe.py`.
The producer checks exact symbolic integrals, equations and conserved energy;
the independent rational probe checks resolvent positivity, cancellation,
polynomial moments, grouped-frequency controls and planted coefficient faults.
Finite tests do not establish the support or Fourier limit: the written
uniform-domain and Cesaro/oscillatory-integral arguments do. Inline hostile
review checks continuum versus finite modes, contact convention, homogeneous
infinite-volume energy, spectral degeneracy and conservation versus readout
convergence. No separate-agent or proof-assistant review is claimed.

Classical Fourier input: [Hart Smith, Fourier transform L1 theory](https://sites.math.washington.edu/~hart/m526/Lecture1.pdf).
Prior scoped action result: [K1844](k1844-screening-positive-response-2026-10-20.md).
