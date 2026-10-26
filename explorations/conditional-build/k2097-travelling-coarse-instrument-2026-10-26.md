---
title: "K2097: A travelling coarse instrument with controlled loss"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, massive apparatus, GU verdict, novelty or external certification
scripts:
  - tests/channel-swings/k2097_travelling_coarse_instrument_probe.py
---

# K2097: A travelling coarse instrument with controlled loss

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

## 1. Operational target and supplied resources

Use two independent copies of [K2096](k2096-bounded-continuum-capture-2026-10-26.md).
The input code is the four-dimensional Fock space of two fixed incoming modes
f1,f2; its state may be arbitrary and entangled with an external reference.
ALL orthogonal input modes, both fermionic memories and later release inputs
start in their supplied empty-Fock vacuum. The two memories are co-located.
These are extra preparation/geometry assumptions, not consequences of a massive
sea state or of source operator9.16. No claim concerns arbitrary states on the
whole incoming continuum or a strictly gauge-invariant-only observable algebra.

In basis |n1,n2>=(00,01,10,11), the coarse effect is

    E=1-(1-n1)n2=diag(1,0,1,1),     E0=I-E, E1=E.         (1)

The target instrument transfers the input code to two specified later outgoing
modes and returns classical label j with CP map rho -> E_j rho E_j, up to the
stated input/output identification. In particular |00><11| survives the j=1
branch. It is parity-even, but not U(1)-invariant. This is the same coarse
observable as K2090; its finite coherent gate is reused, not claimed anew.

After capture, use a bosonic record qubit initially |0> and the bounded memory
unitary

    V=(I-E_memory) tensor I+E_memory tensor X.             (2)

For example H=E_memory tensor(I-X), applied for time pi/2, generates V.
The gate is even in fermions and includes the actual quartic n1 n2 term;
it is a supplied hybrid/nonGaussian resource. It is not quadratic Gaussian
control, and random unrecorded phases are not its substitute. Do not measure
the two memory occupations separately. Finally release both memories into
later chiral output channels and read/dephase only the record qubit.

## 2. Full instrument bound, including external references

Write eta_c,eta_r for the common capture and release efficiencies. Each
selected-mode step is a two-mode fermionic beam splitter with
sin(theta)=sqrt(eta), cos(theta)=sqrt(1-eta), 0<=theta<=pi/2.
Its exterior-power implementation has eigenvalues1,1,exp(i theta),exp(-i theta).
Relative to the ideal signed swap at theta=pi/2,

    ||Gamma(U_theta)-Gamma(U_pi/2)||
       = b(eta):=sqrt(2-2sqrt(eta)).                       (3)

The bound also holds with any spectator CAR modes or external reference,
because this is an even two-mode unitary and the spectator extension has the
same operator norm. Two capture and two release steps plus the SAME gate(2)
therefore differ from the ideal four-swap circuit by operator norm at most
2b(eta_c)+2b(eta_r). Restriction to fixed vacuum ancillas gives the same
Stinespring-isometry bound. Trace and record dephasing are contractive; the
pure-state trace distance is at most the norm distance of purifications.
Consequently the HALF diamond norm of the full classical-record/output channel
obeys

    D <= min(1, 2b(eta_c)+2b(eta_r)).                      (4)

In the ideal reference circuit, the two captures put the input into the two
memories with a known minus sign per excitation; releases put it into the two
outgoing modes. Apply the known output parity phase (-1)^(n1+n2) to remove
that sign. This is even and does not change E. Memory and bypass outputs are
vacuum in the ideal circuit. Equation(4) compares actual and ideal circuits
using the same normalized input/output mode coordinates at each finite eta;
the ideal swaps are mathematical references, not finite-budget capture claims.
If eta_c=eta_r=1-exp(-K), b<=sqrt(2)exp(-K/2), so

    K >= 2 log(4sqrt(2)/delta) implies D<=delta, 0<delta<1. (5)

This sufficient budget is conservative, not optimal. With |g|<=G each pulse
needs duration at least K/G^2; two channels can capture in parallel, the local
gate lies between capture and release, and the output occurs afterwards.
K2096 equations(5) and(7) keep the input and delayed output pulses fixed
throughout this approximation family. There is no acausal inverse of a past output field. The finite-dimensional
mathematical ideal is exact; finite-duration bounded couplings approximate it.

## 3. Necessary error, memory noise and coherent backaction

For input |01>, the desired label is0. With empty memories the second memory
is occupied with probability eta_c, so the actual label0 probability is eta_c.
Neither release nor phase correction changes that label. Thus

    D >= 1-eta_c.                                        (6)

A stronger witness is input |11> and the output event that both outgoing
modes are occupied. The ideal probability is1; the actual probability is
(eta_c eta_r)^2, since both excitations must survive both stages. Hence

    D >= 1-(eta_c eta_r)^2.                               (6a)

For equal eta=1-exp(-K), D<=delta necessarily requires
K>=-log(1-(1-delta)^(1/4)). This complements the sufficient budget(5)
without claiming either bound is the exact diamond error.
These are real instrument-error witnesses, not mutations of a claim string.
For diagonal independent memory occupancies q1,q2, capture sends occupation
x_i to p_i=eta_c x_i+(1-eta_c)q_i. On vacuum input the erroneous label0
probability becomes

    (1-(1-eta_c)q1)(1-eta_c)q2.                           (7)

The empty-memory assumption is visible; a sea input cannot be replaced by
vacuum without preparation. A separate imperfect record initialized as
(1-p)|0><0|+p|1><1| flips the ideal labels with probability p even when capture
and release are perfect. This is consistent with K2090's support/thermal
record bounds; no thermodynamic work of reset is supplied.

For the actual empty-memory circuit, the |00><11| matrix unit in the click
branch has outgoing |00><11| coefficient eta_c eta_r after phase correction.
Only the no-loss branch overlaps the vacuum environment, giving one square
root efficiency per transferred excitation in each stage. Measuring individual
occupations at readout makes this coefficient zero. Thus matching record
probabilities alone misses a load-bearing phase error. The exact probe builds
CAR matrices with their signs, checks the ideal CP maps on all16 code matrix units and finite-loss
coherence/noise witnesses, and compares a genuinely refined readout and noisy states.

## 4. Ceiling and next physical input

This supplies a full readable delayed instrument in a specified causal chiral
boundary model, with an explicit finite-coupling approximation error and a
bounded local hybrid gate. It does not construct a point-local smooth massive
three-dimensional sea detector, finite total work, source-selected dynamics,
or same-mode nondemolition return. K2089's massive distributed transfer and
K2094's pointwise obstruction remain intact. A useful next test is a typed
massive-to-chiral memory interface, including bandwidth/energy and the exact
particle-hole convention; failure there would exclude that interface only.
