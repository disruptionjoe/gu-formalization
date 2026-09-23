---
artifact_type: exploration
status: exploration
doc_type: representation_bridge_candidate
created: 2026-09-23
title: "Quotient descent is not gauge-slice representative selection"
target_claim: "INTERNAL — exact compatibility and incompatibility laws separating corrected-observation descent to a target quotient from a carrier-valued gauge-slice representative selector"
source_claims: [SC-ACT-01, SC-ACT-02, SC-ACT-06, SC-GEN-02, SC-GEN-03, SC-GEN-54, SC-CHI-01, SC-CHI-51]
canon_verdict_change: none
probe: tests/channel-swings/corrected_observation_quotient_slice_compatibility.py
hostile_probe: tests/channel-swings/corrected_observation_quotient_slice_compatibility_probe.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact borders
> conventional gauge quotient, BRST/BV and physical-state language. It binds
> only the supplied complexes and maps. It is not evidence for or against the
> source-native `2+1`, non-chiral observation or connection-curvature
> mechanisms without the missing typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: CORRECTED-OBSERVATION-QUOTIENT-SLICE-COMPATIBILITY
carrier: abstract observed field carrier B with Gamma:B->S, right inverse j:S->B and P=1-j Gamma; actual K77 carriers remain separately typed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: none added; the prior Green-self-adjoint condition remains independent ON=conditional observed carrier B
real_structure: rational real independence fixtures only; no K77 real or Krein physical structure is inferred
grading: quotient cycles modulo target gauge images versus unquotiented carrier representatives; no family or chirality grading is assigned
action_owner: repository-construction -- theorem only; the same-carrier K77 differential, Green form and analytic domain remain open
target: exact law distinguishing descent of corrected observation to a quotient from selection of one representative per gauge coset MAP-TYPE=quotient
```

# Quotient descent is not gauge-slice representative selection

## The semantic fork

Two earlier exact results use the same-looking corrected projector

```text
P = 1 - j Gamma,       Gamma j = 1,
```

but answer different questions.

The August action--observation theorem constructs a map between middle
cohomology **quotients**. In its finite fixture the corrected projector fixes
the observed gauge image:

```text
P d0 = d0.
```

A September physical-slice theorem asks whether `P` itself chooses a
carrier-valued representative that is constant on gauge cosets. That requires

```text
P d_action = 0.
```

The first law preserves a gauge shift so the target quotient can remove it.
The second law removes the gauge shift before the target carrier is returned.
They are not interchangeable.

## Exact quotient law

Let an action complex have gauge differential `d0_A:G_A->B_A`, let an
observed complex have `d0_B:G_B->B_B`, and let `O:B_A->B_B` be the corrected
observation. A map on quotient classes needs a gauge-parameter map `u` with

```text
O d0_A = d0_B u.
```

Then action-gauge-equivalent fields map to target-gauge-equivalent fields.
The carrier outputs need not be equal. In the same-complex special case it is
enough that `P(im d0)` lies in `im d0`; the August fixture uses the stronger
identity `P d0=d0`.

## Exact representative-slice law

A carrier-valued map is constant on action gauge cosets exactly when

```text
P d_action = 0.
```

Because `ker(P)=im(j)`, this is equivalent to

```text
im(d_action) subset im(j).
```

If the gauge image has the full trace size and `Gamma` restricts to an
isomorphism on it, the inclusion becomes the prior equality
`im(d_action)=im(j)`.

The sharp incompatibility is immediate. If the same differential satisfies

```text
P d0 = d0       and       P d0 = 0,
```

then `d0=0`. A nonzero gauge image cannot be both preserved for quotient
descent and killed for carrier-valued representative selection by the same
projector.

## Exact fixtures

Use `B=Q^3`, `Gamma=(0,0,1)`, `j=(0,0,1)^T`, so
`P=diag(1,1,0)`.

For quotient descent take `d0=(1,0,0)^T`. Then `P d0=d0` and a gauge shift
changes the carrier output by that same nonzero gauge shift. The two outputs
are equal only after quotienting by `im(d0)`.

For representative selection take `d_action=j`. Then `P d_action=0`; all
members of one gauge coset have exactly the same carrier-valued projected
representative.

The producer passes eleven exact controls. An independent replay passes ten
controls and rejects eleven hostile mutations.

## Owner audit and correction scope

The August theorem remains valid at its declared grade: it constructs a
conditional map of quotient classes. Its finite fixture does not construct a
gauge-fixed representative in the unquotiented target carrier.

The September theorem also remains valid: it gives the exact same-carrier
criterion for a representative selector and its independent Green condition.

No predecessor is retracted. The correction is semantic: future artifacts
must state which codomain they return.

```text
quotient-valued output: require O d0_A = d0_B u;
carrier-valued slice:   require P d_action = 0;
Green-compatible slice: additionally require P^dagger_H = P on one domain.
```

The current K77 bank still supplies no single typed packet containing all
carriers, differentials, the observation map, gauge-parameter map, Green form
and common analytic domain.

## Hostile review

**Strongest overclaim.** The incompatibility does not say quotient descent and
gauge fixing cannot coexist in a theory. They can coexist as distinct maps or
at distinct stages. It says one nonzero differential cannot be both fixed and
killed by the same projector.

**Strongest contrary construction.** A future K77 diagram may use an action
gauge differential upstairs, a different observed gauge differential
downstairs, and a nontrivial `u`; the quotient law can then hold even when the
corrected observation is not a carrier-valued slice.

**Weakest typing seam.** The exact rational fixtures prove logical
independence, not that either differential is the K77 differential. Equal
dimensions or names do not supply the missing intertwiner.

**Weakest analytic seam.** Neither law selects a closed range, Fredholm
domain, boundary condition or positive physical state space. The prior Green
adjoint condition remains separately necessary when an orthogonal/Krein slice
is claimed.

## Effect and next condition

The physical-seam burden is now more precise. First name the output type. For
a quotient-valued observation, construct one same-carrier diagram and test
`O d0_A=d0_B u`. Only if an actual carrier-valued representative is intended
must the stronger `P d_action=0` and Green/domain laws also hold.

No source polarity, physics-ledger verdict, canon, paper status, family or
chirality interpretation, public posture or GU verdict changes.
