---
title: "Issue-Ready Contributor Tasks - Draft v1"
status: source
doc_type: process_note
updated_at: "2026-05-31"
---

# Issue-Ready Contributor Tasks - Draft v1

Generated: 2026-05-30
Originating card: WRK-380 (#29)
Input substrate: `insight-synthesis.md` + populated v1 ledger (#28) + repo `NEXT-STEPS.md` + repo issue templates.

Each task below is typed to one of the four existing issue templates in `.github/ISSUE_TEMPLATE/`:

- `media-claim-mining.yml`
- `open-problem.yml`
- `reference-pointer.yml`
- `specification-proposal.yml`

Tasks are written as the issue body would be filled out. They remain as markdown stubs in this draft. Maintainers should create or approve GitHub issues from these stubs.

Five tasks total: one per template + one extra in the highest-value category (`open-problem`).

---

## Task 1 - Claim-mine JRE #1453 for the "replace spacetime" framing

**Template:** `media-claim-mining.yml`

**Source ID:** `GU-MEDIA-2020-JRE-1453`

**Link:** Portal Wiki transcript at `https://theportal.wiki/wiki/Joe_Rogan_Experience_1453_-_Eric_Weinstein_(YouTube_Content)`

**Timestamp rows requested:**

```
| GU-MEDIA-2020-JRE-1453 | 02:44:13 (approx, per media-index outline) | terminology | "Geometric Unity replaces spacetime" framing | verified (once direct-quote confirmed) | lab/sources/claim-ledger.md + cross-ref to Oxford 2013 Sector I row |
| GU-MEDIA-2020-JRE-1453 | <find> | construction | any wording of U^14 = met(X^4), pi projection, observerse | verified | cross-ref to Oxford 2013 endogenous construction rows |
| GU-MEDIA-2020-JRE-1453 | <find> | terminology | any sector-numbered references (Sector I, Sector II) | verified | confirms or extends Sector I scope finding |
```

**Caveats to flag in issue body:** Portal Wiki transcript is community-maintained; verify against YouTube video for at least the `02:44:13` row before promotion. Contributor should not invent timestamps; if a row cannot be located, flag and skip.

**Why this is the right first claim-mining issue:** the starter ledger's row 8 (Oxford 2013 Sector I "spacetime is replaced and recovered") needs a popular-surface cross-source check. JRE #1453 is the highest-leverage candidate per the media-index. Direct quote from JRE would elevate insight R3 in `insight-synthesis.md` from "ledger-row-+-media-index-outline" to "verified cross-source recurrence."

**Suggested labels:** `claim-mining`, `good first issue`.

---

## Task 2 - Specification proposal: source-native L1 substrate from `U^{14} = met(X^4)`

**Template:** `specification-proposal.yml`

**Six-axis specification (draft starting point for contributor to complete):**

```
L1 substrate: U^{14} = met(X^4), the space of metrics on a 4-manifold X^4, dimension 14 = 4 (base) + 10 (symmetric 2-tensors on R^4). This is the source-native candidate per ledger row 5 (Oxford 2013 endogenous construction).
L2 observer: an observer is a section of U over a chosen X^4, equivalently a chosen metric on X^4. Self-contemplation framing (ledger row 8, "observerse contemplating itself") is a candidate L2 refinement: observer = fixed point of a self-map. Contributor should pick one.
L3 pairing: pullback via pi (ledger row 6, "let me call this (pi) the projection operator"), so that fields on U appear on X^4 via pi^*. The pairing is the pullback adjunction.
L4 causal order: <unfilled> — Oxford 2013 transcript does not, per starter ledger, specify the causal order on U^{14}. Candidate: lift the causal order on X^4 (per fixed metric) to U^{14} via the projection. Contributor should specify.
L5 emergence: <unfilled> — what emerges and what is fundamental at U^{14} level. Candidate: Standard-Model-like field content emerges as observed-via-pullback structure. Per Oxford 2013, GU is presented as recovering apparently incompatible physical geometries. Contributor should specify.
L6 coordination loop: <unfilled> — how the observer-frame and the substrate-frame coordinate over dynamics. Candidate: pi is fixed and dynamics happens on U; observer sees pullback. Contributor should specify.
```

**Lossy reduction map:** the forgetful map is `pi` itself (pullback to X^4). Smooth-bundle shadow forgets the U-side structure that is not pullback-recoverable.

**Candidate invariant:** chirality/anomaly/generation data that lives at U^{14} level but does not survive `pi^*`. Source-native handle: the "Sector I" sectoring of GU (ledger row 8) suggests at least one sector's worth of data is preserved-but-not-shadow-visible.

**First falsification tests:**

1. Show that `U^{14} = met(X^4)` is incompatible with any chiral-fermion content at the substrate level (i.e. the substrate is too smooth/symmetric to carry chirality). If true, the spec fails before any reduction map matters.
2. Show that the pullback `pi^*` actually forgets nothing non-trivial — i.e. the substrate adds no information beyond the shadow. If true, GU collapses to a standard bundle theory.
3. Show that the four-flavor framing (ledger row 1) implies four different L1 substrates, not one, and that `U^{14} = met(X^4)` is only one of them. If true, the spec is incomplete and must be split.

**References:**

- `lab/sources/claim-ledger.md` (once #28 v1 is committed): rows 5, 6, 7, 8, 9 from Oxford 2013.
- `papers/formal-paper-draft-v2.md` Sec 4 (endogenous construction).
- `lab/process/syntheses/00b-loophole-synthesis-witten-evasion-test.md`.
- Sibling repo card: six-axis-specification-protocol (WRK-375), already drafted at `lab/specifications/six-axis/`.

**Why this is the right first specification-proposal issue:** the six-axis template (sibling #24) was designed to be filled. The starter ledger now provides a source-native L1 substrate candidate that can be cited directly. This issue gives an operator-algebra / NCG contributor a concrete starting point that is not "invent something."

**Suggested labels:** `specification`, `open-problem`.

---

## Task 3 - Open problem: scope Sector I vs other sectors for the no-go map

**Template:** `open-problem.yml`

**Problem:** The starter media ledger surfaces "Sector I" as a Weinstein-native subdivision (Oxford 2013, row 8: "In sector I of the Geometric Unity theory, spacetime is replaced and recovered..."). The repo's no-go-forgetful framing currently reads as "GU evades Witten by substrate replacement" without sector qualification. This open problem: identify and scope the other sectors (II, III, ...) and map each sector to which no-go theorem(s) it structurally engages. The repo's no-go map (sibling WRK-376 / #25) should then be sector-qualified.

**Route:** No-go assumption/evasion matrix.

**Acceptance criteria:**

1. Enumerate Weinstein-named sectors from media surfaces (Oxford 2013, JRE 1453, JRE 1628, TOE Jaimungal GU-40, Keating Revealed Part 1/2) with timestamped quotes.
2. For each sector, identify what structural move it makes (substrate replacement, gauge unification, generation count, etc.).
3. Map each sector to which of the four no-go theorems (Witten 1981, Distler-Garibaldi, Nielsen-Ninomiya, Freed-Hopkins) it structurally engages, evades, or does not address.
4. Update `canon/no-go-class-relative-map.md`'s scope-qualifier language to reflect the sector qualification (this is local repo work, not GU-repo work; coordinate with sibling card owner).
5. Falsification: show that "Sector I" is a one-off use in Oxford 2013 with no consistent sector-numbering across later sources. If true, drop the sector-qualification work and frame the substrate-replacement claim as Oxford-2013-specific.

**References:**

- `lab/sources/claim-ledger.md` (once #28 v1 is committed): row 8.
- `canon/no-go-class-relative-map.md` (sibling #25, draft complete).
- Media items: `GU-MEDIA-2013-OXFORD`, `GU-MEDIA-2020-JRE-1453`, `GU-POD-2021-JRE-1628`, `GU-POD-2025-TOE-JAIMUNGAL-GU-40`, `GU-POD-2021-KEATING-REVEALED-1`, `GU-POD-2021-KEATING-REVEALED-2`.

**Why this is the right first open-problem issue:** it is bounded, agent-doable (transcript mining + table extension), and produces a concrete artifact (sector-qualified no-go map) that improves the repo's defensibility. Falsification path is clean.

**Suggested labels:** `open-problem`, `claim-mining`.

---

## Task 4 - Reference pointer: chirality and lattice fermion literature (for Nielsen-Ninomiya pilot)

**Template:** `reference-pointer.yml`

**Citation or title:** Ginsparg-Wilson relation (`Phys. Rev. D 25, 2649 (1982)`) and Neuberger overlap fermion construction (`Phys. Lett. B 417, 141 (1998)`).

**Link:** `https://link.aps.org/doi/10.1103/PhysRevD.25.2649` (Ginsparg-Wilson), `https://www.sciencedirect.com/science/article/pii/S0370269397013681` (Neuberger).

**Relevance:** Distributed systems / impossibility (Nielsen-Ninomiya protocol-analogy slot).

**Why this matters:** the no-go-forgetful artifact (#25) predicts that "assumption (5) on-site chiral symmetry is the protocol-side analog of GW/overlap, and modified-consistency-model is the expected cleanest evasion." The Nielsen-Ninomiya protocol-analogy pilot (#27) is the natural consumer. When #27 starts, it will need the GW relation and overlap-fermion construction as the canonical "evade lattice no-go by modifying chiral symmetry" reference. This reference pointer issue stages those literature pointers now so contributors don't re-derive them.

**Additional context for the issue:** the GW relation is the standard "modified chiral symmetry" condition that evades Nielsen-Ninomiya without paying its hypotheses' price. The overlap fermion is the concrete construction. Both are well-known to lattice field theorists; the issue exists to make sure the repo cites them rather than re-discovering them.

**Why this is the right first reference-pointer issue:** it is bounded, requires no original work, fills a known gap flagged by sibling #25, and prepares the way for sibling #27 to start without literature search overhead.

**Suggested labels:** `reference-pointer`, `distributed-systems`.

---

## Task 5 - Open problem (second, higher-difficulty): four-flavor enumeration and per-flavor six-axis spec

**Template:** `open-problem.yml`

**Problem:** Oxford 2013 (ledger row 1) frames GU as "coming in four flavors." The starter ledger surfaces exogenous-construction framing (rows 1-4) and endogenous-construction framing (rows 5-7) as at least two of the flavors. The other two flavors are not enumerated in the starter ledger. Open problem: enumerate the four flavors from media surfaces, then for each flavor produce a six-axis specification using the template at `lab/specifications/six-axis/six-axis-template.md`.

**Route:** Six-axis specification.

**Acceptance criteria:**

1. Identify the four flavors by name from at least two independent media surfaces (Oxford 2013 + at least one of JRE / Lex / Keating / TOE).
2. For each flavor, fill the six-axis template (L1 substrate, L2 observer, L3 pairing, L4 causal order, L5 emergence, L6 coordination loop). Mark axes the source does not specify as "underdetermined."
3. Show whether the same forgetful map (candidate: `pi`, per insight N1) applies to all four flavors, or whether each flavor has its own forgetful map.
4. Identify which of the four flavors (if any) is structurally closest to the existing endogenous `U^{14} = met(X^4)` spec from Task 2.
5. Falsification: show that the "four flavors" framing was an Oxford-2013 framing device with no continuation in later sources, in which case the work reduces to a single-flavor spec.

**References:**

- Ledger row 1 (Oxford 2013, "four flavors") once #28 v1 lands.
- Six-axis template: `lab/specifications/six-axis/six-axis-template.md`.
- Worked examples (sibling #24): `lab/specifications/six-axis/examples/` (Type II_1 spectral SM, Sorkin causal-set, RG universality-class).

**Why this is the right second open-problem issue:** it is higher-difficulty than Task 3 (requires multi-source mining + multi-spec authoring), but it is the natural extension of sibling #24's work. It exposes whether GU is genuinely multi-flavor or whether the "four flavors" framing was a single-source rhetorical device, which is itself a useful finding either way.

**Suggested labels:** `open-problem`, `specification`.

---

## Cross-task notes for maintainer review

- All five tasks are gated on at least the v1 starter ledger being committed to the public repo. If maintainers decide to hold the ledger until #28 v2, Tasks 1, 2, 3, 5 should also hold; only Task 4 (reference pointer) is independent.
- Tasks 1 and 3 are the cleanest "claim-mining contributor" handles. Tasks 2 and 5 require more technical depth (six-axis fluency). Task 4 is the lowest-effort.
- No task creates or proposes a GitHub issue body that requires maintainers to make a public claim not already supported by repo evidence. Each task body either cites ledger rows + repo files, or names well-known literature.
- Two of the five tasks (1, 5) require completing the `awaiting #28 v2` mining batch before they can be fully filled. They are listed here so maintainers can decide whether to open them as "issues now, transcript-mining later by contributor" or "hold until #28 v2 lands."
