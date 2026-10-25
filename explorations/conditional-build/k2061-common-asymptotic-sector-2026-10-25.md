---
title: "K2061: Exact and approximate common positive asymptotic states"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: mass-pulse conditional graph only; no universal physical-state obstruction or GU verdict
scripts:
  - tests/channel-swings/k2061_common_asymptotic_sector.py
  - tests/channel-swings/k2061_common_asymptotic_sector_probe.py
---

# K2061: Exact and approximate common positive asymptotic states

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
result: trivial continuum common positive sector, resonant finite-volume exceptions and dense nonclosed mixing range
carrier: complexified real1408 massive observed graph on R3 or a three-torus LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed universal positive metric transported to standard L2 ON=declared_observed_graph
real_structure: real skew mass generator and complex Hilbert evolution
grading: free energy signs, not source fermion parity
action_owner: repository-construction -- K2058 and K2060 fixed graph
target: intersection of incoming and outgoing positive subspaces MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] For every nonzero rectangular mass perturbation of positive duration in K2060's fixed massive graph on R3, the incoming-positive and outgoing-positive subspaces have intersection {0}. Nevertheless normalized positive incoming states can have arbitrarily small outgoing negative norm. The mixing operator has dense, nonclosed range. This is an exact compatibility obstruction, not a positive lower bound on leakage. A torus has actual zero and resonant modes instead. Smooth compact-time pulses with the same trivial-intersection property also exist.

This consumes K2060's exact pulse formula rather than recounting it as new. K2060 proved that the subspaces need not coincide; noncoincidence alone does NOT imply zero intersection. The zero-set and direct-integral argument below is the extra input. K1896 already supplies local-phase CAR obstructions; none is claimed again here. Ordinary mass-quench mixing is established literature, for example [Alves and Camilo, Momentum-space entanglement after smooth quenches](https://doi.org/10.1140/epjc/s10052-019-6581-2). The present claim is the stated conditional one-particle subspace theorem, with no novelty or quantization claim.

## 1. One frozen carrier and the common-state question

Use K2060's actual graph, with real symmetric C_j and real skew M satisfying the four Clifford relations, beta=-iM, mu>0, and

    H0(p)=C.p+mu beta, E0=sqrt(|p|^2+mu^2), P=(I+H0/E0)/2.

The fixed positive metric commutes with these matrices; its constant square-root isometry reduces to standard L2. The total fiber dimension is1408 and each energy fiber has complex dimension704. A mass pulse V=lambda beta is in the admitted real-skew generator class W=lambda M. Take lambda!=0 on [0,tau], tau>0, and zero elsewhere. With free factors stripped, scattering has the same off-block singular values as U=exp(-i tau H1), H1=C.p+(mu+lambda)beta. Free factors preserve both sectors, so they do not change intersection dimensions or leakage norms.

At the incoming endpoint define

    C_common = Ran(P) intersect S^*Ran(P) = ker(B),
    B=(I-P) S P : Ran(P) -> Ran(I-P).

The equivalence is for incoming positive vectors. It is not a claim about all states with positive expectation value, an interacting vacuum, a BV quotient, or a source-selected domain. SC-OP-04/05 supply candidate grammar/rivals, SC-META-53 is UNCERTAIN about positivity, and SC-META-56 DISAVOWS the odd-action prerequisite. LT-SM8/LT-GR6b retain their existing debts. These sources do not select this fixed free-energy criterion.

## 2. Exact singular values and continuum intersection

Clifford anticommutation gives K2060's already-derived identity

    B(p)^* B(p)=rho(r) P(p), r=|p|,
    rho(r)=lambda^2 r^2/(r^2+mu^2)
             * sinc_tau(sqrt(r^2+(mu+lambda)^2))^2,
    sinc_tau(E)=sin(tau E)/E, sinc_tau(0)=tau.          (1)

The corresponding identity BB^*=rho(I-P) holds too: the off-diagonal block of beta is invertible between the equal-dimensional fibers for r>0, and its two squared products equal r^2/E0^2 times the relevant projector. Free factors are unitary on those fibers.

For r>0, rho vanishes only at the discrete radii

    sqrt(r^2+(mu+lambda)^2)*tau = n*pi, n=1,2,... .    (2)

At r=0 it vanishes because beta commutes with H0(0). If mu+lambda=0, the apparent zero denominator is removable, not an additional shell. The union of {0} and the spheres(2) has three-dimensional Lebesgue measure zero. Therefore

    ||B psi||^2 = integral rho(|p|) ||psi_hat(p)||^2 dp =0
    implies psi=0 in L2(R3,C1408).

Plane waves on a resonance sphere are distributions, not counterexamples in L2. No assumption about a chosen spin polarization is hidden here: (1) holds on all704 positive fiber directions. This proves C_common={0} for every nonzero lambda and every tau>0 in this pulse family.

## 3. Approximate compatibility and instability of exact intersection

