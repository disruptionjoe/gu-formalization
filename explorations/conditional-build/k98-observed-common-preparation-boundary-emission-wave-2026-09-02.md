---
title: "K98 observed common-preparation boundary-emission wave"
status: active_research
doc_type: reverse_scaffold_common_preparation_boundary_emission_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K97_COMMON_PREPARATION_CONTROLLED_LOCAL_EMITTER_RECORD_OWNER
claim_ceiling: exact common-preparation, q-controlled boundary-edge CAR model on the natural block-direct-sum Fock domain, with an invariant one-particle sector and asymptotically projective reduced instrument; no source-selected edge, emitter, readout, preparation, trace/Born pairing or physical record semantics, no new Bessel law, prediction, confirmation, held-out score, promotion or verdict
manifest: lab/process/k98-observed-common-preparation-boundary-emission-wave.json
probe: tests/channel-swings/k98_observed_common_preparation_boundary_emission_probe.py
---

# K98 observed common-preparation boundary-emission wave

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
result: common boundary-particle preparation followed by a q-controlled local edge whose reduced readout instrument converges to the projective q record
carrier: C2_q tensor Gamma_a(l2(N0)) with natural block-direct-sum domain (|0><0| tensor D(dGamma(k0))) direct_sum (|1><1| tensor D(dGamma(k1))) LAYER=observed CHIRALITY=N/A
pairing: imported trace/Born state-effect pairing for the emitter-site versus emitted-tail projection ON=repository_owned_controlled_edge_model
real_structure: occupation-basis conjugation and CAR adjoint; k0 and k1 are real Jacobi operators
grading: K94 propagated q label and fermion number; vacuum and one-particle sectors are invariant; no source BV, BFV or ghost grading
action_owner: repository-construction
target: common-preparation controlled local boundary-emission instrument MAP-TYPE=evaluation
```

Scope: this result binds one explicitly constructed half-line free-fermion
control. The label `q` controls the single edge between sites zero and one;
both label branches receive the same boundary one-particle preparation. The
words “emitter,” “emitted,” “readout,” “record,” and their state-effect/Born
semantics are imported interpretations of that control, not source-derived
physics.

## Inline preflight bookend

The route-changing census covered common environment preparations,
controlled Jacobi edges, CAR second quantization, natural direct-sum operator
domains, invariant number sectors, Stinespring instruments, Kraus-phase
freedom, Bessel boundary decay, finite-chain recurrence, source custody and
Born/readout semantics. The narrow decisive repair is to move the `q`
dependence from K97's input map into one local Hamiltonian edge. That preserves
label coherences at preparation and exposes the exact finite-time instrument.

Retrieval checked K91--K97 instrument and record packets, W183's finite-grid
Fano/Krein control and W193's finite-quadrature reservoir control. K97 already
owns the half-line spectral density and the law
`a(t)=exp(-2it)J1(2t)/t`; this packet reuses that law and makes no novelty claim
for Jacobi, CAR, Bessel or Kraus facts. No retrieved packet combines the same
boundary particle in both `q` branches with a single `q`-controlled boundary
edge and the coherence-correct outcome-zero map. The exact three K98 paths
were absent at admission, and the targeted search returned no semantic or
path collision.

## One controlled boundary edge on the natural domain

Let `h1=l2(N0)` with basis `e_n`, let `P_e=|e_0><e_0|`, and let the tail be
`h_tail=span{e_n:n>=1}`. On the tail define the same shifted half-line Jacobi
operator as K97. The two one-particle blocks are

```text
k0 = 2 P_e direct_sum [2I_tail-(S_tail+S_tail*)],
k1 = 2I-(S+S*).                                             (1)
```

Thus `k0` and `k1` differ only by the hopping edge
`-(|e_0><e_1|+|e_1><e_0|)`: at `q=0` the edge is off and at `q=1` it is on.
Both blocks are bounded self-adjoint operators with spectrum contained in
`[0,4]`; `k1` has spectrum `[0,4]`. On `F=Gamma_a(h1)`, set

```text
H = (P0 tensor dGamma(k0)) direct_sum
    (P1 tensor dGamma(k1)),                                  (2)
D(H) = (|0> tensor D(dGamma(k0))) direct_sum
       (|1> tensor D(dGamma(k1))).                           (3)
```

Equation (3), not `C2 tensor D(dGamma(k1))`, is the natural operator domain.
The two second-quantized blocks are self-adjoint and nonnegative on their own
domains, so their orthogonal direct sum is self-adjoint and nonnegative on
(3). The Hamiltonian preserves fermion number. In particular, the vacuum and
one-particle sectors are invariant, and every calculation below is made on
the invariant one-particle sector `C2_q tensor h1`; it is not a claim about an
uncontrolled many-particle preparation.

## Common preparation and exact reduced instrument

Use the same preparation for both labels:

```text
V |psi> = |psi> tensor c_0* Omega.                           (4)
```

Unlike K97's vacuum-versus-particle input, (4) preserves an arbitrary label
coherence. The label weights `2/3,1/3` remain the K94 imported benchmark, but
the instrument is defined on every label density matrix.

On the one-particle sector, the off-edge branch satisfies

```text
exp(-it k0)e_0 = exp(-2it)e_0.                               (5)
```

The on-edge branch is exactly K97's half-line boundary problem:

```text
a(t)=<e_0,exp(-it k1)e_0>
    =exp(-2it)b(t),       b(t)=J1(2t)/t,       b(0)=1.       (6)
