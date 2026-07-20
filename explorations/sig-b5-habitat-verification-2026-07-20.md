---
title: "S_IG/B.5 swing: the P5 carrier habitat machine-verified — pi_1(F) = Z/2 and the K_S twist are REAL (F1, F3 do not fire); the co-flip derived as loop holonomy; dossier 1.2's sign-count mechanism repaired"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (S_IG/B.5 build-or-kill swing, chosen over cross-repo packet freeze and DE audit)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/blockbuster-p5-instance-dossier-2026-07-19.md
inputs:
  - explorations/blockbuster-p5-instance-dossier-2026-07-19.md
  - explorations/pt3-w229-membership-audit-2026-07-19.md
  - docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/channel-swings/pt3_w229_membership_probe.py
  - tests/oq_rk1_cl95_explicit_rep.py
runnable:
  - tests/channel-swings/sig_b5_habitat_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# S_IG/B.5 swing: the Element-1 habitat, machine-verified

The P5 instance dossier staked its Element-1 carrier on two NATIVE-PROVABLE
claims that had never been run, and named its own two cheapest kills (F1
habitat, F3 twist) at exactly those claims. This swing runs them on the
ACTUAL W229 objects (`tests/channel-swings/sig_b5_habitat_probe.py`, exit 0,
headline `15 [E] + 2 [F] = 17`, setup `[T] = 3` excluded). Results:

- **F1 does NOT fire (first exposure).** The metric fiber
  F = GL(4,R)/O(3,1) deformation-retracts onto the RP^3 model
  {I - 2P : P a rank-1 timelike projector} (spectral retraction, signature
  constant along the path, sampled); the generator loop of unoriented
  timelike lines has double-cover monodromy -1 and its square lifts closed
  — the order-2 class at matrix grade. `pi_1(F) = Z/2` is upgraded
  NATIVE-PROVABLE -> **NATIVE-PROVEN (matrix grade)**, with the one
  standard covering-space step (simply-connected double cover) typed
  IMPORTED-standard.
- **F3 does NOT fire — and the sweep is total.** The loop of forms
  `g_t = A_t^T eta A_t` (compact pi-rotation in a mixed (+,-) plane;
  congruence, NOT an isometry — Sylvester keeps signature (9,5)) is a
  genuine closed loop in F, and the continuous g_t-orthonormal frame
  returns with the two plane legs reversed. The transported Krein form
  comes back as **-K_S on ALL 45 mixed planes**, computed as a matrix
  product in the verified Cl(9,5) = M(64,H) rep. Controls: all 36 (+,+)
  and 10 (-,-) planes fix the metric exactly (pure frame loops, trivial in
  F) and transport K_S -> +K_S; the doubled loop is untwisted (order 2);
  frame redefinitions contribute det(h_9) so the -1 is lift-independent.
  The trichotomy is exact: **the twist fires precisely on the genuine
  F-loops.** The dossier's boxed statement — the Krein form is a section
  of a Z/2-twisted bundle whose twist class generates pi_1(F) — is
  upgraded NATIVE-PLAUSIBLE -> **NATIVE-PROVEN (matrix grade)**.
- **The composed identification holds.** Loop holonomy = anchor exchange
  = co-flip, as ONE machine-checked chain on the W229 record structure:
  the transported form exchanges the two Krein anchors exactly
  (P_+(-K_S) = P_-(K_S)), the Krein charge and record current flip sign,
  the (sector, direction) pair co-flips, and the register history is
  invariant. The M6 anchor exchange of the record audit is no longer a
  posited freedom: **it is the holonomy of the fiber twist.** The paid/
  unpaid accounting survives composition: a direction flip inserted ALONE
  (a mu) still splits the register.
