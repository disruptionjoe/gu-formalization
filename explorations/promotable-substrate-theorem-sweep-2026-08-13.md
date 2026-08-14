---
title: "ROR-11 first pass: sweeping the conditional-build surface for promotable substrate theorems"
status: draft_result
doc_type: exploration
artifact_type: exploration_result
created: 2026-08-13
target_claim: NONE-NOT-A-KILL
binding: >-
  Binds nothing. No disposition, no verdict, no claim-status, canon, registry,
  ledger, fence or posture change. Every statement in section 3 is PROPOSED by
  this pass and has NOT been proved here. A proposed statement is a candidate
  for extraction work, not a result.
row_change: none
registry_change: none
---

# ROR-11 first pass: promotable substrate theorems on the conditional-build surface

## 0. Why this pass exists

GU's unbuilt source action gates **promotion of conditional results to physical
claims**. It does not gate promotion to *mathematical* results. The repository has
already published three preprints with DOIs, none of which needed the action:

- **OVST** — a diagonal no-go for self-valuations plus an invariance classification
- **LNF** — the scoped two-primary audit of a Clifford Rarita-Schwinger carrier
- **CIO** — compact-image obstructions for a hyperbolic grading in `Sp(32,32)`

**CIO is the important precedent.** It is not GU-independent; it is a theorem about
the GU arena itself, and it published anyway. So the promotable unit is not "work
that avoids GU." It is **a mathematical claim about the substrate, whose truth does
not depend on the action existing.** "Here is an obstruction in this Clifford
setting" promotes. "GU predicts three generations" does not. Same underlying work,
different claim type.

Those three came out of specific waves, ad hoc. The 500-file
`explorations/conditional-build/` surface has never been swept for further
candidates. This is that sweep's first pass.

## 1. Method and coverage

- Enumerated all 500 files in `explorations/conditional-build/`.
- Partitioned by `artifact_type`. **133 are result artifacts**
  (`construction_result`, `conditional_build_result`,
  `construction_and_composition_result`, `exploration_result`,
  `exact_construction_and_composition_result`). The remaining ~367 are ledger
  summaries, migrations, views and releases — bookkeeping, not results.
- Scored the 133 on content signals for an extractable substrate statement
  (exactness, theorem/classification/obstruction/uniqueness language, integer
  certification, explicit rank and dimension counts, probe pass counts), with
  negative weight for physics-claim language that would carry the action gate.
- **Read the top 3 in full.** Sections 2 and 3 are grounded in those three only.

**Stated coverage limit, per the no-silent-caps rule:** this pass read 3 of 133
scored candidates. The ranked list below is a scan, not an adjudication, and the
scoring heuristic has not been validated against the three known-promotable
precedents. A file scoring low here is not evidence of nothing promotable in it.

## 2. Ranked candidates (top 14 of 133)

| score | file |
| ---: | --- |
| 78 | `k77-moving-observation-y14-domain-obstruction-2026-08-05.md` |
| 71 | `first-interaction-krein-and-global-zero-mode-horn-2026-08-05.md` |
| 67 | `selected-k77-coupled-green-domain-2026-08-11.md` |
| 60 | `selected-k77-i2b-first-nonlinear-torsion-absorption-2026-08-13.md` |
| 60 | `selected-k77-gamma-soldered-epsilon-dupsilon-orbit-2026-08-08.md` |
| 57 | `selected-k77-i2b-action-euler-principal-owner-comparison-2026-08-13.md` |
| 56 | `selected-k77-coupled-gauge-noether-bv-2026-08-11.md` |
| 55 | `observed-upback-stress-normal-constraint-vacuum-2026-08-05.md` |
| 53 | `selected-k77-full-reduction-quotient-reconciliation-2026-08-07.md` |
| 49 | `selected-k77-sobolev-edge-current-algebra-2026-08-08.md` |
| 48 | `selected-k77-nonlocal-ultrahyperbolic-polarization-gate-2026-08-11.md` |
| 48 | `k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md` |
| 47 | `selected-k77-relative-edge-bitorsor-topology-2026-08-09.md` |
| 46 | `pre-shiab-gauss-defect-action-bv-symbol-2026-08-05.md` |

## 3. PROPOSED extractable statements

