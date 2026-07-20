---
artifact_type: exploration
status: exploration (Section-A false-wall check; five personas inline, one worker, no sub-agents; deterministic exact-arithmetic probe, exit 0)
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (five-path fan-out: Dirac-Kahler chirality fork)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
title: "Dirac-Kahler chirality recount of the assumed truncated fermion content Omega^0 x S^+ + Omega^1 x S^- behind the pure-gravitational anomaly obstruction (net chirality -13, grav coeff 13/37800). FORK PROVENANCE: the FORM-DEGREE truncation (0-form + 1-form field slots) is PROGRAM-NATIVE (draft Sec 9.3, PDF p.46); the CHIRALITY assignment (S^+ to the 0-form, S^- to the 1-form, discarding the other Weyl halves) is NOT in the load-bearing source -- draft eq 9.16 carries the FULL Dirac bundle /S with all four components nu+-, zeta+- as distinct fields, and the draft itself calls the world 'fundamentally non-chiral' (p.62) -- so the chirality split is a reconstruction-level physics-default import with one loose native anchor (Sec 12.10 eq 12.22, author-footnoted 'speaking loosely'). RECOUNT: the -13 is EXACTLY the k=1 partial sum of the alternating binomial series sum_p (-1)^p C(14,p) whose completion is zero ((1-1)^14); closed form: truncation at level k gives W = (-1)^k C(13,k), nonzero for EVERY proper truncation, zero ONLY at the full tower. CONSEQUENCE (fork-conditional, per branch): the tr R^8 obstruction SURVIVES (13/37800) only on the chiral-truncation branch; it VANISHES IDENTICALLY on GU's own draft-literal Sec 9.3 content (full /S, vector-like) and on every geometer-complete Dirac-Kahler content (the 2^{14} form components = 64 quaternionic / 128 complex Dirac species, chirally balanced by the KNOWN DK species doubling); partial completions (e.g. Bianconi-style 0+1+2) MOVE it (-13/6300) but never zero it. NO branch is killed and NONE is promoted: the balanced branches trivialize the anomaly at the cost of having no interior chiral matter at all (chirality must then be external/emergent -- which is what the draft asserts and what this repo's own generation-sector canon already computed). Typed fork-conditional throughout; not a canon repair."
grade: "exploration / strong on the arithmetic, provenance-grade on the fork identification. The load-bearing computations are exact rational arithmetic, machine-checked (tests/channel-swings/dk_chirality_recount_probe.py, exit 0, 24 [E] + 6 [F], setup [T] = 7): the A-hat engine re-derived and re-cross-checked (canonical [A-hat]_4,8,12; the AGW degree-16 form; (K3)^4 -> 16 and (HP^2)^2 -> 0 end-to-end indices; p4 coeff -1/2419200), the baseline -13 / 13/37800 REPRODUCED before anything else, the Fierz counting 2^14 = 16384 = dim_R M(64,H) = 64 x 256 = (128)^2_C verified, the partial-sum identity sum_{p<=k} (-1)^p C(14,p) = (-1)^k C(13,k) verified for all k, and every content row's W and coefficient computed fresh (no cached coefficient trusted). The PROVENANCE finding is a reading of the primary source (draft PDF pp.46-49, 62-63) plus the repo record (anomaly-audit 2026-06-22, vz-evasion 2026-06-23, MOVE1-01); it is citation-backed but not machine-checkable. No claim/canon/verdict/posture movement; the global 2-primary Dai-Freed leg is untouched and stays OPEN. Zero em dashes."
construction: "Fork-typed per GEOMETER-VS-PHYSICS-OBJECTS.md, and this swing IS the discipline: every content candidate is NAMED with its construction. C0 (repo baseline) = form slots native + chirality split IMPORTED (standard chiral-anomaly template); C1 = draft-literal Sec 9.3 (native, full /S); C2 = full Dirac-Kahler forms-as-spinors (geometer-complete standard construction, externally suggested by the Bianconi intake but evaluated on GU's own Cl(9,5) = M(64,H)); C3/C5b/C5c = chirality-assignment templates (imports, used to map the fork surface); C5 = the draft 10.10 deformation-complex skeleton (native skeleton, author-disclaimed 'Caveat Emptor'). Standard-field machinery that binds any construction: the A-hat genus, Alvarez-Gaume-Witten anomaly polynomial structure, binomial arithmetic, Dirac-Kahler/Becher-Joos/Rabin forms-spinors dictionary, Nielsen-Ninomiya doubling."
depends_on:
  - docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md   # Section A, MOVE1-01
  - tests/ahat_genus_y14_i16.py
  - tests/chase/MOVE-1/move1_octic_sp64_vs_sp1.py
  - tests/chase/MOVE-1/verify/indep_ahat16.py
  - tests/sp64_octic_trace_i16.py
  - explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md
  - explorations/internal-paths-2026-07-03/anomaly-sp64-i16-daifreed.md
  - explorations/vz-evasion/vz-14d-mixed-covectors-2026-06-23.md
  - explorations/intake-bianconi-entropic-gravity-2026-07-20.md   # leg 3, the trigger
  - explorations/W232-close-a5-signature-witten-anomaly-2026-07-14.md
  - canon/h2-base-index-chirality.md
  - tests/nielsen-ninomiya/nn_domain_wall_records_as_rows.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - Geometric_UnityDraftApril1st2021.pdf   # Sec 9.3 (p.46), 10 (pp.47-49), 12.9-12.10 (pp.62-63)
