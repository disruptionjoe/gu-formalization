---
title: "OQ-RK1 J-restriction probe: the quaternionic structure never implements the B5 mirror coflip; within-vs-exchange on the D2 x D5 branched slots is decided by the (unfrozen) signature allocation of the observer 4-plane -- Lorentzian allocations EXCHANGE same-chirality slot pairs, non-Lorentzian allocations act WITHIN each slot"
status: exploration
doc_type: probe_result
created: 2026-08-03
work_item: "M-H1 (WP-A3)"
code: tests/oq_rk1_j_restriction_probe.py
grade: "EXACT FINITE COMPUTATION (explicit Cl(9,5)=M(64,H) rep on the 1792-dim RS fiber; canonical equivariant slot projectors from Casimir/chirality data only; 180/180 hard asserts, exit 0; matched distances 0.0 or <= 3.0e-15 against unmatched distances >= 11.31, separation ratio >= 3.8e15) / no rank, no count, no claim-status change"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
depends_on:
  - explorations/shiab-operator/b5-observer-symbol-multiplicity-matrix-2026-07-24.md
  - tests/oq_rk1_cl95_explicit_rep.py
  - tests/hardening-pass/oqrk1_indh_rank.py
  - tests/oq_rk1_e_rs_eff_assembly.py
  - papers/drafts/hardening-pass-2026-07-03/A2a-oqrk1-indh-rank-RESULTS-DRAFT.md
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
Clifford generator, hence with `omega`, the gamma-trace `T`, and `Pi_RS`; same
construction that certified the rank_C -> rank_H halving in
`tests/hardening-pass/oqrk1_indh_rank.py`) acts on the common RS fiber
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
slots plus four multiplicity-2 small sectors of dimension 64). Positive
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
the `10 (x) 16` branching identity). The permutation action is then measured
directly as `D[i,j] = ||P_i - J P_j J^{-1}||_F`.

One fact the complexified B5 ledger cannot see: realizing `Spin(4) x Spin(10)`
inside the FIXED real Cl(9,5) representation requires allocating the (9,5)
signature across the 4|10 split. That allocation is part of the unfrozen
native real/Krein data (`B5-NATIVE-REAL-KREIN-ADJOINT-FREEZE`). The probe
therefore sweeps all five allocations of the observer 4-plane: (4,0), (3,1),
(2,2), (1,3), (0,4).

## Result

`OQ-RK1-J-SLOT-ACTION-CLASSIFIED (allocation-conditional)`.

1. **In NO allocation is J the documented B5 mirror coflip.** Structural
   reason: J commutes with total chirality `omega` (exact, error 0.0), while
   the mirror coflip `X32p <-> X32m` etc. exchanges the two total-chirality
   blocks. Certified: `min ||P_mirror - J P J^{-1}||_F = 13.856 (~ sqrt(192))`
   across every X slot in every allocation, against matched distances
   <= 3.0e-15.

2. **The within-vs-exchange dichotomy is decided by the parity of timelike
   directions `q_B` in the observer 4-plane:**

   | base | internal | P4 left scalar c | om_F phase | classification |
   |---|---|---|---|---|
   | (3,1) | (6,4) | +0.75i | i | EXCHANGE (same-chirality pairs) |
   | (1,3) | (8,2) | +0.75i | i | EXCHANGE (same-chirality pairs) |
   | (4,0) | (5,5) | +0.75 | 1 | WITHIN |
   | (2,2) | (7,3) | +0.75 | 1 | WITHIN |
   | (0,4) | (9,1) | +0.75 | 1 | WITHIN |

   `q_B` odd (Lorentzian observer base, either convention) gives EXCHANGE;
   `q_B` even gives WITHIN. The mechanism is visible in two exact scalars:
   the L/R discriminator scalar `c` (the P4 eigenvalue scale) is purely
   imaginary exactly for Lorentzian bases, so the antilinear J conjugates it
   and swaps the two Spin(4) Weyl labels; and the internal chirality
   normalization phase is `i` exactly when the internal signature has an even
   number of timelike directions, so `J om_F J^{-1} = -om_F` and the internal
   `16+ <-> 16-` grading flips. The two flips co-occur in every allocation --
   forced, because `[J, omega] = 0` and `omega = +/- om_B om_F`.

3. **Lorentzian allocations (the physically natural observer split):
   EXCHANGE, but of the same-chirality partners, not the mirror partners.**
   Measured permutation (distances 0.0 to 3.0e-15):

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

The multiplicity-2 small sectors (four 64-dim joint eigenspaces, each mixing
the two total-chirality blocks 32+32) follow the same law: identity in the
WITHIN allocations, `SM21p <-> SM12m`, `SM12p <-> SM21m` in the EXCHANGE
allocations.

Slot names above use the probe's stated conventions (`left := om_B = +1`,
`16+ := om_F = +1`, `144+ :=` the 144 inside `10 (x) 16+`); the
classification statements are invariant under relabeling. The probe's fiber
is `V = R^14 (x) S` (1792 = 1536 X + 256), i.e. the `im Gamma` and
`ker Gamma` provenance material of the B5 ledger; the ledger's third
provenance copy (the 128-dim gamma-trace target `S`) lives in the target of
`T`, not in V, which is why 1792 + 128 = 1920 reconciles with the frozen
ledger total.

## What this means for the 4-vs-8 fork (conditional, spec-gated)

The literal OQ-RK1 question ("does rank_H(Pi_RS . E_+ . Pi_RS) return 4 or
8?") remains BLOCKED_NEEDS_SPEC: the physical projector `Pi_RS^phys` /
`E_RS^eff` does not exist in the repo, and this probe does not construct it.
What the probe adds is a bookkeeping constraint on ANY future H-rank
accounting over the branched slots, conditional on the summand-identification
spec (which slots the physical projector selects) and on the real-form
allocation:

- If the frozen spec allocates a Lorentzian observer 4-plane (the physically
  natural reading), then H-units are the same-chirality PAIRS
  `{(3,2,16+) + (2,3,16-)}`, `{(2,1,144+) + (1,2,144-)}`, and mirrors: the
  eight X slots form exactly FOUR quaternionic units, and any count that
  treats a `16+` slot and its partner as separate H-objects double-counts by
  a factor of 2.
- If the spec allocates a non-Lorentzian 4-plane, every slot is its own
  quaternionic unit and the eight X slots stay EIGHT H-objects.

So the 4-vs-8 ambiguity at the slot-census level maps exactly onto the
within-vs-exchange dichotomy, which in turn is decided by a datum
(signature allocation of the observer plane) that the B5 complexified ledger
deliberately left unfrozen. No generation count follows in either branch;
the missing object is still `RS_GU^phys` (gauge/BRST differential, K-theory
symbol class, `ch_2(F)[K3]`, H-trace, `Y14 <-> K3` bridge).

## Hostile controls

The certificate fails (exit nonzero) if: any Clifford or J property fails;
vector and spinor structure constants disagree; any Casimir calibration or
annihilating polynomial misses its exact spectrum; any slot projector fails
idempotence, orthogonality, completeness, its exact trace, or equivariance;
any X slot leaves `ker T`; a `(3,2) x 144`-type cell is nonempty; the J-image
of a slot projector fails to land exactly on a slot projector; the
permutation fails to be a chirality-preserving involution; the classification
deviates from the measured law; or J implements the mirror coflip anywhere.
No forbidden move (target division, `ind_H = 8` insertion, sub-projector
selection) is executed.

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