```

No new claim is made for (6). K97's spectral calculation gives
`b(t)=O(t^(-3/2))` and `b(t)^2=O(t^(-3))`.

Import the binary one-particle readout

```text
Q0=|e_0><e_0|,                 Q1=I-Q0.                      (7)
```

The outcome-zero Kraus operator on the label is therefore

```text
K0(t)=<e_0|U(t)|e_0>
     =exp(-2it)P0+a(t)P1
     =exp(-2it)(P0+b(t)P1).                                  (8)
```

For `rho=(rho_ij)`, the exact operation is the full Kraus map

```text
I0_t(rho)=K0(t) rho K0(t)*
         =[[rho_00,       b(t)rho_01],
           [b(t)rho_10, b(t)^2 rho_11]].                     (9)
```

In particular, replacing (9) by only its diagonal terms would be wrong: the
common preparation leaves finite-time label coherences. For an orthonormal
tail basis, the outcome-one Kraus family has
`K_n(t)=<e_n|exp(-itk1)e_0>P1`, `n>=1`, so

```text
I1_t(rho)=(1-b(t)^2)P1 rho P1.                              (10)
```

Equations (9)--(10) are completely positive and their sum is trace
preserving. They converge pointwise and in finite-dimensional map norm to

```text
I0_infinity(rho)=P0 rho P0,
I1_infinity(rho)=P1 rho P1.                                 (11)
```

`K0(t)` itself does **not** converge: on the `q=0` line it is the oscillatory
phase `exp(-2it)`. The operation (9) does converge because the common
outcome-zero phase cancels in `K0 rho K0*`, while every relative term is
multiplied by the real decaying factor `b(t)`. Kraus-operator convergence is
neither required nor claimed.

For the imported diagonal benchmark `rho_q=diag(2/3,1/3)`, the mismatch and
readout weights remain

```text
Pr(R!=q)=(1/3)b(t)^2,
Pr(R=1)=(1/3)(1-b(t)^2),
Pr(R=0)=2/3+(1/3)b(t)^2.                                   (12)
```

This equality is a controlled-model consequence of the supplied weights,
edge, readout and Born pairing. It does not derive any of them.

## Owner accounting and maximum licensed conclusion

Repository-owned in this packet: the two Jacobi blocks; their natural
block-direct-sum Fock domain; self-adjoint nonnegative number-preserving
dynamics; invariance of the one-particle sector; the common-preparation
Stinespring calculation; the coherence-complete formula `I0=K0 rho K0*`; and
convergence of the two reduced maps despite nonconvergence of the displayed
Kraus representative.

Imported: the `q` carrier and weights, the choice that `q` controls the
boundary edge, the boundary particle as a common initial state, the
emitter/escape/readout/record interpretation, the effects (7), the
state-effect trace/Born pairing, K97's spectral density and Bessel law, the
endpoint marginal, and K91's gauge-basic zero extension. Source-selected
owner count remains zero.

The maximum licensed conclusion is therefore an exact local control: a common
one-particle preparation plus one label-controlled boundary edge yields an
asymptotically projective record instrument on the label. It repairs the
preparation-coherence defect of K97 inside a constructed model. It is not a
GU-native action, a source-selected measurement interaction, a derivation of
Born probability, or evidence for a physical emitter.

## Inline postflight bookend

- Strongest overclaim: calling the controlled edge or the boundary/tail split
  a source-owned measurement mechanism. Every semantic owner and the Born
  pairing remain imported.
- Strongest contrary construction: if both label blocks use `k1`, their
  boundary amplitudes coincide and the environment carries no `q` record; if
  a finite chain replaces the half-line, recurrence defeats stable map
  convergence.
- Weakest reproducibility seam: the Bessel identity and tail are inherited
  from K97. This packet's new reproducible burden is the direct-sum domain,
  invariant one-particle reduction, full off-diagonal Kraus algebra and the
  distinction between map convergence and Kraus-phase convergence.

The exact probe runs positive controls before result checks and passes
`34/34`; its hostile selftest catches `41/41` planted mutations. No source,
action, KMS preparation, interacting return, continuum AQFT,
microcausality, microlocal/Hadamard, Born, prediction, confirmation, canon,
paper, registry, current-state, held-out or promotion status moves.

## Holdout and promotion fences

Delayed-choice entanglement swapping remains reserved and unscored. This
packet is not a holdout confrontation, prediction, confirmation, hypothesis
vote, canon result, paper result or registry promotion. Cross-packet union is
forbidden without a later typed integration that rechecks every imported
owner.

## Next condition

Derive the `q`-controlled local coupling, common boundary preparation and
readout algebra from one authenticated source-owned action and physical
quotient, or replace the imported trace/Born pairing with a source-owned
probability rule. The present construction supplies none of those owners.
