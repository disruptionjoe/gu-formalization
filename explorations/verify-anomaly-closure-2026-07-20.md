---
artifact_type: exploration
doc_type: adversarial_verification
status: "second dry round (hostile verifier), anomaly-closure result pair; independent re-derivation probe exit 0; no edits to any target file"
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (summit wave: second dry round, anomaly closure)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
title: "Second-dry-round adversarial verification of the anomaly-closure pair (dk-chirality-fork 2f06e7f + global-anomaly-leg 4b83f4b). VERDICT: DRY -- no material revision found after a genuine break attempt. Every load-bearing number re-derived by an independent route where one exists (Bernoulli-route A-hat, from-scratch fixture Pontryagin numbers, splitting-principle Euler product, residue-route a_k = C(16-k,2), Newton-identity Kramers, own AHSS lines); the provenance claim re-verified against the primary source with an honest counter-evidence hunt that found ADDITIONAL confirming evidence (draft p.64 item iii: 'unadorned non-chiral Dirac spinors') and no refuting passage. Three strengthenings, no refutations: (1) ch(G) of the bounding extension vanishes identically through weight 6 (not just the weight-4 density), which also kills the gauge-twisted (S2) extension density -- closing a receipt gap the original probe did not cover; (2) Omega~^spin_5(BSp(64)) = Z/2 DERIVED by AHSS (was flagged unsourced-candidate); (3) the honest C0 p4 coefficient 493/2419200 confirmed by an independent power-sum computation."
grade: "adversarial verification / all recomputation exact rational arithmetic, machine-checked (tests/channel-swings/verify_anomaly_closure_probe.py, exit 0, HEADLINE 50 [E] + 6 [F] = 56, setup [T] = 5). Primary-source pass over all 69 draft pages (full-text extraction; every chiral/Weyl/handed/non-chiral hit read in context). Bordism table corroborated against Tachikawa-Yonekura arXiv:2108.13542 App. A values via web check (13,14,15 = 0; 16 = Z^5; ABP67/Gia71). The ABP wedge shape, Borel BSp degrees, Bott ladder, and Witten's multiplicity rule remain table/theorem inputs here exactly as in the targets (flagged [T]); nothing in this pass depends on trusting the targets' code. Zero em dashes."
construction: "Verification pass only; no new mathematical object is proposed. Route independence enforced per check: where the target used sinh-reciprocal + Newton power sums, this pass uses e^{x/2} x/(e^x-1) with exact Bernoulli numbers; where the target quoted fixture Pontryagin numbers, this pass derives them from nilpotent product algebra; where the target summed coefficient polynomials, this pass computes the K-theory Euler product and the [t^14] residue closed form; where the target used Faddeev-LeVerrier, this pass uses Newton's identities on a different quaternionic fixture."
depends_on:
  - explorations/dk-chirality-fork-2026-07-20.md            # target 1 (commit 2f06e7f)
  - tests/channel-swings/dk_chirality_recount_probe.py      # target 1 probe (read, not re-run)
  - explorations/global-anomaly-leg-2026-07-20.md           # target 2 (commit 4b83f4b)
  - tests/channel-swings/global_anomaly_leg_probe.py        # target 2 probe (read, not re-run)
  - explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md
  - papers/drafts/canonical-structures-14d-metric-geometry-2026-06-22.md
  - lab/process/prediction-package-standing-rule.md         # point 8: two-dry-rounds gate
  - Geometric_UnityDraftApril1st2021.pdf                    # primary source, full-text pass
scripts:
  - tests/channel-swings/verify_anomaly_closure_probe.py
external_refs:
  - "Tachikawa, Y. and Yonekura, K., arXiv:2108.13542 App. A -- Omega^spin table values corroborated by web check this session (13:0, 14:0, 15:0, 16:Z^5; ABP67, Gia71)."
  - "Anderson-Brown-Peterson 1967; Giambalvo 1971; Wall 1960; Borel 1953; Bott 1959; Witten 1982 -- same theorem-grade inputs as the targets, used as [T] inputs here too."
---

# Second dry round: hostile verification of the anomaly-closure pair

