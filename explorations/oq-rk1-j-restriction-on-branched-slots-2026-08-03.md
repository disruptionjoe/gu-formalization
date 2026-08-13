---
title: "OQ-RK1 J-restriction probe: the quaternionic structure never implements the B5 mirror coflip; within-vs-exchange on the D2 x D5 branched slots is decided by the (unfrozen) signature allocation of the observer 4-plane -- Lorentzian allocations EXCHANGE same-chirality slot pairs, non-Lorentzian allocations act WITHIN each slot"
status: exploration
doc_type: probe_result
created: 2026-08-03
work_item: "M-H1 (WP-A3)"
code: tests/oq_rk1_j_restriction_probe.py
grade: "EXACT FINITE COMPUTATION (explicit Cl(9,5)=M(64,H) rep on the 1792-dim RS fiber; equivariant slot projectors from Casimir/chirality data -- canonical/isotypic on the multiplicity-free X block, small sector refined by the Q4/Q10 provenance grading into the ledger's eight 32-dim slots; 232/232 hard asserts, exit 0; matched distances 0.0 or <= 3.0e-15 (coarse) and <= 1.4e-16 (refined) against unmatched distances >= 11.31 (coarse) / >= 8.0 (refined 32-dim), separation ratio >= 3.8e15 coarse) / no rank, no count, no claim-status change"
canon_verdict_change: none
depends_on:
  - explorations/shiab-operator/b5-observer-symbol-multiplicity-matrix-2026-07-24.md
  - tests/oq_rk1_cl95_explicit_rep.py
  - tests/hardening-pass/oqrk1_indh_rank.py
  - tests/oq_rk1_e_rs_eff_assembly.py
  - papers/drafts/hardening-pass-2026-07-03/A2a-oqrk1-indh-rank-RESULTS-DRAFT.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
hostile_review: lab/process/hostile-reviews/2026-08-03-j-restriction-review.md
scripts:
  - tests/oq_rk1_j_restriction_probe.py
---

# OQ-RK1 J-restriction probe: how J acts on the D2 x D5 branched slots

## Layer-0 fence (verbatim, read first)

this computation classifies the antiunitary's action on a decomposition; it
does NOT by itself compute rank_H(S_RS^+), does NOT close OQ-RK1 (which is
BLOCKED_NEEDS_SPEC on the physical projector Π_RS^phys per
tests/oq_rk1_e_rs_eff_assembly.py), and no count claim follows. How the
H-structure factorizes across the tensor splitting is a naming/spec question
this probe INFORMS, not answers.

## Layer-0 homonym block (hostile-review blocking correction 1)

Two different objects are named "4" and "8" in this neighborhood. Marking:
**HOMONYM**, per the AGENTS.md decomposition-to-count discipline:

- **This note's "4 vs 8"** is the number of **J-irreducible UNITS** in the
  block partition of the eight X slots: 4 pair-blocks under EXCHANGE, 8
  singleton blocks under WITHIN. A unit count.
- **OQ-RK1's "4 vs 8"** is `rank_H(Pi_RS . E_+ . Pi_RS) in {4, 8}`, an
  **H-DIMENSION** (`rank_H := rank_C/2`,
  `tests/hardening-pass/oqrk1_indh_rank.py`).

They are not the same object, and neither determines the other. The **768_H
invariant** (probe-asserted, every allocation): the X block carries
`rank_H = 768` in EVERY allocation — EXCHANGE gives `2x96_H + 2x288_H =
768_H`, WITHIN gives `4x48_H + 4x144_H = 768_H`. The within/exchange
dichotomy moves the block PARTITION, never any H-dimension, so the unit
count constrains no `rank_H`.

## Question

The frozen B5 ledger
(`explorations/shiab-operator/b5-observer-symbol-multiplicity-matrix-2026-07-24.md`)
branches the Rarita-Schwinger remainder under `H_C = Spin(4,C) x Spin(10,C)`
into the eight X slots

```text
(3,2,16+) 96   (2,3,16-) 96   (2,1,144+) 288   (1,2,144-) 288
(3,2,16-) 96   (2,3,16+) 96   (2,1,144-) 288   (1,2,144+) 288
```