scripts:
  - tests/channel-swings/dk_chirality_recount_probe.py
external_refs:
  - "Kahler, E., Der innere Differentialkalkul, Rend. Mat. 21 (1962) 425 -- forms as spinor fields."
  - "Becher, P. and Joos, H., The Dirac-Kahler equation and fermions on the lattice, Z. Phys. C15 (1982) 343 -- the 2^{d/2}-fold species content of the DK field."
  - "Rabin, J.M., Homology theory of lattice fermion doubling, Nucl. Phys. B201 (1982) 315 -- DK degeneracy = lattice doubling."
  - "Nielsen, H.B. and Ninomiya, M., Absence of neutrinos on a lattice, Nucl. Phys. B185 (1981) 20 -- no net chirality without breaking the doubling symmetry."
  - "Alvarez-Gaume, L. and Witten, E., Gravitational anomalies, Nucl. Phys. B234 (1984) 269 -- the A-hat/index anomaly-density machinery and the tr R^8 term."
  - "Bianconi, G., Gravity from entropy, arXiv:2408.14391; discrete precursor arXiv:2404.08556 -- Dirac-Kahler (untruncated forms-as-spinors) matter content; intake pointer only, untrusted data."
---

# The Dirac-Kahler chirality fork: is the -13 a fact about GU or a fact about a truncation?

## 0. The charge and the one-paragraph answer

Section A of WHERE-GU-STANDS rests one pillar on this: the pure-gravitational anomaly term
(the tr R^8 coefficient of [A-hat(TY14)]_16, p4 coeff -1/2419200) is nonzero ONLY because the
ASSUMED truncated fermion content `Omega^0 x S^+ (+) Omega^1 x S^-` has net chirality
`n_+ - n_- = 1 - 14 = -13` (grav coefficient 13/37800). The repo has always stamped this
"conditional on the assumed fermion content". This swing runs the geometer-vs-physics fork
discipline ON that content. The answer: the truncation is HALF native. The form-degree part
(fields = 0-form and 1-form spinors) is GU's own; the CHIRALITY split is not derived in the
load-bearing source and enters as a standard-field import. On GU's draft-literal content and on
every geometer-complete Dirac-Kahler content the obstruction vanishes identically; on the
chiral-truncation branch it survives at exactly 13/37800. Every outcome is fork-conditional.
Nothing moves in canon.