## 0. Charge and verdict

Under the stopping rule (lab/process/prediction-package-standing-rule.md, point 8), the
anomaly-closure paper ships only after a second consecutive adversarial pass with no material
revision. This is that pass, run to BREAK the pair:

- Target 1: explorations/dk-chirality-fork-2026-07-20.md + dk_chirality_recount_probe.py (2f06e7f)
- Target 2: explorations/global-anomaly-leg-2026-07-20.md + global_anomaly_leg_probe.py (4b83f4b)

Method: re-derive (not re-run) every load-bearing number by a DIFFERENT route where one
exists; re-read the primary source behind the provenance claim and hunt for counter-evidence
that would refute it; attack the two weakly-sourced bordism inputs; attack the framing.

**VERDICT: DRY.** No material revision. No refutation. Three strengthenings and two
non-material nuances, listed below. The paper may proceed under the stopping rule.

## 1. Per-claim verdict table

Probe: tests/channel-swings/verify_anomaly_closure_probe.py, run 2026-07-20, exit 0,
`HEADLINE: 50 [E] + 6 [F] = 56 (setup [T] = 5 excluded) ALL PASS`.

| # | Claim | Verdict | Independent route used |
|---|---|---|---|
| 1a | Chirality split absent from draft Sec 9.3; import first appears in the 2026-06-22 audit with no draft citation | **CONFIRMED (+ strengthened)** | Full-text primary-source pass, all 69 pages; every chirality-related hit read in context (Sec 2). Repo chain re-verified at commit granularity: audit 6150a8d 06-22 22:30 (Sec 2.6, no citation) precedes the canonical-structures draft d99501d 06-22 23:30 (Construction 5.4, also citation-free, [reconstruction grade]-tagged) |
| 1b | Draft-literal (C1) and completed DK contents give W = 0, tr R^8 coefficient vanishes | **CONFIRMED** | Direct dimension counting of all nine fork rows (V2); curvature-honest confirmation at density level: full-tower exact degree-16 density = 0, every per-slot density nonzero, every proper truncation nonzero (V4) |
| 1c | -13 = the k = 1 partial sum of (1-1)^14; W_k = (-1)^k C(13,k) | **CONFIRMED** | Pascal-induction identity checked for all k = 0..14; -C(13,1) = -13; unique balancing point k = 14 (V2) |
| 2a | Omega^spin_13 = Omega^spin_14 = Omega^spin_15 = 0, Omega^spin_16 = Z^5, all spin torsion 2-primary | **CONFIRMED at table grade** | Literature web check (TY 2108.13542 App. A values: 13,14,15 = 0; 16 = Z^5) + own re-encoding of the ABP wedge extended to the full n = 0..16 window + ranks by Euler pentagonal recurrence p(3) = 3, p(4) = 5 (V3). The ABP shape and Wall's theorem remain [T] inputs, exactly as the target flagged |
| 2b | KO_15 = KSp_15 = 0 (both reality types Bott-dead at 15) | **CONFIRMED** | KSp_n = KO_{n+4} arithmetic: 15 -> 7 mod 8 and 19 -> 3 mod 8 both dead; live positive control KSp_5 = KO_9 = Z/2 (V3) |
| 2c | C3 alternating density identically zero; K-theory Euler class lowest degree 28 > 16 | **CONFIRMED (+ sharpened)** | Splitting-principle product route: sum_p (-1)^p ch(Lambda^p V_C) computed as prod_i (2 - 2cosh x_i) at weight cap 7; equals the coefficient-sum route exactly, vanishes at ALL weights 0..6, and the weight-7 part is EXACTLY -e_7 (V4). Gauge-mixed channels die with it (any ch(R) factor cannot lower the weight) |
| 2d | eta-bar = 0 exactly on the bounding extension; a_k = (15-k)(16-k)/2 | **CONFIRMED (+ receipt gap closed)** | a_k re-derived independently by the residue identity G = [t^14] lambda_t(TZ_C)(1+t)^{-3}, giving a_k = C(16-k,2) = (15-k)(16-k)/2 with the truncation self-terminating (a_15 = a_16 = 0); ch(G) verified ZERO at all weights 0..6 with lowest term exactly -e_7(u_1..u_8), matching the subset-expansion prediction; negative control (truncation at 13) leaves rank -120 (V5). See Sec 3 for the S2 receipt gap this closes |
| 2e | The 5d Witten Z/2 is killed by even quaternionic multiplicity | **CONFIRMED arithmetic / REPRODUCED-ONLY mapping** | pi_4(Sp(N)) = Z/2 and the parity arithmetic (64, 0, 128 all even; single-doublet control odd) are confirmed; the mapping "GU content -> number of pseudoreal multiplets mod 2" is Witten's rule, an imported physics input not independently derivable here (same [T] status as in the target) |
| 2f | The Z/24 arena is disjoint (no odd torsion in the spin ledger) | **CONFIRMED** | Window-level no-odd-torsion check on the derived table + Hom(Z/3, Z) = Hom(Z/3, Z/2^k) = 0 + Omega^spin_3 = 0 (V3); the all-dimensions statement rests on Wall + ABP, theorem-grade [T], as flagged |
| -- | Flagged weak input: Omega~^spin_15(BSp(64)) = 0 (repo W232 AHSS) | **CONFIRMED by own derivation** | Own AHSS line from Borel degrees: E2_{4,11} = E2_{8,7} = E2_{12,3} = 0 because Omega^spin_{11,7,3} = 0; an all-zero line admits no extension (V3) |
| -- | Flagged weak input: Omega~^spin_5(BSp(64)) unsourced, candidate Z/2 | **CONFIRMED and UPGRADED to derived Z/2** | Own AHSS: E2_{4,1} = Z/2 is the only entry on the line; every differential in or out lands in a zero group (H~_{2,1,0,6} = 0), so E_infinity = Z/2 exactly (V3). Harmless to the closure either way (64 even), as the target said |