via the exact D5 identities `10 (x) 16+/- = 144+/- + 16-/+`. The verified
antilinear quaternionic structure `J = M.conj` (`J^2 = -I`, commutes with every
Clifford generator, hence with `omega` and with the gamma-trace `T` in the
T-equivariance sense — `ker T` is J-stable, the certified statement;
commutation with `Pi_RS` follows from unitarity of the `e_a` but is not
separately certified; same construction that certified the rank_C -> rank_H
halving in `tests/hardening-pass/oqrk1_indh_rank.py`) acts on the common RS fiber
`V = R^14 (x) S`, `dim_C = 1792`. Does J act WITHIN each internal `16+`
multiplicity slot, or does it EXCHANGE `16+ <-> 16-` (equivalently, does it
exchange the B5 mirror slot pairs)?

## Method (target-free, canonical)

Slot projectors are built from subalgebra invariant data only -- no basis
choice, no target import: the so(4) Casimir `C4` (3/2 vs 11/2), the so(10)
Casimir `C10` (45/4 on 16-type vs 85/4 on 144-type), the internal chirality
`OmF = I (x) om_F` (grades `16+/144+` against `16-/144-` on the
multiplicity-one X slots), and the degree-2 so(4) Pfaffian Casimir `P4`
(proportional to `C_L - C_R`; separates `(3,2)` from `(2,3)` and `(2,1)` from
`(1,2)`). The four operators commute; Lagrange spectral interpolation of the
certified spectra yields the twelve equivariant slot projectors on V (eight X
slots plus four multiplicity-2 small sectors of dimension 64).

Scope of "canonical" (hostile-review corrections A1-A3): on the
multiplicity-free X block the twelve-projector construction IS the canonical
isotypic decomposition — no re-pairing freedom exists there
(review-confirmed). On the small sector it is NOT: `OmF = I (x) om_F` grades
by spinor-factor chirality, not by the so(10) type of the constituent, so
each 64-dim small-sector projector merges a B5 MIRROR PAIR (e.g.
`SM21p = (2,1,16+) ⊕ (2,1,16-)` by the ledger's own
`10 (x) 16+/- = 144+/- + 16-/+` identity) and the twelve projectors are not
the isotypic decomposition. The probe therefore refines the small sector by
the equivariant J-stable provenance grading `Q4 = P_{R^4} (x) I`,
`Q10 = P_{R^10} (x) I` (splitting `R^4 (x) S = 4x96 + 4x32` and
`R^10 (x) S = 4x288 + 4x32`) into the ledger's eight 32-dim slots, with hard
asserts that both 32-dim pieces of every small sector carry IDENTICAL
`(C4, C10, OmF, P4)` labels — the merge is invisible to the four invariants,
which is exactly why the refinement is needed. Positive
controls, all hard asserts, all passing at machine precision or exactly:
Clifford relations, `omega^2 = +I`, `J^2 = -I`, antilinearity, J-commutation
with all 91 so(9,5) generators and with `omega`, vector/spinor structure
constants agree, Casimir calibrations (`C4 = 3/2`, `C10 = 45/4` on S; 3 and 9
on the vector blocks), annihilating polynomials for all four spectra,
projector idempotence (max err 1.1e-16), completeness (`sum P = I`, 2.2e-16),
all 66 pairwise orthogonality products (8.0e-17), exact traces
(4x96 + 4x288 + 4x64 = 1792), equivariance under sampled generators including
mixed-signature ones (5.6e-17), all eight X slots inside `ker T` (8.3e-17),
and the empty `(3,2) x 144` coarse cells (exactly 0 -- the numerical shadow of
the `10 (x) 16` branching identity). Added with the hostile-review
corrections: Q4/Q10 idempotence, J-stability, and commutation with all twelve
projectors; containment (16-type X slots inside `R^4 (x) S`, 144-type inside
`R^10 (x) S`); the eight refined 32-dim slots idempotent, trace-32, complete
with the X slots, and label-identical in pairs; the refined J-permutation and
refined mirror-exclusion measurements; and the 768_H invariant per allocation
and across allocations. The permutation action is then measured
directly as `D[i,j] = ||P_i - J P_j J^{-1}||_F`, on the twelve coarse slots
and again on the eight refined small slots.

One fact the complexified B5 ledger cannot see: realizing `Spin(4) x Spin(10)`
inside the FIXED real Cl(9,5) representation requires allocating the (9,5)
signature across the 4|10 split. That allocation is part of the unfrozen
native real/Krein data (`B5-NATIVE-REAL-KREIN-ADJOINT-FREEZE`). The probe
therefore sweeps all five allocations of the observer 4-plane: (4,0), (3,1),
(2,2), (1,3), (0,4).

## Result

Two tokens (the split is a hostile-review re-filing: claim 1 is
allocation-INDEPENDENT and must not sit under the conditional label):

