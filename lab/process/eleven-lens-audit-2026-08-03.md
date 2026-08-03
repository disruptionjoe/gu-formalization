---
title: "Eleven-Lens External Audit: verified findings, discards, and fix packet"
status: process
doc_type: audit-report
created: 2026-08-03
updated: 2026-08-03
claim_status_change: none
canon_change: none
method: "11 read-only specialist lenses (rep theory, index theory, homotopy/bordism, statistical cosmology, certificate engineering, Lean fidelity, claim-graph consistency, literature scout, numerical robustness, portfolio economics, hostile external referee), Joe-directed 2026-08-02/03. Every load-bearing finding below was independently re-verified by the orchestrator (quote-trail, re-run, or independent recomputation) before inclusion; findings that failed verification are listed in the Discards section. Lens-verified-only items are marked [lens]."
---

# Eleven-lens audit — verified findings

This is an error audit. The companion opportunity synthesis is
`lab/process/mathematician-panel-synthesis-2026-08-03.md`. Nothing in this file
changes a claim, verdict, grade, or canon status; it identifies where owner
surfaces should change and leaves execution to the repo's own
claim-status-consistency workflow.

## The meta-pattern (the audit's single most consistent result)

**The load-bearing artifacts are honest; the coordination surfaces around them
are systematically stale in the optimistic direction.** The published LNF
manuscript, the certificates' self-scoping, VERIFICATION.md, REVIEWER.md, and
the posture files repeatedly survived hostile reading. The ledgers, indexes,
status rows, and canon consequence-sentences repeatedly did not. Three
corrections were found to be *already recorded inside the repo* and never
propagated to their owner surfaces:

1. The W211 "one free Z/2" was killed twice in-repo
   (`papers/drafts/structurally-forced-internally-undecidable/draft-skeleton.md`
   2026-07-14; `explorations/W219-native-good-stable-stabilizer-input-gate-2026-07-14.md`)
   and `RESEARCH-STATUS.md:134` still advertises it, swept 11 days after the kill.
2. The signature was demoted to UNDER-DETERMINED
   (`explorations/W202-…`, `explorations/wave14/H19-…`) and
   `canon/shiab-existence-cl95.md:70` still says "(9,5) … confirmed by the
   Frobenius metric computation" (the fiber form is quadratic in `g`; only the
   unargued base convention selects (9,5) over (7,7)).
