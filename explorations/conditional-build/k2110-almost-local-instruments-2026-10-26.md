---
title: "K2110: Energy filters and complete almost-local recorded instruments"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional imported positive-Hilbert detector mathematics; no GU recovery or apparatus certification
scripts:
  - tests/channel-swings/k2110_almost_local_instruments_probe.py
---

# K2110: Energy filters and complete almost-local recorded instruments

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
result: conditional detector bounds and constructions with explicit locality and approximation assumptions
carrier: positive-energy Hilbert space with covariant local von Neumann net and invariant vacuum LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_positive_Hilbert_space
real_structure: complex adjoint; no source-selected real form
grading: ordinary observable algebra; no source grading identified
action_owner: repository-construction -- supplied time automorphisms, bounded local observable and spectral filter
target: controlled local approximation of a vacuum-dark recorded instrument MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and inference boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd-action prerequisite. The
positive Hilbert spaces, local algebras, vacuum and dynamics here are imported,
not selected by equation9.16. K2021 local R0/R1 already exists; source-selected
observation and physical domain remain open. LT-SM8/LT-GR6b, source register,
ledger0.263 and canon are unchanged. Native2+1, total/observed chirality,
full20 and K/C accessibility are separate obligations. No GU derivation,
novelty, external-expert or proof-assistant certification is claimed.

## 1. Repair the localization assumption explicitly

Let H>=0 be selfadjoint, U(t)=exp(itH), U(t)Omega=Omega, ||Omega||=1, and
alpha_t(A)=U(t)A U(t)*. Assume a local von Neumann net with isotony and time
covariance, and A in M(O) bounded, O bounded. Choose f with

    fhat(E)=integral dt f(t)exp(iEt) in C_c^infinity((-b,-a)),
    0<a<b, L=||A|| ||f||_1>0.

The inverse transform f is Schwartz and generally complex. Define

    B=integral_R f(t)alpha_t(A)dt,
    B_T=integral_[-T,T] f(t)alpha_t(A)dt,
    eta_T=||A|| integral_|t|>T |f(t)|dt, r_T=eta_T/L.              (1)

These are strong vector integrals: t->alpha_t(A)xi is continuous for each
xi and its norm is bounded by||A||||xi||. No norm-continuous orbit or
operator-norm Bochner integrability is assumed. Integration defines bounded
operators with ||B||<=L, ||B_T||<=L-eta_T and ||B-B_T||<=eta_T.
The spectral theorem gives

    B Omega=fhat(H)A Omega=0.                                   (2)

The negative-frequency convention is essential. Changing fhat to positive
energies ordinarily creates rather than removes vacuum excitations.

