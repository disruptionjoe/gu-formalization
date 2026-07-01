# GU Source Action

> **STATUS (2026-06-27): construction sandbox.** This repo was spun up to *construct* GU's missing RS/IG
> source action. It has not yet built one. The work done here (CONSTRUCT-01..07) turned out to be AUDIT of
> GU's generation sector, not construction, so those results have been **migrated back to
> `../gu-formalization`** (`canon/no-go-quaternionic-parity-generation-sector.md`,
> `tests/generation-sector/`, and the WHERE-GU-STANDS capstone). What remains here is the genuine,
> still-open construction frontier: a **canonical external membrane** (the source action S_IG) that pins
> the under-determined generation count a-priori, without import. Everything in this repo below is
> forward-looking construction scaffolding (the cryptoeconomic membrane lens, the persona vote, the loss
> channels), not audited results. See `DERIVATION-PROGRESS.md` for the full CONSTRUCT-01..07 record.

> **STATUS (2026-06-28): this sandbox is now the test bench for falsification criterion 1 of the
> Firewall-Boundary Hypothesis** (`../gu-formalization/canon/firewall-boundary-hypothesis.md`, the
> repository's primary research question). Building a CLOSED internal source action here is the live
> attempt to KILL that hypothesis: if a closed completion can be constructed without contradiction or
> import, the firewall reading weakens; if every serious attempt instead fails in the same
> boundary-shaped way, it strengthens. Build to disprove the firewall, not to confirm it.

## Front-Door Candidate Lens

The most actionable current design lens is:

> **The missing GU source action may be an adversarial security-budget functional over admissible geometric
> extensions.**

In this reading, a source extension becomes physically admissible only when it increases GU structure while
paying the cost required to make that extension final against every allowed mathematical fork: rival shiab
members, rival boundary spectral sections, RS/BRST inconsistency, theta/source-current drift, anomaly failure,
target import, or acausal decoupling.

Read [`CRYPTOECONOMIC-SOURCE-ACTION.md`](CRYPTOECONOMIC-SOURCE-ACTION.md) before proposing new selectors. It
turns the idea into a concrete minimax workflow and executable scaffold:

```text
Score(phi) = GrowthValue(phi)
             - ValidationCost(phi)
             - FinalizationCost(phi)
             - WorstCaseAdversarialLoss(phi)
```

This is not a result and not a replacement for `SPEC.md`. It is the current best way to make the search
global, adversarial, and testable instead of repeating local selector dead-ends.

For a divergent idea stress test, see
[`PERSONA-LENS-VOTE-2026-06-27.md`](PERSONA-LENS-VOTE-2026-06-27.md): 25 independent lenses rank their top
three workstreams and vote. The current consensus portfolio is GU-native minimax loss channels, a boundary
finality carrier, and an anti-import adversarial oracle.

> **Working name — pending confirmation before this becomes a public repo.**

**An open theoretical-construction program: build the one object that `gu-formalization` proved is missing.**

This repo is the CHILD of [`gu-formalization`](../gu-formalization). That repo is a finished,
adversarially-audited reconstruction of Geometric Unity; its capstone
(`gu-formalization/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md`) proved GU does not close on the
existing material and pinned the single missing object — the stabilized **RS/IG source action** — down to a
precise, buildable spec.

This repo has ONE job: try to construct that object. The target is `SPEC.md`.

## Honest framing (read this first)

This is **open invention, not audit.** It is **expected to mostly fail.** The parent repo earns trust by
keeping only what survives adversarial checking; this repo earns trust by being relentlessly honest about
what it has **not** achieved. A beautiful idea here is worth nothing until it is computed and survives attack.
"It fits beautifully" is a warning sign, not evidence — the parent repo was repeatedly burned by exactly that
(see `DEAD-ENDS.md`). **Never import the answer** (no `24/8`, no assumed-K3, no fitting to the target).

## Dependency

Requires `gu-formalization` checked out as a sibling directory (`../gu-formalization`), or set the env var
`GU_FORMALIZATION_PATH`. The verified machinery — the Cl(9,5)=M(64,H) representation, the gamma-trace
constraint, the obstruction C2, the BV bicomplex — is **imported** via `lib/gu_bridge.py`, never re-derived.
Smoke test: `python tests/test_bridge.py` (reproduces the anchors C2 = 155.36, ||[Pi_RS, M_D]|| = 58.72).

## Start here

`Agents Start Here.md` — the discipline, the spec, the dead-ends not to re-walk, and how to use the bridge.
`DERIVATION-PROGRESS.md` — the running ledger (same compute -> adversarially-verify -> land discipline as the
parent).
