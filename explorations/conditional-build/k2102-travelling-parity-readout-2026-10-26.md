---
title: "K2102: Finite-duration travelling parity readout"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, stable massive apparatus, GU verdict or novelty
scripts:
  - tests/channel-swings/k2102_travelling_parity_readout_probe.py
---

# K2102: Finite-duration travelling parity readout

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
result: conditional mathematical construction and exact scope boundaries
carrier: two localized fermion registers and a chiral L2 line with a two-state pointer LAYER=toy CHIRALITY=N/A
pairing: ordinary positive Hilbert product ON=declared_positive_Hilbert_space
real_structure: ordinary complex conjugation and adjoint, no source-selected reality
grading: fermion parity and U1 number distinct; pointer bosonic
action_owner: repository-construction -- supplied chiral transport and bounded number-controlled potentials
target: full recorded coarse instrument MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and object boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd-action prerequisite. The supplied
positive Hilbert/CAR and apparatus models below are not source operator9.16.
K2021 supplies local R0/R1 without selecting an observed positive algebra,
state or dynamics. LT-SM8/LT-GR6b, source-register, ledger and canon remain
unchanged. Native2+1, total/observed chirality, full20 and K/C accessibility
remain distinct debts. No new substrate pathway, novelty or external
certification is asserted. The calculation supplies a reverse-scaffold
operational constraint or conditional construction, not physical recovery.

## 1. The missing gate, not the missing capture

[K2101](k2101-massive-smeared-instrument-2026-10-26.md) assumes a coherent
coarse gate on two memory modes. Here construct that gate with an actual
finite-duration travelling mediator. The memories below are already localized
registers with commuting occupations n1,n2. This does NOT turn K2101's
spatially smeared field-to-memory coupling into a local capture protocol.
[K2089](k2089-distributed-smooth-transfer-2026-10-26.md) transfers a field
algebra but also leaves collective readout open. No identification of that
extended field with the present two local registers is made.

Use Hilbert space F(C2) tensor L2(R_x) tensor C2_pointer. Let v>0, X the
pointer Pauli matrix, and kappa_j real smooth compact functions in disjoint
intervals I_j=[a_j,b_j], b1<a2, with

    theta_j = integral kappa_j(x) dx/v = pi/2.
    H = -iv partial_x + V(x),
    V(x) = sum_j n_j kappa_j(x)(I-X).                  (1)

The bounded Hermitian multiplication potential makes H self-adjoint on H1.
Allow diagonal memory drift H_M=omega1 n1+omega2 n2; it commutes with (1)
and produces a known output calibration exp(-iTH_M), not an omitted drift.
The model has finite propagation speed v along the line. A finite interaction
zone coupled to one point register is a finite-range model, NOT a strictly
point-local relativistic interaction. K2104 below supplies a separate
point-contact domain model.

## 2. Exact characteristic solution and full instrument

All matrices V(x) commute. With q=x-vT,

    (U(T)Psi)(x)=exp[-i sum_j n_j A_j(q,T)(I-X)] Psi(q),
    A_j(q,T)=integral_q^(q+vT) kappa_j(y)dy/v.         (2)

Differentiate along x=q+vt to verify the equation and initial value. The
matrix factor is unitary, so translation plus this multiplier defines the
unitary solution; no time discretization or weak-coupling limit is used.
Let the mediator start in a fixed normalized wavepacket phi independent of
memory and all references, with support [l,r], r<a1, and l+vT>b2. Every
characteristic then crosses both complete profiles. Since

    exp[-i(pi/2)(I-X)]=X,

(2) factorizes on the whole memory code as

    U(T)(psi tensor phi tensor |0>)
       = (P_even psi tensor |0> + P_odd psi tensor |1>)
           tensor phi_translated,                    (3)

up to the declared memory drift and tensor ordering. P_even projects onto
00,11 and P_odd onto01,10. Thus final pointer readout realizes exactly

    I(rho)=sum_b |b><b|_record tensor P_b rho P_b.      (4)

