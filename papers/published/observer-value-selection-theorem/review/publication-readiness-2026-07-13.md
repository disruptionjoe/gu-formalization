# Publication-readiness report — 2026-07-13

Candidate: *A Diagonal No-Go for Self-Valuations and an Invariance Classification*

This report reconciles the hostile referee triage and the ten-persona bulletproof review against the repaired source, formalization, tests, compiled PDF, and proposed Zenodo package. It records local readiness only. No submission, upload, DOI reservation, email, account action, commit, tag, or push was performed.

## Outcome

The categorical and physics-adjacent framing was removed from the theorem. The release now makes a narrow Set-level claim, proves it pointwise, distinguishes diagonal-row representation from weak point-surjectivity, and states the group-action result as an elementary invariance classification. The paper's interpretive language is quarantined and explicitly denied theorem status.

The final seven-page PDF compiles and passes visual QA. The Lean module and axiom receipt pass. The dedicated finite test passes corrected identity, singleton, third-grade, and three-cycle controls. The clean deposit package reproduces from an isolated copy.

## Hostile-report reconciliation

| # | Issue | Disposition | Release evidence |
|---|---|---|---|
| 1 | Lemma C was not stated pointwise | **Fixed** | Lemma 3.2 states `alpha(p(a)) = p(a)` for each `a`; Theorem 2.1(2) uses exactly that statement. |
| 2 | Categorical generality was unsupported | **Narrowed** | The title, abstract, setting, proof, and limits now say **Set**. No arbitrary-category morphism claim remains. |
| 3 | Identity control confused one diagonal row with WPS | **Fixed** | Example 5.2 and W99 show that an identity-twisted diagonal can equal a row while no WPS map exists for a two-element codomain. A singleton codomain is the positive WPS control. |
| 4 | A third fixed grade was said to dissolve non-enumerability | **Fixed** | Example 5.3 says the fixed grade defeats invariance and that particular diagonal proof only; a fixed-point-free three-cycle still rules out WPS. |
| 5 | The classification example lacked actual valuations | **Fixed** | Example 5.4 gives the concrete constant functions `p_2`, `p_0`, and `p_1` for the `Z/2` action on `{0,1,2}`. |
| 6 | “Forced,” “commit,” and selection language overclaimed | **Fixed** | Removed from theorem/title/abstract; remaining occurrences explicitly say these are not formal predicates or conclusions. |
| 7 | “Determined” could be read as computational decidability | **Fixed** | Section 4 says the classification is group-action-theoretic and makes no general algorithmic decidability claim. |
| 8 | Title and abstract advertised a forced residual | **Fixed** | Both now advertise only a diagonal no-go and invariance classification. |
| 9 | Bibliography was incomplete or weakly verified | **Fixed and verified** | Sixteen cited entries are defined and used. DOI/journal/arXiv metadata was checked against authoritative records; details are in `submission/VERIFICATION.md`. |
| 10 | Novelty boundary was too soft | **Fixed** | Section 6.6 self-grades the contribution as novel packaging and denies novelty for the diagonal theorem, invariance distinction, observer language, and physical theory. |
| 11 | Lean scope did not match the prose exactly | **Fixed** | Remark 5.5 and `reproduction.md` identify the arbitrary-type function core, Boolean corollaries, and what is not formalized. A separate axiom receipt is included. |
| 12 | Limits omitted major negative results | **Fixed** | Section 7 excludes arbitrary-category, operator-algebra, mechanism, canonical residual, prediction, number/count, full-paper formalization, and component-novelty claims. |
| 13 | Classification recommendation was physics-adjacent | **Fixed** | Proposed arXiv routing is `math.LO` primary. `math-ph` is explicitly rejected; no categorical cross-list is recommended for the Set-only release. |

## Ten-persona review reconciliation

| Persona concern | Disposition |
|---|---|
| Bell 1966 was at risk of being described as adding locality | The prior-art paragraph now distinguishes Bell's Gleason-based hidden-variable route from Kochen–Specker finite noncolorability and from later contextuality formalisms. |
| Curie's principle could be misused as a theorem of forced asymmetry | Curie, Earman, and Norton are presented as interpretive symmetry precedents only; the paper uses no causal principle. |
| The reproduction table omitted the shared `no_closure` declaration | Added with exact function-level scope and paper mapping. |
| Lean's curried type and axiom basis were unclear | `A -> A -> B` is identified as the curried form of `A × A -> B`; the eight-declaration axiom receipt reports no dependencies. |
| Broader GU files could be mistaken for paper evidence | The paper and reproduction note rely only on the named proof module, axiom receipt, and W99. Historical W70/W73 are explicitly excluded from the deposit and evidence. |
| AI-use reporting was absent | A dedicated “Use of generative AI tools” statement identifies drafting, formalization support, literature discovery, and adversarial review, while assigning responsibility to the author and noting independent checks. |
| Subject metadata was missing | MSC 2020 codes and keywords are on page 1; `METADATA.md` recommends `math.LO`. |
| Author metadata was unresolved | Joe Hernandez, Independent Researcher, and `joe@disruptionjoe.com` appear in the source/PDF. ORCID is omitted rather than guessed. |
| Release identity and licenses were unclear | Proposed version is 1.0.0 dated 2026-07-13; paper/docs are CC-BY-4.0, bundled code is MIT. |
| PDF compilation remained a Joe-only gate | Closed locally with Tectonic 0.16.9. All seven pages were rendered and inspected. |
| A local tag/release marker was recommended | Version metadata is staged, but no tag was created because the worktree contains unrelated changes and Joe did not authorize a commit/tag/push. This is not a deposit-content blocker. |

## Verification evidence

- `lake env lean Lean/GUFormalization/ResidualSelection.lean`: pass, exit 0.
- `lake env lean Lean/GUFormalization/ResidualSelectionAxioms.lean`: pass; all eight paper-facing declarations report no axiom dependencies.
- Isolated package: `lake -Kjobs=1 build +GUFormalization.ResidualSelection`: pass.
- `python tests/W99_theorem_finite_instances.py`: pass.
- Historical regression checks W70 and W73: pass, but excluded from the paper's evidence.
- TeX static audit: 16 labels resolved; 16 bibliography keys cited and defined; environments/braces balanced; abstract 178 words.
- Tectonic: pass; no errors, unresolved citations/references, or overfull boxes.
- PDF: 7 nonempty pages; metadata present; page-by-page visual QA passed.
- Package manifest, exclusion scan, and required CFF field scan: pass.

## Proposed Zenodo package

Staging directory: `zenodo-package-v1.0.0/`

The package contains only the article PDF/source, metadata, citation metadata, reproduction and verification receipts, the exact Lean/Python evidence, a minimal Lake configuration, toolchain pin, licenses, and an integrity manifest. Reviews, internal run records, rendered QA pages, compiler caches, broader tests, and unrelated repo files are absent.

Recommended record settings:

- upload type: Publication / Preprint;
- version: 1.0.0;
- publication date: 2026-07-13;
- record license: CC-BY-4.0;
- related code repository: <https://github.com/disruptionjoe/gu-formalization>;
- ORCID: leave blank unless Joe supplies it;
- do not prefill a DOI; use the identifier assigned by Zenodo.

## Joe-only actions that are not readiness blockers

- Review the metadata screen and initiate the actual Zenodo publish action.
- Optionally add an ORCID if desired.
- Separately decide whether and when to commit, tag, or push the repaired release files.

## Verdict

READY FOR ZENODO

Remaining blockers: none.
