---
title: "K94 observed autonomous-clock instrument wave"
status: active_research
doc_type: reverse_scaffold_autonomous_clock_instrument_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K94_AUTONOMOUS_FINITE_CAUSAL_INSTRUMENT_COMPILATION
claim_ceiling: exact finite autonomous-clock compilation of the K94 propagation and detector sequence; no source-selected clock or dynamics, selected continuous-time Hamiltonian, continuum AQFT or microcausality, microlocal or Hadamard state, derived Born rule, prediction, confirmation, held-out score or verdict
manifest: lab/process/k94-observed-autonomous-clock-instrument-wave.json
probe: tests/channel-swings/k94_observed_autonomous_clock_instrument_probe.py
---

# K94 observed autonomous-clock instrument wave

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
result: exact autonomous four-clock unitary compiling the K94 propagation and detector sequence with a closing inverse leg
carrier: C4 clock tensor selected P8=(C2)^tensor3 tensor C2 detector LAYER=observed CHIRALITY=N/A
pairing: imported finite trace state-effect pairing on the K94 Gibbs density and detector zero state ON=repository_owned_clocked_instrument_control
real_structure: computational-basis conjugation with phases in the fourth roots of unity
grading: cyclic clock degree 0,1,2,3; three site labels and one detector label; no source BV, BFV or ghost grading
action_owner: repository-construction
target: autonomous finite compilation of causal propagation, record dilation and exact cycle closure MAP-TYPE=evaluation
```

Scope: this result binds only one finite clock compilation of the K94
propagation and detector terms. It neither selects a physical clock nor
constructs a source or continuum Hamiltonian.

## Inline preflight bookend

The problem-matched lens census covered autonomous quantum control, clocked
unitaries, reversible cellular automata, Feynman history constructions,
Stinespring dilation, causal support, cyclic closure, Hamiltonian logarithm
nonuniqueness, quotient descent, AQFT/microlocal ownership and source custody.
The decisive route was an exact controlled shift: it removes the external
choice of which propagation/detector unitary to apply at each step while
making clock initialization and the artificial closing leg visible.

Retrieval found K93's separate CNOT/instrument composition and K94's common
piecewise Hamiltonian control. It found no autonomous finite update compiling
the sequence with an exact closure certificate. Clocked-unitary and reversible
permutation facts receive no novelty claim. Positive controls exhaust the
64 basis states, all phases, all four legs, record weights and descent.
Negative controls omit closure, read the wrong site, leak gauge data and
promote clock, continuum, state or Born ownership.

## One autonomous clocked update

Let the data carrier be the three system bits plus detector bit, and let
`|t>`, `t in Z/4`, be a four-state clock. Retain K94's generated propagation
and detector unitaries `U_prop` and `U_det`. Set

```text
U0=U_prop,
U1=U_det,
U2=I,
U3=(U_det U_prop)*.                                         (1)
```

Define one time-independent discrete update

```text
A=sum_(t=0)^3 |t+1 mod 4><t| tensor Ut.                     (2)
```

Each `Ut` is unitary and the clock transitions have orthogonal source and
target sectors, so `A` is unitary. Starting at clock zero, the four data legs
multiply in temporal order to

```text
U3 U2 U1 U0=(U_det U_prop)* U_det U_prop=I.                 (3)
```

Therefore

```text
A^4=I                                                       (4)
```

on all 64 clock-data basis states, including the accumulated fourth-root
phases. The closing leg is deliberately explicit: without it the clock shift
would remain unitary, but (4) would fail on the data carrier.

## Clocked record

Initialize the clock at zero, the detector in `|0_D>`, and the system in the
K94 action-derived K92 Gibbs density. After clock legs zero and one, the
detector bit equals the propagated middle bit. Hence the input record effect
is again the parity observable

```text
Z0 Z1,                                                      (5)
```

with record weights

```text
(Pr(0),Pr(1))=(2/3,1/3).                                   (6)
```

The endpoint pair is unchanged by both legs. Zero extension over the K91
gauge summand remains representative-independent. The fourth leg then erases
the net data effect exactly; the clock position retains where the system is
inside the cycle.

## Maximum licensed conclusion

The K94 propagation and detector sequence can be compiled into one autonomous
finite unitary whose clock controls the local operations and whose fourth step
closes exactly. This removes an external per-step gate choice inside the finite
control, but it does not remove clock initialization, the chosen program, or
the artificial inverse closing leg.

No continuous-time Hamiltonian is selected: a finite unitary has many
logarithms, and this packet chooses none. The clock is not source geometry,
finite one-step support is not continuum microcausality, and the derived
record dilation still consumes the trace/Born pairing.

## Inline postflight bookend

- Strongest overclaim: calling a compiled four-state program a source-selected
  physical time or inferring a unique continuous-time Hamiltonian from `A`.
- Strongest contrary construction: omitting the inverse closing leg preserves
  a unitary clock shift but destroys `A^4=I` on data, so exact cyclic closure is
  owned by the explicit compilation rather than autonomy alone.
- Weakest reproducibility seam: all basis maps and phases are exhausted
  exactly, but clock-zero initialization and the program table remain supplied.

The exact probe passes `22/22`; its hostile selftest catches `15/15`
mutations. No source, continuum, microlocal, Born, prediction, confirmation,
canon, paper or held-out status moves.

## Next condition

Derive the clock, program and nontrivial long-time dynamics from one
repository-owned time-independent Hamiltonian without an inverse reset leg,
then test stability and action/net covariance. Source credit still requires an
authenticated GU functional action and physical quotient.
