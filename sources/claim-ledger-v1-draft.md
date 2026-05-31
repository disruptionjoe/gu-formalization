# Media Claim Ledger - Populated Starter v1

Generated: 2026-05-30
Originating card: WRK-379 (Reputation - GU Media Claim-Mining Starter)
Pipeline coordination row: #28
Parent (consumer of this output): #29 media-claim-insight-mining

This file is the proposed initial population of `sources/claim-ledger.md`. It is a draft for maintainer review before promotion to the main claim ledger. Do not treat any of these rows as mathematical evidence; each row only establishes that a specific claim was publicly stated at a specific locator.

## Provenance Discipline Used in This Pass

- Only sources with content already grounded in the local repo (`appendix/execution-log.md`, `09-canonical-self-source-capture.md`) are mined here. WebFetch was denied at session time, so the JRE / Lex / Keating / TOE Jaimungal transcripts could not be pulled fresh. See `mining-report.md` for what was skipped and why.
- Where the public source surface uses notation in math (`U^{14}`, `pi`), the claim text preserves source-native wording.
- Strength tag `verified` means: claim wording cross-checks against a locally captured source artifact. `reconstruction` means: claim wording is paraphrased from local notes that summarize the source rather than quoting it. `speculation` is reserved for derived insight rows and is not used in this starter pass.
- `repo implication` points to the artifact a row would affect IF the claim were ever promoted from provenance to evidence. Implication is descriptive; it is not authorization to mutate the artifact.

## Processed / Remaining Status Table

| source id | status before pass | status after pass | rows added | notes |
| --- | --- | --- | --- | --- |
| `GU-MEDIA-2013-OXFORD` | `transcript-available`, partially mined into `09-canonical-self-source-capture.md` | starter rows landed | 12 | covers observerse naming, endogenous construction `U^{14} = met(X^4)`, projection operator wording, Sector I framing, four-flavors framing, stadium analogy |
| `GU-MEDIA-2020-PORTAL-SPECIAL` | `transcript-available` via Oxford page | not mined this pass | 0 | The Portal presentation re-broadcasts the Oxford lecture plus a preface and post-lecture presentation; the Oxford lecture rows here cover the shared substance. Preface / post-lecture wording remains for the next batch. |
| `GU-MEDIA-WEINSTEIN-SITE-2026` | already captured locally | rows landed | 2 | covers self-description sentence and 14-dimensional Observerse phrasing |
| `GU-MEDIA-OXFORD-SEMINAR-2013` | already captured locally | rows landed | 2 | covers Oxford host-page provenance and abstract framing |
| `GU-MEDIA-2021-DRAFT-RELEASE` | `metadata-checked`; manuscript is email-gated | not mined this pass | 0 | The 2021 draft text is not in the local bundle; do not invent claims from secondary paraphrase. |
| `GU-MEDIA-2020-JRE-1453` | `transcript-available` per Portal Wiki | not mined this pass | 0 | WebFetch denied; recommended as first item in the next-batch mining session (see `mining-report.md`). |
| `GU-POD-2021-JRE-1628` | `transcript-available` per Portal Wiki | not mined this pass | 0 | WebFetch denied; recommended as second item in the next-batch mining session. |
| `GU-POD-2020-LEX-88` | `outline-available`, timestamp 44:19 marked | not mined this pass | 0 | WebFetch denied. Outline timestamp alone is not strong enough for a claim row. |
| `GU-POD-2025-TOE-JAIMUNGAL-GU-40` | `outline-available` | not mined this pass | 0 | WebFetch denied. Outline-only items are not safe sources for a starter pass. |
| `GU-MEDIA-KEATING-QG-FBOZSSLXFVI` | `metadata-checked`, `timestamp-needed` | not mined this pass | 0 | WebFetch denied; flagged as candidate for the modern QG-framing batch. |
| `GU-POD-2025-KEATING-DESI-GU` | `metadata-checked`, `timestamp-needed` | not mined this pass | 0 | WebFetch denied; flagged as the modern cosmology/DESI batch. |

Total starter rows landed in this pass: 16.

## Claim Rows

