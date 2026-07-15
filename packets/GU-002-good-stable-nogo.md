---
artifact_type: frozen_packet_companion
packet_id: GU-002
schema: possibility-to-capability frozen-packet-v0.2
status: SOURCE_FROZEN (exploration-grade interface)
created: 2026-07-15
---

# GU-002 -- GU-independent structural good-stable no-go (human-readable companion)

This is the plain-language companion to the machine packet
`packets/GU-002-good-stable-nogo-v0.2.json`. The JSON is the authoritative,
schema-valid, validator-passing object; this file only narrates it. Nothing here
moves any GU verdict, claim status, canon, `bar(b)`, `H59`, or the generation
count.

## What GU-002 packages

A GU-owned frozen packet of the **GU-independent structural good-stable no-go**:

> In `Sp(32,32;H)`, a chirality-safe good-stable requires a compact-image
> (positive-majorant, Proposition 1) isotropy, whose reducing direction is
> intrinsically `Z2`-ODD; the grading `Z` is a non-compact non-elliptic boost
> that no Cartan involution commutes with. No neutral, adjoint, or
> charged-EXTREMAL order parameter (= everything GU natively builds) delivers a
> chirality-safe good-stable interior. Surviving escapes: exotic NON-extremal
> charged vectors (GU-non-native) and denying Proposition 1 (a boundary/firewall
> positivity).

## Pinned source revision

- Repository: `gu-formalization`
- Immutable revision: `65c31a1663e8548327de3ac8453845a03d9580da`
- This revision contains all five explorations (W234, W237, W240, W241, W243,
  dated 2026-07-15) and their five machine tests. The manifest pins the exact
  raw bytes (`byte_length` + `content_sha256`) of all ten blobs.

## The three digests (profile `ptc-frozen-bundle-v1`)

- `manifest_digest = 9d2e2d7949d9ca5bf7315e6ce07024afaaabd4791e51cff56ee09cbc59ab502d`
- `packet_digest   = 8a5df3f26ee165953f4b7069789646dfff9a8cca9cd8c385195a6392f9b9d398`
- `bundle_digest   = 03df01f37287f4f0fa234fa65aed005ffaf191e3eda6342a7940e2662e59e261`

The `integrity.digest` alias equals the `bundle_digest`.

## The five proof legs (a DEPENDENT chain, not independent evidence)

The packet models the no-go honestly as **one dependent proof chain of five
legs**, not five independent evidential units.
`raw_method_count_is_independence_count = false`; `independence_type` and
`convergence` are both `not_applicable`.

| Leg  | Content |
|------|---------|
| W234 | Operator identity `tau1(null) = sigma3(definite) = P`: the only compactification-capable native condensate lands in the `~P` Cartan-involution direction (stabilizer `Sp(32)xSp(32)`, 4096 broken) and is `Z2`-ODD (channel-D chirality-killer). |
| W237 | Structural theorem `COMPACTIFY <=> Z2-ODD` for null-pair bilinears; the chirality-safe channel-S `(16bar)^4` is `Z2`-EVEN but does NOT compactify. Located flaw on the chirality-preserving branch. |
| W240 | Three rank-independent no-go classes: (A) `Z`-neutral, (B) adjoint, (C) no Cartan involution commutes with the non-elliptic boost `Z`. Sole surviving escape: `Z2`-even but `Z`-charged non-adjoint VEVs, GU-native-empty. |
| W241 | Isotropy-algebra lift via Proposition 1; the coincidence-admitting smaller-group front door is closed; A+B exhaustive modulo denying Proposition 1. |
| W243 | Extremal-weight nilradical closure of the charged corridor: an extremal `Z`-charged vector has a non-compact parabolic stabilizer; channel S is extremal (charge `-4`). Upgrades the no-go to UNCONDITIONAL for the extremal/native class. |

The joint argument artifact is W243 (it states the combined
UNCONDITIONAL-vs-SCOPED export).

### Shared load-bearing premises (why agreement is not independence)

All four premises are load-bearing for more than one leg, so they are the exact
`shared_load_bearing_premise_ids`:

- `P-PROP1-COMPACT-IMAGE` -- Proposition 1 (good-stable = relatively compact
  image). Legs W240, W241, W243.
- `P-RECORD-BIT` -- the W235 record-conserved branch (Joe-gated, not decided).
  All five legs.
- `P-CHANNEL-S-EMPTY` -- channel-S emptiness (`16bar (x) 16bar` has zero
  `SO(10)` singlets). Legs W237, W240, W243.
- `P-CL95-REPCANON` -- the standing `Cl(9,5)=M(64,H)` rep-canonicity caveat and
  the finite-model STRUCTURAL lift. All five legs.

Direct leg-to-leg dependencies are recorded as `method_dependency_edges`
(W237<-W234, W240<-W234, W240<-W237, W241<-W237, W243<-W240, W243<-W241).

## Scoped vs unconditional (stated exactly)

- **UNCONDITIONAL** and GU-independent for the neutral, adjoint, and
  charged-EXTREMAL classes -- everything GU natively builds.
- **SCOPED** (honestly OPEN) only against exotic NON-extremal charged vectors
  (interior `Z`-eigenvectors or non-eigenvector `SO(2,1)`-type timelike vectors,
  GU-non-native) and against denying Proposition 1 (a boundary/firewall
  positivity).

## Honest residuals

- `bar(b)` and `H59` remain **OPEN** and Joe-gated; no debit added or cleared.
- The interacting source action, physical state space, and observable algebra
  are unbuilt (W219); unbuilt is not false.
- The STRUCTURAL lift from the faithful finite `so(n,n)`/`u(2,2)` models to the
  full `Sp(32,32;H)` arena is not a full quaternionic recomputation.
- The interior-charged (non-extremal `Z`-eigenvector) class and the
  non-eigenvector `SO(2,1)`-type class are not closed.
- The `Cl(9,5)=M(64,H)` rep-canonicity caveat stands.
- The W235 record bit is not decided.

## Verification status (honest)

Internal-tier: five machine regressions (W234 35/35, W237 44/44, W240 27/27,
W241 46/46, W243 26/26) all exit 0 with positive controls first. An independent
re-verification pass is **IN PROGRESS** (a sibling run). Issued at
exploration-grade interface per the GU-001 issuance plan. No Lean/Lake build was
run.

## Relationship to GU-001

`GU-001` is separately reserved for the grading-sign five-method result (the
`bar(b)` / C-operator object). GU-002 does not hijack or supersede it;
GU-001 is cross-referenced as related work only.

## No cross-repo identity

No TI/TaF or cross-repository identity is asserted. The boundary fields
(`interfaces`) are typed-interface requests only; the reservoir Krein sign / Y14
spectral-section record datum stays a gated time-as-finality object.
