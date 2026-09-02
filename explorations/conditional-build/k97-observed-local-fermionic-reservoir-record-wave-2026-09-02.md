---
title: "K97 observed local fermionic reservoir record wave"
status: active_research
doc_type: reverse_scaffold_local_fermionic_reservoir_record_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K96_LOWER_BOUNDED_LOCAL_CONTINUUM_ASYMPTOTIC_RECORD_OWNER
claim_ceiling: exact lower-bounded local half-line CAR reservoir with algebraic free beta-KMS state and a separately prepared vacuum/one-particle asymptotic record instrument; no claim that the KMS state prepares that instrument, no source selection, interacting thermal return, continuum spacetime AQFT, microlocal state, derived Born law, prediction, confirmation or verdict
manifest: lab/process/k97-observed-local-fermionic-reservoir-record-wave.json
probe: tests/channel-swings/k97_observed_local_fermionic_reservoir_record_probe.py
---

# K97 observed local fermionic reservoir record wave

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
result: lower-bounded local half-line CAR reservoir with exact asymptotic vacuum-versus-escaped-particle record instrument
carrier: C2_q tensor Gamma_a(l2(N0)) with common domain C2_q tensor D(dGamma(h)) LAYER=observed CHIRALITY=N/A
pairing: imported state-effect pairing for the vacuum/boundary-site versus escaped-particle effects ON=repository_owned_CAR_control
real_structure: occupation-basis conjugation and CAR adjoint
grading: K94 propagated parity label q and fermion-number sectors; no source BV, BFV or ghost grading
action_owner: repository-construction
target: local semibounded many-mode reservoir asymptotic record instrument MAP-TYPE=evaluation
```

Scope: this result binds the half-line tight-binding CAR model, its free
algebraic equilibrium state, and a separately supplied conditional
vacuum/one-particle input. The finite-temperature KMS state exists, but it is
not the preparation used to obtain the admitted instrument.

## Inline preflight bookend

The route-changing census covered semibounded spectral uniqueness, half-line
Jacobi operators, CAR quasi-free dynamics, local boundary emission, Bessel
decay, finite-volume recurrences, Gibbs normality, algebraic KMS covariance,
Lieb--Robinson locality, detector effects and reduced instruments. A local
half-line free-fermion reservoir is the cheapest exact model that improves
K96 simultaneously on lower boundedness, many-mode locality and an explicit
asymptotic instrument.

Retrieval found K95's finite recurrence and supplied GKSL arrow, K96's one
unbounded-below translation coordinate, W183's finite-grid Fano/Krein pole
model and W193's finite-quadrature Ohmic/Drude capture threshold. None gives
an infinite local CAR chain, its exact boundary spectral measure, algebraic
beta-KMS covariance and a fixed asymptotic record instrument. Standard CAR,
Jacobi/Bessel and quasi-free KMS facts receive no novelty claim.

## Local semibounded reservoir

Let `h1=l2(N0)` with basis `e_n`. For the unilateral shift
`S e_n=e_(n+1)`, set

```text
h=2I-(S+S*),                  0<=h<=4.                         (1)
```

On the antisymmetric Fock space `F=Gamma_a(h1)`, define

```text
H=dGamma(h)
 =2 sum_(n>=0) c_n* c_n
  -sum_(n>=0)(c_(n+1)* c_n+c_n* c_(n+1)),                    (2)
```

on `D(dGamma(h))`. Equation (2) is number preserving,
self-adjoint, nonnegative and nearest-neighbor local. Its unboundedness above
comes from arbitrarily large finite particle number, not negative energy.

For every `beta>0`, the free CAR dynamics has the gauge-invariant algebraic
quasi-free beta-KMS state with covariance

```text
C_beta=(1+exp(beta h))^(-1).                                  (3)
```

On the infinite half-line this is an algebraic state, not a normal Gibbs
density in the vacuum Fock representation. Equation (3) is an equilibrium
control only. The record calculation below uses different, non-KMS inputs.

## Conditional input and exact local escape

Import the K94 label with weights `Pr(q=0)=2/3`, `Pr(q=1)=1/3`, and prepare

```text
q=0: Omega,                  q=1: c_0* Omega.                 (4)
```

This conditional preparation is supplied; it is not derived from (2) or (3).
The vacuum is stationary. The one-particle branch evolves by `exp(-ith)e_0`.
The boundary spectral measure is

```text
dmu(E)=(1/(2pi))sqrt(E(4-E)) 1_[0,4](E)dE,                   (5)
```

so its exact boundary survival amplitude is

```text
a(t)=<e_0,exp(-ith)e_0>=exp(-2it) J_1(2t)/t,                 (6)
a(0)=1.                                                       (7)
```

The Bessel asymptotic gives `a(t)=O(t^(-3/2))`, hence
`|a(t)|^2=O(t^(-3))`.

On the admitted zero/one-particle sector use the fixed effects

```text
R0=|Omega><Omega|+|e_0><e_0|,       R1=I-R0.                 (8)
```

Outcome zero means vacuum or still at the ready boundary site; outcome one
means the admitted particle has escaped into sites `n>=1`. Then

```text
Pr(R!=q)=(1/3)|a(t)|^2,
Pr(R=1)=(1/3)(1-|a(t)|^2),
Pr(R=0)=2/3+(1/3)|a(t)|^2.                                  (9)
```

The exact reduced classical instrument on the label algebra is

```text
I0_t(rho)=P0 rho P0+|a(t)|^2 P1 rho P1,
I1_t(rho)=(1-|a(t)|^2)P1 rho P1.                             (10)
```

It is completely positive and trace preserving in sum, and converges to the
projective record instrument

```text
I0_infinity(rho)=P0 rho P0,       I1_infinity(rho)=P1 rho P1. (11)
```

Zeros of `J1` give isolated exact-readout instants, but the amplitude becomes
nonzero again. Stable exactness is asymptotic, exactly as the companion
semibounded-boundary packet requires. Finite-chain truncation restores
almost-periodic recurrence and is therefore a negative control, not evidence
for (11).

The fixed input map already places the two labels in orthogonal fermion-number
sectors, so it destroys label coherences before the escape calculation. The
new result is local stabilization of the classical record location, not a
derivation of measurement or Born probability.

The K94 endpoint marginal is carried as an untouched external factor, and
zero extension over K91's gauge summand preserves the same repository-owned
basic descent control.

## Maximum licensed conclusion

A lower-bounded, infinite, nearest-neighbor CAR reservoir has an exact fixed
reduced record instrument whose mismatch tends to zero with the Bessel tail.
The same free dynamics admits an algebraic beta-KMS state, but that state does
not prepare or prove the vacuum/one-particle instrument. This is a local
many-mode reservoir control, not a source-selected physical measurement model.

## Inline postflight bookend

- Strongest overclaim: saying the beta-KMS state produces the record. It does
  not; the conditional input (4) is separately supplied and nonthermal.
- Strongest contrary construction: a finite chain is also local and
  lower-bounded but recurs. Infinite absolutely continuous spectrum is the
  load-bearing escape resource.
- Weakest reproducibility seam: the exact Bessel transform and CAR KMS
  covariance are analytic identities; the probe checks their series,
  spectral moments, positivity, instrument algebra and hostile mutations,
  not a source-action derivation.

No source, interacting-KMS return, spacetime AQFT, microcausality,
microlocal/Hadamard, Born, prediction, confirmation, canon, paper or held-out
status moves.

## Next condition

Derive the conditional preparation and record algebra from a source-owned
local interaction, or prove the asymptotic instrument from an admitted
finite-temperature algebraic KMS input without importing the vacuum/one-
particle branch assignment.
