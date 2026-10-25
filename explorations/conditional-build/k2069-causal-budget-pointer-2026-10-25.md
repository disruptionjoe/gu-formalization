---
title: "K2069: Causal-budget pointer and kinetic-calibration rigidity"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional massive graph with imported homogeneous controls; no source apparatus or spacelike laboratory
scripts:
  - tests/channel-swings/k2069_causal_budget_pointer.py
  - tests/channel-swings/k2069_causal_budget_pointer_probe.py
---

# K2069: Causal-budget pointer and kinetic-calibration rigidity

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
result: causal-budget pointer construction, sharp displacement-gap frontier and kinetic-calibration rigidity
carrier: massive complex1408 graph H_D,+ tensor C352 on R3 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert metric and imported Born rule ON=declared_observed_graph
real_structure: complex completion; source-real admissibility of the apparatus remains unproved
grading: energy sector and supplied multiplicity qubit, not source parity
action_owner: repository-construction -- K2067 massive graph with explicitly modified kinetic coefficients
target: fixed-cone prepared-qubit position measurement MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] The same prepared pointer and Bell readout as
[K2067](k2067-sector-preserving-pointer-control-2026-10-25.md) can be implemented with
maximum full-carrier propagation speed1 and a strictly positive energy-sector gap.
It costs a changed common kinetic coefficient and a longer measurement time. This
removes the enlarged-cone cost of that particular construction; it does not preserve
the calibrated free generator during the pulse. An exact theorem below explains why
that distinction matters: a speed-one Hermitian principal symbol with unchanged free
kinetic trace calibration must equal the free symbol. With exact intermediate-time
sector preservation, the remaining bounded local controls are readout-blind.

No local laboratory, compact positive-energy preparation, source-real apparatus,
physical quotient, GU prediction or novelty is inferred. Generic controlled
translation and time rescaling are prior structure, explicitly reused.

## 1. Fixed object and conditional ownership

H0=alpha.D+m beta on L2(R3,C4 tensor C352), m>0; P=1_(H0>0).
The four Hermitian Clifford matrices obey the usual anticommutation identities.
Choose C352=C2 tensor C176 and a Pauli Z on C2. This is exactly K2067's declared
complex Hilbert graph, not a new identification with the source's real/bar structure.
SC-OP-04 ASSERTS a candidate four-field grammar; SC-OP-05 is UNCERTAIN about rival
southeast maps; SC-META-53 is UNCERTAIN about physical positivity; SC-META-56 DISAVOWS
an odd-action prerequisite. These statements supply neither this control nor the
Born/tensor/preparation assumptions. LT-SM8/GR6b, source register, ledger and canon
remain unchanged. The question is a reverse operational compatibility calculation.

K2062 already classifies bounded local coefficients preserving P; K2067 already
constructs the Gaussian-spinor pointer, proves its variance bound and gives the
prepared-subspace Bell readout. They are hash-pinned dependencies, not new results.
The new discriminator is the conjunction of the original cone bound and an explicit
kinetic-calibration requirement.

## 2. Causal-budget family and exact domains

For constants a>|b|>=0 take

    H_(a,b)=a H0+b D1 Z.

It commutes with P, and on Ran P its eigenvalues are a E_p +/- b p1. Minimizing over
p gives the sharp lower edge m sqrt(a^2-b^2). Transverse momentum only raises E_p;
in the remaining variable the minimum occurs at |p1|=m|b|/sqrt(a^2-b^2).
Wavepackets concentrated there prove sharpness. The full-carrier absolute eigenvalues
are bounded between (a-|b|)E_p and (a+|b|)E_p, so its self-adjoint Fourier-multiplier
domain is H1. At a=|b| this graph-norm assertion fails; for a<|b| the positive-sector
Hamiltonian is unbounded below. These boundary cases are not included.

For unit n, the principal eigenvalues are +/-a +/-b n1. Therefore its full-carrier
maximum directional speed is a+|b n1|, and the Euclidean speed bound is a+|b|.
The first-order symmetric-hyperbolic energy estimate gives finite propagation inside
that cone; equivalently factor free propagation of duration aT and translations
+/-bT. Thus

    a>|b|,  a+|b|<=1                                  (1)

simultaneously preserves the same P, positive energy and the original speed-one
upper cone. It does NOT preserve the original kinetic calibration a=1.

Take a=2/3,b=1/3,T=30/m. Then the gap is m/sqrt(3), the maximum speed is1, the common
free duration aT is20/m, and pointer displacement bT is10/m. This Hamiltonian is
exactly two thirds of K2067's lambda=1/2 Hamiltonian and acts for three halves of its
time. The final unitary and original prepared state are identical. Time rescaling is
not a new measurement principle; making its changed physical clock calibration
explicit prevents it being mistaken for preservation of every old assumption.

For K2067's normalized spinor Gaussian with momentum variance s^2=m^2 per coordinate,
prepare exp(iH0*20/m)phi. The same proven spatial variance is at most17/(4m^2).
Reading the sign of x1 yields a qubit error epsilon<=17/400. With a multiplicity
singlet, common preparation and the four specified Pauli axes, all outcomes give

    CHSH >= 2 sqrt(2) (183/200)^2 >2.                  (2)

Mean free energy remains <=2m. Hilbert positivity, this Bell expression and the
full-carrier propagation estimate do not make the spatially homogeneous controls
into two spacelike-local laboratories.

## 3. Sharp displacement versus uniform spectral gap

