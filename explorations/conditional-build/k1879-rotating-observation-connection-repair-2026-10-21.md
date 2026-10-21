---
title: "K1879: An exact rotating observation lift with its connection term"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional fixed-symbol conservative lift with a non-mass target connection; no pure-mass rotating lift, native GU identification or physical chirality
---

# A rotating mass lifts when its frame connection is retained

K1877's pure mass-plane travelling restriction does not prohibit a target
with an additional connection. Here the actual K1832 source complex
structure intertwines all three K1836 leading observation matrices. It
constructs an exact conservative rotating lift for any smooth phase theta(t,x),
with fixed principal symbols and leading observation. The target necessarily
contains the explicit term

```
F=(theta_t I + sum_i theta_i D_i/24) J/2.                 (1)
```

In this construction F vanishes only for a locally constant phase. It lies
outside the two-dimensional mass plane. Thus this is a constructive repair
in a changed target class, not a solution of the previously open pure-mass
rotating problem. Domain, observation range and circle holonomy are part of
the result, not inferred from pointwise covariance alone.

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
result: explicit complex-frame connection repair of a rotating differential observation
carrier: K1832 real16 source types and K1836 real4 target LAYER=toy CHIRALITY=N/A
pairing: fixed positive source H and target Euclidean form ON=real_L2_and_H1_domains
real_structure: real H-orthogonal and orthogonal matrix multiplication
grading: differential order and source-target intertwining
action_owner: repository-construction -- conservative first-order systems
target: full differential observation and its closed range MAP-TYPE=quotient
```

## 1. Actual coefficient data, not an abstract dimension match

Reuse K1840's constant mass repair C0=R C1, B0=R B1, S0=R S1,
where R is a fixed real number, with

```
P0=partial_t+A_i partial_i+C0,
Q0=partial_t+d_i partial_i+B0,       d_i=D_i/24,
O0=T_i partial_i+S0,                O0 P0=Q0 O0.
```

K1832's serialized complex structure, with signs+,+,-,- in the four
coordinate types, gives L satisfying

```
L²=-I,  L^T H=-HL,  [L,A_i]=0,  T_i L=J T_i,
J=D1 D2 D3,  J²=-I,  J^T=-J,  [J,D_i]=0.                (2)
```

The last identity is checked on the actual matrices for all four types.
The tempting formula L=24³A1A2A3 fails: the source symbols are not a
Clifford triple. Their stored commutant is essential. No replacement
representation, uncompressed invariant restriction or physical quotient
has been silently substituted.

SC-OP-04 ASSERTS candidate four-field grammar, SC-MAS-01 and SC-CHI-02
ASSERTS a stylized curvature-mass/decoupling toy, and SC-OP-05 and
SC-META-53 remain UNCERTAIN. WGS05 does not identify this real16 positive
system with the source's full20 placement, spinless gauge-potential map or
physical domain. This calculation changes none of those source statements,
RA-F1, AC-F1, LT-SM8, physics-ledger or canon verdicts.

## 2. Full construction for arbitrary spacetime phase

For a real C2 phase set U=exp(-theta J/2), W=exp(-theta L/2). These are
target-orthogonal and source-H-orthogonal. From(2), U T_i W^-1=T_i.
Define P= W P0 W^-1, Q=U Q0 U^-1, O=U O0 W^-1. Product differentiation
gives, with summation over spatial i,

```
C = W C0 W^-1 + (theta_t I+theta_i A_i)L/2,
B = U B0 U^-1 + (theta_t I+theta_i d_i)J/2,
S = U S0 W^-1 + theta_i T_i L/2.                          (3)
```

Thus P,Q,O retain their original leading matrices and OP=QO exactly.
The mass part is R[cos(theta)B1+sin(theta)B2], using B1 J=B2.
Every added C term is H-skew because A_i is H-self-adjoint and commutes
with the H-skew L. Every added B term is skew for the same reason.
Consequently the positive source and target energies are conserved on
cores where boundary terms vanish. The construction works for nonlinear
phase, acceleration and multidimensional dependence, not just a helix.

Direct checks independently expand the first-order equations
T_i C-BT_i+SA_i-d_iS=0 and the zeroth-order equation

```
sum_i T_i C_i + SC - S_t - sum_i d_i S_i - BS = 0.         (4)
```

All independent first phase derivatives and symmetric second jets enter.
The symbolic jet checks use several exact rational rotations; the proof
by product differentiation establishes all angles. They are not a finite
sample presented as an all-angle proof.

## 3. The repair cost and the pure-mass boundary

J,d1J,d2J,d3J are mutually Frobenius-orthogonal with squared norms
4,1/144,1/144,1/144. Each is orthogonal to B1 and B2. Therefore

```
||F||_F² = theta_t² + |grad theta|²/576.                  (5)
```

The added coefficient cannot be absorbed into a different mass amplitude
or angle. For theta=omega(x1-vt), its squared norm is
omega²(v²+1/576), including the characteristic speeds v=+/-1/24.
There is no exceptional nonzero speed at which it disappears. For a pure
time rotation it is theta_t J/2; even spatially constant rotation needs it.

This exhausts the no-connection condition in the particular conjugation
construction. It does not classify arbitrary C,S for a pure rotating target,
and does not contradict K1877's necessary Gram control or static-slope
offset obstruction. The successful model explicitly adds non-mass target
components and different source/observation curves. Whether a native GU
connection supplies these particular terms remains a separate question.

## 4. Closed domains, evolution and observation range

On R3 take theta and its first derivatives locally continuous in time,
with spatial derivatives bounded on each finite time interval. Then U,W
and their inverses are bounded unitary multipliers on L2, and preserve H1
by the product rule. Smooth bounded higher derivatives preserve the
Schwartz core when required. These hypotheses are used only for this
global domain statement; the local differential identity needs C2.

The constant symmetric-hyperbolic generators with bounded constant skew
terms generate the usual unitary evolution. In complexified Fourier
space this follows from skew-Hermitian finite matrices; restriction to
real data is preserved. The repaired source propagator is
W(t) E_P0(t-s) W(s)^-1, and the target analogue uses U. These formulas
give the common-domain evolution and conservation directly, without an
unproved global conclusion from a pointwise rank calculation. An
unbounded-gradient phase requires a separately specified transported
domain; it is not covered by the fixed H1 claim.

For constant nonzero R the base observation has

```
O0 O0^dagger = alpha(-Delta+576 R²) I,
||O0^dagger (O0 O0^dagger)^-1|| <= 1/(24|R|sqrt(alpha)).  (6)
```

K1840's cross-Gram terms vanish; its S0 H^-1 S0^T is576alpha R² I.
Fourier multiplication proves that the displayed right inverse maps L2
to the observation domain and O0 times it is the identity. Therefore the
constant-mass observation is onto L2. At each time the repaired Gram is
U(O0 O0^dagger)U^-1, with the same positive lower bound, and the right
inverse is W O0^dagger (O0 O0^dagger)^-1 U^-1. Norm, kernel and range
are transported exactly. This is a bounded observation lift, not a claim
that this chosen right inverse intertwines the source and target evolution.

At R=0 there is no positive gap on R3 and no bounded right inverse from
all L2 with the L2 source norm; arbitrarily low Fourier frequencies prove
this. Unitary frame multiplication cannot repair that fact. On a torus
the massless missing constant modes transport with U; a frame change
does not create modes absent from the observation. No physical mode
count or chirality follows from these analytic range statements.

## 5. Global circle control: winding changes the domain

Suppose theta(x1+ell)=theta(x1)+2pi n. Then U and W acquire the same
factor(-1)^n around the circle. The coefficients(3) and the leading
observation are periodic, because the two signs cancel in conjugations
and derivatives are periodic. But odd n maps periodic fields to
antiperiodic fields. Only even n preserves the original periodic domain.
For odd n the exact equivalence is between the corresponding twisted
domains. It is invalid to claim identical periodic-domain spectra using
a nonperiodic unitary. The real connection holonomy is(-1)^n I;
locally pure gauge does not imply globally trivial on a fixed domain.

For a time-independent phase the spatial generators are unitarily
equivalent on these matched domains. A time-dependent phase has the
extra time connection in(3); equality of instantaneous spatial spectra
is not asserted, although the full propagators are related as above.

## 6. Verification and next discriminating task

The exact producer checks the four complex transports, energy commutants,
all first/second jet equations, mass rotation, Gram gap and orthogonal
connection cost. A separate probe tests coefficient faults and reconstructed
operator identities on exact rational jets, with a clean baseline before
mutations. Analytic conjugation, multiplier-domain, Fourier and holonomy
arguments carry continuum/global claims; no proof assistant, external expert
or new general gauge theorem is claimed.

The meaningful next source-facing task is to identify an actual native
coefficient/pairing/observation-domain adapter and test whether it supplies
this connection or requires a different one. The pure mass-plane rotating
fixed-T nonlinear lift remains open; this explicit repair is not its proof.
Repeating automatic frame covariance would add no new constraint.