Supporting engine checks (all independent route): A-hat coefficients [A-hat]_4,8,12,16 via
the Bernoulli expansion Q(x) = e^{x/2} x/(e^x - 1); p4 coefficient -1/2419200; fixture
Pontryagin numbers of (K3)^4 and (HP^2)^2 DERIVED from nilpotent product algebra (not
quoted) with end-to-end indices 16 = (A-hat(K3))^4 and 0; the honest twisted C0 p4
coefficient 493/2419200 recomputed and ALSO confirmed analytically by power sums
(D_1 p4 = 14(-1/2419200) - 1/5040 = -494/2419200, so D_0 - D_1 gives 493/2419200);
Kramers perfect-square charpoly on a NEW quaternionic fixture via Newton's identities,
with the J-commutation verified as a matrix identity and the non-J control non-square.

## 2. The provenance counter-evidence hunt (the honest part of the attack)

The full draft text was extracted (69 pages) and every occurrence of chiral / non-chiral /
Weyl / handed / "speaking loosely" was read in context. Findings:

**Quotes verified verbatim.** (i) Sec 9.3, PDF p.46: "For nu, nu-bar in Omega^0(Y, /S) and
zeta, zeta-bar in Omega^1(Y, /S) we can begin with operators like: [eq 9.16]" -- and the
9.16 display carries the full four-component column (zeta_+, zeta_-, nu_+, nu_-) against
(zeta-bar_-, zeta-bar_+, nu-bar_-, nu-bar_+): all four Weyl components present as distinct
classical fields, nothing discarded; the "other versions ... with a non-trivial map in the
lower right quadrant" remark is there as the fork doc says. (ii) Sec 12.9, p.62:
"a fundamentally non-chiral world of Dirac Spinors in this simplified example would appear
chiral in regions of low scalar gravity" -- verbatim. (iii) Sec 12.10, pp.62-63: "part of
the field zeta in Omega^1(Y, /S_R) is an ordinary second generation spinor in
Omega^0(Y, /S_L) via the Dirac gamma matrix contraction" -- the loose pairing anchor, in
the speculative 2+1-generations section, as characterized.

