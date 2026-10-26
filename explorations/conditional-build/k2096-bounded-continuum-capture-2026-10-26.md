---
title: "K2096: Bounded continuum capture and an exact coupling budget"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, massive apparatus, GU verdict, novelty or external certification
scripts:
  - tests/channel-swings/k2096_bounded_continuum_capture_probe.py
---

# K2096: Bounded continuum capture and an exact coupling budget

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
result: conditional operational theorem with explicitly supplied representation and controls
carrier: two chiral temporal L2 streams and finite fermionic memories in empty Fock LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert metric ON=declared_complex_completion
real_structure: stated CAR adjoint and particle-hole split only where used; no source derivation
grading: fermion parity, charge and energy signs remain distinct
action_owner: repository-construction -- supplied free dynamics and controls
target: conditional operational state and measurement constraints MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and Layer0 boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd action.
These supplied positive CAR models are not source operator9.16. K2021 already
constructs local R0/R1 but does not source-select these dynamics, observations
or states. LT-SM8/LT-GR6b retain action/observation/quotient/positivity debts.
Source-register, physics-ledger and canon verdicts remain unchanged. No new
substrate pathway or source mechanism is asserted. The results supply scoped
reverse-scaffold constraints and conditional mathematical constructions.

## 1. The changed model and exact continuum evolution

This is a supplied one-dimensional chiral, Markov input-output model with a
single localized fermionic memory. It is NOT the massive three-dimensional
Dirac sea of K2089. Its temporal one-particle space is L2([0,T]); the memory
is C. An empty-Fock representation is supplied. A boundary input-output model
is not a smooth bounded potential on the massive field and does not inherit
K2089's finite sea-energy theorem or particle-hole symmetry. Its microscopic
reservoir, bandwidth and energy realization remain separate obligations.

Fix finite T>0. Let g be real, bounded and square integrable, u an incoming amplitude, z the
memory amplitude and y the outgoing amplitude. Define the model by

    z'=-g(t)^2 z/2-g(t)u(t),      y(t)=u(t)+g(t)z(t).       (1)

These are one-particle equations, not an unjustified bosonic commutator
replacement. Their solution defines a unitary S_g:C+L2[0,T] -> C+L2[0,T].
Indeed d|z|^2/dt=|u|^2-|y|^2. Given final z(T) and y, solve
z'=g^2 z/2-g y backwards and set u=y-gz, proving surjectivity as well as
isometry. The same argument works on each subinterval, giving causal
composition: past output depends only on past input and the initial memory.
The exterior-power unitary Gamma(S_g) gives an exact even, number-conserving
CAR dilation. This establishes a mathematical causal boundary model, not a
new relativistic Hamiltonian realization or an optical-to-fermion theorem.

Define K(t)=integral_0^t g(s)^2 ds, K=K(T), A=exp(-K/2), eta=1-exp(-K).
When K>0 set the normalized incoming and outgoing modes

    f(t)=g(t) exp(-(K-K(t))/2)/sqrt(eta),
    h(t)=g(t) exp(-K(t)/2)/sqrt(eta).                       (2)

The explicit integral solution proves

    z(T)=A z(0)-sqrt(eta)<f,u>,
    S_g restricted to (memory,f) -> (memory,h)
          = [[A,-sqrt(eta)],[sqrt(eta),A]].                (3)

For the second identity, initial memory1 produces outgoing sqrt(eta)h;
input f produces outgoing A h and memory-sqrt(eta). Direct substitution in
(1) proves both columns. Orthogonal input modes map into the complementary
output subspace, since their images are orthogonal to these two columns.
Thus the entire continuum input reduces EXACTLY to one beam splitter plus
a unitary on orthogonal field modes; no finite mesh limit is invoked.

## 2. Optimal capture and the finite-budget boundary

For initial empty memory and normalized input u, capture probability is
eta |<f,u>|^2. The largest possible value is eta, achieved precisely by f
up to phase. Therefore a finite K cannot capture any normalized mode perfectly
in this single-memory passive model. For 0<delta<1 and |g|<=G then

    capture probability <=1-exp(-G^2 T),
    probability >=1-delta requires G^2 T>=log(1/delta).    (4)

This is a necessary budget for the stated model, not all detectors or all
feedback networks. Constant g=G with the matched exponential f attains the
bound. It is not a claim of an optimal smooth-pulse shape or minimal physical
work. K=0 transfers nothing. Infinite incoming time or a singular coupling
can leave the finite-budget class.

The optical perfect-absorption and initial-singularity principles are already
in [Yamamoto and James](https://arxiv.org/abs/1403.1698) and
[Nurdin, James and Yamamoto](https://arxiv.org/abs/1609.05643). We derive the
unitary CAR boundary model above and its consumer below directly; no novelty
or applicability to the massive source completion is inferred from those papers.

## 3. Released construction: smooth capture of a prescribed pulse

Fix any real normalized smooth compactly supported f inside(0,T). It need
not be nonnegative. Let F(t)=integral_0^t f(s)^2 ds and epsilon>0. Choose

    g_epsilon(t)=f(t)/sqrt(epsilon+F(t)).                  (5)

It is bounded and smooth with the same compact support, and

    K(t)=log((epsilon+F(t))/epsilon),
    eta=1/(1+epsilon), A=sqrt(epsilon/(1+epsilon)).        (6)

Substitution into the first expression in(2) returns EXACTLY the prescribed
f. Thus this is a family of genuine finite-coupling absorbers for a fixed
input mode, not a family that improves efficiency by silently changing the
input. Its amplitude satisfies ||g||infinity<=||f||infinity/sqrt(epsilon).
The ideal hazard f/sqrt(F) has divergent integral of g^2 at its first onset,
even if f vanishes to all orders there. Formula(6) quantifies that singular
limit; no bounded exact absorber has been constructed.

A separate pulse releases a memory excitation into its h of(2), with the
same efficiency formula. The outgoing pulse can also be prescribed independently.
For a normalized real smooth compact h, put H(t)=integral_0^t h(s)^2 ds and

    g_release(t)=h(t)/sqrt(epsilon+1-H(t)).                (7)

Its K(t)=log((epsilon+1)/(epsilon+1-H(t))) gives eta=1/(1+epsilon),
and substitution in the second expression of(2) returns exactly h. Thus both
input and delayed output shapes can stay fixed while the errors decrease;
no unbounded limit is silently described as one finite apparatus. Two memories fed by two independent chiral channels
can be placed at the same node. Capture, a bounded coherent local gate, and
release then yield the complete approximate instrument in
[K2097](k2097-travelling-coarse-instrument-2026-10-26.md). The outgoing mode is
later than the incoming mode: this is transport with delay, not instantaneous
restoration of the original spatial field.

## 4. Evidence and exact next condition

The written norm-balance, inverse ODE and two-column calculation establish the
continuum claim. The exact probe checks finite-bin unitary compositions,
unitarity and matched-mode normalization, the analytic regularization identity, and
faults in damping, mode shape and normalization. Finite bins alone do not prove
(1). Their role is an independent algebraic countercontrol for signs and budgets.
The next physical bridge is a derived finite-bandwidth coupling of the actual
massive observed field to these memory coordinates, with energy and causality
estimates. A supplied chiral empty bath cannot be relabeled a sea apparatus.
