---
title: "K2153 Minimum vacuum energy of diagonal detectors"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional detector mathematics; no GU recovery or total apparatus cost
scripts:
  - tests/channel-swings/k2153_diagonal_detector_energy_probe.py
---

# K2153 Minimum vacuum energy of diagonal detectors

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
result: K2153 Minimum vacuum energy of diagonal detectors
carrier: fixed massive scalar Fock vacuum and one canonical oscillator LAYER=toy CHIRALITY=N/A
pairing: global positive vacuum Hilbert form ON=declared_carrier
real_structure: real canonical coordinates and complex Hilbert adjoint
grading: oscillator occupation, distinct from GU or fermion parity
action_owner: repository-construction -- supplied positive Hilbert dynamics and controls
target: fixed-effect energy minimum and detection contrast bound MAP-TYPE=intertwiner
```

## Result and fixed objects

For the fixed mode and signal in [K2151](k2151-optimal-local-mode-discrimination-2026-10-27.md),
positive square-root Kraus operators minimize global vacuum field excitation among
all diagonal nondemolition instruments with the same effects. A randomized optimal
threshold can therefore retain K2151's exact detection probabilities while depositing
less energy than a classical random choice between two sharp threshold instruments.
This optimizes the instrument at prescribed effects, not all local operations or
the complete energy-versus-discrimination frontier.

Keep K2151's real normalized smooth compact smear f, mass m>0, canonical oscillator
b and companion c. Write N>0, z=N/(N+1) in(0,1), and

    Omega=sqrt(1-z) sum_(n>=0) z^(n/2)|n,n>,
    a_h=sqrt(N+1)b-sqrt(N)c†,
    a_j=sqrt(N+1)c-sqrt(N)b†.

The orthonormal original one-particle modes h,j have finite energies
E_h=<h,omega h>, E_j=<j,omega j>, E_sum=E_h+E_j. H=dGamma(omega)>=0,
H Omega=0. The span of h,j need not be invariant under omega. The signal is the
same fixed psi=a_h†Omega. Its one-mode occupation distributions are reused:

    p_n=(1-z)z^n,
    q_0=0, q_n=n(1-z)^2 z^(n-1), n>=1.                       (1)

No choice of an ultraviolet-dependent signal, another mode, or a new energy
normalization is made here. The trivial z=0 oscillator limit is separate.

## Exact energy for every diagonal instrument

Let the countable Kraus family be K_(r,a)=f_(r,a)(n_b), where r is the reported
outcome, a is an unreported Kraus label and

    sum_(r,a)|f_(r,a)(n)|^2=1 for every n>=0.

The bounded diagonal operators form a strongly complete quantum instrument.
Set v_n=(f_(r,a)(n)) in the Kraus-label Hilbert space, so ||v_n||=1. Its unread
GLOBAL vacuum output energy is exactly

    E_out=E_sum sum_(n>=0)(n+1)z^(n+1)||v_(n+1)-v_n||^2.     (2)

To prove this, for one f apply the original annihilators to f(n_b)Omega.
The coefficient of |n,n+1> in a_h f(n_b)Omega is

    sqrt(n+1) z^((n+1)/2)[f(n+1)-f(n)].

The a_j image has the opposite coefficient on |n+1,n>. These two images are
orthogonal; spectator annihilators vanish. The one-particle density therefore
has equal diagonal h,j populations and zero cross expectation. Taking the
omega quadratic form gives E_sum times the squared norm above, even when
omega moves h,j outside their span. Sum over Kraus labels to obtain(2).

Countability and domains do not hide an infinite-energy exception: since every
v_n is unit,

    0 <= E_out <= 4 E_sum z/(1-z)^2.                         (3)

Tonelli's theorem and this summable bound justify the sums. Individual bounded
f have finite weighted difference norm and thus the required H form domain.
These statements use the fixed smooth-mode assumptions; they do not bound a
family whose E_sum or z varies toward a singular limit.

## The minimum at prescribed effects

Fix e_r(n)=sum_a |f_(r,a)(n)|^2 for every r,n. For adjacent occupations,

    Re sum_a conjugate(f_(r,a)(n)) f_(r,a)(n+1)
        <= sqrt(e_r(n)e_r(n+1)).

One positive Kraus sqrt(e_r(n_b)) per outcome attains every one of these
Cauchy--Schwarz bounds simultaneously. Hence the exact minimum is

    E_min=2 E_sum sum_(n>=0)(n+1)z^(n+1)
                    [1-sum_r sqrt(e_r(n)e_r(n+1))].         (4)

This is an energy-specific minimization within the stated diagonal class.
Number-changing feedback, arbitrary spatial-region operations and changes of
the mode are outside it. No uniqueness is asserted.

An effect alone does not determine energy: the single effect e(n)=1 permits
both the identity Kraus and the unitary Kraus (-1)^n. Their output energies
are respectively zero and the upper bound in(3). The latter is a coherent
phase operation, not a detector with hidden information gain. This supplies
a countercontrol to an effects-only disturbance claim.

## A detection advantage requires energy in this class

For a binary effect e_n in[0,1], let alpha=sum p_n e_n be the vacuum click
probability and eta=sum q_n e_n the signal click probability. Summation by
parts, with vanishing geometric boundary terms, gives

    Delta=eta-alpha=(1-z)sum_(n>=0)(n+1)z^n(e_(n+1)-e_n).     (5)

For any implementation v_n, e_n is the squared norm of its click component.
The difference in probabilities of a projection on two unit vectors is at
most their vector distance; hence |e_(n+1)-e_n|<=||v_(n+1)-v_n||.
Cauchy--Schwarz and sum(n+1)z^n=(1-z)^-2 imply

    E_out >= z E_sum (eta-alpha)^2.                          (6)

This is a lower bound, not a claim that the bound is attainable for every
contrast. It covers all diagonal nondemolition implementations of the effect,
with fixed signal and mode. Output field energy is not apparatus work, record
energy, state preparation or a thermodynamic cycle cost. General measurement
resource accounting has other assumptions; see [Abdelkhalek, Nakata and Reeb](https://arxiv.org/abs/1609.06981).

## Exact soft-threshold consequence

K2151's optimal ROC uses e_n=0 for n<k, e_k=t, and e_n=1 for n>k,
with k>=1 and t in[0,1]. Positive square roots give

    E_soft=2 E_sum [k z^k(1-sqrt(1-t))
                       +(k+1)z^(k+1)(1-sqrt(t))].           (7)

The same formula applies at k=0 with its first term defined as zero. It
recovers the two sharp-threshold energies at t=0,1. Classically selecting
threshold k with probability t and threshold k+1 otherwise, then forgetting
that selection, gives the SAME binary effects but

    E_mix=2 E_sum [t k z^k+(1-t)(k+1)z^(k+1)].               (8)

The difference E_mix-E_soft is strictly positive for 0<t<1, since its terms
are 2 E_sum times A[sqrt(1-t)-(1-t)]+B[sqrt(t)-t], with
A=k z^k>=0 and B=(k+1)z^(k+1)>0. Forgetting a classical selection is not
the same channel as coherent square-root readout.

At K2151's inherited z=1/4,E_sum=10, take k=1,t=9/25. Both instruments have
alpha=13/100 and eta=16/25, but E_soft=2 whereas E_mix=17/5. The lower
bound(6) is2601/4000. At a deterministic threshold, (2) reduces to
2k z^k E_sum, reproducing K2151 without counting it as a new result.

[The physical-drift construction](k2154-uncompensated-detector-control-2026-10-27.md)
implements the positive square-root instrument with a bounded onsite angle
control after the existing gather. It gives full recorded error and specified
mean switching-work bounds. Those are separate from the ideal energy minimum.

## Evidence and remaining question

The exact probe reconstructs annihilator differences independently from the
Schmidt amplitudes, checks geometric sums, phase countercontrol, contrast and
soft-versus-mixture channels. Its changed-input/equation faults must fail real
checks after a clean baseline. Countable-channel/domain and optimization proofs
are independently reviewed separately from the finite checks. No external
certification, proof-assistant verification or novelty claim is made.

Next compare the best achievable discrimination under an actual field-energy
budget, allowing effects to vary, or extend beyond diagonal instruments with a
specified feedback resource. Equation(6) does not solve that larger variational
problem. Source SC-OP-04 ASSERTS candidate four-field grammar, SC-OP-05 and
SC-META-53 remain UNCERTAIN, and SC-META-56 DISAVOWS an odd-action prerequisite.
The imported scalar model does not discharge LT-SM8/LT-GR6b or select GU's
physical quotient. Source, ledger0.263 and canon remain unchanged.
