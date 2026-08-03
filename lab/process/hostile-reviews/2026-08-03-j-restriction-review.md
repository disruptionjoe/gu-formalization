---
title: "Hostile field-specialist review: the OQ-RK1 J-restriction probe (M-H1)"
status: process
doc_type: hostile-review
created: 2026-08-03
object_under_review: "tests/oq_rk1_j_restriction_probe.py + explorations/oq-rk1-j-restriction-on-branched-slots-2026-08-03.md"
charge: "two-sided (overclaim / over-fencing), READ-FIRST files mandatory, independent re-runs required; per the 2026-08-03 verdict-flip governance rule"
verdict_summary: "Claims 1-4 CONFIRMED (1 STRONGER than filed: unconditional, allocation-independent — re-file as its own token; 2-3 with corrections; 4 exact, re-derived analytically). Claim 5 — 'the 4-vs-8 census fork maps exactly onto the signature dichotomy' — REFUTED AS STATED: the X block carries 768_H in EVERY allocation (rank_H := rank_C/2 is allocation-invariant); only the J-irreducible block PARTITION moves (4 vs 8 UNITS). The '4 units vs 8 units' is HOMONYMOUS with OQ-RK1's rank_H ∈ {4,8} — the exact AGENTS.md:15 decomposition-to-count failure. Reviewer-2's 'the physical split IS Lorentzian so the conditional is decided' charge is itself REFUTED by GEOMETER-VS-PHYSICS-OBJECTS.md:24 (the Lorentzian-vs-compact carrier split is an explicitly UNSETTLED fork, and the repo's own finite census uses the compact/WITHIN side). New defect: the four small-sector projectors each merge a B5 mirror pair (non-isotypic; collapses the ledger's provenance separation = B5 hostile control #2); Q4/Q10 refinement available. Spec-blocked boundary RESPECTED throughout; no leak to any verdict-adjacent surface."
---

# Hostile review: OQ-RK1 J-restriction probe (panel report, full content)

Pre-reading discharged: GEOMETER-VS-PHYSICS-OBJECTS.md (esp. :24, the
Physical 4+10 carrier split row — load-bearing); six-axis-template.md:46-77
(Layer-0); the B5 ledger; oq_rk1_e_rs_eff_assembly.py; the 2026-07-29 Layer-0
retraction; the new form-spinor note; AGENTS.md:38 and :15.

## (C) Re-runs and independent verification

Probe re-run: exit 0, ALL 180 CHECKS PASSED; cross-split law reproduces
verbatim incl. (1,3) -> internal (8,2). Check 1: rebuilt Cl(9,5) from
scratch — J^2 = -I, [J, e_a] = 0, [J, omega] = 0, all errors exactly 0.0.
Check 2 (kills the robustness charge IN THE PROBE'S FAVOUR): the conjugation
sign vector forces the index set {1,3,5,7,10,12} (not chosen); 300 random
Clifford products have perfectly diagonal Gram (off-diag 0.0, rank 300/300)
=> the commutant of {e_a} is scalars => any antilinear J' = lambda J with
|lambda| = 1, and (lambda J) P (lambda J)^{-1} = J P J^{-1} identically: the
classification is PROVABLY invariant under J -> iJ, -J, unitary conjugation.
Check 3: one slot-exchange distance rebuilt by a disjoint route (512-dim
block eigendecomposition): ||P_X32p - J P_X23m J^{-1}|| = 2.94e-13 vs
||P_X32p - J P_X32p J^{-1}|| = 13.8564065 = sqrt(192). Confirmed.
Check 4 (new): the equivariant J-stable grading Q4 = P_{R^4} (x) I,
Q10 = P_{R^10} (x) I splits R^4(x)S = 4x96 + 4x32 and R^10(x)S = 4x288 +
4x32, with the four 32-dim pieces in each block carrying IDENTICAL
(C4, C10, OmF, P4) labels — see A3.

## (A) Overclaim findings

A1. For the eight X slots the projectors ARE the ledger's slots: the block is
multiplicity-free, so the isotypic decomposition is canonical — the
"re-pairing freedom" charge is REFUTED on X (and check 4 confirms
containment). NOT so for the small sector (A3).

A2. The labeling operator OmF = I (x) om_F grades by spinor-factor chirality,
not the so(10) type of the constituent; faithful on X (verified), but the
note's "canonical ... from subalgebra invariant data only" oversells.

A3. NEW DEFECT: the four SM "slot projectors" (64-dim, chi = 0) each merge a
B5 MIRROR PAIR (e.g. SM21p = (2,1,16+) ⊕ (2,1,16-) = Lp ⊕ Lm), by the
ledger's own 10 (x) 16± = 144± + 16∓ identity. Consequences: the twelve
projectors are NOT the isotypic decomposition; the merge collapses the
provenance separation that is B5 hostile control #2 (b5-...:174); the
"small sectors follow the same law" measurement is structurally blind to a
mirror action there (the mirror is still excluded, but only by [J,omega]=0).
The MIRROR dict's SM entries are never tested (test ranges over X_SLOTS
only). One-line fix: refine by Q4/Q10 into the ledger's eight.

