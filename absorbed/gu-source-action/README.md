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

**Reconciliation (2026-07-11): `L_theta_source` is OVER-determined, not free.** The leg-intersection result
(`../../explorations/source-action-constraint-intersection-2026-07-11.md` and
`../../explorations/willmore-residual-computed-and-buildbench-reconciliation-2026-07-11.md`) shows the
θ/source-current carrier this repo flags as `missing_carrier_blocked` / `underdetermination_fail` is in fact
pinned by gravity ∩ dark energy: it must give `theta ~ M/rho^2` on Schwarzschild (Branch-3), carry amplitude
`f_0` (DESI), and induce a stress matching the now-computed leading Willmore residual
`Q^TF(B) ~ diag(-9/2,-3/2,-3/2,-3/2)·M^2/r^2` (see that note for the `M^2/r^2`-vs-canon-`M^2/r^4` tension and
the OQ2-A gate). Construction should aim `L_theta_source` at this intersection TARGET, not search freely —
without importing the answer (the target is independent physics, not `24/8`).

**Current hourly-progress target (2026-07-10).** Work the roadmap in `../../NEXT-STEPS.md` under
"2026-07-10 Hourly Progress Focus -- source-action buildbench first." Do not try to write the full source
action first. The candidate buildbench, anchor-scale A-door fork, minimal finite-fiber BV/Koszul-Tate
closure attempt, finite-fiber source-Noether/tau solve, and topological-wall tau-selector probe are now
complete; the next hourly work should supply concrete global boundary-condition/source-current data that
selects one wall/tangent map without collapsing back to a fixed projector.

**Update 2026-07-13: first global-boundary tau-data pass.** The current wall/tau family still does not
select a wall from GU-native data. Local scalar rankings pick different walls, and an externally supplied
current can pick one only because the current is supplied. The next object is actual source-current /
derivative data, not another wall-ranking rule. See
`GLOBAL-BOUNDARY-CONDITION-TAU-DATA-PACKET-2026-07-13.md`.

`Agents Start Here.md` — the discipline, the spec, the dead-ends not to re-walk, and how to use the bridge.
`DERIVATION-PROGRESS.md` — the running ledger (same compute -> adversarially-verify -> land discipline as the
parent).
`SECURITY-BUDGET-CARRIER-PACKET-2026-07-01.md` - first executable candidate packet; records that
available-loss-only scoring is missing-carrier blocked, not a source-action success.
`SOURCE-ACTION-BUILDBENCH-PACKET-2026-07-10.md` - first hourly-progress buildbench; records declaration
triples, current hard guards, computable loss channels, named missing carriers, and the A-door handoff.
`ANCHOR-SCALE-A-DOOR-PACKET-2026-07-10.md` - second hourly-progress packet; records that non-null
anchor-scale scalar-spinor shifts pass representation/H-linear/Krein necessary checks, while null-direction
tau and source-derived BV/Koszul-Tate closure remain open.
`MINIMAL-BV-KT-CLOSURE-PACKET-2026-07-10.md` - third hourly-progress packet; records that finite-fiber
BV/Koszul-Tate closure works after projecting the gauge map into `ker Gamma`, but the projection is not yet
derived from a source-level Noether/tau carrier.
`SOURCE-NOETHER-TAU-CARRIER-PACKET-2026-07-10.md` - fourth hourly-progress packet; records that the
finite-fiber tau multiplier derives the projection as a Schur complement, but Noether leaves arbitrary
tangent maps in `ker Gamma` unselected.
`KLEIN-BOTTLE-COSMOLOGY-TOPOLOGICAL-WALL-LENS-2026-07-10.md` - external exploration lens; records the
topology-forced wall/order-parameter pattern as an analogy for the derivative-tau tangent-selector blocker,
without treating it as GU evidence.
`TOPOLOGICAL-WALL-TAU-SELECTOR-PACKET-2026-07-10.md` - fifth hourly-progress packet; records that spacelike
wall involutions generate nonzero tangent selectors, but the admissible wall family remains underdetermined
without a concrete global boundary condition.
`GLOBAL-BOUNDARY-CONDITION-TAU-DATA-PACKET-2026-07-13.md` - sixth hourly-progress packet; records that
available local scalar rankings and externally supplied current weights do not constitute GU-native
source-current data, so wall selection remains externally keyed.
`THETA-SOURCE-CURRENT-CARRIER-PACKET-2026-07-05.md` - carrier-specific packet; records that the
theta/source-current route is blocked on the named missing `L_theta_source` carrier, with a
targeted regression check.
`WEAK-FIELD-SOURCE-CURRENT-CARRIER-PACKET-2026-07-05.md` - carrier-specific packet; records that the
weak-field/source-current route is blocked on the named missing `L_weak_field` carrier, with a
targeted regression check.
`ANOMALY-GREEN-SCHWARZ-CARRIER-PACKET-2026-07-05.md` - carrier-specific packet; records that the
anomaly/Green-Schwarz route is blocked on the named missing `L_anomaly` carrier, with a targeted
regression check.
`RS-BRST-CARRIER-PACKET-2026-07-05.md` - carrier-specific packet; records that the RS/BRST route is
blocked on the named missing `L_RS_BRST` carrier, with a targeted regression check.
`FAMILIES-PUSHFORWARD-CARRIER-PACKET-2026-07-05.md` - carrier-specific packet; records that the
families-pushforward route is blocked on the named missing `L_families_pushforward` carrier, with a
targeted regression check.
`BOUNDARY-SPECTRAL-SECTION-CARRIER-PACKET-2026-07-05.md` - carrier-specific packet; records that the
computed boundary spectral-section route reaches a forced-eta-zero obstruction, not a closed
source-action selector, with a targeted regression check.
`NON-EQUIVARIANT-COMPENSATOR-CARRIER-PACKET-2026-07-05.md` - source-extension packet; records that the
non-equivariant compensator lane is still missing-carrier blocked: simple structured adapter probes stay
zero, arbitrary movement lacks a source carrier, and BV closure remains required.
