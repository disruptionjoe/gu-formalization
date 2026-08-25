---
title: "The D4 contraction rank is J-independent: the proposed non-metricity retyping does not bind this certificate"
status: active_research
doc_type: exact_scope_correction_of_a_proposed_correction
created: "2026-08-23"
directed_by: "Joe direct chat, 2026-08-23"
registry: lab/process/d4-contraction-rank-j-independence.json
probe: tests/channel-swings/d4_contraction_rank_j_independence_probe.py
grade: "EXACT RATIONAL COMPUTATION PLUS A ONE-LINE STRUCTURAL PROOF; SCOPE CORRECTION ONLY; NO VERDICT, CANON OR LEDGER MOVEMENT"
target_claim: NONE-NOT-A-KILL
target_claim_note: "corrects the scope of a proposed internal retyping; kills no source claim and no research route"
canon_verdict_change: none
---

# The D4 contraction rank is J-independent

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact borders
> conventional comparators. Any result about a standard Higgs/VEV, ordinary
> family index or net chirality, SO(10) `126` Majorana mechanism, anomaly
> selector or VEV-only breaking binds only that named model. Read
> `lab/methods/source-native-comparator-routing.md` before reusing this.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: the rank-10 / kernel-95 D4 contraction certificate is independent of the section jet J, so it holds identically at the Riemannian reduction; the proposed non-metricity retyping does not bind it
carrier: D = [I_4 ; J] as a 14x4 real matrix and the induced map on Sym^2 LAYER=toy CHIRALITY=N/A
pairing: symmetric-square contraction T maps to transpose(D) T D ON=Sym2-of-the-14-dimensional-model
real_structure: real
grading: degree-two symmetric tensors
action_owner: repository-construction -- no source action, coefficient or field content is introduced
target: the scope of a proposed retyping MAP-TYPE=evaluation
```

## Result first

The 2026-08-23 observed-side construction wave produced a retyping that
survived both of its adversarial passes: `MD-1`'s `J = ∂_mu g_ab` is a
**coordinate** object, removable pointwise in normal coordinates, whose
invariant content is the non-metricity `Q_(mu ab) = ∇^A_mu g_ab`, a tensor
vanishing identically iff the connection `A` is metric-compatible. **That part
is correct and worth recording.**

The wave then drew a consequence: *every* rank/kernel certificate computed
"with a nonzero rational `J`" — naming the rank-10 / kernel-95 result in the
2026-08-23 D4 typing — should be re-typed as computed at nonzero
non-metricity, i.e. strictly off the Riemannian reduction `theta = 0`.

**For that certificate the consequence is false.** The rank is `10` and the
kernel `95` at `J = 0` exactly as at generic nonzero `J`, so the certificate is
not conditional on non-metricity and re-typing it that way would assert a
dependence that does not exist — and would wrongly imply the D4 contraction
result fails or changes at the Riemannian reduction.

## The computation

Exact rational arithmetic, no floats. The map is
`C_s : Sym^2(T^*Y) -> Sym^2(T^*X)`, `T |-> D^T T D`, with `D = [I_4 ; J]` a
`14 x 4` matrix built from the section jet.

| `J` | rank | kernel |
| --- | ---: | ---: |
| `J = 0` (Riemannian reduction, `theta = 0`) | 10 | 95 |
| generic rational `J` | 10 | 95 |
| structured `J_(ij) = i - j` | 10 | 95 |

and `rank(D) = 4` on `J = 0` together with 200 random rational `J`, with no
other value observed.

## Why it is J-independent, in one line

`D` carries an identity block, so `rank(D) = 4` for **every** `J`. And whenever
`rank(D) = 4` the induced map on symmetric squares is surjective onto
`Sym^2(R^4)^*`: given any `S`, the block-diagonal `T = [[S,0],[0,0]]` satisfies
`D^T T D = S`. Hence `rank C_s = dim Sym^2(R^4)^* = 10` and
`ker C_s = 105 - 10 = 95`, unconditionally in `J`.

The identity block is not incidental — it is what makes the observation map a
**contraction rather than a projection** (`MD-1`, `WG-B06`). So the very
feature that makes `s^*` surjective onto `T^*X` is what makes this certificate
`J`-independent.

## What this changes, and what it does not

**Strengthens, does not weaken.** The D4 typing is now known to hold at the
Riemannian reduction as well as off it. It was never conditional on
non-metricity; nobody had checked, and the proposed retyping would have made
it look conditional.

**The general non-metricity point stands.** `J` is a coordinate object; its
invariant content is `Q`; and `MD-1` should name the connection it
differentiates against. All three are correct, useful, and unaffected by this
correction.

**The invalid step is the quantifier.** "`J` is coordinate-dependent"
licenses re-typing certificates that *depend on* `J`. It does not license
re-typing certificates that are *invariant under* `J`, and the two were not
separated. Any certificate proposed for this retyping must first be tested for
`J`-dependence; this one fails that test and must not be re-typed.

**Claim-indexed, as the doctrine requires.** The retyping recommendation is
correct on the objects it was derived from and wrong on this one. That is a
statement about scope, not about the quality of the underlying observation,
and it is exactly the distinction the claim-indexed verdict doctrine exists to
preserve.

## Ceiling

Scope correction only. No verdict, canon, source ownership, prediction credit
or public posture changes; no ledger row moves; nothing is discharged. The D4
component of the LT-GR8 packet remains `PARTIAL` for the reasons already
recorded — the density conversion and the section-chain variation — neither of
which this touches.