Using |sin(tau E)|<=tau E and E0>=mu,

    sqrt(rho(r)) <= |lambda| tau r/mu.                (3)

For any epsilon>0 take a nonzero smooth Fourier bump in 0<|p|<epsilon times P(p)e for a fixed vector e with P(0)e!=0, then normalize. This gives smooth Schwartz states with

    ||B psi|| <= |lambda| tau epsilon/mu.

Thus inf over unit positive states is zero even though the kernel is trivial. Since ker(B^*)={0} by the second identity in section2, the range of B is dense in the negative sector. Since an injective bounded operator with closed range is bounded below, its range is not closed. This is an ill-conditioned exact inverse problem; it is not an experimentally uniform negative prediction.

Duhamel also gives ||S-I||<=|lambda|tau, hence

    ||S^* P S-P||<=2|lambda|tau.

The norm distance can be arbitrarily small while the exact intersection remains zero. There is no contradiction: two close infinite-dimensional subspaces can have no common nonzero vector. The construction uses approximate states spread in position space; K2060's massive compact-support obstruction remains intact.

On any compact radial annulus avoiding the resonant radii, continuity makes rho_min>0. A normalized positive state entirely supported in that annulus instead satisfies ||B psi||>=sqrt(rho_min). This restricted bound has an explicit momentum hypothesis; it cannot be promoted to a whole-space bound. More generally the norm squared outside the set {rho<=eta^2} is at most ||B psi||^2/eta^2. This quantifies the momentum concentration needed for approximate common positivity.

## 4. Finite volume is genuinely different

On a torus of side L, momenta are 2pi k/L. The exact common sector is the Hilbert direct sum of the704-dimensional positive fibers at p=0 and at lattice momenta satisfying(2). Thus its dimension is704 times the number of resonant lattice points including zero, with the count allowed to be infinite. For all tau outside the countable set

    {n*pi/sqrt(|2pi k/L|^2+(mu+lambda)^2): k!=0,n>=1},

only p=0 survives and the dimension is704. Resonant degeneracy counts momentum vectors, not just radii. No continuum theorem may discard a torus point as a measure-zero set. The lambda=0 or tau=0 control preserves the entire positive space and lies outside section2's hypotheses.

## 5. Smooth temporal pulses: a rigorous construction, not a universal claim

The trivial intersection is not an artifact of a discontinuous pulse. Set mu=1, lambda=-2, tau=pi/(2sqrt(2)). At r=1 the square pulse has rho=1 by K2060. Choose any smooth cutoff f with 0<=f<=1, support inside (0,tau), equal to1 on [epsilon,tau-epsilon], where 0<epsilon<min(tau/2,1/8). Define V_smooth=-2 f(t) beta. The L1 operator-norm difference from the square pulse is at most4epsilon<1/2. Duhamel implies the smooth off-block singular amplitude at r=1 is greater than1/2.

For each r>0, rotate the momentum direction by the Clifford representation and use the two-generator algebra spanned by C.n and beta. It is a direct sum of identical two-dimensional Pauli systems, so every spin/multiplicity block has the same transition amplitude up to fixed basis choices. The finite-time propagator for h_r(t)=r sigma_1+(1-2f(t))sigma_3 is entire in r by the uniformly convergent time-ordered integral series on compact complex r sets. The free eigenvectors can be chosen real analytic for r>0. Hence its off-block scalar amplitude is real analytic there and is not identically zero because of r=1. Its zeros are isolated on (0,infinity). Rotational invariance then again makes the zero set a countable union of spheres plus the origin, of measure zero. The same zero-intersection and dense/nonclosed-range conclusions follow; near r=0 the amplitude tends to zero by continuous dependence and exact decoupling at zero.

More generally this argument applies to any compact-time scalar mass profile for which one proves nonzero transition at a single positive radius. It does NOT assert that every nontrivial smooth profile mixes; reflectionless or echo constructions require their own test. Mere small operator-norm perturbation of an arbitrary infinite-dimensional projection pair would not preserve trivial intersection. Here analyticity plus identical Pauli blocks supplies the missing justification.

## 6. Controls, scope and successor

The producer uses an exact four-dimensional Clifford representation and rational unit-circle propagation coefficients, including the full-transfer point; it pins the existing1408 graph evidence. The separate probe uses two-dimensional Pauli blocks and exact rational projectors; coefficient, zero-set, dimension and leakage-bound faults are rejected after a clean baseline. These are algebraic controls, not numerical evidence for a measure-zero or analytic theorem. The written proof supplies the continuum, smooth-time, closed-range and finite-volume conclusions.

Strongest hostile cases retained: zero pulse, zero momentum, resonance spheres, torus atoms, reflectionless smooth profiles, approximate states and the removable E1=0 denominator. No source verdict, canon, particle-production count, CAR implementation or universal physical quotient is inferred. The next source-facing input is a separately specified physical-state/observable criterion; exact common free positivity is now excluded for this pulse family, while approximate or potential-dependent criteria remain available.
