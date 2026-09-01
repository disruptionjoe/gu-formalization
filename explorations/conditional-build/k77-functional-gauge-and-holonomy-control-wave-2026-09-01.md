---
title: "K77 functional gauge and holonomy-control wave"
status: active_research
doc_type: reverse_scaffold_functional_gauge_and_supplied_connection_control_result
date: 2026-09-01
claim_ceiling: exact compact action-owned functional control, noncompact closed-range obstruction and supplied rank-two holonomy discriminator; no GU-native action/domain/quotient, I1B connection, prediction, confirmation, or verdict
manifest: lab/process/k77-functional-gauge-and-holonomy-control-wave.json
probe: tests/channel-swings/k77_functional_gauge_holonomy_probe.py
---

# K77 functional gauge and holonomy-control wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_CONTROL_ONLY`

```gu-typed-objects
result: compact action-owned functional gauge control plus noncompact closed-range obstruction and supplied rank-two holonomy discriminator
carrier: Maxwell slice H^{s+1}(T^2;R^2) x H^s(T^2;R^2), noncompact H^1(R), and separate rank-two real symplectic controls LAYER=conditional CHIRALITY=N/A
pairing: Maxwell quotient energy, H^1/L^2 norms, and separately supplied alternating/positive forms ON=three_distinct_control_carriers
real_structure: real Abelian gauge fields and real rank-two symplectic matrices
grading: two-term gauge/constraint complex from the supplied Maxwell action; no K77 Koszul--Tate/BV grading
action_owner: conventional Maxwell control owns d0, Gauss constraint and evolution; no GU action and no I1B connection selected
target: K77-PSX-1 through K77-PSX-4 and K77-PSX-7 analytic release conditions plus the independent I1B supplied-connection discriminator MAP-TYPE=classification
```

## Result

The prior wave proved that the observed principal projector and positive
energy cannot choose a gauge complex. This wave supplies an action that does
choose one—but only as an explicitly conventional control.

On the named globally cooriented ultrastatic cylinder

```text
D_control = [0,1] x T^2,
g = -dt^2 + dx^2 + dy^2,
future normal = dt,
```

the Abelian Maxwell action owns the gauge differential, Gauss constraint and
full constant-coefficient evolution. On a time slice,

```text
d0(phi) = (grad phi, 0),
C(A,E) = div E,
partial_t A = E,
partial_t E = Delta A - grad div A.
```

Every nonzero Fourier mode `k in Z^2` has `|k|^2 >= 1`. After splitting off
the constant kernel, `grad` maps mean-zero `H^{s+1}` isomorphically onto the
exact `H^s` one-forms, so its gauge image is closed. The evolution preserves
Gauss, fixes residual gradient-gauge directions, and descends to the
transverse quotient coordinates

```text
Q = k cross A,
P = k cross E,
Qdot = P,
Pdot = -|k|^2 Q.
```

The quotient energy `1/2(P^2/|k|^2 + Q^2)` is representative-independent and
conserved. The zero mode is not derivative gauge; it survives as harmonic
physical control data.

This is the first action-owned functional quotient control in this K77 reverse
scaffold. It is not a GU action or a bridge into the observed rank-1920
carrier. It proves that action ownership, functional closed range and quotient
propagation are jointly feasible when compact topology supplies a spectral
gap.

The analytic limitation is exact. For the derivative

```text
D : H^1(R) -> L^2(R)
```

and normalized triangular dilates
`phi_R(x)=R^(-1/2) max(1-|x|/R,0)`,

```text
||phi_R||_2^2 = 2/3,
||D phi_R||_2^2 = 2/R^2.
```

The derivative is injective but not bounded below; its range is therefore not
closed. A compact Fourier/Poincare proof cannot be transferred to a
noncompact GU domain without its own coercive estimate, weighted topology,
elliptic complex or other closed-range theorem.

Independently, three supplied rank-two symplectic monodromies sharpen the I1B
connection gate. The rotation with trace zero preserves `H=I`. The hyperbolic
matrix `diag(2,1/2)` has trace `5/2` and admits no positive invariant
majorant. The nontrivial parabolic matrix `[[1,1],[0,1]]` has trace `2` but
also admits none: its Jordan shear forces the first diagonal coefficient of
any invariant symmetric form to vanish. Thus trace `2` alone does not certify
a compact/unitary reduction. None of these matrices is I1B holonomy; the
packet still owns no connection or parallel transport.

The exact probe passes `69/69`; its hostile selftest catches `19/19`. No
actual GU domain, source-native action, observed constraint/BV complex,
physical quotient, I1B connection or GU-native state is constructed.

## 1. Action ownership closes the algebraic loop in the control

The action is

```text
S_control[A] = -(1/4) integral_D F_{mu nu} F^{mu nu}.
```

Its gauge symmetry `A -> A + d phi` supplies `d0`; variation of `A_0`
supplies Gauss; and the spatial Euler--Lagrange equations supply the evolution
above. All tangential coefficients are explicit and constant, while every
subprincipal/lower-order coefficient is exactly zero. The complex is not
chosen from the boundary projector or energy after the fact.

For a nonzero Fourier mode the gauge vector is `(k,0)`. The Maxwell generator
annihilates it, preserves `k dot E=0`, and induces the oscillator system on
`(Q,P)`. This supplies the exact owner/propagation relation that the planted
finite complex could only assume.

## 2. Compactness is doing real analytic work

The closed-range proof uses the integer Fourier gap. It is not the statement
that every derivative image is closed. The dilation sequence on `R` removes
that gap while retaining unit-order `H^1` norm, so no positive lower bound for
`||D phi||_2 / ||phi||_{H^1}` exists. Since an injective bounded operator with
closed range has a bounded inverse on its range, the range here is not closed.

This counterexample converts “prove Sobolev closed range” into a typed domain
question. A future K77 action must own not only its differential but also the
topology and estimate that close its image.

## 3. Supplied connection data can fire the holonomy test

For a rank-two symplectic fibre, monodromy lies in `SL(2,R)`. An invariant
positive majorant conjugates it into a compact orthogonal group, hence requires
semisimple unit-circle behavior. The exact controls show all three regimes:

- elliptic rotation: positive invariant majorant exists;
- hyperbolic scaling: none exists;
- nontrivial parabolic shear: none exists despite boundary trace `2`.

This is a discriminator, not an I1B computation. The I1B packet must first
supply a fixed-rank quotient bundle, connection, loops and parallel transport.

## 4. Hostile close and next frontier

The strongest overclaim would identify the Maxwell control with the missing GU
source action. It is not source-attested, has a different carrier, and no
typed observation map connects it to K77. The strongest contrary route is a
source-native or explicitly owner-native K77 action whose variation supplies a
different complex and whose actual noncompact geometry still has closed range.
The weakest seam is precisely that functional estimate.

The next observed-packet object is therefore an owner-native action with a
typed map to the rank-1920 carrier, plus a compactness, ellipticity, weighted
coercivity or other estimate that proves its gauge image closed. The independent
I1B alternative is unchanged in ownership but sharper in acceptance: compute
actual monodromy, check Jordan type as well as trace, then test invariant
majorants.

The Maxwell, observed and I1B carriers remain noncomposable. No actual GU
domain, source-native action, observed constraint/Koszul--Tate/BV complex,
continuum GU propagation theorem, Sobolev closed-range theorem on a GU domain,
physical quotient, GU-native state, Born rule, composite, instrument algebra,
I1B connection or actual holonomy, prediction, confirmation, held-out success,
canon change, paper status, public-posture change or GU verdict is created.
Delayed-choice entanglement swapping remains reserved and unscored.
