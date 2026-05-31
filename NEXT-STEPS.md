# Next Steps for Contributors

This repo should not ask first-time contributors to "solve Geometric Unity." The fastest path is to turn the strongest insights into small, falsifiable work units with clear acceptance criteria.

## Quickest Low-Hanging Fruit

| order | task | why it is fast | output | good for |
| ---: | --- | --- | --- | --- |
| 1 | Build the no-go assumption/evasion matrix | The four target theorem families and their known exits are already named in `deep-research/03-*` and `syntheses/06-*`. | A table mapping hypotheses, known evasions, and what each evasion adds. | Mathematicians, physicists, careful generalists |
| 2 | Claim-mine the GU media index | The media list now exists; contributors can add timestamps without taking a position on the math. | Timestamp rows in `sources/claim-ledger.md`. | New contributors, science communicators |
| 3 | Make the Connes finite spectral triple a control checklist | The Type II_1 path is only meaningful if it preserves what the finite control case does. | A checklist of what a Type II_1 extension must reproduce. | NCG/operator algebra contributors |
| 4 | Fill the six-axis specification template for one candidate | This turns broad speculation into a typed research object. | One complete substrate/observer/pairing/causal/emergence/loop spec. | Anyone proposing a new path |
| 5 | Run the Nielsen-Ninomiya protocol analogy pilot | It is the cleanest distributed-systems bridge because the assumptions are already operational. | A theorem-assumption to protocol-assumption map. | Distributed-systems and TCS contributors |

Most of these first artifacts now have draft public surfaces:

- Six-axis protocol: `syntheses/09-six-axis-specification-protocol.md` and `specifications/six-axis/`
- No-go matrix: `syntheses/10-no-go-forgetful-image-map.md`
- Type II_1 checklist: `syntheses/11-type-ii1-spectral-sm-checklist.md` and `specifications/type-ii1-spectral-sm/`
- Nielsen protocol pilot: `syntheses/12-nielsen-protocol-analogy-pilot.md`

## Highest-Upside Research Paths

These are the paths most likely to yield novel or profound insight, ranked by the five-persona rubric in `syntheses/07-supplementary-five-persona-value-ranking-rubric.md`.

| path | novelty | profundity | first public task | why it matters |
| --- | ---: | ---: | --- | --- |
| No-goes as class-relative theorems | 3 | 4 | Assumption/evasion matrix | It is defensible even if every speculative path fails. |
| Type II_1 / non-embeddable spectral Standard Model | 5 | 5 | Finite-control checklist plus Type II_1 requirements | Strongest math-adjacent open direction with real operator-algebra machinery nearby. |
| Six-axis specification protocol | 4 | 5 | Candidate template plus 5 examples | Keeps heterodox work from dissolving into vibes. |
| Nielsen-Ninomiya as distributed-systems impossibility | 5 | 4 | Protocol-analogy pilot | Best "out of the gradient" bridge because it is novel but operational. |
| Observer-pairing anomaly enrichment | 5 | 5 | Toy enriched-bordism scoping note | Profound if it works, but it needs careful scoping before public claims. |
| Forgetful-image substrate invariant thesis | 4 | 5 | Define data/forgetful map for each no-go | The deepest synthesis; should trail the assumption matrix rather than lead alone. |

## Recommended Sprint Sequence

### 0 to 2 hours: public scaffolding

- Keep `NEXT-STEPS.md` as the public routing page.
- Use issue templates for open problems, media claim-mining, and reference pointers.
- Use labels like `good first issue`, `claim-mining`, `open-problem`, `math-check`, `specification`, `distributed-systems`, and `operator-algebras`.

### 2 to 8 hours: first agent-doable artifacts

1. No-go assumption/evasion matrix.
2. `sources/claim-ledger.md` seeded with 5 to 10 timestamped GU claims from transcript-available sources.
3. Finite Connes control checklist for the Type II_1 path.

The initial media v1 bundle is in `sources/claim-ledger-v1-draft.md`, `sources/media-claim-mining-report-v1.md`, and `syntheses/19-media-claim-and-insight-mining-v1.md`. Treat it as provenance scaffolding until the transcript-rich v2 batch lands.

### First week: public collaborator hooks

1. Publish 3 to 5 GitHub issues from the roadmap.
2. Prioritize one issue per audience:
   - operator algebra / NCG
   - anomaly / topology
   - distributed systems / TCS
   - source/media claim-mining
   - accessibility / exposition
3. Ask contributors for falsification paths, not agreement.

### First month: serious research fork

Pick one of:

- Type II_1 spectral Standard Model control extension.
- Nielsen-Ninomiya protocol analogy pilot.
- Observer-pairing Freed-Hopkins toy category.

The fastest likely path to a profound result is **Type II_1 control checklist -> no-go matrix -> Nielsen protocol pilot**. That order gives the repo a rigorous base, a high-novelty math path, and a heterodox bridge without making the public posture sound like a proof claim.

## What To Avoid

- Do not lead with "GU is true."
- Do not claim Freed-Hopkins is observer-relative; frame it as an extension proposal.
- Do not claim computation evades Witten without a construction.
- Do not attempt a full sextuple sweep.
- Do not add more GU-source archaeology unless it changes a specific claim or timestamp.
