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
searches as parallel tracks. Each track asks the existence question — "is
there any construction in an untested cell that survives this sector's sharp
constraints?" — and grades what it finds on the fit ladder below. Admission
into the search is at Rung 0; Rung 2 is how survivors are graded, not the
entry gate (amended 2026-07-19, Joe direct chat: the previous
natively-produce admission bar tested one candidate at derivation strength
instead of carving the space at existence strength).

### The graded fit ladder

- **Rung 0 — Consistency (admission bar):** the cell is not falsified by the
  sector's sharp constraint list. Cheap, kills cells fast. Consistency means
  passing quantitative constraints, never resemblance: subgroup containment,
  matching names, or field location do not count (standing shortcut ban).
- **Rung 1 — Hosting (typed imports):** the cell accommodates the sector's
  structures with imported choices, where every import is typed with the
  standing vocabulary (native, imported, fitted, forced, assumed) and
  **counted**. The import count N is part of the cell's grade and is
  reported, never hidden.
- **Rung 2 — Native selection (North Star bar):** the sector's structure is
  forced by the construction with no sector-specific repair. This remains
  the charter-level claim; it grades survivors and is never diluted by
  Rung 0/1 results.

### Sharp constraint lists (what Rung 0 must mean)

Each track owns a frozen, predeclared constraint list; a cell passes Rung 0
only against the list, not against vibes:

- SM track: anomaly cancellation, chirality production, three generations,
  absolute hypercharge normalization, physical Higgs sector, complete
  surviving spectrum, extra-mode decoupling.
- QM track: quotient, state space, observables, probability rule, locality,
  and dynamics certificates realizable without contradiction.
- GR track: a vacuum sector whose residual structure can cancel or evade the
  Q^TF(B) obstruction (source nonzero in vacuum, or different residual
  bookkeeping) while preserving the linear cheap-read clears.
- Cosmology track: a physical scalar channel admitting a projector,
  observable map, and closed SVT truncation with dischargeable residues.

Constraint lists may be extended by evidence (a new sharp constraint), never
weakened silently; weakening one is a Joe-gated contract change.

### The expressiveness guard

Consistency-only testing has a known failure mode: an expressive-enough
framework hosts anything, and then fitting a sector is zero evidence. The
guard is threefold: (a) sharp constraint lists above, so Rung 0 is a real
filter with a real kill rate — if a track's Rung 0 kills nothing across many
cells, that track's constraints are too weak and the council must sharpen
them before the track continues; (b) import counting at Rung 1, so
expressiveness is priced rather than hidden; (c) Rung 2 preserved as the
only rung that supports the unification claim. "GU is expressive" must never
be silently substituted for "GU is true."

Sector-fit candidates still require explicit axis deltas from tested cells
and a first falsification test at birth (the defense protocol's Swing-2
escape-admission rule). A sector fit at any rung is a candidate, never a
recovery claim.

## Stage 3 — Weave (intersection is the real falsification target)

Intersect sector survivors on the map, rung-aware: a cell's joint grade
across sectors is the minimum rung it holds in each, with its total import
count. The program's honest falsification target lives here, not in any
single-candidate kill: **if the predeclared space reaches full disposition
and the joint Rung-0 intersection across all four sectors is empty, that is
a real falsification-shaped result** for the predeclared class — handed to
the daily steward and Joe under the standing exhaustion governance. A
non-empty intersection is the constructive result: it characterizes what a
GU construction must be, and driving its import count N toward zero is the
march from hosting toward the Rung-2 rigidity claim.

Prior and future BOUNDED_NO_GO results are boundary data of this feasible
set, not verdicts on GU: each one carves the map.

A construction whose joint grade reaches Rung 1 or better on two or more
sectors becomes a frozen construction candidate and enters the existing
recovery-certification ladder and defense protocol as a new registered
target — this is what satisfies the defense register's reopen conditions.
Weaving must not degrade into sector-specific repair: if the "one"
construction needs per-sector adjustable identifications to fit, that is
the kill condition of RECOVERY-CERTIFICATION, reported honestly with the
weaker surviving compatibility result recorded.

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
- Claim strength always equals the rung achieved: a Rung-0/1 joint survivor
  supports "there exists a construction jointly consistent with these
  sectors with N typed imports" — an honest result in its own right — and
  never the unification claim, which remains Rung 2. Weakening a sector's
  sharp constraint list is a Joe-gated contract change; extending one with
  new evidence is sovereign.
