# Media and Source Index

This index collects public instances where Eric Weinstein or GU-adjacent venues discuss Geometric Unity.

The repo's formal work should treat this file as a provenance map, not as proof. Media entries can establish that a claim, term, analogy, or framing was publicly stated. They do not establish that the claim is mathematically correct.

## Use Discipline

- Use a media item for chronology or terminology only after the relevant line has a source link.
- Use a media item for a mathematical claim only after the relevant claim has a transcript, timestamp, and exact context.
- Prefer primary or official sources over summaries.
- Mark AI summaries, wiki summaries, and social-media paraphrases as discovery aids unless independently checked.
- Keep speculation labels intact: a claim about what GU might imply is different from a theorem, construction, or proof.

## Status Tags

- `metadata-checked` - title/venue/link confirmed, but content not yet claim-mined.
- `transcript-available` - a transcript exists and can support timestamped claim rows.
- `timestamp-needed` - likely useful, but exact timestamp/claim extraction remains open.
- `secondary-index` - useful index or community page, not a primary source.
- `candidate` - plausible GU-relevant source, still needs verification.

## Core Source Surfaces

| id | date | venue / item | type | link | GU relevance | status | use in this repo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `GU-MEDIA-2013-OXFORD` | 2013-05 | Oxford / Simonyi lecture on Geometric Unity | lecture + transcript | [2013 Oxford Lecture](https://geometricunity.org/2013-oxford-lecture/) | Primary public lecture surface for observerse, intrinsic vs auxiliary geometry, field-content framing, Shiab-related language, and the historical GU presentation. | `transcript-available` | Strongest source for claim-mined GU terminology already used in the appendix execution log. |
| `GU-MEDIA-2020-PORTAL-SPECIAL` | 2020-04-02 | "A Portal Special Presentation - Geometric Unity: A First Look" | video presentation | [official GU page](https://geometricunity.org/) | Official release surface for the Oxford lecture recording plus contextual preface and post-lecture presentation. | `transcript-available` via Oxford page | Use for public-release chronology and source-native wording. |
| `GU-MEDIA-2021-DRAFT-RELEASE` | 2021-04-01 | Geometric Unity author's working draft release | manuscript release surface | [official GU page](https://geometricunity.org/) | Official manuscript-release context. | `metadata-checked` | Use for chronology; use the draft itself for claim extraction. |
| `GU-MEDIA-2021-JRE-1453` | 2021-04-01 | Joe Rogan Experience episode 1453 with Eric Weinstein | podcast / video conversation | [Pull That Up, Jamie](https://geometricunity.org/pull-that-up-jamie/) | Public announcement/discussion surface around the manuscript release and visual aids. | `timestamp-needed` | Useful for release context; extract exact GU claims only from transcript/timestamps. |
| `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` | 2021-04 | "Pull That Up, Jamie" visual-aid collection | official media support page | [Pull That Up, Jamie](https://geometricunity.org/pull-that-up-jamie/) | Visual explanations for simpler concepts leading into GU, including GR/gauge-theory incompatibility and Shiab projection motifs. | `metadata-checked` | Use as a pointer to visuals; do not treat visual captions as formal claims without timestamp/context. |
| `GU-MEDIA-2021-PBS-SPACETIME` | 2021 | PBS Space Time discussion of Geometric Unity | interview / explainer | listed on [Portal Wiki GU page](https://theportal.wiki/wiki/Theory_of_Geometric_Unity) | Secondary public discussion surface. | `candidate` | Verify direct link and transcript before use. |
| `GU-MEDIA-KEATING-QG-FBOZSSLXFVI` | 2025-05-22 | "The Problem With Quantum Gravity (ft. Eric Weinstein)" by Dr Brian Keating | YouTube video | [YouTube](https://youtu.be/fBozSSLxFvI) | User-supplied modern media instance. Likely relevant to GU as an alternative to the quantum-gravity framing, with potential discussion of cosmology, Lovelock/GR, spinors, torsion, gauge invariance, and 14-dimensional structure. | `metadata-checked`, `timestamp-needed` | Add transcript/timestamp rows before citing. Best first use: a modern public-claim locator for GU/QG contrast. |

## Candidate Backlog

These entries are worth adding once direct links, dates, and transcripts are verified.

| candidate | likely venue | why it matters | next verification step |
| --- | --- | --- | --- |
| Lex Fridman / AI Podcast GU discussion | Lex Fridman / AI Podcast clips | Long-form public attempt to explain GU and theories of everything. | Verify direct episode/video, date, transcript, and GU timestamp range. |
| Brian Keating / Into the Impossible GU follow-up | Into the Impossible | The official GU visual-aid page points to a more detailed discussion with Brian Keating after the JRE appearance. | Verify direct page/video and extract timestamps. |
| Michael Shermer conversation | IAI / Shermer conversation | Public discussion of ultimate theories / GU in philosophical-science framing. | Verify direct page/video and whether transcript is available. |
| UCSD / recent lecture surfaces | university / public lecture | Possible modern lecture context for the user-supplied Keating clip and recent GU/QG framing. | Verify event page, video title, date, and whether this is distinct from `GU-MEDIA-KEATING-QG-FBOZSSLXFVI`. |
| X / social-media GU threads | Eric Weinstein's X account, Portal Wiki mirrors | Useful chronology for predictions, family-structure claims, and public terminology drift. | Prefer archived or mirrored pages; use only for chronology unless exact posts are independently preserved. |

## Claim-Mining Template

When a media item is processed, add rows like this beneath the relevant source entry or in a future `claim-ledger.md`:

| source_id | timestamp / locator | claim type | exact topic | strength | repo implication |
| --- | --- | --- | --- | --- | --- |
| `GU-MEDIA-...` | `HH:MM:SS` | terminology / prediction / construction / critique | concise description | verified / reconstruction / speculation | where it affects README, appendix, paper, or project plan |
