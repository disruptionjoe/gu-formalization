---
title: "K95 observed finite-Hamiltonian asymptotic no-go wave"
status: active_research
doc_type: reverse_scaffold_finite_hamiltonian_asymptotic_no_go_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K94_FINITE_CLOSED_HAMILTONIAN_STABLE_STATE_AND_RECORD_OWNER
target_claim_verdict: FINITE_CLOSED_HAMILTONIAN_ROUTE_KILLED_SOURCE_CLAIMS_UNCHANGED
claim_ceiling: exact finite-dimensional obstruction to a universal pointwise attracting state or newly formed universally convergent detector effect under one closed time-independent Hamiltonian; no obstruction to infinite reservoirs, thermodynamic limits, open systems, coarse-grained convergence or source GU dynamics
manifest: lab/process/k95-observed-finite-hamiltonian-asymptotic-no-go-wave.json
probe: tests/channel-swings/k95_observed_finite_hamiltonian_asymptotic_no_go_probe.py
---

# K95 observed finite-Hamiltonian asymptotic no-go wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: finite-dimensional unitary-flow obstruction to universal pointwise attraction and newly stable record formation, with the K94 parity detector as exact oscillatory witness
carrier: arbitrary finite complex Hilbert carrier for the theorem; selected P8=(C2)^tensor3 tensor C2 detector for the witness LAYER=observed CHIRALITY=N/A
pairing: imported finite trace state-effect pairing ON=repository_owned_closed_hamiltonian_control
real_structure: ordinary complex conjugation in an energy basis; computational-basis conjugation in the K94 witness
grading: energy eigenspace decomposition and detector bit; no source BV, BFV or ghost grading
action_owner: repository-construction
target: universal pointwise long-time state and detector-record stability under one closed time-independent finite Hamiltonian MAP-TYPE=evaluation
```

Scope: this result binds finite-dimensional closed time-independent Hamiltonian
evolution and universal pointwise asymptotic claims. It is not a no-go for an
infinite reservoir, thermodynamic or weak-coupling limit, open-system
semigroup, explicit coarse-graining, selected initial sector, or source GU
dynamics.

## Inline preflight bookend

The route-changing lens census covered finite spectral theory, trace-distance
invariance, almost-periodic functions, recurrence, Heisenberg observable
limits, ergodic means, conditional expectations, open-system dilations,
reservoir and thermodynamic-limit escapes, causal support, quotient descent,
source custody and falsification scope. The structural route dominates a
larger simulation: invariance of state distance rules out a common attractor,
while finite Fourier-limit rigidity decides stable record formation without a
time grid or tolerance.

Mechanism-level retrieval found K94's piecewise Hamiltonian and four-clock
unitary, K91's finite detector dilation, and earlier stationary-state controls.
It found no result separating a stationary state from an attracting state or a
stable pre-existing effect from a newly formed asymptotic record. Standard
unitary invariance and finite Fourier facts receive no novelty claim. Positive
controls check exact norm preservation, spectral block decomposition, the
commuting-effect case and gauge-basic extension. Negative controls use the K94
parity-controlled detector, its two exact subsequences, an omitted
off-diagonal block, imported averaging and every promotion fence.

## The state-attractor obstruction

Let `H=H*` act on a finite-dimensional complex Hilbert space and

```text
U_t=exp(-itH),                 Phi_t(rho)=U_t rho U_t*.       (1)
```

Unitary conjugation preserves every Schatten distance. In particular,

```text
||Phi_t(rho)-Phi_t(sigma)||_1=||rho-sigma||_1.               (2)
```

If two distinct initial states converged in trace norm to one state
`rho_infinity`, the triangle inequality would force their distance to tend to
zero, contradicting (2). Thus a finite closed Hamiltonian flow has no common
pointwise attracting state on any set containing two distinct states. A Gibbs
state commuting with `H` can be stationary, but stationarity is not attraction
and does not explain preparation.

## The stable-record obstruction

Write the spectral resolution

```text
H=sum_a epsilon_a P_a.                                      (3)
```

For a detector effect `E`, its Heisenberg orbit is the finite Fourier sum

```text
E(t)=U_t* E U_t
    =sum_(a,b) exp(i(epsilon_a-epsilon_b)t) P_a E P_b.       (4)
```

Group (4) by energy gap. A finite sum of distinct real-frequency exponentials
has a limit at positive infinity only when every nonzero-frequency coefficient
vanishes. Therefore, if `Tr(rho E(t))` converges for every density matrix
`rho`, then `E(t)` converges weakly, every nonzero-gap block vanishes, and

```text
E=sum_epsilon P_epsilon E P_epsilon,   [H,E]=0,   E(t)=E.   (5)
```

So a universally convergent detector effect under finite closed Hamiltonian
flow was constant all along. It may preserve a record, but it cannot form a
new one asymptotically. This is the exact universal statement: a specially
chosen state can cancel selected Fourier coefficients, and a time average can
converge, but neither supplies universal pointwise formation.

## K94 exact oscillatory witness

Let `q=s0 xor s1` be K94's propagated middle record. Its Gibbs weight is

```text
Pr(q=1)=1/3.                                                (6)
```

Couple a detector initialized in zero through the one static interaction

```text
H_int=P1_q tensor X_D.                                     (7)
```

The detector-one probability is

```text
Pr(D=1;t)=(1/3) sin^2(t).                                  (8)
```

Along `t=n pi` it is zero, while along `t=pi/2+n pi` it is
`1/3`. Hence it has no pointwise long-time limit. At the half-turn it exactly
reproduces K94's record weights `(2/3,1/3)`; at the next full turn the record
is erased. One static finite Hamiltonian removes the external gate schedule
but not the recurrence obstruction.

The Cesaro mean exists and gives detector-one weight `1/6`, the dephased
conditional expectation of (8). That number differs from the desired `1/3`,
and the averaging operation is a new supplied owner. Zero extension over the
K91 gauge summand remains basic, but it changes none of the asymptotic logic.

## Maximum licensed conclusion

No finite-dimensional closed time-independent Hamiltonian can produce a
universal pointwise attracting state, and no detector effect can form a new
universally convergent record: universal convergence forces that effect to
commute with the Hamiltonian and remain constant. The K94 parity detector is an
exact nontrivial witness, oscillating between erased and complete records.

This kills only the repository-internal K94 finite-closed-Hamiltonian endpoint.
It does not kill a source claim or any infinite/open-system route. A reservoir,
thermodynamic limit, coarse-graining, superselection, dissipation, measurement
or restricted state class may evade the theorem, but each is an additional
owner that must be stated.

## Inline postflight bookend

- Strongest overclaim: promoting a finite closed-flow theorem to a no-go for
  continuum QFT, infinite reservoirs, weak limits or source GU dynamics. None
  is in the quantified class.
- Strongest contrary construction: any `E` commuting with `H` is exactly
  stable. It preserves an existing record and therefore confirms the theorem's
  distinction between record storage and record formation.
- Weakest reproducibility seam: the theorem is structural and the K94 witness
  is exact, but trace/Born interpretation and the physical choice of what
  counts as a record remain imported.

The exact probe passes its declared controls and its hostile selftest catches
all planted scope, recurrence, averaging, custody and promotion mutations. No
source, continuum, microlocal, Born, prediction, confirmation, canon, paper or
held-out status moves.

## Next condition

Add one explicit irreversible owner and ask whether it stabilizes the full K94
record while preserving causal marginals and quotient descent. A Hamiltonian-
only escape requires a genuine infinite-reservoir/domain/scattering
construction, not another finite clock or bath.
