# Coverage Gaps - Draft v1

Generated: 2026-05-30
Originating card: WRK-380 (#29)
Companion to: `insight-synthesis.md` + `contributor-tasks.md` in this draft directory.

This file enumerates what is missing from the v1 synthesis pass, why it is missing, and what additional #28 (WRK-379) ledger work would unlock. It is the explicit "what we did not cover" companion to the synthesis, so maintainers can decide whether to ship v1 or wait for v2.

## 1. Sources processed vs unprocessed (per #28 v1)

Per the populated v1 ledger's status table:

**Processed (16 rows total):**

- `GU-MEDIA-2013-OXFORD` (12 rows)
- `GU-MEDIA-WEINSTEIN-SITE-2026` (2 rows)
- `GU-MEDIA-OXFORD-SEMINAR-2013` (2 rows)

**Not processed in v1 (WebFetch denied at session time per #28's mining-report):**

- `GU-MEDIA-2020-PORTAL-SPECIAL` (preface + post-lecture wording)
- `GU-MEDIA-2021-DRAFT-RELEASE` (manuscript is email-gated)
- `GU-MEDIA-2020-JRE-1453`
- `GU-POD-2021-JRE-1628`
- `GU-POD-2020-LEX-88`
- `GU-POD-2025-TOE-JAIMUNGAL-GU-40`
- `GU-MEDIA-KEATING-QG-FBOZSSLXFVI`
- `GU-POD-2025-KEATING-DESI-GU`

**Never on the v1 mining list (Priority 1 + 2 from card):**

- `GU-POD-2020-KEATING-EP49`
- `GU-POD-2021-LEX-163`
- `GU-POD-2021-KEATING-REVEALED-1`
- `GU-POD-2021-KEATING-REVEALED-2`
- `GU-POD-2026-JRE-2503`
- `GU-POD-2020-JOLLY-SWAGMAN-78`
- `GU-POD-2020-DARKHORSE-FUNDAMENTAL-TRUTH`
- `GU-MEDIA-2021-PBS-SPACETIME`
- `GU-RECEPTION-2025-PIERS-CARROLL-WEINSTEIN`
- `GU-RECEPTION-2025-SABINE-AFRAID`

## 2. Synthesis sections explicitly marked `awaiting #28 v2`

The following sections in `insight-synthesis.md` are flagged as not-yet-supportable from the v1 ledger:

| section | what's awaiting | unlock requires |
|---|---|---|
| R2 (`U^{14} = met(X^4)` continuity) | Whether the construction is restated in 2020-2026 podcasts | JRE 1453, JRE 1628, TOE Jaimungal, Keating Revealed |
| R3 (replace-spacetime framing) | Direct quote from JRE 1453 at ~02:44:13 | JRE 1453 transcript mining |
| R5 (stadium analogy recurrence) | Whether analogies repeat across podcast surfaces | Any 2-3 podcast transcript items |
| C2 (chirality-obstruction evasion claim) | Whether Weinstein directly says he evades Witten 1981 | JRE / Lex / Keating / TOE mining |
| N2 (Sector I scoping) | Whether sectors II, III are named in later sources | TOE Jaimungal GU-40 (longest modern surface), JRE 1628 |
| N3 (four flavors enumeration) | Whether the four flavors are named explicitly | Oxford 2013 deeper mining + at least one podcast |
| Type II_1 spectral SM path mapping | Whether Weinstein's "quantization" / "operator side" language exists | JRE 1628 (manuscript-release episode), TOE Jaimungal |
| Nielsen-Ninomiya path mapping | Whether Weinstein discusses chirality / lattice fermions in any form | Keating Revealed Part 1/2 (physics-facing), TOE Jaimungal |
| 2025-2026 modern framing | Whether the framing has drifted in recent appearances | Keating QG, Keating DESI, JRE #2503 |

## 3. What additional #28 ledger work would unlock

Listed in order of synthesis impact per additional source.

### 3.1 Highest unlock: JRE #1628 + TOE Jaimungal GU-40

These two together would likely unlock:

- Direct quote of `U^{14} = met(X^4)` continuation or shift (R2 v2)
- Sector enumeration if Weinstein uses sector-numbering consistently (N2)
- Modern construction state (the 2021 manuscript-release context for JRE 1628; the 2025 long-form for TOE)
- Quantization-side framing for Type II_1 path mapping
- Whether "four flavors" framing survives or drops (N3)

### 3.2 Second unlock: JRE #1453 + Keating Revealed Part 1/2

These would likely unlock:

- Direct verification of "replace spacetime" popular framing (R3 v2)
- Physics-facing claims (Keating is a physicist, unlike JRE; quality of math statements differs)
- Possible chirality / lattice references for Nielsen-Ninomiya path (N-N path mapping)
- Reception-context: how Weinstein himself frames GU for a physics-aware audience vs a general audience

### 3.3 Third unlock: Lex Fridman #88 + #163

These would likely unlock:

- Mid-difficulty technical explanation surface (Lex is technical but not a physicist)
- Reputation-context (Lex #163 includes the Jeffrey Epstein context per media-index)
- Chronology of construction across 2020 (#88) vs 2021 (#163)

### 3.4 Fourth unlock: 2025-2026 modern surfaces

`GU-MEDIA-KEATING-QG-FBOZSSLXFVI`, `GU-POD-2025-KEATING-DESI-GU`, `GU-POD-2026-JRE-2503` would unlock:

- Modern (post-2024) framing of GU
- DESI / cosmology cross-references (if Weinstein has begun connecting GU to recent DESI dark-energy results)
- Whether the program has shifted in response to recent observational physics

### 3.5 Reception batch (separate authorization)

`GU-RECEPTION-2025-PIERS-CARROLL-WEINSTEIN`, `GU-RECEPTION-2025-SABINE-AFRAID`, plus the Decoding the Gurus backlog candidates would unlock:

- Reception-context synthesis (currently sketched in insight-synthesis.md section 5)
- Whether critics are engaging the math or only the framing
- Whether reception drift from Weinstein's "candidate" self-framing is systematic

This batch is reputation-sensitive. Treat it as a separately approved reception batch before mining begins.

## 4. Repo artifacts not yet read or mapped

The following repo artifacts are referenced in the card's Structural Links but not deeply consumed in this v1 synthesis pass:

- `appendix/execution-log.md` — full execution log; v1 ledger cites Pass 2 and Pass 2-6, this synthesis trusts those citations rather than re-reading.
- `papers/formal-paper-draft-v2.md` — formal paper draft; v1 ledger cites Sec 2 and Sec 4, this synthesis trusts those citations.
- `syntheses/09-canonical-self-source-capture.md` — referenced in v1 ledger's provenance discipline. Not directly read in this pass.
- `syntheses/00b-loophole-synthesis-witten-evasion-test.md` and `00c-hegelian-meta-synthesis.md` — Hegelian Aufhebung framing; this synthesis trusts INDEX.md's summary rather than re-reading.
- `deep-research/` — four briefs referenced by sibling #25 but not read here.

A deeper synthesis pass that integrates the deep-research briefs and the full syntheses 00* series should be handled as a follow-up artifact, or as a v2 after #28 v2 lands.

## 5. Related-artifact status notes

Per the draft coordination notes:

- **#26 (type-ii1-spectral-sm-checklist):** TBD. When it starts, it can consume insight-synthesis.md's R2 (`U^{14} = met(X^4)` as source-native L1) as a worked example of "what the GU side names as its candidate substrate" per WRK-379's cross-reference note.
- **#27 (nielsen-protocol-analogy-pilot):** TBD. When it starts, contributor-tasks.md's Task 4 (Ginsparg-Wilson reference pointer) and the GW/overlap framing in sibling #25 are ready references.
- **#30 (hegelian-persona-protocol-method-note):** TBD. The insight-synthesis.md treatment of Aufhebung (via insight R2-R3-N1) is consistent with sibling #25's framing.
- **#31 (stochastic-parity-breaking-test):** TBD. No insight from this v1 pass directly bears on it.
- **#32 (cartan-twistor-g2-guardrail):** TBD. The L1 substrate slot is occupied by `U^{14} = met(X^4)` in insight-synthesis.md; if Cartan/twistor-G_2 is a different L1 candidate, the two specs should be authored side-by-side per sibling #24's framing.
- **#33 (sorkin-causal-set-axis-note):** TBD. The L4 causal-order axis is explicitly flagged underdetermined in contributor-tasks.md Task 2; sibling #33's note is the natural input when it lands.
- **#34 (rg-universality-axis-note):** TBD. The L5 emergence axis is explicitly flagged underdetermined in contributor-tasks.md Task 2; sibling #34's note is the natural input when it lands.

## 6. What this draft does NOT do (out of scope)

- Does NOT propose `sources/media-mining-status.md` as a public artifact in this v1 draft. Maintainer review decides whether the content of this file becomes a public `sources/media-mining-status.md` or stays as coordination metadata.
- Does NOT create any GitHub issue. Contributor tasks are issue-ready markdown for maintainer conversion.
- Does NOT re-mine #28's territory. The starter ledger's row content is taken as input, not re-derived.
- Does NOT make any claim that requires #28 v2 data without flagging it as `awaiting #28 v2`.
- Does NOT modify related artifacts. Cross-refs are read-only.

## 7. Recommendation for maintainer review decision

**Recommendation:** ship the v1 synthesis as `syntheses/08-media-claim-and-insight-mining.md` IF #28 v1 ledger lands publicly. The v1 synthesis is conservative, well-grounded, and explicitly self-flags its `awaiting #28 v2` boundaries. Waiting for v2 will sharpen R2/R3/N2/N3 but is unlikely to change the DoD-7 answer (improved provenance, no priority redirection, mild public-framing risk).

**Alternative:** hold the synthesis until #28 v2 lands JRE 1628 + TOE Jaimungal rows. This produces a stronger first public synthesis but delays the contributor-task issues that depend on a landed ledger.

**maintainer call.** Either is defensible.
