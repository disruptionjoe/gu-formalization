---
title: "Improvement Register: every audit and panel item, with impact x effort and the implementation plan"
status: process
doc_type: improvement-register
created: 2026-08-03
updated: 2026-08-03
claim_status_change: none
canon_change: none
sources:
  - lab/process/eleven-lens-audit-2026-08-03.md
  - lab/process/mathematician-panel-synthesis-2026-08-03.md
---

# Improvement register

Every item from the 2026-08-03 eleven-lens audit and five-mathematician panel,
none dropped. Two sections (Process & Tooling; Math Research Approach), each
graded Critical / High / Medium / Low. Columns: **I** = impact (C/H/M/L),
**E** = effort (XS &lt; 1 h · S = hours · M = days · L = week+). Items already
fixed this session are marked DONE. IDs are stable — cite them in commits.

Severity here = value of doing the item, not blame. Claim-status-touching
items must run `lab/process/runbooks/claim-status-consistency-quality-workflow.md`;
they are marked (CS). Items gated on a Joe decision are marked (J#) per the
queue in Part D.

---

## PART A — PROCESS & TOOLING

### A-Critical

| ID | Item | Fix | I | E |
|---|---|---|---|---|
| P-C1 | Zenodo release lineage not on `origin/main`; checkpoint `020b682d` unreachable from default branch; `zenodo-package-v1.0.0/`, v2.15, release receipt absent from main; `main.pdf` gitignored/untracked | Merge working branch to main or tag release SHA; name SHA in REVIEWER.md §1; track or de-advertise main.pdf (J3) | C | S |
| P-C2 | MOVE-5 cert prints "NO-GO NOT established", exits 0; verify sibling `indep_check.py` likewise; owner surfaces (DERIVATION-PROGRESS:2594, RESEARCH-STATUS:146, source-action-seiberg-witten-RESULTS:108) say CONFIRMED/9e-15 | Add failure paths (assert/exit) to both; correct the three owner surfaces (CS); math side is M-H6 | C | S |
| P-C3 | 70/780 certs have no assert/raise/exit — unconditional PASSes, concentrated in the adversarial/verify layer (all 8 gu-independent adv_verify*, 5/9 hessian-z3, forcing-slot, carrier-mass, source-action) | **EXECUTED** (2026-08-03, e53e8ae): `process_gates/certificate_shape_audit.py` GREEN; 14 library modules excluded from harness discovery via live import graph (784→770 counted); 66-cert campaign landed hard asserts + exit coupling, zero violations remain. Final accounting (G4 close-out): SIX honest REDs + THREE pinned ESCAPE-FOUND verdicts + label defects + timeout list — see Revision 2 "P-C3 final accounting". Triage pending | C | M |
| P-C4 | Seven-axis/Layer-0 ratification (Joe 2026-07-10) absent from its canon authority file `canon/six-axis-specification-protocol.md` (still six axes, zero L7/Layer-0 hits) while RESEARCH-STATUS:102 and CANON:60 point there | Update the protocol file with the ratified form + supersession note (CS) | C | XS |
| P-C5 | `docs/OVERVIEW.md` (status canon) says "GU is substantially correct", "no longer neutral-map-first", "primary mission is GU reconstruction" — advocacy posture three canon surfaces disclaim; README routes readers to it | Rewrite to the truth-seeking posture or archive with banner (CS) | C | S |
| P-C6 | Lean ledger row T3 "Antilinear null-eigenspace bound: LEAN-VERIFIED" — no antilinear content exists in Lean/; owning canon file says "not a Lean-checked one" | Correct T3 to SYMPY-DERIVED; audit T-rows against actual declarations (CS) | C | XS |
| P-C7 | RESEARCH-STATUS:134 still advertises W211 "free Z/2 / five methods unanimous" — killed twice in-repo (draft-skeleton 07-14; W219) 11 days before the last sweep | Correct the row; point to the uniqueness theorem + W219 (CS) | C | XS |

### A-High

| ID | Item | Fix | I | E |
|---|---|---|---|---|
| P-H1 | Lean ledger T2 titled "conserves net chiral index zero" — the exact phrase HARDENING-QUEUE:118 bans; theorem is 0−0=0 | Retitle per the queue's own instruction | H | XS |
| P-H2 | `LocatedNotForcedFiniteCore.lean` (the paper's headline module), CoflipCore, CoflipAbstract, ResidualSelectionAxioms have no ledger rows and are outside `process_gates/lean_certificate_surface_audit.py`'s file list | Add rows; extend the gate's LEAN_LIBRARY_CERTIFICATES | H | S |
| P-H3 | Ledger LEAN-VERIFIED receipt (2026-07-22) predates the 2026-07-23 rewrite of two certified files; `updated:` never bumped; the valid post-change receipt (zenodo VERIFICATION.md) is unreferenced | Re-receipt or cite the 07-23 receipt; bump | H | XS |
| P-H4 | Root VERIFICATION.md:22 cites `ResidualSelection.lean` as proof of a group-action generalization containing zero group-action content (deposit's own reproduction.md states correct scope) | Align the row to the deposit scope | H | XS |
| P-H5 | `ResidualSelectionAxioms.lean` is a non-enforcing `#print axioms` receipt: not in default target, exits 0 even with sorryAx | **PREMISE CORRECTED + RESIDUE EXECUTED 2026-08-08 (side track).** The stated defect is not present: the Lean tree carries **zero** `sorry` (the only textual hits are docstrings stating their own absence), and LEDGER:59 already labels `ResidualSelectionAxioms.lean` "informational, non-enforcing" rather than LEAN-VERIFIED, with the gate documenting the intentional absence and its reason. The real residue was that LEDGER:23 defines LEAN-VERIFIED as requiring "no `sorry` or unreported axioms" and **nothing enforced it** — a future `sorry` under a LEAN-VERIFIED row would not have been caught. Now enforced as a source-text check in `lean_certificate_surface_audit.py`, explicitly NOT a kernel `#print axioms` guarantee and not to be cited as one. | H | S |
| P-H6 | Reproduction has no committed baseline: no green-run receipt, no expected pass count/runtime; a skeptic's RED is undiagnosable; sweep never flushes stdout (0 bytes for 30 min) | Commit a dated 780/780 receipt; add `flush=True` (reproduce_all.py:190) | H | S |
| P-H7 | No CI runs the Python harness or process gates; lean.yml watches main only — zero CI on any working branch (75+ commits) | Add branches:["**"] + a `--quick --tracked-only` job + process_gates job | H | S |
| P-H8 | Harness has no certificate-shape predicate: `gen_sector_bridge.py` (library imported by 112 certs, anchors never executed) and ~20 other library files counted as passing certs | Shape gate (with P-C3) + `anchors()` called under `__main__` | H | S |
| P-H9 | Two paper certs unreachable by any sweep root (`structurally-forced.../tests/`, `observer-value-selection-theorem/zenodo.../tests/`); scope-audit gate takes the harness's own root list as ground truth (circular) | **EXECUTED 2026-08-08 (side track).** Both halves fixed. `papers/drafts/structurally-forced-internally-undecidable` added to `PAPER_CERT_DIRS` so `general_krein_grading_sign.py` is swept (it runs green; it was the only cert-shaped file outside the declared roots). And the circularity is broken: the existing gate computed its expectation FROM `module.PAPER_CERT_DIRS`, so it verified the harness sweeps what the harness declares and could never see an orphan. A new test walks `papers/` from the filesystem, marks cert-shaped files by the repo's own convention, and requires each to fall inside a declared root. | H | S |
| P-H10 | `pin14_smith_degree_gate.py`: all seven checks restate literals assigned ten lines above (cannot fail); same pattern `gu-forces/verify_legb_intersection.py`; four `a==a`-class asserts in `pin_smith_class_realization_gate.py:146-151` | **EXECUTED** (2026-08-03, e53e8ae): `process_gates/literal_derivation_audit.py` GREEN; both named certs rewritten to derive (pin14: five-step Smith/ABP chain, ABP table checked against cited Ω^Spin column, Sq² via sympy AND Lucas; verify_legb: carrier indices from σ(K3)) and run green. Residual: `pin_smith_class_realization_gate.py` a==a asserts remain (rewrite not in campaign scope; gate correctly does not flag — its other sites derive) | H | S |
| P-H11 | `boundary-eta/verify/plus96_eta_denominator_indep_check.py` re-derives nothing (hand-typed closed forms), contradicting REPRODUCE.md's verify/ promise | Rewrite with a second derivation, or relabel the file's role honestly | H | S |
| P-H12 | requirements "verified numpy 2.4.6" matches no installed build; 76 asserts use tolerances ≥1e-3 despite the "not floating-point tolerances" pin-free rationale | `requirements.lock` for numeric certs (pip-tools already in venv); fix the version note | H | XS |
| P-H13 | DERIVATION-PROGRESS.md terminal entries still say the 2026-07-03 promotions are "staged … PAUSE FOR JOE" (5 occurrences) though files are canon; RESEARCH-STATUS:22 points readers there for a record that isn't there; nothing after 07-03 absorbed | Correction banner + absorb or explicitly close the log (CS) | H | S |
| P-H14 | LANE-STATE.yaml (07-26) asserts needs_joe:false on all lanes / "Nothing needs Joe" / Lane 1 green-up-moving while portfolio holds NEEDS_JOE and 07-29/30 results (B5 BLOCKED, RB7 kill) contradict the lane story; portfolio (07-24) has B5 IN_PROGRESS vs run-plan BLOCKED | Refresh both; then P-H15 | H | S |
| P-H15 | LANE-STATE is hand-written; every stale field is mechanically derivable (last commit touching evidence_ref; needs_joe from portfolio states) | ~50-line generator + CI check that committed == generated | H | M |
| P-H16 | `papers/published/INDEX.md:48` lists LNF and PP3 as "Ready for Joe to post" — both published 2026-07-23 (PP3 receipt in drafting-factory); the factory's GU-based methodology paper (zenodo.21711582) uncross-referenced | Run the repo's own publication-status-reconciliation runbook | H | S |
| P-H17 | Promotion-notice path specified 3 incompatible ways (RESEARCH-STATUS:205 `system/mailboxes/joeops/` — does not exist; AGENTS:35 system-attention; template says in-repo attention/ + envelope); actual notices live in a 4th path (joe-project-management/archive/) | Pick one path; fix all four surfaces; template too | H | XS |
| P-H18 | RESEARCH-STATUS rows 378/397 carry unqualified "Nguyen §3.1 RESOLVED" against the same file's SHIAB-02 (selector identity OPEN); file has no "older rows are provenance" guard | **EXECUTED (verified 2026-08-08): RESEARCH-STATUS rows now read "(existence-only rebuttal; GU's actual operator NOT identified — selector identity OPEN per SHIAB-02)" at :1019 and "(existence-only; selector identity OPEN per SHIAB-02)" at :1038. Row was never marked done; line refs 378/397 are stale against the current ~1019/1038.** Original action: qualify rows or add the guard header (CS) | H | XS |
| P-H19 | RESEARCH-STATUS:376 "N1 (signature audit): (9,5) confirmed — RESOLVED" vs W202/H19 UNDER-DETERMINED | **EXECUTED (verified 2026-08-07): RESEARCH-STATUS now carries "[CORRECTED 2026-08-03: the total signature is UNDER-DETERMINED]" at the N1 row. Register row was never marked done; line ref :376 is also stale, the row is now ~:1009.** Original action: correct the row (CS; pairs with M-H4) | H | XS |
| P-H20 | Signed-readout indexed `active_research` pointing at lab/ while `canon/signed-readout-boundary-theorem-RESULTS.md` is canon-RESOLVED (promoted 07-03); 12 canon docs (incl. the primary-question file) missing from the Current Research Map | Fix row; add missing rows (CS) **EXECUTED 2026-08-08 (side track). Scope was understated twice over: the row says 12 canon docs missing from the Current Research Map; the true figures were CANON.md naming 29 of 57 and the map naming 20 of 57. Fixes: (a) the one genuine misroute corrected — signed-readout pointed at `lab/active-research/` while `canon/signed-readout-boundary-theorem-RESULTS.md` has been `status: canon` since 2026-07-03; the other two `active_research` rows were verified correct, they have no canon file; (b) a mechanically-derived 57-row completeness inventory appended to CANON.md, marking the 28 files absent from the curated spine; (c) a completeness note on the map stating that absence carries no status meaning.** | H | S |
| P-H21 | `ghost-parity-krein-synthesis.md:128` "count is not imported from outside … latent in GU's own geometry" contradicts canon external-by-structure; its own 07-06 update banner doesn't name line 128 (Layer-0 slide) | Extend the banner to name and supersede line 128 (CS) | H | XS |
| P-H22 | Retracted verdict alive in machine-readable frontmatter: `external-datum-ledger…07-29.md` title/outcome still "P3-IS-NOT-EXTERNAL" + body table row, against its own correction banner; companion `source-action-term-by-term…` title carries retracted D3 | Fix YAML + table rows (CS) | H | XS |
| P-H23 | AI-authorship disclosure absent from every top-level repo surface (README, OVERVIEW, VERIFICATION, REPRODUCE, CANON, CONTRIBUTING — zero hits); manuscript discloses properly | One README paragraph: authorship model, what the human decides, what agents do | H | XS |
| P-H24 | "Canon = agent-promoted" disclosure not co-located with the definition (CANON.md:10 defines; :125/:136 mention rule elsewhere) | One clause at CANON.md:10 | H | XS |
| P-H25 | `docs/WHERE-GU-STANDS…` public-register breaks: "proved, with machine-checked computations, that it does not finish" (claim about GU discharged on a reconstruction), "finished, trustworthy … worth citing" (self-certification RESEARCH-POSTURE:128 forbids), ungraded ~2–3× parsimony comparison; §D recommends construction move to a separate repo — contradicted by Lane 1 with no banner | Reword bottom line; delete self-certification; grade-label; add supersession banner for §D (CS) | H | S |
| P-H26 | Randal-Williams cited for the load-bearing e=±p₁/48 at manuscript:796 with no bibliography entry in the DOI'd deposit; W-spin hypothesis of the formula stated nowhere | Fix in a versioned Zenodo correction (v1.0.1) with M-M9; add the hypothesis | H | S |
| P-H27 | Daily portfolio reconciliation decayed since 07-24: 59 explorations unreconciled; `PROOF-STABLE-KERNELS` READY with instructions already executed 07-22 (an agent would redo work); automation signal expired 07-21 with unclosed recheck conditions | One direct reconciliation pass | H | S |
| P-H28 | Wave-scheduling rule absent: pw2fr suffix chain 6 levels deep, ~1.8 commits/hr, zero claim_status_change fields, open list growing (the North-Star note's failure mode) | Adopt: a wave is schedulable only if its stated outcome would move a NAMED gate; prerequisites batch | H | XS |
| P-H29 | Exact-derivative acceptance rule absent: RB6/RB7 nulls were read inside the FD noise band | Adopt: no new interior wave until the prior wave's null is certified with exact derivatives (see M-C2) | H | XS |

### A-Medium

| ID | Item | Fix | I | E |
|---|---|---|---|---|
| P-M1 | Mutation manifest absent for the frozen paper-cited certs (9/11 mutations passed, but nothing prevents regression) | Stored claim-breaking substitutions + driver asserting mutants exit nonzero (~40 lines) | M | S |
| P-M2 | `ghost_parity_krein.py` asserts survive the anti-self-dual triplet and identity ambient metric — certifies weaker claim than docstring/canon name | Add discriminating assert or scope the docstring | M | S |
| P-M3 | Silent scipy-vs-Taylor `expm` fallbacks in 5 certs feed load-bearing numbers with no cross-validation | Validate fallback vs scipy once per run, or require scipy | M | S |
| P-M4 | `gen_ch2_sx_from_codazzi.py` prints headline −5376, asserts only `!= 24`/`!= 3`; `used_chi` assert is tautological; MOVE-4 prints a placeholder `[0.0]` as a computed diagnostic | Assert the headline value; remove/label the placeholder | M | XS |
| P-M5 | MOVE-4 sampling: i==j collisions not excluded → ~2.4% latent false-FAIL on seed change; `anomaly_inflow_toy.py` uses unseeded RNG in checks | Exclude collisions; seed the RNG | M | XS |
| P-M6 | Asserts on hand-typed values that no computation moves (17 sites: euler_S6==2, dim_selfdual==3, etc.); boolean honesty-flags defensible, numeric ones should derive | Derive the numeric ones or mark as declared inputs | M | S |
| P-M7 | "Positive controls first" is a real convention in 141 files but documented nowhere, and violated in 3 named certs (controls after the claim assert — machinery-dead vs claim-false indistinguishable on failure) | Document in tests/README; reorder the three | M | S |
| P-M8 | Four grading ladders with no crosswalk (L1/L2/L3; canon tiers; README's proposal/toy/hosting grades; RESOLVED/CONDITIONALLY/OPEN) | One GRADES.md crosswalk, linked from README | M | S |
| P-M9 | `canon/README.md` declares the whole directory "safe to cite" while 32/55 files carry non-canon YAML status (active/staged/superseded/candidate) | Scope the README claim to status:canon files | M | XS |
| P-M10 | Repo-wide status vocabulary drift: ~8 undeclared values (active, staged, preregistration, completed, complete, blocked, verified…) vs the declared seven — makes the map non-machine-checkable | Extend the declared vocabulary or normalize frontmatter; add a lint gate | M | M |
| P-M11 | Four authority docs lack YAML frontmatter entirely (GEOMETER-VS-PHYSICS-OBJECTS, VERIFICATION, REPRODUCE, WHERE-GU-STANDS) violating RESEARCH-STATUS:77; DERIVATION-PROGRESS + NEXT-STEPS open with UTF-8 BOM breaking strict parsers | Add frontmatter; strip BOMs | M | S |
| P-M12 | Three provably wrong `updated_at` stamps (CANON.md 07-03 with a 07-15 section; no-go map 06-23 with 07-10 content; six-axis template 05-31 with 07-10 content) | Bump; consider a lint that flags content-date > stamp | M | XS |
| P-M13 | `papers/published/INDEX.md` lacks the methodology-paper cross-ref; factory's `CITATION-GROUNDING` cites GU files ≤07-15 — the 07-29 surplus-audit + Layer-0 retraction are exactly its evidence class | Send a v0.6 evidence-refresh seed to the factory | M | S |
| P-M14 | Three candidates carry `citations: PENDING` never verified (keep-and-grade, gen-number-boundary-odd-primary, observer-value-selection) | Citation passes (referee's first attack surface) | M | M |
| P-M15 | Factory's UV-gravity hardening ask (PAPER-SEEDS:66, exact packet spec) unanswered — a valid Lane 3 signal | Answer or decline explicitly | M | S |
| P-M16 | No referee-invitation companion to REVIEWER.md (endorser draft's bibliography-mining logic transfers; unused) | Draft "who to invite and what to ask" | M | S |
| P-M17 | Two-arena draft undersells itself: "recompilation not reproduced, we do not advertise machine-verified" — false since 07-22 (R4TwoArena in pinned default target) | Update the caveat; cite the receipt | M | XS |
| P-M18 | `keep-and-grade-loop-cost` W133 sharpening (Kallen-Lehmann partition) self-identified "natural insertion" never inserted (20+ days) | Insert the subsection | M | S |
| P-M19 | `bar(b)`/H59/count labeled "Joe-gated" in CANON:138 but they are blocked on unbuilt mathematics, not a Joe decision — inflates the apparent queue | Re-label to math-gated; keep verdict-flip Joe-gated (CS) | M | XS |
| P-M20 | `arxiv-submission-package-v7.md` is an abandoned branch (do_not_submit:true) that could be mistaken for the live arXiv path | It already carries the banner — add a pointer from papers/README to the live path | M | XS |
| P-M21 | Sati–Schreiber 2103.01877 (nearest structured neighbor: physical count via π₃ˢ order + refined Adams e) absent from PRIOR-ART-DELTA and the novelty paragraph | Add cite-and-distinguish row | M | S |
| P-M22 | Wan–Wang–Yau version check: LNF must cite v2 (2026-07-21, decisive for the 2/3-split) not v1; Wan 2506.19710 and three more Wang-program papers uncited | Verify bibliography; add rows | M | S |
| P-M23 | Two 2025-26 GU formalization attempts (ResearchGate; one claims "Shiab Uniqueness") unmonitored — priority hazard | Obtain PDFs; check theorem-vs-stipulation; log | M | S |
| P-M24 | W160's "amplitude yes, phase no" stated as GU-derived; it is the standard published everpresent-Λ property (Sorkin; Zwane+; Das+ 2307.13743) | Attribute as inherited; strengthens honesty | M | XS |
| P-M25 | PS-chain verification file: signature-stale (rooted at Spin(7,7), no banner, updated 06-20), ships inside the LNF zenodo package while canon asserts (9,5) | **PREMISE SHIFTED, re-check before acting (2026-08-07): this item calls the file stale FOR BEING ROOTED AT (7,7), but REAL-CLIFFORD-FORM settled the source algebra AT Cl(7,7) on 2026-08-04. The ambient signature (SIGNATURE-AMBIENT) remains open, so a banner is still wanted — but it must now state BOTH statuses, not the one this row assumes. Priority raised: the file ships in the published LNF zenodo package.** Original action: staleness/scope banner; note the (9,5)/(7,7) status (CS) | M | XS |
| P-M26 | NEXT-STEPS.md is a 330KB append-only log whose top block is the only part read | Split live frontier into FRONTIER.md; NEXT-STEPS becomes archive | M | S |
| P-M27 | `computational-toolchain.md` CAS-gate framing: Sage is an accelerator for the branching dictionary, not a gate for the two highest-value branchings (numpy/Racah–Speiser machinery exists in-repo) — partially corrected 2026-08-03 | DONE (OQ-RK1 row); reclassify remaining gates on next edit | M | XS |
| P-M28 | H-07 residuals: README:100 "published preprint" one adjective strong; frozen package says "DOI remains unset" against live DOI; manuscript:706 same | "self-deposited preprint (Zenodo, not peer-reviewed)"; fix in v1.0.1 batch | M | XS |
| P-M29 | CONTRIBUTING:27 sells "Hegelian dialectical synthesis" — aura vocabulary; posture files' honest framing (agent-methodology demonstration) not stated where contributors read | Replace with the plain description | M | XS |
| P-M30 | Six-axis-testability venue decision ("pick a lane") pending — J-gated; its empirical core unexecuted | Joe: venue call (J-queue); then one worked demonstration | M | M |

### A-Low

| ID | Item | Fix | I | E |
|---|---|---|---|---|
| P-L1 | Lean Part B queue "Source" mnemonics unresolvable (R3, V7, A1b…); item D ("power-mean reduction") has no source doc in the repo | Add full paths; locate or drop D | L | S |
| P-L2 | W2Polynomial `certified_theorems` include two content-free tautologies under physics names (`vertical_w2_cancels` = char-2 axiom; `y14_w2_equals_base…` = zero_add) in a machine-readable canon block | Rename or annotate as convention-encoding | L | XS |
| P-L3 | K3IndexArithmetic "from signature" theorems are numeral checks (2=16/8) under general-relation names; header is honest | Rename or annotate | L | XS |
| P-L4 | R4TwoArena docstring/instance-name assert Hom-vanishing the statement doesn't contain (weight-parity only; module docstring honest; ledger row honest) | Align docstring/name | L | XS |
| P-L5 | FiniteCore census: cross-linear filter is `P ∧ ¬P` (tautological 0), sesquilinear≡bilinear and antilinear≡linear definitionally; docstring :219-220 claims derivation; :262-266 honest | Fix the :219 docstring; consider deriving the matching rules | L | S |
| P-L6 | CoflipAbstract: `sig` field and `witnessed : Prop` formally inert (every theorem is about (ε,μ) ∈ ℤˣ×ℤˣ); README oversells | Wire the fields or descope README/docstring | L | S |
| P-L7 | Inert numeric hypotheses (192/96/96/96) in carrier theorem read by manuscript as instantiation; Lean docstring honest; also `torsion_generator_two_primary` unused hypothesis | Annotate or remove; align V15 test copy | L | XS |
| P-L8 | LNF deposit package `lake build` fails (no root module; only module targets work — receipts used those, so valid); reviewer hits unexplained failure | Add the root module or a README note in the package (v1.0.1 batch) | L | XS |
| P-L9 | `no_core_item_selects_generation_integer` formalizes closure of the encoding ("I did not encode one"); manuscript reads it accurately | Optional: docstring note | L | XS |
| P-L10 | RB7 doc says 29 preregistered controls; probe prints 30 | Reconcile | L | XS |
| P-L11 | H44 "Deterministic RK4" is globally 2nd order (np.interp midpoints); empirically benign (1.2e-5) | Relabel or fix midpoints | L | XS |
| P-L12 | H44 fixed-point tol 1e-12 below machine epsilon for its own quantity — loop never exits early; converged_delta is roundoff | Relative criterion | L | XS |
| P-L13 | W129 f0_9 log-interp across a 2.5× grid gap; brentq already used elsewhere in the file | Root-solve the crossing | L | XS |
| P-L14 | RB6 mixes absolute (1e-7) and relative (2e-5) rank tolerances for structurally similar decisions; not scale-covariant across c²/c⁴/c⁶ words; same pattern in three rs_c2 certs | Uniform relative tolerance; note in M-H2's rewrite | L | S |
| P-L15 | DE minor set: A5 band applied GU-only vs its own "common to both" text (±6χ² swing on the ΛCDM control); digit-verification partly repo-vs-repo (A3/A4/A5/A7); radiation in θ★ leg but not BAO E(z) (~0.29 χ², common-mode); "~4.65σ (1-dof equiv)" printed for non-nested zero-parameter comparison; `chi2_marg_amplitude` is a profile not marginalisation (0.11 effect); DR1/DR2 mixing in canon file title/refs vs test chain | Shared-band fix; A-row provenance note; add radiation to E(z); delete σ print; rename; retitle + banner (CS for the last) | L→M | S |
| P-L16 | Notation/wording: `e_R(ν)=1/24=denom(B₂/4)` (should be 24); "power-of-two balance" for 96=2⁵·3 (self-corrected later in file); "Dynkin index 4" normalization-dependent; "128" means dim_R S± and dim_C S in one canon file; Sp(64)=U(64,H) is compact — wrong real form for a Spin(9,5)-containing group (GL(64,H) or Sp(m,n)); commutant is M(14,R)⊗M(64,H) not M(14,C)⊗; PS "ambiguity #4" right conclusion wrong reason (ω²=−1 both, not "only total dim matters") | Six one-line fixes (CS-lite) | L | S |
| P-L17 | IDX wording set: [Â]₁₆ described as classes "of TY14" (vanish on a 14-manifold; descent convention unstated); "two indices pin 5 coefficients" (2 equations, 5 unknowns — the real check is the verify/ re-derivation); APS on closed K3 with fabricated S³ boundary (decorative; η=0 does no work); DECOUPLE table lists denominator 8 for a measured 0; δ-independence argued via "compact perturbation" (bounded, not compact; conclusion right via norm-continuity); ch₂ H-line normalization mixes Cl(9,5) type into a compact Spin(14) computation | Five wording/one typing fix | L | S |
| P-L18 | Cert-lens residue: broad `except` sites are all import-fallbacks (fine) — document the pattern; `tests/README.md` claim-map accuracy unchecked per-directory | Optional doc + one pass | L | S |
| P-L19 | Wiki continuity: this audit/panel/register sequence is a meaningful boundary; no Thinking Wiki event routed (wiki was dirty at last attempt 07-30) | Route one create-only pointer event when wiki volume is writable | L | XS |

---

## PART B — MATH RESEARCH APPROACH

### B-Critical

| ID | Item | Next step | I | E |
|---|---|---|---|---|
| M-C1 | **PREMISE CORRECTED + RESIDUE EXECUTED 2026-08-08 (side track).** The row says "FC3 fired, UNRECORDED". It was recorded: `canon/no-go-class-relative-map.md` GC-FC3 already carried "the standard vector-spinor-minus-trace operator gives ind_H = -144 (not +8) on the file's own computation. FIRING." That is the THIRD register row today found already satisfied, after P-H18 and P-H19. **What was genuinely new:** the recorded firing attacks the `+8` boundary term, while this row's ch2 evidence attacks the `16` bulk term, and the two are unrelated computations. Recorded as **GC-FC3b** (2026-08-08): `tests/gen_ch2_sx_from_codazzi.py` asserts `ch2_normal == -1152`, cert reports `ch2(S_X)[K3] = -5376`, `CH2_NONZERO_OTHER_INDEX`; the `A-hat`-times-rank form of the bulk term is valid only at `ch2 = 0`, so **both halves of `16 + 8` are now independently dead**. **"Retire from live docs" has no target:** CANON.md already records the count as OPEN and "BLOCKED ON A GENUINE GU THEORY GAP", so no live surface asserts the chain and no verdict moves. Fence carried into canon: `pi_!` is NOT_DEFINED, so this retires arithmetic and supplies no replacement count. **Grade C was assessed against the unrecorded premise; actual blast radius is provenance-tier.** | C | S |
| M-C2 | **FD-noise verdict class**: RB7 vertical residual is exactly 0 (published 0.00361491 is s⁻³ roundoff; numbers machine-dependent); RB6 "no nonzero Q resolved" asserted inside declared noise band; two RB7 preregistered controls assert properties of an exactly-zero quantity (will break under any better numerics); W177 floor is FD-limited | Build the exact-derivative library (∂G, ∂²G closed-form — prototype exists in session scratchpad); re-run RB6/RB7/W177 gates; re-issue verdicts (kill likely survives; evidence becomes structural) (CS on re-issue) | C | M |
| M-C3 | **Krein-sign trichotomy (U6/O1)**: uniqueness theorem + W219 make the sign question computable — generate the observable algebra on ker Γ (1664-dim), compute commutant (tensor shortcut), check compactness: irreducible+compact ⇒ sign FORCED; reducible ⇒ missing datum's type/dimension computed; non-compact ⇒ F=∅ ⇒ firewall positivity forced. Retires "one externally-owned bit" framing in any outcome | **EXECUTED-WITH-CORRECTIONS** (2026-08-03): probe + exploration landed (H·I commutant, residual family 0, F=∅ at kinematic scope — all numbers CONFIRMED on independent re-run), then hostile-reviewed; corrections 1–12 applied per `lab/process/hostile-reviews/2026-08-03-trichotomy-review.md` (retyped as COMPRESSION algebra — full matrix algebra by Burnside, not an observable algebra; Theorem-2 warrant replaced by the elementary one; "firewall/deny-Prop-1" label refuted — Prop 1 APPLIES and returns empty; scope re-cut; C4 structural-signature + C8 covariant-contrast asserts added). Exploration tier, claim_status_change: none; result deposit stays J5-gated | C | S–M |
| M-C4 | **Inflow can't carry ℤ/3 (U1)**: "anomaly inflow is the sole bridge" (CRT canon:40) + "spin Dai-Freed ledger has NO 3-primary column" (global-anomaly-leg:252) = the single-decider's SPT route (iii) dies; count-bridge forced onto framed/Pin/String structures. Near-theorem split across two files | **EXECUTED** (2026-08-03): `explorations/inflow-no-three-primary-column-assembly-2026-08-03.md` filed; Pin removed from the candidate list per Revision 1 (framed/String remain, or replace the sole-bridge premise). Row refreshed per council seat 3 staleness finding | C | S |

### B-High

| ID | Item | Next step | I | E |
|---|---|---|---|---|
| M-H1 | **OQ-RK1 branching already filed (U2)**: B5 observer-symbol matrix contains the D₂×D₅ ledger; (3,2,16±) = 4D gravitino with Spin(10)-16 multiplicity; twist = S(6,4)^chiral rank_C 16 | EXECUTED-WITH-CORRECTIONS (2026-08-03): probe `tests/oq_rk1_j_restriction_probe.py` + note `explorations/oq-rk1-j-restriction-on-branched-slots-2026-08-03.md`; hostile review `lab/process/hostile-reviews/2026-08-03-j-restriction-review.md` — claims 1–4 CONFIRMED (claim 1 unconditional, re-filed as its own token), claim 5 (4-vs-8 maps onto the dichotomy) REFUTED as stated (768_H allocation-invariant; unit-count/rank_H homonym); five blocking corrections + Q4/Q10 small-sector refinement applied, probe green 232/232 | H | S |
| M-H2 | **Λ⁵ = internal 126 (U5) + SHIAB-05 correction**: same-chirality channels at every odd k; Λ⁵(ℝ¹⁴) ⊃ 252 = 126⊕126̄ as Lorentz singlet (verified); "external source-action spurion" sentence is a Layer-0 equivocation (14D vs 4D scalar) | Branch Λ⁵(V₁₄) under so(3,1)⊕so(6,4) → PS; explicit Hom on the 128-dim rep (MOVE-4 harness); correct SHIAB-05's consequence sentence (CS) | H | M |
| M-H3 | **Seesaw retrodiction page (U5b)**: SU(4)_c forces m_D^ν = m_up at PS scale ⇒ m_ν₃ ≈ m_t²/M_R ⇒ M_R ≈ 6×10¹⁴ GeV (verified arithmetic) — zero-parameter retrodiction, never written; b–τ unification same machinery | **EXECUTED** (2026-08-03): `explorations/su4c-seesaw-retrodiction-2026-08-03.md` + `tests/seesaw/su4c_seesaw_arithmetic.py` filed; band M_R = 1.1–6.0×10¹⁴ GeV, surplus declared +1 nominal / −1 hostile; non-vacuity control fires (gen-1 nine decades outside). Row refreshed per council seat 3 staleness finding | H | S |
| M-H4 | **Signature crux absorption (U10/R5)**: canon "confirmed by Frobenius" is false (fiber quadratic in g — verified by hand); Kramers wall is (9,5)-only; (7,7) = M(128,ℝ) removes the halving (every dim_H restates) and its O(p,q) Krein form may FORCE the sign (9,5) leaves open; it is the signature of the verified PS chain | Correct canon sentence (CS); build the reality-class ledger table ((9,5) ℍ-value vs (7,7) ℝ-value per count-chain integer); compute the (7,7) stabilizer commutant | H | M |
| M-H5 | **η̃ / bridge gap (i) (U4)**: ν ≅ ℝ ⊕ Sym²(Q*) (panel derivation), trivial over RP³ ⇒ link = RP³×S⁶; Lichnerowicz kills ker D^{S⁶} ⇒ BC applies with no Dai terms; fiberwise reflection candidate ⇒ η̃ = 0 — would close gap (i) from geometry alone. Referee first: reflection vs spin structure/horizontal distribution; then the twisted 7-dim base integral | Verify ν decomposition (half-day); SW/triviality check (hours); reflection lemma (1–2 d); then the base integral | H | M |
| M-H6 | **MOVE-5 repair (with P-C2)**: alt-timelike carrier selected by round(·,3)+1e-3 window picking a 64-dim non-triplet level (Casimir 60/7), empties at 1e-4; worst_flip computed but never gated; exact Casimir spectrum {0,3,8}×{640,832,192} available | Replace with exact integer-eigenvalue clustering; gate worst_flip; document the alt-signature scope honestly (CS) | H | S |
| M-H7 | **Dim-13 restatement (U3a)**: located-not-forced currently proved about the RP³ surrogate; π₁₃ˢ = ℤ/3 purely 3-primary, Im J₁₃ = 0, no String needed (leg_tmf gate vacuous for framed) — "boundary group cannot express the interior obstruction's type" | Restate the disjointness core in dim 13; fix leg_tmf gate; add Ω^Spin₁₃ = 0 citation | H | S–M |
| M-H8 | **Bunke dictionary (U3b)**: universal eta derives Adams e (arXiv:1103.4217) — the dictionary canon:71 says doesn't exist; likely converts gap (iii) into a no-go (η-derived torsion invariant ≠ integer count) | 2-page specialization note; state the gap-(iii) consequence (CS if it closes) | H | S–M |
| M-H9 | **B5 signature test (U7/O2)**: eleven parity values = inertia classes (k,10−k) on ten mirror edges; ε_e are FS-type indicators; prediction (9,5)⇒(58,78), (7,7)⇒(78,58) endpoints only — would derive B5 fields (i)–(iii) natively | **FALSIFIED AT TIER 1, 2026-08-08 (side track).** The endpoint mechanism does not work: `C_perp`'s involution character is `+1` on BOTH bases (residuals 0.0, frame-independent), so the quantity that would flip `k` between horns does not flip and this item cannot discriminate `SIGNATURE-AMBIENT`. Tier 0's base-FS flip is real but cancels downstream. The `(6,4)` fibre premise was confirmed exactly both ways. **`SIGNATURE-AMBIENT` now has no named resolver.** Earlier same-day status follows: **MIS-SPECIFIED + HALF DONE + TIER 0 EXECUTED.** Mis-specified: the named Racah–Speiser module is complexified and signature-blind, returns bit-identical output on either horn, and cannot emit an FS indicator; the sign-carrying object is `C_perp = K.J_obs` in `full20_dewitt_loop_transport_probe.py`. Half done: that probe (green since 2026-07-30) forces all ten `delta_e` EQUAL, so `k` was already `{0,10}` — endpoints only. Tier 0 done: `tests/mh9_base_fs_indicator_horn_flip.py` (green, residuals 0.0) shows the base FS indicator flips `+1` at (3,1) / `-1` at (1,3) with the (6,4) fibre unchanged — **endpoint-flip mechanism confirmed**. Spec correction: per dc-h1 only the RELATIVE sign is well posed; the absolute ordered pair is loop-monodromy dependent. Remaining: Tier 1, re-deriving `mixed_rotation()`'s hardcoded `timelike_leg = 3`. Original action: compute the ten indicators via the in-file Racah–Speiser machinery; rerun under (7,7) | H | M |
| M-H10 | **Bär–Ballmann / boundary-triple skeleton (O3/F4)**: fields (iv)–(v) (Green form, common closed domain) are what the BVP literature constructs generically (1101.1196; non-self-adjoint 1906.08581; non-compact boundary 2401.17784 — zero repo cites); unblocks B5 + OPERATOR-END-PENCIL + RB8 at once; fail-closed contract satisfied natively (symbol-determined pairing; Krein via maximal-isotropic domains) | Write the skeleton against the frozen (9,5)/RS symbol; reorder RB8 before RB7.1 | H | L |
| M-H11 | **RB7 inertia + coercivity (U8/O6)**: saddle verdict uses plain Hessian eigenvalues on a DeWitt-indefinite fiber — only inertia of (Hess, G_V) is invariant; may retire the kill; stabilization is a classification: coercive on the commuting cone ⇔ ker(D⁰)∩ker(C)∩{commuting} = {0} — decidable in days, replacing RB7.1's search; candidate stabilizer = the exact (9/32)(I+T_tr) Gram quartic; physics reading: index-2 saddle = anisotropic (54-direction) VEV branch self-selecting | Re-report inertia (hours, CS if verdict moves); compute the kernel condition; only then a stabilized RB7.1 | H | S–M |
| M-H12 | **DE language + family/point split (DE-01..05)**: "~3.2σ" is 2-dof radius (≈2.7σ; 2.5–3.0 over own ρ-scan); f₀ bounds ~3× looser profiled (0.027→~0.08); "+5.7σ_A" misdiagnosis (ΛCDM +4.0σ_A; real mechanism +19.3 shape — strengthens conclusion restated); "SNe can only hurt" physics error (no H0 info in uncalibrated SNe); family dAIC +1.9..+3.2 below own decisive line — headline should read signal-level-excluded / family-unconstrained | Correct canon + RESEARCH-STATUS wording (CS); the signal-level exclusion itself STANDS | H | S |
| M-H13 | **DESI shape ↔ record accretion (U9)**: exclusion mechanism = too little low-z evolution; W187's r(N)=κ₀√N is a GU-native monotone-in-time coefficient — never connected | Re-solve background with r(N(z)); refit θ★; report Δχ²_shape | H | M |
| M-H14 | **GS factorization as source-action constraint B.7 (topo-6)**: with the corrected 493-density, solve which (n₁/₂, n₃/₂, n_SD-tensor) contents cancel tr R⁸; either a new hard requirement on the spec sheet or "no content cancels" (a falsification) | Extend MOVE-1's exact-Fraction engine; linear solve + factorization test (1–2 d) | H | M |
| M-H15 | **MOVE-1 coefficient propagation (B3)**: 493/2419200 [twice independently verified; already in global-anomaly-leg 07-20] vs published 13/37800; qualitative verdict survives | Propagate to MOVE-1 owner surfaces + tests/chase/README (CS) | H | S |
| M-H16 | **|winding|=1 null hypothesis (phys-6)**: unstated for the dynamical-wall program — hosting read as selection is the exact recurring failure | One preregistration line in the SRC-TOY-01 rung-2 prereg | H | XS |

### B-Medium

| ID | Item | Next step | I | E |
|---|---|---|---|---|
| M-M1 | Signature-independent Λ⁰ lemma (R7/RT-O1): p+q ≡ 2 mod 4 ⇒ dim Hom(S⁺⊗S⁺,Λ⁰)=0 — replaces the 4-case sweep, immunizes fact A against the fork; Lean-able | 2-line proof + corollary; optional Lean | M | S |
| M-M2 | Form-spinor decomposition (RT-O2): Λ²⊗S⁺ = S⁺⊕Σ₁⁺⊕Σ₂⁺ etc. replaces the |W(D₇)|=322560 sum; with End=ℍ gives the corrected real count 16 | Write it; fixes RT-F3 (family dim 16 not 8 — canon 8→4 sentence also wrong constraint name) (CS) | M | S |
| M-M3 | Parity-theorem strengthening (RT-O3): GU-native algebra = full commutant M(896,ℍ); every even index realizable; count=dim_H the natural reading | State as theorem; canon note (CS) | M | S |
| M-M4 | Branching dictionary (R4): one Sage/Racah–Speiser module → Λ^kV⊗S^± decompositions + PS branching + reality types; discharges FC-IRR/FC-HW/FC-MULT/OQ1/OQ-CG-2 and serves M-H1/M-H2 from one build (J2-gated for Sage; D₅ machinery exists without) | Build after J2; cache to JSON | M | M |
| M-M5 | Kobayashi program (R3): discrete decomposability for (O(9,5), O(3,1)×O(6,4)) — decidable cone criterion; minimal rep's null-cone realization = exact-math firewall instance | Literature-verify (oq3b standard), then the root-system computation | M | M |
| M-M6 | f-invariant program (U3c): the detector for α₁β₁ where e is dead; α₁·β₁ factorization posit (3+10=13) with counted surplus; needs (U,fr)² corner data — the Y¹⁴ end has one naturally | Scope Laures/Bunke–Naumann; first number on the RP³×S⁶ model | M | L |
| M-M7 | κ(M) firewall number (O4): boundary-triple Weyl function; N_κ vs Nevanlinna dichotomy = closed-completion vs firewall; bulk type-III result (rankN-krein-tt) blocks bulk Π_κ but NOT the boundary — the wall becomes evidence FOR the hypothesis | After M-H10; conceptual write-up now | M | L |
| M-M8 | η=0 wall dedup + honest 13-dim η (O5/IDX-05/OPP-05): four results = one Hodge-type ansatz; odd-dim boundary has central volume element (no grading, η unobstructed); H37's (H+V)²=H² over-strong; APS-II/Donnelly tooling in-repo | Consolidation note (CS); the honest fibered η is M-H5's follow-on | M | M |
| M-M9 | Framing composite mod-3 (topo-5/HB-02): {0,4} → decided integer; H¹(RP³;ℤ/2) shifts are 2-primary so 3-part = deg f mod 3; also fix the "independent derivation matching" language (HB-01) and add the W-spin hypothesis (with P-H26 in v1.0.1) | One-afternoon computation + text fixes (CS) | M | S |
| M-M10 | ρ-invariant immunity lemma (topo-7): π₁=ℤ/2 ⇒ twisted-untwisted η difference ∈ ℤ[1/2] — permanently immunizes the 3-part against the four flagged 2-adic convention worries | 3–4 h write-up with Donnelly/APS-III citation | M | S |
| M-M11 | Pin⁺₁₄ derivation promote + coprimality (topo-10/HB-06): the ABP+Smith chain (written in the audit) replaces recitation; ℤ/2 (14) ⊥ ℤ/3 (13) — Pin flavor cannot contaminate the count; fixes the portfolio-gate violation | Promote with the chain; leave class-realization open | M | S |
| M-M12 | TQFT/Freed-Teleman axiomatization probe (strat-①): is GU's class the nontrivial element of Ω^{Pin+}₁₄ ≅ ℤ/2? If non-anomalous, the firewall has no home — bounded, well-posed | Write the functorial statement; the class-map question is ANOMALY-DESCENT T1 sharpened | M | M |
| M-M13 | HB-05 Rokhlin retype: lives in Ω^Spin₄ ≅ ℤ (σ/16), not Ω^{Pin+}₄ ≅ ℤ/16; ladder count becomes 4 structural + 3 blocked (2-primarity itself unaffected) | Fix ladder + two-primary-lemma text (CS) | M | S |
| M-M14 | IDX-02 decider repair: BC even/odd-fiber statement inverted; "transparent [PROVEN]" unearned; honest output is ∫Â∧η̃ over the right base (shape mismatch with "scalar e-invariant on the spine") | Fix PART B text + gate; connects to M-H5 (CS) | M | S |
| M-M15 | IDX-04/B9: symbol-eta is content-free (±|p| automatic); remove from "honest global numbers"; "Z-valued APS eta" type error in H37 | Correct capstone + H37 (CS) | M | XS |
| M-M16 | IDX-06: C2 = √(3328/7)·‖ξ‖_E closed-form, frame-dependent — retire "~94% global" and the derived percentages; keep the FORCED_ANALOGY verdict | Correct the two files + DERIVATION-PROGRESS echoes (CS) | M | S |
| M-M17 | IDX-07: b-calculus half-infinite window impossible; noncompact face needs many-body/Vasy or fibered-boundary calculus; discrete-sector conditional vacuous by in-repo FJ rank count (OPP-04: promote the PRIORITY NOTE into both oc2 verdict lines); stale ind=24 import | Banner + verdict-line fixes (CS) | M | S |
| M-M18 | DE additions (DE-12/13/14/15): DESI-w0waCDM positive control through the θ★ pipeline (~30 lines, proves pipeline unbiased); ρ from public DR2 chains; SNe pure-shape leg (M_B-marginalized — the named residual, cheap and decisive); 3-param compressed Planck likelihood (direction: strengthens exclusion) | Four bounded additions to the wave45/46/W129 chain | M | M |
| M-M19 | Λ⁵-VEV surplus audit (R8): run the b5-constraint-surplus template on the internal-126 posit before anyone argues about it | After M-H2 | M | S |
| M-M20 | Boundary EFT matching (phys-8): a minimal 13d defect action gives the shared object that made B5's surplus UNCOMPUTABLE; precondition for surplus-guided search | After M-H10 skeleton | M | M |
| M-M21 | Z₃ vs Z₂ matter parity (phys-7): does the Λ⁵/126 VEV leave ℤ₃ (semi-annihilating DM — distinctive phenomenology) and is it the boundary's 3-primary structure? | Compute the residual discrete subgroup | M | M |
| M-M22 | RG run (phys-10): sin²θ_W = 3/8 earned; metric slot forces PS-side D-even (Sym²(10)=1+54); output M_PS, M_U → τ_p / τ_{n-n̄} (flagship is n–n̄, not p→e⁺π⁰); feeds M_R into M-H3 | Standard 2-loop RGEs | M | M |
| M-M23 | LC-SELECTOR reframe (O7): neutral-on-deficiency = the symplectic/Lagrangian regime of boundary triples, not a dead end; is the ℤ/2 orientation datum a w₁ obstruction or a choice in a connected Lagrangian Grassmannian? | After M-H10 | **ANSWERED 2026-08-08 (side track), C1.** It is a choice in a connected Lagrangian Grassmannian, not a `w1` obstruction, and the dimension is now computed. On the filed `(832,832)` Green trace the deck-fixed admissible set is `⊔ₖ Gr(k,832)`, `dim_R = 2k(832-k)`, maximal **346,112** at `k=416`; the only 0-dimensional strata are `k=0,832`, the two definite sectors ECW3D-A already showed are BOTH admissible. Certificate `tests/c1_domain_moduli_no_canonical_selector.py`, green. Scope: at filed symmetry (Krein, right-`H`, deck) only. | M |
| M-M24 | κ-EP prediction (O8): finite boundary κ bounds the number of exceptional/bistability points — first quantitative firewall claim; feeds the open-krein-loop draft | After M-M7 | M | M |
| M-M25 | Crandall–Rabinowitz on the RB7 branch family (O9): local normal form decides which branches continue into the curved problem before any completion is chosen | 1 week | M | M |
| M-M26 | Observer-value rank-1 scoping (F10): Π₁ Tomita–Takesaki analogue published — sharpen "operator-algebra frontier" to "solved at rank 1, open at rank>1" (verify the reference first) | Citation + one sentence | M | S |
| M-M27 | Kirby–Melvin lens table for all L(p;q) (HB-11d): adversarial control — is the nonzero 3-part special to p=2? | Table computation | M | S |

### B-Low

| ID | Item | Next step | I | E |
|---|---|---|---|---|
| M-L1 | Sage-not-a-gate reclassification residue (R9): after M-M4, re-audit which toolchain gates remain genuinely CAS-bound | Ledger edit | L | XS |
| M-L2 | Howe-duality framing (rep-panel): the Λ•V⊗S dictionary as one osp(1|2)-commutant object — elegant unification, value mostly expository after M-M4 | Optional note | L | S |
| M-L3 | Lattice-Y¹⁴ toy: only if SRC-TOY rung 2 proceeds (inherits hosting-not-selection otherwise) | Hold | L | — |
| M-L4 | S-matrix positivity bounds: needs the unbuilt 4d EFT and a unitarity premise the Krein structure breaks — structurally circular today | Hold until a 4d effective action exists | L | — |
| M-L5 | Twistor methods: guardrail file already gates this; the tangential/gauge fork it would probe is resolved | Skip | L | — |
| M-L6 | Deformation quantization: no identified Poisson structure; live version is the started BV-BFV boundary work | Skip as separate item | L | — |
| M-L7 | Numerical spectral geometry on the link: provably cannot see ℤ/3 (own 2-primary lemma) — wrong instrument; framed/tmf data is the right one (M-M6) | Do not schedule as spectral | L | — |

---

## PART C — IMPACT × EFFORT MATRIX

Quadrants (impact C/H = high; effort XS/S = low). Every register item appears
exactly once, by ID.

**Q1 — HIGH IMPACT, LOW EFFORT (the low-hanging fruit; 27 items):**
P-C1 P-C4 P-C5 P-C6 P-C7 P-C2 · P-H1 P-H3 P-H4 P-H6 P-H7 P-H12 P-H17
P-H18 P-H19 P-H21 P-H22 P-H23 P-H24 P-H28 P-H29 ·
M-C1 M-C3 M-C4 · M-H1 M-H3 M-H12 M-H15 M-H16 M-H6

**Q2 — HIGH IMPACT, HIGHER EFFORT (schedule deliberately):**
P-C3 P-H2 P-H5 P-H8 P-H9 P-H10 P-H11 P-H13 P-H14 P-H15 P-H16 P-H20
P-H25 P-H26 P-H27 · M-C2 M-H2 M-H4 M-H5 M-H7 M-H8 M-H9 M-H10 M-H11
M-H13 M-H14

**Q3 — MEDIUM IMPACT, LOW EFFORT (batch alongside Q1):**
P-M4 P-M5 P-M9 P-M12 P-M17 P-M19 P-M20 P-M24 P-M25 P-M27 P-M28 P-M29 ·
M-M1 M-M2 M-M3 M-M10 M-M11 M-M13 M-M15 M-M16 M-M17 M-M26 M-M27 M-M9 ·
P-L2 P-L3 P-L4 P-L7 P-L8 P-L9 P-L10 P-L11 P-L12 P-L13 P-L19

**Q4 — MEDIUM/LOW IMPACT, HIGHER EFFORT (opportunistic or hold):**
P-M1 P-M2 P-M3 P-M6 P-M7 P-M8 P-M10 P-M11 P-M13 P-M14 P-M15 P-M16
P-M18 P-M21 P-M22 P-M23 P-M26 P-M30 · P-L1 P-L5 P-L6 P-L14 P-L15 P-L16
P-L17 P-L18 · M-M4 M-M5 M-M6 M-M7 M-M8 M-M12 M-M14 M-M18 M-M19 M-M20
M-M21 M-M22 M-M23 M-M24 M-M25 · M-L1 M-L2 · (hold: M-L3 M-L4 M-L5 M-L6 M-L7)

---

## PART D — IMPLEMENTATION PLAN

### Tier 0 — Joe decisions (~40 min; unblock the batches) — CLOSED 2026-08-07

> **This table is historical and carries no open item.** Joe answered these on
> 2026-08-03 and the answers were acted on; the table was never updated to say
> so, so later readers mistook a dated snapshot for a live queue. Dispositions
> recorded 2026-08-07 per Joe direct chat. Nothing here blocks any work, and
> nothing here should be carried forward into a new list.

| J# | Decision | Unblocks | Disposition |
|---|---|---|---|
| J1 | Send the arXiv endorsement email (drafted at `papers/candidates/located-not-forced/ENDORSER-REQUEST-DRAFT.md`) | External-review channel; Part-II sequencing | **WITHDRAWN** 2026-08-07: out of scope. External review is Joe-owned and optional under the 2026-08-03 rule, no work item may block on it, and this one is not to be carried forward or re-raised. |
| J2 | `brew install --cask sage` in a terminal | M-M4 dictionary; remaining CAS gates | **DONE.** SageMath 10.9 installed and in routine use; 30 `.sage` certificates live under `tests/channel-swings/` and the interpreter path is recorded in `lab/process/agent-context-pack.md`. |
| J3 | Name the trunk; authorize merge/tag to main | P-C1; CI value of P-H7 | **AUTHORIZED** 2026-08-03, reaffirmed 2026-08-07. Trunk is `main`. The 2026-08-06 branch integration fast-forwarded `main` onto the integrated line; all agent branches and worktrees are level with it. |
| J4 | Authorize seeding the 4 finished GU-independent assets to Drafting Factory | Banked value; the audit's F-03 | **AUTHORIZED and EXECUTED** 2026-08-03. Seeds filed in `system-runtime#mailboxes/drafting-factory/`: two-plus-one mechanism, two-arena rep-theory core, shape-blind CR lemma, Pati-Salam class-relative survey, good-stable no-go. |
| J5 | Standing answer: may a decisive Tier-1 computation move bar(b)/H59/count (currently Joe-gated)? | M-C3, M-C4, M-H1 result deposit | **RETIRED as superseded**, same day it was written. The "currently Joe-gated" premise is false: `CANON.md:142` records `bar(b)`/H59/the generation count as OPEN because they are blocked on unbuilt mathematics, *not* on a Joe decision, and the ratified 2026-08-03 rule replaced any Joe gate on verdict movement with a required hostile field-specialist review. No standing answer is owed. |

### Batch 1 — Process quick wins (Q1-process + Q3 doc fixes; ~1 agent-day; no claim flips, CS items via the workflow)

1. P-C6, P-H1, P-H3, P-H4 (Lean ledger truth pass) → then P-H2, P-H5.
2. P-C4, P-C5, P-C7, P-H18, P-H19, P-H21, P-H22 (status-surface truth pass, CS).
3. P-C2 process half (failure paths in MOVE-5 + verify; owner-surface wording).
4. P-H6, P-H7, P-H12 (receipt, CI, lockfile) — P-H7 lands fully after J3.
5. P-H17, P-H23, P-H24, P-H28, P-H29 (one-paragraph/one-clause items).
6. Q3 doc-fix batch: P-M4/5/9/12/17/19/20/24/25/27/28/29, P-L2/3/4/7/8/9/10/11/12/13.
7. P-C1 preparation (merge plan + REVIEWER.md SHA) — executes on J3.

### Batch 2 — Math quick wins (Q1-math + Q3-math; ~2–3 agent-days, sequenced by dependency)

1. M-C4 (inflow assembly — pure write-up of two existing results, CS).
2. M-C1 (FC3 FIRED + chain retirement, CS).
3. M-H15 (MOVE-1 coefficient propagation, CS) and M-M16 (C2 94% retirement, CS).
4. M-H6 (MOVE-5 carrier fix — exact Casimir clustering; with P-C2).
5. M-C3 (the trichotomy commutant computation; deposit gated on J5).
6. M-H1 (J-restriction on the B5 ledger; Layer-0 fence stated first).
7. M-H3 (seesaw retrodiction page) and M-H16 (|winding|=1 prereg line).
8. M-H12 (DE language corrections, CS) + M-M15 (symbol-eta removal).
9. M-M1/M-M2/M-M3 (three short rep-theory lemma write-ups).
10. M-M10 (ρ-immunity lemma), M-M11 (Pin⁺ promote), M-M13 (Rokhlin retype),
    M-M9 (framing mod-3 afternoon computation).

### Batch 3 — Structural (Q2; schedule after Batches 1–2 land)

Process: P-C3 shape-gate + 70-cert campaign; P-H8/9/10/11 harness gates;
P-H13/14/16/27 ledger reconciliations; P-H15 derived LANE-STATE; P-H25
capstone rewrite; P-H26 + P-M28 + P-L8 as one Zenodo v1.0.1 correction batch.
Math: M-C2 exact-derivative library then RB re-verdicts; M-H2 Λ⁵ branching;
M-H4 (7,7) ledger; M-H5 η̃ (referee the reflection lemma first); M-H7/M-H8
dim-13 + Bunke; M-H9 B5 signature test; M-H11 inertia + kernel condition;
M-H13 r(N(z)) refit; M-H14 GS/B.7 solve; M-H10 Bär–Ballmann skeleton
(unlocks M-M7/M-M20/M-M23/M-M24).

### Sequencing notes

- Process and math batches are independent; run them in parallel or series
  per capacity. CS-marked items go through the consistency workflow
  regardless of batch.
- The live `agent/null-clifford-omega1-repair` campaign is subject to P-H28/29
  from the moment they are adopted; nothing else in this plan touches it.
- Discovery risk: M-C3, M-H1, M-H9, M-H5 are fork-resolvers — any of them may
  re-rank the remainder of Batch 3. Re-visit this register after each lands.

---

## Revision 1 (2026-08-03, after the interior-agent review of the panel synthesis)

Accepted corrections, applied to the rows above by reference:

- **M-M6 (f-invariant) RETYPED:** Laures' f-invariant lives on even stable
  stems; `alpha_1 beta_1 in pi_13^s` is odd-stem, filtration 3. The item is a
  candidate instrument ONLY after an even-dimensional corner/transgression
  object is constructed; otherwise a different detector is required. Stays
  Tier 3 (REFEREE_CONJECTURE).
- **M-H5 (eta-form) REFEREE TARGET SHARPENED:** the trivialization statement
  is about the 9-dim fiber link over the RP^3 spine; the honest object is the
  S(nu)-bundle over P(TX^4) with the 4-dim base retained. The vanishing
  mechanism in its clean form: if the fiberwise reflection preserves the
  actual framed/Spin operator and domain, then x = -x, and on a purely
  3-primary group 2 is invertible, forcing x = 0. Preservation of the
  framing/operator/domain, plus global bundle control over P(TX), are THE
  referee targets (REFEREE_CONJECTURE until then).
- **M-H2 follow-on CHECKLIST:** channel-to-seesaw requires, in order: the
  bilinear, the Krein pairing, the reality condition, a nonzero VEV, the
  induced 4D mass operator. M-M19's surplus audit runs against this list.
- **M-C4 CANDIDATE LIST NARROWED:** Pin removed (presumptively 2-primary);
  redirect is framed/String or another explicitly odd-primary-capable
  structure. Assembly note edited accordingly.
- **M-H14 REFINED:** anomaly-cancellation-as-B.7 adopts quotient-aware
  constraint-surplus accounting.
- **HEADLINE LABELS ADOPTED** (panel output convention, retroactive):
  VERIFIED_REPO_DISCONNECT — U1 inflow assembly, U5's odd-k/2002 arithmetic,
  the W211/W219 propagation findings, FC3-fired. CHEAP_NEW_COMPUTATION —
  U2/M-H1 J-restriction (executed), U6/M-C3 trichotomy at kinematic scope
  (executed), M-H3 seesaw arithmetic (executed, POSIT grade).
  REFEREE_CONJECTURE — U4/M-H5 eta-form vanishing, M-M6 f-invariant route,
  the trichotomy's dynamical extension, the seesaw's physical reading, the
  B5 endpoint prediction (M-H9).

---

## Revision 2 (2026-08-03, anchor council adjudication)

Source: `lab/process/anchor-council-2026-08-03/` (seats 1–4 + adjudication).
New rows and riders; no existing verdict or grade changes.

| ID | Item | Next step | I | E |
|---|---|---|---|---|
| M-H17 | **BRST/quotient exit has no register ID** (seat1 H4, VERIFIED_REPO_DISCONNECT): the hostile trichotomy review made adding this exit a required correction and no queue item followed. Five-step decomposition (seat1 DQ5): (i) nilpotent interacting BRST charge Q on the RS/ker Γ sector (W173 has only the FREE bicomplex); (ii) state complex; (iii) H⁰(Q) genuinely computed (W207 does not); (iv) nondegenerate descended pairing; (v) commutant + positive-pairing classification on the quotient. Single named blocker: C2 = 155.36 does not close without the unbuilt Y¹⁴ connection-curvature 2-form | Open the construction ledger; any partial step is progress; seat1 K6 names the payoff (positivity interior-supplied would END the boundary-supply reading — the kill most worth attempting) | H | L (blocked) |
| M-M28 | **Layer-0 fence-row bundle** (seats 3–4): "128" three-way (Cl(7,7) Majorana dim / dim_C S / imposter block); "13" three-way (RS multiplicity in 1664=13·128 / dim of the Y¹⁴-end link / anchor-3 receptacle — no artifact relates them); "chirality" four-way (Z2 condensate parity / interior index / 4D V−A / ω-halves); F/Q/Z graded factor-2; RP³×S⁶ = working MODEL (true link: 9-dim S⁶-bundle over RP³ spine, indefinite base required) | **PARTLY ABSORBED** (Resolver Wave B, 2026-08-03): the Q3 operator is renamed `P_hinge`, explicitly distinct from external count/relative-KO `P3`; the 128/chirality/graded-factor fences now control the Wave-B READ-FIRST table and Wave-A handoff. The 13/link-model fences remain recorded here and must travel with the dim-13 wave. | H | XS–S |
| M-M29 | **W224 answers DQ4 and nobody cites it** (seat4 back-pressure #1, VERIFIED_REPO_DISCONNECT): the rolling mode p's representation type — W224 (35/35): only built vacuum candidate is an internal singlet, isotropy the full non-compact Sp(32,32;H). EXACT for the singlet-isotropy/Prop-1 consequence; SOURCE-AUDIT for the identification. Also: p and the record count N are the same variable (N = e^{4p}) — the positivity anchor's cheapest item is a typing question about the cosmology anchor's mode | Wave A-3: READ-FIRST typing + absorption note; upgrade path for the identification named | H | S |
| M-M30 | **Fork-merge absorption (JP1/JP2)**: fiber (6,4) ⇒ carrier fork collapses onto the signature fork ((3,1)→(9,5); (1,3)→(7,7); the TX^{1,3}⊕N^{6,4}⊂Y^{7,7} option is the (7,7) horn); JP1: count-edge existence (C3∧C4) + indefinite-base requirement (boundary-einvariant §7) forbids the compact carrier (4,0)+(5,5) — the finite census's side | JP2 adopted for planning (adjudication R3). JP1: hostile field-specialist review REQUIRED (J5) before any fork-table edit | H | S + review |
| M-M31 | **M-M7 rider (adjudication R2, BINDING)**: "finite boundary κ ⇒ firewall" is unsupported and opposite-signed vs rankN at finite rank (definitizable ⇒ ghost removable ⇒ HORN Q). M-M7 may not assert either direction until the boundary operator exists (D3) and the inference is adjudicated | Rider recorded; DQ7 blocked on DQ6 + adjudication | M | — |
| M-M32 | **M-M20 assumption disclosure** (seat4 §1, VERIFIED_REPO_DISCONNECT): "minimal 13d defect action after M-H10" schedules the consequence of A1∧A2 (13-dim count boundary ≡ firewall adapter ≡ BVP boundary) — identifications no artifact establishes; firewall canon itself says "candidate", not identification | Annotate M-M20 as conditional on A1∧A2; the identification itself is the open item (needs D3 + D4 + an exhibited map) | M | XS |

**Rider on M-H13 update (2026-08-03, DE certification redo):** item (b)
DISCHARGED — the synthetic-injection positive control passed all
preregistered thresholds (tests/de-certification/de12b_*, exit 0); the
pipeline is certified unbiased and C10 stands on it. Item (a) SHARPENED to
BLOCKED-ON-A4: the observation→…→equation composition fails first at the
normalization arrow, which needs the unbuilt native Z_U = |D_A U|² (W203
ledger); the k=0 limit annihilates exactly and only the base-spatial
sub-block, so it cannot decide c_kin — the bridge is BLOCKED, not failed.
Decisive object named: Z_U's (c_b : c_f) block ratio on the A3
configuration. Original rider below stands otherwise.

**Rider on M-H13 (records↔DE refit):** gated on Wave A-2 — (a) the W230
c_kin↔FLRW mapping question (A6), (b) DE-12 pipeline positive control,
(c) the +19.3 inverse-problem feasibility check (with the JP4
signed-readout extension). Pre-register pass/fail per seat2 §2.1(iv)
before any refit is scheduled. Failure modes must be reported per seat2
§4.1's three-way split (bridge fails / rescue spent / saturation), and a
DE-side failure is NOT a bar-(b) failure (r typed differently).

**Rider on P-C3 honest REDs (adjudication R7):** correction banner +
re-run when each directory is next touched; the two "trap decoupling"
labels and the Stueckelberg M_eff/M_D line join the small-fix tail.

**Cross-repo:** records↔DE proposal note dispatched to
`repos/private/system-runtime/mailboxes/time-as-finality/20260803-gu-records-de-anchor-coordination-proposal.md`.

**P-C3 final accounting (2026-08-03, G4 close-out; all edits in e53e8ae):**

*Six HONEST REDs (each cert now exits 1 because its printed claim fails
when asserted; findings, not failures):*
1. `tests/physics-ai-bridge/attention_directionality_winding.py` — symmetric-kernel winding is −2, not the claimed 0.
2. `tests/shiab_selector_sp64.py` — "NOT Sp(64)-equivariant" rests on an identically-zero witness.
3. `tests/rs_ghost_spin95_connection_bv_bicomplex.py` — 4 claims fail (Noether residual 8.08e-2; s² anticommutator 2.61e3 under a ‖M_KT‖≈2.4e9 random-holonomy connection; KT-exactness 1.67e-5; vacuous non-equivariance probe).
4. `tests/gu-independent/nongu_source_action_chiral_count.py` — "48/48/48/48 vectorlike quadrant base" observed (0,0,0,0); ‖[Kr,Gc]‖=28 ⇒ the joint diagonalization behind the 48-count is invalid. Other 7 checks pass.
5. `tests/gu-independent/verify_structural_crux_independent.py` — "only su(2)₊ preserves the carrier" is backwards: ASD generators preserve (~6e-15), all three SD generators leak 0.5. The file's own boolean already printed False against its prose.
6. `tests/hessian-z3/robustness_and_mechanism.py` — "equal-and-opposite half shifts" observed machine-zero both halves (ratio 0.24); superseded by its sibling's docstring, never corrected. Discrimination claim (1) holds.

*Three pinned ESCAPE-FOUND verdicts (exit 0 — the certs' own criteria
refute the frame-triviality no-go they probe):*
- `adv_verify_escape_hunt.py` (802 hits; the ±192 hits are the trivial involution whose frame charge comes from the carrier projector itself — the escape criterion may need tightening; campaign-level question).
- `escape_search_chirality_odd_frame.py` (frame-sourced count 54.58, 25072/50000 samples).
- `structural_frame_triviality_metatheorem.py` (frame-sourced count 32; concurrent-edit conflict resolved to pin-EVADABLE per the honesty rule — the alternative assert-the-no-go/honest-RED convention for all three search certs is a one-block change each, ADJUDICATION OPEN).
TRIAGE PRIORITY: check owner surfaces citing these three as no-go support — if any surface states the frame-triviality no-go as certified, it now contradicts its own artifact.

*Harness timeout list (solo runtimes):* `escape_search_chirality_odd_frame` ~1132s — **exceeds even CI's 900s**; `structural_frame_triviality_metatheorem` ~600–763s; `adv_verify_escape_hunt` ~556–652s; `rs_ghost_stueckelberg_compensator` ~479s; `rs_ghost_spin95_connection_bv_bicomplex` ~451s; `robustness_and_mechanism` ~207s; `verify_sw_carrier_mass_independent` ~240s. CI runs `--quick --tracked-only --timeout 900`; verify whether the >900s cert is inside the quick set before relying on CI green.

*Label defects to reword (small-fix tail):* one-sided σ_trap "decoupled" line in 4 files (asserts only the escape-block zero, not the commutator); Stueckelberg antighost-exactness line computes with M_eff not M_D; escape_class_check "[B] rank-deficient" parenthetical contradicted by computed full rank 192/192.

---

## Revision 3 (2026-08-03, Resolver Wave A)

Source: `explorations/cycle-gates-and-audits/resolver-wave-a-rebase-2026-08-03.md`.
No scientific register row or protected verdict moves.

- **M-M29 / Wave A-3: EXECUTED at `b327ad6`.** W224 was absorbed as the
  conditional singlet-isotropy result; the actual induced action on the rolling
  mode remains unbuilt. `N=e^{4p}` is retained as an exact reparameterization,
  not a generation/count datum.
- **M-H4 rider:** Wave A-1 closes only the canonical `J`-fixed `O(p,q)` sign
  route: that fixed real form is symplectic. The actual stabilizer commutant and
  global signature selection remain open. `PH-K1-KINEMATIC` is confirmed for
  imposter Reading A; `PH-K1-PHYSICAL` remains open.
- **M-H13 rider corrected:** DE-12 is in-sample consistency, not C10
  certification. Corrected proxy searches reproduce the `19.346` gap and find
  monotone and `N^p` realizers. The native record law and W230-to-FLRW
  coefficient map remain unbuilt; no M-H13 no-go or promotion is licensed.
- **Next named gate:** `RESOLVER-WAVE-B`, targeting Q3, DQ3, DQ1 typing, and
  M-M28 fence absorption. A2 cosmology proceeds independently and does not block
  those representation/operator targets.

---

## Revision 4 (2026-08-03, Resolver Wave B)

Source: `explorations/cycle-gates-and-audits/resolver-wave-b-disposition-2026-08-03.md`.
No scientific register row or protected verdict moves.

- **Q3:** the internal `P_hinge` range has exact first-order quotient leakage
  under the raw projected RS symbol in every coordinate direction. This kills
  only invariant-block / sole-leading-II mediation at finite kinematic grade;
  coupled, compressed, BV/physical, ellipticity, and domain routes remain open.
- **DQ3:** the phased `(9,5)` and `(7,7)` beta involutions, metric adjoint, and
  `Gamma Gamma-sharp=14I` give exact signature-free neutrality `(832,832)` on
  raw `ker Gamma`; no physical-chirality or positivity inference follows.
- **DQ1:** exact B4×B2 dimensions give `2U+2X+2Y`; standard compact-Clifford
  reality plus the K-invariant nondegenerate cross-pairing gives three shared
  quaternionic types and residual dimension 12 on this carrier. The actual
  dynamical stabilizer and physical quotient remain open.
- **Next named gate:** `RESOLVER-WAVE-C-REBASED`. Q5/Q6 compute only
  representation-channel availability; occurrence of 126 is not a coupling,
  mediator, mass, or A/B adjudication. Retain the full
  bilinear→Krein→reality→VEV→induced-4D-mass checklist.

---

## Revision 5 (2026-08-03, Resolver Wave C rebased)

Sources:
`explorations/cycle-gates-and-audits/resolver-wave-c-rebased-disposition-2026-08-03.md`
and `lab/process/hostile-reviews/2026-08-03-resolver-wave-c-review.md`.
No scientific register row or protected verdict moves.

- **Q5:** the bare same-label `16+ tensor 144+` contains no 126. Conditional
  on a complex-linear internal operator, the dualized
  `Hom(16+,144+)` Spin(10) factor contains one 126 also occurring in the
  spinor bilinear. The physical Krein/C-real pairing, Spin(4), full-20,
  one-form, and `ad(P)` types remain unbuilt. Weinstein's named passages are
  source-silent on the Hom/126 relation.
- **Q6:** internal `Lambda5(V10)` gives one real 252 with conjugate complex 126
  halves and exact Pati--Salam support for a right-neutrino bilinear and dual
  field. Existing W192/W194 typing obstructs the raw real
  `Lambda5 subset ad(P)` shortcut: the former is K-self-adjoint while an `Sp`
  connection generator must be K-anti-self-adjoint. Phased/reality-completed,
  covector-plus-even-generator, and inhomogeneous/soldering constructions stay
  open. No VEV or mass is built.
- **M-H7:** only the abstract coefficient facts are exact:
  `pi13S=Z/3`, `ImJ13=0`, `Omega13Spin=0`. The candidate radial boundary,
  compactness, normal-bundle triviality, stable framing, and nonzero PT class
  are open. The zero control applies to the external-product stable framing
  with closed stably framed X; non-product framings remain open. This does not
  supersede the existing degree-three spine/J route.
- **Next named gate:** `RESOLVER-WAVE-D-NATIVE-126-CONNECTION-PLACEMENT`.
  Derive the physical pairing first, classify admissible effective connection
  kernels, and test full-20 provenance, observer descent, right-H, Krein,
  C-reality, and source ownership. The independent topology successor is the
  normal-bundle/radial-boundary/framing/clutching construction, not another
  coefficient-table pass.

---

## Revision 6 (2026-08-03, Resolver Wave D)

Sources:
`explorations/cycle-gates-and-audits/resolver-wave-d-native-126-disposition-2026-08-03.md`
and `lab/process/hostile-reviews/2026-08-03-resolver-wave-d-review.md`.
No scientific register row or protected verdict moves.

- The raw-Lambda5 carrier gap is narrowed constructively. Native grade-six
  connection coefficients are K-anti/right-H, and the canonical contraction
  `V10* tensor Lambda6(V10*) -> Lambda5(V10*)` is surjective onto one real 252 with
  conjugate complex 126 halves.
- Full Spin covariance locks an internal five-form's horizontal and vertical
  contributions as `4+5=9`. A vertical-only coefficient is stabilizer-local;
  moving full-Sp descent remains open.
- Bare K and both C spinor factors admit grade five, but live provenance
  controls reverse the result. The complete ordered `P0/rho/Y_K/Y_C` kernel
  remains the physical object.
- For the planted five-form representative, a distinct one-form-output map
  has one desired 144 component per source plus paired `imGamma16` and
  `kerGamma16` companions. It is not a pure 144 map or the source packet's
  written `c_rho:S->S`; `P_R` retains the low-`R` 16, and a naive
  componentwise lift leaks between imGamma and kerGamma. Source-derived
  placement and treatment of the companions are the next construction.
- **Next named gate:**
  `RESOLVER-WAVE-E-SOURCE-OWNED-MOVING-252-FULL20-PLACEMENT`. Vary the actual
  equivariant source one-form, dress the split/grade by moving soldering,
  construct the full-20 reciprocal K/C blocks and P0/Y ordering, and require a
  nonzero Euler coefficient plus Ward identity before any VEV or mass claim.

**Baseline-sweep triage note (2026-08-03, P-H6):** the detached 783-cert
sweep completed VERDICT RED, 24 non-pass. It STRADDLED the e53e8ae campaign
edits mid-run, so it is a triage input, NOT the P-H6 dated receipt; a fresh
clean sweep is deferred until the resolver wave sequence pauses. Triage
classes: (a) the six intentional honest REDs (by design, exit 1); (b) W242
Q5 = stale process coupling (cert asserts NEXT-STEPS still names W242 as
the active hourly queue — superseded; NOT a DESI data event; the real FC-d
tripwire is clock-gated, margin +0.032, untouched); (c) environmental —
carrier-bit-decision PDF-extraction legs (gitignored PDFs); (d) process/
recovery-contract certs asserting queue states; (e) pre-existing physics
REDs predating the campaign: W178, W189, anchor-scale leg1_crosscheck,
big-swing cg_r1/cg_r3, escape-corners cluster (lega1/lega2/legb1/referee
legs), cycle1/cycle2 audit errors, channel-swings uniformity_execution
probe. None introduced by the campaign; (e) items are the standing triage
backlog.

---

## Revision 7 (2026-08-03, Resolver Wave E)

Sources:
`explorations/cycle-gates-and-audits/resolver-wave-e-source-owned-moving-252-full20-disposition-2026-08-03.md`
and `lab/process/hostile-reviews/2026-08-03-resolver-wave-e-review.md`.
No scientific register row or protected verdict moves.

- The actual full-14 direct contraction is now explicit: an internal
  five-form receives four horizontal and five vertical preimages, so
  `delta j5=9I`. The old vertical `5I` result is retained only as an
  observer-stabilizer comparator.
- For one unit simple blade the full-20 horizontal/vertical family has
  rationally reconstructed native support polynomials. The unweighted
  reconstruction keeps one low-`R` 16 plus one X/144 per source. The
  representative's unique clean value `lambda=1/2` removes the low-`R` copy
  and retains rank 128, but every `B_lambda` map is `SOURCE-SILENT`; neither
  representation-wide extension nor source selection follows from fit.
- Diagonal direct-sum K/C reciprocals, right-`H`, coarse `P0` incidence, and
  the trivial-provenance reality restriction are executable. The coarse
  direct `S<->X` sandwich survives only `P0=1`; the full `G2/Y/P0` placement
  and general complex provenance real structure remain open.
- The displayed source bosonic kappa term and a conditional active `j5`
  restriction have exact signed exterior-adjoint and affine Ward/Green
  comparators. The public-source-to-active `(9,5)` port joining them is open;
  the moving Shiab, total fermion residual, N1 `J_D/J_F` bridge fork,
  stationary VEV, mass, quotient, domain, and no-leakage remain open.
- **Next named gate:**
  `RESOLVER-WAVE-F-ACTUAL-SOURCE-SHIAB-FERMION-EULER-WEIGHT-SELECTION`.
  Build the source-to-active real-form/Zorro port, then assemble the actual
  moving total Euler system and determine whether it selects `lambda=1/2`,
  retains the coupled unweighted branch, or kills the rectangular route.
  P1/P2/P3 remain unchanged and unused.

---

## Revision 8 (2026-08-03, Resolver Wave F)

Sources:
`explorations/cycle-gates-and-audits/resolver-wave-f-source-port-action-ownership-disposition-2026-08-03.md`
and `lab/process/hostile-reviews/2026-08-03-resolver-wave-f-review.md`.
No scientific register row or protected verdict moves.

- The fixed `4+10` exterior algebra supplies an exact rank-252 projector
  `Pext^0=j5(1/9)pi_V5 delta` once the input is already typed in
  `C* tensor Lambda6(C*)`; `delta j5=9I` forces the normalization. This does
  not construct `q6` from a generic native adjoint field, and full Krein
  self-adjointness of `Pext^0` is not independently certified.
- Constant signed-permutation fixtures verify a narrow two-leg transport,
  composition, one split-preserving commutant example, one split mover, and
  one infinitesimal projector-chain identity. They do not construct the
  actual tilted `epsilon_src` action, `Theta_Z` overlap descent, or global
  source-to-active port. The coarse `epsilon_plane` obstruction survives.
- The downstream real exterior Hom-space has dimension four after Hodge-star
  twists. `[a:b]` is only its star-even two-dimensional subansatz; the clean
  `[2:1]` result remains one-simple-blade and source-silent.
- The displayed kappa field registry contains no `[a:b]`, and its hostile
  collapsed quadratic `5a^2+4b^2` does not directly select the half-weight.
  Complete moving Shiab plus fermion selection is not evaluable. An isolated
  zero-jet multiplier can force the representative ratio, but coupled
  nonpropagation is open and the field is not source-derived or required.
- The `chi=0` side audit retains `e_hat_0` only as the zero of its supplied
  auxiliary KO family. It supplies no canonical physical basepoint, P3
  identification, or count.
- **Next named gate:**
  `RESOLVER-WAVE-G-Q6-NATIVE-SP-TILTED-SOURCE-PORT-AND-TRANSVERSE-EULER`.
  Construct the generic-adjoint `q6`, its density/Krein adjoint and native
  `Sp` tangency, then the actual tilted `epsilon_src/Theta_Z` transport before
  testing both active and transverse total Euler equations. P1/P2/P3 remain
  unchanged and unused.

---

## Revision 9 (2026-08-03, Resolver Wave G)

Sources:
`explorations/cycle-gates-and-audits/resolver-wave-g-q6-native-tilted-source-port-disposition-2026-08-03.md`
and `lab/process/hostile-reviews/2026-08-03-resolver-wave-g-review.md`.
No scientific register row or protected verdict moves.

- `q6` is no longer formula-only: the Clifford number-operator polynomial is
  exhaustively checked on all 16,384 blades and all 8,256 native adjoint
  blades. It fixes 3,003 grade-six blades and kills the other 5,253.
- The generic native one-form domain has dimension 115,584; `q6` has rank
  42,042 and kernel 73,542. Composing Wave F's now fixed-pairing-self-adjoint
  `Pext^0` gives rank 252 and kernel 115,332.
- Sage certifies that Spin equivariance alone admits five one-form maps: four
  grade-six amplitudes and one grade-ten near-miss. The selected map is
  characterized by coefficientwise grade-six identity plus cross-grade
  annihilation, not equivariance alone.
- A square-zero grade-three native K-anti/right-`H` mover gives an exact
  counterexample to frozen full-`Sp` equivariance. Conjugating the projector
  with the moving Clifford frame repairs covariance.
- Exact noncommuting rational first jets prove left tilted invariance, right
  `Ad(h^-1)` covariance of `T_omega`, the `tau` homomorphism, and semidirect
  associativity in a chosen `A0=0` local convention, with planted untilted
  and wrong-Maurer--Cartan failures. A separate `GL(2)` frame surrogate has
  the expected transformation law but is not a Clifford/`Theta_Z` frame and
  never enters a combined `Psrc(T_omega)` computation.
- The construction remains local and conditional. Public U-type to native
  `Sp` reduction, actual `Theta_Z` coindex/nonconstant overlap descent,
  global lift/Riesz, source variation domain, total active/transverse Euler,
  Ward/Green, domain, and no-leakage remain open.
- **Next named gate:**
  `RESOLVER-WAVE-H-PUBLIC-NATIVE-REDUCTION-THETA-Z-DESCENT-AND-TOTAL-EULER`.
  First instantiate the combined local `Psrc(T_omega)`, then construct or
  obstruct the actual bundle reduction and global moving port,
  then join it to the displayed first source action and derive both Euler
  sectors. P1/P2/P3 remain unchanged and unused.

---

## Revision 10 (2026-08-03, Resolver Wave H)

Sources:
`explorations/cycle-gates-and-audits/resolver-wave-h-public-native-combined-port-disposition-2026-08-03.md`
and `lab/process/hostile-reviews/2026-08-03-resolver-wave-h-review.md`.
No scientific register row or protected verdict moves.

- The repo's previously unpromoted right-`H` averaging involution is now a
  chosen local map `P_J:u(K)->sp(K,J)` on an explicitly phase-typed real
  public carrier. `J_red` is an extra local `U/Sp`-type reduction field with
  source-silent ownership, not a source-owned or bundle-level reduction. Exact
  dimensions are `16384=8256+8128`; the one-form dimensions are
  `229376 -> 115584`.
- The whole chosen-`J`, `q6`, `Pext`, and Chevalley-reincluded source map is
  instantiated. It has rank 252 and kernel 229124, is idempotent and locally
  trace-self-adjoint, and kills both the imaginary public complement and the
  native grade-ten near-miss.
- The same composite now receives an exact `T_omega` first jet. It is left
  tilted basic and right adjoint-covariant conditional on a stipulated paired
  Clifford-frame law, including a public K-unitary mover outside native `Sp`.
  Freezing `J`/the frame fails; moving `J` repairs covariance into the moved
  codomain `sp(K,J_h)`, not one fixed native group.
- `R_J` is not a Lie-algebra homomorphism: two projected-away public coset
  generators have a nonzero native commutator. Therefore the map may project
  tensorial `T_omega` but cannot silently project a connection or curvature;
  coset action/Euler ownership remains required.
- Exact symbolic differentiation verifies the moving-projector formula and
  differentiated idempotence. A live auxiliary quadratic projector-chain
  term has derivative `-4`; this is not a variation of the displayed source
  action, an Euler covector, or a global Euler result.
- Three hostile lenses required and verified repairs to public-carrier typing,
  chosen-`J` ownership, numeric `(K,J)` controls, local adjoint decomposition,
  tilted/frame scope, and source-action wording. The repaired probe passes
  `79/79` checks.
- **Next named gate:**
  `RESOLVER-WAVE-I-ACTUAL-METX-ZORRO-THETA-DESCENT`. Build integrable
  nonconstant base-coordinate changes, their `Sym2` metric-fibre transitions,
  the connection-dependent horizontal/contact coframe, trace-reversed metric
  naturality, and the Spin/J/source/Psrc triple cocycle before total
  Euler/Green/domain work. P1/P2/P3 remain unchanged and unused.

**TaF response absorbed (2026-08-03, two-sided-reviewed PASS-WITH-CORRECTIONS):**
T1 (the W237 record-vs-redundancy bit): OPEN as the binary, ASYMMETRIC —
redundancy pole inadmissible as record content at TaF grade (Q1A
bookkeeping_only + executable witness); conserved pole conditional (H7
weakened_conditional; T110 obstructs strict SCALAR finality monotones in
closed reversible systems); TaF's native record object is a third,
graded/observer-indexed construction. W237's verdict table now carries
this as an EXTERNAL DATUM with provenance; the coupling leans toward the
no-compactification/chirality-kept row but the fork may NOT be collapsed;
settling object = a declared GU-record→TaF bridge map (new joint item).
T2 (N normalization): qualitative half TYPED — N(z) in any M-H13 refit
must be the confirmed/frontier-side count, and must be typed per-observer
or regional-reconciling (the single global scalar ledger is TaF's refuted
shape; FLRW-homogeneity coincidence must be stated as a condition, not
assumed); quantitative half OPEN — no earned TaF surface for any area-law/
exponent-1/2/π√N relation; W185's magnitude remains a GU-side import
(A7 halved: qualitative choice typed, quantitative form free).

---

## Revision 11 (2026-08-03, Resolver Wave I)

Sources:
`explorations/cycle-gates-and-audits/resolver-wave-i-actual-metx-zorro-theta-descent-disposition-2026-08-03.md`
and `lab/process/hostile-reviews/2026-08-03-resolver-wave-i-review.md`.
No scientific register row or protected verdict moves.

- A local nonlinear three-chart `Met(X)` fixture now has exact inverses,
  full 14-dimensional first-jet composition, nonzero Hessians, transformed
  Levi-Civita connections, and `Theta_recon DPhi=L Theta_recon` on `01`,
  `12`, `02`, and the triple.
- Exact trace reversal changes vertical `(7,3)` to `(6,4)` and gives the
  chosen Wave-H total `(9,5)` branch. The live rival `(7,7)` branch remains
  untested and not killed.
- A pointwise arbitrary-fibre adapted frame and coherent Spin lift pass. The
  negative triple sign is a planted inconsistent lift, not a global `w2`
  result.
- Hostile review found a real raw-covector/raised-vector error. A rational
  Lorentz boost exposes `O != O^-T`; raw `C*` now uses `O^-T`, while the
  inherited projector uses Riesz-raised `C`. The repaired map is
  `Psrc_raw=flat_eta Psrc_raised sharp_eta`, and the old vector law fails.
- All 252 selected image basis vectors and representative kernel sectors
  intertwine. The previously constructed `T_omega` remains raw, is raised
  only at the port, and is not retyped into a new source.
- Three hostile lenses returned final `PASS` after repairs. The probe passes
  `43 exact + 1 numeric + 7 source + 13 type + 13 planted = 77`.
- **Next named gate:**
  `RESOLVER-WAVE-J-DESCENDED-SOURCE-ACTION-TOTAL-EULER-AND-WARD`. Write and
  vary the actual source action on the reconstructed local carrier, including
  moving Theta/J/Psrc/connection/density/spinor terms, then test Euler
  tangency, Ward/Green/BV data, a common domain, and no-leakage. External-
  ledger P1/P2/P3 remain unchanged and unused.

---

## Revision 12 (2026-08-03, Resolver Wave J)

Sources:
`explorations/cycle-gates-and-audits/resolver-wave-j-descended-source-action-total-euler-ward-disposition-2026-08-03.md`
and `lab/process/hostile-reviews/2026-08-03-resolver-wave-j-review.md`.
No scientific register row or protected verdict moves.

- A pointwise already-composed source-shaped scalar-density fixture obeys
  Wave I's exact three-chart/Jacobian transport. It is not the displayed
  `I_B^1` and does not construct the native `Omega2 -> Omega13` Shiab.
- Exact cyclic noncommutative differentiation verifies the source
  `1/2,1/3` coefficient arithmetic and independence of the linear/quadratic
  channels. It is a transgression comparator, not the native B1 Euler map.
- Separate finite fixtures expose a live Green boundary and the necessity of
  the inhomogeneous `d xi` gauge response. They are not B1's preboundary,
  native Ward identity, or common domain.
- The exact public-coset pair `i e0`, `i e45678` projects individually to
  zero but returns native curvature `-2 e045678`. This kills the naive
  `F_(R_J A)` shortcut unless `R_J(m wedge m)` is retained.
- Hostile review caught a Layer-0/type failure: isolated coindex components
  of one `Psrc`-fixed one-form were not themselves projector-fixed. Claims of
  image bracket nonclosure, bosonic tangency failure, and selected
  post-variation projection were retracted. The live quadratic coefficient
  is `Omega2`, while `Psrc` acts on `Omega1`.
- Corrected reduced `(a,m)` and full-public/projected-residual constructions
  both remain open. Native Shiab, monolithic B1, degree-correct port order,
  bosonic/total tangency, native Ward/Green/domain, typed fermion residual,
  and no-leakage remain open.
- **Next named gate:**
  `RESOLVER-WAVE-K-NATIVE-SHIAB-MONOLITHIC-B1-VARIATION-AND-PORT-PLACEMENT`.
  Construct and vary the actual bosonic map before adding a typed fermion
  residual. P1/P2/P3 remain unchanged and unused.

---

## Revision 13 (2026-08-04, Resolver Wave K)

Sources:
`explorations/cycle-gates-and-audits/resolver-wave-k-conditional-active-shiab-b1-variation-disposition-2026-08-04.md`
and `lab/process/hostile-reviews/2026-08-04-resolver-wave-k-review.md`.
No scientific register row or protected verdict moves.

- Curt/Eric's `(7,7)` is no longer called an unexplained rival. Exact inertia
  arithmetic gives raw vertical `(7,3)`, trace-reversed vertical `(6,4)`, and
  source `(1,3)+(6,4)=(7,7)`. The active `(9,5)` route used `(3,1)`; `H*`
  does not flip inertia. The different real Clifford/spinor types make this a
  matter-carrier fork, not notation.
- The raw displayed Shiab word is not automatically in Wave H's typed
  public-`u(K)` domain. `R_J` rejects it; the exercised active grade
  projection is repository-derived and carries no source-port attribution.
- Hostile review replaced an arbitrary `e8` selector with the normalized
  DeWitt trace `e10`. The repaired monolithic B1 candidate retains independent
  curvature, covariant-derivative, `q_wedge`, and mass channels; direct and
  owner first variations agree exactly.
- The fixed candidate differs from the repository translated-curvature
  comparator by `-x^2+3*x*y^2/2+3*x*y/2-5*x/4+3*y/2-1/4`. The source equation
  is not killed: its `[T,T]` normalization relative to `T wedge T` is open.
- Ward and port claims were narrowed to one nonvacuous owner-cancellation
  witness and one fixed-background Hodge-conjugation fixture. The Green
  channel remains zeroth-order with zero boundary.
- Primary sources put matter in chimeric spinors and explicitly propose
  fundamental nonchirality plus VEV/curvature-controlled effective Weyl
  sectors. The next burden is an atomic particle crosswalk, not a coarse
  “Standard Model” row.
- **Ordered next gates:** K77-A real spinors/observation branching/atomic
  crosswalk; K77-B bracket-normalized source Shiab/B1; K77-C effective-
  chirality and hidden-parity dynamics; then a comparative K95 audit.
  P1/P2/P3 remain unchanged and unused.

---

## Revision 14 (2026-08-04, Resolver Wave K77-A)

Sources:
`explorations/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md`
and `lab/process/hostile-reviews/2026-08-04-resolver-wave-k77a-review.md`.
No scientific register row or protected verdict moves.

- Atomic rows now separate program-mandatory empirical targets, SM-shadow
  requirements, and source-lane obligations from the candidate mechanism's
  moving evidence grade. Killing a fixture, map, or mechanism emits
  reconstruction debt; it does not delete a required target within its scope.
- Negative results use an ordered scope ladder: fixture, candidate map,
  mechanism (including `LOCAL_PASS__JOINT_FAIL`), lane, then full conditional
  program. Lane and program kills require explicit mechanism/route exhaustion
  and the latter requires Layer 0 plus the full seven-axis protocol.
- The crosswalk has four linked surfaces: atomic target ledger, Eric/Curt
  source-claim registry, typed mechanism registry, and cross-row coherence
  matrix. Sources are navigation directives graded independently from the
  mathematics.
- The real `(7,7)` matter carrier now has exact four-block observation
  branching, invariant pairings, and K77 gamma image/kernel dimensions. The
  one-family charge packet is imported from the independently verified
  internal D5/Pati--Salam chain. F/Q/Z remain source branch arithmetic until
  actual K77 invariant subspaces/projectors are built. None are physical poles
  or a selected vacuum.
- Bare operator incidence and physical Krein-bilinear incidence are recorded
  separately. A vertical coefficient has the desired cross-Weyl/
  ambient-preserving incidence but remains unselected.
- The `F/Q/Z -> three generations` inference is killed at Layer 0 while the
  mandatory three-family target and unspent P3 datum remain live.
- A stale PC1 construction is fenced: left Clifford multiplication is not the
  natural exterior Spin action. The corrected derivation remains authoritative.
- Hostile review also fenced fixed-`c(v)` as a non-equivariant half-spin map
  and the stale `R128 -> C64 -> Weyl C32` story. Exact rank claims now use
  projector/intertwiner/inverse identities rather than floating SVD.
- The executable inventory audit corrected the stale channel-swings manifest
  count from 161 to the actual post-K77-A count of 160.
- **Next named gate:**
  `RESOLVER-WAVE-K77B-SOURCE-BRACKET-NORMALIZATION-DISPLAYED-SHIAB-AND-B1-VARIATION`.
  P1/P2/P3 remain unchanged and unused.

---

## Revision 15 (2026-08-04, Resolver Wave K77-B)

Sources:
`explorations/resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation-2026-08-04.md`
and `lab/process/hostile-reviews/2026-08-04-resolver-wave-k77b-review.md`.
No scientific register row or protected verdict moves.

- A primary-source internal collision closes the quadratic convention:
  equation (12.4)'s `T wedge T` fixes equation (9.4)'s bracket notation to one
  half of the graded self-bracket. Future waves may not reopen the old factor
  without a new source or mathematical contradiction.
- Layer 0 now separates connection difference, ordinary spacetime torsion,
  B1 top-form density, ambient translation Euler covector, and observed
  four-dimensional equation.
- The literal associative-product reading of the displayed Shiab fails its
  real-adjoint codomain on exact K77 fixtures. This is a candidate-map kill,
  not a theory or lane verdict.
- All eight source-inspired low-grade commutator/`i`-symmetric product
  channels are ad-closed. Six are nonvacuous and fail the same-action endpoint
  bank; the remaining two are zero/zero and receive no promotion.
- Sage D7 character arithmetic finds two invariant Phi1 and two Phi2 copies,
  exposing a four-coordinate low/high-grade family. The next gate applies the
  algebraic-curvature/Bianchi and transgression/Helmholtz selectors before
  adding derivative/Green ownership.
- K77-C effective chirality and the 37 atomic targets do not advance until a
  common bosonic action candidate exists. P1/P2/P3 remain unchanged and
  unused.

**DC-H2 result (2026-08-04) — H2 DEAD, blocker STRENGTHENED:** reciprocity
cannot fix Z_U's (c_b : c_f) ratio, and the reason excludes a whole class:
self-adjointness of the source pairing is exactly invariant under the
blockwise congruence group whose orbits ARE the block ratios (verified
exactly; the congruence moves c_f/c_b from 1 to 25/36). The sharp version
is circular — (c_b : c_f) IS the gimmel metric's horizontal:vertical
scale, so stating a constraining reciprocity condition presupposes it.
CONSEQUENCE: any condition invariant under blockwise congruence (every
symmetry-of-pairing / self-adjointness demand) is scale-blind, and A4
needs a scale. M-H13 item (a) does not move. THREE BY-PRODUCTS: (1) exact
nullities 1/2/3 for so(9,5) / so(3,1)+so(6,4) / so(3)+so(6,4) — the three
A4 coefficients are precisely the residual symmetry's invariants; (2) the
residue REDUCES from three coefficients to ONE dimensionful scale, whose
only in-repo value is canon's R_s = c/H_0 import — H44's equation is the
choice (c_b : c_f) = 1:1 PLUS that import (exact demo: l = R_s, 2R_s,
R_s/2 -> M^2 = 8, 2, 32 continuously, which also excludes outcome (b));
(3) a FORK that cannot be double-banked — full so(9,5) equivariance WOULD
fix the ratio uniquely, but it forces L proportional to M, landing in
W230 [NEC]'s escape variety and destroying W230's necessity leg (the
theta = J <=> c_kin = 0 equivalence the A4 COMPLETED-POSIT rests on).
NEW VERIFIED_REPO_DISCONNECT: W230 calls W180's Frobenius Gram "the fixed
equivariant ultralocal Krein kernel"; W203 KER4 proves it is not
(3 of 13 generators violate it, reproduced). Does not change W230's [NEC]
conclusion; logged for repair, not repaired.

---

## Revision 16 (2026-08-04, Resolver Wave K77-B2)

Sources:
`explorations/resolver-wave-k77b2-shiab-family-curvature-selector-transgression-2026-08-04.md`
and `lab/process/hostile-reviews/2026-08-04-resolver-wave-k77b2-review.md`.
No scientific register row or protected verdict moves.

- The algebraic Riemann module is now explicitly the rank-3,185 first-Bianchi
  kernel inside rank-4,186 pair-symmetric curvature and is injected pointwise
  in a fixed frame into the rank-1,490,944 ambient real-adjoint spin-curvature
  domain. Associated-bundle/soldering descent remains open. It is not the
  whole source curvature space.
- Exact complexified D7 arithmetic gives `3185=1+104+3080` and target
  multiplicities `2,2,0`. Weyl-killing is automatic for an equivariant zero-
  order map on this submodule and cannot be used as the missing selector.
- The complete K77-B source-inspired low/high factorized repair family reduces
  to lifted features `(a,b,ac,ad,bc,bd)`. Only two product patterns meet the ambient
  fourteen-dimensional Einstein ratio; exact same-action transgression
  witnesses force both to the zero map.
- The kill is scoped to the displayed ansatz under the joint ambient-Einstein/
  same-action reading. Observed four-dimensional and Frobenius-fibre trace
  maps, the broader bounded grammar, and the K77 lane remain live.
- Explicit low/high maps construct a two-coordinate ambient-Einstein
  restriction exactly on algebraic Riemann curvature at pointwise fixed-frame
  grade. The next construction must first find a source-natural full-domain
  extension, then test cyclic/Helmholtz existence and differential Green data;
  it is not a return to the dead raw printed endpoint.
- **Next named gate:**
  `RESOLVER-WAVE-K77-B3-FULL-DOMAIN-EXTENSION-CYCLIC-EULER-EXISTENCE-AND-GREEN`.
  K77-C and all atomic physics rows remain blocked; P1/P2/P3 remain unchanged
  and unused.

**DC-H1 result (2026-08-04) — (c) PARTIAL, ledger UNCHANGED, one retyping
and one new question.** Path-type YES: the DeWitt metric-fibre loop is
shown exactly to generate pi_1(F) = Z/2 (its GL(4,R) lift ends at
diag(-1,1,1,-1), the PT / non-orthochronous component; an independently
built Gaussian-integer Cl(9,5) gives chi(loop) = -1, chi(loop^2) = +1,
reproducing the published central -1 without importing it). So the
orientation datum is a Z/2 LOCAL SYSTEM with computed nonzero holonomy,
not a value awaiting supply. Framing-type NO — the kill: chi is QUADRATIC
in the Clifford lift, so it descends to SO and cannot see the double
cover (the genuine deck element has chi(-I) = +1; chi(T) = chi(-T) on 40
lifts; chi invariant under arbitrary retrivialization, defect 5.6e-15),
hence the [L^13, SO] reframing freedom acts through the ZERO
homomorphism, and the loop's own lift has T^2 = +I so the double cover is
not merely invisible but NOT ENGAGED. LAYER-0: exhaustively over the 16
diagonal elements of O(3,1), chi is exactly the ORTHOCHRONOUS
(time-orientation) character — a REFLECTION Z/2, not a double-cover Z/2.
Same group order, different mechanism: HOMONYM. The netcode
quaternion-double-cover rhyme does NOT transfer, exactly as the
hypothesis note's weakest-evidence-class warning anticipated. LEDGER: D1
(one Z/2 orientation, P1+P2) and D2 (P3) unchanged; nothing derived,
nothing leaves. PROCESS FINDING: the preregistered binary was
UNDER-SPECIFIED — (a)'s consequent fails and (b)'s "stays value-type" is
also wrong; the split was reported rather than forced to a nearest match.
CHEAPEST NEW QUESTION: if the orbit-sign Z/2 IS the time-orientation
character, the datum's natural home is a TIME-ORIENTATION OF THE
LORENTZIAN BASE, not a boundary framing — never asked in that form.
Scope caveat: the loop lives in the metric fibre F; transfer to L^13 is
hostage to M-H7 gaps O2/O3 (the framing negative is robust either way).

**TIME-ORIENTATION HOME (2026-08-04) — the DC-H1 follow-on, and the
strongest external-datum result of the campaign.** CARRIER: the datum is a
time-orientation of the tautological timelike LINE of X^4 — not of F, not
of Y^14. Exact and Clifford-free at its core: the DeWitt loop is a path of
Lorentzian metrics on ONE fixed tangent space with h_1 = h_0 but
v_1 = -v_0 — the SAME metric returned with future and past cones
EXCHANGED. On the Clifford side chi factors over the fourteen gimmel legs
as chi = chi_base * chi_fibre with chi_fibre == +1 EXHAUSTIVELY over
O(3,1) (all four pi_0 components), for an exhibited reason: the only
flippable fibre legs are the three purely spatial off-diagonals, flipping
in count k(3-k) in {0,2,2,0}, always even — specific to THREE spatial
dimensions. STRUCTURAL CONSEQUENCE: the nontriviality is FIBREWISE (the
loop lies inside one fibre), so the class is NOT in the image of
H^1(X^4;Z/2) -> H^1(Y^14;Z/2), and **the tautological Lorentzian
structure on the observerse is NEVER time-orientable, for any X^4**.
FIXED-VS-PRESUPPOSED: all seven candidates PRESUPPOSE, none FIXES, under a
rule fixed before classification (W166's mode and the Friedmann first
equation are exactly T-EVEN — T exchanges growing and decaying branches,
so "N grows" names a branch, not a direction; record accretion and the
causal-order route are T-odd only by importing the past cone; the
indefinite-base requirement supplies O(3,1)'s four components, not the
orthochronous reduction, so it is the datum's PRECONDITION not its
supplier). A synthetic control classifies FIXES, so the empty result is
not vacuous. Independent of the candidate audit, a BASE-SIDE NO-GO closes
it: a base-side supply has the wrong shape to cancel a fibrewise
obstruction. LEDGER: unchanged in count, relocated and better typed — D1
is w_1 of the orientation cover of the timelike line over the metric
fibre; not a value, not a framing holonomy. BY-PRODUCTS: DC-H1's asserted
fibre signature (6,4) is now DERIVED (exact orthogonality, exact norms,
lambda > 1/4); a fourth homonym excluded (the induced 14-frame return has
det +1, so this is NOT Y^14's spacetime-orientation class). NEW LAYER-0
PAYLOAD: three pairwise-distinct characters — sigma_J(J_obs) = det
(spacetime orientation), sigma_K(K_S) = det*orth (space orientation, =
the spatial 3x3 determinant), chi(C_perp) = orth (time orientation), with
chi = sigma_K * sigma_J. CHEAPEST REOPENER, possible existing Layer-0
error: does CH-REC's eps attach to the LINEAR Krein involution or the
ANTILINEAR coflip? If the former, "the arrow is eps" welds the arrow to
the SPACE-orientation character and is wrong. JOINT ITEM: identifying this
Z/2 with TaF's finality direction needs a TaF-side statement of what that
direction is a direction OF; GU can now hand over three candidate
characters and an exhaustive pi_0 table to test against.

---

## Revision 17 (2026-08-04, post-K77-B2 council and eight-wave rendezvous)

Sources:
`explorations/k77-post-b2-science-council-next-eight-wave-rendezvous-2026-08-04.md`
and `lab/process/k77-post-b2-next-eight-wave-campaign.json`. No scientific
register row, protected verdict, lane, canon, public posture, or P1/P2/P3
status moves.

- The route remains worth pursuing, but the sequence is rebased. The real
  `(7,7)` K77 construction is primary and source-faithful; the active `(9,5)`
  right-`H` construction remains a formally distinct rival implementation and
  negative-test bank. Complexification is not permission to import real
  pairing, chirality, or right-`H` results across the fork.
- K77-B3 is the last isolated selector wave. It must either produce a descended
  full-domain cyclic/action member or bank an exact bounded zero-order no-go
  and return to derivative/moving-field geometry.
- The next three gates force a common source-action rendezvous, an action-owned
  current/Riesz and Noether/BV identity, and an observation/BFV groupoid with
  a typed receiving arrow for any external datum. D1 is treated as a lift of
  the timelike-line orientation cover, not a free scalar repair.
- Physics begins at Wave 4 with local Einstein, Dirac/RS, Maxwell/Yang--Mills,
  gauge-rotated contorsion, and trace-reversed Frobenius-fibre emission from the
  same frozen action. The 37-row atomic ledger is regraded then, rather than
  being reserved for final validation.
- A mandatory breadth reset follows Wave 4. Remaining waves construct the
  coupled Krein/Green/BFV domain, common Higgs/Yukawa/cosmological vacuum,
  physical fermion/chirality/anomaly/count coupling, and one frozen integrated
  held-out acceptance packet.
- Every wave retains lightweight divergent pre-assessment and two hostile
  post-review charges: find where the summary outruns the artifact, and find
  where rigor is defending a superseded object. ML remains optional search
  infrastructure; only exact reconstruction and held-out identities can admit
  a result.

---

## Revision 18 (2026-08-04, K77-B3 full-domain cyclic-kernel result)

Sources:
`explorations/resolver-wave-k77b3-full-domain-cyclic-kernel-obstruction-2026-08-04.md`,
`lab/process/resolver-wave-k77b3-full-domain-cyclic-kernel-obstruction.json`,
and `lab/process/hostile-reviews/2026-08-04-resolver-wave-k77b3-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, or
P1/P2/P3 status moves.

- Replace brute-force expression-DAG enumeration with representation-first
  exhaustion whenever the relevant full equivariant Hom can be computed.
  Here its complexified dimension is `200`, while the actionable grade-two
  low/high blocks each reduce to three explicit real contraction coordinates.
- A Riemann-only selector can pass its own restriction test while failing the
  written translation-field action. Exact low/high kernel witnesses show that
  every fixed-metric, fixed-epsilon, zero-order linear full-domain extension
  with the ambient fourteen-dimensional Einstein restriction fails the
  unit-weight cubic Euler identity unless both Einstein coefficients vanish.
- Record the result at mechanism scope. It does not kill K77, `(7,7)`, the
  fermion carrier, gravity, source actions generally, or physics. Green/domain
  is not reached because the algebraic survivor set is empty.
- The next common-action wave must compare four real rebuild mechanisms: the
  actual symmetrized Euler derivative, moving Shiab/epsilon/soldering/Hodge
  terms, an independent parent curvature/soldering field, and an
  action/BV-derived invariant restricted domain. External datum cannot repair
  a missing variational map.

---

## Revision 19 (2026-08-04, K77 Wave-2 action/even-Ward rendezvous)

Sources:
`explorations/k77-wave2-action-current-riesz-superig-ward-rendezvous-2026-08-04.md`,
`lab/process/k77-wave2-action-current-riesz-superig-ward-rendezvous.json`, and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-action-ward-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, or
P1/P2/P3 status moves.

- The source-guided primary action now emits the fermionic connection current
  once, through `delta_A S_20=J_D+J_F`, rather than inserting a second bridge
  made from the same derivative. The `J_D` and total-current bridge actions
  remain mathematically gauge-invariant negative-test comparators; source
  fidelity is not reported as uniqueness.
- After a full-domain Helmholtz failure, retain the written action and use its
  actual symmetrized Euler derivative. A moving Shiab response belongs to the
  epsilon equation and Ward identity; it cannot repair a translation
  derivative whose variation explicitly holds epsilon fixed.
- A regular parent-field rewrite is not a new mechanism: after auxiliary
  elimination it returns the same symmetrized Euler derivative. Count a parent
  as a reopener only when it supplies new nonregular geometry or constraints.
- The connection current map is an indefinite pointwise pseudo-musical. Never
  let the word Riesz import positivity, boundedness, a Hilbert completion, or a
  common domain.
- The mixed rolled symplectic moment-map bracket constructs only partial
  `TG-1`. Before any super-IG action claim, construct source-group projection,
  simultaneous Krein compatibility, field-versus-parameter identification,
  the full odd action, and odd Ward/BV closure. An even gauge Ward identity or
  `Xi=D Upsilon` cannot substitute for `TG-2/TG-3`.

---

## Revision 20 (2026-08-04, Dirac--de Rham/super-IG requirement correction)

Sources:
`explorations/k77-wave2-dirac-derham-superig-rebase-2026-08-04.md`,
`lab/process/k77-wave2-dirac-derham-superig-rebase.json`, and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-dirac-derham-superig-rebase-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, or
P1/P2/P3 status moves.

- Before declaring a Dirac operator absent, distinguish the ordinary
  Hodge--de Rham Dirac, a truncated form chain, its rolled two-by-two operator,
  a displayed source matrix, and an unreleased cyclic completion. Shared
  “Dirac/de Rham” language is not an identity receipt.
- A fibrewise zero-order contraction composed **after a differential** is a
  first-order operator. Do not let a component's standalone order erase the
  order of the composed middle map.
- For a rank computation over the rationals, a full-rank modular minor is a
  lower certificate. Pair it with an explicit complementary kernel or another
  upper bound before reporting exact deficient rank. Independent Sage replay
  is corroboration, not a substitute for that two-sided certificate.
- In an indefinite/nonchiral setting, failure of a bare middle block to be
  self-adjoint does not kill the fermion action. Test the cross-paired operator
  with its Krein adjoint. Keep that completion conditional until the source's
  actual block placement and global pairing are identified.
- A supersymmetry-like **algebraic extension** does not automatically demand
  an odd action symmetry. Source-check that requirement before spending waves
  on an odd Noether/BV identity. Preserve bracket, Jacobi, real-form, source-
  group, and global descent obligations even when the action demand is
  removed.
- Keep detailed secondary derivations such as Curt's 30-step iceberg as
  construction witnesses, primary author statements as source locators, and
  exact repo computations as a third grade. None may silently promote the
  others.

---

## Revision 21 (2026-08-04, draft-9.16 primalizer/template promotion repair)

Sources:
`explorations/k77-wave2-global-draft916-krein-preboundary-common-domain-2026-08-04.md`,
`lab/process/k77-wave2-global-draft916-krein-preboundary.json`, and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-global-draft916-krein-preboundary-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, family
count, or P1/P2/P3 status moves.

- An exact generic formal-adjoint theorem or finite overlap fixture is not an
  actual global operator assembly. Every result must say whether coefficients,
  form degrees, transitions, and the full displayed block matrix were really
  instantiated.
- When a source bilinear naturally types as `D:E->E!`, construct the
  density/Hodge/pairing primalizer `R:E!->E` before asking whether `R D` is
  Krein self-adjoint. In `(7,7)`, track the different Hodge-square signs on
  degrees `0/14` and `1/13`; never copy the inverse sign between them.
- A principal-symbol test must extract derivative coefficients from the
  computed operator. Comparing an expected expression to itself is a planted
  theater failure even if the formula on both sides is correct.
- Source bars and stars are adjoint-shaped ingredients, not an
  integration-by-parts theorem. Displayed `rho(epsilon)` factors are a
  covariance ansatz, not a global descent proof.
- Finite current, Ward, and K-skew comparators retain their value when labeled
  honestly. They do not recompute an actual moving action or establish
  form-degree/gauge-compatible southeast rivals.
- Type the gamma-trace decomposition as `Omega0`, a chosen splitting image
  `s_Gamma(im Gamma) subset Omega1`, and `ker Gamma subset Omega1`; the raw
  image of `Gamma:Omega1->Omega0` does not live in `Omega1`.
- Hostile post-review must compare the summary to the instantiated object
  before campaign advancement. Here all three reviewers caught the same
  compression error and reverted Wave 3 to Wave 2 partial.

---

## Revision 22 (2026-08-04, actual-carrier D916 rival and source-sign obstruction)

Sources:
`explorations/k77-wave2-actual-draft916-k77-blockwise-adjoint-descent-2026-08-04.md`,
`lab/process/k77-wave2-actual-draft916-blockwise-adjoint-descent.json`, and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-actual-draft916-blockwise-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, family
count, or P1/P2/P3 status moves.

- Reopen later source sections before assigning meanings to equation glyphs.
  Here equation 9.16 alone permitted a total-grading interpretation, while
  section 11.2 identity-grades the same `zeta+/-` and `nu+/-` glyphs as
  ambient half-spinors.  The construction survives only as an explicit rival.
- A decomposition that fits every matrix cell can still fail Layer 0.  Record
  which labels were relabeled and run the incidence/parity problem under the
  source's own typing before calling the fit source-native.
- A functional on a noncompact Lie algebra becomes an algebra element only
  after an invariant duality is supplied.  A same-basis coordinate sum is not
  the inverse trace metric; it can pass compact-looking directions and fail
  boosts.  Plant a noncompact equivariance test.
- A moving-frame conjugation test establishes naturality of the moving
  reduction, not equivariance under the full fixed source group.  Keep global
  reduction existence and full-group descent as separate obligations.
- One nonzero connection direction verifies current ownership and
  non-vacuity.  It is not the complete connection derivative, common-core
  Ward identity, or multi-index formal adjoint.

---

## Revision 23 (2026-08-04, source-sign branches converge on an odd-covector receiver)

Sources:
`explorations/k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md`,
`lab/process/k77-wave2-source-sign-shiab-duality-reconciliation.json`, and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-source-sign-shiab-duality-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, family
count, Wave-3 admission, or P1/P2/P3 status moves.

- A degree-dependent duality question must vary every map the phrase could
  name.  Varying only barred rows falsely killed this branch; adding the
  unbarred column reality maps produced two exact sign solutions.
- A sign-level SAT solution is not yet a natural bundle map.  Compute the
  relevant intertwiner Hom space.  Here `Hom_Spin(S+,S-)=0`, while supplying
  one vector gives a one-dimensional flip channel.
- For natural Clifford contractions, tensor-valence parity is a cheap analytic
  filter; corroborate the claimed exhaustive target with an independent
  character calculation.  The `D7` result is same-half Hom `0`, opposite-half
  Hom `2`.
- Conjugating an odd invariant tensor and chirality by the same moving field
  preserves their relative parity.  Do not count a gauge conjugator as the
  extra vector index needed to make an even map.
- A fixed odd covector can make a local formula fit while destroying
  covariance.  Move the tensor under transitions and plant the fixed version.
- Time orientation selects `q` versus `-q` only after a timelike line exists;
  it does not manufacture the line.  Treat the line/covector as a receiving
  type hypothesis, not as P1 consumption.
- Compute constraint surplus at the first successful fit.  The free-`q`
  principal-symbol repair has surplus `-14` here, so it is construction
  infrastructure whose evidence must come from later adjoint, Ward, current,
  and ownership constraints.
- Completed Runtime receipts are append-only evidence.  If a summary records
  a mistyped commit hash, document the actual revision in the successor review
  rather than rewriting the old receipt.

---

## Revision 24 (2026-08-04, trace-q ownership and Ward non-selection)

Sources:
`explorations/k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md`,
`lab/process/k77-wave2-q-receiver-trace-adjoint-ward-selection.json`, and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-q-receiver-trace-adjoint-ward-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, family
count, Wave-3 admission, or P1/P2/P3 status moves.

- Before pricing a newly required tensor as external datum, search earlier
  native geometry for a type-correct tautological section. Here the DeWitt
  trace line was already constructed before the later odd receiver appeared;
  connecting them removes thirteen free projective parameters.
- Distinguish a Clifford vector from its musically lowered covector. Shared
  coordinates do not repair a type mismatch, while a native nondegenerate
  chimeric metric does.
- A canonical line and a canonical signed section are different. The radial
  Euler section `t_g=g` fixes the sign on one fixed-signature metric component,
  so an orientation bit is not automatically consumed.
- Associated-family covariance may hold for every coefficient in a candidate
  span. In that case the Ward identity has selection rank zero even when
  other held-out currents have full sensitivity rank.
- Do not identify commutators or anticommutators across algebraic factors by
  name. The source coefficient-algebra magic bracket does not select the
  ordering of a Clifford receiver and a form-spinor contraction.
- If a check is labeled exact, avoid floating inversion, eigensolvers, and
  numerical rank when an integral frame, Sylvester minors, or a small exact
  determinant is available.
- A one-form coefficient response is not yet a connection current. Insert an
  actual Lie-algebra generator and state whether one direction or the whole
  current was computed.
- When a composite field supplies the needed object, pull its current back
  into the owner's Euler equation; do not add a second independent field and
  accidentally double-count variation directions.

---

## Revision 25 (2026-08-04, Curt zero-order port and reality non-selection)

Sources:
`explorations/k77-wave2-trace-q-coefficient-zero-order-reality-selection-2026-08-04.md`,
`lab/sources/curt-iceberg-fermion-zero-order-reinspection-2026-08-04.md`,
`lab/process/k77-wave2-trace-q-coefficient-zero-order-reality-selection.json`,
and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-trace-q-coefficient-zero-order-reality-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, family
count, Wave-3 admission, or P1/P2/P3 status moves.

- Pair explanatory secondary sources with later author corrections. Curt's
  Iceberg walk-through locates the zero-order connection term, while Eric's
  later response changes the action architecture from one layer to two.
- A source may identify a support slot without selecting its coefficient.
  Record placement rank and coefficient-selection rank separately.
- Do not impose a Majorana fixed locus merely because the ambient real
  Clifford module exists. The draft's barred/unbarred fields are independent,
  and the optional fixed-locus rival can be strictly more destructive.
- Factor-only adjoint intuition is not a substitute for the full form-index
  times spinor Krein adjoint. The latter can turn an apparent one-dimensional
  eigenspace into an empty projective family.
- Lower-order moving Hodge, density, pairing, or receiver terms cannot repair
  a principal-symbol reality failure, though they remain mandatory in any
  surviving variational action.
- Once isolated symmetry/reality selectors all have rank zero or kill the
  family, stop descending through more selectors. Carry the residual family
  into the smallest common action and let its coupled Euler equations spend
  the remaining freedom.

---

## Revision 26 (2026-08-04, two-layer norm-square versus square-root target)

Sources:
`explorations/k77-wave2-common-two-layer-action-euler-coefficient-selection-2026-08-04.md`,
`lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md`,
`lab/process/k77-wave2-common-two-layer-action-euler-coefficient-selection.json`,
and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-common-two-layer-action-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, family
count, Wave-3 admission, or P1/P2/P3 status moves.

- Run Layer 0 on the word “square.” A residual norm, an operator composition,
  a deformation-differential square, and amplitudes double copy are different
  objects even when one speaker moves between them in one explanation.
- A norm-square layer derived from `Upsilon` is structurally redundant on
  `Upsilon=0`. It cannot select a fixed coupling on that locus merely by
  adding more Euler equations; its derivative factors through `Upsilon`.
- Field equations depending on a coupling are not coupling-selection
  equations. Add a coefficient/modulus Euler row only after constructing its
  field-space owner, symmetry, action term, and datum invoice.
- A self-derived comparator cannot select itself. `D(c)^times D(c)` is a
  family indexed by `c`; it becomes a constraint only when compared with an
  independent target not defined using the same `c`.
- One exact evaluation can prove operator-tensor independence when its output
  vectors attain the maximum possible rank: evaluation cannot increase rank.
  State this lower-bound logic and keep domain/spectrum claims separate.
- A scalar middle symbol is a useful Laplace-type lead, not a Lichnerowicz
  theorem. Require the composed full operator, lower-order curvature, form
  indices, and target before promoting the coefficient.
- When a source names unfinished paths, turn the path diagram into the next
  construction. Do not paraphrase the named cancellation into whichever
  current left/right family happens to be available.

---

## Revision 27 (2026-08-04, two-connection target and cross-map typing)

Sources:
`explorations/k77-wave2-up-back-over-path-adapter-independent-square-root-target-2026-08-04.md`,
`lab/sources/gu-up-back-over-square-root-source-reinspection-2026-08-04.md`,
`lab/process/k77-wave2-up-back-over-path-adapter-independent-square-root-target.json`,
and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-up-back-over-target-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, family
count, Wave-3 admission, or P1/P2/P3 status moves.

- An unreleased spoken formula may bound a reconstruction without sourcing it.
  Attach the source caveat to every reuse and grade the derived algebra
  separately from the attribution.
- When a spoken sign pattern is ambiguous, use a noncommuting exact fixture.
  Here the two-minus placement is uniquely selected among all four choices;
  scalar fixtures would not discriminate the mixed-Bianchi structure.
- Type path-composition language with a block totalization before borrowing an
  available operator. Diagonal `VU/UV` and off-diagonal `DV+VF/UD+FU` require
  cross-carrier maps, not just coefficients of the diagonal operators.
- Full coefficient-column rank from any exact evaluation is a global kernel
  kill for that finite coefficient family. State it as a candidate-map kill,
  not a lane or mechanism kill.
- A candidate kill must emit a reconstruction debt at the same type. The
  failed trace-`q` shortcut emits `U:B->F` and `V:F->B`; it does not emit
  another request for an unspecified external datum.
- Existing cell-typing archaeology remains authoritative even after a fresh
  visual source pass. New synthesis should cite and extend it, not rediscover
  it as a novel result.

---

## Revision 28 (2026-08-04, raw mixed Hessians are not yet cross-carrier maps)

Sources:
`explorations/k77-wave2-stabilized-mixed-bose-fermi-cross-maps-target-match-2026-08-04.md`,
`lab/sources/gu-mixed-bose-fermi-cross-map-source-reinspection-2026-08-04.md`,
`lab/process/k77-wave2-stabilized-mixed-bose-fermi-cross-maps-target-match.json`,
and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-stabilized-mixed-cross-map-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- Read a diagram by node topology before importing a block-square grammar.
  Equation `10.10` is a rectangular deformation-to-Euler complex, not an
  endomorphism square on one Bose--Fermi carrier.
- A scalar common action owns both mixed Hessian directions without an
  independent bridge equation, but their native codomains are equation duals.
  Record `B->F!` and `F->B!` before any musical identification.
- In a Krein setting, dual-to-field maps are moving Hodge/pairing/density
  structures. Identity coordinates are not a source-selected primalizer.
- Mixed-Hessian reciprocity is a Helmholtz condition and may hold across an
  entire coefficient family. Sensitivity rank and coefficient-selection rank
  must be reported separately.
- Before comparing two block matrices entrywise, prove that their gradings
  name the same decomposition. Here the two-connection grading and the
  Bose--Fermi/Euler grading require a comparison functor.
- A frozen one-form witness can prove nonvacuity and exact coefficient rank; it
  cannot stand in for the moving sixteen-cell Hessian, associated-bundle
  descent, Green identity or physical source.
- When a Layer-0 correction blocks the requested numerical match, emit the
  missing typed adapter and rerun order, rather than reporting a numerical
  failure for a comparison that was never defined.

---

## Revision 29 (2026-08-04, source context can invalidate the comparison object)

Sources:
`explorations/k77-wave2-mixed-primalizers-two-connection-comparison-2026-08-04.md`,
`lab/sources/gu-primalizer-two-connection-comparison-source-reinspection-2026-08-04.md`,
`lab/process/k77-wave2-mixed-primalizers-two-connection-comparison.json`, and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-primalizer-comparison-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- Reinspect a spoken construction in its immediately preceding question and
  paragraph. A formula's local context can type it more strongly than a later
  thematic synthesis; here it corrected “bosonic target” to “unreleased
  fermion-cyclic completion or rival.”
- When source correction invalidates a planned test, discard the test as
  wrong-target work. Do not dignify its prospective output as a scoped kill.
- A density-valued Euler action can have canonical pseudo-musicals without an
  orientation choice. Separate absolute density from ordinary top-form Hodge
  notation before assigning an orientation datum.
- For a moving inverse, test `dR=-R(dK)R` and transition naturality. Pointwise
  inversion alone is insufficient evidence of an associated-bundle map.
- A two-by-two mnemonic gives at most one typed arrow until its source and
  target degrees are assigned. A cyclic square requires the reverse arrow and
  both composites; never infer them from the desired result.
- Compare rival block operators by both slot owner and differential order.
  Sharing one connection slot does not make a zero-order curvature block
  equivalent to a first-order Clifford derivative.
- Keep two hostile reviewers with opposite compression charges: one hunts
  summaries that outrun artifacts, and one hunts rigorous artifacts aimed at
  stale or superseded objects.

---

## Revision 30 (2026-08-04, a shifted operator and its action shell are separate builds)

Sources:
`explorations/k77-wave2-two-connection-shifted-superconnection-action-owner-2026-08-04.md`,
`lab/sources/gu-two-connection-shifted-superconnection-source-reinspection-2026-08-04.md`,
`lab/process/k77-wave2-two-connection-shifted-superconnection-action-owner.json`,
and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-two-connection-action-owner-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- Before searching for a reverse arrow, test whether an internal degree shift
  makes one total-odd operator own both parity restrictions.
- Square block operators in a noncommutative exterior DGA. A commuting scalar
  fixture can erase precisely the mixed curvature defect that distinguishes
  two connections.
- Ordinary Bianchi is connection-specific. Never replace
  `d_A F_B-F_B d_B` by zero without constructing a mixed transport law.
- Search the full repository before calling an action owner absent. Here the
  source-owned first-order action was already recorded; only its ownership of
  the later cyclic operator was absent.
- The `1/2,1/3` packet is connection-path-average curvature in the normalized
  wedge convention. Uniqueness from two constraints on two parameters has
  surplus zero, not positive surplus.
- `D^2=0`, `T=0`, `Upsilon=0` and `dI=0` are four different statements until
  Layer 0 supplies the maps between them.
- When an algebraic complex shell misses an action shell, emit the
  Euler-density-to-field primalizer and pair lift as the construction debt;
  an external datum cannot manufacture that map.

**Surface drift, PARTIALLY REPAIRED 2026-08-04 (P-L-class, new):**
`lab_process_readme_surface_map_audit.py` had two failing halves.
(1) FIXED: the directory half — `anchor-council-2026-08-03/`,
`hostile-reviews/`, `queue-reviews/` and `runs/` were live but undeclared;
gate constant and `lab/process/README.md` both updated, that half is green.
(2) OPEN, different owner: the file half still fails because the resolver
campaign writes its per-wave registry JSON directly into `lab/process/`
(k77-wave2-*.json, resolver-wave-k77b-*.json, k77-post-b2-*.json, and
growing one-per-wave). Listing each in the README is not the fix; the
options are a `lab/process/registries/` subdirectory or an explicit gate
exemption for machine-written registries. NOT repaired here because the
files are the active campaign's and moving them mid-run risks breaking its
own references — flagged for the campaign owner. The gate remains in the
CI skip list, so this does not break CI; it does mean the surface map is
not a trustworthy inventory until (2) is chosen.

---

## Revision 31 (2026-08-04, action-shell lift needs a faithful carrier)

Sources:
`explorations/k77-wave2-euler-shell-two-connection-lift-2026-08-04.md`,
`lab/sources/gu-euler-shell-two-connection-source-reinspection-2026-08-04.md`,
`lab/process/k77-wave2-euler-shell-two-connection-lift.json`, and
`lab/process/hostile-reviews/2026-08-04-k77-wave2-euler-shell-two-connection-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- Before testing candidate primalizers, compute the whole natural-map space.
  Scope the dimension to the tensors actually allowed; extra active epsilon,
  Shiab or derivative owners define a larger problem.
- An action Euler density can own a connection difference without introducing
  a new free field: apply the action's own indefinite density/adjoint
  pseudo-musical and mark the resulting connection dependent.
- Use the actual derivative of the written action. A source-advertised endpoint
  that fails Helmholtz on the full domain cannot be substituted into the lift.
- In a two-connection square the southwest block is the cheapest converse
  detector, but only on a faithful coefficient module (or centerless adjoint
  carrier). Carry faithfulness through every later quotient.
- Do not erase a mixed northeast defect. Make it proportional to the actual
  Euler residual and verify that it is live off shell and zero on shell.
- Shared inhomogeneous-term cancellation proves the difference has the right
  affine typing; it is not the complete moving local-gauge Ward theorem.
- A dependent shell equivalence has zero selection surplus. Its value is that
  it makes the construction coherent and retires an unowned debt, not that it
  already predicts physics.

---

## Revision 32 (2026-08-05, observation has two independent false-shell kernels)

Sources:
`explorations/k77-wave2-euler-lift-full-field-ward-observation-port-2026-08-05.md`,
`lab/sources/gu-euler-lift-ward-observation-source-reinspection-2026-08-05.md`,
`lab/process/k77-wave2-euler-lift-ward-observation-port.json`, and
`lab/process/hostile-reviews/2026-08-05-k77-wave2-euler-lift-ward-observation-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- An observed complex detects an upstairs Euler equation only modulo the
  kernel of the complete receiver `rho_X sharp_X O_E`.
- There are two independent false-shell mechanisms: the equation dual can
  erase a normal Euler component, and the observed coefficient representation
  can erase a connection difference that survived equation observation.
- Compute the whole composite kernel before testing observation projectors.
  Local `R L=1` and observed-equation transport do not prove no-leakage.
- The minimal conditional repair is conjunctive: equation no-leakage on the
  lifted field image plus coefficient faithfulness on the observed `tau_E`
  image. Either condition alone is insufficient.
- Ward naturality does not imply no-leakage. A normal Euler covector can pair
  trivially with every tangent gauge generator while remaining nonzero.
- A leakage vector lying in a finite preboundary characteristic kernel is not
  thereby gauge. Quotienting it requires an action-derived tangent/BV
  differential and boundary conditions.
- Reuse existing observation machinery. The remaining debt is the actual K77
  Euler receiver and common domain, not a generic proof that descent can exist.

---

## Revision 33 (2026-08-05, form degree precedes observation rank)

Sources:
`explorations/k77-wave2-actual-y14-receiver-ordering-conormal-2026-08-05.md`,
`lab/sources/gu-actual-y14-receiver-ordering-source-reinspection-2026-08-05.md`,
`lab/process/k77-wave2-actual-y14-receiver-ordering-conormal.json`, and
`lab/process/hostile-reviews/2026-08-05-k77-wave2-actual-y14-receiver-ordering-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- Run the form-degree Layer-0 check before constructing an observation map.
  Literal pullback of a 13-form or 14-form to a four-manifold is zero.
- A density-dual Euler row may be primalized before restriction, but ordinary
  section restriction from fourteen to four covector directions then has a
  complete rank-ten conormal kernel.
- Downstream coefficient faithfulness cannot recover geometry already erased
  by section restriction. Receiver faithfulness and representation
  faithfulness are sequential gates.
- A trace-reversed pseudo-metric supplies a horizontal right inverse for a
  nondegenerate section graph; it does not prove the actual action Euler image
  horizontal. That image condition must be derived, not target-selected.
- Do not present “horizontal action image or retain normal equations” as an
  exhaustive theory fork. A genuine defect/current or induced-density
  reduction of the action followed by variation is a third route, and the N3
  build already contains its moving-support derivative.
- Never write `s*(dvol_Y)` for a lower-dimensional volume form without naming
  the intended induced-density or current-pairing operation. Preserve older
  provenance, but do not reuse the literal notation as proof.
- Matching tangential observed evolution does not establish no-leakage; a live
  normal operator block can be invisible after restriction.
- A tangent-plus-normal decoder is algebraically faithful but does not identify
  the ten normal components as gauge, constraints, particles, or dark content.

---

## Revision 34 (2026-08-05, pullback and vertical coefficient restriction precede normal loss)

Sources:
`explorations/k77-wave2-augmented-torsion-defect-euler-receiver-2026-08-05.md`,
`lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md`,
`lab/process/k77-wave2-augmented-torsion-defect-euler-receiver.json`, and
`lab/process/hostile-reviews/2026-08-05-k77-wave2-augmented-torsion-defect-euler-receiver-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- Before declaring that observation loses normal coefficients, check every
  coefficient restriction already owned by the field construction. Along a
  section, `(s*,res_s^V)` is an isomorphism for one-form coefficients.
- Derive an equation receiver as the dual of the complete field map. For a
  moving graph section its matrix is inverse transpose, and the vertical
  equation includes a forced section-jet correction.
- Source collision precedes new fields: Weinstein's full upstairs augmented
  torsion and N1's existing vertical restriction jointly type the ten outputs,
  so a new normal projector or datum would be redundant.
- A published quadratic term can test action-image horizontality cheaply. A
  constant commuting conormal witness isolates the nonzero-`kappa` term from
  curvature, but the verdict must be scoped to the displayed variation domain.
- A faithful fibrewise receiver is not a reduced action. The current/density,
  moving support, density/Hodge/Shiab variation, Ward/BV descent and domain
  remain independent construction obligations.
- Keep vertical scalar-like coefficients bundle-valued until representation,
  vacuum and physics gates identify them; rank ten is not a Higgs derivation.

---

## Revision 35 (2026-08-05, localizing a first-order action emits normal dipoles)

Sources:
`explorations/k77-wave2-full-source-action-defect-localization-moving-section-ward-bv-2026-08-05.md`,
`lab/sources/gu-defect-localization-ward-bv-source-reinspection-2026-08-05.md`,
`lab/process/k77-wave2-full-source-action-defect-localization.json`, and
`lab/process/hostile-reviews/2026-08-05-k77-wave2-full-source-action-defect-localization-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- Localize an ambient top-density by evaluating its scalar coefficient on the
  section jet and pairing with the induced section density. Literal pullback
  is dimensionally zero.
- First-order ambient normal derivatives produce derivative-of-delta sources.
  The exact conormal Legendre coefficient is `P^a-s_i^a P^i`; neither the
  zero-jet four-plus-ten receiver nor tangential integration by parts erases it.
- Vary support and induced density separately, then recombine them in the
  graph shape Euler operator. Freezing either owner can fake a Ward failure or
  a false simplification.
- Coordinate-density descent introduces no new vertical orientation or P1,
  but it does not repeal orientation/Hodge assumptions already owned upstairs.
- A localization functor preserves a complete even Ward identity; it cannot
  manufacture omitted `epsilon/B/Shiab/background` transformations.
- Keep the BV grade explicit: closed nilpotent even algebra and boundary-free
  descent is not a primitive full-field receipt, odd super-IG action, physical
  BFV phase space, or Green domain.
- A source-shaped proxy can prove a failure mode possible without proving its
  actual coefficient nonzero. Compute the moving K77 conormal symbol before
  promoting zero-jet nonfactorization.
- Localization is not the bulk/defect weld. Replacement, addition and
  independently owned defect terms carry different double-counting and
  dimensional-normalization burdens; fit none of them by default.

---

## Revision 36 (2026-08-05, compute an unselected-family symbol before choosing a representative)

Sources:
`explorations/k77-wave2-i1b-conormal-symbol-bulk-defect-weld-domain-2026-08-05.md`,
`lab/sources/gu-i1b-conormal-weld-domain-source-reinspection-2026-08-05.md`,
`lab/process/k77-wave2-i1b-conormal-symbol-weld-domain.json`, and
`lab/process/hostile-reviews/2026-08-05-k77-wave2-i1b-conormal-symbol-weld-domain-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- When a source supplies an action family but no preferred operator, compute
  the principal symbol as a formula in the family member before searching for
  coefficients. This can close factorization and domain questions without an
  unearned representative.
- Distinguish an action-family result from a selected-coefficient result in
  both prose and executable receipts. A live generic matrix proves nonvacuity,
  not source identity.
- For a `4+10` section, count the conormal-generated input block before trying
  a zero-jet closure: 85 of 91 two-form directions contain a normal leg.
- State annihilator counts per paired coefficient block when suppressed
  internal indices remain. Compression that drops this qualifier recreates
  the owner-surface overstatement problem.
- Pullback observation is not a second action owner. Keep the bulk law once
  and add only independently typed defect densities unless a localized rival
  supplies its normal-density/transverse-profile normalization and a
  double-counting theorem.
- Type density lines before physical dimensions. `length^10` is a valid
  homogeneous-coordinate comparator for codimension ten, not an invariant
  statement when metric-fibre coordinate units are undeclared.
- Separate three domain grades mechanically: smooth common variation core,
  trace-regular Sobolev completion, and closed Green/hyperbolic/BFV domain.
  The first two do not imply the third.
## Revision 37 (2026-08-05, family motion is not family selection)

Sources:
`explorations/k77-wave2-moving-shiab-epsilon-ward-green-domain-2026-08-05.md`,
`lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md`,
`lab/process/k77-wave2-moving-shiab-epsilon-ward-green-domain.json`, and
`lab/process/hostile-reviews/2026-08-05-k77-wave2-moving-shiab-epsilon-ward-green-domain-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- Enumerate a finite source-permitted family exactly before introducing ML or
  fitting. Eight discrete channels need no surrogate.
- Report exterior support, a chosen witness-slice rank and full coefficient
  rank separately. The live-85/rank-14 channel is the planted control against
  expressibility inflation.
- A moving gauge orbit supplies covariance, not a selector. Invertible
  conjugation transports rank and cannot create an annihilator.
- Derive primitive equations through the actual dependency graph. For fixed
  metric and section, epsilon moves `B`, `T` and conjugated invariant forms;
  Hodge, density, metric and section motion remain separate rows.
- Test Ward identities with all transformed owners present. Omitting either
  the moving operator or inhomogeneous connection direction can create a fake
  obstruction.
- Keep formal Green closure, preboundary data and physical evolution as three
  grades. Compact-core Dirichlet zero flux proves only the first.
- After a partial gate, name the narrower successor: action-derived product
  discrimination plus a global coupled domain, not another generic request for
  a source action or external datum.

## Revision 38 (2026-08-05, variational consistency and common regularity are not selectors)

Sources:
`explorations/k77-wave2-action-polarization-common-observation-domain-2026-08-05.md`,
`lab/sources/gu-action-polarization-domain-source-reinspection-2026-08-05.md`,
`lab/process/k77-wave2-action-polarization-common-observation-domain.json`, and
`lab/process/hostile-reviews/2026-08-05-k77-wave2-action-polarization-common-observation-domain-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- Polarize the scalar action before comparing it with a separately printed
  endpoint. Helmholtz symmetry certifies each action-derived Euler pair; when
  every family member is defined by a scalar action, its selection rank is
  zero.
- Compute both projective classes and linear span. Eight pairwise
  nonproportional grade-one restrictions can still span five directions and
  obey three exact relations.
- State the coefficient grade on every rank or relation. A complete
  `91 x 14` grade-one bank is not the full adjoint carrier.
- Use an independent exact engine at a genuinely different layer. Sage proves
  the free threefold product transform has rank eight and determinant 4096;
  the represented K77 grade-one rank-five collapse is therefore a
  Clifford/Hodge restriction effect, not a malformed product encoding.
- A common Sobolev regularity scale is useful construction infrastructure but
  supplies no boundary selection. Channel-dependent principal coefficients
  may change Green forms while preserving `H10 -> H9` mapping regularity.
- Run dimension Layer 0 before calling observation a boundary: `X4` has
  codimension ten in `Y14`, while an ordinary Green boundary has codimension
  one. A defect/current/interface owner is required to connect them.
- When self-consistency conditions are shared by the entire candidate family,
  stop polishing them as selectors. Move to an independently constructed
  Bianchi/exactness or two-connection target.

## Revision 39 (2026-08-05, factor before enumerating and type independent targets)

Sources:
`explorations/k77-wave2-full-adjoint-shiab-bianchi-two-connection-target-2026-08-05.md`,
`lab/sources/gu-shiab-bianchi-two-connection-target-source-reinspection-2026-08-05.md`,
`lab/process/k77-wave2-full-adjoint-shiab-bianchi-two-connection-target.json`,
and
`lab/process/hostile-reviews/2026-08-05-k77-wave2-full-adjoint-bianchi-target-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- Before enumerating a huge carrier, factor the displayed operator formula.
  The exact separation `S_(f,i,o)=A_f+B_(i,o)` plus one complete restriction
  lower bound proved the full eight-map rank in seconds and superseded a
  `91 x 16384 x 8` census.
- Representative tests may corroborate a structural theorem but must not own
  it. The fifteen grade representatives are plants; incidence plus the
  complete grade-one lower bound is the proof.
- Build an independent target before applying the candidate map. The
  connection-path average reconstructed from `(F_B,Delta F,T)` is genuinely
  pre-Shiab and therefore cannot reward a product for matching itself.
- Distinguish input-side Bianchi closure from a product-sensitive chain-map
  law. A pre-Shiab identity has selection rank zero by type; selection can
  enter only through `D_out S-S D_in` or another independently typed codomain
  constraint.
- Preserve immediate source context. The unreleased two-connection mnemonic
  follows the fermion roll; using its curvature blocks does not create a full
  bosonic Euler-complex comparison.

## Revision 40 (2026-08-05, test Bianchi on the right carrier and reject vacuous passes)

Sources:
`explorations/k77-wave2-principal-bianchi-product-selector-2026-08-05.md`,
`lab/sources/gu-shiab-derivation-principal-bianchi-source-reinspection-2026-08-05.md`,
`lab/process/k77-wave2-principal-bianchi-product-selector.json`, and
`lab/process/hostile-reviews/2026-08-05-k77-wave2-principal-bianchi-product-selector-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- A differential-Bianchi test on generic adjoint two-forms asks the wrong
  question. Intersect first with algebraic Riemann pair symmetry and first
  Bianchi; the complete principal carrier is the rank-91
  `(k tensor k) KN Sym2` image.
- Test every principal-covector orbit. Positive/negative axes do not cover the
  null orbit in indefinite signature; exact null controls are mandatory.
- A kernel condition needs a nonvacuity gate. Three product rows passed
  Bianchi only by erasing the entire Riemann sector; zero is not a useful
  selector success.
- Count constraint independence before claiming surplus. Contracted Bianchi
  and the Einstein trace ratio are linked, so the separately assembled
  Einstein match corroborates the selector but is not another surplus row.
- A finite discrete grammar can yield an exact conditional selector without
  yielding full operator uniqueness. Preserve both statements.
- Build comparison diagrams one carrier at a time. The two-connection
  curvature square is now real; augmented torsion and full Euler comparison
  remain the successor rather than being smuggled into the square's label.

## Revision 41 (2026-08-05, never pull a noncyclic Shiab through the variation)

Sources:
`explorations/k77-wave2-eddy-augmented-torsion-euler-prolongation-2026-08-05.md`,
`lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md`,
`lab/process/k77-wave2-eddy-augmented-torsion-euler-prolongation.json`, and
`lab/process/hostile-reviews/2026-08-05-k77-wave2-eddy-augmented-torsion-euler-prolongation-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- The `1/2,1/3` coefficients reconstruct the path-average curvature, but that
  does not make a general Shiab behave like the identity under variation.
  Preserve the Fréchet-adjoint companion
  `(D_T barF)^! S^! T` in the action Euler row.
- A breadth/supersession pass must run before promoting a synthesis. The first
  draft of this wave revived the printed endpoint already killed by K77-B3;
  the paired hostile charge caught and retracted it before commit.
- Keep source-displayed and action-owned equations separate. Here
  `Upsilon_print=S(F_A)+*kappa T` is a typed rival, while
  `E_act=S(barF)+(D_T barF)^!S^!T+*kappa T` is the variational primary.
- Do not impose a metric-Riemann closure condition on generic adjoint
  connection curvature. Here the rank-91 Riemann defect is zero while the
  complete grade-one generic carrier has a live rank-13 image for the
  **printed** degree-14 rival. Do not transfer that rank to the action Euler.
- `Xi_print=D Upsilon_print` cannot be inherited by `E_act` after the
  degree-13 rows separate. Derive an action-owned degree-14/Noether row or
  leave it open.
- A nonzero extra block must have an owner, homotopy, quotient or explicit
  rival disposition. Source hints about an up-and-back stress-energy term are
  search directives, not permission to assign an unreleased block.
- State bracket conventions. A normalized `T^2` coefficient cannot be copied
  unchanged into a raw Lie-bracket convention with `[T,T]=2T wedge T`.
- Use symmetry-orbit checks as robustness, not surplus. The three covector
  orbit ranks are one equivariant structural result, not three independent
  constraints.
- When a residual block meets an already-open total-action debt, join them in
  one successor gate instead of creating another suffix-only wave.

## Revision 42 (2026-08-05, totalize Noether and keep the forced Clifford grades)

Sources:
`explorations/k77-wave2-action-owned-degree14-northeast-totalization-2026-08-05.md`,
`lab/sources/gu-action-owned-degree14-northeast-source-reinspection-2026-08-05.md`,
`lab/process/k77-wave2-action-owned-degree14-northeast-totalization.json`, and
`lab/process/hostile-reviews/2026-08-05-k77-wave2-action-owned-degree14-northeast-totalization-review.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves.

- A selected contraction must be closed on its actual coefficient grades
  before it is interpreted physically. The exact Shiab is surjective onto the
  rank-196 `Cl1` receiver but also forces rank-1001 `Cl5`; projecting the
  latter away would defend a superseded Einstein-only object.
- Construct a formal adjoint entrywise under the declared pairing, and name
  its grade. Invertible diagonal transpose proves the rank exactly but does
  not prove positivity, closability, boundary cancellation or a physical
  Krein domain.
- The action-owned top-degree relation is the coefficient of one gauge
  parameter after all transforming-field Euler terms are integrated by
  parts. `D_B E_act`, `Xi=D Upsilon`, and the full even Noether totalization
  are three distinct objects.
- Test proposed cross-arena owners first by form degree and zero-sector
  controls. A degree-13 fermion current cannot directly equal a degree-3
  cyclic block, and the raw block survives when fermions vanish.
- The right degree is necessary, not sufficient. The minimal pure-trace
  degree-three Shiabs map into degree 14 but erase traceless Ricci on every
  principal-covector orbit.
- A candidate-map kill must emit its remaining search space. Portal's general
  degree law confirms the degree-three arena while its “many bespoke Shiabs”
  statement keeps the larger source-natural basis open.
- Use modular arithmetic where it becomes a theorem: full column rank modulo
  a prime proves rational injectivity when the column count is the absolute
  upper bound.

## Revision 43 (2026-08-05, source-locus verification and the scale-blindness pairing)

Sources:
`lab/sources/keating-interview-2025-06-12-source-record.md` and
`explorations/conditional-build/cb-e-source-contact-rows-2026-08-05.md`.
No protected claim, canon verdict, lane, public posture, physics row, Wave-3
admission, or P1/P2/P3 status moves. No external datum touched.

- **NEW NAMED CHECK — `SRC-LOCUS` (locus verification, distinct from truth
  verification).** A secondary pass attributed the UCSD seminar's own content
  (`ε_ω`, three generations, Pati-Salam) to a later Keating interview. Every
  attributed claim was genuinely Weinstein's, so no truth check could catch it;
  what was wrong was the LOCUS. This is the second provenance-drift instance in
  three days, with polarity reversed from the 2026-08-04 imposter-quote case
  (source-absent content cited as primary). **Before citing any media claim,
  verify the claim exists at the named locus, not merely that the speaker said
  it somewhere.** Cheapest instrument: grep the in-repo transcript first — both
  instances would have been caught in one command.
- A uniqueness claim from a source is worth pairing with the repo's
  scale-blindness results before it is filed as agreement or tension. Doing so
  here QUANTIFIED it: the divergence-free demand is linear and homogeneous in
  the candidate term, so its solution set is a linear subspace and can never be
  a single nonzero point — it forces the ray (form) and cannot fix the point on
  it (scale). DC-H2's congruence-orbit exclusion is the general version of the
  same one-line argument. Corollary worth carrying: no strengthening of the
  divergence-free demand will ever produce the DE magnitude, so the 120-orders
  problem is a different TYPE of problem, not a harder version of this one.
- When a source's claim looks like it threatens a repo result, check whether
  the source refutes the threatening reading itself. Here the magnitude-included
  reading is killed by Weinstein's own next sentence ("once it's constant, it
  has no explanation", `papers/drafts/Transcript into the impossible.md:44`).
  Cheaper and more durable than an adjudication that only cites the repo.
- **Adverse row entered, not softened:** GU derives its DE divergence-freeness
  FROM EQUIVARIANCE, which DC-H2 proved is a member of exactly the scale-blind
  class. GU therefore inherits the residue it objects to in `Λ` — and on CB-D's
  count, twice (two independent length-squareds) where GR had it once. The
  genuine win in this sector is DYNAMISM, never magnitude; canon already scopes
  it correctly at `canon/dark-energy-theta-divergence-free.md:96`.
- **`VERIFIED_REPO_DISCONNECT`, reported not repaired (protected directory).**
  `explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md:50-56`
  displays the DE replacement as `(d_A π)` with `π` an ad-valued 1-form, then
  asserts in the next sentence that the result "lives in ad-valued 1-forms" —
  a one-degree self-contradiction, with `ε_ω` present in the prose and absent
  from the formula. Canon has it right. Fence added to
  `lab/process/agent-context-pack.md` Layer-0.
- **Filing defects in `lab/sources/media-index.md` (canon; not edited).**
  (a) Row `GU-MEDIA-2025-UCSD-SEMINAR` (`:65`) records the local transcript
  path but **no source URL or video ID**, which is exactly what leaves
  undecidable whether the 2025-06-12 upload is a separate video or a ~2h23m
  superset whose first ~50 min are the seminar. (b) Row
  `GU-POD-2025-KEATING-DESI-GU` (`:64`) should point at the new source record;
  its cell must **stay** `metadata-checked`/`timestamp-needed` — the record
  does not discharge it, because no timestamp was transmitted into this repo.
  (c) The seminar transcript exists twice — `lab/literature/weinstein-ucsd-
  2025-04-transcript.md` (with provenance front-matter) and `papers/drafts/
  Transcript into the impossible.md` (without) — and nearly every exploration
  cites the copy that carries no provenance.

**CB-E CORRECTION (2026-08-05) — SRC-LOCUS fires a second time, same day.**
Rows E3 and E9 RETRACTED. E3 priced GU's answer to the dark-energy
MAGNITUDE question as if that answer were divergence-freeness, proved
(correctly) that a linear homogeneous condition cannot fix a scale, and
concluded GU inherits an unexplained magnitude "twice where GR had it
once." Divergence-freeness is Weinstein's answer to the FORM question.
His answer to the MAGNITUDE question is a two-field identification: the
dark-energy VEV is set equal to a curvature-side field which sits near
zero, so it is lured toward zero with it — his diagnosis being that the
disaster is the FIXEDNESS, not the smallness, since a constant cannot
track anything. He explicitly claims only to trade TWO problems for ONE,
not to derive the magnitude. DC-H2 excludes SYMMETRY-type scale
suppliers; a dynamical identification with another field is a different
class and DC-H2 does not reach it — citing it there is a scope error.
E9 ("the coincidence remark supplies no constraint") is retracted for the
same reason: the coincidence argument IS the mechanism, not an aside.
NEW OPEN ROWS: E10 does the identification genuinely reduce the free
count or relocate it (surplus computation, the row that matters); E11 is
the identification inside or outside Weinberg's no-go class for
self-adjusting Lambda mechanisms (same procedure as the Boyle-Turok
foil); E12 is the standard fine-tuning framing itself sound (Keating
raises percent-level rather than parts-per-million; the repo's own DE
lane cites the standard framing). E1/E2/E4-E8 stand unchanged.
