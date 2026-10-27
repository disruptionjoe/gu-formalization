---
title: "K2148: Exact fixed-signal response of ultraviolet local parity"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional scalar mathematics; no causal apparatus, GU recovery or controller-work claim
scripts:
  - tests/channel-swings/k2148_fixed_signal_parity_response_probe.py
---

# K2148: Exact fixed-signal response of ultraviolet local parity

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
result: Exact fixed-signal response of ultraviolet local parity
carrier: massive scalar Fock space and independent record with arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: positive Fock Hilbert form and free field mean energy ON=declared_carrier
real_structure: real Cauchy smear and complex Hilbert adjoint
grading: local canonical oscillator parity, distinct from global particle or fermion parity
action_owner: repository-construction -- supplied local canonical-mode instrument
target: fixed-signal and resource-conditioned recorded-channel limit MAP-TYPE=intertwiner
```

## 1. Ask for a fixed signal, not only a quiet vacuum

[K2146](k2146-fixed-support-parity-ultraviolet-2026-10-27.md) proves small vacuum
response for f_K=c_K g cos(Kx), with fixed nonzero real smooth compact g, m>0,
and ||f_K||=1. Its observable changes with K. Here test the SAME fixed signal
against the family, including the field left after measurement and every record.
Use [K2143](k2143-local-canonical-parity-2026-10-27.md)'s supplied instrument
K_±=(I±V_f)/2, with V_f the local canonical oscillator parity. Set

    omega=sqrt(-partial_x^2+m^2), a_j=<f,omega^j f>,
    u=omega^(1/2)f/sqrt(a_1), v=omega^(-1/2)f/sqrt(a_-1),
    s=(a_-1 a_1)^(-1/2), B=|u><u|+|v><v|.                       (1)

The normalized vectors satisfy <u,v>=s, real and positive. The exact compression
of V_f to the one-particle space is

    P_1 V_f P_1 = s(I-B).                                       (2)

Thus for normalized h,

    p_-(h)=(1-s)/2+(s/2)(|<h,u>|^2+|<h,v>|^2).                 (3)

The signal increment is nonnegative, but need not be large. Vacuum/one-particle
cross elements of V vanish by global parity preservation; local parity itself
is NOT global parity.

## 2. Derivation and independent coordinate-Gaussian control

For the local Weyl characteristic function with real parameters a,b, the vacuum
factor is exp[-(a^2 a_-1+b^2 a_1)/4]. In a one-particle h it is multiplied by
1-|<h,(i a omega^-1/2 f-b omega^1/2 f)/sqrt(2)>|^2. The one-mode parity
expectation is the normalized integral of this characteristic function over a,b.
This Fourier/Wigner identity follows by inserting the coordinate kernel of parity,
(R psi)(q)=psi(-q), into the Weyl inversion formula. The Gaussian integral is
absolutely convergent here, including its quadratic factor. The mixed term is
odd and vanishes. The two Gaussian second moments are 2/a_-1 and 2/a_1,
respectively. Relative to the vacuum integral s this yields (2), first for
expectations and then by polarization. Complex h is allowed.

An independent finite-dimensional coordinate calculation checks the factors.
Let the positive frequency matrix W be diagonal, f real unit, R=I-2ff^T,
M=W+RWR. The vacuum wavefunction is proportional to exp(-x^T W x/2), and
V acts by coordinate reflection R. Gaussian integration gives

    s=2^(n/2) sqrt(det W/det M),
    (P_1 V P_1)_ij=(2s sqrt(W) M^-1 R sqrt(W))_ij.              (4)

For W=diag(1,9,4), f=(1,1,0)/sqrt(2), s=3/5 and

    B=[[1,3/5,0],[3/5,1,0],[0,0,0]],
    P_1 V P_1=[[0,-9/25,0],[-9/25,0,0],[0,0,3/5]].             (5)

The vacuum gives p_-=1/5; symmetric/antisymmetric one-particle signals give
17/25 and 8/25; a spectator gives 1/5 and (1,i,0)/sqrt(2) gives1/2.
These are exact finite oscillator controls, not spatially compact continuum models.

## 3. Every fixed one-particle signal loses its response

K2146's two-lobe Schwartz estimates imply s_K->1 and both u_K,v_K converge
weakly to zero in the one-particle L2 space. To prove weak convergence, first
restrict to any fixed bounded momentum interval: the modulated Fourier tails
vanish faster than every power after the polynomial normalization factors.
The full vectors have norm one. Approximate an arbitrary L2 test vector by a
bounded-momentum vector to finish. No energy or smoothness assumption is needed
on a fixed h for this limiting statement. Equations(2)--(3) give

    p_-(h)->0,  p_-(h)-p_vac->0.                               (6)

In particular h0=g/||g|| is a fixed finite-energy signal with Schwartz Fourier
transform. Products of its transform and either displaced lobe have integrals
smaller than any inverse power, even after omega weights. Thus

    p_-(h0)=p_vac+O(K^-N) for every fixed N.                    (7)

This is mathematical state specification, not a proved local preparation protocol.
Suppressing the baseline here also erases the named signal increment.

## 4. Consume the result in the complete recorded channel

Let C be a fixed finite-dimensional one-particle subspace and code
Ccal=C Omega direct-sum C. Compare the instrument I_f with the deterministic
positive-record identity J(rho)=|+><+| tensor rho; preserve the full output
Fock space, including code leakage, and arbitrary reference systems. Set

    q_C=(1-s)/2+(s/2)||P_C B P_C||,
    F(q)=(sqrt(4q-3q^2)+q)/2.

Then the code-restricted half diamond distance is EXACTLY

    (1/2)||I_f-J||_(diamond,Ccal)=F(q_C).                       (8)

For a pure input/reference with q=<K_->, the negative-record block has trace
norm q and the positive-record difference has trace norm sqrt(4q-3q^2).
F is increasing on [0,1]. Purification bounds mixed inputs; a maximal eigenvector
of the compressed odd effect attains q_C. This rank-two calculation REUSES the
deterministic-record specialization of
[K2133](k2133-recorded-instrument-vacuum-disturbance-2026-10-27.md), rather than
claiming new general channel-distance theory. Its new consumer is (2).

Finite-dimensionality converts weak convergence of u,v to norm convergence of
their compressed vectors. Hence q_C->0 and the full recorded channel converges
to J on every such fixed code. For C spanned by fixed Schwartz vectors, with
mu2=||g'||^2/||g||^2, the actual rate is

    q_C=mu2/(4K^2)+O(K^-4), F(q_C)=sqrt(mu2)/(2K)+O(K^-2).       (9)

Record probability alone misses the order-K^-1 field disturbance. For any
fixed odd one-particle input, comparison to ideal GLOBAL particle-parity
measurement has half trace distance at least 1-p_-(h)->1 just by the record.
This is a failure of that particular global-parity consumer, not every detector.

## 5. The moving-signal countercontrol and released work

For h_+=(u+v)/sqrt(2(1+s)), B h_+=(1+s)h_+, so

    <V>_(h_+)=-s^2, p_-(h_+)=(1+s^2)/2 ->1,
    <h_+,omega h_+>
      =(a_2/a_1+1/a_-1+2s a_1)/(2(1+s)) ~K.                  (10)

The family can detect a correspondingly ultraviolet signal. Thus (6)--(9)
are not unrestricted uniform channel convergence. The energy rises with K;
[K2149](k2149-energy-bounded-parity-limit-2026-10-27.md) tests this resource
seam for ALL mean-energy-bounded Fock inputs, beyond finite one-particle codes.
No causal controller has been built, and K2145's support/communication burden
is unchanged. The result redirects apparatus work toward a fixed named signal
and an actual local controller, rather than another quiet-vacuum sequence.

## Acceptance and inference boundary

The adjacent probe independently reconstructs finite exact identities and perturbs actual
inputs/equations after a green baseline. Finite controls are not continuum proofs; the
written arguments have independent internal specialist review. No external certification,
proof assistant, remote CI, novelty claim or physical detector construction is supplied.
Source SC-OP-04 candidate grammar, SC-OP-05/META53 uncertainty and META56 disavowal retain
their prior polarity. LT-SM8/LT-GR6b, source register, ledger0.263 and canon are unchanged.
The supplied scalar Hilbert model is not a source-selected GU quotient or fermionic grading.