- **[F] REPAIR — dossier 1.2's mechanism was wrong; the conclusion
  survives.** The literal argument ("transport sends the timelike leg
  e_0 -> -e_0; K_S contains e_0 once, so K_S -> -K_S") is mislabeled: in
  the (9,5) convention the timelike legs are e_9..e_13 and are NOT factors
  of K_S = e_0...e_8 — flipping the timelike leg alone leaves K_S exactly
  invariant (machine-checked). The pi-rotation in a mixed plane flips BOTH
  plane legs; the sign comes from the SPACELIKE partner leg, the one K_S
  factor among the two. Same conclusion (K_S -> -K_S), corrected
  mechanism, decided by the sweep rather than the prose. This is exactly
  the failure mode the falsifier discipline exists to catch — the check
  was one line, and the line as written did not survive it.

## Council pass (inline, five lenses, compact)

- **Spectral geometer:** the two-section structure now exists at KINEMATIC
  grade (the two global K_S-signs on the double cover, exchanged by the
  deck action — verified as P_+/P_- exchange). Do not let that read as F2
  discharged: F2 is about spectral sections of the boundary DIRAC FAMILY,
  which needs the N2 mathematics. Kinematic habitat proven; analytic
  object unbuilt. Honored in Boundary below.
- **Topological-QFT theorist:** sector count stays TWO (one loop class);
  no anyon/TEE language imported; the congruence-vs-isometry distinction
  is now explicit in the probe (the loop is not a gauge transformation —
  that is why it moves the metric and why the holonomy is physical).
- **Condensed-matter theorist:** nothing here reads the bit. Kramers
  blindness is untouched and untested by this probe (already
  NATIVE-PROVEN elsewhere); the VALUE of the bit remains the external
  posit. The habitat being real makes the blindness derivation load-bear
  MORE, not less.
- **Category theorist:** the one-datum-many-costumes ledger gains a
  machine-checked edge: end-geometry costume (holonomy) = record costume
  (anchor exchange) is now an identity, not an analogy. No new payload
  item; N-accounting unchanged (core 3, ceiling 4, triggers intact).
- **Buildability engineer:** total cost of this swing was one probe; the
  dossier's remaining cheap exposure is exhausted. The frontier is now
  honestly the N-rungs: N1 (families pushforward over the non-compact
  fiber), N2 (the boundary Dirac family + section classification — the F2
  stake), N3 (the BV-to-boundary-Dirac weld). Nothing below theorem grade
  remains to check on Element 1.

## What moved and what did not

Moved (working grade only, R0_COND, conditional on the standing axiom):

1. Element 1's habitat: both NATIVE-PROVABLE items PROVEN at matrix
   grade; the NATIVE-PLAUSIBLE boxed identification PROVEN at matrix
   grade as a composed statement.
2. The candidate survives its two cheapest falsifiers; its stakes now sit
   entirely on F2/F5 (N2-grade computations) plus the F4 double-edge.
3. Dossier 1.2's derivation text is superseded by the probe's corrected
   mechanism (mislabel found and repaired; conclusion unchanged).

Not moved: no claim status, no canon verdict, no scorecard row, no public
posture, no N-accounting change. The external construction need stands:
nothing here builds S_IG or the B.5 global data; B.5(i)-(iii) remain at
the needs-new-mathematics rung; the bit's VALUE remains externally
posited (p2c-owned); the scale and Door B elements are untouched. If
anything the one-bit result is STRENGTHENED: the bit now has a proven
geometric habitat while remaining GU-natively unreadable — storable,
locally blind, externally valued, exactly as typed.

## Receipts

- Probe (exit 0, deterministic, numpy only):
  `tests/channel-swings/sig_b5_habitat_probe.py`.
- Objects: the verified Cl(9,5) rep via `tests/generation-sector/
  gen_sector_bridge.py` / `tests/oq_rk1_cl95_explicit_rep.py`; K_S, J^a,
  register conventions identical to
  `tests/channel-swings/pt3_w229_membership_probe.py`.
- Dossier under test: `explorations/blockbuster-p5-instance-dossier-2026-07-19.md`
  (Element 1, Section 6 falsifiers F1/F3, Section 1.2 repaired).
- Construction discipline: `GEOMETER-VS-PHYSICS-OBJECTS.md` — the fiber
  and Krein form are program-native objects; the loop is a congruence
  path, named as such; no silent standard-physics substitute.

## Boundary

Exploration tier under the standing axiom, R0_COND working grade. The
probe verifies KINEMATIC habitat statements at matrix grade on the
verified finite rep; it does not construct the boundary Dirac family, any
spectral section for it, the families pushforward, or the BV-to-boundary
weld (F2 and F5 remain open at N2 grade and are the candidate's live
stakes). No claim-status, canon, scorecard, or posture movement; no
cross-owner writes; no external actions. Next GU-side rungs in order of
exposure: (i) a finite Dirac-family shadow of F2 (two admissible
K_S-compatible cuts exchanged by the deck action, or a proof the toy
K-group is trivial — either outcome decisive at toy grade); (ii) the F5
end-model C2 flip-invariance test at M2 grade; (iii) N1-N3 as named.