3. The corrected MOVE-1 gravitational coefficient (493/2419200, vs the rank-only
   13/2419200) was already computed in
   `explorations/global-anomaly-leg-2026-07-20.md` (title block: "NEW
   OBSERVATION for the local-leg custodians") and the custodian surfaces
   (`tests/chase/README.md`, MOVE-1 docs) never moved.

## CRITICAL findings (all orchestrator-verified)

**A1 — The published release is unreachable from the public default branch.**
Zenodo checkpoint `020b682d` is not an ancestor of `origin/main` (verified:
`merge-base --is-ancestor` fails; it lives only on the three `agent/*`
branches). `origin/main` has no `zenodo-package-v1.0.0/`, no v2.15 manuscript,
no release receipt; its README says the lead result is "not yet posted" and its
"If you are here from the paper" block points at
`papers/candidates/observer-value-selection-theorem/submission/`, which exists
on no branch. `main.pdf` is `.gitignore`d and has never been tracked. CI
(`.github/workflows/lean.yml`) watches `main` only, so it has never compiled
the modules the release receipt certifies. `main` is 75 commits behind the
working branch (unMERGED, not unpushed — fix is a merge/tag, not a push).

**A2 — The Lean ledger overclaims what Lean contains.** Row T3
(`lab/process/lean-verification-lane-LEDGER.md:64`, "Antilinear null-eigenspace
bound: LEAN-VERIFIED") has no corresponding Lean content — there is no
antilinear operator anywhere in `Lean/` (verified by grep), and the owning
canon file itself says "This is a symbolic proof, not a Lean-checked one"
(`canon/core-theorems-symbolic-proof-RESULTS.md:98`). Row T2's theorem is
`0 − 0 = 0` (both intersections are `⊥` by the same lemma; verified by direct
reading of `LocatedNotForcedLegs.lean:52-131`), and the ledger titles it with
the exact "net chiral index" phrase `HARDENING-QUEUE.md:118` bans. The
`FiniteKreinForm` `hermitian`/`nondegenerate` fields are never used by any
proof. **The published manuscript grades all of this correctly** — the
overclaims live only in the ledger, `Lean/README.md`, and root
`VERIFICATION.md:22` (which cites `ResidualSelection.lean` for a group-action
generalization containing zero group-action content; the deposit's own
`reproduction.md:20` states the correct scope). Further ledger-tier items
[lens, spot-confirmed]: the 2026-07-22 build receipt predates the 2026-07-23
rewrite of two certified files; `LocatedNotForcedFiniteCore.lean` (the paper's
headline module) has no ledger row and is outside the certificate-surface
gate's file list; the `2/2/2/2/0` census "derivation" includes a filter of the
form `P ∧ ¬P` (a propositional tautology) for its load-bearing zero.

**A3 — A load-bearing chase-to-kill certificate currently prints the opposite
of what two owner surfaces say it proves.** `tests/chase/MOVE-5/krein_nogo_chiral_index.py`
prints `==> NO-GO NOT established; see failing measures above.` and exits 0
(verified by run). `DERIVATION-PROGRESS.md:2594` and `RESEARCH-STATUS.md:146`
describe it as "COMPUTED-CONFIRMED … EXACTLY 0 across 400 random Psi x 3
signatures (graded trace ~9e-15)". The failure is the alt-timelike-A signature
block, whose carrier is selected by a `round(x,3)` + `1e-3` window that picks a
64-dim non-triplet level (Casimir 60/7 ≈ 8.571) and empties at tolerance 1e-4
[lens diagnostic]. The *structural* no-go leg (`struct_ok`, J_q swap) passes in
all blocks and `verify/nonvacuity.py` passes — the physics claim survives; the
"3 signatures agree" packaging and the script's own terminal criterion do not.

**A4 — FC3 fired and nobody noticed.** The repo's own certificate computes
`ch2(S(6,4) normal only) = 4 × (−288) = −1152` (verified by run of
`tests/gen_ch2_sx_from_codazzi.py`), and the repo's own named failure condition
(`explorations/generation-sector/generation-count-rank3-resolution-2026-06-23.md:532`:
"FC3: ch_2(S(6,4))[K3] != 0 changes the required A-hat value") says exactly
what that means. The `ind_H = Â(K3)·rank = 2×8 = 16` move
(`explorations/analytic-index-fredholm/oq-rk2-aps-boundary-rs-k3-2026-06-23.md:38,76,589`)
drops the ch₂ term and is arithmetically dead on in-repo data. The old
`16 + 8 = 24 → 3` chain is over as arithmetic, not merely as provenance; the
count verdict is already OPEN so nothing flips, but FC3 should be recorded
FIRED and the un-bannered files corrected. Live consumers still exist
(`tests/decider/fibered_boundary_reduction_decider.py` PART C;
`docs/NEXT-FRONTIER-HYPOTHESES.md` H1(c)).

**A5 — The seven-axis/Layer-0 ratification never reached its canon authority
file.** `canon/six-axis-specification-protocol.md` (status canon, the file
`RESEARCH-STATUS.md:102` and `CANON.md:60` point to as protocol authority)
contains zero occurrences of L7, Layer-0, or "seven" (verified) and still
defines the protocol as six axes; the 2026-07-10 Joe-ratified change lives in
`AGENTS.md`, the template, and the no-go map only.

**A6 — A canon posture surface still asserts advocacy.** `docs/OVERVIEW.md`
(status canon, updated_at 2026-07-07) says "The working hypothesis is that
Geometric Unity is substantially correct" and "no longer neutral-map-first"
(verified verbatim) — contradicting `RESEARCH-POSTURE.md`, `CANON.md:19-21`,
and `RESEARCH-STATUS.md:24-26`, all of which explicitly disclaim exactly this.
`README.md:107` routes readers to it as the high-level overview.

**A7 — The W211 stale row (meta-pattern instance 1, full statement).**
`RESEARCH-STATUS.md:134` advertises "symmetry reduction LIBERATES the sign as a
free Z/2 … FIVE independent methods return RESIDUAL-BIT-STANDS UNANIMOUSLY."
The same-day adversarial hardening proved the opposite for the constructed
stabilizer ("the admissible fundamental symmetry is unique, not a free Z/2" —
draft-skeleton.md, verified verbatim), `NEXT-STEPS.md:1085-1090` records the
kill ("killed the previous one-free-Z/2 theorem"), and W219 re-proved it at
the program-native `Sp(32)×Sp(32)` level. The GU-native question stays open
(the stabilizer is kinematic, not derived) — but the ledger row is dead.

## MAJOR findings (verified unless marked [lens])

| # | finding | where | note |
|---|---|---|---|
| B1 | Canon says Frobenius computation "confirms (9,5)"; it cannot — fiber form is quadratic in `g`, `(7,3)→(6,4)` under both base conventions (checked by hand); W202/H19 already record UNDER-DETERMINED | `canon/shiab-existence-cl95.md:70,31` | Kramers wall is (9,5)-specific; dissolves on (7,7) |
| B2 | SHIAB-05's consequence "must come from an external source-action spurion" over-claims: same-chirality channels exist at every odd k; `Λ⁵ ⊃ 126⊕126̄` as a Lorentz singlet (arithmetic verified: 2002 = 252+840+720+180+10); canon's own escape-corners has `16×16 = 10+120+126` | `canon/shiab-existence-cl95.md:84`; `canon/escape-corners-campaign-RESULTS.md:56` | Correct statement: no invariant *scalar* channel; odd-form VEV is internal to the family |
| B3 | MOVE-1's gravitational "key number" 13/37800 is the rank-only truncation; correct p₄ coefficient is 493/2419200 (verified by independent sympy recomputation, exact match), a ~38× change. Non-factorization verdict survives (493 ≠ 0). Already known in-repo (see meta-pattern §3) | `tests/chase/MOVE-1/*`; `tests/sp64_octic_trace_i16.py:465-478` | [orchestrator-verified] |
| B4 | RB7's published kill numbers are finite-difference artifact: the vertical residual is exactly 0 (clean O(h²) truncation under exact analytic derivatives; the 0.00361491 scales as s⁻³ roundoff), the numbers don't reproduce across machines past 2 digits, and signal/floor 0.9702 is a ratio of two noise norms. **The kill verdict itself survives** (separation < 1.1 at every scale and 0.740 with exact derivatives). Mixed Gram is exactly (9/32)(I+T_tr) — a stronger, exact statement than the published fit | `explorations/rb7-…-2026-07-30.md:74-93,233-241`; probe | [lens, mechanism spot-checked; full sweep in scratchpad] |
| B5 | The ARB-CERT worked example in `lab/process/computational-toolchain.md` certifies 60 digits of a ratio whose true value is 0/0 noise — rigorous enclosure of a discretization artifact. Orchestrator's own error; corrected this session | `lab/process/computational-toolchain.md` | Replace with the exact 9/32 identity |
| B6 | LNF carrier derivation conflates two different p₁=4's (Kirby–Melvin relative p₁ of RP³'s natural framing vs p₁(adP)=−4c₂ as change-of-framing degree); canon calls them an "independent derivation matching" (quotes verified). The composite class under the twist reading is 2±2 ∈ {0,4}; the cert's own output lists the erasing branches but the identification "Λ²₊ = this exact tangential framing" is a declared premise, which scopes the issue | `canon/final-verdict…:51-57`; `canon/boundary-einvariant…`; cert run verified | Does not touch the "located, not forced" headline |
| B7 | "Randal-Williams" is cited for the load-bearing e = ±p₁/48 formula at `manuscript-v2.15.md:796` with **no bibliography entry** in the published deposit (verified); the formula's W-spin hypothesis is stated nowhere | zenodo package | Needs a v1.0.1-class fix |
| B8 | The Bismut–Cheeger claim in the fibered-boundary decider is inverted (eta-forms are for EVEN-dim fibers; the terms kept are the ones that vanish, the dropped η̃ is the survivor); "fiber transparent [PROVEN]" is unearned. Lichnerowicz gives ker D^{S⁶}=0, so the honest reduction is `∫ Â ∧ η̃` with no Dai corrections — one unknown | `tests/decider/fibered_boundary_reduction_decider.py:268-276,349,362` | [lens; standard-theorem check] |
| B9 | "APS eta = 0 for the actual operator" is the eta of the principal symbol at a point — automatic ±|p| symmetry for every Dirac operator, content-free; carried as an "honest global number" in the capstone | `tests/gen_aps_eta_actual_operator.py`; `docs/WHERE-GU-STANDS…:50` | [lens] |
| B10 | "C2 is ~94% global" survives although C2 = √(3328/7)·‖ξ‖_Euclidean in closed form (repo's own master-identity), frame-dependent (not SO(9,5)-invariant), so the percentage supports no global/topological inference | `explorations/anomaly-and-bordism/c2-is-global-…:24,38`; master-identity 2026-07-20 | [lens; closed form is in-repo] |
| B11 | The η=0 "wall" mechanism is one Hodge-type off-diagonal ansatz appearing as four independent-looking results; on the actual odd-dim (13) boundary the volume element is central, no anticommuting grading exists, and η is unobstructed; H37's `(H+V)²=H²` constraint is over-strong | `canon/rs-boundary-eta-2primary-RESULTS.md`; `explorations/wave13/H37…:85-90` | [two lenses agree] |
| B12 | b-calculus Fredholm "Window 0 = (0,∞)" is impossible (Dirac-type indicial spectrum is unbounded both ways; the half-space restriction at :257 discards the negative half), the boundary face is noncompact so the b-criterion doesn't apply, and the surviving discrete-sector conditional is vacuous by the repo's own Flensted-Jensen rank count | `explorations/analytic-index-fredholm/oc2-b-parametrix-…:257,299,305` | [lens] |
| B13 | DESI chain language: "~3.2σ" is a 2-dof Mahalanobis radius read as 1-D σ (≈2.7σ; 2.5–3.0σ over the repo's own ρ scan — conversion verified analytically); f₀ bounds are ~3× looser with ω_m h² profiled (0.027→~0.08) [lens]; "+5.7σ_A overshoot" is an increment over ΛCDM's own +4.0σ_A and the real mechanism is a +19.3 shape failure [lens]; "SNe can only hurt H0=63.75" is a physics error (uncalibrated SNe carry no H0 information); family-level dAIC is +1.9..+3.2, below the repo's own decisive line — only the signal-level identification is excluded. **The band-wide signal-level exclusion itself survived everything the lens threw at it**, and the DESI DR2 files are byte-verified against the official Cobaya repo | `canon/theta-field-flrw-dark-energy-eos.md`; wave45/46; W129 | |
| B14 | Ledger drift cluster: DERIVATION-PROGRESS still says the 2026-07-03 promotions are "staged … PAUSE FOR JOE" (5 occurrences, verified) while the files are canon; LANE-STATE (07-26) says "Nothing needs Joe"/green/moving while the portfolio holds NEEDS_JOE and the 07-29/30 results contradict the lane story; portfolio json (07-24) has B5 IN_PROGRESS vs the run-plan's BLOCKED; `papers/published/INDEX.md:48` lists both LNF and PP3 as "Ready for Joe to post" though both published 2026-07-23 (PP3 receipt in drafting-factory verified); RESEARCH-STATUS carries unqualified "Nguyen §3.1 RESOLVED" twice against its own SHIAB-02 row (verified) | multiple | |
| B15 | Promotion-notice path is specified three incompatible ways and the RESEARCH-STATUS/CANON path (`system/mailboxes/joeops/`) does not exist on disk; actual notices live in a fourth path (`joe-project-management/archive/`) — where 3 of 4 identifiable promotions DO have notices [lens, path checks verified] | `RESEARCH-STATUS.md:205`; `AGENTS.md:35`; template | |
| B16 | Signature-stale Pati-Salam verification: the 14d "128→64 complex" step is a non-invariant choice (`Cl⁰(7,7)` commutant is R — precisely Nguyen §3.1's objection), unlike the legitimate internal `ω²=−1` complex structure; file carries no staleness banner and ships inside the LNF zenodo package | `lab/active-research/pati-salam-chain-verification.md:118-125` | [lens] |
| B17 | The shiab real family is dim 16, not 8 (`End_Spin(S±_R) = H`, antilinear commutant exists — complexification cross-check 4×4=16); canon's "8 → 4 by the SAME J-commutation" is wrong in the starting number and the constraint name | `canon/shiab-existence-cl95.md:75,81` | [lens; measured commutant] |
| B18 | Environment/reproducibility: the documented `pip install -r requirements.txt` fails under PEP 668 on Homebrew Python; this machine's system interpreter lacks scipy/sympy, so sweeps report RED for environment reasons that read as mathematical ones (fixed in REPRODUCE.md 2026-08-02); no committed green-run baseline receipt exists; no Python CI; Lean CI has never built the working branches | `REPRODUCE.md` | Cheapest CRITICAL-adjacent fix: a dated 780/780 receipt + CI on non-main |

## Selected MINOR / hygiene (full details in session transcript)

Frontmatter carrying retracted verdicts (`external-datum-ledger…` title/outcome
still "P3-IS-NOT-EXTERNAL" against its own correction banner); three provably
wrong `updated_at` stamps (CANON.md contains a section 12 days newer than its
stamp); 32 of 55 `canon/` files carry non-canon YAML status under a README that
declares the whole directory citable, and the repo-wide status vocabulary has
~8 values outside the declared seven; W2Polynomial "certified_theorems" include
two content-free tautologies under physics-conclusion names; `K3IndexArithmetic`
"from signature" theorems are numeral checks; stale "DOI remains unset" text
inside the published deposit; RB7 doc says 29 controls, probe prints 30; the
"RK4" in H44 is globally 2nd-order (np.interp midpoints); H46's "1-dof σ" on a
non-nested point comparison; DR1/DR2 mixing in the theta-field canon file;
`docs/WHERE-GU-STANDS` recommends construction move to a separate repo while
Lane 1 runs it in-repo, with no supersession banner.

## Discards and corrections applied during verification

- Hostile referee's "75 unpushed commits" → they are pushed; unmerged to main.
- Strategist's "main is 502 commits behind" → 75 (verified).
- HB-02 downgraded CRITICAL→MAJOR: the certificate declares the framing
  identification as an input premise and lists the erasing branches openly.
- Literature scout's Scholtz–Geyer–Hahne attribution is secondary-source only
  (flagged by the lens itself); treat as to-verify before citing.
- `lab/process/computational-toolchain.md` (written 2026-08-02) overstated
  OQ-RK1 as CAS-blocked; the repo's own
  `tests/oq_rk1_e_rs_eff_assembly.py` returns BLOCKED_NEEDS_SPEC (the physical
  projector does not exist). Corrected in this session's edit to that file.
- The audit briefing treated the interior campaign as terminal; in fact
  `agent/null-clifford-omega1-repair` was committing the `pw2fr` campaign the
  morning of this audit (verified: commits through 2026-08-03 08:06). Lens
  conclusions about RB1–RB7 stand; "the interior is quiescent" does not.

## What held up (the audit's positive result)

The core Clifford/rep-theory spine (Cl(9,5)≅M(64,H) including the mod-8
convention subtlety — vacuous here since 4≡−4; MOVE-4's dim Hom = 0, re-derived
two independent ways; the full J_quat/Kramers structure; the −38 bookkeeping;
w₂(Y14) corrected form; the 9-signature class sweep). The Â degree-16 density
(reproduced by a third independent route) and both index cross-checks. The
Pati-Salam 19/19 quantum-number table. The DESI DR2 likelihood handling
(byte-verified data, correct covariances, exact amplitude profile, honest
f₀→0 guards) and the band-wide signal-level exclusion. H46C's headline
H0=63.75 (stable to 1.2e-5 across grid sweeps). MOVE-2's integrator. RB7's
Track B closed-form algebra and the exactness of the full residual (stable to
8 digits). The manuscript's claim-status table, six-caveat title block, ceded
priority, and `Hom(Z/3,Z)=0` self-limitation. The observer-value-selection
deposit's per-declaration Lean mapping (the template the ledger should copy).
`ResidualSelection.lean`'s actual theorems at full generality. Zero `sorry`/
`axiom`/`unsafe` across the entire Lean tree. VERIFICATION.md's conceded-
objection column. The dependency discipline on IC4, Assumption 3, W154, and
Proposition 1 (no downstream claim outranks them anywhere — checked). The
seed-routing seam's track record (~15 GU-origin seeds). LNF's novelty claim
(survived a fresh sweep; nearest neighbors are cite-and-distinguish, chiefly
Sati–Schreiber 2103.01877, which is absent from PRIOR-ART-DELTA and should be
added).

## The eleventh lens: certificate engineering (returned late; key items verified)

**A8 — 70 of 780 tracked certificates (9.0%) contain no assert, no raise, and
no exit call — they are unconditional PASSes in every sweep** [orchestrator
spot-verified on 4 named files]. The concentration is in the adversarial/
verify layer — the layer whose purpose is falsifiability: all 8
`tests/gu-independent/adv_verify_*`-class files, 5 of 9 `tests/hessian-z3/`
adversarial files, `forcing-slot/adv_verify_*`, `carrier-mass/verify_*`,
`source-action/verify_C_seesaw.py`. This contradicts REPRODUCE.md's "checks
it with hard asserts … exits nonzero if anything fails." Related [lens,
spot-verified]: MOVE-5's verify sibling ALSO prints "no-go NOT fully
established" and exits 0 (so primary and verifier are simultaneously
RED-in-prose, GREEN-in-exit-code); `gen_sector_bridge.py` — a library imported
by 112 certs whose docstring anchors are never executed — is itself counted
as a passing certificate (the harness has no certificate-shape predicate).

**Further cert-lens findings** [lens; F5 quote verified]: `pin14_smith_degree_gate.py`
is a literal-tautology gate — all seven checks restate constants assigned ten
lines above (confirming the homotopy lens's independent finding that the
Ω^{Pin+}₁₄ "gate" recites A(14)=1 rather than deriving it); one other file
(`gu-forces/verify_legb_intersection.py`) shares the pattern; four `a == a`-class
asserts in `pin_smith_class_realization_gate.py:146-151`; two paper
certificates are unreachable by any sweep root and the scope-audit gate takes
the harness's own root list as ground truth, so it cannot notice; a
`boundary-eta/verify/` "independent recheck" evaluates hand-typed closed
forms (no second derivation); documented "verified numpy 2.4.6" matches no
installed build, and 76 asserts use tolerances ≥1e-3 despite the "not
floating-point tolerances" rationale for pin-free requirements; silent
scipy-vs-Taylor `expm` fallbacks feed load-bearing numbers with no
consistency check; `gen_ch2_sx_from_codazzi.py` prints its headline −5376 but
asserts only the negative (`!= 24`); one seeded-RNG cert has a ~2.4% latent
false-FAIL (index-collision in sampling); `ghost_parity_krein.py`'s asserts
survive substituting the anti-self-dual triplet and the identity ambient
metric — it certifies a weaker statement than its docstring names.

**Cert-lens positive results (mutation testing):** 9 of 11 claim-breaking
mutations across 6 load-bearing certs correctly FAILED — the paper-cited
cores genuinely bind (MOVE-4's Hom-vanishing, MOVE-1's Â coefficients and
Sp(6) control, the Krein metric dependence of ghost_parity, both directions
of the APS eta cert — singled out as the best specimen in the repo: symbolic
derivation, closed-form cross-check, positive control BEFORE the decisive
result). Harness exit-code semantics are correct (FAIL/TIMEOUT/ERROR all
force RED — empirically confirmed); sys.path handling is robust; no asserts
are swallowed by broad excepts anywhere; RNG is deterministic except one
file. The full `--quick --tracked-only` sweep did NOT complete in its 29-min
window (and the harness never flushes stdout, so a redirected partial run
yields zero bytes — add `flush=True`).

## Recommended fix packet (mechanical first; claim-status items go through the repo's own workflow)

1. Merge/tag the release lineage onto `main`; name the SHA in REVIEWER.md;
   retarget README's onboarding block; track or de-advertise `main.pdf`;
   commit a dated green-run receipt; extend CI to working branches + a Python
   `--quick --tracked-only` job. (A1, B18)
2. Ledger truth pass: fix Lean ledger rows T2/T3 wording and add the missing
   file rows + gate coverage (A2); mark FC3 FIRED and banner the three
   consumer files (A4); correct RESEARCH-STATUS rows 134 (A7), 376-377/397
   (B14), the theta-file DR1/DR2 header; refresh LANE-STATE + portfolio
   states; reconcile published/INDEX.md; single promotion-notice path (B15).
3. Canon consequence-sentence pass (claim-status workflow): six-axis→seven-axis
   authority file (A5); OVERVIEW posture (A6); SHIAB-05 spurion sentence (B2);
   Frobenius "confirms" sentence (B1); C2 "94% global" (B10); MOVE-1 corrected
   coefficient propagation (B3); MOVE-5 terminal-criterion repair + carrier
   selector fix (A3).
4. Publication hygiene: Randal-Williams bibliography entry + spin-filling
   hypothesis via a versioned Zenodo correction when next convenient (B7);
   Sati–Schreiber added to PRIOR-ART-DELTA.
5. Numerics: adopt the exact-derivative rewrite for the RB/W177 pipeline
   (drops the floor ~6 decades and converts three "floor" verdicts to
   structural ones); replace the toolchain ARB-CERT example (done); upgrade
   the RB7 mixed-Gram statement to the exact 9/32 identity (B4, B5).
6. Harness hardening (A8): a certificate-shape discovery gate (no
   assert/raise/exit ⇒ discovery failure, with an explicit library allowlist);
   a literal-derivation gate (lands green-with-2-exceptions today); a
   mutation manifest for the frozen paper-cited set; `flush=True` on the
   per-cert print; a `requirements.lock` for the numeric certs (pip-tools is
   already in the venv); wire `reproduce_all.py --quick --tracked-only` plus
   `process_gates/` into CI.