| source_id | timestamp / locator | claim type | exact topic | strength | repo implication |
| --- | --- | --- | --- | --- | --- |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, exogenous-flavor section (locator: "comes in four flavors" framing block) | terminology | "Geometric Unity comes in four flavors" - GU is presented as a multi-flavor program, not a single construction | verified | `OVERVIEW.md` section 1; `passes/01-foundational-math-lenses/` flavor framing |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, exogenous-flavor section | terminology | "take the concept of observation and break the world into two pieces" - observation, not just spacetime, is the structural primitive | verified | `papers/formal-paper-draft-v2.md` Sec 2; `passes/02-substrate-loophole-lenses/` |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, exogenous-flavor section | construction | `X^4` maps into "some other space," which is called an observerse | verified | `appendix/execution-log.md` Pass 2; observerse terminology grounding |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, exogenous-flavor section | metaphor | stadium analogy: observerse as playing field plus stands, coupled parts | verified | non-load-bearing; useful for blog/expository surface only |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, endogenous construction section | construction | endogenous construction states `U^{14} = met(X^4)` (14-dim observerse as space of metrics on `X^4`) | verified | `papers/formal-paper-draft-v2.md` Sec 4; six-axis L1 substrate axis for related artifacts #24, #33, #34 |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, endogenous construction section | terminology | "let me call this (`pi`) the projection operator" - explicit naming of `pi` | verified | `appendix/execution-log.md` Pass 2-6; settles `pi` as source-native, not local invention |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, endogenous construction section | construction | base-side `X^4` and 14-dim `U` construction are distinguished | verified | source-native notation reconciliation; do not collapse `U` to local `O` without reconstruction tag |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, Sector I section | construction | "In sector I of the Geometric Unity theory, spacetime is replaced and recovered by the observerse contemplating itself" | verified | core Sector I claim; structural input for sibling #25 no-go map (smoothness-of-spacetime assumption is what gets replaced) |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, Sector I section | construction | most fields "dance on the `Y` / `U` space and are observed via pullback as if they lived on `X`" | verified | direct relevance to sibling #29 insight synthesis: this is the source-native pullback statement underwriting the Aufhebung framing in `papers/formal-paper-draft-v2.md` |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, dimensional framing | technical | observerse is 14-dimensional in the endogenous construction | verified | dimensional headline; cross-check against `SRC-GU-WEINSTEIN-SITE-2026` self-description for chronology |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, framing section | methodological | GU is presented as recovering apparently incompatible physical geometries from a general structure with minimal assumptions | verified | `OVERVIEW.md` Sec 1; relevant to sibling #25 (no-go forgetful-image map) because "minimal assumptions" is testable against the four no-go assumption signatures |
| `GU-MEDIA-2013-OXFORD` | Oxford 2013 lecture transcript, framing section | critique | GU positions itself as evading the standard Kaluza-Klein chirality obstruction by replacing the reduction, not by Working inside it | reconstruction | wording is paraphrased from local synthesis notes (`papers/formal-paper-draft-v2.md`), not directly quoted from the Oxford transcript; verify exact phrasing on next mining pass before promoting from provenance |
| `GU-MEDIA-OXFORD-SEMINAR-2013` | Oxford Mathematical Institute event page, https://www.maths.ox.ac.uk/node/10511, abstract section | autobiographical | Oxford records a special lecture by Eric Weinstein on May 23, 2013 | verified | provenance for the 2013 lecture as a real historical source surface (not a later paraphrase only) |
| `GU-MEDIA-OXFORD-SEMINAR-2013` | Oxford Mathematical Institute event page, abstract section | methodological | abstract says "seemingly baroque Standard Model features become geometrically natural under the proposed unification" | verified | terminology row for "geometrically natural"; tag as Weinstein's framing language, not as an outcome |
| `GU-MEDIA-WEINSTEIN-SITE-2026` | https://www.eric-weinstein.com/, GU summary section | terminology | Geometric Unity is described as "a candidate theory of fundamental physics built on the 14-dimensional Observerse" | verified | later self-description aligns with Oxford framing; useful for chronology of public terminology stabilization |
| `GU-MEDIA-WEINSTEIN-SITE-2026` | https://www.eric-weinstein.com/, GU summary section | methodological | Weinstein continues to call GU a "candidate theory" on his own author site as of 2026 | verified | reception/chronology row; the candidate framing is Weinstein's own, not only critics' |

## Notes for Related Cross-Reference

Per the v1 coordination notes, these claim rows are not mutations of related artifacts. They are signals that the parent insight-mining artifact and the mathematical follow-up artifacts may want to consume during the next coordination pass.

- For sibling #25 (no-go-forgetful-image-map): rows 8 and 11 are the most directly relevant. Row 8 (Sector I "spacetime is replaced and recovered") is the source-native statement of the substrate inversion that the no-go map argues is what GU is doing structurally. Row 11 ("minimal assumptions") is the methodological hook that lets the no-go map frame each theorem's implicit hypotheses as the actual point of contention.
- For sibling #26 (type-ii1-spectral-sm-checklist): rows 5, 7, and 9 are the most directly relevant. The `U^{14} = met(X^4)` row is the only source-native dimensional/substrate claim with a clean type signature in this starter pass, so the checklist's "what must be preserved" column can cite it directly when discussing what the GU side names as its candidate substrate.
- For sibling #27 (nielsen-protocol-analogy-pilot): no direct rows in this starter pass. The Oxford 2013 transcript does not engage Nielsen-Ninomiya by name. The pilot card's protocol-analogy work should be driven by JRE / Keating mining in the next batch, where Weinstein has historically spoken about chirality and lattice fermion structure in podcast form. Flagging as a known gap for the next pass.
- For sibling #29 (parent insight-mining): row 9 (pullback statement) is the load-bearing source-native input for the Aufhebung framing in `papers/formal-paper-draft-v2.md`. If #29 wants to synthesize "the substrate is primary, the bundle is observer-frame artifact" as a Weinstein-traceable claim rather than a repo-internal synthesis, this is the row to cite.

## Maintainer Review Questions

Before promotion to the canonical claim ledger, maintainers should decide:

1. Whether the 16 starter rows should land as a first claim-ledger commit OR whether the public ledger should wait for a fuller batch including at least JRE #1453, JRE #1628, and TOE Jaimungal GU-40.
2. Whether row 12 ("GU positions itself as evading the standard Kaluza-Klein chirality obstruction by replacing the reduction") is too synthesized for a starter ledger; if so, drop it from the v1 push and re-mine on the next pass with direct quotation.
3. Whether the `notes for sibling cross-reference` section belongs in the public ledger (it is sibling-coordination metadata) or only in this draft for the coordination pass and maintainer review.
