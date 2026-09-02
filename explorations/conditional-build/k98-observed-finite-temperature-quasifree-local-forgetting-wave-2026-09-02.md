---
title: "K98 observed finite-temperature quasifree local-forgetting wave"
status: active_research
doc_type: reverse_scaffold_finite_temperature_quasifree_local_forgetting_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K97_FINITE_TEMPERATURE_FIXED_LOCAL_VERSUS_GLOBAL_RETURN_BOUNDARY
claim_ceiling: exact fixed-finite-region return of a supplied rank-one gauge-invariant quasifree excitation to the free half-line CAR beta-KMS background while global state distance stays positive and covariance trace distance stays delta; no record instrument, global thermalization, KMS preparation or production of a record, source selection, interacting return to equilibrium, continuum spacetime AQFT, microlocal state, derived Born law, prediction, confirmation or verdict
manifest: lab/process/k98-observed-finite-temperature-quasifree-local-forgetting-wave.json
probe: tests/channel-swings/k98_observed_finite_temperature_quasifree_local_forgetting_probe.py
---

# K98 observed finite-temperature quasifree local-forgetting wave

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
result: fixed-local quasifree return with persistent global excitation above a free finite-temperature CAR equilibrium background
carrier: CAR(l2(N0)) with one-particle h=2I-(S+S*) LAYER=observed CHIRALITY=N/A
pairing: gauge-invariant quasifree covariance-to-CAR-correlation pairing ON=repository_owned_CAR_control
real_structure: CAR adjoint and occupation-basis conjugation
grading: fermion parity and gauge-invariant even correlations; no source BV, BFV or ghost grading
action_owner: repository-construction
target: fixed finite-region state restrictions versus global state and covariance norm topology MAP-TYPE=restriction
```

Scope: this result binds only the free half-line CAR dynamics, its standard
algebraic beta-KMS covariance and one supplied rank-one non-KMS quasifree
excitation. “Local” always means a fixed finite set of sites before the
large-time limit. It does not mean a growing light cone, uniform return over
all regions, or a global state-norm limit.

## Inline preflight bookend

The route-changing census covered the K97 half-line Jacobi/Bessel kernel,
gauge-invariant CAR quasifree states, algebraic KMS covariance, finite-region
restriction, Wick determinants, local-versus-global state topology, trace-
class covariance perturbations, scattering escape and return to equilibrium.
The cheapest exact boundary test is the K97 one-particle kernel acting on a
rank-one excitation above the finite-temperature covariance.

Retrieval found K90's finite leading KMS detector response, K95's supplied
nonthermal dissipative stabilization, K96's outgoing translation record and
K97's algebraic beta-KMS background beside a separately prepared vacuum/one-
particle record instrument. It found no packet proving finite-temperature
fixed-local quasifree return while retaining the exact global norm
obstruction. Standard CAR, quasifree, KMS and Bessel facts receive no
literature-novelty claim.

## Thermal background and supplied excitation

Let `h1=l2(N0)` with basis `e_n`, let `S e_n=e_(n+1)`, and use the K97
one-particle Hamiltonian and dynamics

```text
h=2I-(S+S*),        0<=h<=4,        U_t=exp(-ith).           (1)
```

For every `beta>0`, the free CAR dynamics has the gauge-invariant algebraic
beta-KMS state `omega_beta` with covariance

```text
C_beta=(1+exp(beta h))^(-1),       0<C_beta<=1/2.            (2)
```

Fix `0<delta<=1/2` and supply the perturbed covariance

```text
C_1=C_beta+delta |e_0><e_0|.                                 (3)
```

Functional calculus and `delta |e_0><e_0|<=delta I<=I/2` give
`0<C_1<=I`, so (3) defines a gauge-invariant quasifree CAR state `omega_1`.
This preparation is imported. It is not KMS: the rank-one projector does not
commute with `h` (`[h,|e_0><e_0|]e_0=-e_1`), so the state is not invariant
under the free dynamics.

With the evolved covariance convention

```text
C_1(t)=U_t C_1 U_t*=C_beta+delta |U_t e_0><U_t e_0|,          (4)
```

the exact K97 half-line kernel is, for every `n>=0`,

```text
<e_n,U_t e_0>
 =exp(-2it) i^n [J_n(2t)+J_(n+2)(2t)]
 =exp(-2it) i^n (n+1)J_(n+1)(2t)/t,                         (5)
