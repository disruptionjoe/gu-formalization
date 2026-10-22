---
title: "K1953: Connection realizations of the fixed positive SE0 subspace"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional exact connection algebra; no source action, physical quotient or universal GU exclusion
scripts:
  - tests/channel-swings/k1953_spin_connection_stable_mass.py
  - tests/channel-swings/k1953_spin_connection_stable_mass_probe.py
---

# K1953: A connection must preserve the actual stable subspace

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: actual raw connection realization test on the K1951 stable subspace
carrier: conditional real1920 K77 fields with fixed real128 positive subspace LAYER=toy CHIRALITY=N/A
pairing: K1951 fixed positive quotient energy ON=constant_coefficient_observed_system
real_structure: real rational Clifford generators of signature seven positive and seven negative
grading: one-form and auxiliary raw slots; no physical cohomology
action_owner: repository-construction -- specified minimal connection ansatz
target: invariance and conservative mass realization MAP-TYPE=intertwiner
```

## 1. Question and precise scope

[K1951](k1951-coordinated-zero-southeast-principal-2026-10-22.md) constructs
an actual stable real128 subspace inside its changed all-covector SE0 raw
principal system. Its free algebraic mass lift is not automatically a
connection realization. Here the raw principal coefficients, stable injection
J, and positive energy H are fixed. The question is whether replacing the
four observed derivatives by a common Spin(7,7) connection realizes a
nonzero mass while preserving that SAME subspace.

SC-OP-04 ASSERTS a candidate four-independent-field grammar; SC-OP-05 is
UNCERTAIN about the unspecified nonzero-SE rival. SC-MAS-01 and SC-CHI-02
ASSERT a stylized curvature-mass toy, not the present realization. The
[source extraction](../../lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md)
leaves a barred-field/density/reality construction open and records the
ambient-sign versus total-grading collision. SC-META-53 remains UNCERTAIN.
No source, physics-ledger or canon disposition changes; LT-SM8, LT-GR6b and
AC-F1 remain NEEDS. The results below concern explicitly defined conditional
connection classes, not every source candidate or every possible subspace.

## 2. Spinor-only minimal connection: invariance already fails

Use the exact K1951 D0,D7,D8,D9, with invertible D0, and its stable injection
J obtained by stacking the32 actual raw sections. Set

    A_0=I, A_j=D0^{-1}D_j, j=7,8,9,
    A_j J=J C_j, L J=I, H C_j=C_j^T H.

L is the stated pivot left inverse, not a physical observation. For each
observed k let Omega_k be an arbitrary real spin matrix

    Omega_k=sum_(a<b) x_(k,a,b) gamma_a gamma_b.

There are4*91=364 independent real coefficients. Acting on all15 spinor
slots by the SAME connection gives the raw lower-order term

    K(x)=sum_k D_k (I_15 tensor Omega_k),
    V(x)=D0^{-1}K(x)J, M(x)=L V(x),
    E(x)=V(x)-J M(x).                                  (1)

The operator preserves im(J) exactly when E(x)=0. This is a raw equation;
no compressed system is substituted for an invariant restriction.
All K(x) have zero added southeast block because each D_k does.

**Exact exclusion.** The linear map x -> E(x) has rank364. Therefore
E(x)=0 forces EVERY Omega_k=0. In particular no nonzero conservative
Dirac mass is realizable in this class. The energy condition
`HM+M^T H=0` and mass conditions `{M,C_j}=0` are unnecessary for this
exclusion. The four directional contributions are allowed to cancel;
this is not a test of one generator at a time.

The machine-readable certificate selects364 entries of E into a square
rational matrix B and supplies an exact inverse. All selected entries lie
in the leakage equations, before the mass/energy rows. An independent
signed-bit Clifford construction rebuilds D_k, checks the time inverse,
reconstructs the actual raw section, and verifies `B^{-1}B=I`.
This finite identity proves the universal statement for all real x.

## 3. Quantitative and variable-coefficient consequences

In the declared coefficient coordinates the exact certificate has

    ||B^{-1}||_infinity = 109417/36.

Thus every attempted spinor-only realization satisfies

    max_selected |E(x)| >= (36/109417) max |x|.          (2)

This is a coordinate-dependent algebraic residual bound, not a
basis-independent physical energy estimate. No finite-difference or
small-singular-value argument is used.

Since J and all principal coefficients are constant, the same obstruction
holds pointwise for arbitrary real spacetime-dependent connection
coefficients x(t,y): invariance of the fixed subbundle requires x=0 at
each point. For measurable coefficients the assertion holds almost
everywhere wherever the multiplication equations are defined. It does
not cover a moving subbundle J(t,y), where derivatives of J can cancel
leakage, or a changed principal system.

## 4. Tensorial repair test

The spinor-only failure does not dispose of a connection that also acts on
the one-form index. For G_ab=gamma_a gamma_b write

    [G_ab,gamma_c]=sum_d gamma_d V_ab[d,c],
    V_ab[a,b]=2 eta_b, V_ab[b,a]=-2 eta_a.

Extend V by a zero auxiliary row/column. The corresponding explicitly
chosen covector-spinor action is

    rho_ab=I_15 tensor G_ab - V_ab^T tensor I_128.        (3)

The auxiliary slot carries G_ab alone. This is a changed, geometrically
motivated conditional ansatz, not a claim that the source selected this
same-background connection or barred map.

For this class impose the full linear system

    E(x)=0, {M(x),C_j}=0 for j=7,8,9, HM(x)+M(x)^T H=0.  (4)

The exact coefficient matrix has rank359 and a five-dimensional kernel.
Every kernel direction acts as ZERO on the stable fields: `V(x)=0`, hence
`M(x)=0`. Thus the added form-index action permits nonzero connection
coefficients but supplies no nonzero conservative Dirac mass in this class.
This five-dimensional statement is for ALL equations(4), not invariance alone.
In fact, the selected rank359 minor uses only leakage and anticommutation
rows, before any energy row. The same five zero-action vectors are its full
kernel. Thus imposing invariance and the Dirac anticommutation equations
already forces zero mass, even WITHOUT the energy condition.

The report supplies an invertible359-by359 rational minor and five independent
kernel vectors. The producer checks every full equation and zero reduced
image. The independent checker reconstructs the minor and checks that all
five combinations of actual raw connection actions annihilate J. The minor
bounds the kernel dimension above by5; the independent vectors bound it below
by5. This proves completeness without trusting a numerical rank threshold.
The pointwise extension applies to(4) on this fixed background too. No
field-strength or curvature interpretation is inferred from the zero action.

## 5. A surviving conservative potential and its exact dynamics

Do not read the mass exclusion as excluding every invariant tensor connection.
Take only `Omega_0=gamma_1 gamma_2`, all other observed connections zero,
with the covector-spinor action(3). Its reduced matrix R is explicitly supplied
in the report, and exact raw reconstruction proves

    D0^{-1} K J=J R, R^2=-I,
    H R+R^T H=0, [R,C_j]=0 for j=7,8,9.                (5)

This is a nonzero conservative internal rotation. Since R and every C_j are
invertible and commute, `{R,C_j}=2 R C_j` is nonzero: it fails the Dirac mass
condition. The positive example tests the strongest over-reading of the
negative result on the same raw system, not on an unrelated model.

For an arbitrary real time-dependent scalar a(t), consider

    partial_t u=sum_j C_j partial_j u+a(t) R u.

Writing theta(t)=integral_0^t a(s) ds and
`u=(cos(theta) I+sin(theta) R) v` reduces this equation exactly to the free
one for v. The multiplier is H-orthogonal by(5); this conditional potential
is a removable temporal internal rotation, not a massive dispersion relation.
For a real spacetime-dependent scalar a(t,y), the same term still preserves
the H energy of smooth solutions with vanishing boundary flux: the transport
term integrates to a boundary term and `u^T(HR+R^TH)u=0` pointwise. This energy
identity does not assert a general solution-existence theorem or removal of
spatial dependence. It does not identify a source-selected gauge field.

## 6. Verification and remaining bridge

The full coefficient span is explicit. Rank means a rational minor with an
inverse, not a floating threshold. Independent raw reconstruction and
load-bearing connection/covector faults are checked after a green baseline;
identity and pin faults are separate reporting checks. The pointwise and
residual arguments are analytic consequences of the finite identity.
This is internal verification, not external specialist acceptance, novelty
or proof-assistant certification.

A moving geometry, a different invariant carrier, a quotient without this
fixed section, form-index terms outside(3), unobserved-direction
coefficients, a full unitary parent and the source-admitted nonzero-SE rival
are outside the spinor-only exclusion. Actual source cell ordering, barred
pairings, action stationarity and physical observable/domain selection remain
separate obligations. A free stable mass from K1951 survives as an algebraic
construction; failure of a proposed realization does not erase it.
