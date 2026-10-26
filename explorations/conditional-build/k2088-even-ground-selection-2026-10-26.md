---
title: "K2088: Even and neutral ground tests on the actual state class"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source-state selection, GU verdict or external certification
scripts:
  - tests/channel-swings/k2088_even_ground_selection.py
  - tests/channel-swings/k2088_even_ground_selection_probe.py
---

# K2088: Even and neutral ground tests on the actual state class

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
result: nonatomic even ground uniqueness and particle-hole neutral ground uniqueness
carrier: supplied massive complex Dirac1408 CAR on R3 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed positive Hilbert metric and gauge-invariant quasifree input ON=declared_complex_completion
real_structure: inherited b antiunitary with b squared minus identity and b H b inverse equals minus H
grading: fermion parity, charge and energy signs are separate
action_owner: repository-construction -- imported free massive dynamics and stated operational additions
target: operational state and measurement constraints MAP-TYPE=intertwiner
```

[Conditional mathematical result; accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Scope and inherited evidence

SC-OP-04 ASSERTS candidate four-independent-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite.
These calculations use the supplied positive massive CAR completion, not the source
operator (9.16). LT-SM8/GR6b, source-register, physics-ledger and canon verdicts remain
unchanged. K2021 already supplies local R0/R1; source selection and interacting
observation/action/quotient are still separate. No novelty or external certification
is claimed. The operational demands are reverse-scaffold constraints, not predictions.

## 1. Why the operational algebra matters

[K2086](k2086-ground-state-selection-2026-10-26.md) selected the sea using odd
single creation/annihilation tests and correctly left the even-only transfer open.
Here resolve that transfer on the actual infinite massive R3 model, then follow
it into the smaller charge-neutral algebra. Let H be self-adjoint, gapped,
Q=1_(H<0), and let C be a positive contraction commuting strongly with H. The input
state is gauge-invariant quasifree. Ground positivity means

    omega(A* d(A))>=0                                (1)

for every allowed polynomial A with bounded spectral support, with d=[G,·].
These spectral tests need not be strictly spatially localized. This is a full
algebraic ground criterion, not finitely many laboratory tests or passivity.
The imported H, time orientation, state class and allowed algebra remain premises.

## 2. Even algebra suffices on the nonatomic Dirac spectrum

The free massive Dirac H on R3 has no eigenvalues: in Fourier space an energy
level is a sphere (or the threshold point), a Lebesgue-null set. Suppose C has
nonzero occupation on the positive spectral subspace. There is a v with a finite
nonzero measure mu(B)=<v,C E_H(B)v> on a bounded positive interval. This measure
has no atoms because every singleton spectral projection vanishes. Split it into
two disjoint bounded intervals I,J of positive measure. Normalized projections
of v give f,g in the respective spectral subspaces, with

    n_f=<f,Cf>>0, k_f=<f,CHf>>=inf(I)n_f>0

and similarly for g. All cross contractions vanish since C commutes with E_H.
Wick's rule and d(a(f))=-a(Hf), applied to EVEN A=a(f)a(g), give

    omega(A* d(A))=-k_f n_g-n_f k_g
                 <=-(inf I+inf J)n_fn_g<0.           (2)

This contradicts(1). Apply the pair-creation argument to any nonzero hole
covariance 1-C in the negative subspace. Hence C=Q. Conversely the known sea
full-CAR ground state restricts to an even ground state. No physical ground
selector has been derived; the extra operational assumption is now weaker.

## 3. Why finite parity sectors are a real countercontrol

For two positive levels0<E1<E2, the pure state |10> has covariance diag(1,0).
The even algebra preserves parity; its cyclic odd sector contains |10>,|01>,
and H-E1 is nonnegative there. Therefore all EVEN ground tests pass although
A=a1 gives -E1<0 on the full CAR algebra. This is not a counterexample to section2:
there are atoms, so its two-positive-band construction cannot be repeated.
This example does not obey the particle-hole complement premise of section4.
Finite matrix tests alone cannot establish the nonatomic theorem.

## 4. Stronger result: neutral tests plus particle-hole symmetry suffice

Now retain the actual K2086 symmetry bHb^-1=-H and bCb^-1=1-C, b antiunitary.
Take any normalized positive-band f with n=<f,Cf>>0 and k=<f,CHf>>0; g=bf lies
in the negative band. Hole occupation of g is n; its hole-energy expectation
is -k. Cross contractions vanish by the positive/negative spectral split.
The charge-neutral, even transfer A=a*(g)a(f) yields

    omega(A* d(A))=-2nk<0.                           (3)

Thus neutral ground positivity plus this supplied particle-hole symmetry
already implies C=Q. This proof requires neither nonatomic spectrum nor a
square-plus-one real structure; b^2=-I is fully compatible. The symmetry also
turns any negative-band holes into positive-band occupation, completing the
argument. This closes a stronger conditional selector than section2.

Without the complement premise, neutral-only positivity need not select Q.
For a chemical potential mu, C_mu=1_(H<mu) is the quasifree ground covariance
of H-mu. Charge-neutral polynomials have the same dynamics under H and H-mu,
so their restricted state satisfies(1). Choose |mu|>m for a distinct sea;
inside the mass gap C_mu=Q. These rivals have

    b C_mu b^-1=1-C_(-mu)

(no level atoms in R3), not1-C_mu when |mu|>m. Do not use this example against
the symmetry-retaining theorem. It identifies exactly which premise carries
chemical-potential selection. No finite-total-energy claim is made about the
infinite-volume shifted state.

## 5. Released thermal test and remaining source bridge

At finite beta>=0, thermal positive-band occupation is strictly positive.
Equation(3) supplies a neutral witness against ground positivity for that state,
although it remains stationary, positive and particle-hole compatible. At beta>0
thermal equilibrium may be passive; ground spectrum and passivity are different
conditions. This does not make finite-temperature matter inconsistent.
For finite energy+e and partner-e with positive occupation n, the expectation is
-2e n^2. The probe checks this against full Fock matrices, including b^2=-I,
and tests an explicit shifted sea whose neutral ground property survives but
whose complement symmetry fails.

Next determine whether the source-selected observed algebra includes these
neutral transfer observables and whether its state/dynamics satisfy the stated
criterion. Neither abstract symmetry compatibility nor this theorem constructs
that bridge. No observed chirality, 2+1 count or interacting quotient follows.