**Counter-evidence hunt result: NONE FOUND, and the opposite.** No passage anywhere in the
draft assigns S^+ to the 0-form and S^- to the 1-form or discards the complementary Weyl
halves of the fields. The hunt instead found a passage the fork doc did NOT cite, which is
the strongest single provenance datum available: **p.64, Sec 12.11, summary item (iii) of
"the strongest claims of the strongest form of Geometric Unity": "Fermions on X4 are
pullbacks g*(nu) and g*(zeta) of unadorned non-chiral Dirac spinors nu in Omega^0(Y, /S)
and 1-form valued spinors, zeta in Omega^1(Y, /S) on Y. In low gravitational regimes, the
equations governing the fractional spin fields decouple leading to emergent effective
chirality that disguises the non-chiral fundamental theory."** This is an explicit,
summary-grade statement that the field content is full-/S and non-chiral with chirality
emergent -- i.e. draft-literal C1, exactly the branch on which the local obstruction
vanishes. Recommendation (non-blocking): the paper should cite p.64 item (iii) as the
primary provenance anchor; it is stronger than the Sec 9.3 display read alone.

Other sites checked and cleared as non-forcing: Sec 3 (p.23) Weyl-left/right as null dual
GL(64,R) representations (kinematics of the (7,7) discussion, no field-slot assignment);
Sec 4.2 (p.31) the Dirac-vs-Weyl exponent counting ("we might expect the latter [Weyl] in
regions ... where gravity and curvature are weak" -- effective chirality again); Sec 11.2
(p.54) "a non-chiral total theory splits at the emergent level into two separate chiral
theories"; the intro's "why flavor chiral" (a question about observed physics).

**Non-material nuance (recorded for accuracy).** Footnote 13 ("we are speaking loosely
here as if mass eigenstates and flavor eigenstates were one and the same") anchors at the
end of the 12.10 imposter-generation sentence, one sentence after the eq 12.22 pairing
display, and its text concerns the mass/flavor conflation specifically. The fork doc's
"author-footnoted 'speaking loosely' (footnote 13)" is fair at passage level but loose at
sentence level. Not material: the anchor's other two downgrades (speculative section;
contradicts the Sec 9.3 field list) stand independently, and the p.64 item (iii) finding
outweighs the pairing hint in the other direction regardless.

**Repo-chain check.** The audit's Sec 2.6 ("The fermion content in GU (from Weinstein's
construction) is: Psi = (Omega^0(Y14) x S^+) (+) (Omega^1(Y14) x S^-)") carries no draft
citation, in a passage whose neighbors are tagged [reconstruction] -- verified. The other
2026-06-22 artifact (papers/drafts/canonical-structures-14d, Construction 5.4) displays the
same split, also citation-free and [reconstruction grade]-tagged, committed one hour AFTER
the audit (23:30 vs 22:30). "First appearance = the 06-22 audit" holds at commit
granularity.

## 3. The one receipt gap found (closed here; non-material)

The global doc's theorem box includes symmetry-type case S2 (spin + BSp gauge bundle), and
its eta-side receipt (P5) verified the vanishing of the degree-16 part of
A-hat(Z) ch(G) -- the PURE-TANGENT extension density. For an S2 background with a
nontrivial gauge bundle, the extension density is A-hat(Z) ch(G) ch(R-tilde), and its
degree-16 part picks up products of LOWER-weight components of A-hat ch(G) with gauge
classes. The target probe never computed those lower weights.

The gap is real but the conclusion survives: this pass proves ch(G) vanishes IDENTICALLY
at all weights 0..6, with lowest term exactly -e_7(u_1..u_8) at weight 7 (cohomological
degree 28), by two agreeing routes (direct a_k-sum at weight cap 7; the subset-expansion
closed form, which also explains WHY: in prod_i[(1-s)^2 - 2s delta_i]/(1-s)^3, every
subset with fewer than 7 curvature factors is annihilated by [s^14] against a
nonnegative power of (1-s)). Hence A-hat ch(G) ch(R) has zero degree-16 part for EVERY
gauge twist, and the eta phase is exactly 1 on gauge-twisted backgrounds too. The same
mechanism covers the free part on Omega_16(BSp): the C3 anomaly polynomial with gauge
factors included dies because S_alt (the 7-pair Euler product) already vanishes at all
weights 0..4, which the target DID check (its S_alt == {} is all-weight).

