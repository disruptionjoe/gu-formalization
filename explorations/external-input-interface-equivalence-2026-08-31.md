---
artifact_type: exploration
status: active_research
doc_type: exact_interface_schema_and_countercontrols
created: 2026-08-31
title: "External-input interface: exact conditional equivalence and hostile controls"
target_claim: NONE-NOT-A-KILL
target_claim_note: "INTERNAL -- a classifier into typed obstruction-tiebreaker and free-setting codes induces the advertised equivalence iff it is bijective; current GU evidence supplies neither an exhaustive external-input carrier nor such a classifier. The universal two-type equivalence remains unestablished."
canon_verdict_change: none
probe: tests/channel-swings/external_input_interface_equivalence_probe.py
lean: Lean/GUFormalization/ExternalInputInterface.lean
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: conditional exact-interface theorem plus finite hostile controls
carrier: E = admitted physical external-input carrier; T = obstruction identifiers x Bool; S = dependent sum of typed free-modulus values; proposed code carrier = T disjoint-union S LAYER=UNTYPED CHIRALITY=N/A
pairing: NONE
real_structure: UNTYPED; no GU real form or physical Hilbert/Krein completion is constructed
grading: tagged coproduct TIEBREAKER versus SETTING; this tag is not a chirality, ghost or physical-sector grading
action_owner: UNTYPED; no source action, variational owner, external source or physical admission rule is constructed
target: exactness of a supplied external-input classifier MAP-TYPE=isomorphism with a separately stated automorphism-compatibility obligation
```

# Result first

**EXHAUSTIVE TWO-TYPE EQUIVALENCE IS NOT ESTABLISHED.** What is established is
the exact conditional theorem the proposed interface must satisfy.

Let `E` be the already-admitted external-input type, let
`T = Obstruction × Bool` be typed binary obstruction/indifference choices, and
let `S = Σ modulus, Value modulus` be typed free-moduli points. For a supplied
classifier

```text
encode : E -> T disjoint-union S,
```

there exists a decoder satisfying both triangle identities iff `encode` is
bijective. Equivalently, the proposed interface is exact iff:

1. every physical external input is recovered after classification
   (`decode (encode e) = e`: no missing port); and
2. every tagged code is recovered after realization
   (`encode (decode c) = c`: no overlap, alias or double count).

This is proved in Lean by `exists_exact_decoder_iff_bijective`. The consequences
`no_missing_port`, `no_overlap`, and `unique_code` make the two burdens explicit.
The theorem is intentionally not a proof by labeling: until `E` and `encode`
are constructed from an admitted GU source/observation/action surface, neither
bijection obligation can be applied to GU.

## Why the live evidence does not discharge the premises

The Wave-1 audit found no admitted third type in its scoped live candidate set,
but explicitly did not produce an exhaustive census or equivalence. The current
evidence reinforces that ceiling:

- W201 types the conditional count route as factored, CRT-disjoint selector and
  magnitude data sharing an operator; it does not construct the source action,
  the count value, or a complete external-input carrier. Because it borders the
  ordinary-index comparator, it cannot adjudicate Weinstein's source-native
  `2+1` mechanism without the required bridge.
- `conditional-forcing-minimal-input-2026-07-20.md` retains a semantic fork:
  trit-only versus a fresh `Z/6` phase reference. That unresolved ownership
  question prevents using it as a settled primitive port census.
- W183 makes total-system unitarity conditional on an external reservoir Krein
  type; W184 shows that a global involution is only a grading until dynamical
  commutation is proved. Together they motivate, but do not supply, a physical
  external port and show why automorphism/dynamics structure cannot be erased.
- W215's initial condition and W226's fitted amplitude/epoch surfaces are
  setting-shaped only at their stated conditional scopes. They do not prove
  that every external input is a free-moduli point.

Therefore the strongest licensed statement is the conditional iff, not
`ExternalInputs ≃ T ⊕ S` for GU.

## Automorphism ceiling

A bare set bijection preserves cardinality, not the physical groupoid data
requested by the Wave-1 audit. The Lean module separately defines a carrier
with a distinguished automorphism and requires the interface equivalence to
intertwine it. `nontrivial_automorphism_control` proves that a Boolean carrier
with the nontrivial flip cannot be identified, compatibly, with an equally
sized carrier whose automorphism is trivial. Thus an object-level GU theorem
must additionally preserve automorphisms, stabilizers, connected components,
ownership and physical equivalence; none follows from the set theorem.

## Hostile controls

The Lean file and exact finite probe reject all required adversarial cases:

| hostile mutation | exact failure |
|---|---|
| planted history-dependent third type | cardinality/left-triangle failure |
| one port realized by both tags | right-triangle failure; overlap/double count |
| equal-cardinality classifier omitting a port | left-triangle failure |
| nontrivial source flip versus trivial code automorphism | symmetry-intertwining failure despite equal cardinality |
| choose the first solver result | reversing enumeration changes the output, exposing hidden order as an undeclared input |

These controls prove that the test machinery can fail. They do not show that
the finite ports are GU's ports.

## Source and claim ceiling

This artifact is repository-derived pure mathematics plus an exact toy control.
It is not source-confirmed GU physics. It constructs no source-native carrier,
observation map, action term, analytic domain, quotient, external reservoir,
prediction or physical admission decision. It does not settle whether `j_B`, a
source coefficient, a phase reference or any future object is physically
external. It does not transfer a conventional family-index result to the
source-native `2+1` mechanism.

No source claim, canon verdict, action owner, prediction or physical input census moves.

## Reproduction

The claim was formed after checking the Wave-1 audit and the named W201,
conditional-forcing, W183, W184, W215 and W226 evidence. Reproduce the exact
theorem and hostile controls with:

```bash
lake env lean Lean/GUFormalization/ExternalInputInterface.lean
python3 tests/channel-swings/external_input_interface_equivalence_probe.py --selftest
```
