---
artifact_type: exploration
label: W189
created: 2026-07-14
team: HARDENING-MAP
posture: coherence-first program-management pass; exploration grade; honest grading; RUTHLESS prioritization; GU-independence is the credibility axis (RESEARCH-POSTURE.md); registers claim-status items but executes none; drafts/register only; candidate promotion and all external action Joe-gated
role: "Map ALL hardenable items from the day's arc (W144-W188), score them on an impact-vs-difficulty matrix, isolate the high-impact/low-effort QUICK WINS with exact executor-ready actions, and rank the rest. This wave PRODUCES THE REGISTER; it does NOT execute the hardening. Five personas inline (research-program manager; hostile referee / publication strategist; physicist; repo-hygiene / reproducibility engineer; prioritization scorer), one worker, no sub-agents."
verdict: "31-item register built. QUICK-WIN quadrant = 9 items (2 of them FAILING-GATE hygiene, executable now with exact one-line actions); BIG-BET quadrant = 8 (topped by the generic-capture lemma and the all-orders interacting metric, which are the SAME toy-vs-general gate seen from the keep-and-grade side and the open-Krein side); FILL-IN = 9; THANKLESS = 5 (mostly Joe-external, flagged and excluded from the agent fan-out). Two process gates are RED (explorations_readme_surface_map_audit: wave46 undeclared; explorations_top_level_file_boundary_audit: stale, 197 dated top-level notes vs an allow-list of 4). No canon / RESEARCH-STATUS / verdict / posture change; register only."
scripts:
  - tests/W189_hardening_register_checks.py
depends_on:
  - papers/candidates/located-not-forced/HARDENING-QUEUE.md
  - papers/candidates/located-not-forced/STAGING-NOTES.md
  - papers/candidates/keep-and-grade-loop-cost/keep-and-grade-loop-cost-2026-07-11.md
  - papers/candidates/one-residual-complete-picture/one-residual-complete-picture-2026-07-11.md
  - papers/drafts/open-krein-loop-unitarity-bistability/VERIFICATION.md
  - papers/drafts/de-cpl-proxy-vs-raw-bao-likelihood/README.md
  - explorations/W188-class-paper-assessment-2026-07-14.md
  - explorations/W187-gu-dressed-open-selfenergy-2026-07-14.md
  - explorations/W177-build-connection-curvature-c2-2026-07-14.md
  - explorations/W165-lens-abstraction-level-2026-07-14.md
  - explorations/W160-debit3-forced-binary-2026-07-14.md
  - explorations/W157-a2-equals-minus-a1-squared-keystone-2026-07-14.md
---

# W189 -- hardening register for the W144-W188 arc (impact-vs-difficulty matrix + quick wins)

**Role.** Joe's directive: map every hardenable item surfaced across the day's arc, score it on impact
against effort, isolate the high-impact / low-effort quick wins with exact executor-ready actions, and rank
the rest. This wave is a REGISTER: it does not execute any hardening. Five personas inline; the coordinator
fans out execution from the quick-win list afterward. NORTH STAR: drive GU to falsifiability and a
coherent-picture learning; the GU-independent no-gos are the credibility currency, so items that harden the
GU-INDEPENDENT core (or the honesty of an overclaimed leg) score above items that merely tidy.

Every recorded exit status below is CITED from the source wave's ledger; no test was re-run in this pass
except the process-gate sweep (Section 6, machine-checked by `tests/W189_hardening_register_checks.py`).

---

## 1. The register (one row per hardenable item)

Legend. CATEGORY: PAPER-mechanics / PAPER-science / COMPUTATION / PRIOR-ART / TOY-VS-GENERAL / HYGIENE /
WRITE-UP / CLAIM-STATUS. IMPACT and EFFORT are H/M/L (EFFORT `JOE-EXTERNAL` = a Joe-only external action,
excluded from the agent fan-out). QUADRANT: QUICK-WIN (Hi-impact, Lo-effort) / BIG-BET (Hi, Hi) / FILL-IN
(Lo, Lo) / THANKLESS (Lo, Hi) / EXTERNAL (Joe-only).