Classification: receipt gap, not an error -- no target sentence is false, no number
changes, no verdict changes. Non-material under the dry-round standard. Recommendation
(non-blocking): the paper's S2 eta-side step should cite this probe's ch(G) weight-0..6
vanishing rather than the original weight-4-only check.

## 4. Framing attack results

- "CLOSED-trivial on the balanced branches": the phrase appears ONLY in the global doc
  itself; CANON.md's MOVE1-01 row is unchanged and still carries the EXPLICITLY
  CONDITIONAL stamp; DERIVATION-PROGRESS and the papers/drafts tree contain no promotion.
  No overclaim leakage found.
- The Pyrrhic-zero caveat ("balanced branches have no interior chiral matter; the
  triviality is bought at that price") is displayed in the title block, Sec 0, Sec 5, and
  the referee pass of BOTH documents, with the prominence the referee lenses demanded.
- The C0-reopener (a stabilized source action re-forcing chirality revives branch A and
  reopens its global leg) is stated in the fork doc at Secs 4(2), 5, 7 and in the global
  doc at Secs 2.3, 5, 6, 8 -- everywhere the closure is stated. Pass.
- Conditional register: the global doc's theorem statement names its conditions ((9,5)/
  H-class, X4-spin, S1-S4, balanced branches) inside the theorem box itself. Pass.

## 5. What would have made this NOT-DRY (and did not happen)

Pre-declared break conditions this pass hunted for: a draft passage forcing the Weyl
truncation (would refute 1a; none exists, and p.64 argues the opposite); a nonzero
degree-16 component in the alternating density or the extension class by the independent
routes (would refute 2c/2d; both vanish identically, with the lowest terms landing exactly
where the closed forms predict); a bordism table mismatch at 13-16 (would refute 2a; the
literature check concurs); an odd-torsion summand or a live mod-2 slot at 15 (would refute
2b/2f; dead both reality types); a sign or magnitude error in the -13/W table (would
refute 1b/1c; direct counting agrees, and the honest-density observation 493 vs 13
reproduces exactly).

## 6. Receipts

- Probe: tests/channel-swings/verify_anomaly_closure_probe.py -- deterministic, exact
  Fraction arithmetic, no floats, no RNG, no code shared with the target probes.
  Run 2026-07-20: exit 0, `HEADLINE: 50 [E] + 6 [F] = 56 (setup [T] = 5 excluded) ALL PASS`.
- Primary source: Geometric_UnityDraftApril1st2021.pdf, full-text extraction, all
  chirality-relevant hits read (pp. 23, 31, 46-47, 49, 54, 60-64 in context).
- Repo provenance: anomaly-audit-cl95 Sec 2.6 (commit 6150a8d, 06-22 22:30);
  canonical-structures-14d Construction 5.4 (commit d99501d, 06-22 23:30).
- Literature: Omega^spin_{13,14,15} = 0, Omega^spin_16 = Z^5 corroborated against the
  Tachikawa-Yonekura App. A table (arXiv:2108.13542) via web check this session.
- Targets verified as committed: 2f06e7f (fork pair), 4b83f4b (global pair); neither
  file edited by this pass.

## 7. Dry-round disposition

DRY. Under standing-rule point 8 this is the second consecutive adversarial pass with no
material revision: the two-dry-rounds gate for the anomaly-closure paper is SATISFIED from
this pass's side. Non-blocking recommendations for the paper (cosmetic, not revisions of
the result pair): cite draft p.64 item (iii) as the lead provenance anchor; cite the
ch(G) weight-0..6 vanishing for the S2 eta step; upgrade the Omega~^spin_5(BSp(64)) row
from "unsourced candidate" to "derived Z/2 (AHSS, this probe)"; optionally note the
footnote-13 anchoring nuance. None of these changes a number, a verdict, or a boundary.