```

with the continuous values `1` for `n=0,t=0` and `0` for `n>0,t=0`.
The fixed-order Bessel asymptotic makes every fixed-site amplitude tend to
zero.

## Exact fixed-local forgetting

For a fixed finite region `Lambda subset N0`, let `P_Lambda` be its one-
particle projection. Restricting (4) gives the rank-one difference

```text
P_Lambda(C_1(t)-C_beta)P_Lambda
 =delta |P_Lambda U_t e_0><P_Lambda U_t e_0|,                (6)

||P_Lambda(C_1(t)-C_beta)P_Lambda||_1
 =delta ||P_Lambda U_t e_0||^2
 =delta sum_(n in Lambda) |(n+1)J_(n+1)(2t)/t|^2 ->0.       (7)
```

Gauge-invariant quasifree correlations on `CAR(Lambda)` are finite Wick
determinants in the restricted covariance entries (and the complementary
contractions). Equation (7) therefore implies convergence of every local CAR
correlation and, because `CAR(Lambda)` is finite dimensional, norm convergence
of the restricted states:

```text
omega_1,t|CAR(Lambda) -> omega_beta|CAR(Lambda).             (8)
```

This is fixed-local forgetting at finite temperature, not convergence on the
quasilocal algebra in state norm.

## Persistent global distinction

Globally, automorphism isometry and beta-KMS invariance give

```text
||omega_1,t-omega_beta||
 =||omega_1-omega_beta||>0.                                  (9)
```

Positivity is already witnessed at `t=0` by the norm-one occupation effect
`a*(e_0)a(e_0)`, whose expectation difference is `delta`; at later times its
automorphic image supplies the same witness. At covariance level, unitarity
preserves the complete trace-class perturbation exactly:

```text
||C_1(t)-C_beta||_1
 =delta || |U_t e_0><U_t e_0| ||_1=delta.                  (10)
```

Thus the excitation leaves every fixed observation window while remaining a
globally present, coherently transported one-particle covariance increment.
No dissipation, bath-induced erasure or global thermal attractor occurs.

## Owner accounting

Repository-owned in this packet: the exact specialization of the K97 Bessel
kernel to (4), the finite-region trace-norm identity (7), the Wick-continuity
local-return consequence, and the explicit local/global topology separation
(9)--(10).

Imported: the half-line CAR algebra and free dynamics, the standard
gauge-invariant quasifree/KMS theorem, `beta`, the supplied perturbation size
`delta`, the non-KMS covariance (3), and the covariance-to-correlation state
pairing. Source-selected owners: zero.

## Maximum licensed conclusion and fences

One supplied rank-one quasifree excitation above the algebraic free beta-KMS
state becomes invisible in every fixed finite CAR region, while the global
state distance remains strictly positive and its covariance trace distance
remains exactly `delta`. This proves a topology boundary for the named free
model only.

It supplies no record effects, Kraus maps, instrument, pointer algebra or
record semantics. It does not globally thermalize `omega_1`, make `omega_1` a
KMS state, or show that a KMS state produces a record. It proves no interacting
return to equilibrium, uniform/growing-region relaxation, continuum spacetime
AQFT, microcausality, microlocal/Hadamard condition, source-selected state,
Born rule, prediction, confirmation, held-out score, canon or paper result.

## Inline postflight bookend

- Strongest overclaim: replacing fixed-local convergence (8) by global state-
  norm thermalization. Equation (9) proves the opposite.
- Strongest contrary construction: if `h` had a localized bound component
  overlapping `e_0`, its fixed-region amplitude need not vanish; the purely
  absolutely continuous half-line kernel is load-bearing here.
- Weakest reproducibility seam: fixed-order Bessel decay and quasifree Wick
  continuity are analytic facts; the deterministic probe checks the exact
  kernel series, finite-region formula, covariance/state fences and hostile
  mutations, not an interacting return theorem.

No source, instrument, global-thermalization, KMS-record, interacting-return,
continuum-AQFT, microlocal, Born, prediction, confirmation, held-out, canon,
paper or public-posture status moves.

## Next condition

Prove an analogous local/global boundary for a source-owned interacting local
dynamics with an admitted thermal state and specified growing-region topology,
or derive a genuine return-to-equilibrium statement under explicit scattering
and mixing hypotheses without silently upgrading it to global state-norm
convergence.
