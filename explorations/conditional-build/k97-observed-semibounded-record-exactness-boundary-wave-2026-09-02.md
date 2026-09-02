---
title: "K97 observed semibounded record exactness boundary wave"
status: active_research
doc_type: reverse_scaffold_semibounded_survival_boundary_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K96_LOWER_BOUNDED_HAMILTONIAN_RECORD_EXACTNESS_BOUNDARY
claim_ceiling: exact spectral boundary for one ready-state survival amplitude under a semibounded self-adjoint Hamiltonian; no prohibition on isolated zeros, asymptotic records, time-dependent effects, general instruments, source selection, thermalization, locality, Born derivation, prediction, confirmation or verdict
manifest: lab/process/k97-observed-semibounded-record-exactness-boundary-wave.json
probe: tests/channel-swings/k97_observed_semibounded_record_exactness_boundary_probe.py
---

# K97 observed semibounded record exactness boundary wave

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
result: semibounded ready-state survival cannot clear identically on any future time interval
carrier: one Hilbert space with a normalized ready vector psi LAYER=observed CHIRALITY=N/A
pairing: imported Hilbert inner product and ready effect |psi><psi| ON=repository_owned_spectral_boundary
real_structure: complex conjugation of the scalar survival amplitude
grading: K94 propagated parity sector only; no source BV, BFV, ghost or CAR grading
action_owner: repository-construction
target: exactness boundary for stable Hamiltonian record formation MAP-TYPE=evaluation
```

Scope: the theorem binds the scalar survival amplitude of one fixed ready
vector under one time-independent self-adjoint Hamiltonian bounded below. It
does not prohibit isolated zeros or asymptotic clearance, and it is not a
no-go for every possible record observable or instrument.

## Inline preflight bookend

The route-changing census covered K95 finite recurrence, K96's exact outgoing
translation, semibounded spectral measures, Hardy boundary uniqueness,
Paley--Wiener support, Cauchy/Lorentzian line shapes, truncated resonances,
Khalfin tails, local reservoirs and reduced instruments. The cheapest exact
question before constructing another reservoir is whether K96's finite-time
permanent clearance can coexist with a lower spectral bound.

Retrieval found K95's finite-dimensional obstruction and dissipative escape,
K96's unbounded-below translation record, W183's finite-grid Fano survival
sample and W193's finite-quadrature capture windows. None states the precise
semibounded interval-zero boundary or separates a pure exponential amplitude
from probability-only decay. Standard spectral and Hardy uniqueness facts
receive no novelty claim.

## Semibounded interval-zero boundary

Let `H=H*`, `H>=E0`, and let `psi` be normalized. Its survival amplitude is

```text
A(t)=<psi,exp(-itH)psi>=integral_[E0,infinity) exp(-itE) dmu_psi(E).       (1)
```

For `Im z<0`, the same integral defines a bounded analytic function
`F(z)`. If the boundary value `A(t)` vanishes on a nonempty open interval,
Hardy boundary uniqueness forces `F` to vanish identically. That contradicts
`A(0)=1`. Therefore

```text
A(t) cannot be identically zero on any nonempty future interval.             (2)
```

For the fixed ready effect `R_ready=|psi><psi|`, (2) says that exact
clearance cannot begin at a finite time and remain exact forever. Isolated
zeros are allowed. Decay to zero as `t` tends to infinity is allowed.

## Why the exact exponential has a two-sided spectrum

Suppose the stronger amplitude law

```text
A(t)=exp(-i E_* t-(gamma/2)t),       t>=0, gamma>0.                           (3)
```

holds. Unitary symmetry gives `A(-t)=conj(A(t))`, hence

```text
A(t)=exp(-i E_* t-(gamma/2)|t|),     t in R.                                 (4)
```

Fourier inversion uniquely gives the Cauchy density

```text
rho(E)=(1/pi)(gamma/2)/((E-E_*)^2+(gamma/2)^2),       E in R.                (5)
```

It is positive on every real-energy interval and is not bounded below. Thus
an exact constant-rate exponential survival *amplitude* for all future times
cannot be the spectral transform of a semibounded Hamiltonian. A statement
about `|A(t)|` alone, with an unspecified time-dependent phase, is not enough
to infer (5) and is deliberately outside the theorem.

The semibounded positive control

```text
dmu(E)=exp(-E) 1_[0,infinity)(E)dE,
A(t)=1/(1+it),                 |A(t)|^2=1/(1+t^2)                             (6)
```

has the permitted long tail: it never clears at finite time and tends to zero.

## Maximum licensed conclusion

K96's exact post-`t=1` sign clearance uses an unbounded-below translation
generator. In the narrower fixed-ready-projector construction, a
time-independent semibounded Hamiltonian cannot reproduce exact clearance on
an entire future interval. The honest semibounded target is an asymptotic
instrument, not finite-time permanent zero mismatch.

This is not a theorem against isolated perfect-readout instants, time-dependent
readouts, branch-dependent initial records, scattering apparatuses, general POVMs,
or asymptotic reservoir records.

## Inline postflight bookend

- Strongest overclaim: saying semibounded Hamiltonians cannot form records.
  They can form asymptotically exact records; only the stated interval-zero
  survival construction is excluded.
- Strongest contrary construction: the Cauchy spectral law gives exact
  exponential decay, but its support is all of `R`. Truncating it below
  restores semiboundedness and destroys the exact exponential law.
- Weakest reproducibility seam: Hardy boundary uniqueness is an analytic
  theorem, not proved by finite sampling; the probe verifies its hypotheses,
  exact transforms, logical fences and hostile mutations.

The exact probe runs positive controls before result checks and its hostile
selftest plants interval-zero, support, transform, phase-scope, isolated-zero,
asymptotic and promotion errors. No source, KMS, local-reservoir, microlocal,
Born, prediction, confirmation, canon, paper or held-out status moves.

## Next condition

Construct a lower-bounded local continuum reservoir whose fixed reduced
record instrument converges asymptotically, while keeping its preparation,
equilibrium-state status and source ownership explicit.
