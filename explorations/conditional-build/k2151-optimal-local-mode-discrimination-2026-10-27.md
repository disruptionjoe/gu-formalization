---
title: "K2151: Optimal fixed local-mode signal discrimination"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no full raw rigidity, continuum apparatus or GU recovery
scripts:
  - tests/channel-swings/k2151_optimal_local_mode_discrimination_probe.py
---

# K2151: Optimal fixed local-mode signal discrimination

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
result: K2151: Optimal fixed local-mode signal discrimination
carrier: massive scalar Fock space, one canonical oscillator, fixed one-particle signal LAYER=toy CHIRALITY=N/A
pairing: positive global vacuum Hilbert form ON=declared_carrier
real_structure: real coordinates or complex Hilbert adjoint as declared
grading: oscillator number and parity, not GU or fermion parity
action_owner: repository-construction -- supplied conditional objects below
target: single-mode discrimination ROC and recorded vacuum disturbance MAP-TYPE=intertwiner
```

## 1. Freeze the signal and optimize the measurement

[K2148](k2148-fixed-signal-parity-response-2026-10-27.md) computes parity response;
[K2149](k2149-energy-bounded-parity-limit-2026-10-27.md) excludes useful fixed-energy
response from its ultraviolet limit. Here fix ONE real normalized smooth compact
smear f, mass m>0, omega=sqrt(-∂x²+m²), and a_j=<f,omega^j f>.
Set nu=sqrt(a_1/a_-1), Q=phi(f), P=pi(f), [Q,P]=i and

    b=(sqrt(nu)Q+iP/sqrt(nu))/sqrt(2),
    x=(sqrt(nu)omega^-1/2+omega^1/2/sqrt(nu))f/2,
    y=(sqrt(nu)omega^-1/2-omega^1/2/sqrt(nu))f/2.

Then b=a(x)+a†(y), <x,y>=0, ||x||²=N+1, ||y||²=N, where
N=(sqrt(a_1 a_-1)-1)/2. For N>0 put h=x/sqrt(N+1), j=y/sqrt(N),
z=N/(N+1) in(0,1). Freeze the hypotheses as global vacuum Omega versus
psi=a†(h)Omega. This h is exactly K2148's h_+, but f and h do not change during
this test. All moments and signal energy are finite. The case N=0 has the obvious
pure-oscillator vacuum/one-particle limit; nonzero compact continuum f cannot have
N=0 since equality in Cauchy--Schwarz requires an omega eigenvector in L2.

The allowed effects belong to the SINGLE oscillator algebra B(F_b) tensor I,
not the full algebra of the spatial support. Optimality below is only over that
algebra. The whole-region detector can use additional modes.

## 2. Exact reduced distributions from the actual global vacuum

The companion c=sqrt(N+1)a_j+sqrt(N)a_h† commutes with b and satisfies CCR.
The two-mode Bogoliubov inverse is a_h=sqrt(N+1)b-sqrt(N)c†. In the b,c basis,

    Omega=sqrt(1-z) sum_(n>=0) z^(n/2)|n,n>,
    psi=sqrt(1-z)b†Omega.

The inverse annihilates the displayed vacuum, fixing both normalization and
squeeze convention. Spectator modes factor. Partial trace gives commuting states

    p_n=(1-z)z^n,
    q_0=0, q_n=n(1-z)² z^(n-1) for n>=1.                       (1)

This is the photon-ADDED thermal distribution. Choosing a_j†Omega instead
produces (n+1)(1-z)²z^n, a different global signal; the distinction matters.

For any effect E, only e_n=<n|E|n> in[0,1] enters its two probabilities.
Conversely every such diagonal sequence is an effect. Thus optimizing all POVMs
reduces exactly to a classical likelihood problem; offdiagonal measurements
cannot help for these two states. This derivation supplies the actual object
needed for the standard likelihood-threshold argument.

## 3. Entire optimal tradeoff and equal-prior error

The likelihood q_n/p_n=n(1-z)/z increases with n. To maximize detection at fixed
false-click probability alpha, allocate e_n first to highest n. An exchange of
effect weight between two unequal likelihoods proves this rule; finite truncations
and monotone tail convergence give the infinite countable result. The exact ROC
is the polygonal interpolation of the deterministic thresholds n>=k:

    alpha_k=z^k,
    eta_k=z^(k-1)[k-(k-1)z], k>=1,                            (2)

and the endpoints(0,0),(1,1). Randomizing the boundary occupation k by t in[0,1],
with clicks for n>k, gives

    alpha=z^(k+1)+t(1-z)z^k,
    eta=z^k[(k+1)-kz]+t k(1-z)²z^(k-1).                     (3)

For the last segment k=0 use eta=1, alpha=z+t(1-z). No formula with z^-1
at z=0 is needed. The equal-prior optimum clicks where q_n>p_n:

    k=floor(N)+1,
    TV=k(1-z)z^(k-1), P_error=(1-TV)/2.                       (4)

At integer N the occupation n=N is a tie and may be assigned or randomized freely.
The chosen k excludes the tie. Directly summing positive q_n-p_n gives(4).
As N->0 the error tends0; as N->infinity, k/N->1 and TV->exp(-1), so the
error tends(1-exp(-1))/2. These are changing-mode/noise families, not claims
that one fixed apparatus tunes its vacuum covariance freely.

For the exact inherited oscillator control W=diag(1,9,4), f=(1,1,0)/sqrt2,
nu=3, N=1/3, z=1/4 and k=1. The optimum has alpha=1/4, eta=1 and
P_error=1/8. Parity instead has alpha=1/5, eta=17/25 and P_error=13/50.
The threshold accepts more vacuum clicks but improves equal-prior error. Its
false-click constrained advantage is fully described by(3); no objective is
silently changed.

## 4. Consume the quiet-vacuum limit in the full record

At a deterministic threshold alpha=z^k,

    eta=alpha [1+k(1-z)/z] ->0 as k->infinity.                 (5)

For fixed f and signal, reducing vacuum clicks arbitrarily also removes detection.
This explicitly realizes [K2108](k2108-local-detector-tradeoffs-2026-10-26.md)'s
fixed-region conclusion, not a new universal no-darkness theorem. The exact
projective instrument has Kraus P_k=1_[k,infinity)(b†b) and I-P_k. Compared with
deterministic no-click plus unchanged GLOBAL vacuum, its full-record half trace
distance is F(alpha)=(sqrt(4alpha-3alpha²)+alpha)/2; unread vacuum disturbance is
sqrt(alpha(1-alpha)). These reuse [K2133](k2133-recorded-instrument-vacuum-disturbance-2026-10-27.md)'s
projection-channel calculation. A small click probability is not equal to full
field disturbance. Randomized ROC effects specify probabilities; they do not
uniquely fix an instrument or its disturbance.

The released implementation task is [K2152](k2152-finite-chain-threshold-detector-2026-10-27.md):
implement this threshold with all outcomes retained under explicit finite-site
control assumptions, rather than silently identify an algebraic effect with a
causal continuum apparatus. Finite exact controls independently recover Schmidt
coefficients, tail sums, parity, ties and randomized ROC; they do not replace the
infinite-Fock proof or certify state preparation.

## 5. Released resource calculation: exact global vacuum energy

For the SAME fixed f and signal pair h,j, let E_h=<h,omega h>, E_j=<j,omega j>
and E_sum=E_h+E_j. Both are finite; no new mode or signal is selected. The free
Hamiltonian is H=dGamma(omega), with H Omega=0. For deterministic threshold k>=1,

    E_click = k E_sum,
    E_no_click = k z^k E_sum/(1-z^k),
    E_unread = 2 k z^k E_sum.                                (6)

Equivalently E_sum=(a_-1 a_2-a_1)/(a_-1 a_1-1) for N>0; this follows
by adding the h,j spectral moments and matches K2143's parity energy
2N(N+1)E_sum. No optimal-energy criterion is asserted.

These are conditional OUTPUT mean field energies and their probability-weighted mean,
not input energy, preparation cost or controller work. To derive them, the normalized
click state is the Schmidt tail sqrt(1-z) sum_(n>=k) z^((n-k)/2)|n,n>.
It has <n_b>=<n_c>=k+N and <bc>=sqrt(z)[k+1/(1-z)]. Substitution into the
Bogoliubov inverse gives <a_h†a_h>=<a_j†a_j>=k. The cross expectation
<a_h†a_j> vanishes because it changes the b-minus-c occupation, while all
spectator modes remain vacuum. Thus the quadratic-form expectation of H is
k(E_h+E_j), even when omega does not preserve span{h,j}. Its off-subspace terms
have zero expectation; this is not an invariant-subspace assertion for H.
Geometric tails give finite number moments and h,j are in the energy-form domain,
so these expectations and the following polarization are well defined.

Since H^(1/2)Omega=0, the two unnormalized projected vacuum branches have equal
energy norm: H^(1/2)(I-P_k)Omega=-H^(1/2)P_k Omega. Their common squared norm
is k z^k E_sum. Divide by z^k or1-z^k and sum to obtain(6).

In the inherited W=diag(1,9,4) control E_h=E_j=5. Threshold k=1 gives click
energy10, no-click energy10/3 and unread energy5. The parity unread energy is
80/9 from K2143, so in this frozen example the optimal equal-prior threshold
improves error AND unread vacuum energy, while increasing false-click probability.
This is not universal domination at every ROC objective. As k->infinity,
unread energy tends0 but rare click energy grows linearly and detection tends0.
The exact resource law closes the output-field accounting for this supplied
instrument. Its finite-chain realization and remaining control imports are in K2152.

## Evidence and inference boundary

The proofs and finite exact controls are separate evidence kinds. Independent internal
specialists review the actual statements and probe seams. No external certification,
proof assistant, novelty or GU recovery is claimed. SC-OP-04 ASSERTS candidate
four-field grammar; SC-OP-05 and SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS
requiring an odd action as a prerequisite. LT-SM8/LT-GR6b, ledger0.263, source
register and canon are unchanged. The scalar positive Hilbert model is imported;
it is not the source-selected GU quotient, fermionic grading or observed2+1.
