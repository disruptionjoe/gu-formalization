---
title: "K2149: Uniform energy-bounded limit and necessary signal energy"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional scalar mathematics; no causal apparatus, GU recovery or controller-work claim
scripts:
  - tests/channel-swings/k2149_energy_bounded_parity_limit_probe.py
---

# K2149: Uniform energy-bounded limit and necessary signal energy

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
result: Uniform energy-bounded limit and necessary signal energy
carrier: massive scalar Fock space and independent record with arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: positive Fock Hilbert form and free field mean energy ON=declared_carrier
real_structure: real Cauchy smear and complex Hilbert adjoint
grading: local canonical oscillator parity, distinct from global particle or fermion parity
action_owner: repository-construction -- supplied local canonical-mode instrument
target: fixed-signal and resource-conditioned recorded-channel limit MAP-TYPE=intertwiner
```

## 1. Beyond a fixed finite code

[K2148](k2148-fixed-signal-parity-response-2026-10-27.md) finds loss of every
fixed one-particle signal. Here control all Fock inputs, mixtures and references
under a bound on their MEAN input free-field energy. Retain the same massive
scalar, fixed real smooth compact g and f_K=c_K g cos(Kx) as K2146. This is
an input-energy statement, not total work, conditional output energy or controller
construction. Let H=dGamma(omega), omega>=m>0, and E=Tr(rho H).

Choose the local canonical oscillator scale nu=K (K>0). Its annihilator is

    b_K=a(h_K)+a^*(j_K),
    h_K=(sqrt(K) omega^-1/2+omega^1/2/sqrt(K))f_K/2,
    j_K=(sqrt(K) omega^-1/2-omega^1/2/sqrt(K))f_K/2.              (1)

Complex conjugation is included in the creation convention; the spatial vectors
are real. The CCR gives ||h_K||^2-||j_K||^2=1. This is the SAME V_K=(-1)^N_b
as K2143, because parity is unchanged by one-mode squeezing.

## 2. An exact all-Fock probability bound

Define nonnegative finite constants, with a_j=<f_K,omega^j f_K>,

    A_K=||omega^-1/2 h_K||^2=(K a_-2+2a_-1+1/K)/4,
    C_K=||omega^-1/2 j_K||^2=(K a_-2-2a_-1+1/K)/4,
    D_K=||j_K||^2=(K a_-1+a_1/K-2)/4,
    B_K(E)=(sqrt(E A_K)+sqrt(E C_K+D_K))^2.                    (2)

For every input with finite mean energy, including arbitrary references,

    q=Tr(rho K_-) <= min(1, B_K(E)).                           (3)

Proof: on the finite-particle smooth core the standard Fock annihilation bound
||a(h)psi||<=||omega^-1/2 h|| ||H^1/2 psi|| follows from Cauchy--Schwarz
on each particle-number sector. The creation CCR gives
||a^*(j)psi||^2=||a(j)psi||^2+||j||^2||psi||^2. Apply the triangle inequality
to (1). Closure extends the bound to the energy-form domain; it also places that
domain in Dom b_K. The odd spectral projection is bounded above as a quadratic
form by N_b=b_K^*b_K, since odd occupation is at least one. Purify mixed states
and let the identity act on the reference. This proves (3), without a cutoff
or a finite-particle assumption on the input.

Using the projection-channel formula reused in K2148,

    (1/2)||I_K-J||_(diamond,E) <= F(min(1,B_K(E))),
    F(q)=(sqrt(4q-3q^2)+q)/2.                                 (4)

Here the energy constraint is on the input system marginal. It includes entangled
references, and the output includes all field excitations and the complete record.
This is an upper bound, not an asserted optimal energy-constrained distance.

## 3. Controlled asymptotics and a uniform trivial limit

The only new spectral moment needed beyond K2146 is

    a_-2=K^-2+(3mu2-m^2)K^-4+O(K^-6).                         (5)

To justify it split each lobe at |q|=K/2, use the Taylor expansion of
((K+q)^2+m^2)^-1 on the central part, and integrate its uniform remainder
against Schwartz moments. Odd powers vanish because |g-hat(q)|^2 is even.
Outside the central part use the global bound omega^-2<=m^-2 and Schwartz
decay. The cross-lobe and normalization errors are superalgebraically small.
Constants depend on the fixed m,g, not uniformly on arbitrary changing envelopes.
Combining with K2146 yields

    A_K=K^-1+(5mu2-2m^2)/(4K^3)+O(K^-5),
    C_K=mu2/(4K^3)+O(K^-5), D_K=mu2/(4K^2)+O(K^-4).            (6)

For every fixed E, B_K(E)->0 and (4) proves uniform convergence of the complete
instrument to deterministic positive record plus unchanged field, on the ENTIRE
energy-bounded input class. For fixed positive E the bound is O(sqrt(E/K)+K^-1)
in half diamond distance. At E=0 its bound is O(K^-1), consistent with K2148's
exact vacuum scale. More generally E_K=o(K) still implies B_K(E_K)->0.
The fixed-signal theorem did not assume finite energy; this theorem buys
uniformity by imposing it. Neither implies unrestricted norm convergence.

## 4. A necessary resource law with a genuine moving control

A convenient explicit consequence of (2) uses sqrt(E C+D)<=sqrt(E C)+sqrt(D):

    q <= [sqrt(E)(sqrt(A)+sqrt(C))+sqrt(D)]^2,
    E >= ((sqrt(q)-sqrt(D))_+)^2/(sqrt(A)+sqrt(C))^2.            (7)

There is also an exact inverse of the upper envelope in (2). Since A-C=a_-1>0,
for q>=q0>D one necessarily has

    E >= [(q0-D)/(sqrt(A q0)+sqrt(C q0+(A-C)D))]^2.             (7b)

For q0<=D the bound is zero. Squaring sqrt(q0)=sqrt(A E)+sqrt(C E+D)
and choosing the nonnegative smaller admissible root gives (7b), with the
displayed rationalization avoiding cancellation. This is an inverse necessary
bound, not a proof that its energy threshold is attained in the continuum.

Thus any sequence of inputs with q_K>=q0>0 requires

    liminf_(K->infinity) E_K/K >= q0.                         (8)

This is mean input field energy; it is not a lower bound on preparation work or
an autonomous controller's budget. It is independent of whether the input is
pure, mixed or entangled with a reference. The bound is necessary, not sufficient.
For record contrast q_K-p_vac>=delta>0, the same result applies with q0=delta.
The moving h_+ from K2148 has q->1 and E/K->1, matching the unit leading coefficient at LIMITING response one (it need not
satisfy q_K>=1 at finite K). For any fixed 0<q0<1, mix that moving state with
vacuum at weight alpha_K=(q0-p_vac,K)/(p_-(h_+,K)-p_vac,K). For sufficiently
large K this lies in [0,1] and gives EXACT q_K=q0, alpha_K->q0 and E/K->q0; this is an energy/record countercontrol, not a
fixed-signal or causal preparation theorem. Such rare ultraviolet inputs explain
why a fixed-energy mean constraint and unrestricted inputs have different limits.

This consumes the released resource question: small vacuum response cannot
produce order-one record response at sublinear input energy in this family.
The next apparatus question needs a fixed signal/code and an actual causal
finite-duration local interaction; merely raising the mode frequency is not
an improvement on that task. K2146's rare OUTCOME energy and K2145's causal
necessity remain independent constraints, not replaced by this input bound.

## Acceptance and inference boundary

The adjacent probe independently reconstructs finite exact identities and perturbs actual
inputs/equations after a green baseline. Finite controls are not continuum proofs; the
written arguments have independent internal specialist review. No external certification,
proof assistant, remote CI, novelty claim or physical detector construction is supplied.
Source SC-OP-04 candidate grammar, SC-OP-05/META53 uncertainty and META56 disavowal retain
their prior polarity. LT-SM8/LT-GR6b, source register, ledger0.263 and canon are unchanged.
The supplied scalar Hilbert model is not a source-selected GU quotient or fermionic grading.