**Read the binding block first.** These are proposed by this pass. None is proved
here, none is checked here, and each would need its own extraction and verification
work before it is a result. They are written as candidate statements so that the
extraction target is concrete rather than a title.

### P-1 — Observation maps cannot be value-only on the mixed-normal bank
*Source:* `k77-moving-observation-y14-domain-obstruction-2026-08-05.md`

> **Proposed.** For the Bianchi-selected `comm/symi/symi` Clifford-contraction
> operator on the grade-one mixed-normal bank, the response is live in all 85
> mixed-normal exterior directions with rank 1,190. Consequently no value-only or
> tangential-only observation map is faithful on that bank: the complete first jet
> along the moving section, decomposed tangential plus vertical-normal, is
> necessary.

*Why it is promotable:* the statement is about an operator on a Clifford bank and
the faithfulness of a class of restriction maps. It is true or false independently
of whether any action exists. The rank and direction counts are explicit integers.

*Nearest published shape:* CIO (an obstruction/classification statement about the
substrate).

### P-2 — A 120-coordinate family of admissible boundary graphs, unreduced by gauge
*Source:* `selected-k77-coupled-green-domain-2026-08-11.md`

> **Proposed.** For the common algebraic boundary form on the coupled bosonic plus
> four-fermion variable set, compatible boundary conditions exist: bosonic
> Dirichlet data together with a symmetric barred/unbarred fermion-trace graph
> yields a half-dimensional gauge-invariant Lagrangian subspace. The family of such
> graphs is not a point. Even the smallest separable family carries 120
> coordinates, and neither ordinary gauge symmetry nor the Green form selects among
> them.

*Why it is promotable:* this is a boundary-triple / Lagrangian-subspace
classification statement for a class of coupled operators. It is the strongest
candidate in this pass, because non-uniqueness with an explicit dimension count is
exactly the shape that publishes, and because a negative selection result needs no
dynamics to be meaningful.

*Caution:* the source also records that the most obvious reality extension fails a
decisive check (anti-symplectic on the fermion-only fixed-normal part, failing when
extended across the moving bosonic normal). Any extraction must carry that.

### P-3 — Positive spectral majorant with an adverse scoped cubic vertex
*Source:* `first-interaction-krein-and-global-zero-mode-horn-2026-08-05.md`

> **Proposed.** The finite free TT pencil admits the constructed positive spectral
> majorant, while the written scalar horn contains, at constant `theta`, a TT cubic
> vertex. The resulting positivity statement is adverse and sharply scoped.

*Why it is promotable, with a caveat:* the majorant construction is a
finite-dimensional spectral statement. But this file also carries a **source
claim** (that the author expressly declines an action as a prerequisite), and
source-facing content is not substrate mathematics. An extraction must separate the
spectral result from the source reading, and the source reading must go through the
register with a claim ID rather than travelling inside a mathematical paper.

## 4. What this pass did not do

- Did not read 130 of the 133 scored candidates.
- Did not validate the scoring heuristic against OVST, LNF or CIO. Doing so is the
  obvious next step and would tell us whether the ranking finds known-good material.
- Did not check any proposed statement for novelty against the literature, or
  against the two already-staged paper candidates
  (`uv-structure-fourth-order-gravity`, `generation-number-boundary-odd-primary`).
- Did not verify any arithmetic quoted above. The integers (85, 1,190, 120) are
  reported as the source files state them and have not been re-derived here.

## 5. Three standing charges (self-review)

**Where the summary outruns the artifact.** The headline "eight of ten runnable"
in the opportunity register rests on a dependency reading, not on any of these
files. And this pass's own headline risks reading as "three promotable theorems
found" when what it found is three *candidate statements from three files*, with
130 unread.

**Where rigor defends a superseded object.** The former service current-state
file was removed from this repository at `43c66e3b`, hours after the opportunity
register was written against it. The register's old service-track column is
historical rather than current authority; native opportunity state belongs in
the research agenda and evidence surfaces. This pass's result-hardening label
describes scientific purpose only.

**Downstream dispositions.** Dissolved: none. Survives: the ROR-11 entry, now with
a concrete candidate list. Needs-recheck: the opportunity register's lane tags, and
whether the scoring heuristic recovers the three known precedents.
