---
title: "Design packet: emergent-chirality decoupling constructibility (criteria chain and first checks)"
status: active_research
doc_type: constructibility_design_packet
brief_version: "1.0"
target_claim: NONE-NOT-A-KILL
created: 2026-08-12
head_pin: "c4f05a13e31a44c069db0119aa489920791dcff0 (2026-08-11 20:11:50 -0500, source-claim adherence register install); all citations verified against this tree"
authored_by: "Joe-directed design pass (direct chat brief v1.0); repo READ-ONLY for this pass; packet lives outside the repo"
relates_to:
  - lab/sources/source-claim-register.yaml (rows SC-CHI-01..04, SC-CHI-50..54, SC-GEN-01/02, SC-GEN-50/51, SC-OP-04/05, SC-ACT-01)
  - lab/process/CURRENT-RESEARCH-CONTEXT.md (v0.189 head block; live forks 1618-1650; VEV/curvature horn 1539-1548; AC-G1 fence 1091-1099)
  - RESEARCH-STATUS.md (v0.173, v0.174, v0.183, v0.189 entries)
  - explorations/conditional-build/selected-k77-action-adjoint-weight-classification-2026-08-11.md (v0.174: the two pairing horns, weights, p = w+w-)
  - explorations/W224-falsify-nielsen-ninomiya-chirality-2026-07-14.md (the prior NN/SMG/'t Hooft reduction, retired-horn grade)
  - explorations/chirality-grading-and-77-rerun-2026-08-03.md (PH-K1 split; 64+64; 832+/-)
  - explorations/nguyen-pincer-real-form-design-packet-2026-08-11.md (sibling packet; C1/C4/C5 interfaces consumed here)
  - explorations/frontier-design-packets-index-2026-08-11.md (kills-must-name-their-claim rule; the source-native reading)
  - explorations/big-swing-2026-07-07/MP-M2-dark-vs-visible.md (prior "dark mirror" typing, (9,5) horn)
  - canon/escape-corners-campaign-RESULTS.md (corner (a): single VEV dial; chirality-is-VEV-emergent reading)
  - tests/anchored-leads/thooft_anomaly_matching_lever.py (exact-rational anomaly harness, reusable)
  - tests/channel-swings/selected_k77_action_adjoint_weight_classification_probe.py (the CHK-1 fixture source)
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md (p.52 eq 11.6 verbatim incl. the varpi-VEV clause; eq 12.18-12.20 verbatim)
  - GEOMETER-VS-PHYSICS-OBJECTS.md + lab/process/NAMES.md (Layer-0 precondition, read first this pass)
binding: >-
  Design input only. This packet binds no wave, makes no disposition, moves no
  verdict, edits no repo file, claims no queue priority, and changes no claim
  status or posture. Lens outputs below are planning evidence, never scientific
  evidence. Every disposition belongs to a future executing wave under the full
  pre-flight / hostile-review contract; anything canon-adjacent goes through the
  two-phase rule. This packet is NOT a construction of the decoupling and NOT a
  kill of any register row (target_claim: NONE-NOT-A-KILL); it types what
  constructibility of the source's emergent-chirality decoupling would take,
  end-to-end, and which pieces have finite exact checks today.
canon_verdict_change: none
row_change: none
registry_change: none
---

# Design packet: what constructibility of the emergent-chirality decoupling would take

The source asserts a NON-chiral total theory whose chirality is emergent: a
VEV in the Dirac-like operator, tied to scalar curvature as the fundamental
mass scale, couples two chiral halves; when curvature and hence mass drops,
the operator decouples into Weyl-type operators, with the mirror half dark
(SC-CHI-01, draft p.52 eq (11.6); SC-CHI-03, p.61 eq (12.20); SC-CHI-50..53,
TOE 2025 02:36:02-02:37:37; SC-CHI-54, portal 2020 00:22:37 — all register
rows verified at HEAD). This is the vectorlike escape from the anomaly
critique (SC-CHI-50: "it is not chiral ... nobody notices it"), and its
price: the burden of showing the decoupling can actually produce the observed
chiral world. The repo fences the burden (PH-K1-PHYSICAL OPEN/BLOCKED; the
Witten-1983 exit owed for any chiral use of the 384; kinematic-vs-physical
carrier, OQ-RK1 BLOCKED_NEEDS_SPEC — `agent-context-pack.md:1630-1650`) but
no artifact types WHAT CONSTRUCTIBILITY WOULD TAKE end-to-end. This packet is
that criteria-and-first-checks design: a precise criteria chain R1-R5, the
finite exact checks available today on existing banks, the fork conditioning,
and a graded outcome table. It is not a construction, and it does not collide
with the hourly campaign (non-collision statement in Lens 3).

## Layer-0 object table (precondition; the executing wave re-runs it)

Read first this pass: `GEOMETER-VS-PHYSICS-OBJECTS.md` (the fork rule; rows
21, 24, 30) and `lab/process/NAMES.md` (all eight collisions). Persons:
Weinstein is the author (they/them); Curt Jaimungal is an expositor, not
formula authority (they/them; media-index: `secondary-exposition-reviewed`).

| term | senses that collide | rule for this packet |
|---|---|---|
| "chirality" | (a) ambient 14d grading `omega = e_0..e_13` (printed `64+/-`, `832+/-` halves); (b) observed 4d Weyl chirality of physical fields; (c) the `Cl^0` complex-structure choice; (d) base-Lorentz label (four-way homonym, `chirality-grading-and-77-rerun-2026-08-03.md` ruling R5) | the DECOUPLING claim's "two chiral halves" are sense (a) at the operator level; the OBSERVED-world requirement in R3 is sense (b); the bridge between them is exactly PH-K1-PHYSICAL's open map — never silently identified |
| "the VEV" | (i) sub-fields of `varpi` pulled above zero (draft p.52, verbatim, the operative clause of SC-CHI-01); (ii) the spoken "field of VEV in a Dirac like operator" (SC-CHI-51); (iii) the curvature-coaxed augmented-torsion VEV (SC-CHI-52, portal:429); (iv) the repo-derived weight pair `(w+, w-)` / invariant `p = w+ w-` of v0.174 — REPO object, not source-owned | (i)-(iii) are source-owned candidates for R1; (iv) is a repo-derived comparator whose identification with (i) is an OPEN bridge (SCOPED below), never assumed |
| "carrier" | the fixed 192-dim `W` (conditional input) vs `ker(Gamma)` matter content vs the campaign's rank-1,920 conditional real-K77 principal carrier `(Omega^0 + Omega^1)(S)`, `(1+14) x 128` (NAMES.md row 6; RESEARCH-STATUS v0.179-0.184) | this packet's finite checks run on the 1,920 carrier; `ker Gamma` (dim_C 1664, `832+/-`) appears only in the kinematic-grading citations; W/mirror appear only as the campaign's non-invariant seeds (v0.181) |
| "decouples" | (a) operator block-diagonalizes in the ambient-half grading (spectral/kernel statement); (b) IR sectors cease to interact dynamically (QFT statement); (c) the stylized (12.13) toy `dslash_A psi_L = (R/4) psi_R` at `R ~ 0` (SC-CHI-02, auxiliary, draft twice flags "stylized") | R2/R3 type sense (a) precisely; sense (b) is downstream of the unbuilt observation/BRST map (PH-K1-PHYSICAL); sense (c) is custody-grade illustration, cited but never load-bearing |
| "dark" | (i) massive/gapped mirror; (ii) massless but operator-decoupled from observed cells; (iii) dark-sector-confined (charged under a mirror-only factor); prior typing: charged colored mirrors near EW are excluded, a neutral minority is not a clean prediction (MP-M2, (9,5)-horn grade) | R3 requires the wave to pick and verify ONE operator-theoretic sense; "currently dark to us" (p.52) and "reconnect when gravity strengthens" (SC-CHI-53, no scale supplied — custody) do not by themselves select one |
| "imposter" / "the 384" | IMPOSTER-LABEL-AB settled (A), confidence 0.90: the label attaches to the 128 `S(V)(x)S(W)` slot; the RS-shaped 384 is the draft's separate "new cousin"; any chiral use of the 384 owes the Witten-1983 exit (`layer0-fork-registry.yaml:310-330`) | do not re-litigate; R5 uses the settled reading; Witten-1983 = the 1983 KK/RS quantum-numbers object, not Witten 1981/1982/1985 (nguyen packet object table) |
| "settled (7,7)" | REAL-CLIFFORD-FORM (settled `Cl(7,7)=M(128,R)`, author-asserted rationale) vs SIGNATURE-AMBIENT (OPEN, depth 10) — NAMES.md marks Distinct; conflated twice in one month | all criteria below live on the REAL-CLIFFORD-FORM arena; Lens 3 states the SIGNATURE-AMBIENT conditioning explicitly; no ambient-signature claim is made |
| "2+1" | the ledger's block decomposition vs lega2's family census (roles inverted, unadjudicated live fork, `agent-context-pack.md:1647-1648`) | R5 names which 2+1 it means (the settled label-level reading: the "2" are `nu` and the gamma-trace part of `zeta` upstairs) |
| correlation convention | eq (12.20) L-half pairs `L(x)L (+) R(x)R`; eq (11.6) `F+` pairs `2-(x)16+ (+) 2+(x)16-` (anti-correlated); different carriers (plain spinors on Y vs the one-form-valued complex); relative sign = the allocation-dependent `omega_4 omega_10 = +/- omega` caveat — recorded, not adjudicated (extraction s11:265-274) | R2/R3 statements must carry which display's convention they use; the two-carrier discrepancy is itself a datum outcome (c) can name |

## Pre-flight assessment

Failure modes this design could commit, and mitigations:

1. **Redoing the campaign's work or colliding with it.** The hourly campaign
   is building exactly the operator/domain machinery a construction would
   need (current v0.189: observation projector + K77 connection own the
   stabilizer cocycle; next gate a target-blind action-derived `(H,Q)`
   selector, then lower-order BV/KT; v0.183 names the complete sixteen-cell
   lower-order graph/Riccati with the rank-1,920 carrier as control —
   `agent-context-pack.md:12-49`, RESEARCH-STATUS.md:11-54). Mitigation: the
   criteria quantify over an interface (Lens 3); the first checks run on the
   FROZEN v0.173/v0.174 bank, not the moving frontier; no queue priority.
2. **False novelty.** Zero exact hits is not evidence of new.
   `novelty-check.py` was run for this packet's key terms (Prior art below);
   the hits materially changed the design: W224 already reduced the
   mirror-decoupling question to a 't Hooft ledger ONCE, at exploration
   grade, on the retired (9,5) horn — this packet's R4 is typed as the
   settled-horn, typed-content SUCCESSOR of that reduction, not as new.
3. **Layer-0 miss: aiming at an object the source does not own.** The
   deformation candidates are enumerated from register rows with polarity
   and grade; the repo-derived `p = w+ w-` dial is fenced as NOT source-owned
   (v0.174 source return: "SOURCE_SILENT_ON_K77_PAIRING_HORN_AND_INVARIANT_
   WEIGHT_PRODUCT_SELECTION").
4. **Kill-scope inflation.** A future negative result here kills the
   source-native emergent-chirality reading only if it names the rows; the
   frontier index's standing rule is "Kills must name which claim they kill"
   (`frontier-design-packets-index-2026-08-11.md:53`). The outcome table
   pre-names the target rows for each branch; THIS packet itself kills
   nothing (target_claim: NONE-NOT-A-KILL).
5. **Numerics discipline.** All check designs are exact (integer /
   `fractions.Fraction` / two-prime `GF(1009)`,`GF(1013)` as in the v0.174
   probe). FD-band numerics decide nothing anywhere in this packet.
6. **Disposition leakage.** Binds-nothing: no dispositions are made here;
   the wave owns them; lens outputs are planning evidence (frontmatter
   binding block).
7. **Stale-horn contamination.** W224/W222/W216/MP-M2 machinery is
   (9,5)-side (Sp(64) pseudoreal, SO(10) 16 delivery, record condensate);
   REAL-CLIFFORD-FORM settled `Cl(7,7)=M(128,R)` on 2026-08-04, after those
   files. Mitigation: they enter only as prior art, harness patterns, and
   controls — every load-bearing premise is re-typed on the settled horn.

## State of the problem, compressed (each line cited)

- **The claim, source-native, verbatim.** "The idea being explored here is
  that the full operator depicted decouples effectively into two separate
  Dirac like operators, when there is no vacuum expectation value pulling
  the various sub-fields of varpi to values significantly above zero. Thus
  we assert that a non-chiral total theory splits at the emergent level
  into two separate chiral theories..." (draft p.52 after eq (11.6);
  extraction s11:140; SC-CHI-01, hard-core, extraction-verified). The 2025
  spoken chain: not chiral / anomaly critique misses (SC-CHI-50, 02:36:02);
  must produce an effectively chiral world via a field VEV in a
  Dirac-Rarita-Schwinger-like operator (SC-CHI-51, 02:36:29); scalar
  curvature coaxes the VEV and plays the fundamental mass scale, masses
  drop, Dirac-type decouples into Weyl-type (SC-CHI-52, auxiliary,
  02:37:07); two chiral halves coupled by a VEV, luminous reconnects to
  dark when gravity strengthens (SC-CHI-53, 02:37:37, no scale supplied).
  Strongest-claims synopsis adds Witten's non-isomorphic R and R-bar via
  branching rules (SC-CHI-04, p.64).
- **The grading arithmetic.** Eq (11.6): `F+/- = 2-/+(x)16+ (+) 2+/-(x)16-`
  (64 each), `Q+/- = 192`, `Z+/- = 576`; `64+192+576 = 832` per ambient
  half (extraction s11:146-149). The imposter 128 grades `64+64` balanced
  under both signatures and all allocations; 384 grades `192+192`; 1152
  grades `576+576`; total `832+832` on `ker Gamma` (PH-K1-KINEMATIC
  CONFIRMED, `chirality-grading-and-77-rerun-2026-08-03.md`).
- **The fences that hold the burden.** PH-K1-PHYSICAL OPEN/BLOCKED "on the
  unresolved imposter A/B referent [since settled (A)] and the unbuilt
  observation/VEV/BRST/reality/SM-gauge map"; any chiral use of the 384
  owes the Witten-1983 exit; `Pi_RS^phys` does not exist (OQ-RK1
  BLOCKED_NEEDS_SPEC) (`agent-context-pack.md:1630-1650`;
  `layer0-fork-registry.yaml:310-330`).
- **The campaign bank the checks run on.** v0.173: the source-admitted
  wedge-Shiab plus nonzero-southeast family (the SE rival is source-admitted,
  SC-OP-05) removes the rank-128 principal Jordan remainder without
  quotient; K77 relations `12 w+ ell- = 11`, `12 w- ell+ = 11`; null symbol
  rank/nullity 960/960 (RESEARCH-STATUS.md:166-178). v0.174: complete
  four-scalar Spin-natural degree-diagonal pairing classification on the
  1,920 carrier — exactly two projective horns, `(1,1,1,1)` symmetric
  pairing with anti-self-adjoint operator and `(1,-1,-1,1)` skew pairing
  with self-adjoint operator, both rank 1,920 nondegenerate, both
  Grassmann-alternating on all 14 axes for arbitrary nonzero chiral weights
  `(w+, w-)`; adjoint/Grassmann compatibility imposes ZERO equations on the
  weights; a pairing-preserving chiral isometry `S = r P_+ + r^{-1} P_-`
  removes the ratio, leaving one invariant `p = w+ w-`; two primes
  (`selected-k77-action-adjoint-weight-classification-2026-08-11.md`).
  v0.177: both horns satisfy `P^T A + A^T P = 0` (graded Green reality
  graphs). v0.181/0.182: `W`, mirror, and union are NOT invariant boundary
  subcomplexes (each leaks rank 128); all generate the same conditional
  `H640 = 512+128`. v0.184: the ambient hull is rank 1,920. Current v0.189
  as in Pre-flight item 1.
- **The already-typed VEV/curvature linkage.** The local action-derived
  curvature/VEV horn passes the limited two-values-to-one count but fails
  screening exactly; action-owned `w(z)` remains open
  (`agent-context-pack.md:1539-1548`; SC-CHI-52 adherence: the dynamical
  half — masses drop, Dirac decouples into Weyl — "has no construction or
  fence anywhere; it is PH-K1-PHYSICAL's unnamed source-side mechanism").
- **The prior reduction of the mirror problem (retired-horn grade).** W224
  (2026-07-14, exploration, (9,5) horn): NN doubling realized inside GU
  (`{D, omega} = 0` exactly forces `tr(omega sign D) = 0`); GU's operator is
  NOT Ginsparg-Wilson type; the geometric fiber is not a chiralizing domain
  wall; the entire falsification reduces to ONE ledger — are ALL 't Hooft
  anomalies of the would-be-gapped mirror zero (Eichten-Preskill/Wang-Wen
  SMG criterion) — and on the SO(10)-16 reading all vanish (perturbative
  cubic; Witten SU(2) even; mod-16 = 16 mod 16 = 0, `nu_R` load-bearing);
  teeth: dropping `nu_R` gives 15 mod 16 != 0 and the verdict FLIPS.
  Load-bearing caveat recorded there: the anomaly condition is necessary
  only; the sufficient DYNAMICAL condition (the symmetric gapped phase is
  realized) was GRANTED, not shown (`W224-...-2026-07-14.md`, grade block
  and section 7).
- **The sibling packet's interfaces.** Nguyen-pincer packet C1 (typed
  parent from the p.42 ladder), C4 (`dim Hom(S^+ (x) S^+, L0)` expect 0 by
  D7 duality [SCOPED there]; `dim Hom(S^+ (x) S^-, L0)` expect 1), C5
  (2-primary global receptacle honesty pass); its content-level dilemma:
  chiral use of the 14d carrier and local anomaly consistency cannot
  coexist on the settled horn; vectorlike use defuses at the price of the
  chirality the program wants (`nguyen-pincer-real-form-design-packet-2026-08-11.md`).
- **The count claim.** SC-GEN-01 (disavowed-by-source polarity: nature has
  NOT simply repeated three times; the second copy DOES match — two stay
  identical; the third merely effectively identical); SC-GEN-02 (12.10
  title: 2+1, two True Generations and one Effective Imposter); SC-GEN-51
  (two-equivalent-one-not via subgroup restriction — computed structure);
  the 2+1 mechanism is panel-settled at label/multiplicity level, fenced
  "multiplicity, not index" (`agent-context-pack.md:1703-1713`). The
  escape-corners campaign: the spin-3/2's mass "rides the SAME single VEV
  dial whose decrease is GU's generation mechanism"
  (`canon/escape-corners-campaign-RESULTS.md`, title block).

## Lens 1 — Requirements: the criteria chain (R1-R5)

The decoupling claim is constructible if and only if all five hold, in
order. Each criterion names its object, its source row, and its status.

- **R1 — a source-owned mass/VEV deformation term exists in the completed
  operator family.** The completed K77 operator family (v0.173/v0.174,
  interface I below) must admit a zero-order deformation `B` whose switch-on
  couples the two ambient chirality halves and whose switch-off is the
  decoupling limit. Candidate deformation objects, enumerated from the
  register (the wave adjudicates WHICH is the source's):
  (i) the `varpi` sub-field VEV — the operative p.52 clause (SC-CHI-01
  verbatim; `varpi` is the ad-valued one-form of the field content, SC-FLD
  row at register:726 and `T_omega = varpi - eps^{-1} d_0 eps` in SC-ACT-01)
  — hard-core, extraction-verified;
  (ii) the scalar-curvature-as-mass-scale link — SC-CHI-52 (auxiliary,
  claim-mine-verified; the stylized (12.13) `R/4` coupling is SC-CHI-02,
  auxiliary, custody);
  (iii) a zero-order cell of eq (9.16)'s sixteen-cell structure — SC-OP-04
  (the `rho(eps)` wrapping is certified; no global adjoint/domain), with
  the source-admitted nonzero-southeast rival SC-OP-05 = the campaign's
  operator-completion route;
  (iv) comparator only, NOT source-owned: the v0.174 chiral weights
  `(w+, w-)` with invariant `p = w+ w-` — the completed family's own
  one-parameter chirality dial, on which the pairing imposes zero
  equations. OPEN BRIDGE [SCOPED]: whether the source's (i) lands on (iv)
  under the completion — i.e., whether "sub-fields of varpi above zero"
  deforms exactly the cells the weights multiply — is a finite,
  checkable placement question once the source's VEV placement is typed;
  if the source never fixes the placement, that is outcome (c)'s datum.
- **R2 — at nonzero VEV the coupled operator is vectorlike
  (anomaly-safe).** The deformed operator's spectrum/kernel structure must
  pair the two ambient halves: every complexified internal-chirality
  component appears with both base-side chiralities in equal multiplicity
  (the artifact-defined "vectorlike", `chirality-grading-...:57`), so the
  UV anomaly ledger is identically zero. Status: CONFIRMED at kinematic
  grade for the 128 (PH-K1-KINEMATIC, 64+64, joint 32/32/32/32) and for
  the grading arithmetic `832+832`; NOT yet stated for the deformed
  completed operator (the pairing-horn compatibility `P^T A + A^T P = 0`
  of v0.177 is the banked ingredient; the spectral pairing statement is
  unbuilt). R2 is where "anomaly-safe" is EARNED rather than asserted:
  the vectorlike defusal carries surplus only if the pairing survives the
  deformation (nguyen packet Lens 6: surplus >= 5 with zero posited
  parameters on the vectorlike branch).
- **R3 — as VEV -> 0 the operator decomposes into single-chirality
  Weyl-type pieces, observed half light, mirror half dark.** Operator
  statement: in the limit, the completed operator block-diagonalizes in
  the ambient-half grading into two Weyl-type operators (the p.52 "two
  separate Dirac like operators" and the 12.20 luminous/looking-glass
  labels), and the OBSERVED assignment holds: the half carrying the
  matter reading stays light while the mirror half is EXACTLY ONE of:
  (d-i) massive (gapped by a residual deformation the limit does not
  kill), (d-ii) massless but operator-decoupled (zero cross-cells AND
  zero shared gauge-cell response — else it is luminous), or (d-iii)
  confined in a mirror-only sector. "Dark" MUST be typed as one of these
  for the claim to survive: (d-ii) is the reading the p.52 text supports
  ("currently dark to us", reconnection when gravity strengthens,
  SC-CHI-53), and it is the most dangerous, because a massless mirror
  charged under the SAME gauge cells is empirically luminous — prior
  (9,5)-horn typing: charged colored mirrors near EW are excluded;
  neutral-minority darkness is dynamics-gated, not clean (MP-M2 caveats
  4-5). A wave asserting (d-i) inherits R4's asymmetric-mass problem; a
  wave asserting (d-iii) posits a sector factor the source does not
  display (count its surplus). Also load-bearing here: WHICH correlation
  convention ((12.20) L(x)L vs (11.6) anti-correlated) defines the halves
  — recorded, unadjudicated (Layer-0 table, last row).
- **R4 — the decomposition survives the known continuum obstructions.**
  Literature-flag discipline: Nielsen-Ninomiya is lattice-specific (local
  translation-invariant lattice operators); it does NOT directly govern
  the continuum claim, and W224 already both realized its continuum
  shadow inside GU and identified the operative escape. The relevant
  continuum questions are:
  (R4a) **gauge invariance of chirality-asymmetric mass terms.** To make
  the mirror heavy while the observed half stays light with an EXPLICIT
  mass, one needs an invariant zero-order term supported on one ambient
  half. On the settled horn the equivariant same-half scalar channel is
  expected EMPTY — `dim Hom(S^+ (x) S^+, L0) = 0` by D7 half-spin duality
  [SCOPED, = nguyen C4's expectation; the (9,5) analog SHIAB-05 is exact
  in-repo] — so explicit asymmetry is expected unavailable, and the
  asymmetry must come SPONTANEOUSLY: from the VEV direction in a
  nontrivial representation (which is in fact the source's own mechanism
  claim, SC-CHI-51/52). The wave must verify the deformation's rep type
  actually distinguishes the halves at nonzero VEV and not at zero.
  (R4b) **'t Hooft anomaly matching between the vectorlike UV and the
  claimed chiral IR — the packet's central obstruction.** Stated
  carefully: in the UV the theory is vectorlike, so EVERY 't Hooft
  anomaly (perturbative cubic, mixed gauge-gravity, Witten-type mod-2,
  discrete/cobordism classes) of any symmetry that survives to the IR is
  ZERO. The claimed IR is the observed chiral world plus a dark mirror.
  Matching forces: (anomalies of the visible chiral sector) + (anomalies
  of the mirror sector) = 0, for every matched symmetry. Consequences:
  any symmetry under which the visible sector has a nonzero 't Hooft
  anomaly MUST also act on the mirror with the opposite anomaly — and a
  sector that must saturate anomalies of a shared symmetry cannot be
  arbitrarily decoupled from it. The sharpest known killer of
  emergent-chirality proposals is exactly this ledger failing: a mirror
  that cannot be symmetrically gapped/decoupled because a required
  anomaly is nonzero. The modern SMG criterion (Eichten-Preskill 1986;
  Wang-Wen; Razamat-Tong — all literature-flagged, independent
  citation-check required) makes it iff-shaped: the mirror is
  symmetrically gappable iff ALL its 't Hooft anomalies vanish, including
  the discrete mod-16 class of `Omega^Spin_5(B G_SM) = Z/16`
  (Garcia-Etxebarria & Montero, flagged). W224 checked this ledger once
  and found it satisfied — on the retired horn, with the SO(10)-16
  delivery (W222) that is itself horn-stale, and with the dynamical
  sufficiency GRANTED. The settled-horn, typed-content re-run is CHK-2.
  (R4c) **vectorlike-theory parity/chirality rigidity [literature flag,
  scoped].** Vafa-Witten-type theorems (parity not spontaneously broken
  in vectorlike gauge theories with positive measure) would, if
  applicable, obstruct the spontaneous route R4a forces. Two exact hits
  in-repo are query-vocabulary only (locator batch), so this obstruction
  is NOT yet typed in-repo. Layer-0 discipline applies: the theorem's
  positivity premise is a physics-default assumption; the program-native
  arena is Krein/indefinite (GEOMETER-VS-PHYSICS rows 20-21), where the
  premise plausibly fails — which construction governs is exactly the
  fork rule's question, and a kill is only as strong as the construction
  it lives in. Independent citation-check owed before any disposition
  consumes this either way.
  (R4d) the dynamical realization: the gap/decoupling phase must actually
  be delivered by the source's own curvature dynamics (SC-CHI-52's
  "unnamed source-side mechanism"; W224's granted condensate). No finite
  check exists today; naming it as the terminal remainder is itself the
  honest form (SC-CHI-51 adherence: "carried as an unpaid debt").
- **R5 — the count claim (2+1, two-stay-identical) survives R1-R4.** The
  surviving light spectrum at VEV -> 0 must be: two families that remain
  representation-identical (SC-GEN-01: the second copy DOES match; under
  the settled reading the "2" are `nu` and the gamma-trace part of `zeta`
  upstairs) plus one EFFECTIVE imposter (the 128 label, settled A), with
  the RS 384 not used chirally without paying the Witten-1983 exit, and
  the mirror half entirely on the dark side of R3's typing. Constraint
  inherited from the escape-corners campaign: the spin-3/2 mass rides the
  SAME single VEV dial as the generation mechanism — R5 fails if making
  the mirror heavy also lifts or splits the two true families
  differently (one dial, several jobs: the wave must exhibit the dial's
  action on all sectors simultaneously). Fenced: multiplicity, not
  index; blocks are not generations by decomposition alone (Rung 1).

## Lens 2 — First computable checks (finite, exact, today, on existing banks)

Interface I (what every check quantifies over): the tuple
`(V, X, P_sym, P_skew, D)` where `V = R^1920` is the conditional real-K77
principal carrier `(Omega^0 + Omega^1)(S)` at a point, `(1+14) x 128 = 1920`,
with ambient chirality involution `X` splitting `960 + 960` (each 128 =
64+ + 64-); `P_sym = (1,1,1,1)` and `P_skew = (1,-1,-1,1)` are the two
v0.174 pairing horns (both rank 1,920); `D` is the completed v0.173/v0.174
operator family member with weights `(w+, w-)`. Frozen fixtures:
`tests/channel-swings/selected_k77_action_adjoint_weight_classification_probe.py`.
If the campaign later supersedes the family (its own named next gates), the
checks re-run through the same interface; nothing here depends on the moving
v0.189 frontier.

- **CHK-1 — the chirality-asymmetric deformation space (THE first check;
  bounded linear algebra on the 1,920 carrier).** Specification, exact:
  for each horn `P` in `{P_sym, P_skew}` and each equivariance layer,
  compute the dimensions of the four cells of the zero-order deformation
  space
  `Z(P, L) = { B in Layer L subset End(R^1920) : (P B)^T = -(P B) }`
  (the Grassmann-alternating admissibility of v0.174 — the corrected
  criterion: what must be alternating is the full quadratic coefficient),
  graded by the chirality involution:
  `Z_even = {B : [B, X] = 0}` (half-preserving; within it report the
  swap-asymmetric subdimension, i.e., the part with `B_+` not identified
  with `B_-` under the halves' pairing — the explicit-asymmetric-mass
  cell) and `Z_odd = {B : {B, X} = 0}` (half-coupling — the VEV-term
  cell). Layers: L0 = all of `End(R^1920)` (control only: alternating
  dimension is `1920*1919/2 = 1,842,240`, and the even/odd block split is
  `2*960^2` each — trivially nonzero, decides nothing; stated so the wave
  cannot mistake the uninformative layer for the result); L1 = the
  Spin-natural degree-diagonal four-scalar family's ambient cell lattice
  (the v0.174 arena — finitely many cells, dimension expected single
  digits); L2 = the full sixteen-cell grammar of eq (9.16) as certified
  by the s9 extraction (barred row order, `rho(eps)` wrapping, minus-star
  lower-left). Two primes (`GF(1009)`, `GF(1013)`) plus rational
  certification of the load-bearing ranks, per the campaign's own
  standard. Planted controls: (i) regression — the four-scalar family
  itself must reproduce v0.174's two-horn classification exactly; (ii) a
  planted Dirac-type half-coupling mass (the matched `64+ <-> 64-`
  identity block in the zero-form sector) must be classified `Z_odd` and
  its admissibility per horn computed, not assumed; (iii) a planted
  single-half mass (`B_+ != 0, B_- = 0`) must land in the `Z_even`
  swap-asymmetric cell; (iv) a random non-equivariant `B` must be
  rejected by the L1 projector; (v) a deliberately symmetrized `(P B)`
  must be rejected by the alternation test. Kill conditions, pre-declared:
  `dim Z_odd(P, L1) = dim Z_odd(P, L2) = 0` for BOTH horns => NO
  pairing-compatible half-coupling deformation exists in the natural
  family => R1 fails in this construction (route to outcome (b);
  escalate; per the fork rule, check whether the wall survives on the
  other construction before believing it). Surprise tripwire:
  `dim Z_even-asymmetric(P, L1) > 0` at the equivariant layer would
  contradict the D7-duality expectation (R4a / nguyen C4) => hand audit
  before any use, both ways. Deliverable: one table,
  `{horn} x {L1, L2} x {odd, even-symmetric, even-asymmetric} -> dim`,
  exact integers.
- **CHK-2 — the anomaly-matching ledger (finite table the wave fills).**
  Rows (the discrete data that must match): `[SU(3)]^3`;
  `[SU(2)]^2 U(1)`; `[U(1)]^3`; `U(1)-grav^2`; Witten SU(2) mod-2
  (doublet parity); the mod-16 class of `Omega^Spin_5(B G_SM) = Z/16`
  [literature-flagged value]; the Dai-Freed class of the TYPED parent
  (consumes nguyen C1/C5 output; 2-primary honesty pass, no vanishing
  claim without differentials); one row per additional global symmetry
  the wave declares surviving to the IR (B-L etc. — declared, not
  discovered). Columns: UV total (vectorlike => compute the identical
  zero, do not assert it); IR visible; IR mirror (forced = minus
  visible); verdict per row. Existing exact harnesses to extend, not
  rebuild: `tests/anchored-leads/thooft_anomaly_matching_lever.py` (exact
  rational SM/16 rows; also proves 't Hooft coefficients are linear in
  `n_gen`, so matching alone never fixes the count — R5 must not lean on
  this lever. INTEGRATION NOTE, Joe direct chat 2026-08-12: this lever
  closes a door only the PHYSICS-DEFAULT reading would walk through. The
  source's count claim never stood on matching: in the source-native
  reading there is no free multiplicity `n` to fix — the three
  family-shaped slots are forced by the branching arithmetic itself
  (SC-GEN-04/05: `nu`; the gamma-trace part of `zeta`; the imposter
  revealed inside the RS remainder — structural slots, per the Rung 1
  multiplicity-not-index fence), and what wants a mechanism is not the
  count but the EFFECTIVENESS and stability of the third (SC-GEN-01
  "effectively identical ... only at low energy"; SC-GEN-57
  two-stay-identical; SC-GEN-54's supercharge-extension claim — UNTYPED,
  the register's top adherence gap, and the actual open leg). Matching's
  only role here is R4 consistency, where linearity is mildly
  CONFIRMATORY for the source: each surviving family must be anomaly-free
  on its own, which the SM family is — exactly why a structural count of
  anomaly-free slots passes matching trivially at any count) and W224's ledger script. The load-bearing OPEN premise the
  table exposes: the IR-visible content on the SETTLED horn — the 16-vs-15
  datum (`nu_R` delivery) was established via W222 on the retired horn;
  the settled-horn delivery is untyped. Controls: the 15-content flip
  must show `15 mod 16 != 0` (W224's teeth, reproduced); a lone chiral
  `3` must show `[SU(3)]^3 = 1`. Kill condition: any row whose forced
  mirror value is incompatible with the R3 dark-typing chosen (e.g., a
  nonzero anomaly under a symmetry the mirror must not carry to be dark)
  => R3 and R4 cannot both hold on that typing => route to outcome (b)
  if it holds for ALL three dark-typings.
- **CHK-3 — consume, do not reschedule: the (7,7) invariant-mass channel.**
  `dim Hom(S^+ (x) S^+, L0)` and `dim Hom(S^+ (x) S^-, L0)` on the
  settled horn are exactly nguyen C4 (designed there, harness ports from
  MOVE-4/R4). Their values decide R4a's explicit-vs-spontaneous split.
  Non-collision: this packet only registers the dependency.

What has NO finite check today (stated so the wave does not improvise one):
R4d (dynamical realization); the global/analytic decoupling limit (the
campaign's global Green/domain problem is open at v0.174-0.189); the
observation/BRST descent of any of it (PH-K1-PHYSICAL's map chain). These
are the named remainder in outcome (a).

## Lens 3 — Fork conditioning and non-collision

- **SIGNATURE-AMBIENT (OPEN, depth 10 over threshold, own resolver packet
  2026-08-11):** every criterion and check above lives on the settled
  REAL-CLIFFORD-FORM arena (`Cl(7,7) = M(128,R)`) and the K77 campaign
  bank. Conditional statements: if the ambient-signature fork later lands
  (9,5)-side in a way that revives `M(64,H)` machinery, CHK-1's carrier
  and horns must be rebuilt (the v0.173 relations are "opposite in sign to
  K95"), and W224's Sp(64)-side apparatus partially revives; the criteria
  chain R1-R5 itself is signature-blind in statement, signature-bound in
  every computation. M-H9 (the B5 signature test, endpoints
  `(9,5) => (58,78)` vs `(7,7) => (78,58)`) is the named discriminator —
  not this packet's to schedule.
- **CARRIER-SPLIT (three horns, unadjudicated):** the decoupling texts
  themselves sit on horn 3 (p.61 `TX^{1,3} (+) N^{6,4} subset Y^{7,7}`,
  eq (12.18)-(12.19) — SC-CHI-03 adherence: typed as CARRIER-SPLIT horn 3,
  explicitly unadjudicated). R3's brace-label assignment and the
  (12.20)-vs-(11.6) correlation discrepancy are horn-3 statements; the
  finite checks run on the campaign's conditional K77 carrier. A wave
  moving R3 to disposition must carry the horn explicitly.
- **What the hourly's current gates already constrain:** v0.189's next gate
  (target-blind action-derived `(H,Q)` selector, else prove refinement
  directions gauge, BEFORE lower-order BV/KT) and v0.183's open complete
  sixteen-cell lower-order graph/Riccati mean the campaign itself will
  produce the L2 sixteen-cell lower-order structure CHK-1 needs at layer
  L2 — CHK-1's L1 layer is runnable on today's frozen bank regardless;
  its L2 layer consumes whatever the campaign certifies. v0.181's result
  that `W`/mirror/union are not invariant subcomplexes constrains R3(d-ii):
  "operator-decoupled mirror" cannot be formulated as restriction to those
  seeds; it must be formulated on the deformed operator's own kernel
  grading.
- **Non-collision statement (explicit):** this packet schedules nothing,
  claims no queue rank, and its first checks run READ-ONLY on banked
  v0.173/v0.174 fixtures outside the campaign's write path; the criteria
  quantify over interface I so that every future campaign object slots in
  without rework; the single overlap surface (the sixteen-cell lower-order
  system) is consumed as an interface, and the campaign's own next-gate
  text remains the sole queue truth (`agent-context-pack.md:1096-1099`
  discipline).

## Lens 4 — Graded outcome table (dispositions owned by the wave, not this packet)

| # | evidence pattern | reading the wave may file | consequences / target rows |
|---|---|---|---|
| (a) constructible-so-far | CHK-1: `dim Z_odd > 0` for at least one horn at L1 or L2, controls green; CHK-2: ledger all-zero on typed settled-horn content incl. the 16-datum; CHK-3: same-half channel 0, cross-half 1 (asymmetry is spontaneous, matching the source's own mechanism shape) | the vectorlike escape STANDS AS CONSTRUCTIBLE-SO-FAR: a pairing-compatible VEV coupling term exists, the mirror is gappable/decouplable in principle, explicit asymmetric mass is correctly absent | the burden NARROWS to the named remainder: (1) source placement of the varpi VEV in the operator (the R1 bridge), (2) the dynamical realization R4d, (3) the PH-K1-PHYSICAL map chain, (4) Witten-1983 if the 384 is used chirally. No verdict moves; the fences SURVIVE and are corroborated; adherence notes on SC-CHI-51/52 may upgrade PARTIAL context |
| (b) the route dies | CHK-1: `dim Z_odd(P, L1) = dim Z_odd(P, L2) = 0` for BOTH horns (no coupling deformation exists in the natural family), OR CHK-2: a matched-symmetry row provably fails on typed content under ALL THREE R3 dark-typings | the emergent-chirality decoupling route is DEAD in this construction — the honest completion of the falsification the Nguyen critique gestures at (its content-level arm: vectorlike defusal at the price of chirality; here the price proves unpayable) | any such artifact carries `target_claim:` with the CHI hard-core rows it kills: SC-CHI-01, SC-CHI-03, SC-CHI-04, SC-CHI-50, SC-CHI-51, SC-CHI-53, SC-CHI-54 (and auxiliary SC-CHI-02/52 as mechanism rows); fork rule applies before belief (does the wall survive the other construction?); verdict-flip => hostile field-specialist review mandatory; two-phase rule for canon |
| (c) source-underdetermined | CHK-1 finds `dim Z_odd > 0` (a coupling-term SPACE exists) but neither the draft nor the 2025 sources fix WHICH term — the exact missing data: the draft never displays the varpi-VEV's cell placement in eq (9.16)/(11.6) (the dashed-line diagram carries no operator cells; SC-OP-04 certifies no global adjoint/domain; v0.174's source return is SOURCE-SILENT on horn and on `p`) | re-type, not resolve: the open datum is the source's VEV-placement display (which sub-fields of varpi, in which cells, with which horn); the deformation-space table becomes the register of what any future source display must select from | mirrors nguyen O4; the register records the exact datum and a wake condition (a source display fixing placement); the R1 bridge (source varpi-VEV vs repo `p = w+ w-`) stays SCOPED-OPEN |
| (d) surprise | CHK-1 tripwire: equivariant explicit-asymmetric cell nonzero (contradicts D7-duality expectation), or CHK-3 returns same-half dim > 0 | hand audit before use; both the check design and the R4a typing re-derived | nothing downstream is filed until resolved; if it stands, R4a's spontaneous-only reading is WRONG and explicit asymmetric mass returns to the table (major information, both ways) |

## Prior art

**In-repo (novelty-check run this pass; hits read before design; the ones
that changed the design listed):** `python3 lab/process/novelty-check.py`
on "decoupling constructibility" (0 exact, 0 co-occurrence),
"chirality-asymmetric deformation" (0/0), "VEV deformation" (0 exact, 31
co-occurrence), "anomaly matching" (26 exact), "'t Hooft" (143 exact),
"mirror fermion" (6 exact), "Vafa-Witten" (2 exact — query vocabulary in a
locator batch, not a result), "mass deformation" (10 exact), "Weyl
decoupling" (10 exact). Zero-hit strings are absences of the exact strings
only, per the standing rule — the adjacent work exists and is cited:
**W224** (the single most important prior artifact: NN realized inside GU;
the GW/domain-wall evasions closed; the reduction of the whole mirror
question to the 't Hooft/SMG ledger; the ledger checked once, retired-horn
grade, dynamics granted); **the thooft lever**
(`tests/anchored-leads/thooft_anomaly_matching_lever.py`: exact-rational
ledger rows + the linearity-in-`n_gen` result that blocks count-by-matching);
**MP-M2** (dark-vs-visible mirror typing, (9,5) horn, collider caveat
from-memory); **escape-corners** (corner (a): chirality-is-VEV-emergent
reading closes GP at author-assertion tier; the single VEV dial constraint
consumed by R5); **the v0.173/v0.174 artifacts** (the completed family and
pairing horns — the bank CHK-1 runs on); **chirality-grading Q2/DQ2**
(PH-K1 split, the kinematic 64+64); **the nguyen-pincer packet** (the
content-level dilemma; C1/C4/C5 consumed as interfaces); **cb-c**
(`W = 0` forced by local consistency; the chiral branch 12/12-fatal);
**the s11-s12 and s9 extractions** (verbatim loci). What is NEW relative
to these hits: the end-to-end criteria CHAIN R1-R5 as a single typed
object; the exact specification of the deformation-space computation
(CHK-1's cell table with horns, layers, grading, controls, and
pre-declared kills); the UV/IR ledger as a finite fillable table with the
16-datum exposed as the settled-horn open premise; the three-way
operator-theoretic typing of "dark" as a forced choice; and the
identification of the v0.174 invariant `p = w+ w-` as the repo-side
candidate landing site for the source's VEV dial (bridge SCOPED-OPEN). No
mathematical result is claimed new; every computation specified is a
typed-content instantiation of machinery the repo already validated.

**Literature (ALL flagged for independent citation-check; none certified
here; none enters any disposition unchecked):** Nielsen & Ninomiya 1981
(lattice-specific doubling; premises do not transfer verbatim to the
continuum claim); Ginsparg-Wilson / Neuberger / Luscher (the modified
chiral symmetry GU's exact anticommutation lacks, per W224); Kaplan 1992
(domain wall); Eichten & Preskill 1986; Wang & Wen 2018-2020 and
Razamat & Tong 2021 (the SMG iff-criterion — the load-bearing lore of
R4b); Garcia-Etxebarria & Montero 2019 (`Omega^Spin_5(B G_SM) = Z/16`);
Dai-Freed 1994 / Freed-Hopkins 2021 (global leg conventions, via nguyen
C5); Witten 1982 (SU(2) mod-2) vs Witten 1983 (the repo's RS exit object
— distinct papers, never merged); Vafa & Witten 1984 (parity
non-breaking in vectorlike theories — positivity premise vs the Krein
arena, R4c, untyped in-repo); 't Hooft 1979 (anomaly matching).

## What this packet does not do

No registry, ledger, fence, canon, verdict, residue, adherence, or posture
change; no wave bound or scheduled; no queue priority claimed over the K77
campaign frontier; no construction of the decoupling attempted; no kill
made or implied (target_claim: NONE-NOT-A-KILL); no repo file edited (the
repo was read-only for this pass; this packet lives in the session
scratchpad); no anomaly value asserted beyond the file-pinned and
flagged items in the manifest; no dark-typing chosen; no fork horn
adjudicated; the hostile review any executing wave owes is not satisfied
by the self-review below.

## Verify status manifest

- HEAD pin `c4f05a1`; register rows SC-CHI-01..04/50..54, SC-GEN-01/02/50/51,
  SC-OP-04/05, SC-ACT-01 (polarity, grade, core, adherence notes); the p.52
  and (12.18)-(12.20) verbatim passages; PH-K1-KINEMATIC/PHYSICAL statuses;
  the Witten-1983 fence; OQ-RK1 BLOCKED_NEEDS_SPEC; IMPOSTER-LABEL-AB
  settled (A) 0.90; v0.173/v0.174/v0.177/v0.181-0.184/v0.189 ledger
  sentences; the two pairing horns `(1,1,1,1)`/`(1,-1,-1,1)`, weights,
  `p = w+ w-`, zero weight equations, two primes; W224's verdict, ledger,
  teeth, and caveat; MP-M2 caveats 4-6; escape-corners title-block
  sentences; the frontier-index kills-name-their-claim rule; the
  curvature/VEV two-values-to-one-passes/screening-fails sentence:
  **CONFIRMED** (each file opened at HEAD this pass; quotes verified where
  quoted).
- Arithmetic in this packet (`1920 = (1+14) x 128`; halves `960 + 960`;
  `64/192/576` and `832` per half; `128 -> 64+64`; `1920*1919/2 =
  1,842,240`; `2*960^2` block split): **CONFIRMED** (exact integers,
  recomputed this pass).
- D7-duality emptiness of the same-half channel on (7,7); the
  L1-layer dimensions being small; the settled-horn 16-datum being
  deliverable; the `p = w+ w-` <-> varpi-VEV bridge: **SCOPED** (each is
  exactly what a named check computes or what a source display must
  supply; none carries a disposition).
- The SMG iff-criterion; the mod-16 value; Vafa-Witten's applicability
  and its Krein-premise failure: **SCOPED with literature flag**
  (independent citation-check required before any disposition consumes
  them).
- The criteria chain R1-R5 as the constructibility decomposition; the
  CHK-1/CHK-2 designs, controls, and kill conditions; the outcome table;
  the dark-typing trichotomy: **PROPOSED** (design judgment; the executing
  wave certifies or refutes).

## Self-hostile review (the three standing charges; same-pass)

**Charge 1 — where the summary outruns the artifact.** (i) Calling R4b
"the packet's central obstruction" is a design judgment; W224's one prior
run of that ledger PASSED (retired horn, granted dynamics), so the
obstruction's bite on the settled horn is expected-open, not
expected-fatal — the headline is graded PROPOSED and outcome (a) exists.
(ii) The claim that the v0.174 weights are "the completed family's own
chirality dial" is verbatim-supported for the family (zero weight
equations, invariant `p`) but the DIAL reading (that `p -> 0` is the
decoupling locus) is an interpretation no artifact states; it is fenced
as the SCOPED-OPEN R1 bridge and appears in no kill condition.
(iii) CHK-1's L1 layer is described as "runnable today"; its cell lattice
definition leans on the v0.174 probe's internal structure, which the wave
must re-derive from the fixture rather than trust this packet's summary
of it. No other overrun found; list otherwise empty.
**Charge 2 — where rigor defends a superseded or mistyped object.** Audit:
W224/W222/W216/MP-M2 are (9,5)-side and pre-date the REAL-CLIFFORD-FORM
settlement; they enter only as prior art, harness patterns, teeth
controls, and caveat sources — no R-criterion premises on them.
The stylized (12.13) toy is custody-grade and never load-bearing. The
16-datum is explicitly exposed as an open settled-horn premise rather
than imported from W222. Residual risk: the whole packet quantifies over
the v0.173/v0.174 completed family, which the campaign itself may
supersede (it has once already, v0.173 -> v0.174 correcting the adjoint
criterion); mitigation is the interface clause, but a superseding
correction of the ALTERNATION criterion itself would invalidate CHK-1's
admissibility condition, not just its inputs — the wave re-verifies the
criterion against the then-current ledger before running. List otherwise
empty.
**Charge 3 — what else must change if the result stands.**
- If (a) stands: the fences (PH-K1-PHYSICAL, Witten-1983, Rung 1) —
  **survive** (corroborated, burden narrowed onto them); SC-CHI-51/52
  adherence notes — **needs-recheck** (PARTIAL context may cite the
  deformation-space table); the nguyen packet's Lens 6 surplus
  accounting — **needs-recheck** (the vectorlike defusal's zero-freedom
  claim gains one computed constraint); dissolved rows — **none** (stated
  explicitly).
- If (b) stands: the CHI hard-core rows named in the outcome table carry
  the kill (via the executing artifact's `target_claim:`, not this
  packet); the frontier-index sentence that the source-native reading "is
  untouched by that kill" — **needs-recheck** (it would no longer be
  untouched); the vectorlike-defusal surplus reading — **needs-recheck**
  (the price side of the dilemma becomes unpayable, which STRENGTHENS the
  pincer's content-level arm); PH-K1-PHYSICAL — **survives** as a fence
  but its OPEN becomes CLOSED-NEGATIVE-in-this-construction pending the
  fork-rule cross-check; dissolved rows — **none** until the two-phase
  rule runs.
- If (c) stands: the register gains one narrowed open datum (the VEV
  placement display) with a wake condition; nothing dissolves; this
  packet's R1 candidate list — **needs-recheck** per any new source
  display. Empty lists are stated as empty.
