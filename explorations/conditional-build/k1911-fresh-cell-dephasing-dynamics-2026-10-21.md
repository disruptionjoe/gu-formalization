---
title: "K1911: Fresh quantum cells with explicit error, drive and energy"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite quantum models; no native GU identification, total thermodynamic cost, or novelty
scripts:
  - tests/channel-swings/k1911_fresh_cell_dephasing_dynamics.py
  - tests/channel-swings/k1911_fresh_cell_dephasing_dynamics_probe.py
---

# K1911: Fresh quantum cells with explicit error, drive and energy

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
result: three-state cell realization, certified process limit and finite nonclassical circuit
carrier: four-level system and specified finite-dimensional environment LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=conditional_target
real_structure: ordinary complex conjugation; native K/C not identified
grading: population labels; no source graded-IG identification
action_owner: repository-construction -- explicit controlled unitary interactions
target: conditional coherence dynamics and bath resource constraints MAP-TYPE=intertwiner
```


## 1. A concrete reservoir model

[K1910](k1910-minimal-dephasing-bath-energy-2026-10-21.md) excludes a bounded
regular start and an autonomous finite reservoir for the exact Poisson
semigroup. It does not exclude repeated fresh cells. Here the reservoir is
an ordered supply of independent qutrits, one per time step, initially in
|vac>. Control timing and cell preparation are supplied. No spatial field,
relativistic transport, thermal preparation or clock cost is derived.

Use K1903's channel convention C_jk=<e_k,e_j>, with

    e1=(1,0), e2=(0,1), e3=(1,1)/sqrt2, e4=(1,-i)/sqrt2.

For 0<h<1 define qutrit vectors and a controlled unitary by

    f_j(h)=sqrt(1-h)|vac>+sqrt(h)e_j,
    U_h=sum_j |j><j| tensor exp[-i theta K_j],
    K_j=i(|e_j><vac|-|vac><e_j|), theta=arcsin(sqrt(h)).   (1)

The event subspace C^2 is orthogonal to |vac>. K_j is Hermitian, has
norm1, and K_j^2 projects onto span(vac,e_j). Thus its exponential maps
vac exactly to f_j, and leaves the orthogonal direction fixed. Discarding
that cell implements

    Psi_h=(1-h)Id+h Phi_C,
    D_h=(1-h)J+h C.                                      (2)

Three pure-bath dimensions are necessary and sufficient for this exact
step. The displayed Gram vectors give rank at most3, while the leading
3-by-3 minor is h^2(1-h)(3-2sqrt2)>0. At h=0 the rank is1;
at h=1 it is2. These endpoint exceptions are not omitted.

Repeated-interaction limits and singular coupling scaling are established
frameworks: [Attal and Pautrat](https://arxiv.org/abs/math-ph/0311002) and
[Attal and Joye](https://arxiv.org/abs/math-ph/0501012). The following direct
calculation specializes them without importing a continuum reservoir theorem.

## 2. Uniform operational error, including entangled inputs

After n independent cells, the reduced map is Psi_h^n and the coefficient
matrix is D_h raised ENTRYWISE to power n. Set t=nh. The target is

    T_t=exp[t(Phi_C-Id)], F_jk(t)=exp[t(C_jk-1)].           (3)

These are binomial and Poisson mixtures of the same channel powers.
For one step the l1 distance of Bernoulli(h) and Poisson(h) is exactly
2h(1-exp(-h))<=2h^2: compare the mass at0, at1 and above1 separately.
Each channel power has diamond norm1, so a mixture difference is at most
its l1 coefficient difference. Telescoping n contractions yields

    ||Psi_h^n-T_t||_diamond <=2nh^2=2t h.                 (4)

This bound includes arbitrary reference-system inputs; it is not an
entrywise-to-diamond guess. A coupling of the classical event counts gives
the same estimate. The finite chain is an approximation at grid times;
no finite h is declared the exact continuous semigroup. For t/n<1 the
bound is2t^2/n and tends to zero uniformly on bounded grid-time intervals.

## 3. Drive and emitted energy are different resources

A constant Hamiltonian theta K_j/h over each cell interval realizes (1).
Its norm is theta/h~h^(-1/2). Smooth pulses flat at interval boundaries
also work exactly: multiply K_j by a nonnegative smooth envelope of integral
theta. For a fixed normalized pulse shape their peak has the same scaling.
Include any specified free bath Hamiltonian by interaction-picture
conjugation; its finite norm adds only a bounded term to a lab-frame control.

This divergence is necessary in order, though our constant is not asserted
optimal. Let A_h be the integrated operator norm of a common control producing
this step from a pure cell, with free phases removed. Each conditional bath
ray can move at most A_h in projective angle from its initial ray. Since
|<f2,f1>|=1-h, the triangle inequality gives

    A_h >= (1/2) arccos(1-h) ~ sqrt(h/2).                 (5)

For general joint controls with the required population-fixed endpoint, the
same bound follows by applying the ray-speed bound to each basis input and
its final product vector. A finite peak M implies A_h<=Mh, so a family with
uniformly bounded M cannot realize these exact steps as h tends to zero.
Our construction uses A_h=arcsin(sqrt(h)); it matches the exponent, not the
best prefactor. For constant peak M the exact necessary inequality is
2Mh>=arccos(1-h), rather than an asymptotic equality.

Give each qutrit Hamiltonian H_E=omega(I-|vac><vac|). In the displayed
orientation every outgoing cell has excitation probability h, for every
input population. Therefore n cells emit exactly omega n h=omega t in
mean endpoint excitation. Cells may be mutually correlated through the
system, but additivity of the sum of cell Hamiltonians still makes this
energy sum valid. With diagonal system energy unchanged and interactions
off at endpoints it equals control work on system plus cells, excluding
cell preparation, reset, clock and transport.

K1910's passive rearrangement also gives the population-adapted minimum
for each step: omega[1-lambda_max(sqrt(p)D_h sqrt(p))]. Its small-h slope is

    alpha(p)=1-||sum_j p_j e_j||^2,
    alpha(uniform)=(11-3sqrt2)/16.                       (6)

The eigenvalue1 at h=0 is simple; finite analytic perturbation gives (6).
A common output rotation attains this energy without changing the channel.
For fixed p the n-cell total tends to omega t alpha(p); this optimized
orientation depends on p and is not a universal worst-input optimum.
A ground eigenvector near vac differs by O(sqrt(h)); its rotation adds
O(sqrt(h)) integrated control, so optimization retains the same scaling.
No optimal control prefactor or preparation/reset minimum is claimed.

## 4. Released finite circuit, with no limit required

K1909 already proves the output T_(1/110)(|+><+|) is at trace distance
strictly greater than1/176000 from every classical-phase output. Its
certificate and scope are reused, not independently recounted as a new proof.
Take t=1/110, n=15, h=1/1650. Equation(4) gives output trace-distance error
at most t h=1/181500. Thus this explicit fifteen-qutrit circuit remains
separated from every classical-phase channel by at least

    1/176000-1/181500 = 1/5808000                        (7)

on the equal-superposition input (strict inequality inherited from K1909).
It uses finite drives, total simple-orientation energy omega/110, and no
infinite reservoir at this fixed endpoint. The small certified margin is a
sufficient error budget, not an optimum. The unitary collision is quantum;
a classical Bernoulli event count does not make the channel classical phase
noise. This distinction is the actual operational consumer of (4).

## 5. Hostile review

Strongest overclaim: describing a finite chain as exact all-time dynamics or
as a local field bath. Neither follows. Strongest contrary construction:
unit-phase collisions are classical at every n; reset-free reuse is outside
the fresh-cell hypothesis. Weakest seam: complex Gram orientation and
confusing diamond distance with its half-distance convention. The producer
constructs all qutrit rotations and step Grams, while the separate probe uses
channel Kraus diagonals and direct binomial expansion. Equation(4) is analytic.
The exact fifteen-cell margin and a wrong-sign Gram control test the consumer.


## Source and verification boundary

SC-OP-04 ASSERTS a candidate four-field operator grammar, SC-MAS-01 and
SC-CHI-02 ASSERT the stylized curvature-mass toy, and SC-META-53 remains
UNCERTAIN about unbounded spectra. None selects these positive Hilbert bath
models, their accessible algebra, coupling, clock, spectrum or physical units.
LT-SM8, LT-GR6b and AC-F1 remain unchanged. Full20 injection, separate K/C,
physical domain and accessibility are independent construction debts.
No source/physics-ledger/canon verdict, GU recovery, novelty, external expert
review or formal proof is claimed. General statements rest on the analytic
arguments above; exact probes check finite matrices and identities, while
report and pin faults test only consistency and provenance.
