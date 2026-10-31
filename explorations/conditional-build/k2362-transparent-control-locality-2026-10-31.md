---
title: "K2362 Minimal transparent Z locality and constructive gate set"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematical and numerical results; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2362_transparent_control_locality_probe.py
---

# K2362 Minimal transparent Z locality and constructive gate set

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2362
carrier: eight physical neutral qubits per four-dual-rail logical block LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and reference-aware trace distance ON=declared_carrier
real_structure: complex positive-Hilbert amplitudes, Hermitian Pauli operators and real control envelopes
grading: physical Pauli weight, rail occupation, syndrome and logical qubit differ
action_owner: repository-construction -- supplied simultaneous many-body controls on K2356 code
target: continuous loss-transparent logical control MAP-TYPE=evaluation
```

## Result and scope

For the exact K2356 code, a nontrivial continuous logical Hamiltonian that preserves every pair excitation number and the code cannot be made exactly transparent to one pair loss using physical two-body terms alone. A three-body Hamiltonian realizes transparent logical Z, so three is the minimal physical Pauli locality under those precise premises. Explicit weight-at-most-five X and weight-at-most-six two-block ZZ then give a conditional universal logical control set. Weight five is also minimal for a transparent logical X component under these premises; the two-block ZZ weight is only an upper bound. Continuous simultaneous terms and calibrated ratios are new physical requirements; serially compiling only an endpoint does not establish transparency during the gate.

This is positive-Hilbert apparatus mathematics, not hardware realization or native GU positivity. SC-META-53 UNCERTAIN and LT-SM8 remain unchanged. [K2359](k2359-loss-during-neutral-control-2026-10-31.md) supplies the unknown-time loss obstruction and the covariance criterion. [K2356](k2356-protected-erasure-record-2026-10-31.md) supplies preparation/recovery, whose costs remain additional.

## 1. Fixed carrier and error maps

For pair i let N_i=n_qi+n_ri, z_i=(Z_qi-Z_ri)/2 and x_i=(X_qi X_ri+Y_qi Y_ri)/2. Encode outer bit b by |b,1-b>. z_i restricts to outer Z and x_i to outer X; both vanish on vacuum and double occupation. N=sum_i N_i. The outer code is

    V|b>=(|00bb>+|11,(1 xor b),(1 xor b)>)/sqrt2.

Let A_js be the one-loss map erasing pair j and recording its pre-loss outer bit s in the environment. A_js† A_js=I/2. Different j are physically flagged; at fixed j the s images are orthogonal. Transparency sufficient for ordinary end recovery is H V=V H_L and H A_js=A_js H_L, or logical-independent syndrome shifts/mixing. We construct the stronger exact identities. Equal rail damping makes the no-jump loss attenuation scalar in every occupied sector. Arbitrary unequal rail rates, dephasing and heating do not share that property.

## 2. Two-local impossibility under explicit hypotheses

Let H be a Hermitian sum of physical Pauli terms of weight<=2, [H,N_i]=0 for every pair, and H preserve the code at each instant. Average the Pauli expansion over independent pair phase rotations. Since H commutes with every N_i this leaves H unchanged, preserves physical locality, and projects onto number-conserving terms. Number conservation restricts the off-diagonal terms to exchange inside one pair; inter-pair terms are diagonal number/Z couplings. For each separate logical basis vector, its two supporting bit strings are complementary at Hamming distance four. Single-bit-flip neighborhoods are disjoint and outside all code support. Thus code preservation forces each exchange amplitude to vanish (both bit directions occur). Cancellation between outputs of different logical input columns cannot repair this condition. Diagonal H cannot induce logical X/Y.

On the occupied outer space H is c+sum h_i Z_i+sum J_ik Z_i Z_k. Put groups L={1,2},R={3,4}. For the code strings with random r, Z_i=(-1)^r for i in L and (-1)^(r+b) for i in R. Code preservation cancels r-dependent linear terms. Its logical-Z coefficient is D=sum_{i in L,k in R}J_ik. After pair j is erased, couplings involving j become at most single-site terms; average the diagonal logical coefficient over the two lost-bit syndromes s and those terms cancel. The remaining logical coefficient is D_j=sum_{i,k surviving}J_ik. Transparency up to arbitrary logical-independent syndrome energy requires D_j=D for every j. Since each cross edge survives exactly two of the four erasures, sum_j D_j=2D, whereas transparency demands4D. Hence D=0. A diagonal physical H supplies no off-diagonal syndrome mixing, so allowing such mixing in the criterion does not evade the argument. Only logical scalars remain.

This is not a no-go for gates built by non-code-preserving paths, total-number-only controls, time-resolved recovery, ancillas, higher locality or approximate error correction. Each changes a named premise.

## 3. Exact three-local Z and full-carrier cost

Define S=(z1+z2)(z3+z4), and

    Z_ET=(5-N)S/4.

On the code N=4,S=4Z_L. On a one-loss image N=3,S=2Z_L. Therefore Z_ET V=VZ_L and Z_ET A_js=A_js Z_L for all eight error maps. This is a diagonal operator on the full256-dimensional physical Hilbert space, not just a ternary truncation. With a,b singly occupied pairs in the two groups, d doubly occupied pairs, |S|<=ab and N=a+b+2d. Enumerating a,b in{0,1,2}, 0<=d<=4-a-b gives |(5-N)S/4|<=1, attained on the code. Thus ||g Z_ET||=|g|.

Let A=Zq1-Zr1+Zq2-Zr2 and B=Zq3-Zr3+Zq4-Zr4. Exact Pauli expansion is

    Z_ET=[AB+(Zq1 Zq2-Zr1 Zr2)B+A(Zq3 Zq4-Zr3 Zr4)]/16.

It has16 weight2 and16 weight3 strings, each coefficient magnitude1/16, coefficient l1 norm2. Thus physical locality3 is sufficient and, with section2, minimal for nontrivial transparent Z under the hypotheses. A whole-H norm cap is not the sum of physical drive amplitudes; both costs are exposed.

## 4. X and two-block entangling construction

Define T12=x1x2,T34=x3x4, and

    X_ET=(5-N)(T12+T34)/2.

On code both T12,T34 act as X_L; after one loss, the term touching its group vanishes and the other still acts as X_L without changing the surviving syndrome. The factors1/2 and1 in N4/N3 give the required identities on every A_js. On the full Hilbert space, max norm is3/2, attained with exactly one complete group singly occupied and the other group vacuum. Within fixed occupations T12,T34 commute, each norm<=1 when its two pairs are singly occupied and zero otherwise; the finite occupation count proves the global bound including double occupation. The Pauli expansion has8 weight4 and32 weight5 terms, l1 norm3. Weight5 is necessary for a nonzero transparent logical X/Y component under the same fixed-code and pair-number-preserving premises. For weight<=4, a matrix element flipping both dual pairs in a group consumes four physical supports, so its coefficient cannot depend on any spectator pair. Let lambda=<1|H_L|0> be the desired logical offdiagonal amplitude, and alpha_L,alpha_R the group |00> to |11> amplitudes. One lost pair in L, comparing the same-syndrome logical offdiagonal matrix elements for s=0,1, forces alpha_R=lambda and alpha_R*=lambda. Loss in R similarly forces alpha_L=lambda=alpha_L*, hence lambda is real. On the intact code, the offdiagonal matrix element is (alpha_L+alpha_L*+alpha_R+alpha_R*)/2=2lambda, but must equal lambda. Therefore lambda=0. Syndrome-only terms have zero same-syndrome/logical-offdiagonal matrix elements and cannot repair this. The explicit weight5 X attains the lower bound. General ancillas, moving-code paths or non-pair-conserving controls remain outside the theorem.

For two independent encoded blocks define ZZ_ET=Z_ET^(A) tensor Z_ET^(B). Norm1, Pauli weight<=6 and coefficient l1 norm4. It acts as logical ZZ on the product code and on every image with at most one erased pair PER block. The tensor factor proof includes losses during the entangling pulse. It does not cover two losses in one block. Arbitrary single-logical-qubit X/Z plus entangling ZZ generate the usual universal gate set on the encoded inputs; this is a Hamiltonian/control algebra statement, not a complete fault-tolerant computer.

For simultaneous aX_ET+bZ_ET, covariance is linear and norm<=3|a|/2+|b|; no optimal joint norm claim. For a generator of norm c, logical angle theta and whole-H cap G and slew V, a zero-endpoint pulse has duration2sqrt(c theta/V) when theta<=G²/(cV), otherwise c theta/G+G/V. Use c=1 for Z/ZZ and c=3/2 for X; this is not multiplication of the old duration by c. Actual simultaneous Pauli drives must track the displayed coefficients continuously. Their synthesis errors, noise and source costs are separate.

## 5. Noise follow-through

Under independently matched amplitude damping, pair loss probability p=1-exp(-gamma T), exact continuous transparent controls preserve zero/one-loss correction during a gate. One-block bad-event probability is B(p)=6p²-8p³+3p⁴. For a two-block ZZ gate it is1-[1-B(p)]² under independent block noise. The reference-aware half-diamond error is bounded by this bad-event probability for ideal recovery because the success branch is the intended channel and event probabilities are logical-state independent. At p=.1 these upper bounds are.0523 and.10186471. Add preparation, recovery/readout and control error debts; do not call these complete instrument errors. Correlated blocks allow a union bound at most B_A+B_B only if the respective marginal assumptions hold; arbitrary correlated common resets require their own model. Phase noise, unequal rails and two losses in one block are explicit scope failures, not silently priced by this erasure polynomial.

Exact tests use all256 physical basis states, every code and single-loss column, complete occupation blocks, physical Pauli coefficient counts and changed-control counterexamples. Written locality, trajectory and channel arguments carry the universal statements. The transparent-control concept and general body-locality restrictions are established prior art: [Vy, Wang and Jacobs](https://arxiv.org/abs/1210.8007). The present claims concern this specified dual-rail loss code and conservation premises; no novelty or device certification is asserted.
