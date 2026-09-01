---
title: "K77 packet-local positive-state extension wave"
status: active_research
doc_type: reverse_scaffold_packet_local_selection_obstruction_and_extension_contract
date: 2026-09-01
claim_ceiling: packet-local raw-linear selection obstruction plus carrier-neutral quadratic-lift feasibility; no GU-native physical state, action, prediction, confirmation, or verdict
manifest: lab/process/k77-packet-local-positive-state-extension-wave.json
probe: tests/channel-swings/k77_packet_local_positive_state_extension_probe.py
lean: Lean/GUFormalization/PacketLocalPositiveCone.lean
---

# K77 packet-local positive-state extension wave

## Result

The two live K77 packets cannot use their owned raw linear data itself as the
positive normalized state carrier demanded by `QD-R1-2` and `QD-R1-5`.
The reason is structural and narrower than a no-go for positivity:

> A sign-invariant pointed subset of an additive carrier contains only zero.
> Therefore the range of a linear map on a nontrivial carrier cannot itself be
> both a pointed and generating positive cone.

`Lean/GUFormalization/PacketLocalPositiveCone.lean` proves this statement and
also proves the phase version: if a proposed cone is preserved by a map whose
square is negation, then it cannot simultaneously be nontrivial, pointed and
generating. The theorem applies to a raw linear carrier or linear projector
range. It does **not** say that the carrier admits no positive cone after extra
structure is supplied.

The repair shape is constructive. An exact rational two-level model sends an
amplitude `v` to the rank-one matrix `v v^T`, so `v` and `-v` define the same
positive state. On the lifted carrier, the positive-semidefinite cone, trace
unit, projector effects, selective and nonselective instruments, reversible
quarter-turn phase action and contractive dephasing coexist exactly. The probe
passes `15/15`; its hostile selftest catches `13/13` mutations.

That model is a carrier-neutral feasibility witness. It is not attached to
either K77 packet and supplies no Born rule, complex Hilbert space, complete
positivity, tensor-product rule or GU physical state.

## 1. Formal selection boundary

Let `C` be the proposed positive subset of an additive carrier `V`. The three
relevant properties are:

1. **sign invariance:** `x in C` implies `-x in C`;
2. **pointedness:** `x,-x in C` implies `x=0`;
3. **generation:** every `v` is a difference of two members of `C`.

Sign invariance and pointedness make every member of `C` zero. On a nontrivial
carrier, the zero subset is not generating. Because the range of any linear
map is closed under negation, a raw projector range or linear solution range
cannot itself be the required proper order cone.

This isolates what the reverse scaffold must add. The state carrier must forget
amplitude sign by a ray, quadratic, positive-functional or equivalent lift,
and the physical order must be selected on the resulting carrier. Merely
renaming a linear subspace as the positive sector cannot work.

## 2. K77 I1B packet

The I1B packet owns a real linear distortion/metric fluctuation carrier, a
source-native quadratic Hessian at the local `T=0` fixed-boundary germ, formal
mixed Green data and fixed-rank stratum quotients. Those are material starting
objects, but none is yet the ordered state carrier.

The exact earlier calculations show that the Green representative is
presymplectic on the tracked carrier, with large radicals and a null/non-null
rank jump. The radical is not an owned gauge image, and the coupled symbol does
not select a common hyperbolic cone or physical closed domain. Consequently:

- the raw linear fluctuation carrier is sign-symmetric;
- the Green form is not a positive normalized event pairing;
- a fixed-rank stratum quotient is not yet the physical gauge quotient;
- no deterministic unit, effect interval, instrument algebra, phase family,
  decoherence family or composite marginal rule is owned.

The I1B result is therefore `not_selected_and_not_sufficient`, not
`impossible`. Its next constructive packet must independently establish the
physical quotient and a positive majorant or polarization before attempting
the quadratic state lift.

## 3. K77 observed-projector packet

The observed packet owns a distinct real rank-1,920 fermionic carrier,
conditional Clifford principal coefficients, a rank-960 incoming projector
after a normal is supplied, transported positive principal energy and
pointwise Green-isotropic doubled-Majorana horns.

Those facts control boundary propagation, not operational normalization. A
projector range is a linear subspace and hence contains every vector together
with its negative. Positive principal energy controls flux relative to the
supplied principal data; it does not turn the range into a pointed cone, supply
a trace-like unit, define event effects, or identify boundary projection with
gauge reduction. The normal selects a member of the projector family, while no
global physical horn or causal domain is selected.

This packet is independently `not_selected_and_not_sufficient`. It must build
its own physical quotient and positive majorant. Nothing from the I1B Green
packet may be imported to fill those cells.

## 4. Exact quadratic-lift control

The control uses rational two-component amplitudes and symmetric `2 x 2`
matrices. For normalized `v=(x,y)`, define

```text
rho(v) = v v^T = [[x^2, xy], [xy, y^2]].
```

Then `rho(v)=rho(-v)`, `rho(v)` is positive semidefinite, and its trace is one.
The identity is the deterministic effect; the coordinate projectors form a
normalized two-outcome instrument. Their nonselective sum removes the
off-diagonal terms while preserving trace. Conjugation by the rational
quarter-turn matrix preserves positivity and normalization, and its square is
amplitude negation while acting trivially on `rho(v)`. Multiplying the
off-diagonal entries by `eta` for `0 <= eta <= 1` gives an exact dephasing
control.

The model demonstrates that the sign obstruction points toward a viable
quadratic carrier extension rather than a dead end. It does not demonstrate
that either K77 packet selects that extension.

## 5. Minimal packet-local extension contract

Each packet must independently construct all seven objects:

1. a physical constraint/gauge quotient with representative-independent
   descent;
2. a positive majorant, real structure or polarization on that quotient,
   distinguished from the Green form or principal flux;
3. a quadratic, ray or positive-functional state carrier with a pointed
   generating cone;
4. a strictly positive deterministic unit and its effect interval;
5. a packet-local composite rule, local embeddings and marginals;
6. positive descended instruments on one named causal domain, including
   nonselective remote-marginal preservation;
7. reversible phase-sensitive and normalization-preserving decoherence maps
   on the same state/effect interface.

This is the backward-derived demand line for later action candidates. It does
not require an action in order to formulate or test the objects. An action may
receive forward-certification credit only after it independently owns them.

## 6. Custody and next frontier

The I1B distortion/metric packet and the observed fermionic projector packet
differ in carrier, variational owner, field role and domain. Their cells remain
noncomposable. The abstract density control is also not a third K77 candidate.

The next Big Wave is now sharply constructive: build the quotient and positive
majorant packets independently on I1B and on the observed projector, then test
whether either releases a packet-local quadratic state/unit/effect descent.
Failure of one packet reroutes capacity to the other packet or the next
compatible reverse edge; it does not return the program to source-action-first
search, maintenance, scale reduction or zero work.

No source action, physical state space, Born rule, prediction, confirmation,
held-out success, canon change, paper status, public posture or GU verdict is
created here. Delayed-choice entanglement swapping remains reserved and
unscored.