Require an instantaneous positive-sector gap at least gamma*m, 0<gamma<1, while
retaining(1). Since a<=1-|b|,

    gamma^2 <= a^2-b^2 <= 1-2|b|,
    |b| <= (1-gamma^2)/2.                            (3)

Equality is realized by a=(1+gamma^2)/2, |b|=(1-gamma^2)/2.
For any time-dependent member of this family with the same uniform gap,

    |J|=|integral_0^T b(t)dt| <= T(1-gamma^2)/2.       (4)

This is the sharp time cost for a required displacement J in this family. It is
not a necessary minimum time for every possible measurement, nor does Chebyshev's
sufficient error bound establish the optimal discrimination error. Gamma=1 forces
b=0. A prescribed nonzero gap therefore limits how rapidly the pointer can move
while the full characteristic cone remains bounded by the original cone.

Smooth switching is possible. Choose b(t) smooth, zero outside the pulse,
0<=b<=bmax<1/2, and a(t)=1-b(t). All operators at different times commute, their
common H1 domain has a uniform graph-norm bound, and

    U(T,0)=exp(-iH0 integral a) exp(-iD1 Z integral b).

The same preparation uses integral a, and the same error uses J=integral b.
Bounded multiplicity rotations before the pulse choose each axis; equal durations
and free waiting preserve the common preparation. Smooth ramps approach the constant
frontier in(4) but do not attain it if nonzero ramp intervals are imposed. No
instantaneous, setting-dependent preparation is hidden in this statement.

## 4. Exact calibration rigidity, beyond the chosen family

Let C(n)=alpha.n tensor I352, N=1408. For any Hermitian matrix A(n) with
||A(n)||<=1 define the normalized kinetic trace deficit

    delta(n)=1-Re Tr(C(n)A(n))/N.

Since C(n)^2=I and Tr A(n)^2<=N,

    0<=||A(n)-C(n)||_HS^2
       <=2N delta(n),
    ||A(n)-C(n)|| <=sqrt(2N delta(n)).                (5)

In particular delta(n)>=0 and delta(n)=0 forces A(n)=C(n). No assumption that
A commutes with C is needed. Checking delta(ej)=0 for the three coordinate directions
already fixes every coefficient of a linear first-order principal symbol.

Apply this pointwise to a symmetric first-order local Hamiltonian with Hermitian
principal matrices A_j(t,x), a speed-one symbol bound, and exactly unchanged free
trace calibration in each direction. It forces A_j=alpha_j. If its remaining
potential relative to H0 is bounded, Hermitian, locally time-integrable and preserves
Ran P under every two-sided propagator, K2062 forces that potential to be spatially
constant in the Clifford commutant. K2067 then makes the scalar-position POVM at a
common final time readout-blind. This class-level calibrated restriction includes
variable principal coefficients before imposing the hypotheses. It is not a theorem
about final-time-only echoes, unbounded potentials, nonlocal generators or a changing
projector. Equation(1) evades the calibrated hypothesis openly: delta(ej)=1-a.

## 5. What approximate calibration actually controls

An arbitrarily small principal coefficient error is unbounded on the unrestricted
momentum space. Do not turn(5) into a uniform unitary or measurement norm estimate.
There is a useful energy-conditioned statement for spatially constant coefficients.
Suppose actual and readout-blind reference propagators have a common H1 domain,
reference generator H0+B0(t) with B0 a bounded Clifford commutant, and

    H-H_ref=sum_j (A_j-alpha_j) D_j + W(t),
    ||W(t)||<=kappa(t).

For a normalized preparation with ||D_j psi||<=K_j, Duhamel and commutation of
D_j with the reference evolution give

    ||(U-U_ref)psi||
       <= integral [sum_j sqrt(2N delta(ej,t))*K_j+kappa(t)]dt = r. (6)

The corresponding difference in any effect probability is at most min(1,r), by the
pure-state trace-distance bound. The same bound holds uniformly on a common prepared
qubit subspace when the K_j bounds hold there, including ancillary purification.
Hence K2065's prepared-observable resource inequality gives
CHSH<=min(2sqrt(2),2+4sqrt(r_0^2+r_1^2)) when Alice's two prepared settings meet these
bounds and the reference is the common readout-blind POVM. For the Gaussian, K_j=s.
This is a finite-preparation bound, not a universal field-observable identity.

## 6. Proof, controls, scope and next test

The written spectral minimization, Fourier domain argument, hyperbolic factorization,
trace inequality and Duhamel estimate carry the continuous and class-wide claims.
The producer passes36 finite exact Clifford, characteristic, resource and matrix
controls. The separate probe passes21 rational resource controls and detects five
corruptions of cone, gap, translation, probability and Bell data after a passing
baseline. No finite count certifies the analytic theorem by itself. Same-author
checking only; no independent specialist, proof-assistant or external certification.

Strongest overclaim rejected: full-carrier finite propagation is not compactly
localized positive-energy preparation or operational spacelike locality. Positive
energy localization issues are established prior literature; see Hegerfeldt,
[Causality, particle localization and positivity of the energy](https://arxiv.org/abs/quant-ph/9806036).
Our Gaussian already has tails, and the full Dirac carrier has both energy signs.
No contradiction or novel evasion of that result is claimed.

The next meaningful apparatus question needs spatially confined control and an
explicit approximate-sector or detector-field criterion on the same preparations.
Repeating a homogeneous speed rescaling cannot provide that locality bridge. Exact
calibration and exact sector preservation have the stated restriction; changing
those assumptions defines the next construction explicitly.