## 1. Fork provenance (question 1: native or import?)

The assumed content has two separable ingredients. They have different provenance.

### 1.1 The form-degree truncation (only p = 0 and p = 1): PROGRAM-NATIVE

- Draft Sec 9.3, PDF p.46: "For nu, nu-bar in Omega^0(Y, /S) and zeta, zeta-bar in
  Omega^1(Y, /S) we can begin with operators like: [eq 9.16]". The fermion FIELDS of GU are
  exactly the 0-form spinor nu and the 1-form spinor zeta. The higher form degrees that appear
  (Omega^{d-1}(Y,/S), Omega^d(Y,/S) in eqs 9.18-9.19 and diagram 10.10) are EQUATION/codomain
  spaces of the deformation complex, not additional independent fields.
- Corroborated by the UCSD talk record (lab/literature/weinstein-ucsd-2025-04-transcript.md via
  DERIVATION-PROGRESS RS-BRST entry): "zero-form and one-form linearized field content", with the
  middle differential to Omega^{d-1} named as the open hard part.
- So restricting the FIELD content to p in {0, 1} is not an import. GU is not a Dirac-Kahler
  theory in its own words; its field list is a 2-slot truncation of the form tower BY DESIGN.

### 1.2 The chirality assignment (S^+ to the 0-form, S^- to the 1-form): IMPORT with one loose native anchor

- The load-bearing field-content display, draft eq 9.16 (p.46), values BOTH fields in the FULL
  Dirac bundle /S: the operator matrix acts on the four-component column (zeta_+, zeta_-, nu_+,
  nu_-) against (zeta-bar_-, zeta-bar_+, nu-bar_-, nu-bar_+). All four Weyl components of both
  fields are present as distinct classical fields. Nothing in Sec 9.3 discards nu_- or zeta_+.
- The draft's own physical posture is the OPPOSITE of a chiral truncation: p.62 (Sec 12.9), "a
  fundamentally non-chiral world of Dirac Spinors in this simplified example would appear chiral
  in regions of low scalar gravity". GU asserts fundamental non-chirality with apparent/emergent
  chirality.
- The one native anchor for the pairing: Sec 12.10, eq 12.22 (p.62) displays
  `zeta in Omega^1(Y, /S_R)` with part of it "an ordinary second generation spinor in
  Omega^0(Y, /S_L) via the Dirac gamma matrix contraction". That is a 1-form-with-R /
  0-form-with-L pairing hint -- but it sits in the speculative 2+1-generations section, is
  author-footnoted "we are speaking loosely here" (footnote 13), and contradicts the Sec 9.3
  field list if read as a Weyl truncation of the fields.
- Where the truncation actually entered the repo:
  `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md` Sec 2.6 states
  "The fermion content in GU (from Weinstein's construction) is: Psi = (Omega^0(Y14) x S^+) (+)
  (Omega^1(Y14) x S^-)" -- with NO draft citation for the chirality split, in a passage whose
  neighboring structural statements are tagged `[reconstruction]`. The vz-evasion reconstruction
  (vz-14d-mixed-covectors-2026-06-23.md Sec "Operator") then fixed
  `E = (Omega^0 x S^+) (+) (Omega^1 x S^-)` as the domain of the Dirac-type symbol, and
  `tests/sp64_octic_trace_i16.py` / MOVE-1 inherited it as "the assumed chiral content".
- Why the import happened (named honestly): a perturbative anomaly computation is VACUOUS for a
  vector-like content, and the standard-field template for "the chiral content of a Dirac-type
  operator between two bundles" is to take opposite Weyl halves on domain summands. That is the
  physics default doing the work, not a GU derivation.
- Independent corroboration that the chirality is not internally forced, from this repo's OWN
  canon on a different line: `canon/h2-base-index-chirality.md` -- T1a computed net chirality 0
  for GU-native kinematics and the file's verdict splits "multiplicity (native)" from
  "net-chirality (not internally forced)". The anomaly line's -13 sits on the far side of exactly
  that fork.

