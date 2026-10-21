---
title: "K1877: Travelling mass amplitude is rigid in the full conservative observation class"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-symbol positive conservative travelling mass-plane class; no native GU verdict or exclusion of rotating, changed-symbol or general spacetime coefficients
---

# A travelling mass cannot change amplitude in this conservative class

Keep K1840's fixed principal matrices, leading differential observation and
positive pairings. Allow arbitrary smooth travelling coefficients C(z),S(z),
including nonzero offsets, with z=x1-vt and any fixed v!=0. If the target
coefficient stays in the two-dimensional mass plane,
`B(z)=m(z)B1+n(z)B2`, exact conservative intertwining forces

```
m(z)²+n(z)² = constant.                                  (1)
```

A fixed-direction real mass is therefore constant on a connected interval.
In particular, the general affine-offset moving tanh kink left open in K1875
is impossible in this class: the192 quadratic equations need not be solved.
No zero-normalization, linearity or mass-local dependence assumption is used.
A positive Gram operator DOES admit a circular mass control, however; (1)
is not a proof that all moving mass-plane coefficients are impossible.

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
result: travelling mass-amplitude rigidity from full observation Gram evolution
carrier: K1840 real16 compressed source and real4 target, all four coordinate types LAYER=toy CHIRALITY=N/A
pairing: fixed positive source H and target Euclidean form ON=real_smooth_compactly_supported_fields
real_structure: real smooth travelling matrix coefficients and two real mass components
grading: differential order in the formal observation Gram identity
action_owner: repository-construction -- conservative fixed-symbol first-order equations
target: exact differential intertwining along z=x1-vt MAP-TYPE=quotient
```

## 1. Objects, scope and source boundary

Write

```
P=partial_t+A_i partial_i+C(z),
Q=partial_t+d_i partial_i+B(z),
O=T_i partial_i+S(z),            d_i=D_i/24.
```

All leading matrices and H are the pinned K1840 data. H is positive,
H A_i is symmetric, HC+C^T H=0, d_i is symmetric, B^T=-B, and OP=QO.
Take C,S and m,n of class C3 on a connected open z interval; this regularity
is more than sufficient for the identities used here. There is no global
boundedness, boundary condition, mass-zero or finite-energy eigenmode premise:
the obstruction already holds locally on compactly supported test fields.
All four source coordinate types are checked. Alpha>0 is their fixed scalar
principal Gram coefficient. D_i are normalized real Clifford matrices,
`{D_i,D_j}=2delta_ij I`, and J=D1 D2 D3 is skew, central, J²=-I.
The mass basis is skew, anticommutes with each D_i, and satisfies
B1²=B2²=-I, {B1,B2}=0 and B1 J=B2.

[K1875](k1875-nonlinear-moving-zero-obstruction-2026-10-20.md) correctly
rejects treating the full Gram as scalar: its first-derivative image has
four freedoms even at B=0. We retain all four. The current result extends
its zero-normalized obstruction and closes its specific general affine kink
question; it does not retroactively make its failed scalar-Gram shortcut valid.

SC-OP-04 ASSERTS candidate four-field grammar; SC-MAS-01 and SC-CHI-02
ASSERTS the stylized mass/decoupling toy; SC-OP-05 and SC-META-53 remain
UNCERTAIN. WGS05 does not identify these compressed coefficients or positive
pairings with the source's full connection/scalar-curvature bundle map.
This result binds the stated repository construction only. RA-F1, AC-F1,
LT-SM8, source adherence, physics-ledger and canon verdicts are unchanged.
It is neither physical chirality nor a falsification of the source claim.

## 2. Full Gram evolution, without discarding its first derivatives

The formal adjoint uses source H and target Euclidean pairing. Define
K=O O^dagger. Direct expansion gives

```
K=-alpha Delta + G_i(z) partial_i + V(z),
G_i=T_i H^-1 S^T-S H^-1 T_i^T,
V=T1 H^-1 (S')^T+S H^-1 S^T,
V-V^T=G1'.
```

Conservative intertwining implies

```
partial_t K + [d_i partial_i+B,K]=0.                       (2)
```

Indeed O_t+L_Q O-O L_P=0 and both spatial generators are formally
skew-adjoint in their fixed pairings. Differentiating O O^dagger cancels
L_P. This formal identity needs no spectral transfer or closed-domain claim.
The complete44-dimensional conservative pointwise bank has exactly

```
G_i=a_i(z) J+b(z)D_i J.                                   (3)
```

Every bank row is reconstructed and checked; its Gram image lies in this
four-dimensional span and has rank4. Equation (3) follows from the full
bank, not a preferred repair ansatz. No non-scalar G_i is omitted.

## 3. Nonzero travelling speed freezes every Gram derivative coefficient

Put a prime for d/dz. The coefficient of partial_j in (2) is

```
E_j=(-vI+d1)G_j'+[B,G_j]+[d_j,V]+2alpha delta_j1 B'=0.      (4)
```

Trace against J^T and (D_j J)^T. Clifford/mass-plane identities give

```
tr(J^T E_j)=4[-v a_j'+delta_j1 b'/24],
tr((D_j J)^T E_j)=4[-v b'+delta_j1 a1'/24].                (5)
```

The commutator with V drops from these traces because the test matrix
commutes with d_j; the mass-plane terms have zero trace. No symmetry of V
is assumed at this step. Taking j=2 gives b'=0 for every v!=0, then the
first identity for all j gives a_i'=0. This avoids any division by
v²-1/576 or hidden exceptional characteristic speed. Thus G_i are constant
and the formal self-adjointness identity gives V=V^T.

## 4. First-order matching and the two decisive traces

With constant a_i,b, the full solution of (4) among symmetric V is

```
V=u(z) I -24alpha D1 B' -24 sum_i a_i D_i B J.              (6)
```

Substitution verifies it. The difference between any two solutions commutes
with all D_i; their common symmetric commutant is exactly the scalars
(the exact10-column linear system has rank9). Thus (6) leaves no hidden
symmetric potential freedom. The coefficient b drops out because B commutes
with D_i J while it anticommutes with J.

The zeroth-order coefficient in (2) is

```
Z=(-vI+d1)V'+[B,V]+alpha B''-G1 B'=0.
```

Its two scalar traces are

```
tr Z = -4v u',
tr(D1 Z) = u'/6 -192alpha (m m'+n n').                    (7)
```

These polynomial identities are checked for two independently variable mass
components and their first two jets. Nonzero v gives u'=0; positive alpha
then gives (m²+n²)'=0, proving (1). For B=m B1 a further independent
projection is `tr((D1 B1)^T Z)=96alpha v m''`; it is a useful control,
not needed to derive constancy. A continuous fixed-direction real mass with
constant square is constant, including the zero case.

## 5. Consequences and exact assumption boundaries

The conclusion covers arbitrary smooth C(z),S(z), not just functions of m.
It therefore covers nonzero affine offsets, arbitrary smooth mass-local
curves, and derivative-dependent ansatzes that evaluate to smooth functions
of this same travelling coordinate. Such dependence alone cannot rescue a
changing amplitude. It rules out moving tanh kinks, nonconstant fixed-direction
pulses and travelling interpolation between unequal mass magnitudes in the
stated class. The static v=0 repair remains valid; the first trace then gives
no condition u'=0. Constant mass remains a valid control at every speed.

It does not exclude target coefficients with additional non-mass-plane
components, time/space dependence beyond z, moving H or target pairing,
changed principal symbols, or a changed leading observation. K1873's common
drift changes the principal symbols and remains a valid repair. Nor does
this theorem identify the fixed compressed setup with native GU coefficients.

## 6. Executed circular control: Gram compatibility is not an observation lift

Let `B(z)=R[cos(omega z)B1+sin(omega z)B2]`, so
B'=omega B J and B''=-omega² B. The constant operator

```
K=-alpha Delta-alpha omega J partial_1+u I
```

satisfies (2) exactly at every speed. It is positive on the real-line/Euclidean
Schwartz core whenever u>=alpha omega²/4, since

```
K=-alpha(partial_1+omega J/2)²-alpha partial_2²-alpha partial_3²
       +(u-alpha omega²/4)I.
```

This is a substantive contrary control: conservation and positive Gram
compatibility alone cannot eliminate constant-amplitude rotation. It does
NOT construct C,S or an O with the fixed leading T_i satisfying OP=QO.
The simplest attempted factorization adds `S0=J T1/2` to the static
mass observation with frequency scaling. Its massless offset fails the
complete pointwise first-order bank: adjoining `[B0=0,S0]` raises the
bank's rank by1 for all four types. Thus that particular circular lift fails
before any nonlinear calculation. This failed ansatz is preserved; it does
not exclude other factorizations or promote Gram compatibility to existence.

A broader follow-through also fails: keep the two saved static mass triples
(C1,B1,S1),(C2,B2,S2), and allow EVERY conservative massless constant offset
(C0,0,S0). For nonzero R,omega and v, the circular ansatz

```
C=C0+R cos(omega z)C1+R sin(omega z)C2,
S=S0+R cos(omega z)S1+R sin(omega z)S2
```

requires the two harmonic equations

```
S0 C1+S1 C0-B1 S0 = -v omega S2,
S0 C2+S2 C0-B2 S0 =  v omega S1.
```

The massless bank has38 coordinates. The128-by38 linear system has rank31,
whereas adjoining the normalized nonzero right-hand side raises rank to32
for all four coordinate types. The certificate stores rational dual witnesses
that annihilate every allowed column and pair to1 with the right-hand side;
the separate verifier reconstructs and checks these witnesses. Thus all such
offsets fail already at harmonic order; the remaining constant quadratic
condition S0 C0=0 cannot repair them. This is broader than the failed
S0=J T1/2 choice, but it still fixes the two static slopes and is not a
classification of every rotating coefficient curve.

The next genuinely different test is a full fixed-T factorization of a
constant-amplitude rotating mass with new coefficient curves, or an explicit
non-mass target connection.
The old192-equation changing-amplitude affine-kink search is now unnecessary.

## 7. Reproduction and hostile review

The [producer](../../tests/channel-swings/k1877_traveling_gram_amplitude_rigidity.py)
checks48 exact matrix/polynomial groups and4 input pins. The
[independent probe](../../tests/channel-swings/k1877_traveling_gram_amplitude_rigidity_probe.py)
reconstructs the conservative bank row by row, derives the differential
commutator through its action on exponential test fields, checks the circular
positive control, and tests planted mathematical and reporting faults.
The analytic formal-adjoint and connected-domain argument above owns the
continuum transfer. No proof-assistant or external expert verification is claimed.

Hostile review targeted the sign of O_t and the commutator, the 1/24 speed
normalization, possible non-symmetric V before G'=0, every full-bank Gram
freedom, exceptional nonzero speeds, both mass directions, positive versus
indefinite H, local versus global domains, arbitrary offsets, and the
necessary-versus-sufficient circular control. No unproved circular lift or
native physics consequence is included in the result.
