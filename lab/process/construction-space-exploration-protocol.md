---
title: "Construction-Space Exploration Protocol"
status: active
doc_type: research_protocol
scope: repo-local
created: 2026-07-19
authorized_by: "Joe direct chat, 2026-07-19 (option A)"
method_source: ai-epistemology/field-guide/branch-5-evolvability
defense_register: lab/process/recovery-no-go-defense-register.json
portfolio_item: CONSTRUCTION-SPACE-EXPLORATION
---

# Construction-Space Exploration Protocol

The defense protocol prevents a branch-local no-go from being mistaken for an
exhaustive no-go, and its stop rule prevents unlimited rescue-swinging of one
frozen construction. What it does not do is generate new constructions: its
reopen conditions are passive ("wake when a fork appears") and nothing owned
producing that fork. This protocol makes the search itself first-class Lane 1
work. It changes the search strategy only — the truth standard (target-free,
native-versus-imported typing, adversarial twins, Joe-gated verdicts) is
unchanged.

The failure mode this protocol exists to prevent is local-minimum capture:
picking one construction, exhausting it, and stopping — or worse, circling
it — when the real question is "what is the most efficient way to explore the
space of constructions that could fit?"

## Stage 1 — Map the space (first deliverable)

Build `lab/process/construction-space-map.json`: the predeclared construction
space enumerated as cells along the existing six-axis template (Layer 0
semantic alignment plus L1 substrate, L2 observer, L3 pairing, L4 causal
order, L5 emergence, L6 coordination loop, L7 positivity/state-space metric).
Seed it from what already exists: the defense register's
construction_space_status entries, the escape-hatch map, and canon. Every
cell carries a state: `TESTED_NO_GO` (with register pointer), `GATED`
(named dependency), `UNTESTED`, or `UNDERDEFINED` (per the register's
underdefinition rule, a blank axis supplies neither rescue nor evidence).

The map is the search's coverage ledger and the lane summary's denominator:
`scope_position` reports "N of M cells dispositioned." A cell, once
dispositioned, is never silently revisited — reopening a cell requires the
same history-audit discipline the defense protocol already imposes.

## Stage 2 — Sector-fit searches (candidate generators)

Instead of freeze-one-construction-then-test-every-sector, run per-sector
searches as parallel tracks, each asking one question:

- SM track: can any construction in an untested cell natively produce the
  Standard Model selector (finite algebra, global gauge quotient, absolute
  hypercharge, chirality, physical Higgs, spectrum, decoupling)?
- QM track: can any cell supply source-owned quotient, state, observable,
  probability, locality, and dynamics certificates?
- GR track: can any cell supply a source-owned vacuum cancellation for the
  Q^TF(B) obstruction (a source nonzero in vacuum, or a different residual
  structure)?
- Cosmology track: can any cell derive a physical scalar projector,
  observable map, and closed SVT truncation?

Sector-fit keeps the full truth standard: target-free construction, explicit
axis deltas from tested cells, and a first falsification test per candidate
(the defense protocol's Swing-2 escape-admission rule, applied at birth). A
sector fit is a candidate, never a recovery claim.

## Stage 3 — Weave

Intersect sector survivors on the map. A construction whose axis signature
fits two or more sectors becomes a frozen construction candidate and enters
the existing recovery-certification ladder and defense protocol as a new
registered target — this is what satisfies the defense register's reopen
conditions. Weaving must not degrade into sector-specific repair: if the
"one" construction needs per-sector adjustable identifications to fit, that
is the kill condition of RECOVERY-CERTIFICATION, reported honestly.

## Search-strategy council (at every stage boundary)

At each stage boundary — map built, each sector track's round complete,
before each weave — run a search-strategy council as an inline persona pass
in one worker (members reason independently, then rank, then a chairman
synthesizes; never one agent per persona). Standing bench, adjustable per
round: differential geometer, category theorist, statistician
(experimental-design/information-gain), computer scientist (search
algorithms), machine-learning researcher, condensed-matter physicist,
numerical engineer, logician, optimization theorist, historian of physics.

The council's question is never "is GU true" and it issues no verdicts. Its
question is: what is the most efficient next probe of this space — where is
the information gain, what cheap discriminating test kills the most cells
fastest, and is the parameterization of the space itself wrong? Output: a
ranked search plan with expected information gain per probe, recorded in the
map file, consumed by the next hourly run. Council output guides search; it
is not evidence for or against GU and cannot move claim status.

## Anti-local-minimum guards (structural)

- Breadth-first: no cell receives a second deep probe while an untested,
  reachable cell in the same track has a cheaper first probe, unless the
  council explicitly ranks depth higher with stated information-gain
  reasoning.
- The defense protocol's three-swing cap stands: a candidate that fails gets
  its bounded defense and returns control to the map.
- No silent revisits: the map is append-honest; dispositions carry evidence
  pointers, and reopening requires a history audit.
- Coverage is visible: `scope_position` in LANE-STATE reports map coverage,
  so circling is visible from the helicopter view instead of being buried in
  hourly narration.

## Boundaries

- This protocol changes search strategy, not the truth standard. Verdict
  changes, claim-status moves, public posture, and exhaustion calls remain
  governed exactly as before (daily steward + Joe gates).
- The defense register's wake conditions are unchanged; this program is
  their active generator, not their replacement.
- Sector-fit candidates are internal work objects, not publishable claims;
  Lane 3 handles hardening only after a candidate survives its own frozen
  benchmark.