| ID | ITEM | CATEGORY | WHAT-IT-UNBLOCKS | IMPACT | EFFORT | QUADRANT |
|---|---|---|---|---|---|---|
| H01 | Declare `explorations/wave46` in `explorations/README.md` surface map | HYGIENE | turns `explorations_readme_surface_map_audit` GREEN (currently RED) | M -- a red repo gate is a live reproducibility defect an external reviewer would hit | L -- one line in the wave list | QUICK-WIN |
| H02 | Rescope / repair `explorations_top_level_file_boundary_audit` (asserts 4 allowed top-level notes; 201 exist, 197 dated W###/H## arc notes) | HYGIENE | turns the second RED gate GREEN; makes the top-level-dated-note convention the gate's actual contract | M -- red gate + the gate no longer matches the repo's real convention | M -- a scoping decision + code edit (exclude `^[WH]\d+.*-\d{4}-\d{2}-\d{2}\.md$`), not a one-liner | BIG-BET(small) |
| H03 | Scrub em-dashes from the submission-facing support docs (ENDORSER-REQUEST, REVIEWER, SUBMISSION-RUNBOOK, ZENODO-RELEASE-CHECKLIST, observer-value `submission/` + `zenodo-package/`) | HYGIENE | keeps the reviewer/zenodo-facing surface to the zero-em-dash public-copy rule | M -- external-reviewer-facing text; credibility | L -- scripted ASCII replace on a named file set, visual check | QUICK-WIN |
| H04 | H4 premise-flag consistency audit: verify every "located" narrative locus (title, abstract, intro, S7, S9, S12, status table) carries the `Hom(Z/3,Z)=0` category-error flag adjacent; produce a flag-location map | PAPER-mechanics | closes review-attack W2 on the LEAD paper; makes the premise unmissable | H -- the LEAD paper's single most-mistakable point; guards the headline honesty | L -- grep the loci + a one-page map; no new math | QUICK-WIN |
| H05 | H5 per-claim GU-dependency audit: one-line tag per theorem/lemma ("Cl(p,q) RS-sector only" vs "GU-specific choice X"); produce the GU-independence table | PAPER-mechanics | backs the LEAD paper's GU-INDEPENDENT-CORE claim (the credibility currency) with an auditable table | H -- the credibility axis of the whole program | L -- a tagging pass over an existing theorem list | QUICK-WIN |
| H06 | Demote / clearly-flag the everpresent-fade leg (P6) out of the open-Krein draft's load-bearing claims and abstract | WRITE-UP | removes the draft's weakest (ported, debit-carrying, non-unitary-window) leg from anything the abstract leans on | H -- prevents overclaim on the flagship open-Krein draft; honesty is the currency | L -- edit the draft abstract + one grade line | QUICK-WIN |
| H07 | State the total-C-operator NON-LOCALITY price explicitly in the open-Krein draft (inherits W54/W121 non-locality onto the total space) | WRITE-UP | keeps total unitarity from being oversold; pre-empts a referee "unitary but non-local?" hit | M -- a known referee attack the draft must pre-answer | L -- one honest paragraph, math already in W121 | QUICK-WIN |
| H08 | Write the Bender-Mannheim prior-art delta (T4/T5 = the OPEN-system extension of their closed operative-vs-not dichotomy; cite PU no-ghost + conformal-gravity unitarity) | PRIOR-ART | one of the three prior-art deltas that let the open-Krein draft survive a novelty attack | M -- necessary novelty scaffolding, not sufficient alone | L -- a paragraph; the scholarship is already in W188 S1 | QUICK-WIN |
| H09 | Write the Lee-Wick / CLOP / fakeon prior-art delta (T1 = the removal-family physical-subspace defect re-read sign-definite in the keep branch; the draft does not compete with removal) | PRIOR-ART | second open-Krein prior-art delta; positions the draft against the two established loop-unitarity prescriptions | M -- necessary novelty scaffolding | L -- a paragraph; scholarship in W188 S1 | QUICK-WIN |
| H10 | Write up the W165 SHAPE-BLIND `c_R` lemma as a standalone note: `c_R = -(4/9)(alpha+beta)` on `alpha\|II\|^2 + beta\|H\|^2`, so `sign(c_R) = -sign(alpha+beta)`, shape-orthogonal | WRITE-UP | crystallizes the exact result that any positive-total-weight norm-square forces the tachyon; a clean citable lemma feeding the tachyon-debit story | M -- sharpest single structural fact of the tachyon arc; GU-independent geometry | L -- the derivation is DONE and machine-checked (W165, `tests/W165` 12/12 exit 0); this is transcription | QUICK-WIN |
| H11 | Write up W157 `a2 = -(a1)^2` as COINCIDENCE (MSS-slice-basis + `a0=2` normalization artifact; the physical covariant `c_R = -4/9` breaks it by 4); record that only the SIGN `c_R<0` survives | WRITE-UP | prevents a future wave from re-leaning on the demoted keystone; folds the demotion into the durable record | M -- corrects a would-be structural overclaim (W156 personas 6/10) | L -- the verdict is COMPUTED and decisive (W157, `tests/W157` 19/19 exit 0); transcription into a note | QUICK-WIN |
| H12 | Fold W160's result into claim-status: the crossing-epoch derivation is PROVABLY obstructed (deriving the everpresent amplitude and deriving the epoch are mutually exclusive), so the DESI `z~0.405` is a fitted boundary datum, not a GU prediction; H41 narrows from "un-attempted" to "provably obstructed" | CLAIM-STATUS | sharpens the honest dark-energy-sector claim; pre-empts a "you fit DESI and called it a prediction" attack | M -- protects a falsifiability-relevant honesty boundary | L -- register the status delta (execution Joe-gated); result is COMPUTED (W160, `tests/W160` 27/27 exit 0) | QUICK-WIN(register) |
| H13 | Commit the uncommitted W191 artifacts under their own W191 label (working tree had `explorations/W191-*.md` + `tests/W191_*.py` uncommitted at survey time) | HYGIENE | keeps per-label commit attribution clean; avoids the staging-race sweep | L -- housekeeping, no claim moves | L -- one explicit-path commit | FILL-IN |
| H14 | H3 explicit class-C boundary table (IN/OUT of class C with exact closure conditions: covariant, sector-interior, linear-or-antilinear, so(4)+so(10)-equivariant, sector-built; state what OUT means) | PAPER-mechanics | makes the LEAD paper's delimitation auditable rather than prose (attacks review W3) | M -- strengthens the scoping, not the headline | M -- a real scholarship/consistency table | FILL-IN(upper) |
| H15 | H6 prior-art delta table for the LEAD paper (Wang 2023 24/8=3; Wan-Wang-Yau Pontryagin-mod-3 + color triality; Garcia-Etxebarria-Montero Z_9; Dobrescu-Poppitz; Kaplan-Sun): which layer each targets and what the inverse 2-primary-blindness reading adds | PRIOR-ART | backs the LEAD paper's novelty claim against the nearest references | M -- expected by a referee; scholarship | M -- a careful table, mostly assembled in STAGING-NOTES already | FILL-IN(upper) |
| H16 | H7 antilinear-residual scoping: close-or-scope the K-definite non-chirality re-gradings and the function-space extension (WC-FUNCTION-SPACE-EXT) | PAPER-science | closes the last disclosed residual on the LEAD paper (never needed for the title claim) | M -- tidies a disclosed non-blocker | M -- a bounded computation or a crisp scope paragraph | FILL-IN(upper) |
| H17 | Open-Krein prior-art delta vs driven-dissipative / non-Hermitian open-system bistability (Longhi, PT-open-systems, dissipative phase transitions): state the delta is that the order parameter is the OPERATIVITY OF THE TOTAL METRIC with self-consistent feedback, not a physical observable | PRIOR-ART | the third and hardest open-Krein prior-art delta; a referee has seen bistability/EPs for two decades | M -- necessary; the toughest novelty attack | M -- a genuine literature sweep + cite closest analogues | FILL-IN(upper) |
| H18 | H8/H9 external-reviewer packet + load-bearing-number manifest with a SECOND independent re-derivation per number (LEAD paper) | PAPER-mechanics | lowers the barrier to the external review that W1 (circular internal verification) demands -- the LEAD paper's biggest weakness | M -- attacks W1 but cannot close it (only humans break the single-process ceiling) | M -- packaging + a second derivation per number | FILL-IN(upper) |
| H19 | Firm the de-cpl draft's `M^2 = 8 H0^2` reconstruction-grade mass input (OQ2 open) toward derivation-grade, or scope it loudly in the abstract | PAPER-science | the de-cpl draft's one soft input; the CPL-falsification result is otherwise referee-grade statistics | M -- the draft is publishable-shaped once this is scoped or firmed | M -- a bounded provenance argument or an explicit scope line | FILL-IN(upper) |
| H20 | Conformal-factor gauge status (keep-and-grade Result 2): physical-vs-gauge status of the conformal-mode | PAPER-science | one of keep-and-grade's named load-bearing open items; bears on the unitarity accounting | M -- structural, class-wide open problem | M -- a bounded gauge/BRST analysis | FILL-IN(upper) |
| H21 | GENERIC-CAPTURE LEMMA (decisive): prove a generic Stelle-class operator coupled to a physically reasonable external reservoir realizes the T4 bistable-fixed-point structure (finite Fano-Anderson model is representative, not a rig). Alt discharge: a W187-style dressed computation of `r*` for a real reservoir | TOY-VS-GENERAL | THE gate between "toy observation" and a class-level theorem for the WHOLE open-Krein draft; without it there is no candidate | H -- promotes the flagship draft toward a real paper | H -- a genuine representation/capture theorem or a real dressed QFT computation | BIG-BET |
| H22 | All-orders interacting keep-and-grade metric (Result 3 is free-case + first order only); it is now the SOLE remaining unitarity resource after W132 consolidated the physical-subspace optical-theorem cost into it | COMPUTATION | the load-bearing open item of the keep-and-grade paper; the interacting-C existence question | H -- the keep-and-grade paper's central science gap | H -- an all-orders C-operator construction (W169/W179 are conditional-on-sub-threshold) | BIG-BET |
| H23 | Build the eta-from-gimmel-area MAGNITUDE `kappa_ext` (the nonlocal induced-YM completion, W180/W151), GU-native-in-principle but UNBUILT | COMPUTATION | supplies the one GU-native magnitude in the W187 open-self-energy story; the fade+accretion result already discharges the magnitude LEG dynamically, so this firms the epoch, not the verdict | M -- narrows but does not decide (sign is the decider) | H -- a nonlocal induced-Yang-Mills completion never computed | BIG-BET(lower) |
| H24 | QFT-lift of open-Krein T2/T3 beyond the finite Friedrichs model (even a 1+1 or mini-superspace model) | COMPUTATION | raises the reduced-pole-vs-total-eigenvalue separation from STRUCTURAL to THEOREM in QFT (the draft's strongest single contribution) | M -- strengthens the one genuinely clean point | H -- a field-theoretic construction | BIG-BET(lower) |
| H25 | Remaining 2-loop CLOP item: finite-width Lee-Wick boundary value by full Euclidean continuation + lift of the CLOP-band arithmetic to tensor numerators (Stage C spin-2 numerators already CLOSED, W134 14/14) | COMPUTATION | closes the last half of the family question in the keep-and-grade paper | M -- the family question's residual; much already done | H -- a two-loop tensor / Euclidean-continuation computation | BIG-BET(lower) |
| H26 | Non-translation-invariant strengthening of the no-local-positive-metric theorem: residual = position-dependent local kernels with entire non-polynomial fiber symbols (theorem shown TIGHT on quasi-local metrics, W121 11/11) | COMPUTATION | strengthens the GU-independent no-local-positive-metric theorem (a credibility no-go) | M -- hardens a no-go; the theorem already sits on the true boundary | H -- an operator-theoretic argument over a hard residual class | BIG-BET(lower) |
| H27 | H2 Lean-formalize the LEAD paper's class-C enumeration-completeness + the 2-primary arithmetic identities (machine-checked, no sorry/axiom) | PAPER-mechanics | attacks W1/W3/W6 by machine-checking the finite core beyond the engine sweep | M -- raises rigor of the finite core | H -- Lean proof engineering | THANKLESS(upper) |
| H28 | Fold this week's corroboration (V7 CP^2 kill: every selected twist `m^2 = 1 mod 3`) into the LEAD paper's S8/S9 as fresh category-error evidence (H10, maintainer-gated) | PAPER-science | adds one citation to an already-made point | L -- the paper already makes the equivalent point | JOE-EXTERNAL -- do NOT edit the frozen ready paper without maintainer go | EXTERNAL |
| H29 | Register RESEARCH-STATUS.md / CANON.md / DERIVATION-PROGRESS.md staleness (updated_at 2026-07-07, canon_sweep 2026-07-03) vs the day's arc: bar(b) NARROWED to a single cross-repo datum (the reservoir Krein sign, W187); the physical-subspace optical-theorem cost consolidated into the C-operator item (W132); the crossing epoch provably obstructed (W160); count still {1,3} | CLAIM-STATUS | keeps the runbook-facing status ledger honest with the day's results | M -- the status docs steer the program; drift misleads | L to register / M to execute (Joe-gated canon edits) | QUICK-WIN(register) |
| H30 | LEAD paper external submission: compile `.tex` (Overleaf), final deep-research pass, arXiv submit (hep-th primary; math-ph, math.AT secondary); on live, move folder to `papers/published/` with arXiv id | PAPER-mechanics | the LEAD paper is READY pending exactly these Joe-side steps | H -- ships the theorem-grade GU-independent result | JOE-EXTERNAL -- arXiv endorser + compile + post | EXTERNAL |
| H31 | Note the historical staging-race commit-attribution (W146/W149 artifacts landed under the W145 commit `cbaae18`; "Preserve orphaned W145" `e4d9f4a`); adopt per-label explicit-path staging going forward | HYGIENE | prevents recurrence of cross-label sweeps; history itself is immutable and not worth a rewrite | L -- attribution only; no claim moves | L -- a process note; do not rewrite history | FILL-IN |

---

## 2. Quick-win list (Hi-impact + Lo-effort, ready to fan out)

Each is agent-executable NOW unless flagged. Ordered so the two RED gates and the honesty edits land first.

1. **H01 -- declare wave46 (FAILING GATE).** In `explorations/README.md`, add `[`wave46`](wave46/)` to the
   "Hypothesis-wave runs" list (currently ends at `wave45` on the line after `wave43/wave44`). Re-run
   `python process_gates/explorations_readme_surface_map_audit.py`; expect exit 0. Agent-executable.
2. **H03 -- em-dash scrub (submission-facing).** Replace every `—` with ` -- ` (or a comma, per sense) in:
   `papers/candidates/located-not-forced/{ENDORSER-REQUEST-DRAFT,REVIEWER,SUBMISSION-RUNBOOK,ZENODO-RELEASE-CHECKLIST}.md`
   and `papers/candidates/observer-value-selection-theorem/{submission,zenodo-package-v1.0.0}/**.md`. Visual
   check each. Leave internal CHANGELOG-*.md for a lower-priority pass. Agent-executable.
3. **H04 -- premise-flag consistency map.** Grep the LEAD paper for every "located"/"locates the slot" locus;
   confirm each carries the `Hom(Z/3,Z)=0` category-error flag adjacent; emit a flag-location map
   (locus -> line -> adjacent caveat present Y/N). Deliverable: a short map file; no paper edit without
   maintainer go. Agent-executable.
4. **H05 -- per-claim GU-dependency table.** For each theorem/lemma in the LEAD paper, tag "Cl(p,q) RS-sector
   only (GU-independent)" vs "GU-specific choice X". Emit the table. Agent-executable.
5. **H06 -- demote the fade leg.** In `papers/drafts/open-krein-loop-unitarity-bistability/draft-skeleton.md`,
   move P6 (everpresent-fade dynamical selection) out of the abstract and any load-bearing claim list; mark it
   a clearly-flagged PLAUSIBLE-ONLY remark (ported, debit-carrying, passes a finite-N non-unitary window).
   Agent-executable (drafts only).
6. **H07 -- non-locality price paragraph.** In the same draft, add one honest paragraph: the operative total
   metric inherits the W54/W121 non-locality (kernel decaying at the ghost scale); total unitarity is bought
   with a non-local C-operator. Agent-executable.
7. **H08 -- Bender-Mannheim delta.** One paragraph in the draft: T4/T5 are the OPEN-system extension of the
   Bender-Mannheim closed operative-vs-not dichotomy; cite the PU no-ghost theorem + conformal-gravity
   unitarity. Scholarship already in W188 S1. Agent-executable.
8. **H09 -- Lee-Wick/CLOP delta.** One paragraph: T1 is the removal-family physical-subspace unitarity defect
   re-read sign-definite in the keep branch; the draft characterizes the keep branch, it does not compete with
   removal. Agent-executable.
9. **H10 -- shape-blind c_R lemma note.** Transcribe the DONE, machine-checked W165 result into a standalone
   lemma note: on `alpha|II|^2 + beta|H|^2`, `c_R = -(4/9)(alpha+beta)` (shape-blind), so `sign(c_R) =
   -sign(alpha+beta)`; any positive-total-weight norm-square forces the tachyon; health needs opposite Krein
   signs on the trace vs trace-free isotypic components. Cite `tests/W165` (12/12, exit 0). Agent-executable.

**Register-grade quick wins (produce the status delta; do NOT execute the canon edit -- Joe-gated):** H11
(W157 coincidence write-up), H12 (W160 epoch-obstruction claim-status), H29 (RESEARCH-STATUS/CANON/
DERIVATION-PROGRESS staleness). Each is a low-effort note; the actual canon mutation waits for Joe.

---

## 3. Big-bet ranking (Hi-impact + Hi-effort, by impact-per-unit-effort)

1. **H21 -- GENERIC-CAPTURE LEMMA.** Highest impact-per-effort: it is the single gate that converts the ENTIRE
   open-Krein draft from a toy to a class-level result, and its cheapest discharge (a W187-style dressed
   computation of `r*` for one real reservoir) is bounded. Do this before any open-Krein prior-art polish.
2. **H22 -- all-orders interacting keep-and-grade metric.** The keep-and-grade paper's central science gap and,
   after W132, the SOLE remaining unitarity resource; W169/W179 already reach conditional-on-sub-threshold, so
   the remaining distance is defined, not open-ended.
3. **H24 -- QFT-lift of T2/T3.** Cheapest of the three field-theory lifts (a 1+1 / mini-superspace model
   suffices) and it upgrades the draft's single strongest, cleanest, correct contribution to THEOREM-in-QFT.
4. **H25 -- 2-loop CLOP residual.** Most of the family question is already closed (W124 Stage A/B, W134 Stage C
   spin-2 numerators); only the finite-width Euclidean-continuation boundary value + the CLOP-band tensor lift
   remain, so high completion-per-effort.
5. **H23 -- eta-from-gimmel-area magnitude.** Ranked below H24/H25 because W187 already discharges the
   magnitude LEG dynamically (fade + accretion cross `r*` at a finite epoch for every `kappa0>0`); building
   `kappa_ext` firms the epoch, not the verdict, and the sign (the actual decider) is cross-repo, not here.

(H26 non-translation-invariant strengthening and H27 Lean formalization are real but lower impact-per-effort:
H26 hardens an already-tight no-go; H27 raises rigor on a finite core already reproduced by harness. H02 is a
small big-bet -- a gate rescope, not a research item -- and belongs with the hygiene fan-out, not this list.)

---

## 4. Quadrant counts

| Quadrant | Count | IDs |
|---|---:|---|
| QUICK-WIN | 9 (+3 register-grade) | H01, H03, H04, H05, H06, H07, H08, H09, H10 (+ H11, H12, H29 register) |
| BIG-BET | 8 | H02 (small), H21, H22, H23, H24, H25, H26, H27 |
| FILL-IN | 9 | H13, H14, H15, H16, H17, H18, H19, H20, H31 |
| THANKLESS / EXTERNAL | 5 | H27 (upper-thankless), H28, H30 (EXTERNAL); H31/H13 tidy |

(Some IDs sit on a quadrant boundary and are annotated "(upper)"/"(lower)" in the table; the counts place each
at its dominant quadrant. H27 is counted once, in BIG-BET, as its rigor payoff is real.)

---

## 5. Recommended sequence

Land the two honesty-and-hygiene fronts first because they are cheap and protect credibility: run the
FAILING-GATE quick wins (H01 now; H02 as a bounded gate-rescope) and the em-dash scrub (H03) to get the repo
gate-green and reviewer-clean, then the paper-honesty quick wins (H04, H05 on the LEAD paper; H06, H07, H08,
H09 on the open-Krein draft; H10, H11 as standalone lemma/coincidence notes), and register the three
claim-status deltas (H12, H29, and H11's demotion) without executing the canon edits (Joe-gated). That
clears the entire quick-win quadrant in one fan-out at near-zero risk. THEN commit the sole big bet worth
starting immediately -- H21, the generic-capture lemma via a single dressed `r*` computation -- because it is
the one item that promotes the flagship open-Krein draft from toy to class-level and unblocks H24/H17 behind
it; queue H22 (all-orders interacting metric) as the parallel keep-and-grade track. Hold H28 and H30 (arXiv
compile/submit; frozen-paper corroboration fold) for Joe: they are external actions, not agent work.

---

*Filed 2026-07-14 by TEAM HARDENING-MAP (W189). Coherence-first program-management; exploration grade;
honest grading; RUTHLESS prioritization. Five personas inline (research-program manager; hostile referee /
publication strategist; physicist; repo-hygiene / reproducibility engineer; prioritization scorer); no
sub-agents. This wave REGISTERS hardenable items and their quadrants; it EXECUTES none. No canon /
RESEARCH-STATUS / claim-status / verdict / posture change; register only; candidate promotion and all
external action Joe-gated. Zero em dashes in this paper-facing text (` -- ` throughout).*
