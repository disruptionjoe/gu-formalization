---
title: "K2246 Autonomous vacuum-chain reset and spatial information escape"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied mathematics; no source selection or physical recovery
scripts:
  - tests/channel-swings/k2246_autonomous_vacuum_reservoir_probe.py
---

# K2246 Autonomous vacuum-chain reset and spatial information escape

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2246 Autonomous vacuum-chain reset and spatial information escape
carrier: half-line XY vacuum Fock sector with one target qubit and arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: declared positive product Hilbert norm ON=declared_carrier
real_structure: real raw matrices or complex Hilbert adjoint as specified below
grading: local spin/fermion excitation number, not physical families
action_owner: repository-construction -- explicitly supplied operator below
target: one-input vacuum reset and finite-prefix reference channel MAP-TYPE=intertwiner
```

## Question and scope

[K2235](k2235-microscopic-thermal-renewal-2026-10-29.md) and [K2238](k2238-finite-clock-thermal-circuit-2026-10-29.md) priced finite fresh stock and a finite clock. Here a semi-infinite, time-independent local chain carries one input's quantum information away. A computable bound holds at every sufficiently late time. A finite truncation supplies a rigorous finite time window, with recurrence retained afterward.

This is one qubit initially coupled to an independent zero-temperature vacuum. It is neither the finite-temperature renewal channel of K2232 nor an indefinitely reusable input service, output-isolation mechanism, permanent finite clock halt or GU prediction. Vacuum preparation, an infinite reservoir and Hamiltonian parameters are supplied. No source/ledger/canon verdict changes.

## 1. A defined positive autonomous Hamiltonian

Let J>0, omega>=2J, sites n=0,1,..., with target at0 and bath at1,2,... . On the one-particle space l2(N0), let S be the unilateral shift and

    h=omega I+J(S+S*),  h>=0,  ||h||<=omega+2J.

Define H=dGamma(h) on fermionic Fock space with its standard selfadjoint second-quantization domain. The vacuum representation of the half-line spin chain under Jordan-Wigner gives the local XY expression

    H=omega sum n_j+J sum (sigma+_j sigma-_(j+1)+h.c.).

The Fock definition, not a formal unconverged infinite tensor sum, fixes the operator. Every edge interaction is bounded and local. H is positive; the prepared input occupies only vacuum plus one excitation, where H is bounded by omega+2J. J=0 would never reset and is excluded. With an arbitrary reference, the bath initially factors as vacuum; correlations with the target are allowed only in the reference.

## 2. Exact endpoint channel and a reference-uniform envelope

The sine transform phi_n(k)=sqrt(2/pi) sin((n+1)k), 0<k<pi, diagonalizes h with eigenvalue omega+2J cos k. Thus, for x=2Jt,

    a_n(t)=<n|exp(-ith)|0>
          =exp(-i omega t)(-i)^n [J_n(x)+J_(n+2)(x)]
          =exp(-i omega t)(-i)^n (n+1)J_(n+1)(x)/(Jt).

At t=0 the expression is understood by continuity. Bessel J notation here is unrelated to the GU volume operator. The integral and recurrence are standard [DLMF10.9.2](https://dlmf.nist.gov/10.9.E2) and [DLMF10.6.1](https://dlmf.nist.gov/10.6.E1); the chain application is derived by the displayed sine transform, with no novelty claim. In particular a=a_0=exp(-i omega t)J_1(2Jt)/(Jt). The real integral gives |J_n(x)|<=1 for integer n, so

    r=|a|<=min(1,1/(Jt)), t>0.                     (1)

Vacuum stays vacuum, and one target excitation evolves to a|1,vac>+|0,chi>, with ||chi||²=1-r² and chi orthogonal to vacuum. Tracing the bath gives the exact amplitude-damping channel. For any target/reference density matrix rho=[[A,C],[C*,B]], its difference from ground replacement is

    [[-r² B, a* C],[a C*, +r² B]].                  (2)

Block positivity gives ||C||1<=sqrt(Tr A Tr B)<=1/2. Splitting diagonal and off-diagonal matrices bounds half trace norm by r² Tr B+r||C||1<=r²+r/2. We use the simpler conservative bound

    half diamond distance to ground replacement <=min(1,r+r²). (3)

At Jt>=200, (3)<=201/40000=0.005025 for ALL later times. The excitation probability is at most1/40000. No Markov or exponential decay approximation is made. In particular this is an algebraic envelope, not a decay-rate fit, and it makes no claim of monotonicity of the exact oscillatory channel.

## 3. Information escapes every fixed spatial prefix

For L sites0,...,L-1, (1)'s general coefficient gives

    p_prefix <=sum_(n=0)^(L-1) (n+1)^2/(Jt)^2
              =L(L+1)(2L+1)/(6(Jt)^2).             (4)

This is a statement about the one-excitation propagator. With the arbitrary input/reference the prefix channel is an amplitude-damping isometry into its normalized one-particle profile; the same block argument gives half trace distance to prefix-vacuum replacement <=min(1,sqrt(p_prefix)+p_prefix). Thus correlations leave each fixed finite region, while the full unitary state retains them in the chain. Total energy is conserved; nothing is erased globally.

For L=10 and Jt>=10000, p_prefix<=385/10^8<1/250000. Hence reference-uniform prefix error<1/500+1/250000=0.002004. This consumer shows spatial export, beyond resetting only site0. It is not a repeated-input or thermal-capacity theorem.

## 4. A finite chain with a guaranteed horizon

Use M sites0,...,M-1, M>=2. Remove edge(M-1,M) from the infinite chain; its initial-left evolution equals the M-site model. Duhamel bounds the state-vector difference on |0> by the integral of J times the infinite-chain amplitude at M-1 and M. A walk from0 to n has length at least n; ||S+S*||<=2. For u>=0,

    |a_n(u)|<=exp(2Ju)(2Ju)^n/n!.

If M>=2JT+1, the n=M term is no larger than n=M-1 for0<=u<=T. Consequently

    sup_(0<=t<=T) ||(U_M(t)-U_infty(t))|0>||
      <=b_M(T)=2JT exp(2JT)(2JT)^(M-1)/(M-1)!.     (5)

Both evolutions fix vacuum, so their Stinespring isometries differ by at most b_M(T) even with arbitrary reference. The same is a half-diamond upper bound after tracing any common finite output prefix of length L<=M. Combining(3),(5) bounds finite-chain reset error on [t0,T] by 1/(Jt0)+1/(Jt0)^2+b_M(T).

Concrete dimensionless consumer: J=1, T=200, M=4001. Since n!>=(n/e)^n and e<3,

    b_M(T)<=400 exp(400)(400)^4000/4000!
             <400*3^400*(3/10)^4000 <10^(-1000).

The finite-size consumer is checked directly with integers and the factorial. On the full window100<=t<=200, a4001-site chain resets within0.0101+10^-1000, and at t=200 within0.005025+10^-1000; the general window formula applies for any t0<=T. The deliberately loose bound uses no floating-point Bessel evaluation or enormous matrix exponential.

The finite chain has finitely many frequencies in this sector, so arbitrarily good recurrence to its initial state exists. This contradicts permanent finite-chain reset, not(5)'s finite horizon. The infinite one-particle spectrum is continuous, which permits (1)'s all-later-time envelope. The distinction is mathematical and physical resource accounting, not a stopping exception.

## 5. Review, reproducibility and remaining interfaces

Finite exact controls compare path moments with the Bessel power series, finite versus infinite boundary returns, complete channel matrix units, and integer resource bounds. Changed endpoint weights, periodic versus open boundary, bulk versus endpoint propagator, omitted reference coherences, conjugated phase, excited bath input, and insufficient reservoir length are actual-input faults. The continuous spectral and arbitrary-reference arguments remain written proofs, independently reviewed rather than certified by samples.

The next useful work must handle repeated injections with correlations, a finite-temperature bath and the intended Gibbs fixed point, or output extraction/renewal with a resource account. This construction explicitly supplies spatial escape for one vacuum input and a finite-size approximation. It does not establish those other apparatus functions.

## Reproduction and evidence kinds

Run `python tests/channel-swings/k2246_autonomous_vacuum_reservoir_probe.py`. `--write` refreshes the report; default execution recomputes finite controls and input faults and rejects stale note/code/dependency hashes. Universal proofs are internally reviewed mathematical arguments, distinct from finite controls and reporting integrity. No external-expert, proof-assistant, remote-CI, hardware or novelty certification.