- `OQ-RK1-J-IS-NOT-THE-B5-MIRROR-COFLIP` — **unconditional**.
- `OQ-RK1-J-SLOT-ACTION-CLASSIFIED (allocation-conditional)` — the
  within/exchange law, items 2-4 below.

1. **In NO allocation is J the documented B5 mirror coflip — unconditional,
   structural, allocation-independent (its own token above).** Structural
   reason: J commutes with total chirality `omega` (exact, error 0.0), while
   the mirror coflip `X32p <-> X32m` etc. exchanges the two total-chirality
   blocks. Certified: `min ||P_mirror - J P J^{-1}||_F = 13.856 (~ sqrt(192))`
   across every X slot in every allocation, against matched distances
   <= 3.0e-15; after the Q4/Q10 refinement the exclusion is also MEASURED on
   every refined 32-dim small slot in every allocation (min distance
   `8.0 = sqrt(64)`), where the unrefined 64-dim measurement was structurally
   blind to a mirror action inside a merged pair. The review's independent
   re-run further certifies the statement is invariant under
   `J -> lambda J` (`|lambda| = 1`), `-J`, and unitary conjugation (the
   commutant of the Clifford generators is scalars), so it does not depend on
   the particular `M` chosen. Per the review this is LICENSED citable into
   `B5-NATIVE-REAL-KREIN-ADJOINT-FREEZE` as a closed option: the ledger's
   open antilinear-mirror option is foreclosed.

2. **The within-vs-exchange dichotomy is decided by the parity of timelike
   directions `q_B` in the observer 4-plane:**

   | base | internal | P4 left scalar c | om_F phase | classification |
   |---|---|---|---|---|
   | (3,1) | (6,4) | +0.75i | i | EXCHANGE (same-chirality pairs) |
   | (1,3) | (8,2) | +0.75i | i | EXCHANGE (same-chirality pairs) |
   | (4,0) | (5,5) | +0.75 | 1 | WITHIN |
   | (2,2) | (7,3) | +0.75 | 1 | WITHIN |
   | (0,4) | (9,1) | +0.75 | 1 | WITHIN |

   `q_B` odd gives EXCHANGE; `q_B` even gives WITHIN. (Corrected wording: the
   two `q_B`-odd rows are physically DISTINCT allocations, not two
   conventions for one split — inside the fixed (9,5) a (1,3) observer base
   forces internal (8,2), and only `(3,1)+(6,4)` is the named physical
   split.) The mechanism is visible in two exact scalars:
   the L/R discriminator scalar `c` (the P4 eigenvalue scale) is purely
   imaginary exactly for Lorentzian bases, so the antilinear J conjugates it
   and swaps the two Spin(4) Weyl labels; and the internal chirality
   normalization phase is `i` exactly when the internal signature has an even
   number of timelike directions, so `J om_F J^{-1} = -om_F` and the internal
   `16+ <-> 16-` grading flips. The two flips co-occur in every allocation --
   forced, because `[J, omega] = 0` and `omega = +/- om_B om_F`.

3. **Lorentzian allocations — the `(3,1)+(6,4)` row of the standing carrier-
   split fork (`GEOMETER-VS-PHYSICS-OBJECTS.md:24`): EXCHANGE, but of the
   same-chirality partners, not the mirror partners.** (Corrected: the
   original filing called this "the physically natural observer split"
   without citing the fork row; that tilt is retracted — see the fork
   paragraph after item 4.) Measured permutation (distances 0.0 to 3.0e-15):

   ```text
   J : (3,2,16+) <-> (2,3,16-)     J : (2,1,144+) <-> (1,2,144-)
   J : (3,2,16-) <-> (2,3,16+)     J : (2,1,144-) <-> (1,2,144+)
   ```

   J flips BOTH Spin(4) Weyl labels AND the internal D5 chirality while
   preserving total chirality: each pair lies inside one B5 table row-block.
   So J does NOT act within any internal `16+` multiplicity slot here, and
   the quaternionic structure lives only on the pair sums
   (96 + 96 = 192_C = 96_H, 288 + 288 = 576_C = 288_H).

4. **Non-Lorentzian allocations: WITHIN.** J maps every slot projector to
   itself (distance exactly 0.0). Each slot is J-stable with `J^2 = -I` on
   it, so each slot separately carries a quaternionic structure:
   96_C = 48_H per 16-type X slot, 288_C = 144_H per 144-type X slot. This is
   an algebra-level halving statement about the raw kinematic decomposition,
   not a rank of any physical operator.