The statement holds for all code states and arbitrary entangled external
references. The unobserved spatial mediator has the SAME final wavepacket
for every occupation; tracing it loses no intra-sector coherence. In particular
|00><11| survives. All16 memory matrix units verify the full map, not just
four occupation probabilities. No fresh intermediate record is read.

The identity term in I-X is essential: using -X alone gives i^(n1+n2)
X^(n1+n2). It gets all classical parity labels right but reverses |00><11|.
That changed instrument is rejected by a coherence control. The same apparatus
measures mod2 number of any finite chain of localized registers; each sees
one such profile, the final pointer is X^(sum n_j), and the entire spatial
packet must traverse every profile. This extension does not require individually
recorded occupations or a nonlocal simultaneous coupling.

## 3. Errors, travel time and resource boundary

For phases theta_j=pi/2+delta_j and complete traversal, comparing the actual
and ideal unitary gives operator error <=2 sum_j |delta_j|, capped by2.
After pointer readout, trace-distance channel error (half diamond norm) is
therefore <=min(1,2 sum_j |delta_j|). The estimate covers arbitrary references.
For a fixed independent spatial input with probability p on initial positions
whose trajectories do not traverse both complete profiles, discard the spatial
output. The resulting channel is exactly the integral of position-conditioned
finite channels with weight |phi(q)|², since the position trace kills offdiagonal
q terms. Good trajectories implement (4), so their complement costs at most p.
Combine to get min(1,p+2 sum|delta_j|). This linear p bound is for the reduced
recorded instrument; comparison retaining the spatial output generally needs
a square-root decoupling bound. For correlated preparations, let tau(dq) be the positive operator-valued
position measure on the memory/reference system. After discarding position
the same conditional-channel integral applies to tau(dq). On good paths it
agrees with the ideal channel; the trace of tau on bad paths is p. Triangle
inequality and trace contraction therefore give the SAME statewise p bound
on the joint memory/reference marginal, even with initial spatial correlations.
A uniform diamond statement requires a fixed input-preparation channel and
a uniform bad-path bound; it does not follow from one correlated input.
The statewise bound is sharp: prepare sqrt(1-p)|00,good>+sqrt(p)|01,bad>
with orthogonal spatial packets, good fully traversing and bad encountering
no interaction. After discarding position, the bad odd branch gets record0
instead of1, giving trace-distance error exactly p.

If |kappa_j|<=kmax, area pi v/2 implies width |I_j|>=pi v/(2kmax).
A trajectory must spend at least pi/(2kmax) in each interaction zone; total
protocol time also includes gaps and packet length. No speed-independent
instantaneous gate is being smuggled into (3). Bounded calibration drift
errors add their actual time integral in norm. A general memory Hamiltonian
mixing n1,n2 need not commute with V; it requires a new reference evolution
or explicit compensation, not this formula.

The chiral free generator has spectrum R. Adding bounded V does not make a
semibounded apparatus Hamiltonian; indeed the gauge equivalence in K2104
shows the same spectrum. The injected packet and pure pointer are supplied
resources. No passive reset, total work, massive3D sea realization, stable
vacuum or source selection follows. This explicit model removes the
instantaneous coarse-gate assumption conditional on chiral transport; it leaves
physical mediator stability and actual massive-field capture unresolved.

## 4. Precedent, verification and successor

Sequential flying-probe parity measurement is established prior art:
[Kerckhoff et al., PRA79 024305 (2009)](https://arxiv.org/abs/0812.1246) and
[McIntyre and Coish, PRResearch6 023247 (2024)](https://arxiv.org/abs/2402.17001).
No novelty claim or transfer of their optical implementation is made. The
specific proof here is (1)--(4), including finite support, drift and channel
scope. The finite exact probe checks all code matrix units, explicit zero-extended C1 polynomial
profile integrals, crossing cases and an interior characteristic derivative, bad-path mixtures and
wrong generator/readout/area controls. These checks do not prove continuum
domains; the analytic unitary construction does. K2104 resolves point-contact
locality in a distinct domain model, retaining the energy-spectrum limitation.
