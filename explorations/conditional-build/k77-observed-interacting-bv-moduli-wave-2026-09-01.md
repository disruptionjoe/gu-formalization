---
title: "K77 observed interacting BV moduli wave"
status: active_research
doc_type: reverse_scaffold_repository_owned_interacting_minimal_bv_result
date: 2026-09-01
claim_ceiling: exact repository-owned nonlinear interacting action family and formal minimal abelian BV completion on the previously constructed rank-1920 direct-summand quotient; coefficient-moduli nonselection, with no source-native gauge algebra, gauge-fixed quantum theory, analytic BV phase space, unique physical action, prediction, confirmation, or verdict
manifest: lab/process/k77-observed-interacting-bv-moduli-wave.json
probe: tests/channel-swings/k77_observed_interacting_bv_moduli_probe.py
---

# K77 observed interacting BV moduli wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: nonlinear interacting rank-1920 quotient-action family with a formal minimal abelian BV completion and exact coefficient-moduli nonselection
carrier: H1 sections of V1920=K960 direct_sum W960 on [0,1]xT3, with odd ghost sections of K960 LAYER=conditional CHIRALITY=N/A
pairing: transported positive quotient energy H on W and canonical algebraic field-antifield BV pairing ON=repository_owned_candidate_family
real_structure: real field and gauge carriers; parity shift only on the ghost and antifield variables
grading: K ghost in degree +1, fields in degree 0 and antifields in negative degree; minimal abelian BV complex only
action_owner: repository-owned reverse-scaffold candidate family built from the observed projector and frozen downstream demands; not source-selected or attributed to Weinstein
target: nonlinear action, conserved quotient dynamics, minimal classical master equation and degree-zero quotient observables MAP-TYPE=construction
```

## The candidate action is now genuinely interacting

Retain the complete packet of the predecessor. On the cooriented ultrastatic
slab

```text
M = [0,1]_t x T3,       V = K960 direct_sum W960,
P:V -> W,               psi=P Phi,
```

let `H` be the transported positive form on `W`. For
`m2>0` and `lambda>=0`, write

```text
S_(m2,lambda)[Phi] = integral_M [
  1/2 H(dt psi,dt psi)
  - 1/2 sum_j H(dj psi,dj psi)
  - m2/2 H(psi,psi)
  - lambda/4 H(psi,psi)^2
].                                                     (1)
```

When `lambda>0`, (1) is nonlinear and interacting: its Euler equation contains
the cubic term

```text
box psi + m2 psi + lambda H(psi,psi) psi = 0.          (2)
```

The nonlinearity is not a relabelled quadratic coefficient. On a one-mode
control, the restoring map obeys
`F(q1+q2) != F(q1)+F(q2)` for nonzero `lambda`.

The gauge image remains the closed direct summand `H1(K)`. Every term in (1)
depends only on `P Phi`, so arbitrary shifts `Phi -> Phi+iota(kappa)` leave the
action unchanged. On smooth solutions the nonlinear quotient energy

```text
E_t = integral_T3 [
  1/2 |dt psi|_H^2 + 1/2 |grad psi|_H^2
  + m2/2 |psi|_H^2 + lambda/4 |psi|_H^4
]                                                       (3)
```

is positive for `m2>0`, `lambda>=0` and conserved. The exact probe verifies
the modal identity without a numerical integrator.

## Minimal abelian BV completion

Let `c` be an odd ghost in `H1(K)` and `iota:K->V` the direct-summand
inclusion. The candidate gauge differential is

```text
s Phi = iota(c),       s c = 0,       s(P Phi)=0.       (4)
```

It is irreducible and abelian, so `s^2=0`. With the canonical algebraic
field-antifield pairing, the minimal BV action is

```text
S_BV = S_(m2,lambda)[Phi] + <Phi*,iota(c)>.            (5)
```

The classical master equation follows exactly. The antifield-number-zero term
is the gauge variation of (1), which vanishes because `P iota(c)=0`; the
ghost-square term vanishes because the gauge algebra is abelian. At degree
zero, the BRST cohomology is the algebra of functions of `psi=P Phi`: the
`K` coordinate and its ghost form a contractible gauge pair.

This is a formal minimal classical BV completion for this repository-owned
candidate family. It is not a gauge fixing, quantum measure, renormalized QFT,
source-native GU gauge algebra, BV-BFV boundary theory or analytic global BV
phase space.

## BV closure and interaction do not select the coefficients

The new structures close a previously explicit gap but have no decision power
inside this direct-summand class. Every pair

```text
(m2,lambda) in (0,infinity) x [0,infinity)
```

has the same closed gauge complex, the same nilpotent BRST differential, the
same formal master equation and the same degree-zero quotient-observable
algebra. For `lambda>0`, all members are interacting. They are nevertheless
inequivalent: changing `m2` changes the linearized zero-mode frequency, and
changing `lambda` changes the cubic response and nonlinear energy.

The prior mass-one and mass-four candidates are therefore not selected by
adding the minimal BV relation. Adding one arbitrary quartic coupling enlarges
the nonselected family rather than fixing it. The exact certificate passes
`21/21`; its hostile selftest catches `15/15` mutations.

The predecessor's quadratic densities, trace/effects, two-copy marginals,
local instruments, phase and dephasing still descend representative-
independently because they remain functions of `P Phi`. This says nothing
about whether the interacting dynamics selects those imported instruments.

## Next condition

The observed selector gate has narrowed again. Minimal abelian BV closure and
a positive quartic interaction are insufficient. Selection now requires an
independently owned relation that couples `m2` or `lambda` to another native
coefficient or observable, a nonabelian/open gauge algebra whose master
equation imposes a coefficient identity, a source-owned action term, or a
frozen structural discriminator with declared decision power over the full
`(m2,lambda)` family. Delayed-choice entanglement swapping remains reserved
and unscored until forward observable export exists.
