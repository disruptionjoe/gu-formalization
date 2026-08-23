---
title: "The requirements spec is current to the moment before the build wave: SA-G11..SA-G13 restore the 2026-07-14/15 supply items"
status: active_research
doc_type: requirement_surface_currency_audit
created: "2026-08-23"
directed_by: "Joe direct chat, 2026-08-23 (continue; awareness-note canon path)"
registry: lab/process/source-action-spec-build-wave-currency.json
probe: tests/channel-swings/source_action_spec_build_wave_currency_probe.py
grade: "EXACT REPOSITORY-SURFACE CURRENCY AUDIT WITH THREE ROW ADDITIONS; NO NEW PHYSICS, NO NEW FREEDOM, NO VERDICT, CANON, CLAIM-STATUS OR PREDICTION MOVEMENT"
target_claim: "internal target SOURCE-ACTION-SPEC-CURRENCY; verdict the spec's append-only maintenance lapsed at the 2026-07-14/15 build wave, leaving three named supply items uncarried"
canon_verdict_change: none
---

# The requirements spec is current to the moment before the build wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY`

Scope: this audit adjudicates the currency of a repository map against a
documented wave of build artifacts. It binds no comparator, is evidence about
Weinstein's mechanism in neither direction, and moves no verdict. Every item
added was already computed, classified and machine-checked in the cited
artifacts.

```gu-typed-objects
result: three supply items restored to the consolidated requirements spec, with the maintenance lapse that hid them identified from the spec's own edit history
carrier: repository requirement-surface and its git history LAYER=toy CHIRALITY=N/A
pairing: the 2026-07-14/15 build-wave artifacts paired against the 2026-07-13 spec table ON=repository-surfaces
real_structure: N/A; this artifact interprets no mathematical carrier
grading: process-integrity result only; every cited computation keeps its own recorded grade and conditions
action_owner: repository-construction -- no action term, coefficient or physics object is introduced or changed
target: internal requirement-surface currency defect MAP-TYPE=evaluation
```

## Result first

The earlier audit today closed one coverage gap (`SA-G10`, `alpha_W`) whose
mechanical cause was an incomplete source set. That raised the obvious
follow-up: was it the only one? It was not, and the second cause is
different and more systematic.

The spec was maintained by **append-only status notes as each build attempt
landed** — W125 on 2026-07-13, W131 on 2026-07-14, both recorded in its git
history. That discipline then stopped. The source-action build wave continued
through **W203 → W154 → W229 → W230 → W236 on 2026-07-14/15**, and the spec
received no further content change until today. It is therefore current to
the moment *before* the wave it exists to serve.

Three named supply items from that wave were uncarried, now added:

| row | item | class | why it belongs |
| --- | --- | --- | --- |
| `SA-G11` | `kappa`, the ultralocal mass-kernel normalization | FIT (normalization; branch-conditional; **sign forced**) | W203 pins every other coefficient by Krein-equivariance/Schur uniqueness and leaves exactly this one |
| `SA-G12` | `Z_U`, the induced-YM gradient stiffness (`ell^2 = Z_U kappa`) | FIT (normalization; branch-conditional) | W229 forces the fiber pairing and the operator and leaves exactly this one magnitude |
| `SA-G13` | the source-current identification `theta = J[Psi]` | DECLARATION (**reduced to one axiom; sign forced**) | W230 proves symmetry cannot force it — a full 14-dimensional space of equivariant divergence-free currents survives — so it is a required independent assumption |

Tallies move 28 → 31 rows, DECLARATION 9 → 10, FIT 11 → 13; the companion
consistency test's table and assertions were updated in the same change and
pass.

## Why this does not loosen the object

Recording free data can read as weakening a program. Here it does the
opposite, and the honest statement is W229's own: the complete branch-3
action carries **exactly two normalization scales and zero data-fitted
coefficients**, with every relative and tensor coefficient forced. A table
that omitted `kappa` and `Z_U` was not describing a tighter object; it was
describing an object whose tightness had not been written down. Likewise
`SA-G13` records a **narrowing**: W230 took an assumption that could have
been an open family and reduced it to one axiom with its sign forced.

## Typing: branch-conditional, not unconditional

All three items are typed **branch-3 / W154-conditional**. They are what that
route's reconstruction of H41 still needs, not unconditional requirements of
H41 itself. This matters downstream: W236's `theta = 0` in the `Psi = 0`
gravitational vacuum — the result that dissolves the theta-sector
over-determination annotated earlier today — inherits `SA-G13`'s
conditionality exactly. Withdrawing the posit reopens both.

The spec's own framing is preserved: **H41 remains unbuilt**. Every artifact
in the wave says so in its own grade line (`W229`: "H41 unbuilt (narrowed)"),
and this audit asserts nothing stronger. The wave narrowed the object; it did
not build it.

## Route selection and hostile review

The census ran a maintenance-history lens (the lapse is read from the spec's
git history, not inferred from content), a scope lens (are branch-3 items in
this spec's business — yes, the wave narrows H41 and the spec's job is what
H41 must supply, but the conditionality must be explicit), a
freedom-accounting lens (does adding FIT rows misrepresent tightness — no,
provided W229's zero-data-fitted accounting is stated, which it now is), a
provenance lens (every cited test path verified to exist; one incorrect path
was caught and corrected before shipping), and a hostile reviewer. The
strongest attack — "this is the same finding as this morning's, re-sold" —
fails on cause: the first gap came from an incomplete `depends_on` set, this
one from a lapsed maintenance discipline at a specific dated boundary; the
first was found by direction, this one by asking whether the first had a
systematic sibling. Second attack — "H41 is actually built and the spec's
framing is stale too" — was checked and **refuted**: W154, W229 and W230 all
carry "H41 unbuilt" in their own grade lines, so the spec's framing is
correct and only its table was behind.

No scientific ledger verdict, canon, source ownership, prediction credit, or
public posture changes.