**The two branches ARE the two rows of the standing carrier-split fork**
(`GEOMETER-VS-PHYSICS-OBJECTS.md:24`, "Physical 4+10 carrier split"; this
identification is LICENSED by the hostile review, item iii): the Lorentzian
`(3,1)+(6,4)` row of the fork lands in EXCHANGE, and the compact/complexified
`(4,0)+(5,5)` row lands in WITHIN. That fork is explicitly UNSETTLED ("do not
transfer the packet silently"), so neither branch is "the physical one"
today — and the repo's own finite census sits on the compact/WITHIN side of
it. Any argument that the conditional is already decided Lorentzian-side is
refuted by the fork row itself.

The multiplicity-2 small sectors (four 64-dim joint eigenspaces, each mixing
the two total-chirality blocks 32+32) are NOT isotypic slots: each merges a
B5 mirror pair (`SM21p = (2,1,16+) ⊕ (2,1,16-)`, etc.), so on its own the
64-dim measurement is structurally blind to a mirror action inside a merged
pair and collapses the ledger's provenance separation (B5 hostile control
#2). Refined by the equivariant J-stable provenance grading `Q4/Q10` into
the ledger's eight 32-dim slots (both pieces of each sector carrying
IDENTICAL `(C4, C10, OmF, P4)` labels), the measured law extends: identity
on all eight refined slots in the WITHIN allocations, and
`SM21p.Q* <-> SM12m.Q*`, `SM12p.Q* <-> SM21m.Q*` — preserving the
provenance block — in the EXCHANGE allocations. J is NOT the mirror coflip
on any refined small slot in any allocation (min distance `8.0 = sqrt(64)`
against matched distances at machine precision): measured, no longer merely
implied by `[J, omega] = 0`.

Slot names above use the probe's stated conventions (`left := om_B = +1`,
`16+ := om_F = +1`, `144+ :=` the 144 inside `10 (x) 16+`); the
classification statements are invariant under relabeling. The probe's fiber
is `V = R^14 (x) S` (1792 = 1536 X + 256), i.e. the `im Gamma` and
`ker Gamma` provenance material of the B5 ledger; the ledger's third
provenance copy (the 128-dim gamma-trace target `S`) lives in the target of
`T`, not in V, which is why 1792 + 128 = 1920 reconciles with the frozen
ledger total.

## What this means for OQ-RK1's 4-vs-8 (CORRECTED: a unit count under the 768_H invariant, not a rank statement)

The literal OQ-RK1 question ("does rank_H(Pi_RS . E_+ . Pi_RS) return 4 or
8?") remains BLOCKED_NEEDS_SPEC: the physical projector `Pi_RS^phys` /
`E_RS^eff` does not exist in the repo, and this probe does not construct it.

STRUCK AND RESTATED (hostile-review blocking corrections 1-2; the original
filing's claim that "the 4-vs-8 ambiguity at the slot-census level maps
exactly onto the within-vs-exchange dichotomy" was REFUTED AS STATED, and
its "any count that treats a `16+` slot and its partner as separate
H-objects double-counts by a factor of 2" was dimensionally false —
`48_H + 48_H = 96_H`, no H-dimension doubles). The corrected statement:

- **768_H invariant (probe-asserted).** The X block carries `rank_H = 768`
  in EVERY allocation: EXCHANGE partitions it into the four pair-units
  `{(3,2,16+) + (2,3,16-)}`, `{(3,2,16-) + (2,3,16+)}`,
  `{(2,1,144+) + (1,2,144-)}`, `{(2,1,144-) + (1,2,144+)}` of H-dimensions
  `96_H, 96_H, 288_H, 288_H` (`2x96_H + 2x288_H = 768_H`); WITHIN partitions
  it into eight singleton units of `48_H, 48_H, 48_H, 48_H, 144_H, 144_H,
  144_H, 144_H` (`4x48_H + 4x144_H = 768_H`). Identical total in every
  allocation: the dichotomy moves the block PARTITION, never any
  H-dimension.
- **The salvageable statement (review wording):** the number of
  J-irreducible blocks in the branched X sector is 4 or 8 by `q_B` parity;
  this is a UNIT COUNT, HOMONYMOUS with OQ-RK1's `rank_H in {4,8}` (see the
  Layer-0 homonym block above), and constrains no H-dimension.

The within-vs-exchange dichotomy itself is decided by a datum (signature
allocation of the observer plane — the `GEOMETER-VS-PHYSICS-OBJECTS.md:24`
fork) that the B5 complexified ledger deliberately left unfrozen. Under the
768_H invariant, no `rank_H` statement, no generation count, and no
"4 H-units vs 8 H-units" statement adjacent to OQ-RK1's `rank_H` follows in
either branch; the missing object is still `RS_GU^phys` (gauge/BRST
differential, K-theory symbol class, `ch_2(F)[K3]`, H-trace,
`Y14 <-> K3` bridge).