This is the standard energy-decreasing almost-local detector strategy;
see [Porrmann](https://arxiv.org/abs/hep-th/0208230)
for related detector theory (bibliographic attribution only; the stated
bounds are proved here). It is not a novel exact local dark detector.

## 2. Supply a signal rather than assuming one

Require P_(0,infinity)A*Omega nonzero. This is not automatic for every A:
A=I produces B=0. Let mu be the spectral measure of A*Omega. Select a compact
interval I inside(a,b) with mu(I)>0 and a real nonnegative fhat(-E)>=b0>0
on I. For psi=P_I A*Omega/sqrt(mu(I)),

    <Omega,B psi>=integral_I fhat(-E)d mu(E)/sqrt(mu(I))
                  >=b0 sqrt(mu(I))>0.                          (3)

To see the sign, <Omega,alpha_t(A)psi>=<A*Omega,e^(-itH)psi>.
Thus c=||B psi||>=b0 sqrt(mu(I)). This constructs a normalized finite-band
signal state from the declared local observable and spectral projections.
It is not a local state-preparation procedure, a source-selected state or
unit-efficiency capture. For a given A, positive excitation spectral weight
provides some such finite interval after choosing the filter band to contain it.
For a previously fixed band, overlapping spectral mass is still required; otherwise this construction has no signal.

## 3. Finite-region detector errors and an explicit resource estimate

Take a bounded region O_T containing O translated by all |t|<=T. Covariance,
isotony, strong closure and bounded strong integral approximation imply
B_T in M(O_T). Then

    E=B*B/L², E_T=B_T*B_T/L², 0<=E,E_T<=I,
    p_vac(E)=0, p_vac(E_T)<=r_T²,
    p_psi(E_T)>=max(0,c-eta_T)²/L².                             (4)

For every integer N>1, integration by parts in the compact smooth fhat gives
|f(t)|<=||fhat^(N)||_1/(2pi |t|^N). Consequently

    eta_T <= ||A|| ||fhat^(N)||_1 /[pi(N-1) T^(N-1)].            (5)

This makes the approximation and its filter-dependent constant explicit.
The spatial radius of a containing double cone grows at least according to
the chosen causal enclosure of the translated support; for O within a radius-R
standard double cone, radius R+T suffices. We assert a sufficient enclosure,
not a minimum implementation duration. At any finite T, a separating vacuum
and nonzero E_T imply strictly positive p_vac by K2108. Equation(4) is an upper
bound, not a claim of finite-T darkness or uniform high detection efficiency.

For s=c/L>0 and r_T<s/2, the actual finite-time signal contrast obeys
p_psi(E_T)-p_vac(E_T)>=(s-r_T)²-r_T²=s²-2sr_T>0. Thus a fixed
nonzero spectral witness can be separated from vacuum at some finite T,
with explicit filter-dependent tail control, without claiming unit efficiency.

The filter also annihilates the entire low-energy subspace P_[0,a]H.
To prove this without operator-valued integration assumptions, take
psi in that subspace and phi in P_[0,M]H. Approximate both spectral
unitary orbits by finite step sums with input energies y in[0,a] and
output energies x in[0,M]. Every time-smeared matrix coefficient contains
fhat(x-y)=0 since x-y>=-a. Step sums converge pointwise in t, and their
matrix elements are bounded by||A||||phi||||psi||. Dominated convergence
against |f(t)| gives <phi,B psi>=0. Finite-energy phi are dense, proving
B P_[0,a]=0. Hence ||B_T P_[0,a]||<=eta_T and every normal state supported
in this low band has click probability<=r_T². This is an energy threshold
property, not a particle-count theorem.

## 4. Complete recorded-instrument convergence, including references

Let d_T=||E-E_T||. Product expansion and the bounds following(1) give

    d_T <= min(1, r_T(2-r_T)).                                  (6)

Use the binary square-root instruments with both outcomes retained,

    J_E(rho)=sum_j |j><j| tensor K_j rho K_j*,
    K_1=sqrt(E), K_0=sqrt(I-E),

and similarly J_ET. The positive square-root Holder inequality gives
||sqrt(E)-sqrt(E_T)||<=sqrt(d_T), as does the complement. For their common
Stinespring isometries, with an extra copy of j to dephase the record,
||V_E-V_ET||<=sqrt(2d_T). Trace-distance contraction of pure dilations and
convexity, also after tensoring any reference, yield

    (1/2)||J_E-J_ET||_diamond <= min(1,sqrt(2d_T)).                (7)

This includes post-measurement system coherence and the record, not merely
click probability. The universal square-root estimate is standard functional
calculus; the exact finite probe checks a noncommuting pair, Kraus completeness and retained
within-outcome coherence, not a full channel-distance computation.

Each finite-T Kraus operator belongs to M(O_T) by functional calculus.
For any remote observable C in M(O_T)', the nonselective dual channel gives
sum_j K_j* C K_j=C. Selective conditioning can change correlations. Algebraic
causality outside the entire O_T does not construct a local interaction
Hamiltonian or permit treating the whole region as a pointlike operation.
That realization gap was already identified by K2081 and remains open.

## 5. Joint consequence and limits

Fix a signal lower target0<eta<c²/L². For T sufficiently large, equation(4)
keeps p_psi>=eta while its vacuum upper bound tends to zero. K2108 then says
that any bounded commutant approximants to this same psi for the changing
algebras M(O_T), meaning D_T in M(O_T)',
||psi-D_T Omega||<=delta and ||D_T||<=C_T, with fixed
0<=delta<sqrt(eta), must have norm bounds

    C_T >= (sqrt(eta)-delta)/r_T                               (8)

whenever r_T>0. If actual vacuum response is smaller, the necessary cost is
larger. The changing region is the escape from a fixed-algebra uniform bound;
this is not a contradiction to Reeh–Schlieder or a universal energy/time law.
If no such commutant approximant is assumed, (8) asserts no existence.

K2080's compact CAR cutoff already gives another approximate local effect;
this filtered construction adds a complete recorded-instrument norm bound
with explicit time/localization/filter resources. It does not provide the
same-field massive capture, finite-duration apparatus or source-selected
observed-domain bridge needed by the original consumer. Those remain next
constructive questions, with exact zero-noise demands removed only where
these assumptions actually apply.