### 1.3 Fork verdict

**The recount is a FORK-CONDITIONAL statement, not a repair.** The -13 content is not
program-derived: its form-degree half is native, its chirality half is a reconstruction-level
standard-field import whose only native anchor is a "speaking loosely" display. But the balanced
alternatives are not program-FORCED either: GU's fermionic action is never stabilized (draft
eq 10.10, "Caveat Emptor", PDF p.49), so no reading of the content is theorem-grade. The fork
stays open; the table below populates it.

## 2. Fierz / dimension sanity (question 4)

All verified exactly in the probe (Part 2):

- `dim_R Lambda^*(R^14) = 2^14 = 16384 = dim_R M(64,H) = dim_R Cl(9,5)` (the Clifford/exterior
  vector-space isomorphism, on GU's own corrected algebra).
- As a left module over itself, `M(64,H)` = 64 copies of `S = H^64` (`64 x 256 = 16384`): the
  Dirac-Kahler field on Y^14 is 64 quaternionic Dirac species.
- Complexified: `2^14 = 128 x 128`, i.e. `Lambda^*_C ~= S_C (x) S_C^*` -- 128 complex Dirac
  species of the 128-dim complex spinor. This is the DK Fierz count; the d = 4 lattice control
  `2^4 = 4 x 4` (4 species) is verified alongside.
- Each species splits `S = S^+ (+) S^-` (128 + 128 real; volume element omega^2 = +1 for
  p - q = 4 mod 8) and the split is species-wise, so the full DK content has
  `n_+ = n_- = 64` exactly: **chirally balanced, by the known species-doubling mechanism**
  (Becher-Joos, Rabin), not by accident.

## 3. The recount and the anomaly consequence (questions 2 and 3)

Probe: `tests/channel-swings/dk_chirality_recount_probe.py` (exit 0). The A-hat machinery is
RE-DERIVED inside the probe and re-cross-checked (canonical [A-hat]_4,8,12; the full AGW
degree-16 form over 464486400; end-to-end indices (K3)^4 -> 16 and (HP^2)^2 -> 0; p4 coeff
-1/2419200), and the baseline is REPRODUCED before any new row is computed. Convention identical
to MOVE-1: coeff = 64 * W * (-1/2419200) with W = n_+ - n_-; the survive/vanish verdict is
proven normalization-independent (coeff = 0 iff W = 0, checked under three normalizations).

**The structural identity (new, and the sharpest single fact of the swing):** for the
alternating-chirality tower `Omega^p x S^{(-1)^p}`, truncation at level k gives

    W_k = sum_{p=0}^{k} (-1)^p C(14,p) = (-1)^k C(13,k)

verified for all k = 0..14. The baseline -13 is EXACTLY the k = 1 entry, `-C(13,1)`. Every
proper truncation (k = 0..13) is nonzero; the series balances ONLY at the full tower
(k = 14, the binomial identity (1-1)^14 = 0). The -13 is literally the first partial sum of an
alternating series whose completion is zero.

| # | Content (construction named) | W = n_+ - n_- | tr R^8 coeff | Obstruction |
|---|---|---|---|---|
| C0 | Repo baseline `Om^0 x S^+ + Om^1 x S^-` (form slots native; chirality IMPORT) | -13 | 13/37800 | **SURVIVES** |
| C0m | Mirror `Om^0 x S^- + Om^1 x S^+` (import, sign choice) | +13 | -13/37800 | SURVIVES (sign moves) |
| C1 | **Draft-literal Sec 9.3**: nu, zeta in `Om^{0,1}(Y,/S)`, full Dirac (NATIVE) | 0 | 0 | **VANISHES** |
| C2 | **Full Dirac-Kahler** `Om^0..Om^14` forms-as-spinors = 64 copies of S (geometer-complete) | 0 | 0 | **VANISHES** |
| C3 | Alternating-chirality DK tower `Om^p x S^{(-1)^p}`, p = 0..14 (template completion) | 0 | 0 | **VANISHES** |
| C4 | Bianconi-style partial completion 0+1+2, alternating (partial, structurally motivated) | +78 | -13/6300 | MOVES |
| C5 | Draft 10.10 deformation-complex skeleton `Om^0, Om^0+Om^1, Om^13, Om^14`, full-/S slots (native skeleton) | 0 | 0 | VANISHES |
| C5b | Chiral 4-slot reading (+,-,+,-) of the 10.10 skeleton (template) | 0 | 0 | VANISHES |
| C5c | Chiral 4-slot Hodge-paired (+,-,-,+) (template) | -26 | 13/18900 | MOVES |

Notes on honest completions (question 2's "what does completed mean in GU's setup"):

- The completion arena is Y^14, not X^4: the obstruction [A-hat(TY14)]_16 lives on the 14-dim
  total space, so the DK completion evaluated is `Lambda^*(Y^14)`. (A base-level `Lambda^*(X^4)`
  DK story -- Bianconi's actual habitat -- bears on the SM-boundary line, not on this term.)
- There are at least TWO inequivalent honest completions (C2 full-/S and C3
  alternating-chirality) and one native non-completion that is already balanced (C1). They agree:
  W = 0. The 10.10 skeleton (C5), read with its native full-/S slots, is also balanced; only
  chirality-template variants of it (C5c) are not.
- The gauge channel carries the SAME weight W (MOVE-1 convention), so a balanced content zeroes
  the entire conditional local I_16 top-line, not just the tr R^8 term (probe check E-gauge).

**Consequence per branch (all fork-conditional):**

- **Branch A (chiral truncation, import-flagged):** the pure-gravitational obstruction SURVIVES,
  exactly 13/37800. The wall is real ON THIS BRANCH.
- **Branch B (draft-literal Sec 9.3, full /S):** the obstruction VANISHES IDENTICALLY. The
  content is vector-like; the local anomaly is zero for the trivial reason that there is no net
  chirality to be anomalous.
- **Branch C (geometer-complete Dirac-Kahler, full or alternating):** VANISHES IDENTICALLY, by
  the species-doubling balance; and the partial-sum closed form shows completion is the UNIQUE
  balancing point of the alternating tower.
- **Partial completions (incl. the Bianconi-shaped 0+1+2):** the obstruction MOVES (-13/6300)
  but never vanishes. There is no "small repair" of the truncation that kills the term; only
  full balance does.

**What this does NOT do:** it does not repair, kill, or promote anything. The local
non-factorizability finding (MOVE1-01) was ALREADY stamped conditional on the content; this
swing converts that stamp from a caveat into a populated fork table and shows the conditional
branch is load-bearing (the other branches zero the term). The global 2-primary Dai-Freed leg
is untouched (and W232 separately showed the Witten Z/2 vanishes on (9,5)); vanishing of the
LOCAL term on a branch is necessary-not-sufficient for anomaly freedom on that branch.

## 4. Council pass (five lenses, inline)

**Anomaly specialist (A-hat/index arithmetic).** The engine was re-derived, not imported from
the repo's own cached file, and re-pinned by two independent end-to-end indices; the p4
coefficient matches AGW. The per-content coefficient is linear in W, so the entire fork table
reduces to exact integer arithmetic on binomials; the survive/vanish verdict is
normalization-independent (checked). One caution stands: a vector-like content zeroes the
PERTURBATIVE anomaly identically -- that is a triviality, not a cancellation mechanism, and it
says nothing about the 2-primary global leg. Signed off.

**Representation theorist (Cl(9,5) = M(64,H) dictionary).** The forms-spinors dictionary holds
on GU's corrected algebra: Lambda^* ~= Cl(9,5) as Spin(9,5)-modules (vector-space iso), the
left-regular decomposition gives exactly 64 copies of S = H^64, the right-H (Sp(1) commutant)
action commutes with the left Clifford action and preserves the chirality blocks, and
omega^2 = +1 (p - q = 4 mod 8) makes the S^+/S^- split well-defined. The quaternionic structure
does not obstruct the count: each S^+/S^- is H^32 internally, and the balance n_+ = n_- = 64 is
exact. Signed off, with the note that C3's chirality assignment (-1)^p is an extra grading NOT
canonically supplied by the Clifford dictionary -- correctly typed as a template.

**Lattice / discrete theorist (the doubling subtlety -- the mandated check).** Yes: the
completion reintroduces balance PRECISELY by species doubling, and this is the KNOWN DK fact
(naive DK = 2^{d/2} degenerate Dirac species; in d = 4 the famous 4-fold staggered degeneracy;
here 128-fold complex / 64-fold quaternionic, verified). Is that legitimate or a cheat? On a
smooth manifold it is not a discretization artifact: the continuum DK complex genuinely IS
vector-like. The Nielsen-Ninomiya lesson cuts the other way: obtaining NET chirality from a
form-valued (geometrically complete) fermion field requires breaking the doubling symmetry --
i.e., a truncation/projection -- and no local, symmetric, doubling-free chiral projection
exists. So the -13 branch is exactly a "chirality by truncation" move, and the repo's own
domain-wall line (tests/nielsen-ninomiya/, the "external by structure" canon) already holds
that GU-native interiors are balanced and chirality must arrive from a boundary/external
mechanism. The recount is CONSISTENT with that: balanced interior content, obstruction zero,
chirality (and any surviving anomaly) pushed to the boundary leg. Signed off.

**GU-native geometer (what the program's documents force).** The documents force the 0/1-form
field slots (Sec 9.3) and nothing more. They do NOT force the Weyl truncation; eq 9.16 is
explicitly full-/S, the fermionic action is author-disclaimed (10.10 "Caveat Emptor"), and the
draft's stated physics is "fundamentally non-chiral... would appear chiral" -- which, read
plainly, PREDICTS a balanced fundamental content with apparent chirality emerging in a regime,
i.e. branch B/C behavior. The only pro-truncation datum is the loose Sec 12.10 pairing. On the
documents alone, the balanced reading is closer to GU's own posture than the truncated one; but
"closer to posture" is not "derived", and the unwritten source action could stabilize either.
The fork is genuinely open; the geometer declines to promote a side.

**Adversarial referee (are the completions imports in disguise?).** Three attacks. (1) "The DK
completion is a Bianconi import dressed as geometry." Partially sustained: C2/C3 are
externally-SUGGESTED completions -- but the vanishing verdict does NOT depend on them, because
the draft-literal C1 (no completion, no import, just Sec 9.3 read as written) already gives
W = 0. The import objection cannot rescue the truncation. (2) "The barred fields / Berezin
structure of 9.16 might encode an effective chiral asymmetry" (the zero lower-right quadrant of
the 9.16 operator IS an asymmetry, and the draft notes versions "with a non-trivial map in the
lower right quadrant"). Sustained as a residual: the 9.16 operator is author-flagged unstable,
and no reconstruction-grade extraction of a Weyl truncation from it exists; if the stabilized
source action ever forces one, branch A revives natively. This is the sharpest open door and it
is recorded, not waved away. (3) "A balanced content proves too much: it makes GU anomaly-trivial
AND chirality-free, so the recount is a Pyrrhic zero." Correct and accepted: on branches B/C the
obstruction vanishes because there is no interior chiral matter at all, so those branches must
supply observed chirality externally (domain-wall/boundary/emergence) -- which is precisely the
repo's standing "external by structure" characterization and the draft's own claim. The referee
certifies the typing: no branch killed, no branch promoted, all outcomes conditional.

## 5. Honest typing

- **Type of every outcome: FORK-CONDITIONAL.** The -13 / 13/37800 result remains true AS
  STATED (it was always stamped conditional); what is new is the populated fork table and the
  provenance finding that its conditioning assumption's chirality half is an import, its
  form-degree half native.
- **The MAJOR-finding row exists and is typed, not promoted:** contents that zero the
  obstruction include GU's OWN literal Sec 9.3 field content. Under the mission's typing rule
  this is a fork-conditional statement -- the pure-gravitational wall is a property of the
  chiral-truncation branch, not of every honest reading of GU's fermion content.
- **What would move it:** a stabilized source action (the Section-B missing object) that forces
  a Weyl structure on (nu, zeta) would collapse the fork to branch A natively (wall hardens,
  import stamp removed); one that forces full-/S or a DK extension collapses it to B/C
  (obstruction gone locally, anomaly question migrates entirely to the global 2-primary leg and
  the boundary/inflow mechanism). Either way the fork table above is the decision surface.
- No claim-status, canon-verdict, or public-posture change. CANON.md's MOVE1-01 row needs no
  edit: its "EXPLICITLY CONDITIONAL on the assumed truncated fermion content" stamp is exactly
  the fork this document populates.

## 6. Receipts

- Probe: `tests/channel-swings/dk_chirality_recount_probe.py` -- deterministic, exact Fraction
  arithmetic, no RNG, no numpy. Run 2026-07-20: exit 0,
  `HEADLINE: 24 [E] + 6 [F] = 30 (setup [T] = 7 excluded) ALL PASS`.
  Reproduces the baseline (-13; 13/37800) BEFORE computing any new row; re-derives the A-hat
  engine with the canonical low-degree, AGW degree-16, and two end-to-end index cross-checks.
- Primary source: `Geometric_UnityDraftApril1st2021.pdf` -- Sec 9.3 field content and eq 9.16
  (PDF p.46); eqs 9.18-9.19 codomain tower (p.46); diagram 10.10 + "Caveat Emptor" (p.49);
  "fundamentally non-chiral world of Dirac Spinors" (Sec 12.9, p.62); eq 12.22 and the /S_R //S_L
  pairing with footnote 13 "speaking loosely" (pp.62-63).
- Repo provenance chain for the truncation: anomaly-audit-cl95-gauge-group-2026-06-22.md
  (Sec 2.6, first appearance, no draft citation for the split) -> vz-14d-mixed-covectors
  2026-06-23 (operator domain fixed) -> sp64_octic_trace_i16.py (ANOMALY-04) ->
  move1_octic_sp64_vs_sp1.py + verify/indep_ahat16.py (MOVE1-01) ->
  WHERE-GU-STANDS Section A.
- Consistency cross-references: canon/h2-base-index-chirality.md (net chirality not internally
  forced); tests/nielsen-ninomiya/nn_domain_wall_records_as_rows.py (balanced interior, boundary
  chirality); W232 (global Z/2 leg independent of this fork).

## 7. Boundary (what this swing does NOT establish)

- It does not decide the fork. GU's source never stabilizes the fermionic action; both the
  truncated and balanced readings remain live constructions.
- It does not make GU anomaly-free on any branch: branches B/C zero the LOCAL term only; the
  global 2-primary Dai-Freed/eta leg stays OPEN as before.
- It does not touch the Sp(64)-vs-Sp(1) gauge-reading question (the gravitational channel is
  reading-independent; the gauge rows inherit MOVE1-01's resolution unchanged).
- It does not evaluate Bianconi's theory; the intake is a shape-trigger only, and the decisive
  balanced candidate (C1) is GU's own text, not an import.
- The referee's residual door stands: a stabilized eq 9.16/10.10 could yet force a chiral
  structure and re-nativize branch A. That is the precise object (Section B spec sheet) this
  repo already names as the missing one.