## Hostile controls

The certificate fails (exit nonzero) if: any Clifford or J property fails;
vector and spinor structure constants disagree; any Casimir calibration or
annihilating polynomial misses its exact spectrum; any slot projector fails
idempotence, orthogonality, completeness, its exact trace, or equivariance;
any X slot leaves `ker T`; a `(3,2) x 144`-type cell is nonempty; the J-image
of a slot projector fails to land exactly on a slot projector; the
permutation fails to be a chirality-preserving involution; the classification
deviates from the measured law; or J implements the mirror coflip anywhere.
Added with the hostile-review corrections, it also fails if: `Q4`/`Q10` fail
idempotence, complementarity, J-stability, or commutation with any slot
projector; any 16-type X slot leaves `R^4 (x) S` or 144-type slot leaves
`R^10 (x) S`; any refined 32-dim slot fails idempotence, its exact trace-32,
completeness with the X slots, or the identical-label condition; the refined
J-permutation fails to land exactly on refined slots, fails decisive
separation, deviates from the parent law, or breaks the provenance block; J
implements the mirror coflip on any refined small slot; or the 768_H
invariant fails in any allocation or across allocations (unit count not in
{4, 8}, H-total not 768, or unit count inconsistent with the
classification). No forbidden move (target division, `ind_H = 8` insertion,
sub-projector selection) is executed.

## Named next step

`OQ-RK1-J-SLOT-FACTORIZATION-SPEC`: freeze, from source data and not from
convenience, (i) the signature allocation of the observer 4-plane inside
(9,5) -- equivalently the real form pair `so(q_B') x so(p_F, q_F)` that the
native Krein structure selects -- and (ii) the summand identification of
`Pi_RS^phys` against the B5 slot ledger. This is a within-item feeder to the
standing `B5-NATIVE-REAL-KREIN-ADJOINT-FREEZE` residual. Only after that
freeze does "within vs exchange" become a fact about `S_RS^+` rather than a
fact about allocations, and only then can any H-unit census of the branched
slots enter a rank argument.

## Hostile review (2026-08-03): verdicts and corrections applied

Reviewed per the verdict-flip governance rule by
`lab/process/hostile-reviews/2026-08-03-j-restriction-review.md` (two-sided
charge, independent re-runs). Verdicts: claims 1-4 CONFIRMED — claim 1
STRONGER than filed (unconditional, allocation-independent; re-filed above
as its own token `OQ-RK1-J-IS-NOT-THE-B5-MIRROR-COFLIP`), claims 2-3 with
corrections, claim 4 exact and re-derived analytically. Claim 5 ("the
4-vs-8 census fork maps exactly onto the signature dichotomy") REFUTED AS
STATED: the X block carries 768_H in every allocation; only the J-unit
partition moves — struck and restated above.

Blocking corrections applied in this revision (and mirrored in
`tests/oq_rk1_j_restriction_probe.py`): (1) Layer-0 homonym block naming
which "4"/"8" each side means; (2) the former :166-168 double-count passage
struck and restated with the 768_H invariant; (3)
`GEOMETER-VS-PHYSICS-OBJECTS.md:24` cited, with the statement that the
finite census uses the WITHIN branch of that unsettled fork; (4) the
small-sector projectors flagged as non-isotypic and refined by Q4/Q10 into
the ledger's eight 32-dim slots, with the J-permutation and mirror tests
extended to them; (5) the (1,3) "opposite convention" wording fixed to a
physically distinct allocation.

Licensed by the review: (i) J-is-not-the-mirror-coflip citable into
`B5-NATIVE-REAL-KREIN-ADJOINT-FREEZE` as a closed option; (ii) the
within/exchange law on the eight X slots as a function of `q_B` parity with
the exact `(c_B, c_F)` mechanism; (iii) the identification of the two
branches with the two rows of the `GEOMETER-VS-PHYSICS-OBJECTS.md:24` fork.
NOT licensed (respected here): any "4 H-units vs 8 H-units" statement
adjacent to OQ-RK1's `rank_H`; any claim the allocation bears on
`rank_H(S_RS^+)`; any use of the small-sector result as a statement about
the ledger's E± irreducibles; treating (3,1) as settled. This note keeps
exploration tier and `claim_status_change: none`; OQ-RK1 remains
BLOCKED_NEEDS_SPEC.