A4. The Pfaffian-scalar mechanism is verified AND provable:
(prod_{a in I} e_a)^2 = (-1)^{|I|(|I|-1)/2} (-1)^{q_I}; |I|=10 gives c_F = 1
iff q_F odd, i iff q_F even; |I|=4 gives c_B = 1 iff q_B even; J om J^{-1} =
(conj(c)/c) om. |c| = 3/4 from the three Pfaffian pairings. The two "flips"
trace to the single datum (c_B, c_F), which is why [J,omega] = 0 forces
co-occurrence (the note says this; wording nit only).

A5. THE LOAD-BEARING OVERCLAIM (panel's central finding): "the fork maps
exactly onto the signature dichotomy" is a HOMONYM. The repo defines
rank_H := rank_C/2 (oqrk1_indh_rank.py:37); OQ-RK1's 4-vs-8 is a rank_H.
Computing with the note's own numbers: EXCHANGE gives 2x96_H + 2x288_H =
768_H; WITHIN gives 4x48_H + 4x144_H = 768_H. IDENTICAL in every allocation:
the dichotomy moves the block PARTITION (a unit count), not any H-dimension.
The note's ":166-168 double-counts by a factor of 2" is dimensionally false
(48_H + 48_H = 96_H). This is verbatim the AGENTS.md:15 failure and the
shape of the 2026-07-29 retraction; the note has a Layer-0 FENCE but never
ran the Layer-0 CHECK (no SAME-OBJECT/HOMONYM/UNCERTAIN marking on the
load-bearing terms "4"/"8"). Salvageable restatement: "the number of
J-irreducible blocks in the branched X sector is 4 or 8 by q_B parity; this
is a unit count, HOMONYMOUS with OQ-RK1's rank_H in {4,8}, and constrains no
H-dimension."

A6. Smaller: (1,3) is not "the opposite convention" — inside a fixed (9,5)
it forces internal (8,2), a physically distinct allocation (only (3,1)+(6,4)
is the named split). "J commutes with Pi_RS" is asserted; only
T-equivariance/J-stability of ker T is checked (the stronger statement
follows from unitarity of the e_a but should be checked or derived).

## (B) Underclaim / over-fencing findings

B1. The charge "the physical split IS Lorentzian, so the conditional is
decided" is REFUTED by the READ-FIRST table itself:
GEOMETER-VS-PHYSICS-OBJECTS.md:24 types the 4+10 carrier split as an
UNSETTLED fork between Lorentzian (3,1)+(6,4) and the compact/complexified
(4,0)+(5,5) THAT THE FINITE CENSUS USES — the probe's branches are exactly
the fork's two rows. The fence is real work. B2: but the note itself tilts
("physically natural") without citing the fork row or noting the census sits
on the WITHIN side — required correction, cutting against reviewer 2. B3:
genuine under-labeling — claim 1 is allocation-INDEPENDENT and unconditional
(forecloses the ledger's open antilinear-mirror option, a real narrowing of
B5-NATIVE-REAL-KREIN-ADJOINT-FREEZE); it deserves its own unconditional
token, not the (allocation-conditional) label. B4: the H-structure
factorization fence is upheld (the probe factorizes over the kinematic
R^14 (x) S, not S_RS^+; Pi_RS^phys does not exist).

## Verdict block

1. J ≠ B5 mirror coflip: CONFIRMED, STRONGER than filed (unconditional,
structural; re-file as its own token). 2. Lorentzian => EXCHANGE:
CONFIRMED-WITH-CORRECTIONS (pairs are NOT mirror pairs; "4 H-units" is a
unit count; (1,3) wording). 3. Non-Lorentzian => WITHIN: CONFIRMED on X
(canonical); WITH-CORRECTIONS on the small sectors (mirror-pair merge).
4. Mechanism exact: CONFIRMED (re-derived analytically). 5. "Fork maps
exactly onto the dichotomy": REFUTED AS STATED (768_H invariant; homonym).

Spec-blocked boundary RESPECTED (fences verbatim in note+code+runtime; no
repo citation of the note anywhere; OQ-RK1 remains BLOCKED_NEEDS_SPEC).

LICENSED: (i) J-is-not-the-mirror-coflip citable into
B5-NATIVE-REAL-KREIN-ADJOINT-FREEZE as a closed option; (ii) the
within/exchange law on the eight X slots as a function of q_B parity with
the exact (c_B, c_F) mechanism; (iii) the identification of the two branches
with the two rows of the GEOMETER-VS-PHYSICS-OBJECTS:24 fork — the most
useful thing here, currently uncited by the note.

NOT LICENSED: any "4 H-units vs 8 H-units" statement adjacent to OQ-RK1's
rank_H in any surface until the Layer-0 homonym marking is executed; any
claim the allocation bears on rank_H(S_RS^+); any use of the small-sector
result as a statement about the ledger's E± irreducibles; treating (3,1) as
settled.

BLOCKING CORRECTIONS: (1) Layer-0 homonym block naming which "4"/"8" each
side means; (2) strike/restate :166-168 with the 768_H invariant; (3) cite
GEOMETER-VS-PHYSICS-OBJECTS:24 and state the census uses the WITHIN branch;
(4) flag the small-sector projectors as non-isotypic with the Q4/Q10
refinement; (5) fix the (1,3) wording.
